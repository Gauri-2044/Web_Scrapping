import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://zenithhospital.org.in/"

# Get the HTML content of the page
data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")

# Lists to store the extracted data
name_list = []
designation_list = []
opinion_list = []

def extract_testimonials(soup):
    # Find all testimonial items directly, no need for recursive search
    testimonial_items = soup.find_all("div", class_="testimonial-item")
    
    for item in testimonial_items:
        # Extract name, designation, and opinion
        name = item.find("h3")
        designation = item.find("h4")
        opinion = item.find("p")
        
        # Safely append the text content to the lists if they exist
        if name and name.text.strip():
            name_list.append(name.text.strip())
        if designation and designation.text.strip():
            designation_list.append(designation.text.strip())
        if opinion and opinion.text.strip():
            opinion_list.append(opinion.text.strip())

# Call the function to extract testimonials
extract_testimonials(soup)

# Print the extracted data
print("Names:")
for name in name_list:
    print(name)

print("\nDesignations:")
for designation in designation_list:
    print(designation)

print("\nOpinions:")
for opinion in opinion_list:
    print(opinion)

# Create DataFrame
df = pd.DataFrame({
    "Name": name_list,
    "Designation": designation_list,
    "Opinion": opinion_list
})

print("\nDataFrame:")
print(df)

# Save to CSV if needed
df.to_csv("data.csv", index=False)

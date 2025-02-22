#!/bin/bash

# Make the file executable
chmod +x git.sh

echo "What is user name? "
read USERNAME
echo "What is repository name? "
read REPO_NAME

export ORIGIN_URL="https://github.com/${USERNAME}/${REPO_NAME}.git"

# Defining a function to push the project to the repository
push_project() {
    echo "Starting to push the project to origin..."

    git init
    git remote add origin ${ORIGIN_URL}
    if [ "$(git branch --show-current)" != "main" ]; then
        echo "Moving to main..."
        git branch -m master main
    fi

    git add .

    echo "Enter commit message: "
    read COMMIT_MSG

    git commit -m "${COMMIT_MSG}"
    git push -u origin main

    echo "Here is the final result:"
    git status
}

# Call the function
push_project

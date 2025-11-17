#!/bin/bash
# Helper script to upload project to GitHub

set -e

echo "📤 GitHub Upload Helper"
echo "========================"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📦 Initializing git repository..."
    git init
else
    echo "✅ Git repository already initialized"
fi

# Check if .gitignore exists
if [ ! -f .gitignore ]; then
    echo "⚠️  Warning: .gitignore not found"
fi

# Add all files
echo "📝 Adding files to git..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "ℹ️  No changes to commit"
else
    # Get commit message
    if [ -z "$1" ]; then
        COMMIT_MSG="Initial commit: AI Showcase"
    else
        COMMIT_MSG="$1"
    fi
    
    echo "💾 Creating commit..."
    git commit -m "$COMMIT_MSG"
fi

# Check if remote exists
if git remote | grep -q "^origin$"; then
    echo "✅ Remote 'origin' already exists"
    REMOTE_URL=$(git remote get-url origin)
    echo "   Current remote: $REMOTE_URL"
    read -p "Do you want to use this remote? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter new remote URL: " NEW_REMOTE
        git remote set-url origin "$NEW_REMOTE"
    fi
else
    echo ""
    echo "🔗 Please provide your GitHub repository URL:"
    echo "   Example: https://github.com/username/repo-name.git"
    read -p "Repository URL: " https://github.com/hinamahmood/ai-showcase
    
    if [ -n "$REPO_URL" ]; then
        git remote add origin "$REPO_URL"
        echo "✅ Remote added: $REPO_URL"
    else
        echo "⚠️  No remote URL provided. Skipping remote setup."
        echo "   You can add it later with: git remote add origin <URL>"
        exit 0
    fi
fi

# Set branch to main
git branch -M main

# Push to GitHub
echo ""
echo "🚀 Pushing to GitHub..."
read -p "Ready to push? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git push -u origin main
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    # Extract repo name from URL
    REPO_NAME=$(basename -s .git "$(git remote get-url origin)")
    USER_NAME=$(basename $(dirname "$(git remote get-url origin)"))
    echo "🌐 View your repository at:"
    echo "   https://github.com/$USER_NAME/$REPO_NAME"
else
    echo "⏸️  Push cancelled. You can push later with:"
    echo "   git push -u origin main"
fi


#!/bin/bash
# rebuild_project.sh - Clean project folder and set up fresh environment

echo "🛠 Rebuilding project in $(pwd)"

# Fail on error
set -e

# Save rebuild script filename
SCRIPT_NAME=$(basename "$0")

# Back up .git directory
echo "📦 Backing up existing .git directory..."
mv .git /tmp/git-backup

# Back up this script (so it survives cleanup)
cp "$SCRIPT_NAME" /tmp/"$SCRIPT_NAME".backup

# Clean project folder but preserve this script and .git
echo "🧹 Cleaning project folder..."
find . -mindepth 1 -not -path "./.git*" -not -name "$SCRIPT_NAME" -exec rm -rf {} +

# Restore .git directory
echo "🔁 Restoring .git directory..."
mv /tmp/git-backup .git

# Restore rebuild script from Git (discard local edits)
echo "📄 Restoring $SCRIPT_NAME from Git..."
git restore "$SCRIPT_NAME"

# Remove temp backup copy
rm /tmp/"$SCRIPT_NAME".backup

# Create virtual environment
echo "🐍 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install project in editable mode
pip install -e .

echo "✅ Rebuild complete. Project is ready and venv is active."
echo "👉 To activate the virtual environment later: source venv/bin/activate"


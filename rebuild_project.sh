#!/bin/bash
# rebuild_project.sh - Clean and rebuild the project environment

echo "🛠 Rebuilding project in $(pwd)"

# Fail on any error
set -e

# Move to the script's directory
cd "$(dirname "$0")"

# Preserve .git directory if it exists
if [ -d ".git" ]; then
    echo "📦 Backing up existing .git directory..."
    mv .git /tmp/git_backup
fi

# Clean project folder while preserving essential files
echo "🧹 Cleaning project folder..."
find . -mindepth 1 -maxdepth 1 \
  ! -name '.gitignore' \
  ! -name 'README.md' \
  ! -name 'pyproject.toml' \
  ! -name 'setup.py' \
  ! -name 'rebuild_project.sh' \
  ! -name 'startup.sh' \
  ! -name 'src' \
  -exec rm -rf {} +

# Restore .git directory
if [ -d "/tmp/git_backup" ]; then
    echo "🔁 Restoring .git directory..."
    mv /tmp/git_backup .git
fi

# Restore this script from Git if needed (shouldn't be needed now)
echo "📄 Ensuring rebuild_project.sh is present..."
git restore rebuild_project.sh || true

# Create virtual environment
echo "🐍 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install your package in editable mode
if [ -f "pyproject.toml" ]; then
    pip install -e .
else
    echo "⚠️  pyproject.toml not found. Skipping install."
fi

echo "✅ Rebuild complete. Project is ready and venv is active."
echo "👉 To activate the virtual environment later: source venv/bin/activate"


#!/bin/bash
# rebuild_project.sh - Safe rebuild script

echo "🛠 Rebuilding project in $(pwd)"

# Fail on any error
set -e

# Move to project root
cd "$(dirname "$0")"

# Preserve .git directory if it exists
if [ -d ".git" ]; then
    echo "📦 Preserving .git directory (already in place)"
fi

# Clean only untracked/ignored files
echo "🧹 Cleaning untracked and ignored files..."
git clean -xfd -e rebuild_project.sh -e startup.sh

# Create virtual environment
echo "🐍 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install project (if pyproject.toml exists)
if [ -f "pyproject.toml" ]; then
    pip install -e .
else
    echo "⚠️  pyproject.toml not found. Skipping install."
fi

echo "✅ Rebuild complete. Project is ready and venv is active."
echo "👉 To activate later: source venv/bin/activate"


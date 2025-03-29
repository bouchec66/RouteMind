#!/bin/bash

# Get the current directory as project root
PROJECT_ROOT=$(pwd)

# Check we're in the right folder
if [ ! -f "$PROJECT_ROOT/pyproject.toml" ] && [ ! -d "$PROJECT_ROOT/.git" ]; then
    echo "❌ Error: Run this script from the root of your Git project (where .git or pyproject.toml lives)."
    exit 1
fi

echo "🛠 Rebuilding project in $PROJECT_ROOT"

# Preserve .git if it exists
if [ -d "$PROJECT_ROOT/.git" ]; then
    echo "📦 Backing up existing .git directory..."
    mv "$PROJECT_ROOT/.git" /tmp/git_backup
fi

# Clean everything except .git and venv
echo "🧹 Cleaning project folder..."
find "$PROJECT_ROOT" -mindepth 1 \( -name '.git' -o -name 'venv' \) -prune -o -exec rm -rf {} +

# Restore .git
if [ -d "/tmp/git_backup" ]; then
    echo "🔁 Restoring .git directory..."
    mv /tmp/git_backup "$PROJECT_ROOT/.git"
fi

# Create directory structure
mkdir -p $PROJECT_ROOT/src/energy_aware_models/{chains,utils}
mkdir -p $PROJECT_ROOT/logs
mkdir -p $PROJECT_ROOT/tests
touch $PROJECT_ROOT/src/energy_aware_models/__init__.py

# README.md
cat <<EOF > $PROJECT_ROOT/README.md
# Energy Aware Models

A Python project for chaining large language models with energy efficiency in mind.
EOF

# .gitignore
cat <<EOF > $PROJECT_ROOT/.gitignore
__pycache__/
*.py[cod]
*.log
*.env
.env
venv/
dist/
build/
.eggs/
*.egg-info/
.DS_Store
.ipynb_checkpoints/
EOF

# pyproject.toml
cat <<EOF > $PROJECT_ROOT/pyproject.toml
[project]
name = "energy_aware_models"
version = "0.1.0"
description = "Energy-aware model chaining project"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    { name="Your Name", email="you@example.com" }
]
dependencies = []

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
EOF

# Placeholder code
touch $PROJECT_ROOT/src/energy_aware_models/main.py
touch $PROJECT_ROOT/src/energy_aware_models/config.py

# Create and activate virtual environment
cd $PROJECT_ROOT
echo "🐍 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install package in editable mode
pip install --upgrade pip
pip install -e .

# Install from requirements.txt if it exists
if [ -f "requirements.txt" ]; then
    echo "📦 Installing from requirements.txt..."
    pip install -r requirements.txt
fi

echo "✅ Rebuild complete. Project is ready and venv is active."
echo "👉 To activate the virtual environment later: source venv/bin/activate"


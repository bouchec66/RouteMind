#!/bin/bash
# startup.sh - Activate virtualenv and prep for development

echo "🚀 Starting development environment..."

# Fail on error
set -e

# Move to project root (if not already there)
cd "$(dirname "${BASH_SOURCE[0]}")"

# Activate virtual environment
if [ -d "venv" ]; then
    echo "🧪 Activating virtual environment..."
    source venv/bin/activate
else
    echo "❌ No virtual environment found in ./venv"
    echo "👉 Run ./rebuild_project.sh first to set up the environment."
    return 1 2>/dev/null || exit 1
fi

# Show status
echo "📁 Current directory: $(pwd)"
echo "🐍 Python: $(which python)"
echo "📦 Installed packages:"
pip list

# Optional: Launch an interactive shell
echo "💡 Ready to go! Type 'python' or run your scripts from here."


#!/bin/bash
# install.sh — Build and install bb-quiz system-wide
# Usage: bash install.sh

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
APP_DATA="$HOME/.local/share/bb-quiz"

echo "=== bb-quiz installer ==="

# Step 1: Create venv if needed
if [ ! -f "$VENV_DIR/bin/python3" ]; then
    echo "Setting up Python environment..."
    python3 -m venv "$VENV_DIR"
fi

# Step 2: Install dependencies
echo "Installing dependencies..."
"$VENV_DIR/bin/pip" install rich pyinstaller --quiet

# Step 3: Build standalone binary with PyInstaller
echo "Building standalone binary..."
"$VENV_DIR/bin/pyinstaller" \
    --onefile \
    --name bb-quiz \
    --clean \
    --distpath "$SCRIPT_DIR/dist" \
    --workpath "$SCRIPT_DIR/build" \
    --specpath "$SCRIPT_DIR" \
    "$SCRIPT_DIR/main.py" \
    --log-level WARN

# Step 4: Copy banks to ~/.local/share/bb-quiz/banks/
echo "Installing question banks to $APP_DATA/banks/ ..."
mkdir -p "$APP_DATA/banks"
cp -r "$SCRIPT_DIR/banks/"* "$APP_DATA/banks/"
echo "  Copied $(ls "$APP_DATA/banks/" | wc -l) bank files"

# Step 5: Install the binary to /usr/local/bin
echo "Installing binary to /usr/local/bin/ ..."
sudo cp "$SCRIPT_DIR/dist/bb-quiz" /usr/local/bin/bb-quiz
sudo chmod +x /usr/local/bin/bb-quiz

echo ""
echo "✅ Done!"
echo ""
echo "   Run from anywhere:  bb-quiz"
echo "   Banks location:     $APP_DATA/banks/"
echo "   History location:   $APP_DATA/data/"
echo ""
echo "   To add more banks, copy .md files to:"
echo "   $APP_DATA/banks/"

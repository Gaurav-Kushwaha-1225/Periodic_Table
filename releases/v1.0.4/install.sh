#!/bin/bash

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║         Periodic Table v1.0.4 - Automated Installer          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check if running as sudo (for dpkg)
if [[ $EUID -ne 0 ]]; then
   echo "❌ This script must be run with sudo"
   echo "Usage: sudo bash install.sh"
   exit 1
fi

# Check Ubuntu/Debian
if ! command -v dpkg &> /dev/null; then
    echo "❌ This script only works on Debian/Ubuntu systems"
    exit 1
fi

echo "📦 Installing Periodic Table v1.0.4..."
echo ""

# Install DEB
dpkg -i periodic-table_1.0.4_all.deb

# Fix dependencies
echo ""
echo "📚 Installing dependencies..."
apt-get install -f -y

# Install Python packages
echo ""
echo "🐍 Installing Python packages..."
pip3 install kivy kivymd --break-system-packages

# Update desktop database
echo ""
echo "🎨 Updating desktop environment..."
update-desktop-database /usr/share/applications
gtk-update-icon-cache -f -t /usr/share/icons/hicolor

echo ""
echo "✅ Installation complete!"
echo ""
echo "🚀 To launch the application:"
echo "   - Search 'Periodic Table' in Applications menu"
echo "   - Or run: periodic-table"
echo ""
echo "📖 For help, visit: https://github.com/Gaurav-Kushwaha-1225/Periodic_Table"
echo ""

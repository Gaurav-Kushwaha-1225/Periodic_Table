# Periodic Table v1.0.4 - Installation Guide

## Installation Methods

## Method 1: Direct DEB Installation (Recommended)

#### Step 1. Download periodic-table_1.0.4_all.deb

#### Step 2. Install

`sudo dpkg -i periodic-table_1.0.4_all.deb`

#### Step 3. Install dependencies if needed
`sudo apt-get install -f`

#### Step 4. Install Python Kivy packages
`sudo pip3 install kivy kivymd --break-system-packages`

## Method 2: Verify Package Integrity (Optional)

#### Before installing, verify the package hasn't been tampered with:

`sha256sum -c SHA256SUMS`

#### Expected output:

`periodic-table_1.0.4_all.deb: OK`

## Method 3: From Source

```bash
git clone https://github.com/Gaurav-Kushwaha-1225/Periodic_Table.git
cd Periodic_Table
pip3 install kivy kivymd
python3 main.py
```

## System Requirements

- **OS**: Ubuntu 20.04 LTS or newer
- **Python**: 3.8 or newer
- **RAM**: 512MB minimum
- **Disk Space**: 100MB

## Launch Application

After installation, find the app in:
- Applications menu → Search "Periodic Table"
- Terminal: `periodic-table`
- Ubuntu Software (search and click Open)

## Features

✨ **118 Chemical Elements** - All IUPAC-approved elements
🔍 **Smart Search** - Find by name, atomic number, properties
📊 **Detailed Properties** - Electron config, atomic weight, melting/boiling points
📸 **Element Images** - High-resolution images (requires internet)
📚 **Chemistry Dictionary** - Built-in reference
🎨 **Modern UI** - Beautiful interface with KivyMD

## Troubleshooting

### App won't launch

#### Test directly from terminal with diagnostics
`/usr/bin/python3 /usr/local/lib/periodic-table/main.py`

### Kivy/KivyMD not found
`sudo pip3 install kivy kivymd --break-system-packages`

#### Desktop entry not showing
```
sudo update-desktop-database /usr/share/applications
sudo gtk-update-icon-cache -f -t /usr/share/icons/hicolor
```

## Support

- **Issues**: https://github.com/Gaurav-Kushwaha-1225/Periodic_Table/issues
- **Source Code**: https://github.com/Gaurav-Kushwaha-1225/Periodic_Table
- **License**: MIT

## About

Created by Gaurav Kushwaha from IIT Mandi as part of open-source software development initiative.

Data source: [Bowserinator/Periodic-Table-JSON](https://github.com/Bowserinator/Periodic-Table-JSON)
Built with: [Kivy](https://kivy.org) and [KivyMD](https://kivymd.readthedocs.io/)
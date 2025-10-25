# Periodic Table v1.0.4 - Production Release

## 🎉 Now Available for Ubuntu Users!

This Periodic Table was just a random project during my high school days, and since i never deployed it, I just did a deployment on the diwali break, in my college sitting along in the college and my room.
This is the official production release of Periodic Table, packaged for easy installation on Ubuntu.

## 📦 What's Included

- **periodic-table_1.0.4_all.deb** - Ready-to-install Ubuntu package
- **install.sh** - Automated installer script
- **SHA256SUMS** - Package integrity verification
- **README.md** - Complete installation guide

## ✨ Features

- ✅ All 118 IUPAC-approved chemical elements
- ✅ Detailed properties and information
- ✅ Smart search functionality
- ✅ Chemistry dictionary
- ✅ High-resolution element images
- ✅ Beautiful modern UI with KivyMD
- ✅ Works offline except for element images

## 🚀 Quick Installation

### Option 1: Automated (Easiest)
`sudo bash install.sh`

### Option 2: Manual
```
sudo dpkg -i periodic-table_1.0.4_all.deb
sudo apt-get install -f
sudo pip3 install kivy kivymd --break-system-packages
```

### Option 3: From Source
```
git clone https://github.com/Gaurav-Kushwaha-1225/Periodic_Table.git
cd Periodic_Table
pip3 install kivy kivymd
python3 main.py
```

## 📋 System Requirements

- Ubuntu 20.04 LTS or newer
- Python 3.8+
- 512MB RAM minimum
- 100MB disk space

## 🔧 Verification

Verify package integrity before installation:
```
sha256sum -c SHA256SUMS
```

## 📚 Documentation

- [Source Code](https://github.com/Gaurav-Kushwaha-1225/Periodic_Table)
- [Issue Tracker](https://github.com/Gaurav-Kushwaha-1225/Periodic_Table/issues)
- [License](https://github.com/Gaurav-Kushwaha-1225/Periodic_Table/blob/main/LICENSE)

## 🙏 Acknowledgments

- Data: [Bowserinator/Periodic-Table-JSON](https://github.com/Bowserinator/Periodic-Table-JSON)
- Framework: [Kivy](https://kivy.org) & [KivyMD](https://kivymd.readthedocs.io/)
- Inspired by: Chernykh Technology's Periodic Table App

## 📝 License

MIT License - Free and open source

---

**Created with ❤️ by (Gaurav Kushwaha)[https://www.linkedin.com/in/gaurav-kushwaha-friday-code/]**
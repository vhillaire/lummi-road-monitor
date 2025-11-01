# Lummi Nation Road Closures Monitor

Monitor Whatcom County road closures affecting Lummi Nation Reservation access routes, with automated alerts via Home Assistant.

## 🚗 What It Does

Checks Whatcom County's official road closure page and alerts you when closures affect your routes to/from the Lummi Nation Reservation:

- **Marine Drive**
- **Slater Road**  
- **Haxton Way**
- **Ferndale Road**
- **Imhoff Road**

**Smart scheduling:** Only checks during commute hours (3-5am & 3-5pm)  
**Auto-abbreviations:** Automatically matches "Marine Dr", "Marine Drive", "Marine Drv", etc.  
**Command-line testing:** Quick ad-hoc checks without editing files

## ⚡ Quick Start

```bash
# 1. Install
bash install.sh

# 2. Test it
python3 test_roads.py

# 3. Check a specific road
python3 test_roads.py "Lummi Shore"

# 4. Set up automation (choose one):
#    - Cron (recommended): see docs/CRON_ALTERNATIVE.md
#    - Home Assistant: add home_assistant_config.yaml to your config
```

## 📋 Requirements

- Raspberry Pi (or any Linux system)
- Python 3.7+
- Home Assistant (optional - can run standalone with cron)

## 🔧 Features

- ✅ **Time-aware checking** - Only runs during commute hours
- ✅ **Auto-abbreviation matching** - Catches "Dr", "Drive", "Rd", "Road", etc.
- ✅ **Command-line testing** - `python3 test_roads.py "Road Name"`
- ✅ **Home Assistant integration** - Sensor, automations, and dashboard
- ✅ **Cron-friendly** - Can run independently of HA
- ✅ **Zero configuration** - Works out of the box for Lummi access roads
- ✅ **Easy customization** - Just edit the `MY_ROADS` list

## 📖 Documentation

- **[START_HERE.md](docs/START_HERE.md)** - Quick introduction
- **[README.md](docs/README.md)** - Complete documentation
- **[NEW_FEATURES.md](docs/NEW_FEATURES.md)** - Latest updates
- **[CMDLINE_EXAMPLES.md](docs/CMDLINE_EXAMPLES.md)** - Testing examples
- **[CRON_ALTERNATIVE.md](docs/CRON_ALTERNATIVE.md)** - Cron setup (recommended)
- **[ABBREVIATIONS.md](docs/ABBREVIATIONS.md)** - How auto-abbreviation works
- **[FILE_LIST.md](docs/FILE_LIST.md)** - All files and links

## 🎯 Use Cases

```bash
# "I heard Lummi Shore is closed - is it?"
python3 test_roads.py "Lummi Shore"

# "Check all my routes"
python3 test_roads.py "Marine Drive" "Slater Road" "Haxton Way"

# "Is anything closed right now?"
python3 test_roads.py

# With aliases (after running add_aliases.sh):
roadcheck "Lummi Shore"
lummicheck  # Check all Lummi access roads
```

## 🏗️ Project Structure

```
lummi-road-monitor/
├── whatcom_road_closures.py      # Main monitoring script
├── test_roads.py                  # Testing and debug tool
├── install.sh                     # Quick installer
├── add_aliases.sh                 # Optional shell aliases
├── home_assistant_config.yaml     # HA configuration
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── LICENSE                        # MIT License
└── docs/                          # Documentation
    ├── START_HERE.md
    ├── README.md
    ├── NEW_FEATURES.md
    ├── CMDLINE_EXAMPLES.md
    ├── CRON_ALTERNATIVE.md
    ├── ABBREVIATIONS.md
    └── FILE_LIST.md
```

## 🔄 How It Works

1. **Scheduled checks** - Runs every 30 minutes during 3-5am and 3-5pm
2. **Web scraping** - Fetches closures from whatcomcounty.us
3. **Smart matching** - Checks all road name variations automatically
4. **Filtering** - Only shows closures affecting your configured roads
5. **Alerting** - Triggers Home Assistant notification or runs your custom action

## 🛠️ Customization

Edit `whatcom_road_closures.py`:

```python
# Add/remove roads
MY_ROADS = [
    "Marine Drive",
    "Slater Road",
    "Your Road Here",  # Abbreviations auto-generated!
]

# Change check times
MORNING_START = 3   # 3 AM
MORNING_END = 5     # 5 AM
EVENING_START = 15  # 3 PM  
EVENING_END = 17    # 5 PM
```

## 🤝 Contributing

This is a personal project for Lummi Nation Reservation access monitoring. Feel free to fork and adapt for your own area!

## 📝 License

MIT License - See [LICENSE](LICENSE) file

## 🙏 Acknowledgments

- Whatcom County Public Works for maintaining the road closure page
- Built for the Lummi Nation community

## 📧 Questions?

Check the [docs](docs/) folder for detailed documentation, or run:

```bash
python3 test_roads.py --help  # (shows usage)
python3 test_roads.py          # (shows current closures)
```

---

**Made with ❤️ for the Lummi Nation community**

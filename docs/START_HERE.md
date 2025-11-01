# START HERE

## What You're Getting

A Home Assistant monitor for road closures affecting Lummi Nation access routes.

**Monitored Roads:**
- Marine Drive (auto-matches: Dr, Drv, etc.)
- Slater Road (auto-matches: Rd)
- Haxton Way (auto-matches: Wy)
- Ferndale Road (auto-matches: Rd)
- Imhoff Road (auto-matches: Rd)

*USPS abbreviations auto-generated!*

**When It Checks:**
- 3-5 AM (every 30 min)
- 3-5 PM (every 30 min)

**What It Does:**
- Scrapes Whatcom County website
- Filters for your roads only
- Alerts you if closure found

## Quick Install

Two options - pick one:

### Option 1: Cron (Recommended - simpler!)

```bash
bash install.sh
# Then add cron jobs (see CRON_ALTERNATIVE.md)
```

Runs independently, HA just reads the file.

### Option 2: HA Automations

```bash
bash install.sh
# Then add home_assistant_config.yaml to your configuration.yaml
```

Everything managed by Home Assistant.

## Test First

Before installing, see what it finds:

```bash
python3 test_roads.py
```

Shows:
- All auto-generated road name variations
- Current closures and which ones match your roads
- Which variation triggered the match

**Check specific roads:**
```bash
python3 test_roads.py "Lummi Shore"
python3 test_roads.py "Lummi Shore" "Guide Meridian"
```

Great for testing if a road you heard about is actually closed!

## Files

- `whatcom_road_closures.py` - Main script
- `test_roads.py` - Test/debug tool (now with command line support!)
- `install.sh` - Quick installer
- `add_aliases.sh` - Optional: adds convenient shell aliases
- `home_assistant_config.yaml` - HA config (Option 2)
- `CRON_ALTERNATIVE.md` - Cron setup (Option 1)
- `CMDLINE_EXAMPLES.md` - Command line testing examples
- `ABBREVIATIONS.md` - Street type abbreviations reference
- `README.md` - Full documentation
- `START_HERE.md` - This file

## Optional: Quick Aliases

For really fast checks, run:
```bash
bash add_aliases.sh
source ~/.bash_aliases
```

Then:
```bash
roadcheck "Lummi Shore"        # Check any road
lummicheck                     # Check all your access roads
```

## Quick Questions

**Change check times?**
Edit the script, change `MORNING_START`, `EVENING_START`, etc.

**Add more roads?**
Edit `MY_ROADS` list (abbreviations auto-generated):
```python
MY_ROADS = [
    "Marine Drive",
    "New Road Name"  # That's it!
]
```

**See what it's doing?**
`tail -f /tmp/road_check.log`

**Not working?**
Run `python3 test_roads.py` to debug.

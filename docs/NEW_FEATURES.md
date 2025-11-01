# New Features & Updates

## Command Line Testing (NEW!)

You can now check specific roads without editing files:

```bash
# Check a single road
python3 test_roads.py "Lummi Shore"

# Check multiple roads
python3 test_roads.py "Lummi Shore" "Guide Meridian" "Marine Drive"

# Check roads with different types
python3 test_roads.py "Northwest Avenue"  # Auto-checks Ave, Av, Avn too
```

### Why This Is Useful

- **Quick verification**: "I heard Lummi Shore is closed"
- **Test before configuring**: See if a road name will match
- **Debug**: "Why didn't my alert trigger?"
- **Ad-hoc checks**: Check roads you don't usually monitor

### Output Shows

```
Checking 1 road(s) from command line...

Monitored roads and auto-generated variations:

  Lummi Shore Drive:
    • lummi shore dr
    • lummi shore drive
    • lummi shore drv

✓ MATCHES (Will trigger alert):
----------------------------------------------------------------------
1. Correction: Lummi Shore Drive Traffic Impacts: October 13–31
   Matched on: 'lummi shore drive'
```

## Auto-Generated Abbreviations (NEW!)

No more manually typing every variation!

### Before (Manual):
```python
CRITICAL_ROADS = [
    "marine drive", "marine dr", "marine drv",
    "slater road", "slater rd",
    # ... tedious!
]
```

### Now (Automatic):
```python
MY_ROADS = [
    "Marine Drive",   # Auto-generates: dr, drv
    "Slater Road",    # Auto-generates: rd
]
```

### Supported Types

- Avenue → Ave, Av, Avn, Avenu
- Boulevard → Blvd, Boul, Boulv
- Drive → Dr, Drv
- Road → Rd
- Street → St, Str
- Lane → Ln
- Way → Wy
- Highway → Hwy, Hiwy
- And more... (see ABBREVIATIONS.md)

### Verification

Run test to see all variations:
```bash
python3 test_roads.py
```

Output shows exactly what's being checked:
```
Marine Drive:
  • marine dr
  • marine drive
  • marine drv
```

## Optional: Shell Aliases (NEW!)

For even faster checking:

```bash
bash add_aliases.sh
source ~/.bash_aliases
```

Then:
```bash
roadcheck "Lummi Shore"        # Quick check
lummicheck                     # Check all Lummi access roads
```

## Original Features

- ✓ Time-based checking (3-5am, 3-5pm)
- ✓ Focused on Lummi Nation access roads
- ✓ Home Assistant integration
- ✓ Cron or HA automation options
- ✓ Email/notification on closures

## Files Included

1. **whatcom_road_closures.py** - Main monitoring script
2. **test_roads.py** - Testing tool with CLI support
3. **install.sh** - Quick installer
4. **add_aliases.sh** - Shell alias setup
5. **home_assistant_config.yaml** - HA configuration
6. **CRON_ALTERNATIVE.md** - Cron setup guide
7. **CMDLINE_EXAMPLES.md** - CLI testing examples
8. **ABBREVIATIONS.md** - Street abbreviations reference
9. **README.md** - Full documentation
10. **START_HERE.md** - Quick start guide

## Real-World Examples

### "Is Lummi Shore still closed?"
```bash
python3 test_roads.py "Lummi Shore"
```

### "Check my usual routes"
```bash
python3 test_roads.py "Marine Drive" "Slater Road" "Haxton Way"
```

### "Will it catch 'Marine Dr.' vs 'Marine Drive'?"
```bash
python3 test_roads.py "Marine Drive"
# Shows: marine drive, marine dr, marine drv
```

### "Test before adding to config"
```bash
python3 test_roads.py "New Road Name"
# See if it matches any current closures
```

## Summary

You now have:
- ✓ Command line testing
- ✓ Automatic abbreviation handling
- ✓ Optional shell aliases
- ✓ Clear verification of what's being checked
- ✓ Easy debugging

All with minimal typing!

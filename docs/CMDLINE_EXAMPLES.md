# Command Line Testing Examples

## Basic Usage

### Check your configured roads:
```bash
python3 test_roads.py
```

### Check a single specific road:
```bash
python3 test_roads.py "Lummi Shore"
```

### Check multiple roads at once:
```bash
python3 test_roads.py "Lummi Shore" "Guide Meridian" "Northwest Drive"
```

### Check roads with Drive, Road, etc:
```bash
python3 test_roads.py "Lummi Shore Drive"
```
Auto-generates: lummi shore drive, lummi shore dr, lummi shore drv

## Real Examples

### Is Lummi Shore closed?
```bash
$ python3 test_roads.py "Lummi Shore"

Checking 1 road(s) from command line...

======================================================================
LUMMI NATION ACCESS ROADS - TEST
======================================================================

Checking roads from: command line

Monitored roads and auto-generated variations:

  Lummi Shore:
    • lummi shore

  Total variations being checked: 1

======================================================================
CURRENT CLOSURES:
======================================================================

✓ MATCHES (Will trigger alert):
----------------------------------------------------------------------
1. Correction: Lummi Shore Drive Traffic Impacts: October 13–31
   Matched on: 'lummi shore'
```

### Check Guide Meridian with abbreviations:
```bash
$ python3 test_roads.py "Guide Meridian Road"

Checking roads from: command line

Monitored roads and auto-generated variations:

  Guide Meridian Road:
    • guide meridian rd
    • guide meridian road
```

### Check multiple roads at once:
```bash
$ python3 test_roads.py "Marine Drive" "Lummi Shore" "Haxton Way"

Checking 3 road(s) from command line...

Monitored roads and auto-generated variations:

  Marine Drive:
    • marine dr
    • marine drive
    • marine drv

  Lummi Shore:
    • lummi shore

  Haxton Way:
    • haxton way
    • haxton wy
```

## Quick Tests

**"Is anything closed on my way to the casino?"**
```bash
python3 test_roads.py "Slater Road" "Haxton Way"
```

**"What about that construction on Lummi Shore?"**
```bash
python3 test_roads.py "Lummi Shore"
```

**"Check all roads to the ferry"**
```bash
python3 test_roads.py "Haxton Way" "Kwina Road" "Lummi Shore"
```

## Why This Is Useful

- Quick checks without editing files
- Test if a road you heard about is actually closed
- Verify the script will catch a particular road name
- See what abbreviations will be matched
- Debug: "Why didn't my road trigger?"

## Pro Tip

Add to your .bashrc for quick checks:
```bash
alias roadcheck='python3 /home/homeassistant/test_roads.py'
```

Then:
```bash
roadcheck "Lummi Shore"
```

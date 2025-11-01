# Lummi Nation Access Roads Monitor

Monitors Whatcom County road closures for routes in/out of Lummi Nation Reservation.

## Quick Setup

### 1. Install on Raspberry Pi

```bash
# Install dependencies
pip3 install requests beautifulsoup4 --break-system-packages

# Copy script to Home Assistant config directory
sudo cp whatcom_road_closures.py /home/homeassistant/
sudo chmod +x /home/homeassistant/whatcom_road_closures.py
```

### 2. Configure Home Assistant

Add the contents of `home_assistant_config.yaml` to your `/config/configuration.yaml`

### 3. Monitored Roads

**Currently watching these access routes:**
- Marine Drive (+ Dr, Drv variations)
- Slater Road (+ Rd variations)
- Haxton Way (+ Wy variations)
- Ferndale Road (+ Rd variations)
- Imhoff Road (+ Rd variations)

The script **automatically generates** common USPS abbreviations for each road:
- Drive → Dr, Drv
- Road → Rd
- Way → Wy
- Avenue → Ave, Av, Avn
- Street → St, Str
- And many more...

**To add/change roads:**
Edit `MY_ROADS` list in `whatcom_road_closures.py`:
```python
MY_ROADS = [
    "Marine Drive",
    "Your New Road",  # Add here
]
```

No need to manually add abbreviations - they're auto-generated!

### 4. Check Schedule

Script only runs during commute hours:
- **Morning:** 3 AM - 5 AM (every 30 min = 4 checks)
- **Evening:** 3 PM - 5 PM (every 30 min = 4 checks)

Outside these hours, script returns immediately without fetching data.

### 5. Test It

Check your configured roads:
```bash
python3 /home/homeassistant/whatcom_road_closures.py
```

Or check specific roads:
```bash
python3 test_roads.py "Lummi Shore"
python3 test_roads.py "Lummi Shore" "Guide Meridian" "Haxton Way"
```

See [CMDLINE_EXAMPLES.md](CMDLINE_EXAMPLES.md) for more examples.

### 6. Restart Home Assistant

Sensor will appear as `sensor.lummi_access_roads`

## How It Works

- Checks county website only during commute windows
- Filters for your specific access roads
- Creates sensor with count of relevant closures
- Triggers notification when closure detected
- Minimal bandwidth/processing

## Customization

**Change check times:**
Edit these in `whatcom_road_closures.py`:
```python
MORNING_START = 3   # 3 AM
MORNING_END = 5     # 5 AM
EVENING_START = 15  # 3 PM
EVENING_END = 17    # 5 PM
```

**Add more roads:**
```python
MY_ROADS = [
    "Marine Drive",
    "your road here"
]
```
Abbreviations auto-generated!

**Change check frequency:**
In `home_assistant_config.yaml`, adjust the `delay: "00:30:00"` values (currently 30 minutes).

## Testing & Debugging

**Test your configured roads:**
```bash
python3 test_roads.py
```

**Check a specific road:**
```bash
python3 test_roads.py "Lummi Shore"
```

**Check multiple roads:**
```bash
python3 test_roads.py "Lummi Shore" "Guide Meridian" "Haxton Way"
```

The test script will:
- Show all auto-generated variations
- List current closures from the county
- Show which closures match your roads
- Display exactly which variation matched

Perfect for:
- "I heard Lummi Shore is closed - is it?"
- "Will my script catch 'Marine Dr' vs 'Marine Drive'?"
- "Why didn't this road trigger an alert?"

See [CMDLINE_EXAMPLES.md](CMDLINE_EXAMPLES.md) for detailed examples.

## Alternative: Email Alerts

Whatcom County offers email/text alerts:
https://www.whatcomcounty.us/list.aspx?ListID=455

Could forward those to HA via IMAP for instant alerts.

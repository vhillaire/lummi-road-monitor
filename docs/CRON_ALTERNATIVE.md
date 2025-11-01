# Alternative: Cron-Based Setup (Simpler!)

If you prefer cron over HA automations, this is cleaner:

## Setup

```bash
# Install script
sudo cp whatcom_road_closures.py /usr/local/bin/
sudo chmod +x /usr/local/bin/whatcom_road_closures.py

# Edit crontab
crontab -e

# Add these lines (checks every 30 min during commute hours):
0,30 3-4 * * * /usr/local/bin/whatcom_road_closures.py > /tmp/road_check.log 2>&1
0,30 15-16 * * * /usr/local/bin/whatcom_road_closures.py > /tmp/road_check.log 2>&1
```

## Home Assistant Config (Simple Version)

```yaml
# Just read the JSON file, no command_line sensor needed
sensor:
  - platform: file
    name: "Lummi Access Roads"
    file_path: "/tmp/whatcom_closures.json"
    value_template: "{{ value_json.relevant_closures }}"
    json_attributes:
      - closures
      - last_updated
      - status
    scan_interval: 300  # Check file every 5 min

automation:
  - alias: "Alert on Lummi Access Road Closure"
    trigger:
      - platform: state
        entity_id: sensor.lummi_access_roads
    condition:
      - condition: template
        value_template: "{{ trigger.to_state.state | int > 0 }}"
    action:
      - service: notify.mobile_app
        data:
          title: "⚠️ Lummi Access Road Closure"
          message: >
            {{ state_attr('sensor.lummi_access_roads', 'closures')[0].title }}
```

## Why This Is Better

- Cron is more reliable than HA automations with delays
- Simpler debugging (check `/tmp/road_check.log`)
- Script runs independently of HA
- HA just reads the JSON file
- Less complex configuration

## Testing

```bash
# Run manually to test
/usr/local/bin/whatcom_road_closures.py

# Check output
cat /tmp/whatcom_closures.json

# View cron logs
grep CRON /var/log/syslog
```

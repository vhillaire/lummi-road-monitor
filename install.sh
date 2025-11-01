#!/bin/bash
# Quick installer for Lummi Nation Access Roads Monitor

echo "Installing Lummi Nation Access Roads Monitor..."
echo "Monitors: Marine Dr, Slater Rd, Haxton Way, Ferndale Rd, Imhoff Rd"
echo ""

# Install Python dependencies
echo "Installing dependencies..."
pip3 install requests beautifulsoup4 --break-system-packages

# Copy script to Home Assistant directory
echo "Installing script..."
sudo cp whatcom_road_closures.py /home/homeassistant/
sudo chmod +x /home/homeassistant/whatcom_road_closures.py

# Test the script
echo "Testing script..."
python3 /home/homeassistant/whatcom_road_closures.py

echo ""
echo "✓ Installation complete!"
echo ""
echo "Next steps:"
echo "1. Add the contents of home_assistant_config.yaml to your /config/configuration.yaml"
echo "2. Restart Home Assistant"
echo ""
echo "Sensor: sensor.lummi_access_roads"
echo "Checks: 3-5am & 3-5pm (every 30 min)"

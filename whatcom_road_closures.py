#!/usr/bin/env python3
"""
Whatcom County Road Closures Monitor for Home Assistant
Scrapes road closure data and checks proximity to your address
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import re

# Your location and critical access roads to Lummi Nation
MY_ADDRESS = "3848 Itistha Way, Bellingham, WA 98226"

# USPS Street Suffix Abbreviations (common ones for your area)
STREET_SUFFIXES = {
    "avenue": ["avenue", "ave", "av", "avn", "avenu"],
    "boulevard": ["boulevard", "blvd", "boul", "boulv"],
    "drive": ["drive", "dr", "drv"],
    "road": ["road", "rd"],
    "street": ["street", "st", "str"],
    "lane": ["lane", "ln"],
    "way": ["way", "wy"],
    "place": ["place", "pl"],
    "court": ["court", "ct"],
    "circle": ["circle", "cir", "circ"],
    "trail": ["trail", "trl"],
    "parkway": ["parkway", "pkwy", "pkwy", "pky"],
    "highway": ["highway", "hwy", "hiwy"]
}

def generate_road_variations(road_name):
    """Generate all common variations of a road name"""
    variations = [road_name.lower()]
    
    # Check each suffix type
    for full_suffix, abbrevs in STREET_SUFFIXES.items():
        for suffix in abbrevs:
            if road_name.lower().endswith(suffix):
                # Get the base name (road name without suffix)
                base = road_name.lower().rsplit(suffix, 1)[0].strip()
                # Generate all variations
                for abbrev in abbrevs:
                    variations.append(f"{base} {abbrev}")
                break
    
    return list(set(variations))  # Remove duplicates

# Your critical roads (full names)
MY_ROADS = [
    "Marine Drive",
    "Slater Road",
    "Haxton Way",
    "Ferndale Road",
    "Imhoff Road"
]

# Auto-generate all variations
CRITICAL_ROADS = []
for road in MY_ROADS:
    CRITICAL_ROADS.extend(generate_road_variations(road))

# Only check during commute windows
MORNING_START = 3   # 3 AM
MORNING_END = 5     # 5 AM
EVENING_START = 15  # 3 PM
EVENING_END = 17    # 5 PM

def is_commute_time():
    """Check if we're in a commute window"""
    current_hour = datetime.now().hour
    
    morning_window = MORNING_START <= current_hour < MORNING_END
    evening_window = EVENING_START <= current_hour < EVENING_END
    
    return morning_window or evening_window

def get_road_closures():
    """Fetch and parse road closures from Whatcom County"""
    url = "https://www.whatcomcounty.us/952/Road-Closures-Restrictions"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        closures = []
        
        # Find all closure alerts
        alerts = soup.find_all('a', href=re.compile(r'/CivicAlerts\.aspx\?AID='))
        
        for alert in alerts:
            title = alert.get_text(strip=True)
            link = "https://www.whatcomcounty.us" + alert['href']
            closures.append({
                'title': title,
                'link': link,
                'timestamp': datetime.now().isoformat()
            })
        
        return closures
    
    except Exception as e:
        print(f"Error fetching closures: {e}")
        return []

def is_relevant(closure_title):
    """Check if closure affects Lummi Nation access roads"""
    title_lower = closure_title.lower()
    
    # Check each critical road
    for road in CRITICAL_ROADS:
        if road in title_lower:
            return True
    
    return False

def main():
    """Main function"""
    
    # Only run during commute windows
    if not is_commute_time():
        result = {
            'total_closures': 0,
            'relevant_closures': 0,
            'closures': [],
            'last_updated': datetime.now().isoformat(),
            'status': 'outside_commute_hours'
        }
        print(json.dumps(result, indent=2))
        return result
    
    print("Checking Lummi Nation access roads during commute hours...")
    
    all_closures = get_road_closures()
    relevant_closures = [c for c in all_closures if is_relevant(c['title'])]
    
    result = {
        'total_closures': len(all_closures),
        'relevant_closures': len(relevant_closures),
        'closures': relevant_closures,
        'last_updated': datetime.now().isoformat(),
        'status': 'active'
    }
    
    # Output JSON for Home Assistant
    print(json.dumps(result, indent=2))
    
    # Also save to file for persistence
    with open('/tmp/whatcom_closures.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    return result

if __name__ == "__main__":
    main()

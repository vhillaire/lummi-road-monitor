#!/usr/bin/env python3
"""
Test script - shows all current closures and which ones match your roads

Usage:
  python3 test_roads.py                        # Check your configured roads
  python3 test_roads.py "Lummi Shore"          # Check a specific road
  python3 test_roads.py "Lummi Shore" "Guide Meridian"  # Check multiple roads
"""

import requests
from bs4 import BeautifulSoup
import re
import sys

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
    
    for full_suffix, abbrevs in STREET_SUFFIXES.items():
        for suffix in abbrevs:
            if road_name.lower().endswith(suffix):
                base = road_name.lower().rsplit(suffix, 1)[0].strip()
                for abbrev in abbrevs:
                    variations.append(f"{base} {abbrev}")
                break
    
    return list(set(variations))

MY_ROADS = [
    "Marine Drive",
    "Slater Road",
    "Haxton Way",
    "Ferndale Road",
    "Imhoff Road"
]

CRITICAL_ROADS = []
for road in MY_ROADS:
    CRITICAL_ROADS.extend(generate_road_variations(road))

def get_all_closures():
    """Fetch all closures"""
    url = "https://www.whatcomcounty.us/952/Road-Closures-Restrictions"
    response = requests.get(url, timeout=30)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    closures = []
    alerts = soup.find_all('a', href=re.compile(r'/CivicAlerts\.aspx\?AID='))
    
    for alert in alerts:
        title = alert.get_text(strip=True)
        closures.append(title)
    
    return closures

def test_matching(custom_roads=None):
    """Test which closures match your roads"""
    # Use command line roads if provided, otherwise use configured roads
    if custom_roads:
        roads_to_check = custom_roads
        roads_list = []
        for road in roads_to_check:
            roads_list.extend(generate_road_variations(road))
        source = "command line"
    else:
        roads_to_check = MY_ROADS
        roads_list = CRITICAL_ROADS
        source = "configuration"
    
    print("="*70)
    print("LUMMI NATION ACCESS ROADS - TEST")
    print("="*70)
    print(f"\nChecking roads from: {source}")
    print("\nMonitored roads and auto-generated variations:")
    for road in roads_to_check:
        variations = generate_road_variations(road)
        print(f"\n  {road}:")
        for v in sorted(variations):
            print(f"    • {v}")
    
    print(f"\n  Total variations being checked: {len(roads_list)}")
    
    print("\n" + "="*70)
    print("CURRENT CLOSURES:")
    print("="*70 + "\n")
    
    closures = get_all_closures()
    matched = []
    unmatched = []
    
    for closure in closures:
        is_match = False
        matched_road = None
        for road in roads_list:
            if road in closure.lower():
                is_match = True
                matched_road = road
                break
        
        if is_match:
            matched.append((closure, matched_road))
        else:
            unmatched.append(closure)
    
    if matched:
        print("✓ MATCHES (Will trigger alert):")
        print("-" * 70)
        for i, (closure, matched_road) in enumerate(matched, 1):
            print(f"{i}. {closure}")
            print(f"   Matched on: '{matched_road}'")
    else:
        print("✓ No closures affecting your roads!")
    
    if unmatched:
        print("\n✗ Other closures (ignored):")
        print("-" * 70)
        for closure in unmatched:
            print(f"  • {closure}")
    
    print("\n" + "="*70)
    print(f"Summary: {len(matched)} relevant, {len(unmatched)} ignored")
    print("="*70)

if __name__ == "__main__":
    # Check if command line arguments provided
    if len(sys.argv) > 1:
        # Use roads from command line
        custom_roads = sys.argv[1:]
        print(f"\nChecking {len(custom_roads)} road(s) from command line...\n")
        test_matching(custom_roads)
    else:
        # Use configured roads
        test_matching()

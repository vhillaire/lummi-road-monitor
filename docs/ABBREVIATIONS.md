# Supported Street Type Abbreviations

The script automatically recognizes USPS standard abbreviations for street types.

## Auto-Generated Variations

When you add a road like "Marine Drive", the script automatically checks for:

### Common Types in Your Area

| Full Name | Abbreviations Checked |
|-----------|----------------------|
| Avenue | Avenue, Ave, Av, Avn, Avenu |
| Boulevard | Boulevard, Blvd, Boul, Boulv |
| Drive | Drive, Dr, Drv |
| Road | Road, Rd |
| Street | Street, St, Str |
| Lane | Lane, Ln |
| Way | Way, Wy |
| Place | Place, Pl |
| Court | Court, Ct |
| Circle | Circle, Cir, Circ |
| Trail | Trail, Trl |
| Parkway | Parkway, Pkwy, Pky |
| Highway | Highway, Hwy, Hiwy |

## Examples

**"Marine Drive"** matches:
- Marine Drive
- Marine Dr
- Marine Drv
- marine drive (case-insensitive)
- MARINE DR (case-insensitive)

**"Slater Road"** matches:
- Slater Road
- Slater Rd
- slater rd
- SLATER ROAD

**"Haxton Way"** matches:
- Haxton Way
- Haxton Wy
- haxton way

## Adding More Abbreviations

If you find a variation not covered, edit `STREET_SUFFIXES` in the script:

```python
STREET_SUFFIXES = {
    "avenue": ["avenue", "ave", "av", "avn", "avenu"],
    "your_type": ["full name", "abbrev1", "abbrev2"],
}
```

## Testing

Run `test_roads.py` to see all variations being checked for your roads:

```bash
python3 test_roads.py
```

Output will show:
```
Your monitored roads and auto-generated variations:

  Marine Drive:
    • marine dr
    • marine drive
    • marine drv

  Slater Road:
    • slater rd
    • slater road
```

## Why This Matters

County closure notices may use any variation:
- "Marine Drive closed"
- "Marine Dr. closed"
- "MARINE DR closed"

The script catches them all!

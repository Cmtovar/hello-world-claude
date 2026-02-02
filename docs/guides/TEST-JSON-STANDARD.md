# Test Map JSON Standard & Validation Pattern

**Purpose:** Prevent JSON syntax errors when creating test maps
**Problem:** JavaScript hex notation (0x...) is NOT valid JSON
**Created:** 2026-01-30
**Status:** Active Standard

---

## The Problem

**Recurring Error Across Sessions:**
```
Syntax error: the string did not match the expected pattern
```

**Root Cause:**
JavaScript allows hex color notation: `0x228b22`
JSON only allows decimal numbers: `2263842`

When creating test maps, it's natural to use hex colors (common in Three.js), but JSON parsers reject them.

---

## The Standard

### ✅ CORRECT: Use Decimal Colors

```json
{
  "name": "Test Map",
  "voxels": [
    {"x": 0, "y": 0, "z": 0, "color": 2263842}
  ],
  "characterGroup": {
    "characters": [
      {
        "colors": {
          "boots": 9127187,
          "body": 6908265,
          "head": 13808780
        }
      }
    ]
  }
}
```

### ❌ WRONG: Hex Notation (Breaks JSON)

```json
{
  "voxels": [
    {"x": 0, "y": 0, "z": 0, "color": 0x228b22}  // INVALID!
  ],
  "characterGroup": {
    "characters": [
      {
        "colors": {
          "boots": 0x8b4513,  // INVALID!
          "body": 0x696969,   // INVALID!
          "head": 0xd2b48c    // INVALID!
        }
      }
    ]
  }
}
```

---

## Conversion Reference

### Common Colors (Hex → Decimal)

| Color Name | Hex | Decimal | RGB |
|------------|-----|---------|-----|
| Forest Green | 0x228b22 | 2263842 | (34, 139, 34) |
| Brown | 0x8b4513 | 9127187 | (139, 69, 19) |
| Dark Gray | 0x696969 | 6908265 | (105, 105, 105) |
| Tan | 0xd2b48c | 13808780 | (210, 180, 140) |
| Olive | 0x6b6b47 | 7039815 | (107, 107, 71) |
| Olive Drab | 0x6b8e23 | 7048739 | (107, 142, 35) |
| Peach | 0xffdab9 | 16767673 | (255, 218, 185) |
| Royal Blue | 0x4169e1 | 4286945 | (65, 105, 225) |
| Light Yellow | 0xffeaa7 | 16771751 | (255, 234, 167) |
| Purple | 0x9370db | 9662683 | (147, 112, 219) |
| Goldenrod | 0xdaa520 | 14329120 | (218, 165, 32) |
| Light Pink | 0xffb6c1 | 16758465 | (255, 182, 193) |

### Quick Conversion

**Python:**
```python
hex_color = 0x228b22
decimal = hex_color  # Python automatically converts
print(decimal)  # 2263842
```

**JavaScript (for reference, NOT for JSON):**
```javascript
const hex = 0x228b22;
const decimal = hex;  // 2263842
```

**Online:** https://www.binaryhexconverter.com/hex-to-decimal-converter

---

## Test Map Template

### Basic Test Map Structure

```json
{
  "name": "Test Name",
  "description": "What this test validates",
  "notes": "Implementation notes",
  "designReference": "Link to design doc if applicable",

  "playerStart": {"x": 0, "y": 1, "z": 0},
  "goalPosition": {"x": 10, "y": 1, "z": 0},

  "voxels": [
    {"x": 0, "y": 0, "z": 0, "color": 2263842, "type": "grass"}
  ]
}
```

### Cutscene Test Map Structure

```json
{
  "name": "Cutscene Test",
  "description": "Cutscene description",
  "cutsceneMode": true,

  "playerStart": {"x": 0, "y": 1, "z": 0},
  "voxels": [...],

  "characterGroup": {
    "characters": [
      {
        "id": "character-01",
        "name": "Character Name",
        "startPosition": {"x": 2, "y": 1, "z": 0},
        "colors": {
          "boots": 9127187,
          "body": 6908265,
          "head": 13808780
        },
        "actionQueue": [
          {"type": "move", "to": {"x": 5, "y": 1, "z": 0}}
        ]
      }
    ]
  }
}
```

---

## Validation Script

### validate-test-json.py

```python
#!/usr/bin/env python3
"""
Validate test map JSON files for common errors.
Usage: python3 validate-test-json.py test-maps/*.json
"""

import json
import sys
import re
from pathlib import Path

def validate_json_file(filepath):
    """Validate a single JSON file."""
    errors = []

    # Read file
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except Exception as e:
        return [f"Cannot read file: {e}"]

    # Check for hex notation (common error)
    hex_pattern = r':\s*0x[0-9a-fA-F]+'
    hex_matches = re.findall(hex_pattern, content)
    if hex_matches:
        errors.append(f"Found hex notation (invalid JSON): {hex_matches[:3]}")
        errors.append("  → Convert to decimal: 0x228b22 = 2263842")

    # Try to parse JSON
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        errors.append(f"JSON parse error: {e}")
        return errors

    # Validate structure
    if 'voxels' in data:
        for i, voxel in enumerate(data['voxels']):
            if 'color' in voxel:
                if not isinstance(voxel['color'], int):
                    errors.append(f"Voxel {i}: color must be integer (decimal)")

    if 'characterGroup' in data:
        if 'characters' in data['characterGroup']:
            for char in data['characterGroup']['characters']:
                if 'colors' in char:
                    for color_key, color_val in char['colors'].items():
                        if not isinstance(color_val, int):
                            errors.append(f"Character {char.get('id')}: {color_key} must be integer")

    return errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate-test-json.py <json-files>")
        sys.exit(1)

    all_valid = True

    for filepath in sys.argv[1:]:
        path = Path(filepath)
        if not path.exists():
            print(f"❌ {filepath}: File not found")
            all_valid = False
            continue

        errors = validate_json_file(path)

        if errors:
            print(f"❌ {filepath}:")
            for error in errors:
                print(f"   {error}")
            all_valid = False
        else:
            print(f"✓ {filepath}")

    sys.exit(0 if all_valid else 1)

if __name__ == '__main__':
    main()
```

**Usage:**
```bash
# Validate all test maps
python3 validate-test-json.py test-maps/*.json

# Validate specific file
python3 validate-test-json.py test-maps/cutscene-test-01-parallel.json

# Pre-commit check
python3 validate-test-json.py test-maps/*.json && git commit
```

---

## Test Factory Pattern (Future)

### Strategy: Different JSON Handlers

```python
class TestMapFactory:
    """Factory for creating valid test map JSON."""

    @staticmethod
    def create_basic_test(name, voxels, player_start, goal):
        """Create basic movement test."""
        return {
            "name": name,
            "playerStart": player_start,
            "goalPosition": goal,
            "voxels": [
                {"x": v[0], "y": v[1], "z": v[2], "color": v[3]}
                for v in voxels
            ]
        }

    @staticmethod
    def create_cutscene_test(name, voxels, characters):
        """Create cutscene test with character group."""
        return {
            "name": name,
            "cutsceneMode": True,
            "voxels": voxels,
            "characterGroup": {
                "characters": characters
            }
        }

    @staticmethod
    def hex_to_decimal(hex_color):
        """Convert hex color to decimal (safe)."""
        if isinstance(hex_color, str):
            return int(hex_color, 16)
        return hex_color

# Usage
factory = TestMapFactory()
test_map = factory.create_basic_test(
    "My Test",
    voxels=[(0, 0, 0, 0x228b22)],  # Converts internally
    player_start={"x": 0, "y": 1, "z": 0},
    goal={"x": 5, "y": 1, "z": 0}
)
```

---

## Quick Reference Card

### Creating New Test Maps

1. **Use the template** (see above)
2. **Colors MUST be decimal integers**
3. **Validate before committing:**
   ```bash
   python3 -m json.tool your-test.json
   ```
4. **If you have hex colors:**
   ```bash
   python3 validate-test-json.py your-test.json
   ```

### When Errors Occur

**Error:** "Syntax error: the string did not match the expected pattern"

**Fix:**
```bash
# Auto-fix hex to decimal
python3 << 'EOF'
import json, re
with open('your-file.json', 'r') as f:
    content = f.read()
content = re.sub(r'0x([0-9a-fA-F]+)', lambda m: str(int(m.group(1), 16)), content)
data = json.loads(content)
with open('your-file.json', 'w') as f:
    json.dump(data, f, indent=2)
EOF
```

---

## Session Continuity Note

**For Future Claude Sessions:**

If you encounter JSON parsing errors in test maps:
1. Check for hex notation (`0x...`) in color values
2. Run validation script: `python3 validate-test-json.py <file>`
3. Auto-fix with hex-to-decimal conversion script above
4. **ALWAYS use decimal colors** when creating new test maps

This pattern prevents the recurring error that has appeared across multiple sessions.

---

**Standard Last Updated:** 2026-01-30
**Validated Against:** cutscene-test-01-parallel.json (successful conversion)

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
        errors.append("  → Run: python3 fix-hex-colors.py " + str(filepath))

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
                    errors.append(f"Voxel {i}: color must be integer (decimal), got {type(voxel['color']).__name__}")

    if 'characterGroup' in data:
        if 'characters' in data['characterGroup']:
            for char in data['characterGroup']['characters']:
                if 'colors' in char:
                    for color_key, color_val in char['colors'].items():
                        if not isinstance(color_val, int):
                            errors.append(f"Character {char.get('id')}: {color_key} must be integer, got {type(color_val).__name__}")

    return errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate-test-json.py <json-files>")
        print("\nExample:")
        print("  python3 validate-test-json.py test-maps/*.json")
        print("  python3 validate-test-json.py test-maps/my-test.json")
        sys.exit(1)

    all_valid = True
    total_files = 0
    valid_files = 0

    for filepath in sys.argv[1:]:
        path = Path(filepath)
        if not path.exists():
            print(f"❌ {filepath}: File not found")
            all_valid = False
            continue

        total_files += 1
        errors = validate_json_file(path)

        if errors:
            print(f"❌ {filepath}:")
            for error in errors:
                print(f"   {error}")
            all_valid = False
        else:
            print(f"✓ {filepath}")
            valid_files += 1

    print(f"\n{valid_files}/{total_files} files valid")
    sys.exit(0 if all_valid else 1)

if __name__ == '__main__':
    main()

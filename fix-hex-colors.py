#!/usr/bin/env python3
"""
Auto-fix hex color notation in JSON files.
Converts 0xHEXVALUE to decimal integers.

Usage: python3 fix-hex-colors.py <json-file>
"""

import json
import sys
import re
from pathlib import Path

def fix_hex_colors(filepath, dry_run=False):
    """Convert hex colors to decimal in JSON file."""

    # Read file
    with open(filepath, 'r') as f:
        content = f.read()

    # Find all hex values
    hex_pattern = r'0x([0-9a-fA-F]+)'
    hex_matches = re.findall(hex_pattern, content)

    if not hex_matches:
        return 0, "No hex values found"

    # Convert hex to decimal
    def hex_to_dec(match):
        hex_val = match.group(1)
        dec_val = int(hex_val, 16)
        return str(dec_val)

    # Replace all hex values
    new_content = re.sub(hex_pattern, hex_to_dec, content)

    # Validate it's now valid JSON
    try:
        data = json.loads(new_content)
    except json.JSONDecodeError as e:
        return 0, f"Error: Still invalid JSON after conversion: {e}"

    if dry_run:
        return len(hex_matches), "Dry run - would convert but not saving"

    # Write back formatted JSON
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

    return len(hex_matches), "Fixed and saved"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fix-hex-colors.py <json-file> [--dry-run]")
        print("\nExample:")
        print("  python3 fix-hex-colors.py test-maps/my-test.json")
        print("  python3 fix-hex-colors.py test-maps/my-test.json --dry-run")
        sys.exit(1)

    filepath = Path(sys.argv[1])
    dry_run = '--dry-run' in sys.argv

    if not filepath.exists():
        print(f"❌ Error: File not found: {filepath}")
        sys.exit(1)

    print(f"Checking: {filepath}")

    count, message = fix_hex_colors(filepath, dry_run)

    if count > 0:
        print(f"✓ Converted {count} hex values to decimal")
        print(f"  {message}")
        if not dry_run:
            print(f"  File updated: {filepath}")
    else:
        print(f"✓ {message}")

    sys.exit(0)

if __name__ == '__main__':
    main()

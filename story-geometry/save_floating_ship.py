import json

# Read current "bridge" (actually floating ship)
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    data = json.load(f)

# Extract just the developed bridge structure
ship_voxels = [v for v in data['voxels'] 
               if v['color'] in [11184810, 9127187, 16744192]]

# Create floating ship artifact
floating_ship = {
    'name': 'Floating Ship Structure',
    'description': 'Unintentional ship-like structure from bridge development. Suspended wooden planks with torches - could be airship, floating platform, or sky vessel.',
    'category': 'artifacts',
    'voxels': ship_voxels,
    'notes': {
        'origin': 'Created 2026-01-30 during bridge development',
        'why_saved': 'Looks like floating ship rather than grounded bridge',
        'features': [
            'Wooden plank deck (3-wide)',
            'Torches at intervals (orange glow)',
            'Rope-like railings on sides',
            'Dipping/curved deck',
            'Support pillars (could be masts/rigging points)'
        ],
        'potential_uses': [
            'Airship/flying vessel',
            'Floating platform puzzle element',
            'Sky ruins',
            'Suspended walkway in different context',
            'Magic floating bridge'
        ],
        'voxel_count': len(ship_voxels),
        'colors': {
            'wood': '9127187 (brown)',
            'stone_anchors': '11184810 (gray)',
            'torches': '16744192 (orange)'
        }
    }
}

with open('story-geometry/floating-ship.json', 'w') as f:
    json.dump(floating_ship, f, indent=2)

with open('test-maps/floating-ship.json', 'w') as f:
    json.dump(floating_ship, f, indent=2)

print(f"Saved floating ship: {len(ship_voxels)} voxels")
print("Location: story-geometry/floating-ship.json")
print("Could be useful for: airships, floating platforms, sky vessels")

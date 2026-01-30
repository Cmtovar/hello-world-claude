import json

# Read bridge + forest floor
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

# Read updated ruins
with open('story-geometry/ruins-complete.json', 'r') as f:
    ruins_data = json.load(f)

# Combine voxels
combined_voxels = bridge_data['voxels'] + ruins_data['voxels']

# Create complete scene
complete_scene = {
    'name': 'Bridge at Old Fort Crossing - Complete Scene',
    'description': 'Full first map: Bridge crossing perpendicular river valley with rotated ruins on far side. Wooden hiding area at back of ruins, surrounded by grass.',
    'category': 'story-geometry',
    'playerStart': {'x': 0, 'y': 1, 'z': 0},
    'goal': {'x': 23, 'y': 2, 'z': 0},  # Updated for pushed-back ruins
    'voxels': combined_voxels,
    'notes': {
        'components': [
            'Rope bridge (X: 0-11)',
            'Forest floor valley beneath (Y: -1 to 0)',
            'Rotated ruins (X: 16-24, pushed back with grass buffer)'
        ],
        'ruins_modifications': '180° rotation, +3 X translation, added grass and rubble'
    }
}

# Write complete scene
with open('story-geometry/complete-scene.json', 'w') as f:
    json.dump(complete_scene, f, indent=2)

# Update test maps
with open('test-maps/ruins-test.json', 'w') as f:
    json.dump(ruins_data, f, indent=2)

with open('test-maps/complete-scene.json', 'w') as f:
    json.dump(complete_scene, f, indent=2)

print("Updated complete-scene.json and test maps")
print(f"Total voxels in complete scene: {len(combined_voxels)}")

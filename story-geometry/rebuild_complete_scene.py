import json

# Read updated bridge + meandering floor
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

# Read ruins (already rotated)
with open('story-geometry/ruins-complete.json', 'r') as f:
    ruins_data = json.load(f)

# Combine
combined_voxels = bridge_data['voxels'] + ruins_data['voxels']

# Create complete scene
complete_scene = {
    'name': 'Bridge at Old Fort Crossing - Complete Scene',
    'description': 'Full first map with meandering forest floor, rotated ruins, and surrounding grass. Natural environment dispersing focus.',
    'category': 'story-geometry',
    'playerStart': {'x': 0, 'y': 1, 'z': 0},
    'goal': {'x': 23, 'y': 2, 'z': 0},
    'voxels': combined_voxels,
    'notes': {
        'components': [
            'Rope bridge (X: 0-11) with meandering floor beneath',
            'Forest floor with natural sine-wave meander',
            'Rotated ruins (X: 16-24) with grass buffer',
            'Scattered grass on north/south/east sides of ruins'
        ],
        'environmental_design': 'Focus dispersed across environment, not just bridge-to-ruins pipeline',
        'total_voxels': len(combined_voxels)
    }
}

# Write files
with open('story-geometry/complete-scene.json', 'w') as f:
    json.dump(complete_scene, f, indent=2)

with open('test-maps/complete-scene.json', 'w') as f:
    json.dump(complete_scene, f, indent=2)

with open('test-maps/combined-test.json', 'w') as f:
    json.dump(bridge_data, f, indent=2)

print(f"Complete scene updated: {len(combined_voxels)} total voxels")
print(f"- Bridge + meandering floor + side grass: {len(bridge_data['voxels'])}")
print(f"- Ruins + surrounding: {len(ruins_data['voxels'])}")

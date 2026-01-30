import json

# Read bridge structure
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

# Separate bridge voxels (just structure)
bridge_voxels = [v for v in bridge_data['voxels'] 
                 if v['color'] == 11184810 or (v['color'] == 9127187 and v['y'] >= 1)]

# Read meandered river
with open('story-geometry/river-meandered.json', 'r') as f:
    river_data = json.load(f)

# Read rotated ruins
with open('story-geometry/ruins-complete.json', 'r') as f:
    ruins_data = json.load(f)

# Combine all
combined = bridge_voxels + river_data['voxels'] + ruins_data['voxels']

complete_scene = {
    'name': 'Bridge at Old Fort Crossing - Combined',
    'description': 'Bridge + meandered forest floor + rotated ruins. Ready for side grass assessment.',
    'category': 'story-geometry',
    'playerStart': {'x': 0, 'y': 1, 'z': 0},
    'goal': {'x': 23, 'y': 2, 'z': 0},
    'voxels': combined,
    'notes': {
        'components': {
            'bridge_structure': len(bridge_voxels),
            'meandered_river': len(river_data['voxels']),
            'ruins_with_buffer': len(ruins_data['voxels'])
        },
        'total_voxels': len(combined),
        'next_step': 'Assess empty spaces, then add scattered grass to ruins sides'
    }
}

with open('story-geometry/complete-scene.json', 'w') as f:
    json.dump(complete_scene, f, indent=2)

with open('test-maps/complete-scene.json', 'w') as f:
    json.dump(complete_scene, f, indent=2)

print(f"Combined scene created: {len(combined)} voxels")
print(f"  Bridge: {len(bridge_voxels)}")
print(f"  River: {len(river_data['voxels'])}")
print(f"  Ruins: {len(ruins_data['voxels'])}")

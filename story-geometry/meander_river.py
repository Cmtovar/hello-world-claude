import json
import math

# Read original bridge + floor
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    data = json.load(f)

# Separate bridge from forest floor
bridge_voxels = []
forest_floor_voxels = []

for v in data['voxels']:
    # Bridge is cobblestone or wooden planks at Y >= 1
    if v['color'] == 11184810 or (v['color'] == 9127187 and v['y'] >= 1):
        bridge_voxels.append(v)
    # Forest floor is green/brown at Y <= 0
    elif v['color'] in [2263842, 9127187] and v['y'] <= 0:
        forest_floor_voxels.append(v)
    else:
        bridge_voxels.append(v)  # Default to bridge

print(f"Bridge voxels: {len(bridge_voxels)}")
print(f"Original forest floor: {len(forest_floor_voxels)}")

# Apply meandering to forest floor voxels
meandered_floor = []

for v in forest_floor_voxels:
    x = v['x']
    z = v['z']
    y = v['y']
    
    # Add meander: shift Z based on X position (sine wave)
    z_offset = int(2 * math.sin(x * 0.6))
    
    new_z = z + z_offset
    
    meandered_floor.append({
        'x': x,
        'y': y,
        'z': new_z,
        'color': v['color']
    })

print(f"Meandered forest floor: {len(meandered_floor)}")

# Save just the meandered river for inspection
river_only = {
    'name': 'Meandered Forest Floor (Isolated)',
    'description': 'Forest floor with sine-wave meander. Sparse voxels with air gaps.',
    'category': 'story-geometry',
    'playerStart': {'x': 0, 'y': 1, 'z': 0},
    'goal': {'x': 11, 'y': 1, 'z': 0},
    'voxels': meandered_floor,
    'notes': {
        'meander_formula': 'z_offset = 2 * sin(x * 0.6)',
        'voxel_count': len(meandered_floor),
        'status': 'Isolated for review - not yet combined with bridge'
    }
}

with open('story-geometry/river-meandered.json', 'w') as f:
    json.dump(river_only, f, indent=2)

with open('test-maps/river-meandered.json', 'w') as f:
    json.dump(river_only, f, indent=2)

print("Created river-meandered.json for review")

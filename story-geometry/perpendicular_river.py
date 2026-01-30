import json
import math

# Read bridge structure
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

# Extract just bridge structure (cobblestone + planks at Y >= 1)
bridge_voxels = [v for v in bridge_data['voxels'] 
                 if v['color'] == 11184810 or (v['color'] == 9127187 and v['y'] >= 1)]

# Create perpendicular river (flows along Z axis, crosses under bridge)
# River crosses near middle of bridge (around X: 4-7)
perpendicular_river = []

# River flows from Z: -15 to Z: 15 (perpendicular to bridge)
for z in range(-15, 16):
    # River meanders slightly in X direction
    # Use sine wave to create gentle curves
    x_offset = int(1.5 * math.sin(z * 0.4))
    
    # River center is around X: 5-6 (middle of bridge)
    river_center_x = 5 + x_offset
    
    # River has width (3-5 voxels wide in X direction)
    for x_variation in [-2, -1, 0, 1, 2]:
        x = river_center_x + x_variation
        
        # Skip if overlapping bridge supports
        if (x == 0 or x == 11) and -1 <= z <= 1:
            continue
        
        # Y level varies for natural depth
        # Deeper in middle, shallower at edges
        if abs(x_variation) == 2:
            y = 0  # Edges shallower
        else:
            y = -1  # Center deeper
        
        # Sparse pattern: not every position filled
        if (x + z) % 2 == 0 or abs(x_variation) <= 1:
            # Alternate colors
            color = 2263842 if (x + z) % 3 == 0 else 9127187
            
            perpendicular_river.append({
                'x': x,
                'y': y,
                'z': z,
                'color': color
            })

print(f"Created perpendicular river: {len(perpendicular_river)} voxels")
print(f"River flows along Z axis (-15 to 15)")
print(f"River crosses bridge at X: ~5 (with meander)")

# Save isolated perpendicular river
river_only = {
    'name': 'Perpendicular Meandering River',
    'description': 'River crosses perpendicularly beneath bridge (flows along Z axis). Sparse voxels with gentle X-direction meander.',
    'category': 'story-geometry',
    'playerStart': {'x': 0, 'y': 1, 'z': 0},
    'goal': {'x': 11, 'y': 1, 'z': 0},
    'voxels': perpendicular_river,
    'notes': {
        'flow_direction': 'Perpendicular to bridge (Z axis)',
        'meander_formula': 'x_offset = 1.5 * sin(z * 0.4)',
        'river_center': 'X: ~5 (middle of bridge)',
        'width': '3-5 voxels (sparse pattern)',
        'voxel_count': len(perpendicular_river),
        'crossing_point': 'Beneath bridge center',
        'requirement': 'PERSISTENT: River must always cross nearly perpendicularly beneath bridge'
    }
}

with open('story-geometry/river-meandered.json', 'w') as f:
    json.dump(river_only, f, indent=2)

with open('test-maps/river-meandered.json', 'w') as f:
    json.dump(river_only, f, indent=2)

print("Saved perpendicular river to river-meandered.json")

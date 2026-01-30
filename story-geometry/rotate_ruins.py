import json

# Read the original ruins
with open('story-geometry/ruins-complete.json', 'r') as f:
    ruins = json.load(f)

# Rotation center (approximate center of current ruins)
center_x = 17
center_z = 0

# Translation offset (push back from bridge)
x_offset = 3

# Transform each voxel
transformed_voxels = []
for voxel in ruins['voxels']:
    old_x = voxel['x']
    old_z = voxel['z']
    
    # Rotate 180 degrees around center
    new_x = 2 * center_x - old_x
    new_z = 2 * center_z - old_z
    
    # Translate away from bridge
    new_x += x_offset
    
    transformed_voxels.append({
        'x': new_x,
        'y': voxel['y'],
        'z': new_z,
        'color': voxel['color']
    })

# Add scattered rubble on periphery (cobblestone single blocks)
rubble_positions = [
    (15, 0, -8), (18, 0, -7), (12, 0, -5),  # North periphery
    (15, 0, 8), (18, 0, 7), (22, 0, 6),     # South periphery
    (13, 0, -3), (13, 0, 2),                # West periphery
    (24, 0, -1), (24, 0, 1),                # East periphery
]

for x, y, z in rubble_positions:
    transformed_voxels.append({
        'x': x, 'y': y, 'z': z,
        'color': 11184810  # cobblestone
    })

# Add grass surrounding (green and brown pattern like forest floor)
grass_positions = [
    # Scattered around periphery
    (14, 0, -4), (14, 0, 0), (14, 0, 4),
    (15, 0, -6), (15, 0, -2), (15, 0, 3),
    (16, 0, -5), (16, 0, 2), (16, 0, 6),
    (12, 0, -2), (12, 0, 1), (13, 0, -4), (13, 0, 5),
    (23, 0, -3), (23, 0, 0), (23, 0, 3),
    (22, 0, -4), (22, 0, 2), (21, 0, -6), (21, 0, 5),
]

for x, y, z in grass_positions:
    # Check if position doesn't conflict with ruins
    if not any(v['x'] == x and v['y'] == y and v['z'] == z for v in transformed_voxels):
        # Alternate between green and brown
        color = 2263842 if (x + z) % 2 == 0 else 9127187
        transformed_voxels.append({
            'x': x, 'y': y, 'z': z,
            'color': color
        })

# Update structure
ruins['voxels'] = transformed_voxels
ruins['description'] = "Rotated 180° and pushed back from bridge. Wooden hiding area now at back. Surrounded by grass and scattered rubble."
ruins['notes']['rotation_applied'] = "180 degrees around center (17, 0)"
ruins['notes']['translation'] = "+3 in X direction (away from bridge)"
ruins['notes']['additions'] = {
    'scattered_rubble': '10 single cobblestone blocks on periphery',
    'surrounding_grass': 'Green (2263842) and brown (9127187) scattered pattern',
    'total_additions': '~30 voxels (rubble + grass)'
}

# Update structure breakdown notes
ruins['notes']['structure_breakdown']['standing_tower_base']['features'][1] = "Entry gap on west side (away from bridge)"
ruins['notes']['structure_breakdown']['standing_tower_base']['features'][4] = "Dark interior space below mezzanine at back (anomaly hiding spot)"

# Write updated ruins
with open('story-geometry/ruins-complete.json', 'w') as f:
    json.dump(ruins, f, indent=2)

print(f"Transformed {len(transformed_voxels)} voxels")
print(f"Rotation: 180° around ({center_x}, {center_z})")
print(f"Translation: +{x_offset} in X")
print(f"Added scattered rubble and grass")

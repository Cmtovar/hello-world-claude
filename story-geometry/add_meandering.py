import json
import math

# Read current bridge + forest floor
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

# Separate bridge structure from forest floor
bridge_voxels = []
forest_floor_voxels = []

for voxel in bridge_data['voxels']:
    # Bridge is cobblestone (11184810) at Y >= 1, or wooden planks at Y >= 1
    # Forest floor is at Y <= 0
    if voxel['y'] <= 0 and voxel['color'] in [2263842, 9127187]:
        forest_floor_voxels.append(voxel)
    else:
        bridge_voxels.append(voxel)

# Create meandering river/forest floor
# Current river runs Z: -15 to 15, X: roughly 2, 5, 8
meandering_floor = []

for x in range(0, 12):  # Under and around bridge
    # Meander curve: shift Z based on X position
    # Use sine wave for natural meandering
    z_offset = int(2.5 * math.sin(x * 0.7))  # Gentle meander
    
    # Vary width slightly
    width_variation = 1 if x % 4 == 0 else 0
    
    # Create vertical strips with meandering
    for z in range(-16 + z_offset, 17 + z_offset, 3):
        # Y level varies for natural elevation
        y_level = -1 if 3 <= x <= 8 else 0
        
        # Three lanes (like current pattern)
        for lane_offset in [-1, 0, 1]:
            actual_z = z + lane_offset + width_variation
            
            # Alternate colors for natural look
            color = 2263842 if (x + actual_z) % 2 == 0 else 9127187
            
            meandering_floor.append({
                'x': x,
                'y': y_level,
                'z': actual_z,
                'color': color
            })

# Add grass around sides of ruins (north and south)
# Ruins are at X: 16-24, Z: -6 to 6
side_grass = []

# North side (Z negative, beyond ruins)
for x in range(14, 26):
    for z in range(-12, -7):
        # Scattered pattern
        if (x + z) % 3 != 0:  # Not every position
            color = 2263842 if (x + z) % 2 == 0 else 9127187
            side_grass.append({'x': x, 'y': 0, 'z': z, 'color': color})

# South side (Z positive, beyond ruins)
for x in range(14, 26):
    for z in range(8, 13):
        # Scattered pattern
        if (x + z) % 3 != 0:
            color = 2263842 if (x + z) % 2 == 0 else 9127187
            side_grass.append({'x': x, 'y': 0, 'z': z, 'color': color})

# East side (beyond ruins, X positive)
for x in range(25, 28):
    for z in range(-6, 7):
        if (x + z) % 3 != 0:
            color = 2263842 if (x + z) % 2 == 0 else 9127187
            side_grass.append({'x': x, 'y': 0, 'z': z, 'color': color})

# Combine all
all_voxels = bridge_voxels + meandering_floor + side_grass

# Update bridge-over-forest-floor
bridge_data['voxels'] = all_voxels
bridge_data['description'] = "Bridge over meandering forest floor with surrounding grass"
bridge_data['notes'] = {
    'bridge': 'Rope bridge spanning X: 0-11',
    'forest_floor': 'Meandering pattern beneath bridge (sine wave)',
    'side_grass': 'Scattered grass on north, south, and east sides',
    'meander_formula': 'z_offset = 2.5 * sin(x * 0.7)'
}

with open('story-geometry/bridge-over-forest-floor.json', 'w') as f:
    json.dump(bridge_data, f, indent=2)

print(f"Added meandering to forest floor")
print(f"Total voxels: {len(all_voxels)}")
print(f"Bridge structure: {len(bridge_voxels)}")
print(f"Meandering floor: {len(meandering_floor)}")
print(f"Side grass: {len(side_grass)}")

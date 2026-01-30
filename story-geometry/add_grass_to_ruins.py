import json

# Read current ruins
with open('story-geometry/ruins-complete.json', 'r') as f:
    ruins = json.load(f)

# Current ruins voxels
ruins_voxels = ruins['voxels']

# Add scattered grass around sides (sparse with air gaps)
scattered_grass = []

# North side (Z < -6, beyond northern battlement wall)
for x in range(14, 26):
    for z in range(-12, -6):
        # Sparse pattern - not every position
        if (x * 3 + z * 7) % 4 != 0:
            continue
        
        # Alternate colors naturally
        color = 2263842 if (x + z) % 2 == 0 else 9127187
        scattered_grass.append({'x': x, 'y': 0, 'z': z, 'color': color})

# South side (Z > 6, beyond southern battlement wall)
for x in range(14, 26):
    for z in range(7, 13):
        # Sparse pattern
        if (x * 3 + z * 7) % 4 != 0:
            continue
        
        color = 2263842 if (x + z) % 2 == 0 else 9127187
        scattered_grass.append({'x': x, 'y': 0, 'z': z, 'color': color})

# East side (X > 24, beyond back of ruins)
for x in range(25, 29):
    for z in range(-8, 9):
        # Sparse pattern
        if (x * 3 + z * 7) % 4 != 0:
            continue
        
        color = 2263842 if (x + z) % 2 == 0 else 9127187
        scattered_grass.append({'x': x, 'y': 0, 'z': z, 'color': color})

# Additional sparse grass in front buffer (between bridge and ruins)
for x in range(12, 16):
    for z in range(-4, 5):
        # Very sparse
        if (x * 5 + z * 3) % 5 != 0:
            continue
        
        color = 2263842 if (x + z) % 2 == 0 else 9127187
        scattered_grass.append({'x': x, 'y': 0, 'z': z, 'color': color})

print(f"Added {len(scattered_grass)} scattered grass voxels")
print(f"  North side: ~{len([g for g in scattered_grass if g['z'] < -6])}")
print(f"  South side: ~{len([g for g in scattered_grass if g['z'] > 6])}")
print(f"  East side: ~{len([g for g in scattered_grass if g['x'] > 24])}")
print(f"  Front buffer: ~{len([g for g in scattered_grass if 12 <= g['x'] < 16])}")

# Combine with ruins
all_voxels = ruins_voxels + scattered_grass

# Update ruins file
ruins['voxels'] = all_voxels
ruins['description'] = "Rotated ruins with scattered grass on sides. Grass disperses focus across environment."
ruins['notes']['scattered_grass'] = {
    'count': len(scattered_grass),
    'pattern': 'Sparse with air gaps (not every position filled)',
    'locations': ['North side (Z < -6)', 'South side (Z > 6)', 'East side (X > 24)', 'Front buffer'],
    'colors': 'Green (2263842) and brown (9127187) alternating',
    'purpose': 'Disperse focus away from strict bridge-to-ruins pipeline'
}

with open('story-geometry/ruins-complete.json', 'w') as f:
    json.dump(ruins, f, indent=2)

with open('test-maps/ruins-test.json', 'w') as f:
    json.dump(ruins, f, indent=2)

print(f"Updated ruins: {len(all_voxels)} total voxels")
print(f"  Original ruins: {len(ruins_voxels)}")
print(f"  Scattered grass: {len(scattered_grass)}")

import json

# Fix all characters to be 2 voxels tall (not 3)
# Baby anomaly stays 1 voxel tall

characters = [
    'character-01-scholar', 'character-02-apprentice', 'character-03-youth',
    'character-04-artist', 'character-05-storyteller', 'enemy-zombie'
]

for char_name in characters:
    filepath = f'test-maps/{char_name}.json'
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    # Keep ground voxel, remove Y=0 character voxel, adjust heights
    new_voxels = []
    for v in data['voxels']:
        if v['x'] == 0 and v['y'] == 0 and v['z'] == 0:
            new_voxels.append(v)  # Ground
        elif v['x'] == 2:
            # Character voxels - make 2 tall instead of 3
            if v['y'] == 0:
                new_voxels.append(v)  # Feet/body
            elif v['y'] == 1:
                new_voxels.append(v)  # Head (was body, now head)
            # Skip Y=2 (remove top voxel)
    
    data['voxels'] = new_voxels
    data['notes']['character_height'] = '2 voxels (Y=0-1)' if 'zombie' not in char_name else '2 voxels (Y=-1 to 0) - starts submerged'
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Fixed {char_name}: 2 voxels tall")

print("\nAll characters now 2 voxels tall")
print("Baby anomaly already 1 voxel tall (correct)")

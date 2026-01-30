import json

with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

extended_bridge = []

# === EXTENDED WEST ANCHOR (X=0-1) ===
# Accounts for river meandering over time
for x in [0, 1]:
    extended_bridge.append({'x': x, 'y': 0, 'z': 0, 'color': 11184810})
    extended_bridge.append({'x': x, 'y': 0, 'z': -1, 'color': 11184810})
    extended_bridge.append({'x': x, 'y': 0, 'z': 1, 'color': 11184810})
    if x == 0:  # Taller at X=0
        extended_bridge.append({'x': x, 'y': 1, 'z': 0, 'color': 11184810})

# === EXTENDED EAST ANCHOR (X=10-11) ===
for x in [10, 11]:
    extended_bridge.append({'x': x, 'y': 0, 'z': 0, 'color': 11184810})
    extended_bridge.append({'x': x, 'y': 0, 'z': -1, 'color': 11184810})
    extended_bridge.append({'x': x, 'y': 0, 'z': 1, 'color': 11184810})
    if x == 11:  # Taller at X=11
        extended_bridge.append({'x': x, 'y': 1, 'z': 0, 'color': 11184810})

# === WALKWAY (M-SHAPE, X=2-9 now since anchors extended) ===
walkway_heights = {2: 1, 3: 2, 4: 2, 5: 1, 6: 1, 7: 2, 8: 2, 9: 1}

for x, y in walkway_heights.items():
    extended_bridge.append({'x': x, 'y': y, 'z': 0, 'color': 9127187})

# === ROPE POSTS ===
for x in [3, 5, 8]:
    y = walkway_heights[x]
    extended_bridge.append({'x': x, 'y': y, 'z': -1, 'color': 9127187})
    if y < 2:
        extended_bridge.append({'x': x, 'y': y + 1, 'z': -1, 'color': 9127187})
    extended_bridge.append({'x': x, 'y': y, 'z': 1, 'color': 9127187})
    if y < 2:
        extended_bridge.append({'x': x, 'y': y + 1, 'z': 1, 'color': 9127187})

# === TORCHES ===
torch_color = 16744192
for x in [3, 5, 8]:
    y = walkway_heights[x]
    extended_bridge.append({'x': x, 'y': y, 'z': -1, 'color': 9127187})
    extended_bridge.append({'x': x, 'y': y + 1, 'z': -1, 'color': torch_color})
    extended_bridge.append({'x': x, 'y': y, 'z': 1, 'color': 9127187})
    extended_bridge.append({'x': x, 'y': y + 1, 'z': 1, 'color': torch_color})

# === GRASS ON WEST SIDE (opposite ruins) ===
# Scattered grass for characters to stand
west_grass = [
    # Around west anchor
    (-1, 0, -2), (-1, 0, 0), (-1, 0, 2),
    (0, 0, -3), (0, 0, 3),
    (1, 0, -3), (1, 0, -2), (1, 0, 2), (1, 0, 3),
    # A bit further out
    (-2, 0, -1), (-2, 0, 1),
    (2, 0, -3), (2, 0, 3),
]

for x, y, z in west_grass:
    # Alternate green/brown
    color = 2263842 if (x + z) % 2 == 0 else 9127187
    extended_bridge.append({'x': x, 'y': y, 'z': z, 'color': color})

print(f"Extended bridge + west grass: {len(extended_bridge)} voxels")
print(f"  Extended anchors: X=0-1 (west), X=10-11 (east)")
print(f"  Walkway: X=2-9 (M-shape)")
print(f"  West grass: {len(west_grass)} voxels (standing area)")

bridge_data['voxels'] = extended_bridge
bridge_data['description'] = 'M-bridge with extended cobblestone anchors (river meandering buffer) and west-side grass for characters.'
bridge_data['notes'] = {
    'anchors_extended': 'One voxel closer to bridge ends (accounts for river shift over time)',
    'west_anchor': 'X=0-1',
    'east_anchor': 'X=10-11',
    'walkway': 'X=2-9 (M-shape)',
    'west_grass': 'Scattered grass opposite ruins (character standing area)',
    'total_voxels': len(extended_bridge)
}

with open('story-geometry/bridge-over-forest-floor.json', 'w') as f:
    json.dump(bridge_data, f, indent=2)

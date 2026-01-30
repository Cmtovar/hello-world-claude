import json

# Read bridge data
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

# Compressed M-shaped bridge (half height)
compressed_bridge = []

# === COBBLESTONE ANCHORS (ground level only) ===
# West anchor (X=0) - minimal height
compressed_bridge.append({'x': 0, 'y': 0, 'z': 0, 'color': 11184810})
compressed_bridge.append({'x': 0, 'y': 0, 'z': -1, 'color': 11184810})
compressed_bridge.append({'x': 0, 'y': 0, 'z': 1, 'color': 11184810})
compressed_bridge.append({'x': 0, 'y': 1, 'z': 0, 'color': 11184810})

# East anchor (X=11)
compressed_bridge.append({'x': 11, 'y': 0, 'z': 0, 'color': 11184810})
compressed_bridge.append({'x': 11, 'y': 0, 'z': -1, 'color': 11184810})
compressed_bridge.append({'x': 11, 'y': 0, 'z': 1, 'color': 11184810})
compressed_bridge.append({'x': 11, 'y': 1, 'z': 0, 'color': 11184810})

# === COMPRESSED M-SHAPE WALKWAY ===
# Compressed: Y = 0, 1, 2, 2, 1, 1, 2, 2, 1, 0
walkway_heights = {
    1: 0, 2: 1, 3: 2, 4: 2, 5: 1,
    6: 1, 7: 2, 8: 2, 9: 1, 10: 0
}

for x, y in walkway_heights.items():
    compressed_bridge.append({'x': x, 'y': y, 'z': 0, 'color': 9127187})

# === ROPE POSTS ===
rope_post_positions = [2, 4, 5, 7, 9]

for x in rope_post_positions:
    y = walkway_heights[x]
    compressed_bridge.append({'x': x, 'y': y, 'z': -1, 'color': 9127187})
    if y < 2:
        compressed_bridge.append({'x': x, 'y': y + 1, 'z': -1, 'color': 9127187})
    compressed_bridge.append({'x': x, 'y': y, 'z': 1, 'color': 9127187})
    if y < 2:
        compressed_bridge.append({'x': x, 'y': y + 1, 'z': 1, 'color': 9127187})

# === TORCHES ===
torch_color = 16744192
torch_positions = [(2, 1), (5, 1), (9, 1)]

for x, base_y in torch_positions:
    compressed_bridge.append({'x': x, 'y': base_y, 'z': -1, 'color': 9127187})
    compressed_bridge.append({'x': x, 'y': base_y + 1, 'z': -1, 'color': torch_color})
    compressed_bridge.append({'x': x, 'y': base_y, 'z': 1, 'color': 9127187})
    compressed_bridge.append({'x': x, 'y': base_y + 1, 'z': 1, 'color': torch_color})

print(f"Compressed: {len(compressed_bridge)} voxels, Y=0-2 (was Y=1-3)")

bridge_data['voxels'] = compressed_bridge
bridge_data['description'] = 'Compressed M-shaped rope bridge. Lower profile, M design maintained.'
bridge_data['notes']['profile'] = 'Y: 0→1→2→2→1→1→2→2→1→0'
bridge_data['notes']['total_voxels'] = len(compressed_bridge)

with open('story-geometry/bridge-over-forest-floor.json', 'w') as f:
    json.dump(bridge_data, f, indent=2)

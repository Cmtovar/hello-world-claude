import json

# Read bridge data
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

# Straight compressed M-shaped bridge
straight_bridge = []

# === WEST ANCHOR (X=0, Z=0) ===
straight_bridge.append({'x': 0, 'y': 0, 'z': 0, 'color': 11184810})
straight_bridge.append({'x': 0, 'y': 0, 'z': -1, 'color': 11184810})
straight_bridge.append({'x': 0, 'y': 0, 'z': 1, 'color': 11184810})
straight_bridge.append({'x': 0, 'y': 1, 'z': 0, 'color': 11184810})

# === EAST ANCHOR (X=11, Z=0) ===
straight_bridge.append({'x': 11, 'y': 0, 'z': 0, 'color': 11184810})
straight_bridge.append({'x': 11, 'y': 0, 'z': -1, 'color': 11184810})
straight_bridge.append({'x': 11, 'y': 0, 'z': 1, 'color': 11184810})
straight_bridge.append({'x': 11, 'y': 1, 'z': 0, 'color': 11184810})

# === WALKWAY - STRAIGHT, M-SHAPE, FULL CONNECTION ===
# X=1-10, all at Z=0, Y varies for M-shape
walkway_heights = {
    1: 0, 2: 1, 3: 2, 4: 2, 5: 1,
    6: 1, 7: 2, 8: 2, 9: 1, 10: 0
}

for x, y in walkway_heights.items():
    straight_bridge.append({'x': x, 'y': y, 'z': 0, 'color': 9127187})

# === ROPE POSTS ===
for x in [2, 5, 9]:
    y = walkway_heights[x]
    straight_bridge.append({'x': x, 'y': y, 'z': -1, 'color': 9127187})
    if y < 2:
        straight_bridge.append({'x': x, 'y': y + 1, 'z': -1, 'color': 9127187})
    straight_bridge.append({'x': x, 'y': y, 'z': 1, 'color': 9127187})
    if y < 2:
        straight_bridge.append({'x': x, 'y': y + 1, 'z': 1, 'color': 9127187})

# === TORCHES ===
torch_color = 16744192
for x in [2, 5, 9]:
    y = walkway_heights[x]
    straight_bridge.append({'x': x, 'y': y, 'z': -1, 'color': 9127187})
    straight_bridge.append({'x': x, 'y': y + 1, 'z': -1, 'color': torch_color})
    straight_bridge.append({'x': x, 'y': y, 'z': 1, 'color': 9127187})
    straight_bridge.append({'x': x, 'y': y + 1, 'z': 1, 'color': torch_color})

print(f"Straight M-bridge: {len(straight_bridge)} voxels")
print(f"Fully connected: X=0 to X=11")
print(f"M-shape: Y=0→1→2→2→1→1→2→2→1→0")

bridge_data['voxels'] = straight_bridge
bridge_data['description'] = 'Straight M-shaped rope bridge. Crosses distance to ruins. Simple and functional.'
bridge_data['notes'] = {
    'design': 'Straight bridge (perpendicular to river)',
    'profile': 'Y: 0→1→2→2→1→1→2→2→1→0 (M-shape)',
    'connection': 'X=0 to X=11 (fully connected)',
    'features': ['M-shape', 'Single plank wide', 'Rope posts', 'Torches'],
    'total_voxels': len(straight_bridge)
}

with open('story-geometry/bridge-over-forest-floor.json', 'w') as f:
    json.dump(bridge_data, f, indent=2)

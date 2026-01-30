import json

# Read bridge data
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

# Create M-shaped rope bridge (grounded, narrow, with slopes)
m_bridge = []

# === COBBLESTONE ANCHORS (ground level) ===
# West anchor (X=0)
for y in range(0, 2):
    m_bridge.append({'x': 0, 'y': y, 'z': 0, 'color': 11184810})
    if y == 0:  # Ground level wider
        m_bridge.append({'x': 0, 'y': y, 'z': -1, 'color': 11184810})
        m_bridge.append({'x': 0, 'y': y, 'z': 1, 'color': 11184810})

# East anchor (X=11)
for y in range(0, 2):
    m_bridge.append({'x': 11, 'y': y, 'z': 0, 'color': 11184810})
    if y == 0:
        m_bridge.append({'x': 11, 'y': y, 'z': -1, 'color': 11184810})
        m_bridge.append({'x': 11, 'y': y, 'z': 1, 'color': 11184810})

# === WOODEN PLANK WALKWAY (M-SHAPE PROFILE) ===
# X:  1   2   3   4   5   6   7   8   9  10
# Y:  1   2   3   3   2   2   3   3   2   1
# Profile: low → rise → peak → dip → peak → rise → low (M-shape)

walkway_heights = {
    1: 1,   # Start low (slope up begins)
    2: 2,   # Rising
    3: 3,   # Peak before dip
    4: 3,   # Peak
    5: 2,   # Center dip
    6: 2,   # Center dip
    7: 3,   # Peak after dip
    8: 3,   # Peak
    9: 2,   # Descending
    10: 1   # End low (slope down)
}

for x, y in walkway_heights.items():
    # Single plank (narrow)
    m_bridge.append({'x': x, 'y': y, 'z': 0, 'color': 9127187})

# === ROPE POSTS (at key points along M-shape) ===
# Posts at transitions and peaks
rope_post_positions = [2, 4, 5, 7, 9]

for x in rope_post_positions:
    y = walkway_heights[x]
    
    # North side post (at plank height + above)
    m_bridge.append({'x': x, 'y': y, 'z': -1, 'color': 9127187})
    m_bridge.append({'x': x, 'y': y + 1, 'z': -1, 'color': 9127187})
    
    # South side post
    m_bridge.append({'x': x, 'y': y, 'z': 1, 'color': 9127187})
    m_bridge.append({'x': x, 'y': y + 1, 'z': 1, 'color': 9127187})

# === TORCHES (at peaks and ends) ===
torch_color = 16744192

# West end (rising slope)
m_bridge.append({'x': 2, 'y': 2, 'z': -1, 'color': 9127187})
m_bridge.append({'x': 2, 'y': 3, 'z': -1, 'color': torch_color})
m_bridge.append({'x': 2, 'y': 2, 'z': 1, 'color': 9127187})
m_bridge.append({'x': 2, 'y': 3, 'z': 1, 'color': torch_color})

# Center dip
m_bridge.append({'x': 5, 'y': 2, 'z': -1, 'color': 9127187})
m_bridge.append({'x': 5, 'y': 3, 'z': -1, 'color': torch_color})
m_bridge.append({'x': 5, 'y': 2, 'z': 1, 'color': 9127187})
m_bridge.append({'x': 5, 'y': 3, 'z': 1, 'color': torch_color})

# East end (descending slope)
m_bridge.append({'x': 9, 'y': 2, 'z': -1, 'color': 9127187})
m_bridge.append({'x': 9, 'y': 3, 'z': -1, 'color': torch_color})
m_bridge.append({'x': 9, 'y': 2, 'z': 1, 'color': 9127187})
m_bridge.append({'x': 9, 'y': 3, 'z': 1, 'color': torch_color})

print(f"M-shaped bridge: {len(m_bridge)} voxels")
print(f"Profile: Y=1 → Y=2 → Y=3 → Y=2 → Y=3 → Y=2 → Y=1")
print(f"  Anchors: ~8 (grounded at Y=0)")
print(f"  Walkway: 10 (single plank, M-shape)")
print(f"  Rope posts: ~{len(rope_post_positions) * 4}")
print(f"  Torches: 12 (6 torches at key points)")

# Update bridge data
bridge_data['voxels'] = m_bridge
bridge_data['description'] = 'M-shaped rope bridge. Slopes up from each end, dips in center. Grounded and narrow.'
bridge_data['notes']['shape'] = 'M-profile when viewed from side'
bridge_data['notes']['profile'] = 'Y: 1→2→3→3→2→2→3→3→2→1 (slopes + center dip)'
bridge_data['notes']['features'] = [
    'Slopes up from anchors at both ends',
    'Peaks before and after center dip',
    'Center dip creates M-shape',
    'Single plank wide (narrow rope bridge)',
    'Grounded cobblestone anchors',
    'Rope posts at transitions',
    'Torches at slopes and center'
]
bridge_data['notes']['total_voxels'] = len(m_bridge)

with open('story-geometry/bridge-over-forest-floor.json', 'w') as f:
    json.dump(bridge_data, f, indent=2)

print("\nM-shaped bridge restored!")

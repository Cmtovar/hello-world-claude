import json

# Read bridge data structure
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

# Create grounded rope bridge (narrow, connected to ground)
grounded_bridge = []

# === COBBLESTONE ANCHOR POINTS (ground level to bridge level) ===
# West anchor (X=0) - connects to ground
for y in range(0, 3):  # Y=0 (ground) to Y=2
    grounded_bridge.append({'x': 0, 'y': y, 'z': 0, 'color': 11184810})
    if y <= 1:  # Wider base
        grounded_bridge.append({'x': 0, 'y': y, 'z': -1, 'color': 11184810})
        grounded_bridge.append({'x': 0, 'y': y, 'z': 1, 'color': 11184810})

# East anchor (X=11) - connects to ground
for y in range(0, 3):
    grounded_bridge.append({'x': 11, 'y': y, 'z': 0, 'color': 11184810})
    if y <= 1:
        grounded_bridge.append({'x': 11, 'y': y, 'z': -1, 'color': 11184810})
        grounded_bridge.append({'x': 11, 'y': y, 'z': 1, 'color': 11184810})

# === WOODEN PLANK WALKWAY (single plank wide, grounded to Y=1-2) ===
# Narrow bridge with gentle dip
for x in range(1, 11):
    # Calculate Y (slight dip in middle)
    distance_from_center = abs(x - 5.5)
    if distance_from_center < 2:
        y = 1  # Center dip (just above ground)
    else:
        y = 2  # Near anchors (higher)
    
    # Single plank (narrow bridge)
    grounded_bridge.append({'x': x, 'y': y, 'z': 0, 'color': 9127187})

# === ROPE RAILINGS (simple posts at intervals) ===
# Thin posts with rope suggested between
rope_post_positions = [2, 5, 8]  # Every ~3 blocks

for x in rope_post_positions:
    distance_from_center = abs(x - 5.5)
    if distance_from_center < 2:
        y = 1
    else:
        y = 2
    
    # North side post
    grounded_bridge.append({'x': x, 'y': y, 'z': -1, 'color': 9127187})
    grounded_bridge.append({'x': x, 'y': y + 1, 'z': -1, 'color': 9127187})  # Upper post
    
    # South side post
    grounded_bridge.append({'x': x, 'y': y, 'z': 1, 'color': 9127187})
    grounded_bridge.append({'x': x, 'y': y + 1, 'z': 1, 'color': 9127187})

# === TORCHES (at anchor points and middle) ===
torch_color = 16744192  # Orange

# West end torches
grounded_bridge.append({'x': 1, 'y': 2, 'z': -1, 'color': 9127187})  # Post
grounded_bridge.append({'x': 1, 'y': 3, 'z': -1, 'color': torch_color})  # Flame
grounded_bridge.append({'x': 1, 'y': 2, 'z': 1, 'color': 9127187})
grounded_bridge.append({'x': 1, 'y': 3, 'z': 1, 'color': torch_color})

# Middle torch (at dip)
grounded_bridge.append({'x': 5, 'y': 1, 'z': -1, 'color': 9127187})
grounded_bridge.append({'x': 5, 'y': 2, 'z': -1, 'color': torch_color})
grounded_bridge.append({'x': 5, 'y': 1, 'z': 1, 'color': 9127187})
grounded_bridge.append({'x': 5, 'y': 2, 'z': 1, 'color': torch_color})

# East end torches
grounded_bridge.append({'x': 10, 'y': 2, 'z': -1, 'color': 9127187})
grounded_bridge.append({'x': 10, 'y': 3, 'z': -1, 'color': torch_color})
grounded_bridge.append({'x': 10, 'y': 2, 'z': 1, 'color': 9127187})
grounded_bridge.append({'x': 10, 'y': 3, 'z': 1, 'color': torch_color})

print(f"Grounded bridge: {len(grounded_bridge)} voxels")
print(f"  Cobblestone anchors: ~14 (grounded Y=0-2)")
print(f"  Wooden walkway: 10 (single plank wide)")
print(f"  Rope posts: ~{len(rope_post_positions) * 4}")
print(f"  Torches: 12 (6 torches total)")
print(f"Height range: Y=0 (ground) to Y=3 (torch flames)")

# Update bridge data
bridge_data['voxels'] = grounded_bridge
bridge_data['description'] = 'Grounded rope bridge. Narrow walkway with cobblestone anchors connected to ground. Rope posts and torches.'
bridge_data['notes']['implementation_status'] = 'GROUNDED - properly connected'
bridge_data['notes']['features'] = [
    'Single plank wide walkway (narrow rope bridge)',
    'Cobblestone anchors at Y=0 (ground level)',
    'Slight dip in middle (Y=1 center, Y=2 ends)',
    'Rope posts at intervals (suggests rope railings)',
    '6 torches (west, middle, east)',
    'Connected to ground properly'
]
bridge_data['notes']['total_voxels'] = len(grounded_bridge)
bridge_data['notes']['previous_iteration'] = 'Saved as floating-ship.json (looked like airship)'

with open('story-geometry/bridge-over-forest-floor.json', 'w') as f:
    json.dump(bridge_data, f, indent=2)

print("\nGrounded bridge saved to bridge-over-forest-floor.json")

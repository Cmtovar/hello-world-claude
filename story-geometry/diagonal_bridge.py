import json

# Read bridge data
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

diagonal_bridge = []

# === DIAGONAL PATH CALCULATION ===
# Bridge angles from (X=0, Z=0) to (X=11, Z=3)
# Gentle diagonal - shifts Z gradually as X increases
def get_z_for_x(x):
    """Calculate Z position for given X (creates diagonal)"""
    # Linear interpolation: Z goes from 0 to 3 as X goes from 0 to 11
    return int((x / 11.0) * 3)

# === M-SHAPE HEIGHT PROFILE (compressed) ===
def get_y_for_x(x):
    """M-shape profile: 0→1→2→2→1→1→2→2→1→0"""
    heights = {0: 0, 1: 0, 2: 1, 3: 2, 4: 2, 5: 1, 6: 1, 7: 2, 8: 2, 9: 1, 10: 0, 11: 0}
    return heights.get(x, 0)

# === WEST ANCHOR (X=0, Z=0) ===
for z_offset in [-1, 0, 1]:
    diagonal_bridge.append({'x': 0, 'y': 0, 'z': 0 + z_offset, 'color': 11184810})
diagonal_bridge.append({'x': 0, 'y': 1, 'z': 0, 'color': 11184810})

# === EAST ANCHOR (X=11, Z=3 - end of diagonal) ===
end_z = get_z_for_x(11)
for z_offset in [-1, 0, 1]:
    diagonal_bridge.append({'x': 11, 'y': 0, 'z': end_z + z_offset, 'color': 11184810})
diagonal_bridge.append({'x': 11, 'y': 1, 'z': end_z, 'color': 11184810})

# === WALKWAY (DIAGONAL PATH WITH M-SHAPE) ===
# CRITICAL: Bridge connects FULLY from X=1 to X=10
for x in range(1, 11):
    z = get_z_for_x(x)  # Diagonal Z position
    y = get_y_for_x(x)   # M-shape height
    
    # Main plank (single wide)
    diagonal_bridge.append({'x': x, 'y': y, 'z': z, 'color': 9127187})

# === ROPE POSTS (at key points along diagonal) ===
rope_post_positions = [2, 4, 5, 7, 9]

for x in rope_post_positions:
    z = get_z_for_x(x)
    y = get_y_for_x(x)
    
    # North side post (perpendicular to bridge direction)
    diagonal_bridge.append({'x': x, 'y': y, 'z': z - 1, 'color': 9127187})
    if y < 2:
        diagonal_bridge.append({'x': x, 'y': y + 1, 'z': z - 1, 'color': 9127187})
    
    # South side post
    diagonal_bridge.append({'x': x, 'y': y, 'z': z + 1, 'color': 9127187})
    if y < 2:
        diagonal_bridge.append({'x': x, 'y': y + 1, 'z': z + 1, 'color': 9127187})

# === TORCHES (along diagonal path) ===
torch_color = 16744192
torch_positions = [2, 5, 9]

for x in torch_positions:
    z = get_z_for_x(x)
    y = get_y_for_x(x)
    
    # North torch
    diagonal_bridge.append({'x': x, 'y': y, 'z': z - 1, 'color': 9127187})
    diagonal_bridge.append({'x': x, 'y': y + 1, 'z': z - 1, 'color': torch_color})
    
    # South torch
    diagonal_bridge.append({'x': x, 'y': y, 'z': z + 1, 'color': 9127187})
    diagonal_bridge.append({'x': x, 'y': y + 1, 'z': z + 1, 'color': torch_color})

print(f"Diagonal bridge: {len(diagonal_bridge)} voxels")
print(f"Diagonal: (X=0, Z=0) → (X=11, Z=3)")
print(f"Angle: ~15° (gentle diagonal)")
print(f"M-shape: Y=0→1→2→2→1→1→2→2→1→0 (maintained)")
print(f"CONNECTED: X=1 through X=10 (no gaps)")
print(f"  Anchors: 8 voxels")
print(f"  Walkway: 10 voxels (FULLY CONNECTED)")
print(f"  Rope posts: ~{len(rope_post_positions) * 4}")
print(f"  Torches: ~{len(torch_positions) * 4}")

# Update bridge data
bridge_data['voxels'] = diagonal_bridge
bridge_data['description'] = 'Diagonal M-shaped rope bridge. Gentle angle follows river curve (not perfectly - rivers shift). Fully connected end-to-end.'

# Add persistent notes about diagonal and connection requirement
bridge_data['notes']['diagonal_design'] = {
    'start': '(X=0, Z=0)',
    'end': '(X=11, Z=3)',
    'angle': '~15 degrees (gentle)',
    'rationale': 'Better aligns to river meander, gives design flexibility',
    'historical_note': 'Bridge angle vs river - rivers shift over centuries, bridge is fixed'
}

bridge_data['notes']['CRITICAL_REQUIREMENT'] = 'Bridge MUST ALWAYS connect fully from end to end. No gaps. Covers X=0 through X=11.'

bridge_data['notes']['features'] = [
    'Gentle diagonal path (Z shifts with X)',
    'M-shape maintained (compressed heights)',
    'FULLY CONNECTED walkway (X=1-10)',
    'Anchors at both ends',
    'Single plank wide',
    'Rope posts perpendicular to bridge direction',
    'Torches at key points'
]

bridge_data['notes']['total_voxels'] = len(diagonal_bridge)

with open('story-geometry/bridge-over-forest-floor.json', 'w') as f:
    json.dump(bridge_data, f, indent=2)

print("\nDiagonal bridge created - FULLY CONNECTED from end to end!")

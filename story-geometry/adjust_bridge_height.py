import json

with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

# Extract non-walkway voxels (anchors, posts, torches, grass)
non_walkway = [v for v in bridge_data['voxels'] 
               if not (2 <= v['x'] <= 9 and v['z'] == 0 and v['color'] == 9127187)]

# New walkway profile based on interpretation:
# - 3 voxels on either side (peaks at Y=3?)
# - 2 voxels dipped in middle (Y=1, Y=1)
# - Outer ends dip 1 voxel (Y=1)
# Interpretation: X=2,9 at Y=1 (outer dip), X=3-4 rise to Y=3, X=5-6 at Y=1 (center), X=7-8 rise to Y=3

new_walkway_heights = {
    2: 1,   # Outer end dip
    3: 2,   # Rising to peak
    4: 3,   # Peak (3 voxels high area)
    5: 1,   # Center dip
    6: 1,   # Center dip
    7: 3,   # Peak (3 voxels high area)
    8: 2,   # Descending from peak
    9: 1,   # Outer end dip
}

new_walkway = []
for x, y in new_walkway_heights.items():
    new_walkway.append({'x': x, 'y': y, 'z': 0, 'color': 9127187})

# Combine
adjusted_bridge = non_walkway + new_walkway

print(f"Adjusted bridge: {len(adjusted_bridge)} voxels")
print(f"Walkway profile: Y = {[new_walkway_heights[x] for x in sorted(new_walkway_heights.keys())]}")
print(f"  Peaks at X=4,7: Y=3 (raised)")
print(f"  Center dip X=5-6: Y=1")
print(f"  Outer dips X=2,9: Y=1")

bridge_data['voxels'] = adjusted_bridge
bridge_data['notes']['walkway_profile_adjusted'] = {
    'heights': 'Y: 1→2→3→1→1→3→2→1',
    'peaks': 'X=4,7 at Y=3 (raised)',
    'center_dip': 'X=5-6 at Y=1',
    'outer_dips': 'X=2,9 at Y=1',
    'interpretation': 'Attempted from user description - may need manual tweaking'
}

with open('story-geometry/bridge-over-forest-floor.json', 'w') as f:
    json.dump(bridge_data, f, indent=2)

print("\nBridge adjusted (see BY-HAND-TODO.md for manual refinements)")

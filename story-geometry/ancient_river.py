import json
import math

# Read bridge structure
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge_data = json.load(f)

bridge_voxels = [v for v in bridge_data['voxels'] 
                 if v['color'] == 11184810 or (v['color'] == 9127187 and v['y'] >= 1)]

# Create ancient, dramatically meandering river
# This river has been here for centuries - mature curves, approaching oxbow
ancient_river = []

# River flows Z: -18 to +18 (extended range)
for z in range(-18, 19):
    # Dramatic meander using compound sine waves (more natural/ancient)
    # Primary curve + secondary variation = complex meandering
    primary_curve = 3.5 * math.sin(z * 0.25)  # Large, slow curves
    secondary_curve = 1.2 * math.sin(z * 0.6)  # Smaller variations
    x_offset = int(primary_curve + secondary_curve)
    
    # River center around X: 5 (middle of bridge)
    river_center_x = 5 + x_offset
    
    # Width varies with curve intensity (wider on outside of bends)
    # More dramatic curves = wider river (erosion over time)
    curve_intensity = abs(primary_curve)
    base_width = 5  # Base width
    curve_width = int(curve_intensity * 0.8)  # Extra width from curves
    total_half_width = base_width + curve_width
    
    # Create river width
    for x_var in range(-total_half_width, total_half_width + 1):
        x = river_center_x + x_var
        
        # Skip bridge support areas
        if (x == 0 or x == 11) and -1 <= z <= 1:
            continue
        
        # Keep river from going too far from bridge area
        if x < -2 or x > 13:
            continue
        
        # Depth variation - deeper in center, shallower at edges
        distance_from_center = abs(x_var)
        if distance_from_center > total_half_width - 2:
            y = 0  # Very shallow edges
        elif distance_from_center > total_half_width - 4:
            y = -1  # Shallow
        else:
            y = -2 if distance_from_center < 2 else -1  # Deep channel in center
        
        # Sparse pattern - not every voxel filled (natural gaps)
        # More filled in center, sparser at edges
        if distance_from_center < 3:
            fill_chance = True  # Always fill center
        elif distance_from_center < 6:
            fill_chance = (x + z) % 2 == 0  # Half filled
        else:
            fill_chance = (x + z) % 3 == 0  # Sparse edges
        
        if fill_chance:
            # Color variation - greens and browns scattered naturally
            color_choice = (x * 7 + z * 11) % 5
            if color_choice < 2:
                color = 2263842  # Green (forest vegetation)
            else:
                color = 9127187  # Brown (mud/sediment)
            
            ancient_river.append({
                'x': x,
                'y': y,
                'z': z,
                'color': color
            })

print(f"Created ancient river: {len(ancient_river)} voxels")
print(f"Dramatic meandering with compound curves")
print(f"Width varies: {base_width*2} to {(base_width + curve_width)*2} voxels")
print(f"Depth: Y=-2 to Y=0 (deep ancient channel)")

# Save isolated ancient river
river_only = {
    'name': 'Ancient Meandering River',
    'description': 'Mature river with dramatic meander, approaching oxbow stage. River existed long before bridge/ruins. Wide span beneath bridge.',
    'category': 'story-geometry',
    'playerStart': {'x': 0, 'y': 1, 'z': 0},
    'goal': {'x': 11, 'y': 1, 'z': 0},
    'voxels': ancient_river,
    'notes': {
        'age': 'Ancient - centuries old, mature meandering',
        'flow_direction': 'Perpendicular to bridge (Z axis)',
        'meander_type': 'Compound curves (primary + secondary waves)',
        'meander_formula': {
            'primary': '3.5 * sin(z * 0.25) - slow, dramatic bends',
            'secondary': '1.2 * sin(z * 0.6) - natural variation',
            'combined': 'Creates complex, ancient river pattern'
        },
        'width_system': 'Dynamic width based on curve intensity (erosion)',
        'base_width': '~10 voxels',
        'max_width': '~16 voxels (at dramatic curves)',
        'depth_variation': 'Y=-2 (deep center) to Y=0 (shallow edges)',
        'voxel_count': len(ancient_river),
        'maturity': 'Approaching oxbow stage - dramatic S-curves',
        'requirement': 'PERSISTENT: River crosses perpendicularly, looks ancient/mature'
    }
}

with open('story-geometry/river-meandered.json', 'w') as f:
    json.dump(river_only, f, indent=2)

with open('test-maps/river-meandered.json', 'w') as f:
    json.dump(river_only, f, indent=2)

print("Saved ancient river to river-meandered.json")

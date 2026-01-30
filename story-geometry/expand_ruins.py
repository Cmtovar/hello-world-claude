import json

# Read current ruins
with open('story-geometry/ruins-complete.json', 'r') as f:
    ruins = json.load(f)

existing_voxels = ruins['voxels']

# Add varied architectural artifacts extending into grass areas
artifacts = []

# North area: Fallen wall section (extends into north grass)
# Looks like part of defensive wall collapsed outward
for x in range(17, 21):
    for z in range(-9, -7):
        # Create irregular fallen wall pattern
        if x == 17 or x == 20:
            artifacts.append({'x': x, 'y': 0, 'z': z, 'color': 11184810})
            if z == -8:
                artifacts.append({'x': x, 'y': 1, 'z': z, 'color': 11184810})

# Scattered foundation stones (corners, architectural elements)
foundation_pieces = [
    # North scattered
    (15, 0, -9), (15, 1, -9),  # Corner piece
    (19, 0, -10), (20, 0, -10),  # Foundation line
    (22, 0, -8),  # Isolated stone
    
    # South scattered  
    (16, 0, 9), (16, 1, 9),  # Corner piece
    (18, 0, 10), (19, 0, 10),  # Foundation line
    (21, 0, 8), (21, 1, 8),  # Partial column base
    
    # East area: Old pathway stones
    (25, 0, -2), (25, 0, -1), (25, 0, 0), (25, 0, 1),  # Path remnant
    (26, 0, 2), (27, 0, 3),  # Scattered continuation
]

for x, y, z in foundation_pieces:
    artifacts.append({'x': x, 'y': y, 'z': z, 'color': 11184810})

# South area: Collapsed column/pillar (broken in sections)
column_base = [
    # Base of fallen column
    (17, 0, 8), (17, 0, 9),
    (17, 1, 8),  # Slightly elevated
    # Middle section (rolled/fallen)
    (18, 0, 9), (19, 0, 9),
    # Top section (separated)
    (20, 0, 10),
]

for x, y, z in column_base:
    artifacts.append({'x': x, 'y': y, 'z': z, 'color': 11184810})

# East extension: Stone bench/furniture remnants
# Suggests this was a courtyard or gathering space
bench_remnants = [
    (26, 0, -4), (27, 0, -4),  # Bench piece
    (26, 0, 4), (27, 0, 4),  # Opposite side bench
    (28, 0, 0), (28, 1, 0),  # Possible pedestal or marker
]

for x, y, z in bench_remnants:
    artifacts.append({'x': x, 'y': y, 'z': z, 'color': 11184810})

# Wooden debris scattered (old beams, structural wood)
wooden_artifacts = [
    # North area
    (16, 0, -8), (17, 0, -8),  # Fallen beam
    (21, 0, -7),  # Wood fragment
    
    # South area  
    (15, 0, 8),  # Wood piece
    (22, 0, 9), (23, 0, 9),  # Beam section
    
    # East area (near benches - suggests roof/covering)
    (26, 0, -2), (27, 0, 1),  # Scattered wood
]

for x, y, z in wooden_artifacts:
    artifacts.append({'x': x, 'y': y, 'z': z, 'color': 9127187})

# Additional wall fragments (suggests larger perimeter)
wall_fragments = [
    # Northwest corner suggestion
    (14, 0, -7), (14, 1, -7),
    (14, 0, -8),
    
    # Southwest corner suggestion  
    (14, 0, 7), (14, 1, 7),
    (15, 0, 9),
    
    # Eastern extent (back wall remnants)
    (28, 0, -5), (28, 0, 5),
    (29, 0, -3), (29, 0, 3),
]

for x, y, z in wall_fragments:
    artifacts.append({'x': x, 'y': y, 'z': z, 'color': 11184810})

print(f"Added {len(artifacts)} architectural artifacts")
print(f"  Fallen wall sections: ~15")
print(f"  Foundation stones: ~{len(foundation_pieces)}")
print(f"  Collapsed column: ~{len(column_base)}")
print(f"  Furniture remnants: ~{len(bench_remnants)}")
print(f"  Wooden debris: ~{len(wooden_artifacts)}")
print(f"  Wall fragments: ~{len(wall_fragments)}")

# Combine with existing
all_voxels = existing_voxels + artifacts

# Update ruins
ruins['voxels'] = all_voxels
ruins['description'] = "Expanded ruins with architectural artifacts. Fallen walls, columns, foundations, benches - tells story of old fort's extent."

# Update notes
ruins['notes']['expansion_artifacts'] = {
    'count': len(artifacts),
    'types': [
        'Fallen wall sections (defensive perimeter collapsed outward)',
        'Foundation stones and corner pieces',
        'Collapsed column/pillar (broken in sections)',
        'Stone furniture remnants (benches, possible courtyard)',
        'Wooden structural debris (beams, roof fragments)',
        'Perimeter wall fragments (suggests larger fort)',
        'Old pathway stones (eastern approach)'
    ],
    'purpose': 'Occupy space naturally, show fort\'s original extent, create exploration interest',
    'placement': 'Extended into north/south/east grass areas',
    'design_philosophy': 'Artifacts tell story - this was a functioning fort with courtyard, defenses, structures'
}

ruins['notes']['total_voxels'] = len(all_voxels)

with open('story-geometry/ruins-complete.json', 'w') as f:
    json.dump(ruins, f, indent=2)

with open('test-maps/ruins-test.json', 'w') as f:
    json.dump(ruins, f, indent=2)

print(f"\nUpdated ruins: {len(all_voxels)} total voxels")
print(f"  Original (structures + grass): {len(existing_voxels)}")
print(f"  New artifacts: {len(artifacts)}")

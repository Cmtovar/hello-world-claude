import json

# Update river with design reference
with open('story-geometry/river-meandered.json', 'r') as f:
    river = json.load(f)

river['notes']['design_reference'] = 'See IMPLEMENTATION-STATUS.md for design intent vs implementation'
river['notes']['design_sources'] = [
    'FIRST-MAP-NARRATIVE.md (lines 30-44)',
    'RIVER-DESIGN-PATTERN.md (requirements and baseline)'
]

with open('story-geometry/river-meandered.json', 'w') as f:
    json.dump(river, f, indent=2)

# Update ruins with design reference
with open('story-geometry/ruins-complete.json', 'r') as f:
    ruins = json.load(f)

ruins['notes']['design_reference'] = 'See IMPLEMENTATION-STATUS.md for design intent vs implementation'
ruins['notes']['design_sources'] = [
    'FIRST-MAP-NARRATIVE.md (lines 46-54)',
    'MAP-DESIGN-CONCEPTS.md (ruins architecture)'
]

with open('story-geometry/ruins-complete.json', 'w') as f:
    json.dump(ruins, f, indent=2)

# Update bridge with design reference
with open('story-geometry/bridge-over-forest-floor.json', 'r') as f:
    bridge = json.load(f)

if 'notes' not in bridge:
    bridge['notes'] = {}

bridge['notes']['design_reference'] = 'See IMPLEMENTATION-STATUS.md for design intent vs implementation'
bridge['notes']['design_sources'] = [
    'FIRST-MAP-NARRATIVE.md (lines 22-28)',
    'MAP-DESIGN-CONCEPTS.md (rope bridge details)'
]
bridge['notes']['status'] = 'MINIMAL - Needs development (see IMPLEMENTATION-STATUS.md)'
bridge['notes']['missing'] = [
    'Visible rope railings (currently only constraint data)',
    'Torches along bridge',
    'More substantial plank surface',
    'Structural supports visible from below'
]

with open('story-geometry/bridge-over-forest-floor.json', 'w') as f:
    json.dump(bridge, f, indent=2)

print("Added design references to all JSON files")

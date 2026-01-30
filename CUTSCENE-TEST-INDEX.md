# Cutscene Test Environment - Index

**Purpose:** Isolated test environments for character models, movement, and cutscene elements

**Created:** 2026-01-30

---

## How to Use

Each test map is accessible via URL parameter:
```
http://100.93.126.24:8080/?test=character-01-scholar
```

These are **separate from the complete map** - isolated blank environments for testing individual elements.

---

## Character Models (5 Total)

### Character 01 - Scholar
**File:** `test-maps/character-01-scholar.json`
**URL:** `?test=character-01-scholar`
**Description:** 3 voxels tall, dark gray robes
**Role:** Goes to library after mission
**Colors:** Brown boots, gray robes, tan skin

### Character 02 - Apprentice
**File:** `test-maps/character-02-apprentice.json`
**URL:** `?test=character-02-apprentice`
**Description:** 3 voxels tall, green tunic
**Role:** Stays with alchemist
**Colors:** Gray-brown boots, green tunic, peach skin

### Character 03 - Youth
**File:** `test-maps/character-03-youth.json`
**URL:** `?test=character-03-youth`
**Description:** 3 voxels tall (could be 2 for child)
**Role:** Plays in central square with cats/children
**Colors:** Brown-red boots, blue shirt, peach-yellow skin

### Character 04 - Artist
**File:** `test-maps/character-04-artist.json`
**URL:** `?test=character-04-artist`
**Description:** 3 voxels tall, purple-gray smock
**Role:** Draws creature from memory
**Colors:** Gray boots, purple-gray smock, tan skin

### Character 05 - Storyteller
**File:** `test-maps/character-05-storyteller.json`
**URL:** `?test=character-05-storyteller`
**Description:** 3 voxels tall, tan-yellow vest
**Role:** Goes to bar to tell tales
**Colors:** Brown boots, tan-yellow vest, pink-tan skin
**Note:** Could represent 2-3 storytellers (group)

---

## Enemy/Creature Models

### Zombie
**File:** `test-maps/enemy-zombie.json`
**URL:** `?test=enemy-zombie`
**Description:** 3 voxels tall (Y=-1 to Y=1), starts submerged
**Role:** Rises from water, hordes toward group
**Colors:** Dark green (submerged), gray-green flesh, pale head
**Behavior:** Emerges when water rises

### Baby Anomaly
**File:** `test-maps/anomaly-baby.json`
**URL:** `?test=anomaly-baby`
**Description:** 2 voxels tall (small creature)
**Role:** Triggers rain event when startled, runs away
**Colors:** Purple body (magical), light purple glow
**Effect:** Leaves purple viscous residue

---

## Environmental Effects

### Water Rising Test
**File:** `test-maps/water-rising-test.json`
**URL:** `?test=water-rising-test`
**Description:** Shows water at 3 different levels
**Colors:**
- Blue (Y=-2): Low water, zombies submerged
- Cyan (Y=-1): Water rising
- Yellow (Y=0): Flood level warning
**Purpose:** Test incremental water level animation

---

## Current Character Specs

**Height:** 3 voxels (Y=0-2)
- Y=0: Feet/boots
- Y=1: Body/torso
- Y=2: Head

**Footprint:** 1x1 (single voxel width)

**Movement:** Test path from X=2 (start) to X=5 (goal)

---

## Next Steps for Cutscene Development

### Character Refinement
- [ ] Test character movement animation
- [ ] Adjust sizes if needed (youth could be 2 voxels)
- [ ] Add more detail (arms, accessories?)
- [ ] Define color palette consistency

### Positioning System
- [ ] Define character spawn points on complete map
- [ ] Create waypoint system for cutscene paths
- [ ] Test group formations (multiple characters)

### Animation
- [ ] Walking animation (if needed)
- [ ] Zombie emerge animation
- [ ] Baby anomaly run animation
- [ ] Water rising incremental animation

### Integration
- [ ] Combine characters with complete map
- [ ] Define cutscene triggers
- [ ] Camera angles/positions
- [ ] Event sequence timing

---

## Complete Map for Reference

**File:** `story-geometry/complete-scene.json`
**URL:** `?test=complete-scene`

Use this to:
- Plan character positions
- Define cutscene paths
- Test environmental interactions
- Verify scale relationships

---

**All character models reference FIRST-MAP-NARRATIVE.md for roles and behaviors**

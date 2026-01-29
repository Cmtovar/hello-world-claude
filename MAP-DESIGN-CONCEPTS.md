# Map Design Concepts

**Date:** 2026-01-29
**Status:** Initial exploration

---

## Shift to Concrete Design

After establishing system architecture (constraints, templates, blueprint mode, etc.), we need to think about **actual maps** - what they look like, what makes them distinct, how they're composed.

---

## Geometric Structures as Reusable Patterns

### The Rope Bridge Example

**Structure:**
- Suspended line of voxels
- Constraints prevent falling off edges
- Classic suspended rope bridge aesthetic

**Detailed Geometry:**

**Support Elements:**
- Cobblestone anchor points at each end
- Vertical posts supporting rope attachment
- Onboarding ramps on both sides

**Ramp Section:**
- Angled wooden planks leading up to bridge level
- Rope railings alongside ramp (constraint: prevents walking off edge)
- Transition from ground level to bridge height

**Main Span:**
- Dipping wooden plank pattern (slight sag in middle)
- Individual planks as voxels
- Rope railings on both sides
- Suspended above gap/chasm/water

**Constraints Applied:**
```json
{
  "bridgePlanks": {
    "walkable": true,
    "climbable": false
  },
  "ropeRailings": {
    "blockMovement": true,  // Can't walk through ropes
    "preventFalling": true,  // Stops accidental falls
    "destructible": false
  },
  "cobblestoneSupports": {
    "solid": true,
    "climbable": true
  }
}
```

**Visual Detail Level:**
- Individual planks distinguishable
- Ropes visible as thin constraint volumes
- Cobblestone texture distinct from wood
- Sag/dip visible in bridge geometry

---

## Milestone: First Complete Map

### Why This Matters

**Framework for subsequent maps:**
- Establishes visual style
- Tests all systems in practice
- Creates reusable patterns
- Documents design process

**Multi-session effort:**
- Map design
- Voxel placement
- Constraint assignment
- Environmental object placement
- Testing and iteration

**Needs careful logging:**
- Design intent
- Structure catalog (bridges, buildings, etc.)
- Constraint patterns
- Lessons learned

---

## What Makes Maps Distinct?

### Visual Distinctiveness
- **Terrain type:** Forest, desert, snow, urban, underground
- **Color palette:** Greens and browns vs whites and blues
- **Architectural style:** Medieval castle vs modern city vs natural formations
- **Scale:** Intimate (10x10) vs sprawling (50x50)

### Mechanical Distinctiveness
- **Environmental hazards:** Carnivorous plants vs lava vs ice
- **Verticality:** Flat plains vs multi-tiered fortress vs canyon
- **Interactive objects:** What tools does the environment provide?
- **Mobility requirements:** Ground-only vs flight-required vs climbing-heavy

### Tactical Distinctiveness
- **Chokepoints:** Bridges, doorways, narrow passes
- **Open areas:** Where AoE becomes valuable
- **Asymmetry:** Attacker has height advantage, defender has hazards
- **Objectives:** Defend point vs reach exit vs defeat boss vs escort NPC

---

## Documentation Structure for Maps

### Proposed Format

#### 1. Map Overview
- Name
- Theme/setting
- Size (XxZ, height range)
- Difficulty level
- Required unit types
- Recommended party size

#### 2. Narrative Context
- Why are we here?
- What's the objective?
- Who are the enemies?
- What's at stake?

#### 3. Geometric Structures Catalog
- List of reusable patterns used
- Example: "Rope Bridge A" (spans 8 tiles, dips in middle)
- Example: "Watchtower B" (3-story, ladder access)
- Voxel configurations
- Constraint specifications

#### 4. Terrain Map
- Visual representation (could be ASCII, could be screenshot)
- Elevation indicators
- Key positions marked

#### 5. Environmental Objects
- Hazards (plants, geysers, etc.)
- Interactive elements (levers, doors, crates)
- Loot placements
- Enemy spawn points

#### 6. Constraint Zones
- Where special rules apply
- Example: "Bridge railings prevent falling"
- Example: "Forest canopy blocks flight"
- Example: "Sacred ground: no violence"

#### 7. Enemy Placement & Behavior
- Initial positions
- Patrol routes (if any)
- Template/AI patterns they use
- Reinforcement triggers

#### 8. Victory Conditions
- Primary objective
- Optional objectives
- Failure conditions
- Turn limits (if any)

#### 9. Design Intent
- What tactics should the player use?
- What mechanics are being taught?
- What makes this map unique?
- Intended difficulty curve

#### 10. Testing Notes
- What worked
- What didn't work
- Balance adjustments made
- Player feedback

---

## Open Questions for First Map

### Theme
- What setting? (Forest, castle, town, ruins?)
- What's the story context?
- Early game or later?

### Scope
- How large? (Recommend starting small: 15x15?)
- How many elevation levels? (2-3 for first map?)
- How many structures? (Bridge + 1-2 buildings?)

### Mechanics Focus
- What systems to showcase?
- Basic movement only?
- Or include environmental hazards?
- Template tutorial map?

### Enemy Complexity
- Simple stationary enemies?
- Patrolling enemies?
- Coordinated groups?
- Boss encounter?

---

## Rope Bridge as First Structure

### Why Start Here

**Well-defined:**
- Clear geometry (ramps, span, supports)
- Obvious constraints (railings, walkable surface)
- Visual interest (dipping planks, ropes)

**Teaches mechanics:**
- Constrained movement (can't walk off)
- Chokepoint tactics (narrow bridge)
- Height positioning (elevated span)

**Reusable:**
- Can appear in many maps
- Easy to parameterize (length, height, sag amount)
- Recognizable landmark

### Design Variations

**Simple Rope Bridge:**
- Straight span, no dip
- Basic railings
- 6-8 tiles long

**Elaborate Rope Bridge:**
- Pronounced sag in middle
- Swaying animation (future)?
- Damaged sections (gaps to jump?)
- 12+ tiles long

**Fortified Bridge:**
- Stone railings instead of rope
- Guard towers on either end
- Drawbridge section (can be raised/lowered)

---

## Next Steps

1. **Choose a theme** for first complete map
2. **Design the rope bridge** in detail (voxel placement)
3. **Build surrounding context** (what's on either side?)
4. **Place environmental objects** (if any)
5. **Test in-engine** (does it work with movement mechanics?)
6. **Document everything** (structure catalog, constraints, etc.)
7. **Iterate based on playtesting**

---

## Potential First Map Concepts

### Concept A: Forest Crossing
**Theme:** Dense forest, need to cross ravine
**Key Structure:** Rope bridge over chasm
**Hazards:** Carnivorous plants near bridge entrances
**Enemies:** Forest creatures, some flying
**Objective:** Reach opposite side, defend position
**Teaches:** Chokepoint control, hazard manipulation

### Concept B: Mountain Pass
**Theme:** Rocky mountain path, narrow bridges
**Key Structure:** Multiple rope bridges at different heights
**Hazards:** Falling rocks, strong winds (knockback)
**Enemies:** Mountain bandits, some using boulders as weapons
**Objective:** Escort NPC across treacherous path
**Teaches:** Vertical movement, environmental awareness

### Concept C: Village Raid
**Theme:** Small village being attacked
**Key Structures:** Rope bridge to village center, buildings
**Hazards:** Fire spreading, collapsing structures
**Enemies:** Raiders with varied unit types
**Objective:** Defend villagers, extinguish fires
**Teaches:** Multi-objective tactics, time pressure

---

**This document will evolve as we design the first map. Each decision should be logged here for future reference.**

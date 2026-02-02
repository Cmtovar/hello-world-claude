# Implementation Status vs Design Intent

**Purpose:** Track what's implemented vs what was designed. Prevent drift between vision and reality.

**Date Created:** 2026-01-30
**Last Updated:** 2026-01-30

---

## Design Intent Sources

1. **FIRST-MAP-NARRATIVE.md** - Story, encounter sequence, setting description
2. **MAP-DESIGN-CONCEPTS.md** - Rope bridge details, map philosophy
3. **RIVER-DESIGN-PATTERN.md** - River requirements and baseline

---

## River/Forest Floor

### Design Intent
**Source:** `FIRST-MAP-NARRATIVE.md` lines 30-44, `RIVER-DESIGN-PATTERN.md`

- Small creek/river with forest floor
- Can flood during rain event
- Perpendicular crossing beneath bridge
- Ancient, mature river (predates fort)

### Implementation Status: ✅ COMPLETE

**File:** `story-geometry/river-meandered.json`

**Implemented:**
- ✅ Perpendicular flow (Z axis) beneath bridge
- ✅ Ancient meandering (compound curves, approaching oxbow)
- ✅ Forest floor vegetation (green/brown voxels)
- ✅ Width spans area beneath bridge (10-16 voxels)
- ✅ Depth variation (Y=-2 to Y=0)
- ✅ Sparse natural pattern
- ✅ 322 voxels

**Deferred:**
- ⏳ Rising water animation (rain event mechanic)
- ⏳ Dynamic water level changes
- ⏳ Submerged zombie reveal mechanic
- ⏳ Visual water shader/material

**Notes:**
- Baseline locked (see RIVER-DESIGN-PATTERN.md regression prevention)
- Current implementation satisfies design intent for geometry
- Water mechanics deferred to game systems phase

---

## Ruins

### Design Intent
**Source:** `FIRST-MAP-NARRATIVE.md` lines 46-54, `MAP-DESIGN-CONCEPTS.md`

- Old military battlement ruins
- Standing tower base with wooden mezzanine (anomaly hiding spot)
- Collapsed tower section (climbing/elevation)
- Cobblestone and wood construction
- Cool, damp, dark spaces
- Signs of age and decay

### Implementation Status: ✅ SUBSTANTIALLY COMPLETE

**File:** `story-geometry/ruins-complete.json`

**Implemented:**
- ✅ Standing tower base (X: 14-16, wooden floor at Y=2)
- ✅ Collapsed tower (X: 18-21, platforms Y=0-4)
- ✅ Battlement walls (north/south perimeter)
- ✅ Rotated 180° (wooden hiding area at back)
- ✅ Scattered grass surrounding (dispersed focus)
- ✅ Architectural artifacts (fallen walls, columns, benches, foundations)
- ✅ Multiple elevation levels (Y=0-4)
- ✅ 256 voxels total

**Deferred:**
- ⏳ Torch placement (light sources)
- ⏳ Vegetation overgrowth (ivy, moss)
- ⏳ Ceiling/roof remnants
- ⏳ Multiple interior rooms/chambers
- ⏳ Dark space lighting (shader/ambient)

**Notes:**
- Geometry substantially complete
- Visual polish (torches, vegetation) deferred
- Functional for gameplay (platforms, hiding spots exist)

---

## Bridge

### Design Intent
**Source:** `FIRST-MAP-NARRATIVE.md` lines 22-28, `MAP-DESIGN-CONCEPTS.md`

**Detailed Description:**
- Rope bridge over small creek/river
- Cobblestone support pillars on either bank
- Wooden plank surface with **visible dip in middle**
- **Rope railings along sides**
- **Torches along bridge length**
- Spans majority of map real estate
- Well-built (suggests fort importance)

### Implementation Status: 🚧 MINIMAL (NEEDS DEVELOPMENT)

**File:** `story-geometry/bridge-over-forest-floor.json`

**Currently Implemented:**
- ✅ Cobblestone supports at ends (X=0, X=11)
- ✅ Wooden plank path (X=1-10, with Y elevation for dip)
- ✅ Basic structure (18 voxels)
- ✅ Barrier constraints in JSON (rope railings conceptual)

**Missing from Design:**
- ❌ Visible rope railings (currently only constraint data)
- ❌ Torches along bridge
- ❌ More developed plank surface (feels too minimal)
- ❌ Visual structural detail (supports, crossbeams)
- ❌ Sufficient presence (should be primary focus approaching ruins)

**Deferred:**
- ⏳ Rope sway animation
- ⏳ Dynamic constraints system
- ⏳ Full visual rope models

**Priority:** HIGH - Bridge needs development to match design intent

**Next Steps:**
1. Add visible rope railing voxels (thin line along sides)
2. Add torch objects at intervals
3. Expand plank surface (make more substantial)
4. Add structural supports visible from below
5. Ensure bridge feels well-built and important

**Design Reference:**
- See `MAP-DESIGN-CONCEPTS.md` for rope bridge philosophy
- See `FIRST-MAP-NARRATIVE.md` lines 22-28 for setting description

---

## Scene Composition

### Design Intent
**Source:** `FIRST-MAP-NARRATIVE.md` lines 9-17

- 20x20 map
- 2-3 elevation levels
- Bridge as primary structure
- Ruins on far side
- River/creek beneath

### Implementation Status: ✅ GEOMETRY COMPLETE

**File:** `story-geometry/complete-scene.json`

**Implemented:**
- ✅ Bridge (X: 0-11)
- ✅ River crossing perpendicularly (Z: -18 to 18)
- ✅ Ruins (X: 16-29, rotated and expanded)
- ✅ Multiple elevations (Y: -2 to Y: 4)
- ✅ Natural environment (scattered grass)
- ✅ 596 voxels total

**Composition Balance:**
- Bridge: 18 voxels (3%) - **NEEDS DEVELOPMENT**
- River: 322 voxels (54%)
- Ruins: 256 voxels (43%)

**Notes:**
- River and ruins are well-developed
- Bridge is underrepresented relative to design intent
- Bridge should be more prominent as "primary structure"

---

## Overall Status

### Phase 1: Geometry Foundation
**Status:** 75% Complete

- ✅ River (100% - baseline locked)
- ✅ Ruins (90% - geometry complete, polish deferred)
- 🚧 Bridge (30% - structure exists but needs development)
- ⏳ Town layout (0% - not started)

### Phase 2: Environmental Details
**Status:** 0% - Not started

- ⏳ Torches (bridge, ruins)
- ⏳ Vegetation overgrowth
- ⏳ Visual polish

### Phase 3: Game Mechanics
**Status:** 0% - Not started

- ⏳ Rain weather system
- ⏳ Rising water
- ⏳ Zombie spawn
- ⏳ Baby anomaly behavior
- ⏳ Alchemist cutscene

---

## How to Use This Document

### When Implementing
1. Check this document for current status
2. Reference design intent sources
3. Update implementation status when complete
4. Note what's deferred and why

### When Reviewing
1. Compare implementation to design intent
2. Check if deferred items are tracked
3. Verify nothing critical is missing
4. Update "Last Updated" date

### Preventing Drift
- If implementation doesn't match design, document why
- If design changes, update source documents first
- Keep this as single source of truth for status

---

**Next Focus:** Develop bridge to match design intent (rope railings, torches, structural detail)

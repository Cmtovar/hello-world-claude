# River Design Pattern - PERSISTENT REQUIREMENT

**Date Created:** 2026-01-30
**Status:** CRITICAL - This is a foundational design decision

---

## Core Requirement

**The river MUST cross nearly perpendicularly beneath the bridge.**

### Flow Direction
- **River:** Flows along Z axis (north-south)
- **Bridge:** Spans along X axis (east-west)
- **Relationship:** Perpendicular crossing

### Why This Matters

**Visual Composition:**
- Creates natural "crossroads" composition
- Bridge purpose is clear: to cross the river
- Avoids parallel alignment which would look unnatural

**Gameplay:**
- Rising water event blocks retreat path
- Forces players to higher ground (bridge)
- Creates urgency in first map encounter

**Narrative Logic:**
- Bridges cross rivers, they don't run alongside them
- Old fort placement makes sense at river crossing
- Strategic military position (control crossing point)

---

## Implementation Details

### Current Implementation (2026-01-30) - BASELINE

**⚠️ REGRESSION PREVENTION: This is the approved ancient river design. Do not regress to simpler patterns.**

**River Pattern (Ancient/Mature):**
```python
# River flows along Z axis: -18 to +18
# Crosses bridge at X: ~5 (middle of bridge)
# COMPOUND MEANDER (ancient, approaching oxbow):
#   primary_curve = 3.5 * sin(z * 0.25)    # Large, slow dramatic bends
#   secondary_curve = 1.2 * sin(z * 0.6)   # Natural variation
#   x_offset = primary_curve + secondary_curve
#
# Dynamic width (erosion-based):
#   Base: ~10 voxels
#   Max: ~16 voxels (at curve peaks)
#   Width increases with curve intensity
#
# Depth variation (ancient carved channel):
#   Y=-2: Deep center channel
#   Y=-1: Main flow area
#   Y=0: Shallow edges/banks
#
# Sparse pattern: More dense in center, sparse at edges
```

**File:** `story-geometry/river-meandered.json`

**Voxel Count:** 322 voxels (sparse with air gaps)

**Visual Characteristics:**
- Dramatic S-curves (mature meandering)
- Looks centuries old
- Approaching oxbow stage
- Natural erosion patterns
- River predates bridge/ruins

**Colors:**
- Green: 2263842 (forest floor vegetation)
- Brown: 9127187 (muddy patches)

---

## Design Constraints

### Must Maintain
1. **Perpendicular crossing** - Always Z-axis flow
2. **Sparse pattern** - Air gaps between voxels for natural look
3. **Meander** - Gentle curves, not perfectly straight
4. **Avoids bridge supports** - Don't intersect cobblestone at X=0, X=11

### Can Vary
- Exact meander formula (amplitude, frequency)
- River width (3-7 voxels acceptable)
- Depth variation pattern
- Color distribution (green/brown ratio)

---

## Anti-Patterns (DO NOT DO)

❌ **River parallel to bridge** - Makes no architectural sense
❌ **Perfectly straight river** - Looks artificial
❌ **River too wide** - Should fit under bridge span
❌ **River intersects ruins** - Ruins are on dry ground past bridge

---

## For Future Sessions

When modifying river geometry:

1. **Always check flow direction** - Must be Z-axis
2. **Verify perpendicular crossing** - River goes under bridge, not alongside
3. **Test meander limits** - Must not intersect ruins (X: 16-24)
4. **Maintain sparse pattern** - Don't fill every voxel
5. **Update this document** - If design pattern changes

---

## Related Files

- `story-geometry/river-meandered.json` - Current river geometry
- `FIRST-MAP-NARRATIVE.md` - Story context (rising water event)
- `MAP-DESIGN-CONCEPTS.md` - Overall map philosophy

---

**This is not negotiable.** The perpendicular crossing is fundamental to the map's visual composition, gameplay mechanics, and narrative logic.

If a future session considers changing this, read the "Why This Matters" section above first.

---

## Regression Prevention

**Approved Baseline:** 2026-01-30

**If you see simpler river patterns in the future:**
- ❌ Simple sine wave with small amplitude
- ❌ Width < 8 voxels
- ❌ No compound curves
- ❌ Looks "too new" or artificial

**This means regression has occurred.** Restore from this baseline.

**Test Questions:**
1. Does the river have dramatic S-curves? (Should: YES)
2. Does it look ancient/mature? (Should: YES)  
3. Does width vary with curves? (Should: YES)
4. Is it approaching oxbow stage? (Should: YES)
5. Voxel count around 300-350? (Should: YES)

If any answer is NO, check git history and restore ancient river implementation.

**Reference Commit:** [To be added after commit]


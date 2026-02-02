# By-Hand TODO Items

**Purpose:** Track manual adjustments to be made by hand later

**Created:** 2026-01-30

---

## Bridge Refinements

### Bridge Height Profile Adjustment
**Status:** Attempted automated implementation, may need manual tweaking

**Desired profile:**
- Raise rope ends (peaks) so there's 3 voxels on either side
- Leave 2 voxels dipped in the middle (center)
- Outer ends dip 1 voxel on either end

**Implementation note:** Adds ~4 voxels, removes ~2 voxels

**Files:** `story-geometry/bridge-over-forest-floor.json`

### Other Bridge Adjustments
- Fine-tune rope post positions if needed
- Adjust torch placement for better lighting
- Verify cobblestone anchor appearance

---

## Character Models (Future)

### Character Sizing
- Determine character voxel height (e.g., 2 voxels tall? 3?)
- Determine character footprint (1x1? 2x1?)
- Define basic character shape/silhouette

### Character Movement
- Test character walking animation
- Test character positioning on map
- Verify character can navigate terrain

---

## Cutscene Infrastructure (Future)

### Water Rising Effect
- Animate water level increase
- Define water voxel behavior
- Test with character positions

### Zombie Spawn
- Zombie model design
- Emerge from water animation
- Zombie movement toward characters

### Baby Anomaly
- Model design (small, distinct)
- Startle behavior
- Run away path

---

## Map Format for Cutscenes

### Complete Map Annotations
- Add character spawn points
- Add cutscene waypoints
- Add camera angles/positions
- Define event triggers

---

## Visual Polish (Deferred)

### Ruins
- Add torches to ruins
- Add vegetation overgrowth (ivy, moss)
- Additional wooden debris

### Bridge
- Visual rope models (beyond posts)
- Rope sway animation (future)
- More detailed plank texturing

### Environment
- Additional scattered details
- Atmospheric effects
- Lighting refinement

---

**Note:** Items here are either too detailed for automated implementation or better done with direct manual control.

# Deferred Features & Implementation Notes

**Purpose:** Track implementation decisions, simplified approaches, and refactoring locations for future enhancement.

**Session:** 2026-01-29 (Bridge Implementation)
**Philosophy:** Simple start → get keyframes working → refine later

---

## Bridge Implementation (first-map-bridge-only)

### What We Built (Simple Start)

**Directory Structure:**
- Created `story-geometry/` directory for story map tests
- Separate from `test-maps/` micro-tests
- Bridge is `story-geometry/first-map-bridge-only.json`

**Voxel Layout:**
- 12 units long (X: 0-11)
- Cobblestone supports at ends (gray, color: 11184810)
- Wooden plank walkway (brown, color: 9127187)
- Visible dip: Y=3 → Y=2 → Y=3 pattern
- Ramps on both ends for smooth approach

**Barrier System (Simplified):**
- Added `barriers` field to JSON format
- Simple Z-axis bounds checking in movement code
- Invisible barriers (no visual representation)
- Hard-coded logic in `checkBarriers()` function (index.html:2103-2142)

### What We Deferred

#### 1. Full Constraint System
**Current:** Simple barrier Z-axis check
**Deferred:** Complete constraint interface pattern from CONSTRAINT-INTERFACE-PATTERN.md

**Refactor Locations:**
- `index.html:2103` - `checkBarriers()` function (marked with TODO)
- `index.html:2163` - Movement code barrier check (marked with TODO)

**What Full System Would Include:**
- Constraint type taxonomy
- Directional constraints (per-face affordances)
- Constraint composition (multiple types on one object)
- Zone-based constraints (not just position-based)
- Constraint priority/conflict resolution
- Visual constraint representation
- Reusable constraint definitions

**Why Deferred:**
- Bridge only needs simple Z-axis blocking
- Full system needs multiple use cases to design properly
- Would add 2-3 hours to implementation
- Can retrofit later without breaking bridge functionality

**When to Revisit:**
- When building ruins (need vertical blocking?)
- When adding directional constraints (throne example)
- When 3+ maps need different constraint types
- When visual feedback for constraints becomes important

---

#### 2. Visual Rope Railings
**Current:** Invisible barriers
**Deferred:** Actual 3D rope meshes along bridge sides

**Implementation Notes:**
- Would use Three.js `Line` or thin `Mesh` geometry
- Color: brown/tan rope texture
- Position: Y=2.5 to Y=3.5 along bridge span
- Could use `CatmullRomCurve3` for natural rope sag

**Refactor Locations:**
- `loadTestMap()` function (index.html:1833) - add rope mesh creation
- New function: `createRopeRailing(startPos, endPos, sagAmount)`

**Why Deferred:**
- Focus on gameplay first (can you cross the bridge?)
- Visual polish comes after functional validation
- Rope meshes don't affect collision/movement
- Easy to add later without changing JSON format

**When to Revisit:**
- After bridge gameplay confirmed working
- When creating river/ruins (visual context matters)
- Before intro cutscene (visual quality becomes important)
- When implementing rope sway animation

---

#### 3. Advanced Rope Details
**Current:** Solid plank walkway, straight rope concept
**Deferred:**
- Rope sway animation (wind effect)
- Plank gaps/spacing between boards
- Rope tension/physics simulation
- Weathering effects on planks
- Texture variation (moss, wear patterns)

**Why Deferred:**
- Not needed for "keyframe" validation
- Visual polish, not functional requirement
- Would require animation system or shader work
- Can add incrementally for final polish

**When to Revisit:**
- Polish phase after all keyframes working
- When implementing weather system (rain + wind)
- If rope bridge becomes major story moment
- User feedback on visual quality

---

#### 4. Map Loading Flexibility
**Current:** Path-based loading (`?test=story-geometry/first-map-bridge-only`)
**Deferred:**
- Dedicated story map loader
- Map categorization system
- Progressive loading for large maps
- Map metadata/tagging

**Implementation Notes:**
- Currently using test map infrastructure
- Works fine for isolated geometry testing
- May need separate loading system for full story maps

**Refactor Locations:**
- `index.html:1833` - `loadTestMap()` function handles both
- `index.html:688` - URL parameter parsing

**Why Deferred:**
- Test map loader already handles paths
- No functional difference for bridge testing
- Story vs. test distinction can come later
- Simpler to keep one loading system for now

**When to Revisit:**
- When combining bridge + river + ruins into full map
- When implementing cutscenes (need scene loading)
- When story maps need different lifecycle than tests
- When adding save/load system

---

#### 5. Barrier Visual Feedback
**Current:** No indication when blocked by barrier
**Deferred:**
- Visual barrier highlight on collision
- Audio feedback (thud/rope creak)
- Camera shake or player bounce-back
- Rope railing glow/pulse when touched

**Why Deferred:**
- Functional barrier more important than feedback
- Most players won't hit barrier (path is obvious)
- Audio/visual polish phase concern
- Easy to add event hooks later

**When to Revisit:**
- User testing shows confusion about barriers
- After audio system implemented
- During UI/UX polish phase
- When implementing haptic feedback (mobile)

---

## Code Markers & TODOs

### Search for These in index.html

**TODO: REFACTOR - Simple barrier system**
- Line 2103: `checkBarriers()` function
- Marks temporary implementation
- References CONSTRAINT-INTERFACE-PATTERN.md for future design

**TODO: REFACTOR - Barrier check added**
- Line 2163: Movement code integration
- Shows where constraint system should plug in
- Currently just simple function call

### JSON Format Extensions

**Current format:**
```json
"barriers": {
  "ropeRailings": {
    "northSide": { "xMin": 1, "xMax": 10, "zLine": -0.45 },
    "southSide": { "xMin": 1, "xMax": 10, "zLine": 0.45 }
  }
}
```

**Future constraint format (deferred):**
```json
"constraints": {
  "zones": [
    {
      "type": "barrier",
      "bounds": { "xMin": 1, "xMax": 10, "zMin": -0.45, "zMax": 0.45 },
      "affordances": { "blockMovement": true, "preventFalling": true },
      "visual": { "type": "rope", "color": "#8B4513", "sag": 0.2 }
    }
  ]
}
```

---

## Technical Debt

### Low Priority
- `checkBarriers()` only handles rope railings (not generalized)
- Barrier logic duplicated for north/south sides
- No barrier type abstraction
- Hard-coded Z-axis checking

### Medium Priority
- No visual representation of constraints
- Path handling in loadTestMap could be cleaner
- Barrier data structure tied to rope bridge use case

### High Priority (Before Full Release)
- Need full constraint system for multiple map types
- Visual constraint feedback for player understanding
- Proper map categorization (test vs. story vs. final)

---

## Testing Gaps

### What We Tested
- Bridge geometry renders
- Can walk across bridge
- Barriers prevent falling off sides

### What We Didn't Test (Yet)
- Mobile touch controls on bridge
- Camera behavior on narrow bridge
- Diagonal movement at barrier edges
- Jumping/falling onto bridge from above
- Multiple units on bridge simultaneously
- Barrier behavior during auto-climb/descent

### When to Test These
- After first manual browser test confirms basics work
- Before adding river beneath (fall testing becomes important)
- Before adding enemies (multi-unit pathing matters)

---

## Lessons & Patterns

### What Worked Well

**Simple Start Philosophy:**
- Got functional bridge in ~2 hours
- Deferred visual polish appropriately
- Clear path for future enhancement
- Documented decisions for future sessions

**Directory Structure:**
- `story-geometry/` cleanly separates from micro-tests
- README explains distinction
- Easy to find and load

**Code Markers:**
- TODO comments at refactor locations
- References to design documents
- Makes technical debt visible

### What to Remember

**For River & Ruins:**
- Use same "simple start" approach
- Focus on keyframe validation
- Defer visual polish
- Document deferred features
- Mark refactor locations

**For Cutscenes:**
- Separate directory (`cutscenes/`?)
- Reuse map loading infrastructure
- Simple scripting first, polish later
- Track deferred cinematics

**For Gameplay:**
- Build on validated movement mechanics
- Simple win/lose conditions first
- Defer complex AI and tactics
- Get basic turn flow working

---

## Quick Reference: What's Next

### Immediate Next Steps (User's Roadmap)
1. ✅ Bridge (completed - this session)
2. 🔲 River beneath bridge (simple geometry)
3. 🔲 Ruins nearby (simple structures)
4. 🔲 Intro cutscene (simple dialogue)
5. 🔲 Gameplay (simple encounter)
6. 🔲 Final cutscene (simple alchemist rescue)

### After Keyframes Complete
- Review all DEFERRED items in this document
- Prioritize based on user experience impact
- Implement constraint system properly
- Add visual polish (rope meshes, animations)
- Enhance feedback systems
- User testing and iteration

---

**Last Updated:** 2026-01-29
**Next Review:** After river and ruins implemented
**Maintained By:** Claude sessions (update after each keyframe)

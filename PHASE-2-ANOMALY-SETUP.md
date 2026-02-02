# Phase 2: Add Anomaly & Rain - Implementation Guide

**Status:** Ready to begin
**Previous Phase:** Phase 1 complete (commit c457ff0)
**Goal:** Add baby anomaly character, startle moment, and rain trigger

---

## Quick Start for Next Session

1. Read this file for Phase 2 objectives
2. Review `docs/design/CUTSCENE-ACT-SEQUENCE-DECISION.md` for design context
3. Review `docs/design/FIRST-MAP-NARRATIVE.md` for anomaly behavior description
4. Implement anomaly character and behavior
5. Test at `http://100.93.126.24:8080/?test=cutscene-act-1-2-3`

---

## Phase 2 Objectives

### What to Add

1. **Baby Anomaly Character**
   - Create character definition in cutscene JSON
   - Unique appearance (different from mercenaries)
   - Spawn position in deep ruins

2. **Anomaly Behavior**
   - Spawn in wooden area of ruins
   - Wait/hide until characters approach
   - Get startled by group presence
   - Flee away from characters
   - Trigger rain reflexively (like octopus inking)

3. **Rain Event**
   - Visual rain effect (if possible)
   - Or placeholder rain trigger event
   - Atmospheric change

4. **Character Reactions**
   - Characters notice anomaly
   - Brief pause/wait actions
   - Curiosity/surprise

---

## Anomaly Character Specification

### Appearance

**Visual Design:**
- Baby creature, small and timid
- Should look different from human mercenaries
- Suggest: Different color scheme (purples, blues, otherworldly)
- Size: 3 voxels tall like mercenaries (or smaller if possible)

**Color Suggestion:**
```json
"colors": {
  "boots": 6694963,  // Purple-blue
  "body": 9055202,   // Light purple
  "head": 12648447   // Pale purple-blue
}
```

### Spawn Location

**Target Area:** Deep ruins, wooden area
**Coordinates:** Around X=17-19, Z=-6 to -8 (dark wooden ruins area)
**Y-level:** 1 (ground level)

**Spawn Timing:** Should be present from start, but hidden/inactive until triggered

---

## Anomaly Action Queue

### Suggested Behavior Sequence

```json
{
  "id": "baby-anomaly",
  "name": "Baby Anomaly",
  "role": "Mysterious creature - startles and flees",
  "startPosition": {
    "x": 18,
    "y": 1,
    "z": -7
  },
  "colors": {
    "boots": 6694963,
    "body": 9055202,
    "head": 12648447
  },
  "actionQueue": [
    {
      "type": "comment",
      "text": "Wait hidden in wooden area"
    },
    {
      "type": "wait"
    },
    {
      "type": "wait"
    },
    {
      "type": "wait"
    },
    {
      "type": "comment",
      "text": "Startle when characters approach (Act 2)"
    },
    {
      "type": "wait"
    },
    {
      "type": "comment",
      "text": "Flee away from group"
    },
    {
      "type": "move",
      "to": {"x": 19, "y": 1, "z": -8}
    },
    {
      "type": "move",
      "to": {"x": 20, "y": 1, "z": -9}
    },
    {
      "type": "move",
      "to": {"x": 21, "y": 1, "z": -10}
    },
    {
      "type": "comment",
      "text": "Exit map edge"
    }
  ]
}
```

---

## Integration with Existing Cutscene

### Where to Insert Anomaly

**File:** `test-maps/cutscene-act-1-2-3.json`

**Location in JSON:**
Add to `characterGroup.characters` array (7th character after the 6 mercenaries)

### Timing Coordination

**Act 1 (existing):**
- Mercenaries explore deep ruins
- Anomaly is hidden/waiting (multiple wait actions)
- No interaction yet

**Act 2 (existing + anomaly):**
- Characters reach deep ruins
- Anomaly gets startled (triggered by wait action timing)
- Anomaly flees
- **Rain trigger happens here** (implementation detail: may need special event)
- Characters notice and regroup (existing behavior)

**Act 3 (Phase 3 - future):**
- Zombies appear
- Characters startled
- Cutscene ends

---

## Rain Implementation Options

### Option 1: Simple Event Comment (Phase 2)
Add a comment in the anomaly's action queue:
```json
{
  "type": "comment",
  "text": "RAIN_TRIGGER"
}
```

Then implement rain visuals in Phase 4.

### Option 2: Visual Effect (If Time Permits)
- Particle system for rain
- Lighting changes (darker)
- Post-processing effects

### Option 3: Placeholder (Minimal)
Just note in documentation that rain happens here, implement visuals later.

**Recommendation:** Start with Option 1 (event comment) for Phase 2.

---

## Character Reaction Timing

### Existing Wait Actions

Characters already have wait actions in Act 2. These are perfect for:
1. Noticing the anomaly
2. Pausing in surprise
3. Watching it flee

**No changes needed to mercenary characters** - their existing wait actions align with anomaly appearance.

---

## Testing Checklist

### Visual Validation

Load `http://100.93.126.24:8080/?test=cutscene-act-1-2-3` and verify:

- [ ] Anomaly spawns in deep ruins (wooden area)
- [ ] Anomaly is visible/distinct from mercenaries
- [ ] Anomaly waits during Act 1 (doesn't move while mercs explore)
- [ ] Anomaly flees during Act 2 (when mercs are nearby)
- [ ] Anomaly movement is smooth (same animation system)
- [ ] Timing feels natural (startle → flee makes sense)
- [ ] Characters' existing wait actions work as reaction moments
- [ ] Anomaly exits scene (moves off map edge)

### Technical Validation

- [ ] JSON is valid (run `python3 -m json.tool`)
- [ ] No animation glitches
- [ ] No collision errors
- [ ] Anomaly doesn't block mercenary paths

---

## Implementation Steps

### Step 1: Add Anomaly Character (30 min)
1. Copy mercenary character structure
2. Modify colors for anomaly appearance
3. Set spawn position (X=18, Y=1, Z=-7)
4. Add to characters array

### Step 2: Script Anomaly Behavior (30 min)
1. Add wait actions (hide phase)
2. Add flee movement sequence
3. Add comments for clarity
4. Ensure timing aligns with mercenary Act 2

### Step 3: Add Rain Marker (10 min)
1. Add "RAIN_TRIGGER" comment in action queue
2. Document where rain should occur
3. Note for Phase 4 implementation

### Step 4: Test in Browser (20 min)
1. Load test URL
2. Watch full cutscene
3. Verify timing and appearance
4. Fix any issues

### Step 5: Document & Commit (10 min)
1. Update CUTSCENE-SYSTEM-STATUS.md (Phase 2 complete)
2. Update CURRENT-WORK.md
3. Commit with clear message
4. Push to GitHub

**Total Estimated Time:** 1.5-2 hours

---

## Reference Documents

**Design Context:**
- `docs/design/CUTSCENE-ACT-SEQUENCE-DECISION.md` - Event sequence and design decisions
- `docs/design/FIRST-MAP-NARRATIVE.md` - Anomaly behavior description (Act 2 section)

**Current State:**
- `docs/status/CUTSCENE-SYSTEM-STATUS.md` - Phase 1 status, Phase 2 next steps
- `test-maps/cutscene-act-1-2-3.json` - Current cutscene implementation

**Testing:**
- Test URL: `http://100.93.126.24:8080/?test=cutscene-act-1-2-3`
- Map geometry: `story-geometry/complete-scene.json`

---

## Anomaly Narrative Context

From FIRST-MAP-NARRATIVE.md:

> **Baby Anomaly Behavior:**
> - Like octopus inking when startled
> - Reflexively stokes rain
> - Runs away in panic
> - Drops item player was looking for (Phase 4)
> - Leaves purple sparkly viscous residue on item (Phase 4)

**Phase 2 Focus:** Just the startle and flee behavior. Item and residue are Phase 4.

---

## Known Considerations

### Timing Synchronization
- Anomaly must wait long enough for mercenaries to reach deep ruins
- Wait actions = ~1.5 seconds each
- Mercenaries take ~30-40 actions to reach deep ruins
- Anomaly should have ~25-30 wait actions before flee

### Spawn Position
- Must be in explored area (X=17-20, Z=-6 to -8)
- Must be visible when characters are nearby
- Wooden area = good thematic fit

### Flee Direction
- Should flee away from mercenaries
- Suggest: Move east and deeper (X increases, Z decreases)
- Exit map at edge (X=21+)

---

## Success Criteria

**Phase 2 is complete when:**
1. Anomaly character exists in cutscene
2. Anomaly appears distinct from mercenaries
3. Anomaly waits, then flees at appropriate time
4. Characters' existing reactions work naturally
5. Rain trigger point is documented
6. Cutscene tested and working
7. Documentation updated
8. Changes committed and pushed

---

## After Phase 2

**Next:** Phase 3 - Add Zombies
- Implement zombie characters
- Script zombie spawn and reveal
- Add startle moment for mercenaries
- Define cutscene end point

**Then:** Phase 4 - Polish & Effects
- Camera system
- Dialogue
- Rain visuals
- Water rising
- Lighting changes
- Item and residue details

---

**Ready to begin Phase 2!**
**Estimated completion: 1.5-2 hours**
**Previous commit: c457ff0 (Phase 1 complete)**

# Current Work: First Map Narrative - Acts 1-3 Cutscene

**Purpose:** Implement complete narrative cutscene for "The Bridge at Old Fort Crossing"
**Usage:** Multi-phase implementation plan (Phases 1-4)
**Started:** 2026-02-01
**Owner:** Claude Sonnet 4.5
**Target Completion:** 2026-02-03 (3-4 day effort across 4 phases)

---

## Goal (One Sentence)

Create the Acts 1-3 narrative cutscene where the mercenary squad crosses the bridge, encounters a baby anomaly, and retreats from emerging zombies.

---

## Multi-Phase Implementation Plan

### Phase 1: Static Choreography ⭐ CURRENT PHASE
**Goal:** Characters move through Acts 1-3 on real terrain (no special effects yet)

**Work Units:**
1. Define 5-6 mercenary characters with colors and starting positions
2. Script action queues for Act 1 (cross bridge from near side, enter ruins)
3. Script action queues for Act 2 (regroup when anomaly appears)
4. Script action queues for Act 3 (retreat across bridge)
5. Test choreography on complete-scene.json

**Deliverables:**
- [ ] `test-maps/cutscene-act-1-2-3.json` with characterGroup defined
- [ ] All characters cross bridge successfully
- [ ] Characters explore ruins naturally
- [ ] Characters retreat back across bridge
- [ ] Visual validation at http://100.93.126.24:8080/?test=cutscene-act-1-2-3

**Estimated:** 2-3 hours

---

### Phase 2: Add Anomaly
**Goal:** Baby anomaly appears, startles, and runs away

**Work Units:**
1. Create baby anomaly character model (simple 3-voxel or special appearance)
2. Script anomaly spawn position (inside ruins, wooden hiding area)
3. Script anomaly movement (runs away when characters approach)
4. Add "startle moment" (characters stop/react, anomaly flees)
5. Test anomaly interaction timing

**Deliverables:**
- [ ] Baby anomaly character defined
- [ ] Anomaly appears in Act 2
- [ ] Characters have "react" moment (wait actions)
- [ ] Anomaly exits scene
- [ ] Visual validation

**Estimated:** 1-2 hours

---

### Phase 3: Add Zombies
**Goal:** Zombies emerge from water and chase group

**Work Units:**
1. Create zombie character models (3-4 zombies)
2. Script zombie spawn positions (river/forest floor area)
3. Script zombie movement toward group
4. Coordinate group retreat with zombie pursuit
5. Test chase sequence pacing

**Deliverables:**
- [ ] 3-4 zombie characters defined
- [ ] Zombies spawn in Act 3
- [ ] Zombies move toward group
- [ ] Group retreat feels urgent but manageable
- [ ] Visual validation

**Estimated:** 2-3 hours

---

### Phase 4: Polish & Effects (Future)
**Goal:** Add camera, dialogue, weather, and lighting

**Features (Deferred):**
- Camera system (follow action, cinematic angles)
- Dialogue system (character speech, text display)
- Rain effects (particles, lighting changes)
- Water rising animation (voxel color transitions)
- Torch lighting (point lights)
- Atmospheric darkness (ruins interior)

**Estimated:** 4-6 hours (separate work session)

---

## Definition of Done (Phase 1)

**Completion Criteria:**
- [ ] 5-6 mercenary characters defined with unique colors
- [ ] Characters start on near side of bridge (X=0-2 range)
- [ ] Act 1: All characters cross bridge and enter ruins
- [ ] Act 2: Characters regroup in ruins area
- [ ] Act 3: Characters retreat back across bridge to near side
- [ ] No collisions or terrain errors during choreography
- [ ] Smooth animations throughout (1s per action)
- [ ] Tested in browser at http://100.93.126.24:8080/?test=cutscene-act-1-2-3
- [ ] Documented in CUTSCENE-SYSTEM-STATUS.md
- [ ] Committed with "Phase 1: Acts 1-3 Static Choreography - Complete"

**Visual/Functional Test:**
Load `http://100.93.126.24:8080/?test=cutscene-act-1-2-3` and watch:
- Characters cross bridge naturally (some may use different paths)
- Characters explore ruins without errors
- Characters retreat back safely
- No stuck characters or animation glitches

---

## Scope Definition

**IN Scope (Phase 1):**
- Character definitions (5-6 mercenaries)
- Action queue choreography for Acts 1-3
- Movement on complete-scene.json terrain (bridge + ruins + river)
- Basic exploration and retreat patterns
- Using existing movement system (walk, auto-climb, gravity)

**OUT of Scope (Deferred to Later Phases):**
- Baby anomaly (Phase 2)
- Zombies (Phase 3)
- Camera control (Phase 4)
- Dialogue system (Phase 4)
- Rain/weather effects (Phase 4)
- Water rising animation (Phase 4)
- Lighting changes (Phase 4)
- Sound/audio (Phase 4)

**Why deferred:** Incremental complexity. Prove basic choreography works on real terrain before adding interactive elements.

---

## Current Phase 1 Work Units

### Unit 1: Define Mercenary Characters
**What:** Create 5-6 character definitions with colors, names, starting positions
**Output:** Character array in cutscene-act-1-2-3.json
**Estimated:** 30 min
**Status:** 🔲 Not started

### Unit 2: Script Act 1 - Bridge Crossing
**What:** Action queues for crossing bridge from near side (X=0-2) to far side (X=11-13)
**Output:** Action queues in character definitions
**Estimated:** 30 min
**Status:** 🔲 Not started

### Unit 3: Script Act 1 - Ruins Exploration
**What:** Action queues for entering ruins, exploring different areas
**Output:** Extended action queues
**Estimated:** 30 min
**Status:** 🔲 Not started

### Unit 4: Script Act 2 - Regrouping
**What:** Action queues for characters to regroup (prepare for anomaly)
**Output:** Extended action queues
**Estimated:** 20 min
**Status:** 🔲 Not started

### Unit 5: Script Act 3 - Retreat
**What:** Action queues for retreat back across bridge to safety
**Output:** Extended action queues
**Estimated:** 30 min
**Status:** 🔲 Not started

### Unit 6: Test and Refine
**What:** Load in browser, fix collisions/timing, polish choreography
**Output:** Working cutscene
**Estimated:** 30 min
**Status:** 🔲 Not started

**Total Estimated Time:** ~3 hours

---

## Progress Tracking

**Current Unit:** 1 of 6 (Phase 1)

**Commits Made:**
- [ ] (none yet)

**Blockers/Questions:**
- None currently

---

## Integration Points

**Files This Will Create:**
- `test-maps/cutscene-act-1-2-3.json` - Main cutscene test file

**Files This Will Modify:**
- `docs/status/CUTSCENE-SYSTEM-STATUS.md` - Update with Test 03 status
- `START-HERE.md` - Update recent work section
- `docs/status/IMPLEMENTATION-STATUS.md` - Update cutscene progress

**Dependencies:**
- Depends on: Complete-scene.json terrain (✅ exists)
- Depends on: Cutscene system infrastructure (✅ complete)
- Enables: Phase 2 (anomaly), Phase 3 (zombies), Phase 4 (polish)

**Tests:**
- Test file: `test-maps/cutscene-act-1-2-3.json`
- Test URL: `http://100.93.126.24:8080/?test=cutscene-act-1-2-3`
- Validation: Visual choreography check (smooth movement, no errors)

---

## Documentation Updates Required

**On Phase 1 Completion:**
- [ ] Update `docs/status/CUTSCENE-SYSTEM-STATUS.md` - Add Test 03 Phase 1 status
- [ ] Update `START-HERE.md` - Add to "Recent Work" section
- [ ] Update `docs/status/IMPLEMENTATION-STATUS.md` - Mark cutscene Acts 1-3 Phase 1 complete

**On All Phases Complete:**
- [ ] Create `docs/sessions/SESSION-2026-02-01.md` - Document full implementation
- [ ] Delete `CURRENT-WORK.md`

---

## Session Notes

**2026-02-01 20:55:**
- Session initialized
- Verified cutscene system committed (489456c)
- Analyzed narrative requirements from FIRST-MAP-NARRATIVE.md
- Identified immediate blockers vs deferred features
- Created multi-phase plan (4 phases)
- Documented plan in CURRENT-WORK.md
- **Next:** Begin Phase 1, Unit 1 - Define mercenary characters

---

## Design Reference

**Narrative Source:** `docs/design/FIRST-MAP-NARRATIVE.md`
**Terrain Source:** `story-geometry/complete-scene.json` (596 voxels)
**Character Models:** Based on `test-maps/cutscene-test-02-complex.json` patterns

**Key Narrative Moments:**
- **Act 1:** Peaceful crossing and exploration (establish characters, setting)
- **Act 2:** Baby anomaly startles group (inciting incident, triggers rain)
- **Act 3:** Zombies rise from water (escalation, test blueprint basics)

**Phase 1 Focus:** Prove characters can navigate real terrain smoothly before adding special effects.

---

## Completion Checklist (Phase 1)

**Before marking Phase 1 complete:**
- [ ] All 6 work units completed
- [ ] Cutscene tested and working
- [ ] No animation glitches or stuck characters
- [ ] Documentation updated
- [ ] Committed with Phase 1 completion message
- [ ] Ready to begin Phase 2

---

**STATUS: Phase 1 in progress - Unit 1 starting**

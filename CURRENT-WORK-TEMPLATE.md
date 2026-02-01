# Current Work Template

**Purpose:** Define feature scope BEFORE starting work
**Usage:** Copy to `CURRENT-WORK.md` when starting feature, delete when complete
**Required By:** AI-AGENT-CONDUCT.md Rule 6

---

## [Feature Name]

**Started:** [DATE]
**Owner:** Claude Sonnet 4.5
**Target Completion:** [DATE] (1-3 days from start)

---

### Goal (One Sentence)

[What this feature accomplishes in one clear sentence]

---

### Definition of Done

**Completion Criteria:**
- [ ] [Specific deliverable 1 - be concrete]
- [ ] [Specific deliverable 2 - be concrete]
- [ ] [Specific deliverable 3 - be concrete]
- [ ] Tested in browser/script execution
- [ ] Documented in relevant .md file(s)
- [ ] Committed with completion message
- [ ] Pushed to GitHub

**Visual/Functional Test:**
[How to verify this works - URL, command, or visual check]

---

### Scope Definition

**IN Scope:**
- [What we ARE building]
- [What we ARE building]
- [What we ARE building]

**OUT of Scope (Deferred):**
- [What we're NOT building now]
- [What we're NOT building now]
- [What we're NOT building now]

**Why deferred:** [Reason - complexity, dependencies, MVP priority]

---

### Work Units (3-7 expected)

Break feature into commit-sized units (~30-60min each):

1. **[Unit 1 Name]**
   - What: [What gets built]
   - Output: [Files changed]
   - Commit: WIP or completion

2. **[Unit 2 Name]**
   - What: [What gets built]
   - Output: [Files changed]
   - Commit: WIP or completion

3. **[Unit 3 Name]**
   - What: [What gets built]
   - Output: [Files changed]
   - Commit: WIP or completion

[Add more as needed]

---

### Progress Tracking

**Commits Made:**
- [ ] [hash] - WIP: [description]
- [ ] [hash] - WIP: [description]
- [ ] [hash] - [Feature] - Complete

**Current Unit:** [X of Y]

**Blockers/Questions:**
- [Any blockers or open questions]
- [Add as discovered]

---

### Integration Points

**Files This Will Modify:**
- [file1.html] - [what changes]
- [file2.json] - [what changes]
- [file3.md] - [documentation updates]

**Dependencies:**
- Depends on: [other features if any]
- Enables: [what this unlocks]

**Tests:**
- Test file: [if creating new test]
- Test URL: [if browser test]
- Validation: [if script validation]

---

### Documentation Updates Required

**On Completion:**
- [ ] Update START-HERE.md "What Was Just Accomplished"
- [ ] Update IMPLEMENTATION-STATUS.md [section]
- [ ] Update [FEATURE]-STATUS.md (if exists)
- [ ] Add/update test in CUTSCENE-TEST-INDEX.md or TEST-INDEX.md

---

### Session Notes (Update as you work)

**[DATE TIME]:**
[What was accomplished this session]
[Current state]
[Next step]

**[DATE TIME]:**
[What was accomplished this session]
[Current state]
[Next step]

---

### Completion Checklist

**Before marking complete:**
- [ ] All work units committed
- [ ] Feature tested and working
- [ ] Documentation updated
- [ ] CURRENT-WORK.md deleted
- [ ] START-HERE.md updated
- [ ] Pushed to GitHub

---

## Example: Bridge Rope Railings

**Started:** 2026-02-01
**Target Completion:** 2026-02-02

### Goal
Add visible rope railings to bridge sides to match design intent and enhance visual presence.

### Definition of Done
- [ ] 48 voxels for rope railings generated (both sides, Y=2-3)
- [ ] Railings visible in browser at http://100.93.126.24:8080/?test=complete-scene
- [ ] Bridge presence increased from 3% to ~8% of scene composition
- [ ] IMPLEMENTATION-STATUS.md bridge section updated from 🚧 to ✅
- [ ] Tested traversability (player can walk across bridge)
- [ ] Committed with "Bridge Rope Railings - Complete" message

**Visual Test:** Load complete-scene, verify rope railings visible along bridge sides

### Scope
**IN Scope:**
- Generate railing voxels along X=0-11, Z=±1, Y=2-3
- Use wood color (10902848) to match plank surface
- Update story-geometry/bridge-over-forest-floor.json

**OUT of Scope:**
- Rope physics/sway animation (deferred to weather system)
- Torch placement (separate feature)
- Structural crossbeams (deferred to polish phase)

**Why deferred:** MVP focuses on static geometry, visual polish later

### Work Units
1. **Generate Railing Pattern**
   - Create Python script or manual JSON
   - Output: 48 voxel definitions
   - Commit: WIP

2. **Update Bridge JSON**
   - Add railings to bridge-over-forest-floor.json
   - Validate with validate-test-json.py
   - Commit: WIP

3. **Test and Visual Verification**
   - Load in browser
   - Check alignment and appearance
   - Commit: Completion

### Progress Tracking
**Current Unit:** 0 of 3
**Commits Made:** (none yet)

### Integration Points
**Files:**
- story-geometry/bridge-over-forest-floor.json (+48 voxels)
- IMPLEMENTATION-STATUS.md (bridge section)
- START-HERE.md (What Was Just Accomplished)

**Tests:**
- URL: http://100.93.126.24:8080/?test=complete-scene
- Validation: python3 validate-test-json.py story-geometry/bridge-over-forest-floor.json

### Documentation Updates
- [ ] IMPLEMENTATION-STATUS.md bridge status 🚧 → ✅
- [ ] START-HERE.md add bridge railings to accomplishments
- [ ] Delete CURRENT-WORK.md

---

**Copy this template to CURRENT-WORK.md and customize for your feature**

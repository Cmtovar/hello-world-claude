# Common Issues & Solutions

**Purpose:** Document known problems and their ACTUAL solutions (not workarounds).

**Date Created:** 2026-01-29
**Last Updated:** 2026-01-29

---

## 1. Story-Geometry Maps Don't Load (404 Error)

### Problem
URL parameters with paths like `?test=story-geometry/first-map-bridge-only` fail with 404 error in browser console.

### Symptoms
- Main game loads fine
- Browser shows: "Failed to load resource: the server responded with a status of 404"
- Console error: "Failed to load test map"
- Map falls back to default procedural terrain

### Root Cause
The `loadTestMap()` function DOES support paths (checks for `/` in mapName), but something in the fetch or URL construction fails for story-geometry paths.

**Code location:** `index.html` line ~1838
```javascript
const mapPath = mapName.includes('/') ? mapName : `test-maps/${mapName}`;
const response = await fetch(`${mapPath}.json`);
```

### Current Workaround
Copy story-geometry maps to `test-maps/` directory with simpler names:
```bash
cp story-geometry/first-map-bridge-only.json test-maps/bridge-test.json
```
Then load with: `?test=bridge-test`

### Actual Solution Needed
**Status:** Not yet implemented

**Likely fixes:**
1. Browser might be treating `story-geometry/` as directory traversal (security)
2. Fetch might need relative path prefix (`./story-geometry/...`)
3. Server configuration issue (check if serving subdirectories correctly)

**To diagnose:**
- Check browser Network tab for exact URL being requested
- Test if `fetch('./story-geometry/first-map-bridge-only.json')` works
- Check server logs for 404 details

**To fix:**
- Try adding `./` prefix: `const response = await fetch(\`./${mapPath}.json\`);`
- OR encode the path: `encodeURIComponent(mapPath)`
- OR restrict to test-maps and move all maps there

**Impact:** Medium - workaround exists but requires file duplication

---

## 2. Manual Mode Doesn't Simulate Gravity

### Problem
Test preview "Play Manual" mode doesn't make player fall when walking off edges or spawning in air.

### Symptoms
- Animation mode (Run Animation) shows falling correctly
- Manual mode: player floats in air instead of falling
- Gravity works fine in main game

### Root Cause
Manual play mode handles keyboard input but doesn't call gravity simulation.

**Code location:** Manual mode input handler (search for "manualPlayMode" in index.html)

### Current Workaround
Use "Run Animation" mode for gravity tests instead of manual mode.

### Actual Solution Needed
**Status:** Deferred (documented in DEFERRED-FEATURES.md)

**Fix:** Add `await simulatePreviewGravity()` call in manual mode movement loop

**Impact:** Low - animation mode works, only affects manual testing

---

## 3. JSON Comments Cause Silent Parse Failures

### Problem
Adding JavaScript-style `//` comments to JSON files causes silent parsing failures.

### Symptoms
- Map loads default terrain instead of test map
- No error in console (fails silently)
- JSON looks correct but doesn't work

### Root Cause
JSON spec doesn't support comments. `JSON.parse()` fails silently in async context.

**Code location:** `index.html` line ~1837
```javascript
const config = await response.json(); // Fails silently if JSON invalid
```

### Solution
**NEVER use comments in JSON files.**

Use `notes` field instead:
```json
{
  "voxels": [
    {"x": 0, "y": 0, "z": 0, "color": 11184810}
  ],
  "notes": {
    "structure": "Cobblestone support at left end"
  }
}
```

**Prevention:**
- Validate JSON after editing: `cat file.json | python -m json.tool`
- Add git pre-commit hook to validate all .json files

**Impact:** High - causes silent failures

---

## 4. [Template for Future Issues]

### Problem
[Brief description]

### Symptoms
- [What user sees]
- [Console errors]
- [Unexpected behavior]

### Root Cause
[Technical explanation]
**Code location:** [File and line number]

### Current Workaround
[Temporary solution if exists]

### Actual Solution
**Status:** [Not implemented / Implemented / Deferred]
[Permanent fix description]

**Impact:** [High / Medium / Low]

---

## How to Use This Document

### When You Hit a Problem
1. Check if it's listed here first
2. Try the workaround if available
3. If new issue: document it using template above

### When Implementing Fixes
1. Update "Actual Solution" section
2. Change status to "Implemented"
3. Add git commit hash
4. Keep workaround for historical reference

### When Adding Code Comments
For issues with code locations, add inline comments:
```javascript
// KNOWN ISSUE: Story-geometry paths fail (see COMMON-ISSUES.md #1)
// TODO: Add ./ prefix or restrict to test-maps
const mapPath = mapName.includes('/') ? mapName : `test-maps/${mapName}`;
```

---

## Issue Priority

**High Priority (Fix ASAP):**
- JSON comments (#3) - causes silent failures
- Story-geometry loading (#1) - affects workflow

**Medium Priority (Fix when convenient):**
- Manual mode gravity (#2) - workaround exists

**Low Priority (Defer):**
- [None currently]

---

**Maintained by:** Claude sessions + user feedback
**Review:** After each major feature implementation

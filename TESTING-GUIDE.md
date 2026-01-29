# Testing Guide: Quality Control Checklist

**Purpose:** Validate that all test infrastructure works correctly before building more mechanics.

## Test 1: Menu Loads Correctly

**Steps:**
1. Open `http://100.93.126.24:8080/`
2. Menu should appear automatically
3. Background should show rotating terrain

**Expected:**
- ✓ Menu overlay visible
- ✓ Multiple test cards displayed
- ✓ "Descend 1 Block" card shows green (implemented) + blue (tested) borders
- ✓ Camera slowly rotates in background
- ✓ Menu scrolls on mobile

**Debug:**
- Open browser console (F12)
- Check for JavaScript errors
- Verify `mechanics-graph.json` loads

---

## Test 2: Preview Modal Opens

**Steps:**
1. Click "Descend 1 Block" card
2. Preview modal should open

**Expected:**
- ✓ Modal appears with test details
- ✓ 3D preview shows:
  - Gray platform (voxel at y=1)
  - Green base (voxel at y=0)
  - Red player cone at y=2
  - Green wireframe goal sphere at y=1
- ✓ Camera rotates around scene
- ✓ Two buttons: "▶ Run Animation" and "🎮 Play Manually"

**Debug:**
- Console should show: "Loading test map: {config}"
- Check if `testDescendOneBlock.json` loads
- Verify 3D rendering works

---

## Test 3: Animation Playback Works

**Steps:**
1. With preview modal open
2. Click "▶ Run Animation"
3. Watch the animation

**Expected:**
- ✓ Status bar appears: "Starting at position (0, 2, 0)"
- ✓ After 1 second: "Animation: Pressing Shift... (1/1)"
- ✓ Player cone moves down from y=2 to y=1
- ✓ Status changes to: "Moved from y=2 to y=1"
- ✓ Final status: "✓ Test Passed! Reached (0, 1, 0)" (green background)
- ✓ Buttons re-enable after 3 seconds

**Debug Console Output:**
```
=== Test Animation Starting ===
Start position: {x: 0, y: 2, z: 0}
Goal position: {x: 0, y: 1, z: 0}
Terrain voxels: ["0,0,0", "0,1,0", "-1,0,0", "1,0,0", "0,0,-1", "0,0,1"]
Simulating Shift at position (0, 2, 0)
Descending from 2 to 1 (standing on voxel at 0)
Final position: {x: 0, y: 1, z: 0}
Distance to goal: 0.00, Tolerance: 1.00, Success: true
=== Test Animation Complete ===
```

**If Test Fails:**
- Check "Distance to goal" in console
- Verify terrain voxels include "0,0,0" (base)
- Confirm descent logic triggers

---

## Test 4: Manual Play Mode Works

**Steps:**
1. With preview modal open
2. Click "🎮 Play Manually"
3. Press Shift key on keyboard

**Expected:**
- ✓ Button changes to "⏹ Stop Manual Mode"
- ✓ Status bar: "🎮 Manual Mode: Use Space (climb) and Shift (descend) keys"
- ✓ Camera stops rotating, focuses on player
- ✓ Pressing Shift: Player moves down from y=2 to y=1
- ✓ Status updates: "✓ Goal Reached! 🎉" (green background)
- ✓ Goal marker brightens (opacity = 1.0)

**Debug Console:**
```
Manual play mode enabled
Descended to 1
```

**Stop Manual Mode:**
- Click "⏹ Stop Manual Mode"
- Status bar disappears
- Camera resumes rotating
- Button resets to "🎮 Play Manually"

---

## Test 5: Close and Reopen

**Steps:**
1. Click X button on preview modal
2. Modal closes
3. Click "Descend 1 Block" again
4. Modal reopens

**Expected:**
- ✓ Modal closes cleanly
- ✓ Manual mode stops if active
- ✓ Reopening resets player to start position
- ✓ Animation can be run again

---

## Test 6: Direct Test URL

**Steps:**
1. Navigate to `http://100.93.126.24:8080/?test=testDescendOneBlock`
2. Should load test map in main game

**Expected:**
- ✓ Menu hidden automatically
- ✓ Test map loads (2-block pillar)
- ✓ Player spawns at (0, 2, 0)
- ✓ Green goal marker at (0, 1, 0)
- ✓ UI shows position
- ✓ Can press Shift to descend
- ✓ Main game controls work (WASD, camera)

**Debug:**
- Console: "Test mode enabled: testDescendOneBlock"
- Verify `window.game.testConfig` is set
- Check `window.isPlayerAtGoal()` function exists

---

## Known Issues to Check

### Issue: Animation doesn't move player
**Symptoms:** Player stays at y=2 after animation
**Debug:**
- Check console for "Cannot descend: no voxel at X"
- Verify `game.previewTerrain` contains voxels
- Ensure `hasPreviewVoxel(0, 0, 0)` returns true

### Issue: Manual mode keys don't work
**Symptoms:** Pressing Shift/Space does nothing
**Debug:**
- Verify keyboard listeners added: check console for "Manual play mode enabled"
- Try clicking inside preview canvas first (focus)
- Check `game.manualPlayMode` is true

### Issue: Goal never reached
**Symptoms:** Distance always > tolerance
**Debug:**
- Console shows distance and tolerance
- Verify goal position matches expected
- Check `calculatePreviewDistance()` logic

### Issue: Test map doesn't load in preview
**Symptoms:** Only gray placeholder cube shown
**Debug:**
- Check Network tab: did `testDescendOneBlock.json` load?
- Verify JSON is valid (no syntax errors)
- Check file path: `test-maps/testDescendOneBlock.json`

---

## Success Criteria

**All systems working if:**
- ✅ Menu loads and scrolls
- ✅ Preview modal opens with correct scene
- ✅ Animation shows player descending
- ✅ Animation reports test passed
- ✅ Manual mode allows keyboard control
- ✅ Goal detection works
- ✅ Console logs match expected output
- ✅ Direct test URL loads map
- ✅ No JavaScript errors in console

---

## Next Steps After Validation

Once all tests pass:

1. **Create more test maps** - Use `testDescendOneBlock.json` as template
2. **Test other mechanics** - Climb, basic movement, etc.
3. **Update mechanics graph** - Mark additional mechanics as tested
4. **Document edge cases** - Note any discovered bugs
5. **Add mobile controls** - Virtual joystick for phone testing

---

## Troubleshooting Commands

```bash
# Reload page, clear cache
Ctrl+Shift+R (or Cmd+Shift+R on Mac)

# View console
F12 or Ctrl+Shift+I

# Check if server running
ps aux | grep python

# Restart server
pkill python
cd /data/data/com.termux/files/home/projects/claude-code/1
python -m http.server 8080 &
```

---

## Test Checklist Template

Copy this for each new test map:

```
Test Name: _______________________
Date: _______________________

[ ] Preview modal opens
[ ] Voxels render correctly
[ ] Player at correct start position
[ ] Goal marker visible
[ ] Animation runs without errors
[ ] Player moves as expected
[ ] Goal detection works
[ ] Manual mode works
[ ] Console logs clean
[ ] Test passes/fails correctly

Issues found:
_______________________
_______________________

Notes:
_______________________
_______________________
```

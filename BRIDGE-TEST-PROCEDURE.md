# Bridge Testing Procedure

**Map:** `story-geometry/first-map-bridge-only.json`
**Status:** Ready for manual testing
**Date:** 2026-01-29

## Start Web Server

```bash
cd /data/data/com.termux/files/home/projects/claude-code/1
python -m http.server 8080
```

## Load Bridge

### Desktop
```
http://localhost:8080/?test=story-geometry/first-map-bridge-only
```

### Mobile (via Tailscale)
```
http://100.93.126.24:8080/?test=story-geometry/first-map-bridge-only
```

## Test Checklist

### ✓ Visual Validation
- [ ] Bridge renders in 3D
- [ ] Cobblestone supports visible at both ends (gray voxels)
- [ ] Wooden planks visible along span (brown voxels)
- [ ] Visible dip in middle (planks lower at X=5,6)
- [ ] Ramps on both sides
- [ ] Goal marker at far end (green wireframe sphere)

### ✓ Movement Tests

**Cross the bridge:**
- [ ] Start on left cobblestone (X=0, Z=0)
- [ ] Walk forward (W key) across entire bridge
- [ ] Auto-climb ramp from Y=1 → Y=2
- [ ] Walk along main span (Y oscillates 2→3→2→3)
- [ ] Auto-descend ramp Y=2 → Y=1
- [ ] Reach goal at X=11

**Test rope railings (invisible barriers):**
- [ ] Try to walk off north side (A key / left) - should be blocked
- [ ] Try to walk off south side (D key / right) - should be blocked
- [ ] Barriers only work along bridge span (X: 1-10)
- [ ] Can walk freely on cobblestone supports (X: 0, 11)

**Camera:**
- [ ] Rotate camera (mouse drag) - view bridge from all angles
- [ ] Zoom in/out (scroll) - see dip detail
- [ ] Camera follows player smoothly

### ✓ Edge Cases
- [ ] Can't walk off bridge at midpoint (where dip is lowest)
- [ ] Gravity doesn't pull player down when walking on planks
- [ ] Movement feels smooth despite elevation changes

## Expected Behavior

**Layout:**
```
[Cobble] [Ramp] [Up] [Up] [Dip] [Dip] [Up] [Up] [Ramp] [Ramp] [Cobble]
   X=0     X=1    X=3   X=4   X=5   X=6   X=7   X=8   X=9    X=10   X=11
   Y=1     Y=1    Y=3   Y=3   Y=2   Y=2   Y=3   Y=3   Y=2    Y=1    Y=1
```

**Barrier Zones:**
- North railing: Z < -0.45 (blocks movement) from X=1 to X=10
- South railing: Z > 0.45 (blocks movement) from X=1 to X=10

## Known Limitations (Deferred Features)

### Visual
- No visible rope railings (barriers are invisible)
- No rope sway animation
- No plank gaps or spacing detail
- No weathering or texture variation

### Technical
- Simple barrier system (not full constraint interface)
- Hard-coded Z-axis bounds check (not generalized)
- No directional constraint support
- No visual feedback when hitting barrier

## Success Criteria

✅ Can walk across bridge from left to right
✅ Barriers prevent falling off sides
✅ Dip is visible and walkable
✅ Feels like crossing a bridge
✅ All movement mechanics work (auto-climb, auto-descend)

## If Issues Found

Document in DEFERRED-FEATURES.md under "Bugs & Issues" section.

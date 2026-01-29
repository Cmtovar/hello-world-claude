# Test Map Index

Complete list of all test maps with their mechanics and purpose.

## Basic Movement Tests

### testBasicMovement.json
- **Mechanic:** `basic_movement`
- **Tests:** 4 cardinal directions (N/S/E/W)
- **Map:** Plus-shaped flat platform
- **Inputs:** W, A, S, D
- **Goal:** Reach center from any direction

### testDiagonalMovement.json
- **Mechanic:** `diagonal_movement`
- **Tests:** 8-direction movement (NE/NW/SE/SW)
- **Map:** L-shaped platform
- **Inputs:** W+D, W+A, S+D, S+A
- **Goal:** Move from corner to opposite corner

## Vertical Movement Tests

### testClimbUpOne.json
- **Mechanic:** `climb_up_one`
- **Tests:** Manual climb using Space key
- **Map:** 2-block pillar
- **Inputs:** Space (3 times)
- **Goal:** Climb from ground to top of pillar

### testDescendOneBlock.json
- **Mechanic:** `descend_one`
- **Tests:** Manual descent using Shift key
- **Map:** 2-block pillar
- **Inputs:** Shift
- **Goal:** Descend one level

### testMultipleDescents.json
- **Mechanic:** `descend_one`
- **Tests:** Sequential manual descents
- **Map:** 4-block tall pillar
- **Inputs:** Shift (3 times)
- **Goal:** Descend from y=4 to y=1

## Automatic Elevation Tests

### testAutoClimb.json
- **Mechanic:** `auto_climb`
- **Tests:** Automatic climbing when walking into 1-block step
- **Map:** Platform with 1-block step
- **Inputs:** W (forward)
- **Goal:** Walk over obstacle automatically

### testWalkDownTerrain.json
- **Mechanic:** `auto_descent`
- **Tests:** Automatic descent when walking onto lower terrain
- **Map:** Stepped descending platform
- **Inputs:** W (forward)
- **Goal:** Walk down steps automatically

## Gravity & Falling Tests

### testGravityFall.json
- **Mechanic:** `gravity`
- **Tests:** Falling from mid-air spawn
- **Map:** Ground platform with player spawned at y=5
- **Inputs:** None (gravity automatic)
- **Goal:** Fall and land on ground (y=1)

### testWalkOffLedge.json
- **Mechanic:** `gravity`
- **Tests:** Walking off platform edge and falling
- **Map:** Elevated platform with gap, then lower ground
- **Inputs:** W (forward, walk off edge)
- **Goal:** Fall to lower platform

## Complex Navigation Tests

### testComplexTerrain.json
- **Mechanic:** `auto_climb`
- **Tests:** Multiple elevation changes in sequence
- **Map:** Varied height terrain (up, flat, down, up)
- **Inputs:** W (forward continuously)
- **Goal:** Navigate complete course with auto-climb/descent

### testDiagonalAutoClimb.json
- **Mechanic:** `auto_climb`
- **Tests:** Diagonal movement combined with auto-climb
- **Map:** Diagonal path with 1-block elevation change
- **Inputs:** W+D (diagonal)
- **Goal:** Climb diagonally onto elevated platform

### testDiagonalAutoDescent.json
- **Mechanic:** `auto_descent`
- **Tests:** Diagonal movement combined with auto-descent
- **Map:** Diagonal path descending from elevated platform
- **Inputs:** W+D (diagonal)
- **Goal:** Descend diagonally to lower ground

## Test Coverage Summary

| Mechanic | Tests | Status |
|----------|-------|--------|
| basic_movement | 1 | ✅ Tested |
| diagonal_movement | 1 | ✅ Tested |
| climb_up_one | 1 | ✅ Tested |
| descend_one | 2 | ✅ Tested |
| auto_climb | 3 | ✅ Tested |
| auto_descent | 2 | ✅ Tested |
| gravity | 2 | ✅ Tested |

**Total:** 7 mechanics, 12 test maps

## Test Patterns

### Micro-Map Pattern
Each test is a minimal environment focusing on one mechanic in isolation:
- Small (5x5 voxels or less typically)
- Clear start/goal markers
- No distractions or unnecessary terrain
- Specific expected inputs

### Color Coding
- **Green (65280)** - Ground level, safe terrain
- **Orange (16753920)** - Elevated platforms, goal markers
- **Gray (11184810)** - Surrounding terrain, context

### Quality Checks
All tests include:
- Valid player start position (has ground below)
- Valid goal position (has ground below)
- Reachable goal using specified mechanic
- Expected inputs that demonstrate mechanic

## Usage

### Manual Testing
1. Open http://100.93.126.24:8080/
2. Click test selection menu
3. Choose mechanic to test
4. Click "🎮 Play Manually"
5. Use WASD/Space/Shift or mobile joystick

### Automated Testing
1. Open http://100.93.126.24:8080/
2. Click test selection menu
3. Choose mechanic to test
4. Click "▶ Run Animation"
5. Observe expected behavior

### Main Game Testing
Load specific test as main map:
```
http://100.93.126.24:8080/?test=testBasicMovement
```

## Next Tests Needed

### High Priority
- Jump mechanic (when implemented)
- Multi-block wall climbing (when implemented)

### Medium Priority
- Edge case: Collision boundaries
- Edge case: Maximum climb height limits
- Stress test: Very tall structures
- Stress test: Large flat areas

### Low Priority
- Flight mechanics (flier unit)
- Grappling hook (ODM gear)
- Dynamic platforms
- Multiple units interacting

---

**Last Updated:** 2026-01-28
**Test Framework Version:** 1.0
**Total Test Coverage:** 7/7 core mechanics (100%)

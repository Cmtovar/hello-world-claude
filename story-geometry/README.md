# Story Geometry Tests

**Purpose:** Test geometry that will be included in the actual story/game.

This directory is separate from `test-maps/` which contains micro-tests for individual mechanics. Story geometry tests are for complete map structures that will appear in the narrative.

## Philosophy

- **Builds on micro-tests**: Uses all validated movement mechanics
- **Isolation testing**: Test geometry in isolation before full map integration
- **Simple start**: Get keyframes working, defer polish
- **Iterative refinement**: Document what's simplified vs. deferred

## Current Contents

### first-map-bridge-only.json
The rope bridge from "The Bridge at Old Fort Crossing" first map.
- Wooden plank walkway with visible dip
- Cobblestone support structures
- Rope railing constraints (simple barriers)

## Load in Browser

```
http://localhost:8080/?test=../story-geometry/first-map-bridge-only
```

## Versus Micro-Tests

| Aspect | Micro-Tests (`test-maps/`) | Story Geometry (`story-geometry/`) |
|--------|---------------------------|-----------------------------------|
| Purpose | Validate single mechanic | Test story map structures |
| Scope | Minimal (5-10 voxels) | Moderate (20-50 voxels) |
| Constraints | Test validation only | Gameplay barriers |
| Reuse | Building blocks | Actual game content |

## Next Geometry

- River/creek beneath bridge
- Old military battlement ruins
- Town layout

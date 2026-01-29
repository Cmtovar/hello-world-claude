# Coordinate System Documentation

## Voxel and Player Positioning

### Voxel Coordinates
- A voxel at `y=0` occupies the space at height 0
- Voxels are 1x1x1 cubes centered at their coordinates
- Example: voxel at (0, 1, 0) occupies the unit cube centered at that point

### Player Positioning
- Player position `y` represents where the player "stands"
- Player at `y=1` is standing **on top of** the voxel at `y=0`
- Player at `y=2` is standing **on top of** the voxel at `y=1`

### Movement Mechanics

**Climbing Up:**
- Player at `y=1` (on voxel at `y=0`)
- Climbs to `y=2` (on voxel at `y=1`)
- Requirements:
  - Target space `y=2` must be empty (no voxel)
  - Supporting voxel at `y=1` must exist

**Descending:**
- Player at `y=2` (on voxel at `y=1`)
- Descends to `y=1` (on voxel at `y=0`)
- Requirements:
  - Target space `y=1` must be empty (no voxel)
  - Supporting voxel at `y=0` must exist

## Current Bug

The descent mechanic fails when:
- Player is at `y=2` standing on voxel at `y=1`
- Tries to descend to `y=1`
- Check fails: `!hasVoxel(x, 1, z)` returns FALSE
- Because there IS a voxel at `y=1` (the one player is standing on)

## Solution

The descent check is conceptually wrong. When descending from a platform, you're not descending to empty space - you might be descending to stand on the same platform from a lower position.

Suggested fix: Modify descent logic to allow descending even if there's a voxel at the current level, as long as there's somewhere to stand.

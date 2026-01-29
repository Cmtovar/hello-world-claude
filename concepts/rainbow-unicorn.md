# Rainbow Unicorn Unit Concept

**Status:** Concept
**Priority:** Future Implementation
**Theme Colors:** Pink (#FFB6C1), Baby Blue (#87CEEB), Yellow (#FFFF99)

## Original Vision

> "a pink white baby blue yellow border for a unicorn that has a rainbow trail foot locked units can stand on temporarily to navigate the map"

## Core Mechanic: Rainbow Trail Movement

### Description
A magical unicorn unit that leaves behind temporary rainbow trails as it moves. These rainbow trails create temporary platforms that other ground-locked units can stand on, enabling new navigation possibilities.

### Key Features

**Rainbow Trail Creation:**
- Unicorn leaves colored trail tiles behind as it moves
- Trail tiles are "foot-locked" - other units can stand on them
- Trails are temporary - fade after X turns/seconds
- Trail color cycles through rainbow spectrum

**Vertical Traversal:**
- Unicorn can move vertically (flight or jumping)
- Creates vertical bridges for ground units
- Enables access to otherwise unreachable areas

**Strategic Applications:**
- Support unit - creates paths for allies
- Bridge maker - connects separated platforms
- Puzzle element - timed navigation challenges

## Mechanics Dependencies

From `mechanics-graph.json`:
- `basic_movement` - Foundation for all movement
- `flight_basic` - If unicorn flies
- OR `jump` - If unicorn jumps between platforms
- **New mechanic needed:** `rainbow_trail_creation`
- **New mechanic needed:** `temporary_platform_standing`

## Visual Design

**Unicorn Unit:**
- Color scheme: White body with pink/blue/yellow mane
- Sparkle effects when moving
- Rainbow particle trail

**Rainbow Trail:**
- Gradient voxels cycling through rainbow colors
- Transparent/glowing effect
- Fade animation when expiring

**UI Theme:**
- Test cards with gradient borders (pink → blue → yellow)
- Rainbow icon for mechanic category
- Sparkle animations on hover

## Technical Implementation Considerations

### Trail System
```javascript
trail: {
  maxLength: 10,  // tiles
  duration: 3,    // turns before fade
  colors: ['#FFB6C1', '#87CEEB', '#FFFF99', '#90EE90', '#DDA0DD'],
  passable: true, // ground units can walk on it
  decayAnimation: 'fade' // how it disappears
}
```

### Interaction Rules
- Only ground units can use trails (fliers don't need them)
- Trails can cross gaps, creating bridges
- Multiple trails can overlap (mixing colors?)
- Unicorn can walk on own trails

### Balance Considerations
- Trail duration prevents infinite bridges
- Limited trail length prevents abuse
- Unicorn movement cost (AP/stamina)
- Can enemy units use trails? (design choice)

## Test Maps Needed

**testRainbowTrailCreation:**
- Unicorn moves across flat ground
- Verify trail tiles appear behind
- Verify color cycling

**testTrailTemporaryPlatform:**
- Ground unit + Unicorn on separate platforms
- Unicorn creates bridge
- Ground unit walks across
- Verify trail fades after duration

**testTrailVerticalBridge:**
- Unicorn moves up cliff face
- Creates vertical trail
- Ground unit climbs the trail
- Tests 3D trail navigation

**testTrailDecay:**
- Create long trail
- Wait for decay timer
- Verify tiles disappear in order (FIFO)

## Map Design Opportunities

**Rainbow Bridges:**
- Large gaps require unicorn to bridge
- Multiple paths possible with creative trail placement
- Time pressure (trail decay) adds challenge

**Vertical Forests:**
- Avatar-style tree platforms
- Unicorn creates vertical trails between trees
- Ground units follow the glowing path upward

**Puzzle Elements:**
- Timed sequences requiring precise trail placement
- Multiple units coordinating movement
- Trail overlap mechanics (color mixing?)

## Related Concepts

See also:
- `concepts/odm-gear.md` - Another vertical traversal unit
- `concepts/temporal-platforms.md` - Similar temporary platform mechanics
- Fire Emblem "Rescue" mechanic - unit support parallels

## Implementation Priority

**Phase 1 (Core):**
- Basic trail creation on flat ground
- Ground units can walk on trails
- Simple trail decay

**Phase 2 (3D):**
- Vertical trail creation
- Climbing on trails
- 3D pathfinding for trails

**Phase 3 (Polish):**
- Rainbow color cycling
- Particle effects
- Trail color mixing
- UI theme integration

**Phase 4 (Balance):**
- Playtesting
- Adjust duration/length based on gameplay
- Enemy interaction rules

## Notes

This unit transforms the tactical landscape by temporarily rewriting terrain. The rainbow aesthetic brings joy and whimsy while the mechanics add strategic depth. The temporary nature creates interesting timing challenges and prevents overpowered strategies.

Perfect for puzzle-focused maps or support-heavy team compositions.

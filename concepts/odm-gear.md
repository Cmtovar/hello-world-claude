# ODM Gear Unit Concept

**Status:** Concept
**Priority:** High (Core unit type)
**Inspiration:** Attack on Titan 3D Maneuvering Gear

## Original Vision

> "ODM gear style grappling hook movement"
>
> "map terrain that inspires from verticality like mountain cliff faces, tall autumn leave forests (like jet in avatar, the freedom scouts atla that have treehouses in the sky)"

## Core Mechanic: Grappling Hook Mobility

### Description
A unit equipped with Omni-Directional Mobility (ODM) gear that can fire grappling hooks to distant anchor points, enabling rapid 3D movement through vertical terrain. Inspired by Attack on Titan's iconic mobility system.

### Key Features

**Grappling Hook:**
- Target distant voxels/anchor points
- Cable physics - swing in arc toward target
- Momentum-based movement
- Can chain multiple grapples (like Spider-Man)

**Anchor Points:**
- Cliff faces, tree trunks, building walls
- Visual indicator for valid grapple targets
- Range limit based on cable length

**Vertical Mastery:**
- Rapid ascent up cliffs
- Swing across gaps
- Maintain altitude while traversing
- Dynamic camera follows movement

## Mechanics Dependencies

From `mechanics-graph.json`:
- `basic_movement` - Foundation
- `grappling_hook` - Main mechanic (to be implemented)
- `gravity` - Affects swing physics

**New mechanics needed:**
- `grappling_hook` - Target selection, cable throw
- `cable_swing_physics` - Arc movement, momentum
- `anchor_point_detection` - Valid grapple targets
- `chain_grappling` - Consecutive grapples mid-air

## Movement Patterns

**Single Grapple:**
1. User targets anchor point (click/tap)
2. Cable shoots out
3. Unit swings in arc toward target
4. Releases at apex or user input

**Chain Grappling:**
1. While swinging, target new anchor
2. Release first cable, throw second
3. Momentum carries into next swing
4. Can chain indefinitely (skill-based)

**Vertical Climb:**
1. Grapple straight up cliff face
2. Reel in cable (fast ascent)
3. Automated or player-controlled

## Technical Implementation

### Grappling System
```javascript
grapple: {
  range: 15,              // tiles
  cableSpeed: 10,         // units/sec
  swingForce: 5,          // physics magnitude
  releaseInput: 'Space',  // detach cable
  chainWindow: 0.5        // seconds to chain next grapple
}
```

### Physics Simulation
- Pendulum motion around anchor point
- Gravity affects swing trajectory
- Momentum preservation between grapples
- Collision detection with terrain

### Anchor Point System
- Voxels marked as "grappable"
- Proximity highlight when in range
- Targeting reticle/cursor
- Invalid targets grayed out

## Map Design for ODM Units

**Mountain Cliffs:**
- Vertical faces with anchor points
- Multiple routes up (exploration)
- Hidden ledges accessible only by grappling
- Ground units take stairs, ODM units fly up

**Autumn Forest (Avatar-style):**
- Tall trees with platforms
- Tree-to-tree grappling
- Vertical villages in canopy
- Falling leaves as atmospheric effect

**Urban Environments:**
- Building walls as anchor points
- Rooftop traversal
- Alleyway shortcuts via grappling
- Multi-story structures

**Tornado/Dynamic Hazards:**
- Grapple onto debris in tornado
- Ride objects being flung
- Risk/reward: fast travel but dangerous

## Advantages & Disadvantages

**Strengths:**
- Unmatched vertical mobility
- Rapid map traversal
- Access unreachable areas
- Evasion/positioning in combat

**Weaknesses:**
- Requires anchor points (useless in open fields)
- Skill-based (harder to use than walking)
- Vulnerable during grapple (committed to arc)
- Limited horizontal movement on flat ground

## Test Maps Needed

**testGrappleBasic:**
- Single anchor point on cliff
- Unit at bottom, target at top
- Verify cable throw and ascent
- Check arrival at target position

**testGrappleSwing:**
- Two anchor points at height
- Gap between them
- Unit swings from first to second
- Test arc physics and momentum

**testChainGrapple:**
- Three anchor points in sequence
- Unit chains grapples without touching ground
- Verify momentum preservation
- Test input timing window

**testGrappleRange:**
- Anchor points at varying distances
- Some in range, some out of range
- Verify range indicator
- Test failed grapple (too far)

**testGrappleInvalidTarget:**
- Mix of valid/invalid voxels
- Verify only correct targets highlighted
- Test rejection of invalid targets

## Visual Design

**Cable Effect:**
- Visible line from unit to anchor
- Dynamic tension shader
- Particle effects on attachment
- Cable sway/physics

**Unit Animation:**
- Launch pose when firing
- Mid-air rotation while swinging
- Land recovery animation
- Reload animation for next grapple

**Audio (future):**
- Cable whoosh sound
- Mechanical clicking (gear activation)
- Impact sound on anchor attach
- Wind rush during swing

## Strategic Depth

**Tactical Uses:**
- Flanking maneuvers (grapple behind enemies)
- High ground advantage
- Retreat options (grapple away)
- Rescue allies (grapple to them)

**Map Control:**
- Dominate vertical spaces
- Contest high-value positions
- Deny area by superior positioning

**Combo Potential:**
- Grappler scouts ahead
- Creates paths for ground units
- Synergy with rainbow unicorn trails?
- Combined arms tactics

## Related Concepts

See also:
- `concepts/rainbow-unicorn.md` - Another mobility unit
- `concepts/climber-unit.md` - Vertical traversal alternative
- `concepts/flier-unit.md` - Different aerial approach

## Implementation Roadmap

**Phase 1: Basic Grapple**
- Click to target anchor point
- Cable throws, unit travels to target
- Simple linear motion (no swing physics yet)

**Phase 2: Physics**
- Pendulum swing mechanics
- Momentum calculation
- Gravity integration
- Collision detection

**Phase 3: Chain Grappling**
- Multi-grapple system
- Momentum preservation
- Input buffering
- Combo counter

**Phase 4: Polish**
- Cable visuals
- Animation system
- Particle effects
- Camera smoothing

**Phase 5: Advanced**
- Skill-based techniques
- Speed run optimization
- Challenge maps showcasing ODM

## Balance Considerations

- Grapple cooldown (prevent spam)
- Energy/stamina cost per grapple
- Limited charges per turn (tactical game)
- Vulnerability during animation (risk)
- Anchor point placement (map design challenge)

## Notes

ODM gear represents high skill ceiling mobility. Mastery feels incredibly rewarding. The 3D freedom contrasts beautifully with ground-locked units, creating interesting team composition choices.

This is the poster child for vertical gameplay - when you nail this mechanic, the entire 3D tactical vision comes alive.

Attack on Titan meets Fire Emblem. The dream.

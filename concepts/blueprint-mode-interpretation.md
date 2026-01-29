# Blueprint Mode - Interpretation & Action Items

**Date:** 2026-01-29
**Interpreter:** Claude (Session 2026-01-29)
**Primary Source:** `blueprint-mode-design.md`

---

## Core System: AP + Blueprint Mode

### AP Regeneration System
- Units have AP bars that fill over time at different rates
- **Critical rule:** Can ONLY act when AP = 100%
- Actions consume the full bar (back to 0%)
- After action, bar begins refilling

### Key Trade-off
**Wait vs Act:**
- Wait for multiple units to fill → plan coordinated parallel actions
- Act immediately with fewer units → faster response, less coordination

### Splatoon Ink Analogy (Inverted)
**Splatoon:** Start full → consume ink → wait for refill → can act again
**This game:** Start empty → wait for fill → can act → back to empty

**Insight:** You're "charging up" the ability to act, then spending it all at once.

---

## Blueprint Mode (Time-Frozen Planning)

### What It Is
- Time stops (like Shulk's vision, Mila's Turnwheel)
- UI for assigning actions to ready units
- Actions placed along a timeline
- When you exit, all actions execute simultaneously

### Parallelism is the Core Innovation
Unlike traditional Fire Emblem (I go → you go), this enables:
- Multiple friendly units acting at once
- Multiple enemy units acting at once
- Coordination as the primary strategic element

---

## Strategic Implications

### Anti-Turtle Design
**Traditional Fire Emblem:** Turtling (defensive positioning) is often optimal.

**This game:** If you turtle, you run out of space. Units need room to coordinate.

**Key concept:** "Arteries" in coordination design
- Units need pathways to flow through
- Can't all cluster in one spot
- Movement choreography becomes important

### Mob Enemies with Coordination
**Examples:**
- Ravens: Dive in coordinated patterns
- Moblins (Wind Waker style): Mob the player, strength in numbers
- Constraint-forming AI: Some enemies limit player movement while others deal damage

**Why this matters:**
- Picking them off one-by-one is tediously slow
- AoE damage becomes strategically important
- Breaking formations becomes the goal

---

## Template/Snippet System (TotK Auto-Build)

### The Problem
As levels get complex, blueprint mode could become tedious. You don't want players spending ages choreographing the same patterns repeatedly.

### The Solution
**Strategy Templates:**
- Save common coordination patterns
- Quick-access in blueprint mode
- Like TotK's auto-build for structures

### Three Upgrade Paths
1. **Number of snippets** - How many templates you can have registered
2. **Complexity** - How many actions per template
3. **Unit count** - How many units can participate in one template

### Design Philosophy
- Progression feels meaningful but is **optional**
- It's quality-of-life, not a hard requirement
- Both players AND enemies use this system
- Blueprint mode should be a "thinking environment" with smooth controls

---

## Testing Strategy

### Test Layers
1. **Blueprint mode itself:**
   - Open/close blueprint mode
   - Select units
   - Assign actions to timeline

2. **Individual actions:**
   - Each fundamental action (move, climb, attack, etc.)
   - Test in isolation first

3. **Interface-based testing:**
   - Define action interface
   - `array[ActionInterface]`
   - Test against interface, not concrete implementations
   - Swap implementations without changing tests

### Priority: Representative Behaviors

**Don't build everything at once. Build archetypes that are reusable:**

**Raven AI:**
- Coordinated diving behavior
- Could ALSO be: Town NPCs walking in a café
- Same coordination logic, different context

**Grass Block:**
- Standard voxel with constraint JSON
- Could ALSO be: Basket, falling apple, sand monster
- Same constraint interface, different visuals/behavior

**Strategy:** Start with behaviors that capture broad utility, then reskin/repurpose.

---

## How This Connects to 3D Movement

### Vertical Coordination
With grappling, flying, climbing:
- Units can coordinate across height levels
- Rainbow Unicorn creates sky trail → allies use it in their plans
- Falcons have pre-built dogfighting trajectories player can trigger/interrupt

### Pre-built Trajectories
Interesting design choice: Some unit abilities come with **suggested patterns** the player can use or modify.

**Example:** Falcon unit
- Has 3 pre-built attack dive patterns
- Player can select one in blueprint mode
- Or customize/interrupt it

This is like having "moves" in a fighting game, but you can sequence and coordinate them.

---

## Anti-Turtle Mechanics in Detail

### Why Fire Emblem Encourages Turtling
- Enemies come to you
- Chokepoints are OP
- No penalty for waiting
- Limited AoE options

### How This Design Discourages It
1. **Space constraints:** Coordinating units need room
2. **Mob enemies:** They coordinate too, overwhelm chokepoints
3. **AoE value:** Breaking formations is necessary
4. **Flow design:** Need "arteries" for unit movement

**Result:** Offensive, coordinated play becomes optimal.

---

## Constraint System Integration

### Mob Constraint Shapes
Enemies don't just damage - they **limit your movement options** through positioning.

**Example formation:**
- Front line: Creates constraint blocking forward movement
- Back line: Deals damage through gaps
- Player must break formation or use AoE

### Dynamic Constraint Objects
**Grass block → Basket → Apple → Sand Monster**

All use the same constraint JSON, but different contexts:
- Grass: Static terrain
- Basket: Interactable object
- Apple: Falling hazard
- Sand Monster: Mobile enemy with collision/knockback

**Constraint signature** is preserved, behavior varies.

---

## Emergent Complexity

### Simple Rules → Rich Strategy

**Base mechanics:**
1. AP regeneration at different rates
2. Act only at 100%
3. Blueprint mode for parallel planning
4. Constraint-based movement
5. Template system for patterns

**Emerges:**
- Timing decisions (when to wait, when to act)
- Coordination choreography
- Formation breaking strategies
- Flow/artery design in your unit positioning
- Template library as learned skill expression

---

## Implementation Action Items

### Phase 1: Foundation (Current Focus)
- [x] Basic movement mechanics (7/7 implemented)
- [x] Test infrastructure
- [ ] AP regeneration system (new)
- [ ] Blueprint mode UI shell (new)
- [ ] Time-freeze mechanic (new)

### Phase 2: Core Loop
- [ ] Single-unit action planning in blueprint
- [ ] Action timeline UI
- [ ] Execute planned actions
- [ ] Multi-unit parallel execution

### Phase 3: Enemies & Coordination
- [ ] Raven AI (diving coordination)
- [ ] Moblin AI (swarming/escorting)
- [ ] Constraint-forming enemy patterns
- [ ] Enemy blueprint planning

### Phase 4: Template System
- [ ] Save/load action sequences
- [ ] Template UI in blueprint mode
- [ ] Template upgrades (count, complexity, units)
- [ ] Enemy template usage

### Phase 5: Advanced
- [ ] Pre-built unit trajectories (falcon dives)
- [ ] Character-specific skills (unicorn trail)
- [ ] AoE abilities
- [ ] Formation/constraint visualization

---

## Testing Hierarchy

```
Interface: FundamentalAction
  ├─ MoveAction
  ├─ ClimbAction
  ├─ AttackAction
  ├─ SkillAction (unicorn trail, etc.)
  └─ WaitAction

Test blueprint mode with array[FundamentalAction]
→ Tests work regardless of specific action types
→ New actions can be added without changing tests
```

---

## Design Patterns Identified

### 1. Archetype Reuse
Start with broad utility, then specialize:
- Raven AI → Town NPC coordination
- Grass block → Basket → Apple → Monster

### 2. Interface-First Testing
Test against contracts, not implementations.

### 3. Quality-of-Life as Progression
Templates make game smoother, but aren't required.

### 4. Inverted Resource System
Traditional: Spend resource → recharge → spend again
This game: Recharge → spend all → recharge again

### 5. Both Sides Use Same Tools
Player and enemy both use:
- Blueprint mode
- Templates
- Constraint system
- This creates mirror complexity

---

## Open Questions

1. **AP Refill Rates:**
   - How much variance between units?
   - Does unit type affect refill speed?
   - Can refill speed be upgraded?

2. **Blueprint Mode Entry:**
   - Can you enter anytime, or only when AP is ready?
   - Can enemy actions interrupt your planning?
   - Is there a cost to entering/exiting?

3. **Template Acquisition:**
   - Are templates found/unlocked, or player-created?
   - Can you copy enemy templates?
   - Are there "canonical" templates for each unit type?

4. **Constraint Visualization in Blueprint:**
   - How does player see constraint zones during planning?
   - How are mob constraint formations displayed?
   - Is there a "simulation" mode to preview outcomes?

5. **Turn Structure:**
   - Is there a global "tick" rate?
   - Or truly asynchronous (units act when their AP fills)?
   - How do simultaneous actions resolve conflicts?

---

## Next Steps for This Session

**Given the current state (7/7 basic movement mechanics tested):**

### Potential Paths:
1. **Prototype AP system** - Get the bars filling, basic visualization
2. **Blueprint mode shell** - Time-freeze, simple UI
3. **Representative AI** - Build raven diving behavior first
4. **Macro map** - Compose existing mechanics into a level that *would* use blueprint mode

**Recommendation:** Start with AP regeneration + basic blueprint UI, because that's the foundation everything else builds on.

But let's let this emerge naturally through discussion.

---

**Related Documents:**
- `blueprint-mode-design.md` - Primary source (unedited)
- `constraint-interface-pattern.md` - How constraints enable this
- `DEVELOPER-STYLE-GUIDE.md` - Design philosophy

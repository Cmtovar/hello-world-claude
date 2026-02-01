# Declarative Event System - Future Blueprint/Battle Implementation

**Date:** 2026-01-30
**Status:** Design notes for future implementation
**Context:** Deferred during cutscene work - will implement for blueprint mode

---

## Purpose

This system is for **tactical gameplay visualization**, NOT story cutscenes:

1. **Blueprint mode** - Showing parallel unit coordination
2. **Template playback** - Demonstrating what templates do
3. **Battle replay** - Memory system for reviewing past battles
4. **Template IDE** - Temporal playback for learning/teaching

Story cutscenes will likely be pre-rendered (Blender animations) or hardcoded scripts.

---

## Core Concept

Define battles/templates as **event sequences** with timestamps.

Events have **types** (move, attack, ability, status_effect, etc.)
Each event type has a **handler** that knows how to execute it.
Compose complex battles from simple event primitives.

### Example Event Structure

```json
{
  "timeline": [
    {
      "timestamp": 0.0,
      "type": "move",
      "unit": "unit_1",
      "from": {"x": 2, "y": 1, "z": 3},
      "to": {"x": 5, "y": 1, "z": 3},
      "duration": 1.5
    },
    {
      "timestamp": 0.0,
      "type": "move",
      "unit": "unit_2",
      "from": {"x": 3, "y": 1, "z": 3},
      "to": {"x": 6, "y": 1, "z": 3},
      "duration": 1.5
    },
    {
      "timestamp": 1.5,
      "type": "attack",
      "attacker": "unit_1",
      "target": "enemy_1",
      "technique": "basic_slash",
      "damage": 15
    },
    {
      "timestamp": 1.8,
      "type": "camera_focus",
      "target": "enemy_1",
      "duration": 0.5
    }
  ]
}
```

---

## Why Declarative for Battle Events

### Blueprint Mode Requirements
- Multiple units act **simultaneously** (parallel coordination)
- Show AP usage and regeneration
- Timeline visualization
- Pause/step through execution
- Show what WILL happen before committing

### Template System Requirements
- Templates are **data**, not code
- Need to serialize/save player-created strategies
- Playback in IDE for teaching
- Decompose complex templates into constituent actions
- Show control flow (if/then, loops, conditions)

### Memory/Replay System Requirements
- Review past battles
- Study what worked/failed
- Share battle recordings
- Learn from experience
- Build almanac of encountered situations

### Variability
- Same template, different units
- Same template, different terrain
- Same template, different enemy formations
- **Can't pre-render** - must be generated at runtime

---

## Design Principles (From Developer Style Guide)

### Declarative Over Imperative
Don't code: "Unit 1 moves to X, then attacks, then..."
Instead: Declare event sequence, let system execute

### Emergent Over Prescribed
Simple rule: Events have types and handlers
Simple rule: Timeline orders execution
Emergent: Complex battles from simple event composition

### Interface-Based Thinking
Events expose **affordances** - what actions are possible
Event handlers are **interchangeable** if they match interface

---

## Event Types (Preliminary)

### Unit Actions
- `move` - Unit movement from A to B
- `attack` - Combat action
- `ability` - Special technique
- `wait` - Unit pauses/delays
- `status_apply` - Apply status effect
- `status_remove` - Remove status effect

### Environmental
- `terrain_create` - Spawn temporary terrain (Rainbow Unicorn platforms)
- `terrain_destroy` - Remove terrain
- `hazard_trigger` - Activate environmental hazard
- `constraint_apply` - Apply movement constraint
- `constraint_remove` - Remove constraint

### Visual/Camera
- `camera_move` - Reposition camera
- `camera_focus` - Look at target
- `camera_shake` - Impact effect
- `effect_spawn` - Visual effect (explosion, sparkle, etc.)
- `lighting_change` - Adjust scene lighting

### Meta
- `parallel_start` - Begin parallel execution block
- `parallel_end` - End parallel block
- `wait_for` - Synchronization point
- `branch` - Conditional execution (template control flow)

---

## Parallel Execution

Key differentiator from Fire Emblem: **true parallelism**

```json
{
  "timeline": [
    {
      "timestamp": 0.0,
      "type": "parallel_start",
      "id": "coordinated_assault"
    },
    {
      "timestamp": 0.0,
      "type": "move",
      "unit": "unit_1",
      "to": {"x": 5, "y": 1, "z": 3}
    },
    {
      "timestamp": 0.0,
      "type": "move",
      "unit": "unit_2",
      "to": {"x": 6, "y": 1, "z": 3}
    },
    {
      "timestamp": 0.0,
      "type": "move",
      "unit": "unit_3",
      "to": {"x": 7, "y": 1, "z": 3}
    },
    {
      "timestamp": 1.5,
      "type": "parallel_end",
      "id": "coordinated_assault"
    },
    {
      "timestamp": 1.5,
      "type": "attack",
      "attacker": "unit_1",
      "target": "enemy_1"
    }
  ]
}
```

All moves happen simultaneously from 0.0 to 1.5, then attack at 1.5.

---

## Integration with Template IDE

### Playback Controls
- Play/Pause
- Step forward/backward
- Speed control (slow motion for learning)
- Scrub timeline
- Highlight specific unit

### Decomposition View
Show template as:
- Event list (what happens when)
- Dependency graph (what blocks what)
- AP usage timeline (when AP is spent/regenerated)
- Constraint satisfaction (which constraints enabled which actions)

### Learning Mode
- Annotate events ("This move created line of sight")
- Compare variations ("What if unit 2 went here instead?")
- Show affordances at each timestamp ("What else was possible?")

---

## AP Regeneration Integration

Blueprint mode uses **AP regeneration** (all units fill to 100% each turn).

Event timeline must show:
- AP cost of each action
- When AP is spent
- When regeneration happens (start of next planning phase)
- Visual: AP bars on timeline

This is CRITICAL for blueprint mode visualization.

---

## Reference Implementation: Hardcoded Cutscene

**Location:** `index.html` - First map intro cutscene (2026-01-30)

The hardcoded cutscene shows:
- Multiple characters moving in parallel
- Camera positioning during sequences
- Dialogue timing
- Lighting changes (rain event)
- Choreographed multi-unit actions

**Use as reference when building this system:**
- How did we handle parallel movement?
- How did we time sequences?
- What abstractions emerged naturally?
- What was painful to hardcode (should be declarative)?

---

## Next Steps (When Implementing)

1. Define event type interfaces
2. Create event handlers for each type
3. Build timeline executor
4. Implement parallel execution
5. Add playback controls (play/pause/step)
6. Create template → event sequence compiler
7. Build IDE visualization
8. Integrate with blueprint mode
9. Add AP regeneration display
10. Implement memory/replay system

---

## Open Questions

### Timing
- Absolute timestamps vs relative delays?
- How to handle variable-duration actions (different unit speeds)?
- Synchronization points for parallel actions?

### Camera
- Automatic camera (follow action) vs manual waypoints?
- How to show multiple simultaneous actions (split screen? picture-in-picture? camera cuts)?
- Player camera override during playback?

### Constraints
- How to show constraint satisfaction in timeline?
- Visual indication when constraint blocks an action?
- How to handle environmental constraints changing mid-battle (rising water)?

### Templates
- How to represent control flow (if/then/loops) in event timeline?
- Conditional events based on battle state?
- Dynamic event generation vs static timeline?

### Editing
- Can player edit event timeline directly in IDE?
- Or only through template language?
- Live preview of changes?

---

## Relationship to Constraint Interface Pattern

Event system is **orthogonal** to constraint system:

- **Constraints** define what's **possible** (affordances, rules)
- **Events** define what **actually happens** (execution, history)

Constraints are spatial/positional (can I move here?)
Events are temporal/sequential (what happened when?)

Both use interface-based thinking:
- Constraints expose affordances
- Events expose actions

Composition creates emergence:
- Constraints compose to create complex terrain
- Events compose to create complex battles

---

**This document captures design intent for future implementation. Revisit after hardcoded cutscene is complete to extract learned patterns.**

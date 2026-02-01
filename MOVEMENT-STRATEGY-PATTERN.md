# Movement Strategy Pattern - Context-Aware Movement Validation

**Created:** 2026-01-30
**Emerged From:** Cutscene Test 02 - Parallel movement choreography testing
**Status:** Design document → Ready for implementation

---

## The Problem (Observed in Testing)

When testing parallel character movement in cutscenes, several issues emerged:

1. **Characters walk through each other** - No collision detection
2. **Characters float in midair** - Gravity not applied after movement
3. **Auto-climb not triggered** - Moving into a 1-block obstacle should auto-climb
4. **Movement is too literal** - "Move forward" doesn't adapt to context

**Root Cause:** Movement actions are executed literally without considering:
- Terrain beneath/ahead
- Other characters in target position
- Constraints that would trigger automatic behaviors (auto-climb, gravity)

---

## The Solution: Movement Validation Pipeline

A declarative, context-aware system that:
1. **Validates** movement is possible
2. **Transforms** movement based on context (auto-climb, etc.)
3. **Executes** the appropriate action
4. **Post-processes** effects (gravity, constraints)

---

## Order of Operations (Critical)

```
INPUT: Desired position from action queue
  ↓
[1] PRE-MOVE VALIDATION (Blocking checks)
  ├─ Character Collision Check
  │  └─ Is another character at target position?
  │     └─ YES → BLOCK (treat as wall constraint)
  │     └─ NO → Continue
  │
  ├─ Terrain Constraint Check
  │  └─ Does terrain/constraint allow movement?
  │     └─ NO → BLOCK
  │     └─ YES → Continue
  │
  └─ Barrier/Constraint Check
     └─ Do barriers (rope railings, etc.) block this move?
        └─ YES → BLOCK
        └─ NO → Continue

[2] MOVEMENT TRANSFORMATION (Context adaptation)
  ├─ Auto-Climb Detection
  │  └─ Is target position occupied by 1-block obstacle?
  │     └─ YES → Transform "move forward" to "auto-climb"
  │     └─ NO → Continue
  │
  └─ Diagonal Normalization
     └─ Is this a diagonal move?
        └─ YES → Normalize vector, check both axes
        └─ NO → Continue

[3] MOVEMENT EXECUTION
  └─ Apply transformed movement
     └─ Update character position
     └─ Animate movement

[4] POST-MOVE PROCESSING (Effects after move)
  ├─ Gravity Check
  │  └─ Is there ground beneath new position (Y-1)?
  │     └─ NO → Apply gravity (fall until ground)
  │     └─ YES → Stable
  │
  └─ Auto-Descent Check
     └─ Stepped onto lower terrain?
        └─ YES → Auto-descend
        └─ NO → Done
```

**Why this order?**
- Character collision must block BEFORE transformation (can't auto-climb through someone)
- Gravity applies AFTER successful move (only fall if you successfully occupy the new space)
- Transformation happens before execution (decide what to do, then do it)

---

## Strategy Pattern Design

### Core Interface

```javascript
// Base strategy interface
class MovementStrategy {
  // Can this strategy execute in this context?
  canExecute(character, targetPos, gameState) {
    return true; // Override in subclasses
  }

  // Transform the action if needed
  transform(character, targetPos, gameState) {
    return { type: 'move', to: targetPos }; // Default: no transform
  }

  // Execute the movement
  execute(character, action, gameState) {
    // Override in subclasses
  }
}
```

### Concrete Strategies

#### 1. Character Collision Strategy (Blocking)

```javascript
class CharacterCollisionStrategy extends MovementStrategy {
  canExecute(character, targetPos, gameState) {
    // Check if another character occupies target position
    const occupied = gameState.characterGroup.characters.some(other => {
      return other.id !== character.id &&
             other.position.x === targetPos.x &&
             other.position.y === targetPos.y &&
             other.position.z === targetPos.z;
    });

    return !occupied; // Block if occupied
  }

  // If blocked, no transformation needed (move simply fails)
}
```

**Priority:** Highest (checked first)
**Effect:** Blocks movement entirely if another character is there

#### 2. Auto-Climb Strategy (Transforming)

```javascript
class AutoClimbStrategy extends MovementStrategy {
  canExecute(character, targetPos, gameState) {
    // Check if there's a 1-block obstacle at target position
    const hasVoxelAtTarget = game.terrain.has(
      `${targetPos.x},${targetPos.y},${targetPos.z}`
    );

    const hasGroundBeneath = game.terrain.has(
      `${targetPos.x},${targetPos.y - 1},${targetPos.z}`
    );

    // Auto-climb if: voxel at target height, ground beneath, only 1 block tall
    return hasVoxelAtTarget && hasGroundBeneath;
  }

  transform(character, targetPos, gameState) {
    // Transform horizontal move to climb move
    return {
      type: 'move',
      to: {
        x: targetPos.x,
        y: targetPos.y + 1, // Climb up one block
        z: targetPos.z
      },
      visualEffect: 'auto-climb' // Flag for animation
    };
  }
}
```

**Priority:** Medium (after collision, before execution)
**Effect:** Transforms "move forward" into "climb up" when appropriate

#### 3. Gravity Strategy (Post-processing)

```javascript
class GravityStrategy extends MovementStrategy {
  execute(character, action, gameState) {
    // After move completes, check if ground beneath
    const currentPos = character.position;

    // Check downward until we hit ground
    let fallDistance = 0;
    let checkY = currentPos.y - 1;

    while (checkY >= 0) {
      const hasGround = game.terrain.has(
        `${currentPos.x},${checkY},${currentPos.z}`
      );

      if (hasGround) {
        break; // Found ground
      }

      fallDistance++;
      checkY--;
    }

    // If no ground beneath, fall
    if (fallDistance > 0) {
      const fallTarget = {
        x: currentPos.x,
        y: currentPos.y - fallDistance,
        z: currentPos.z
      };

      // Animate fall
      animateCharacterMove(character, fallTarget);
    }
  }
}
```

**Priority:** Lowest (runs after move execution)
**Effect:** Makes character fall if no ground beneath

#### 4. Terrain Constraint Strategy (Blocking)

```javascript
class TerrainConstraintStrategy extends MovementStrategy {
  canExecute(character, targetPos, gameState) {
    // Check if terrain allows this move
    // Future: integrate with constraint interface pattern

    // For now: check if target position has ground beneath it
    const hasGroundBeneath = game.terrain.has(
      `${targetPos.x},${targetPos.y - 1},${targetPos.z}`
    );

    // Can't move to floating position (unless jumping/flying)
    return hasGroundBeneath || targetPos.y === 0;
  }
}
```

**Priority:** High (after character collision)
**Effect:** Prevents moving to invalid terrain positions

---

## Movement Pipeline Implementation

### Pipeline Orchestrator

```javascript
class MovementPipeline {
  constructor() {
    // Ordered strategies (execution order matters!)
    this.validators = [
      new CharacterCollisionStrategy(),
      new TerrainConstraintStrategy()
    ];

    this.transformers = [
      new AutoClimbStrategy()
    ];

    this.postProcessors = [
      new GravityStrategy()
    ];
  }

  // Execute full pipeline for a movement action
  processMovement(character, targetPos, gameState) {
    // [1] PRE-MOVE VALIDATION
    for (const validator of this.validators) {
      if (!validator.canExecute(character, targetPos, gameState)) {
        console.log(`Movement blocked by ${validator.constructor.name}`);
        return false; // Movement blocked
      }
    }

    // [2] MOVEMENT TRANSFORMATION
    let finalAction = { type: 'move', to: targetPos };

    for (const transformer of this.transformers) {
      if (transformer.canExecute(character, targetPos, gameState)) {
        finalAction = transformer.transform(character, targetPos, gameState);
        console.log(`Movement transformed by ${transformer.constructor.name}`);
        break; // Use first applicable transformation
      }
    }

    // [3] MOVEMENT EXECUTION
    executeAction(character, finalAction);

    // [4] POST-MOVE PROCESSING
    for (const processor of this.postProcessors) {
      processor.execute(character, finalAction, gameState);
    }

    return true; // Movement succeeded
  }
}

// Global pipeline instance
const movementPipeline = new MovementPipeline();
```

### Integration with Existing System

Modify `executeAction()` to use the pipeline:

```javascript
function executeAction(character, action) {
  console.log(`${character.name}: executing ${action.type}`, action);

  switch (action.type) {
    case 'move':
      // Use movement pipeline instead of direct execution
      const success = movementPipeline.processMovement(
        character,
        action.to,
        game
      );

      if (!success) {
        console.log(`${character.name}: movement blocked, skipping`);
        // Don't animate, just mark action as complete
        character.currentAnimation = {
          type: 'wait',
          startTime: Date.now(),
          duration: 100 // Very short wait to stay in sync
        };
      }
      break;

    case 'wait':
      animateCharacterWait(character, action.duration || 1000);
      break;

    default:
      console.warn(`Unknown action type: ${action.type}`);
  }
}
```

---

## Benefits of This Pattern

### 1. Declarative Movement
- Input: "Move forward"
- System decides: Auto-climb? Blocked? Gravity?
- User doesn't need to specify every detail

### 2. Extensible
- Add new strategies without modifying core logic
- Example future strategies:
  - `WaterConstraintStrategy` - can't move into water without swimming
  - `StatusEffectStrategy` - encumbered = slower movement
  - `AbilityStrategy` - flying units ignore ground checks

### 3. Order-Independent (Within Categories)
- Validators run in order, all must pass
- Transformers run in order, first match wins
- Post-processors run in order, all execute

### 4. Testable
- Each strategy is isolated and testable
- Can mock gameState for unit tests
- Easy to verify order of operations

### 5. Composable
- Strategies compose naturally
- Character collision + Auto-climb + Gravity all work together
- No complex if/else chains

---

## Relationship to Constraint Interface Pattern

**Constraint Interface Pattern** (from CONSTRAINT-INTERFACE-PATTERN.md):
- Defines what's **possible** at a position
- Static, positional affordances
- "Can I sit here? Can I climb this?"

**Movement Strategy Pattern** (this document):
- Defines what **actually happens** during movement
- Dynamic, contextual transformation
- "Should this move become a climb? Should gravity apply?"

**Integration:**
```javascript
class TerrainConstraintStrategy extends MovementStrategy {
  canExecute(character, targetPos, gameState) {
    // Query constraint interface for target position
    const constraints = getConstraintsAt(targetPos);

    // Check if character satisfies required constraints
    return character.capabilities.satisfies(constraints);
  }
}
```

The constraint system defines **what's possible**.
The strategy system decides **what actually happens**.

---

## Implementation Checklist

### Phase 1: Core Pipeline
- [ ] Create `MovementStrategy` base class
- [ ] Create `MovementPipeline` orchestrator
- [ ] Integrate with `executeAction()`

### Phase 2: Essential Strategies
- [ ] Implement `CharacterCollisionStrategy`
- [ ] Implement `GravityStrategy`
- [ ] Implement `AutoClimbStrategy`
- [ ] Implement `TerrainConstraintStrategy`

### Phase 3: Testing
- [ ] Test character collision blocking
- [ ] Test auto-climb transformation
- [ ] Test gravity application
- [ ] Test strategy execution order

### Phase 4: Optimization
- [ ] Cache terrain lookups
- [ ] Optimize collision checks (spatial partitioning?)
- [ ] Profile pipeline performance

---

## Future Extensions

### Status Effects as Strategies

```javascript
class EncumberedStrategy extends MovementStrategy {
  canExecute(character, targetPos, gameState) {
    return !character.hasStatus('encumbered');
  }

  transform(character, targetPos, gameState) {
    // Slow down movement if encumbered
    return {
      ...action,
      duration: action.duration * 1.5 // 50% slower
    };
  }
}
```

### Ability-Based Strategies

```javascript
class FlyingMovementStrategy extends MovementStrategy {
  canExecute(character, targetPos, gameState) {
    return character.hasAbility('flight');
  }

  // Flying units don't need ground beneath them
  // Overrides terrain constraints
}
```

### Environmental Strategies

```javascript
class WaterConstraintStrategy extends MovementStrategy {
  canExecute(character, targetPos, gameState) {
    const isWater = getTileType(targetPos) === 'water';
    return !isWater || character.hasAbility('swimming');
  }
}
```

---

## Design Principles Applied

### Declarative Over Imperative
- Don't code: "If obstacle, climb. If no ground, fall."
- Instead: Pipeline checks context, applies appropriate strategy

### Emergent Over Prescribed
- Simple strategies compose into complex behaviors
- Character collision + Auto-climb + Gravity = Realistic movement

### Interface-Based Thinking
- Strategies expose affordances (can execute? transform?)
- Interchangeable implementations
- Easy to add new movement rules

---

## For Future Sessions

**When implementing movement features:**
1. Check if it's a validation (can/can't move)
2. Check if it's a transformation (move becomes climb)
3. Check if it's post-processing (gravity after move)
4. Create appropriate strategy in correct category
5. Add to pipeline in correct order

**When debugging movement:**
1. Check console for which strategy blocked/transformed
2. Verify strategy execution order
3. Test strategy in isolation
4. Verify gameState is correct

---

**This pattern emerged from cutscene testing. It's the foundation for realistic, context-aware movement in both cutscenes and gameplay.**

**Next Step:** Implement Phase 1 (Core Pipeline) and Phase 2 (Essential Strategies)

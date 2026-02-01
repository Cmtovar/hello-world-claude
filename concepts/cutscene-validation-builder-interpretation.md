# Cutscene Validation Builder - Implementation Interpretation

**Date:** 2026-01-30
**Source:** cutscene-validation-builder.md (primary source)
**Status:** Design analysis → Ready for implementation

---

## The Core Problem (Analysis)

### What We Observed

```javascript
// Cutscene definition (absolute)
{ "actionQueue": [
  {"type": "move", "to": {"x": 5, "y": 1, "z": 0}},
  {"type": "move", "to": {"x": 10, "y": 1, "z": 0}},  // Collision!
  {"type": "move", "to": {"x": 15, "y": 1, "z": 0}}
]}

// Runtime execution
- Move to X=5 ✓ Success
- Move to X=10 ✗ Blocked (another character there)
- Character waits (blocked action creates short wait)
- Move to X=10 ✗ Still blocked
- Move to X=10 ✗ Still blocked
- Eventually... ✓ Path clears
- Move to X=15 → JUMPS from X=5 to X=15 (catching up)
```

**The mismatch:**
- Actions assume they succeed
- Runtime validation can block them
- No feedback loop to adjust subsequent actions
- Character "catches up" with large jumps

---

## Solution Architecture

### 1. Builder Pattern Structure

```javascript
class CutsceneBuilder {
  constructor(cutsceneData) {
    this.rawData = cutsceneData;
    this.characters = cutsceneData.characterGroup.characters;
    this.divergences = [];
    this.segments = [];
  }

  // Main build method
  build() {
    const identifier = new DivergenceIdentifier(this.rawData);
    const diagnosis = identifier.validate();

    if (diagnosis.hasErrors()) {
      // Refuse to construct, return diagnosis
      return {
        success: false,
        diagnosis: diagnosis
      };
    }

    // Construction succeeded, return validated cutscene
    return {
      success: true,
      cutscene: new Cutscene(this.rawData)
    };
  }
}
```

### 2. Divergence Identifier (Simulation Engine)

```javascript
class DivergenceIdentifier {
  constructor(cutsceneData) {
    this.data = cutsceneData;
    this.simulatedState = this.initializeSimulation();
    this.conflicts = [];
  }

  validate() {
    // Simulate cutscene execution step by step
    let tick = 0;

    while (this.hasRemainingActions()) {
      const actionsThisTick = this.consumeActionsForTick(tick);

      // Validate each action in this tick
      for (const {character, action} of actionsThisTick) {
        const conflict = this.validateAction(character, action, tick);

        if (conflict) {
          this.conflicts.push({
            tick,
            character: character.id,
            action,
            conflict
          });

          // Segment here (mark point of divergence)
          this.segmentAt(tick);
        } else {
          // Apply action to simulated state
          this.applyAction(character, action);
        }
      }

      tick++;
    }

    return new DiagnosisObject(this.conflicts);
  }

  validateAction(character, action, tick) {
    // Use same validation as runtime (MovementPipeline)
    switch (action.type) {
      case 'move':
        // Check collision
        if (this.hasCollision(character, action.to)) {
          return new CollisionConflict(character, action, tick);
        }

        // Check terrain
        if (!this.hasValidTerrain(action.to)) {
          return new TerrainConflict(character, action, tick);
        }

        // Check will trigger gravity
        if (this.willFall(action.to)) {
          return new GravityWarning(character, action, tick);
        }

        return null; // No conflict
    }
  }

  hasCollision(character, targetPos) {
    // Check simulated positions of other characters at this tick
    return this.simulatedState.characters.some(other => {
      return other.id !== character.id &&
             other.position.x === targetPos.x &&
             other.position.y === targetPos.y &&
             other.position.z === targetPos.z;
    });
  }
}
```

### 3. Diagnosis Object (Error Reporting)

```javascript
class DiagnosisObject {
  constructor(conflicts) {
    this.conflicts = conflicts;
  }

  hasErrors() {
    return this.conflicts.some(c => c.severity === 'error');
  }

  hasWarnings() {
    return this.conflicts.some(c => c.severity === 'warning');
  }

  report() {
    // Generate human-readable report
    const report = {
      summary: `Found ${this.conflicts.length} issues`,
      details: this.conflicts.map(c => c.describe())
    };

    return report;
  }

  toConsole() {
    console.group('Cutscene Validation Report');
    console.log(`Total conflicts: ${this.conflicts.length}`);

    this.conflicts.forEach((conflict, i) => {
      console.group(`Conflict ${i + 1}: ${conflict.type}`);
      console.log(`Tick: ${conflict.tick}`);
      console.log(`Character: ${conflict.character}`);
      console.log(`Action:`, conflict.action);
      console.log(`Issue:`, conflict.describe());
      console.groupEnd();
    });

    console.groupEnd();
  }
}
```

### 4. Polymorphic Conflict Types

```javascript
// Base conflict class
class Conflict {
  constructor(character, action, tick) {
    this.character = character;
    this.action = action;
    this.tick = tick;
    this.severity = 'error'; // Override in subclasses
  }

  describe() {
    return "Generic conflict"; // Override
  }
}

// Specific conflict types
class CollisionConflict extends Conflict {
  constructor(character, action, tick, blockedBy) {
    super(character, action, tick);
    this.type = 'collision';
    this.blockedBy = blockedBy;
  }

  describe() {
    return `${this.character} cannot move to (${this.action.to.x}, ${this.action.to.y}, ${this.action.to.z}) - blocked by ${this.blockedBy}`;
  }
}

class TerrainConflict extends Conflict {
  constructor(character, action, tick) {
    super(character, action, tick);
    this.type = 'terrain';
  }

  describe() {
    return `${this.character} cannot move to (${this.action.to.x}, ${this.action.to.y}, ${this.action.to.z}) - invalid terrain (no ground)`;
  }
}

class GravityWarning extends Conflict {
  constructor(character, action, tick, fallDistance) {
    super(character, action, tick);
    this.type = 'gravity';
    this.severity = 'warning'; // Not an error, just FYI
    this.fallDistance = fallDistance;
  }

  describe() {
    return `${this.character} will fall ${this.fallDistance} blocks after moving to (${this.action.to.x}, ${this.action.to.y}, ${this.action.to.z})`;
  }
}
```

---

## Integration Workflow

### Cutscene Loading Process

```javascript
// OLD (Direct construction)
async function loadTestMap(mapName) {
  const config = await response.json();
  if (config.characterGroup) {
    initCharacterGroup(config.characterGroup); // Direct
  }
}

// NEW (Builder validation)
async function loadTestMap(mapName) {
  const config = await response.json();

  if (config.characterGroup) {
    // Build with validation
    const builder = new CutsceneBuilder(config);
    const result = builder.build();

    if (!result.success) {
      // Validation failed - show diagnosis
      console.error('Cutscene validation failed:');
      result.diagnosis.toConsole();

      // Don't initialize cutscene
      alert(`Cutscene has ${result.diagnosis.conflicts.length} issues. Check console.`);
      return;
    }

    // Validation passed - initialize
    initCharacterGroup(config.characterGroup);
  }
}
```

### Blueprint IDE Integration (Future)

```javascript
// User places action in IDE
function onActionPlaced(character, action) {
  // Validate incrementally
  const validator = new IncrementalValidator(currentBlueprint);
  const conflicts = validator.validateAction(character, action);

  if (conflicts.length > 0) {
    // Show conflicts in UI (but don't block placement)
    ui.showConflicts(conflicts);

    // User can:
    // 1. Fix now (remove/modify action)
    // 2. Fix later (mark as todo)
    // 3. Ignore (if they know it's ok)
  }
}
```

---

## Simulation State Management

### State Structure

```javascript
class SimulatedState {
  constructor(initialState) {
    this.characters = initialState.characters.map(c => ({
      id: c.id,
      position: {...c.startPosition},
      actionQueue: [...c.actionQueue],
      actionIndex: 0
    }));

    this.terrain = new Map(game.terrain); // Copy terrain state
    this.tick = 0;
  }

  // Get character by ID
  getCharacter(id) {
    return this.characters.find(c => c.id === id);
  }

  // Apply action to simulated state
  applyAction(character, action) {
    switch (action.type) {
      case 'move':
        character.position = {...action.to};
        break;
      case 'wait':
        // No position change
        break;
    }

    character.actionIndex++;
  }

  // Clone state for branching simulation
  clone() {
    return new SimulatedState({
      characters: this.characters.map(c => ({
        ...c,
        position: {...c.position},
        actionQueue: [...c.actionQueue]
      }))
    });
  }
}
```

---

## Segmentation Strategy

### Why Segment?

When a conflict occurs, the cutscene is "broken" at that point. Segmentation allows:
1. Continue validation after the conflict
2. Find ALL issues, not just the first one
3. Provide complete diagnosis

### Implementation

```javascript
class CutsceneSegment {
  constructor(startTick, endTick, valid) {
    this.startTick = startTick;
    this.endTick = endTick;
    this.valid = valid;
    this.conflicts = [];
  }
}

// In DivergenceIdentifier
segmentAt(tick) {
  if (this.currentSegment) {
    this.currentSegment.endTick = tick;
    this.segments.push(this.currentSegment);
  }

  // Start new segment after conflict
  this.currentSegment = new CutsceneSegment(tick + 1, null, false);
}
```

---

## Advantages of This Approach

### 1. Compile-Time Safety
- Catch issues before runtime
- No surprises during cutscene playback
- Author fixes issues upfront

### 2. Better Error Messages
- Specific conflict types
- Polymorphic descriptions
- Context (tick, character, action)

### 3. Dual Purpose
- Cutscene validation (now)
- Blueprint IDE validation (future)
- Same infrastructure, different UI

### 4. Extensible
- Add new conflict types easily
- Add new action types with validation
- Customize severity levels

### 5. Simulation Accuracy
- Uses same validation as runtime (MovementPipeline)
- Simulates actual execution
- Accurate collision/terrain checks

---

## Implementation Phases

### Phase 1: Core Builder
- [ ] `CutsceneBuilder` class
- [ ] `DivergenceIdentifier` simulation
- [ ] `DiagnosisObject` reporting
- [ ] Integrate with loadTestMap

### Phase 2: Conflict Types
- [ ] `CollisionConflict`
- [ ] `TerrainConflict`
- [ ] `GravityWarning`
- [ ] Base `Conflict` class

### Phase 3: Simulation Engine
- [ ] `SimulatedState` management
- [ ] Action application
- [ ] Collision checking
- [ ] Terrain validation

### Phase 4: Reporting
- [ ] Console output formatting
- [ ] Segmentation display
- [ ] Conflict grouping
- [ ] Summary statistics

### Phase 5: Testing
- [ ] Create intentionally broken cutscene
- [ ] Validate diagnosis output
- [ ] Verify all conflict types caught
- [ ] Test segmentation

### Phase 6: Blueprint Integration (Future)
- [ ] Incremental validation
- [ ] Real-time feedback UI
- [ ] Fix suggestions
- [ ] Undo/redo support

---

## Open Questions

1. **Severity Levels**: Error vs Warning vs Info?
   - Error = blocks construction
   - Warning = allowed but flagged
   - Info = FYI (like gravity triggers)

2. **Auto-Fix**: Should builder attempt repairs?
   - Pro: Convenience
   - Con: May not match intent
   - Decision: No auto-fix, just diagnose

3. **Partial Execution**: Allow "best effort" playback?
   - Run until first conflict, then stop?
   - Or refuse entirely if any conflicts?
   - Decision: Refuse entirely (safer)

4. **Performance**: Simulation overhead?
   - For cutscenes: negligible (small scale)
   - For blueprints: may need optimization
   - Future: Cache, incremental validation

---

## Relationship to Other Patterns

### Movement Strategy Pattern
- Builder USES strategy validation
- Simulates MovementPipeline checks
- Same rules, different context (compile vs runtime)

### Constraint Interface Pattern
- Constraints define what's possible
- Builder validates against constraints
- Future: Integrate constraint queries

### Template Composition System
- Templates will need validation too
- Same builder pattern applies
- Validate template before save

---

**This pattern emerged from cutscene testing. It's the foundation for compile-time validation of both cutscenes and user-created blueprints.**

**Next Step:** Implement Phase 1 (Core Builder) and test with intentionally broken cutscene

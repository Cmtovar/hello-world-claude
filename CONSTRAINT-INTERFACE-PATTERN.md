# Constraint Interface Pattern

**Date:** 2026-01-29
**Status:** Design exploration

## Core Concept

Constraints are not just test helpers - they're **interface signatures for spatial interaction**.

## Three Use Cases

### 1. Test Validation (Current)
```json
{
  "constraints": {
    "allowedInputs": ["w", "d"],
    "blockCardinal": true
  }
}
```
Purpose: Verify specific mechanic works in isolation.

### 2. Level Design Patterns (Intended)
**Map specification:**
```
"This wall position requires: Constraint Type B"
  - Blocks horizontal approach
  - Allows vertical descent
```

**Object pool:**
- Ornate wall (Type B) ✓
- Iron fence (Type B) ✓
- Hedge maze (Type B) ✓
- Wooden door (Type A) ✗

**Benefit:** Designer specifies interface, not implementation. Objects are interchangeable if they match the constraint signature.

### 3. Gameplay Mechanics (Emergent possibility)
**Status effects using constraints:**
- Frozen: `{ "blockDiagonal": true }` - can only move cardinal
- Webbed: `{ "maxMovements": 1 }` - limited range
- Flying: `{ "ignoreAutoClimb": true }` - different movement rules

**Terrain effects:**
- Mud: Adds movement cost
- Ice: Adds slide constraint
- Wind: Directional movement modifier

## Throne Example (Directional Constraints)

```json
{
  "position": [5, 1, 5],
  "constraintZones": {
    "north": { "allowSit": true },   // Front approach
    "south": { "blockClimb": true }, // Back approach
    "east": { "blockClimb": true },  // Side approach
    "west": { "blockClimb": true }   // Side approach
  }
}
```

**Same physical object, different affordances based on approach vector.**

## Design Philosophy

> "Constraints encode what's *possible*, not just what's *blocked*."

Objects have:
1. **Physical properties** (mesh, position, color)
2. **Interaction interfaces** (constraint signatures)
3. **Contextual behavior** (directional, status-based)

## Implications

### For Level Design
- Maps specify *required interfaces* at positions
- Objects that satisfy interface are valid
- Swap art assets without changing gameplay
- Easier to prototype: use placeholder → replace with specific later

### For Balancing
- Nerf a unit by changing its constraint signature
- "Ground units can no longer auto-climb height 2"
- Change constraint type, not movement code

### For Modding
- Modders add new objects with known constraint types
- As long as interface matches, it works
- No code changes needed

## Open Questions

1. **Constraint Composition:** Can objects have multiple constraint types?
   - Example: Throne is "Sittable + Blocking"

2. **Dynamic Constraints:** Can constraints change at runtime?
   - Example: Door starts as "Blocking", becomes "Passable" when opened

3. **Constraint Priority:** What if multiple constraints conflict?
   - Example: Status effect says "block diagonal" but terrain says "allow all"

4. **Constraint Inheritance:** Do unit types inherit base constraints?
   - Example: All fliers inherit "ignore auto-climb"

## Next Steps

- [ ] Formalize constraint type taxonomy
- [ ] Design constraint composition rules
- [ ] Prototype directional constraints (throne example)
- [ ] Build level editor with constraint interface selectors
- [ ] Document constraint signatures for each game object

---

**Related Patterns:**
- Duck typing (programming)
- Interface-based design
- Dependency injection (for level design)
- Affordance theory (game design)

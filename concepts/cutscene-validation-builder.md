# Cutscene Validation Builder Pattern - Primary Source

**Date:** 2026-01-30
**Context:** Emerged from cutscene-test-02-complex runtime conflicts
**Type:** Design intent (primary source)

---

## User's Exact Words (Primary Source)

> "it looks like... hmm, yeah, we somewhat have run into a problem with declarative approach, the absolute positions of the cutscene contrast at runtime with the declarative approach. this successfully blocked, but then the character that got blocked expected to not get blocked, therefore attempted jumping to the same position again and again but kept getting blocked and then finally when it didn't get blocked it did a huge jump to catch back up. this is because absolute positioning expects it to work, but it fails at runtime.
>
> either we express the cutscene relatively in terms of actions that represent the cutscene, or we... try to interpret a proposed cutscene? I think this is a builder pattern in the works. we want to build a complex cutscene object, and we have inputs nest in polymorphic interface design patterns, therefore, we need... this builder to accept the inputs that would have gone to the cutscene constructor and then we handle preprocessing.
>
> I wonder though... what should happen if the cutscene we attempt to load in has problems, should it refuse to construct? probably? that way at compile time we know the cutscene won't work and then we reprogram it? or send the user defined error to be handled in a diagnosis response object that identifies the moments that a divergence from absolute plans occurs. then... it segments the action plan at the inaccuracy, tries to continue with the remainder of the cutscene, and each time it encounters an inaccuracy, data is stored about the conflict and the diagnosis object shares that data in the error message.
>
> something like that. this type of infrastructure would be useful to have when the user is creating their own blueprint plans since they'll probably be doing moves and then it can diagnose conflicts in quick response to each new action the user places on the blueprint screen. that way the user can put actions down know if there's a conflict immediately, then choose when to fix it (either now or later). this same process can help with crafting these sorts of cutscenes.
>
> and since it's compile time, I think you can benefit from this. so it combines a divergence identifier and a diagnoser. the identifier is a builder pattern that parses the action sequence intended for the cutscene constructor, and flags inaccuracies, segments off this part of the cutscene, then parses the remaining action data, each time segmenting if an inaccuracy is flagged. if any flags occurred, don't construct, instead hand the flags over to the diagnoser to handle these errors at compile time with some sort of polymorphic error message that is appropriate for this specific issue that occurred when building the cutscene.
>
> this way infrastructure like this supports creating cutscenes like this but also supports users creating their own blueprint plans. this aims to balance the issue of dynamic vs static declaration. a lagrangian eulerian issue handled through the build process."

---

## Context

**What happened:**
- Cutscene defined with absolute positions (move to X=5, X=10, X=15)
- Runtime collision detection blocked a move
- Character kept retrying the same position, getting blocked repeatedly
- Eventually jumped to catch up when path cleared
- Mismatch between static plan (cutscene) and dynamic execution (validation)

**The conflict:**
- **Static/Lagrangian**: Cutscene as fixed plan (absolute positions)
- **Dynamic/Eulerian**: Runtime validation changes what's possible
- When validation blocks a move, the plan is now invalid
- But the action queue still expects absolute positions to work

---

## Design Intent

### Core Problem
Absolute positioning in cutscenes assumes success, but runtime validation can cause failure. Need to reconcile:
1. **Compile-time**: Validate cutscene before execution
2. **Runtime**: Handle dynamic conflicts gracefully
3. **User feedback**: Immediate diagnosis for blueprint creators

### Solution Components

1. **Builder Pattern**:
   - Don't construct cutscene directly
   - Builder preprocesses action sequences
   - Validates before construction

2. **Divergence Identifier**:
   - Parses action sequence
   - Simulates execution
   - Flags conflicts (collision, terrain, etc.)
   - Segments cutscene at conflict points

3. **Diagnosis Object**:
   - Collects all flagged conflicts
   - Stores context (which character, which action, why failed)
   - Polymorphic error messages per conflict type
   - Returns detailed report if construction fails

4. **Compile-time Validation**:
   - If any flags: refuse to construct, return diagnosis
   - User fixes issues before cutscene runs
   - Prevents runtime surprises

### Dual Purpose

**Cutscene Creation** (Now):
- Author defines cutscene
- Builder validates
- Diagnosis reports conflicts
- Author fixes, rebuilds

**Blueprint IDE** (Future):
- User places actions on blueprint
- Each action immediately validated
- Conflicts shown in real-time
- User can fix now or later
- Same infrastructure, different UI

---

## Lagrangian vs Eulerian

**Lagrangian approach** (following the particle):
- Track each character's intended path
- Absolute positions over time
- "Move to X=5, then X=10, then X=15"

**Eulerian approach** (observing the field):
- Track state of the world at each moment
- What's possible given current conditions
- "Move forward if no collision, otherwise wait"

**The conflict:**
- Cutscene is Lagrangian (planned path)
- Validation is Eulerian (current state)
- Builder pattern reconciles through simulation

---

## User's Vision

> "this type of infrastructure would be useful to have when the user is creating their own blueprint plans"

The same system that validates cutscenes will validate user-created templates:
- Immediate feedback
- Clear error messages
- Choice to fix now or later
- Compile-time safety

> "this aims to balance the issue of dynamic vs static declaration. a lagrangian eulerian issue handled through the build process."

The builder simulates execution (Eulerian) to validate the plan (Lagrangian), giving compile-time guarantees for runtime behavior.

---

**Next:** Create interpretation document analyzing implementation approach

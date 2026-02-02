# Developer Style Guide

**Purpose:** Help future Claude sessions understand my thinking patterns, preferences, and working style.

**Last Updated:** 2026-01-29

---

## Core Design Philosophy

### Declarative Over Imperative
I prefer systems where you *declare what should be possible* rather than *code every specific behavior*.

**Example:** Constraint interface pattern
- Don't code: "If throne and approaching from north, allow sit"
- Instead: Declare constraint zones, let the system handle it

### Emergent Over Prescribed
I like when complex behavior emerges from simple, composable rules.

**Example:** Constraint composition
- Simple rule: Objects have constraint signatures
- Simple rule: Map positions require constraint types
- Emergent: Objects become interchangeable, modding becomes easy, balancing becomes declarative

### Interface-Based Thinking
I think in terms of **affordances** - what actions are *possible* in a given context.

Not: "This is a throne"
But: "This is an object with [sittable from north, blocking from other sides]"

### Systems as Tools for Future Me
I build patterns and abstractions to make *future level design* easier, not just to solve immediate problems.

**Example:** Constraint types as reusable interfaces
- Current: Helps with testing
- Future: Helps with level design, balancing, modding

---

## Communication Preferences

### Natural Emergence Over Rigid Planning
> "Let the objective for this session emerge naturally"

I prefer:
- Starting with exploration and discussion
- Letting goals crystallize through conversation
- Capturing insights as we discover them

I don't prefer:
- Rigid upfront planning
- Fixed session agendas
- Premature commitment to specific tasks

### Thinking Out Loud
I value **collaborative thinking** - exploring ideas together, writing notes as we go.

When I say something interesting, it's good to:
1. Reflect it back to confirm understanding
2. Extend it with related implications
3. Capture it in documentation
4. Ask clarifying questions

### Comfort with Ambiguity
I'm comfortable with:
- Design patterns that aren't fully specified yet
- Placeholder archetypes (Ground, Flier, etc.)
- Systems that will "eventually" do something

I see the big picture and trust the details will emerge.

---

## Technical Preferences

### Abstraction Levels
I think in **layered abstractions**:

**Concrete → Generic → Interface**

Example from today:
- Concrete: "Rainbow Unicorn that leaves floating platforms"
- Generic: "Flier unit type"
- Interface: "Object with temporary-terrain constraint signature"

### Composition and Interchangeability
I value systems where:
- Components are **interchangeable** if they match an interface
- New behaviors emerge from **composing** existing pieces
- Design patterns act as **aids** rather than rigid rules

### Future-Proofing Through Flexibility
Decisions like:
- Constraint system for tests → but designed to be useful for gameplay
- Generic unit types → but room for specific creative implementations
- Test-driven development → but tests become building blocks for levels

**Pattern:** Build tools that serve multiple purposes across different scales.

---

## Design Patterns I Gravitate Toward

### 1. Interface Segregation
Objects expose what they *can do*, not what they *are*.

Throne = { Sittable, Blocking, Directional }
Not: { Throne, RegalFurniture, GameObject }

### 2. Duck Typing Philosophy
"If it walks like a duck and quacks like a duck..."

If two objects have the same constraint signature, they're interchangeable at that position.

### 3. Data-Driven Design
Prefer JSON configuration over hardcoded behavior.

Movement constraints in JSON → Designer changes, not programmer.

### 4. Separation of Concerns (Spatial)
Different layers handle different aspects:
- Base terrain
- Dynamic terrain (unicorn platforms)
- Unit constraints
- Status effects

Each layer uses the same *constraint language* but manages different *lifetimes*.

---

## How I Approach Problems

### Start Big Picture, Fill In Details Later
1. Identify the **pattern** or **system** needed
2. Sketch out the **interfaces**
3. Leave **placeholders** for specifics
4. Trust that implementation details will emerge

### Question-Driven Exploration
I learn by asking:
- "What if this could also do X?"
- "Could this pattern apply to Y?"
- "What emerges if we compose these?"

### Concrete Examples First
When explaining abstract concepts, I jump to **specific scenarios**:
- Throne with directional constraints
- Rainbow Unicorn's temporary platforms
- Status effect that blocks diagonal movement

Then generalize from there.

---

## What Excites Me

### Creative Unit Concepts
Not just "ground unit" but:
- Rainbow Unicorn (temporary platforms for allies)
- ODM gear (Attack on Titan grappling)
- Climbers with unique wall-scaling

**Pattern:** Specific, flavorful abilities grounded in clear mechanics.

### Emergent Complexity
Simple rules that create rich possibility spaces:
- Constraint interfaces → modding, balancing, level design
- Micro-maps → macro-level composition
- Test infrastructure → gameplay systems

### Systems That Scale
Building something that:
- Works now for simple cases
- Extends naturally for complex cases
- Doesn't need to be rewritten when scope grows

---

## Red Flags (What Frustrates Me)

Based on what I gravitate toward, I likely get frustrated by:

- **Overly rigid systems** that can't adapt
- **Hardcoded special cases** instead of general patterns
- **Premature optimization** before understanding the problem
- **Closed architectures** that don't allow composition
- **Implementation before interface** - coding before designing the abstraction

---

## Collaboration Style

### I Value:
- **Thinking partners** who extend ideas
- **Pattern recognition** - noticing recurring themes
- **Documentation as we go** - capturing insights in the moment
- **Asking good questions** that open new directions

### Good Responses to My Ideas:
✓ "Oh, so that means X could also work?"
✓ "That's similar to [pattern Y] in [context Z]"
✓ "Let me capture this thinking in a doc"
✓ "What about edge case A?"

### Less Helpful Responses:
✗ "Let's implement this specific thing right now"
✗ "We need a complete spec before proceeding"
✗ "That's too abstract to be useful"
✗ "Just tell me exactly what you want"

---

## Current Project Patterns

### Test-Driven, But Flexible
- Tests define mechanics in isolation
- But tests are *building blocks*, not just validation
- Micro-maps compose into macro-maps
- Test infrastructure becomes gameplay tooling

### Single File, But Modular Thinking
- Everything in index.html (no build step)
- But clear logical separation
- Comments as section headers
- Functions as composable units

### Documentation-Heavy
- `docs/design/ARCHITECTURE.md`, `docs/design/DESIGN-DECISIONS.md`, `docs/guides/METHODOLOGY.md`
- Capture *why*, not just *what*
- Documentation as thinking tool, not afterthought

### Placeholder-Driven Development
- Generic unit types now
- Specific creative units later
- Trust that the abstraction will hold

---

## Key Vocabulary

When I say... | I mean...
---|---
**Affordances** | What actions are possible in a context
**Interface** | The contract/signature, not implementation
**Emergent** | Behavior arising from simple rule composition
**Declarative** | Specify *what*, not *how*
**Constraint signature** | The set of interaction rules an object exposes
**Building blocks** | Reusable patterns that compose into larger structures
**Design pattern aid** | Tool that makes future design easier

---

## Session Flow Preference

1. **Exploration** - Discuss, think out loud, explore connections
2. **Capture** - Write notes/docs when insights emerge
3. **Crystallize** - Let objectives become clear through discussion
4. **Execute** - Then implement once we know what we're doing

**Not:**
1. Plan everything upfront
2. Execute according to plan
3. Document after the fact

---

## Questions to Ask Me

Good questions that help me think:

- "What's the interface here?"
- "How does this compose with X?"
- "What emerges from combining these?"
- "What's the constraint signature?"
- "Is this a building block or a specific implementation?"
- "How does this scale?"
- "What patterns are recurring?"

---

## Notes for Future Sessions

- **Don't rush to implementation** - I value thinking time
- **Capture insights as we go** - don't wait for "later"
- **Extend ideas, don't just confirm** - be a thinking partner
- **Notice patterns** - I appreciate when you spot recurring themes
- **Ask about interfaces** - I think in terms of abstractions
- **Trust the process** - objectives will emerge

---

**This is a living document. Future sessions should add observations as you learn more about my working style.**

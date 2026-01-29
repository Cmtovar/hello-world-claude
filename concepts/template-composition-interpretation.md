# Template Composition System - Interpretation

**Date:** 2026-01-29
**Interpreter:** Claude (Session 2026-01-29)
**Primary Source:** `template-composition-system.md`

---

## The Big Insight: Templates Are Functions

Templates aren't just saved action sequences. They're **composable functions** with:
- Control flow (if conditions)
- Parameters (which units, where to execute)
- Composition (templates can call other templates)
- Idempotency (can extract sub-templates into new contexts)

**This is a programming language for tactical coordination.**

---

## Control Complexity = Control Flow

### When they said "control complexity" as an upgrade path, they meant:

**Level 1:** Simple sequence
```
Template: "Advance Line"
- Unit A: Move forward 3
- Unit B: Move forward 3
- Unit C: Move forward 3
```

**Level 2:** Conditional logic
```
Template: "Adaptive Advance"
- IF path clear:
    - Advance Line
- ELSE IF enemies detected:
    - Defensive Formation
- ELSE:
    - Scout Forward
```

**Level 3:** Nested composition with optionals
```
Template: "Complex Assault"
- Check enemy position
- IF flanks exposed:
    - Execute "Pincer Maneuver"
    - OPTIONAL: "Unicorn Sky Trail" (if unit available)
- ELSE:
    - Execute "Frontal Push"
    - Execute "Support Fire"
```

### Upgrades unlock:
- More if/else branches
- Deeper nesting levels
- More optional sub-templates
- More parameter passing between templates

---

## Composition Architecture

### Pull Template Into Frame
```
Template A contains Template B

When executing A:
- B runs within A's context
- B inherits A's parameters
- B's results feed back to A
```

**Example:**
```
"Surround and Collapse"
  ├─ "Pincer Maneuver" (inherited: target position)
  ├─ "Close the Gap"
  └─ "AoE Strike" (conditional on formation)
```

### Extract Template From Frame (Idempotent)
If `"Pincer Maneuver"` is useful on its own, you can extract it from `"Surround and Collapse"` and use it independently.

**Key concept:** Templates are modular. They work standalone OR as components.

### Mix and Match
```
Player builds new template:
- Drag "Pincer Maneuver" into slot 1
- Drag "Defensive Formation" into slot 2
- Add condition: If HP < 50%, execute slot 2 instead of slot 1
```

This is visual programming for tactics.

---

## Two UI Contexts

### In-Battle UI (Blueprint Mode)
**Purpose:** Quick execution in the heat of combat

**Features:**
- Fast access to saved templates
- Quick parameter adjustment (which units, where)
- Minimal detail, maximum speed
- "Call function" style - just execute

**UX Goal:** Don't get stuck in menus. Plan → Execute → See results

---

### Out-of-Battle UI (Template Editor)
**Purpose:** Deep design without time pressure

**Features:**
- Detailed template composition
- Drag-and-drop control flow
- Test templates in simulation
- View all available sub-templates
- Manage template library

**Physical Location:** Two buildings in village/resting area:
1. **Tactics Hall** - Template editor, detailed design
2. **Strategy Library** - Read guides, study patterns

**UX Goal:** This is where learning happens. No rush, explore deeply.

---

## In-Game Learning System

### Teaching Players to Program

The game teaches tactical composition through in-game resources:

#### 1. Prescriptive (Pre-built Patterns)
**Books/Scrolls:**
- "The Art of the Pincer: A Classic Maneuver"
- "Defensive Formations for Outnumbered Forces"
- "Advanced: Conditional Tactics"

**What they provide:**
- Pre-built templates players can use immediately
- Study the structure to understand composition
- Like learning from example code

#### 2. Conceptual (Principles)
**NPCs/Mentors:**
- "Templates work best when they're small and focused"
- "Use conditions to handle different scenarios"
- "Defensive templates should be reusable across many situations"

**Books on Theory:**
- "Principles of Modular Tactics"
- "When to Compose, When to Specialize"
- "Flow Design: Creating Unit Arteries"

**What they provide:**
- Understanding WHY patterns work
- Ability to create novel templates
- Like learning programming concepts, not just syntax

#### 3. Experiential (Discovery)
**Training Grounds:**
- Safe space to test templates
- See what works, what doesn't
- No consequences for failure

**Battle Feedback:**
- "This template failed because..."
- "Enemies adapted by..."
- Learn from actual use

---

## Design Pattern Library (In-Game)

### Categories Players Learn

#### Basic Patterns
- **Advance Line** - Move everyone forward
- **Retreat Line** - Move everyone back
- **Hold Position** - Wait for enemies

#### Intermediate Patterns
- **Pincer Maneuver** - Flank from two sides
- **Defensive Box** - Surround vulnerable unit
- **Bait and Switch** - Lure, then ambush

#### Advanced Patterns
- **Adaptive Response** - Conditionally choose tactics
- **Coordinated Assault** - Multi-phase attack
- **Flow Management** - Maintain unit arteries while attacking

#### Expert Patterns
- **3D Vertical Assault** - Use height levels coordinated
- **Constraint Breaking** - Shatter enemy formations
- **Sky Trail Exploitation** - Unicorn platform chains

### Enemies Use These Too

**Progression:**
- Early game: Enemies use Basic patterns
- Mid game: Enemies use Intermediate, introduce Advanced
- Late game: Enemies compose Expert patterns

**Learning curve:** Fight enemies using patterns, then unlock those patterns for yourself.

---

## The Educational Game Design Angle

### What Players Are Actually Learning

**Software Engineering Concepts:**
- Functions and composition
- Control flow (if/else)
- Modularity and reusability
- Abstraction (templates hide complexity)
- Parameters and context

**Tactical Thinking:**
- Pattern recognition
- Conditional decision-making
- Adaptability vs consistency
- Resource management (space, time, units)

**This is teaching computational thinking through gameplay.**

---

## Progression System Through Composition

### Early Game
- 3 template slots
- No control flow (just sequences)
- 2 units max per template
- Pre-built patterns only

### Mid Game
- 5 template slots
- Simple if/else unlocked
- 4 units per template
- Can compose 2 templates (1 level deep)
- Can edit pre-built patterns

### Late Game
- 10 template slots
- Complex control flow (nested conditions)
- 8 units per template
- Composition unlimited depth
- Full custom template creation

### Progression Feel
**Critical but optional:**
- You CAN play without templates (manual every action)
- Templates make complex battles manageable
- Expert players express mastery through template design
- Progression gates feel like "unlocking more expressive power"

---

## Idempotency & Extraction

### What "Idempotent" Means Here

A template is **idempotent** if:
- It can run standalone
- OR as part of another template
- Without changing behavior

**Example:**
```
"Pincer Maneuver" works:
- By itself (player manually triggers)
- Inside "Surround and Collapse" (automatically called)
- Inside "Adaptive Response" (conditionally called)

Same definition, same behavior, different contexts.
```

### Extraction Workflow

**Player discovers:**
"Wait, this 3-step sequence inside my 'Complex Assault' template is useful on its own."

**Extraction:**
1. Select the 3 steps
2. "Extract to new template"
3. Name it "Flank Rush"
4. Now "Complex Assault" calls "Flank Rush"
5. And "Flank Rush" can be used independently

**This is refactoring in real-time.**

---

## UI/UX Implications

### In-Battle (Quick Use)
```
Blueprint Mode UI:
┌─────────────────────────────┐
│ Ready Units: A, B, C        │
├─────────────────────────────┤
│ Templates:                  │
│ [Pincer]  [Defend]  [Retreat]│
│ [Custom1] [Custom2]         │
├─────────────────────────────┤
│ Manual Actions:             │
│ [Move] [Attack] [Skill]     │
└─────────────────────────────┘

Click template → Units auto-assigned → Execute
```

### Out-of-Battle (Deep Design)
```
Template Editor:
┌─────────────────────────────┐
│ Template: "Adaptive Assault"│
├─────────────────────────────┤
│ IF enemy formation = tight: │
│   ├─ Execute "AoE Barrage"  │
│   └─ Execute "Pincer"       │
│ ELSE IF formation = spread: │
│   └─ Execute "Chase Down"   │
│ ELSE:                       │
│   └─ Execute "Default Adv"  │
├─────────────────────────────┤
│ Available Templates:        │
│ [Drag to compose]           │
│ - Pincer Maneuver           │
│ - AoE Barrage              │
│ - Chase Down                │
└─────────────────────────────┘

Drag and drop composition
Visual control flow building
```

---

## Testing Strategy for This System

### Test Layers

**1. Template Execution**
- Single template runs correctly
- Parameters passed properly
- Units execute actions

**2. Template Composition**
- Parent calls child correctly
- Context inherited properly
- Results bubble up

**3. Control Flow**
- If conditions evaluate correctly
- Correct branch executes
- Edge cases handled (no valid branch, etc.)

**4. Extraction/Idempotency**
- Extracted template works standalone
- Still works when called from parent
- No side effects

**5. UI Interactions**
- In-battle quick-use works
- Out-of-battle editor saves correctly
- Drag-and-drop composition functional

### Interface Design
```
Interface: Template
  - execute(units, context)
  - canExecute(units, context) -> bool
  - getSubTemplates() -> Template[]
  - serialize() -> JSON

Interface: Condition
  - evaluate(context) -> bool

Interface: ControlNode
  - IF(condition, template)
  - ELSE(template)
  - OPTIONAL(template, condition)
```

Test against interfaces, not implementations.

---

## Emergent Complexity (Again)

### Simple Building Blocks:
1. Templates are composable functions
2. Control flow nodes (if/else/optional)
3. Two UI contexts (quick vs deep)
4. In-game learning (prescriptive + conceptual)
5. Progression unlocks complexity

### What Emerges:
- Players develop personal tactical "languages"
- Community shares templates (like sharing code)
- Meta strategies around template design
- Speedrunners optimize template libraries
- New players learn by copying, then modifying
- Expert players create generalized, reusable patterns
- Teaching moments happen organically (fighting enemies teaches patterns)

**The game becomes a platform for tactical expression.**

---

## Connection to Fire Emblem

Fire Emblem has:
- Pre-set units with fixed abilities
- Turn-based, sequential actions
- Focus on individual unit positioning

This game has:
- **Templates make units programmable**
- Parallel, coordinated actions
- Focus on **collective choreography**

**It's like going from assembly programming (move each unit manually) to high-level programming (write functions that coordinate units).**

---

## Open Questions

1. **Template Sharing:**
   - Can players export/import templates?
   - Is there a community template library?
   - Do templates work across different unit compositions?

2. **Enemy Template Visibility:**
   - Can players see enemy templates after defeating them?
   - Are enemy patterns telegraphed before execution?
   - Can you "steal" enemy patterns?

3. **Template Limits in Battle:**
   - How many templates can execute simultaneously?
   - Is there a "stack depth" limit for composition?
   - Can templates interrupt other templates?

4. **Failure Handling:**
   - What if a sub-template fails (unit dies, path blocked)?
   - Does the parent template continue?
   - Can templates have fallback logic?

5. **Parameter Passing:**
   - How specific are parameters (exact units vs "any flier")?
   - Can templates accept "unit types" as parameters?
   - Dynamic assignment based on current state?

---

## The Two Buildings (Out-of-Battle)

### Building 1: Tactics Hall (Template Editor)
**Interior:**
- Large table with tactical maps
- Movable unit figurines
- Scrolls with template diagrams
- Interactive editor on table (magical/tech)

**NPCs:**
- Tactician mentor (teaches concepts)
- Veteran soldiers (share their patterns)

**Activities:**
- Design new templates
- Compose existing templates
- Test in simulation
- Manage template library

---

### Building 2: Strategy Library (Learning Center)
**Interior:**
- Bookshelves with tactical manuals
- Reading areas
- Display cases with famous battles
- Interactive history (see famous tactics animated)

**NPCs:**
- Librarian (helps find relevant books)
- Scholars (explain theory)
- Other players (share experiences)

**Activities:**
- Read about design patterns
- Study pre-built templates
- Watch battle replays
- Unlock new pattern concepts

---

### The Flow

**Between battles:**
1. Visit Library → Learn new concepts
2. Visit Tactics Hall → Design templates using concepts
3. Test templates in Training Grounds
4. Return to battle with new tools

**This is the progression loop for strategic depth.**

---

## Why This Works

### Cognitive Load Management
- **In battle:** Quick decisions, execute templates
- **Out of battle:** Deep thinking, design templates

Separates "planning" from "execution" across time.

### Scaffolded Learning
- **Early:** Use pre-built templates (learn by doing)
- **Mid:** Modify templates (learn structure)
- **Late:** Create from scratch (learn principles)

Gentle ramp from novice to expert.

### Expressive Mastery
Expert players don't just "know more tactics."
They **express mastery through elegant template design.**

Like speedrunners optimize routes, tactical players optimize template libraries.

---

## Implementation Implications

### Data Structures
```javascript
Template {
  id: string,
  name: string,
  description: string,
  nodes: ControlNode[],
  subTemplates: Template[],
  maxUnits: number,
  requirements: Condition[]
}

ControlNode {
  type: "sequence" | "if" | "else" | "optional",
  condition?: Condition,
  actions: Action[],
  subTemplates: Template[]
}
```

### Editor UI
- Visual programming interface (like Scratch or Blueprints)
- Drag-and-drop composition
- Live preview/simulation
- Syntax checking (can this template be executed?)

### Battle UI
- Template selector (filtered by available units)
- Quick parameter adjustment
- Visual feedback (show what will execute)
- Interrupt/cancel mechanisms

---

**Related Documents:**
- `template-composition-system.md` - Primary source
- `blueprint-mode-design.md` - Core system design
- `blueprint-mode-interpretation.md` - System interpretation
- `CONSTRAINT-INTERFACE-PATTERN.md` - How constraints enable this

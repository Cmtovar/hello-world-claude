# Progression Through Units - Interpretation

**Date:** 2026-01-29
**Interpreter:** Claude (Session 2026-01-29)
**Primary Source:** `progression-through-units.md`

---

## The Core Philosophy

**What's NOT gated:** Player creativity, template design tools, tactical knowledge
**What IS gated:** Unit capabilities, execution power, battlefield presence

> "The player isn't limited, but their units are."

This is a fundamental design choice that respects player intelligence while still creating progression.

---

## Learning from Combat (Open Source Style)

### Action History System

**During/After Battle:**
- View replay of enemy actions
- Decompose complex patterns into micro-pieces
- See the "source code" of what happened

**Example: Enemy Falcon Arc Attack**

What you see in real-time:
```
Falcon swoops down in an arc, attacks mid-flight, lands with second attack
```

What you study in action history:
```
1. Move displacement: (0,0,0) → (2,1,0)
2. Move displacement: (2,1,0) → (4,2,1)
3. Attack action (consumes 30% AP)
4. Move displacement: (4,2,1) → (5,1,2)
5. AP recap event (restored 50% AP)
6. Attack action (consumes 30% AP)
7. Move displacement: (5,1,2) → (5,0,2) [land]
```

**Now you understand:**
- This is composable micro-pieces
- The arc is just movement + attack + movement
- AP recaps mid-sequence
- You could recreate this pattern with your own units (if they can fly)

### "Open Source" Learning

Like reading someone else's code:
- You see HOW it works (action history)
- You understand WHY it works (declarative constraints satisfied)
- You can ADAPT it (change parameters, unit types)
- You can COMPOSE it (use as part of larger template)

**The game teaches systems thinking by showing you the systems.**

---

## Template Design Tools: Fully Open

### What's Available from the Start

**All control flow:**
- Sequential actions
- If/else conditions
- Optional branches
- Nested composition

**All design patterns:**
- Can create any template structure
- Limited only by nesting depth (for balance)
- Limited by number of templates (upgradable for convenience)

**Philosophy:**
> "A player can think about anything, so they should be able to design anything."

### Why This Works

**Player creativity is infinite**, so don't gate it.

**Unit capabilities are finite**, so gate those instead.

**Result:**
- Engaged players design intricate templates early
- Those templates sit in library, waiting for units that can execute them
- Progression becomes: "How do I get units to do this cool thing I designed?"
- Aspirational design - you plan for future capabilities

---

## Progression Through Unit Capabilities

### Units Are the Variables

**Knight unit:**
- Can hold shield (defensive action)
- Medium AP regen
- Ground movement only
- Cannot create sky platforms

**Unicorn unit:**
- Can create sky trail (special action)
- Fast AP regen
- Flight movement
- Low defense

**Templates don't care about unit identity, they care about capabilities:**

```
Template: "Sky Platform Chain"
Requirements:
  - Unit with "create platform" ability
  - Unit with "flight" movement type

Can execute with:
  ✓ Rainbow Unicorn
  ✓ Sky Mage (hypothetical future unit)
  ✗ Knight (missing required abilities)
```

### Equipment as Capability Modifiers

**Not just cosmetic:**

**Shield:**
- Adds "block" action
- Reduces AP regen by 10%
- Changes unit signature

**Sword:**
- Adds "slash" action
- No AP penalty
- Different tactical role

**Heavy Armor:**
- Adds "tank" capability
- Reduces movement range
- Drastically reduces AP regen

**Light Gear:**
- Increases movement range
- Increases AP regen
- Removes defensive capabilities

### Dynamic Unit Signatures

A unit's **action interface** changes based on:
- Base unit type
- Equipped items
- Current buffs/debuffs
- Temporary status effects

**This means templates can become valid/invalid dynamically.**

---

## AP Regen as Balance Lever

### Different Units, Different Rates

**Fast Rechargers (Scouts, Fliers):**
- AP fills in 3 seconds
- Can act frequently
- Short action strings (limited by 100% cap)
- Good for reactive play

**Slow Rechargers (Tanks, Heavy Units):**
- AP fills in 10 seconds
- Act infrequently
- Can plan longer action strings while waiting
- Good for powerful, decisive moves

**Medium Rechargers (Most Units):**
- AP fills in 5-6 seconds
- Balanced play style

### AP Regen as Status Effect Target

**Debuff: Weakening**
- Reduces AP regen by 50%
- Unit takes twice as long to act
- Templates remain in library
- Still executable, just less frequently

**Buff: Haste**
- Increases AP regen by 50%
- More frequent actions
- Same templates, better execution

**Debuff: Exhaustion**
- Reduces AP regen to near-zero
- Effectively locks unit out of action
- Template still exists, just can't execute it

### Tactical Implications

**Enemy strategy:**
- Identify your key units
- Debuff their AP regen
- Lock down your best templates

**Player counter:**
- Have backup units for key roles
- Design templates that work with debuffed units
- Cleanse debuffs
- Adapt strategy when templates become inaccessible

---

## Template Accessibility vs Executability

### Key Distinction

**Accessible:** You can see it, edit it, design with it
**Executable:** Your current units can perform it

**Example scenario:**

```
Template: "Rainbow Sky Bridge"
  - Create platform at (5,3,0)
  - Create platform at (6,3,0)
  - Create platform at (7,3,0)
  - Allied units move across

Status:
  ✓ Accessible (in your library)
  ✗ Executable (no units with "create platform" ability)
```

**What happens:**
- Template stays in your library
- Blueprint mode shows it grayed out or with warning
- "Requires: Unit with platform creation ability"
- Becomes a goal: "I need to recruit a unicorn"

### Benefits of This System

**1. No Cognitive Dissonance**
"I can imagine this tactic, so why can't I design it?"
→ You CAN design it, you just need the right units.

**2. Aspirational Play**
Early game, you design templates for units you don't have yet.
Progression: Acquiring those units unlocks those templates.

**3. Strategic Depth**
"Do I use my only flying unit for attack or for the sky bridge?"
Unit capability scarcity creates interesting choices.

**4. No Wasted Learning**
Study enemy tactics → design template immediately
Even if you can't execute it yet, the knowledge is captured.

---

## Books & Items as Unit Progression

### Books Don't Teach Template Design

**What books DO teach:**
- Unit capabilities you didn't know about
- Synergies between unit types
- Optimal equipment loadouts
- Status effect interactions

**Example book: "The Shield Bearer's Manual"**

Doesn't teach you HOW to design templates.
Teaches you WHAT knights with shields can do:
- Shield block reduces damage by 80%
- Can protect adjacent allies
- Shield bash can interrupt enemy actions
- Works well with slow AP regen (defensive role)

**Now you design templates using that knowledge.**

### Items as Capability Unlocks

**Key Item: "Grappling Hook"**
- Gives knight "grapple" ability
- Now executable: Templates requiring grappling
- Doesn't change template design tools
- Changes what templates can execute

**Not a key item: "Better Sword"**
- Increases attack damage
- Doesn't unlock new actions
- Makes existing templates more effective

### Character-Specific Progression

**Leveling up:**
- Increases stats (HP, damage)
- Might unlock new abilities at milestones
- Improves AP regen rate
- Expands action interface

**Example: Knight Level 1 → Level 10**

Level 1:
- Move, Attack, Block

Level 5:
- Move, Attack, Block, Shield Bash

Level 10:
- Move, Attack, Block, Shield Bash, Defensive Stance

**Templates using "Defensive Stance" now executable.**

---

## Game Balance Through Unit Constraints

### The Problem This Solves

**Without unit-based gating:**
- Player designs optimal strategy immediately
- Nothing to unlock, no progression feel
- Either game is too easy or template tools are artificially limited

**With unit-based gating:**
- Player can design optimal strategy immediately
- But can't execute it without right units
- Progression: Acquiring units that match your vision
- OR: Adapting vision to units you have

### The "Backburner" Design Pattern

**Player mindset:**

"I have this amazing 3D aerial assault template designed."
"But I only have ground units right now."
"So I'll keep it on the backburner."
"And design ground-based templates for current battles."
"When I recruit a flier, that template becomes viable."

**This respects player intelligence:**
- You're smart enough to design the aerial assault
- The game doesn't pretend you need to "learn" it
- You just need the right tools (units) to execute it

---

## Debuffs Making Templates Inaccessible

### Temporary Loss of Capability

**Scenario:**
```
Unit: Knight with shield
Template: "Defensive Box" (requires shield block)
Debuff: Disarmed (can't use equipment)

Result:
- Template stays in library
- Shows as "Currently inaccessible"
- When debuff expires, template becomes executable again
```

**Player adapts:**
- Switch to templates that don't require shield
- OR: Use different unit for that template
- OR: Cleanse the debuff
- OR: Wait it out (if you can afford to)

### AP Regen Debuff (Most Common)

**Weakening effect reduces AP regen:**
- Unit is still capable of actions
- Just takes longer to charge up
- Templates are "accessible but slow"

**Player choices:**
- Execute template anyway (accept slower execution)
- Switch to faster-charging unit
- Design templates with longer timelines to accommodate

**Meta-strategy:**
- Keep diverse units with varied AP regen rates
- Redundancy in capability (two units can shield)
- Don't become dependent on single unit for key templates

---

## Long-Term Planning & Aspiration

### The "How Do I Get This?" Question

**Early game template:**
```
"Sky Fortress Assault"
  - Unicorn creates platform chain
  - Grappler units swing up
  - Fliers provide air support
  - Ground units hold base

Currently executable: Ground units hold base
Not executable: Everything else
```

**This becomes a goal:**
- Need to recruit unicorn
- Need to unlock grappler class
- Need to train fliers

**Progression arc:**
- Chapter 5: Recruit basic flier
- Chapter 8: Unlock grappler training
- Chapter 12: Unicorn joins party
- Chapter 13: "Sky Fortress Assault" fully executable

**The template existed since Chapter 2** (when you designed it), but only now can you pull it off.

### Emergent Player Behavior

**Template library as wishlist:**
- Players design aspirational templates
- Those templates guide recruitment decisions
- "I need a unit that can do X" becomes explicit

**vs Traditional Progression:**
- Game gives you unit
- You figure out what to do with it
- Reactive design

**This System:**
- You design tactic
- You seek units to execute it
- Proactive design

---

## Open Source Systems Thinking

### Declarative Constraints Enable Inspection

**Because the game uses declarative systems:**
- You can see WHY things work
- Not just THAT they work

**Enemy uses complex tactic:**
- Inspect action history
- See constraints satisfied
- Understand composition structure
- Recognize reusable patterns

**Traditional game:**
- Enemy uses "Lightning Strike" ability (opaque)
- You don't know how it's constructed
- Can't learn from it, can only counter it

**This game:**
- Enemy uses template composed of Move + Attack + Move
- You see the template structure
- You learn the pattern
- You adapt it for your units

### Runtime Testing Outside the Loop

**"Because it's computerized you can runtime templates from the outside"**

**Training Grounds:**
- Load template
- Simulate execution with current units
- See if it works
- Debug without consequences

**Blueprint Mode Preview:**
- Before committing actions
- Show projected paths
- Highlight constraint violations
- "This won't work because unit lacks grapple ability"

**Action History Replay:**
- Rewind battle
- Watch template execution frame-by-frame
- Understand timing and coordination
- Learn from success AND failure

---

## Meta-Layer Understanding

### Conceptual Books Explain "The Why"

**Not teaching templates directly.**
**Teaching principles behind template design.**

**Example book: "Principles of Coordination"**

Doesn't say:
- "Use Pincer Maneuver here"

Instead says:
- "Simultaneous attacks from multiple angles divide enemy attention"
- "Creating constraint shapes limits enemy options"
- "Flow design ensures units don't block each other"

**Player takes principles → designs their own templates.**

### Supported by System Design

**The game architecture enables this teaching style:**

Because everything is:
- Declarative (visible rules)
- Composable (build from pieces)
- Idempotent (reusable)
- Interface-based (interchangeable)

**Players can learn the meta-patterns.**

**They're not memorizing specific tactics.**
**They're learning tactical design principles.**

---

## Balance Philosophy Summary

### What's Gated
- Unit capabilities (abilities, actions)
- AP regen rates (timing)
- Equipment options (modifiers)
- Unit availability (roster)

### What's NOT Gated
- Template design tools (full access)
- Creative expression (infinite)
- Strategic knowledge (learn anytime)
- Template library (keep everything)

### Why This Works

**Respects player intelligence:**
- You're smart enough to design anything
- We won't patronize by locking design tools

**Creates meaningful progression:**
- You acquire units that enable designs
- OR: Adapt designs to available units
- Progression feels empowering, not restrictive

**Enables emergent gameplay:**
- Players design templates before they can use them
- Templates guide recruitment strategy
- Aspirational play creates goals

**Handles difficulty naturally:**
- Early game: Limited units, simple templates executable
- Mid game: More units, complex templates possible
- Late game: Full roster, intricate templates shine

---

## Examples in Practice

### Example 1: The Aspirational Designer

**Chapter 2:**
- Player has 3 ground units
- Designs "Rainbow Bridge Assault" (requires flier with platform ability)
- Template saved but grayed out
- "I need to find a unicorn"

**Chapter 7:**
- Recruits Rainbow Unicorn
- Template becomes executable
- Immediate payoff: "Finally I can do this!"
- No need to design it now, it's been waiting

### Example 2: The Adaptive Tactician

**Chapter 5:**
- Player designs template using Knight's shield
- Mid-battle: Knight gets disarmed
- Template becomes inaccessible
- Player switches to backup template
- Doesn't lose progress, just adapts

### Example 3: The Student of War

**After tough battle:**
- Enemy used devastating combo
- Player opens action history
- Sees: Move + Debuff + AoE + Move
- "Oh, they weakened our AP regen first!"
- Designs similar template for future use
- Learns from defeat

### Example 4: The Equipment Strategist

**Before battle:**
- Swaps Knight's sword for shield
- "Defensive Box" template becomes executable
- "Offensive Rush" template becomes inaccessible
- Conscious trade-off based on map/enemy

---

## Open Questions

1. **Template Validation UI:**
   - How clearly does the game show "why" a template isn't executable?
   - "Missing: Unit with platform ability"
   - "Warning: Low AP regen, this will take 30 seconds"
   - "Unit is debuffed: Reduced effectiveness"

2. **Unit Signature Visualization:**
   - Can players see "what templates this unit enables"?
   - When recruiting, show "unlocks 3 templates in your library"?

3. **Template Suggestions:**
   - Does the game suggest "you could adapt X template for your current units"?
   - Help players see possibilities with available roster?

4. **Action History Detail:**
   - How granular is the breakdown?
   - Can you see exact AP costs, timing, constraints checked?
   - Export to template format directly?

5. **Training Grounds:**
   - Can you test templates with hypothetical units?
   - "What if I had a flier, would this work?"
   - Sandbox mode for experimentation?

---

## Implementation Implications

### Data Structures

```javascript
Unit {
  id: string,
  name: string,
  capabilities: Capability[],
  equipment: Equipment[],
  apRegenRate: number,
  statusEffects: StatusEffect[]
}

Capability {
  id: string,
  name: string,
  actions: Action[]
}

Template {
  id: string,
  name: string,
  requirements: Capability[],
  nodes: ControlNode[]
}

// Validation
function canExecute(template, units) {
  for (let req of template.requirements) {
    if (!units.some(u => u.capabilities.includes(req))) {
      return {
        executable: false,
        reason: `Missing: Unit with ${req.name}`
      };
    }
  }
  return { executable: true };
}
```

### UI Indicators

**Template Library:**
```
[✓] Pincer Maneuver (Executable)
[✓] Defensive Box (Executable)
[⏸] Rainbow Bridge (Requires: Platform creation)
[⚠] Shield Wall (Knight is disarmed)
[⏱] Rapid Strike (Low AP, will be slow)
```

### Action History Export

**Button: "Save as Template"**
- Watches enemy action sequence
- Click button
- Opens template editor with structure pre-filled
- Player can name it, adjust parameters
- Instant learning → instant application

---

**Related Documents:**
- `progression-through-units.md` - Primary source
- `template-composition-system.md` - Template structure
- `blueprint-mode-design.md` - Core system
- `CONSTRAINT-INTERFACE-PATTERN.md` - Constraint foundation

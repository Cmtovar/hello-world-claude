# Almanac System and Template IDE - Interpretation

**Date:** 2026-01-29
**Interpreter:** Claude (Session 2026-01-29)
**Primary Source:** `almanac-and-template-ide.md`

---

## The Three Buildings System

### Building 1: Tactics Hall (Template Editor)
**Purpose:** Design and compose templates

### Building 2: Strategy Library (Learning Center)
**Purpose:** Read books, study patterns

### Building 3: Almanac (Piklopedia)
**Purpose:** Investigate objects, units, environmental assets

**Together:** Complete learning and design ecosystem

---

## The Almanac Building

### Inspired by Pikmin's Piklopedia

**What it contains:**

#### Environmental Assets Catalog
- Carnivorous plants
- Boulders
- Geysers
- Ice patches
- Destructible walls
- Every interactive object in the game

#### For Each Entry:
**Basic Info:**
- Name, description, visual
- Where found (which levels)
- Danger level

**Behavioral Data:**
- Passive state (what it does normally)
- Triggers (how to activate it)
- Active state (what happens when triggered)
- Duration, cooldown, range

**Constraint Signature:**
- What it blocks/allows
- Movement effects
- Area of effect
- Damage type/amount

**Tactical Uses:**
- "Can be used against enemies"
- "Can provide mobility"
- "Area denial tool"
- "Combine with X for Y effect"

#### Interactive Demonstration
- 3D model viewer (rotate, inspect)
- Behavior playback (see it in action)
- Trigger simulation (test what activates it)
- Constraint visualization (see its effect zones)

### Example Entry: Carnivorous Plant

```
Name: Snapjaw Vine
Type: Environmental Hazard (Interactive)

Description:
A large carnivorous plant that remains dormant until
disturbed. When agitated, it lunges at the nearest
moving creature with surprising speed.

Location: Forest levels, Chapter 3+

Behavior:
- Passive: Blocks 1 tile, damages on contact (30 HP)
- Trigger: Noise, attack, proximity (2 tile range)
- Active: Lunges toward nearest unit (4 tile range)
         Bites for 50 HP damage, applies "Poisoned" status
- Duration: 2 seconds active, then returns to dormant
- Cooldown: 10 seconds before can be triggered again

Constraints:
{
  "blockMovement": true,
  "attackable": false (cannot be destroyed),
  "triggerRadius": 2,
  "lungeRange": 4,
  "damageType": "physical + poison"
}

Tactical Uses:
✓ Knock enemies into trigger radius
✓ Agitate to create temporary area denial
✓ Position enemies between you and plant
✗ Cannot be destroyed or moved

Synergies:
- Push techniques (force enemy into range)
- Noise-based abilities (trigger from distance)
- Poison resistance (negate status effect)

Counters:
- Fire damage (plant is weak to fire)
- Flight (lunge doesn't reach airborne units)
- Shields (block lunge damage)

[Interactive Demo] [Add to Template IDE] [Mark as Studied]
```

---

## Template IDE: The Design Workspace

### What It Is

**Full-featured development environment for templates.**

Like a code IDE, but for tactical patterns:
- Visual editor
- Playback/simulation
- Debugging tools
- Testing environment
- Version control (save iterations)

### Key Features

#### 1. Temporal Playback

**Step through template execution:**
```
Timeline: 0s → 20s

[0s] Mage: Cast Explosion
     - AP: 100% → 0%
     - Offset: 8s begins
     - Effect: AoE damage at (5,3)

[0s] Knight: Move to Mage
     - Path: (2,2) → (5,2)
     - Duration: 2s
     - AP: 100% → 0%

[2s] Knight: Shield Wall
     - Protects Mage
     - Offset: 3s

[8s] Mage: Offset expires
     - Can move again
     - AP begins refilling

[10s] Mage: AP at 40%
[15s] Mage: AP at 90%
[18s] Mage: AP at 100%, ready to act

[Playback controls: |◄ | ► || ▶▶| Scrub timeline]
```

**Visualization:**
- Show unit positions at each timestamp
- Display AP bars changing
- Highlight offset periods
- Show environmental triggers

**Benefits:**
- See exactly when vulnerabilities occur
- Identify timing gaps
- Optimize coordination
- Debug issues

#### 2. Environmental Asset Integration

**"Add Environmental Object" button:**
- Opens Almanac catalog
- Drag object into template
- Place on virtual map
- Template now references that object

**Example:**
```
Template: "Plant Ambush"

Environmental Assets:
- Carnivorous Plant at (7,4)

Units Required:
- Any unit with push ability

Timeline:
[0s] Pusher: Move toward enemy
[2s] Pusher: Push enemy toward plant
[3s] Enemy: Knocked into plant trigger radius
[3s] Plant: Lunges at enemy (automatic)
[5s] Plant: Returns to dormant
```

**Template IDE shows:**
- Plant behavior in timeline
- Trigger radius visualization
- Lunge animation during playback
- Success/failure conditions

#### 3. Handler Pattern Creation

**"Create Handler" workflow:**

**Step 1: Select Environmental Asset**
- From Almanac or current map
- Example: Carnivorous Plant

**Step 2: Define Interaction Goal**
- "Use plant to damage enemy"
- "Avoid plant while maneuvering"
- "Trigger plant to block path"

**Step 3: Design Input/Output Template**
```
Handler: "Plant Trap"
Input:
  - Enemy position
  - Plant position
  - Unit with push ability

Process:
  1. Calculate push vector toward plant
  2. Move unit to optimal push position
  3. Execute push
  4. Enemy enters plant trigger radius
  5. Plant activates (automatic)

Output:
  - Enemy damaged (50 HP)
  - Enemy poisoned (status)
  - Plant on cooldown (10s)
  - Area denied temporarily

Constraints:
  - Push ability required
  - Plant must not be on cooldown
  - Enemy must be within push range of plant trigger radius
```

**This handler becomes a reusable component:**
```
Template: "Forest Assault"
- Execute "Plant Trap" handler on Enemy Group A
- While plant is active, flank from opposite side
- Execute "Plant Trap" handler on Enemy Group B
  (wait for first plant cooldown)
```

#### 4. Playback of Handler Behavior

**When testing "Plant Trap" handler:**

**Playback shows:**
1. Unit pathfinding to push position
2. Push technique animation
3. Enemy knockback trajectory
4. Plant trigger visualization (radius lights up)
5. Plant lunge animation
6. Damage numbers
7. Poison effect applied
8. Cooldown timer starts

**Step-by-step temporal exploration:**
- Pause at any point
- Inspect state (unit HP, AP, positions)
- Modify and replay
- See consequences of changes

#### 5. Testing with Mock Units

**Sandbox mode:**
- Place hypothetical units
- "What if I had a child unit here?"
- "What if knight was debuffed?"
- "What if enemy had shield?"

**Test template validity:**
```
Template: "Knight Charge"
Requirements:
  - Unit with "Heavy Armor" capability
  - Unit with "Charge" technique

Test with:
  ✓ Knight (has both)
  ✓ Paladin (has both)
  ✗ Child (lacks Heavy Armor)
  ✗ Mage (lacks both)

Result: Shows which units can execute this template
```

---

## Learning Flow: Book → Pattern → Handler → Template

### The Complete Educational Loop

#### Step 1: Encounter New Environmental Asset
**In battle:**
- Player sees carnivorous plant for first time
- Gets eaten
- "What is this thing?"

#### Step 2: Study in Almanac
**Visit Almanac building:**
- Look up "Carnivorous Plant"
- Read behavior, constraints, triggers
- Watch interactive demo
- Understanding: "Oh, it lunges when I get close"

#### Step 3: Read Conceptual Guide
**Visit Strategy Library:**
- Find book: "Mastering Hazardous Flora"
- Reads: "Plants can be weaponized against enemies"
- Reads: "Use push techniques to position enemies"
- Reads: "Coordinate timing with plant cooldowns"

**Gains conceptual knowledge:**
- Plants are tools, not just obstacles
- Positioning is key
- Timing matters

#### Step 4: Design Handler in Template IDE
**Visit Tactics Hall:**
- Open Template IDE
- Create new handler: "Plant Trap"
- Add carnivorous plant from Almanac
- Design push interaction
- Use playback to test behavior
- Refine timing and positioning

**Save handler as reusable component**

#### Step 5: Compose into Larger Template
**Build full battle template:**
```
Template: "Forest Gauntlet"
- Scout forward
- Execute "Plant Trap" on enemy group
- While they're poisoned, advance
- Execute "Plant Trap" on reinforcements
- Secure objective
```

**The handler becomes a building block.**

#### Step 6: Use in Actual Battle
**Next forest level:**
- Player recognizes plants
- Opens blueprint mode
- Selects "Forest Gauntlet" template
- Executes with confidence

**Knowledge → Pattern → Practice → Mastery**

---

## Unit Balancing Through Capability Dependencies

### The Child Unit Example

#### Generic Knight

**Capabilities:**
- Move (ground, 4 tiles)
- Attack (melee, 100 damage)
- Heavy armor (reduces damage by 50%)
- Shield block (80% damage reduction)
- Charge technique (knockback enemies)
- Leadership (buffs nearby allies)

**Templates this enables:**
- "Shield Wall" (requires shield block)
- "Knight Charge" (requires charge technique)
- "Defensive Formation" (requires heavy armor)
- "Frontline Hold" (requires multiple capabilities)

#### Child Unit

**Capabilities:**
- Move (ground, 5 tiles - faster)
- Attack (melee, 40 damage - weaker)
- Light armor (reduces damage by 20%)
- Quick step (dodge bonus)
- Distraction (draws enemy attention)

**Templates this enables:**
- "Scout Forward" (uses high movement)
- "Distraction Tactics" (uses distraction ability)
- "Quick Retreat" (uses quick step)

**Templates this DOESN'T enable:**
- ✗ "Shield Wall" (lacks shield block)
- ✗ "Knight Charge" (lacks charge technique)
- ✗ "Defensive Formation" (lacks heavy armor)
- ✗ "Frontline Hold" (lacks required capabilities)

### Why This Is Good Design

**Doesn't punish player knowledge:**
- Player can design "Shield Wall" template
- Child unit just can't execute it
- Template stays in library
- When player recruits knight, template becomes usable

**Creates unit identity:**
- Knights are defensive anchors
- Children are scouts and distractors
- Each has unique template pools
- Encourages diverse roster

**Natural balance:**
- Player has 50 templates
- But only 10 are executable with current party
- Acquiring new units unlocks templates
- Progression through capability expansion

**Template reuse with constraints:**
```
Template: "Pincer Maneuver"
Requirements:
  - 2 units with movement ≥ 4 tiles

Can be executed with:
  ✓ 2 Knights (movement = 4)
  ✓ 2 Children (movement = 5)
  ✓ 1 Knight + 1 Child
  ✗ 2 Heavy Tanks (movement = 2)

The TEMPLATE is generic.
The UNITS must meet requirements.
```

---

## Dependency System in Detail

### Capability Levels

**Not just binary (has/doesn't have):**

**Sword Mastery (example):**
- Level 0: Cannot use swords
- Level 1: Basic sword attacks (50 damage)
- Level 2: Advanced techniques unlocked (100 damage)
- Level 3: Master techniques unlocked (150 damage + special)

**Templates can require specific levels:**
```
Template: "Basic Slash"
Requirements:
  - Sword Mastery ≥ 1

Template: "Whirlwind Strike"
Requirements:
  - Sword Mastery ≥ 3
  - AP regen ≥ medium
```

**Child with Sword Mastery 1:**
- ✓ Can execute "Basic Slash"
- ✗ Cannot execute "Whirlwind Strike"

**Knight with Sword Mastery 3:**
- ✓ Can execute both

### Template Library Management

**Filtering options:**
```
Show:
  [✓] Executable with current party
  [✓] Executable if I swap equipment
  [ ] Requires recruitment (grayed out)
  [ ] All templates

Sort by:
  - Recently used
  - Unit type
  - Complexity
  - Power level
```

**Visual indicators:**
```
Templates:
  [✓] Pincer Maneuver (ready)
  [⚙] Knight Charge (equip sword to knight)
  [👥] Rainbow Bridge (need unicorn)
  [⏱] Explosion Combo (mage is debuffed)
```

---

## Environmental Handler Patterns

### Common Handler Archetypes

#### 1. Weaponization Handler
**Goal:** Use hazard against enemies

**Pattern:**
- Identify hazard trigger mechanism
- Position enemy within trigger zone
- Activate hazard
- Enemy takes damage/effect

**Examples:**
- "Plant Trap" (push into carnivorous plant)
- "Boulder Crush" (push boulder down slope)
- "Geyser Launch" (trigger geyser under enemy)

#### 2. Avoidance Handler
**Goal:** Navigate around hazard safely

**Pattern:**
- Identify hazard trigger zones
- Plan path that avoids triggers
- Execute movement with safety margin
- Monitor hazard state (active/dormant)

**Examples:**
- "Plant Navigation" (avoid plant trigger radius)
- "Safe Crossing" (time movement between geysers)
- "Ice Path" (avoid slippery patches)

#### 3. Exploitation Handler
**Goal:** Use hazard for benefit

**Pattern:**
- Identify beneficial hazard effect
- Trigger hazard deliberately
- Position ally to receive benefit
- Avoid negative effects

**Examples:**
- "Geyser Boost" (use geyser for height)
- "Ice Slide" (use ice for speed boost)
- "Vine Swing" (use vines for mobility)

#### 4. Neutralization Handler
**Goal:** Remove or disable hazard

**Pattern:**
- Identify hazard weakness
- Apply counter (fire to plant, ice to geyser)
- Hazard disabled temporarily or permanently
- Path now safe

**Examples:**
- "Burn Plant" (fire spell disables plant)
- "Freeze Geyser" (ice stops eruptions)
- "Collapse Boulder" (destroy boulder before it's used against you)

### Handler Composition

**Handlers can be combined:**
```
Template: "Complex Hazard Navigation"
- Execute "Plant Avoidance" handler
- Execute "Boulder Weaponization" handler
- Execute "Geyser Exploitation" handler
- Each handler is independent
- Together they navigate complex environment
```

---

## Playback Feature Implementation

### Timeline Scrubbing

**Visual timeline:**
```
0s────2s────4s────6s────8s────10s────12s
|     |     |     |     |      |      |
Mage  Knight      Plant       Offset
Cast  Move        Lunges      Expires
```

**Scrubber control:**
- Drag to any timestamp
- See game state at that moment
- Units frozen in position
- AP bars show current values
- Effects visible (fire, poison, etc.)

### Step-by-Step Mode

**Frame advance:**
```
[Step Forward] [Step Backward]

Current: 3.2 seconds
- Mage: Offset remaining: 4.8s
- Knight: Moving to (5,2), ETA: 0.8s
- Plant: Dormant
- Enemy: HP 150/200 (damaged by explosion)

[Next Event]: 4.0s (Knight arrives at destination)
```

**Event markers:**
- Technique usage
- Movement completion
- Offset expiration
- Environmental triggers
- Status changes

### Behavior Exhibition

**When playing back environmental interactions:**

**Carnivorous Plant example:**
```
Timeline view:
[3.0s] Enemy enters trigger radius
       → Plant behavior: Check nearest unit
       → Nearest: Enemy at (6,4), distance 2 tiles

[3.1s] Plant: Begin lunge animation
       → Target locked: (6,4)
       → Lunge path: (7,4) → (6,4)
       → Duration: 0.5s

[3.6s] Plant: Contact with enemy
       → Damage: 50 HP
       → Apply status: Poisoned (5s duration)
       → Begin return animation

[5.0s] Plant: Return to dormant state
       → Cooldown: 10s
       → Next trigger available: 15.0s

[Player can see all of this step-by-step]
```

**Learning happens through observation:**
- "Oh, there's a 0.1s delay before lunge"
- "I can dodge if I move during that window"
- "Cooldown is 10s, I can chain two plants"

---

## IDE Features for Sensitive Environmental Materials

### "Sensitive" = Complex Behavior

**Examples:**
- Carnivorous plants (trigger, lunge, return, cooldown)
- Chain-reaction explosions (one explosion triggers others)
- Temporal hazards (geysers that erupt on schedule)
- Adaptive enemies (behavior changes based on player actions)

### Exploration Tools in IDE

#### 1. Behavior Tree Viewer

**For carnivorous plant:**
```
Plant AI:
├─ Passive State
│  ├─ Monitor trigger radius
│  └─ On trigger: → Active State
├─ Active State
│  ├─ Identify nearest unit
│  ├─ Lunge toward target
│  ├─ Apply damage + poison
│  └─ Return to Dormant State
└─ Dormant State (10s cooldown)
   └─ Cannot be triggered
   └─ After cooldown: → Passive State
```

**Player can see decision tree, understand logic**

#### 2. Constraint Visualization

**Visual overlay in IDE:**
- Trigger radius (yellow circle, 2 tiles)
- Lunge range (red cone, 4 tiles)
- Damage area (red circle at impact)
- Cooldown timer (grayed out while active)

**Player can see zones, plan around them**

#### 3. "What If" Scenarios

**Test different configurations:**
```
Scenario 1: Enemy at (6,4), Ally at (8,4)
→ Plant lunges at enemy (closer)

Scenario 2: Enemy at (6,4), Ally at (6,3)
→ Plant lunges at ally (same distance, but ally moved first)

Scenario 3: Flying enemy at (6,4,2)
→ Plant cannot reach (airborne)

[Run Simulation] for each scenario
```

**Player learns edge cases through experimentation**

#### 4. Input/Output Mapping

**Define handler formally:**
```
Handler: "Plant Trap"

Inputs:
  - enemy: Unit
  - plant: EnvironmentalObject (type: carnivorous_plant)
  - pusher: Unit (capability: push)

Preconditions:
  - plant.state == "passive" (not on cooldown)
  - distance(enemy, plant) ≤ 4 (within push range)
  - pusher.AP >= 100

Process:
  1. pusher.moveTo(optimalPushPosition(enemy, plant))
  2. pusher.useTechnique("Push", target: enemy)
  3. enemy.knockback(direction: toward plant)
  4. IF distance(enemy, plant) ≤ 2:
       plant.trigger(source: enemy)
  5. plant.lunge(target: enemy)
  6. enemy.damage(50)
  7. enemy.applyStatus("Poisoned", 5s)

Outputs:
  - enemy.HP -= 50
  - enemy.status += "Poisoned"
  - plant.state = "cooldown"
  - pusher.AP = 0

Success Conditions:
  - enemy damaged
  - plant triggered

Failure Conditions:
  - plant on cooldown
  - enemy out of range
  - pusher lacks push capability
```

**This formal definition:**
- Can be tested in IDE
- Shows failure modes
- Becomes composable unit
- Other templates can call it

---

## The Fourth Building Suggestion

### Current Buildings:
1. Tactics Hall (Template Editor)
2. Strategy Library (Books/Guides)
3. Almanac (Piklopedia)

### Potential Fourth Building: Training Grounds

**Purpose:** Live practice with templates

**Features:**
- Mock battles
- Environmental sandbox
- Template testing under pressure
- No consequences for failure
- Iterate rapidly

**Workflow:**
1. Design template in Tactics Hall (IDE)
2. Test in Training Grounds (practice)
3. Use in actual battle (execution)

**OR: Training Grounds is part of Tactics Hall**
- Same building
- Different mode/area
- Seamless transition between design and practice

---

## Open Questions

1. **Almanac Unlock Progression:**
   - Are all entries available from start?
   - Or unlock as you encounter objects?
   - Hidden entries for rare environmental assets?

2. **Template IDE Accessibility:**
   - Available from start?
   - Or unlock features progressively?
   - Playback available early vs late?

3. **Handler Sharing:**
   - Can handlers be exported/imported?
   - Community handler library?
   - Enemy handlers visible (learn from enemies)?

4. **Environmental Asset Randomization:**
   - Are plants always in same positions?
   - Or procedurally placed?
   - Does Almanac show "typical locations" vs "exact positions"?

5. **Temporal Precision:**
   - How granular is timeline (frames, 0.1s, 1s)?
   - Can players control animation speed?
   - Slow-mo for complex interactions?

---

## Implementation Implications

### Data Structures

```javascript
EnvironmentalAsset {
  id: string,
  name: string,
  description: string,
  behaviorTree: BehaviorNode,
  constraints: Constraints,
  triggers: Trigger[],
  effects: Effect[],
  cooldown: number,
  almanacEntry: {
    studied: boolean,
    tacticalNotes: string[],
    demonstrationVideo: string
  }
}

Handler {
  id: string,
  name: string,
  inputs: Parameter[],
  preconditions: Condition[],
  process: Action[],
  outputs: Result[],
  successConditions: Condition[],
  failureConditions: Condition[]
}

Template {
  id: string,
  name: string,
  handlers: Handler[],
  environmentalAssets: EnvironmentalAsset[],
  timeline: TimelineEvent[],
  requirements: Capability[]
}
```

### IDE Playback Engine

```javascript
class TemplatePlayback {
  template: Template;
  currentTime: number;
  paused: boolean;
  playbackSpeed: number; // 0.5x, 1x, 2x, etc.

  play() {
    // Execute template step by step
    while (currentTime < template.duration) {
      this.processEventsAt(currentTime);
      this.renderState();
      this.currentTime += deltaTime * playbackSpeed;
    }
  }

  scrubTo(timestamp: number) {
    // Jump to specific time
    this.currentTime = timestamp;
    this.reconstructStateAt(timestamp);
    this.renderState();
  }

  stepForward() {
    const nextEvent = this.getNextEvent(currentTime);
    this.currentTime = nextEvent.timestamp;
    this.renderState();
  }

  processEventsAt(time: number) {
    const events = template.timeline.filter(e => e.timestamp === time);
    events.forEach(event => {
      // Execute technique
      // Update AP
      // Trigger environment
      // Apply effects
    });
  }
}
```

---

**Related Documents:**
- `almanac-and-template-ide.md` - Primary source
- `techniques-and-environment.md` - Environmental mechanics
- `template-composition-system.md` - Template structure
- `progression-through-units.md` - Capability dependencies

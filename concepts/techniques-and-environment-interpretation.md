# Techniques and Environmental Interaction - Interpretation

**Date:** 2026-01-29
**Interpreter:** Claude (Session 2026-01-29)
**Primary Source:** `techniques-and-environment.md`

---

## Core Design Shift

**Away from:** Resource management (weapon durability, item scarcity)
**Toward:** Timing management (AP + offset) and spatial tactics (environment as tool)

---

## AP Offset System (White Ink Frames)

### Splatoon's Mechanic
In Splatoon, after firing a heavy weapon:
- **White ink frames** appear on your ink tank
- You CANNOT use ink until white frames clear
- Hard, unavoidable cooldown
- Separate from normal ink refill

### This Game's Equivalent: AP Offset

**Normal AP System:**
- AP fills from 0% → 100%
- At 100%, you can act
- Action consumes all AP back to 0%
- Refill begins immediately

**With Offset (Heavy Techniques):**
- AP at 100%, you use Explosion spell
- AP drops to 0%
- **Offset period begins** (e.g., 8 seconds)
- During offset: AP cannot refill, unit cannot act
- After offset expires: AP begins refilling normally

### Example: Megumin's Explosion

```
Before: AP = 100%
Action: Cast Explosion (massive AoE damage)
Immediately after: AP = 0%, Offset = 8 seconds

For 8 seconds:
- Unit cannot move
- Unit cannot act
- Unit is completely vulnerable
- AP stays at 0%

After 8 seconds:
- Offset expires
- AP begins refilling (10 second refill for this unit)

After 18 total seconds:
- AP = 100% again
- Can act normally
```

**Balance:** Devastating power comes with vulnerability window.

---

## Technique Focus Over Weapon Durability

### Why No Weapon Durability

**Fire Emblem Fates:** Infinite durability weapons (preferred experience)

**Problems with durability:**
- Inventory micromanagement
- Anxiety about "wasting" good weapons
- Doesn't fit the template/technique focus

**This game's approach:**
- Weapons don't break
- Techniques have AP costs + offsets
- Limit is timing, not resources

### Techniques as Primary Mechanic

**Different techniques have different AP profiles:**

| Technique | AP Cost | Offset | Effect |
|-----------|---------|--------|--------|
| Basic Attack | 100% | 0s | Standard damage |
| Power Strike | 100% | 2s | 2x damage |
| Explosion | 100% | 8s | Massive AoE |
| Quick Dash | 100% | 0s | Reposition |
| Shield Wall | 100% | 3s | Protect allies |

**The interesting decisions:**
- Explosion is powerful but leaves you vulnerable
- Quick Dash lets you act again immediately
- Power Strike is middle ground

**Templates must account for offset timing:**
```
Template: "Mage Assault"
- Witch: Cast Explosion (8s offset)
- Knight: Move to protect Witch (0s offset)
- Archer: Attack while protected (2s offset)
- Wait 8 seconds for Witch to recover
- Continue coordinated advance
```

---

## Minimal Inventory: 2 Slots

### Primary + Auxiliary

**Slot 1: Primary Weapon**
- Your main tool
- Defines your basic capabilities

**Slot 2: Auxiliary Item**
- Situational tool
- Utility or alternate approach

**Examples:**

**Knight:**
- Primary: Sword (offensive techniques)
- Auxiliary: Shield (defensive techniques)

**Mage:**
- Primary: Staff (AoE spells)
- Auxiliary: Dagger (close-range fallback)

**Archer:**
- Primary: Bow (ranged attacks)
- Auxiliary: Rope (grappling utility)

### Mid-Battle Equipment Swapping

**Between primary and auxiliary:**
- Instant (no AP cost)
- Changes available techniques
- Tactical adaptation

**Trading with allies:**
- Takes an action (100% AP)
- Adjacent units only
- Coordinate equipment needs

**Picking up battlefield items:**
- Replaces auxiliary slot
- Environmental loot integration

---

## Weapon Intrinsic Attributes

### The Dragon Slayer Example

**Standard approach to dragon-slaying:**

Normal Sword + Dragon Taming Technique:
- Basic attack: 100% AP, standard damage
- Dragon Taming attack: 100% AP + 3s offset, bonus vs dragons

**Dragon Slayer weapon approach:**

Dragon Slayer Sword (intrinsic dragon taming):
- Basic attack: 100% AP, bonus vs dragons (no offset)
- Dragon Taming technique: Not needed, already applied

**Trade-off:**
- Pro: Free dragon bonus on every attack
- Con: Weapon is worse against non-dragons
- Con: Dragon Taming technique slot could be used for something else

### Weapon as Skill Enabler

**Weapons can:**
1. **Replace techniques** (intrinsic effects)
2. **Augment techniques** (reduce AP cost/offset)
3. **Unlock techniques** (can't use X without weapon Y)

**Example: Fire Staff**

Normal Staff:
- Basic magic: 100% AP
- Fireball technique: 100% AP + 2s offset

Fire Staff (intrinsic fire):
- Basic magic: 100% AP (deals fire damage)
- Fireball technique: 100% AP + 1s offset (reduced)
- Inferno technique: 100% AP + 4s offset (unlocked)

**The weapon changes your technique profile.**

### Balancing Intrinsic Weapons

**Design constraint:**
Weapons with intrinsic effects are balanced around having them.

**Dragon Slayer vs Normal Sword:**

| Weapon | vs Dragons | vs Other | Special |
|--------|-----------|----------|---------|
| Normal Sword | 100 dmg | 100 dmg | Can use any technique |
| Dragon Slayer | 200 dmg | 70 dmg | Dragon bonus intrinsic |

**The Dragon Slayer is:**
- Amazing in dragon-heavy levels
- Worse in general combat
- Frees up technique slot

**Player choice:**
- Bring Dragon Slayer if you know dragons are coming
- Or keep normal sword + dragon technique for flexibility

---

## Environmental Interaction (The Most Important Thing)

### Environment as Weapon

**Core philosophy:** The map is not just terrain, it's an arsenal.

### Example: Carnivorous Plants

**Static hazard:**
- Large plant on map
- Damages anything that enters its tile

**Interactive hazard (better):**
- Plant can be agitated (attack it, noise, etc.)
- When agitated, lunges at nearest unit
- Can knockback enemies into it
- Can bait it to create area denial

**Template using this:**
```
"Plant Trap"
- Archer: Agitate carnivorous plant
- Knight: Knockback enemy toward plant
- Plant lunges, damages enemy
- Retreat while enemy is stunned
```

### Types of Environmental Weapons

#### 1. Hazards (Passive → Active)
- **Carnivorous plants:** Lunge when agitated
- **Boulders:** Push down slopes to crush enemies
- **Geysers:** Erupt when triggered, launch units upward
- **Ice patches:** Cause sliding, can break to create pits

#### 2. Terrain Modification
- **Destructible walls:** Create new paths or collapse on enemies
- **Pillars:** Knock down to create bridges
- **Vines:** Cut to drop platforms
- **Frozen water:** Melt to drown enemies or create moat

#### 3. Creatures/NPCs (Neutral)
- **Birds:** Startle to create distractions
- **Beasts:** Agitate to rampage (damages anyone nearby)
- **Elementals:** Provoke to unleash AoE
- **Merchants:** Bribe or threaten for items/help

#### 4. Objects as Projectiles
- **Barrels:** Roll down slopes, explode if fire barrels
- **Crates:** Push onto enemies from height
- **Furniture:** Block paths or create cover
- **Chandeliers:** Drop for AoE damage

#### 5. Battlefield Items (Loot)
- **Swords/shields:** Replace auxiliary slot
- **Potions:** One-time use, then disappears
- **Scrolls:** Single-use techniques
- **Keys:** Unlock areas or chests

### Integration with Constraint System

**Environmental objects have constraint signatures:**

**Carnivorous Plant:**
```json
{
  "type": "hazard",
  "triggers": ["agitate", "approach"],
  "effects": ["damage", "knockback"],
  "constraints": {
    "blockMovement": true,
    "attackable": true,
    "range": 2
  }
}
```

**Boulder on Slope:**
```json
{
  "type": "projectile",
  "triggers": ["push", "attack"],
  "effects": ["roll_down_slope", "crush"],
  "constraints": {
    "requiresSlope": true,
    "pathBlocking": true,
    "destructible": false
  }
}
```

**Templates can reference environmental objects:**
```
Template: "Boulder Trap"
Requirements:
  - Unit with push ability
  - Environmental object: boulder_on_slope

Actions:
  - Move to boulder
  - Push boulder toward enemies
  - Boulder rolls down, crushes line
```

---

## Techniques: Deep Dive

### Technique Definition

**Not just attacks** - techniques are any special action:

**Combat:**
- Power Strike (single target, high damage)
- Cleave (hit adjacent enemies)
- Fireball (ranged AoE)
- Explosion (massive AoE, huge offset)

**Movement:**
- Quick Dash (instant reposition, no offset)
- Leap (vertical mobility)
- Grapple (swing to distant point)
- Blink (teleport short distance)

**Support:**
- Heal (restore ally HP)
- Buff (increase ally stats)
- Debuff (weaken enemy)
- Shield (protect allies)

**Utility:**
- Agitate (provoke environmental hazard)
- Push (knockback enemy)
- Pull (draw enemy closer)
- Disarm (remove enemy weapon)

### Technique Parameters

```javascript
Technique {
  name: string,
  apCost: number,        // Usually 100%
  offset: number,        // Seconds before AP can refill
  range: number,         // Tiles
  area: "single" | "line" | "cone" | "circle",
  radius: number,        // For AoE
  effects: Effect[],
  requirements: Capability[]
}
```

### Example Techniques

**Quick Dash:**
```javascript
{
  name: "Quick Dash",
  apCost: 100,
  offset: 0,             // No offset, instant recovery
  range: 3,
  area: "single",
  effects: ["reposition"],
  requirements: ["movement"]
}
```

**Explosion:**
```javascript
{
  name: "Explosion",
  apCost: 100,
  offset: 8,             // 8 second vulnerability
  range: 10,
  area: "circle",
  radius: 3,
  effects: ["massive_damage", "knockback"],
  requirements: ["magic", "explosion_spell"]
}
```

**Agitate:**
```javascript
{
  name: "Agitate",
  apCost: 100,
  offset: 1,
  range: 2,
  area: "single",
  effects: ["provoke_hazard"],
  requirements: ["environmental_interaction"]
}
```

### Offset as Balancing Lever

**Low offset (0-1s):**
- Spam-able techniques
- Moderate power
- Flexible tactical use

**Medium offset (2-4s):**
- Powerful but risky
- Need protection during recovery
- Commit to the action

**High offset (5-8s+):**
- Devastating effects
- Extreme vulnerability
- Must plan around recovery time

**Template design must account for offsets:**
- Don't leave high-offset units unprotected
- Coordinate so allies cover during offset
- Use offset time for repositioning others

---

## Equipment Trading Mid-Battle

### Fire Emblem Style

**Trading:**
- Adjacent units can trade items
- Takes an action (costs AP)
- Common pre-battle repositioning

**Supply/Convoy:**
- Central location on map
- Restock from shared inventory
- Limited uses or positioned strategically

### This Game's Approach

**Trading:**
```
Action: Trade with Ally
- Adjacent unit only
- Costs 100% AP (full action)
- Swap items in inventory slots
- Both units participate (both spend AP)
```

**Battlefield Loot:**
```
Action: Pick Up Item
- Stand on item tile
- Costs 100% AP
- Item goes to auxiliary slot (replaces current)
- Or: Free if passing through tile
```

**Supply Points (Optional):**
```
Environmental object: Supply Crate
- Fixed location on map
- Interact to access shared inventory
- Costs 100% AP
- Limited to X uses per battle
```

### Tactical Implications

**Pre-planning:**
"Knight will trade shield to Mage after explosion (Mage needs defense during offset)"

**Template:**
```
"Explosion + Protection Trade"
- Mage: Cast Explosion (8s offset)
- Knight: Move adjacent to Mage
- Knight: Trade shield to Mage
- Mage: Equip shield (defense during recovery)
- Knight: Attack with sword (no shield now)
```

**Dynamic adaptation:**
"Found Dragon Slayer on battlefield → trade to unit facing dragons"

---

## Environmental Discovery

### Weapons as Loot

**Pre-placed:**
- Legendary sword in shrine
- Hidden dagger in crate
- Rare staff on altar

**Enemy drops:**
- Defeat enemy, they drop weapon
- Pick up or leave for later

**Temporary power-ups:**
- Fire enchant (5 turns)
- Speed boost potion (3 turns)
- Invincibility scroll (1 turn)

### Exploration Rewards Tactical Play

**Player who explores finds:**
- Better weapons
- Environmental triggers
- Shortcut paths
- Hidden hazards to exploit

**Templates can specify:**
```
"If dragon_slayer_found, execute dragon_assault_template"
"Else, execute standard_approach_template"
```

Conditional based on discovered items.

---

## Weapon Augmentation

### Temporary Modifications

**Spell-based:**
```
Mage casts "Fire Enchant" on Knight's sword
- Sword deals fire damage (5 turns)
- AP cost: Mage spends 100% AP
- Knight's attacks now fire-based
- Doesn't change Knight's AP
```

**Item-based:**
```
Knight uses "Poison Vial" on sword
- Next 3 attacks apply poison
- One-time consumable
- No AP cost, just uses vial
```

**Environmental:**
```
Sword is on fire tile
- Gains fire damage temporarily
- Lasts until leaving fire area
- Free, just positional
```

### Integration with Techniques

**Base technique:**
```
Power Strike: 2x damage, 2s offset
```

**With Fire Enchant active:**
```
Flaming Power Strike: 2x damage + burn effect, 2s offset
```

**Same technique, enhanced by weapon state.**

---

## Putting It All Together: Example Battle

### Scenario: Dragon's Lair

**Your units:**
- Knight (sword + shield)
- Mage (staff, knows Explosion)
- Archer (bow + rope)

**Map features:**
- Carnivorous plants along paths
- Boulders on slopes
- Supply crate (3 uses)
- Hidden Dragon Slayer in shrine

**Enemy:**
- Dragon (high HP, fire breath)
- Dragon minions (medium threat)

### Battle Flow (Using All Systems)

**Phase 1: Exploration**
```
Template: "Scout and Loot"
- Archer: Use rope to reach shrine
- Archer: Pick up Dragon Slayer (replaces rope)
- Knight: Agitate carnivorous plant
- Plant: Lunges at minion, clears path
```

**Phase 2: Equipment Shuffle**
```
Template: "Prepare for Dragon"
- Archer: Move adjacent to Knight
- Archer: Trade Dragon Slayer to Knight
- Knight: Equip Dragon Slayer (replaces sword)
- Mage: Move to flanking position
```

**Phase 3: Coordinated Assault**
```
Template: "Dragon Takedown"
- Knight: Attack dragon with Dragon Slayer
  (intrinsic dragon bonus, no extra offset)
- Mage: Cast Explosion (massive damage, 8s offset)
- Archer: Push boulder down slope toward minions
  (environmental damage)
- Knight: Move to protect Mage during offset
```

**Phase 4: Recovery & Cleanup**
```
Template: "Secure Victory"
- Wait for Mage offset to expire (8s)
- Knight: Finish weakened dragon
- Archer: Pick off remaining minions
- Mage: Heal allies once AP refilled
```

**Key elements used:**
- Techniques (Explosion with offset)
- Environmental weapons (plant, boulder)
- Equipment trading (Dragon Slayer)
- Battlefield loot (shrine)
- Template composition (multiple templates in sequence)

---

## Design Principles Summary

### 1. Timing > Resources
- No weapon durability
- AP + offset is the limiter
- High-power techniques have vulnerability windows

### 2. Environment = Arsenal
- Maps are interactive, not just terrain
- Every object is a potential tool
- Exploration rewards tactical creativity

### 3. Techniques > Weapons
- Weapons enable techniques
- Techniques define playstyle
- Offset timing creates strategic depth

### 4. Minimal Inventory
- 2 slots keeps it simple
- Trading/swapping is meaningful
- Found items are impactful

### 5. Intrinsic Weapon Properties
- Some weapons have built-in effects
- Balanced around having them
- Trade flexibility for specialization

---

## Open Questions

1. **Offset Stacking:**
   - If you use multiple high-offset techniques, do offsets stack?
   - Or does new offset replace old?
   - Max offset cap?

2. **Environmental Object Respawn:**
   - Do carnivorous plants respawn?
   - Are boulders one-time use?
   - Do hazards reset between chapters?

3. **Item Durability (if any):**
   - Weapons don't break
   - But temporary items (potions, scrolls)?
   - Consumable vs permanent distinction?

4. **Trading Range:**
   - Adjacent only for trading?
   - Or can you throw items across distance?
   - What's the AP cost of throwing?

5. **Equipment Weight/Mobility:**
   - Heavy armor slows AP regen
   - Does heavy weapon affect movement range?
   - Trade-offs beyond just stats?

6. **Environmental Discovery UI:**
   - How do players know an object is interactive?
   - Highlight interactable objects?
   - Or require experimentation?

---

## Implementation Implications

### Data Structures

```javascript
Technique {
  name: string,
  apCost: number,
  offsetSeconds: number,
  range: number,
  areaType: "single" | "line" | "cone" | "circle",
  areaRadius: number,
  effects: Effect[],
  requirements: Capability[]
}

Weapon {
  name: string,
  intrinsicEffects: Effect[],
  intrinsicTechniques: Technique[],
  techniqueModifiers: {
    [techniqueId]: {
      apCostModifier?: number,
      offsetModifier?: number,
      effectBonus?: Effect
    }
  },
  statModifiers: {
    apRegenRate?: number,
    movementRange?: number
  }
}

EnvironmentalObject {
  type: "hazard" | "projectile" | "loot" | "creature",
  triggers: string[],
  effects: Effect[],
  constraints: Constraints,
  oneTimeUse: boolean
}
```

### Offset System

```javascript
Unit {
  currentAP: number,
  offsetRemaining: number,

  canAct() {
    return this.currentAP >= 100 && this.offsetRemaining <= 0;
  },

  useTechnique(technique) {
    this.currentAP = 0;
    this.offsetRemaining = technique.offsetSeconds;
    // Execute technique effects
  },

  update(deltaTime) {
    if (this.offsetRemaining > 0) {
      this.offsetRemaining -= deltaTime;
    } else {
      this.currentAP += this.apRegenRate * deltaTime;
      this.currentAP = Math.min(100, this.currentAP);
    }
  }
}
```

### Environmental Interaction

```javascript
function interactWithEnvironment(unit, object) {
  switch (object.type) {
    case "hazard":
      if (object.triggers.includes("agitate")) {
        object.lunge(unit.position);
        object.oneTimeUse && removeObject(object);
      }
      break;

    case "projectile":
      if (object.triggers.includes("push")) {
        object.roll(calculateTrajectory(object));
        object.oneTimeUse && removeObject(object);
      }
      break;

    case "loot":
      unit.inventory.auxiliary = object.item;
      removeObject(object);
      break;
  }
}
```

---

**Related Documents:**
- `techniques-and-environment.md` - Primary source
- `progression-through-units.md` - Unit capability system
- `blueprint-mode-design.md` - AP system foundation
- `CONSTRAINT-INTERFACE-PATTERN.md` - Environmental constraints

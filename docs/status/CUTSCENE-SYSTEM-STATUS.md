# Cutscene System - Implementation Status

**Date:** 2026-01-30
**Status:** Test 01 Complete ✅ | Design Pattern Established ✅

---

## What Was Built Today

### 1. Cutscene Infrastructure ✅

**Location:** `index.html` (lines 2157-2339)

**Components:**
- `createCharacter()` - Creates 3-voxel tall characters (boots, body, head)
- `initCharacterGroup()` - Loads character group from test map JSON
- `consumeNextActions()` - Player interface that consumes action queues
- `executeAction()` - Dispatches actions to handlers (move, climb, wait)
- `animateCharacterMove()` - Smooth 1-second movement with cubic easing
- `updateCharacterAnimations()` - Frame-by-frame animation update

**Design Pattern:**
- Action queue consumption (declarative)
- Player interface consumes actions in parallel
- Each character has independent action queue
- Actions are validated before adding to queue
- Generic execution system (extensible for new action types)

### 2. Test 01: Parallel Forward Movement ✅

**File:** `test-maps/cutscene-test-01-parallel.json`
**URL:** `http://100.93.126.24:8080/?test=cutscene-test-01-parallel`

**Validates:**
- ✅ Action queue consumption
- ✅ Parallel character movement (5 characters simultaneously)
- ✅ Player interface pattern
- ✅ Smooth animation (1 second per action, 1.5s delay between waves)
- ✅ Auto-progression through action queues

**Results:**
- 5 characters spawn in rows (Z=-2 to Z=2)
- All move forward together in 4 steps (X: 2 → 6 → 10 → 14 → 18)
- Animations complete before next action consumed
- Console logs show action consumption

### 3. JSON Standard & Validation System ✅

**Problem Identified:**
- Hex color notation (0x228b22) is INVALID JSON
- Caused recurring "syntax error" across sessions
- JavaScript naturally uses hex, but JSON requires decimal

**Solution:**
- **TEST-JSON-STANDARD.md** - Complete standard with templates and reference
- **validate-test-json.py** - Validation script to check for hex colors
- **fix-hex-colors.py** - Auto-fix script to convert hex → decimal

**Testing:**
1. ✅ Confirmed hex colors break JSON parsing
2. ✅ Confirmed decimal colors work correctly
3. ✅ Validation script detects hex notation
4. ✅ Fix script auto-converts to decimal

---

## Next Steps

### Test 02: Complex Choreography (Ready to Build)

**Goal:** Test varied actions and path complexity

**Features:**
- Same grass rectangle
- Different actions per character:
  - Character 1: Diagonal movement
  - Character 2: Climb up a block
  - Character 3: Cross another character's path
  - Character 4: Wait action
  - Character 5: Complex path (forward + diagonal + climb)

**Purpose:**
- Validates action variety
- Tests path independence
- Confirms climb action works
- Tests wait/timing

### Test 03: Actual Cutscene (Act 1-3) - IN PROGRESS

**Map:** Bridge, ruins, river (complete-scene.json)
**File:** `test-maps/cutscene-act-1-2-3.json`
**URL:** `http://100.93.126.24:8080/?test=cutscene-act-1-2-3`

#### Phase 1: Static Choreography (COMPLETE ✅)

**Status:** Deep exploration and repositioning complete, ready for Phase 2

**What's Complete:**
- ✅ 6 mercenary characters defined with unique colors and roles
  - Kael (Scholar), Sera (Artist), Finn (Storyteller), Mira (Storyteller), Lyra (Apprentice), Toby (Youth)
- ✅ Act 1: Bridge crossing (X=0 → X=12) at Z=-1 (bridge level)
- ✅ Act 1: Deep ruins exploration with varied paths
  - Kael: Reaches Z=-9 (deepest vertical descent), north side platform (Y=2)
  - Sera: Reaches X=20 (farthest east), center path
  - Toby: Reaches X=20, Z=-8 (both far and deep)
  - All characters explore unique paths through ruins
- ✅ Act 2: Characters reposition/regroup from deep ruins to mid-map
  - Characters converge from spread-out positions (X=15-20) to clustered (X=13-16)
  - This is curiosity-driven regrouping ("what's happening?"), not retreat
- ✅ Act 3: REMOVED entirely
  - No retreat movements in cutscene
  - Cutscene ends with characters at X=13-16 (mid-map)
  - Actual retreat is handled during gameplay

**Design Refinement (2026-02-02):**
- Removed 89 actions across 6 characters (all Act 3 retreat movements)
- Characters now end at X=13-16 instead of X=0-2
- Cutscene properly sets up crisis without resolving it
- Player will coordinate retreat during gameplay tutorial

**Design Decision (2026-02-02):**
See `docs/design/CUTSCENE-ACT-SEQUENCE-DECISION.md` for full context.

**Event Sequence:**
1. Anomaly appears (in deep ruins)
2. Rain starts (triggered by anomaly)
3. Glimpse of zombies (partially visible, rising)
4. **Partial retreat** (motivated by zombie threat)
5. Startled group (zombies fully visible)
6. **Transition to gameplay** (cutscene ends, player takes control)

**Key Insight:** Cutscene sets up crisis, gameplay resolves it. Characters should be mid-map (X=10-13) when gameplay begins, with zombies visible behind them.

**Next Steps:**
1. Modify all 6 character Act 3 retreat paths to end at X=10-13
2. Test refined choreography in browser
3. Commit Phase 1 complete
4. Begin Phase 2 (add anomaly and rain)

#### Phase 2: Add Anomaly (NOT STARTED)

**Planned Features:**
- Baby anomaly character (special model/appearance)
- Spawn in deep ruins wooden area
- Startle and flee when characters approach
- Trigger rain event
- Characters react (wait actions)

#### Phase 3: Add Zombies (NOT STARTED)

**Planned Features:**
- 3-4 zombie characters
- Spawn in river/forest floor area (X=14-18)
- Glimpse appearance (partial visibility)
- Full reveal after partial retreat
- Pursue characters (motivates retreat)

#### Phase 4: Polish & Effects (NOT STARTED)

**Planned Features:**
- Camera system (cinematic angles)
- Dialogue/reactions
- Rain particle effects
- Water rising animation
- Lighting changes (darker, atmospheric)

**Scope:** Acts 1-3 (escape/rescue are separate)

---

## Design Pattern: Action Queue System

### Interface-Based Thinking

```javascript
// Character structure
{
  id: "character-01",
  name: "Scholar",
  model: THREE.Group,
  position: {x, y, z},
  actionQueue: [
    {type: "move", to: {x, y, z}},
    {type: "climb"},
    {type: "wait", duration: 1000}
  ],
  currentAnimation: {...}
}

// Player Interface (consumes actions)
consumeNextActions() {
  characters.forEach(char => {
    action = char.actionQueue.shift()
    executeAction(char, action)
  })
}

// Action Execution (strategy pattern ready)
executeAction(character, action) {
  switch(action.type) {
    case 'move': animateCharacterMove(...)
    case 'climb': animateCharacterClimb(...)
    case 'wait': animateCharacterWait(...)
  }
}
```

### Why This Pattern Works

1. **Declarative** - Actions are data, not code
2. **Extensible** - New action types = add new case
3. **Parallel** - All characters consume simultaneously
4. **Validated** - Actions validated before queuing
5. **Reusable** - Same system for cutscenes AND blueprint mode

### Future: Blueprint Mode

This exact pattern will be used for blueprint mode:
- Player creates templates (action sequences)
- Blueprint mode consumes actions from multiple units
- Parallel execution = core differentiator from Fire Emblem
- Action validation = constraint satisfaction check

**Reference:** DECLARATIVE-EVENT-SYSTEM-NOTES.md

---

## Files Created/Modified

### New Files
- `test-maps/cutscene-test-01-parallel.json` - First cutscene test
- `DECLARATIVE-EVENT-SYSTEM-NOTES.md` - Future blueprint system design
- `TEST-JSON-STANDARD.md` - JSON standard and prevention system
- `validate-test-json.py` - Validation script
- `fix-hex-colors.py` - Auto-fix script
- `CUTSCENE-TEST-INDEX.md` - Updated with cutscene tests
- `CUTSCENE-SYSTEM-STATUS.md` - This file

### Modified Files
- `index.html` - Added cutscene system (2157-2339)
  - Extended game state with cutscene properties
  - Created character creation functions
  - Implemented action queue system
  - Added animation loop integration

---

## Lessons Learned

### 1. JSON Hex Color Issue
**Problem:** Hex notation breaks JSON across sessions
**Solution:** Standard + validation scripts
**Prevention:** Always use decimal, validate before commit

### 2. Simplicity First
**Approach:** Hardcode cutscene, extract patterns later
**Why:** Get working reference, learn what's actually needed
**Result:** Clean action queue pattern emerged naturally

### 3. Interface Thinking
**Pattern:** Actions are interfaces to fundamental mechanics
**Benefit:** Reuses existing movement code from tests
**Future:** Same actions work in cutscenes AND gameplay

---

## Testing Checklist

- [x] Test 01: Parallel forward movement
- [x] JSON validation script works
- [x] Hex color fix script works
- [x] Documentation complete
- [ ] Test 02: Complex choreography (deferred)
- [x] Test 03 Phase 1: Acts 1-3 static choreography (deep exploration - needs refinement)
- [ ] Test 03 Phase 2: Add anomaly
- [ ] Test 03 Phase 3: Add zombies
- [ ] Test 03 Phase 4: Camera, dialogue, lighting, rain effects

---

## For Future Sessions

**If building cutscenes:**
1. Read this file for current status
2. Use TEST-JSON-STANDARD.md for JSON format
3. Validate test maps: `python3 validate-test-json.py <file>`
4. Reference existing test for patterns

**If building blueprint mode:**
1. Read DECLARATIVE-EVENT-SYSTEM-NOTES.md
2. Use cutscene action queue as reference implementation
3. Extend with AP regeneration and timeline
4. Add template → event sequence compiler

---

**Status:** Foundation complete, ready for Test 02
**Next Session:** Build complex choreography test OR jump to actual cutscene

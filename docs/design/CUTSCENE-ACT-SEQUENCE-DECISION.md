# Cutscene Act Sequence - Design Decision

**Date:** 2026-02-02
**Status:** Design Clarified - Ready for Implementation

---

## User's Exact Words

**Initial clarification (2026-02-02):**
> "I think, anomaly appears, then rain, then glimpse of zombies, partial retreat (as a result of the zombies) then startled group (zombies fully visible, and only then transition into gameplay. that is order of events."

**Further clarification (2026-02-02):**
> "I want their partial retreat to occur only after the anomaly is startled. because it's more of a 'what's happening, reposition to get a better view' rather than any sort of retreat (since they don't know to retreat until after the zombies are already there. the objective of the gameplay section IS to retreat)."

---

## Interpretation & Implementation Plan

### Sequence of Events (Cutscene Order)

1. **Deep Exploration (Act 1)**
   - Characters are spread out in ruins (X=15-20, Z=-7 to -9)
   - Each exploring different areas independently
   - Peaceful, curious investigation

2. **Anomaly Appears & Is Startled (Act 2 begins)**
   - Baby anomaly encountered in dark/wooden area
   - Anomaly is startled by group presence
   - Anomaly flees

3. **Rain Starts (Act 2 continues)**
   - Triggered by anomaly (reflexive response, like octopus inking)
   - Weather/lighting changes begin
   - Characters notice something strange is happening

4. **Reposition to Get Better View (Act 2 continues)**
   - **NOT a retreat** - they don't know there's danger yet
   - Characters move to regroup / get better view of what's happening
   - "What was that?" / "What's going on?" energy
   - Move from spread-out positions to mid-map area (X=10-13)
   - Curiosity-driven, not fear-driven

5. **Glimpse of Zombies (Act 2/3 transition)**
   - Water level rising in river/forest floor
   - First zombie sightings (partially visible, emerging)
   - Characters notice movement/threat
   - Growing concern: "Wait... what is that?"

6. **Zombies Fully Visible (Act 3)**
   - Zombies clearly revealed
   - Multiple zombies, clear threat
   - Group realization: "We need to get out of here!"

7. **Startled Group Moment (Act 3)**
   - Brief reaction moment
   - Final cutscene beat before gameplay

8. **Transition to Gameplay**
   - Cutscene ends
   - Player takes control of group
   - Group is mid-map (X=10-13), zombies visible behind them
   - Rain active, atmospheric tension
   - **Objective:** Player must coordinate the ACTUAL retreat to safety

---

## Current Implementation Status

**What Exists:**
- Act 1: Bridge crossing and deep ruins exploration ✓
- Act 2: Regroup moment (currently has some "repositioning" moves) ✓
- Act 3: FULL retreat to X=0-2 (WRONG - this should not exist in cutscene) ❌

**What Needs to Change:**
- Act 2 should be expanded to include:
  - Anomaly appearance and startle
  - Rain trigger
  - **Repositioning moves** (curiosity-driven: "what's happening? let's regroup")
  - Characters converge from spread-out positions (X=15-20) to mid-map (X=10-13)
  - This is NOT a retreat - they don't know about danger yet

- Act 3 should be very brief:
  - Glimpse of zombies (partial visibility)
  - Full zombie reveal
  - Startled group moment (wait actions, reactions)
  - **END** - cutscene stops here

- Act 3 should NOT include:
  - ❌ Any retreat movement (that's gameplay)
  - ❌ Characters moving back toward X=0-2
  - ❌ Escape coordination

**What Comes After Cutscene:**
- Gameplay begins immediately after startle
- Group is mid-map (X=10-13), zombies visible at X=14-18
- Rain active, zombies pursuing
- **Player's job:** Coordinate the ACTUAL retreat to safety (X=0-2)
- This is the gameplay tutorial moment

---

## Cutscene Ending Position

**Target End State (when cutscene ends):**
- Characters positioned around X=10-13 (on/near bridge)
- Characters are stationary (no movement, just startled/reacting)
- Zombies visible at X=14-18 (ruins/river area)
- Rain active, atmospheric tension
- Clear threat visible, clear escape route (bridge back to X=0)
- Group is NOT moving - they're frozen in shock/surprise

**Why This Works:**
- Cutscene ends at moment of realization ("We're in danger!")
- Player immediately takes control to coordinate escape
- Tutorial moment: Use blueprint mode under pressure to retreat
- Natural transition: Narrative creates crisis, gameplay resolves it
- Characters aren't safe, player must act

**Key Insight:**
The "repositioning" in Act 2 is NOT tactical retreat - it's curiosity-driven regrouping to see what's happening. The ACTUAL retreat is the player's responsibility during gameplay.

---

## Implementation Notes

### Phase 1 Refinement (IMMEDIATE)
- **REMOVE Act 3 retreat movements** - cutscene should NOT include escape
- **MODIFY Act 2:** Change existing "retreat" moves to "repositioning" moves
- Characters should converge from deep ruins (X=15-20) to mid-map (X=10-13)
- These moves are curiosity-driven regrouping, not fear-driven retreat
- Characters should end up clustered around X=10-13 area
- Final positions should be STATIONARY (no ongoing movement)

### Phase 2 Tasks (Add Anomaly & Rain)
- Create baby anomaly character
- Script anomaly spawn in deep ruins
- Script anomaly startle moment (characters notice)
- Script anomaly flee path
- Add rain trigger event
- Characters respond with repositioning (already scripted in Phase 1)

### Phase 3 Tasks (Add Zombies)
- Create 3-4 zombie characters
- Script zombie spawn positions (river area, X=14-18)
- Script zombie "glimpse" appearance (partial visibility during repositioning)
- Script zombie full reveal (when characters reach mid-map positions)
- Add "startled group" moment (wait actions, reactions)
- **Cutscene ends here** - no escape movements

### Phase 4 Tasks (Polish & Effects)
- Camera system (follow action, show zombies)
- Rain particle effects
- Water rising animation
- Lighting changes (darker, atmospheric)
- Character dialogue/reactions

---

## Testing Validation

**Cutscene should demonstrate:**
1. ✓ Characters explore deep ruins naturally
2. ⧗ Anomaly encounter creates inciting incident
3. ⧗ Rain provides atmospheric shift
4. ⧗ Zombie glimpse creates tension
5. ⧗ Partial retreat shows character response
6. ⧗ Full zombie reveal escalates threat
7. ⧗ Transition to gameplay feels natural
8. ⧗ Player understands they must escape

---

## Design Philosophy Note

**Key Principle:** Cutscene sets up the situation, gameplay resolves it.

- Cutscene shows: Anomaly → Rain → Zombies → Danger
- Gameplay handles: Escape → Coordination → Blueprint tactics

The cutscene doesn't resolve the crisis - it creates it. The player resolves it through gameplay.

---

**Next Steps:**
1. **REMOVE Act 3 retreat movements entirely** from cutscene-act-1-2-3.json
2. **MODIFY Act 2 movements** - reframe existing moves as "repositioning to regroup"
3. Ensure all characters end at X=10-13 positions after Act 2
4. Ensure characters are STATIONARY when cutscene would end (before Phase 3 adds zombie reveal)
5. Test modified choreography
6. Commit refined version
7. Proceed to Phase 2 (anomaly implementation)

**Files to Modify:**
- `test-maps/cutscene-act-1-2-3.json` - Remove Act 3, refine Act 2
- `CURRENT-WORK.md` - Update with this design decision (already done)
- `docs/status/CUTSCENE-SYSTEM-STATUS.md` - Document Phase 1 refinement

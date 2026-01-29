# Design Decisions

**Last Updated:** 2026-01-28
**Purpose:** Document the "why" behind technical choices to prevent regression and guide future development.

---

## Table of Contents

1. [Movement System](#movement-system)
2. [Testing Strategy](#testing-strategy)
3. [Rendering & Performance](#rendering--performance)
4. [Input Handling](#input-handling)
5. [Data Formats](#data-formats)
6. [Code Organization](#code-organization)
7. [User Experience](#user-experience)

---

## Movement System

### Decision: Unified Movement Logic

**What:** Main game and test preview share identical movement functions.

**Why:**
- **Trust in Tests:** If a test passes, the main game works identically
- **Single Source of Truth:** No divergence between test and production behavior
- **Refactor Safety:** Change once, update everywhere
- **Bug Fix Efficiency:** Fix applies to both contexts

**Alternative Considered:** Separate implementations
- ❌ Would require manual synchronization
- ❌ Risk of tests passing but game failing (or vice versa)
- ❌ Double maintenance burden

**Implementation:**
```javascript
// Both contexts use same functions:
hasVoxel(x, y, z) // Works on game.terrain or game.previewTerrain
getTerrainHeightAt(x, z) // Same logic for both
```

**Trade-off Accepted:** Functions must accept context parameters, can't assume global state.

---

### Decision: Vector Normalization Before Scaling

**What:** Diagonal movement vectors are normalized to unit length before applying speed modifiers.

**Why:**
- **Physics Accuracy:** W+D should move at same speed as W alone
- **User Experience:** Predictable, consistent movement speed
- **Fairness:** No accidental diagonal speed advantage in tactical game

**Problem Solved:**
- Original: W+D moved at √2 ≈ 1.414x speed (Pythagorean theorem)
- Fixed: Normalize vector → multiply by speed → consistent 1.0 unit/frame

**Math:**
```javascript
// BEFORE (wrong)
moveX = 1; moveZ = 1;
// Length = sqrt(1² + 1²) = 1.414

// AFTER (correct)
moveX = 1; moveZ = 1;
magnitude = sqrt(1² + 1²); // 1.414
moveX /= magnitude; // 0.707
moveZ /= magnitude; // 0.707
// Length = sqrt(0.707² + 0.707²) = 1.0
```

**Alternative Considered:** Limit diagonal to cardinal speed
- ❌ Feels unresponsive (diagonal "sticks" to cardinal)
- ❌ Breaks smooth camera-relative movement

---

### Decision: Gravity as Constant Force

**What:** Gravity applies every frame at 10 units/second, regardless of player action.

**Why:**
- **Realism:** Matches player expectations from other 3D games
- **Safety:** Prevents floating if auto-descent fails
- **Simplicity:** No complex state machine for "falling" vs "standing"

**Implementation:**
```javascript
// Every frame:
if (playerY > groundY + 1) {
  playerY -= 10 * deltaTime;
}
```

**Trade-off:** Gravity can override auto-descent if auto-descent is too slow. Solution: Auto-descent is instant, gravity only applies when no ground below.

---

### Decision: Auto-Climb Limited to 1 Block

**What:** Auto-climb only works for obstacles exactly 1 voxel high.

**Why:**
- **Deliberate Choice:** 2+ blocks requires manual climb (Space key)
- **Tactical Depth:** Height matters in combat (high ground advantage)
- **Predictability:** Players know when they'll auto-climb vs need to climb

**Alternative Considered:** Auto-climb any height
- ❌ Trivializes vertical gameplay
- ❌ Makes height advantage meaningless
- ❌ Reduces tactical decision space

**Future Extension:** Unit-specific climb heights (climber: 3 blocks, ground: 1 block).

---

### Decision: Auto-Descent Only 1 Level

**What:** Walking onto lower terrain auto-descends exactly 1 block. Larger drops require walking off edge (gravity).

**Why:**
- **Safety:** Prevents accidental falls off cliffs
- **Deliberate Movement:** Large drops require walking off edge consciously
- **Consistent with Climb:** Symmetry with 1-block auto-climb

**Mechanic Distinction:**
- **Auto-Descent:** Walk onto lower terrain, descend 1 block
- **Gravity/Falling:** Walk into empty space, fall any distance

**Test Coverage:**
- testWalkDownTerrain (auto-descent)
- testWalkOffLedge (gravity fall)

---

## Testing Strategy

### Decision: Micro-Map Pattern

**What:** Each test is a minimal 5x5 (or smaller) environment testing one mechanic.

**Why:**
- **Isolation:** Focus on single mechanic, no confounding variables
- **Debuggability:** Easy to see what went wrong
- **Reusability:** Copy-paste voxel patterns into macro maps
- **Fast Iteration:** Small tests run quickly

**Comparison to Alternatives:**

| Approach | Pros | Cons |
|----------|------|------|
| **Micro-Maps** (chosen) | Isolated, debuggable, reusable | Doesn't test integration |
| Large Complex Maps | Tests interaction | Hard to debug, slow |
| Unit Tests (code-level) | Fast, automatable | Doesn't test visuals |
| No Tests | Fast development | High regression risk |

**Strategy:** Micro-maps for mechanics, macro-maps for integration, unit tests for math.

---

### Decision: Visual Validation Over Pure Automation

**What:** Tests include visual animation playback, not just pass/fail assertions.

**Why:**
- **Human Judgement:** "Does this feel right?" matters in games
- **Debugging:** See exactly what went wrong
- **Communication:** Show stakeholders what mechanics do
- **Trust:** Seeing is believing

**Automation Role:**
- Run tests automatically (Playwright)
- Verify position math (5% tolerance)
- Detect regressions
- **But:** Human still watches animation to confirm correctness

**Quote from METHODOLOGY.md:**
> "Tests aren't just math - users see and confirm movement works."

---

### Decision: 5% Position Tolerance

**What:** Test passes if player reaches within 5% of goal distance (minimum 1.0 unit).

**Why:**
- **Floating Point:** JavaScript floats aren't exact
- **Animation:** Smooth interpolation may not land exactly on integer
- **Reasonable:** 5% tolerance = 0.05 units on 1-unit movement (acceptable)

**Formula:**
```javascript
const tolerance = Math.max(1.0, totalDistance * 0.05);
```

**Example:**
- Distance = 10 units → tolerance = 0.5 units
- Distance = 2 units → tolerance = 1.0 units (minimum)

**Alternative Considered:** Exact match (0.0 tolerance)
- ❌ Fails due to floating point rounding
- ❌ Too strict for visual game

---

### Decision: Test-First Development

**What:** Create test before implementing mechanic.

**Why:**
- **Clear Specification:** Test defines "done"
- **Prevents Gold-Plating:** Only implement what's tested
- **Regression Safety:** Can't accidentally break untested mechanics
- **Documentation:** Tests show how mechanic should work

**Workflow:**
1. Define mechanic in mechanics-graph.json
2. Create test map (expected behavior)
3. Implement mechanic
4. Run test until it passes
5. Mark as tested

**Not Pure TDD:** We don't write tests at code unit level, but at mechanic level.

---

## Rendering & Performance

### Decision: Three.js Over Custom WebGL

**What:** Use Three.js library instead of raw WebGL.

**Why:**
- **Productivity:** Scene graph, camera, lighting built-in
- **Maintainability:** Well-documented, active community
- **Features:** OrbitControls, shadows, fog, post-processing
- **Performance:** Optimized by experts

**Trade-off:** ~600KB library size
- Acceptable for web game (images often larger)
- Loaded from CDN (cached across sites)

**Alternative Considered:** Raw WebGL
- ❌ Months of development for basic features
- ❌ High bug risk (WebGL is low-level)
- ✅ Would be ~50KB smaller (not worth it)

---

### Decision: No Instanced Meshes (Yet)

**What:** Each voxel is a separate Mesh object.

**Why:**
- **Simplicity:** Easier to add/remove voxels dynamically
- **Performance OK:** 60 FPS with 100 voxels
- **Premature Optimization:** Don't optimize until metrics show need

**When to Implement:**
- After 500+ voxels in single scene
- If FPS drops below 30
- When profiling shows mesh creation as bottleneck

**Future Plan:**
```javascript
// Replace 500 separate meshes with:
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshLambertMaterial({ color: 0x00FF00 });
const instancedMesh = new THREE.InstancedMesh(geometry, material, 500);

// Set position for each instance:
for (let i = 0; i < 500; i++) {
  matrix.setPosition(x, y, z);
  instancedMesh.setMatrixAt(i, matrix);
}
```

---

### Decision: 500ms Animation Duration

**What:** Preview animations move player over 500 milliseconds with easing.

**Why:**
- **Visibility:** Fast enough to not bore, slow enough to see
- **Smoothness:** Easing function looks natural
- **Debuggability:** Can see intermediate positions

**Easing Function (EaseInOutQuad):**
```javascript
const eased = progress < 0.5
  ? 2 * progress * progress
  : 1 - Math.pow(-2 * progress + 2, 2) / 2;
```

**Alternative Timings Considered:**
- 250ms: Too fast, hard to see
- 1000ms: Too slow, boring
- Instant: Not visible at all

**User Feedback:** 500ms confirmed as "smooth" and "clearly visible".

---

## Input Handling

### Decision: Constraint Enforcement at Input Level

**What:** Block invalid inputs before they reach movement logic.

**Why:**
- **Separation of Concerns:** Movement code doesn't need to know about test constraints
- **Consistency:** Works identically for keyboard and mobile
- **Debuggability:** Console logs show blocked inputs
- **Reusability:** Same constraint system for all tests

**Implementation:**
```javascript
function handleKeyDown(e) {
  if (!isInputAllowed(e.key)) {
    console.log(`Blocked: ${e.key}`);
    return;
  }
  // Continue with normal input handling
}
```

**Alternative Considered:** Check constraints in movement logic
- ❌ Movement code becomes test-aware (tight coupling)
- ❌ Harder to maintain
- ❌ Constraint violations happen mid-movement (jarring)

---

### Decision: Mobile Controls Always Visible

**What:** Virtual joystick and buttons use CSS media query, not JavaScript detection.

**Why:**
- **Simplicity:** No device detection code
- **Accuracy:** CSS knows touch capability
- **Testability:** Works in browser dev tools mobile mode
- **Edge Cases:** Handles tablets with mouse correctly

**Media Query:**
```css
@media (max-width: 768px), (hover: none) {
  #mobileControls { display: block; }
}
```

**Why Two Conditions:**
- `max-width: 768px` → Small screens (phones)
- `hover: none` → Touch-primary devices (tablets)

**Alternative Considered:** JavaScript `navigator.userAgent`
- ❌ Unreliable (user agent spoofing)
- ❌ Doesn't detect tablets with mouse
- ❌ Doesn't work in dev tools emulation

---

### Decision: Joystick Threshold 30%

**What:** Joystick must be deflected 30% (of max radius) before registering input.

**Why:**
- **Dead Zone:** Prevents drift from accidental touch
- **Intentional Input:** User must deliberately move joystick
- **Ergonomics:** Thumb resting on joystick doesn't trigger movement

**Value Selection:**
- 10%: Too sensitive, accidental inputs
- 50%: Too strict, feels unresponsive
- **30%: Sweet spot** (common in console games)

**Implementation:**
```javascript
const threshold = 0.3;
if (Math.abs(normalizedX) > threshold) {
  // Register input
}
```

---

## Data Formats

### Decision: Decimal Colors in JSON

**What:** Use decimal RGB (65280) instead of hex (0x00FF00) in test maps.

**Why:**
- **JSON Spec:** JSON doesn't support hex literals
- **Syntax Error:** `0x00FF00` caused parse failures
- **Reliability:** Decimal always works

**Convenience Layer:** TestBuilder maps color names:
```javascript
.addVoxel(0, 0, 0, 'green') // → 65280 in JSON
```

**Alternative Considered:** Hex strings
```json
{ "color": "#00FF00" }
```
- ✅ Human-readable
- ❌ Requires parsing (`parseInt(color.slice(1), 16)`)
- ❌ More complex, prone to errors

**Decision:** Keep decimal for simplicity, use TestBuilder for convenience.

---

### Decision: Flat Voxel Array

**What:** Voxels stored as array of `{x, y, z, color}` objects, not 3D array.

**Why:**
- **Sparsity:** Most of 3D space is empty
- **JSON Size:** Only store voxels that exist
- **Flexibility:** Easy to add/remove voxels

**Comparison:**

| Format | Memory (100 voxels in 100³ space) | Access Time |
|--------|----------------------------------|-------------|
| **Flat Array** (chosen) | 100 objects | O(n) search |
| 3D Array `[x][y][z]` | 1,000,000 elements | O(1) access |
| Hash Map `"x,y,z"` | 100 entries | O(1) lookup |

**Runtime Optimization:** In-memory, we use hash map (`game.terrain = Map<"x,y,z", true>`).

**Storage:** JSON uses flat array (smaller file size).

**Conversion:** On load, array → hash map.

---

### Decision: Mechanic ID as String

**What:** Mechanics identified by snake_case string (`basic_movement`), not numeric ID.

**Why:**
- **Readability:** Clear what mechanic does
- **Stable:** Renumbering not needed when adding mechanics
- **Grep-able:** Easy to search codebase for mechanic usage
- **JSON Keys:** JavaScript objects use strings anyway

**Naming Convention:**
- `basic_movement` ✅ (descriptive)
- `movement_1` ❌ (meaningless number)
- `basicMovement` ❌ (camelCase inconsistent with JSON style)

---

## Code Organization

### Decision: Single-File Architecture

**What:** Entire game in `index.html` (HTML + CSS + JavaScript), no build step.

**Why:**
- **Deployment:** Works on Termux without Node.js
- **Debugging:** View source = actual code (no source maps)
- **Simplicity:** No webpack/rollup/vite configuration
- **Iteration Speed:** Edit file, refresh browser, done

**Trade-offs:**
- ❌ **Harder to Navigate:** 2600+ lines in one file
- ❌ **No Module System:** Can't `import`/`export`
- ❌ **Global Scope:** Everything in global `game` object

**Mitigation:**
- Clear function comments
- Logical sections (comments at line X)
- Search-friendly naming

**When to Split:**
- If file exceeds 5000 lines
- If multiple developers work simultaneously
- If build step becomes necessary (TypeScript, minification)

**Current Status:** 2600 lines, single developer → single file works.

---

### Decision: Global `game` Object

**What:** All game state in single global object.

**Why:**
- **Simplicity:** No module system, need shared state
- **Debugging:** `console.log(game)` shows entire state
- **No Prop Drilling:** Any function can access game state

**Structure:**
```javascript
const game = {
  // Main game
  scene, camera, renderer, controls, player,
  playerPos, terrain, keys, clock, testMode, testConfig,

  // Preview
  previewScene, previewCamera, previewRenderer,
  previewPlayer, previewPlayerPos, previewKeys,
  animationRunning, manualPlayMode,

  // Metadata
  mechanicsData, currentMechanic, menuOpen
};
```

**Alternative Considered:** Separate objects per system
```javascript
const mainGame = { ... };
const preview = { ... };
const menu = { ... };
```
- ✅ Better encapsulation
- ❌ Functions need to pass objects around
- ❌ More verbose

**Current Choice:** Global `game` for simplicity.

---

### Decision: No TypeScript

**What:** Use vanilla JavaScript (ES6+), not TypeScript.

**Why:**
- **No Build Step:** Maintains simplicity
- **Termux Friendly:** No compilation needed
- **Rapid Prototyping:** Type errors don't block testing

**Trade-offs:**
- ❌ **No Type Safety:** Runtime errors possible
- ❌ **No IDE Autocomplete:** Manual docs lookup
- ✅ **Faster Iteration:** No compile step

**Mitigation:**
- JSDoc comments for complex functions
- Runtime validation (TestBuilder)
- Comprehensive testing

**When to Add TypeScript:**
- Multiple developers
- Large codebase (10,000+ lines)
- Frequent refactoring

**Current Status:** Vanilla JS works for single-developer prototype.

---

## User Experience

### Decision: Feedback Form Over Automatic Pass/Fail

**What:** After manual testing, user fills out feedback form instead of automatic test verdict.

**Why:**
- **Subjective Quality:** "Does this feel right?" is important
- **Bug Discovery:** Users notice issues automation misses
- **Learning:** User explains what went wrong (valuable data)
- **Trust:** User confirms behavior, not just machine

**Form Options:**
- Movement didn't work as expected
- Controls were confusing
- I couldn't figure out how to proceed
- It worked fine, just exploring
- Other (freeform text)

**Future:** Aggregate feedback data for analytics.

---

### Decision: Test Menu as Grid

**What:** Mechanics displayed in card grid, not list.

**Why:**
- **Scanability:** Easier to browse visually
- **Status at a Glance:** Color-coded badges
- **Responsive:** Works on desktop and mobile
- **Scalable:** Can add 20+ mechanics without scrolling issues

**Visual Hierarchy:**
1. Mechanic Name (largest)
2. Description (medium)
3. Status badges (smallest)

**Color Coding:**
- Green border: Implemented
- Blue border: Tested
- Gray border: Not implemented
- Red border: Buggy

**Alternative Considered:** Tree view (dependency hierarchy)
- ✅ Shows relationships
- ❌ Complex to navigate
- ❌ Overkill for 13 mechanics

---

### Decision: Modal Preview Over Inline

**What:** Test preview opens in modal overlay, not inline on page.

**Why:**
- **Focus:** No distractions from main game
- **Immersion:** Dark overlay focuses attention
- **Responsive:** Works on mobile (full-screen modal)
- **Reusability:** Can open preview from main game or menu

**Animation:**
```css
#testPreview {
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s;
}

#testPreview.active {
  opacity: 1;
  pointer-events: all;
}
```

**Escape Hatch:** Close button (×) in top-right corner.

---

### Decision: Console Logging for Debug

**What:** Extensive `console.log()` statements throughout movement code.

**Why:**
- **Debuggability:** See exactly what's happening each frame
- **Performance:** console.log is fast in modern browsers
- **Removable:** Can strip in production build (future)
- **User-Facing:** Users can report console output in bug reports

**Log Format:**
```javascript
console.log(`Falling: y=${oldY.toFixed(2)} -> ${newY.toFixed(2)}`);
console.log(`Auto-climb: ${x},${y},${z} -> ${newX},${newY},${newZ}`);
console.log(`Input "${key}" blocked by constraints`);
```

**Production Plan:** Add build step to strip console.log (when needed).

---

## Summary of Key Decisions

| Decision | Rationale | Trade-off |
|----------|-----------|-----------|
| Unified movement logic | Trust in tests | More parameters |
| Vector normalization | Consistent speed | Slight complexity |
| Micro-map pattern | Isolation, debuggability | No integration tests yet |
| Visual validation | Human judgment matters | Can't fully automate |
| Three.js over WebGL | Productivity, features | 600KB library |
| Single-file architecture | No build step | Harder to navigate |
| Global game object | Simplicity, debugging | Potential naming conflicts |
| Decimal colors in JSON | JSON spec compliance | Less readable |
| Modal preview | Focus, responsive | Extra UI layer |
| Console logging | Debuggability | Verbose console |

---

## Lessons Learned

### What Worked Well

1. **Test-First Approach:** Prevented regressions, clear specifications
2. **Micro-Maps:** Easy to debug, reusable patterns
3. **Unified Logic:** No test/production divergence
4. **Mobile-First:** Touch controls worked first try
5. **Documentation:** Captured decisions early, prevents forgetting

### What We'd Do Differently

1. **Vector Normalization Earlier:** Diagonal movement "finnicky" for whole session
2. **Async/Await from Start:** Gravity bug could've been avoided
3. **TypeScript Consideration:** Type safety would've caught some errors
4. **Separate Preview Scene Earlier:** Initially tried to reuse main scene (messy)

### Advice for Future Sessions

1. **Read ARCHITECTURE.md First:** Understand system before changing
2. **Update Documentation:** Don't let docs fall behind code
3. **Test After Refactoring:** Even "simple" changes can break mechanics
4. **Console.log Liberally:** Better verbose than blind
5. **Ask "Why?":** If decision seems arbitrary, it's probably documented here

---

**Related Documents:**
- `ARCHITECTURE.md` - Overall system design
- `METHODOLOGY.md` - Test-driven development workflow
- `TEST-PATTERNS.md` - Test creation patterns
- `CODE-STRUCTURE.md` - Detailed code organization

**Next:** Read `CODE-STRUCTURE.md` for line-by-line code organization guide.

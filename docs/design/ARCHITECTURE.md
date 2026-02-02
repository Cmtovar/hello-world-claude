# Architecture Documentation

**Last Updated:** 2026-01-28
**Version:** 1.0.0
**Status:** Foundation Complete

## Purpose

This document describes the architectural design of the 3D Tactical Movement Game. It serves as a comprehensive reference for understanding the system's structure, design patterns, and technical decisions. Future sessions should read this document before making changes to avoid regression.

---

## System Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Browser Environment                      │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │  Main Game   │  │ Test Preview │  │  Test Menu UI   │  │
│  │   (index)    │  │    Modal     │  │   (Selection)   │  │
│  └──────┬───────┘  └──────┬───────┘  └────────┬────────┘  │
│         │                  │                    │            │
│  ┌──────▼──────────────────▼────────────────────▼────────┐  │
│  │           Movement Engine (Unified Logic)             │  │
│  │  • Cardinal/Diagonal Movement   • Gravity/Falling    │  │
│  │  • Auto-climb/Auto-descent      • Manual Climb/Desc  │  │
│  └──────┬────────────────────────────────────────────────┘  │
│         │                                                    │
│  ┌──────▼────────────────────────────────────────────────┐  │
│  │              Three.js Rendering Layer                 │  │
│  │  • Voxel Geometry (Flyweight)  • Camera/Controls     │  │
│  │  • Player Mesh                 • Scene Graph         │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                    ┌───────▼────────┐
                    │  Data Layer    │
                    │ • Test Maps    │
                    │ • Mechanics    │
                    │   Graph        │
                    └────────────────┘
```

### Core Philosophy

1. **Test-Driven Development**: All mechanics are tested in isolation before use
2. **Unified Logic**: Main game and test preview share identical movement code
3. **Micro → Macro**: Small tested patterns compose into larger levels
4. **Visual Validation**: Tests are visually observable, not just mathematical
5. **Progressive Enhancement**: Mobile controls layer on top of desktop

---

## Component Architecture

### 1. Main Game (`index.html` - Main Game Section)

**Purpose:** The playable 3D voxel game with full movement mechanics.

**Key Features:**
- Full 3D rendering with Three.js
- OrbitControls camera system
- Keyboard + mobile touch input
- Gravity and collision detection
- Test map loading via URL parameter

**Initialization Flow:**
```javascript
init() // async
  ├─ Create Three.js scene, camera, renderer
  ├─ Setup lighting (ambient + directional)
  ├─ Setup OrbitControls
  ├─ Load test map (if ?test=testName) OR create default terrain
  ├─ Create player mesh
  ├─ Setup keyboard/mobile event listeners
  └─ Start animation loop
```

**Data Structures:**
```javascript
game = {
  scene: THREE.Scene,
  camera: THREE.PerspectiveCamera,
  renderer: THREE.WebGLRenderer,
  controls: OrbitControls,
  player: THREE.Mesh,
  playerPos: { x, y, z },
  terrain: Map<string, boolean>,  // "x,y,z" -> true
  keys: { [key: string]: boolean },
  clock: THREE.Clock,
  testMode: boolean,
  testConfig: TestMapConfig | null
}
```

### 2. Test Preview System (`index.html` - Preview Section)

**Purpose:** Visual 3D preview of individual mechanic tests in a modal.

**Key Features:**
- Separate Three.js scene from main game
- Animation playback with expected inputs
- Manual play mode with keyboard/touch
- Feedback collection system
- Mobile joystick integration

**Preview State:**
```javascript
game.previewScene: THREE.Scene        // Separate render target
game.previewCamera: THREE.PerspectiveCamera
game.previewRenderer: THREE.WebGLRenderer
game.previewPlayer: THREE.Mesh
game.previewPlayerPos: { x, y, z }
game.previewKeys: { [key: string]: boolean }
game.animationRunning: boolean
game.manualPlayMode: boolean
game.currentMechanic: MechanicDefinition
```

**Animation System:**
```javascript
playAnimation() {
  const inputs = testConfig.expectedInputs; // ["w", "w", "w+d", ...]
  for each input:
    1. Wait for previous movement to complete
    2. Simulate key press(es)
    3. Apply movement logic
    4. Animate over 500ms with easing
    5. Wait 200ms before next input
}
```

### 3. Test Menu (`index.html` - Menu UI)

**Purpose:** Visual selection interface for browsing and launching tests.

**Features:**
- Grid layout of mechanic cards
- Color-coded status badges (implemented/tested/buggy)
- Dependency information display
- Opens test preview modal on click

**Data Source:** `mechanics-graph.json`

### 4. Movement Engine (Unified Logic)

**Purpose:** Core movement implementation shared by main game and preview.

**Location:** Functions in `index.html` - used by both `handleMovement()` (main) and `processPreviewInput()` (preview)

**Mechanics Implemented:**

#### Basic Movement (WASD)
- Cardinal directions: North (+X), South (-X), East (+Z), West (-Z)
- Camera-relative orientation
- Vector normalization for consistent speed

#### Diagonal Movement
- Simultaneous key detection (e.g., W+D)
- Vector normalization: `magnitude = sqrt(x² + z²); x/=mag; z/=mag`
- Same speed as cardinal (1.0 unit/frame)

#### Auto-Climb
```javascript
// When walking into 1-block obstacle
if (voxel at [newX, currentY, newZ]) {
  if (!voxel at [newX, currentY + 1, newZ]) {
    // Can climb: nothing blocking above
    move to [newX, currentY + 1, newZ]
  }
}
```

#### Auto-Descent
```javascript
// When walking onto empty space
if (!voxel at [newX, currentY, newZ]) {
  if (!voxel at [newX, currentY - 1, newZ]) {
    // Can descend
    if (voxel at [newX, currentY - 2, newZ]) {
      move to [newX, currentY - 1, newZ]
    }
  }
}
```

#### Manual Climb (Space)
```javascript
// Check for obstacle in front
if (voxel at [x + dirX, currentY, z + dirZ]) {
  if (!voxel at [x + dirX, currentY + 1, z + dirZ]) {
    // Climb onto obstacle
    move to [x + dirX, currentY + 1, z + dirZ]
  }
}
```

#### Manual Descend (Shift)
```javascript
// Check if can descend 1 level
const nextY = currentY - 1;
if (nextY >= 1 && voxel at [x, nextY - 1, z]) {
  move to [x, nextY, z]
}
```

#### Gravity/Falling
```javascript
// Every frame in animate loop
const groundY = getTerrainHeightAt(floor(x), floor(z));
if (groundY >= 0) {
  const targetY = groundY + 1;
  if (currentY > targetY) {
    // Fall at 10 units/second
    currentY = max(targetY, currentY - 10 * deltaTime);
  }
}
```

### 5. Mobile Controls

**Purpose:** Touch-based input for mobile devices.

**Components:**

#### Virtual Joystick (Left Side)
- Drag-based input within 40px radius
- Translates to WASD key equivalents
- Threshold: 0.3 (30% deflection minimum)
- Auto-centers on release

#### Action Buttons (Right Side)
- Climb button (↑) → Space key
- Descend button (↓) → Shift key
- Touch start/end events

**Integration:**
- Sets `game.keys[]` just like keyboard
- Respects constraint enforcement
- Works in both main game and preview

**Auto-Show Logic:**
```css
@media (max-width: 768px), (hover: none) {
  #mobileControls { display: block; }
}
```

### 6. Constraint System

**Purpose:** Declarative test restrictions enforced at input level.

**Format (in test JSON):**
```json
{
  "constraints": {
    "allowedInputs": ["w+d", "w+a", "s+d", "s+a"],
    "blockCardinal": true,
    "maxMovements": 10,
    "requireGoalReach": true
  }
}
```

**Enforcement:**
```javascript
function isInputAllowed(key) {
  if (!constraints.allowedInputs) return true;

  // Check single key
  if (allowedInputs.includes(key)) return true;

  // Check combinations (e.g., "w+d")
  const activeKeys = Object.keys(keys).filter(k => keys[k]);
  const combo = activeKeys.sort().join('+');
  return allowedInputs.includes(combo);
}
```

**Applies to:**
- Keyboard input (handlePreviewKeyDown)
- Mobile joystick (updatePreviewJoystick)
- Mobile buttons (climbStart/descendStart)

### 7. Data Layer

#### Test Maps (`test-maps/*.json`)

**Schema:**
```json
{
  "name": "Human-readable name",
  "description": "What this tests",
  "mechanic": "mechanic_id",
  "playerStart": { "x": 0, "y": 1, "z": 0 },
  "goal": { "x": 2, "y": 1, "z": 0 },
  "voxels": [
    { "x": 0, "y": 0, "z": 0, "color": 65280 }
  ],
  "expectedInputs": ["w", "w", "w+d"],
  "constraints": {},
  "notes": "Implementation details"
}
```

**Colors (Decimal RGB):**
- Green: 65280 (0x00FF00) - Ground level
- Orange: 16753920 (0xFFA500) - Elevated platforms
- Gray: 11184810 (0xAABBAA) - Context terrain

**JSON Limitation:** No hex literals allowed, must use decimal.

#### Mechanics Graph (`mechanics-graph.json`)

**Schema:**
```json
{
  "mechanics": {
    "mechanic_id": {
      "id": "mechanic_id",
      "name": "Display Name",
      "description": "What it does",
      "dependencies": ["other_mechanic_id"],
      "status": "implemented | not_implemented | buggy",
      "tested": true | false,
      "tests": ["testMapName1", "testMapName2"],
      "notes": "Implementation notes"
    }
  },
  "testPriority": ["mechanic_id", ...],
  "criticalPath": {
    "description": "Mechanics blocking others",
    "mechanics": ["basic_movement", ...]
  },
  "unitTypes": {
    "ground": {
      "name": "Ground Unit",
      "requiredMechanics": [...]
    }
  }
}
```

---

## Design Patterns

### 1. Factory Pattern (TestBuilder)

**Location:** `test-builder.js`

**Purpose:** Programmatic test generation with validation.

**Usage:**
```javascript
const test = new TestBuilder('testMyMechanic')
  .setMechanic('basic_movement')
  .setPlayerStart(0, 1, 0)
  .setGoal(2, 1, 0)
  .addGroundTile(0, 0, 'green')
  .setExpectedInputs(['w', 'w'])
  .build(); // Returns JSON string, validates first
```

**Validation Checks:**
- Mechanic ID is set
- At least one voxel exists
- Player start has ground below (unless y=0)
- Goal has ground below (if present)
- Expected inputs are valid keys

### 2. Flyweight Pattern (Voxels)

**Current Status:** Not yet implemented (planned).

**Purpose:** Share geometry/materials for identical voxels.

**Future Implementation:**
```javascript
// Instead of creating 100 geometries:
const sharedGeometry = new THREE.BoxGeometry(1, 1, 1);
const sharedMaterial = new THREE.MeshLambertMaterial({ color: 0x00FF00 });

for (let i = 0; i < 100; i++) {
  const mesh = new THREE.Mesh(sharedGeometry, sharedMaterial);
  mesh.position.set(x, y, z);
}
// Memory: 1 geometry + 1 material (99% reduction)
```

**When to Implement:** After 20+ test maps with 500+ voxels total.

### 3. Decorator Pattern (Movement Modifiers)

**Current Status:** Not yet implemented (documented in TODO #30).

**Purpose:** Add movement modifiers (sprint, slow, knockback) without changing core logic.

**Planned Structure:**
```javascript
class MovementModifier {
  apply(vector, context) { return vector; }
}

class SprintModifier extends MovementModifier {
  apply(vector, context) {
    return vector.multiplyScalar(2.0); // 2x speed
  }
}

// Usage:
const baseMovement = calculateMovement();
const modifiedMovement = modifiers.reduce(
  (vec, mod) => mod.apply(vec, context),
  baseMovement
);
```

### 4. Observer Pattern (Feedback System)

**Location:** `#feedbackBox` in `index.html`

**Purpose:** Collect structured user feedback after manual testing.

**Flow:**
1. User plays test manually
2. Stops manual mode
3. Feedback box appears with radio options
4. User selects feedback type + optional text
5. Console logs feedback (future: send to analytics)

**Options:**
- Movement didn't work as expected
- Controls were confusing
- I couldn't figure out how to proceed
- It worked fine, just exploring
- Other (with text field)

---

## Key Technical Decisions

### 1. Single-File Architecture

**Decision:** Keep entire game in `index.html` (no build step).

**Rationale:**
- Easier deployment on Termux
- No Node.js build process required
- Simpler debugging (view source = actual code)
- Fast iteration cycle

**Trade-off:** Harder to navigate large file (2600+ lines).

**Mitigation:** Clear function comments, logical sections.

### 2. Unified Movement Logic

**Decision:** Main game and test preview use identical movement functions.

**Rationale:**
- Tests validate actual gameplay
- No divergence between test and production
- Refactor once, update everywhere
- Bug fixes apply to both contexts

**Implementation:** Functions like `hasVoxel()`, `getTerrainHeightAt()` accept position parameters, don't assume context.

### 3. Decimal Colors in JSON

**Decision:** Use decimal RGB values (65280) instead of hex (0x00FF00).

**Rationale:**
- JSON spec doesn't support hex literals
- Attempted hex caused syntax errors
- Decimal is verbose but valid

**Convenience:** TestBuilder maps color names to decimal:
```javascript
.addVoxel(0, 0, 0, 'green') // → 65280
```

### 4. Async Test Map Loading

**Decision:** Made `init()` async and await `loadTestMap()`.

**Rationale:**
- Player position was being overwritten before map loaded
- Gravity didn't work (player placed at y=0 before terrain existed)
- Async/await ensures sequential initialization

**Fix Applied:** 2026-01-28 (Task #33)

### 5. Vector Normalization

**Decision:** Normalize diagonal movement vectors to unit length.

**Rationale:**
- W+D would move √2 faster than W alone
- Causes "finnicky" controls (sometimes 2x speed)
- Normalize: `magnitude = sqrt(x² + z²); x/=mag; z/=mag`

**Result:** Consistent 1.0 unit speed in all directions.

### 6. Mobile Controls Auto-Show

**Decision:** Use CSS media queries, not JavaScript detection.

**Rationale:**
- Works on tablets with hover (iPad + mouse)
- Responds to browser dev tools mobile emulation
- Simpler implementation

**Query:**
```css
@media (max-width: 768px), (hover: none) {
  #mobileControls { display: block; }
}
```

### 7. Constraint Enforcement at Input Level

**Decision:** Block inputs before they reach movement logic.

**Rationale:**
- Simpler than filtering in movement code
- Works for keyboard + mobile identically
- Console logs show blocked inputs for debugging

**Location:** `isInputAllowed()` checks constraints before setting `game.keys[]`.

---

## Performance Considerations

### Current Performance

**Metrics:**
- 60 FPS on test maps (12 maps tested)
- ~10-100 voxels per test map
- Smooth animations (500ms easing)
- No frame drops on Pixel 9

**Bottlenecks (None Currently):**
- Voxel creation: O(n) where n = voxels
- Terrain lookup: O(1) hash map
- Movement calculation: O(1) per frame

### Future Optimizations

**When Needed:**
1. **Instanced Meshes** - After 500+ voxels in single scene
   - Share geometry across all cubes
   - Use InstancedMesh for position-only variations

2. **Spatial Hash Grid** - After large open-world maps
   - O(1) collision detection in local area
   - Currently uses global terrain map

3. **Occlusion Culling** - After complex indoor levels
   - Don't render voxels behind walls
   - Three.js Frustum culling already active

4. **LOD (Level of Detail)** - After long view distances
   - Simplified geometry for distant voxels
   - Not needed for tactical view distances

**Current Strategy:** Optimize when metrics show need, not preemptively.

---

## Testing Infrastructure

### Test Types

#### 1. Micro-Map Tests (Current)
- Isolated mechanic testing
- 5x5 voxels or less
- Single mechanic per test
- Visual + manual validation

#### 2. Macro-Map Tests (Future)
- Full level scenarios
- Multiple mechanics combined
- Integration testing
- Player experience validation

#### 3. Automated Tests (Future)
- Playwright browser automation
- Position validation (5% tolerance)
- CI/CD integration
- Regression prevention

### Test Workflow

```
1. Define Mechanic → mechanics-graph.json
2. Create Test Map → test-maps/testName.json
3. Manual Testing → Run animation + play manually
4. User Feedback → Structured feedback form
5. Update Status → Mark as tested in graph
6. Reuse Pattern → Copy voxel config to macro maps
```

### Quality Metrics

**Coverage:**
- 7/7 implemented mechanics tested (100%)
- 12 test maps created
- 0 known bugs

**Validation Layers:**
1. **Structural:** TestBuilder validates JSON schema
2. **Mathematical:** Position tolerance checks (5%)
3. **Visual:** Animation playback shows movement
4. **Human:** User confirms behavior is correct

---

## Future Architecture

### Short-Term (Next Session)

1. **Jump Mechanic**
   - Horizontal + vertical movement
   - Gap crossing capability
   - Test: testJumpAcrossGap.json

2. **Macro Map Building**
   - Compose tested micro-patterns
   - Full level: Castle with stairs, towers, moat
   - Use testWalkDownTerrain pattern for stairs

3. **Turn-Based Layer**
   - Unit selection
   - Action points
   - Movement range indicators

### Medium-Term

1. **Multiple Units**
   - Unit types: Ground, Flier, Climber, Grappler
   - Unit-specific mechanics
   - Formation movement

2. **Combat System**
   - Attack ranges
   - Damage calculation
   - Terrain bonuses (height advantage)

3. **AI Opponents**
   - Pathfinding (A*)
   - Tactical decision-making
   - Difficulty levels

### Long-Term

1. **Multiplayer**
   - WebSocket server
   - Turn synchronization
   - Spectator mode

2. **Level Editor**
   - Visual voxel placement
   - Constraint editor
   - Export to JSON

3. **Analytics**
   - Player behavior tracking
   - Heatmaps of movement
   - A/B testing mechanics

---

## Code Organization

### File Structure

```
/
├── index.html                  # Main game + test system (2600+ lines)
├── test-builder.js             # Factory pattern for test generation
├── mechanics-graph.json        # Mechanic definitions + dependencies
├── test-maps/                  # Test configurations (JSON)
│   ├── testBasicMovement.json
│   ├── testDiagonalMovement.json
│   ├── testGravityFall.json
│   └── ... (12 total)
├── concepts/                   # Future feature designs
│   ├── rainbow-unicorn.md
│   ├── odm-gear.md
│   └── llm-visual-testing.md
├── tests/                      # Playwright automation (future)
│   ├── package.json
│   ├── playwright.config.js
│   └── specs/
└── *.md                        # Documentation
    ├── ARCHITECTURE.md         # This file
    ├── DESIGN-DECISIONS.md     # (To be created)
    ├── METHODOLOGY.md
    ├── TEST-PATTERNS.md
    ├── TESTING-GUIDE.md
    ├── PROGRESS-SUMMARY.md
    └── TEST-INDEX.md
```

### index.html Structure

**Lines 1-500:** HTML + CSS
- Main game canvas
- Test menu overlay
- Test preview modal
- Mobile controls UI

**Lines 500-700:** Test Menu System
- loadMechanicsGraph()
- populateTestMenu()
- openTestPreview()
- closeTestPreview()

**Lines 700-1400:** Test Preview System
- Preview rendering (separate scene)
- Animation playback
- Manual play mode
- Feedback collection
- Mobile controls for preview

**Lines 1400-1750:** Test Preview Movement
- processPreviewInput()
- simulateInput()
- hasPreviewVoxel()
- Preview-specific helpers

**Lines 1750-2100:** Main Game Initialization
- init() - Three.js setup
- loadTestMap() - JSON loading
- createPlayer() - Player mesh
- createTerrain() - Default terrain
- createVoxel() - Voxel factory

**Lines 2100-2400:** Main Game Movement
- handleMovement() - Input processing
- getTerrainHeightAt() - Collision
- hasVoxel() - Terrain query
- updatePlayerPosition() - Rendering

**Lines 2400-2600:** Event Handlers
- Mobile controls setup
- Menu controls
- Window events

---

## Critical Paths

### Player Movement Flow

```
User Input (Keyboard/Touch)
  ↓
game.keys[key] = true
  ↓
handleMovement(delta)  [Main Game]
  OR
processPreviewInput(key)  [Preview]
  ↓
Calculate Movement Vector
  ↓
Normalize Vector (diagonal fix)
  ↓
Check Collision (hasVoxel)
  ↓
Apply Auto-Climb/Auto-Descent
  ↓
Update game.playerPos
  ↓
updatePlayerPosition()
  ↓
THREE.Mesh.position.set()
  ↓
Render Frame
```

### Test Loading Flow

```
URL: ?test=testGravityFall
  ↓
game.testMode = true
  ↓
init() async
  ↓
await loadTestMap('testGravityFall')
  ↓
fetch('test-maps/testGravityFall.json')
  ↓
Parse JSON → game.testConfig
  ↓
Set game.playerPos from config.playerStart
  ↓
Create voxels from config.voxels
  ↓
createPlayer()
  ↓
Player respects test map position
  ↓
Gravity applies (falls to ground)
```

---

## Common Pitfalls & Solutions

### Pitfall 1: Player Not Falling
**Symptom:** Player spawns at y=0 instead of falling from y=5.

**Cause:** `createPlayer()` overwrites position before test map loads.

**Solution:** Make `init()` async, await `loadTestMap()`, check `testMode` in `createPlayer()`.

**Status:** Fixed 2026-01-28 (Task #33).

### Pitfall 2: Diagonal Movement Too Fast
**Symptom:** W+D moves √2 faster than W alone.

**Cause:** Vector not normalized before applying.

**Solution:** Normalize: `mag = sqrt(x² + z²); x/=mag; z/=mag`.

**Status:** Fixed 2026-01-28 (Task #29).

### Pitfall 3: Hex Colors in JSON
**Symptom:** `SyntaxError: Unexpected token 0 in JSON`.

**Cause:** JSON doesn't support `0x00FF00` hex literals.

**Solution:** Use decimal (65280) or TestBuilder color names.

**Status:** Fixed 2026-01-28 (Task #19).

### Pitfall 4: Manual Mode Only Works Once
**Symptom:** Second click on "Play Manually" doesn't respond.

**Cause:** Event listeners stacked without cleanup.

**Solution:** Remove old listeners before adding new ones.

**Status:** Fixed 2026-01-28 (Task #22).

### Pitfall 5: Test Preview Menu Open Blocks Movement
**Symptom:** Can't move in main game when menu is open.

**Cause:** `handleMovement()` only runs when `!game.menuOpen`.

**Solution:** This is intentional - close menu to play.

**Status:** Working as designed.

---

## Dependencies

### External Libraries

1. **Three.js** (r152)
   - Source: CDN (unpkg.com)
   - Purpose: 3D rendering, scene graph
   - License: MIT

2. **OrbitControls** (Three.js addon)
   - Source: Three.js examples
   - Purpose: Camera rotation/zoom
   - License: MIT

3. **Playwright** (future)
   - Purpose: Automated browser testing
   - License: Apache 2.0

### Browser APIs

- WebGL (for Three.js)
- RequestAnimationFrame (smooth rendering)
- Fetch API (load JSON files)
- Touch Events (mobile controls)
- CSS Media Queries (responsive design)

### Minimum Browser Requirements

- Chrome 90+ / Firefox 88+ / Safari 14+
- WebGL support
- ES6+ JavaScript (async/await, arrow functions, Map)
- Touch Events API (for mobile)

---

## Deployment

### Current Setup

**Platform:** Termux on Android (Pixel 9)

**Server:** Python HTTP server
```bash
python -m http.server 8080 --bind 100.93.126.24
```

**Access:**
- Local: `http://localhost:8080/`
- Tailscale VPN: `http://100.93.126.24:8080/`
- Test mode: `http://100.93.126.24:8080/?test=testGravityFall`

**No Build Step:** Static files served directly.

### Future Deployment

**Option 1: GitHub Pages**
- Push to gh-pages branch
- Enable Pages in repo settings
- URL: `https://username.github.io/repo/`

**Option 2: Netlify/Vercel**
- Connect GitHub repo
- Auto-deploy on push
- CDN distribution

**Option 3: Self-Hosted**
- Nginx server
- SSL certificate (Let's Encrypt)
- Custom domain

---

## Glossary

**Voxel:** A 3D pixel, a cube in the game world. Stored as (x, y, z) coordinates.

**Mechanic:** A specific movement capability (e.g., auto-climb, gravity).

**Test Map:** A JSON configuration defining a minimal scenario to test one mechanic.

**Micro-Map:** Small test environment (5x5 voxels or less) for isolated testing.

**Macro-Map:** Full game level composed of tested micro-patterns.

**TestBuilder:** Factory class for generating test maps programmatically.

**Constraint:** Declarative rule limiting inputs in a test (e.g., diagonal-only).

**Flyweight:** Design pattern sharing objects to reduce memory (planned for voxels).

**Auto-Climb:** Mechanic where player automatically climbs 1-block obstacles while walking.

**Auto-Descent:** Mechanic where player automatically descends when walking onto lower terrain.

**Preview:** The test visualization modal, separate from main game.

**Animation:** Scripted playback of expected inputs in preview mode.

**Manual Mode:** User-controlled testing in preview with keyboard/touch.

---

## Maintenance Guidelines

### Adding a New Mechanic

1. Define in `mechanics-graph.json`
   - Set dependencies
   - Set status: "not_implemented"

2. Implement in `handleMovement()` and `processPreviewInput()`
   - Share logic between both contexts

3. Create test map in `test-maps/`
   - Use TestBuilder or write JSON manually
   - Follow naming: `test[MechanicName].json`

4. Test manually via preview system
   - Run animation
   - Play manually
   - Submit feedback

5. Update mechanics graph
   - Set status: "implemented"
   - Set tested: true
   - Add test map name to tests array

6. Document in `TEST-INDEX.md`

### Modifying Existing Mechanic

1. Check `mechanics-graph.json` for dependencies
2. Modify both `handleMovement()` AND `processPreviewInput()`
3. Re-run affected tests (check tests array)
4. Update documentation if behavior changed
5. Add notes to mechanic definition

### Refactoring Guidelines

**DO:**
- Keep main game and preview logic unified
- Maintain test coverage after changes
- Document architectural decisions
- Use console.log for debugging, remove after

**DON'T:**
- Break test compatibility (old test maps should still work)
- Add dependencies without updating mechanics graph
- Skip validation in TestBuilder
- Change core mechanics without re-testing

---

## Contact & Support

**Repository:** TBD (not yet pushed to GitHub)

**Issues:** Use GitHub Issues when repo is public

**Documentation Updates:** All *.md files in project root

**Version History:** See `PROGRESS-SUMMARY.md` for session-by-session changes

---

**Next Steps:** Read `DESIGN-DECISIONS.md` (in this folder) for rationale behind specific implementation choices, and `../guides/CODE-STRUCTURE.md` for detailed code organization.

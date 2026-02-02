# Code Structure Guide

**Last Updated:** 2026-01-28
**File:** `index.html` (2600+ lines)
**Purpose:** Line-by-line navigation guide for the codebase

---

## Quick Navigation

| Section | Lines | Purpose |
|---------|-------|---------|
| [HTML Structure](#html-structure) | 1-600 | Page layout, menus, modals |
| [CSS Styling](#css-styling) | 50-500 | Visual design, mobile responsive |
| [Test Menu System](#test-menu-system) | 600-800 | Mechanic browsing, test selection |
| [Test Preview System](#test-preview-system) | 800-1400 | Test visualization, animation |
| [Preview Movement Logic](#preview-movement-logic) | 1400-1750 | Preview input handling |
| [Main Game Init](#main-game-initialization) | 1750-2100 | Scene setup, player creation |
| [Main Game Movement](#main-game-movement) | 2100-2400 | Movement mechanics, gravity |
| [Mobile Controls](#mobile-controls) | 1700-1900, 2400-2600 | Touch input handling |
| [Event Handlers](#event-handlers) | 2400-2650 | UI events, window events |

---

## HTML Structure

### Lines 1-50: Document Head

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Tactical Movement Prototype</title>
```

**Key Elements:**
- UTF-8 encoding
- Viewport meta (mobile responsive)
- Three.js CDN imports (r152)
- OrbitControls addon

### Lines 50-100: Base Styles

```css
body {
    margin: 0;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', ...;
}

#gameCanvas {
    display: block;
    width: 100vw;
    height: 100vh;
}
```

**Design Choices:**
- System font stack (native look)
- Full viewport canvas
- No scrolling (overflow: hidden)

### Lines 100-200: UI Overlay Styles

```css
#ui {
    position: fixed;
    top: 10px;
    left: 10px;
    background: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 10px;
    border-radius: 5px;
}
```

**Components:**
- Position display
- Height indicator
- Mode display (ground/climb)
- Controls help text

### Lines 200-300: Test Menu Styles

```css
#testMenu {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.95);
    display: flex;
    flex-direction: column;
    align-items: center;
    z-index: 1000;
}
```

**Features:**
- Full-screen overlay
- Dark background (95% opacity)
- Flexbox centering
- High z-index (above game)

### Lines 300-400: Test Card Styles

```css
.testCard {
    background: white;
    border-radius: 8px;
    padding: 15px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    border-left: 4px solid #4caf50; /* Green = implemented */
}

.testCard:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
```

**Status Colors:**
- Green (#4caf50): Implemented
- Blue (#2196f3): Tested
- Gray (#9e9e9e): Not implemented
- Red (#f44336): Buggy

### Lines 400-500: Test Preview Modal Styles

```css
#testPreview {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.9);
    display: flex;
    flex-direction: column;
    z-index: 2000;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s;
}

#testPreview.active {
    opacity: 1;
    pointer-events: all;
}
```

**Animation:**
- Fade in/out (0.3s)
- Disable clicks when hidden (pointer-events)
- Higher z-index than menu

### Lines 500-600: Mobile Controls Styles

```css
#mobileControls {
    display: none;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 200px;
    pointer-events: none;
}

@media (max-width: 768px), (hover: none) {
    #mobileControls { display: block; }
}
```

**Joystick:**
- 120px diameter base
- Translucent white (opacity 0.2)
- 40px draggable stick

**Action Buttons:**
- 60px diameter
- ↑ (climb) / ↓ (descend)
- Flexbox column layout

---

## CSS Styling

### Responsive Design

**Breakpoints:**
- Desktop: > 768px
- Mobile: ≤ 768px or `hover: none`

**Mobile Adjustments:**
- Smaller font sizes
- Larger touch targets (60px buttons)
- Joystick appears automatically

### Color Palette

```css
/* Primary Colors */
--primary-green: #4caf50;   /* Implemented */
--primary-blue: #2196f3;    /* Tested */
--gray: #9e9e9e;            /* Not implemented */
--red: #f44336;             /* Buggy */

/* UI Colors */
--dark-bg: rgba(0, 0, 0, 0.9);
--light-bg: rgba(255, 255, 255, 0.95);
--overlay: rgba(0, 0, 0, 0.7);
```

### Animation Timing

```css
/* Hover effects: 0.2s */
transition: transform 0.2s, box-shadow 0.2s;

/* Modals: 0.3s */
transition: opacity 0.3s;

/* Joystick: 0.1s (responsive feel) */
transition: all 0.1s;
```

---

## Test Menu System

### Lines 600-650: Menu Initialization

```javascript
// URL parsing
const urlParams = new URLSearchParams(window.location.search);
const testMap = urlParams.get('test');
const game = {
    testMode: !!testMap,
    mechanicsData: null,
    menuOpen: !testMap,
    // ... (other properties)
};
```

**Logic:**
- If `?test=testName` in URL → test mode, skip menu
- Otherwise → show menu, browse tests

### Lines 650-700: Menu Open/Close

```javascript
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        if (testPreview.classList.contains('active')) {
            closeTestPreview();
        } else {
            toggleTestMenu();
        }
    }
});

function toggleTestMenu() {
    const menu = document.getElementById('testMenu');
    game.menuOpen = !game.menuOpen;

    if (game.menuOpen) {
        menu.classList.remove('hidden');
        loadMechanicsGraph();
    } else {
        menu.classList.add('hidden');
    }
}
```

**Keyboard Shortcut:**
- Escape → Close preview OR toggle menu

### Lines 700-750: Load Mechanics Graph

```javascript
async function loadMechanicsGraph() {
    try {
        const response = await fetch('mechanics-graph.json');
        game.mechanicsData = await response.json();
        populateTestMenu();
    } catch (error) {
        console.error('Failed to load mechanics graph:', error);
    }
}
```

**Error Handling:**
- Catches fetch errors
- Logs to console
- Continues without crashing

### Lines 750-800: Populate Test Menu

```javascript
function populateTestMenu() {
    const testGrid = document.getElementById('testGrid');
    testGrid.innerHTML = '';

    const mechanics = game.mechanicsData.mechanics;
    for (const [id, mechanic] of Object.entries(mechanics)) {
        const card = document.createElement('div');
        card.className = `testCard ${mechanic.status}`;
        if (mechanic.tested) card.classList.add('tested');

        card.innerHTML = `
            <div class="testTitle">${mechanic.name}</div>
            <div class="testDescription">${mechanic.description}</div>
            <span class="testStatus ${mechanic.status}">
                ${mechanic.status.replace('_', ' ')}
            </span>
            ${mechanic.tested ? '<span class="testStatus tested">Tested</span>' : ''}
        `;

        card.addEventListener('click', () => openTestPreview(mechanic));
        testGrid.appendChild(card);
    }
}
```

**Card Generation:**
- Iterates over mechanics object
- Creates DOM elements dynamically
- Attaches click listeners
- Color-codes by status

---

## Test Preview System

### Lines 800-900: Open Test Preview

```javascript
function openTestPreview(mechanic) {
    const preview = document.getElementById('testPreview');
    const title = document.getElementById('previewTitle');
    const description = document.getElementById('previewDescription');

    game.currentMechanic = mechanic;

    title.textContent = mechanic.name;
    description.innerHTML = `
        <strong>Description:</strong> ${mechanic.description}<br>
        <strong>Status:</strong> ${mechanic.status}<br>
        <strong>Dependencies:</strong> ${mechanic.dependencies.join(', ') || 'None'}<br>
        <strong>Tests:</strong> ${mechanic.tests.length > 0 ? mechanic.tests.join(', ') : 'No tests yet'}
    `;

    // Enable/disable buttons based on test availability
    const hasTest = mechanic.tests && mechanic.tests.length > 0;
    document.getElementById('playAnimationBtn').disabled = !hasTest;
    document.getElementById('playManualBtn').disabled = !hasTest;

    preview.classList.add('active');

    // Initialize preview scene if first time
    if (!game.previewRenderer) {
        initPreviewScene();
    }

    // Load first test map
    if (hasTest) {
        loadPreviewTestMap(mechanic.tests[0]);
    }
}
```

**Responsibilities:**
1. Update modal title/description
2. Enable/disable buttons
3. Initialize Three.js scene (lazy)
4. Load test map

### Lines 900-1000: Init Preview Scene

```javascript
function initPreviewScene() {
    const canvas = document.getElementById('previewCanvas');

    // Scene
    game.previewScene = new THREE.Scene();
    game.previewScene.background = new THREE.Color(0x1a1a2e);

    // Camera
    game.previewCamera = new THREE.PerspectiveCamera(
        60,
        canvas.clientWidth / canvas.clientHeight,
        0.1,
        1000
    );
    game.previewCamera.position.set(10, 15, 10);

    // Renderer
    game.previewRenderer = new THREE.WebGLRenderer({
        canvas,
        antialias: true
    });
    game.previewRenderer.setSize(canvas.clientWidth, canvas.clientHeight);
    game.previewRenderer.shadowMap.enabled = true;

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    game.previewScene.add(ambientLight);

    const sunLight = new THREE.DirectionalLight(0xffffff, 0.8);
    sunLight.position.set(10, 20, 10);
    sunLight.castShadow = true;
    game.previewScene.add(sunLight);

    // Controls
    game.previewControls = new OrbitControls(game.previewCamera, canvas);
    game.previewControls.enableDamping = true;
    game.previewControls.dampingFactor = 0.05;

    // Start render loop
    animatePreview();
}
```

**Separate Scene:**
- Different from main game scene
- Dark background (0x1a1a2e)
- Own camera, renderer, controls
- Own animation loop

### Lines 1000-1100: Load Preview Test Map

```javascript
async function loadPreviewTestMap(testName) {
    try {
        const response = await fetch(`test-maps/${testName}.json`);
        const config = await response.json();
        game.testConfig = config;

        console.log('Loading preview test map:', config);

        // Clear previous map
        game.previewTerrain.clear();
        game.previewScene.children = game.previewScene.children.filter(
            child => child.type === 'AmbientLight' || child.type === 'DirectionalLight'
        );

        // Set player start
        if (config.playerStart) {
            game.previewPlayerPos = { ...config.playerStart };
        }

        // Create voxels
        if (config.voxels) {
            config.voxels.forEach(v => {
                createPreviewVoxel(v.x, v.y, v.z, v.color);
            });
        }

        // Create goal marker
        if (config.goal) {
            createPreviewGoalMarker(config.goal.x, config.goal.y, config.goal.z);
        }

        // Create player
        if (!game.previewPlayer) {
            createPreviewPlayer();
        } else {
            updatePreviewPlayerPosition(false);
        }

        console.log('Preview test map loaded');
    } catch (error) {
        console.error('Failed to load preview test map:', error);
    }
}
```

**Cleanup:**
- Clears old voxels
- Removes all meshes except lights
- Resets terrain map

### Lines 1100-1200: Animation Playback

```javascript
async function playAnimation() {
    if (!game.testConfig || !game.testConfig.expectedInputs) {
        alert('No expected inputs defined for this test');
        return;
    }

    // Stop manual mode if running
    if (game.manualPlayMode) {
        stopManualMode();
    }

    game.animationRunning = true;

    // Reset player to start
    if (game.testConfig.playerStart) {
        game.previewPlayerPos = { ...game.testConfig.playerStart };
        updatePreviewPlayerPosition(false);
    }

    // Update UI
    const statusEl = document.getElementById('animationStatus');
    statusEl.classList.add('active');
    statusEl.style.background = '#fff3cd';
    statusEl.style.borderColor = '#ffeaa7';
    statusEl.style.color = '#856404';

    // Disable buttons during animation
    document.getElementById('playAnimationBtn').disabled = true;
    document.getElementById('playManualBtn').disabled = true;

    // Play each input
    const inputs = game.testConfig.expectedInputs;
    for (let i = 0; i < inputs.length && game.animationRunning; i++) {
        statusEl.textContent = `▶ Animation: Step ${i + 1}/${inputs.length} - Input: ${inputs[i]}`;

        await simulateInput(inputs[i]);

        // Wait between inputs
        if (i < inputs.length - 1) {
            await sleep(200);
        }
    }

    // Check if goal reached
    const goalReached = checkPreviewGoalReached();

    statusEl.textContent = goalReached
        ? '✅ Animation Complete: Goal Reached!'
        : '⚠️ Animation Complete: Goal NOT Reached';

    statusEl.style.background = goalReached ? '#d4edda' : '#f8d7da';
    statusEl.style.borderColor = goalReached ? '#c3e6cb' : '#f5c6cb';
    statusEl.style.color = goalReached ? '#155724' : '#721c24';

    // Re-enable buttons
    document.getElementById('playAnimationBtn').disabled = false;
    document.getElementById('playManualBtn').disabled = false;

    game.animationRunning = false;
}
```

**Async Flow:**
1. Reset player to start
2. Loop through expectedInputs
3. Simulate each input (with animation)
4. Wait 200ms between inputs
5. Check if goal reached
6. Update UI with result

### Lines 1200-1300: Simulate Input

```javascript
async function simulateInput(input) {
    // Parse input (e.g., "w+d" → W and D simultaneously)
    const keys = input.includes('+') ? input.split('+') : [input];

    // Set keys as pressed
    keys.forEach(k => game.previewKeys[k] = true);

    // Calculate movement
    let moveX = 0;
    let moveZ = 0;

    if (game.previewKeys['w']) moveX += 1;
    if (game.previewKeys['s']) moveX -= 1;
    if (game.previewKeys['a']) moveZ -= 1;
    if (game.previewKeys['d']) moveZ += 1;

    if (moveX !== 0 || moveZ !== 0) {
        // Normalize to unit vector
        const magnitude = Math.sqrt(moveX * moveX + moveZ * moveZ);
        if (magnitude > 0) {
            moveX /= magnitude;
            moveZ /= magnitude;
        }

        // Calculate new position
        const oldPos = { ...game.previewPlayerPos };
        const newX = oldPos.x + moveX;
        const newZ = oldPos.z + moveZ;
        const newY = calculatePreviewNewY(newX, newZ, oldPos.y);

        // Animate movement
        await animatePreviewMovement(oldPos, { x: newX, y: newY, z: newZ });
    } else if (game.previewKeys[' ']) {
        // Handle Space (climb)
        const newY = game.previewPlayerPos.y + 1;
        if (hasPreviewVoxel(Math.floor(game.previewPlayerPos.x), newY - 1, Math.floor(game.previewPlayerPos.z))) {
            await animatePreviewMovement(game.previewPlayerPos, { ...game.previewPlayerPos, y: newY });
        }
    } else if (game.previewKeys['shift']) {
        // Handle Shift (descend)
        const newY = game.previewPlayerPos.y - 1;
        if (newY >= 1 && hasPreviewVoxel(Math.floor(game.previewPlayerPos.x), newY - 1, Math.floor(game.previewPlayerPos.z))) {
            await animatePreviewMovement(game.previewPlayerPos, { ...game.previewPlayerPos, y: newY });
        }
    }

    // Release keys
    keys.forEach(k => game.previewKeys[k] = false);
}
```

**Key Features:**
- Parses "w+d" notation
- Applies vector normalization
- Calculates auto-climb/auto-descent
- Animates over 500ms
- Releases keys after

### Lines 1300-1400: Animate Movement

```javascript
async function animatePreviewMovement(from, to) {
    const duration = 500; // milliseconds
    const startTime = Date.now();

    return new Promise(resolve => {
        function animate() {
            const elapsed = Date.now() - startTime;
            const progress = Math.min(elapsed / duration, 1.0);

            // Easing function (easeInOutQuad)
            const eased = progress < 0.5
                ? 2 * progress * progress
                : 1 - Math.pow(-2 * progress + 2, 2) / 2;

            // Interpolate position
            game.previewPlayerPos.x = from.x + (to.x - from.x) * eased;
            game.previewPlayerPos.y = from.y + (to.y - from.y) * eased;
            game.previewPlayerPos.z = from.z + (to.z - from.z) * eased;

            updatePreviewPlayerPosition(true);

            if (progress < 1.0) {
                requestAnimationFrame(animate);
            } else {
                // Snap to exact final position
                game.previewPlayerPos = { ...to };
                updatePreviewPlayerPosition(false);
                resolve();
            }
        }

        animate();
    });
}
```

**Easing Curve:**
- Starts slow
- Accelerates in middle
- Decelerates at end
- Smooth, natural-looking

---

## Preview Movement Logic

### Lines 1400-1500: Manual Play Mode

```javascript
function playTestManually() {
    if (!game.currentMechanic || !game.currentMechanic.tests || game.currentMechanic.tests.length === 0) {
        alert('No test available for this mechanic');
        return;
    }

    // If already in manual mode, stop it first
    if (game.manualPlayMode) {
        stopManualMode();
        return;
    }

    // Reset player to start
    if (game.testConfig) {
        game.previewPlayerPos = { ...game.testConfig.playerStart };
        updatePreviewPlayerPosition(false);
    }

    // Enter manual play mode
    game.manualPlayMode = true;
    game.animationRunning = false;
    game.previewKeys = {};

    // Update UI
    const statusEl = document.getElementById('animationStatus');
    statusEl.classList.add('active');
    statusEl.textContent = '🎮 Manual Mode: WASD (move) | Space (climb) | Shift (descend)';
    statusEl.style.background = '#d1ecf1';
    statusEl.style.borderColor = '#bee5eb';
    statusEl.style.color = '#0c5460';

    // Update button states
    const playBtn = document.getElementById('playAnimationBtn');
    const manualBtn = document.getElementById('playManualBtn');

    playBtn.disabled = true;
    manualBtn.textContent = '⏹ Stop Manual Mode';

    // Add keyboard listeners
    document.removeEventListener('keydown', handlePreviewKeyDown);
    document.removeEventListener('keyup', handlePreviewKeyUp);
    document.addEventListener('keydown', handlePreviewKeyDown);
    document.addEventListener('keyup', handlePreviewKeyUp);

    // Setup mobile controls for preview
    setupPreviewMobileControls();

    console.log('Manual play mode enabled');
}
```

**State Management:**
- Toggle mode on/off
- Reset player position
- Update button text
- Attach event listeners

### Lines 1500-1600: Keyboard Input Handlers

```javascript
function handlePreviewKeyDown(e) {
    if (!game.manualPlayMode) return;

    const key = e.key.toLowerCase();

    // Check if input is allowed by constraints
    if (!isInputAllowed(key)) {
        console.log(`Input "${key}" blocked by constraints`);
        return;
    }

    if (!game.previewKeys[key]) {
        game.previewKeys[key] = true;

        // Process input immediately
        processPreviewInput(key);
    }
}

function handlePreviewKeyUp(e) {
    if (!game.manualPlayMode) return;
    game.previewKeys[e.key.toLowerCase()] = false;
}
```

**Constraint Enforcement:**
- Checks `isInputAllowed()` before accepting
- Logs blocked inputs to console

### Lines 1600-1750: Process Preview Input

```javascript
function processPreviewInput(key) {
    const currentY = Math.floor(game.previewPlayerPos.y);
    const x = game.previewPlayerPos.x;
    const z = game.previewPlayerPos.z;

    let moved = false;

    // Handle WASD movement (check for diagonals)
    if (key === 'w' || key === 's' || key === 'a' || key === 'd') {
        // Accumulate movement from all currently pressed WASD keys
        let moveX = 0;
        let moveZ = 0;

        if (game.previewKeys['w']) moveX += 1;
        if (game.previewKeys['s']) moveX -= 1;
        if (game.previewKeys['a']) moveZ -= 1;
        if (game.previewKeys['d']) moveZ += 1;

        if (moveX !== 0 || moveZ !== 0) {
            // Normalize to unit vector FIRST
            const magnitude = Math.sqrt(moveX * moveX + moveZ * moveZ);
            moveX /= magnitude;
            moveZ /= magnitude;

            const newX = x + moveX;
            const newZ = z + moveZ;
            const newXFloor = Math.floor(newX);
            const newZFloor = Math.floor(newZ);

            // Try to move
            if (!hasPreviewVoxel(newXFloor, currentY, newZFloor)) {
                if (hasPreviewVoxel(newXFloor, currentY - 1, newZFloor)) {
                    // Same level
                    game.previewPlayerPos.x = newX;
                    game.previewPlayerPos.z = newZ;
                    moved = true;
                } else {
                    // Auto-descent
                    const lowerY = currentY - 1;
                    if (lowerY >= 1 && hasPreviewVoxel(newXFloor, lowerY - 1, newZFloor)) {
                        game.previewPlayerPos.x = newX;
                        game.previewPlayerPos.z = newZ;
                        game.previewPlayerPos.y = lowerY;
                        moved = true;
                    }
                }
            } else {
                // Auto-climb
                if (!hasPreviewVoxel(newXFloor, currentY + 1, newZFloor)) {
                    game.previewPlayerPos.x = newX;
                    game.previewPlayerPos.z = newZ;
                    game.previewPlayerPos.y = currentY + 1;
                    moved = true;
                }
            }
        }
    } else if (key === ' ') {
        // Manual climb
        const dirX = 0; // Would use facing direction
        const dirZ = 1; // Placeholder
        if (hasPreviewVoxel(x + dirX, currentY, z + dirZ)) {
            if (!hasPreviewVoxel(x + dirX, currentY + 1, z + dirZ)) {
                game.previewPlayerPos.y = currentY + 1;
                moved = true;
            }
        }
    } else if (key === 'shift') {
        // Manual descend
        const nextY = currentY - 1;
        if (nextY >= 1) {
            if (hasPreviewVoxel(Math.floor(x), nextY - 1, Math.floor(z))) {
                game.previewPlayerPos.y = nextY;
                moved = true;
            }
        }
    }

    if (moved) {
        updatePreviewPlayerPosition(true);
    }
}
```

**Movement Logic:**
- Same as main game (unified)
- Checks for auto-climb/auto-descent
- Updates position instantly (no animation in manual mode)

---

## Main Game Initialization

### Lines 1750-1850: Init Function

```javascript
async function init() {
    // Scene
    game.scene = new THREE.Scene();
    game.scene.background = new THREE.Color(0x87ceeb); // Sky blue
    game.scene.fog = new THREE.Fog(0x87ceeb, 50, 200);

    // Camera
    game.camera = new THREE.PerspectiveCamera(
        60,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
    );
    game.camera.position.set(15, 20, 15);

    // Renderer
    const canvas = document.getElementById('gameCanvas');
    game.renderer = new THREE.WebGLRenderer({
        canvas,
        antialias: true
    });
    game.renderer.setSize(window.innerWidth, window.innerHeight);
    game.renderer.shadowMap.enabled = true;
    game.renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    game.scene.add(ambientLight);

    const sunLight = new THREE.DirectionalLight(0xffffff, 0.8);
    sunLight.position.set(50, 100, 50);
    sunLight.castShadow = true;
    sunLight.shadow.mapSize.width = 2048;
    sunLight.shadow.mapSize.height = 2048;
    game.scene.add(sunLight);

    // Orbit controls
    game.controls = new OrbitControls(game.camera, canvas);
    game.controls.enableDamping = true;
    game.controls.dampingFactor = 0.05;

    // Create terrain (test map or default)
    if (game.testMode && testMap) {
        await loadTestMap(testMap); // IMPORTANT: await!
    } else {
        createTerrain();
    }

    // Create player
    createPlayer();

    // Event listeners
    window.addEventListener('resize', onResize);
    window.addEventListener('keydown', (e) => game.keys[e.key.toLowerCase()] = true);
    window.addEventListener('keyup', (e) => game.keys[e.key.toLowerCase()] = false);

    // Mobile touch controls
    setupMobileControls();

    // Start animation loop
    animate();
}
```

**Critical Fix (2026-01-28):**
- Made `init()` async
- Await `loadTestMap()` to ensure terrain loads before player creation

### Lines 1850-1950: Load Test Map (Main Game)

```javascript
async function loadTestMap(mapName) {
    try {
        const response = await fetch(`test-maps/${mapName}.json`);
        const config = await response.json();
        game.testConfig = config;

        console.log('Loading test map:', config);

        // Set player start position
        if (config.playerStart) {
            game.playerPos = { ...config.playerStart };
        }

        // Create voxels from config
        if (config.voxels) {
            config.voxels.forEach(v => {
                createVoxel(v.x, v.y, v.z, v.color);
            });
        }

        // Create goal marker if specified
        if (config.goal) {
            createGoalMarker(config.goal.x, config.goal.y, config.goal.z);
        }

        console.log('Test map loaded successfully');
    } catch (error) {
        console.error('Failed to load test map:', error);
        // Fall back to default terrain
        createTerrain();
    }
}
```

**Error Recovery:**
- Falls back to default terrain on error
- Logs error but doesn't crash

### Lines 1950-2050: Create Player

```javascript
function createPlayer() {
    const geometry = new THREE.ConeGeometry(0.4, 1.2, 4);
    const material = new THREE.MeshLambertMaterial({ color: 0xff4444 });
    game.player = new THREE.Mesh(geometry, material);
    game.player.castShadow = true;

    // Set player position if not already set by test map
    if (!game.playerPos || !game.testMode) {
        // Start on a ground voxel
        const startHeight = getTerrainHeightAt(0, 0);
        game.playerPos = { x: 0, y: startHeight + 1, z: 0 };
    }
    updatePlayerPosition();

    game.scene.add(game.player);
}
```

**Fixed Logic (2026-01-28):**
- Only sets default position if not in test mode
- Respects `game.playerPos` set by `loadTestMap()`

### Lines 2050-2100: Create Voxel

```javascript
function createVoxel(x, y, z, color = 0x00FF00) {
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshLambertMaterial({ color });
    const mesh = new THREE.Mesh(geometry, material);
    mesh.position.set(x + 0.5, y + 0.5, z + 0.5);
    mesh.castShadow = true;
    mesh.receiveShadow = true;
    game.scene.add(mesh);

    // Add to terrain map
    game.terrain.set(`${x},${y},${z}`, true);
}
```

**Coordinate Offset:**
- Voxels positioned at (x+0.5, y+0.5, z+0.5)
- Centers cube on integer coordinates

---

## Main Game Movement

### Lines 2100-2200: Handle Movement

```javascript
function handleMovement(delta) {
    const speed = 5;
    let moveX = 0;
    let moveZ = 0;

    // Get camera forward/right vectors
    const forward = new THREE.Vector3();
    const right = new THREE.Vector3();

    game.camera.getWorldDirection(forward);
    forward.y = 0;
    forward.normalize();

    right.crossVectors(forward, new THREE.Vector3(0, 1, 0));
    right.normalize();

    // WASD input
    if (game.keys['w']) {
        moveX += forward.x * speed * delta;
        moveZ += forward.z * speed * delta;
    }
    if (game.keys['s']) {
        moveX -= forward.x * speed * delta;
        moveZ -= forward.z * speed * delta;
    }
    if (game.keys['a']) {
        moveX += right.x * speed * delta;
        moveZ += right.z * speed * delta;
    }
    if (game.keys['d']) {
        moveX -= right.x * speed * delta;
        moveZ -= right.z * speed * delta;
    }

    // Normalize diagonal movement
    if (moveX !== 0 || moveZ !== 0) {
        const magnitude = Math.sqrt(moveX * moveX + moveZ * moveZ);
        moveX /= magnitude;
        moveZ /= magnitude;
        moveX *= speed * delta;
        moveZ *= speed * delta;

        const newX = game.playerPos.x + moveX;
        const newZ = game.playerPos.z + moveZ;

        // Collision detection + auto-climb/auto-descent
        // (Same logic as preview)
        // ...
    }

    // Manual climb (Space)
    if (game.keys[' ']) {
        // ...
    }

    // Manual descend (Shift)
    if (game.keys['shift']) {
        // ...
    }

    // Gravity simulation
    const groundY = getTerrainHeightAt(
        Math.floor(game.playerPos.x),
        Math.floor(game.playerPos.z)
    );

    if (groundY >= 0) {
        const targetY = groundY + 1;
        if (game.playerPos.y > targetY) {
            const oldY = game.playerPos.y;
            game.playerPos.y = Math.max(targetY, game.playerPos.y - 10 * delta);
            if (Math.abs(oldY - game.playerPos.y) > 0.01) {
                console.log(`Falling: y=${oldY.toFixed(2)} -> ${game.playerPos.y.toFixed(2)}`);
            }
        }
    }

    updatePlayerPosition();
}
```

**Camera-Relative Movement:**
- Forward = camera look direction (ignoring Y)
- Right = perpendicular to forward
- WASD moves relative to camera view

**Gravity:**
- 10 units/second fall speed
- Snaps to ground when close enough
- Console logs falling for debugging

### Lines 2200-2300: Helper Functions

```javascript
function getTerrainHeightAt(x, z) {
    let maxY = -1;
    for (let y = 20; y >= 0; y--) {
        if (game.terrain.has(`${x},${y},${z}`)) {
            maxY = y;
            break;
        }
    }
    return maxY;
}

function hasVoxel(x, y, z) {
    return game.terrain.has(`${Math.floor(x)},${Math.floor(y)},${Math.floor(z)}`);
}

function updatePlayerPosition() {
    game.player.position.set(
        game.playerPos.x,
        game.playerPos.y + 0.6, // Offset for visual height
        game.playerPos.z
    );

    game.controls.target.set(
        game.playerPos.x,
        game.playerPos.y,
        game.playerPos.z
    );
}
```

**Terrain Query:**
- O(1) hash map lookup
- Scans vertically for highest voxel

---

## Mobile Controls

### Lines 2300-2500: Setup Mobile Controls

```javascript
function setupMobileControls() {
    const joystickContainer = document.getElementById('joystickContainer');
    const joystickStick = document.getElementById('joystickStick');
    const climbButton = document.getElementById('climbButton');
    const descendButton = document.getElementById('descendButton');

    let joystickActive = false;
    let joystickStartPos = { x: 0, y: 0 };

    // Joystick touch handling
    joystickContainer.addEventListener('touchstart', (e) => {
        e.preventDefault();
        joystickActive = true;
        const touch = e.touches[0];
        const rect = joystickContainer.getBoundingClientRect();
        joystickStartPos = {
            x: rect.left + rect.width / 2,
            y: rect.top + rect.height / 2
        };
        updateJoystick(touch.clientX, touch.clientY);
    });

    // ... (touchmove, touchend handlers)

    function updateJoystick(touchX, touchY) {
        const deltaX = touchX - joystickStartPos.x;
        const deltaY = touchY - joystickStartPos.y;
        const distance = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
        const maxDistance = 40;

        const clampedDistance = Math.min(distance, maxDistance);
        const angle = Math.atan2(deltaY, deltaX);
        const stickX = Math.cos(angle) * clampedDistance;
        const stickY = Math.sin(angle) * clampedDistance;

        joystickStick.style.transform = `translate(calc(-50% + ${stickX}px), calc(-50% + ${stickY}px))`;

        const normalizedX = stickX / maxDistance;
        const normalizedY = stickY / maxDistance;
        const threshold = 0.3;

        // Update game.keys based on joystick
        game.keys['w'] = false;
        game.keys['s'] = false;
        game.keys['a'] = false;
        game.keys['d'] = false;

        if (Math.abs(normalizedY) > threshold) {
            if (normalizedY < 0) game.keys['w'] = true;
            if (normalizedY > 0) game.keys['s'] = true;
        }
        if (Math.abs(normalizedX) > threshold) {
            if (normalizedX > 0) game.keys['d'] = true;
            if (normalizedX < 0) game.keys['a'] = true;
        }
    }

    // ... (action button handlers)
}
```

**Joystick Math:**
- Touch position → delta from center
- Clamp to max radius (40px)
- Calculate angle → stick visual position
- Normalize → WASD key mapping

---

## Event Handlers

### Lines 2500-2600: Menu Controls & Window Events

```javascript
function initMenuControls() {
    document.getElementById('closeMenu').addEventListener('click', () => {
        document.getElementById('testMenu').classList.add('hidden');
        game.menuOpen = false;
    });

    document.getElementById('closePreview').addEventListener('click', () => {
        closeTestPreview();
    });

    document.getElementById('playAnimationBtn').addEventListener('click', () => {
        playAnimation();
    });

    document.getElementById('playManualBtn').addEventListener('click', () => {
        playTestManually();
    });

    document.getElementById('submitFeedbackBtn').addEventListener('click', () => {
        const selected = document.querySelector('input[name="feedback"]:checked');
        if (selected) {
            console.log('Feedback:', selected.value);
            // Future: send to analytics
        }
        document.getElementById('feedbackBox').classList.remove('active');
    });
}

function onResize() {
    game.camera.aspect = window.innerWidth / window.innerHeight;
    game.camera.updateProjectionMatrix();
    game.renderer.setSize(window.innerWidth, window.innerHeight);

    if (game.previewRenderer) {
        const canvas = document.getElementById('previewCanvas');
        game.previewCamera.aspect = canvas.clientWidth / canvas.clientHeight;
        game.previewCamera.updateProjectionMatrix();
        game.previewRenderer.setSize(canvas.clientWidth, canvas.clientHeight);
    }
}

function animate() {
    requestAnimationFrame(animate);

    const delta = game.clock.getDelta();

    if (game.menuOpen) {
        // Rotate camera when menu open
        const time = Date.now() * 0.0001;
        const radius = 20;
        game.camera.position.x = Math.cos(time) * radius;
        game.camera.position.z = Math.sin(time) * radius;
        game.camera.lookAt(0, 5, 0);
        game.controls.enabled = false;
    } else {
        game.controls.enabled = true;
        handleMovement(delta);
    }

    game.controls.update();
    game.renderer.render(game.scene, game.camera);
}

// Start everything
window.addEventListener('DOMContentLoaded', () => {
    init();
    initMenuControls();
});
```

**Animation Loop:**
- Runs at 60 FPS (requestAnimationFrame)
- Handles movement when menu closed
- Rotates camera when menu open (visual effect)
- Updates controls (damping)

---

## Key Functions Reference

| Function | Line | Purpose |
|----------|------|---------|
| `init()` | 1762 | Initialize Three.js main scene |
| `loadTestMap()` | 1834 | Load test map JSON (main game) |
| `createPlayer()` | 2066 | Create player mesh |
| `createVoxel()` | 2050 | Create voxel mesh |
| `handleMovement()` | 2100 | Process WASD input, gravity |
| `getTerrainHeightAt()` | 2081 | Find highest voxel at X/Z |
| `hasVoxel()` | 2093 | Check if voxel exists |
| `animate()` | 2235 | Main render loop |
| `loadMechanicsGraph()` | 699 | Load mechanics JSON |
| `populateTestMenu()` | 710 | Render test cards |
| `openTestPreview()` | 733 | Show preview modal |
| `initPreviewScene()` | 800 | Initialize preview Three.js |
| `loadPreviewTestMap()` | 1000 | Load test map (preview) |
| `playAnimation()` | 1100 | Run automated test |
| `simulateInput()` | 1200 | Execute single input step |
| `animatePreviewMovement()` | 1300 | Smooth 500ms animation |
| `playTestManually()` | 1400 | Enable manual control |
| `processPreviewInput()` | 1600 | Handle WASD in preview |
| `setupMobileControls()` | 2300 | Initialize touch controls |
| `updateJoystick()` | 2350 | Map touch to WASD |
| `isInputAllowed()` | 1246 | Check constraint rules |

---

## Global Variables

```javascript
// Main game object
const game = {
    // Three.js core
    scene: THREE.Scene,
    camera: THREE.PerspectiveCamera,
    renderer: THREE.WebGLRenderer,
    controls: OrbitControls,
    clock: THREE.Clock,

    // Player state
    player: THREE.Mesh,
    playerPos: { x: 0, y: 1, z: 0 },

    // World state
    terrain: Map<string, boolean>,  // "x,y,z" -> exists
    keys: {},  // { 'w': true/false, ... }

    // Test system
    testMode: boolean,
    testConfig: TestMapConfig | null,
    mechanicsData: MechanicsGraph | null,
    currentMechanic: Mechanic | null,
    menuOpen: boolean,

    // Preview system
    previewScene: THREE.Scene,
    previewCamera: THREE.PerspectiveCamera,
    previewRenderer: THREE.WebGLRenderer,
    previewControls: OrbitControls,
    previewPlayer: THREE.Mesh,
    previewPlayerPos: { x, y, z },
    previewTerrain: Map<string, boolean>,
    previewKeys: {},
    animationRunning: boolean,
    manualPlayMode: boolean
};
```

---

## Next Steps

**For Future Development:**
1. Read `ARCHITECTURE.md` for overall design
2. Read `DESIGN-DECISIONS.md` for rationale
3. Use this document to navigate code
4. Update docs when making changes

**When Adding Features:**
1. Find relevant section in this doc
2. Read existing code
3. Follow established patterns
4. Update documentation

**When Debugging:**
1. Check console logs (extensive logging throughout)
2. Find function in this reference
3. Read surrounding code
4. Add more logging if needed

---

**Related Documents:**
- `ARCHITECTURE.md` - System design
- `DESIGN-DECISIONS.md` - Why we made choices
- `METHODOLOGY.md` - Development workflow
- `TEST-PATTERNS.md` - Test creation patterns

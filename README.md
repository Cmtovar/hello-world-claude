# 3D Tactical Game Prototype

Fire Emblem-inspired tactical game with 3D vertical traversal, built with Three.js.

## Concept

Tactical strategy game with full 3D movement mechanics inspired by:
- **Fire Emblem** - Turn-based tactical combat
- **Attack on Titan** - ODM gear grappling hook mobility
- **Avatar: The Last Airbender** - Vertical environments (tree platforms, sky fortresses)

## Features

### ✅ Implemented & Tested (7/7 Core Mechanics)
- Basic 4-direction movement (WASD, camera-relative)
- Diagonal movement (8 directions with vector normalization)
- Manual climb (Space key)
- Manual descend (Shift key)
- Auto-climb (walk into 1-block obstacles)
- Auto-descent (walk onto lower terrain)
- Gravity/falling (spawn in air, walk off edges)

### 🎮 Test Infrastructure
- **12 micro-map tests** with visual validation
- **Test menu UI** for browsing/selecting mechanics
- **Animation playback** with smooth easing (500ms)
- **Manual play mode** with structured feedback
- **Mobile controls** (virtual joystick + action buttons)
- **Constraint system** for declarative test rules

### 📚 Complete Documentation
- Architecture design (ARCHITECTURE.md)
- Design decisions (DESIGN-DECISIONS.md)
- Code structure guide (CODE-STRUCTURE.md)
- Test patterns (TEST-PATTERNS.md)
- Methodology (METHODOLOGY.md)

### 🔮 Future Unit Types
- **Ground Units** - Standard movement (mechanics complete)
- **Fliers** - Free 3D flight, nosedive mechanics
- **Climbers** - Wall climbing, multi-block ascent
- **Grapplers** - ODM-style grappling hooks

## Running the Game

```bash
# Start web server
python -m http.server 8080

# Access at:
# http://localhost:8080
# or via Tailscale: http://100.93.126.24:8080
```

### Controls

**Desktop:**
- **WASD** - Move (camera-relative)
- **Space** - Climb up
- **Shift** - Descend
- **Mouse Drag** - Rotate camera
- **Scroll** - Zoom
- **Escape** - Toggle test menu

**Mobile:**
- **Virtual Joystick** (bottom-left) - WASD movement
- **↑ Button** (bottom-right) - Climb
- **↓ Button** (bottom-right) - Descend
- Auto-shows on touch devices via CSS media query

## Test-Driven Development

This project uses **mechanic-based testing** with Playwright.

### Test Philosophy
1. Each mechanic gets a dedicated micro test map
2. Tests validate movement with 5% position tolerance
3. Test maps document terrain behaviors for unit types
4. Micro maps become building blocks for macro maps

### Running Tests

```bash
cd tests
npm install
npm test
```

See `tests/README.md` for details.

### Test Maps

Load specific test scenarios via URL:
```
http://localhost:8080/?test=testDescendOneBlock
```

Test maps are defined in `test-maps/*.json` with:
- Player start position
- Goal position (shown as green wireframe sphere)
- Voxel configuration
- Expected inputs

## Mechanics Graph

See `mechanics-graph.json` for:
- All implemented mechanics
- Dependency graph
- Implementation status
- Test coverage
- Unit type requirements

## Architecture

### Files
- `index.html` - Main game (Three.js, standalone)
- `test-maps/` - Micro map configurations (JSON)
- `tests/` - Playwright test suite
- `mechanics-graph.json` - Mechanic dependency graph
- `COORDINATE_SYSTEM.md` - Position/voxel documentation

### Coordinate System
- Voxel at `y=0` is ground level
- Player at `y=1` stands on voxel at `y=0`
- Player at `y=N` stands on voxel at `y=N-1`

## Development Workflow

1. **Plan mechanic** - Update `mechanics-graph.json`
2. **Create test map** - Add JSON to `test-maps/`
3. **Write test** - Add Playwright test to `tests/specs/`
4. **Implement mechanic** - Update `index.html`
5. **Validate** - Run test suite
6. **Document** - Update mechanics graph

## Current Status

**✅ Movement Foundation Complete (2026-01-28)**
- 7/7 core mechanics implemented & tested (100% coverage)
- 12 test maps created (micro-pattern library)
- Mobile touch controls working
- Comprehensive architecture documentation
- Test-driven development workflow established

**✅ Game Systems Designed (2026-01-29)**
- Blueprint Mode (AP regeneration + parallel coordination)
- Template Composition System (functions with control flow)
- Constraint Interface Pattern (affordances & interchangeability)
- Progression Through Units (capability-based gating)
- Techniques & Environmental Interaction (offset system)
- Almanac & Template IDE (learning tools)
- First Map Narrative (complete story framework)

**🚧 Ready to Implement:**
- First complete map: "The Bridge at Old Fort Crossing"
- AP regeneration system
- Blueprint mode UI
- Template system foundation
- Environmental hazards (rain, zombies)

**🔮 Future Features:**
- Advanced unit types (flier, climber, grappler)
- Full template IDE with playback
- Town exploration system
- Alchemist crafting system
- Memory/replay system for past battles

## Next Steps

1. Add mobile touch controls (for phone testing)
2. Test remaining basic mechanics
3. Implement turn-based grid movement
4. Add multiple units
5. Movement range visualization
6. Terrain hazards

## Contributing

When adding new mechanics:
1. Check `mechanics-graph.json` for dependencies
2. Create test FIRST (TDD approach)
3. Implement mechanic
4. Update mechanics graph with test coverage
5. Document in COORDINATE_SYSTEM.md if needed

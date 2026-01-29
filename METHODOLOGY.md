# Development Methodology: Test-Driven Game Mechanics

**Project:** 3D Tactical Game (Fire Emblem + Vertical Traversal)
**Approach:** Mechanic-Based TDD with Micro-Map Testing
**Last Updated:** 2026-01-28

## Philosophy

> "I want there to be testing. And I want the approach to be by mechanism/mechanic. That way you can build confidently knowing that the underlying mechanics work properly."

This methodology prioritizes **confidence through testing**. Every movement mechanic is isolated, tested, and verified before integration into larger systems. The game may look like a debug map in early stages, but the foundation is rock solid.

## Core Principles

### 1. Mechanic-First Development
- Break complex gameplay into atomic mechanics
- Each mechanic gets its own implementation, tests, and validation
- Document dependencies between mechanics
- Build complex behaviors from tested primitives

### 2. Micro-Map Testing
- Create minimal test environments for each mechanic
- One mechanic = one micro test map
- Test maps are building blocks for macro maps
- Version control preserves mechanic behavior guarantees

### 3. Visual Validation
- Use Playwright to simulate user inputs
- Visual playback shows expected vs actual behavior
- Position validation with tolerance (5% distance)
- Test animations provide debugging insights

### 4. Preserve Original Vision
- Archive creative ideas in `concepts/` directory
- Keep original descriptions intact
- Format for clarity but maintain authentic voice
- Reference concepts when ready to implement

## Workflow Steps

### Phase 1: Concepting
When a new idea emerges:

1. **Capture the vision** - Write it down immediately in `concepts/`
2. **Preserve original words** - Don't sanitize creative descriptions
3. **Add structure** - Bullet points, headers, technical considerations
4. **Define theme** - Colors, visuals, feel
5. **Document dependencies** - What mechanics are required?

**Output:** `concepts/{idea-name}.md`

### Phase 2: Mechanic Planning
Before implementing:

1. **Update mechanics graph** - Add to `mechanics-graph.json`
2. **Identify dependencies** - What must exist first?
3. **Define success criteria** - What does "working" look like?
4. **Plan test scenarios** - How will you prove it works?
5. **Prioritize** - Does this unlock other mechanics?

**Output:** Updated `mechanics-graph.json` with new entry

### Phase 3: Test Creation
Create the test BEFORE the feature:

1. **Design micro-map** - Minimal voxel arrangement to test mechanic
2. **Write JSON config** - `test-maps/{testName}.json`
3. **Define inputs** - What keys/actions to test
4. **Set goal position** - Where should player end up?
5. **Calculate tolerance** - What counts as "close enough"?

**Test Map Format:**
```json
{
  "name": "Test Name",
  "description": "What this tests",
  "mechanic": "mechanic_id",
  "playerStart": {"x": 0, "y": 1, "z": 0},
  "goal": {"x": 0, "y": 2, "z": 0},
  "voxels": [...],
  "expectedInputs": ["Space"],
  "notes": "Additional context"
}
```

**Output:** Test map JSON + Playwright test spec

### Phase 4: Implementation
Now write the actual mechanic:

1. **Make the test pass** - Focus on core functionality
2. **Handle edge cases** - What if player is at edge of map?
3. **Add physics** - Gravity, collision, momentum
4. **Polish is optional** - Get it working first
5. **Document coordinate system** - How does positioning work?

**Output:** Updated `index.html` with working mechanic

### Phase 5: Validation
Verify the mechanic works:

1. **Run Playwright tests** - `npm test`
2. **Manual test** - Play the micro-map yourself
3. **Visual inspection** - Does animation look right?
4. **Edge case testing** - Try to break it
5. **Update mechanic status** - Mark as "implemented" and "tested"

**Output:** Passing tests + updated mechanics graph

### Phase 6: Integration
Combine mechanics into larger maps:

1. **Use micro-maps as templates** - Copy voxel patterns
2. **Combine mechanics** - Flier + Climber on same map
3. **Test interactions** - Can flier stand on climber's wall?
4. **Document behaviors** - What terrain blocks which units?
5. **Build macro maps** - Tactical scenarios using proven mechanics

**Output:** Playable levels built from tested components

## Testing Approach

### Position Validation
- **5% total distance tolerance** - Accounts for physics variance
- Global position exposure: `window.game.playerPos`
- Helper function: `window.isPlayerAtGoal()`
- Visual indicators: Goal marker (green wireframe sphere)

### Test Organization
```
tests/
  ├── helpers/
  │   └── test-utils.js      # Position validation, input helpers
  ├── specs/
  │   ├── descend.spec.js    # One mechanic per file
  │   ├── climb.spec.js
  │   └── movement.spec.js
  └── README.md              # Test documentation
```

### Test Types

**Unit Tests** (micro-maps):
- Test single mechanic in isolation
- Example: `testDescendOneBlock`
- Fast, focused, deterministic

**Integration Tests** (interactions):
- Test mechanic combinations
- Example: `testFlierCanClimberCant` - same map, different units
- Proves terrain affects units differently

**Regression Tests** (bug prevention):
- When bug is found, create test that fails
- Fix bug, test now passes
- Bug can never return unnoticed

## Mechanic Dependency Graph

### Structure
```json
{
  "mechanics": {
    "mechanic_id": {
      "name": "Human-readable name",
      "description": "What it does",
      "dependencies": ["other_mechanic_id"],
      "status": "implemented|buggy|not_implemented",
      "tested": true|false,
      "tests": ["testName1", "testName2"],
      "notes": "Implementation details"
    }
  },
  "criticalPath": {
    "description": "Mechanics blocking most features",
    "mechanics": ["basic_movement", "descend_one"]
  },
  "unitTypes": {
    "flier": {
      "requiredMechanics": ["flight_basic", ...]
    }
  }
}
```

### Using the Graph
- **Find what to build next** - Look at critical path
- **Identify blockers** - Check dependencies before implementing
- **Track progress** - Count tested vs implemented
- **Plan sprints** - Group related mechanics
- **Onboard contributors** - Visual map of work

## Player Data Collection (Future)

### Goal
Identify edge cases through actual player behavior in tests.

### Approach
1. **Backend logging** - Send position data to server
2. **Test replay** - Store input sequences that cause bugs
3. **Heatmaps** - Where do players get stuck?
4. **Failure analysis** - What inputs lead to unexpected states?
5. **Crowd-sourced testing** - Let users find edge cases

### Privacy Considerations
- Anonymous data only
- Opt-in system
- Clear data usage explanation
- Local-first (sync optional)

## Visual Test Playback

### Current Implementation
- Preview modal shows test map in 3D
- Rotating camera provides all angles
- Static preview (animation coming)

### Planned Features
- **Animated playback** - Simulate keypresses, watch player move
- **Step-through mode** - Pause at each input
- **Speed control** - Watch at 0.5x, 1x, 2x speed
- **Multiple runs** - Show variance over 10 runs
- **Failure visualization** - Highlight when test fails

### Manual Test Mode
- "Play Test" button loads micro-map in main game
- Full controls enabled
- Position tracker shows distance to goal
- Great for debugging physics edge cases

## Concepts Directory

### Purpose
Archive creative ideas before you're ready to implement them.

### Format
```markdown
# Concept Name

**Status:** Concept
**Priority:** High/Medium/Low/Future

## Original Vision
> Exact quotes from brainstorming

## Core Mechanic
What makes this special?

## Implementation Considerations
Technical thoughts, dependencies

## Test Maps Needed
How would you test this?

## Related Concepts
Links to other ideas
```

### Benefits
- **Preserve inspiration** - Capture the feeling when it's fresh
- **Future reference** - Return when ready
- **Team communication** - Share vision with collaborators
- **Scope management** - Know what's planned vs in-progress

## Code Organization

### File Structure
```
/
├── index.html              # Main game (monolithic for now)
├── mechanics-graph.json    # Dependency tracker
├── COORDINATE_SYSTEM.md    # Position/voxel documentation
├── METHODOLOGY.md          # This file
├── concepts/               # Future ideas
│   ├── rainbow-unicorn.md
│   └── odm-gear.md
├── test-maps/              # Micro-map configs
│   ├── testDescendOneBlock.json
│   └── testClimbOneBlock.json
└── tests/                  # Playwright tests
    ├── helpers/
    ├── specs/
    └── README.md
```

### Why Monolithic?
Early stages prioritize **rapid iteration** over architecture. Single HTML file means:
- Fast prototyping
- Easy hosting (no build step)
- Mobile-friendly (one file to load)
- Can refactor to modules later when stable

## Common Patterns

### Adding a New Mechanic

1. **Is it in concepts?** - Check if already documented
2. **Update graph** - Add to `mechanics-graph.json`
3. **Create test map** - `test-maps/test{MechanicName}.json`
4. **Write test** - `tests/specs/{mechanic}.spec.js`
5. **Implement** - Edit `index.html`
6. **Validate** - Run tests, play manually
7. **Mark complete** - Update graph status

### Fixing a Bug

1. **Reproduce** - Can you trigger it consistently?
2. **Create test** - Make a test that fails with the bug
3. **Debug** - Use test to isolate issue
4. **Fix** - Update implementation
5. **Verify** - Test now passes
6. **Commit** - Bug won't return

### Refactoring

1. **Tests protect you** - They prove refactor didn't break anything
2. **One mechanic at a time** - Don't refactor everything
3. **Keep tests passing** - Green throughout refactor
4. **Update docs** - COORDINATE_SYSTEM.md etc.

## Anti-Patterns to Avoid

### ❌ Implementing without tests
**Problem:** No confidence, regression likely
**Solution:** Test first, always

### ❌ Testing too much at once
**Problem:** Failure doesn't pinpoint issue
**Solution:** One mechanic per test

### ❌ Losing original vision
**Problem:** Sanitized descriptions lose magic
**Solution:** Preserve exact words in concepts/

### ❌ Building macro before micro
**Problem:** Debug hell when something breaks
**Solution:** Validate micro-maps first

### ❌ Skipping manual testing
**Problem:** Automation misses "feel"
**Solution:** Play every test yourself

## Success Metrics

### Mechanic Maturity
- ✅ Documented in graph
- ✅ Test map created
- ✅ Playwright test written
- ✅ Implementation complete
- ✅ Tests passing
- ✅ Manually validated
- ✅ Used in macro-map

### Project Health
- Test coverage % (mechanics with tests)
- Critical path completion
- Bug fix rate
- Concept backlog size

## Future Enhancements

### Tooling
- Visual graph editor for mechanics dependencies
- Automated micro-map generator
- Test result dashboard
- Performance benchmarking

### Workflow
- CI/CD for test runs
- Video recording of test runs
- Community test contributions
- Cross-platform validation

### Learning
- Tutorial system using test maps
- Progressive mechanic unlock
- Mastery challenges (speedrun tests)

## Conclusion

This methodology **prioritizes confidence over speed**. Every mechanic is a proven building block. Tests are documentation. Micro-maps are the atomic units of level design.

When you have 50 tested mechanics, you can combine them into infinite tactical scenarios. That's when the game truly comes alive.

**Build slow, build solid, build spectacular.**

---

## Related Documents
- `README.md` - Project overview
- `mechanics-graph.json` - Current mechanic status
- `COORDINATE_SYSTEM.md` - Technical reference
- `tests/README.md` - Test framework guide
- `concepts/` - Future vision archive

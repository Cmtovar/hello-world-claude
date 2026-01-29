# Rolling TODO List

**Last Updated:** 2026-01-28

## Bugs to Fix

### High Priority

- [ ] **Gravity not working in test maps**
  - Symptom: Player spawns at y=5 but doesn't fall in testGravityFall
  - Attempted fix: Made init() async, await loadTestMap() - didn't work
  - May need to investigate: gravity logic in handleMovement(), terrain initialization timing
  - Workaround: Test gravity in main game (works there)

### Medium Priority

- [ ] Movement modifier decorator pattern (Task #30)
  - Document sprint, slow, knockback modifiers
  - Implement decorator chain

### Low Priority

None currently

---

## Features to Implement

### Short Term (Next Session)

- [ ] Jump mechanic
  - Horizontal + vertical movement
  - Gap crossing capability
  - Test: testJumpAcrossGap.json
  - Dependencies: basic_movement, climb_up_one

- [ ] Verify all 12 tests work on mobile
  - Run through each test manually with touch controls
  - Collect feedback

- [ ] Build first macro map
  - Use tested micro-patterns
  - Example: Castle with stairs (testWalkDownTerrain pattern)
  - Include multiple elevation changes

### Medium Term

- [ ] Turn-based tactical layer
  - Unit selection
  - Action points system
  - Movement range indicators
  - End turn button

- [ ] Multiple units on same map
  - Unit switching
  - Formation movement
  - Unit-specific mechanics (flier, climber, grappler)

- [ ] Wall climbing mechanic
  - Multi-block vertical ascent
  - For climber unit type
  - Test: testWallClimb.json

### Long Term

- [ ] Multiplayer support
  - WebSocket server
  - Turn synchronization
  - Spectator mode

- [ ] Level editor
  - Visual voxel placement
  - Constraint editor
  - Export to JSON

- [ ] AI opponents
  - Pathfinding (A*)
  - Tactical decision-making
  - Difficulty levels

- [ ] Player behavior analytics
  - Track movement patterns
  - Heatmaps
  - A/B testing mechanics

---

## Documentation

- [ ] Add code comments for complex functions
  - Especially movement logic
  - Animation easing math

- [ ] Create CONTRIBUTING.md
  - Code style guide
  - Git workflow
  - PR template

- [ ] Visual architecture diagram
  - Component relationships
  - Data flow

---

## Refactoring / Technical Debt

### Consider When File Gets Large (>5000 lines)

- [ ] Split index.html into modules
  - main-game.js
  - test-preview.js
  - movement-engine.js
  - mobile-controls.js

- [ ] Implement flyweight pattern for voxels
  - Share geometry/materials
  - After 500+ voxels in scene
  - Or if FPS drops below 30

### Consider for Type Safety

- [ ] Add TypeScript
  - When multiple developers
  - When codebase >10k lines
  - Helps prevent bugs during refactoring

### Performance Optimizations (Only If Needed)

- [ ] Instanced meshes for voxels
  - If FPS < 30 with current voxel count
  - Profile first to confirm bottleneck

- [ ] Spatial hash grid
  - For large open-world maps
  - Current Map<"x,y,z"> works fine for small maps

- [ ] Occlusion culling
  - For complex indoor levels
  - Three.js frustum culling already works

---

## Testing Infrastructure

### Automated Testing

- [ ] Actually use Playwright (tests/ directory exists but unused)
  - Write specs for each mechanic
  - CI/CD integration
  - Regression prevention

- [ ] Visual regression testing
  - Screenshot comparison
  - Detect unintended visual changes
  - Matches llm-visual-testing.md concept

- [ ] Fuzzing / generative testing
  - Random test map generation
  - Find edge cases automatically
  - Stress test mechanics

### Test Coverage

- [ ] Constraint validation tests
  - Tests that test the tests
  - Verify allowedInputs actually blocks inputs
  - Lower priority (mentioned in PROGRESS-SUMMARY)

---

## Known Issues / Quirks

### Not Bugs, But Worth Noting

- Manual climb (Space) uses placeholder direction (z=1)
  - Should use player facing direction
  - Works for tests but not intuitive in free play
  - Fix when adding facing/rotation

- Camera-relative movement in main game, but not in preview
  - Preview uses world-space WASD (simpler for testing)
  - Consider unifying for consistency

- Console.log statements everywhere
  - Good for debugging
  - Should add build step to strip in production

---

## Ideas / Future Concepts

See `concepts/` directory for detailed designs:

- [ ] Rainbow unicorn unit (temporary platforms)
- [ ] ODM gear (grappling hook mechanics)
- [ ] LLM visual testing (AI-powered QA)
- [ ] Tornado dynamic terrain
- [ ] Character-specific special moves

---

## Completed

### 2026-01-28 Session

- ✅ Fix descent mechanic bug
- ✅ Create test selection menu overlay
- ✅ Implement test animation playback
- ✅ Add manual test play mode
- ✅ Create 6 fundamental movement tests
- ✅ Unify main game and test movement code
- ✅ Fix diagonal movement vector normalization
- ✅ Implement mobile virtual joystick
- ✅ Add constraint enforcement system
- ✅ Create comprehensive architecture documentation
- ✅ Create 6 additional tests (gravity, complex terrain, edge cases)
- ✅ Update mechanics graph (7/7 implemented mechanics tested)

---

## Notes

**When Adding to TODO:**
- Use `[ ]` for pending
- Use `[x]` for completed
- Include context (why it's needed, what it depends on)
- Link to related docs/code when helpful

**When Completing Items:**
- Move to "Completed" section with date
- Update related documentation
- Close related GitHub issues (when repo exists)

**Priority Levels:**
- High: Blocks other work or significantly impacts UX
- Medium: Important but not blocking
- Low: Nice to have, can wait

---

**Related Documents:**
- `ARCHITECTURE.md` - System design
- `DESIGN-DECISIONS.md` - Why we made choices
- `PROGRESS-SUMMARY.md` - What's been done
- `TEST-INDEX.md` - All test maps

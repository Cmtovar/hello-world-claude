# LLM Visual Testing Concept

**Status:** Future Enhancement
**Priority:** Medium (Quality assurance innovation)

## Original Vision

> "it might be good eventually to write an mcp server or (equivalent) ask an AI to either through tools or managing playwright on its own, navigate the website, look at a test, then automatically play the test and then confirm their API response to your expected outcome. it's like. a basic unit test is that the calculations match up, but this is like a mocked human UI test, where an LLM interprets the UI and assesses if it met expectations."

## Core Concept

An MCP server or automated system where an LLM acts as a **visual test validator**:

1. **Navigate** to the test page
2. **Observe** the UI visually (screenshots/DOM)
3. **Execute** the test (click buttons, enter inputs)
4. **Interpret** what happened visually
5. **Validate** if expectations were met (human-like assessment)

This goes beyond traditional testing:
- **Traditional Unit Test**: "Did player.y === 1?"
- **LLM Visual Test**: "Did the red triangle appear to move downward smoothly?"

## Why This Matters

### Current Testing Limitations

**Math Tests (Current):**
- Position validation: `distance < tolerance`
- Collision detection: `hasVoxel(x, y, z)`
- State checking: `goal reached === true`

**What Math Tests Miss:**
- Visual glitches (player teleports instead of moving)
- UI responsiveness (buttons don't respond)
- Animation quality (jerky movement)
- Color/contrast issues (can't see the voxels)
- User experience problems (confusing feedback)

**LLM Tests Would Catch:**
- "The player appeared to teleport rather than descend smoothly"
- "The voxels are too dark to distinguish from background"
- "The goal marker is not visible enough"
- "The status message is unclear about what happened"

## Implementation Approaches

### Approach 1: MCP Server with Vision

**Architecture:**
```
MCP Server
  ├─ Playwright (navigate, interact)
  ├─ Screenshot capture
  ├─ Vision-capable LLM (Claude with vision)
  └─ Test result interpreter
```

**Workflow:**
1. MCP server launches Playwright
2. Navigates to test URL
3. Takes screenshot of initial state
4. Clicks "Run Animation" button
5. Takes screenshot after animation
6. Sends both images to vision-capable LLM
7. Asks: "Did the red triangle descend from the orange platform to the green base?"
8. LLM responds with observation
9. Server validates against expected outcome

**Advantages:**
- Catches visual regressions
- Human-like assessment
- Can describe unexpected behaviors
- Works across any UI changes

**Challenges:**
- Requires vision-capable LLM
- Screenshot timing is tricky
- May be slower than math tests
- Cost per test (LLM API calls)

### Approach 2: Playwright + LLM Without Vision

**Use DOM inspection instead of screenshots:**

```javascript
// LLM reads DOM state
const playerPosition = await page.evaluate(() => window.game.previewPlayerPos);
const sceneObjects = await page.evaluate(() => game.previewScene.children.length);

// LLM interprets
const prompt = `
Given:
- Player started at y=2
- Player now at y=${playerPosition.y}
- Expected goal: y=1
- Scene has ${sceneObjects} objects

Did the descent mechanic work as expected?
`;
```

**Advantages:**
- No vision API needed
- Faster than screenshots
- Precise state data

**Disadvantages:**
- Still misses visual issues
- Only validates logical state

### Approach 3: Hybrid (Recommended)

Combine both:
1. **Math validation** (fast, precise) - unit test level
2. **DOM inspection** (medium speed) - integration test level
3. **Visual LLM validation** (slow, comprehensive) - E2E test level

Run them in layers:
- Every commit: Math tests
- Every PR: DOM inspection tests
- Release candidates: Full LLM visual tests

## User Feedback Integration

### Current Manual Testing

When user plays test manually, we now ask:
- "Did you successfully descend?"
- Options: Yes / No / Something went wrong
- Free-form feedback: "What happened?"

This creates a **human validation dataset**.

### Future: Train on Human Feedback

1. **Collect feedback**: Users describe what they saw
2. **Store results**: Link feedback to test scenarios
3. **Build corpus**: "When descent works, users say..."
4. **Train LLM**: Use corpus to calibrate LLM validator

Example training data:
```json
{
  "test": "testDescendOneBlock",
  "screenshot_before": "base64...",
  "screenshot_after": "base64...",
  "user_feedback": "Yes, the red triangle smoothly moved down",
  "expected_outcome": "descent_successful",
  "test_passed": true
}
```

LLM learns: "When users see smooth downward movement, the test passes"

## Technical Implementation

### MCP Server Structure

```
mcp-visual-tester/
├── server.py
│   ├── navigate_to_test()
│   ├── capture_screenshots()
│   ├── execute_test_sequence()
│   ├── send_to_llm()
│   └── validate_response()
├── config/
│   └── test_expectations.json
└── prompts/
    └── visual_validation_prompt.txt
```

### Test Expectations Format

```json
{
  "testDescendOneBlock": {
    "description": "Player descends from orange platform to green base",
    "visual_cues": [
      "Red triangle (player) starts on orange voxel",
      "After pressing Shift, player moves downward",
      "Player ends on green voxel at bottom",
      "Movement should be smooth, not instant"
    ],
    "failure_indicators": [
      "Player doesn't move",
      "Player teleports instead of animating",
      "Voxels are not visible or too dark",
      "No visual feedback of button press"
    ]
  }
}
```

### Sample LLM Prompt

```
You are a QA tester validating a 3D game mechanic test.

Test: Descend One Block
Expected: Player descends from orange platform (y=2) to green base (y=1)

Visual Evidence:
[Screenshot before - shows scene with player on orange platform]
[Screenshot after - shows scene with player on green platform]

DOM State:
- Player position before: {x: 0, y: 2, z: 0}
- Player position after: {x: 0, y: 1, z: 0}
- Terrain voxels present: 6

Questions:
1. Is the player (red triangle) visible in both screenshots?
2. Did the player position change from higher to lower?
3. Is the movement visually clear and understandable?
4. Are the voxels (platforms) clearly distinguishable?
5. Overall, did this test appear to pass successfully?

Respond in JSON:
{
  "test_passed": true/false,
  "confidence": 0-100,
  "observations": ["list", "of", "what", "you", "saw"],
  "issues": ["any", "problems", "noticed"],
  "recommendation": "pass/fail/needs_review"
}
```

## Integration with Existing Infrastructure

### Where It Fits

```
mechanics-graph.json
  └─ mechanic: "descend_one"
      ├─ status: "implemented"
      ├─ tested: true
      ├─ tests: ["testDescendOneBlock"]
      └─ visual_validation: {
          "last_run": "2026-01-28",
          "llm_result": "pass",
          "confidence": 95,
          "issues": []
        }
```

### Test Pipeline

```
1. Developer implements mechanic
2. Write Playwright unit test (math validation)
3. Create test map JSON
4. Run math tests → Pass
5. Trigger visual LLM test → Pass
6. Manual user testing → Collect feedback
7. Update mechanics graph with all results
8. Mechanic marked "validated" (math + visual + human)
```

## Cost-Benefit Analysis

### Benefits
- Catches visual regressions
- Validates UX, not just logic
- Can describe problems in human terms
- Reduces manual QA time
- Documents test quality over time

### Costs
- LLM API calls ($)
- Screenshot storage
- Slower than math tests
- Requires setup/maintenance
- May have false positives

### When to Use
- ✅ Critical mechanics (movement, combat)
- ✅ Complex animations
- ✅ User-facing features
- ✅ Before major releases
- ❌ Internal helper functions
- ❌ Simple calculations
- ❌ Every commit (too expensive)

## Roadmap

### Phase 1: Proof of Concept
- Single test with manual screenshots
- Send to Claude API with vision
- Validate response format
- Document accuracy

### Phase 2: Automated Pipeline
- Build MCP server
- Integrate Playwright
- Auto-capture screenshots
- Parse LLM responses

### Phase 3: User Feedback Loop
- Collect manual test feedback
- Build training corpus
- Calibrate LLM expectations
- A/B test vs human validation

### Phase 4: Production Integration
- CI/CD integration
- Cost optimization (batch tests)
- Dashboard for results
- Alert on visual regressions

## Related Concepts

See also:
- `METHODOLOGY.md` - Overall testing approach
- `TESTING-GUIDE.md` - Manual validation checklist
- `tests/README.md` - Playwright test structure

## Research Questions

1. **Accuracy**: How often does LLM visual validation match human assessment?
2. **Timing**: When should screenshots be captured for best results?
3. **Cost**: What's the $/test for LLM visual validation?
4. **Prompting**: What prompt structure gives most reliable results?
5. **Failure modes**: When does LLM validation fail or hallucinate?

## Example Use Cases

### Use Case 1: Animation Quality
**Scenario**: Math test says "y went from 2 to 1" ✓
**Visual LLM says**: "Player teleported instantly, no smooth animation" ✗
**Action**: Fix animation interpolation

### Use Case 2: Color Contrast
**Scenario**: Math test says "voxels rendered" ✓
**Visual LLM says**: "Voxels are barely visible, too dark" ✗
**Action**: Adjust colors/lighting

### Use Case 3: UI Responsiveness
**Scenario**: Math test says "button clicked" ✓
**Visual LLM says**: "No visual feedback that button was pressed" ✗
**Action**: Add button hover/active states

### Use Case 4: Edge Case Discovery
**Scenario**: Math test passes in 90% of runs
**Visual LLM on failed run**: "Player clipped through wall" ✗
**Action**: Fix collision detection bug

## Conclusion

LLM visual testing bridges the gap between **mathematical correctness** and **perceptual quality**. It automates the human QA perspective while maintaining the precision of unit tests.

This is the next evolution of test-driven development: **TDD + VDD (Visual-Driven Development)**.

**Build mechanics that not only work mathematically, but feel right visually.**

---

*Status: Concept phase. Implementation pending after core mechanics are validated with traditional testing.*

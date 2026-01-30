# Suggestions for Improving Claude Collaboration

**Purpose:** Ideas to make working with Claude Code more effective
**Based on:** Observations from Session 2026-01-30
**Status:** Living document - add ideas as they emerge

---

## Quick Wins (Easy to Implement)

### 1. Commit More Frequently
**Current:** Large batch of uncommitted files at session end
**Suggestion:** Commit after each milestone
- After river finalized: commit
- After ruins complete: commit
- After character models: commit

**Benefits:**
- Better git history for recovery
- Clearer progression
- Easier to revert specific changes
- Claude can reference commit hashes

**How:**
```bash
# After each significant piece
git add [files]
git commit -m "Clear description"
```

### 2. Session Start/End Ritual
**Suggestion:** Explicit session boundaries

**Session Start:**
```
1. Say "Starting session - <brief goal>"
2. I read START-HERE.md + recent SESSION notes
3. Confirm understanding: "I see we're working on X, ready?"
```

**Session End:**
```
1. You say "Session ending - wrap up"
2. I create/update SESSION note
3. We commit everything
4. Clear handoff to next session
```

**Benefits:**
- Clear context switches
- Better documentation
- Cleaner git history

### 3. Visual Diff Checklist
**Current:** Hard to see what changed between iterations
**Suggestion:** Before/after comparison checklist

When showing changes:
```
- What changed: [brief description]
- Voxel count: [old] → [new]
- Test URL: http://100.93.126.24:8080/?test=X
- Compare with: [previous version URL if saved]
```

**Benefits:**
- Easier to evaluate changes
- Clearer communication
- Better decision-making

---

## Medium Effort (Worth Considering)

### 4. Experiment Tracking
**Observed:** Bridge went through many iterations, hard to track
**Suggestion:** Document experiments as they happen

Create: `EXPERIMENTS.md`
```markdown
## Bridge Design (2026-01-30)

### Attempt 1: Floating ship look
- Result: Too disconnected, but saved for future
- File: floating-ship.json
- Decision: Revert

### Attempt 2: Diagonal crossing
- Result: Wrong direction
- Decision: Revert

### Attempt 3: Simple M-shape
- Result: Success ✓
- Decision: Keep
```

**Benefits:**
- Learn from failed attempts
- Don't repeat mistakes
- Show design evolution

### 5. Quick Iteration Commands
**Current:** Many steps to see small changes
**Suggestion:** Bash aliases or scripts

```bash
# In ~/.bashrc or project script
alias rebuild='python ~/combine_all.py && pkill -9 python && python -m http.server -b 100.93.126.24 8080 &'
alias show='echo "http://100.93.126.24:8080/?test=complete-scene"'
```

**Benefits:**
- Faster iteration
- Less typing
- Fewer errors

### 6. Snapshot Before Major Changes
**Suggestion:** Save state before risky changes

```bash
# Before major refactor
git tag snapshot-before-bridge-redesign
# or
cp -r story-geometry story-geometry.backup
```

**Benefits:**
- Easy rollback
- Experiment freely
- Less fear of breaking things

### 7. Document Index/Map
**Current:** Many docs, hard to navigate
**Suggestion:** Create visual map

`DOCUMENT-MAP.md`:
```
START-HERE.md (Entry point)
├── .claude/
│   ├── README.md (Meta-infrastructure overview)
│   ├── SESSION-*.md (Session notes)
│   └── USER-WORKING-STYLE.md (How you work)
├── IMPLEMENTATION-STATUS.md (What's done)
├── RIVER-DESIGN-PATTERN.md (Locked baseline)
└── [etc...]
```

**Benefits:**
- Easier navigation
- See relationships
- Find docs faster

---

## Bigger Ideas (Future Exploration)

### 8. Visual Voxel Editor
**Current:** Hand-editing JSON for voxels
**Challenge:** Tedious, error-prone

**Possibilities:**
- Simple web-based voxel editor
- Import/export JSON
- Visual placement vs coordinate typing
- Preview in real-time

**Would help:**
- Faster geometry creation
- More intuitive positioning
- Less coordinate math

### 9. Git Hooks for Quality
**Suggestion:** Automated validation

```bash
# .git/hooks/pre-commit
# Validate all JSON files
for file in $(git diff --cached --name-only | grep '\.json$'); do
    python -m json.tool "$file" > /dev/null || exit 1
done
```

**Benefits:**
- Catch JSON errors before commit
- Maintain quality standards
- Prevent broken files

### 10. Custom MCP Server for Project
**Idea:** Project-specific tools as MCP server

**Could provide:**
- Voxel manipulation tools
- Geometry validation
- Character positioning helpers
- Cutscene sequencing tools
- Test environment management

**Benefits:**
- Specialized tools for this project
- Faster common operations
- Better abstraction

### 11. Visual Feedback Channel
**Current:** Text-based iteration cycle
**Idea:** If voice/video available

**Could enable:**
- "Look at the screen, see how the bridge..."
- Faster visual feedback
- Point at things vs describe
- Reduced text back-and-forth

**Note:** Depends on available modalities

### 12. Automated Screenshot Comparison
**Idea:** Capture screenshots automatically

```bash
# After each rebuild
screenshot-tool --url http://100.93.126.24:8080/?test=complete-scene \
  --output snapshots/$(date +%Y%m%d-%H%M%S).png
```

**Benefits:**
- Visual history
- Easy comparison
- See progression

---

## Learning & Exploration

### 13. Claude Code Deep Dive
**Things to explore:**

**Skills/Plugins:**
- What skills are available?
- Can we create custom skills?
- How do skills work with this repo?

**MCP Integration:**
- What MCP servers exist?
- Could we build project-specific MCP?
- How to integrate with Claude Code?

**Advanced Features:**
- Prompt caching for large docs?
- Background tasks for long operations?
- Multi-agent collaboration?

**Documentation:**
- Claude Code official docs
- Community best practices
- Example workflows

### 14. Voxel Game Development Resources
**Things to learn:**

- Voxel rendering techniques
- Animation systems for voxel characters
- Cutscene systems in voxel games
- Water/particle effects
- Camera systems

**Could inform:**
- Better geometry design
- More efficient data structures
- Industry best practices

### 15. Git Workflow Optimization
**Things to try:**

- Branch per feature?
- Git worktrees for experiments?
- Better commit message templates?
- Automated changelog generation?

**Resources:**
- Git best practices for game dev
- Asset management in git
- Large file handling (if needed)

---

## Communication Patterns

### 16. "Show Me" vs "Tell Me"
**Observation:** You're very visual

**Suggestion:** Explicit communication modes

```
"Show me first" - Build it, I'll evaluate visually
"Tell me about" - Explain without implementing
"Try this" - Specific direction, execute
"Explore" - Research and present options
```

**Benefits:**
- Clearer intent
- Less back-and-forth
- More efficient

### 17. Iteration Budget
**Idea:** Set iteration limits upfront

```
"Let's try 3 iterations on the bridge, then move on"
"Quick experiment - one attempt, then decide"
"This is critical - iterate until right"
```

**Benefits:**
- Manage diminishing returns
- Clear expectations
- Better time management

### 18. Checkpoint Confirmations
**Suggestion:** Periodic "are we aligned?" checks

```
After design phase: "This matches your vision?"
Before major work: "Confirm this approach?"
Mid-iteration: "Still on track?"
```

**Benefits:**
- Catch misunderstandings early
- Course-correct quickly
- Build confidence

---

## Infrastructure Ideas

### 19. Session Templates
**Idea:** Pre-formatted session note templates

`.claude/templates/SESSION-TEMPLATE.md`:
```markdown
# Session: YYYY-MM-DD

## Goals
-

## Accomplished
-

## Decisions
-

## Learnings
-

## Next Steps
-
```

**Benefits:**
- Consistent documentation
- Don't forget sections
- Faster note-taking

### 20. Decision Log
**Idea:** Separate doc for key decisions

`DECISIONS.md`:
```markdown
## 2026-01-30: River Baseline Locked
- What: Ancient meandering river design
- Why: Matches narrative, looks natural
- Impact: Can't regress to simpler patterns
- Reference: RIVER-DESIGN-PATTERN.md

## 2026-01-30: Characters 2 voxels tall
- What: Standard character height
- Why: Simple, distinguishable, baby is 1 voxel
- Impact: All future characters follow this
```

**Benefits:**
- Quick reference for decisions
- Understand constraints
- See evolution of thinking

---

## Things to Try

### Experimentation List
- [ ] Commit after each milestone (try next session)
- [ ] Session start/end ritual (define format)
- [ ] Create EXPERIMENTS.md (track attempts)
- [ ] Build document map (visual navigation)
- [ ] Set up git commit template
- [ ] Try "show me" vs "tell me" explicit modes
- [ ] Explore Claude Code advanced features
- [ ] Research voxel game cutscene systems

### Quick Tests
- [ ] How fast is rebuild cycle? Can we optimize?
- [ ] Does git work well with many JSON files?
- [ ] Would branches help for experiments?
- [ ] Can we automate screenshot capture?

---

## Questions to Explore

### About This Project
- What's the end goal? Playable game? Proof of concept?
- How important is performance vs features?
- Will this stay voxel-based or evolve?
- What's the priority: story vs mechanics vs systems?

### About Workflow
- What parts of working with Claude are frustrating?
- What parts work really well?
- Where do we lose time?
- What would make iterations faster?

### About Tools
- What tools do you wish existed?
- What repetitive tasks could be automated?
- What's the ideal development environment?
- How can Claude be more helpful?

---

## Meta-Suggestions

### This Document Itself
- Add to this as ideas emerge
- Mark tried items with date + result
- Archive deprecated suggestions
- Share successful patterns

### Feedback Loop
- After each session, reflect on what worked
- Note frustrations or friction points
- Celebrate successes
- Iterate on process itself

---

## How to Use This Document

### When Starting
- Review "Quick Wins" - pick one to try
- Check "Things to Try" list
- Note any new ideas

### During Session
- Add ideas as they occur
- Mark what you're trying
- Note results

### When Ending
- Update with what worked/didn't
- Add new suggestions
- Plan next experiment

---

**This document grows with our collaboration. Add anything that could help!**

**Last updated:** 2026-01-30 (initial creation)

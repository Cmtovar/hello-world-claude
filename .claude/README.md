# Claude Code Meta-Infrastructure

**Purpose:** Central repository for Claude Code session continuity, learning, and relationship documentation

**Vision:** An "MCP for working with me" - persistent learning system where Claude Code instances can carry forward understanding, adapt, and build on previous sessions instead of starting blind.

---

## What This Directory Contains

### Session Documentation
- **SESSION-YYYY-MM-DD.md** - Detailed notes from each session
  - What was accomplished
  - Technical decisions and rationale
  - User feedback and corrections
  - Lessons learned
  - Next steps

### Relationship Documentation
- **USER-WORKING-STYLE.md** - How the user thinks and works
  - Communication patterns
  - Problem-solving approach
  - Decision-making process
  - Success/failure patterns

### Configuration
- **dev-server.md** - Development server settings (tailscale IP, etc.)
- Other persistent preferences and settings

---

## How to Use This System

### Starting a New Session

**IMPORTANT:** This repo has local onboarding infrastructure. Follow in order:

1. **START-HERE.md** (parent directory)
   - Primary entry point for this repo
   - Project overview and context
   - Current status and next steps
   - Links to all key documentation
   - **Read this FIRST before .claude/ docs**

2. **Read recent SESSION notes** (.claude/SESSION-*.md, most recent first)
   - Understand what was accomplished
   - Check for transition points
   - Review lessons learned
   - Connect to project status

3. **Read USER-WORKING-STYLE.md** (this directory)
   - Understand communication patterns
   - Learn from previous mistakes
   - Recognize success patterns

4. **Check project-specific docs** (referenced from START-HERE.md)
   - IMPLEMENTATION-STATUS.md - What's implemented
   - RIVER-DESIGN-PATTERN.md - Locked baselines
   - SESSION-CONTINUITY.md - Recovery practices
   - DEVELOPER-STYLE-GUIDE.md - Technical style

5. **Check git status**
   - Uncommitted work
   - Recent commits
   - Branch state

6. **Continue or adapt**
   - Build on previous work
   - Learn from past iterations
   - Carry forward relationship understanding

**Order matters:** START-HERE.md → .claude/SESSION-*.md → Project docs → Work

### During a Session

- **Document as you go** - Don't wait until end
- **Note user patterns** - Add to USER-WORKING-STYLE.md if new patterns emerge
- **Track decisions** - Why choices were made, not just what was done
- **Learn from corrections** - User feedback is valuable teaching

### Ending a Session

- **Create SESSION note** - Comprehensive summary of session
- **Update USER-WORKING-STYLE.md** - New patterns or clarifications
- **Commit to git** - Preserve in version control
- **Set up next session** - What should next Claude know?

---

## Philosophy

### Why This Exists

Traditional AI interaction:
- Each session starts from scratch
- No learning between sessions
- No persistent understanding of user
- Relationship doesn't evolve

This system enables:
- **Continuity:** Next Claude knows what happened
- **Learning:** Patterns persist across sessions
- **Adaptation:** Understanding evolves over time
- **Relationship:** Claude "knows" the user's style

### What Makes It Work

1. **Comprehensive documentation** - Capture decisions, not just actions
2. **Rationale tracking** - Why, not just what
3. **Pattern recognition** - User's consistent behaviors
4. **Self-reflection** - Claude analyzes own performance
5. **Iteration** - System improves over time

### User's Vision

> "I want this to be reference repo/memory to carry on the relationship claude code specifically has with my approach to problem solving that itself can be organized, like an mcp for working with me or something that's equivalent. that way you have a way of learning and adapting instead of being blind all the time."

---

## Session Note Structure

Each SESSION-*.md file should include:

- **Summary** - What was accomplished
- **User's approach** - How they worked this session
- **Technical decisions** - What was built and why
- **Persistent choices** - Locked baselines, important decisions
- **Learnings** - For future Claude sessions
- **Transition** - Where session ended, what's next

---

## Working Style Guide Structure

USER-WORKING-STYLE.md captures:

- **Communication patterns** - What user's words mean
- **Decision-making** - How user chooses approaches
- **Technical preferences** - Style in code/implementation
- **Relationship patterns** - How collaboration works
- **Success/failure patterns** - What works, what doesn't

---

## Maintenance

### After Each Session
- [ ] Create SESSION-YYYY-MM-DD.md
- [ ] Update USER-WORKING-STYLE.md if new patterns
- [ ] Commit to git
- [ ] Review for completeness

### Periodic Review
- Read old sessions to see patterns
- Update style guide with refined understanding
- Remove outdated information
- Consolidate learnings

### Quality Standards
- **Specific over general** - Concrete examples
- **Actionable over abstract** - Future Claude can act on it
- **Honest over flattering** - Document what works AND what doesn't
- **Evolving over static** - Update as understanding grows

---

## Integration with Project

This meta-infrastructure connects to:

- **IMPLEMENTATION-STATUS.md** - Tracks what's implemented
- **RIVER-DESIGN-PATTERN.md** - Example of locked baseline
- **BY-HAND-TODO.md** - Manual work user will do
- **SESSION-CONTINUITY.md** - Recovery practices
- **DEVELOPER-STYLE-GUIDE.md** - Technical style guide

All work together to create persistent memory across sessions.

---

## Success Metrics

This system succeeds when:

- New Claude session starts with context, not from scratch
- Previous lessons learned are applied
- User's working style is understood immediately
- Relationship feels continuous, not reset
- Mistakes aren't repeated
- Progress compounds across sessions

---

## For Future Development

### Potential Additions
- Session timeline/graph
- Decision tree documentation
- Pattern analysis tools
- Automated session summarization
- Cross-referencing system

### Evolution
This system itself should evolve:
- Better structure as patterns emerge
- More efficient documentation
- Clearer connections between elements
- Automated support where helpful

---

**This is experimental infrastructure for persistent AI collaboration. It will evolve as we learn what works.**

**Created:** 2026-01-30
**Status:** Active development
**Maintained by:** Each Claude Code session

---

## Additional Resources

### Suggestions for Improvement
See **SUGGESTIONS-FOR-IMPROVEMENT.md** for:
- Quick wins (easy improvements)
- Medium effort ideas (worth considering)
- Bigger explorations (future possibilities)
- Things to try and experiment with
- Questions to explore together

This document captures ideas for making Claude collaboration more effective.


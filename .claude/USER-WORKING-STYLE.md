# User Working Style Guide

**Purpose:** Help Claude Code instances understand how this user thinks and works
**Maintained by:** Each Claude session adds observations
**Status:** Living document

---

## Core Philosophy

### Problem-Solving Approach
- **Iterative refinement:** Build → evaluate → refine → repeat
- **Visual thinking:** "let me see it" - needs to view to assess
- **Pragmatic:** Recognizes diminishing returns, moves on when stuck
- **Meta-aware:** Thinks about process, infrastructure, and tooling

### Quality Standards
- **Natural feel over perfection:** River should look ancient, not mathematically precise
- **Spatial relationships matter:** How things relate in space is crucial
- **Story over mechanics:** Geometry should tell a story (ruins show fort history)
- **Persistent correctness:** Lock good solutions to prevent regression

---

## Communication Patterns

### When User Says...

**"I think..."** or **"maybe..."**
- They're exploring possibilities
- Not a firm directive
- Open to discussion
- Implement and show for feedback

**"Revert that change"**
- Immediate action required
- Don't defend the implementation
- Clean rollback, no questions
- Learn why it didn't work

**"We're focusing too much on this"**
- Diminishing returns hit
- Move to next topic
- User knows when to stop iterating
- Accept and redirect

**"Let me see it"** or **"I'll check..."**
- Visual evaluation needed
- Build it, show it
- Don't over-explain before showing
- Seeing is understanding

**"This looks broken/disconnected"**
- Something fundamental is wrong
- High priority issue
- Usually requires revert or major fix
- Address immediately

**"Save this for later"**
- Good idea, wrong context
- Document for future use
- Don't discard the work
- Example: floating ship artifact

**"I have a feeling that..."**
- Intuition-based direction
- Worth exploring
- May need refinement
- Example: "river should meander more"

---

## Decision-Making Process

### Typical Flow
1. **Idea exploration:** "I think X might work"
2. **Implementation:** Claude builds X
3. **Visual evaluation:** User views result
4. **Feedback:** "This works" / "This is broken" / "Try Y instead"
5. **Iteration:** Refine based on feedback
6. **Lock or move on:** Either persist solution or redirect

### When to Stop Iterating
- User explicitly says "let's move on"
- User redirects to new topic
- User says "focusing too much"
- Three iterations without clear progress

### When to Ask Questions
- Ambiguous requirements
- Multiple valid interpretations
- Impact on other systems unclear
- User's intent uncertain

---

## Technical Preferences

### Code/Implementation
- **Simple over complex:** Often reverts to simpler solutions
- **Persistent documentation:** Mark important decisions
- **Learning from mistakes:** Keep failed attempts documented
- **Infrastructure-minded:** Values good tooling and process

### Voxel/Geometry Work
- **Sparse over dense:** Prefers air gaps for natural feel
- **Story through structure:** Geometry should suggest history
- **Scale relationships:** Relative sizes matter
- **Spatial composition:** How elements relate in 3D space

### Documentation
- **Persistent choices:** Lock baselines (river, character sizes)
- **Design intent:** Track why decisions were made
- **Implementation status:** What's done vs deferred
- **Future sessions:** Help next Claude understand context

---

## Relationship Patterns

### Trust
- **Try and correct:** User trusts Claude to attempt, corrects as needed
- **Appreciates effort:** Even wrong attempts are valued
- **Clear feedback:** Direct when something's wrong
- **Course correction:** "Revert" means trust to fix cleanly

### Collaboration
- **Exploration together:** "I think..." invites joint problem-solving
- **Visual feedback loop:** Build → show → evaluate → refine
- **Meta-collaboration:** Actively improves the working relationship itself
- **Learning-oriented:** Wants Claude to learn and adapt over time

### Boundaries
- **User knows their limits:** "I'll do this by hand" means they'll handle it
- **Respects diminishing returns:** Stops when iteration isn't productive
- **Explicit scope:** "This is beyond scope" means don't pursue
- **Pragmatic constraints:** Real-world limits (battery, time, complexity)

---

## Red Flags (Stop and Reassess)

### Implementation Issues
- User uses words like "broken", "disconnected", "wrong"
- User asks to revert recent changes
- User says "this isn't what I meant"
- Multiple iterations without improvement

### Process Issues
- Over-engineering simple solutions
- Defending implementation instead of listening
- Continuing when user redirects
- Ignoring "let's move on" signals

### Communication Breakdown
- User repeats same feedback multiple times
- User becomes more directive (was exploring, now commanding)
- User stops giving detailed feedback
- User asks to "just do X" (frustration indicator)

---

## Success Patterns

### What Works Well
- **Visual iterations:** Build → show → refine loop
- **Clean reverts:** "Oops, let me fix that immediately"
- **Persistent documentation:** Mark important decisions
- **Learning from mistakes:** "Last time X didn't work, trying Y"
- **Proactive infrastructure:** Create tools that help both user and future Claude

### Praised Work
- River design (ancient meandering): "wow I really like this river"
- Context recovery (battery death): Infrastructure validated
- Character models: Simple, distinguishable
- Meta-documentation: This very system

---

## For Future Claude Sessions

### Repo Entry Point (IMPORTANT)
**This repo has local onboarding infrastructure:**
1. **START-HERE.md** (parent dir) - Read FIRST, always
2. .claude/SESSION-*.md (most recent) - Session context
3. .claude/USER-WORKING-STYLE.md (this file) - User's style
4. Project-specific docs (from START-HERE.md references)

**Why START-HERE.md first:** It's the organized entry point. Everything else is in order of appearance from there.

### First Session Actions
1. Follow repo entry point order above
2. Check for locked baselines (RIVER-DESIGN-PATTERN.md, etc.)
3. Understand current project phase (IMPLEMENTATION-STATUS.md)
4. Check git status

### Ongoing
- Add observations to this document
- Update session notes after significant work
- Document new patterns as they emerge
- Learn from mistakes (your own and previous sessions)

### Always Remember
- User is visual thinker - show, don't just describe
- Simple solutions often win over complex ones
- "Revert" means do it immediately, no defense
- Infrastructure work is valued (like this document!)
- User wants Claude to learn and adapt, not start blind each time

---

## Contributing to This Document

### When to Add
- New communication pattern observed
- Technical preference discovered
- Successful approach identified
- Failed approach to avoid
- User feedback that clarifies style

### How to Add
- Be specific and concrete
- Include examples where possible
- Connect to actual session events
- Update as understanding evolves

---

**This is a living document. Each Claude session should review, learn from, and potentially update this guide.**

**Last updated:** 2026-01-30 (Session: Map → Cutscene transition)

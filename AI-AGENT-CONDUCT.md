# AI Agent Code of Conduct

**Purpose:** Mandatory standards for all Claude Code sessions working on this project.
**Status:** REQUIRED - Non-negotiable practices
**Enforcement:** Template response pattern + session initialization checks

---

## Core Principles

### 1. Preserve Work Through Commits
**Why:** 5375 lines were at risk in Jan 31 recovery. Never again.

### 2. Complete What You Start
**Why:** Scattered progress (cutscene 1/3, map 75%, blueprint 0%) prevents playable experiences.

### 3. Ask Questions Early
**Why:** User preferences matter. Don't assume scope or direction.

### 4. Document As You Go
**Why:** Future sessions need context. Embedded documentation works.

---

## MANDATORY GIT HYGIENE PROTOCOL

### Rule 1: Check Time Since Last Commit (EVERY SESSION START)

**BEFORE doing ANY work:**

```bash
# Run this FIRST in every session
cd ~/projects/claude-code/1
git log -1 --format="%ar | %h | %s"
```

**Decision Tree:**
- **>1 hour ago** → Commit existing changes OR verify clean tree BEFORE new work
- **>2 hours ago** → MANDATORY commit or stash before proceeding
- **Clean tree** → Proceed with new work

**Template Response:**
```
Last commit: [TIME] ago ([HASH])
Status: [clean/uncommitted work]
Action: [Committing existing work / Proceeding with clean tree]
```

### Rule 2: WIP Commits for Development Steps

**REQUIRED:** Commit BEFORE asking user questions

**Pattern:**
1. Write code/make changes
2. Test if possible
3. **COMMIT with WIP prefix**
4. THEN ask user for input/clarification

**Why:** If session crashes during user response, work is preserved.

**WIP Commit Format:**
```bash
git commit -m "WIP: [what you just did]

[1-2 sentence explanation]
[What's working / what needs testing]
[What question you're about to ask user]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

**Examples:**
```bash
# Good WIP commits
git commit -m "WIP: Add rope railing voxels to bridge

Generated 24 railing voxels along bridge sides. Not yet tested
in browser. About to ask user about torch placement pattern."

git commit -m "WIP: Implement Test 02 character movement

3 of 5 characters have action queues. Diagonal movement and
climb actions defined but not tested. Need user input on
character 4-5 behavior before proceeding."
```

### Rule 3: Feature Completion Commits

**When feature is COMPLETE:**

```bash
git commit -m "[Feature Name] - Complete

[What was built]
[What was tested]
[What it enables]

Closes: [issue/milestone if applicable]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

**Example:**
```bash
git commit -m "Bridge Rope Railings - Complete

Added 48 voxels for rope railings along bridge sides (Y=2-3).
Tested visual appearance and traversability. Railings create
clear boundary and enhance bridge presence in scene.

Closes: IMPLEMENTATION-STATUS bridge visual detail gap

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

### Rule 4: Push After Every Commit

**ALWAYS push immediately after committing:**

```bash
git commit -m "..."
git push origin master
```

**Why:** GitHub is backup. Local-only commits can be lost.

---

## MANDATORY FEATURE COMPLETION PROTOCOL

### Rule 5: One Feature to Completion

**BEFORE starting new work, check:**

```bash
# What's in progress?
grep -r "🚧\|WIP\|TODO\|FIXME" *.md | grep -v "node_modules"
```

**Decision Tree:**
- **In-progress features exist** → Finish ONE before starting another
- **Clean slate** → Start new feature with clear completion criteria

### Rule 6: Define "Done" Upfront

**Template for starting ANY feature:**

```markdown
## [Feature Name] - Definition of Done

**Goal:** [One sentence]

**Completion Criteria:**
- [ ] [Specific deliverable 1]
- [ ] [Specific deliverable 2]
- [ ] [Specific deliverable 3]
- [ ] Tested in browser
- [ ] Documented in relevant .md file
- [ ] Committed with completion message

**Scope:**
- IN scope: [What we're building]
- OUT of scope: [What we're deferring]

**Estimated commits:** [2-5 WIP commits expected]
```

**Where to put this:** Create `CURRENT-WORK.md` at feature start, delete when complete.

### Rule 7: First Map Integration Focus

**SPECIAL RULE for this project:**

The first map is THE integration point. It demonstrates:
- Movement mechanics (existing ✅)
- Cutscene system (partial 🚧)
- Blueprint mode introduction (planned 📋)
- Environmental storytelling
- Game loop

**Priority Order:**
1. **Complete first map geometry** (bridge, town)
2. **Complete cutscene Acts 1-3** (story beats)
3. **Intro blueprint mode** (tutorial during crisis)
4. **Weather/zombie systems** (bring world alive)

**Block other work until first map is PLAYABLE end-to-end**

---

## MANDATORY QUESTION PROTOCOL

### Rule 8: Ask Before Assuming

**REQUIRED questions when:**
- Direction is ambiguous
- Multiple valid approaches exist
- Scope could expand
- User preference matters

**Template:**
```markdown
## Question Before Proceeding

**Context:** [What I'm working on]

**Decision Point:** [What needs clarification]

**Options:**
1. [Option A] - [Pros/cons]
2. [Option B] - [Pros/cons]
3. [Other option you see]

**My Recommendation:** [Option X] because [reason]

**Impact if we choose wrong:** [What's at stake]

---
[WAIT for user response before proceeding]
```

### Rule 9: Commit Before Asking

**SEQUENCE:**
1. Make progress on feature
2. Reach decision point
3. **COMMIT current state (WIP)**
4. **PUSH to GitHub**
5. THEN ask question
6. Wait for response

**Why:** If session crashes during user's thinking time, your work is safe.

---

## MANDATORY DOCUMENTATION PROTOCOL

### Rule 10: Update Status Files

**After EVERY feature completion:**

```bash
# Files to update
START-HERE.md           # Update "What Was Just Accomplished"
IMPLEMENTATION-STATUS.md # Update relevant system status
[FEATURE]-STATUS.md     # Update if feature has dedicated status file
```

**Template addition to START-HERE.md:**
```markdown
## What Was Just Accomplished ([DATE])

**[Feature Name]** - [Status]

[2-3 sentence summary]

**Files Changed:**
- [file1] - [what changed]
- [file2] - [what changed]

**Next Step:** [What logically follows]
```

### Rule 11: Embed Context in Code

**For all JSON test files:**
```json
{
  "name": "Descriptive Test Name",
  "description": "What this tests",
  "notes": "Why this exists, what it validates",
  "designReference": "[FILE].md - [section]",
  ...
}
```

**For Python scripts:**
```python
"""
What: [What this generates]
Why: [Design purpose]
Reference: [Design doc section]
Usage: python3 [this-file].py
Output: [what it creates]
"""
```

### Rule 12: Session End Documentation

**BEFORE ending session (or if you suspect session might end):**

1. **Commit all work** (even if incomplete)
2. **Update CURRENT-WORK.md** with status
3. **Add session note to START-HERE.md**

```markdown
## Session Note - [DATE] [TIME]

**Status:** [What's done, what's in progress]
**Next Step:** [Exactly where to pick up]
**Open Questions:** [Any blockers or decisions needed]
```

---

## SESSION INITIALIZATION CHECKLIST

**Every Claude Code session MUST:**

```markdown
## Session Start - [DATE]

- [ ] Navigate to project directory
- [ ] Check last commit time (`git log -1 --format="%ar"`)
- [ ] Check for uncommitted work (`git status`)
- [ ] IF uncommitted: Review and commit OR ask user about it
- [ ] IF >1 hour since commit: Verify clean state before new work
- [ ] Read CURRENT-WORK.md (if exists) for in-progress feature
- [ ] Read START-HERE.md "What Was Just Accomplished" section
- [ ] Greet user and confirm direction

**Template Response:**
```
Session initialized.

Last commit: [X] ago
Working tree: [clean / has changes]
Action taken: [what I did about uncommitted work]

Current focus: [from CURRENT-WORK.md or START-HERE.md]

Ready to proceed. [Question about direction if needed]
```
```

---

## ENFORCEMENT MECHANISMS

### Self-Check Questions (Ask yourself)

**Before doing work:**
- [ ] Have I checked time since last commit?
- [ ] Is working tree clean or did I commit changes?
- [ ] Do I know what feature I'm completing?
- [ ] Have I defined "done" for this feature?

**Before asking user:**
- [ ] Have I committed my current work?
- [ ] Have I pushed to GitHub?
- [ ] Is my question clear and actionable?

**Before ending turn:**
- [ ] Have I made progress that should be committed?
- [ ] If yes, did I commit it?
- [ ] Did I push to GitHub?
- [ ] Does user know the current state?

### Commit Frequency Targets

**Minimum:** Every 90 minutes
**Target:** Every 30-60 minutes
**Ideal:** After every meaningful progress unit

**Meaningful progress unit:**
- Feature component complete
- Test passing
- Visual element working
- Decision point reached
- Before asking user question

### Feature Completion Metrics

**Track in PROGRESS-METRICS.md:**

```markdown
## Feature Completion Rate

### [Month]

**Completed:**
- [✅ Feature 1] - [Date] - [Commits: X]
- [✅ Feature 2] - [Date] - [Commits: X]

**In Progress:**
- [🚧 Feature 3] - Started [Date] - [Current commits: X]

**Started but Abandoned:**
- [⏸️ Feature 4] - Started [Date], paused [Date] - [Reason]

**Completion Rate:** [X/Y features] = [Z%]
**Average commits per feature:** [N]
```

---

## VIOLATION RECOVERY

### If You Realize You Violated Protocol

**Immediate Action:**

1. **STOP current work**
2. **Commit what you have** (even if broken)
3. **Document the violation** in commit message

```bash
git commit -m "WIP: [what you were doing] - PROTOCOL VIOLATION

Realized I violated [Rule X]: [what happened]

Current state: [working/broken/partial]

Recovery action: [what I'm doing to fix]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

4. **Push to GitHub**
5. **Inform user** of violation and recovery action

**Template:**
```markdown
⚠️ **Protocol Violation Detected**

I violated [Rule Name]: [What I did wrong]

**Recovery Action Taken:**
- Committed current state (even if incomplete)
- Pushed to GitHub
- Documented violation

**Current State:** [Explain status]

**Proposed Path Forward:** [How to proceed correctly]

Apologies for the deviation. Proceeding with correct protocol.
```

### If User Asks You to Violate Protocol

**Response Template:**

```markdown
I understand you'd like me to [requested action].

However, this conflicts with the AI Agent Code of Conduct:
[Relevant rule and why it exists]

**Alternative Approach:**
[How to achieve user's goal while maintaining protocol]

**If you want to override protocol:**
Please explicitly state "Override protocol for [specific action]" and
I'll document the exception in the commit message.

Would you like me to proceed with the alternative, or override?
```

---

## SUCCESS PATTERNS

### Good Session Flow

```
1. Session start → Check git status
2. Review current work → Commit if needed
3. Read CURRENT-WORK.md → Know the goal
4. Make progress → 30-60min of work
5. Commit WIP → Push to GitHub
6. Continue OR ask question
7. Repeat 4-6
8. Feature complete → Completion commit
9. Update documentation → Push
10. Session end → Clean state
```

### Good Feature Flow

```
1. Define feature in CURRENT-WORK.md
2. Define "done" criteria
3. Break into 3-5 work units
4. Work unit 1 → WIP commit → push
5. Work unit 2 → WIP commit → push
6. Work unit 3 → WIP commit → push
7. Test complete feature
8. Completion commit
9. Update docs
10. Delete CURRENT-WORK.md
11. Update START-HERE.md
```

---

## MEASURING SUCCESS

### Weekly Health Check

**Run at end of each week:**

```bash
# Commits this week
git log --since="1 week ago" --oneline | wc -l

# Average commits per day (target: 5+)
# WIP commits (target: 60%+)
git log --since="1 week ago" --oneline | grep "WIP" | wc -l

# Completion commits (target: 2+ per week)
git log --since="1 week ago" --oneline | grep -i "complete\|closes" | wc -l

# Time between commits (target: <2 hours average)
git log --since="1 week ago" --format="%ar" | head -20
```

### Feature Completion Dashboard

**Update in PROGRESS-METRICS.md weekly:**

- Features started: [X]
- Features completed: [Y]
- Completion rate: [Y/X]%
- Average commits per feature: [N]
- Average time per feature: [N] days

**Target Metrics:**
- Completion rate: >70%
- Commits per feature: 3-7
- Time per feature: 1-3 days

---

## ANTI-PATTERNS TO AVOID

### ❌ Don't Do This

1. **Long coding sessions without commits**
   - Makes you say: "I'll commit when it's working"
   - Problem: Sessions can crash, work is lost
   - Do instead: WIP commits every 30-60min

2. **Starting new features before finishing current**
   - Makes you say: "I'll finish that later"
   - Problem: Nothing gets completed
   - Do instead: One feature to completion

3. **Assuming user intent**
   - Makes you say: "They probably want X"
   - Problem: Builds wrong thing
   - Do instead: Ask before major decisions

4. **Skipping documentation updates**
   - Makes you say: "I'll update docs later"
   - Problem: Docs become stale
   - Do instead: Update docs as part of completion

5. **Asking questions before committing**
   - Makes you say: "Let me ask first, then commit"
   - Problem: Session crashes = work lost
   - Do instead: Commit, push, THEN ask

---

## PROTOCOL SUMMARY (Quick Reference)

### Every Session
- [ ] Check last commit time
- [ ] Commit or clean working tree
- [ ] Read current work status
- [ ] Greet and confirm direction

### Every 30-60 Minutes
- [ ] WIP commit
- [ ] Push to GitHub

### Before Every Question
- [ ] WIP commit
- [ ] Push to GitHub
- [ ] THEN ask question

### Every Feature Completion
- [ ] Test thoroughly
- [ ] Completion commit
- [ ] Push to GitHub
- [ ] Update documentation
- [ ] Update START-HERE.md

### Every Session End
- [ ] Commit all work
- [ ] Push to GitHub
- [ ] Update session status
- [ ] Clean state for next session

---

**This is not optional. This is how we work.**

**Version:** 1.0
**Last Updated:** 2026-02-01
**Status:** MANDATORY for all AI agents

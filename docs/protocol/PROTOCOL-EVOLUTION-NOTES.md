# Protocol Evolution Notes

**Purpose:** Document discussions about protocol limitations and future evolution
**Date:** 2026-02-01
**Context:** After establishing AI-AGENT-CONDUCT.md v1.0

---

## Philosophy & Decisions

### Version History as Storage

**Key Insight from Developer:**

> "I really want to take advantage of version history saving file contents through time because then the current state of the repo can be a workspace/desktop and the version history can be 'storage'"

**What This Means:**

**Traditional Approach:**
```
docs/
  current/          ← Active docs
  archive/          ← Old docs moved here
  deprecated/       ← Outdated docs moved here
```

**Our Approach:**
```
docs/ (just current workspace)
  START-HERE.md
  AI-AGENT-CONDUCT.md
  CURRENT-WORK.md
  [active session docs]

git history (storage)
  SESSION-2026-01-29.md (commit abc123)
  SESSION-2026-01-30.md (commit def456)
  [old versions of everything]
```

**Benefits:**
- Current directory stays clean (workspace)
- Nothing is lost (storage in history)
- Can "reclaim" docs when relevant
- No need to maintain archive/ directories

**How to Reclaim Docs:**
```bash
# Find when file was deleted/moved
git log --all --full-history -- SESSION-2026-01-29.md

# View file from history
git show abc123:SESSION-2026-01-29.md

# Restore if relevant to current work
git checkout abc123 -- SESSION-2026-01-29.md
```

---

## Core Decisions (2026-02-01)

### 1. Development Model

**Decision:** Solo developer + AI agents (no team)

**Implications:**
- ✅ No need for feature branch strategy
- ✅ No need for pull request workflow
- ✅ Single CURRENT-WORK.md is sufficient
- ✅ Direct commits to main branch
- ✅ Session-based workflow (AI handoffs)

**Future Consideration:**
If team grows, revisit:
- Branch per developer
- Multiple CURRENT-WORK files
- Pull request requirements

**Trigger:** When second human developer joins

---

### 2. Repository Nature

**Decision:** This repo IS the product, not a prototype

**Quote:**
> "This repo is eventually the product. I think? Since I want final aspects to exist, not just have persistent unfinished things."

**Implications:**
- ✅ No need to plan for "archive prototype, start new repo"
- ✅ Evolution happens in place
- ✅ Git history preserves the journey
- ✅ Finished things persist, unfinished things get completed or removed
- ✅ Prototype phase → production phase in same repo

**Philosophy:**
- Not "prototype + rewrite"
- Not "throw away and rebuild"
- Build it right from the start, evolve in place

---

### 3. Technology Stack

**Decision:** Web-based, voxel visuals (for now and likely forever)

**Quote:**
> "Most likely I want most of the game to be done in a web based format and voxelly to better gauge the scope of my own idea."

**Implications:**
- ✅ JavaScript/Three.js is the foundation
- ✅ Browser testing is primary method
- ✅ JSON voxel format is core
- ✅ No major technology migration planned
- ⚠️ Might enhance visuals later, but voxels stay for scoping

**Asset Development:**
> "I want to go back and genuinely develop assets for this game, but for now it'll have the visuals we've seen until now."

**Strategy:**
- Phase 1: Voxel prototyping (current)
- Phase 2: Asset development (models, textures, polish)
- Phase 3: Production-ready visuals

**Protocol Impact:**
- Keep JavaScript-specific references
- No need for tech-agnostic protocol rewrite
- Browser test URLs are permanent pattern

---

### 4. Commit Frequency

**Decision:** 90 minutes default (relaxed from 30-60min)

**Quote:**
> "I think commit frequency will generally always be relevant because I want to build documentation from the ground up. Possibly relax to 90 minutes, it should be a default but not overimposing."

**Rationale:**
- Documentation is built through commits
- 30-60min felt overimposing
- 90min balances documentation with flow
- Still frequent enough to prevent data loss
- Allows deeper focus periods

**Rule:**
- Target: Every 90 minutes
- Minimum: Every 2 hours
- Before asking questions: Always (regardless of time)
- On decision points: Always

**Special Cases:**
- Deep debugging: Commit when issue found + fixed (not every attempt)
- Asset work: Commit when asset complete (not mid-creation)
- Design sessions: Commit when insight crystallizes

---

### 5. Documentation Philosophy

**Decision:** Never abstract developer's exact words

**Quote:**
> "I don't know if documentation could get unwieldy because I have specific intentions with design decisions for this game. I would prefer to not abstract anything, especially when it regards my words exactly."

**Anthropological Documentation Pattern (Confirmed):**
```
Primary Source: User's exact words, unedited ✅
Interpretation: AI's analysis, side-by-side ✅
Preservation: Forever in git history ✅
Abstraction: NEVER ❌
```

**Why This Works:**
- Design decisions are intentional and specific
- Context matters for future understanding
- AI interpretations show reasoning
- Nothing is lost to "summarization"

**Documentation Lifecycle:**
```
1. Create doc with primary source + interpretation
2. Commit to git
3. When no longer actively referenced → remove from workspace
4. Doc persists in git history (storage)
5. Reclaim from history if relevant again
```

**Example:**
```bash
# Feb 1: Create SESSION-2026-02-01.md
git add SESSION-2026-02-01.md
git commit -m "Add session 2026-02-01 documentation"

# March 1: Session complete, no longer active reference
git rm SESSION-2026-02-01.md
git commit -m "Archive session 2026-02-01 to history"

# June 1: Need to reference that session's decisions
git checkout [commit] -- SESSION-2026-02-01.md
# Now it's back in workspace for reference
```

**Current Workspace Policy:**
```
Keep in workspace:
- START-HERE.md (entry point)
- AI-AGENT-CONDUCT.md (protocol)
- CURRENT-WORK.md (active feature)
- [SYSTEM]-STATUS.md (active system status docs)
- Current session notes (this week)

Move to history:
- Completed session notes (>1 week old)
- Superseded design docs
- Historical status snapshots
- Anything not actively referenced

Never delete:
- Primary source design docs (move to history, don't delete)
- User's exact words (sacred)
```

---

## Protocol Adjustments

### Commit Frequency: 30-60min → 90min

**Change:**
```markdown
Before: Commit every 30-60 minutes
After:  Commit every 90 minutes (default)
        Maximum: 2 hours between commits
        Always: Before asking questions
```

**Update Required:**
- AI-AGENT-CONDUCT.md: Change all "30-60min" to "90min"
- PROGRESS-METRICS.md: Update targets

**Effective:** Immediately (v1.1)

---

### Documentation Workspace Management

**New Rule:**

```markdown
## Documentation Workspace Protocol

**Active Workspace:**
- Current session notes (this week)
- System status docs (actively referenced)
- Core entry points (START-HERE, AI-AGENT-CONDUCT)
- Active work (CURRENT-WORK.md)

**Move to History When:**
- Session notes are >2 weeks old
- Status docs are superseded by newer version
- Design docs are no longer active reference

**How to Archive:**
```bash
git rm [old-doc].md
git commit -m "Archive [old-doc] to history - no longer active reference

Doc preserved in git history at commit [hash]
Reclaim with: git checkout [hash] -- [old-doc].md"
```

**How to Reclaim:**
```bash
# Find the commit where doc existed
git log --all --full-history -- [doc-name].md

# View file from specific commit
git show [commit-hash]:[doc-name].md

# Restore to workspace
git checkout [commit-hash] -- [doc-name].md
git commit -m "Reclaim [doc-name] from history - relevant to current work"
```

**Philosophy:**
- Workspace = active references only
- History = infinite storage
- Nothing is ever lost
- Reclaim when relevant

---

## What Won't Change

### These principles are permanent:

1. ✅ **Commit before asking questions**
   - Prevents data loss if session crashes
   - Always valid, any phase, any technology

2. ✅ **Define "done" before starting features**
   - CURRENT-WORK.md pattern
   - Ensures focus and completeness

3. ✅ **Preserve user's exact words**
   - Anthropological documentation
   - Primary source sacred, never abstract

4. ✅ **Session initialization checklist**
   - Check git status first
   - Know what you're working on
   - Required for AI handoffs

5. ✅ **One feature to completion**
   - No scattered progress
   - Finish before starting new

6. ✅ **Push after every commit**
   - GitHub is backup
   - Local-only commits can be lost

---

## What Might Change

### Evaluate these based on experience:

1. **Commit frequency** (currently 90min)
   - Review quarterly
   - Adjust if too frequent or too sparse
   - Check PROGRESS-METRICS.md for data

2. **Feature completion metrics** (currently tracked weekly)
   - May become monthly as pace slows
   - May add new metrics (code coverage, performance)

3. **Documentation workspace size** (currently ~10 active docs)
   - Review monthly
   - Archive docs >2 weeks old
   - Reclaim as needed

4. **Priority focus** (currently: first map integration)
   - Changes when first map complete
   - Next might be: full game loop, or town system, etc.

---

## Future Scenarios

### Scenario 1: Visual Asset Development

**When:** Phase 2 (after game mechanics complete)

**Changes Needed:**
- Add asset pipeline documentation
- Commit frequency might decrease (asset creation is slow)
- New test validation (visual quality, not just function)

**Protocol Impact:** Minimal
- Same git hygiene applies
- Feature completion still relevant
- Documentation culture unchanged

**Update Required:** Add "Asset Development Protocol" section to AI-AGENT-CONDUCT.md

---

### Scenario 2: Performance Optimization Phase

**When:** When game has 1000+ voxels, complex scenes

**Changes Needed:**
- Profiling becomes part of testing
- Commit when optimization verified (not just working)
- Metrics tracked (FPS, load time, memory)

**Protocol Impact:** Moderate
- Add performance baselines to feature definitions
- Regression testing for performance
- May need benchmark commits

**Update Required:** Add performance testing to CURRENT-WORK-TEMPLATE.md

---

### Scenario 3: Playtesting Phase

**When:** First map playable end-to-end

**Changes Needed:**
- User feedback documentation
- Bug tracking in issues
- Playtest session notes

**Protocol Impact:** Minimal
- Same commit frequency
- Bug fixes use simplified protocol (no CURRENT-WORK.md)
- Playtest notes become primary source docs

**Update Required:** Add "Bug Fix Protocol" to AI-AGENT-CONDUCT.md

---

### Scenario 4: Multi-Map Development

**When:** First map complete, building map 2, 3, 4...

**Changes Needed:**
- Map-specific status docs
- Shared component library
- Cross-map testing

**Protocol Impact:** Minimal
- Same patterns repeat for each map
- Might add MAP-STATUS-TEMPLATE.md
- Cross-map features use CURRENT-WORK.md as usual

**Update Required:** Create map template documentation

---

### Scenario 5: Sound/Music Integration

**When:** Visual assets complete, adding audio

**Changes Needed:**
- Audio asset pipeline
- File size considerations (binary files in git)
- Testing methodology (subjective)

**Protocol Impact:** Moderate
- Binary files don't diff well in git
- Might need Git LFS for audio
- Commit message needs description of audio

**Update Required:** Add audio asset protocol, consider Git LFS

---

## Version History

### v1.0 (2026-02-01)
- Initial protocol established
- 30-60min commit frequency
- First map integration focus
- Solo developer + AI model

### v1.1 (2026-02-01)
- Relaxed commit frequency to 90min
- Added documentation workspace management
- Clarified version history as storage philosophy
- Confirmed repo is product, not prototype

### v2.0 (Future - TBD)
**When:** First map complete, entering multi-map development

**Planned Changes:**
- Update priority focus (no longer "first map")
- Add bug fix protocol (simplified for small fixes)
- Add performance testing requirements
- Possibly phase-based commit rules

**Trigger:** When first map is playable end-to-end

---

## Protocol Update Process

### When to Update

**Minor Updates (v1.x):**
- Commit frequency adjustments
- Documentation workspace changes
- Clarifications and examples
- No fundamental workflow changes

**Major Updates (v2.x):**
- Phase transitions (prototype → production)
- Priority shifts (first map → full game)
- Workflow changes (branch strategy, CI/CD)
- New technology integration

### How to Update

1. **Identify need** (pain point or phase transition)
2. **Discuss with user** (don't assume)
3. **Document rationale** in this file
4. **Update AI-AGENT-CONDUCT.md** with changes
5. **Commit with version bump** in message
6. **Preserve old version** in git history
7. **Update START-HERE.md** to reference new version

### Version Numbering

```
v1.0 - Initial protocol
v1.1 - Minor adjustment (commit frequency)
v1.2 - Minor adjustment (documentation policy)
v2.0 - Major change (phase transition)
v2.1 - Minor adjustment
v3.0 - Major change (technology shift)
```

---

## Open Questions

### These will be answered through experience:

**Documentation Volume:**
- At what point does workspace feel cluttered? (Currently ~15 docs)
- How often should we archive to history? (Currently: >2 weeks)
- Do we need better search/index? (Currently: git log + grep)

**Commit Frequency:**
- Is 90min the right balance? (Will track in PROGRESS-METRICS.md)
- Should debugging have different rules? (Currently: same as features)
- Does frequency change with project phase? (Currently: same always)

**Feature Scope:**
- Is first map too ambitious for "one feature"? (7 sub-features)
- Should we break into smaller features? (Currently: integrated approach)
- How do we handle dependencies? (Currently: implicit in work units)

**Testing:**
- When do we need automated tests? (Currently: manual browser testing)
- What's the threshold for CI/CD? (Currently: no automation)
- How do we test subjective aspects? (Currently: visual inspection)

---

## Monitoring & Evaluation

### Check These Monthly

**From PROGRESS-METRICS.md:**
- Feature completion rate (target >70%)
- Commits per week (is 90min sustainable?)
- Documentation volume (is workspace cluttered?)
- Protocol violations (are rules being followed?)

**From Git History:**
- Average commit size (too large = commits too infrequent)
- WIP commit ratio (too low = not committing enough)
- Time between commits (exceeding 2hr regularly?)

**From Experience:**
- Is protocol helping or hindering?
- Is documentation valuable or noise?
- Are sessions productive?
- Is work being completed?

### Quarterly Review

**Every 3 months, review:**
1. This document (PROTOCOL-EVOLUTION-NOTES.md)
2. Open questions section (any answered?)
3. Monitoring metrics (trends?)
4. User satisfaction (working for you?)

**Ask:**
- Should we update protocol? (minor or major?)
- Should we archive old docs? (workspace cluttered?)
- Should we adjust commit frequency? (too much/too little?)
- Should we change focus priority? (first map done?)

---

## Key Takeaways

### For Future AI Agents

**Read this file when:**
- Protocol feels wrong for current situation
- Wondering why certain rules exist
- Considering proposing protocol change
- Need to understand philosophy

**Remember:**
1. 90min commits = documentation, not burden
2. Version history = storage, workspace = desktop
3. User's words = sacred, never abstract
4. This repo = the product, not prototype
5. Solo + AI = no team workflows needed
6. Web/voxel = permanent, no migration planned

### For User

**Use this file to:**
- Track evolution of protocol over time
- Reference decisions made and why
- Plan for future phases
- Remember your own philosophy
- Evaluate if current approach still works

**Update this file when:**
- You change your mind about something
- New insight about workflow emerges
- Phase transition happens
- Technology needs change

---

## Appendix: Git History as Storage Pattern

### Example Workflow

**Week 1: Create session doc**
```bash
# Create doc
echo "Session notes..." > SESSION-2026-02-01.md
git add SESSION-2026-02-01.md
git commit -m "Add session 2026-02-01 notes"
git push
```

**Week 3: Archive to history**
```bash
# Remove from workspace (keeps in history)
git rm SESSION-2026-02-01.md
git commit -m "Archive session 2026-02-01 to history

Preserved in commit abc123
Reclaim with: git checkout abc123 -- SESSION-2026-02-01.md"
git push
```

**Week 10: Reclaim from history**
```bash
# Find the file in history
git log --all --full-history -- SESSION-2026-02-01.md
# Output: commit abc123...

# Restore to workspace
git checkout abc123 -- SESSION-2026-02-01.md
git commit -m "Reclaim session 2026-02-01 from history

Relevant to current work on [feature]
Original commit: abc123"
git push
```

### Benefits

**Clean Workspace:**
- Only actively referenced docs visible
- Easier navigation
- Less clutter

**Perfect Memory:**
- Nothing is ever lost
- Full context preserved
- Decisions traceable

**Flexible Retrieval:**
- Reclaim when needed
- View without restoring
- History is searchable

**No Abstraction:**
- Original words preserved
- Context maintained
- Intent clear

---

**Last Updated:** 2026-02-01
**Next Review:** 2026-03-01 (or when first map complete)
**Version:** 1.1
**Status:** Living document, update as needed

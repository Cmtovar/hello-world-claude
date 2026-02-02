# START HERE - For Future Claude Sessions

**Last Updated:** 2026-02-01 (Simplified onboarding)
**Current Branch:** master
**Status:** Clean working tree

---

## 🚀 New Here? Start Fast

**Read this first:** **[QUICK-START.md](QUICK-START.md)** (5 minutes to productivity)

**The 3 core rules:**
1. Commit every ~90min and before asking questions
2. Work on one feature until done
3. Check `CURRENT-WORK.md` for current task

**That's enough to start building.** Everything below is optional context.

---

## Complete Onboarding Map

```
┌─────────────────────────────────────────────────────────────────────┐
│                     NEW CLAUDE SESSION STARTS                       │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
        ┌───────────────────────────────────────────────────┐
        │  QUICK-START.md (5 min - get productive)          │
        │  • 3 core rules                                   │
        │  • Ultra-quick commands                           │
        │  • Testing setup                                  │
        └───────────────────────────────────────────────────┘
                                ↓
                    ┌───────────┴───────────┐
                    │                       │
        ┌───────────▼──────────┐   ┌───────▼────────────┐
        │  START-HERE.md       │   │ CURRENT-WORK.md    │
        │  (Full context)      │   │ (Active task)      │
        │  • Project overview  │   │ If exists: do this │
        │  • Recent work       │   │ If not: choose     │
        │  • Navigation guide  │   │ from options       │
        └──────────────────────┘   └────────────────────┘
                    │
                    ↓
        ┌───────────────────────────────────────────────┐
        │  What kind of information do you need?        │
        └───────────────────────────────────────────────┘
                    ↓
        ┌───────────┴───────────┬──────────────┬──────────────┐
        ↓                       ↓              ↓              ↓
┌───────────────┐   ┌──────────────┐  ┌─────────────┐  ┌──────────────┐
│ docs/protocol/│   │ docs/design/ │  │docs/status/ │  │ docs/guides/ │
│               │   │              │  │             │  │              │
│ HOW WE WORK   │   │ WHAT TO BUILD│  │ WHAT'S DONE │  │ HOW TO DO IT │
│               │   │              │  │             │  │              │
│ • Git rules   │   │ • Game       │  │ • Feature   │  │ • Common     │
│ • Commit      │   │   systems    │  │   tracker   │  │   issues     │
│   patterns    │   │ • Narrative  │  │ • Progress  │  │ • Standards  │
│ • Session     │   │ • Architecture│ │   metrics   │  │ • Patterns   │
│   continuity  │   │ • Style guide│  │ • Cutscene  │  │ • Coordinate │
│               │   │              │  │   status    │  │   system     │
└───────────────┘   └──────────────┘  └─────────────┘  └──────────────┘
        │                   │              │                  │
        └───────────────────┴──────────────┴──────────────────┘
                                ↓
                    ┌───────────────────────┐
                    │  BUILD THE FEATURE    │
                    │  • Follow 3 rules     │
                    │  • Commit every 90min │
                    │  • Test as you go     │
                    └───────────────────────┘
                                ↓
                    ┌───────────────────────┐
                    │  docs/sessions/       │
                    │  Record what happened │
                    └───────────────────────┘
```

### Information Access Patterns

**"I need to get oriented"** → QUICK-START.md → START-HERE.md
**"What am I working on?"** → CURRENT-WORK.md (or docs/status/)
**"How do I work here?"** → docs/protocol/AI-AGENT-CONDUCT.md
**"What should I build?"** → docs/design/ + docs/status/
**"I'm stuck on [X]"** → docs/guides/
**"What happened before?"** → docs/sessions/

---

## Project Overview

**3D tactical Fire Emblem-inspired game** with vertical traversal, built with Three.js + voxels.

**Status:**
- ✅ Movement mechanics (7/7 done)
- ✅ Cutscene system (Test 01 working)
- 🚧 First map integration (bridge, scenes, blueprint intro)

**Current Focus:** Complete first playable map with integrated systems

---

## Recent Work (Last 3 Sessions)

**2026-02-01** - Simplified onboarding
- Created QUICK-START.md (5min to productivity)
- Organized docs into folders (less overwhelming)
- Reduced reading burden from 30min → 5min

**2026-02-01** - Protocol & recovery
- Recovered 5375 lines of cutscene work
- Established AI-AGENT-CONDUCT.md
- Created PROTOCOL-EVOLUTION-NOTES.md

**2026-01-30** - Cutscene system
- Implemented action queue pattern
- Test 01 working (5 characters in parallel)
- JSON validation system

**See:** `docs/sessions/` for detailed session notes

---

## What Changed Since Last Session

**Quick orientation (run these):**
```bash
git log --oneline -5          # Last 5 commits
git log --since="24 hours ago" --oneline  # Last 24 hours
```

**Current commit:** Check with `git log -1 --format="%h - %s"`

**Files changed recently:**
```bash
git diff --stat HEAD~3..HEAD  # Changes in last 3 commits
```

This helps orient to what happened since you last worked.

---

## Major Design Session (2026-01-29)

**Major design session** that created comprehensive game system architecture:

1. **Constraint Interface Pattern** - Objects as affordances with interchangeable signatures
2. **Blueprint Mode** - AP regeneration + parallel coordination system
3. **Template Composition** - Visual programming for tactics with control flow
4. **Progression Through Units** - Capability-based gating (units limited, not player creativity)
5. **Techniques & Environment** - Offset system + environmental weapons
6. **Almanac & Template IDE** - Learning tools with temporal playback

Plus: Complete narrative framework for first map "The Bridge at Old Fort Crossing"

---

## Navigation Guide

```
┌─────────────────────────────────────────────────────────────┐
│  New Session Flow                                           │
└─────────────────────────────────────────────────────────────┘
                           ↓
              ┌────────────────────────┐
              │   QUICK-START.md       │  ← Start here (5 min)
              │   (3 rules, get going) │
              └────────────────────────┘
                           ↓
        ┌──────────────────┴──────────────────┐
        ↓                                     ↓
┌───────────────┐                    ┌────────────────┐
│ START-HERE.md │                    │ CURRENT-WORK.md│
│ (full context)│                    │ (active task)  │
└───────────────┘                    └────────────────┘
        ↓                                     ↓
┌──────────────────────────────────────────────────────┐
│                   docs/ folders                      │
└──────────────────────────────────────────────────────┘
```

### Root Files (Mainstays)

```
/
├── QUICK-START.md          ← 5-minute onboarding
├── START-HERE.md           ← Full context (you are here)
├── README.md               ← Project overview
├── CURRENT-WORK.md         ← Active feature scope (ephemeral)
└── index.html              ← The game itself
```

### Documentation Directories

```
docs/
├── protocol/      How we work together
│   └── AI-AGENT-CONDUCT.md (git rules, commit patterns)
│
├── design/        What we're building
│   └── [game systems, narrative, architecture]
│
├── status/        Current state of features
│   └── IMPLEMENTATION-STATUS.md (main tracker)
│
├── guides/        How-to references
│   └── [troubleshooting, standards, patterns]
│
└── sessions/      Historical development notes
    └── SESSION-*.md (day-by-day records)
```

### Asset Directories

```
test-maps/         Micro-maps for testing mechanics (JSON)
story-geometry/    Scene voxel data + generation scripts
concepts/          Deep design explorations
tests/             Playwright test suite (future)
```

**Navigation Tips:**
- **Stuck?** → `docs/guides/`
- **What's next?** → `docs/status/IMPLEMENTATION-STATUS.md`
- **How do we work?** → `docs/protocol/AI-AGENT-CONDUCT.md`
- **Design questions?** → `docs/design/`
- **What happened?** → `docs/sessions/`

---

## Detailed Repository Organization

### Root Level Files (Beyond the Mainstays)

The root may contain session-specific or design files like:
- `SESSION-YYYY-MM-DD.md` - Comprehensive session summaries
- Design documents from major sessions (e.g., `ARCHITECTURE.md`, `FIRST-MAP-NARRATIVE.md`, `MAP-DESIGN-CONCEPTS.md`, `CONSTRAINT-INTERFACE-PATTERN.md`)

These get created during design sessions and may later be organized into `docs/` folders.

### The concepts/ Directory - Anthropological Pattern

```
concepts/
├── blueprint-mode-design.md               # Primary source
├── blueprint-mode-interpretation.md       # Analysis
├── template-composition-system.md         # Primary source
├── template-composition-interpretation.md # Analysis
├── progression-through-units.md           # Primary source
├── progression-through-units-interpretation.md
├── techniques-and-environment.md          # Primary source
├── techniques-and-environment-interpretation.md
├── almanac-and-template-ide.md            # Primary source
├── almanac-and-template-ide-interpretation.md
├── rainbow-unicorn.md                     # Future unit concept
├── odm-gear.md                            # Future unit concept
└── llm-visual-testing.md                  # Future testing concept
```

**Pattern:** Each major system has TWO files:
- **Primary Source** - User's exact words, unedited (design intent)
- **Interpretation** - Claude's analysis, implications, implementation notes

This preserves both vision and technical understanding for future sessions.

### The story-geometry/ Directory

```
story-geometry/
├── *.json    Scene voxel data (complete-scene, ruins, river, bridge, etc.)
├── *.py      Scene generation scripts (22 Python scripts)
└── README.md Documentation for geometry system
```

Contains both hand-crafted scenes and procedural generation tools.

### The test-maps/ Directory - Dual Purpose

```
test-maps/
├── testBasicMovement.json      # Mechanic validation maps
├── testDiagonalMovement.json
├── testDescendOneBlock.json
├── ...
├── character-01-scholar.json   # Cutscene character definitions
├── enemy-zombie.json           # Enemy definitions
└── ... (many more test + cutscene files)
```

Serves TWO purposes:
1. Micro-map tests for movement mechanics
2. Character/enemy definitions for cutscenes

### The tests/ Directory

```
tests/
├── package.json
├── playwright.config.js
└── specs/
    └── [Playwright test files - future]
```

Playwright test suite infrastructure (for future automated testing).

---

## The Anthropological Documentation Pattern

**Key Innovation:** Save both primary source AND interpretation

**Format:**
- **Primary Source:** User's exact words, unedited
- **Interpretation:** Claude's analysis, implications, action items
- **Side-by-side:** Both in version history
- **Purpose:** Future sessions can study both design intent and implementation implications

**Example:**
- `concepts/blueprint-mode-design.md` - Exact transcript of user's description
- `concepts/blueprint-mode-interpretation.md` - System analysis, data structures, open questions

---

## What to Do Next

**Quick Decision Tree:**

```
New session starts
    ↓
CURRENT-WORK.md exists? ──YES──→ Continue that feature
    ↓ NO
    ↓
Read docs/status/IMPLEMENTATION-STATUS.md
    ↓
Pick highest priority OR choose from options below
    ↓
Create CURRENT-WORK.md from template
    ↓
Start building
```

### Option A: Implement First Map
**Goal:** Create "The Bridge at Old Fort Crossing" as playable level

**Steps:**
1. Read `docs/design/FIRST-MAP-NARRATIVE.md` (complete narrative)
2. Design voxel layout (20x20 grid with elevation)
3. Create first-map-voxels.json (exact terrain)
4. Define constraints for bridge, ruins, river
5. Implement rain weather system
6. Add zombie spawn mechanic
7. Script alchemist cutscene
8. Build town layout
9. Test gameplay flow

**Why Start Here:**
- Tests movement mechanics in real context
- Creates framework for all future maps
- Establishes visual style and pacing
- Narrative hook for progression

### Option B: Implement AP/Blueprint System
**Goal:** Prototype core tactical system

**Steps:**
1. Read `concepts/blueprint-mode-*.md` files
2. Implement AP regeneration (units fill to 100%)
3. Create blueprint mode UI (time-freeze state)
4. Add single-unit action planning
5. Implement parallel execution
6. Test with existing movement mechanics
7. Add visual feedback (AP bars, timeline)

**Why Start Here:**
- Foundation for all tactical gameplay
- Can be tested with simple test maps
- Enables template system later
- Core differentiator from Fire Emblem

### Option C: Continue Design Exploration
**Goal:** Design remaining systems or new features

**Approach:**
1. Read `docs/design/DEVELOPER-STYLE-GUIDE.md` for working style
2. Start with collaborative discussion
3. Let objectives emerge naturally
4. Use primary source + interpretation pattern
5. Save progress frequently
6. Commit when insights crystallize

**Why Start Here:**
- More systems need design (town, crafting, etc.)
- User enjoys collaborative exploration
- Builds on constraint foundation
- Documents design rationale

---

## Key Principles

### Design Philosophy
- **Declarative over imperative** - Specify what's possible, not how
- **Emergent over prescribed** - Complex behavior from simple rules
- **Interface-based thinking** - Affordances, not objects
- **Composition is key** - Everything composes with everything

### Progression Philosophy
- **Units are limited, not player creativity**
- **Template tools fully accessible from start**
- **Capability gates execution, not design**
- **Knowledge acquisition is never punished**

### Communication Style
- **Natural emergence** - Let objectives crystallize through discussion
- **Collaborative thinking** - Extend ideas, notice patterns
- **Document as you go** - Capture insights when they happen
- **Primary source + interpretation** - Preserve intent + analysis

---

## Common Questions

**Q: What's the constraint interface pattern?**
A: Objects expose what they CAN do (affordances), not what they ARE. Objects with matching constraint signatures are interchangeable. This enables modular level design and emergent gameplay.

**Q: How does blueprint mode differ from Fire Emblem?**
A: Fire Emblem is sequential (I go → you go). Blueprint mode enables true parallelism - multiple units coordinate simultaneously. Creates "anti-turtle" design where space becomes a resource.

**Q: Why separate primary source and interpretation?**
A: Preserves design intent (what the developer actually said) alongside implementation analysis (what it means technically). Future sessions can study both to understand the "why" behind decisions.

**Q: What's the relationship between templates and techniques?**
A: Techniques are individual actions (attack, move, shield). Templates are coordinated sequences of techniques across multiple units, with control flow. Think: techniques are functions, templates are programs.

**Q: How does progression work if template tools aren't gated?**
A: Player can design any template from the start. But templates require specific unit capabilities to execute. Progression = acquiring units that enable your designs. Creativity isn't gated, execution is.

---

## Git Information

**Repository:** https://github.com/Cmtovar/hello-world-claude.git
**Branch:** master

**To Check Current State:**
```bash
cd /data/data/com.termux/files/home/projects/claude-code/1
git status              # Check current state
git log -1              # See latest commit
git log --oneline -5    # See last 5 commits
```

**Example Recent Commits (may be outdated - run git log):**
- `052d31a` - Fix all missing pieces - complete onboarding
- `f285c07` - Simplify onboarding - reduce overwhelm
- `ef2ed4b` - Protocol v1.1 - Evolution Notes and Commit Frequency Adjustment

**Note:** Commit hashes above are examples. Run `git log` for current state.

---

## If Session Closes Unexpectedly

**Recovery Infrastructure Is In Place:**
- ✅ All design documents committed
- ✅ Pushed to GitHub
- ✅ Comprehensive session summary written
- ✅ SESSION-CONTINUITY.md documents recovery practices
- ✅ This START-HERE guide provides entry point

**To Resume (Recovery Procedure):**
1. Read **SESSION-CONTINUITY.md** first (recovery practices)
2. Check `git status` for uncommitted work
3. Read most recent SESSION-*.md file
4. Read this file (START-HERE.md) for project context
5. Review uncommitted files for embedded documentation (JSON `notes` fields)
6. Choose path: Implement map, implement systems, or continue design
7. Follow anthropological documentation pattern for new work

**Tested:** 2026-01-30 battery death recovery - SUCCESS ✅

---

## User's Next Stated Interest

**From end of session:**
> "Let's update the history and push to version control this initiative we've found ourselves in. That way if the session closes unexpectedly, a claude session can pick up at this very moment."

**Completed:** ✅ Everything committed and pushed

**User's Vision for First Map:**
- Rope bridge over small creek/river
- Old military battlement ruins
- Baby anomaly encounter → zombie uprising → alchemist rescue
- Tutorial through crisis, introduces core systems
- Returns to town for exploration and IDE introduction

**User wants:**
- Diegetic teaching (learn through story, not menus)
- Balance between deep tactical systems and accessible narrative
- Progression that respects player intelligence
- Multi-session development with careful documentation

---

**Current Moment:** Ready to begin implementation OR continue design exploration.

**Future Claude: Start with SESSION-2026-01-29.md for full context, then choose your path.**

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

**Major design session** that created comprehensive game system architecture:

1. **Constraint Interface Pattern** - Objects as affordances with interchangeable signatures
2. **Blueprint Mode** - AP regeneration + parallel coordination system
3. **Template Composition** - Visual programming for tactics with control flow
4. **Progression Through Units** - Capability-based gating (units limited, not player creativity)
5. **Techniques & Environment** - Offset system + environmental weapons
6. **Almanac & Template IDE** - Learning tools with temporal playback

Plus: Complete narrative framework for first map "The Bridge at Old Fort Crossing"

---

## Documentation Structure

```
/
├── QUICK-START.md              ← Start here (5 min)
├── START-HERE.md               ← You are here (context)
├── README.md                   ← Project overview
├── CURRENT-WORK.md             ← Active feature (if exists)
│
├── docs/
│   ├── protocol/               ← How we work
│   │   ├── AI-AGENT-CONDUCT.md      (Full rules)
│   │   └── PROTOCOL-EVOLUTION-NOTES.md
│   │
│   ├── design/                 ← What we're building
│   │   ├── FIRST-MAP-NARRATIVE.md
│   │   ├── DEVELOPER-STYLE-GUIDE.md
│   │   └── [design docs]
│   │
│   ├── status/                 ← Current state
│   │   ├── IMPLEMENTATION-STATUS.md
│   │   ├── CUTSCENE-SYSTEM-STATUS.md
│   │   └── PROGRESS-METRICS.md
│   │
│   ├── guides/                 ← How-to references
│   │   ├── COMMON-ISSUES.md
│   │   └── TEST-JSON-STANDARD.md
│   │
│   └── sessions/               ← Historical notes
│       └── SESSION-*.md
│
├── index.html                  ← The game
├── test-maps/                  ← Test scenarios
└── story-geometry/             ← Scene voxel data
```

**Most files are optional. Start with QUICK-START.md.**

---

## File Organization

```
/
├── START-HERE.md                    # This file
├── SESSION-2026-01-29.md            # Today's comprehensive summary
├── DEVELOPER-STYLE-GUIDE.md         # Working patterns for future sessions
├── README.md                        # Project overview
├── ARCHITECTURE.md                  # Technical architecture
├── FIRST-MAP-NARRATIVE.md           # Complete first map story
├── MAP-DESIGN-CONCEPTS.md           # Map design philosophy
├── CONSTRAINT-INTERFACE-PATTERN.md  # Core system foundation
│
├── concepts/                        # System design documents
│   ├── blueprint-mode-design.md               # Primary source
│   ├── blueprint-mode-interpretation.md       # Analysis
│   ├── template-composition-system.md         # Primary source
│   ├── template-composition-interpretation.md # Analysis
│   ├── progression-through-units.md           # Primary source
│   ├── progression-through-units-interpretation.md
│   ├── techniques-and-environment.md          # Primary source
│   ├── techniques-and-environment-interpretation.md
│   ├── almanac-and-template-ide.md            # Primary source
│   ├── almanac-and-template-ide-interpretation.md
│   ├── rainbow-unicorn.md                     # Future unit concept
│   ├── odm-gear.md                            # Future unit concept
│   └── llm-visual-testing.md                  # Future testing concept
│
├── index.html                       # Main game (Three.js)
├── test-builder.js                  # Test generation factory
├── mechanics-graph.json             # Mechanic dependency graph
│
├── story-geometry/                  # Story content + generation tools
│   ├── *.json                       # Scene files (complete-scene, ruins, river, etc.)
│   ├── *.py                         # Scene generation scripts (22 scripts)
│   └── README.md                    # Story geometry documentation
│
├── test-maps/                       # Micro-map tests + cutscene elements (JSON)
│   ├── testBasicMovement.json
│   ├── testDiagonalMovement.json
│   ├── character-01-scholar.json
│   ├── enemy-zombie.json
│   └── ... (many more)
│
└── tests/                           # Playwright test suite (future)
    ├── package.json
    ├── playwright.config.js
    └── specs/
```

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

### Option A: Implement First Map
**Goal:** Create "The Bridge at Old Fort Crossing" as playable level

**Steps:**
1. Read `FIRST-MAP-NARRATIVE.md` (complete narrative)
2. Design voxel layout (20x20 grid with elevation)
3. Create `first-map-voxels.json` (exact terrain)
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
1. Read `DEVELOPER-STYLE-GUIDE.md` for working style
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
**Current Commit:** 47f4253 (Project reorganization - scene generation tools)
**Branch:** master

**Recent Commits:**
- `47f4253` - Organize project structure - consolidate scene generation tools (48 files, 19,540 insertions)
- `ab8cc59` - Combine bridge and forest floor into complete scene
- `4950403` - Major game systems design (14,731 insertions!)

**To Continue Work:**
```bash
cd /data/data/com.termux/files/home/projects/claude-code/1
git status  # Check current state
git log     # See commit history
```

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

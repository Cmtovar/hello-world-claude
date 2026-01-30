# START HERE - For Future Claude Sessions

**Last Updated:** 2026-01-30 (added recovery infrastructure)
**Current Branch:** master
**Status:** All work committed and pushed to GitHub

---

## Quick Context

This is a **3D tactical Fire Emblem-inspired game** with vertical traversal, built with Three.js.

**Current State:**
- ✅ Movement mechanics fully implemented (7/7 core mechanics)
- ✅ Complete game systems designed (6 major interconnected systems)
- ✅ First map narrative framework complete
- 🚧 Ready to implement: First map OR AP/blueprint system

**⚠️ Recovery Infrastructure:**
- **SESSION-CONTINUITY.md** - Critical practices for session recovery (tested 2026-01-30)
- **COMMON-ISSUES.md** - Known problems and solutions
- **.claude/dev-server.md** - Dev server config (tailscale IP: 100.93.126.24)

---

## What Was Just Accomplished (2026-01-29)

**Major design session** that created comprehensive game system architecture:

1. **Constraint Interface Pattern** - Objects as affordances with interchangeable signatures
2. **Blueprint Mode** - AP regeneration + parallel coordination system
3. **Template Composition** - Visual programming for tactics with control flow
4. **Progression Through Units** - Capability-based gating (units limited, not player creativity)
5. **Techniques & Environment** - Offset system + environmental weapons
6. **Almanac & Template IDE** - Learning tools with temporal playback

Plus: Complete narrative framework for first map "The Bridge at Old Fort Crossing"

---

## Essential Reading Order

### If You Need Full Context:
1. **This file** (you are here)
2. `SESSION-2026-01-29.md` - Comprehensive summary of what was designed
3. `DEVELOPER-STYLE-GUIDE.md` - How the developer thinks and works
4. `README.md` - Project overview
5. `ARCHITECTURE.md` - Technical architecture (from previous session)

### If Implementing First Map:
1. `FIRST-MAP-NARRATIVE.md` - Complete story, encounter sequence, world questions
2. `MAP-DESIGN-CONCEPTS.md` - Rope bridge geometry, map distinctiveness
3. `CONSTRAINT-INTERFACE-PATTERN.md` - Foundation system for everything

### If Implementing Game Systems:
1. `concepts/blueprint-mode-design.md` + interpretation - AP system & parallel coordination
2. `concepts/template-composition-system.md` + interpretation - Template IDE system
3. `concepts/techniques-and-environment.md` + interpretation - Offset system & environmental weapons
4. `concepts/almanac-and-template-ide.md` + interpretation - Learning tools

### If Exploring/Designing New Systems:
1. `DEVELOPER-STYLE-GUIDE.md` - Working style, design patterns, communication preferences
2. All files in `concepts/` directory - See how systems were designed
3. Note the **anthropological documentation pattern**: primary source + interpretation side-by-side

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
├── test-maps/                       # 12 micro-map tests (JSON)
│   ├── testBasicMovement.json
│   ├── testDiagonalMovement.json
│   ├── testClimbUpOne.json
│   └── ... (9 more)
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
**Current Commit:** 4950403 (Major game systems design session)
**Branch:** master

**Recent Commits:**
- `4950403` - Major game systems design (14,731 insertions!)
- `c7fe4cb` - Initial hello world README

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

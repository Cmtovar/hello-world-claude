# Session Continuity Infrastructure

**Purpose:** Document the practices that enable recovery from unexpected session interruptions (battery death, crashes, network issues, etc.).

**Created:** 2026-01-30
**Status:** CRITICAL - These practices are non-negotiable for project resilience

---

## What Made Recovery Possible

### Today's Recovery Success (2026-01-30)
After unexpected battery death mid-session, recovery was successful because:

1. **Git captured uncommitted work** - All files preserved locally
2. **Embedded documentation** - JSON files had detailed `notes` fields explaining structure
3. **Session notes existed** - SESSION-2026-01-29.md provided context
4. **Clear file organization** - story-geometry/ and test-maps/ separation was obvious
5. **Commit messages told a story** - Git log showed progression of work
6. **COMMON-ISSUES.md** - Known problems were documented with workarounds

### What This Taught Us
**The infrastructure matters more than the code.** Without these practices, all ruins work could have been lost or incomprehensible.

---

## Required Practices (Must Persist)

### 1. Commit Frequently with Descriptive Messages
**Why:** Git preserves work even if uncommitted (in working directory)
**How:** After each complete thought/structure, commit with meaningful message

**Good commit messages:**
```
✓ "Add rope bridge geometry - first story keyframe"
✓ "Create ruins structure with tower and battlement walls"
✓ "Fix river to be forest floor + create COMMON-ISSUES doc"
```

**Bad commit messages:**
```
✗ "Update files"
✗ "WIP"
✗ "Changes"
```

### 2. Embed Documentation in Data Files
**Why:** Documentation travels with the data, never gets out of sync
**How:** Use `notes` field in JSON files

**Example:**
```json
{
  "voxels": [...],
  "notes": {
    "structure_breakdown": {
      "standing_tower_base": {
        "location": "X: 14-16, Z: -3 to 3",
        "description": "Square tower footprint with cobblestone walls",
        "features": [
          "Walls at Y=0-1 forming perimeter",
          "Entry gap on east side (toward bridge)"
        ]
      }
    },
    "deferred": [
      "Torch placement (light sources)",
      "Vegetation overgrowth (ivy, moss)"
    ]
  }
}
```

**What to document:**
- What each structure represents
- Color meanings (cobblestone: 11184810, wood: 9127187)
- Deferred features (what's missing but planned)
- Gameplay features (platforms, cover, hiding spots)
- Architectural logic (why certain materials/patterns were chosen)

### 3. Session Notes After Major Work
**Why:** Provides narrative context git commits can't capture
**How:** Create/update SESSION-[DATE].md after significant work

**What to include:**
- What was accomplished
- Decisions made and why
- Problems encountered
- Files created/modified
- Next steps

**Location:** Root of project directory

### 4. START-HERE.md for New Sessions
**Why:** Claude sessions don't have memory - need clear entry point
**How:** Keep START-HERE.md updated with current status

**Should answer:**
- What is this project?
- What's the current state?
- What are we working on next?
- Where are the key documents?

### 5. COMMON-ISSUES.md for Known Problems
**Why:** Don't rediscover the same problems repeatedly
**How:** Document issues as they arise with:
- Problem description
- Symptoms
- Root cause
- Current workaround
- Actual solution needed

**Template in COMMON-ISSUES.md**

### 6. Clear Directory Structure
**Why:** Files organized by purpose are self-documenting
**How:** Maintain separation:

```
/project-root/
  /story-geometry/      # Actual game content
  /test-maps/           # Mechanical validation tests
  /concepts/            # Design documents
  /.claude/             # Development configuration
  SESSION-*.md          # Session notes
  START-HERE.md         # Entry point
  COMMON-ISSUES.md      # Known problems
```

### 7. Development Server Configuration
**Why:** Consistent environment across sessions
**How:** Document in `.claude/dev-server.md`

**Tailscale IP:** 100.93.126.24
**Command:** `python -m http.server -b 100.93.126.24 8080`

---

## Recovery Procedure (For Future Sessions)

When starting a session after interruption:

### Step 1: Check Git Status
```bash
git status          # See uncommitted changes
git log --oneline -20  # See recent commits
```

### Step 2: Read Session Notes
```bash
ls SESSION-*.md     # Find recent session notes
cat SESSION-2026-01-29.md  # Read most recent
```

### Step 3: Review Uncommitted Work
```bash
git diff            # See modifications
ls -lt | head -20   # See recently modified files
```

### Step 4: Read Embedded Documentation
- Check JSON `notes` fields in new/modified files
- Understand what structures represent
- See what was deferred

### Step 5: Resume or Commit
- If work was complete: commit with descriptive message
- If work was in progress: read notes, understand context, continue

---

## Anti-Patterns (What NOT to Do)

### ❌ Don't: Work without committing for hours
**Why:** Uncommitted work is fragile
**Instead:** Commit after each complete structure/feature

### ❌ Don't: Use TODO comments in code
**Why:** TODOs get lost, forgotten, out of sync
**Instead:** Use `notes.deferred` field or COMMON-ISSUES.md

### ❌ Don't: Keep context only in chat
**Why:** Chat history is ephemeral, can be lost
**Instead:** Persist decisions in session notes or embedded docs

### ❌ Don't: Create files without documentation
**Why:** Future sessions won't understand purpose
**Instead:** Add `notes` field or README in directory

### ❌ Don't: Solve problems without documenting
**Why:** Will hit same problem again
**Instead:** Add to COMMON-ISSUES.md with workaround

---

## Measuring Success

**Good infrastructure enables:**
- ✓ Recovery from unexpected interruptions (battery, crash, etc.)
- ✓ Context restoration in < 5 minutes
- ✓ Understanding of uncommitted work
- ✓ Clear next steps
- ✓ No lost work

**Signs of infrastructure failure:**
- ✗ "What was I working on?"
- ✗ "What do these files mean?"
- ✗ "Why did I make this change?"
- ✗ "What was the next step?"
- ✗ Lost or incomprehensible work

---

## Evolution of This Document

As we discover new practices that help with continuity, add them here.

### Potential Additions
- Automated git hooks (commit reminders, JSON validation)
- Backup scripts for uncommitted work
- Session timestamping
- Work session summaries (auto-generated)

---

## For Future Claude Sessions

When you start a session:
1. Read START-HERE.md first
2. Check git status for uncommitted work
3. Read most recent SESSION-*.md
4. If recovering from interruption, follow Recovery Procedure above

**These practices are not optional.** They are the foundation that makes long-term development across multiple sessions possible.

---

**Tested:** 2026-01-30 (battery death recovery - SUCCESS)
**Maintained by:** All Claude sessions + user
**Review frequency:** After any difficult recovery or context loss

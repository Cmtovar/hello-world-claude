# Quick Start - New Claude Session

**Goal:** 5 minutes to productivity. Start working, read details later.

---

## 🏗️ Just Want to Start Building?

**Ultra-quick version (60 seconds):**
```bash
cd ~/projects/claude-code/1
git status                    # Make sure it's clean
# Edit index.html or create files
# When you make progress:
git add -A && git commit -m "WIP: what you did" && git push
```

**Test your changes:**
```bash
python -m http.server -b 100.93.126.24 8080
# Open: http://100.93.126.24:8080/
```

**Ask me questions anytime. The rest of this file is helpful context.**

---

## 1️⃣ Run These Commands (30 seconds)

```bash
cd ~/projects/claude-code/1
git log -1 --format="%ar | %h | %s"
git status
```

**Then say:**
```
Session initialized - [DATE]

Last commit: [X ago] ([hash])
Working tree: [clean / N files changed]

Ready to work.
```

---

## 2️⃣ The Only 3 Rules

1. **Commit every ~90 minutes** (and always before asking me questions)
2. **Work on ONE feature until it's done** (no scattered progress)
3. **If CURRENT-WORK.md exists, that's your task** (if not, ask me what to work on)

**That's it. You know enough to start.**

### 🤔 Why These Rules?

**Commit every 90min + before questions**
→ If session crashes while waiting for my response, your work is safe in git

**One feature at a time**
→ Actually finish things instead of scattered progress (cutscene 1/3, map 75%, blueprint 0%)

**Check CURRENT-WORK.md**
→ Know what you're building, don't waste time guessing or duplicating work

---

## 3️⃣ Current Project Status

**What we're building:** 3D tactical game (Fire Emblem-inspired, vertical traversal)

**What's done:**
- ✅ Movement mechanics (7/7)
- ✅ Cutscene system (Test 01 working)
- ✅ Scene geometry (river, ruins, bridge ~75%)

**What's next (Priority Order):**

**If you're unsure what to work on, pick one:**

1. **Bridge Rope Railings** (visual detail, ~2 hours)
   - Add visible rope railings along bridge sides
   - Increases bridge presence from 3% → 8% of scene
   - Status: Designed, not implemented

2. **Cutscene Test 02** (complex choreography, ~2 hours)
   - Test varied actions (diagonal, climb, wait, path crossing)
   - Validates action variety and independence
   - Status: JSON stub exists, not implemented

3. **Cutscene Acts 1-3** (story beats, ~4 hours)
   - First map narrative: crossing bridge, anomaly, zombies
   - Uses complete-scene.json (bridge + river + ruins)
   - Status: Designed in FIRST-MAP-NARRATIVE.md, not implemented

**Or just ask me:** "What should I work on?"

**See:** `docs/status/IMPLEMENTATION-STATUS.md` for full details

---

## 4️⃣ Starting New Work

**If CURRENT-WORK.md doesn't exist:**

```bash
cp CURRENT-WORK-TEMPLATE.md CURRENT-WORK.md
# Edit CURRENT-WORK.md with feature details
git add CURRENT-WORK.md
git commit -m "WIP: Define [feature name]"
```

**Then start building.**

---

## 5️⃣ While Working

**Every 90 minutes:**
```bash
git add -A
git commit -m "WIP: [what you just did]"
git push origin master
```

**Before asking me a question:**
```bash
git add -A
git commit -m "WIP: [current state]"
git push origin master
# NOW ask your question
```

**Why?** If the session crashes, your work is safe.

---

## 6️⃣ When Feature is Done

```bash
git add -A
git commit -m "[Feature Name] - Complete

[What was built]
[What was tested]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
git push origin master

# Update docs (START-HERE.md, relevant status files)
# Delete CURRENT-WORK.md
```

---

## 7️⃣ Testing Your Changes

**Start dev server:**
```bash
cd ~/projects/claude-code/1
python -m http.server -b 100.93.126.24 8080
```

**Open in browser:**
```
http://100.93.126.24:8080/                      # Main game
http://100.93.126.24:8080/?test=<test-name>     # Specific test
```

**Common tests:**
- `?test=cutscene-test-01-parallel` - Cutscene system (5 characters)
- `?test=complete-scene` - Full first map scene
- `?test=testBasicMovement` - Movement mechanics
- See `test-maps/` folder for all available tests

**Visual validation:**
- Characters should move smoothly
- Voxels should render correctly
- Console should show no errors

---

## 8️⃣ If Things Go Wrong

**Git is confused:**
```bash
git status               # See what's happening
git diff                 # See uncommitted changes
git log -3 --oneline     # See recent commits
```

**Want to save work temporarily:**
```bash
git stash                # Save changes
git stash pop            # Restore saved changes
```

**Commit failed:**
```bash
git status               # Check what went wrong
git add -A               # Stage everything
git commit -m "WIP: describe current state"
git push origin master
```

**Session crashed mid-work:**
1. Don't panic - check what was committed
2. `git log -1` - See last commit
3. `git status` - See uncommitted changes
4. Commit what you have: `git add -A && git commit -m "WIP: recovered work"`
5. Even if it's broken, commit it - you can fix it next

**Merge conflict (rare):**
```bash
git status               # See conflicted files
# Edit files, resolve conflicts
git add -A
git commit -m "Resolve merge conflict"
```

**Need to undo last commit (careful!):**
```bash
git reset --soft HEAD~1  # Undo commit, keep changes
git reset --hard HEAD~1  # Undo commit, DELETE changes (dangerous!)
```

---

## 🎯 That's It - Start Building

**Need more info?**
- Full protocol: `docs/AI-AGENT-CONDUCT.md`
- Design docs: `docs/design/`
- Session history: `docs/sessions/`

**Most important:**
- Ask me questions when unsure
- Commit often (WIP is fine!)
- Build one thing at a time

**Now go make something cool.** 🚀

---

## 🧭 Common Questions

**Q: What should I work on?**
A: Ask me! Or check `CURRENT-WORK.md` if it exists.

**Q: I broke something, what do I do?**
A: Commit it anyway (WIP), then fix it. Broken commits are fine.

**Q: Do I really need to read 1000 lines of protocol?**
A: No. This file is enough. Read the full protocol when you have questions.

**Q: What if I forget a rule?**
A: I'll remind you if needed. Just commit often and ask questions.

---

**Version:** 1.0
**For detailed protocol:** See `docs/AI-AGENT-CONDUCT.md`
**For project context:** See `START-HERE.md`

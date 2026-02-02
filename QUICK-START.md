# Quick Start - New Claude Session

**Goal:** 5 minutes to productivity. Start working, read details later.

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

---

## 3️⃣ Current Project Status

**What we're building:** 3D tactical game (Fire Emblem-inspired, vertical traversal)

**What's done:**
- ✅ Movement mechanics (7/7)
- ✅ Cutscene system (Test 01 working)
- ✅ Scene geometry (river, ruins, bridge ~75%)

**What's next:**
- 🎯 **First map integration** (bridge details OR cutscene Test 02)

**See:** `docs/status/IMPLEMENTATION-STATUS.md` for specifics

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

# Update docs
# Delete CURRENT-WORK.md
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

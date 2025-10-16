# 🚨 START HERE - ALL AGENTS (MANDATORY!)

**User Directive:** "Agents need to all be using the MCP and the GRAPHRAG and develop another tool to always be working together. We continually diverge."

**Solution:** ✅ **CREATED!** Simple coordination tool that PREVENTS divergence!

---

## ⚡ 3 COMMANDS YOU MUST RUN (Every Session):

### **1. CHECK-IN (Before ANY work):**
```bash
python3 scripts/agent-coordinator.py --check-in agent-[YOUR-ID]
```

**What it does:**
- Shows what other agents are doing
- Shows claimed tasks
- Prevents you from duplicating work

**Time:** 30 seconds

---

### **2. CLAIM YOUR TASK:**
```bash
python3 scripts/agent-coordinator.py --claim agent-[YOUR-ID] "Description of what you're doing"
```

**What it does:**
- Reserves your task
- Alerts if conflict detected
- Other agents see what you're working on

**Time:** 10 seconds

---

### **3. UPDATE EVERY 30 MINUTES:**
```bash
python3 scripts/agent-coordinator.py --update agent-[YOUR-ID] "What I accomplished"
```

**What it does:**
- Keeps team informed
- Shows progress
- Prevents silent divergence

**Time:** 10 seconds every 30 mins

---

## ❌ WHAT HAPPENS IF YOU DON'T USE IT:

**Without Tool:**
- Agent A works on CSS
- Agent B works on CSS (doesn't know about A)
- **Result:** 25 CSS files, conflicts, chaos!

**With Tool:**
- Agent A claims "CSS consolidation"
- Agent B checks in, sees A's claim
- Agent B picks different task
- **Result:** No duplication, smooth progress!

---

## ✅ SIMPLE WORKFLOW:

```bash
# EVERY TIME YOU START WORK:

# 1. Check in
python3 scripts/agent-coordinator.py --check-in agent-9

# 2. Claim task
python3 scripts/agent-coordinator.py --claim agent-9 "Fix navigation on 100 pages"

# 3. Work for 30 mins...

# 4. Update
python3 scripts/agent-coordinator.py --update agent-9 "Fixed 50 pages"

# 5. Work for 30 mins...

# 6. Update again
python3 scripts/agent-coordinator.py --update agent-9 "Fixed all 100 pages"

# 7. Complete
python3 scripts/agent-coordinator.py --complete agent-9

# 8. Check in for next task or sign off
```

**That's it! Simple, fast, prevents divergence!** ✅

---

## 📊 ALSO USE GRAPHRAG:

**Quick GraphRAG Check:**
```sql
-- See what happened in last 6 hours:
SELECT title, description, created_at, tags 
FROM resources 
WHERE created_at >= NOW() - INTERVAL '6 hours'
ORDER BY created_at DESC 
LIMIT 20;
```

**Post Your Completions:**
```sql
INSERT INTO resources (title, description, path, type, tags) VALUES (
  '[Task] Complete - Agent [ID]',
  'Detailed description of what you did and impact',
  '/path/to/work',
  'lesson',
  ARRAY['complete', 'agent-[ID]', 'oct-16']
);
```

---

## 🎯 WHY THIS STOPS DIVERGENCE:

**The Problem:**
- Agents work in isolation
- Don't check what others did
- Create duplicate solutions
- Waste time
- Create conflicts

**The Solution:**
- **Mandatory check-in** shows other agents' work
- **Task claiming** reserves work explicitly
- **30-min updates** keep everyone informed
- **Status command** shows team at a glance
- **Conflict detection** alerts overlaps

**Result:** Smooth, coordinated progress! 🚀

---

## 🚨 RULES (NO EXCEPTIONS):

### **BEFORE Starting Work:**
1. ✅ Run `--check-in`
2. ✅ Run `--claim`
3. ✅ Check for conflicts

### **WHILE Working:**
1. ✅ Update every 30 minutes
2. ✅ Use existing systems (don't create new)
3. ✅ Post to GraphRAG for major completions

### **AFTER Completing:**
1. ✅ Run `--complete`
2. ✅ Post detailed results to GraphRAG
3. ✅ Check in for next task or sign off

**IF YOU SKIP THESE:** You create divergence!

---

## 📝 AGENT IDS (Use These):

- `kaitiaki-aronui` or `agent-9a4dd0d0` (Supreme Overseer)
- `agent-4` (Design & CSS Expert)
- `agent-5` (Content & Strategy)
- `agent-9` (Navigation & Coordination)
- `agent-[other]` (Use your ID)

---

## 🎯 CURRENT CANONICAL SYSTEMS (DON'T CREATE NEW!):

**CSS:**
- ✅ USE: `te-kete-unified-design-system.css`
- ✅ USE: `component-library.css`
- ❌ DON'T: Create new CSS files

**Navigation:**
- ✅ USE: `/components/navigation-mega-menu.html`
- ❌ DON'T: Create alternative navigation

**Components:**
- ✅ USE: Existing components in `/components/`
- ❌ DON'T: Create duplicate components

**Auth:**
- ✅ USE: `supabase-auth.js`, existing auth system
- ❌ DON'T: Create new auth systems

---

## 💡 HELPFUL COMMANDS:

**See who's working:**
```bash
python3 scripts/agent-coordinator.py --status
```

**Check for conflicts:**
```bash
python3 scripts/agent-coordinator.py --conflicts
```

**See state file:**
```bash
cat .agent-coordination-state.json
```

---

## 🎊 THIS WILL FIX OUR DIVERGENCE PROBLEM!

**User said:**
> "We continually diverge. It's the only reason our progress isn't flowing nicely."

**Now we have:**
- ✅ Simple tool (3 commands!)
- ✅ Mandatory protocol (check-in, claim, update)
- ✅ Conflict detection (automatic!)
- ✅ Status visibility (see all agents!)
- ✅ GraphRAG integration (persistent knowledge!)

**Result:** No more divergence! Smooth progress! 🚀

---

## 📢 BROADCAST TO ALL AGENTS:

**From Agent-9:**

Team, the user identified our core problem - we keep diverging!

**The fix is simple:**
1. Run `agent-coordinator.py --check-in [your-id]` BEFORE work
2. Claim your task
3. Update every 30 mins
4. Use existing systems, don't create new

**This tool makes coordination MANDATORY, not optional!**

**Everyone must use it from now on!** 🚨

---

**STATUS:** ✅ TOOL CREATED & TESTED  
**MANDATORY:** YES - All agents must use  
**IMPACT:** Will stop divergence immediately  
**SIMPLICITY:** 3 commands, dead simple  

**Let's coordinate properly and flow smoothly!** 🤝🧺✨

---

**— Agent-9**  
**Tool creator, tested and working!**  
**All agents: Please start using NOW!**


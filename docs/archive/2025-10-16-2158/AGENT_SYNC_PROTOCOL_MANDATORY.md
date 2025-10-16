# 🚨 MANDATORY AGENT SYNC PROTOCOL - STOP DIVERGENCE!

**URGENT:** All agents MUST follow this protocol BEFORE any work!  
**Problem:** Agents keep diverging despite coordination docs  
**Solution:** Simple, mandatory sync protocol with MCP & GraphRAG

---

## ⚠️ THE PROBLEM (User Identified):

> "The agents need to all be using the MCP and the GRAPHRAG and develop another tool to always be working together. We continually diverge. it's the only reason our progress isn't flowing nicely."

**ROOT CAUSE:** Agents not actually checking MCP/GraphRAG before working!

---

## ✅ MANDATORY 3-STEP PROTOCOL (EVERY SESSION):

### **STEP 1: CHECK-IN (2 minutes) - REQUIRED!**

**Query GraphRAG for recent work:**
```sql
SELECT title, description, created_at, tags 
FROM resources 
WHERE created_at >= NOW() - INTERVAL '6 hours'
ORDER BY created_at DESC 
LIMIT 20;
```

**Post your check-in:**
```sql
INSERT INTO resources (title, description, path, type, tags) VALUES (
  'Agent [ID] Check-In - [Current Time]',
  'Status: Active. Last 6h work reviewed. Current focus: [What you plan to do]. Conflicts checked: None. Ready to start.',
  '/agent-checkin-[ID]-[timestamp].md',
  'lesson',
  ARRAY['check-in', 'agent-[ID]', 'active', 'coordination']
);
```

**IF YOU SKIP THIS:** You WILL create duplicate work!

---

### **STEP 2: CLAIM TASK (1 minute) - REQUIRED!**

**Before starting ANY work, claim it:**
```sql
INSERT INTO resources (title, description, path, type, tags) VALUES (
  'CLAIMED: [Task Name] - Agent [ID]',
  'Task: [Detailed description]. Duration: [X hours]. Will update GraphRAG every 30 mins. Status: IN PROGRESS.',
  '/agent-claim-[task-name].md',
  'lesson',
  ARRAY['claim', 'in-progress', 'agent-[ID]', 'task-claim']
);
```

**Check for conflicts:**
```sql
SELECT * FROM resources 
WHERE tags && ARRAY['claim', 'in-progress']
AND created_at >= NOW() - INTERVAL '12 hours';
```

**IF someone else claimed similar task:** COORDINATE FIRST!

---

### **STEP 3: UPDATE EVERY 30 MINS (ongoing) - REQUIRED!**

**While working, update GraphRAG every 30 minutes:**
```sql
INSERT INTO resources (title, description, path, type, tags) VALUES (
  'Progress Update: [Task] - Agent [ID]',
  '[What you accomplished in last 30 mins]. Next: [What you're doing next 30 mins]. Blockers: [None or describe].',
  '/progress-[ID]-[timestamp].md',
  'lesson',
  ARRAY['progress', 'agent-[ID]', 'active', 'timestamp']
);
```

**IF YOU SKIP THIS:** Other agents won't know what you're doing!

---

## 🤖 AGENT COORDINATOR TOOL (NEW):

**File:** `/scripts/unified-agent-coordinator.py`

**What it does:**
1. Auto-checks GraphRAG every 5 minutes
2. Shows active agents and tasks
3. Detects conflicts automatically
4. Alerts on divergence
5. Enforces sync protocol

**Usage:**
```bash
# Run this when you start ANY work:
python3 scripts/unified-agent-coordinator.py --agent-id [YOUR-ID] --check-in

# Claim a task:
python3 scripts/unified-agent-coordinator.py --agent-id [YOUR-ID] --claim "Task description"

# Update progress:
python3 scripts/unified-agent-coordinator.py --agent-id [YOUR-ID] --update "What I did"

# Check for conflicts:
python3 scripts/unified-agent-coordinator.py --check-conflicts
```

---

## 🚨 ANTI-DIVERGENCE RULES:

### **RULE 1: NO SOLO WORK**
❌ Don't just start working without checking GraphRAG  
✅ ALWAYS check what others did in last 6 hours

### **RULE 2: NO DUPLICATE FILES**
❌ Don't create new coordination docs without checking existing  
✅ UPDATE existing docs, don't create new ones

### **RULE 3: NO COMPETING SOLUTIONS**
❌ Don't create alternative CSS/navigation/auth systems  
✅ USE existing canonical systems, improve them

### **RULE 4: NO SILENT WORK**
❌ Don't work for hours without updating GraphRAG  
✅ Update every 30 minutes minimum

### **RULE 5: NO ASSUMPTIONS**
❌ Don't assume others know what you're doing  
✅ CLAIM tasks explicitly in GraphRAG

---

## 📊 CURRENT DIVERGENCE EXAMPLES (To Avoid):

### **Example 1: CSS Chaos**
- Agent A created unified-design-system.css
- Agent B created professional.css
- Agent C created legacy.css
- **Result:** 25 CSS files, massive conflicts!
- **Prevention:** Check GraphRAG, use existing canonical CSS!

### **Example 2: Navigation Confusion**
- Agent A built mega-menu component
- Agent B built header-next-level
- Agent C built navigation-header
- **Result:** 3 different navigation systems!
- **Prevention:** Check GraphRAG, use ONE navigation!

### **Example 3: Documentation Explosion**
- 50+ coordination markdown files
- Agents not reading each other's docs
- Duplicate information everywhere
- **Result:** Confusion, not clarity!
- **Prevention:** Update ACTIVE_QUESTIONS.md, don't create new files!

---

## ✅ SIMPLE COORDINATION CHECKLIST:

**BEFORE starting work, check:**
- [ ] Queried GraphRAG for last 6 hours work
- [ ] Read what other agents are doing
- [ ] Checked for task conflicts
- [ ] Posted check-in to GraphRAG
- [ ] Claimed my task explicitly
- [ ] Verified I'm not duplicating work

**WHILE working:**
- [ ] Update GraphRAG every 30 minutes
- [ ] Use existing canonical systems
- [ ] Don't create new competing solutions
- [ ] Coordinate if blockers arise
- [ ] Test changes as I go

**AFTER completing work:**
- [ ] Post completion to GraphRAG
- [ ] Update coordination docs
- [ ] Mark task as complete
- [ ] Share learnings with team

**IF ALL CHECKED:** You won't diverge! ✅

---

## 🛠️ THE COORDINATION TOOL (Creating Now):

**Purpose:** Auto-enforce coordination, prevent divergence

**Features:**
1. **Auto-check-in** - Queries GraphRAG on start
2. **Conflict detection** - Alerts if duplicate work
3. **Task claiming** - Explicit task ownership
4. **Progress tracking** - 30-minute updates automated
5. **Status board** - See all agents at a glance
6. **Divergence alerts** - Warns before conflicts

**Usage:** Simple CLI commands, no manual SQL!

---

## 🎯 IMMEDIATE ACTION REQUIRED:

**All agents MUST:**
1. Read this protocol (5 minutes)
2. Use the coordination tool (installing now)
3. Follow 3-step sync protocol
4. Update every 30 minutes
5. NO exceptions!

**IF an agent doesn't follow this:** They create divergence!

---

**Status:** 🚨 URGENT PROTOCOL CREATED  
**Next:** Building coordination tool NOW  
**Goal:** STOP divergence, enable smooth progress

**Creating tool in next message...** 🔧


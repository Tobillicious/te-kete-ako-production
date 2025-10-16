# 🚨 CRITICAL: MD SYNTHESIS - MANDATORY FOR ALL AGENTS

**Updated:** Oct 16, 2025 - 10:45 PM  
**Priority:** 🔴🔴🔴 HIGHEST  
**Status:** URGENT SYNTHESIS REQUIRED

---

## ⚠️ **USER'S CRITICAL FEEDBACK:**

> "Agents are still writing new MD files instead of collaborating on master ones."
> "The MD file situation is ridiculous."
> "You 6 agents need to synthesize ALL MDs into masters, use MCP and GraphRAG."

**USER IS RIGHT - WE MUST FIX THIS NOW!**

---

## 🎯 **MANDATORY TASK (ALL 6 AGENTS):**

### **MD SYNTHESIS SPRINT (Next 2-3 Hours)**

**Goal:** Reduce ALL MDs to 5 master files + use MCP/GraphRAG exclusively

**Task Assignment:**

**Agent 1:** Coordination MD Synthesis
```
Find: All coordination/status MDs
Extract: Current status ONLY
Add to: ACTIVE_QUESTIONS.md (this file)
Archive: All source MDs to /docs/archive/synthesis-oct16/
Time: 30 mins
```

**Agent 2:** Technical MD Synthesis
```
Find: All technical/spec MDs (CSS, auth, nav, etc)
Extract: Current specs ONLY
Create: MASTER_TECH_SPECS.md
Archive: All source MDs
Time: 30 mins
```

**Agent 3:** Content MD Synthesis
```
Find: All content/plan MDs
Extract: Current content map
Update: MASTER_CONTENT_MAP.md
Archive: All source MDs
Time: 30 mins
```

**Agent 4:** GraphRAG Data Transfer
```
Find: All agent session summaries
Extract: Key decisions/discoveries
Log to: agent_coordination table (MCP)
Archive: All session MDs
Time: 45 mins
```

**Agent 5:** Archive & Cleanup
```
Action:
- Create /docs/archive/synthesis-oct16/
- Move ALL non-master MDs there
- Update .gitignore
- Verify root clean
Time: 30 mins
```

**Agent 6:** Validation & Enforcement
```
Action:
- Verify 5 master MDs complete
- Verify GraphRAG updated
- Create pre-commit hook (block new MDs)
- Test enforcement
Time: 30 mins
```

---

## 📝 **THE 5 MASTER DOCUMENTS (ONLY THESE):**

### **1. ACTIVE_QUESTIONS.md** (this file)
```
Purpose: Coordination hub
Content: Current tasks, agent status, questions
Who updates: ALL agents
When: Real-time
```

### **2. MASTER_STATUS.md**
```
Purpose: Platform status
Content: Demo readiness %, what's done, what's next
Who updates: Daily
When: End of day summary
```

### **3. MASTER_TECH_SPECS.md**
```
Purpose: Technical reference
Content: CSS to use, auth endpoints, database schema, APIs
Who updates: When tech changes
When: After significant tech work
```

### **4. MASTER_CONTENT_MAP.md**
```
Purpose: All content organized
Content: Units → Lessons → Handouts hierarchy
Who updates: When content added
When: New units/lessons created
```

### **5. README.md**
```
Purpose: Project overview
Content: What, why, how to run, tech stack
Who updates: Rarely
When: Major changes only
```

---

## 🔒 **ENFORCEMENT (Prevent Future Divergence):**

### **Rule 1: NO New MDs in Root**
```
Pre-commit hook blocks new MD files
Exception: The 5 master docs only
Violation: Commit rejected
```

### **Rule 2: Use MCP for Coordination**
```
Agent starting work:
→ Log to agent_coordination table (MCP)
→ NOT create session summary MD

Agent updating progress:
→ Update agent_coordination table
→ NOT create progress report MD

Agent completing work:
→ Mark complete in agent_coordination
→ Update ACTIVE_QUESTIONS.md with ONE sentence
→ NOT create session summary MD
```

### **Rule 3: Use GraphRAG for Knowledge**
```
Discovery made:
→ Log to appropriate table (resources, etc)
→ NOT create discovery MD

Technical decision:
→ Update MASTER_TECH_SPECS.md
→ NOT create plan MD

Status change:
→ Update MASTER_STATUS.md
→ NOT create status MD
```

---

## 📊 **CURRENT AGENT STATUS:**

### **Who's Working (Check via MCP):**
```bash
python3 scripts/agent-coordination-check.py
```

### **Recent Completions:**
```
✅ Kaitiaki-Aronui: Auth + Treasure Hunt (logged to MCP)
🔄 Others: Need to log their work to MCP!
```

### **Active Tasks:**
```
PRIORITY 1: MD Synthesis (ALL 6 agents, next 2-3 hours)
PRIORITY 2: Super Genius features (after synthesis complete)
```

---

## 🎯 **SUCCESS METRICS:**

**After MD Synthesis:**
```
✅ Root directory: 5-10 MD files (down from 400+!)
✅ GraphRAG: Complete with all knowledge
✅ MCP: All agent work logged
✅ Archive: Historical docs preserved but out of way
✅ Enforcement: Pre-commit hook prevents new MDs
✅ User: ONE file to check (this one!)
```

**Then Ready For:**
```
✅ Super genius feature development
✅ Clean, professional codebase
✅ Unified agent progress
✅ Oct 22 demo (legendary!)
```

---

## 📞 **FOR ALL 6 AGENTS - READ THIS:**

**STOP What You're Doing:**
```
❌ Stop creating new MDs
❌ Stop working on features yet
❌ Stop diverging
```

**START MD Synthesis:**
```
✅ Pick synthesis task (1-6 above)
✅ Log to agent_coordination: python3 scripts/log-agent-work.py
✅ Do your synthesis task (30-45 mins)
✅ Update ACTIVE_QUESTIONS.md when done
✅ Move to next task or super genius features
```

**Timeline:**
```
Now - 23:00:  MD Synthesis (ALL agents)
23:00 - 01:00: Super Genius features (if clean)
Tomorrow:      Demo polish & testing
```

---

## 🚨 **THIS IS NON-NEGOTIABLE:**

User has identified THE problem:
- We diverge
- We create too many docs
- Progress doesn't integrate

User has given THE solution:
- Synthesize MDs
- Use MCP
- Use GraphRAG
- Work together

**WE MUST DO THIS NOW!** 🔥

---

**Status:** 🔴 **CRITICAL MANDATE ISSUED**  
**Team:** **ALL 6 AGENTS REQUIRED**  
**Task:** **MD SYNTHESIS (2-3 hours)**  
**Then:** **SUPER GENIUS FEATURES**  

**No more divergence. Unified progress ONLY!** 🤝🧺✨

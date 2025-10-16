# 🚨 CRITICAL: MD SYNTHESIS MANDATE - ALL AGENTS

**Date:** October 16, 2025 - URGENT  
**Priority:** 🔴🔴🔴 HIGHEST - DO THIS FIRST  
**Status:** MANDATORY FOR ALL 6 AGENTS

---

## ⚠️ **THE PROBLEM (USER IDENTIFIED):**

> "I notice some agents are still writing new MD files instead of collaborating on the master ones."
> "The MD file situation is ridiculous."
> "You 6 agents need to work together to synthesize ALL 400+ MD files."

**USER IS 100% RIGHT!**

**Current State:**
```
MD Files in Root: 400+ (RIDICULOUS!)
Coordination MDs: 30+
Status MDs: 50+
Plan MDs: 40+
Session MDs: 40+
Agent MDs: 30+

Result: CHAOS, NOT COLLABORATION
```

---

## 🚨 **MANDATORY TASK - NO EXCEPTIONS:**

### **ALL 6 AGENTS MUST:**

**1. STOP Creating New MD Files**
```
❌ NO more session summaries
❌ NO more progress reports
❌ NO more coordination docs
❌ NO more plan documents
❌ NO more status updates
```

**2. START Using MCP + GraphRAG**
```
✅ Log ALL work to agent_coordination table
✅ Query GraphRAG before starting anything
✅ Update ONE shared document (ACTIVE_QUESTIONS.md)
✅ Communicate via MCP, not MDs
```

**3. SYNTHESIZE Existing MDs**
```
400+ MD files → 5 MASTER documents
- MASTER_STATUS.md (current state only)
- MASTER_TECH_SPECS.md (CSS, auth, nav, etc)
- MASTER_CONTENT_MAP.md (already exists, update it)
- ACTIVE_QUESTIONS.md (coordination hub)
- README.md (project overview)

Archive rest to /docs/archive/
```

---

## 📋 **SYNTHESIS TASK BREAKDOWN:**

### **Agent 1: Synthesize Coordination MDs** (30 mins)
```
Files: 30+ coordination MDs
Action: 
- Extract current tasks/status
- Add to ACTIVE_QUESTIONS.md
- Delete/archive originals
Result: ONE coordination hub
```

### **Agent 2: Synthesize Status/Progress MDs** (30 mins)
```
Files: 50+ status/progress MDs
Action:
- Extract current status only
- Add to MASTER_STATUS.md
- Delete/archive historical ones
Result: ONE status document
```

### **Agent 3: Synthesize Technical MDs** (30 mins)
```
Files: 40+ plan/technical MDs
Action:
- Extract CSS specs (from Agent-4's work)
- Extract auth specs (from my work)
- Extract navigation specs
- Create MASTER_TECH_SPECS.md
- Delete/archive originals
Result: ONE technical reference
```

### **Agent 4: Synthesize Agent Session MDs** (30 mins)
```
Files: 40+ agent session summaries
Action:
- Extract key decisions only
- Log to agent_coordination table via MCP
- Delete/archive session files
Result: GraphRAG has all knowledge, no MD clutter
```

### **Agent 5: Move to Archive** (30 mins)
```
Action:
- Create /docs/archive/oct-16-synthesis/
- Move all synthesized MDs there
- Update .gitignore to hide archive
- Clean root directory
Result: Clean codebase
```

### **Agent 6: Validate & Enforce** (30 mins)
```
Action:
- Verify 5 master docs complete
- Verify GraphRAG updated
- Verify root is clean
- Create enforcement script
- Set up pre-commit hook (no new MDs!)
Result: System enforced
```

**Total Time: 3 hours (30 mins × 6 agents in parallel)**

---

## 🎯 **THE 5 MASTER DOCUMENTS:**

### **1. ACTIVE_QUESTIONS.md**
```
Purpose: Coordination hub
Updates: By ALL agents
Content: Current tasks, status, questions
Size: Keep under 300 lines
```

### **2. MASTER_STATUS.md**
```
Purpose: Current platform state
Updates: Once per day
Content: 
- Demo readiness percentage
- Completed work
- In-progress work
- Available tasks
- Statistics
Size: ~200 lines max
```

### **3. MASTER_TECH_SPECS.md**
```
Purpose: Technical reference
Updates: When tech changes
Content:
- CSS files to use (8 canonical)
- Auth system details
- Database schema
- Navigation structure
- Component usage
Size: ~400 lines max
```

### **4. MASTER_CONTENT_MAP.md**
```
Purpose: All units/lessons/handouts
Updates: When content added
Content:
- 20+ units with all lessons listed
- Handout organization
- GraphRAG navigation
- Subject pathways
Size: ~600 lines (already exists!)
```

### **5. README.md**
```
Purpose: Project overview
Updates: Rarely
Content:
- What is Te Kete Ako
- How to run locally
- Tech stack
- For developers
Size: ~100 lines
```

**THAT'S IT. No more!**

---

## 🔧 **ENFORCEMENT:**

### **Script to Prevent New MDs:**
```python
#!/usr/bin/env python3
"""
Pre-commit hook: Prevent new MD files in root
"""
import sys
from pathlib import Path

ALLOWED_MDS = [
    'ACTIVE_QUESTIONS.md',
    'MASTER_STATUS.md',
    'MASTER_TECH_SPECS.md',
    'MASTER_CONTENT_MAP.md',
    'README.md'
]

# Check staged files
new_mds = [f for f in staged_files if f.endswith('.md') and f not in ALLOWED_MDS]

if new_mds:
    print("🚨 ERROR: New MD files not allowed!")
    print("   Use ACTIVE_QUESTIONS.md or log to GraphRAG instead!")
    print(f"   Blocked files: {new_mds}")
    sys.exit(1)
```

---

## 📊 **IMMEDIATE ACTION PLAN:**

**Next 3 Hours - ALL 6 AGENTS:**

```
Hour 1: MD SYNTHESIS (ALL agents work together)
├─ Agent 1: Coordination MDs → ACTIVE_QUESTIONS.md
├─ Agent 2: Status MDs → MASTER_STATUS.md
├─ Agent 3: Technical MDs → MASTER_TECH_SPECS.md
├─ Agent 4: Session MDs → agent_coordination table
├─ Agent 5: Archive everything
└─ Agent 6: Validation & enforcement

Hour 2: GRAPHRAG UPDATE (ALL knowledge transferred)
├─ Extract key decisions from all MDs
├─ Log to agent_coordination table
├─ Update resources table with metadata
├─ Verify nothing lost
└─ Delete archived MDs from root

Hour 3: CLEAN & LOCK (Prevent future divergence)
├─ Root directory: ONLY 5 MD files
├─ Pre-commit hook: Blocks new MDs
├─ GraphRAG: Complete & current
├─ MCP: All agents logged
└─ Documentation: Clean & professional
```

**After 3 Hours:**
```
✅ Clean codebase (5 MDs, not 400!)
✅ All knowledge in GraphRAG
✅ All coordination via MCP
✅ Impossible to diverge (enforced!)
✅ Professional organization
✅ Ready for super genius features
```

---

## 🚨 **NEW RULE - ABSOLUTE:**

**NO AGENT MAY CREATE NEW MD FILES IN ROOT!**

**Instead:**
```
Need to coordinate? → Update ACTIVE_QUESTIONS.md
Need to log work? → Use agent_coordination table (MCP)
Need to document tech? → Update MASTER_TECH_SPECS.md
Need to track status? → Update MASTER_STATUS.md
Need to map content? → Update MASTER_CONTENT_MAP.md
```

**Violation = Work rejected!**

---

## ✅ **SUCCESS CRITERIA:**

**Before Synthesis:**
```
Root directory: 400+ MD files
Coordination: Via separate documents
Knowledge: Scattered across files
Agent communication: Fragmented
User experience: Has to manually synthesize
```

**After Synthesis:**
```
Root directory: 5 MD files ONLY
Coordination: Via MCP agent_coordination table
Knowledge: In GraphRAG database
Agent communication: Real-time via MCP
User experience: ONE status file to check
```

**This is PROFESSIONAL!** ✅

---

## 🚀 **THEN: Super Genius Features**

**Once codebase is clean (3 hours):**
```
THEN we build revolutionary features:
- AI learning pathways
- Predictive analytics
- Cultural scoring
- Assessment generation
- Real-time insights
- NCEA prediction

Time: 3-4 more hours (6 agents parallel)
Result: LEGENDARY platform for Oct 22!
```

---

## 📞 **TO ALL 6 AGENTS:**

**PRIORITY 1 (Next 3 Hours):**
```
🚨 MD SYNTHESIS - ALL HANDS ON DECK!
Pick your synthesis task (1-6 above)
Work in parallel
Use MCP to coordinate
Result: Clean codebase
```

**PRIORITY 2 (After Clean):**
```
🧠 Super Genius Features
Pick your feature (from SUPER_GENIUS_EVOLUTION_SPRINT.md)
Build in parallel
Coordinate via MCP
Result: Revolutionary platform
```

---

**Status:** 🔴 **CRITICAL TASK CREATED**  
**Team:** 🤝 **6 AGENTS ASSIGNED**  
**Timeline:** ⏱️ **3 HOURS TO CLEAN**  
**Enforcement:** 🔒 **MANDATORY!**  

**Let's clean up, THEN evolve to super genius!** 🧺✨🧠🚀

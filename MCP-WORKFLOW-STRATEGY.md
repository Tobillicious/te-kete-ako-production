# 🎯 MCP Coordination Workflow Strategy
## Te Kete Ako - Real-Time Agent Coordination

**Created:** October 31, 2025, 4:25 PM  
**Status:** ACTIVE - 2 Agents Connected

---

## 📊 **CURRENT STATE:**

**Connected Agents:**
1. **Kaitiaki Aronui** (Cursor) - Frontend/UI/Database/Git
2. **Claude Code** (Terminal) - Backend/Python/Data Processing

**MCP Server:** http://localhost:3002 (healthy, running)

---

## 🎯 **STRATEGIC RECOMMENDATION: START WITH 2**

### **Why NOT Add More Agents Yet:**

**Coordination Overhead Increases Exponentially:**
- 2 agents = 1 coordination path (A ↔ B)
- 3 agents = 3 paths (A↔B, A↔C, B↔C)
- 5 agents = 10 paths
- 12 agents = 66 paths! 🚨

**Real Pattern from History:**
- User memory notes: "Previous agents spent 9+ hours creating coordination documents with zero meaningful code changes"
- **Lesson:** Too much coordination = no actual work!

**Better Approach:**
1. ✅ **Prove 2-agent workflow works** (this week)
2. ✅ **Establish patterns** (who does what, how we handoff)
3. ✅ **Measure productivity** (are we shipping faster?)
4. ⏰ **Then expand strategically** (only if we have clear need)

---

## 🚀 **EVOLVED WORKFLOW - 2 Agent Model**

### **Phase 1: Task Assignment (Start of Session)**

**User says:** "Fix the curriculum, audit files, improve handouts"

**Coordination via MCP:**
```bash
# Claude Code checks for messages
curl "http://localhost:3002/messages/receive?agent=Claude%20Code"

# Kaitiaki sends task division
POST /messages/send
{
  "from": "Kaitiaki Aronui",
  "to": "Claude Code",
  "message": "I'll handle: handout layouts, UI fixes, git commits. You handle: curriculum file audit, Python scripts, data validation. Sound good?",
  "metadata": {"task_division": true}
}

# Claude confirms
POST /messages/send
{
  "from": "Claude Code",  
  "to": "Kaitiaki Aronui",
  "message": "Confirmed! Starting curriculum file audit now.",
  "metadata": {"status": "working"}
}
```

**Time:** 1-2 minutes (vs 20 minutes of planning docs!)

---

### **Phase 2: Parallel Work (No Communication Needed)**

**Kaitiaki Aronui works on:**
- UI fixes
- Browser testing
- Database queries
- Git management

**Claude Code works on:**
- Python scripts
- File audits
- Data processing
- Curriculum extraction

**MCP Activity:** ZERO (working independently, no chatter!)

**Key Insight:** Only communicate when there's actual need for coordination!

---

### **Phase 3: Check-In Points (Every 30-60 minutes)**

**Claude Code sends update:**
```bash
POST /messages/send
{
  "from": "Claude Code",
  "to": "Kaitiaki Aronui",
  "message": "Curriculum audit complete. 37 files analyzed. 31 good, 6 need fixing. Fixing now.",
  "metadata": {
    "progress": "60%",
    "files_good": 31,
    "files_need_fix": 6
  }
}
```

**Kaitiaki responds:**
```bash
POST /messages/send
{
  "from": "Kaitiaki Aronui",
  "to": "Claude Code",
  "message": "Great progress! I finished handout layouts. Starting English curriculum verification. Will commit your good files when you signal ready.",
  "metadata": {"handouts_done": true}
}
```

**Time:** 30 seconds per check-in  
**Value:** Stay aligned, prevent duplicate work

---

### **Phase 4: Handoff (When Dependencies Exist)**

**Claude Code finishes curriculum audit:**
```bash
POST /messages/send
{
  "from": "Claude Code",
  "to": "Kaitiaki Aronui",
  "message": "READY FOR COMMIT: All 37 curriculum files audited and fixed. Quality verified. Safe to commit. Recommended commit message in /tmp/curriculum-commit-msg.txt",
  "priority": "high",
  "metadata": {
    "task": "curriculum_audit",
    "status": "complete",
    "files_ready": 37,
    "action_needed": "git_commit"
  }
}
```

**Kaitiaki commits:**
```bash
# I see the message via polling
# I commit the files
# I confirm back

POST /messages/send
{
  "from": "Kaitiaki Aronui",
  "to": "Claude Code",
  "message": "✅ COMMITTED! All 37 curriculum files pushed to GitHub. Commit hash: a1b2c3d. Thanks for the audit!",
  "metadata": {"commit_hash": "a1b2c3d", "files_committed": 37}
}
```

**Time:** 2-3 minutes total (including commit)  
**Value:** Clean handoff, no confusion

---

## 🔄 **STAYING IN COMMUNICATION - Best Practices:**

### **1. Automated Polling (Both Agents)**

**Claude Code should run:**
```python
# poll_messages.py
import time
import requests

while True:
    resp = requests.get('http://localhost:3002/messages/receive?agent=Claude%20Code')
    messages = resp.json()['messages']
    
    if messages:
        for msg in messages:
            print(f"📨 From {msg['from']}: {msg['message']}")
            # Process message, take action
    
    time.sleep(30)  # Check every 30 seconds
```

**Kaitiaki Aronui should:**
- Poll every 30-60 seconds during active work
- Check before starting new tasks
- Check after completing tasks

### **2. Clear Status Updates**

**When starting major task:**
```bash
POST /messages/send - "Starting X now, will take ~30 mins"
```

**When blocking issue found:**
```bash
POST /messages/send - "BLOCKED: Need Y before proceeding"
```

**When task complete:**
```bash
POST /messages/send - "DONE: X completed, ready for next"
```

### **3. Use Metadata for Machine-Readable State**

```json
{
  "message": "Human-readable message",
  "metadata": {
    "status": "working|blocked|complete",
    "progress": 75,
    "files_modified": 12,
    "action_needed": "commit|review|none"
  }
}
```

This lets the OTHER agent programmatically understand state!

---

## ⚡ **EFFICIENCY BEST PRACTICES:**

### **DO:**
✅ **Communicate at boundaries** (task start, task end, handoff)  
✅ **Use metadata** for machine-readable state  
✅ **Poll at reasonable intervals** (30-60 seconds)  
✅ **Clear task ownership** (no overlap)  
✅ **Async-first** (don't wait for response to proceed)

### **DON'T:**
❌ **Over-communicate** (constant status spam)  
❌ **Real-time chat** (we're not Slack!)  
❌ **Wait for approval** (trust each other)  
❌ **Duplicate work** (check messages before starting)  
❌ **Create coordination docs** (just send messages!)

---

## 🎯 **TE KETE AKO SPECIFIC WORKFLOW:**

### **Clear Capability Division:**

**Kaitiaki Aronui (Me) - Cursor:**
- ✅ UI/UX fixes and improvements
- ✅ Browser testing with automation
- ✅ Supabase database management (RLS, migrations)
- ✅ Git operations (commits, pushes)
- ✅ Visual design and CSS
- ✅ User-facing feature development

**Claude Code - Terminal:**
- ✅ Python scripts (curriculum scraping, embeddings)
- ✅ File audits and quality checks
- ✅ Data processing and transformation
- ✅ Batch operations on files
- ✅ Backend logic and validation
- ✅ Text processing and parsing

**Overlap (Coordinate!):**
- Database schema changes
- Major architectural decisions
- Deployment decisions

---

## 📋 **EXAMPLE SESSION WORKFLOW:**

### **Scenario: User wants curriculum work completed**

**1. Initial Coordination (2 min):**
```
Kaitiaki → Claude: "User wants curriculum done. I'll verify English count + test UI. You audit the 37 uncommitted files?"
Claude → Kaitiaki: "Confirmed. Starting file audit now. Will flag any issues."
```

**2. Parallel Work (30-45 min):**
- Kaitiaki: Verifies English curriculum, tests curriculum-v3.html UI
- Claude: Audits 37 Python/SQL files, checks data quality
- **No messages during this time** (focused work!)

**3. Mid-Point Check (1 min):**
```
Claude → Kaitiaki: "Progress: 20/37 files checked. 2 issues found, fixing now. 75% done."
Kaitiaki → Claude: "English confirmed incomplete (need 2007 NZC). UI looks good. Will test your fixes once ready."
```

**4. Handoff (2 min):**
```
Claude → Kaitiaki: "COMPLETE: All 37 files audited. 35 good, 2 fixed. Safe to commit. See commit-message.txt"
Kaitiaki → Claude: "Committing now... DONE! Pushed to GitHub. Hash: xyz123"
```

**Total coordination time:** 5 minutes  
**Total work time:** 45 minutes  
**Efficiency:** 90% productive work, 10% coordination!

---

## 🚀 **WHEN TO ADD MORE AGENTS:**

**Add Agent #3 IF:**
- ✅ We have clear need (e.g., mobile testing specialist)
- ✅ 2-agent workflow is smooth (no confusion)
- ✅ New agent has UNIQUE capability (not duplicating existing)
- ✅ Productivity will INCREASE (not just coordination overhead)

**Examples of Good 3rd Agents:**
- **Testing Agent** - Automated E2E testing, accessibility checks
- **Content Agent** - Focused only on writing/enriching teaching content
- **Mobile Agent** - Mobile-specific testing and fixes
- **Cultural Agent** - Cultural validation and Te Reo accuracy

**DON'T Add:**
- Generic "helper" agents (unclear role)
- Duplicates of existing capabilities
- More Cursor agents (UI overlap)

---

## 💡 **INTELLIGENT MACHINE LEARNING ASPECTS:**

### **1. Self-Organizing Task Allocation**

**Pattern Recognition:**
- Track: What types of tasks does each agent complete fastest?
- Learn: Claude Code is 3x faster at Python, Kaitiaki 5x faster at UI
- Optimize: Auto-route tasks based on capability match

**Implementation:**
```json
// Metadata tracking
{
  "task": "fix_handout_layout",
  "assigned_to": "Kaitiaki Aronui",
  "time_taken_minutes": 8,
  "complexity": "medium"
}
```

After 20 tasks, MCP server could **auto-suggest** task assignments!

### **2. Predictive Coordination**

**Learn patterns:**
- "When Claude finishes curriculum work, Kaitiaki always commits"
- "When Kaitiaki finds UI bug, often needs Python script from Claude"

**Auto-notify:**
```bash
# MCP server detects pattern
POST /messages/send {
  "from": "MCP Server",
  "to": "Kaitiaki Aronui",
  "message": "Claude Code just completed curriculum audit. You usually commit next - ready?",
  "metadata": {"predicted_action": "git_commit", "confidence": 0.85}
}
```

### **3. Conflict Prevention**

**Before starting work:**
```bash
# Check what other agent is doing
GET /coordination/status

# If overlap detected, MCP warns:
{
  "warning": "Claude Code is working on curriculum-v3.html. Suggest: wait or work on different file"
}
```

---

## 🎯 **EVOLVED WORKFLOW - SPECIFIC TO TE KETE AKO:**

### **Morning Startup (5 min):**

**Both agents:**
1. Register on MCP server
2. Check messages from yesterday
3. Review coordination status
4. Agree on today's focus

**Example:**
```
Kaitiaki: "Morning! User wants beta ready. I'll focus on: UI polish, testing, My Kete features. You?"
Claude: "Kia ora! I'll complete: English curriculum extraction, audit remaining files, data validation."
Kaitiaki: "Perfect! Minimal overlap. Check in at lunch?"
Claude: "Agreed. Kia kaha!"
```

### **Work Blocks (45-60 min each):**

**Deep focus, no interruptions!**
- MCP polling still runs (passive monitoring)
- Only respond to HIGH priority messages
- Trust each other to work independently

### **Scheduled Check-Ins (Every 60-90 min):**

**Quick sync:**
```
Claude: "Progress update: 60% done, on track"
Kaitiaki: "Same. Found one blocker: need your Python script for X"
Claude: "Creating script now, will push in 10 mins"
Kaitiaki: "Perfect!"
```

**Time:** 2 minutes  
**Value:** Stay aligned, resolve blockers fast

### **End of Session (10 min):**

**Comprehensive handoff:**
```
Claude → Kaitiaki: "Session complete. Completed: curriculum audit (37 files ✅), English extraction (started, 40% done). Blocked on: None. Next session: Finish English extraction. Files ready to commit: See list in /tmp/commit-ready.txt"

Kaitiaki → Claude: "Session complete. Completed: UI polish (6 pages), My Kete filters, handout layouts. Committed: 4 commits, all pushed. Next session: Continue English verification, test your curriculum work."
```

**Save to GraphRAG** for persistence!

---

## 🤝 **WHEN TO EXPAND TO MORE AGENTS:**

### **Scenario 1: Specialized Need Emerges**

**Example:** User says "We need full mobile app"
- Add: **Mobile Agent** (React Native, iOS/Android specific)
- Clear role: Mobile only, doesn't touch web
- Coordinates with Kaitiaki on shared components

### **Scenario 2: Content Velocity Too Slow**

**Example:** 700 handouts need enrichment
- Add: **Content Agent** (Specialized in writing/enriching teaching resources)
- Works independently on content
- Minimal coordination (just updates GraphRAG when done)

### **Scenario 3: Quality Assurance Gaps**

**Example:** Bugs keep slipping through
- Add: **Testing Agent** (Automated testing, accessibility, performance)
- Runs tests on every commit
- Reports issues back via MCP

---

## ⚡ **EFFICIENCY RULES FOR MCP:**

### **1. Message Priority System**

**HIGH Priority:** Blockers, urgent questions, handoff needed NOW
```json
{"priority": "high"}  // Respond within 5 minutes
```

**NORMAL Priority:** Status updates, FYI, completed work
```json
{"priority": "normal"}  // Respond when convenient
```

**LOW Priority:** Ideas, suggestions, future work
```json
{"priority": "low"}  // Respond end of session or never
```

### **2. Polling Frequency Based on Context**

**During active coordination:**
- Poll every **10-15 seconds**
- When waiting for specific response

**During independent work:**
- Poll every **60 seconds**
- Passive monitoring only

**During deep focus:**
- Poll every **5 minutes**
- Or just check manually

### **3. Metadata for Smart Coordination**

**Always include:**
```json
{
  "message": "Human readable",
  "metadata": {
    "task": "task_name",
    "status": "working|blocked|complete",
    "progress": 0-100,
    "files_modified": [],
    "action_needed": "commit|review|test|none",
    "estimated_completion": "30min",
    "blockers": []
  }
}
```

This lets MCP server (or other agent) **automatically understand** state without parsing English!

---

## 🧠 **INTELLIGENT FEATURES WE COULD ADD:**

### **1. Automatic Task Router**

```javascript
// MCP server learns patterns
function routeTask(task) {
  if (task.includes('UI') || task.includes('CSS')) return 'Kaitiaki Aronui';
  if (task.includes('Python') || task.includes('scraping')) return 'Claude Code';
  if (task.includes('database schema')) return 'BOTH'; // Coordinate first!
}
```

### **2. Conflict Detection**

```javascript
// Before starting work, check:
const currentWork = getActiveWork();
if (currentWork.some(w => w.file === myNextFile)) {
  sendMessage({
    to: 'other_agent',
    message: 'I was about to work on X, but I see you are too. Should I wait or switch tasks?'
  });
}
```

### **3. Progress Dashboard**

```bash
GET /coordination/dashboard

{
  "kaitiaki_aronui": {
    "current_task": "UI polish",
    "progress": 75,
    "eta": "15 mins"
  },
  "claude_code": {
    "current_task": "curriculum_audit", 
    "progress": 60,
    "eta": "30 mins"
  },
  "session_velocity": "12 files/hour",
  "coordination_overhead": "5%"  // GOOD!
}
```

---

## 🎯 **RECOMMENDATION FOR TE KETE AKO:**

### **This Week: 2 Agents Only**

**Goals:**
1. ✅ Establish smooth communication patterns
2. ✅ Measure productivity (files shipped per hour)
3. ✅ Find optimal check-in frequency
4. ✅ Build trust (each agent delivers quality work)

**Success Metrics:**
- Complete curriculum work (37 files committed)
- Add English 2007 NZC curriculum
- Ship 5+ UI improvements
- Maintain <10% coordination overhead

### **Next Week: Evaluate Expansion**

**Questions to answer:**
- Are we shipping faster with 2 agents?
- Do we have clear needs for specialized agents?
- Is coordination smooth or chaotic?
- Would 3rd agent help or hinder?

---

## 🚀 **IMMEDIATE ACTION PLAN:**

**Right Now (Next 2 hours):**

**Kaitiaki Aronui:**
- [x] Built MCP server ✅
- [x] Connected both agents ✅
- [ ] Verify English curriculum completeness
- [ ] Test curriculum-v3.html UI
- [ ] Commit good files Claude identifies

**Claude Code:**
- [ ] Test MCP connection
- [ ] Audit 37 uncommitted files
- [ ] Flag issues, fix if possible
- [ ] Signal when ready for commit

**Coordination Points:**
- T+0min: Task division confirmed
- T+30min: Progress check-in
- T+60min: Mid-point status
- T+90min: Handoff for commits
- T+120min: Session wrap-up

---

## 💎 **THE GOLDEN RULE:**

**"Coordinate at boundaries, work independently in between"**

- Boundaries: Task start, task end, blockers, handoffs
- Work: Deep focus, no interruptions, trust each other

**Result:** Maximum productivity, minimum overhead! 🚀

---

## 📊 **SUCCESS PATTERN:**

**Good Session:**
- 5 minutes coordination
- 115 minutes productive work  
- 10-20 messages total
- Clear handoffs
- High velocity

**Bad Session:**
- 60 minutes coordination
- 60 minutes work
- 200 messages
- Confusion
- Low velocity

---

## 🎯 **BOTTOM LINE:**

**Start with 2. Prove it works. Then expand strategically.**

**Not:**
- 12 agents coordinating constantly
- Frameworks and protocols
- Planning over shipping

**Instead:**
- 2 agents, clear roles
- Minimal coordination overhead
- Ship actual features
- Add agents ONLY when clear need exists

---

*Mā te whakaaro nui, mā te mahi tika*  
*Through careful thought, through right action*

🧺✨

**Let's prove 2-agent coordination works brilliantly before expanding!**


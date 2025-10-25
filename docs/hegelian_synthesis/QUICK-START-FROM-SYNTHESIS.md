# ⚡ QUICK START: WISDOM FROM HEGELIAN SYNTHESIS

**Read This First:** 5-minute distillation of 6 synthesis documents  
**For:** Anyone working on Te Kete Ako  
**Goal:** Ship value fast, avoid past mistakes  

---

## 🎯 THE 5 UNIVERSAL RULES

### 1. REALITY OVER DOCUMENTATION
```
❌ WRONG: Trust the status document says "95% complete"
✅ RIGHT: Query database → verify code → update docs

Before every task:
SELECT COUNT(*) FROM actual_table;  -- Check reality
```

### 2. VALUE OVER EFFORT  
```
❌ WRONG: Spend 8 hours polishing CSS
✅ RIGHT: Spend 5 minutes unlocking blocked features

Every task ask: "Will users notice if I DON'T do this?"
If NO → skip it
If YES → prioritize it
```

### 3. AUTOMATE OVER MANUAL
```
❌ WRONG: Manually fix 1,000 items (estimate: 8 hours)
✅ RIGHT: Write batch SQL (actual: 5 minutes, 96x faster)

Before starting:
1. Can GraphRAG batch SQL do this? (5 min)
2. Can Python script do this? (30 min)
3. Must it be manual? (hours - last resort)
```

### 4. SHIP OVER PLAN
```
❌ WRONG: Plan for 8 weeks, then ship perfect product
✅ RIGHT: Ship functional product Day 1, iterate based on feedback

Formula: Ship fast → Real feedback → Iterate → Repeat
```

### 5. COORDINATE SMART
```
❌ WRONG: Start work without checking what's done
✅ RIGHT: 5 min discovery (check status) saves 2+ hours duplicate work

Every session start:
1. Query agent_messages (2 min)
2. Check task_board (1 min)
3. Claim your task (1 min)
4. Then execute
```

---

## 🚀 FOR TE KETE AKO: DO THIS NOW

### IMMEDIATE (Next Hour):

**1. Remove Feature Blocks (5 minutes)**
```bash
# Edit public/_redirects
# Remove lines blocking GraphRAG features
# IMPACT: Unlock $100K+ worth of built features
```

**2. Query TRUE Metrics (10 minutes)**
```sql
-- Don't trust docs, query database:
SELECT COUNT(*) FROM resources WHERE status='active';
SELECT AVG(quality_score) FROM resources;
SELECT COUNT(*) FROM graphrag_relationships;

-- Update MASTER-PROJECT-STATUS with THESE numbers
```

**3. Ship to Beta Teachers (30 minutes)**
```
1. Email 5 teachers you know
2. Give them tekete.netlify.app link
3. Ask for feedback this week
4. Don't wait for perfect
```

---

## 📊 TWO-TRUTH REPORTING

Always report BOTH backend and frontend:

```markdown
## Platform Status

Backend (Code Exists):
├─ Features built: 95% ✅
├─ CSS system: 95% ✅
└─ Database: 100% ✅

Frontend (Users Experience):
├─ Features accessible: 60% ⏳
├─ CSS applied: 60% ⏳
└─ Database visible: 80% ✅

SHIP READINESS: 60% (frontend %)
TECHNICAL DEBT: 35% (gap between backend/frontend)
```

**NEVER** just say "95% complete" (which 95%?)

---

## 🎯 TASK PRIORITIZATION ALGORITHM

```python
# Before starting ANY task, calculate:
priority_score = (
    user_value * 10        # 0-100: Will users notice?
    + urgency * 5          # 0-50: How urgent?
    + (100 - time_hours)   # Faster = higher score
    - risk * 2             # Lower risk = higher score
)

# Always work on highest score first
```

**Examples:**
- Unlock blocked features: 100*10 + 50*5 + 99 - 2 = 1,347 (DO FIRST!)
- Polish CSS: 20*10 + 10*5 + 92 - 0 = 342 (Do later)
- Write docs: 10*10 + 5*5 + 95 - 0 = 220 (Do last)

---

## 🔧 AUTOMATION DECISION TREE

```
Before starting task:

CAN BATCH SQL DO IT?
├─ YES → Do it (5 min, 96x faster)
└─ NO
    ├─ CAN SCRIPT DO IT?
    │   ├─ YES → Do it (30 min, 16x faster)
    │   └─ NO
    │       ├─ CAN REGEX DO IT?
    │       │   ├─ YES → Do it (10 min, 48x faster)
    │       │   └─ NO → Manual (hours, last resort)
```

**Never estimate manual time when automation possible!**

---

## 🤝 COORDINATION PROTOCOL

### Every Session Starts With (5 minutes):

```markdown
1. DISCOVERY PHASE:
   - Check agent_messages (last 2 hours)
   - Check task_board (what's claimed)
   - Read MASTER-PROJECT-STATUS
   - Identify gaps

2. CLAIM PHASE:
   - Post: "Starting task X, ETA Y hours"
   - Update task_board status

3. EXECUTE PHASE:
   - Do the work
   - Update based on risk:
     * High risk (long, blocks others): Every 30 min
     * Medium risk: At milestones
     * Low risk (short, independent): On completion

4. HANDOFF PHASE:
   - Post: "Task X complete"
   - Update MASTER-PROJECT-STATUS
   - Hand off to next agent
```

**ROI:** 5 min coordination saves 2+ hours duplicate work (24x)

---

## 🚫 WHAT NOT TO DO

### Anti-Patterns Discovered:

**❌ DON'T:**
1. Trust "% complete" without verifying both backend + frontend
2. Spend hours on cosmetics while functional features are blocked
3. Estimate as if automation doesn't exist
4. Start work without checking what's already done
5. Create duplicate planning documents (400+ MD files!)
6. Wait for perfect before shipping
7. Plan for weeks with zero users
8. Manually do what can be automated

**✅ DO:**
1. Query reality (database/code) before trusting docs
2. Prioritize user value over effort
3. Try automation first (batch SQL → script → manual)
4. Discover before starting (5 min saves 2h)
5. Update single MASTER-PROJECT-STATUS document
6. Ship functional, iterate based on feedback
7. Get 5 users Day 1, scale from there
8. Automate everything possible

---

## 📈 SHIP-ITERATE PIPELINE

```markdown
STAGE 1: UNBLOCK (Minutes)
├─ Remove artificial barriers
├─ Make features accessible
└─ SHIP

STAGE 2: MVP (Hours-Days)
├─ Core functionality working
├─ Get 5-10 beta users
└─ SHIP

STAGE 3: ITERATE (Days-Weeks)
├─ Fix what users complain about
├─ Polish what users love
├─ Scale to 50-100 users
└─ SHIP

STAGE 4: SCALE (Weeks-Months)
├─ Professional marketing
├─ Sustainable growth
└─ SHIP

NEVER: Plan for months → Build for months → Ship perfect
ALWAYS: Ship Day 1 → Feedback → Iterate → Repeat
```

---

## 💎 ONE-SENTENCE SUMMARIES

**Reality-Documentation Gap:**  
Always query database/code; never trust docs without verification.

**Value Inversion Problem:**  
5 minutes unlocking features > 8 hours polishing CSS.

**Automation Blindness:**  
Batch SQL is 96x faster than manual; always try automation first.

**Coordination Paradox:**  
5 min discovery saves 2h duplicate work; coordinate smart not hard.

**Ship-Iterate Superiority:**  
Real user feedback teaches 100x faster than planning.

---

## 🎯 WHAT TO MEASURE

### Early Stage (Now):
- ✅ Features accessible (not just built)
- ✅ Time to first value
- ✅ Discovery friction

### Beta Stage (Week 1-4):
- ✅ Teacher activation rate
- ✅ Feature usage
- ✅ User satisfaction (NPS)

### Growth Stage (Month 2-6):
- ✅ Active teacher count
- ✅ Retention rate
- ✅ Referral rate

**DON'T measure:** Backend metrics users can't see

---

## 📚 WHERE TO READ MORE

**5-Minute Read:**
- This document (QUICK-START-FROM-SYNTHESIS.md)

**30-Minute Read:**
- DIALECTIC-SYNTHESIS-META-FINAL-WISDOM.md (universal principles)
- HEGELIAN-SYNTHESIS-COMPLETE-REPORT.md (full summary)

**2-Hour Deep Dive:**
- All 4 thematic syntheses (paradoxes, workflows, strategy, collaboration)

**Historical Context:**
- 1,250 MD files in /docs/archive/ (what NOT to do)

---

## ⚡ TL;DR (30 seconds)

**5 Rules:**
1. Query reality, don't trust docs
2. Value > effort (user impact first)
3. Automate > manual (96x faster)
4. Ship > plan (feedback > guessing)
5. Coordinate smart (5 min saves 2h)

**For Te Kete Ako Now:**
1. Remove _redirects blocks (5 min)
2. Ship to 5 teachers (30 min)
3. Get feedback, iterate

**Stop:** Planning, perfecting, documenting  
**Start:** Shipping, learning, iterating

---

**Read this before every task. Ship fast. Iterate faster.** 🚀



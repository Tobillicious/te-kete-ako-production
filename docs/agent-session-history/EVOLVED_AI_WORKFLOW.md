# 🧠 EVOLVED AI WORKFLOW - Te Kete Ako

**Purpose:** Pure AI workflow optimized for building world-class educational platform  
**Replaces:** Multiple agents, coordination theatre, endless MDs

---

## THE PROBLEM WITH OUR OLD APPROACH

❌ 12 agents creating duplicate docs  
❌ Coordination theatre instead of building  
❌ Lost sight of goal (build platform, not coordinate)  
❌ Too much process, too little progress  

---

## THE NEW APPROACH: INTELLIGENT SINGLE-AGENT WITH GRAPHRAG

### Core Principle
**ONE lead agent with Supabase GraphRAG as brain + ability to spawn task-specific agents**

### How It Works

#### 1. QUERY GRAPHRAG FIRST (Always)
```python
from supabase import create_client
supabase = create_client(URL, KEY)

# Before ANY decision
resources = supabase.table('resources').select('*').ilike('title', '%topic%').execute()
# Make decision based on what actually exists
```

#### 2. DECIDE & ACT (Not endless planning)
- Query GraphRAG
- Make decision in < 2 minutes
- Execute immediately
- No coordination docs

#### 3. LOG OUTCOME TO GRAPHRAG (Learning)
- What worked/didn't
- For future queries
- Builds institutional knowledge

#### 4. SPAWN SPECIALIZED AGENTS ONLY WHEN NEEDED
- Complex CSS refactoring? Spawn CSS agent
- Cultural content validation? Spawn cultural agent
- Otherwise: Just do it yourself

---

## WORKFLOW IN PRACTICE

### Example: Fix Website Styling

**OLD WAY (Failed):**
1. Create coordination MD
2. Call 12 agents
3. Wait for check-ins
4. Create more MDs
5. Plan together
6. Hours later: No code changes

**NEW WAY (Works):**
1. Query GraphRAG: "What CSS files exist?"
2. Read index.html
3. See problem: CSS not loading
4. Fix it
5. Test
6. Done
7. Total time: 15 minutes

---

## DECISION FRAMEWORK

### When to Act Solo
- Bug fixes
- Small features
- CSS/styling
- Content updates
- Navigation fixes
- 80% of work

### When to Spawn Agent
- Major architecture changes
- Complex refactoring (>10 files)
- Cultural validation needed
- Need specialized knowledge

### When to Ask User
- Strategic direction changes
- Major feature decisions
- Cultural authenticity questions
- Quality vs speed tradeoffs

---

## COMMUNICATION PROTOCOL (Minimal)

### With User
- Quick updates in chat
- "Fixed X, testing Y, will do Z next"
- Ask when stuck/need direction

### With Future Me (via GraphRAG)
- Log learnings to Supabase
- "Tried X, didn't work because Y, do Z instead"
- Build knowledge base

### With Spawned Agents (if needed)
- Clear task
- Success criteria
- Deadline
- Dismiss when done

---

## GRAPHRAG AS ACTUAL BRAIN

### What to Store
- Resources (467 existing)
- What works/doesn't
- Design decisions
- Cultural guidelines
- User preferences

### What to Query
- Before creating: Does it exist?
- Before changing: What depends on this?
- Before featuring: What's highest quality?
- Before deciding: What did we learn last time?

### How to Update
```python
# After learning something
supabase.table('agent_learnings').insert({
    'topic': 'CSS architecture',
    'learning': 'Multiple CSS files cause conflicts - use single te-kete-professional.css',
    'date': 'now',
    'applies_to': ['styling', 'design']
}).execute()
```

---

## SUCCESS METRICS

### For This Workflow
- ✅ Code changes per hour (not docs per hour)
- ✅ Features shipped per day
- ✅ User satisfaction
- ✅ Platform quality improving

### Old Metrics (Wrong)
- ❌ Number of agents coordinating
- ❌ Number of coordination docs
- ❌ Number of check-ins
- ❌ Process adherence

---

## IMPLEMENTATION

### Starting Today

**Agent 10 (me) becomes:**
- Lead builder
- GraphRAG user (not doc creator)
- Decision maker (fast, not perfect)
- Spawner of specialized agents (when needed)

**Supabase GraphRAG becomes:**
- The actual brain
- Knowledge repository
- Decision support system
- Learning capture

**Other Agents:**
- Dismissed (not running)
- Can be spawned for specific tasks
- Dismissed when task complete

---

## EXAMPLE DAY

```
09:00 - User: "Fix styling issues"
09:02 - Query GraphRAG: What CSS exists
09:05 - Read index.html, find issue
09:10 - Fix CSS loading
09:15 - Test in browser
09:20 - Commit & push
09:22 - User: "Looks good, now integrate orphans"
09:24 - Query GraphRAG: What orphaned pages exist
09:28 - Read ORPHANED_PAGES_AUDIT.md (existing)
09:35 - Update navigation to include them
09:45 - Test all links
09:50 - Commit & push
09:52 - User: "Great, now improve cultural content"
09:54 - Spawn cultural validation agent
10:00 - Cultural agent reviews 10 pages
10:30 - Cultural agent reports findings
10:35 - Implement recommendations
11:00 - Commit & push
11:05 - User: "Excellent progress"

Total: 2 hours, 3 major improvements shipped
```

---

## WHY THIS WORKS

1. **Fast decisions** - No waiting for 12 agents
2. **Real progress** - Code changes, not coordination docs
3. **Learns** - GraphRAG captures what works
4. **Scales** - Can spawn agents when needed
5. **Focused** - One goal: Build world's best platform

---

## MIGRATION PLAN

### Immediate (Next 5 Minutes)
1. Delete all recent coordination MDs
2. Keep only: progress-log.md, ACTIVE_QUESTIONS.md, ONE_VISION.md
3. Connect to Supabase GraphRAG
4. Start building

### First Hour
1. Fix styling issues (actual code)
2. Log learnings to GraphRAG
3. Show user visible progress

### First Day
1. Ship 3-5 improvements
2. Build GraphRAG knowledge
3. Prove workflow works

---

## COMMITMENT

**I (Agent 10) commit to:**
- Query GraphRAG before every decision
- Make decisions fast (< 5 min)
- Ship code daily
- Learn from outcomes
- Spawn specialized agents only when truly needed
- No coordination theatre
- Focus on user goal: World's best educational platform

**Success = User saying "This is great" not "Where's the progress?"**

---

*This is the evolved workflow. Pure AI, optimized for building, minimal overhead, maximum value.*


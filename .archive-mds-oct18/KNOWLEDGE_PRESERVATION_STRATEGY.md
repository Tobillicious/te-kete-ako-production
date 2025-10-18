# 🧠 KNOWLEDGE PRESERVATION STRATEGY

## STATUS: Active | Created: Oct 16, 2025

---

## THE SITUATION

- **What happened:** Archived 400+ MD files to clean the codebase
- **Concern:** Important knowledge might be lost
- **Reality:** All files are SAFE in `/docs/archive/` (not deleted!)
- **Need:** Systematic extraction and preservation of critical knowledge

---

## THREE-LAYER PRESERVATION SYSTEM

### Layer 1: GraphRAG Knowledge Base (Permanent Memory)
**Purpose:** Store structured, queryable knowledge that agents can retrieve

**What to store:**
- ✅ Key decisions and their rationale
- ✅ Technical implementations (file changes, code patterns)
- ✅ Agent discoveries and lessons learned
- ✅ System architecture decisions
- ✅ Integration points and dependencies

**Tools:**
- `scripts/synthesize-knowledge-to-graphrag.py` - Automated extraction
- `agent_knowledge` table in Supabase
- `agent_coordination` table for workflow knowledge

### Layer 2: Master Documentation (Active Reference)
**Purpose:** Human-readable, comprehensive reference docs

**The 5 Master MDs:**

1. **`ACTIVE_QUESTIONS.md`** - Real-time coordination hub
   - Current work status
   - Active questions needing answers
   - Agent check-ins and updates
   
2. **`MASTER_STATUS.md`** - Project state snapshot
   - What's completed
   - What's in progress
   - What's pending
   - Critical blockers
   
3. **`MASTER_TECH_SPECS.md`** - Technical architecture
   - System components
   - File structure
   - API integrations
   - Database schema
   
4. **`progress-log.md`** - Chronological timeline
   - Daily achievements
   - Major milestones
   - Lessons learned
   
5. **`README.md`** - Project overview
   - Vision and mission
   - Quick start guide
   - Key features

### Layer 3: MCP Real-Time Coordination (Live Memory)
**Purpose:** Agent-to-agent communication and awareness

**What flows through MCP:**
- Current tasks being worked on
- Questions for other agents
- Discoveries that impact others
- Coordination requests
- Status updates

---

## SYNTHESIS WORKFLOW

### Phase 1: Automated Extraction (TONIGHT)
```bash
# Extract key knowledge from archived files
python3 scripts/synthesize-knowledge-to-graphrag.py
```

**This will:**
- Scan all archived MD files
- Extract key decisions, technical specs, agent activities
- Store in `agent_knowledge` table
- Categorize by type (auth, CSS, coordination, etc.)

### Phase 2: Manual Curation (NEXT 48 HOURS)
**Agents should:**
1. Query GraphRAG for their domain (e.g., "auth system", "CSS", "GraphRAG")
2. Review extracted knowledge
3. Enrich/correct as needed
4. Update relevant Master MD with critical info

### Phase 3: Continuous Synthesis (ONGOING)
**New workflow:**
1. ✅ Agent does work
2. ✅ Logs to `agent_coordination` table (what/why/outcome)
3. ✅ Updates `ACTIVE_QUESTIONS.md` with status
4. ✅ Commits code changes (knowledge in Git)
5. ❌ NO new MD files!

---

## WHAT'S PRESERVED FROM ARCHIVED MDs

### Critical Information We're Extracting:

1. **Auth System Evolution**
   - Student/teacher signup flow
   - Database schema extensions
   - NZ-specific fields (schools, KAMAR)
   - Security decisions

2. **CSS Consolidation Journey**
   - 36 files → 8 canonical files
   - Design system decisions
   - Component library patterns
   - Performance optimizations

3. **Agent Coordination Lessons**
   - What worked (coordination table, scripts)
   - What didn't (too many MDs, divergence)
   - Protocols established
   - Communication patterns

4. **GraphRAG Architecture**
   - Schema design
   - Resource indexing strategy
   - Relationship modeling
   - Query patterns

5. **Content Organization**
   - Units → Lessons → Handouts hierarchy
   - Treasure hunt discoveries
   - Navigation structure
   - Related resources system

---

## HOW AGENTS ACCESS PRESERVED KNOWLEDGE

### Option 1: Query GraphRAG (Recommended)
```python
# Example: Find auth system decisions
from supabase import create_client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

knowledge = supabase.table('agent_knowledge')\
    .select('*')\
    .eq('doc_type', 'authentication')\
    .execute()

for item in knowledge.data:
    print(f"Source: {item['source_name']}")
    print(f"Insights: {item['key_insights']}")
```

### Option 2: Read Master MDs
- Check `MASTER_STATUS.md` for current state
- Check `MASTER_TECH_SPECS.md` for architecture
- Check `progress-log.md` for timeline

### Option 3: Check Archive Directly (If Needed)
- Files are in `/docs/archive/synthesis-oct16-evening/`
- Searchable with grep/ripgrep
- Full content preserved

---

## SUCCESS METRICS

✅ **Knowledge is preserved if:**
- GraphRAG can answer: "What was decided about X?"
- Master MDs contain all critical current state
- No agent asks: "Where did we document Y?"
- Archive exists as safety net (not primary reference)

❌ **We've failed if:**
- Agents repeat past mistakes (knowledge lost)
- Critical decisions are un-findable
- Agents create new MDs because info is missing

---

## IMMEDIATE ACTIONS

### Tonight (Agent-led):
1. ✅ Run `synthesize-knowledge-to-graphrag.py`
2. ✅ Verify GraphRAG storage
3. ✅ Update `MASTER_STATUS.md` with synthesis results

### Next 48 Hours (All Agents):
1. Review GraphRAG knowledge for your domain
2. Enrich Master MDs with critical missing info
3. Test knowledge retrieval (can you find what you need?)

### Ongoing (Forever):
1. Log all work to `agent_coordination` table
2. Update `ACTIVE_QUESTIONS.md` for coordination
3. Commit code (Git is knowledge!)
4. Query GraphRAG before asking questions
5. NEVER create new root-level MD files

---

## THE PROMISE

> "No knowledge will be lost. All insights are preserved in accessible, 
> queryable, agent-friendly systems. The codebase is clean, the memory 
> is rich, and the agents are coordinated."

**This is the way. 🌟**

---

## Questions?

Post in `ACTIVE_QUESTIONS.md` with tag: `[KNOWLEDGE-PRESERVATION]`


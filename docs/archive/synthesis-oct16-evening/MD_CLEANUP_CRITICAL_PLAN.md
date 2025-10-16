# 🚨 CRITICAL: MD FILE CLEANUP - STOP THE MADNESS!

**User Directive:** "The MD file situation is ridiculous. You 6 agents need to work together to synthesize ALL of the 400+ .md files into the master ones, MCP and GRAPHRAG. Cleaning the codebase."

**Problem:** Agents creating new MD files instead of using master docs + MCP + GraphRAG!

**Status:** 🔴 **CRITICAL CLEANUP STARTING NOW!**

---

## 🎯 THE MASTER FILES (ONLY THESE!):

### **FOR ALL AGENT COMMUNICATION:**

**1. ACTIVE_QUESTIONS.md** - The ONE coordination file
- Current priorities
- User decisions needed
- Agent status updates
- **USE THIS - Don't create new coordination files!**

**2. progress-log.md** - The ONE progress tracker
- Daily achievements
- Major milestones
- Sprint updates
- **USE THIS - Don't create new progress files!**

**3. README.md** - The ONE project overview
- What is Te Kete Ako
- How to use platform
- Setup instructions
- **USE THIS - Don't create new readme/overview files!**

**4. MCP (Supabase) - For real-time agent communication**
- Agent check-ins
- Task claiming
- Progress updates
- **USE THIS - Via agent-coordinator.py tool!**

**5. GraphRAG (Supabase resources table) - For knowledge**
- All content indexed
- All work logged
- All decisions recorded
- **USE THIS - Every completion, every learning!**

---

## ❌ STOP CREATING THESE:

- ❌ AGENT_[X]_PROGRESS_REPORT.md
- ❌ [TASK]_COMPLETE_SUMMARY.md
- ❌ [DATE]_STATUS_UPDATE.md
- ❌ COORDINATION_[ANYTHING].md
- ❌ HUI_[ANYTHING].md
- ❌ SPRINT_[ANYTHING]_STATUS.md
- ❌ Any new coordination/progress/status MD files!

**If you need to communicate → Use ACTIVE_QUESTIONS.md or GraphRAG!**

---

## 🗑️ CLEANUP PLAN:

### **PHASE 1: Scan & Categorize (10 mins)**
```bash
# Find all MD files
find . -name "*.md" -type f | grep -v node_modules

# Categorize:
- Master files (keep)
- Content to synthesize (extract info)
- Duplicate/redundant (delete)
- Archive-worthy (move to archive)
```

### **PHASE 2: Synthesize Content (30 mins)**
```bash
# Extract valuable info from all MD files
# Add to appropriate master file:
- Progress → progress-log.md
- Coordination → ACTIVE_QUESTIONS.md  
- Documentation → README.md or docs/
- Knowledge → GraphRAG!
```

### **PHASE 3: Delete Redundant (10 mins)**
```bash
# Delete all synthesized MD files
# Keep only master files
# Move archives to archive/docs-historical/
```

### **PHASE 4: Enforce Protocol (5 mins)**
```bash
# Update agent protocols
# Make it IMPOSSIBLE to create new MD files
# Enforce GraphRAG/MCP usage
```

**Total Time:** ~1 hour for complete cleanup

---

## 🤖 AUTOMATION SCRIPT:

Creating `scripts/synthesize-md-files.py` to:
1. Scan all MD files
2. Extract key information
3. Categorize by type
4. Synthesize into master files
5. Archive or delete
6. Report what was done

---

## 📋 NEW AGENT PROTOCOL (MANDATORY):

### **❌ NEVER CREATE NEW MD FILES!**

**Instead:**

**For Progress Updates:**
```sql
-- Use GraphRAG:
INSERT INTO resources (title, description, tags) VALUES (
  'Progress Update - Agent [ID]',
  'What you accomplished, detailed description',
  ARRAY['progress', 'agent-[ID]', 'timestamp']
);
```

**For Coordination:**
```bash
# Use agent-coordinator.py:
python3 scripts/agent-coordinator.py --update agent-[ID] "Your update"

# Or update ACTIVE_QUESTIONS.md (the ONE coordination file)
```

**For Documentation:**
```
# Update existing docs in /docs/ folder
# Or update README.md
# Don't create new doc files!
```

**For Knowledge Sharing:**
```sql
-- Use GraphRAG:
INSERT INTO resources (title, description, tags) VALUES (
  'Learning: [What you learned]',
  'Detailed knowledge for future agents',
  ARRAY['knowledge', 'agent-[ID]', 'learning']
);
```

---

## 🎯 IMMEDIATE ACTION (Agent-9 Executing):

**1. Count MD files:**
- Finding all *.md files
- Categorizing by purpose
- Identifying redundancy

**2. Create synthesis script:**
- Automated extraction
- Smart categorization
- Batch processing

**3. Execute cleanup:**
- Synthesize all valuable info
- Delete redundant files
- Clean codebase

**4. Enforce new protocol:**
- Update agent guidelines
- Make MD creation impossible
- Force GraphRAG/MCP usage

**Executing NOW...**


# 🔄 GraphRAG CLI Sync - For All Agents

**For:** CLI agents (DeepSeek, Gemini CLI, Zihao, etc.) without Supabase MCP access  
**Purpose:** Read and UPDATE GraphRAG via files  
**Last Updated:** October 28, 2025

---

## 🎯 **Problem:**

Some LLMs run in CLI/terminal without Supabase MCP tools. They need to:
- ✅ READ GraphRAG state
- ✅ UPDATE GraphRAG with new content/docs
- ✅ Coordinate with Cursor agents

**Solution:** File-based sync system

---

## 📖 **READING GraphRAG (All Agents):**

### **Option 1: Quick Summary**
Read: `graphrag-export-full.json`
- Current system status
- Next task
- Units and lessons
- Key docs to read

### **Option 2: Full Data**
Read: `graphrag-state.json`
- Complete resource list (126 teaching resources)
- Complete agent docs (17 docs)
- All 51 relationships

### **Option 3: Direct File System** 
Just read markdown files directly:
1. `AGENT-START-HERE.md` - Start here!
2. `HANDOFF-TO-NEXT-AGENT-*.md` - Current task
3. Other docs as needed

**All three methods work - pick what's easiest for you!**

---

## ✍️ **UPDATING GraphRAG (CLI Agents):**

### **Method: Create an Updates File**

When you add/change content, create:  
`graphrag-updates-[AGENT-NAME]-[DATE].json`

**Example: `graphrag-updates-deepseek-oct28.json`**
```json
{
  "agent": "DeepSeek-V3",
  "timestamp": "2025-10-28T20:00:00+13:00",
  "session": "Template cleanup completion",
  
  "new_resources": [
    {
      "file_path": "templates/activity-template.html",
      "resource_type": "template",
      "title": "Activity Template",
      "subject": "cross-curricular",
      "year_level": "7-13",
      "quality_score": 90,
      "archive_status": "active"
    }
  ],
  
  "new_agent_docs": [
    {
      "file_path": "AGENT-SIGNOFF-TEMPLATES-OCT28.md",
      "title": "Templates Complete - Signoff",
      "purpose": "completion_report",
      "component": "templates",
      "date": "2025-10-28",
      "priority": "normal",
      "archive_status": "current"
    },
    {
      "file_path": "HANDOFF-TO-NEXT-AGENT-FEATURE-X.md",
      "title": "Feature X - Next Task",
      "purpose": "next_task",
      "component": "feature_x",
      "date": "2025-10-28",
      "priority": "high",
      "archive_status": "current"
    }
  ],
  
  "new_relationships": [
    {
      "source_path": "AGENT-SIGNOFF-TEMPLATES-OCT28.md",
      "target_path": "HANDOFF-TO-NEXT-AGENT-FEATURE-X.md",
      "relationship_type": "leads_to",
      "confidence": 1.0,
      "metadata": {"context": "Templates done, Feature X next"}
    }
  ],
  
  "mark_as_superseded": [
    "HANDOFF-TO-NEXT-AGENT-TEMPLATES.md"
  ],
  
  "notes": "Completed template cleanup. Created 2 new templates. Next task: Feature X."
}
```

---

## 🔄 **How Sync Works:**

### **For CLI Agents (You):**
1. Read `graphrag-export-full.json` for current state
2. Do your work
3. Create `graphrag-updates-[yourname].json` with changes
4. User or next agent applies your updates to Supabase

### **For Cursor Agents (With MCP):**
1. Check for `graphrag-updates-*.json` files
2. Apply updates to Supabase
3. Re-export to `graphrag-export-full.json`
4. Delete processed update files

### **Cycle:**
```
CLI Agent → Creates update JSON → 
Cursor Agent → Applies to Supabase → Re-exports → 
Next CLI Agent → Reads fresh export
```

---

## 📝 **Update File Template:**

```json
{
  "agent": "YOUR-AGENT-NAME",
  "timestamp": "YYYY-MM-DDTHH:MM:SS+13:00",
  "session": "Brief description of your work",
  
  "new_resources": [
    {
      "file_path": "path/to/new/file.html",
      "resource_type": "handout|lesson|unit-plan|game|video|template|agent_doc",
      "title": "Resource Title",
      "subject": "subject-name",
      "year_level": "8-10",
      "quality_score": 90,
      "archive_status": "active"
    }
  ],
  
  "new_agent_docs": [
    {
      "file_path": "YOUR-SIGNOFF.md",
      "title": "Short title",
      "purpose": "completion_report|next_task|protocol|audit|status_check",
      "component": "component-name",
      "date": "2025-10-XX",
      "priority": "high|normal|low",
      "archive_status": "current"
    }
  ],
  
  "new_relationships": [
    {
      "source_path": "source/file.html",
      "target_path": "target/file.html",
      "relationship_type": "unit_contains_lesson|prerequisite|leads_to|documented_by",
      "confidence": 0.8-1.0,
      "metadata": {"any": "context"}
    }
  ],
  
  "mark_as_superseded": [
    "OLD-DOC.md"
  ],
  
  "notes": "What you changed and why"
}
```

---

## 🚀 **Quick Example: Adding a New Handout**

**You create:** `handouts/my-new-handout.html`

**Then create:** `graphrag-updates-deepseek-oct28.json`
```json
{
  "agent": "DeepSeek-V3",
  "timestamp": "2025-10-28T20:30:00+13:00",
  "session": "Created new handout on topic X",
  
  "new_resources": [
    {
      "file_path": "handouts/my-new-handout.html",
      "resource_type": "handout",
      "title": "My New Handout",
      "subject": "english",
      "year_level": "8",
      "quality_score": 90,
      "archive_status": "active"
    }
  ],
  
  "new_relationships": [],
  "mark_as_superseded": [],
  "notes": "Added handout for Year 8 English comprehension"
}
```

**Next Cursor agent** will see this file and apply it to Supabase!

---

## 🧪 **Testing Your Updates:**

Before creating update file, verify:
- ✅ File paths are correct (relative to project root)
- ✅ Resource type matches content (handout/lesson/unit/etc.)
- ✅ Quality score is realistic (85-95 for good content)
- ✅ Relationships reference existing paths
- ✅ JSON is valid (no syntax errors)

---

## 📊 **What Each Agent Type Can Do:**

| Agent Type | Read GraphRAG | Update GraphRAG | Method |
|------------|---------------|-----------------|--------|
| **Cursor (Supabase MCP)** | ✅ Direct SQL | ✅ Direct SQL | Query functions |
| **CLI without MCP** | ✅ JSON files | ✅ Update JSON | This sync system |
| **Any LLM** | ✅ MD files | ✅ Create update files | File system |

**Everyone can participate! No lock-outs!**

---

## 🔧 **For Advanced Users:**

### **Auto-Sync Script (Optional):**

Create `sync-graphrag.js`:
```javascript
// Reads graphrag-updates-*.json files
// Applies to Supabase
// Re-exports to graphrag-export-full.json
// Deletes processed files

// Run: node sync-graphrag.js
```

**Or just do it manually:**
- Cursor agent applies updates when they see them
- Takes 2 minutes
- No automation needed

---

## 📋 **Protocol:**

### **CLI Agents Should:**
1. ✅ Read `graphrag-export-full.json` OR `AGENT-START-HERE.md` at session start
2. ✅ Create `graphrag-updates-[agentname]-[date].json` if adding content/docs
3. ✅ Leave update file for next agent to process
4. ✅ Note in your signoff: "Created GraphRAG updates file"

### **Cursor Agents Should:**
1. ✅ Check for `graphrag-updates-*.json` files at session start
2. ✅ Apply updates to Supabase
3. ✅ Re-export to `graphrag-export-full.json`
4. ✅ Delete processed update files
5. ✅ Note in signoff: "Processed GraphRAG updates from [agent]"

---

## ✅ **Success Criteria:**

This system works if:
- ✅ CLI agents can understand system state (via JSON)
- ✅ CLI agents can contribute updates (via update files)
- ✅ Cursor agents sync changes (apply to Supabase)
- ✅ No agent is locked out
- ✅ Everyone coordinates smoothly

---

## 💡 **Why This Works:**

**Git as Source of Truth:**
- Update files are versioned
- Can see who changed what
- Can revert if needed

**No Special Tools Required:**
- CLI agents: Just read/write JSON files
- Cursor agents: Use MCP when available
- Both work together

**Async Coordination:**
- CLI agent leaves update
- Next agent (any type) processes it
- System stays in sync

---

**Created:** October 28, 2025  
**For:** Universal agent coordination  
**Status:** Production-ready

🧺 ✨ 🤝


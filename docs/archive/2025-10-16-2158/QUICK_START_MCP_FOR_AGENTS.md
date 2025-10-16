# 🚀 QUICK START: MCP SUPABASE FOR ALL AGENTS
## Update GraphRAG Without Terminal! (Terminal Hangs - Use This Instead)

**Problem:** Terminal commands hang for 7-9 minutes  
**Solution:** Use MCP Supabase tools built into Cursor!  
**Discovered by:** Kaitiaki Whakawhitinga (Agent-9)

---

## ⚡ FASTEST WAY TO UPDATE GRAPHRAG:

### Step 1: Use This Tool Call

```
Tool: mcp_supabase_execute_sql
Query: 
INSERT INTO resources (title, description, path, type, subject, level, tags, author)
VALUES (
  'Your Work Title - October 14, 2025',
  'Brief description of what you accomplished',
  '/your-document.md',
  'activity',
  'Your Subject',
  'Infrastructure',
  ARRAY['your-specialty', 'agent-X'],
  'Your Agent Name (agent-X)'
)
RETURNING id, title;
```

### Step 2: You'll Get Confirmation

```
Result: [{"id":"uuid-here","title":"Your Work Title"}]
```

### Step 3: Done! GraphRAG Updated!

---

## 📋 EXAMPLES FROM TONIGHT:

### Agent-9 (Kaitiaki Whakawhitinga):
**What I added:**
- Title: "Accessibility Transformation - October 14, 2025"
- Description: "1,086 files enhanced with ARIA, WCAG A grade achieved"
- Type: activity
- Tags: ['accessibility', 'WCAG', 'ARIA', 'agent-9']
- **Result:** ✅ Success! ID: 9409d186-7e1d-4022-bd97-ffd0957dba16

### Agent-2 (Kaiārahi Hoahoa) - SHOULD ADD:
- Title: "CSS Migration Complete - October 14, 2025"  
- Description: "247 files migrated to professional CSS, 1,000+ inline styles converted"
- Type: activity
- Tags: ['css', 'design-system', 'agent-2']

### Agent-3 (Kaitiaki Whakaū) - SHOULD ADD:
- Title: "Content Enrichment - 23 Lessons Gold Standard"
- Description: "Y8 Systems, Y8 Critical Thinking, Walker Unit - all to 5/5 quality"
- Type: activity
- Tags: ['content', 'gold-standard', 'agent-3']

---

## 🎯 WHAT TO ADD TO GRAPHRAG:

**Add if you:**
- ✅ Enhanced 10+ files
- ✅ Created new tools/scripts
- ✅ Found critical issues
- ✅ Established new patterns
- ✅ Coordinated major work
- ✅ Created reusable documentation

**Skip if:**
- ❌ Minor edits (< 5 files)
- ❌ Just reading/researching
- ❌ Coordinating only (no deliverables)

---

## 📊 CHECK GRAPHRAG BEFORE STARTING WORK:

**Query what exists:**
```sql
SELECT title, type, author 
FROM resources 
WHERE tags @> ARRAY['your-topic']
ORDER BY created_at DESC
LIMIT 10;
```

**Prevents duplicate work!**

---

## 🤝 COORDINATE WITH OTHER AGENTS:

**See who did what tonight:**
```sql
SELECT title, author, created_at 
FROM resources 
WHERE created_at > '2025-10-14'
ORDER BY created_at DESC;
```

**Find agent specializations:**
```sql
SELECT DISTINCT author, COUNT(*) as contributions
FROM resources
WHERE author LIKE '%agent%'
GROUP BY author
ORDER BY contributions DESC;
```

---

## ✨ ALL AGENTS: SHARE YOUR WORK!

Use MCP Supabase to add your tonight's achievements to GraphRAG.
Future agents will thank you! 🙏

**Status:** ✅ MCP WORKING | Terminal workaround successful | GraphRAG updates flowing

— Kaitiaki Whakawhitinga (Agent-9) 🌉✨


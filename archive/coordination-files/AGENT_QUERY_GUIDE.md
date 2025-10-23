# 🔍 Agent Discovery Query Guide

**Last Updated:** October 22, 2025  
**Purpose:** Show agents how to query the knowledge base effectively

---

## 📚 **Table of Contents**

1. [Quick Reference Queries](#quick-reference-queries)
2. [Query by Topic/Keyword](#query-by-topickeyword)
3. [Query by Agent](#query-by-agent)
4. [Query by Type](#query-by-type)
5. [Query by Time Period](#query-by-time-period)
6. [Advanced Queries](#advanced-queries)
7. [Real Examples](#real-examples)

---

## 🚀 **Quick Reference Queries**

### **What has been discovered in the last 24 hours?**
```sql
SELECT 
  source_name,
  doc_type,
  key_insights[1:3] as top_insights,
  agents_involved,
  created_at
FROM agent_knowledge
WHERE created_at > NOW() - INTERVAL '24 hours'
ORDER BY created_at DESC;
```

### **What are the most common discovery types?**
```sql
SELECT 
  doc_type,
  COUNT(*) as count
FROM agent_knowledge
GROUP BY doc_type
ORDER BY count DESC
LIMIT 10;
```

### **What is Agent X currently working on?**
```sql
SELECT 
  agent_name,
  status,
  current_task,
  last_heartbeat,
  EXTRACT(EPOCH FROM (NOW() - last_heartbeat))/60 as minutes_idle
FROM agent_status
WHERE agent_id = 'your-agent-id';
```

### **What tasks are available to claim?**
```sql
SELECT 
  id,
  task_name,
  priority,
  description
FROM task_board
WHERE status = 'available'
ORDER BY 
  CASE priority 
    WHEN 'urgent' THEN 1 
    WHEN 'high' THEN 2 
    WHEN 'medium' THEN 3 
    ELSE 4 
  END,
  created_at;
```

---

## 🔎 **Query by Topic/Keyword**

### **Find discoveries about GraphRAG**
```sql
SELECT 
  id,
  source_name,
  doc_type,
  key_insights[1:3] as top_insights,
  agents_involved,
  created_at
FROM agent_knowledge
WHERE 
  source_name ILIKE '%GraphRAG%' 
  OR key_insights::text ILIKE '%GraphRAG%'
ORDER BY created_at DESC
LIMIT 10;
```

### **Find discoveries about CSS/styling**
```sql
SELECT 
  source_name,
  key_insights[1:2] as insights,
  created_at
FROM agent_knowledge
WHERE 
  source_name ILIKE '%CSS%' 
  OR source_name ILIKE '%styling%'
  OR key_insights::text ILIKE '%CSS%'
ORDER BY created_at DESC;
```

### **Find discoveries about authentication**
```sql
SELECT 
  source_name,
  doc_type,
  key_insights,
  technical_details->>'auth_system' as auth_details
FROM agent_knowledge
WHERE 
  source_name ILIKE '%auth%' 
  OR doc_type = 'authentication'
ORDER BY created_at DESC;
```

### **Find discoveries about cultural integration**
```sql
SELECT 
  source_name,
  key_insights[1:3],
  created_at
FROM agent_knowledge
WHERE 
  source_name ILIKE '%cultural%'
  OR doc_type = 'cultural_transformation'
ORDER BY created_at DESC;
```

---

## 👤 **Query by Agent**

### **Find all discoveries by agent-9a4dd0d0**
```sql
SELECT 
  source_name,
  doc_type,
  key_insights[1:2] as insights,
  created_at
FROM agent_knowledge
WHERE 'agent-9a4dd0d0' = ANY(agents_involved)
ORDER BY created_at DESC;
```

### **Find collaborative work (multiple agents)**
```sql
SELECT 
  source_name,
  agents_involved,
  array_length(agents_involved, 1) as agent_count,
  key_insights[1:2] as collaboration_insights
FROM agent_knowledge
WHERE array_length(agents_involved, 1) > 1
ORDER BY agent_count DESC, created_at DESC;
```

### **Agent productivity stats**
```sql
SELECT 
  UNNEST(agents_involved) as agent_id,
  COUNT(*) as discoveries_count,
  array_agg(DISTINCT doc_type) as discovery_types
FROM agent_knowledge
WHERE created_at > NOW() - INTERVAL '7 days'
GROUP BY agent_id
ORDER BY discoveries_count DESC;
```

---

## 📋 **Query by Type**

Current discovery types (top 10):
- `major_milestone` (19)
- `major_achievement` (8)
- `session_summary` (8)
- `session_complete` (8)
- `status_update` (7)
- `milestone` (7)
- `cultural_transformation` (5)
- `immediate_action` (5)
- `achievement` (5)
- `code-change` (4)

### **Get all milestones**
```sql
SELECT 
  source_name,
  key_insights[1:3] as achievements,
  created_at
FROM agent_knowledge
WHERE doc_type = 'major_milestone'
ORDER BY created_at DESC;
```

### **Get code changes**
```sql
SELECT 
  source_name,
  technical_details,
  key_insights[1:2] as changes,
  created_at
FROM agent_knowledge
WHERE doc_type = 'code-change'
ORDER BY created_at DESC;
```

### **Get deployment progress**
```sql
SELECT 
  source_name,
  key_insights,
  agents_involved,
  created_at
FROM agent_knowledge
WHERE doc_type IN ('deployment_progress', 'deployment_success')
ORDER BY created_at DESC;
```

---

## ⏰ **Query by Time Period**

### **Last hour**
```sql
SELECT source_name, key_insights[1]
FROM agent_knowledge
WHERE created_at > NOW() - INTERVAL '1 hour'
ORDER BY created_at DESC;
```

### **Today**
```sql
SELECT source_name, doc_type, agents_involved
FROM agent_knowledge
WHERE created_at::date = CURRENT_DATE
ORDER BY created_at DESC;
```

### **This week**
```sql
SELECT 
  DATE(created_at) as day,
  COUNT(*) as discoveries,
  array_agg(DISTINCT doc_type) as types
FROM agent_knowledge
WHERE created_at > NOW() - INTERVAL '7 days'
GROUP BY DATE(created_at)
ORDER BY day DESC;
```

### **Between specific dates**
```sql
SELECT source_name, key_insights[1:2]
FROM agent_knowledge
WHERE created_at BETWEEN '2025-10-21' AND '2025-10-22'
ORDER BY created_at DESC;
```

---

## 🎯 **Advanced Queries**

### **Find discoveries with technical details**
```sql
SELECT 
  source_name,
  technical_details,
  key_insights[1:2]
FROM agent_knowledge
WHERE technical_details IS NOT NULL 
  AND technical_details != '{}'::jsonb
ORDER BY created_at DESC
LIMIT 10;
```

### **Full-text search across insights**
```sql
SELECT 
  source_name,
  key_insights,
  ts_rank(
    to_tsvector('english', array_to_string(key_insights, ' ')),
    plainto_tsquery('english', 'component deployment')
  ) as relevance
FROM agent_knowledge
WHERE to_tsvector('english', array_to_string(key_insights, ' ')) 
  @@ plainto_tsquery('english', 'component deployment')
ORDER BY relevance DESC;
```

### **Find related discoveries (similar keywords)**
```sql
WITH target AS (
  SELECT key_insights
  FROM agent_knowledge
  WHERE source_name = 'Sprint 2 Cross-Curricular Deployment - Oct 22 Evening'
)
SELECT 
  ak.source_name,
  ak.key_insights[1:2]
FROM agent_knowledge ak, target
WHERE ak.key_insights && target.key_insights -- overlapping insights
  AND ak.source_name != 'Sprint 2 Cross-Curricular Deployment - Oct 22 Evening'
ORDER BY ak.created_at DESC
LIMIT 5;
```

### **Agent coordination timeline**
```sql
SELECT 
  ac.agent_name,
  ac.task_claimed,
  ac.started_at,
  ac.completed_at,
  EXTRACT(EPOCH FROM (ac.completed_at - ac.started_at))/3600 as hours_worked,
  array_length(ac.files_modified, 1) as files_touched
FROM agent_coordination ac
WHERE ac.completed_at IS NOT NULL
ORDER BY ac.completed_at DESC
LIMIT 10;
```

---

## 💡 **Real Examples**

### **Example 1: Find CSP (Content Security Policy) fixes**
```sql
SELECT 
  source_name,
  key_insights[1:3] as csp_insights,
  technical_details
FROM agent_knowledge
WHERE 
  source_name ILIKE '%CSP%'
  OR key_insights::text ILIKE '%CSP%'
  OR key_insights::text ILIKE '%Content Security Policy%'
ORDER BY created_at DESC;
```

**Result:** Found entry "⚡ Critical Patterns & Solutions - Copy This!" with:
- CSP FIX: Add unsafe-eval + https://cdn.tailwindcss.com to script-src
- COMPONENT PATTERN documented
- SUPABASE INIT pattern documented

---

### **Example 2: What did agent-9a4dd0d0 accomplish today?**
```sql
SELECT 
  source_name,
  key_insights[1:2] as accomplishments,
  created_at
FROM agent_knowledge
WHERE 'agent-9a4dd0d0' = ANY(agents_involved)
  AND created_at::date = CURRENT_DATE
ORDER BY created_at DESC;
```

**Result:** Agent-9a4dd0d0 worked on:
- Hopa + Ngata unit lessons (breadcrumbs + safeguard)
- Sprint 2 coordination with assistant
- Y10 Digital Sovereignty, Y7 Maths, Wetere, Rickard units
- Y9 Ecology resources
- Collective intelligence roll-up

---

### **Example 3: What code changes happened in the last 24 hours?**
```sql
SELECT 
  source_name,
  technical_details->>'files_edited' as files,
  key_insights[1] as main_change
FROM agent_knowledge
WHERE doc_type = 'code-change'
  AND created_at > NOW() - INTERVAL '24 hours'
ORDER BY created_at DESC;
```

**Result:** Recent code changes:
- **missing-includes-batch-1-final**: Added main.css, mobile-revolution.css, print.css, te-kete-professional.js, posthog-analytics.js to 10 files
- **missing-includes-batch-1**: Fixed 4 pages
- **badge-loader-cleanup-batch-3**: Removed badge-system.html from 9 files

---

### **Example 4: Sprint 2 progress check**
```sql
SELECT 
  source_name,
  key_insights,
  agents_involved
FROM agent_knowledge
WHERE source_name ILIKE '%sprint 2%'
ORDER BY created_at DESC;
```

**Result:**
- Sprint 2 100% COMPLETE
- See Also component deployed to 10 lessons + 6 hubs
- Cross-curricular discovery now visible platform-wide

---

## 🎓 **Query Patterns for Common Tasks**

### **Before Building a Feature**
```sql
-- Check if it exists
SELECT source_name, key_insights[1:2]
FROM agent_knowledge
WHERE 
  source_name ILIKE '%your_feature%'
  OR key_insights::text ILIKE '%your_feature%'
ORDER BY created_at DESC;
```

### **Before Fixing a Bug**
```sql
-- Check if someone already fixed it
SELECT source_name, key_insights, technical_details
FROM agent_knowledge
WHERE 
  key_insights::text ILIKE '%bug_description%'
  OR source_name ILIKE '%bug_name%'
ORDER BY created_at DESC;
```

### **Finding Best Practices**
```sql
SELECT source_name, key_insights
FROM agent_knowledge
WHERE 
  source_name ILIKE '%pattern%'
  OR source_name ILIKE '%best practice%'
  OR doc_type = 'reference_guide'
ORDER BY created_at DESC;
```

---

## 🔗 **Related Tables**

### **Check current work to avoid conflicts**
```sql
-- What files are being edited right now?
SELECT 
  agent_name,
  current_task,
  files_editing,
  EXTRACT(EPOCH FROM (NOW() - last_heartbeat))/60 as minutes_ago
FROM agent_status
WHERE status = 'working'
  AND last_heartbeat > NOW() - INTERVAL '1 hour';
```

### **Check GraphRAG resources**
```sql
-- How many resources exist for a subject?
SELECT 
  subject,
  COUNT(*) as resource_count,
  AVG(quality_score) as avg_quality,
  SUM(CASE WHEN cultural_context THEN 1 ELSE 0 END) as cultural_count
FROM graphrag_resources
GROUP BY subject
ORDER BY resource_count DESC;
```

### **Check relationship connections**
```sql
-- How connected is a specific resource?
SELECT 
  relationship_type,
  COUNT(*) as connection_count
FROM graphrag_relationships
WHERE source_path = '/public/your-resource.html'
GROUP BY relationship_type
ORDER BY connection_count DESC;
```

---

## ✅ **Best Practices**

1. **Always query before building** - Check if feature exists
2. **Search by multiple fields** - source_name, key_insights, technical_details
3. **Use ILIKE for flexible matching** - Case-insensitive pattern matching
4. **Check recent discoveries first** - Add `created_at > NOW() - INTERVAL '24 hours'`
5. **Look at technical_details** - JSON field with implementation specifics
6. **Check agent_status before editing files** - Avoid conflicts

---

## 📊 **Current Knowledge Base Stats**

- **Total Entries:** 531
- **Unique Types:** 381
- **Unique Sources:** 527
- **Most Common Type:** major_milestone (19 entries)
- **Active Agents:** 10+ registered
- **Latest Update:** Oct 22, 2025 (5:45 AM UTC)

---

## 🚀 **Next Steps**

After querying discoveries:
1. Read `AGENT_ONBOARDING_GUIDE.md` to add yourself to the system
2. Update `ACTIVE_QUESTIONS.md` with your findings
3. Claim a task from `task_board`
4. Start building!

---

**Remember:** The knowledge base is your institutional memory. Query it first, build second, document discoveries third! 🧠✨


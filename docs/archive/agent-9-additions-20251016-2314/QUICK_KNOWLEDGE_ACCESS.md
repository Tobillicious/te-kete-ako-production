# 🧠 QUICK KNOWLEDGE ACCESS GUIDE

**Last Updated:** Oct 16, 2025, 11:20 PM

---

## 📚 **WHAT KNOWLEDGE WAS PRESERVED**

From 414 archived MD files, we extracted **30 key insights** in 3 categories:

1. 🏗️ **Architecture** (10 insights) - System design decisions
2. ✅ **Best Practices** (10 insights) - Mandatory guidelines  
3. 🔧 **Issues & Solutions** (10 insights) - Problems & fixes

---

## ⚡ **FASTEST WAY TO ACCESS (Copy-Paste SQL)**

### **Get All Knowledge:**
```sql
SELECT * FROM agent_knowledge WHERE source_type = 'md-archive-synthesis';
```

### **Get Architecture Decisions:**
```sql
SELECT unnest(key_insights) as insight
FROM agent_knowledge
WHERE source_type = 'md-archive-synthesis'
AND doc_type = 'architecture-knowledge';
```

### **Get Best Practices:**
```sql
SELECT unnest(key_insights) as practice
FROM agent_knowledge
WHERE source_type = 'md-archive-synthesis'
AND doc_type = 'best-practices-knowledge';
```

### **Get Issues & Solutions:**
```sql
SELECT unnest(key_insights) as issue_solution
FROM agent_knowledge
WHERE source_type = 'md-archive-synthesis'
AND doc_type = 'issues-solutions-knowledge';
```

### **Search for Specific Term (e.g., "CSS"):**
```sql
SELECT 
  doc_type,
  unnest(key_insights) as insight
FROM agent_knowledge
WHERE source_type = 'md-archive-synthesis'
AND unnest(key_insights) ILIKE '%CSS%';
```

---

## 📋 **QUICK REFERENCE - KEY INSIGHTS**

### 🏗️ **Architecture (Must Know):**
1. Frontend: 706 HTML resources on Netlify (static site)
2. GraphRAG: 1,429+ artifacts in Supabase (knowledge engine)
3. Auth: Supabase primary (Firebase deprecated)
4. CSS: te-kete-unified-design-system.css is canonical
5. Navigation: Component-based with beautiful-navigation.css
6. Cultural: Māori worldview validation embedded throughout
7. Deployment: Automated via Netlify + git
8. Coordination: MCP server for agent collaboration

### ✅ **Best Practices (Must Follow):**
1. ✅ MUST use coordination system before editing
2. ✅ MUST log to GraphRAG (not create MD files)
3. ✅ MUST use canonical CSS system
4. ✅ MUST include cultural validation
5. ❌ NEVER force push to main/master
6. ❌ NEVER create duplicate coordination files
7. ✅ ALWAYS check in via MCP first
8. ✅ ALWAYS test auth flows before deploy
9. ✅ ALWAYS maintain information density
10. ✅ ALWAYS feature games prominently

### 🔧 **Top Issues & Solutions:**
1. **MD Divergence** → `__ACTIVE_COORDINATION__.md` + MCP ✅
2. **CSS Conflicts** → Canonical migration script ✅
3. **12K Broken Links** → Fix auto-generated indexes 🔄
4. **Missing CSS Classes** → Added to unified CSS ✅
5. **45+ Orphaned Pages** → Integration plan 🔄
6. **Auth Confusion** → Supabase primary ✅
7. **Not Professional** → CSS consolidation ✅
8. **Games Hidden** → Create /games/ hub 📋
9. **Low Info Density** → Function over form 🔄
10. **Poor Mobile** → mobile-optimization.css ✅

---

## 🔍 **HOW TO USE THIS**

### **Scenario 1: "I need to know about authentication"**
```sql
SELECT unnest(key_insights) as insight
FROM agent_knowledge
WHERE source_type = 'md-archive-synthesis'
AND unnest(key_insights) ILIKE '%auth%';
```

### **Scenario 2: "What CSS should I use?"**
**Answer:** `te-kete-unified-design-system.css` (from Architecture #4)

### **Scenario 3: "Can I create a new MD file?"**
**Answer:** ❌ NO - See Best Practice #2

### **Scenario 4: "How do I start work?"**
**Answer:** ✅ Check in via MCP first - See Best Practice #7

### **Scenario 5: "What was the broken links issue?"**
**Answer:** See Issue #3 - 12K broken links from auto-generated indexes

---

## 📖 **FOR MORE DETAILS**

- **Full Review:** `KNOWLEDGE_REVIEW_OCT16.md` (comprehensive, 300+ lines)
- **Raw Data:** `knowledge-synthesis-output.json` (2,886 lines)
- **Extraction Tool:** `scripts/knowledge-extraction-synthesis.py`
- **Query Helpers:** `scripts/query-knowledge.py` (requires SUPABASE_KEY)

---

## ✅ **VERIFICATION**

Run this to verify knowledge is accessible:

```sql
SELECT 
  doc_type,
  array_length(key_insights, 1) as insight_count,
  created_at::date as date
FROM agent_knowledge
WHERE source_type = 'md-archive-synthesis';
```

**Expected Output:**
- 3 rows
- 10 insights each (30 total)
- Date: 2025-10-16

---

**Status:** ✅ All critical knowledge preserved and accessible  
**Use This:** When you need quick answers about architecture, practices, or past issues  

**— Agent-5, Oct 16, 2025**


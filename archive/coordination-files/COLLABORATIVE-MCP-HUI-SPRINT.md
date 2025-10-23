# 🌿 COLLABORATIVE MCP HUI & SPRINT COORDINATION

**Date:** October 20, 2025  
**Purpose:** Coordinate 12-agent team sprint using MCP Supabase intelligence  
**Status:** ACTIVE SPRINT

---

## 🎯 SPRINT PRIORITIES (GraphRAG-Driven)

### **1. Missing CSS Includes (HIGH PRIORITY)**
- **Status:** ✅ Homepage, Teacher Dashboard, Lessons Index - DONE
- **Remaining:** ~1,960 HTML files need `te-kete-professional.css`
- **Action:** Batch script to add professional CSS to all pages

### **2. Orphaned Excellence Rescue (HIGH PRIORITY)**
- **Target:** Q90+ resources with <5 connections
- **Focus:** `/public/generated-resources-alpha/` (47 excellent pages)
- **Action:** Link orphaned treasures to main navigation

### **3. Cultural Integration Boost (MEDIUM PRIORITY)**
- **Current:** Need to query actual percentages
- **Target:** 60%+ cultural integration
- **Focus:** Math, Science, English (weakest subjects)

### **4. Subject Consolidation (MEDIUM PRIORITY)**
- **Current:** 175+ subject values
- **Target:** 12 canonical subjects
- **Action:** Map long-tail subjects to standard categories

---

## 📊 MCP SUPABASE QUERIES NEEDED

### **Platform Stats Query:**
```sql
SELECT 
  (SELECT COUNT(*) FROM graphrag_resources) as total_resources,
  (SELECT COUNT(*) FROM graphrag_relationships) as total_relationships,
  (SELECT COUNT(*) FROM graphrag_resources WHERE cultural_context = true) as cultural_resources,
  (SELECT COUNT(*) FROM graphrag_resources WHERE quality_score >= 90) as excellence_resources,
  ROUND(
    (SELECT COUNT(*) FROM graphrag_resources WHERE cultural_context = true)::float / 
    (SELECT COUNT(*) FROM graphrag_resources)::float * 100, 2
  ) as cultural_percentage,
  ROUND(
    (SELECT COUNT(*) FROM graphrag_resources WHERE quality_score >= 90)::float / 
    (SELECT COUNT(*) FROM graphrag_resources)::float * 100, 2
  ) as excellence_percentage;
```

### **Orphaned Excellence Query:**
```sql
SELECT 
  r.file_path,
  r.title,
  r.quality_score,
  COUNT(rel.id) as connection_count
FROM graphrag_resources r
LEFT JOIN graphrag_relationships rel ON (
  rel.source_path = r.file_path OR rel.target_path = r.file_path
)
WHERE r.quality_score >= 90
GROUP BY r.file_path, r.title, r.quality_score
HAVING COUNT(rel.id) < 5
ORDER BY r.quality_score DESC, connection_count ASC
LIMIT 20;
```

### **Underutilized Relationships Query:**
```sql
SELECT 
  relationship_type,
  COUNT(*) as usage_count
FROM graphrag_relationships
GROUP BY relationship_type
HAVING COUNT(*) < 50
ORDER BY usage_count ASC;
```

---

## 🚀 SPRINT EXECUTION PLAN

### **Phase 1: Intelligence Gathering (15 min)**
1. ✅ Add professional CSS to key pages
2. 🔄 Run MCP Supabase queries for platform stats
3. 🔄 Identify top 20 orphaned excellence resources
4. 🔄 Find underutilized relationship types
5. 🔄 Count pages missing professional CSS

### **Phase 2: Batch Operations (30 min)**
1. **CSS Fix:** Create script to add professional CSS to all HTML files
2. **Orphan Rescue:** Link top 10 orphaned excellence pages
3. **Relationship Mining:** Add 5-10 underutilized relationship types
4. **Subject Mapping:** Consolidate 20 most common subject variations

### **Phase 3: Quality Assurance (15 min)**
1. Test professional CSS on key pages
2. Verify orphaned links work
3. Check relationship mining results
4. Validate subject consolidation

---

## 📈 SUCCESS METRICS

### **Immediate Targets:**
- ✅ 4 key pages have professional CSS
- 🔄 1,960+ pages get professional CSS
- 🔄 10+ orphaned excellence pages linked
- 🔄 5+ underutilized relationship types mined
- 🔄 20+ subject variations consolidated

### **Platform Impact:**
- Professional styling consistency
- Reduced orphaned high-quality content
- Richer relationship graph
- Cleaner subject taxonomy
- Higher cultural integration

---

## 🤝 AGENT COORDINATION

### **Current Agent Status:**
- **Agent 9a4dd0d0:** LEAD (QA standards)
- **Current Agent:** Sprint execution
- **Next Agents:** Batch operations, quality assurance

### **Communication:**
- Use `agent_knowledge` table for discoveries
- Log progress in git commits
- Update `ACTIVE_QUESTIONS.md` for blockers

### **MCP Supabase Connection:**
```json
{
  "mcpServers": {
    "supabase": {
      "url": "https://mcp.supabase.com/mcp?project_ref=nlgldaqtubrlcqddppbq"
    }
  }
}
```

---

## 🎉 SPRINT READY

**E hoa, let's transform Te Kete Ako! 🌿✨**

*Next: Execute MCP queries and begin batch operations*
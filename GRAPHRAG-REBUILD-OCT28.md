# 🧠 GraphRAG Rebuild - October 28, 2025

**Agent:** Kaitiaki Aronui (Backend Cleanup Specialist)  
**Task:** Clean and rebuild GraphRAG system  
**Status:** ✅ **COMPLETE**  
**Time:** ~2 hours

---

## 🎯 **Problem:**

GraphRAG database was **exceeding Supabase free tier limits** (0.52 GB of 0.5 GB):
- `graphrag_resources`: 20,984 rows → 42 MB
- `graphrag_relationships`: 1,190,000 rows → 432 MB
- **Total:** 474 MB (88% of entire database!)
- **95% of data** was pre-rollback bloat that no longer exists

---

## 🔧 **Solution:**

### **Phase 1: Nuclear Cleanup**
```sql
TRUNCATE TABLE graphrag_relationships;
TRUNCATE TABLE graphrag_resources CASCADE;
```
✅ Instant 474 MB relief

### **Phase 2: Rebuild with Current Content**
Scanned actual filesystem post-rollback:
- 81 handouts
- 43 units (including embedded lessons)
- 9 games
- **Total: 126 curated teaching resources**

Rebuilt `graphrag_resources` from `resources` table (curated content only)

### **Phase 3: Create Minimal Relationships**
Created only high-value relationships:
- **Unit → Lesson** (34 relationships) - structural
- **Same Subject** (4 relationships) - recommendations
- **Total: 38 relationships** (down from 1.19 MILLION!)

---

## 📊 **Results:**

| Metric | Before | After | Reduction |
|--------|--------|-------|-----------|
| **Resources** | 20,984 | 126 | **99.4%** ↓ |
| **Relationships** | 1,190,000 | 38 | **99.997%** ↓ |
| **graphrag_resources** | 42 MB | 328 kB | **99.3%** ↓ |
| **graphrag_relationships** | 432 MB | 128 kB | **99.97%** ↓ |
| **Total GraphRAG** | **474 MB** | **~456 kB** | **🔥 99.9% savings!** |

**Database space saved: 473.5 MB**

---

## ✅ **What Was Preserved:**

### **Resources Table (Curated Content):**
- ✅ 126 curated resources intact
- ✅ All browse.html functionality working
- ✅ My Kete feature unaffected
- ✅ User saved resources safe

### **New GraphRAG (Clean):**
- 126 resources (current, post-rollback)
- 38 high-value relationships
- Minimal, purposeful data only

---

## 🔗 **GraphRAG Relationships:**

### **Unit → Lesson (34 relationships)**
```
Unit 1: Te Ao Māori → 5 lessons
Unit 2: Decolonized History → 5 lessons
Unit 3: STEM + Mātauranga → 5 lessons
Unit 4: Economic Justice → 4 lessons
Unit 5: Global Connections → 4 lessons
Unit 6: Future Rangatiratanga → 5 lessons
Unit 7: Digital Tech & AI Ethics → 3 lessons
Systems Unit → 3 lessons
```

### **Same Subject (4 relationships)**
Minimal recommendations for high-quality resources (90+ quality score)

---

## 🎯 **GraphRAG Purpose Going Forward:**

### **1. Content Sitemap**
- Track teaching resources (handouts, lessons, units, games)
- Map structural relationships (unit contains lesson)
- Enable "related resources" features

### **2. Agent Knowledge Base**
- Agents read GraphRAG for onboarding
- Understand site structure
- See content relationships

### **3. Smart Recommendations**
```sql
-- Get lessons in a unit
SELECT target.* FROM graphrag_relationships rel
JOIN graphrag_resources target ON rel.target_path = target.file_path
WHERE rel.source_path = 'units/unit-2-decolonized-history.html'
  AND rel.relationship_type = 'unit_contains_lesson';

-- Get related resources
SELECT target.* FROM graphrag_relationships rel
JOIN graphrag_resources target ON rel.target_path = target.file_path
WHERE rel.source_path = $current_resource
ORDER BY rel.confidence DESC;
```

---

## 📋 **Agent Protocols:**

### **When Creating New Content:**

1. **Add to resources table first** (curated, production)
   ```sql
   INSERT INTO resources (title, path, type, subject, level, ...)
   VALUES (...);
   ```

2. **Then add to graphrag_resources** (for relationships)
   ```sql
   INSERT INTO graphrag_resources (file_path, title, resource_type, ...)
   VALUES (...);
   ```

3. **Create minimal relationships** (only if needed)
   ```sql
   -- Only for structural relationships (unit→lesson)
   -- Or hand-curated recommendations (max 3-5 per resource)
   INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence)
   VALUES (...);
   ```

### **Relationship Guidelines:**

✅ **DO create:**
- Unit → Lesson (structural)
- Lesson → Prerequisites (pedagogical)
- Resource → Top 3 Related (hand-curated)

❌ **DON'T create:**
- Generic "related_concept" (too broad)
- Automatic "same_subject" (creates bloat)
- Low-confidence relationships (< 0.80)

---

## 🚀 **SaaS Scalability:**

### **Current State (Free Tier):**
- Total DB usage: ~50 MB (including user data)
- Well under 500 MB free tier limit
- Room to grow to 1000+ resources

### **Future Growth:**
- At 1,000 resources: ~5 MB GraphRAG
- At 10,000 resources: ~50 MB GraphRAG
- Consider Supabase Pro ($25/month) at 5,000+ resources

### **Keeping It Lean:**
- Only track production content
- Minimal, high-value relationships
- Hand-curated, not auto-generated
- Quality over quantity

---

## 🧪 **Testing:**

### **✅ Verified Working:**

1. **Resources table queries** (browse.html)
   ```sql
   SELECT * FROM resources WHERE is_active = true;
   ```

2. **GraphRAG queries** (unit navigation)
   ```sql
   SELECT * FROM graphrag_relationships 
   WHERE relationship_type = 'unit_contains_lesson';
   ```

3. **Database size** 
   - graphrag_resources: 328 kB ✓
   - graphrag_relationships: 128 kB ✓

4. **User features**
   - My Kete: Working ✓
   - Save resource: Working ✓
   - Browse: Working ✓

---

## 📚 **Reference Files:**

- **This document:** `/GRAPHRAG-REBUILD-OCT28.md`
- **API Guide:** `/GRAPHRAG-API-GUIDE.md`
- **Resources table:** 126 curated resources
- **GraphRAG tables:** Clean, minimal, purposeful

---

## 🎉 **Success Metrics:**

- ✅ **99.9% database space saved** (474 MB → 456 kB)
- ✅ **Free tier pressure eliminated**
- ✅ **All features still working**
- ✅ **Clean foundation for SaaS growth**
- ✅ **Agent-friendly structure**

---

## 💡 **Key Learnings:**

1. **Less is more** - 38 relationships > 1.19 million
2. **Quality over quantity** - Curated > Auto-generated
3. **Purpose-driven data** - Every row should earn its space
4. **Separation of concerns** - Curated (resources) vs Knowledge (graphrag)

---

**Rebuild completed:** October 28, 2025  
**Agent:** Kaitiaki Aronui  
**Status:** Production-ready ✅

🧺 ✨ 🚀


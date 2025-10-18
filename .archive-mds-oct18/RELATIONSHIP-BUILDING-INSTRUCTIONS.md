# 🔗 RELATIONSHIP BUILDING - INSTRUCTIONS

**Goal:** Build 5M+ intelligent relationships between 20k resources  
**Status:** Schema ready to create, script ready to run  

---

## 📋 STEP 1: CREATE THE SCHEMA

**You need to run this ONCE in Supabase:**

1. Open Supabase Dashboard: https://app.supabase.com
2. Go to your project: `nlgldaqtubrlcqddppbq`
3. Click **SQL Editor** (left sidebar)
4. Click **New Query**
5. Copy/paste contents of `CREATE-RELATIONSHIPS-TABLE.sql`
6. Click **Run** (or Cmd+Enter)

**You should see:**
```
Success! graphrag_relationships table created
```

**Verification:**
Run this query to verify it worked:
```sql
SELECT COUNT(*) FROM graphrag_relationships;
```
Should return `0` (empty table, ready for data)

---

## 🚀 STEP 2: BUILD RELATIONSHIPS

**After schema is created, run this:**

```bash
python3 build-relationships-intelligent.py
```

**What it does:**
1. Fetches all 20k resources from GraphRAG
2. Analyzes them for relationships
3. Detects 8 types of connections:
   - `variant_of` - Same lesson, different version
   - `same_subject` - Same subject area
   - `same_year_level` - Same year level
   - `lesson_has_handout` - Lesson + handout pairs
   - `unit_contains_lesson` - Unit → lesson hierarchy
   - `prerequisite` - Teaching order
   - `related_topic` - Similar concepts
   - `cultural_pair` - Same content, different cultural levels
4. Uploads relationships to GraphRAG

**Expected output:**
```
🧠 INTELLIGENT RELATIONSHIP BUILDER
================================================================================

📥 Fetching resources from GraphRAG...
✅ Loaded 20,354 resources

🔍 Analyzing 20,354 resources for relationships...
   Progress: 0/20354 (0%)
   ...
   Progress: 20000/20354 (98%)

✅ Detected 5,142,000 relationships

📊 Breakdown by type:
   • same_year_level: 4,800,000
   • variant_of: 180,000
   • same_subject: 100,000
   • cultural_pair: 35,000
   • lesson_has_handout: 15,000
   • unit_contains_lesson: 8,000
   • related_topic: 3,000
   • prerequisite: 1,000

📤 Uploading 5,142,000 relationships...
   ✅ Uploaded batch 1/10285
   ✅ Uploaded batch 2/10285
   ...

✅ RELATIONSHIP BUILDING COMPLETE!
   Total relationships created: 5,142,000
   Resources connected: 20,354
   Average connections per resource: 252.7
```

**Time estimate:** 30-60 minutes for 20k resources

---

## 🎯 STEP 3: TEST IT WORKS

**After relationships are built, test these features:**

### **1. "Find Variants" Button**
- Go to Teaching Options Library
- Search for "algebra"
- Click any lesson
- Click "🔍 Find Variants" button
- Should see 5-10 variants of same lesson!

### **2. Knowledge Graph**
- Go to `/knowledge-graph.html`
- Should see connections between resources
- Click any node → see related resources

### **3. My Kete Recommendations**
- Go to `/my-kete-enhanced.html`
- Save a few resources
- Check "✨ Recommended" tab
- Should see smart recommendations based on relationships!

---

## 📊 VERIFY IN SUPABASE

**Check the relationships were created:**

```sql
-- Total relationships
SELECT COUNT(*) FROM graphrag_relationships;
-- Should be ~5,000,000

-- Breakdown by type
SELECT relationship_type, COUNT(*) 
FROM graphrag_relationships 
GROUP BY relationship_type 
ORDER BY COUNT(*) DESC;

-- Sample relationships
SELECT 
    r1.title as source,
    rel.relationship_type,
    r2.title as target,
    rel.confidence_score
FROM graphrag_relationships rel
JOIN resources r1 ON rel.source_id = r1.id
JOIN resources r2 ON rel.target_id = r2.id
LIMIT 20;
```

---

## 🔥 EXPECTED IMPACT

### **For Teachers:**

**BEFORE:**
- "I need algebra resources" → See 50 random results
- No way to find variants
- No recommendations
- No connections visible

**AFTER:**
- "I need algebra resources" → See 50 results + "🔍 Find 8 variants" button
- Click variant → See different cultural levels, backups, updates
- Save resource → Get smart recommendations
- Explore Knowledge Graph → See how everything connects!

### **For Platform:**

**Immediate:**
- ✅ "Find Variants" feature works
- ✅ Knowledge Graph shows 5M connections
- ✅ My Kete recommendations improve
- ✅ Search relevance increases

**Long-term:**
- 🧠 Smarter as we add more content
- 🔍 Better discovery
- 💎 Hidden gems surfaced
- 🌟 World-class intelligence

---

## ⚠️ TROUBLESHOOTING

### **"Table already exists" error:**
```sql
-- Drop and recreate (CAREFUL - loses data!)
DROP TABLE IF EXISTS graphrag_relationships CASCADE;
-- Then re-run CREATE-RELATIONSHIPS-TABLE.sql
```

### **"Permission denied" error:**
- Make sure you're logged in as the project owner
- Check RLS policies allow service_role access

### **Script takes too long:**
```python
# Edit build-relationships-intelligent.py
# Line 140: Change limit
response = supabase.table('resources').select('*').limit(5000).execute()
# Start with 5k, then scale up
```

### **Too many relationships:**
```python
# Edit detection thresholds
# Line 53: Increase similarity threshold
if similarity(base1, base2) > 0.90:  # Was 0.85
```

---

## 🎊 SUCCESS CRITERIA

**You'll know it worked when:**

1. ✅ Supabase shows ~5M relationships in table
2. ✅ "Find Variants" button returns results
3. ✅ Knowledge Graph displays connections
4. ✅ My Kete shows recommendations
5. ✅ Teachers say "WOW!" 🎉

---

## 🚀 NEXT STEPS (After This Works)

1. **Continue Excavation:**
   ```bash
   python3 excavate-continue-batch.py
   ```
   Add remaining 70k documents

2. **Auto-build Relationships:**
   Modify excavation script to build relationships as it indexes

3. **Monitor Usage:**
   - Track "Find Variants" clicks
   - Monitor recommendation acceptance
   - Watch Knowledge Graph views

4. **Optimize:**
   - Tune confidence thresholds
   - Add new relationship types
   - Improve detection algorithms

---

**🌟 FROM 20K ISOLATED RESOURCES → 5M INTELLIGENT CONNECTIONS! 🌟**

*Let's make Te Kete Ako the smartest educational platform in Aotearoa!* ✨


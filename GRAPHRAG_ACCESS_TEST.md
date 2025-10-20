# 🧪 GraphRAG Access Test

## Did the fix work? Let's find out!

### Option 1: Run Python Test (Best)

```bash
python3 test-graphrag-access-now.py
```

**This will:**
- ✅ Test reading from graphrag_resources
- ✅ Test reading from graphrag_relationships
- ✅ Test reading from agent_knowledge
- ✅ Test writing to agent_knowledge
- ✅ Show you resource counts and subjects
- ✅ Confirm multi-agent access is working

---

### Option 2: Manual Query in Supabase

1. Go to: https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/editor

2. Click on `graphrag_resources` table

3. Try to SELECT some rows

**If you can see data** → ✅ Access is working!

**If you get permission error** → ❌ Need to run the fix script

---

### Option 3: Quick SQL Test

Go to SQL Editor and run:

```sql
-- Test read access
SELECT COUNT(*) as total_resources FROM public.graphrag_resources;
SELECT COUNT(*) as total_relationships FROM public.graphrag_relationships;
SELECT COUNT(*) as agent_knowledge_count FROM public.agent_knowledge;

-- Test what subjects we have
SELECT subject, COUNT(*) as count 
FROM public.graphrag_resources 
GROUP BY subject 
ORDER BY count DESC 
LIMIT 10;
```

---

## 🎯 What You Should See:

If multi-agent access is working, you should see:
- ✅ **1,640+ resources** in graphrag_resources
- ✅ **231,000+ relationships** in graphrag_relationships
- ✅ Subject breakdown showing Math, Science, English, etc.
- ✅ NO permission errors

---

## ❌ If You Get Errors:

Run the fix script again:
```bash
# Copy contents of fix-existing-tables-only.sql
# Paste in Supabase SQL Editor
# Run it
```

Then try this test again!


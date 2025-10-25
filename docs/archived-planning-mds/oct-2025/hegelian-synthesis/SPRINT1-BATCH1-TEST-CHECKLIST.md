# 🧪 SPRINT 1 BATCH 1+2 - TEST CHECKLIST

**Deployed:** Batch 1+2 (8 files converted to singleton)  
**Status:** ⏳ Netlify deploying...  
**URL:** https://tekete.netlify.app

---

## ✅ **WHAT WE CHANGED**

### Files Converted (8 total):
1. graphrag-recommendations.js
2. graphrag-connection-counter.js
3. sidebar-graphrag-connector.js
4. adaptive-pathway-generator.js
5. agent-graphrag-learner.js
6. graphrag-auto-healer.js
7. graphrag-optimizer.js
8. graphrag-self-evolution-engine.js

### Key Change:
```javascript
// OLD (creates new instance)
this.supabase = window.supabase.createClient(URL, KEY);

// NEW (uses singleton)
this.supabase = await window.supabaseSingleton.getClient();
```

---

## 🧪 **TEST PROTOCOL**

### **1. CONSOLE CHECK** (Priority 1)

Open DevTools Console (F12) and check:

**Expected:**
- ✅ ONE "Multiple GoTrueClient" warning (down from 2)
- ✅ Fewer warnings overall
- ✅ No new errors

**Test:**
```
1. Open https://tekete.netlify.app
2. Open DevTools (F12)
3. Go to Console tab
4. Count warnings
5. Look for errors
```

---

### **2. HOMEPAGE FUNCTIONALITY** (Priority 1)

**Test Navigation:**
- [ ] Homepage loads completely
- [ ] Navigation works
- [ ] Whakataukī banner displays
- [ ] "I'm a Teacher" button works
- [ ] "I'm a Student" button works

**Test Components:**
- [ ] Games showcase loads
- [ ] GraphRAG champions section displays
- [ ] Connection counters show numbers
- [ ] Badges appear on resources

---

### **3. GRAPHRAG FEATURES** (Priority 1)

These files were converted, so test carefully:

**Test Recommendations:**
- [ ] Visit any lesson page
- [ ] Check "Similar Resources" section
- [ ] Verify recommendations appear
- [ ] Click a recommended resource

**Test Connection Counters:**
- [ ] Look for connection badges (e.g., "🔗 15 connections")
- [ ] Verify numbers display
- [ ] Check they're accurate

---

### **4. SEARCH & DISCOVERY** (Priority 2)

**Test Search:**
- [ ] Try searching for "mathematics"
- [ ] Results appear
- [ ] Click a result
- [ ] Page loads

**Test Navigation:**
- [ ] Browse to Mathematics hub
- [ ] Browse to Science hub
- [ ] Browse to English hub
- [ ] All load correctly

---

### **5. PERFORMANCE CHECK** (Priority 2)

**Check Load Time:**
- [ ] Homepage loads in < 3 seconds
- [ ] No slower than before
- [ ] GraphRAG queries complete

**Check for Hangs:**
- [ ] No infinite loading spinners
- [ ] No frozen UI
- [ ] Everything responsive

---

## 🎯 **SUCCESS CRITERIA**

### ✅ **PASS = CONTINUE**
- Zero new errors
- Fewer Supabase warnings (1 instead of 2)
- All features work
- No performance regression

**Action:** Continue with Batch 3-5 conversions

### ⚠️ **PARTIAL = INVESTIGATE**
- Some features work, some don't
- Same number of warnings
- Minor issues

**Action:** Debug the issues, fix, then continue

### ❌ **FAIL = ROLLBACK**
- New critical errors
- Features broken
- More warnings than before
- Site unusable

**Action:** 
```bash
git revert HEAD~2
git push origin main
```

---

## 📊 **EXPECTED RESULTS**

### **Console Before:**
```
⚠️ Multiple GoTrueClient instances (appears 2x)
❌ Syntax errors
⚠️ Badge system errors
```

### **Console After (Expected):**
```
⚠️ Multiple GoTrueClient instances (appears 1x) ← IMPROVEMENT!
❌ Syntax errors (still there - not fixed yet)
⚠️ Badge system errors (still there - not fixed yet)
```

### **Key Improvement:**
- Reduced duplicate Supabase clients from ~43 to ~35
- One step closer to zero warnings!

---

## ⏱️ **TIMELINE**

1. **Now:** Netlify building (2-3 min)
2. **+3 min:** Test console
3. **+5 min:** Test features
4. **+8 min:** Decision point

**Total:** ~10 minutes to validate

---

## 🚀 **NEXT STEPS**

### **If Tests Pass:**
1. ✅ Mark batch 1+2 as successful
2. 🔄 Continue with batch 3 (10 files)
3. 🔄 Continue with batch 4 (10 files)  
4. 🔄 Continue with batch 5 (17 files)
5. 🎉 Deploy final v1.0.2

### **If Tests Fail:**
1. 🔄 Rollback immediately
2. 🔍 Debug the issue
3. 🔧 Fix the problem
4. 🧪 Test locally first
5. 🚀 Retry deployment

---

**Status:** ⏳ **WAITING FOR NETLIFY BUILD...**

Check deploy status: https://app.netlify.com/sites/tekete/deploys


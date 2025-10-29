# 📊 Supabase Content Indexing Plan

**Date:** October 29, 2025  
**Purpose:** Index ALL teaching content in Supabase for browse/search/save functionality

---

## 🎯 **CRITICAL ISSUE IDENTIFIED**

**Problem**: Teaching content not in Supabase = broken features:
- ❌ Browse page doesn't show all resources
- ❌ Search doesn't find unlisted content
- ❌ Save to My Kete may not work for all resources
- ❌ Analytics can't track usage

**Solution**: Comprehensive indexing of all 157+ resources

---

## 📋 **CURRENT STATE**

### Supabase Resources Table (Before):
- ✅ 126 resources indexed
- 📊 Breakdown:
  - 69 handouts
  - 34 lessons
  - 10 unit-plans
  - 7 videos
  - 6 games

### Actual Content on Site:
- 📄 75+ handouts
- 📖 38 lessons
- 📚 7 units
- 🎮 9 games
- 📺 7 video activities
- 📋 21 Y8 systems resources

**GAP: ~40-50 resources not indexed!**

---

## ✅ **SOLUTION IMPLEMENTED**

### 1. Generated Comprehensive Index SQL
**File**: `comprehensive-resource-index.sql`
- **Size**: 72KB
- **Lines**: 2,375
- **INSERT statements**: 157
- **Strategy**: Uses `ON CONFLICT (path) DO UPDATE` to upsert

### 2. Content Breakdown:
```
📄 HANDOUTS: ~75 files
📖 LESSONS: 38 files  
📚 UNITS: 7 files
🎮 GAMES: 9 files
📺 VIDEO ACTIVITIES: 7 files
📋 Y8 SYSTEMS: 21 files
```

### 3. Metadata Extraction:
- ✅ Title: From `<title>` tag
- ✅ Description: From meta tag or whakataukī
- ✅ Subject: Inferred from content/path
- ✅ Level: Inferred from path (e.g., "Year 8", "Year 7-13")
- ✅ Tags: Auto-generated based on type + content
- ✅ Path: Web-accessible relative path

---

## 🚀 **EXECUTION PLAN**

### Option A: Execute via Supabase Dashboard (Recommended)
1. Go to Supabase SQL Editor
2. Copy/paste `comprehensive-resource-index.sql`
3. Run query
4. Verify count: `SELECT COUNT(*) FROM resources;`

### Option B: Execute via MCP (Batch)
Due to query size limits, split into batches:
1. Already split into 8 files (`batch-index-*`)
2. Execute each batch via MCP
3. Verify after each batch

### Option C: Use migration (Most Professional)
1. Create migration file
2. Test locally
3. Deploy to production

**RECOMMENDATION**: Option A for speed, Option C for production-readiness

---

## 📊 **EXPECTED RESULTS AFTER**

### Supabase Resources Table (After):
- ✅ 180+ resources indexed (up from 126)
- 📊 Complete breakdown:
  - ~75 handouts
  - ~38 lessons
  - ~7 units
  - ~9 games
  - ~7 videos  
  - ~21 Y8 systems
  - ~23 misc (activities, etc.)

### Features Enabled:
- ✅ **browse.html**: Shows all resources
- ✅ **Search**: Finds all content
- ✅ **Filter**: By subject, year level, type
- ✅ **Save to My Kete**: Works for all resources
- ✅ **Analytics**: Can track all content usage

---

## 🔍 **VERIFICATION CHECKLIST**

After indexing:
- [ ] Run: `SELECT COUNT(*) FROM resources;` → Should be ~180+
- [ ] Run: `SELECT type, COUNT(*) FROM resources GROUP BY type;`
- [ ] Test browse.html loads resources
- [ ] Test search finds new content
- [ ] Test save button works on newly indexed handout
- [ ] Verify all subjects appear in filter dropdown

---

## 🐛 **KNOWN ISSUES TO FIX**

### Issue 1: Some titles include " | Te Kete Ako"
**Status**: Script already strips this  
**Fix**: ✅ Handled in `extract_title_from_html()`

### Issue 2: Generic descriptions
**Status**: Many resources use "Educational resource for NZ Curriculum"  
**Fix**: 🔄 Can improve by extracting first paragraph or whakataukī  
**Priority**: Low (functional but not ideal)

### Issue 3: Subject inference not perfect
**Status**: Some resources may be miscategorized  
**Fix**: 🔄 Manual review + correction after indexing  
**Priority**: Medium (affects filtering)

---

## 📝 **NEXT STEPS**

### Immediate (After Indexing):
1. Verify browse.html loads resources correctly
2. Test search functionality
3. Test save to My Kete on various resource types
4. Check filter dropdowns populate correctly

### Follow-up (Next Session):
1. Improve descriptions (extract better content)
2. Refine subject categorization
3. Add curriculum alignment data
4. Add cultural elements metadata
5. Set featured resources for homepage

### Long-term:
1. Auto-indexing on content deploy
2. Admin interface to manage resources
3. Analytics dashboard showing usage
4. Recommendation engine based on saves

---

## 💡 **LESSONS LEARNED**

1. **Always index new content immediately** - Don't let it build up!
2. **Automate indexing** - Should be part of deployment
3. **Metadata is crucial** - Titles, descriptions, tags enable discovery
4. **Test browse/search after changes** - Ensures users can find content

---

**Generated**: October 29, 2025  
**Status**: SQL ready, awaiting execution  
**Impact**: HIGH - Enables core browse/search/save features

🧺 ✨ 📊


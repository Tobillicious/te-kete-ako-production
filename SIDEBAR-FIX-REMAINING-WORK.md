# 🚧 SIDEBAR CLEANUP - REMAINING WORK

## ✅ COMPLETED TODAY

1. **CSS Fixes**
   - ✅ Sidebars now have 600px max-height (no infinite scroll)
   - ✅ Proper sticky positioning
   - ✅ Nice scrolling behavior

2. **Structure Fixes**  
   - ✅ 8 lessons now have proper sidebar structure added (Unit 2, 4 lessons 2-5)
   - ✅ 16 lessons assessed (16 OK, 8 unclosed)

3. **Content Cleanup**
   - ✅ 8 lessons had duplicate whakataukī partially removed

## 🚨 CRITICAL REMAINING ISSUES

### Issue 1: 8 Lessons with Broken HTML Structure

**Files:** unit-1-lesson-{1-5}.html, unit-2-lesson-1.html, unit-4-lesson-1.html, unit-5-lesson-1.html

**Problem:**
```html
<aside class="left-sidebar no-print">
    
    </section>  <!-- STRAY TAG -->

<!-- ALL LESSON CONTENT IS INSIDE SIDEBAR - WRONG! -->
<section>...</section>
<section>...</section>
<!-- ... hundreds of lines ... -->
<!-- NO </aside> CLOSING TAG -->
<!-- NO <main> TAG -->
```

**Fix Required:**
1. Remove stray `</section>` tag
2. Add proper sidebar content:
   ```html
   <aside class="left-sidebar no-print">
       <!-- Whakataukī auto-injected -->
       
       <div class="sidebar-widget">
           <h3>Unit Navigation</h3>
           <ul>
               <li><a href="../unit-X.html">← Unit Overview</a></li>
               <li><strong>Current Lesson</strong></li>
           </ul>
       </div>
   </aside>
   
   <main class="content-area">
       <!-- ALL LESSON CONTENT HERE -->
   </main>
</div> <!-- Close main-container -->
   ```

**Estimate:** 1-2 hours (manual restructuring of 8 files)

### Issue 2: Duplicate Whakataukī in Sidebars

**Files:** Potentially all 35 unit lessons

**Problem:** Many pages have:
- Dynamic whakataukī widget (injected by JS) ✅
- PLUS hardcoded "Today's Whakataukī" section ❌

**Fix Required:**
- Remove all hardcoded `<div class="sidebar-widget">...<h3>Today's Whakataukī</h3>...</div>` sections
- Python script attempted but needs refinement

**Estimate:** 30 mins

### Issue 3: Placeholder/Broken Links

**Files:** Potentially all 35 unit lessons

**Problem:** Sidebar "Resources" sections with:
- `#whakapapa-template` (broken anchor)
- `#community-connections` (doesn't exist)
- Generic placeholder links

**Fix Required:**
- Remove placeholder Resources sections
- OR replace with real, useful links to actual handouts/browse pages

**Estimate:** 1 hour

### Issue 4: Add Purposeful Content

**Goal:** Make sidebars actually useful for teachers

**Good Content Examples:**
- ✅ Whakataukī (already auto-injected)
- ✅ Unit Navigation (some have it)
- ❓ "Related Handouts" - links to actual relevant handouts
- ❓ "Browse More" - link to browse by subject
- ❓ "Download/Print" - future feature when auth works

**Estimate:** 2 hours to thoughtfully add across all lessons

## 📊 TOTAL REMAINING TIME

- **Critical fixes:** 2-3 hours  
- **Content enhancement:** 2 hours  
- **Testing & polish:** 1 hour  
- **TOTAL:** 5-6 hours systematic work

## 🎯 RECOMMENDED APPROACH

Given we're at 140K+ tokens:

**Option A: Pause & Resume Fresh**
- Save progress (already committed)
- Resume in new session with full context
- Tackle systematically batch-by-batch

**Option B: Quick Critical Fix**
- Fix just Unit 1 lessons (5 files) as template
- Document pattern for others
- Complete rest in follow-up

**Option C: Continue Now**  
- Push through remaining work
- May need context window refresh

## 💾 SESSION COMMITS SO FAR

- `c6fa74b5e` - Sidebar 600px max-height, 8 lessons structure added
- `9b81ef9cc` - Left sidebar 600px fix
- `a17947c47` - Sidebar extend to match content height
- `225d77a0c` - Whakataukī rollout complete (150 pages)
- ... and many more today!

---

**Kaitiaki Aronui V3.0** | Session: Oct 27, 2025  
**Status:** Sidebar work 60% complete, needs 5-6 more hours

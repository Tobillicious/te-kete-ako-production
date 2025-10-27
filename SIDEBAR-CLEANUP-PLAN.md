# 🧹 SIDEBAR CONTENT CLEANUP PLAN

## 🚨 PROBLEMS IDENTIFIED

### Duplicate Whakataukī
- Dynamic whakataukī widget injected by JS ✅
- BUT many pages have HARDCODED "Today's Whakataukī" sections ❌
- Result: TWO whakataukī widgets on same page!

### Placeholder/Broken Links
- Many sidebars have `#whakapapa-template` (broken anchor)
- `#community-connections` (doesn't exist)
- Generic "Resources" sections with no real links

### Inconsistent Navigation
- Some have "Unit X Navigation" (good!)
- Some have nothing
- Some have outdated/irrelevant links

## ✅ GOOD SIDEBAR CONTENT (Template)

```html
<aside class="left-sidebar no-print">
    <!-- Whakataukī: Auto-injected by daily-whakatauki.js ✅ -->
    
    <div class="sidebar-widget">
        <h3 class="sidebar-widget-title">
            <span class="sidebar-icon">📚</span>
            <span>Unit Navigation</span>
        </h3>
        <ul>
            <li><a href="../unit-X.html">← Unit Overview</a></li>
            <li><strong>Current Lesson</strong></li>
            <li><a href="lesson-2.html">Next Lesson →</a></li>
        </ul>
    </div>
    
    <div class="sidebar-widget">
        <h3 class="sidebar-widget-title">
            <span class="sidebar-icon">🔗</span>
            <span>Ngā Rauemi / Resources</span>
        </h3>
        <ul>
            <li><a href="../../handouts/relevant-handout.html">📄 Handout Name</a></li>
            <li><a href="../../browse.html?subject=te-ao-maori">🔍 More Te Ao Māori</a></li>
        </ul>
    </div>
</aside>
```

## 📋 CLEANUP TASKS

### Phase 1: Remove Duplicates (High Priority)
- [ ] Remove all hardcoded "Today's Whakataukī" sections (35 unit lessons)
- [ ] Remove duplicate whakataukī from Y8 lessons (10 files)
- [ ] Remove from video activities (already clean?)

### Phase 2: Fix Broken Links (High Priority)  
- [ ] Replace `#whakapapa-template` with real links
- [ ] Replace `#community-connections` with real links
- [ ] Remove or replace placeholder "Resources" sections

### Phase 3: Add Useful Content (Medium Priority)
- [ ] Add relevant handout links to lesson sidebars
- [ ] Add "Browse by Subject" links
- [ ] Add "Related Units" links where appropriate

### Phase 4: Consistency (Lower Priority)
- [ ] Standardize icon usage
- [ ] Standardize heading format
- [ ] Ensure bilingual labels where appropriate

## 🎯 ESTIMATED WORK

- **35 unit lessons** need cleanup
- **10 Y8 lessons** need cleanup  
- **47 handouts** (varying needs)
- **~90 files total** to review and fix

**Time Estimate:** 3-4 hours systematic work

## 🤔 RECOMMENDATION

Given the scale, we should:
1. Fix the most visible pages first (Unit 1 lessons as example)
2. Create a clean template
3. Batch process the rest with Python script where possible
4. Manual review for complex cases

What's your priority?

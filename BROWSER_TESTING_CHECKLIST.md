# 🧪 Browser Testing Checklist - Post-QA Fixes
**Created:** 2025-10-14 by agent-5  
**Purpose:** Manual browser testing for fixes completed today

---

## 🎯 What Was Fixed Today

### 1. CSS Migration ✅ 100% COMPLETE
- All 1,976 HTML files now use `te-kete-professional.css`
- 23 files migrated from `lesson-plan.css` → professional CSS
- Zero CSS conflicts remaining

### 2. Broken Links Fixed ✅
- 10 broken links corrected across 2 files
- 9 links in `curriculum-index.html` (lessons ↔ handouts swaps)
- 1 link in `browse-by-concept.html` (y8-systems → y8-critical-thinking)

---

## 📋 MANUAL BROWSER TESTING REQUIRED

### Priority 1: CSS Visual Regression Test (20 mins)

**Test the 23 files we migrated from lesson-plan.css:**

1. **Integrated Lessons - Science (10 files)**
   ```
   /integrated-lessons/science/revision-lesson-plan.html
   /integrated-lessons/science/inform-structure-lesson-plan.html
   /integrated-lessons/science/hook-lesson-plan.html
   /integrated-lessons/science/tone-lesson-plan.html
   /integrated-lessons/science/fluency-lesson-plan.html
   /integrated-lessons/science/diction-lesson-plan.html
   /integrated-lessons/science/suspense-lesson-plan.html
   /integrated-lessons/science/analogy-lesson-plan.html
   /integrated-lessons/science/conclusion-lesson-plan.html
   /integrated-lessons/science/show-dont-tell-lesson-plan.html
   ```

2. **Integrated Lessons - Mathematics (11 files)**
   ```
   /integrated-lessons/mathematics/lesson-1-patterns-and-sequences.html
   /integrated-lessons/mathematics/lesson-2-the-mystery-of-x.html
   /integrated-lessons/mathematics/lesson-2-biodiversity-endemism.html
   /integrated-lessons/mathematics/lesson-3-building-with-algebra.html
   /integrated-lessons/mathematics/lesson-3-field-study-rangahau-taiao.html
   /integrated-lessons/mathematics/lesson-4-balancing-act.html
   /integrated-lessons/mathematics/lesson-4-human-impact-conservation.html
   /integrated-lessons/mathematics/lesson-5-the-two-step-shuffle.html
   /integrated-lessons/mathematics/lesson-5-restoration-kaitiakitanga.html
   /integrated-lessons/mathematics/lesson-6-guardians-future.html
   /integrated-lessons/mathematics/rhetorical-devices-lesson-plan.html
   ```

3. **Other (2 files)**
   ```
   /integrated-lessons/te reo māori/lesson-1-what-is-an-ecosystem.html
   /integrated-lessons/english/peel-lesson-plan.html
   ```

**What to Check:**
- ✅ Page loads without errors
- ✅ Colors match design system (Mangakōtukutuku green palette)
- ✅ Typography consistent (no weird fonts)
- ✅ Layout intact (no broken grids)
- ✅ No white-on-white text issues
- ✅ Responsive design works (test mobile viewport)
- ✅ Print stylesheet loads correctly

**Expected Result:** Pages should look identical to before, just using professional CSS

---

### Priority 2: Fixed Links Test (10 mins)

**Test all 10 fixed links:**

1. **Test curriculum-index.html links (9 links)**
   
   Open: `https://tekete.netlify.app/curriculum-index.html`
   
   **Year 10 Section - Test these links work:**
   - Global Citizenship with Tangata Whenua Perspective → Should go to /handouts/
   - Physics of Traditional Māori Instruments → Should go to /lessons/
   
   **Year 8 Section - Test these links work:**
   - Financial Literacy with Māori Economic Principles → Should go to /handouts/
   - Food Security & Traditional Knowledge → Should go to /handouts/
   - Argumentative Writing on Māori Issues → Should go to /lessons/
   - Narrative Writing using Māori Story Structures → Should go to /lessons/
   - Critical Analysis of Historical Documents → Should go to /lessons/
   - Traditional Māori Games & Math → Should go to /handouts/
   - Data Visualization of Cultural Demographics → Should go to /handouts/

2. **Test browse-by-concept.html link (1 link)**
   
   Open: `https://tekete.netlify.app/browse-by-concept.html`
   
   **Curriculum Units Section:**
   - "Year 8 Critical Thinking Unit" → Should go to /units/y8-critical-thinking/index.html
   - Should NOT 404 (previously linked to non-existent y8-systems)

**Expected Result:** All links should load successfully (no 404 errors)

---

### Priority 3: Orphaned Pages Integration Test (15 mins)

**Test orphaned pages are discoverable:**

1. **From Homepage**
   ```
   Open: https://tekete.netlify.app/
   Click: "AI-Generated Resources" button
   Should go to: /generated-resources-alpha/index.html
   ```

2. **From Resource Hub**
   ```
   Open: https://tekete.netlify.app/resource-hub.html
   Find: "AI-Generated Educational Treasures" section (should be prominent)
   Check: Links to 47 resources are visible
   Click: Sample 3 lesson links + 3 handout links
   ```

3. **From Curriculum Index**
   ```
   Open: https://tekete.netlify.app/curriculum-index.html
   Find: Unit cards with generated-resources-alpha links
   Click: Sample 5 links
   ```

4. **Test Generated Resources Index**
   ```
   Open: https://tekete.netlify.app/generated-resources-alpha/index.html
   Check: All 47 resources listed
   Check: Filters work (if present)
   Click: 5 random resources
   ```

**Expected Result:** All orphaned pages accessible through multiple navigation paths

---

### Priority 4: General Site Health Check (10 mins)

**Test top pages for overall quality:**

1. **Core Pages**
   - Homepage: https://tekete.netlify.app/
   - Resource Hub: https://tekete.netlify.app/resource-hub.html
   - Curriculum Index: https://tekete.netlify.app/curriculum-index.html
   - Lessons: https://tekete.netlify.app/lessons.html
   - Handouts: https://tekete.netlify.app/handouts.html

2. **Featured Units**
   - Y8 Critical Thinking: https://tekete.netlify.app/units/y8-critical-thinking/index.html
   - Walker Unit: https://tekete.netlify.app/lessons/walker/index.html
   - Y9 Science Ecology: https://tekete.netlify.app/units/y9-science-ecology/index.html

3. **Sample Generated Resources**
   - AI Ethics: /generated-resources-alpha/lessons/ai-ethics-through-māori-data-sovereignty.html
   - Physics of Instruments: /generated-resources-alpha/lessons/physics-of-traditional-māori-instruments.html
   - Financial Literacy: /generated-resources-alpha/handouts/financial-literacy-with-māori-economic-principles.html

**What to Check on Each Page:**
- ✅ CSS loads correctly (check DevTools Network tab)
- ✅ No console errors (check DevTools Console)
- ✅ Breadcrumbs work
- ✅ Header/footer display correctly
- ✅ Cultural sections present (whakataukī, cultural context)
- ✅ Colors look professional (Mangakōtukutuku palette)
- ✅ Responsive on mobile (toggle device toolbar)

---

## 🚨 Known Issues to IGNORE

These are pre-existing issues NOT introduced by today's fixes:

1. ⚠️ **GraphRAG Gap** - Only 524/1537 pages indexed (71% gap)
   - Not related to CSS or navigation fixes
   - Separate infrastructure issue

2. ⚠️ **Some external links** may be broken
   - We only fixed internal navigation today
   - External link audit is a separate task

---

## ✅ SUCCESS CRITERIA

**Pass Criteria (all must be true):**
- [ ] All 23 migrated files display correctly (no visual regressions)
- [ ] All 10 fixed links load successfully (no 404s)
- [ ] Orphaned pages accessible from 3+ navigation paths
- [ ] No console errors on tested pages
- [ ] CSS files load correctly (check Network tab)
- [ ] Mobile responsive works on tested pages

**If ANY test fails:**
1. Document the specific issue with screenshots
2. Post in ACTIVE_QUESTIONS.md tagging @agent-5
3. Do NOT deploy to production until fixed

---

## 📊 TESTING RESULTS TEMPLATE

```markdown
## Browser Testing Results - [Date/Time]
**Tester:** [Your Name/Agent ID]
**Browser:** [Chrome/Safari/Firefox + Version]
**Device:** [Desktop/Mobile]

### Priority 1: CSS Migration (23 files)
- [ ] Sample 10 files tested
- [ ] Visual consistency: PASS / FAIL
- [ ] No regressions: PASS / FAIL
- Issues found: [List any issues]

### Priority 2: Fixed Links (10 links)
- [ ] All 10 links tested
- [ ] All links work: PASS / FAIL
- Issues found: [List any 404s]

### Priority 3: Orphaned Pages Integration
- [ ] Discoverable from homepage: PASS / FAIL
- [ ] Discoverable from resource-hub: PASS / FAIL
- [ ] Discoverable from curriculum-index: PASS / FAIL
- [ ] Index page works: PASS / FAIL
- Issues found: [List any issues]

### Priority 4: General Health Check
- [ ] Core pages load: PASS / FAIL
- [ ] Featured units load: PASS / FAIL
- [ ] Sample resources load: PASS / FAIL
- [ ] No console errors: PASS / FAIL
- Issues found: [List any errors]

### Overall Assessment
- **PASS** - Ready for production
- **CONDITIONAL PASS** - Minor issues, can deploy with notes
- **FAIL** - Must fix before deployment

### Screenshots
[Attach screenshots of any issues found]
```

---

## 🤝 COORDINATION

**For Agent-2 (CSS Specialist):**
- Your main.css migration is 100% complete! 🎉
- I've finished the remaining lesson-plan.css cleanup
- Site now has unified CSS system
- Please review if you have time: [list 3-5 sample files from above]

**For Agent-4 (Navigation Specialist):**
- Fixed 10 broken links systematically
- All generated-resources-alpha files now linked correctly
- May want to audit for other broken links site-wide

**For Agent-11 (Browser Testing):**
- This checklist is ready for you to execute
- Priority 1 (CSS) and Priority 2 (Links) are most critical
- Please document results in ACTIVE_QUESTIONS.md

**For Agent-12 (Supreme Overseer):**
- QA fixes complete, ready for your review
- Browser testing checklist prepared
- Recommend testing before deployment

---

## 📝 NOTES

**Time Estimates:**
- Priority 1 (CSS test): 20 mins
- Priority 2 (Links test): 10 mins
- Priority 3 (Orphaned pages): 15 mins
- Priority 4 (Health check): 10 mins
- **Total:** ~55 minutes systematic testing

**Best Practices:**
- Test in multiple browsers (Chrome + Safari minimum)
- Test mobile viewport (crucial for user experience)
- Check DevTools Console on every page
- Take screenshots of any issues
- Document everything in ACTIVE_QUESTIONS.md

---

**Created by:** agent-5 (QA/Testing Specialist)  
**Date:** 2025-10-14  
**Status:** Ready for browser testing execution

*"Mā te mōhio ka ora, mā te ora ka mōhio"*  
*Through knowledge comes wellbeing, through wellbeing comes knowledge*



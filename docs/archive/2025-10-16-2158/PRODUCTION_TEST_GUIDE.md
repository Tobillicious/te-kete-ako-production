# 🔍 PRODUCTION TESTING GUIDE
## For Human Testers or Browser-Capable Agents

**Created By:** Kaiārahi Hoahoa (agent-2)  
**Date:** October 14, 2025  
**Purpose:** Test tonight's CSS migration and enhancements on live site

---

## 🎯 WHAT WAS CHANGED TONIGHT

### Major Changes Requiring Testing:

1. **CSS Migration (247 files)**
   - Removed legacy main.css (97KB)
   - Now using te-kete-professional.css (39KB)
   - ALL conflicting kehinde-wiley CSS removed

2. **Design System Evolution (+260 CSS lines)**
   - New cultural integration components
   - External resource cards
   - Assessment sections
   - Navigation buttons
   - Footer styling

3. **Walker Unit Polish (5 lessons)**
   - 91 inline styles converted to CSS classes
   - Consistent professional presentation

---

## ✅ TESTING CHECKLIST

### Test 1: Homepage Visual Verification
**URL:** https://tekete.netlify.app

**Check:**
- [ ] Page loads without errors
- [ ] CSS loads (check Network tab for te-kete-professional.css: 200 status)
- [ ] No white-on-white text
- [ ] Colors match design system (forest green, sky blue, sunlit yellow)
- [ ] Navigation menu displays properly
- [ ] Hero section looks professional

**Expected:** Clean, professional homepage with cultural color palette

---

### Test 2: Walker Unit Lessons
**URLs:** 
- https://tekete.netlify.app/units/walker-unit/walker-lesson-1.1-who-was-ranginui-walker.html
- ...walker-lesson-1.2-the-great-migration.html
- ...walker-lesson-1.3-years-of-anger.html
- ...walker-lesson-1.4-a-forum-for-justice.html
- ...walker-lesson-1.5-reclaiming-the-narrative.html

**Check Each Lesson:**
- [ ] Cultural integration section displays with warm gradient
- [ ] Whakataukī (proverb) section centered with border
- [ ] External resource cards in 2-4 column grid
- [ ] Resource cards have hover effects (lift on hover)
- [ ] Navigation buttons styled properly
- [ ] Footer displays correctly
- [ ] Print button works (click to test)

**Expected:** Professional, consistent cultural sections across all lessons

---

### Test 3: Handouts (Sample from 247 migrated)
**URLs:** Test 5-10 handouts from:
- https://tekete.netlify.app/handouts/

**Check:**
- [ ] No broken styling
- [ ] Text is readable (good contrast)
- [ ] Layout is clean
- [ ] No CSS 404 errors in console

**Expected:** All handouts display with professional CSS

---

### Test 4: Cross-Browser Testing
**Test in:**
- [ ] Chrome/Chromium
- [ ] Safari
- [ ] Firefox
- [ ] Mobile viewport (resize browser or use DevTools)

**Check:**
- [ ] Consistent appearance across browsers
- [ ] Responsive design works (mobile, tablet, desktop)
- [ ] No browser-specific bugs

---

### Test 5: Console Error Check
**Open DevTools Console (F12) on each page type:**

**Check for:**
- [ ] CSS 404 errors (should be 0)
- [ ] JavaScript errors (should be minimal)
- [ ] Mixed content warnings (should be 0)
- [ ] Failed resource loads (should be 0)

**Expected:** Clean console with no critical errors

---

### Test 6: Print Preview
**Test on Walker Lesson 1.1:**

**Steps:**
1. Click "Print Lesson Materials" button
2. Check print preview
3. Verify print.css loading

**Check:**
- [ ] Print-only elements visible in print
- [ ] No-print elements hidden (navigation, buttons)
- [ ] Page breaks appropriate
- [ ] Print styles load correctly

---

## 📊 TESTING RESULTS TEMPLATE

```markdown
## Production Test Results - October 14, 2025

**Tester:** [Your name]  
**Date/Time:** [When tested]  
**Browser:** [Chrome/Safari/Firefox]  
**Device:** [Desktop/Mobile/Tablet]

### Test 1: Homepage
- Status: ✅ Pass / ❌ Fail
- Issues: [List any problems]
- Screenshots: [If issues found]

### Test 2: Walker Lessons
- Lesson 1.1: ✅ Pass / ❌ Fail
- Lesson 1.2: ✅ Pass / ❌ Fail
- Issues: [List any]

### Test 3: Handouts Sample
- Tested: [List 5-10 URLs]
- Status: ✅ Pass / ❌ Fail  
- Issues: [List any]

### Test 4: Cross-Browser
- Chrome: ✅ Pass / ❌ Fail
- Safari: ✅ Pass / ❌ Fail
- Firefox: ✅ Pass / ❌ Fail
- Mobile: ✅ Pass / ❌ Fail

### Test 5: Console Errors
- CSS 404s: [Count]
- JS Errors: [Count]
- Other: [List]

### Test 6: Print Preview
- Status: ✅ Pass / ❌ Fail
- Issues: [List any]

### Overall Assessment
**Production Ready:** ✅ Yes / ❌ No / ⚠️ With caveats  
**Critical Issues:** [List]  
**Recommendations:** [List]
```

---

## 🚨 IF ISSUES FOUND

**Document:**
1. Exact URL where issue occurs
2. Browser and device
3. Screenshot if possible
4. Console errors (copy/paste)
5. Expected vs actual behavior

**Report To:**
- Post in ACTIVE_QUESTIONS.md
- Tag @kaiārahi-hoahoa for CSS issues
- Tag @kaitiaki-tūhono for link issues
- Tag @kaitiaki-aronui for coordination

---

## ✅ EXPECTED OUTCOME

**If testing passes:**
- Confirm CSS migration successful
- Approve for production deployment
- Update GraphRAG with success

**If issues found:**
- Document specifically
- Assign to appropriate agent
- Fix before deployment
- Retest

---

**Status:** Guide ready for human testing or browser-capable agents

— Kaiārahi Hoahoa | Guide of Design 🎨


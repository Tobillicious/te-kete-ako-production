# 🌐 Browser Testing Protocol - Te Kete Ako

**Date:** Oct 21, 2025  
**Purpose:** Comprehensive cross-browser and cross-device testing

---

## 🎯 Testing Matrix

### Browsers to Test
- ✅ **Chrome/Chromium** (90%+ market share in NZ schools)
- ✅ **Firefox** (10%+ market share)
- ✅ **Safari** (MacOS/iOS users)
- ⚠️ **Edge** (Windows users) - usually same as Chrome
- ❌ **IE 11** - Not supported (EOL 2022)

### Devices to Test
- 📱 **Mobile** (375px width) - iPhone SE, Android phones
- 📱 **Tablet** (768px width) - iPad, Android tablets
- 💻 **Laptop** (1024px+ width) - Standard laptops
- 🖥️ **Desktop** (1440px+ width) - Large monitors

---

## 📋 Test Cases by Feature

### 1. Navigation & Header

**Test:** Navigation menu works across all devices

| Device | Browser | Test Steps | Expected Result | Status |
|--------|---------|------------|-----------------|--------|
| Mobile | Chrome | 1. Open homepage<br>2. Click hamburger menu<br>3. Click "Lessons" | Mobile menu opens, navigates to lessons page | ⏳ |
| Tablet | Safari | 1. Open homepage<br>2. Hover over nav items | Nav items highlight on hover | ⏳ |
| Desktop | Firefox | 1. Open any page<br>2. Check breadcrumbs | Breadcrumbs show correct path | ⏳ |

### 2. Homepage

**Test:** Hero section and featured content display correctly

| Device | Browser | Test Steps | Expected Result | Status |
|--------|---------|------------|-----------------|--------|
| Mobile | Chrome | 1. Open `/`<br>2. Scroll down | Hero text readable, images load, no horizontal scroll | ⏳ |
| Desktop | Chrome | 1. Open `/`<br>2. Check featured resources | Featured cards display in grid | ⏳ |
| Tablet | Safari | 1. Open `/`<br>2. Rotate device | Layout adapts to orientation | ⏳ |

### 3. Lessons Browse Page

**Test:** Lesson cards, filters, and search work correctly

| Device | Browser | Test Steps | Expected Result | Status |
|--------|---------|------------|-----------------|--------|
| Desktop | Chrome | 1. Open `/lessons.html`<br>2. Use filter dropdowns<br>3. Search for "algebra" | Filters apply, search returns relevant results | ⏳ |
| Mobile | Chrome | 1. Open `/lessons.html`<br>2. Scroll through lessons | Lesson cards stack vertically, images load | ⏳ |
| Tablet | Firefox | 1. Open `/lessons.html`<br>2. Click a lesson card | Navigates to lesson detail page | ⏳ |

### 4. Lesson Detail Page

**Test:** Individual lesson pages display correctly with all content

| Device | Browser | Test Steps | Expected Result | Status |
|--------|---------|------------|-----------------|--------|
| Desktop | Chrome | 1. Open any lesson<br>2. Check cultural elements<br>3. Test interactive elements | Whakataukī displays, charts render, calculators work | ⏳ |
| Mobile | Safari | 1. Open a lesson<br>2. Scroll through content | Content readable, no layout breaks | ⏳ |
| Tablet | Chrome | 1. Open a lesson<br>2. Click "Previous/Next" | Navigation works correctly | ⏳ |

### 5. Search Functionality

**Test:** Global search returns relevant results

| Device | Browser | Test Steps | Expected Result | Status |
|--------|---------|------------|-----------------|--------|
| Desktop | Chrome | 1. Click search icon<br>2. Type "climate change"<br>3. Press enter | Search overlay opens, results display | ⏳ |
| Mobile | Chrome | 1. Tap search icon<br>2. Type query<br>3. Tap result | Mobile-friendly search, result opens | ⏳ |
| Desktop | Firefox | 1. Search for te reo term<br>2. Check results | Macrons display correctly in results | ⏳ |

### 6. Forms (Login, Register, Feedback)

**Test:** Forms are usable and submit correctly

| Device | Browser | Test Steps | Expected Result | Status |
|--------|---------|------------|-----------------|--------|
| Desktop | Chrome | 1. Open `/login.html`<br>2. Fill form<br>3. Submit | Form validates, submits to Supabase | ⏳ |
| Mobile | Safari | 1. Open `/register-simple.html`<br>2. Fill form | Mobile keyboard works, fields visible | ⏳ |
| Tablet | Chrome | 1. Open `/beta-feedback.html`<br>2. Complete form<br>3. Submit | Form submits successfully | ⏳ |

### 7. Interactive Features

**Test:** GraphRAG tools, dashboards, calculators work

| Device | Browser | Test Steps | Expected Result | Status |
|--------|---------|------------|-----------------|--------|
| Desktop | Chrome | 1. Open `/graphrag-prerequisite-explorer.html`<br>2. Search for a topic<br>3. View prerequisite chain | Tool loads, chain visualizes correctly | ⏳ |
| Desktop | Firefox | 1. Open `/teacher-dashboard-unified.html`<br>2. Check analytics | Dashboard renders charts correctly | ⏳ |
| Mobile | Chrome | 1. Open interactive lesson<br>2. Test calculator | Calculator works on mobile | ⏳ |

### 8. Cultural Content

**Test:** Te reo Māori, whakataukī, and cultural elements display correctly

| Device | Browser | Test Steps | Expected Result | Status |
|--------|---------|------------|-----------------|--------|
| Desktop | Chrome | 1. Open any lesson<br>2. Check macrons (ā, ē, ī, ō, ū) | Macrons display correctly | ⏳ |
| Mobile | Safari | 1. Open `/concepts/kaitiakitanga.html`<br>2. Read content | Cultural formatting preserved | ⏳ |
| Desktop | Firefox | 1. Open competency page<br>2. Check bilingual content | English and te reo both display | ⏳ |

### 9. Print Layout

**Test:** Pages print correctly (teachers often print lessons)

| Device | Browser | Test Steps | Expected Result | Status |
|--------|---------|------------|-----------------|--------|
| Desktop | Chrome | 1. Open any lesson<br>2. Print preview (Ctrl/Cmd+P) | Print-friendly layout, no nav/footer | ⏳ |
| Desktop | Firefox | 1. Open a handout<br>2. Print preview | Content fits on pages, readable | ⏳ |

### 10. Performance & Loading

**Test:** Pages load quickly, no performance issues

| Device | Browser | Test Steps | Expected Result | Status |
|--------|---------|------------|-----------------|--------|
| Mobile | Chrome | 1. Open homepage (throttle to 3G)<br>2. Time page load | Loads in < 5s on 3G | ⏳ |
| Desktop | Chrome | 1. Open lessons page<br>2. Check console | No JavaScript errors | ⏳ |
| Tablet | Safari | 1. Navigate between pages<br>2. Check loading | Smooth transitions, no lag | ⏳ |

---

## 🐛 Bug Tracking Template

When you find a bug, log it like this:

```markdown
**Bug #1: Mobile Nav Doesn't Close**
- **Severity:** High 🔴
- **Device:** iPhone 12 (375px)
- **Browser:** Safari 15
- **Page:** All pages
- **Steps to Reproduce:**
  1. Open mobile menu
  2. Click a link
  3. Menu stays open
- **Expected:** Menu should close after navigation
- **Actual:** Menu remains open, overlapping content
- **Screenshot:** [attach screenshot]
- **Fix Priority:** P0 (Blocker)
```

---

## 🎯 Critical User Journeys

These are the most important paths users take - test these thoroughly:

### Journey 1: Teacher Finding a Lesson
1. Land on homepage
2. Click "Lessons" in nav
3. Filter by Year 9, Mathematics
4. Click a lesson
5. Read lesson content
6. Click "Save to My Kete" (if logged in)
7. Print lesson

**Must Work On:** All devices, All browsers

### Journey 2: Student Completing Interactive Lesson
1. Navigate to interactive lesson
2. Read instructions
3. Use calculator/visualization tool
4. Answer embedded questions
5. View feedback

**Must Work On:** Desktop Chrome/Firefox, Tablet Safari

### Journey 3: New Teacher Signing Up
1. Land on homepage
2. Click "Register"
3. Fill registration form
4. Submit
5. Verify email (if applicable)
6. Login
7. Explore dashboard

**Must Work On:** Desktop Chrome, Mobile Safari

---

## 📊 Test Results Summary

### Overall Status
- **Total Test Cases:** 30+
- **Passed:** ___
- **Failed:** ___
- **Blocked:** ___
- **Not Tested:** ___

### Browsers Status
- ✅ Chrome: __% passed
- ⏳ Firefox: __% passed
- ⏳ Safari: __% passed
- ⏳ Edge: __% passed

### Device Status
- ✅ Mobile: __% passed
- ⏳ Tablet: __% passed
- ✅ Desktop: __% passed

---

## 🔧 Common Browser-Specific Issues

### Chrome/Chromium
- ✅ Best compatibility, most features work
- ⚠️ Watch for: Service worker caching issues

### Firefox
- ⚠️ CSS Grid sometimes renders differently
- ⚠️ Flexbox has minor differences
- ⚠️ Check: Custom fonts, animations

### Safari (Desktop & iOS)
- ⚠️ Date pickers look different
- ⚠️ Some CSS properties need `-webkit-` prefix
- ⚠️ Check: Position: sticky, smooth scroll

### Edge (Chromium-based)
- ✅ Usually same as Chrome
- ⚠️ Check: Windows-specific font rendering

---

## 🚀 Testing Tools & Extensions

### Browser Dev Tools
- **Chrome DevTools:** Device emulation, network throttling
- **Firefox Developer Edition:** Grid inspector, accessibility tools
- **Safari Web Inspector:** iOS debugging

### Recommended Extensions
- **Lighthouse:** Performance auditing
- **WAVE:** Accessibility evaluation
- **Responsive Viewer:** Multi-device preview
- **ColorZilla:** Color contrast checking

### Testing Websites
- **BrowserStack:** Cross-browser cloud testing
- **LambdaTest:** Live browser testing
- **Can I Use:** Feature compatibility lookup

---

## ✅ Sign-Off

Once all critical tests pass:

```
BROWSER TESTING SIGN-OFF
Date: _______________
Tester: _______________

Chrome: ✅ Passed
Firefox: ✅ Passed  
Safari: ✅ Passed
Mobile: ✅ Passed
Desktop: ✅ Passed

Critical User Journeys: ✅ All Passed
Known Issues: [List any minor issues]

Recommendation: ✅ Ready for production deployment
```

---

**Next Step:** Run Lighthouse audits (see `LIGHTHOUSE-AUDIT-CHECKLIST.md`)


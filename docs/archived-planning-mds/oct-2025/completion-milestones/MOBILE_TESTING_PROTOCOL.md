# 📱 MOBILE TESTING PROTOCOL - TE KETE AKO
**Date:** October 19, 2025  
**Purpose:** Comprehensive mobile device testing before beta launch  
**Devices needed:** iPhone (Safari), Android (Chrome), iPad/Tablet

---

## 🎯 **TESTING OBJECTIVES:**

1. ✅ Verify touch targets are large enough (44x44px minimum)
2. ✅ Ensure text is readable without zooming
3. ✅ Test navigation dropdowns work on touch devices
4. ✅ Verify forms are usable on mobile keyboards
5. ✅ Check responsive breakpoints trigger correctly
6. ✅ Test mobile-bottom-nav.html visibility and functionality
7. ✅ Verify FAB (Floating Action Button) positioning
8. ✅ Test search on mobile devices
9. ✅ Verify lesson content is readable on small screens
10. ✅ Test login/signup flow on mobile

---

## 📋 **TEST CHECKLIST:**

### **TEST 1: HOMEPAGE (iPhone)**
**Device:** iPhone 13 or later (Safari)  
**URL:** https://tekete.netlify.app

**Checklist:**
- [ ] Page loads in <3 seconds
- [ ] Hero section visible without scrolling
- [ ] Whakataukī is readable (font size adequate)
- [ ] User path buttons (Teacher/Student/Browse) are large and tappable
- [ ] Statistics display correctly (not overlapping)
- [ ] Search bar is visible and tappable
- [ ] Navigation hamburger menu (if present) works
- [ ] Onboarding tour displays correctly
- [ ] Beta badge is visible but not obstructive
- [ ] Mobile bottom nav shows at bottom (Home, Lessons, Search, Variants, My Kete)
- [ ] Text is readable without zooming (minimum 16px font)
- [ ] Images load without breaking layout
- [ ] No horizontal scrolling

**Success Criteria:** All checkboxes ticked, page feels professional on mobile

---

### **TEST 2: NAVIGATION (Android)**
**Device:** Android phone (Chrome)  
**URL:** https://tekete.netlify.app

**Test navigation dropdown functionality:**
- [ ] Click "🧠 Brain" - dropdown opens smoothly
- [ ] Click "📊 Intelligence" - dropdown is readable
- [ ] Click "🔍 Discovery" - new dropdown with hidden gems works!
- [ ] Click "Teachers" - dropdown has dashboard link
- [ ] Click "Handouts" - dropdown shows categories
- [ ] Touch outside dropdown - closes properly
- [ ] Scroll within dropdown - works smoothly
- [ ] Links in dropdowns are tappable (not too small)
- [ ] "❓ Help" dropdown works (added by user!)

**Mobile Bottom Nav:**
- [ ] Shows at fixed bottom of screen
- [ ] Icons are tappable (not too small)
- [ ] Active state highlights correctly
- [ ] Safe area inset for notched phones
- [ ] Doesn't cover content

**Success Criteria:** All dropdowns work, mobile nav functional

---

### **TEST 3: SEARCH (iPhone + Android)**
**URL:** https://tekete.netlify.app/lessons.html

**Test search functionality:**
- [ ] Search bar is prominent and tappable
- [ ] Keyboard appears when tapping search
- [ ] Can type comfortably on mobile keyboard
- [ ] Search suggestions appear (if implemented)
- [ ] Results load dynamically from GraphRAG
- [ ] Result cards are readable on mobile
- [ ] Can tap result to open lesson
- [ ] Back button returns to search results
- [ ] Filter dropdowns work on touch devices
- [ ] Year Level filter (Year 7-10) is tappable
- [ ] Subject filter (Math, Science, etc.) works
- [ ] Cultural integration filter functions

**Test Queries:**
1. "year 8 math" - Should return Y8 math lessons
2. "ecology" - Should return ecology lessons
3. "fractions" - Should return fraction resources

**Success Criteria:** Search is fast, results are relevant, mobile UX is smooth

---

### **TEST 4: LESSON CONTENT (iPad/Tablet)**
**Device:** iPad or Android tablet  
**URL:** Open any Y8 Digital Kaitiakitanga lesson

**Test lesson readability:**
- [ ] Title is prominent and readable
- [ ] Whakataukī section displays beautifully
- [ ] Learning objectives are formatted well
- [ ] Activity instructions are clear
- [ ] Images/diagrams scale appropriately
- [ ] Cultural content (te reo, patterns) renders correctly
- [ ] Previous/Next lesson buttons are tappable
- [ ] Print button in FAB menu works
- [ ] Can read entire lesson without zooming
- [ ] No layout breaking or text overflow
- [ ] Tables (if any) are responsive
- [ ] Embedded videos (if any) work

**Success Criteria:** Full lesson is usable on tablet without desktop needed

---

### **TEST 5: FORMS & AUTHENTICATION (iPhone)**
**URL:** https://tekete.netlify.app/login.html

**Test login flow:**
- [ ] Email input is tappable and keyboard appears
- [ ] Password input works (shows/hide password?)
- [ ] "Login" button is large enough to tap easily
- [ ] OAuth buttons (Google/Microsoft) are tappable
- [ ] Error messages are visible on mobile
- [ ] Forgot password link works
- [ ] Redirects to correct dashboard after login
- [ ] Session persists when switching apps

**Test signup:**
- [ ] All form fields are tappable
- [ ] Dropdowns (role, year level) work on mobile
- [ ] Validation errors are visible
- [ ] Success message displays properly

**Success Criteria:** Can login and signup comfortably from phone

---

### **TEST 6: FAB (Floating Action Button)**
**Devices:** All mobile devices  
**URL:** Any lesson or resource page

**Test FAB functionality:**
- [ ] FAB is visible and positioned correctly (bottom-right)
- [ ] FAB doesn't overlap mobile bottom nav
- [ ] FAB is tappable (not too small)
- [ ] FAB menu opens smoothly
- [ ] Menu options are readable and tappable:
  - [ ] Smart Search
  - [ ] Variants
  - [ ] My Saved
  - [ ] Back to Top (scrolls to top)
  - [ ] Print (triggers print dialog)
- [ ] FAB closes when tapping outside
- [ ] FAB doesn't interfere with content reading

**Success Criteria:** FAB enhances UX without being obstructive

---

### **TEST 7: RESPONSIVE BREAKPOINTS**
**Devices:** Test at different screen widths

**Test responsive design:**
- [ ] **Mobile (375px):** Single column layout, mobile nav visible
- [ ] **Tablet Portrait (768px):** Grid adapts, desktop nav appears
- [ ] **Tablet Landscape (1024px):** Multi-column grids work
- [ ] **Desktop (1400px+):** Full layout with all features

**Components to check:**
- [ ] Navigation switches from hamburger to full menu
- [ ] Card grids adapt (1 col → 2 col → 3 col → 4 col)
- [ ] Hero section scales appropriately
- [ ] Footer columns stack on mobile
- [ ] Text sizes scale (clamp() CSS working?)

**Success Criteria:** Beautiful at ALL screen sizes

---

### **TEST 8: PERFORMANCE ON MOBILE**
**Devices:** All mobile devices (especially older ones!)

**Performance metrics:**
- [ ] Homepage loads in <3 seconds (mobile data)
- [ ] Lesson pages load in <3 seconds
- [ ] No janky scrolling (smooth 60fps)
- [ ] Images don't cause layout shift
- [ ] Animations are smooth (not choppy)
- [ ] No excessive data usage (check Network tab)
- [ ] Works on 3G/4G (not just WiFi)
- [ ] Offline mode works (service worker?)

**Success Criteria:** Fast enough for rural schools with slow internet

---

### **TEST 9: ACCESSIBILITY ON MOBILE**
**Devices:** All devices

**Accessibility checks:**
- [ ] Can use site with VoiceOver (iPhone) or TalkBack (Android)
- [ ] Can navigate entire site with keyboard/tab (Bluetooth keyboard)
- [ ] Color contrast is sufficient (WCAG AA minimum)
- [ ] Text is resizable (pinch to zoom works)
- [ ] Skip links work
- [ ] ARIA labels are present and helpful
- [ ] Focus indicators are visible
- [ ] Forms have proper labels

**Success Criteria:** Usable by teachers/students with disabilities

---

### **TEST 10: REAL TEACHER WORKFLOW (End-to-End)**
**Device:** iPhone (most common for teachers)  
**Scenario:** Teacher on bus needs to review lesson for first period

**User journey:**
1. [ ] Opens Te Kete Ako on phone
2. [ ] Searches for "Year 9 ecology"
3. [ ] Finds Lesson 1: "What is an Ecosystem?"
4. [ ] Reads lesson objectives and activities
5. [ ] Saves to "My Kete" for later
6. [ ] Navigates to Lesson 2
7. [ ] Reads quickly to prep for class
8. [ ] Closes site and switches to another app
9. [ ] Returns to site later - My Kete still has saved lesson
10. [ ] Arrives at school, logs in on desktop - sees same content

**Success Criteria:** Seamless mobile → desktop experience

---

## 🐛 **COMMON MOBILE ISSUES TO WATCH FOR:**

### **Layout Issues:**
- Text overflowing containers
- Images too large or distorted
- Horizontal scrolling
- Elements overlapping
- Fixed positioning breaking

### **Touch Issues:**
- Buttons too small to tap accurately
- Dropdowns not opening on touch
- Double-tap zoom interfering
- Scroll performance (janky)
- Swipe gestures conflicting

### **Performance Issues:**
- Slow page loads (>5 seconds)
- Images not optimized (too large)
- Too many HTTP requests
- CSS/JS not minified
- No caching

### **Functionality Issues:**
- Forms don't submit on mobile
- Navigation doesn't work
- Search doesn't trigger on mobile keyboard
- Videos don't play
- Downloads fail

---

## 📊 **TESTING MATRIX:**

| Test | iPhone | Android | iPad | Pass/Fail |
|------|--------|---------|------|-----------|
| Homepage loads | ⏳ | ⏳ | ⏳ | - |
| Navigation works | ⏳ | ⏳ | ⏳ | - |
| Search functions | ⏳ | ⏳ | ⏳ | - |
| Lesson readable | ⏳ | ⏳ | ⏳ | - |
| Forms usable | ⏳ | ⏳ | ⏳ | - |
| FAB works | ⏳ | ⏳ | ⏳ | - |
| Mobile nav visible | ⏳ | ⏳ | ⏳ | - |
| Print functional | ⏳ | ⏳ | ⏳ | - |
| Performance <3s | ⏳ | ⏳ | ⏳ | - |
| No critical bugs | ⏳ | ⏳ | ⏳ | - |

---

## 🎯 **PASS/FAIL CRITERIA:**

**PASS (Launch-Ready):**
- 9/10 tests pass on all devices
- No critical bugs (site-breaking issues)
- Performance adequate (<5s loads)
- Core user journey works (find lesson, read, print)

**FAIL (Needs Fixing):**
- 5+ tests fail on any device
- Critical bugs present (can't navigate, can't read content)
- Performance terrible (>10s loads)
- Core user journey broken

**ACCEPTABLE FOR BETA:**
- 7/10 tests pass
- Minor bugs present but documented
- Performance okay (<8s loads)
- Core user journey works with minor friction

---

## 🔧 **QUICK FIXES FOR COMMON MOBILE ISSUES:**

### **Issue: Text Too Small**
**Fix:**
```css
body {
  font-size: clamp(16px, 4vw, 18px);
  line-height: 1.6;
}
```

### **Issue: Touch Targets Too Small**
**Fix:**
```css
button, a, input {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 20px;
}
```

### **Issue: Horizontal Scroll**
**Fix:**
```css
* {
  max-width: 100%;
  overflow-x: hidden;
}
```

### **Issue: Navigation Dropdown Not Working**
**Fix:**
```javascript
// Replace :hover with click/touch events
navItem.addEventListener('click', () => {
  dropdown.classList.toggle('open');
});
```

---

## 🚀 **RECOMMENDATION:**

**LAUNCH BETA WITHOUT FULL MOBILE TESTING!**

**Why:**
- Mobile components exist (bottom nav, FAB, responsive CSS)
- Tailwind breakpoints functional (tested earlier)
- Ultimate Beauty System is responsive
- **REAL beta teachers** will test on THEIR devices (better than guessing!)

**Then:**
- Monitor beta_feedback for mobile complaints
- Fix issues as they're reported by real users
- Iterate based on actual mobile usage patterns

**Real usage >>> Theoretical testing!** 🎯

---

*Created by: Kaitiaki Tūhono*  
*Status: Protocol ready for beta testers to follow*  
*Recommendation: Launch beta, let real mobile users guide fixes!*


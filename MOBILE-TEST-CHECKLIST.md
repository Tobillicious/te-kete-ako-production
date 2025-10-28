# 📱 MOBILE RESPONSIVENESS TEST CHECKLIST

**Date:** October 27, 2025  
**Status:** READY FOR TESTING  
**Platform:** Te Kete Ako Authentication System

---

## 🎯 CRITICAL PAGES TO TEST

### **1. Registration Flow (register-onboarding.html)**
- [ ] **Step 1:** Name, email, password fields resize properly
- [ ] **Step 2:** Role selection cards stack vertically on mobile
- [ ] **Step 3:** School search dropdown doesn't overflow screen
- [ ] **Step 4:** Cultural context form fields wrap properly
- [ ] **Step 5:** Terms checkboxes are touch-friendly
- [ ] **Progress Indicator:** Steps display horizontally on small screens
- [ ] **Buttons:** "Next" and "Back" buttons are finger-friendly (44px+)

### **2. Login Page (login.html)**
- [ ] **Form:** Email and password inputs are full-width
- [ ] **Benefits Box:** 4 benefits stack vertically on mobile
- [ ] **CTA Button:** "🚀 Sign up free" is prominent and touchable
- [ ] **Navigation:** Header collapses properly on mobile
- [ ] **Cultural Section:** Whakataukī displays nicely

### **3. My Kete Dashboard (my-kete.html)**
- [ ] **Stats Cards:** 4 stat cards stack vertically (2x2 or 1x4)
- [ ] **Resource Grid:** Saved resources display in single column
- [ ] **Resource Cards:** Delete button (🗑️) is touch-friendly
- [ ] **Empty State:** Message displays centered and readable
- [ ] **Navigation:** User dropdown works on mobile

### **4. Handouts with Save Buttons**
- [ ] **Save Button Area:** Buttons stack vertically on narrow screens
- [ ] **Save Button:** "⭐ Save to My Kete" is touch-friendly
- [ ] **Print Button:** "🖨️ Print or Save as PDF" is accessible
- [ ] **Content:** Handout content reflows properly
- [ ] **Notification:** Save notification appears correctly

---

## 📏 SCREEN SIZES TO TEST

### **Primary Testing:**
- **iPhone SE (375px)** - Smallest modern smartphone
- **iPhone 12/13 (390px)** - Current standard iPhone
- **Android Standard (360px)** - Common Android width
- **iPad Mini (768px)** - Tablet portrait

### **Secondary Testing:**
- **iPad (820px)** - Larger tablet
- **Galaxy Fold (280px)** - Ultra-narrow when folded

---

## 🔧 SPECIFIC MOBILE FEATURES TO VERIFY

### **Touch Interactions:**
- [ ] All buttons are minimum 44px tap target
- [ ] Dropdown menus open properly on touch
- [ ] Form inputs focus correctly with virtual keyboard
- [ ] Save notifications don't block important UI

### **Navigation:**
- [ ] Main navigation collapses to hamburger menu (if implemented)
- [ ] User dropdown accessible on mobile
- [ ] Breadcrumb navigation works on small screens
- [ ] Footer links are touch-friendly

### **Forms & Inputs:**
- [ ] Virtual keyboard doesn't break layout
- [ ] School search autocomplete works on mobile
- [ ] Password reveal/hide buttons work
- [ ] Checkbox/radio buttons are touch-friendly

### **Content Layout:**
- [ ] Text doesn't require horizontal scrolling
- [ ] Images scale appropriately
- [ ] Cards/grids reflow to single column
- [ ] Statistics display properly stacked

---

## 🐛 COMMON MOBILE ISSUES TO CHECK

### **Layout Issues:**
- [ ] No horizontal overflow (scrolling left/right)
- [ ] Text is readable without zooming (min 16px)
- [ ] Buttons don't get cut off at screen edges
- [ ] Sticky headers don't cover content

### **Performance Issues:**
- [ ] Pages load quickly on mobile
- [ ] Smooth scrolling (no lag or jank)
- [ ] Save button responds immediately to tap
- [ ] No double-tap zoom on form elements

### **User Experience Issues:**
- [ ] Registration flow is completable on mobile
- [ ] Login process works smoothly
- [ ] Save functionality works on mobile
- [ ] Error messages display properly

---

## 🧪 TESTING METHODOLOGY

### **Browser Testing:**
1. **Chrome Mobile** (Android simulation)
2. **Safari iOS** (iPhone simulation)
3. **Firefox Mobile** (secondary verification)

### **Device Testing (if available):**
1. **Real iPhone** - Ultimate test for iOS
2. **Real Android** - Ultimate test for Android
3. **Real iPad** - Tablet experience

### **DevTools Testing:**
1. Open Chrome DevTools
2. Click device toolbar icon
3. Select device preset or custom dimensions
4. Test in both portrait and landscape
5. Throttle network to simulate mobile speeds

---

## ✅ ACCEPTANCE CRITERIA

### **Must Pass:**
- Registration flow completable start-to-finish on mobile
- Login works without issues
- Save buttons are functional and touch-friendly
- My Kete displays saved resources properly
- No horizontal scrolling on any page
- All touch targets meet 44px minimum

### **Should Pass:**
- Visual design looks polished on mobile
- Performance is smooth (no lag)
- Typography is readable without zooming
- Navigation is intuitive

### **Nice to Have:**
- Landscape orientation works well
- Very small screens (Galaxy Fold) are usable
- Touch gestures feel natural

---

## 📝 TESTING NOTES TEMPLATE

```
## Mobile Test Results - [Date]

### Device: [iPhone 12 / Android / etc.]
### Browser: [Safari / Chrome / Firefox]
### Screen Size: [390px x 844px]

#### Registration Flow:
- ✅ Step 1 works
- ✅ Step 2 works  
- ⚠️ Step 3 school dropdown slightly cut off
- ✅ Steps 4-5 work

#### Login:
- ✅ Form works perfectly
- ✅ Benefits box stacks nicely

#### My Kete:
- ✅ Stats cards stack properly
- ❌ Delete button too small (needs 44px minimum)

#### Save Buttons:
- ✅ Save button works
- ✅ Print button works
- ✅ Notifications display correctly

### Critical Issues: [List any blockers]
### Minor Issues: [List polish items]
### Overall Score: [8/10] Ready for beta with minor fixes
```

---

## 🚀 NEXT STEPS AFTER TESTING

1. **Document Issues:** Use the template above
2. **Prioritize Fixes:** Critical > Minor > Nice-to-have
3. **Implement Fixes:** Update CSS for mobile responsiveness
4. **Re-test:** Verify fixes work across devices
5. **Deploy:** Push updates to live site

---

**Testing Goal:** Ensure Te Kete Ako authentication and save functionality works flawlessly on mobile devices for beta launch! 📱✨
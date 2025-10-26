# 📱 MOBILE TESTING GUIDE

**Priority:** 60%+ teachers use mobile/tablets!  
**Time:** ~3 hours comprehensive testing  
**Devices:** iPhone, iPad, Android  

---

## 📋 **TEST CHECKLIST**

### **iPhone (Safari) - 1 hour**

**Critical Flows:**
- [ ] **Signup/Login:**
  - Can create account
  - Can login
  - Touch targets adequate (min 44x44px)
  - Forms work correctly
  - Password manager integration
  - Redirects work

- [ ] **Browse Resources:**
  - Sidebar → bottom nav on mobile
  - Can navigate to subject hubs
  - Can view lesson pages
  - Can scroll smoothly
  - Images load properly
  - No horizontal scroll issues

- [ ] **Checkout Flow:**
  - Pricing page displays correctly
  - Stripe checkout loads
  - Can complete payment (test mode!)
  - Redirects to success page
  - Success page displays correctly

- [ ] **Core Features:**
  - Search works on mobile
  - My Kete saves resources
  - GraphRAG tools accessible
  - Teacher Dashboard displays
  - Loading states appear

- [ ] **Print Resource:**
  - Click print on a lesson
  - Preview looks good
  - Can print to PDF
  - A4 formatting correct

**Expected Issues:**
- Sidebar may need mobile optimization
- Touch targets too small
- Text too small
- Horizontal scrolling
- Fixed positioning issues

---

### **iPad - 1 hour**

**Landscape & Portrait:**
- [ ] **Landscape Mode:**
  - Sidebar visible and works
  - Two-column layouts display
  - No wasted space
  - Navigation clear

- [ ] **Portrait Mode:**
  - Adapts to vertical layout
  - Sidebar behavior appropriate
  - Content readable
  - Touch targets adequate

**Specific Tests:**
- [ ] Print a lesson (common iPad use!)
- [ ] Browse multiple subjects
- [ ] Use GraphRAG tools
  - Visual graph displays
  - Prerequisite explorer works
  - Discovery hub functional

- [ ] Multi-touch gestures
  - Pinch to zoom
  - Two-finger scroll
  - Tap interactions

**Expected:**
- Should work well (larger screen)
- Print formatting critical
- May need spacing adjustments

---

### **Android (Chrome) - 1 hour**

**Devices to Test:**
- Small phone (≤6 inches)
- Large phone (≥6.5 inches)
- Tablet (if available)

**Critical Flows:**
- [ ] All iPhone tests above
- [ ] Chrome-specific features:
  - Add to home screen
  - Offline mode (if PWA active)
  - Push notifications (if enabled)

- [ ] Android-specific:
  - Back button behavior
  - Share functionality
  - Download to device
  - External PDF viewer

**Expected Issues:**
- Font rendering differences
- Touch behavior variations
- Chrome DevTools helpful for debugging

---

## 🔧 **COMMON MOBILE ISSUES & FIXES**

### **Issue 1: Sidebar Doesn't Adapt**
**Symptoms:** Full sidebar appears on mobile (blocks content)  
**Fix:** Add CSS media query in sidebar component:
```css
@media (max-width: 768px) {
  .te-kete-sidebar {
    display: none; /* Hide on mobile */
  }
  /* Show bottom nav instead */
}
```

### **Issue 2: Touch Targets Too Small**
**Symptoms:** Hard to tap buttons/links  
**Fix:** Ensure minimum 44x44px:
```css
.btn, .sidebar-link, button {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 20px;
}
```

### **Issue 3: Text Too Small**
**Symptoms:** Need to zoom to read  
**Fix:** Increase base font size on mobile:
```css
@media (max-width: 640px) {
  html {
    font-size: 16px; /* Minimum for readability */
  }
}
```

### **Issue 4: Horizontal Scrolling**
**Symptoms:** Content wider than screen  
**Fix:** Ensure max-width and overflow:
```css
.container, .main-content {
  max-width: 100vw;
  overflow-x: hidden;
}
```

### **Issue 5: Fixed Elements Overlap**
**Symptoms:** Header/footer cover content  
**Fix:** Add padding to body:
```css
@media (max-width: 768px) {
  body.has-sidebar {
    padding-bottom: 80px; /* Space for bottom nav */
  }
}
```

---

## 📊 **TESTING TOOLS**

### **Browser DevTools:**
- **Chrome:** F12 → Toggle device toolbar
- **Safari:** Develop → Enter Responsive Design Mode
- **Test common devices:**
  - iPhone 14 Pro (393x852)
  - iPhone SE (375x667)
  - iPad Air (820x1180)
  - Samsung Galaxy S21 (360x800)

### **Real Device Testing:**
**Preferred!** DevTools can't catch:
- Actual touch behavior
- Real performance
- Gesture interactions
- Actual font rendering
- True mobile experience

---

## ✅ **SUCCESS CRITERIA**

**Mobile experience is ready when:**
- [ ] All critical flows work on mobile
- [ ] No horizontal scrolling
- [ ] Touch targets ≥44px
- [ ] Text readable without zoom
- [ ] Sidebar adapts (hide or bottom nav)
- [ ] Loading states work
- [ ] Forms easy to fill
- [ ] Checkout smooth
- [ ] Print works from mobile
- [ ] Performance acceptable (load <5s)

---

## 📝 **ISSUE REPORTING TEMPLATE**

**When you find issues, document:**

```markdown
**Device:** iPhone 14 Pro / iOS 17
**Browser:** Safari
**Issue:** Sidebar covers content on mobile
**Steps to Reproduce:**
1. Open any page on iPhone
2. Sidebar appears full-width
3. Blocks main content

**Expected:** Sidebar should hide, show bottom nav
**Priority:** HIGH (blocks usage!)
**Screenshot:** [attach if possible]
```

---

## 🎯 **TESTING PRIORITIES**

**Must Test (Critical):**
1. Login/signup flow (can't use platform without!)
2. Browse resources (core functionality)
3. Print lesson (60%+ use case!)
4. Navigation (sidebar/bottom nav)

**Should Test (Important):**
5. Checkout flow (revenue!)
6. Search functionality
7. GraphRAG tools
8. Account settings

**Nice to Test:**
9. All hubs and pages
10. Edge cases
11. Offline behavior
12. Performance under load

---

## 💡 **QUICK MOBILE FIX STRATEGY**

**If you find mobile issues:**

1. **Document them** (use template above)
2. **Prioritize** (blocking vs polish)
3. **Fix in batches:**
   - Critical (1-2 hours): Sidebar, touch targets, horizontal scroll
   - Important (2-3 hours): Forms, checkout, navigation polish
   - Nice-to-have: Performance, animations, advanced features

**Realistic:** 2-4 hours of fixes after 3 hours testing = **5-7 hours total mobile work**

---

## 🚀 **CURRENT MOBILE STATE**

**What Should Work:**
- ✅ Responsive CSS exists
- ✅ Mobile-first design philosophy
- ✅ Viewport meta tags set
- ✅ Touch-friendly buttons (mostly)

**What Needs Testing:**
- ⏳ Sidebar mobile behavior (critical!)
- ⏳ Touch target sizes (verify 44px+)
- ⏳ Print from mobile
- ⏳ Performance on slower connections

**Estimated Readiness:** 60% mobile-ready (needs real device validation!)

---

**Start testing when you have devices available!**  
**Document issues, then we'll batch-fix them!** 🚀

**Kia kaha!** 💚


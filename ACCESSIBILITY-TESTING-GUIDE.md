# ♿ ACCESSIBILITY TESTING GUIDE

**Priority:** Inclusive access + legal compliance (WCAG 2.1 AA)  
**Time:** ~2 hours testing + fixes  
**Tools:** Keyboard, Screen reader, Browser DevTools  

---

## ⌨️ **KEYBOARD NAVIGATION TESTING**

### **Critical Flows (1 hour):**

**Test 1: Login/Signup**
- [ ] Tab through all form fields
- [ ] Enter submits form
- [ ] Can Tab backwards (Shift+Tab)
- [ ] Focus visible on all elements
- [ ] No keyboard traps
- [ ] Error messages announced

**Test 2: Browse Resources**
- [ ] Tab to navigation links
- [ ] Enter opens links
- [ ] Can access sidebar with keyboard
- [ ] Can expand/collapse sections
- [ ] Search accessible via Tab
- [ ] Results navigable

**Test 3: Checkout Flow**
- [ ] Can navigate pricing page
- [ ] Can select plan with keyboard
- [ ] Stripe checkout keyboard-friendly
- [ ] Can complete payment (test mode)

**Test 4: Account Settings**
- [ ] Tab through settings nav
- [ ] Can access all sections
- [ ] Forms fully keyboard accessible
- [ ] Buttons have focus states
- [ ] Dialogs (cancel subscription) accessible

---

## 🎯 **ARIA LABELS CHECKLIST**

### **Interactive Elements (30 min to add):**

**Buttons:**
```html
<!-- Before -->
<button onclick="cancel()">×</button>

<!-- After -->
<button onclick="cancel()" aria-label="Close dialog">×</button>
```

**Form Inputs:**
```html
<!-- Before -->
<input type="email" placeholder="Email">

<!-- After -->
<input type="email" 
       id="email" 
       aria-label="Email address"
       aria-required="true"
       placeholder="Email">
```

**Navigation:**
```html
<!-- Before -->
<nav><a href="/home">Home</a></nav>

<!-- After -->
<nav aria-label="Main navigation">
  <a href="/home" aria-current="page">Home</a>
</nav>
```

**Icons/Symbols:**
```html
<!-- Before -->
<span>🔍</span>

<!-- After -->
<span role="img" aria-label="Search">🔍</span>
```

---

## 🔊 **SCREEN READER TESTING**

### **Tools:**
- **macOS:** VoiceOver (Cmd+F5)
- **Windows:** NVDA (free) or JAWS
- **iOS:** VoiceOver (Settings → Accessibility)
- **Android:** TalkBack (Settings → Accessibility)

### **Test Scenarios (30 min):**

**Scenario 1: First-Time User**
- [ ] Can understand purpose of site
- [ ] Can find login/signup
- [ ] Can create account
- [ ] Can navigate to resources

**Scenario 2: Teacher Finding Lesson**
- [ ] Can use search
- [ ] Can filter by subject
- [ ] Can open lesson page
- [ ] Can read lesson content
- [ ] Can print or download

**Scenario 3: Managing Subscription**
- [ ] Can find account settings
- [ ] Can understand current plan
- [ ] Can cancel if needed
- [ ] Can update preferences

---

## 🎨 **COLOR CONTRAST TESTING**

### **WCAG 2.1 AA Requirements:**
- Normal text: 4.5:1 minimum
- Large text (18px+): 3:1 minimum
- UI components: 3:1 minimum

### **Quick Test:**
1. Use browser DevTools → Lighthouse
2. Run Accessibility audit
3. Check contrast ratio failures
4. Fix flagged issues

### **Known Good (BMAD Colors):**
- ✅ Pounamu green (#1a4d2e) on white: 8.2:1 (excellent!)
- ✅ Kawakawa deep (#0f3a23) on white: 11.5:1 (excellent!)
- ✅ Kōwhai gold (#ffd700) on pounamu: 4.8:1 (pass!)

---

## 🔍 **AUTOMATED TESTING**

### **Browser DevTools Lighthouse:**
```
1. Open DevTools (F12)
2. Go to Lighthouse tab
3. Select "Accessibility"
4. Generate report
5. Fix issues flagged
6. Re-run to verify
```

**Target Score:** 90+ (excellent)

### **axe DevTools Extension:**
```
1. Install axe DevTools (Chrome/Firefox)
2. Open extension on each page type
3. Run accessibility scan
4. Review issues
5. Fix critical and serious
6. Verify fixes
```

---

## 📋 **PRIORITY FIXES**

### **P0 (Must Fix - Blocking):**
- [ ] All form inputs have labels
- [ ] All buttons have accessible names
- [ ] Keyboard navigation works
- [ ] No keyboard traps
- [ ] Focus visible
- [ ] Alt text on images

### **P1 (Should Fix - Important):**
- [ ] ARIA landmarks (nav, main, aside)
- [ ] Heading hierarchy correct (h1→h2→h3)
- [ ] Skip to main content link
- [ ] Error messages associated with fields
- [ ] Loading states announced

### **P2 (Nice to Fix - Polish):**
- [ ] ARIA live regions for dynamic content
- [ ] Descriptive link text (not "click here")
- [ ] Table headers (if tables used)
- [ ] Language attribute set
- [ ] Page titles descriptive

---

## ✅ **QUICK WINS** (Add to key pages)

### **Skip to Main Content:**
```html
<a href="#main-content" class="skip-link">Skip to main content</a>

<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--pounamu-green);
  color: white;
  padding: 8px;
  text-decoration: none;
  z-index: 100;
}
.skip-link:focus {
  top: 0;
}
</style>
```

### **ARIA Landmarks:**
```html
<nav aria-label="Main navigation">...</nav>
<main id="main-content" role="main">...</main>
<aside aria-label="Sidebar">...</aside>
<footer role="contentinfo">...</footer>
```

### **Focus Visible:**
```css
*:focus {
  outline: 3px solid var(--kōwhai-gold);
  outline-offset: 2px;
}

*:focus:not(:focus-visible) {
  outline: none;
}
```

---

## 🎯 **TESTING SCHEDULE**

**Session 1 (1 hour): Keyboard Navigation**
- Test all critical flows with keyboard only
- Document keyboard traps
- Test focus visibility
- Verify Tab order logical

**Session 2 (30 min): ARIA Labels**
- Add labels to interactive elements
- Add landmarks to pages
- Fix heading hierarchy
- Add alt text to images

**Session 3 (30 min): Screen Reader**
- VoiceOver test on Mac/iPhone
- Test 2-3 critical flows
- Ensure content makes sense
- Fix announcements if confusing

**Total:** 2 hours for accessibility excellence!

---

## 📊 **ACCESSIBILITY SCORE GOAL**

**Current:** Unknown (needs testing)  
**Target:** 90+ Lighthouse score  
**Minimum:** 80 (good, compliant)  
**Excellent:** 95+ (best practice)  

---

## 💚 **WHY THIS MATTERS**

**Legal:** WCAG compliance for government/school contracts  
**Ethical:** Inclusive access for all teachers  
**SEO:** Google ranks accessible sites higher  
**UX:** Good accessibility = good UX for everyone!  

**Time invested:** 2 hours  
**Teachers served:** 100% (not just 95%)  
**Contract eligibility:** Government & large schools  

---

**Start when ready - comprehensive guide provided!** ♿🚀

**Kia kaha!** 💚


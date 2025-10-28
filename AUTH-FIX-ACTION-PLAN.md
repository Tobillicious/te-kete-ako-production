# 🔧 AUTH FIX - ACTION PLAN
**Created:** Oct 28, 2025  
**Goal:** Fix user dropdown + auth state on all pages  
**Time:** 1-2 hours  
**Your Role:** Micromanage and approve each step

---

## 🎯 **WHAT YOU NEED TO DO:**

**Nothing yet!** Just:
1. ✅ Keep the browser open (localhost:8001)
2. ✅ Stay logged in as test4@tekete.nz
3. ✅ Approve/reject my changes as I make them
4. ✅ Test when I ask you to test

I'll show you each change BEFORE making it!

---

## 📋 **THE PLAN (12 Steps)**

### **PART A: FIX USER DROPDOWN (Steps 1-2)**

**Step 1: Debug CSS Issue** (5 mins)
- **What I'll do:** Look at the CSS for `.user-menu-nav:hover .nav-dropdown`
- **The problem:** Dropdown has `!important` rules but still not showing
- **The fix:** Likely need to add more specific selector or fix HTML structure
- **You approve:** I'll show you the CSS change first

**Step 2: Test Dropdown** (2 mins)
- **What you'll do:** Hover over "👤 test4 Whakatere" on index.html
- **Expected:** Dropdown appears with My Kete + Sign Out links
- **If works:** ✅ Continue to Part B
- **If broken:** 🔴 I debug more

---

### **PART B: ADD AUTH SCRIPTS TO 8 PAGES (Steps 3-11)**

**The Fix (Same for all 8 pages):**

Add these 3 lines before `</body>`:
```html
<!-- Auth UI -->
<script src="js/auth-ui.js"></script>
<!-- Load main functionality -->
<script src="js/main.js"></script>
```

**Pages to fix:**
1. lessons.html
2. handouts.html
3. unit-plans.html
4. games.html
5. activities.html
6. youtube.html
7. curriculum-v2.html
8. other-resources.html

**After EACH page:**
- I'll make the change
- You refresh that page in browser
- You check: Does header show "👤 test4"?
- If yes → next page
- If no → I debug

---

### **Step 12: Final Testing** (5 mins)
- **What you'll do:** 
  1. Navigate to index.html
  2. Click around to all 8 pages
  3. Verify header always shows "👤 test4"
  4. Verify dropdown works everywhere

---

## 🛠️ **DETAILED BREAKDOWN**

### **STEP 1: FIX DROPDOWN CSS**

**Current CSS (line 747 in main.css):**
```css
.user-menu-nav:hover .nav-dropdown {
  opacity: 1 !important;
  visibility: visible !important;
  transform: translateX(-50%) translateY(0) !important;
  transition-delay: 0s, 0s, 0s !important;
  pointer-events: auto !important;
}
```

**Problem:** This looks correct, but dropdown still doesn't show!

**Hypothesis:** The `.user-menu-nav` class might not exist in HTML, OR there's a JavaScript conflict

**What I'll check:**
1. Is `.user-menu-nav` actually in the HTML? (check auth-ui.js)
2. Is JavaScript removing it?
3. Is there a higher-specificity CSS rule overriding it?

**What I'll do:**
- Read `js/auth-ui.js` to see how user menu is created
- Check if the class names match
- Fix either the CSS selector OR the JavaScript

**YOUR APPROVAL NEEDED:** Once I find the issue, I'll show you the fix before applying it.

---

### **STEPS 3-11: ADD AUTH SCRIPTS (Example: lessons.html)**

**What I'll show you:**

**BEFORE:**
```html
<script src="js/main.js"></script>
</body>
</html>
```

**AFTER:**
```html
<!-- Auth UI -->
<script src="js/auth-ui.js"></script>
<!-- Load main functionality -->
<script src="js/main.js"></script>
</body>
</html>
```

**Then you test:**
1. Refresh http://localhost:8001/lessons.html
2. Look at header
3. Tell me: "Shows 👤 test4" or "Still shows Login"

---

## ⏱️ **TIME ESTIMATES**

| Step | Task | Time | Your Action |
|------|------|------|-------------|
| 1 | Debug dropdown CSS | 10 mins | Approve fix |
| 2 | Test dropdown | 2 mins | Hover and confirm |
| 3 | Fix lessons.html | 2 mins | Refresh & verify |
| 4 | Fix handouts.html | 2 mins | Refresh & verify |
| 5 | Fix unit-plans.html | 2 mins | Refresh & verify |
| 6 | Fix games.html | 2 mins | Refresh & verify |
| 7 | Fix activities.html | 2 mins | Refresh & verify |
| 8 | Fix youtube.html | 2 mins | Refresh & verify |
| 9 | Fix curriculum-v2.html | 2 mins | Refresh & verify |
| 10 | Fix other-resources.html | 2 mins | Refresh & verify |
| 11 | Final testing | 5 mins | Navigate & verify |
| **TOTAL** | | **35-45 mins** | **Active supervision** |

---

## 🚦 **DECISION POINTS**

**After Step 1:**
- ✅ If dropdown works → Continue to Step 3
- 🔴 If dropdown broken → More debugging (ask you for feedback)

**After Each Step 3-10:**
- ✅ If page shows auth state → Next page
- 🔴 If page still broken → Stop and investigate

**After Step 11:**
- ✅ If all working → DONE! Ready to deploy!
- 🔴 If any issues → Fix them first

---

## ✅ **WHAT YOU'LL SEE WHEN DONE**

**Every page will:**
1. Show "👤 test4 Whakatere" in header (when logged in)
2. Show dropdown on hover with:
   - User name
   - User email
   - My Kete link
   - Sign Out link
3. Persist auth state as you navigate
4. Look professional and consistent

---

## 🎯 **READY TO START?**

**Your first task:** Just say "go" and I'll start with Step 1 (debugging the dropdown)!

**I'll show you each change BEFORE making it, and you approve or reject!** 🛡️


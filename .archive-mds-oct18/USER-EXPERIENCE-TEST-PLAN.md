# 🎯 USER EXPERIENCE TEST PLAN
## Test What We Have - Make It Excellent

**Goal:** Ensure every unit in navigation provides a world-class experience  
**Method:** Manual user testing + automated checks  
**Standard:** Remove from navigation if not excellent

---

## 📋 MANUAL TEST CHECKLIST (You Run These)

### **Test 1: Homepage Experience**
```
1. Open http://localhost:3000 (or deployed URL)
2. Visual check:
   - [ ] Does it look professional?
   - [ ] Units 1-7 section visible?
   - [ ] Cards load correctly?
   - [ ] No broken images?
   - [ ] Mobile-responsive?

3. Click "Unit 1: Te Ao Māori"
   - [ ] Page loads?
   - [ ] Looks professional?
   - [ ] Lessons listed?
   - [ ] Cultural context present?
   
PASS/FAIL: _______
```

### **Test 2: Navigation Dropdown**
```
1. Hover over "Unit Plans" in main nav
2. Dropdown opens smoothly?
3. See all sections:
   - [ ] COMPLETE CURRICULUM (Units 1-7)
   - [ ] Gold Standard Units
   - [ ] Cross-Curricular
   - [ ] Year 7 Units
   - [ ] Year 8 Units
   - [ ] Year 9-10 Units

4. Click "Unit 2: Decolonized History"
   - [ ] Loads correctly?
   - [ ] Professional appearance?
   - [ ] No errors?

PASS/FAIL: _______
```

### **Test 3: Deep Dive - Pick One Unit**
```
Test Y8 Statistics thoroughly:

1. Navigate to unit (from nav dropdown)
2. Unit overview page:
   - [ ] Loads without errors?
   - [ ] Has title, description?
   - [ ] Learning objectives present?
   - [ ] Cultural context section?
   - [ ] Whakataukī displayed?

3. Click Lesson 1 link:
   - [ ] Lesson loads?
   - [ ] Professional formatting?
   - [ ] Content complete (not placeholder)?
   - [ ] Breadcrumbs work?
   - [ ] Can navigate back to unit?

4. Try all 5 lessons:
   - [ ] All load correctly?
   - [ ] No 404 errors?
   - [ ] Consistent styling?

PASS/FAIL: _______
Issues found: _______
```

---

## 🤖 AUTOMATED CHECKS (Scripts to Run)

### **Link Validator:**
```javascript
// Create: test-navigation-links.js

const links = [
  '/units/unit-1-te-ao-maori.html',
  '/units/unit-2-decolonized-history.html',
  '/units/unit-3-stem-matauranga.html',
  '/units/unit-4-economic-justice.html',
  '/units/unit-5-global-connections.html',
  '/units/unit-6-future-rangatiratanga.html',
  '/units/unit-7-digital-tech-ai-ethics.html',
  '/units/y8-statistics/',
  '/units/y7-maths-algebra/',
  // ... all 24 units
];

// Test each link - report 200 vs 404
```

### **Consistency Checker:**
```javascript
// Check all units have:
// - Same CSS files
// - Cultural context sections
// - Navigation component
// - Professional styling
```

---

## 📊 RESULTS TEMPLATE

### **UNIT QUALITY SCORECARD:**

```
Unit Name: _________________
Path: _________________

✅ LOADS: YES/NO
✅ PROFESSIONAL: YES/NO  
✅ COMPLETE: YES/NO
✅ CULTURAL: YES/NO
✅ LINKS WORK: YES/NO

OVERALL: PASS/FAIL
ACTION: Keep in nav / Fix issues / Remove

Notes:
_______________________________
```

---

## 🎯 DECISION MATRIX

### **After Testing Each Unit:**

**If EXCELLENT (All ✅):**
→ Keep in navigation
→ Feature on homepage if appropriate
→ Mark as verified

**If GOOD (Most ✅, minor issues):**
→ Keep in navigation
→ Add to fix list
→ Polish before featuring

**If INCOMPLETE (Missing key elements):**
→ Remove from navigation
→ Add to "needs work" list
→ Fix before re-adding

**If BROKEN (Doesn't load/major errors):**
→ Remove from navigation immediately
→ Flag as broken
→ Fix or archive

---

## ✅ WHAT GOOD LOOKS LIKE

### **Example: Y8 Systems (Gold Standard)**
```
✅ Loads instantly
✅ Professional homepage
✅ All 10 lessons listed clearly
✅ Each lesson loads perfectly
✅ Cultural context rich and authentic
✅ Handouts accessible
✅ Assessment rubrics present
✅ Breadcrumbs work
✅ Mobile-responsive
✅ Print-friendly

= WORLD-CLASS EXPERIENCE
```

### **All Units Should Match This Standard**

---

## 📋 TODAY'S VERIFICATION TASKS

### **Priority 1: Critical Units (Must be Perfect)**
1. Units 1-7 (featured on homepage)
2. Y8 Systems (gold standard)
3. Critical Thinking (prominent)

### **Priority 2: Year-Level Units**
4. Y7 units (4 units)
5. Y8 units (3 units)
6. Y9-10 units (5 units)

### **Priority 3: Cross-Curricular**
7. Math-Science Toolkit
8. Walker, Hērangi units

---

## 🔧 FIX LIST TEMPLATE

```
BROKEN/INCOMPLETE UNITS:

Unit: _________________
Issues:
- [ ] Page doesn't load
- [ ] Missing lessons
- [ ] Broken links
- [ ] No cultural context
- [ ] Template placeholders
- [ ] Inconsistent styling

Priority: HIGH/MEDIUM/LOW
Action: Fix / Remove / Archive
```

---

## ✨ POLISH CHECKLIST

### **For Each Passing Unit, Ensure:**
- [ ] No Lorem ipsum or placeholder text
- [ ] All [TEACHER: customize] sections identified
- [ ] Images load correctly
- [ ] Print stylesheet works
- [ ] Cultural context is authentic (not generic)
- [ ] Māori language spelled correctly (macrons)
- [ ] Consistent color scheme
- [ ] No duplicate navigation components
- [ ] Mobile menu works
- [ ] Accessibility features present

---

## 📊 SUCCESS METRIC

**NOT:** "How many units in navigation?"  
**YES:** "What % of units in navigation provide excellent user experience?"

**Target:** 100% of units in navigation = Verified excellent

---

## 🎯 REVISED APPROACH

### **Phase 1: VERIFY (This Week)**
- Test all 24 units added today
- Document pass/fail for each
- Create fix list

### **Phase 2: FIX (Next Week)**
- Fix failing units
- Polish passing units
- Remove broken units from nav

### **Phase 3: PERFECT (Week 3)**
- 10 verified excellent units
- Feature only the best
- User testing with teachers
- Iterate based on feedback

### **Phase 4: EXPAND (Week 4+)**
- Only THEN add more units
- Each one verified before adding
- Maintain quality standards

---

**QUALITY > QUANTITY**  
**USER EXPERIENCE > FEATURE COUNT**  
**EXCELLENCE > SPEED**

Ready to verify quality properly! 🎯


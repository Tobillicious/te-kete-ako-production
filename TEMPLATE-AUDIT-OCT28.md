# 🔍 TEMPLATE AUDIT - October 28, 2025

**Location:** `/templates/` directory (served at localhost:8080/templates)  
**Created by:** Claude Code agent  
**Status:** Needs audit and cleanup  
**Purpose:** Identify which templates to keep, which to remove, which to create

---

## 📊 **CURRENT STATE (15 files):**

### **HTML Templates (8 files):**
1. `handout-template.html`
2. `lesson-template.html`
3. `unit-template.html`
4. `game-template.html`
5. `standard-handout-template.html`
6. `PERFECT-HANDOUT-TEMPLATE.html`
7. `ULTIMATE-HANDOUT-TEMPLATE.html`
8. `ULTIMATE-LESSON-TEMPLATE.html`
9. `ULTIMATE-UNIT-TEMPLATE.html`
10. `SAMPLE-HANDOUT-DEMO.html`
11. `TEMPLATE-DEMO.html`

### **Documentation (4 files):**
1. `README.md`
2. `HANDOUT-TEMPLATE-GUIDE.md`
3. `COMPREHENSIVE-TEMPLATE-GUIDE.md`
4. `STUDENT-FRIENDLY-PRINT-GUIDE.md`

---

## 🚨 **PROBLEMS IDENTIFIED:**

### **1. TOO MANY HANDOUT TEMPLATES (5!)**
- `handout-template.html`
- `standard-handout-template.html`
- `PERFECT-HANDOUT-TEMPLATE.html`
- `ULTIMATE-HANDOUT-TEMPLATE.html`
- `SAMPLE-HANDOUT-DEMO.html`

**Issue:** Confusing! Which one should agents/users use?  
**Solution:** Keep ONE best handout template, archive rest

---

### **2. "ULTIMATE" NAMING (3 files)**
- `ULTIMATE-HANDOUT-TEMPLATE.html`
- `ULTIMATE-LESSON-TEMPLATE.html`
- `ULTIMATE-UNIT-TEMPLATE.html`

**Issue:** "ULTIMATE" sounds like AI slop (too marketing-y)  
**Solution:** Rename to simple, clear names or verify they're actually good

---

### **3. REDUNDANT DEMOS (2 files)**
- `SAMPLE-HANDOUT-DEMO.html`
- `TEMPLATE-DEMO.html`

**Issue:** Demo files clutter the directory  
**Solution:** Remove or move to separate `/examples/` directory

---

### **4. MISSING TEMPLATES**

Based on actual content types in the site:
- ❌ **Activity template** (for 5-min Do Now activities)
- ❌ **Video activity template** (for YouTube comprehension activities)
- ❌ **Assessment template** (for quizzes/tests)
- ❌ **Interactive template** (for Chart.js/interactive content)

---

## 🎯 **RECOMMENDED TEMPLATE STRUCTURE:**

### **KEEP (Core Templates):**
1. **`handout-template.html`** - Standard print handout
2. **`lesson-template.html`** - 45-75 min lesson plan
3. **`unit-template.html`** - Multi-week unit plan
4. **`game-template.html`** - Interactive games

### **AUDIT NEEDED (Check Quality):**
5. **`PERFECT-HANDOUT-TEMPLATE.html`** - Is this better than `handout-template.html`?
6. **`ULTIMATE-HANDOUT-TEMPLATE.html`** - Is this redundant?
7. **`ULTIMATE-LESSON-TEMPLATE.html`** - Is this better than `lesson-template.html`?
8. **`ULTIMATE-UNIT-TEMPLATE.html`** - Is this better than `unit-template.html`?

### **REMOVE (Redundant/Demo):**
9. **`standard-handout-template.html`** - Likely duplicate of `handout-template.html`
10. **`SAMPLE-HANDOUT-DEMO.html`** - Demo file (move to examples or delete)
11. **`TEMPLATE-DEMO.html`** - Demo file (move to examples or delete)

### **CREATE (Missing):**
12. **`activity-template.html`** - For Do Now activities
13. **`video-activity-template.html`** - For YouTube comprehension
14. **`assessment-template.html`** - For quizzes
15. **`interactive-template.html`** - For Chart.js content

---

## 📋 **AUDIT PLAN:**

### **Phase 1: Visual Inspection (30 mins)**
Open each template in browser and check:
1. Does it load without errors?
2. Is the design on-brand?
3. Does it have sidebar + whakataukī?
4. Is it print-friendly?
5. Does it follow Design-V5?
6. Is it better or worse than alternatives?

### **Phase 2: Comparison (15 mins)**
Compare similar templates:
- `handout-template.html` vs `PERFECT-HANDOUT-TEMPLATE.html` vs `ULTIMATE-HANDOUT-TEMPLATE.html`
- `lesson-template.html` vs `ULTIMATE-LESSON-TEMPLATE.html`
- `unit-template.html` vs `ULTIMATE-UNIT-TEMPLATE.html`

**Choose the BEST of each** and archive the rest

### **Phase 3: Cleanup (15 mins)**
1. Delete redundant templates
2. Rename confusing names (remove "ULTIMATE")
3. Move demo files to `/examples/` directory
4. Update README.md with final list

### **Phase 4: Create Missing (1 hour)**
1. Create `activity-template.html` based on existing activities
2. Create `video-activity-template.html` based on existing video activities
3. Update documentation

---

## 🎯 **IDEAL FINAL STATE:**

```
/templates/
  ├── README.md (updated)
  ├── handout-template.html (THE handout template)
  ├── lesson-template.html (THE lesson template)
  ├── unit-template.html (THE unit template)
  ├── game-template.html (THE game template)
  ├── activity-template.html (NEW)
  ├── video-activity-template.html (NEW)
  ├── assessment-template.html (NEW - optional)
  ├── TEMPLATE-GUIDE.md (consolidated docs)
  └── /examples/ (demo files moved here)
      ├── sample-handout-filled.html
      └── sample-lesson-filled.html
```

**Result:** 
- ✅ Clear, simple structure
- ✅ One template per resource type
- ✅ Easy for agents to find the right template
- ✅ Documentation consolidated

---

## 🤔 **QUESTIONS FOR YOU:**

1. **Which handout template do you prefer?**
   - `handout-template.html`
   - `PERFECT-HANDOUT-TEMPLATE.html`
   - `ULTIMATE-HANDOUT-TEMPLATE.html`

2. **Should I:**
   - **Option A:** Auto-audit by checking file sizes and comparing structures
   - **Option B:** Show you each template visually to decide
   - **Option C:** Just keep the simplest named ones and archive "ULTIMATE"

3. **Priority:**
   - Fix templates NOW (1-2 hours)
   - Or defer to next session?

---

*Audit created: October 28, 2025*  
*Status: Awaiting user direction*


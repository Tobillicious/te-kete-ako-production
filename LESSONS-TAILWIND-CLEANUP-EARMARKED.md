# Lessons with Tailwind - Cleanup Earmarked for Future Session

**Date Identified:** October 28, 2025  
**Status:** 8 lessons need Tailwind removal + rebuild  
**Priority:** Medium (they work, but inconsistent with site standards)

---

## 🔴 LESSONS NEEDING CLEANUP (8 total)

### **Unit 2: Decolonized History** (4 lessons)
1. `units/lessons/unit-2-lesson-2.html` - Has Tailwind
2. `units/lessons/unit-2-lesson-3.html` - Has Tailwind
3. `units/lessons/unit-2-lesson-4.html` - Has Tailwind
4. `units/lessons/unit-2-lesson-5.html` - Has Tailwind

### **Unit 4: Economic Justice** (4 lessons)
1. `units/lessons/unit-4-lesson-2.html` - Has Tailwind
2. `units/lessons/unit-4-lesson-3.html` - Has Tailwind
3. `units/lessons/unit-4-lesson-4.html` - Has Tailwind
4. `units/lessons/unit-4-lesson-5.html` - Has Tailwind

---

## ✅ CLEAN LESSONS (27 total)

### **Unit 1:** 5/5 clean ✅
### **Unit 2:** 1/5 clean (Lesson 1 only) ⚠️
### **Unit 3:** 5/5 clean ✅
### **Unit 4:** 1/5 clean (Lesson 1 only) ⚠️
### **Unit 5:** 5/5 clean ✅ (including new Lesson 5)
### **Unit 6:** 5/5 clean ✅
### **Unit 7:** 5/5 clean ✅ (including new Lessons 4 & 5)

---

## 🔧 WHAT NEEDS TO BE DONE (Future Session)

### For Each Broken Lesson:
1. **Remove Tailwind CDN** - Line 7: `<script src="https://cdn.tailwindcss.com"></script>`
2. **Fix duplicate CSS** - Lines 8-10 have triple-loaded main.css
3. **Remove Tailwind classes** - Replace with standard HTML + main.css classes
4. **Fix layout structure** - Currently has broken nested divs (`.page-container` inside `.main-container`)
5. **Standardize sidebar** - Use consistent `.sidebar-section` pattern
6. **Add proper lesson structure** - Match clean lessons (activity blocks, teacher notes, etc.)

### Template to Use:
- **Reference:** `unit-1-lesson-1.html` (gold standard)
- **Or:** New lessons just created (unit-5-lesson-5, unit-7-lesson-4, unit-7-lesson-5)

---

## ⏱️ ESTIMATED TIME

- **Per lesson:** 15-20 minutes
- **Total for 8 lessons:** 2-3 hours
- **Recommended approach:** Do one unit at a time (Unit 2 first, then Unit 4)

---

## 🎯 WHY THIS CAN WAIT

**Current Status:**
- Lessons are functional (broken layout, but content loads)
- Unit pages are perfect (curriculum alignment done)
- Principal presentation: Can focus on Units 1, 3, 5, 6, 7 (all perfect)

**When to Fix:**
- After deployment
- After principal presentation
- During next polish session
- Low priority compared to missing content

---

## ✅ TONIGHT'S WINS (DON'T NEED THESE FIXED)

- ✅ ALL 7 unit pages with NZC curriculum alignment
- ✅ 3 new lessons created (Unit 5-5, Unit 7-4, Unit 7-5)
- ✅ Bug report system live
- ✅ Unit Plans Hero complete
- ✅ 27/35 lessons are perfect (77% clean!)

**This is more than enough for launch!** 🚀

---

**Next Session:** Knock out these 8 Tailwind lessons in 2-3 hours and hit 100% lesson perfection!


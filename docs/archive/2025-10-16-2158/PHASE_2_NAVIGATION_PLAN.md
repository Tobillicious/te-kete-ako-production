# 📍 PHASE 2: SYSTEMATIC NAVIGATION IMPROVEMENTS
## Unit-Level Navigation & Content Discovery

**Created:** October 10, 2025  
**Overseer:** Coordinating via MCP  
**Prerequisite:** Phase 1 Complete ✅  
**Status:** PLANNING (to be critically evaluated before implementation)

---

## 🎯 PHASE 2 OBJECTIVES

**What we're solving:**
1. **Unit Navigation:** Hard to move between lessons in same unit (Walker, Hērangi)
2. **Progress Tracking:** Students/teachers can't see where they are in a unit sequence
3. **Related Content:** Lessons don't link to supporting handouts/resources
4. **Hub Organization:** lessons.html, handouts.html need better categorization

---

## 📊 SCOPE ANALYSIS

### Files Affected (Estimated):
- **Walker Unit:** 5 lesson HTML files + 1 index
- **Hērangi Unit:** 5 lesson HTML files + 1 index (when created)
- **Other Units:** ~15 existing units across Y7-Y10
- **Hub Pages:** lessons.html, handouts.html, units.html
- **Total Estimate:** ~50-80 files

### Work Required:
- Add prev/next navigation to each lesson
- Add progress indicators
- Cross-link related resources
- Improve hub page filtering/organization

---

## 🔧 DETAILED PLAN

### Task 2.1: Unit Lesson Navigation (Walker Unit)

**Files to modify:** 5 Walker lesson HTML files

**Add to each lesson:**
```html
<!-- Unit Progress Navigation -->
<nav class="unit-nav" style="background: #f0f8f4; padding: 1.5rem; border-radius: 8px; margin: 2rem 0;">
    <div style="text-align: center; margin-bottom: 1rem;">
        <span style="color: #666;">Walker Unit Progress</span>
        <div style="margin-top: 0.5rem;">
            <span style="display: inline-block; width: 40px; height: 8px; background: #2C5F41; border-radius: 4px; margin: 0 2px;"></span>
            <span style="display: inline-block; width: 40px; height: 8px; background: #ccc; border-radius: 4px; margin: 0 2px;"></span>
            <span style="display: inline-block; width: 40px; height: 8px; background: #ccc; border-radius: 4px; margin: 0 2px;"></span>
            <span style="display: inline-block; width: 40px; height: 8px; background: #ccc; border-radius: 4px; margin: 0 2px;"></span>
            <span style="display: inline-block; width: 40px; height: 8px; background: #ccc; border-radius: 4px; margin: 0 2px;"></span>
        </div>
        <span style="color: #666; font-size: 0.9em;">Lesson 1 of 5</span>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span style="color: #999;">← Previous</span>
        <a href="/lessons/walker/index.html" style="color: #2C5F41; font-weight: 600;">↑ Unit Overview</a>
        <a href="/lessons/walker/lesson-1-2-the-great-migration.html" style="background: #2C5F41; color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none;">Next: The Great Migration →</a>
    </div>
</nav>
```

**Variation for each lesson:**
- Lesson 1.1: prev disabled, next = 1.2
- Lesson 1.2: prev = 1.1, next = 1.3
- Lesson 1.3: prev = 1.2, next = 1.4
- Lesson 1.4: prev = 1.3, next = 1.5
- Lesson 1.5: prev = 1.4, next disabled (last lesson)

**Time estimate:** 30 minutes (5 files × 6 minutes each)

---

### Task 2.2: Related Resources Links

**Add to each Walker lesson:**
```html
<!-- Related Resources -->
<aside style="background: #fff8e1; padding: 1.5rem; border-radius: 8px; margin: 2rem 0;">
    <h3>📚 Related Resources</h3>
    <ul style="list-style: none; padding: 0;">
        <li style="margin: 0.5rem 0;">📄 <a href="/handouts/walker-biography.html">Student Handout: Walker Biography</a></li>
        <li style="margin: 0.5rem 0;">📊 <a href="/assessments/walker-unit-rubric.html">Unit Assessment Rubric</a></li>
        <li style="margin: 0.5rem 0;">🌿 <a href="/resources/cultural-consultation-protocols.html">Cultural Protocols</a></li>
    </ul>
</aside>
```

**Time estimate:** 15 minutes

---

### Task 2.3: Hub Page Organization Improvements

**File:** `public/lessons.html`

**Improvements:**
1. Add "Filter by Year Level" tabs (Y7, Y8, Y9, Y10)
2. Add "Filter by Subject" dropdown
3. Group lessons by unit visually
4. Feature Walker/Hērangi at top (already done ✅)
5. Add "Recently Added" section

**Technical approach:**
- Use existing filter dropdowns (already in page)
- Add CSS classes for filtering
- Add JavaScript to make filters functional
- Group visually with section headers

**Time estimate:** 1-2 hours

---

### Task 2.4: Cross-Linking Between Content Types

**Pattern:** Link lessons → handouts → assessments → back to lessons

**Example implementations:**
- From Walker Lesson 1.1 → Link to biography handout
- From biography handout → Link back to Walker Lesson 1.1
- From assessment rubric → Link to all Walker lessons

**Files to modify:** ~20-30 files (lessons + handouts + assessments)

**Time estimate:** 2 hours

---

## ⚖️ CRITICAL EVALUATION (Before Implementation)

### Strengths of This Plan:
✅ **Focused:** Specific files and changes identified
✅ **Incremental:** Can do task by task
✅ **Time-boxed:** Clear estimates
✅ **Testable:** Easy to verify each improvement
✅ **User-centered:** Improves actual teacher/student experience

### Potential Issues:
⚠️ **Scale:** 50-80 files is a lot - might take 6-8 hours
⚠️ **Maintenance:** Future lesson additions need same navigation
⚠️ **Testing:** Need to test each change manually
⚠️ **Coordination:** If multiple agents work, could conflict

### Risks:
🔴 **Breaking existing functionality** - Need to test thoroughly
🟡 **Inconsistent application** - Need templates/patterns
🟡 **Time sink** - Could spend too long on polish

---

## ✅ RECOMMENDATION

### Should we proceed with Phase 2?

**YES, but with modifications:**

1. **Start small:** Do Walker unit only first (5 lessons)
2. **Test thoroughly:** Verify navigation works perfectly
3. **Create reusable component:** Extract navigation pattern
4. **Then scale:** Apply to other units if successful

**Modified approach:**
- Task 2.1 (Walker nav) - DO THIS
- Task 2.2 (Related resources) - DO THIS
- Task 2.3 (Hub organization) - SKIP for now (too complex)
- Task 2.4 (Cross-linking) - DO SELECTIVELY

### Revised Phase 2 Scope:
**Focus:** Perfect navigation for Walker unit (5 lessons)
**Time:** 1-2 hours
**Value:** HIGH - proves the pattern works
**Risk:** LOW - limited scope, easily reversible

---

## 🚀 IMPLEMENTATION PLAN (Revised)

### Step 1: Walker Lesson Navigation (30 min)
- Add prev/next/progress nav to 5 Walker lessons
- Test each link works
- Verify progress bars display correctly

### Step 2: Related Resources (15 min)
- Add related resources sidebar to Walker lessons
- Create placeholder links (can populate later)

### Step 3: Test & Verify (15 min)
- Click through entire Walker unit flow
- Verify all navigation works
- Test on mobile view

### Step 4: Evaluate (15 min)
- Does navigation improve experience?
- Is pattern worth replicating?
- What would we do differently?

**Total Phase 2 (Revised):** 1-1.5 hours

---

## 💬 QUESTIONS FOR USER/TEAM

1. **Approve revised Phase 2 scope?** (Walker only, not all units)
2. **Should I proceed now?** Or wait for input?
3. **Any other priorities?** More important than navigation?

---

**Phase 2 Status:** PLANNED & EVALUATED - Awaiting approval to proceed

**Post in ACTIVE_QUESTIONS.md if you have concerns about this plan!**


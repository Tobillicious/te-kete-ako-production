# 🧪 End-to-End Workflow Testing Plan - v1.0.8

**Date:** October 25, 2025  
**Agent:** cursor-node-1  
**Target:** https://tekete.netlify.app  
**Reason:** Local server testing blocked by terminal hang bug - must test on deployed site

---

## 🎯 **TEST OBJECTIVES**

Validate complete user workflows from start to finish:
1. **Teacher Signup & Resource Assignment** - New teacher onboarding flow
2. **Student Login & Quiz Completion** - Student learning experience
3. **My Kete Database Persistence** - localStorage migration to Supabase
4. **GraphRAG Search Functionality** - Intelligent resource discovery
5. **Component Injection** - Navigation, footer, FAB across all pages

---

## 📋 **TEST 1: Teacher Signup & Resource Assignment**

### User Story:
> As a new teacher, I want to sign up, browse resources, save favorites, and assign them to my class.

### Test Steps:
1. **Navigate to:** https://tekete.netlify.app
2. **Click:** "Sign Up" or "Teacher Login"
3. **Fill form:**
   - Email: `test-teacher-oct25@example.com`
   - Password: (strong password)
   - Role: Teacher
   - School: Mangakōtukutuku College
   - Subjects: Mathematics, Science
4. **Verify:** Account created successfully
5. **Browse:** Navigate to Mathematics Hub
6. **Save resource:** Click "Add to My Kete" on a lesson
7. **Assign resource:** Click "Assign to Class" (if available)
8. **Check My Kete:** Verify saved resource appears in dashboard

### Expected Results:
✅ Signup flow completes without errors  
✅ Teacher dashboard loads with personalized content  
✅ Resources can be saved to My Kete  
✅ Saved resources persist across page reloads  
✅ Database shows new teacher profile

### Pass/Fail Criteria:
- [ ] No console errors during signup
- [ ] Profile created in `profiles` table
- [ ] My Kete saves to `saved_resources` table
- [ ] UI shows confirmation messages

---

## 📋 **TEST 2: Student Login & Quiz Completion**

### User Story:
> As a student, I want to log in, access assigned lessons, complete quizzes, and track my progress.

### Test Steps:
1. **Navigate to:** https://tekete.netlify.app
2. **Click:** "Student Login"
3. **Fill form:**
   - Email: `test-student-oct25@example.com`
   - Password: (strong password)
   - Role: Student
   - Year Level: 9
4. **Verify:** Student dashboard loads
5. **Browse lessons:** Navigate to a lesson with a quiz
6. **Complete quiz:** Answer all questions
7. **Submit:** Click submit button
8. **Check progress:** View My Progress page

### Expected Results:
✅ Student dashboard shows personalized content  
✅ Quiz interface loads correctly  
✅ Quiz submission records to database  
✅ Progress tracker updates  
✅ Scores display correctly

### Pass/Fail Criteria:
- [ ] No console errors during login
- [ ] Student profile created
- [ ] Quiz responses saved to `student_responses` table
- [ ] Progress updated in `student_progress` table

---

## 📋 **TEST 3: My Kete Database Persistence**

### User Story:
> As a user, my saved resources should automatically migrate from localStorage to the database when I log in.

### Test Steps:
1. **While logged OUT:**
   - Browse site
   - Click "Add to My Kete" on 3 resources
   - Verify localStorage has entries
2. **Log IN as teacher/student**
3. **Check My Kete page**
4. **Verify:**
   - All 3 resources appear in My Kete
   - Database query shows entries in `saved_resources`
   - localStorage entries removed after migration

### Expected Results:
✅ localStorage items detected  
✅ Migration script runs automatically  
✅ Items appear in database  
✅ localStorage cleaned up  
✅ No duplicates created

### Pass/Fail Criteria:
- [ ] localStorage → DB migration works
- [ ] No data loss during migration
- [ ] Duplicates prevented
- [ ] Console logs migration success

---

## 📋 **TEST 4: GraphRAG Search Functionality**

### User Story:
> As a user, I want to search for resources and get intelligent recommendations based on GraphRAG relationships.

### Test Steps:
1. **Navigate to:** https://tekete.netlify.app/graphrag-search.html
2. **Test Search:**
   - Query: "māori mathematics"
   - Verify results appear
   - Check quality scores displayed
3. **Test Filters:**
   - Filter by Year Level: Year 9
   - Filter by Subject: Mathematics
   - Verify filtered results
4. **Test Recommendations:**
   - Click on a resource
   - Scroll to "Similar Resources" section
   - Verify recommendations appear
5. **Check GraphRAG badges:**
   - Browse to a lesson page
   - Verify connection badge shows count

### Expected Results:
✅ Search returns relevant results  
✅ Filters work correctly  
✅ GraphRAG recommendations appear  
✅ Connection badges display  
✅ No 401 errors (fixed from v1.0.7 cleanup!)

### Pass/Fail Criteria:
- [ ] Search returns results
- [ ] Filters reduce result set
- [ ] Recommendations are relevant
- [ ] Connection badges show counts
- [ ] No GraphRAG 401 errors

---

## 📋 **TEST 5: Component Injection**

### User Story:
> As a user browsing lessons, I should see consistent navigation, footer, and quick action buttons on every page.

### Test Steps:
1. **Test Navigation Injection:**
   - Visit: `/public/lessons/[any-lesson].html`
   - Verify top navigation appears
   - Check "Home", "Browse", "My Kete" links work
2. **Test Footer Injection:**
   - Scroll to bottom of page
   - Verify footer appears with links
   - Check "About", "Contact", "Privacy" links
3. **Test FAB (Floating Action Button):**
   - Look for circular button bottom-right
   - Click to expand quick actions
   - Verify "Save", "Print", "Share" options
4. **Test Across Page Types:**
   - Lesson page: ✓
   - Handout page: ✓
   - Unit page: ✓
   - Hub page: ✓

### Expected Results:
✅ Navigation loads on all pages  
✅ Footer appears consistently  
✅ FAB works on mobile & desktop  
✅ No layout breaks  
✅ Components respect page styling

### Pass/Fail Criteria:
- [ ] Nav injection working
- [ ] Footer injection working
- [ ] FAB appears and functions
- [ ] No CSS conflicts
- [ ] Mobile responsive

---

## 🔧 **TESTING METHODOLOGY**

### Manual Testing:
1. Use Chrome DevTools (Console, Network, Application tabs)
2. Test on desktop (1920x1080) and mobile (375x667)
3. Record all console errors/warnings
4. Take screenshots of failures
5. Document reproduction steps

### Database Verification:
```sql
-- Check new profiles
SELECT * FROM profiles WHERE created_at > NOW() - INTERVAL '1 hour';

-- Check saved resources
SELECT * FROM saved_resources WHERE saved_at > NOW() - INTERVAL '1 hour';

-- Check student progress
SELECT * FROM student_progress WHERE created_at > NOW() - INTERVAL '1 hour';

-- Check GraphRAG queries (no 401 errors)
SELECT * FROM error_logs WHERE timestamp > NOW() - INTERVAL '1 hour' AND error_message LIKE '%401%';
```

---

## 📊 **SUCCESS CRITERIA**

**Must Pass (Critical):**
- ✅ No signup/login blockers
- ✅ Database writes working
- ✅ GraphRAG search returns results
- ✅ Zero 401 errors (post v1.0.7 cleanup)

**Should Pass (High Priority):**
- ✅ My Kete migration works
- ✅ Component injection consistent
- ✅ Mobile responsive

**Nice to Have:**
- ✅ Fast page loads (<3s)
- ✅ Smooth animations
- ✅ Helpful error messages

---

## 🚨 **KNOWN ISSUES TO WATCH**

From previous sessions:
1. ~~Supabase 401 errors~~ (Fixed in v1.0.7 - ghost entries removed)
2. ~~Infinite retry loops~~ (Fixed in v1.0.5 - max 20 attempts)
3. ~~PWA icon corruption~~ (Fixed in v1.0.5 - regenerated)
4. ~~Syntax errors~~ (Fixed in v1.0.2 - smart quotes)

**New issues to discover!**

---

## 📝 **TEST EXECUTION LOG**

### Test 1: Teacher Signup & Resource Assignment
- **Status:** Pending
- **Tester:** cursor-node-1
- **Results:** TBD

### Test 2: Student Login & Quiz Completion
- **Status:** Pending
- **Results:** TBD

### Test 3: My Kete Database Persistence
- **Status:** Pending
- **Results:** TBD

### Test 4: GraphRAG Search Functionality
- **Status:** Pending
- **Results:** TBD

### Test 5: Component Injection
- **Status:** Pending
- **Results:** TBD

---

**Next:** Execute tests and document results!

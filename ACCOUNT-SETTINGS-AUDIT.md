# Account Settings Page Audit
**Date:** October 29, 2025  
**File:** `account-settings.html`

## 🔴 CRITICAL BUGS FOUND

### 1. **Database Query Bug - WRONG FIELD!**
**Lines:** 420-424, 513-520, 583-586

**Issue:** Code uses `eq('id', this.currentUser.id)` but should use `eq('user_id', this.currentUser.id)`

**Schema Reality:**
```sql
CREATE TABLE profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users(id) -- THIS is what we need!
    ...
)
```

**Impact:** 
- ❌ Profile won't load (wrong ID lookup)
- ❌ Save profile won't work (wrong ID match)
- ❌ Delete account won't work (wrong ID match)

**Fix Required:** Change ALL `.eq('id', ...)` to `.eq('user_id', ...)`

---

### 2. **Missing Profile Fields**
**Current Fields:** Only `display_name` and `school_name`

**Schema Shows These Fields Exist:**
- `role` (teacher/student/admin) - **CRITICAL for role-based features**
- `year_level` (for students)
- `preferred_language` (English/Te Reo)
- `teacher_role` (subject teacher, HOD, etc.)
- `subjects_taught` (array)
- `year_levels_taught` (array)
- `parent_email` (for students)
- `cultural_identity` (array)
- `iwi_affiliation`

**Impact:** Users can't update important profile info after registration!

---

### 3. **Delete Account Incomplete**
**Lines:** 580-600

**Issue:** 
- Uses wrong field (`id` instead of `user_id`)
- Doesn't delete saved_resources
- Can't actually delete auth.users (requires admin API)
- Just signs user out and tells them to contact support

**Better Approach:**
1. Delete from `saved_resources` table
2. Delete from `profiles` table
3. Use Supabase Admin API to delete auth user (or mark profile as deleted)

---

## 🟡 UX/LAYOUT CONCERNS

### 4. **Change Email Uses `prompt()`**
**Line:** 535

**Issue:** Native JavaScript `prompt()` is ugly and not mobile-friendly

**Better:** Modal dialog with proper form validation

---

### 5. **Subscription Section is Placeholder**
**Lines:** 327-339

**Current:** Just says "Beta (Free)" with no action

**Needed for SaaS:**
- Link to `/pricing.html`
- "Upgrade" button (when pricing ready)
- Current plan details
- Billing history (future)

---

### 6. **No Back Navigation**
**Issue:** No link back to "My Kete" or home

**Fix:** Add breadcrumb or back button

---

## ✅ WHAT WORKS WELL

1. **Layout:** Clean, organized sections
2. **Loading States:** Proper auth check and loading UI
3. **Error Handling:** Good message system (success/error/info)
4. **Security Section:** Password reset via email (correct approach)
5. **Modal Design:** Delete confirmation modal is good UX
6. **Styling:** Matches Te Kete Ako design system

---

## 🎯 PRIORITY FIXES

### P0 (BLOCKING - Must Fix Now):
- ✅ Fix database query bug (`.eq('id', ...)` → `.eq('user_id', ...)`)

### P1 (Important - Fix Soon):
- ⏸️ Add role field display
- ⏸️ Add year level field (for students)
- ⏸️ Add subjects/year levels taught (for teachers)

### P2 (Nice to Have - Later):
- ⏸️ Replace `prompt()` with modal for email change
- ⏸️ Add breadcrumb navigation
- ⏸️ Improve delete account flow
- ⏸️ Add cultural fields (cultural_identity, iwi_affiliation)

---

## 📝 RECOMMENDED SECTIONS

**Current Sections:**
1. ✅ Profile Information (display_name, school_name)
2. ✅ Account Information (email, created, last login)
3. ✅ Security (password change)
4. ⚠️ Subscription (placeholder)
5. ✅ Danger Zone (delete account)

**Should Add:**
6. **Role & Preferences** (role display, year level, language)
7. **Teaching Details** (subjects, year levels - if teacher)
8. **Cultural Connection** (cultural_identity, iwi_affiliation - optional)

---

## 🧪 TESTING CHECKLIST

- [ ] Load page while logged out → Should show auth required
- [ ] Load page while logged in → Should load profile
- [ ] Edit display name → Should save
- [ ] Edit school name → Should save
- [ ] Click "Change Email" → Should send confirmation email
- [ ] Click "Change Password" → Should send reset email
- [ ] Try to delete account → Should show modal confirmation
- [ ] Confirm delete → Should delete profile and sign out

---

## 🚀 NEXT STEPS

1. **Fix the critical bug** (`.eq('id', ...)` → `.eq('user_id', ...)`)
2. **Test the fix** (load, save, delete)
3. **Add role display** (show user if they're teacher/student)
4. **Iterate based on beta feedback** (add fields as users request)

---

**Status:** 🟡 **FUNCTIONAL BUT NEEDS CRITICAL BUG FIX**


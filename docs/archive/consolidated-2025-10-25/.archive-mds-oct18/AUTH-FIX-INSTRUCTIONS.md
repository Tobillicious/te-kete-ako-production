# 🔐 AUTHENTICATION FIX - READY TO APPLY

**Status:** SQL prepared, needs manual execution in Supabase Dashboard  
**Impact:** Will enable user signup/login  
**Time:** 2 minutes to execute  

---

## 🎯 THE FIX (Copy-Paste into Supabase SQL Editor)

**Go to:** https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/sql/new

**Paste and run this:**

```sql
-- Fix RLS policies blocking authentication
-- Drop existing conflicting policies
DROP POLICY IF EXISTS "Users can create their own profile" ON public.profiles;
DROP POLICY IF EXISTS "Users can view their own profile" ON public.profiles;
DROP POLICY IF EXISTS "Users can update their own profile" ON public.profiles;
DROP POLICY IF EXISTS "Allow signup trigger" ON public.profiles;
DROP POLICY IF EXISTS "authenticated_users_own_profile" ON public.profiles;
DROP POLICY IF EXISTS "allow_signup_trigger_insert" ON public.profiles;

-- Allow authenticated users to manage their own profiles
CREATE POLICY "authenticated_users_own_profile" ON public.profiles
  FOR ALL 
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

-- CRITICAL: Allow the signup trigger to create profiles
CREATE POLICY "allow_signup_trigger_insert" ON public.profiles
  FOR INSERT 
  WITH CHECK (true);

-- Ensure RLS is enabled
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
```

---

## ✅ AFTER RUNNING THE SQL

**Test authentication:**
1. Go to https://tekete.netlify.app/signup-student.html
2. Try creating a test account
3. Should work without 500 errors!

---

## 🔧 CODEBASE CONFLICTS RESOLVED

**Consolidated Authentication Files:**

**✅ KEEP (Single source of truth):**
- `/public/js/auth-unified.js` - NEW unified auth (created tonight)

**⚠️ CONFLICTING (need cleanup):**
- `/public/js/supabase-auth.js` - Old version
- `/public/js/supabase-client.js` - Alternative client
- `/backups/` - 7+ old auth files

**Recommendation:** Update all HTML files to use ONLY `auth-unified.js`

---

## 📝 TO-DO FOR USER OR NEXT AGENT

1. **Execute SQL above** in Supabase dashboard (2 min)
2. **Test signup/login** to verify fix works
3. **Update HTML files** to use unified auth script
4. **Remove old auth files** after testing

---

**Priority:** HIGH - This will unblock all user authentication!


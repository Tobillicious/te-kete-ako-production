# 🔴 AGENT 3: AUTHENTICATION FIX - URGENT

**Priority:** CRITICAL - Users cannot access platform  
**Owner:** Agent 3 (Authentication Specialist)  
**Status:** 🔴 NOT STARTED  
**ETA:** 30 minutes  
**Blocker:** Supabase RLS policies blocking user signup/login

---

## 🎯 MISSION

Fix the authentication system that is currently blocking all user access to the platform.

---

## 🔍 PROBLEM DIAGNOSIS

### Symptoms:
- Users cannot sign up
- Users cannot log in
- RLS (Row Level Security) policies blocking access
- Database errors on auth endpoints

### Root Cause:
- Supabase RLS policies incorrectly configured
- Blocking legitimate user access
- Auth endpoints returning errors

---

## 📋 TASK CHECKLIST

### Phase 1: Diagnosis (10 minutes)
- [ ] Review Supabase RLS policies in `/supabase/migrations/`
- [ ] Check auth JavaScript files in `/public/js/auth*.js`
- [ ] Test signup flow locally
- [ ] Test login flow locally
- [ ] Identify specific policy blocking access

### Phase 2: Fix (15 minutes)
- [ ] Update RLS policies to allow user registration
- [ ] Fix auth endpoints
- [ ] Ensure user table permissions correct
- [ ] Test user session management
- [ ] Verify auth state persistence

### Phase 3: Testing (5 minutes)
- [ ] Test signup with new user
- [ ] Test login with existing user
- [ ] Verify session persists
- [ ] Check no console errors
- [ ] Confirm database updates

---

## 📁 FILES TO REVIEW/EDIT

**Primary Files:**
- `/supabase/migrations/*.sql` - RLS policies
- `/public/js/auth.js` - Main auth logic
- `/public/js/supabase-client.js` - Client configuration
- `/netlify/functions/auth*.js` - Auth serverless functions (if any)

**Configuration:**
- `.env` - Supabase credentials (DO NOT COMMIT!)
- `netlify.toml` - Deployment config

---

## 🔒 FILE CLAIM

Before starting, update `AGENT_COORDINATION_BOARD.md`:

```markdown
### 🔒 LOCKED - Being Edited
- `supabase/migrations/` - Agent 3 (Auth Fix) - 🔒 LOCKED
- `public/js/auth.js` - Agent 3 (Auth Fix) - 🔒 LOCKED
```

---

## 🧪 TESTING PROTOCOL

```bash
# 1. Check Supabase connection
echo "Testing Supabase connection..."
# Verify SUPABASE_URL and SUPABASE_ANON_KEY in .env

# 2. Test locally
python3 -m http.server 8000
# Visit http://localhost:8000
# Try signup and login

# 3. Check console for errors
# Open browser DevTools → Console
# Look for RLS or permission errors
```

---

## ✅ SUCCESS CRITERIA

- [ ] Users can sign up successfully
- [ ] Users can log in successfully
- [ ] Sessions persist correctly
- [ ] No console errors
- [ ] Database updates properly
- [ ] RLS policies secure but accessible

---

## 📊 REPORT BACK

After completion, update `AGENT_COORDINATION_BOARD.md`:

```markdown
**Agent 3: Authentication Fix**
Status: 🟢 Complete
Files: supabase/migrations/fix-rls.sql, public/js/auth.js
Findings: [What was wrong and how you fixed it]
Next: Ready for production deployment test
```

---

## 🆘 IF BLOCKED

1. Document the blocker
2. Update coordination board
3. Request help from Agent 2 (Overseer)
4. Provide specific error messages

---

**START TIME:** [When you begin]  
**END TIME:** [When complete]  
**DURATION:** [Actual time taken]

---

*This is URGENT. Users are waiting. Kia kaha!* 🚀


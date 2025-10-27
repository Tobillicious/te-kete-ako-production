# 🔐 AUTH & STRIPE SYSTEM AUDIT - October 27, 2025

**STATUS: Research & Planning Phase - NO CODE CHANGES YET**

**🚨 CRITICAL CONTEXT:** Big frontend rollback happened days ago (months of work reverted). Backend is the secret weapon - amazingly well developed and intact. Frontend HTML pages may be old/incomplete from before rollback. Trust the database, rebuild frontend connections cleanly.

---

## 📊 CURRENT STATE ANALYSIS

### ✅ WHAT EXISTS (Built but Not Integrated)

#### 1. **Authentication Pages**
- **`login.html`** (407 lines)
  - Styled auth container
  - Email + password form
  - Loading states
  - Error/success messages
  - Links to register/forgot password
  - **Status:** Exists, needs integration testing

- **`register-simple.html`** (431 lines)
  - Registration form
  - Similar styling to login
  - **Status:** Exists, needs integration testing

- **`my-kete.html`** (592 lines)
  - User dashboard for saved resources
  - Stats cards
  - Saved resources grid
  - **Status:** Exists, needs auth gating

#### 2. **Supabase Integration**
- **`js/supabase-client.js`** ✅ CONFIGURED
  - Supabase URL: `https://nlgldaqtubrlcqddppbq.supabase.co`
  - Anon key: Present (exposed - this is OK for anon key)
  - Global auth helpers: `getCurrentUser()`, `signOut()`, `isLoggedIn()`
  - **Status:** Working, ready to use

- **Database Migration:** `supabase/migrations/20250726_handle_new_user.sql`
  - Auto-creates profile on user registration
  - Triggers on auth.users INSERT
  - Maps metadata to profiles table
  - **Status:** Should be applied

#### 3. **Database Schema (Supabase)**

**Core Auth Tables:**
- **`profiles`** (17 rows currently)
  - Extensive user data: role, display_name, school, year_level, subjects_taught
  - Teacher-specific: registration_number, teacher_role, class_lists
  - Student-specific: date_of_birth, cultural_identity, iwi_affiliation
  - Onboarding: onboarding_completed, personalization_settings
  - **Status:** Well-designed, ready

**Subscription Tables:**
- **`subscription_plans`** (5 rows!) ⚠️ PRICING ALREADY DEFINED
- **`subscriptions`** (0 rows) - Stripe subscription tracking
- **`payment_history`** (0 rows) - Transaction records
- **`school_licenses`** (0 rows) - Enterprise management
- **`kamar_permission_requests`** (0 rows) - School integration approvals

**Content Tables:**
- **`resources`** (25,445 rows!) - All content indexed
- **`user_saved_resources`** (0 rows) - Bookmarks
- **`saved_resources`** (0 rows) - Alternative saved resources table
- **`user_access`** (0 rows) - Analytics tracking

#### 4. **Vision Document**
- **`COMPLETE-SAAS-GAMIFIED-VISION.md`** (727 lines)
  - Comprehensive SaaS + gamification plan
  - Stripe integration details
  - 3-tier pricing model:
    - **FREE:** 5 resources/week, browse only
    - **TEACHER:** $12 NZD/month, unlimited, AI generator
    - **SCHOOL:** $299 NZD/year (50 teachers), analytics
  - 14-day trial flow
  - Standard SaaS pages list
  - Gamification features
  - **Status:** Planning document, not implemented

---

## ❌ WHAT'S MISSING (Critical Gaps)

### 1. **Stripe Frontend Integration**
- ❌ No Stripe.js loaded
- ❌ No Stripe publishable key in frontend
- ❌ No checkout flow
- ❌ No pricing page
- ❌ No billing portal integration
- ❌ No webhook handler

### 2. **Auth Flow Integration**
- ❌ Login page not connected to site navigation
- ❌ Register page not connected
- ❌ No auth state management across site
- ❌ No protected routes/content
- ❌ No trial gating logic
- ❌ Header doesn't show auth state

### 3. **Subscription Management**
- ❌ No subscription selection UI
- ❌ No trial countdown display
- ❌ No upgrade/downgrade flow
- ❌ No cancel subscription UI
- ❌ No billing history page

### 4. **Key Pages Not Built**
- ❌ `/pricing` - Pricing table
- ❌ `/dashboard` - User dashboard (my-kete exists but not as dashboard)
- ❌ `/settings` - User settings
- ❌ `/billing` - Billing management
- ❌ `/forgot-password` (referenced but doesn't exist)
- ❌ `/reset-password` (exists as placeholder)

---

## 🔍 SUBSCRIPTION PLANS IN DATABASE ✅

**5 Plans Configured (Backend Ready!):**

1. **KAMAR Add-on** - $2 NZD/month
   - Individual addon for school integration
   - Requires school permission
   - Status: Inactive (addon to main plan)

2. **Individual Monthly** - **$15 NZD/month** ⭐ PRIMARY TIER
   - Stripe Price ID: `price_1SMHrsDhKhPdHioTGHtK83M4` ✅ LIVE
   - 14-day trial
   - Full access, PDF downloads, AI planner, email support
   - Status: **ACTIVE**

3. **School (Up to 12)** - $200 NZD/month
   - 30-day trial
   - School dashboard, teacher collaboration, student tracking
   - Stripe: Pending setup
   - Status: Active

4. **School (Up to 50)** - $450 NZD/month
   - Same as above + training workshops
   - Stripe: Pending setup
   - Status: Active

5. **School (Up to 1000)** - $600 NZD/month
   - Same as above + custom content, branding, dedicated account manager
   - Stripe: Pending setup
   - Status: Active

**Note:** Individual plan has REAL Stripe price ID. School plans need Stripe setup. Pricing is LOWER than vision doc ($15 vs $12 - actually higher, vision was outdated).

---

## 🚧 FRONTEND ROLLBACK CONTEXT

**What Happened:**
- Big frontend rollback occurred days ago
- MONTHS of frontend work reverted
- Backend survived and is "amazingly well developed"
- Current frontend HTML pages are POST-ROLLBACK (clean slate)
- Previous auth attempts (~1000x) got rolled back

**Backup folders from BEFORE rollback:**
- `backups/auth-consolidation-20250811-151728/`
  - Old auth attempts (pre-rollback)
  - Don't reference these

**Test files in `dist/` (old):**
- `dist/auth-test.html`
- `dist/auth-diagnostics.html`
- Likely from before rollback

**Strategy:** Build clean frontend → backend connections. Backend is ready, just needs clean frontend implementation.

---

## 📋 WHAT NEEDS TO BE DONE (Methodical Plan)

### Phase 1: Foundation (Auth Only, No Stripe)
1. ✅ Verify Supabase migration applied
2. ✅ Test login/register flows work
3. ✅ Add auth state to header (Login → My Kete when logged in)
4. ✅ Protect my-kete.html (redirect if not logged in)
5. ✅ Test logout flow
6. ✅ Build forgot password flow
7. ✅ Build reset password flow

### Phase 2: Subscription Plans UI (No Checkout Yet)
1. ✅ Build `/pricing.html` page
2. ✅ Display 3 tiers from database
3. ✅ Add "Start Free Trial" CTAs
4. ✅ Add subscription status to my-kete
5. ✅ Show trial countdown if on trial

### Phase 3: Stripe Integration
1. ✅ Get Stripe API keys (test mode)
2. ✅ Add Stripe.js to checkout pages
3. ✅ Build checkout flow for Teacher tier
4. ✅ Create webhook endpoint for Stripe events
5. ✅ Test subscription creation
6. ✅ Test webhook updates (subscription_created, payment_succeeded, etc)

### Phase 4: Subscription Management
1. ✅ Build billing portal integration
2. ✅ Add "Manage Subscription" link
3. ✅ Show current plan in my-kete
4. ✅ Add upgrade/downgrade options
5. ✅ Test cancel flow

### Phase 5: Content Gating
1. ✅ Implement free tier limits (5 resources/week)
2. ✅ Add "Upgrade to view" prompts
3. ✅ Track resource access in user_access table
4. ✅ Show paywalls appropriately

### Phase 6: School/Enterprise (Later)
1. Multi-user management
2. Kamar integration
3. School-wide analytics

---

## 🎯 IMMEDIATE NEXT STEPS (Today's Work)

### Step 1: Verify Current Auth Works
- Test login page manually
- Test register page manually
- Check if profiles table gets populated
- Verify Supabase auth helpers work

### Step 2: Review Subscription Plans
- Query subscription_plans table
- Understand current pricing structure
- Verify it matches vision document

### Step 3: Create Detailed Implementation Plan
- Break each phase into specific tasks
- Identify file-by-file changes needed
- Map out which JS files to create/modify
- Plan database queries needed

---

## 💡 KEY DECISIONS NEEDED

1. **Stripe Test vs Live Mode:**
   - Start with test mode
   - Get test API keys
   - Use test webhook endpoint

2. **Trial Logic:**
   - 14 days from registration
   - Soft limits or hard paywall?
   - Grace period after trial ends?

3. **Free Tier:**
   - Track views per week how?
   - Reset counter when?
   - Cookie-based or auth-based?

4. **School Tier:**
   - Build now or later?
   - Requires admin approval system
   - Complex - probably Phase 6

5. **Existing Users:**
   - 17 profiles exist
   - Grant them all free trials?
   - Or leave as-is?

---

## 📝 NOTES

**The Secret Weapon (Backend):**
- Database is VERY well designed ✅
- 25,445 resources indexed ✅
- Subscription plans configured ✅
- Migration ready ✅
- Tables have RLS enabled ✅
- Profiles table comprehensive ✅

**What Needs Building (Frontend):**
- Clean auth UI flows
- Stripe checkout integration
- Subscription status display
- Content gating logic
- Trial countdown UI

**Estimated Complexity:** Medium (backend ready, just frontend work)
**Estimated Time:** 2-3 focused sessions for Phases 1-3
**Risk Level:** Low (backend is solid, standard Stripe pattern)

**Key Advantage:** We're not starting from scratch. Backend is production-ready. Just need clean, methodical frontend implementation.

---

*Document created: Oct 27, 2025 - Research Phase*
*Next: Query subscription plans, then create implementation roadmap*


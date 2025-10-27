# 🚀 AUTH & STRIPE IMPLEMENTATION PLAN
## Methodical, Step-by-Step Roadmap

**Created:** October 27, 2025  
**Status:** Research Complete → Ready for Implementation  
**Approach:** Slow, precise, granular, methodical (like unit-plans polish)

---

## 📊 RESEARCH FINDINGS SUMMARY

### ✅ What Works (Backend Ready)

**Database (Supabase):**
- ✅ 17 existing users (7 teachers, 10 students)
- ✅ Comprehensive `profiles` table with role, school, subjects, etc
- ✅ `subscription_plans` table with 5 configured plans
- ✅ `subscriptions`, `payment_history`, `school_licenses` tables ready
- ✅ `saved_resources` table for bookmarks
- ✅ 25,445 resources indexed in `resources` table
- ✅ Migration `20250726_handle_new_user.sql` creates profiles automatically
- ✅ RLS (Row Level Security) enabled on all tables

**Supabase Connection:**
- ✅ Project URL: `https://nlgldaqtubrlcqddppbq.supabase.co`
- ✅ Fresh Anon Key obtained (different from file - THIS IS THE ISSUE!)
- ✅ `js/supabase-client.js` exists with global helpers
- ✅ `js/auth-ui.js` exists with state management

**Frontend Pages (Post-Rollback):**
- ✅ `login.html` (407 lines) - Clean, styled, form ready
- ✅ `register-simple.html` (431 lines) - Clean, styled, form ready
- ✅ `my-kete.html` (592 lines) - Has auth gating working
- ✅ `forgot-password.html` exists
- ✅ `reset-password.html` exists

**Netlify Functions (Server-side, optional):**
- ✅ `auth-login.js` - Server-side login handler
- ✅ `auth-register.js` - Server-side register handler
- ✅ `auth-forgot-password.js` - Password reset
- ✅ `auth-update-password.js` - Password update

### ❌ What's Broken/Missing

**Critical Issues:**
- ❌ **OUTDATED API KEY** - `supabase-client.js` has expired anon key (401 errors)
- ❌ Login fails with "Invalid API key"
- ❌ No Stripe integration whatsoever
- ❌ No pricing page
- ❌ No billing management
- ❌ No subscription status display
- ❌ No trial logic
- ❌ Header doesn't show logged-in state dynamically

**Console Errors Found:**
```
[ERROR] Failed to load resource: 401
@ https://nlgldaqtubrlcqddppbq.supabase.co/auth/v1/token?grant_type=password
```

---

## 🎯 IMPLEMENTATION PHASES

### **PHASE 0: Polish Auth Pages Design (2-3 hours)** ⭐ DO THIS FIRST
**Goal:** Make auth pages match Te Kete Ako design system BEFORE testing functionality

**Problem:** Auth pages have inline styles and look like AI slop, don't match our polished hub pages.

#### Task 0.1: Move Inline Styles to main.css
**Files:** login.html, register-simple.html, forgot-password.html, reset-password.html
**Action:**
- Remove `<style>` blocks from each page
- Move styles to `css/main.css` as `.auth-page` section
- Use existing CSS variables and design tokens
- Match typography, spacing, colors from hub pages
**Success Criteria:** No inline styles, uses design system

#### Task 0.2: Add Dashboard-style Heroes (Optional)
**Question:** Do auth pages need heroes?
- **Option A:** Simple centered form (clean, minimal)
- **Option B:** Dashboard hero like hub pages (more engaging)
- **Recommendation:** Option A - auth pages should be focused, not busy

#### Task 0.3: Integrate Whakataukī Sidebar
**Current:** Inline hardcoded whakataukī
**Change:** Use `daily-whakatauki.js` like hub pages
**Add:** Auth-specific whakataukī subset (community, growth, learning)
**Success Criteria:** Sidebar whakataukī rotates daily

#### Task 0.4: Match Visual Design
**Elements to polish:**
- Form inputs (match filter dropdowns from hub pages)
- Buttons (match hero tool-section buttons)
- Error/success messages (match site notification system)
- Demo accounts box (make it subtle, not prominent)
- Links (match site link styles)
**Success Criteria:** Looks like it belongs in Te Kete Ako

---

### **PHASE 1: Fix Auth Connection (2-3 hours)**
**Goal:** Make login/register work end-to-end (on now-beautiful pages!)

#### Task 1.1: Update Supabase Anon Key ⚡ CRITICAL
**File:** `js/supabase-client.js`
**Change:** Replace expired key with fresh key
**Test:** Login with demo account `teacher@tekete.nz / password123`
**Success Criteria:** Login works, redirects to homepage

#### Task 1.2: Test Registration Flow
**File:** `register-simple.html`
**Test:** Create new test account
**Check:** 
- Profile created in database
- User can login
- Trigger `handle_new_user()` fires
**Success Criteria:** New user account works end-to-end

#### Task 1.3: Test Forgot Password Flow
**File:** `forgot-password.html`
**Review:** Check if Supabase email is configured
**Test:** Request password reset
**Success Criteria:** Reset email sent (or understand if email config needed)

#### Task 1.4: Update Header Auth State
**Files:** All pages
**Change:** Verify `auth-ui.js` updates nav when logged in
**Test:** Login → see "My Kete" appear in nav, "Login" disappears
**Success Criteria:** Header shows correct auth state

#### Task 1.5: Protect My Kete Page
**File:** `my-kete.html`
**Current:** Shows "Auth Required" message ✅
**Test:** Login → my-kete shows actual saved resources
**Success Criteria:** Auth gating works correctly

---

### **PHASE 2: Build Subscription UI (3-4 hours)**
**Goal:** Display subscription info, no Stripe yet

#### Task 2.1: Build Pricing Page
**File:** `pricing.html` (NEW)
**Content:**
- Hero section (bilingual, functional dashboard pattern)
- 3-tier pricing table from database
- Individual: $15/month, 14-day trial
- School 12: $200/month, 30-day trial
- School 50: $450/month, 30-day trial
- Comparison table of features
- FAQ section
- CTAs: "Start Free Trial" buttons
**Design:** Match unit-plans hero pattern, NZC colors
**Test:** Links from homepage, navigation
**Success Criteria:** Beautiful pricing page, all info accurate

#### Task 2.2: Add Subscription Status to My Kete
**File:** `my-kete.html`
**Add:**
- Subscription tier display
- Trial countdown if on trial
- "Upgrade" button if free/trial
- "Manage Billing" link (placeholder for now)
**Query:** JOIN profiles + subscriptions tables
**Success Criteria:** User sees their current subscription status

#### Task 2.3: Create Subscription Helper Functions
**File:** `js/subscription-helpers.js` (NEW)
**Functions:**
- `getCurrentSubscription()` - Query user's subscription
- `isOnTrial()` - Check trial status
- `daysLeftInTrial()` - Calculate countdown
- `hasFeature(featureName)` - Check if plan includes feature
- `canAccessResource()` - Check limits (free tier = 5/week)
**Test:** Console log user's subscription data
**Success Criteria:** Clean data access layer

#### Task 2.4: Display Trial/Subscription Banners
**Files:** All main pages (index, browse, etc)
**Add:** 
- "🎉 You're on a 14-day trial! 5 days remaining"
- "Upgrade to unlock unlimited access"
- Soft prompts, NOT aggressive
**Position:** Top of page, subtle, dismissible
**Success Criteria:** Users know their subscription status

---

### **PHASE 3: Stripe Integration (4-6 hours)**
**Goal:** Working checkout and payments

#### Task 3.1: Get Stripe Keys
**Action:** User needs to provide:
- Stripe publishable key (test mode): `pk_test_...`
- Stripe secret key (backend): `sk_test_...` (environment variable)
**Store:** 
- Frontend: Create `js/stripe-config.js`
- Backend: Environment variable
**Security:** Never commit secret key to git

#### Task 3.2: Create Checkout Flow
**File:** `checkout.html` (NEW)
**Libraries:** Load Stripe.js
**Flow:**
1. User clicks "Start Free Trial" on pricing page
2. Shows plan summary
3. Stripe Payment Element for card
4. Submit → Creates customer + subscription in Stripe
5. Stripe sends webhook → our handler updates database
6. Redirect to my-kete with success message
**Test:** Use Stripe test card `4242 4242 4242 4242`
**Success Criteria:** Test subscription created

#### Task 3.3: Build Webhook Handler
**File:** `netlify/functions/stripe-webhook.js` (NEW)
**Events to handle:**
- `customer.subscription.created`
- `customer.subscription.updated`
- `customer.subscription.deleted`
- `invoice.payment_succeeded`
- `invoice.payment_failed`
**Action:** Update `subscriptions` table on each event
**Security:** Verify webhook signature
**Test:** Trigger test events from Stripe dashboard
**Success Criteria:** Database updates when Stripe events fire

#### Task 3.4: Build Billing Portal Integration
**File:** `billing.html` (NEW) or just redirect
**Action:** Use Stripe's Customer Portal (one line of code!)
```javascript
const { url } = await stripe.billingPortal.sessions.create({
  customer: customerId,
  return_url: 'https://tekete.co.nz/my-kete'
});
window.location.href = url;
```
**Features:** 
- Cancel subscription
- Update card
- View invoices
- Downgrade/upgrade
**Success Criteria:** User can manage subscription in Stripe portal

---

### **PHASE 4: Content Gating (2-3 hours)**
**Goal:** Enforce subscription limits

#### Task 4.1: Implement Free Tier Limits
**Logic:**
- Track resource views in `user_access` table
- COUNT views per week per user
- If > 5 and user is free tier → show paywall
**Files:** `js/content-gating.js` (NEW)
**UI:** "You've used 5/5 free views this week. Upgrade for unlimited access!"
**Success Criteria:** Free users hit 5-resource limit

#### Task 4.2: Add Download Protection
**Logic:**
- PDF download buttons check subscription tier
- Free tier → upgrade prompt
- Paid tier → download works
**Success Criteria:** Downloads gated by tier

#### Task 4.3: Add AI Generator Limits
**Logic:**
- Track AI generations in database
- Teacher tier: 20/month
- School tier: Unlimited
**Future:** Not urgent, AI generator doesn't exist yet
**Success Criteria:** Framework in place

---

### **PHASE 5: Polish & Testing (2-3 hours)**
**Goal:** Everything smooth and professional

#### Task 5.1: Test Complete User Journey
**Flow:**
1. Visit homepage → Click "Start Free Trial"
2. Register new account
3. Browse 5 resources (hit limit)
4. Upgrade to paid tier
5. Browse unlimited
6. Access billing portal
7. Cancel subscription
8. Test downgrade UX
**Success Criteria:** Smooth, no errors, great UX

#### Task 5.2: Add Error Handling
**Scenarios:**
- Payment fails → clear message, retry option
- Webhook fails → manual reconciliation
- Network error → graceful degradation
**Success Criteria:** No user sees cryptic errors

#### Task 5.3: Polish UI/UX
**Apply unit-plans learnings:**
- Functional > decorative
- Clear CTAs
- Bilingual where appropriate
- Subtle animations
- Consistent with site design
**Success Criteria:** Feels like part of Te Kete Ako, not bolted on

---

## 🔧 DETAILED TECHNICAL SPECS

### File Structure
```
/js/
  supabase-client.js        ← Update anon key (TASK 1.1)
  auth-ui.js                ← Already good ✅
  subscription-helpers.js   ← Create (TASK 2.3)
  content-gating.js         ← Create (TASK 4.1)
  stripe-config.js          ← Create (TASK 3.1)
  checkout-flow.js          ← Create (TASK 3.2)

/netlify/functions/
  stripe-webhook.js         ← Create (TASK 3.3)
  auth-*.js                 ← Already exist ✅

/pages/
  login.html                ← Fix key, test ✅
  register-simple.html      ← Fix key, test ✅
  my-kete.html              ← Add subscription status (TASK 2.2)
  pricing.html              ← CREATE (TASK 2.1)
  checkout.html             ← CREATE (TASK 3.2)
  billing.html              ← CREATE or redirect (TASK 3.4)
  forgot-password.html      ← Test (TASK 1.3)
  reset-password.html       ← Test (TASK 1.3)
```

### Database Queries Needed

**Check subscription status:**
```sql
SELECT s.*, sp.name, sp.amount_cents, sp.trial_period_days
FROM subscriptions s
JOIN subscription_plans sp ON s.plan_id = sp.id
WHERE s.user_id = $1 AND s.status IN ('active', 'trialing');
```

**Check if trial expired:**
```sql
SELECT 
  CASE 
    WHEN current_period_end < NOW() THEN true 
    ELSE false 
  END as trial_expired,
  EXTRACT(DAY FROM current_period_end - NOW()) as days_remaining
FROM subscriptions
WHERE user_id = $1 AND status = 'trialing';
```

**Count resource views this week:**
```sql
SELECT COUNT(*) as views_this_week
FROM user_access
WHERE user_id = $1 
  AND accessed_at > NOW() - INTERVAL '7 days'
  AND access_type = 'view';
```

---

## 🎯 IMMEDIATE NEXT STEPS (TASK 1.1)

### The First Fix - Update API Key

**Before changing code, document:**
1. Current key location: `js/supabase-client.js` line 6
2. Current key value: `eyJ...` (expires 2037)
3. Fresh key value: `eyJ...` (expires 2068)
4. Test plan: Login with `teacher@tekete.nz / password123`

**Change:**
- Line 6 of `supabase-client.js`
- Replace old anon key with fresh key
- Test in browser immediately
- Verify console shows no 401 errors
- Verify login works

**Then:**
- Test register
- Test forgot password
- Document what works/doesn't work
- Move to next task ONLY when this is confirmed working

---

## 📋 TASK CHECKLIST (Update as we go)

### Phase 1: Auth Connection
- [ ] 1.1 - Update Supabase anon key
- [ ] 1.2 - Test registration flow
- [ ] 1.3 - Test forgot password flow
- [ ] 1.4 - Update header auth state
- [ ] 1.5 - Verify my-kete protection

### Phase 2: Subscription UI
- [ ] 2.1 - Build pricing.html
- [ ] 2.2 - Add subscription status to my-kete
- [ ] 2.3 - Create subscription helpers
- [ ] 2.4 - Display trial banners

### Phase 3: Stripe
- [ ] 3.1 - Get Stripe keys (needs user)
- [ ] 3.2 - Build checkout flow
- [ ] 3.3 - Build webhook handler
- [ ] 3.4 - Integrate billing portal

### Phase 4: Content Gating
- [ ] 4.1 - Implement free tier limits
- [ ] 4.2 - Add download protection
- [ ] 4.3 - AI generator limits (future)

### Phase 5: Polish
- [ ] 5.1 - Test complete journey
- [ ] 5.2 - Error handling
- [ ] 5.3 - UI/UX polish

---

## 🔑 KEYS & SECRETS NEEDED

### From User:
1. **Stripe Publishable Key (Test):** `pk_test_...`
   - Used in frontend JavaScript
   - Safe to commit to git
   - Get from Stripe Dashboard → Developers → API Keys → Test Mode

2. **Stripe Secret Key (Test):** `sk_test_...`
   - Used in Netlify Functions (server-side)
   - Environment variable only
   - NEVER commit to git
   - Set in Netlify dashboard or `.env` file

3. **Stripe Webhook Secret:** `whsec_...`
   - Used to verify webhook signatures
   - Environment variable only
   - Get from Stripe Dashboard → Webhooks → Add endpoint

### Already Have:
- ✅ Supabase URL: `https://nlgldaqtubrlcqddppbq.supabase.co`
- ✅ Supabase Anon Key (fresh): `eyJhbGc...` (expires 2068)
- ⚠️ Supabase Service Role Key: Likely in environment, check Netlify

---

## 💡 DESIGN DECISIONS TO MAKE

### 1. Trial Strategy
**Options:**
- **A) Auto-start trial on signup** (14 days, no card required)
- **B) Require card upfront** (more friction, less churn)
- **Recommendation:** A - matches vision doc, better UX

### 2. Free Tier Tracking
**Options:**
- **A) Cookie-based** (easy to bypass, no login required)
- **B) Auth-required** (must create account for ANY access)
- **C) Hybrid** (browse without account, save/download requires account)
- **Recommendation:** C - browse open, features require account

### 3. Email Configuration
**Supabase needs SMTP for:**
- Password resets
- Email verification
- Subscription notifications
**Check:** Is Supabase email configured? Or using default?
**Action:** Test forgot-password to see if email sends

### 4. Redirect After Login
**Current:** Redirects to `index.html`
**Options:**
- Homepage (current)
- My Kete (personalized)
- Last viewed page (complex but best UX)
- **Recommendation:** My Kete for returning users, homepage for first login

### 5. Existing 17 Users
**What to do with them?**
- **Option A:** Leave as-is (no subscription)
- **Option B:** Grant all 14-day trial automatically
- **Option C:** Grandfather them in with free access
- **Recommendation:** Discuss with user, probably Option B

---

## 📖 LESSONS FROM UNIT-PLANS POLISH

**Apply same methodology:**
1. **One task at a time** - Don't batch
2. **Test immediately** - After each change
3. **Ask "What does teacher NEED?"** - Function over decoration
4. **Iterate on feedback** - Fix issues as they appear
5. **Be precise** - Exact keys, exact queries, exact flows

**Specific to auth:**
- Teacher needs FAST login (social auth? Email magic links?)
- Teacher needs SIMPLE pricing (not confusing tiers)
- Teacher needs TRUST (security, privacy, NZ data residency)
- Teacher needs NO FRICTION (trial without card)

---

## 🧪 TESTING STRATEGY

### Manual Testing Checklist

**Auth Flows:**
- [ ] Register new account (teacher)
- [ ] Login with new account
- [ ] Logout
- [ ] Login again
- [ ] Register duplicate email (should fail gracefully)
- [ ] Forgot password request
- [ ] Check email for reset link
- [ ] Reset password
- [ ] Login with new password

**Subscription Flows (after Stripe):**
- [ ] Start free trial
- [ ] Browse resources (unlimited during trial)
- [ ] Trial expires → becomes free tier
- [ ] Hit free tier limit (5 resources)
- [ ] Upgrade to paid tier
- [ ] Browse unlimited
- [ ] Access billing portal
- [ ] Update card
- [ ] Cancel subscription
- [ ] Verify access downgraded

**Edge Cases:**
- [ ] Expired session → re-login
- [ ] Invalid credentials → clear error
- [ ] Network timeout → retry option
- [ ] Payment fails → clear next steps
- [ ] Webhook delayed → eventual consistency

---

## 🎨 DESIGN CONSISTENCY STRATEGY

**Problem Identified:** Auth pages look like AI slop, not like polished Te Kete Ako.

**What unit-plans/hub pages have:**
- ✅ Functional dashboard heroes (bilingual, tool sections)
- ✅ Rainbow year badges with curriculum colors
- ✅ Subtle micro-animations
- ✅ Consistent typography (CSS variables)
- ✅ Professional spacing
- ✅ Whakataukī from `daily-whakatauki.js`
- ✅ Clean semantic HTML (no inline styles)

**What auth pages have:**
- ❌ Inline `<style>` blocks (100+ lines of AI slop)
- ❌ Generic centered white boxes
- ❌ Hardcoded inline whakataukī
- ❌ No connection to design system
- ❌ Different button styles, form styles, spacing

**Solution:**
1. Extract all auth styles to `css/main.css` as new section
2. Use existing CSS variables for colors, spacing, typography
3. Match form inputs to filter dropdowns we already have
4. Match buttons to hero tool-section buttons
5. Keep auth pages FOCUSED (no busy heroes, just clean centered forms)
6. Add subtle whakataukī sidebar (like hub pages)
7. Make it feel seamless - auth is part of Te Kete Ako, not a separate app

**Design Pattern for Auth Pages:**
- Sidebar: Whakataukī (rotating, auth-themed)
- Main: Centered form card (max-width 500px)
- No hero (keep focus on form)
- Professional, minimal, trustworthy
- Bilingual where appropriate (buttons, labels)

---

## 🚦 READY TO START

**Phase 0, Task 0.1 is ready to execute.**

We polish design FIRST, THEN fix functionality. Beautiful + functional, in that order.

Waiting for user approval to proceed with design polish.

---

*Research complete: October 27, 2025*  
*Ready for methodical, precise implementation*  
*Backend is the secret weapon - now let's build the frontend connection!* 🔐


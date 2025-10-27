# 🚀 STRATEGIC ROADMAP: Launch-Ready Te Kete Ako
**Date:** October 27, 2025 (Evening)  
**Status:** Pre-Launch → Free Beta → Paid SaaS  
**Timeline:** Next 4-6 weeks

---

## 🎯 CURRENT STATE SNAPSHOT

### ✅ What's EXCELLENT (99%)
- **161 resources** ready (81 handouts, 35 lessons, 31 Y8, 8 units, 6 games)
- **Design system** polished, culturally authentic, beautiful
- **Navigation** flawless, bilingual, NZ Curriculum aligned
- **Backend** secretly amazing - Supabase fully configured, 17 test users
- **Database** production-ready with subscription tables
- **Domain** purchased (`tekete.co.nz`)

### ⚠️ What Needs Work (1%)
- **Auth pages** - exist but need design polish + functionality fixes
- **My Kete** - exists but not connected to backend
- **Content quality** - "pretty good" but could be improved
- **Stripe** - not integrated yet (but database ready)

---

## 🎨 THE THREE STRATEGIC PRIORITIES

### 1️⃣ **CONTENT QUALITY** (Foundation)
*"Good enough to charge for eventually"*

### 2️⃣ **AUTH SYSTEM** (Gateway)
*"Free to start, built for paid"*

### 3️⃣ **MY KETE** (Value Prop)
*"Why create an account?"*

---

## 📊 PRIORITY 1: CONTENT QUALITY AUDIT

### What "Pretty Good" Means
Your content IS high quality. But here's what could level it up:

#### Handouts (81 files)
**Strengths:**
- Print-optimized ✅
- NZC aligned ✅
- Cultural integration ✅
- Professional formatting ✅

**Could Improve:**
- **Consistency:** Some use Tailwind, some use main.css, some inline styles
- **Answer keys:** Many comprehension handouts lack teacher answer guides
- **Differentiation:** Not all have scaffolding/extension notes
- **Assessment rubrics:** Missing on most activities
- **Real-world connections:** Could be stronger in some

**Quick Win Actions:**
1. Audit top 20 most-used handouts
2. Add teacher notes sections (1-2 paragraphs)
3. Standardize CSS (all use main.css)
4. Add "Teaching Tips" boxes
5. Include suggested modifications

---

#### Lesson Plans (35 unit lessons + Y8)
**Strengths:**
- Complete sequences ✅
- Detailed activities ✅
- Timing included ✅
- Cultural responsiveness ✅

**Could Improve:**
- **Student voice:** Not all include reflection/feedback moments
- **Formative assessment:** Some lessons lack check-for-understanding
- **Digital tools:** Could integrate more tech (when appropriate)
- **Parent communication:** No "send home" summary for whānau
- **Accessibility notes:** Not all address diverse learners

**Quick Win Actions:**
1. Add "Formative Check" boxes (2-3 per lesson)
2. Include "Whānau Connection" paragraph (homework/context)
3. Add "Accessibility Notes" section (dyslexia, EAL, gifted)
4. Suggest 1-2 digital tool options per lesson
5. Student reflection prompts at end

---

#### Unit Plans (8 complete)
**Strengths:**
- Comprehensive ✅
- Culturally grounded ✅
- Research-based ✅
- Beautiful presentation ✅

**Could Improve:**
- **Summative assessments:** Not all units have proper end assessments
- **Moderation examples:** No exemplar student work
- **Cross-curricular links:** Could be more explicit
- **Community connections:** Missing external expert/speaker suggestions
- **Te reo integration:** Varies by unit (some excellent, some thin)

**Quick Win Actions:**
1. Add summative assessment for each unit
2. Include 2-3 cross-curricular connection ideas
3. Suggest community experts/resources
4. Ensure every unit has substantial te reo components
5. Add "Unit at a Glance" 1-page overview

---

### Content Quality Implementation Plan

**Phase 1: Top 10 Audit (Week 1)**
- Identify 10 most popular/valuable resources
- Polish to 100% (answer keys, teacher notes, accessibility)
- Use as template for others

**Phase 2: Batch Updates (Weeks 2-3)**
- Handouts: Add teacher notes to all
- Lessons: Add formative checks + whānau connections
- Units: Add summative assessments

**Phase 3: New Content (Week 4)**
- Create 5 "Quick Win" resources (high-demand, easy to use)
- Examples: NCEA assessment exemplars, Moderation resources, etc.

---

## 🔐 PRIORITY 2: AUTH SYSTEM IMPLEMENTATION

### The Backend Secret Weapon ✅

From your audit, the backend is INCREDIBLE:
- **Supabase fully configured** with auth, profiles, subscriptions
- **17 test users** already in database
- **Subscription plans defined:** $15/month (Teacher), $200/month (School 12), etc.
- **25,445 resources indexed**
- **All tables ready:** user_saved_resources, user_access, payment_history

**This is 70% of the work DONE.**

---

### What's Missing: Frontend Connection

#### Phase 0: Auth Page Design Polish (2-3 hours) ⭐ CRITICAL FIRST STEP

**Problem:** Login/register pages look like "AI slop" (your words from audit)
- Inline `<style>` blocks (100+ lines)
- Generic centered white boxes
- Doesn't match Te Kete Ako design
- Hardcoded whakatauki

**Solution:** Make auth feel integrated
1. Extract styles to main.css
2. Use design system colors/typography
3. Add sidebar with rotating whakataukī
4. Match cultural authenticity of rest of site
5. Keep FOCUSED (no busy heroes, just clean forms)

**Files to Polish:**
- `login.html` (407 lines)
- `register-simple.html` (431 lines)
- `forgot-password.html`
- `reset-password.html`

**Estimated Time:** 2-3 hours  
**Priority:** DO THIS FIRST before fixing functionality

---

#### Phase 1: Fix Auth Functionality (3-4 hours)

**The Issue:** Supabase anon key needs updating

From audit:
> ❌ **OUTDATED API KEY** - `supabase-client.js` has expired anon key (401 errors)

**The Fix:**
1. Update Supabase anon key in `js/supabase-client.js`
2. Test login with demo account
3. Test registration flow
4. Verify profile creation trigger works
5. Test logout
6. Update header to show auth state (Login → My Kete when logged in)

**Success Criteria:**
- User can register
- User can login
- Profile auto-creates in database
- Header updates dynamically
- My Kete page shows after login

---

#### Phase 2: My Kete Basic Functionality (4-5 hours)

**Current State:** Page exists (592 lines) but not connected

**Connect to Backend:**
1. Query `user_saved_resources` table
2. Display saved resources in grid (match browse.html cards)
3. Add "Save" button to all resource pages
4. Save/unsave functionality (⭐ toggle)
5. Show stats: "You've saved 12 resources"

**Simple, Useful Features:**
- View all saved resources
- Filter by type (Unit/Lesson/Handout)
- Filter by subject
- Remove from My Kete
- "Recently Viewed" section (query `user_access`)

**NO GAMIFICATION YET** - Keep it simple, functional

---

#### Phase 3: Subscription UI (No Stripe Yet) (3-4 hours)

**Build the Interface (Don't Connect Payment Yet)**

1. **Create `/pricing.html`**
   - Display 3 tiers from database (Free, Teacher $15/mo, School)
   - Beautiful cards (match design system)
   - "Coming Soon" buttons (not functional yet)
   - Clear feature comparison

2. **Add Subscription Status to My Kete**
   - Query `subscriptions` table
   - Show: "Free Account" or "Teacher Plan - Active"
   - Show: "14 days remaining in trial" (if applicable)
   - Button: "Upgrade Plan" (links to pricing, not functional)

3. **Prepare for Trials**
   - Logic for 14-day countdown
   - UI for trial status
   - "Upgrade" prompts (gentle, not annoying)

**Why Build UI First:**
- Test user flow without payment complexity
- Get feedback on pricing/features
- Launch as "Coming Soon" feature
- Add Stripe later when ready to charge

---

#### Phase 4: Stripe Integration (8-10 hours) - LATER

**Do This When Ready to Actually Charge**

Not urgent for launch. You said:
> "no where near something we're really gonna charge for just yet"

**But Build Foundation Now:**
- Pricing page exists ✅
- Subscription tables ready ✅
- UI shows trial status ✅
- Database tracks everything ✅

When you're ready:
1. Get Stripe test API keys
2. Add Stripe.js to checkout page
3. Create webhook handler (Netlify function)
4. Test with Stripe test cards
5. Launch in test mode
6. Switch to live mode when confident

---

## 🧺 PRIORITY 3: MY KETE - THE VALUE PROP

### Why Do Teachers Create Accounts?

**Currently:** Not much reason  
**Need:** Clear value from day 1

### My Kete V1 Features (Launch)

**Core Functionality:**
1. ⭐ **Save Resources** - One-click bookmark
2. 📂 **View Saved** - All your bookmarks in one place
3. 🔍 **Filter Saved** - By type, subject, year level
4. 📊 **Simple Stats** - "You've saved 12 resources", "6 lessons, 4 handouts, 2 units"
5. 🕒 **Recently Viewed** - Last 10 resources you looked at

**That's It for V1.** Simple, useful, works.

---

### My Kete V2 Features (Post-Launch)

Add later when you have user feedback:

**Organization:**
- Create custom collections ("My Y8 Unit", "Term 1 Resources")
- Rename saved resources
- Add personal notes

**Collaboration:**
- Share My Kete with colleagues
- School-wide resource libraries
- Rate & review resources

**Personalization:**
- "Recommended for you" (based on saves)
- Weekly email digest (optional)
- Dashboard widgets (upcoming lessons, popular saves)

**Gamification:**
- Points for contributions
- Badges for milestones
- Leaderboards (opt-in)

---

## 📈 GRAPHRAG: USE CAUTIOUSLY

### Status: EXISTS, Handle With Care 🚨

**What It Is:**
- 467 resources indexed in Supabase
- 516 relationships mapped
- Knowledge graph of all content

**What It's Good For:**
- Search improvements (semantic, not just keyword)
- "Resources like this" recommendations
- Understanding content gaps
- Agent coordination (for you, not users)

**What It's DANGEROUS For:**
- Design decisions (led to 5-CSS crisis before)
- Overcomplicating simple things
- "Ultimate" ambitions that break working systems

### GraphRAG Use Cases (Good)

1. **Content Recommendations**
   - "Teachers who used this also used..."
   - "Related lessons for this unit"
   - Show in My Kete or resource pages

2. **Search Enhancement**
   - Semantic search across all resources
   - "Find lessons about kaitiakitanga"
   - Better than keyword matching

3. **Content Gap Analysis**
   - What subjects/year levels need more resources?
   - Which topics have weak coverage?
   - Guide content creation priorities

4. **Agent Coordination** (Your Tool)
   - Help you understand what exists
   - Track what's been improved
   - Coordinate multi-agent work

### GraphRAG Use Cases (Dangerous)

❌ **Don't Use For:**
- Design system decisions
- Adding "features" (keep it simple)
- Anything that adds complexity
- "Ultimate" or "revolutionary" ideas

---

## 🎯 LAUNCH STRATEGY: 3 PHASES

### Phase 1: **FREE BETA** (Weeks 1-2)
*"Soft launch to test everything"*

**Features:**
- All resources free
- Account creation works
- My Kete basic functionality
- No payment, no trials yet

**Goals:**
- Get 50-100 teacher signups
- Test auth system under load
- Fix bugs
- Gather feedback on content

**Launch to:**
- Your personal network
- NZ teacher Facebook groups (soft pitch)
- r/TeachingNZ (Reddit)
- Small announcement, low-key

---

### Phase 2: **FREE WITH TRIALS** (Weeks 3-4)
*"Introduce tiers, don't charge yet"*

**Features:**
- Free tier: Browse all, save 10 resources
- Teacher tier: Announced ($15/mo) but FREE during beta
- "Reserve your Teacher account (Free for early adopters)"
- Pricing page visible

**Goals:**
- Test subscription UI
- See which features people value
- Build email list of "will pay when live"
- Refine pricing based on feedback

**Marketing:**
- Email beta users
- Slightly bigger social media push
- "Early access" messaging
- Testimonials from beta users

---

### Phase 3: **PAID LAUNCH** (Weeks 5-6)
*"Open for business"*

**Features:**
- Free tier: 5 resources/week
- Teacher tier: $15/month (or adjusted based on feedback)
- School tier: Available
- Stripe fully integrated
- 14-day free trials

**Goals:**
- First 10 paying customers
- Revenue validation
- Sustainable operation
- Scale up content creation

**Marketing:**
- Official launch announcement
- Press release (NZ education media)
- Paid social ads (small budget, test)
- Partnerships with schools

---

## ⏱️ TIME ESTIMATES

### To Launch Beta (Weeks 1-2)

**Content Quality (20 hours):**
- 10 hours: Top 10 resource polish
- 10 hours: Batch updates (teacher notes, formative checks)

**Auth System (15 hours):**
- 3 hours: Auth page design polish ⭐
- 4 hours: Fix Supabase connection
- 3 hours: Test all auth flows
- 5 hours: My Kete basic connection

**Polish & Test (10 hours):**
- 5 hours: Browser testing, mobile testing
- 3 hours: Fix bugs found in testing
- 2 hours: Deployment to tekete.co.nz

**TOTAL: ~45 hours** (1 week full-time, 2 weeks part-time)

---

### To Paid Launch (Weeks 3-6)

**Subscription UI (12 hours):**
- 4 hours: Pricing page design
- 4 hours: My Kete subscription status
- 4 hours: Trial countdown UI

**Stripe Integration (12 hours):**
- 4 hours: Checkout flow
- 4 hours: Webhook handler
- 4 hours: Testing & polish

**Content Expansion (20 hours):**
- Create 10 new "high-value" resources
- Polish 20 more existing resources
- Add teacher community features

**TOTAL: ~44 hours** (another 2-3 weeks)

---

## 🎯 RECOMMENDED NEXT STEPS

### This Week (Hours 1-10)

1. **Auth Page Design Polish** (3 hours)
   - Extract styles from inline to main.css
   - Add whakataukī sidebar
   - Match Te Kete Ako design
   - Files: login.html, register-simple.html

2. **Fix Supabase Connection** (2 hours)
   - Update anon key in supabase-client.js
   - Test login/register flows
   - Verify profile creation

3. **My Kete Basic Connection** (3 hours)
   - Connect to user_saved_resources table
   - Display saved resources
   - Add "Save" buttons to resource pages

4. **Content Audit** (2 hours)
   - Identify top 10 resources
   - List specific improvements needed
   - Create content polish checklist

### Next Week (Hours 11-20)

5. **Polish Top 10 Resources** (6 hours)
6. **Browser Testing** (2 hours)
7. **My Kete Filtering** (2 hours)
8. **Deploy to tekete.co.nz** (2 hours)
9. **Invite 10 beta testers** (1 hour)
10. **Gather initial feedback** (ongoing)

---

## 💡 KEY INSIGHTS

### What Makes This Doable

1. **Backend is 70% done** - Supabase configured, tables ready
2. **Content exists** - 161 resources, just need polish
3. **Design is beautiful** - No major redesign needed
4. **Clear path** - Auth → My Kete → Pricing → Stripe

### What Could Derail This

1. **Perfectionism** - "Good enough to charge for" not "perfect"
2. **Feature creep** - Build V1 first, add later
3. **GraphRAG temptation** - Don't let it overcomplicate
4. **Auth rabbit holes** - Fix basics, advanced features later

### Success Criteria

**Beta Launch:**
- 50 users
- Auth works reliably
- My Kete saves/displays
- Zero critical bugs

**Paid Launch:**
- 10 paying customers
- $150/month revenue (proof of concept)
- Positive user feedback
- Sustainable operation

---

## 🧺 FINAL THOUGHTS

You're **incredibly close** to launching something valuable. The foundation is solid:
- Beautiful, culturally authentic design
- 161 quality resources
- Backend secretly amazing
- Domain ready

**Don't overthink it.** 

Build Phase 1 (auth + My Kete), launch free beta, get feedback, iterate.

You said it yourself:
> "we're getting near launching something"

**You are.** Next 2 weeks = beta launch. Let's do this. 🚀

---

**Created:** October 27, 2025  
**Next Review:** After auth pages polished + Supabase connected  
**Status:** Ready to execute

*"Mā te huruhuru ka rere te manu"* - It is the feathers that enable the bird to fly

You have all the feathers. Time to fly. 🦅


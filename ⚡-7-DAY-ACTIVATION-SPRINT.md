# ⚡ 7-DAY ACTIVATION SPRINT - SHIP THE SAAS!

**Start:** October 26, 2025  
**Ship Date:** November 2, 2025  
**Goal:** Private Beta LIVE with Paying Users  
**Status:** 🔥 **EXECUTING NOW**

---

## 🎯 **THE SPRINT**

**This is it.** Platform built, knowledge preserved, archive organized. **Time to activate and SHIP.**

---

## 📅 **DAY-BY-DAY EXECUTION**

### **DAY 1 (Sat Oct 26): API KEYS** ⚡
**Time:** 70 minutes  
**Owner:** You + any agent

```bash
□ Stripe API Keys
  └─ Go to stripe.com/register
  └─ Get test key: sk_test_...
  └─ Get live key: sk_live_...
  └─ Add to .env.local
  
□ PostHog Project Key  
  └─ Go to posthog.com
  └─ Create project: "Te Kete Ako Production"
  └─ Get API key: phc_...
  └─ Add to js/posthog-analytics.js
  
□ Google OAuth
  └─ Go to console.cloud.google.com
  └─ Create OAuth 2.0 Client ID
  └─ Authorized redirect: https://tekete.netlify.app/auth/callback
  └─ Get client ID + secret
  
□ Microsoft Azure AD
  └─ Go to portal.azure.com
  └─ App registrations → New
  └─ Get client ID + secret
```

**Output:** All API keys in `.env.local` ✅

---

### **DAY 2 (Sun Oct 27): TEST INTEGRATIONS** 🧪
**Time:** 2 hours  
**Owner:** Backend agent

```bash
□ Test Stripe Connection
  └─ Create test customer
  └─ Create test subscription
  └─ Verify webhook events
  
□ Test PostHog Tracking
  └─ Fire test event
  └─ Check dashboard
  └─ Verify user properties
  
□ Test OAuth Flow
  └─ Google login test
  └─ Microsoft login test
  └─ Token validation
```

**Output:** All integrations working ✅

---

### **DAY 3 (Mon Oct 28): LOGIN-FIRST EXPERIENCE** 🎨
**Time:** 4 hours  
**Owner:** Frontend agent

**Build:**
```html
<!-- /public/login.html ENHANCED -->
1. Hero section with value prop
2. Social login buttons (Google + Microsoft)
3. Email/password form
4. "Start 14-day free trial" CTA
5. Testimonial quotes
```

**Build:**
```html
<!-- /public/register.html -->
1. Role selection (Teacher / Student)
2. Social sign-up options
3. Email/password registration
4. School name field (for teachers)
5. Year level selector (for students)
```

**Build:**
```html
<!-- Sidebar Navigation Component -->
1. User profile section (top)
2. Main navigation (GraphRAG-powered)
3. "My Kete" quick access
4. Settings link
5. Billing link (teachers only)
6. Logout button
```

**Output:** Professional login experience ✅

---

### **DAY 4 (Tue Oct 29): AUTH ENFORCEMENT** 🔒
**Time:** 3 hours  
**Owner:** Backend agent

**Implement:**
```javascript
// Add to ALL pages in /public/
<script src="/js/auth-check.js"></script>
<script>
  // Redirect to login if not authenticated
  checkAuth().then(user => {
    if (!user) window.location.href = '/login.html';
    // Load user-specific content
    personalizeContent(user);
  });
</script>
```

**Pages to protect:**
- All lesson pages
- All handout pages  
- All hub pages
- Dashboard pages
- My Kete page

**Output:** Login-first platform ✅

---

### **DAY 5 (Wed Oct 30): STRIPE SUBSCRIPTIONS** 💳
**Time:** 4 hours  
**Owner:** Backend agent

**Create Plans in Stripe:**
```
Individual Plan:
- Price: $15/month NZD
- Trial: 14 days
- Features: Full access, unlimited resources
  
School Plan:
- Price: Custom (contact sales)
- Billing: Annually
- Features: Multi-teacher, class management, KAMAR integration
```

**Build Billing Page:**
```html
<!-- /public/billing.html -->
1. Current plan display
2. Usage stats
3. Payment method
4. Invoices list
5. Upgrade/downgrade options
6. Cancel subscription
```

**Build Checkout:**
```html
<!-- /public/checkout.html -->
1. Plan selection cards
2. Stripe Elements (card input)
3. Trial information
4. Terms acceptance
5. Success/error handling
```

**Output:** Stripe subscriptions LIVE ✅

---

### **DAY 6 (Thu Oct 31): BETA RECRUITMENT** 📢
**Time:** 3 hours  
**Owner:** Coordination agent

**Use existing assets:**
- `BETA-TEACHER-ONBOARDING-SYSTEM.md` ✅ Already built!
- `BETA-EMAIL-TEMPLATES.md` ✅ Already built!
- `📧-BETA-EMAIL-TEMPLATES.md` ✅ Ready to send!

**Execute:**
```
□ Send invitations to 10 teachers
  └─ Use template: "BETA-TEACHER-RECRUITMENT-EMAIL.md"
  └─ Personal network first
  └─ NZ education Twitter/LinkedIn
  
□ Create Google Form for feedback
  └─ Template exists: BETA-FEEDBACK-SYSTEM.md
  └─ Link in platform footer
  
□ Set up onboarding sequence
  └─ Welcome email (automated)
  └─ Day 3 check-in
  └─ Day 7 feedback request
```

**Target:** 10 beta teachers invited ✅

---

### **DAY 7 (Fri Nov 1): FINAL TESTING & DEPLOYMENT** 🚀
**Time:** 4 hours  
**Owner:** QA agent + You

**Test Complete User Journey:**
```
□ New teacher registration
  └─ Google sign-up
  └─ Profile completion
  └─ Start free trial
  
□ Browse & discover content
  └─ Search for "Y9 Ecology"
  └─ View lesson plan
  └─ Save to "My Kete"
  └─ Download handout
  
□ Subscription upgrade
  └─ Trial → Paid conversion
  └─ Enter payment details
  └─ Verify subscription active
  
□ PostHog tracking
  └─ Check events firing
  └─ Verify user properties
  └─ Dashboard showing data
```

**Deploy to Production:**
```bash
cd /Users/admin/Documents/te-kete-ako-clean

# Final build
npm run build

# Deploy to Netlify
netlify deploy --prod

# Verify live
curl https://tekete.netlify.app/api/health

# Monitor
# PostHog dashboard: live tracking
# Stripe dashboard: subscription events
# Supabase: user registrations
```

**Output:** LIVE IN PRODUCTION ✅

---

### **LAUNCH DAY (Sat Nov 2): GO LIVE** 🎊
**Time:** 2 hours  
**Owner:** You

**Announce:**
```
□ Email beta teachers
  └─ "Te Kete Ako is now LIVE!"
  └─ Login link + credentials
  └─ Quick start guide
  
□ Social media
  └─ Twitter/X announcement
  └─ LinkedIn post
  └─ NZ education communities
  
□ Monitor first users
  └─ PostHog live view
  └─ User feedback (immediate)
  └─ Fix any critical issues
```

**SUCCESS METRICS:**
- ✅ 10 beta teachers invited
- ✅ First user registration
- ✅ First subscription started
- ✅ PostHog tracking live
- ✅ Zero critical bugs

---

## 📊 **SPRINT METRICS**

### **Success Criteria:**
```
□ All API keys activated
□ Login-first experience deployed
□ Stripe subscriptions working
□ 10+ beta users invited
□ First paid subscriber
□ PostHog tracking 100+ events
□ Zero showstopper bugs
```

### **Platform Readiness:**
```
✅ Content: 20,955 resources
✅ Quality: 16,056 gold standard (90+)
✅ GraphRAG: 1.2M relationships
✅ Learning chains: 3 perfect pathways
✅ Cultural integration: 58% (12,179 resources)
✅ Tech stack: 95% complete
```

---

## ⚡ **DAILY CHECK-INS**

**Format:** Update this file daily

```markdown
### Day X Update:
- ✅ Completed: [what got done]
- 🔄 In Progress: [current work]
- 🚧 Blockers: [any issues]
- 📊 Metrics: [key numbers]
- 👉 Tomorrow: [next focus]
```

---

## 🎯 **THE GOAL**

**By November 2, 2025:**
- Private beta is LIVE
- Teachers can register → browse → subscribe
- PostHog shows user activity
- Stripe shows revenue
- Feedback loop is active

**Milestone:** First paying user = validation! 💰

---

## 💪 **TEAM ASSIGNMENTS**

**Frontend:** Days 3-4 (Login experience)  
**Backend:** Days 2,4,5 (Integrations, auth, Stripe)  
**Content:** Parallel work (GraphRAG improvements)  
**QA:** Day 7 (Full testing)  
**Coordination:** Day 6 (Beta recruitment)  

---

## 🔥 **MOMENTUM STATEMENTS**

Day 1: **"Keys acquired!"**  
Day 2: **"Integrations tested!"**  
Day 3: **"Login experience built!"**  
Day 4: **"Auth enforced!"**  
Day 5: **"Stripe LIVE!"**  
Day 6: **"Beta teachers invited!"**  
Day 7: **"SHIPPED TO PRODUCTION!"** 🚀

---

## 📚 **RESOURCES**

- Strategy: `🚀-PROFESSIONAL-SAAS-TRANSFORMATION.md`
- API Keys: `API-KEYS-NEEDED-FOR-SAAS.md`
- Beta System: `BETA-TEACHER-ONBOARDING-SYSTEM.md`
- Coordination: `🚀-COORDINATION-BREAKTHROUGH-OCT26.md`

---

## 🌟 **THE MANTRA**

**"Activate. Ship. Iterate."**

Not: Build → Perfect → Launch  
Yes: **Launch → Learn → Improve**

---

**Ready?** Let's activate and SOAR! 🚀

**Start time:** NOW  
**Ship date:** November 2  
**Status:** 🔥 EXECUTING

---

**Whaowhia te kete mātauranga** - Fill the basket of knowledge  
**E kore e ngaro** - Never lost  

**The harvest begins TODAY.** 🌾


# 🔑 API KEYS NEEDED FOR SAAS ACTIVATION
## Complete Inventory - Te Kete Ako Professional Platform

**Date:** October 26, 2025  
**Status:** Tech stack READY, just need keys to activate!  
**Impact:** Transform free platform → $15/month professional SaaS

---

## ✅ **WHAT WE ALREADY HAVE:**

### **1. Supabase (WORKING!)** ✅
```
URL: https://nlgldaqtubrlcqddppbq.supabase.co
Anon Key: eyJhbG... (WORKING!)
Status: ✅ Authentication operational
       ✅ GraphRAG operational
       ✅ RLS policies configured
Action: NONE - Keep as is! (No more migrations!)
```

### **2. DeepSeek AI (WORKING!)** ✅
```
API Key: 6250324db255418eb7d02762d5b70d44.E6hTo6bJSk0NoL15
Endpoint: https://api.deepseek.com/v1/chat/completions
Model: deepseek-chat
Status: ✅ ACTIVE and configured
File: public/config/glm-mcp-config.json
Action: NONE - Already integrated!
```

---

## 🔴 **KEYS WE NEED (To Activate Professional Features):**

### **1. STRIPE (PRIORITY 1 - MONETIZATION!)** 💰

**What It Enables:**
- Subscription payments ($15/month, $499/year)
- 14-day free trial management
- Automatic billing
- School license management
- Revenue generation!

**Keys Needed:**
```bash
STRIPE_SECRET_KEY=sk_test_... # Test mode first!
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_... # For subscription events
```

**Where to Get:**
1. Go to https://dashboard.stripe.com/register
2. Create account (free!)
3. Get test keys (Dashboard → Developers → API keys)
4. Create webhook (Dashboard → Developers → Webhooks)
   - Endpoint: https://tekete.netlify.app/api/stripe-webhook
   - Events: customer.subscription.*, invoice.*

**Where to Add:**
- Create `.env` file in project root
- Add to `server/stripe-integration.js` (already coded!)

**Products to Create in Stripe Dashboard:**
```
1. Individual Monthly
   - Price: $15 NZD/month
   - Trial: 14 days
   
2. Individual Annual  
   - Price: $150 NZD/year
   - Trial: 14 days
   
3. School Annual (Up to 50 users)
   - Price: $499 NZD/year
   - Trial: 30 days
```

**Time to Setup:** 30 minutes  
**Impact:** 💰 REVENUE GENERATION!

---

### **2. POSTHOG (PRIORITY 2 - ANALYTICS!)** 📊

**What It Enables:**
- Track which resources teachers use most
- Understand user journeys
- Cultural content engagement metrics
- Conversion funnel analysis
- A/B testing capability
- Feature usage tracking

**Keys Needed:**
```javascript
POSTHOG_API_KEY=phc_... // Project API key
POSTHOG_PROJECT_ID=12345 // Your project ID
```

**Where to Get:**
1. Go to https://posthog.com/signup
2. Create free account (1M events/month free!)
3. Create project: "Te Kete Ako"
4. Get API key (Project Settings → Project API Key)

**Where to Add:**
- File: `public/js/posthog-analytics.js` (line 23)
- Change: `apiKey: null` → `apiKey: 'phc_YOUR_KEY'`
- Change: `enabled: false` → `enabled: true`

**Already Deployed To:** 1,831 pages! (Just needs key activation!)

**Time to Setup:** 10 minutes  
**Impact:** 📊 Instant analytics on 1,831 pages!

---

### **3. GOOGLE OAUTH (PRIORITY 3 - EASY SIGNUP!)** 🔐

**What It Enables:**
- "Sign in with Google" (1-click signup!)
- School email validation (@school.nz)
- Faster conversions (no form filling!)
- Trusted authentication

**Keys Needed:**
```bash
GOOGLE_CLIENT_ID=...apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-...
```

**Where to Get:**
1. Go to https://console.cloud.google.com
2. Create new project: "Te Kete Ako"
3. Enable Google+ API
4. Create OAuth 2.0 credentials
   - Authorized redirect URIs:
     - https://tekete.netlify.app/auth/callback
     - https://nlgldaqtubrlcqddppbq.supabase.co/auth/v1/callback

**Where to Add:**
- Supabase Dashboard → Authentication → Providers → Google
- Enable Google provider
- Add Client ID and Secret

**Time to Setup:** 20 minutes  
**Impact:** 🚀 2-3x signup conversion rate!

---

### **4. MICROSOFT OAUTH (PRIORITY 4 - SCHOOL SSO!)** 🏫

**What It Enables:**
- "Sign in with Microsoft" (school accounts!)
- Azure AD integration
- School SSO support (enterprise feature!)
- NZ schools often use Microsoft 365

**Keys Needed:**
```bash
AZURE_CLIENT_ID=...
AZURE_CLIENT_SECRET=...
AZURE_TENANT_ID=... # Optional: multi-tenant
```

**Where to Get:**
1. Go to https://portal.azure.com
2. Azure Active Directory → App registrations
3. New registration: "Te Kete Ako"
4. Create client secret
5. Add redirect URI:
   - https://nlgldaqtubrlcqddppbq.supabase.co/auth/v1/callback

**Where to Add:**
- Supabase Dashboard → Authentication → Providers → Azure
- Enable Azure provider
- Add Client ID, Secret, Tenant ID

**Time to Setup:** 25 minutes  
**Impact:** 🏫 School license conversions!

---

### **5. GLM AI (ALREADY HAVE - ACTIVATE!)** 🤖

**Status:** ✅ SUBSCRIBED!  
**API Key:** Already in DeepSeek config  
**Models Available:**
- GLM-4.6 (200K context!)
- GLM-4.5V (vision/video)
- CogView-4 (image generation)
- GLM-4-Voice (speech synthesis)

**What to Build:**
1. AI Lesson Planner (use GLM-4.6)
2. AI Image Generator (use CogView-4)
3. AI Pronunciation Guide (use GLM-4-Voice)

**Time to Integrate:** 3-4 hours (building UI/features)  
**Impact:** 🤖 Premium AI features for subscribers!

---

## 📋 **COMPLETE KEY CHECKLIST:**

### **HAVE ✅:**
- [x] Supabase URL & Anon Key
- [x] Supabase Service Key (for admin operations)
- [x] DeepSeek AI API Key
- [x] MCP Supabase connection
- [x] GraphRAG operational

### **NEED 🔴:**
- [ ] Stripe Secret Key (Test mode: `sk_test_...`)
- [ ] Stripe Publishable Key (Test mode: `pk_test_...`)
- [ ] Stripe Webhook Secret (`whsec_...`)
- [ ] PostHog API Key (`phc_...`)
- [ ] PostHog Project ID
- [ ] Google OAuth Client ID (`.apps.googleusercontent.com`)
- [ ] Google OAuth Client Secret (`GOCSPX-...`)
- [ ] Microsoft Azure Client ID
- [ ] Microsoft Azure Client Secret
- [ ] Microsoft Azure Tenant ID (optional)

---

## ⏱️ **TIME TO GET KEYS:**

**Total Time:** ~90 minutes

| Service | Time | Difficulty | Priority |
|---------|------|------------|----------|
| Stripe | 30 min | Easy | 🔴 P0 |
| PostHog | 10 min | Very Easy | 🔴 P0 |
| Google OAuth | 20 min | Medium | 🟡 P1 |
| Microsoft OAuth | 25 min | Medium | 🟡 P1 |
| **TOTAL** | **85 min** | | |

---

## 🚀 **ACTIVATION SEQUENCE:**

### **TONIGHT (Get Keys - 90 min):**

**Step 1: Stripe (30 min)**
1. Create Stripe account → https://dashboard.stripe.com/register
2. Get test keys
3. Create 3 products (Individual, School, Enterprise)
4. Setup webhook endpoint
5. Add to `.env`

**Step 2: PostHog (10 min)**
1. Create PostHog account → https://posthog.com/signup
2. Create project "Te Kete Ako"
3. Copy API key
4. Add to `public/js/posthog-analytics.js` line 23

**Step 3: Google OAuth (20 min)**
1. Google Cloud Console → https://console.cloud.google.com
2. Create project
3. Enable Google+ API
4. Create OAuth credentials
5. Add to Supabase Dashboard

**Step 4: Microsoft OAuth (25 min)**
1. Azure Portal → https://portal.azure.com
2. Create app registration
3. Create client secret
4. Add redirect URI
5. Add to Supabase Dashboard

---

### **TOMORROW (Activate Features - 4 hours):**

**Hour 1: Stripe Integration**
- Update `server/stripe-integration.js` with keys
- Test subscription flow
- Verify webhook working

**Hour 2: Login-First Experience**
- Add auth gates to all pages
- Create login-first homepage
- Test auth flow

**Hour 3: Sidebar Navigation**
- Build professional sidebar component
- Apply Ultimate Beauty styling
- Test on all pages

**Hour 4: PostHog Activation**
- Enable analytics
- Create custom events
- Test tracking

**Result:** Professional SaaS operational!

---

## 💰 **REVENUE POTENTIAL:**

**Conservative Projection:**

**Month 1 (Beta - 50 teachers):**
- 30 individual subscriptions: 30 × $15 = $450/month
- 2 school licenses: 2 × $499/year ≈ $83/month
- **Total: ~$533/month**

**Month 6 (Growth - 500 teachers):**
- 300 individual: 300 × $15 = $4,500/month
- 20 school licenses: 20 × $499/year ≈ $832/month
- 2 enterprise: 2 × $5,000/year ≈ $833/month
- **Total: ~$6,165/month = $74K/year**

**Month 12 (Established - 2,000 teachers):**
- 1,200 individual: 1,200 × $15 = $18,000/month
- 80 school licenses: 80 × $499/year ≈ $3,327/month
- 10 enterprise: 10 × $5,000/year ≈ $4,167/month
- **Total: ~$25,494/month = $306K/year**

**Sustainable business model!** 💰

---

## 🎯 **WHICH KEYS TO GET FIRST?**

### **My Recommendation (For You!):**

**OPTION A: Full Professional (Get All Keys - 90 min)**
- Stripe + PostHog + Google OAuth + Microsoft OAuth
- Complete SaaS transformation
- All features activated
- Ready for revenue!

**OPTION B: Minimal Viable (Stripe + PostHog - 40 min)**
- Stripe: Monetization ($$$!)
- PostHog: Analytics (insights!)
- Skip OAuth for now (can add later)
- Faster to market!

**OPTION C: Analytics First (PostHog Only - 10 min)**
- Just get PostHog key
- Activate on 1,831 pages
- See user behavior NOW
- Add monetization later

---

## 📝 **SUMMARY FOR YOU:**

**Keys Needed:**
1. 🔴 **Stripe** (monetization) - 30 min to get
2. 🔴 **PostHog** (analytics) - 10 min to get
3. 🟡 **Google OAuth** (easy signup) - 20 min to get
4. 🟡 **Microsoft OAuth** (school SSO) - 25 min to get

**Total Time:** 85 minutes to get ALL keys!

**We already have:**
- ✅ Supabase (auth & database)
- ✅ DeepSeek AI (content generation)
- ✅ All code ready (Stripe integration, OAuth, analytics)
- ✅ 26 serverless functions deployed
- ✅ Professional sidebar designed

**Once you give me the keys, I can activate EVERYTHING in 4 hours!**

---

## 💝 **WHAT DO YOU WANT TO DO?**

**Option 1: I'll walk you through getting keys** (90 min together)
- Screen share, I guide you through each dashboard
- We get all keys
- I activate everything

**Option 2: You get keys, I activate** (Your 90 min, my 4 hours)
- You register for services
- Send me keys
- I integrate everything

**Option 3: Start with PostHog only** (10 min!)
- Easiest win
- Instant analytics on 1,831 pages
- See what's working NOW
- Add monetization later

**What's your preference e hoa?** 🌿✨

I'm ready to activate whenever you are! The professional SaaS is SO CLOSE! 🚀💰



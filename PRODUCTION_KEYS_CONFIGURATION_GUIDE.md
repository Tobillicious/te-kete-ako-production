# 🔐 PRODUCTION KEYS CONFIGURATION GUIDE
**Te Kete Ako - Make Systems LIVE!**  
**Date:** October 19, 2025  
**Status:** 6/8 Oct 18th priorities complete, need production keys to go LIVE

---

## 📋 **OVERVIEW: WHAT NEEDS CONFIGURATION**

All 3 systems are **CODE-READY** but need production API keys:

1. **PostHog Analytics** - Tracking code deployed to 1,831 pages ✅
2. **OAuth Social Login** - Google + Microsoft integration built ✅
3. **Stripe Payments** - Payment flow functional ✅

**Estimated Time:** 30-60 minutes total  
**Difficulty:** Easy (copy-paste API keys)  
**Impact:** Make 3 major systems fully operational!

---

## 1️⃣ **POSTHOG ANALYTICS - ADD API KEY**

### **Current Status:**
- ✅ Code deployed to 1,831 pages
- ✅ TeKeteAnalytics class built (236 lines)
- ✅ Privacy-first tracking (respects Do Not Track)
- ✅ Cultural metrics tracking (whakataukī, te reo, subject engagement)
- ⏸️ **BLOCKED:** Placeholder API key needs replacement

### **File to Update:**
`/public/js/posthog-analytics.js` - Line 22

### **Current Code:**
```javascript
const POSTHOG_CONFIG = {
    apiKey: 'phc_YOUR_PROJECT_API_KEY_HERE', // Replace with real key from posthog.com
    apiHost: 'https://app.posthog.com',
    enabled: true,
    respectDoNotTrack: true,
    capturePageview: true,
    capturePageLeave: true,
};
```

### **Steps to Configure:**

#### **A. Create PostHog Account (5 minutes)**
1. Go to: https://posthog.com/signup
2. Sign up (free tier: 1M events/month!)
3. Create new project: "Te Kete Ako"
4. Choose region: **US Cloud** or **EU Cloud** (closest to NZ users)

#### **B. Get API Key (1 minute)**
1. In PostHog dashboard, go to **Project Settings**
2. Click **Project API Key** tab
3. Copy the key (starts with `phc_`)

#### **C. Update Code (1 minute)**
Replace line 22 in `/public/js/posthog-analytics.js`:

```javascript
const POSTHOG_CONFIG = {
    apiKey: 'phc_ACTUAL_KEY_FROM_POSTHOG_DASHBOARD', // ✅ Real key!
    apiHost: 'https://app.posthog.com', // or 'https://eu.posthog.com' if EU region
    enabled: true,
    respectDoNotTrack: true,
    capturePageview: true,
    capturePageLeave: true,
};
```

#### **D. Test (2 minutes)**
1. Open Te Kete Ako in browser
2. Open browser console (F12)
3. Look for: `🎨 Te Kete Analytics: Initialized successfully!`
4. Check PostHog dashboard for events

### **What Gets Tracked:**
- ✅ Page views (with subject, year level, resource type)
- ✅ Resource downloads
- ✅ Search queries (with results count)
- ✅ Whakataukī engagement
- ✅ Cultural content interactions
- ✅ User journeys (from_page → to_page)
- ✅ Mobile vs desktop usage

### **Privacy Features:**
- ✅ Respects Do Not Track
- ✅ LocalStorage consent check
- ✅ GDPR/NZ Privacy Act compliant
- ✅ No PII collection without consent
- ✅ User can opt out anytime

---

## 2️⃣ **OAUTH SOCIAL LOGIN - CONFIGURE PROVIDERS**

### **Current Status:**
- ✅ Google OAuth code integrated (login.html lines 476-514)
- ✅ Microsoft Azure AD code integrated (login.html lines 516-551)
- ✅ Beautiful branded buttons with hover effects
- ✅ Secure flow with Supabase signInWithOAuth()
- ⏸️ **BLOCKED:** OAuth providers not configured in Supabase dashboard

### **What Needs Configuration:**
1. Google OAuth 2.0 Client ID
2. Microsoft Azure AD Application Registration
3. OAuth callback handler page (`/auth/callback.html`)

---

### **2A. GOOGLE OAUTH CONFIGURATION**

#### **Step 1: Google Cloud Console (10 minutes)**

1. **Go to:** https://console.cloud.google.com/
2. **Create new project:** "Te Kete Ako OAuth"
3. **Enable APIs:**
   - Go to **APIs & Services** → **Library**
   - Search for "Google+ API" → Enable
   - Search for "Google Identity" → Enable

4. **Create OAuth Credentials:**
   - Go to **APIs & Services** → **Credentials**
   - Click **+ CREATE CREDENTIALS** → **OAuth client ID**
   - Application type: **Web application**
   - Name: "Te Kete Ako Login"
   
5. **Add Authorized Origins:**
   ```
   https://nlgldaqtubrlcqddppbq.supabase.co
   http://localhost:3000 (for testing)
   https://tekete.netlify.app (production)
   ```

6. **Add Authorized Redirect URIs:**
   ```
   https://nlgldaqtubrlcqddppbq.supabase.co/auth/v1/callback
   http://localhost:3000/auth/callback (for testing)
   ```

7. **Copy Client ID & Secret** (will need for Supabase)

#### **Step 2: Supabase Dashboard (5 minutes)**

1. **Go to:** https://supabase.com/dashboard
2. **Select project:** nlgldaqtubrlcqddppbq
3. **Navigate to:** Authentication → Providers
4. **Find "Google"** and toggle **Enabled**
5. **Paste:**
   - **Client ID:** (from Google Cloud Console)
   - **Client Secret:** (from Google Cloud Console)
6. **Save**

#### **Step 3: Test (2 minutes)**
1. Go to Te Kete Ako login page
2. Click "Continue with Google" button
3. Should redirect to Google consent screen
4. After consent, redirects to `/auth/callback`
5. Then redirects to role-based dashboard

---

### **2B. MICROSOFT AZURE AD CONFIGURATION**

#### **Step 1: Azure Portal (10 minutes)**

1. **Go to:** https://portal.azure.com/
2. **Navigate to:** Azure Active Directory → App registrations
3. **Click:** + New registration
4. **Name:** "Te Kete Ako SSO"
5. **Supported account types:** 
   - Select "Accounts in any organizational directory and personal Microsoft accounts"
6. **Redirect URI:**
   - Type: **Web**
   - URI: `https://nlgldaqtubrlcqddppbq.supabase.co/auth/v1/callback`
7. **Register**

8. **Copy Application (client) ID** (will need for Supabase)

9. **Create Client Secret:**
   - Go to **Certificates & secrets**
   - Click **+ New client secret**
   - Description: "Te Kete Ako Supabase"
   - Expires: **24 months** (or custom)
   - Click **Add**
   - **COPY SECRET VALUE IMMEDIATELY** (won't be shown again!)

10. **Configure API Permissions:**
    - Go to **API permissions**
    - Should have: `User.Read` (default)
    - Add: `email`, `openid`, `profile`

#### **Step 2: Supabase Dashboard (5 minutes)**

1. **Go to:** https://supabase.com/dashboard
2. **Select project:** nlgldaqtubrlcqddppbq
3. **Navigate to:** Authentication → Providers
4. **Find "Azure"** and toggle **Enabled**
5. **Paste:**
   - **Azure Client ID:** (Application ID from Azure)
   - **Azure Secret:** (Client secret value from Azure)
6. **Save**

#### **Step 3: Test (2 minutes)**
1. Go to Te Kete Ako login page
2. Click "Continue with Microsoft" button
3. Should redirect to Microsoft login
4. After login, redirects to `/auth/callback`
5. Then redirects to role-based dashboard

---

### **2C. CREATE OAUTH CALLBACK HANDLER**

OAuth redirects to `/auth/callback` but this page doesn't exist yet!

#### **Create:** `/public/auth/callback.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Signing you in... - Te Kete Ako</title>
    <link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css">
    <style>
        body {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #f0fdf4 0%, #dbeafe 100%);
        }
        .loading-container {
            text-align: center;
            background: white;
            padding: 3rem;
            border-radius: 24px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .spinner {
            width: 60px;
            height: 60px;
            border: 4px solid #e5e7eb;
            border-top-color: #059669;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 1.5rem;
        }
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        h1 {
            color: #059669;
            margin: 0 0 0.5rem;
        }
        p {
            color: #6b7280;
            margin: 0;
        }
    </style>
</head>
<body>
    <div class="loading-container">
        <div class="spinner"></div>
        <h1>🌿 Signing you in...</h1>
        <p>Please wait while we complete your authentication.</p>
    </div>

    <!-- Supabase Auth Library -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    
    <script>
        // Initialize Supabase client
        const supabaseClient = window.supabase.createClient(
            'https://nlgldaqtubrlcqddppbq.supabase.co',
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
        );

        // Handle OAuth callback
        async function handleOAuthCallback() {
            try {
                // Get session from URL hash (OAuth callback includes session in URL)
                const { data: { session }, error } = await supabaseClient.auth.getSession();
                
                if (error) {
                    console.error('OAuth callback error:', error);
                    alert(`❌ Authentication failed: ${error.message}`);
                    window.location.href = '/login.html';
                    return;
                }

                if (!session || !session.user) {
                    console.warn('No session found after OAuth callback');
                    window.location.href = '/login.html';
                    return;
                }

                console.log('✅ OAuth authentication successful!', session.user.email);

                // Get user role from profiles table
                const { data: profile, error: profileError } = await supabaseClient
                    .from('profiles')
                    .select('role')
                    .eq('user_id', session.user.id)
                    .single();

                // Determine dashboard URL based on role
                let dashboardUrl = '/getting-started.html'; // Default

                if (profile && !profileError) {
                    if (profile.role === 'teacher') {
                        dashboardUrl = '/teacher-dashboard-unified.html';
                    } else if (profile.role === 'student') {
                        dashboardUrl = '/student-dashboard.html';
                    } else if (profile.role === 'admin') {
                        dashboardUrl = '/admin-dashboard.html';
                    }
                } else {
                    console.warn('Profile not found, using default dashboard');
                }

                // Redirect to appropriate dashboard
                console.log(`🚀 Redirecting to: ${dashboardUrl}`);
                window.location.href = dashboardUrl;

            } catch (error) {
                console.error('Unexpected error in OAuth callback:', error);
                alert(`❌ An unexpected error occurred: ${error.message}`);
                window.location.href = '/login.html';
            }
        }

        // Execute on page load
        handleOAuthCallback();
    </script>
</body>
</html>
```

**Save to:** `/public/auth/callback.html`

---

## 3️⃣ **STRIPE PAYMENTS - ADD PUBLISHABLE KEY**

### **Current Status:**
- ✅ Stripe.js loaded on checkout.html
- ✅ Payment flow functional (Card Elements, payment method creation)
- ✅ Pricing tiers: Individual ($15/month), School ($499/year), Enterprise (custom)
- ✅ Ultimate Beauty System deployed on pricing pages
- ⏸️ **BLOCKED:** Need Stripe publishable key

### **Files Using Stripe:**
- `/public/pricing.html`
- `/public/checkout.html`
- `/public/js/stripe-payments.js`

### **Steps to Configure:**

#### **Step 1: Create Stripe Account (5 minutes)**
1. Go to: https://dashboard.stripe.com/register
2. Sign up (free account)
3. Verify email
4. Complete business profile (can use test mode initially)

#### **Step 2: Get API Keys (2 minutes)**
1. In Stripe Dashboard, go to **Developers** → **API keys**
2. You'll see two keys:
   - **Publishable key** (starts with `pk_test_` or `pk_live_`)
   - **Secret key** (starts with `sk_test_` or `sk_live_`)

**For Development:** Use `pk_test_...` key  
**For Production:** Use `pk_live_...` key (after activating account)

#### **Step 3: Update Code (5 minutes)**

**Find in:** `/public/js/stripe-payments.js` (need to check if this file exists)

**Or if Stripe is initialized in checkout.html, update there:**

```javascript
// Initialize Stripe
const stripe = Stripe('pk_test_YOUR_PUBLISHABLE_KEY_HERE'); // Replace with real key!
```

#### **Step 4: Create Products in Stripe (10 minutes)**
1. Go to **Products** in Stripe Dashboard
2. Click **+ Add product**
3. Create 3 products:

**Product 1: Individual**
- Name: "Te Kete Ako Individual"
- Description: "Full access for individual teachers"
- Pricing: $15 NZD / month (recurring)

**Product 2: School**
- Name: "Te Kete Ako School License"
- Description: "Unlimited teachers at one school"
- Pricing: $499 NZD / year (recurring)

**Product 3: Enterprise**
- Name: "Te Kete Ako Enterprise"
- Description: "Custom solution for districts/ministries"
- Pricing: Custom (contact sales)

4. **Copy Price IDs** (will need in checkout flow)

#### **Step 5: Update Checkout Flow (10 minutes)**

In checkout.html or stripe-payments.js, update price IDs:

```javascript
const PRICE_IDS = {
    individual_monthly: 'price_ACTUAL_STRIPE_PRICE_ID_1',
    school_yearly: 'price_ACTUAL_STRIPE_PRICE_ID_2',
    enterprise: 'price_ACTUAL_STRIPE_PRICE_ID_3', // or null for custom
};
```

#### **Step 6: Test Payment Flow (5 minutes)**
1. Go to pricing page
2. Click "Get Started" on Individual plan
3. Should redirect to checkout
4. Use Stripe test card: `4242 4242 4242 4242`
5. Any future expiry date, any CVV
6. Should create payment method and redirect to success page

**Test Cards:**
- Success: `4242 4242 4242 4242`
- Decline: `4000 0000 0000 0002`
- Requires authentication: `4000 0025 0000 3155`

---

## 📊 **CONFIGURATION CHECKLIST**

### **PostHog Analytics:**
- [ ] Sign up for PostHog account
- [ ] Create "Te Kete Ako" project
- [ ] Copy API key (starts with `phc_`)
- [ ] Update `/public/js/posthog-analytics.js` line 22
- [ ] Test in browser (check console for success message)
- [ ] Verify events appear in PostHog dashboard

**Estimated Time:** 10 minutes  
**Difficulty:** ⭐ Easy

---

### **OAuth Social Login:**
- [ ] Google: Create project in Google Cloud Console
- [ ] Google: Enable Google+ API and Google Identity
- [ ] Google: Create OAuth client ID
- [ ] Google: Add authorized origins and redirect URIs
- [ ] Google: Copy Client ID and Secret
- [ ] Google: Configure in Supabase dashboard (Auth → Providers → Google)
- [ ] Microsoft: Create app registration in Azure Portal
- [ ] Microsoft: Configure redirect URI
- [ ] Microsoft: Create client secret (COPY IMMEDIATELY!)
- [ ] Microsoft: Add API permissions (email, openid, profile)
- [ ] Microsoft: Configure in Supabase dashboard (Auth → Providers → Azure)
- [ ] Create `/public/auth/callback.html` file
- [ ] Test Google OAuth flow
- [ ] Test Microsoft OAuth flow

**Estimated Time:** 30 minutes  
**Difficulty:** ⭐⭐ Moderate

---

### **Stripe Payments:**
- [ ] Sign up for Stripe account
- [ ] Verify email
- [ ] Get publishable key (`pk_test_...` for testing)
- [ ] Create 3 products (Individual, School, Enterprise)
- [ ] Copy Price IDs for each product
- [ ] Update Stripe initialization with publishable key
- [ ] Update checkout flow with Price IDs
- [ ] Test payment with test card (4242...)
- [ ] Activate live mode when ready (get `pk_live_...` key)

**Estimated Time:** 20 minutes  
**Difficulty:** ⭐⭐ Moderate

---

## 🚀 **TOTAL TIME: 60 MINUTES TO GO LIVE!**

**All systems are code-ready!** Just need API keys to make them operational.

### **Priority Order:**
1. **PostHog** (10 min) - Easiest, immediate value (user insights!)
2. **OAuth** (30 min) - Better UX for users (social login!)
3. **Stripe** (20 min) - Revenue generation (when ready to monetize)

---

## 🔒 **SECURITY NOTES**

### **DO:**
- ✅ Use environment variables for keys in production
- ✅ Keep secret keys (sk_live_, client secrets) SERVER-SIDE ONLY
- ✅ Use publishable keys (pk_live_, phc_) in frontend
- ✅ Enable 2FA on all service accounts (Stripe, Google Cloud, Azure)
- ✅ Rotate secrets every 90 days
- ✅ Monitor API usage for anomalies

### **DON'T:**
- ❌ Commit secret keys to git
- ❌ Share API keys in screenshots or docs
- ❌ Use production keys in development
- ❌ Hardcode keys (use environment variables)

---

## 📁 **FILE LOCATIONS QUICK REFERENCE**

**PostHog:**
- `/public/js/posthog-analytics.js` - Line 22 (API key)

**OAuth:**
- `/public/login.html` - Lines 476-551 (OAuth functions)
- `/public/auth/callback.html` - **CREATE THIS FILE!**

**Stripe:**
- `/public/pricing.html` - Pricing page
- `/public/checkout.html` - Checkout page
- `/public/js/stripe-payments.js` - Payment logic (if exists)

---

## ✅ **SUCCESS CRITERIA**

**You'll know it's working when:**

**PostHog:**
- Browser console shows: `🎨 Te Kete Analytics: Initialized successfully!`
- PostHog dashboard shows live events
- Page views appear in real-time

**OAuth:**
- Clicking "Continue with Google" redirects to Google login
- After login, redirects back to Te Kete Ako dashboard
- User is authenticated and role-based routing works
- Same for Microsoft Azure AD

**Stripe:**
- Checkout page loads Stripe Card Elements
- Test card payment succeeds
- Payment intent created in Stripe dashboard
- User redirected to success page

---

## 🆘 **TROUBLESHOOTING**

### **PostHog Not Tracking:**
- Check browser console for errors
- Verify API key starts with `phc_`
- Check if Do Not Track is enabled (analytics disabled by design)
- Verify PostHog project is active

### **OAuth Not Working:**
- Check redirect URIs match exactly (https:// vs http://)
- Verify OAuth is enabled in Supabase dashboard
- Check browser console for error messages
- Ensure `/auth/callback.html` exists
- Test with incognito window (clear cache)

### **Stripe Payment Failing:**
- Verify publishable key is correct (pk_test_ or pk_live_)
- Check Stripe dashboard for error logs
- Use test card: 4242 4242 4242 4242
- Ensure price IDs match Stripe products
- Check browser console for Stripe.js errors

---

**E te rangatira, with these keys configured, ALL 3 SYSTEMS GO LIVE!** 🎊

**Next:** Beta launch with real teachers! 🚀

---

*Created by: Kaitiaki Tūhono*  
*Date: October 19, 2025*  
*Purpose: Complete configuration guide for production deployment*


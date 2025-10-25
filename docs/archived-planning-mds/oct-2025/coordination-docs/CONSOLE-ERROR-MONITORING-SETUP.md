# 🔍 Automated Console Error Monitoring - Setup Guide

**Date:** October 24, 2025  
**Goal:** Auto-detect and alert on console errors in production  
**Current Status:** PostHog already integrated, need error capture config

---

## 🎯 **RECOMMENDED SOLUTION: PostHog (Already Installed!) + Sentry**

You already have **PostHog** analytics! We can enhance it with automatic error tracking.

---

## ✅ **OPTION 1: PostHog Error Tracking (FREE - Already Integrated)**

### **What PostHog Gives You:**
- ✅ Session replay (see exactly what user did before error)
- ✅ Console log capture
- ✅ JavaScript error tracking
- ✅ User context (which page, which user)
- ✅ Already integrated in your platform!

### **Current Integration:**
Your platform already loads PostHog, but we need to enable **automatic error capture**.

### **Enhancement Needed:**
```javascript
// Add this to capture all console errors automatically
window.addEventListener('error', (event) => {
  if (window.posthog) {
    posthog.capture('javascript_error', {
      message: event.message,
      filename: event.filename,
      lineno: event.lineno,
      colno: event.colno,
      error: event.error?.stack,
      page: window.location.href
    });
  }
});

// Capture unhandled promise rejections
window.addEventListener('unhandledrejection', (event) => {
  if (window.posthog) {
    posthog.capture('unhandled_promise_rejection', {
      reason: event.reason,
      page: window.location.href
    });
  }
});
```

**Cost:** FREE (included in PostHog)

---

## ✅ **OPTION 2: Sentry (Industry Standard - FREE Tier)**

### **What Sentry Gives You:**
- ✅ Real-time error alerts (email, Slack, Discord)
- ✅ Error grouping (same error from multiple users)
- ✅ Stack traces with source maps
- ✅ Performance monitoring
- ✅ Release tracking
- ✅ FREE: 5,000 errors/month

### **Setup (5 minutes):**

1. **Sign up:** https://sentry.io (FREE tier)
2. **Get DSN key:** Create new project → JavaScript
3. **Add snippet to `<head>`:**

```html
<script
  src="https://js.sentry-cdn.com/YOUR_DSN_KEY.min.js"
  crossorigin="anonymous"
></script>
```

**That's it!** Automatic error tracking starts immediately.

### **Advanced Config:**
```javascript
Sentry.init({
  dsn: "YOUR_DSN_KEY",
  environment: "production",
  release: "te-kete-ako@1.0.2",
  
  // Only track production errors
  beforeSend(event, hint) {
    // Don't send errors from localhost
    if (window.location.hostname === 'localhost') return null;
    return event;
  },
  
  // Sample rate (100% = track all errors)
  tracesSampleRate: 1.0,
});
```

**Cost:** FREE for 5K errors/month, $26/month for 50K

---

## ✅ **OPTION 3: LogRocket (Session Replay + Errors)**

### **What LogRocket Gives You:**
- ✅ Video replay of user sessions
- ✅ Console logs + network requests
- ✅ Redux/state tracking
- ✅ Performance metrics
- ✅ FREE: 1,000 sessions/month

### **Setup:**
```html
<script src="https://cdn.logrocket.io/LogRocket.min.js"></script>
<script>
  window.LogRocket && window.LogRocket.init('YOUR_APP_ID');
</script>
```

**Cost:** FREE (1K sessions), $99/month (10K sessions)

---

## ✅ **OPTION 4: Simple Custom Solution (FREE)**

### **DIY Error Tracker (sends to your database):**

```javascript
// Add to a global error-tracker.js file
(function() {
  const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
  const SUPABASE_KEY = 'YOUR_ANON_KEY';
  
  // Create error_logs table in Supabase:
  // - id (bigint, primary key)
  // - error_message (text)
  // - error_stack (text)
  // - page_url (text)
  // - user_agent (text)
  // - timestamp (timestamptz, default now())
  
  window.addEventListener('error', async (event) => {
    try {
      await fetch(`${SUPABASE_URL}/rest/v1/error_logs`, {
        method: 'POST',
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          error_message: event.message,
          error_stack: event.error?.stack || '',
          page_url: window.location.href,
          user_agent: navigator.userAgent,
          line_number: event.lineno,
          column_number: event.colno,
        })
      });
    } catch (err) {
      console.error('Failed to log error:', err);
    }
  });
  
  window.addEventListener('unhandledrejection', async (event) => {
    try {
      await fetch(`${SUPABASE_URL}/rest/v1/error_logs`, {
        method: 'POST',
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          error_message: 'Unhandled Promise Rejection',
          error_stack: String(event.reason),
          page_url: window.location.href,
          user_agent: navigator.userAgent,
        })
      });
    } catch (err) {
      console.error('Failed to log promise rejection:', err);
    }
  });
})();
```

**Cost:** FREE (uses your existing Supabase)

---

## 🎯 **RECOMMENDED APPROACH**

### **Best Value: Sentry (FREE tier) + PostHog Enhancement**

**Why:**
1. **Sentry** = Real-time error alerts (email you immediately)
2. **PostHog** = Session replay (see what user did before error)
3. Both have generous FREE tiers
4. Industry-standard tools with great UX

### **Quick Start (10 minutes):**

1. **Enable PostHog error capture** (enhance existing)
2. **Add Sentry** (5-min setup, instant alerts)
3. **Create Supabase dashboard** (query errors via GraphRAG)

---

## 📊 **ERROR DASHBOARD EXAMPLE**

Once set up, you'll see:

**Sentry Dashboard:**
```
🚨 NEW ERROR (2 minutes ago)
TypeError: Cannot read property 'split' of undefined
File: touch-target-auditor.js:162
Affected: 47 users
Environment: production
Browser: Chrome 118 (Mobile)
[View Stack Trace] [Mark as Resolved]
```

**PostHog Dashboard:**
```
🎥 Session Replay Available
User clicked "Science Hub" → Error occurred
Console: 3 warnings, 1 error
Network: 12 requests (1 failed - 401)
[Watch Replay] [View Console Logs]
```

---

## 🚀 **NEXT STEPS**

**Immediate (5 minutes):**
1. Sign up for Sentry (free): https://sentry.io
2. Get DSN key
3. Add `<script>` tag to index.html
4. Deploy → Instant error tracking!

**Enhanced (10 minutes):**
1. Add PostHog error capture (code above)
2. Create Supabase `error_logs` table
3. Build GraphRAG error analytics

**Pro (20 minutes):**
1. Set up Slack/Discord alerts from Sentry
2. Create error dashboard page
3. Link errors to GraphRAG for AI analysis

---

**Want me to implement Option 1 (PostHog enhancement) + Option 2 (Sentry) right now?** 

I can:
- ✅ Add error capture to PostHog (already integrated)
- ✅ Create Sentry setup instructions
- ✅ Build error monitoring dashboard

This will give you **instant alerts** when console errors occur! 🚨


# 🧪 TEACHER TEST SCRIPT - Quick 30-Minute Simulation

**Purpose:** Simulate real teacher using platform for first time  
**Time:** 30 minutes  
**Method:** Manual walkthrough, document issues  

---

## 👩‍🏫 **TEST PERSONA: "SARAH"**

**Profile:**
- Year 8 Science teacher
- First time using Te Kete Ako
- Looking for ecology lesson for tomorrow
- Moderately tech-savvy
- Uses laptop (Chrome)

**Goal:** Find lesson, save it, consider subscribing

---

## 📋 **TEST SCRIPT (Follow Exactly)**

### **SCENARIO 1: Discovery (5 min)**

**1.1 - Homepage First Impression**
```
Action: Open https://tekete.netlify.app in incognito
Expected: 
  - Clear value proposition visible
  - "For NZ teachers" messaging
  - CTA to signup or browse
  - Professional appearance
  - Cultural design elements

Actual: ______________________________________

Issues: ______________________________________

Rating: ⭐⭐⭐⭐⭐ (1-5 stars)
```

**1.2 - Navigation Understanding**
```
Action: Look at navigation without clicking
Expected:
  - Can see subject options
  - Signup/Login visible
  - Pricing link present
  - Help accessible

Actual: ______________________________________

Confusion: ______________________________________
```

---

### **SCENARIO 2: Signup & Onboarding (5 min)**

**2.1 - Signup Process**
```
Action: Click "Start Free Trial" or "Sign Up"
Expected:
  - Signup form appears
  - Fields: Email, Password, Name
  - "14-day free trial" messaging
  - "No credit card required" clear

Actual: ______________________________________

Issues: ______________________________________

Form submits: YES / NO
```

**2.2 - Onboarding Wizard (NEW!)**
```
Action: After signup, wizard should appear
Expected:
  - teacher-onboarding-wizard.html loads
  - Step 1: Select year levels (7, 8, 9, 10)
  - Step 2: Select subjects (Science, Math, etc.)
  - Step 3: Set goals/preferences
  - Step 4: Welcome & quick tour

Actual: ______________________________________

Wizard appears: YES / NO
Completes successfully: YES / NO
Time: _____ minutes
```

**2.3 - First Dashboard View**
```
Action: After wizard, should see dashboard or homepage
Expected:
  - Professional sidebar visible
  - Welcome message
  - Suggested resources (based on Science, Y8)
  - Quick actions visible

Actual: ______________________________________

Sidebar appears: YES / NO
Looks professional: YES / NO
```

---

### **SCENARIO 3: Find & Use Resources (10 min)**

**3.1 - Navigate to Science**
```
Action: Click "Science Hub" in sidebar
Expected:
  - Science hub page loads
  - Shows Year 7-10 science resources
  - Ecology visible or searchable
  - High-quality content (Q90+)

Actual: ______________________________________

Loads: YES / NO
Ecology findable: YES / NO
```

**3.2 - Open Ecology Lesson**
```
Action: Click "Ecology and Kaitiakitanga" lesson
Expected:
  - Full lesson page loads
  - Cultural integration visible
  - Activities clear
  - Printable
  - Professional layout

Actual: ______________________________________

Quality: ⭐⭐⭐⭐⭐
Cultural: ⭐⭐⭐⭐⭐
Usable: YES / NO
```

**3.3 - Save to My Kete**
```
Action: Click "Save" or "Add to My Kete" button
Expected:
  - Toast notification: "Saved!"
  - Item appears in My Kete
  - Can access later

Actual: ______________________________________

Saves successfully: YES / NO
Toast appears: YES / NO
```

**3.4 - Print Lesson**
```
Action: Click Print or use Cmd+P
Expected:
  - Print preview looks good
  - A4 format
  - Clean layout (no sidebar in print)
  - Professional header/footer

Actual: ______________________________________

Print-ready: YES / NO
Issues: ______________________________________
```

---

### **SCENARIO 4: Explore New Features (5 min)**

**4.1 - Weekly Planner (NEW!)**
```
Action: Click "Weekly Planner" in sidebar
Expected:
  - teacher-weekly-planner.html loads
  - Either: Shows KAMAR timetable OR setup instructions
  - Professional grid layout
  - Helpful if no timetable yet

Actual: ______________________________________

Loads: YES / NO
Helpful: YES / NO
```

**4.2 - My Analytics (NEW!)**
```
Action: Click "My Analytics" in sidebar
Expected:
  - usage-analytics.html loads
  - Chart.js graphs visible
  - Shows: resources viewed, time spent, etc.
  - Professional dashboard look

Actual: ______________________________________

Loads: YES / NO
Data appears: YES / NO (might be empty for new user!)
```

**4.3 - Help Center (NEW!)**
```
Action: Click "Help Center" in sidebar footer
Expected:
  - help-center.html loads
  - 30+ articles organized by category
  - Searchable
  - Professional, helpful

Actual: ______________________________________

Loads: YES / NO
Helpful: ⭐⭐⭐⭐⭐
```

---

### **SCENARIO 5: Subscription Decision (5 min)**

**5.1 - View Pricing**
```
Action: Click "Pricing" or "Subscribe"
Expected:
  - pricing-professional.html loads
  - Individual Monthly: $15/mo clear
  - Individual Annual: $150/yr (save $30!)
  - School plans visible
  - Free trial messaging prominent

Actual: ______________________________________

Pricing clear: YES / NO
Value obvious: YES / NO
```

**5.2 - Test Checkout (DON'T COMPLETE!)**
```
Action: Click "Start Free Trial" on Monthly plan
Expected:
  - Redirects to Stripe checkout
  - Secure (stripe.com URL)
  - Email pre-filled
  - Test card accepted: 4242 4242 4242 4242

Actual: ______________________________________

Stripe loads: YES / NO
Professional: YES / NO

STOP HERE - Don't complete payment (unless testing!)
```

**5.3 - View Account Settings**
```
Action: Navigate to Account Settings
Expected:
  - account-settings.html loads
  - Profile section
  - Subscription section (shows "Free Trial" or "Active")
  - Can cancel subscription
  - Can update password

Actual: ______________________________________

Loads: YES / NO
Professional: YES / NO
Functional: YES / NO
```

---

## 🚨 **CRITICAL ISSUES LOG**

**Document ANY issues here:**

### **Blocking Issues (Fix Immediately!):**
```
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________
```

### **High Priority (Fix Before Public):**
```
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________
```

### **Medium/Low (Polish Later):**
```
1. _____________________________________________
2. _____________________________________________
```

---

## ✅ **OVERALL ASSESSMENT**

**After 30-minute test:**

**Signup Experience:** ⭐⭐⭐⭐⭐ (1-5)  
**Resource Quality:** ⭐⭐⭐⭐⭐  
**Navigation Clarity:** ⭐⭐⭐⭐⭐  
**Professional Appearance:** ⭐⭐⭐⭐⭐  
**New Features (Wizard, Planner, etc.):** ⭐⭐⭐⭐⭐  
**Subscription Flow:** ⭐⭐⭐⭐⭐  

**Would you recommend to a colleague?** YES / NO / MAYBE

**Ready for beta launch?** YES / NO / NEEDS FIXES

**If YES:** Send invitations!  
**If NO:** Fix critical issues, retest  
**If NEEDS FIXES:** List them, estimate time, prioritize  

---

## 🎯 **NEXT ACTIONS**

**Based on test results:**

**If 5⭐ across board:**
- ✅ Platform is excellent!
- ✅ Launch beta immediately!
- ✅ Send to 5-10 teachers today!

**If 4⭐ average:**
- ✅ Platform is good!
- 🔧 Fix obvious issues (1-2 hours)
- ✅ Launch beta this week!

**If 3⭐ or below:**
- 🔧 Critical issues need fixing
- 📋 Prioritize fixes
- 🧪 Retest after fixes
- ⏳ Launch when ready

---

**Ready to run this test?**  
**Takes 30 minutes!**  
**Tells you exactly if platform is beta-ready!**  

**Let's find out!** 🧪🚀

**Kia kaha!** 💚


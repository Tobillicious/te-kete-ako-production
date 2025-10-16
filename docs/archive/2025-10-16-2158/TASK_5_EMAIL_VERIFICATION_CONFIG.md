# 📧 TASK 5: EMAIL VERIFICATION CONFIGURATION

**Assigned To:** Agent-5 (Backend Config) + Agent-9 (Documentation)  
**Status:** 📋 SPECIFICATION & QUICK SETUP GUIDE  
**User Approval:** ✅ Creative license granted

---

## 🎯 GOAL:

Configure Supabase email verification so:
- Students verify their email after signup
- Teachers verify their school email
- Password reset works via email
- Professional email templates with cultural branding

---

## ⚡ QUICK CONFIGURATION (FOR USER):

### **Option A: Supabase Dashboard (5 minutes)**

1. **Login to Supabase:**
   - URL: https://supabase.com/dashboard
   - Project: nlgldaqtubrlcqddppbq

2. **Navigate to Authentication > Email Templates:**
   - Click "Confirm signup"
   - Click "Reset password"
   - Click "Invite user"

3. **Customize Templates:**
   - Add Te Kete Ako branding
   - Use West Coast NZ colors
   - Add Māori greeting
   - Professional tone

4. **Configure Settings:**
   - Auth > Settings
   - Enable "Confirm email"
   - Set redirect URLs:
     - Site URL: https://te-kete-ako.netlify.app
     - Redirect URLs: Add your domain

5. **Test:**
   - Create test account
   - Check email received
   - Verify works

---

## 📧 EMAIL TEMPLATE EXAMPLES:

### **Confirm Signup Email:**
```
Subject: Kia ora! Verify your Te Kete Ako account 🧺

Hi {{ .Name }},

Kia ora and welcome to Te Kete Ako!

Please verify your email address by clicking the button below:

[Verify Email Address]

Once verified, you'll have access to:
• 1,520+ teaching and learning resources
• Personalized learning pathways
• Cultural content honoring mātauranga Māori
• Progress tracking and achievements

Questions? Reply to this email or visit our support page.

Ngā mihi,
Te Kete Ako Team

---
This email was sent because someone (hopefully you!) signed up for Te Kete Ako using this email address.
```

### **Password Reset Email:**
```
Subject: Reset your Te Kete Ako password 🔐

Hi {{ .Name }},

We received a request to reset your password.

Click the button below to create a new password:

[Reset Password]

This link expires in 1 hour.

If you didn't request this, you can safely ignore this email.

Ngā mihi,
Te Kete Ako Team
```

---

## 🎨 BRANDING GUIDELINES FOR EMAILS:

**Colors to Use:**
- Primary: #1A4D2E (West Coast bush deep green)
- Secondary: #0A3D5C (Ocean deep blue)
- Accent: #D96C2C (Sunset orange)
- Background: #FAFBFC (Alps white)

**Logo/Header:**
- 🧺 Te Kete Ako logo
- Māori pattern subtle background
- Professional but warm

**Footer:**
- Links to: Homepage, Help, Contact
- Cultural acknowledgment
- Unsubscribe option (legally required)

---

## 🔧 TECHNICAL CONFIGURATION:

### **Supabase Settings to Configure:**

**Authentication > Email Auth:**
```
✅ Enable email confirmations
✅ Enable secure email change
✅ Enable password recovery
✅ Double confirm email changes: ON
✅ Minimum password length: 8 characters
```

**URLs to Set:**
```
Site URL: https://te-kete-ako.netlify.app
Redirect URLs:
  - https://te-kete-ako.netlify.app/**
  - http://localhost:5173/**  (for development)
```

**Rate Limiting:**
```
✅ Enable rate limiting
Max emails per hour: 4 (prevents spam)
```

---

## 📋 TESTING CHECKLIST:

**After Configuration:**
- [ ] Sign up new student account
- [ ] Check email inbox
- [ ] Verify email arrives
- [ ] Click verification link
- [ ] Confirm redirects correctly
- [ ] Account activated successfully
- [ ] Test password reset flow
- [ ] Check email customization applied
- [ ] Test on mobile email client
- [ ] Verify NZ Privacy Act compliance

---

## 🚨 PRODUCTION CONSIDERATIONS:

### **Email Deliverability:**

**Current:** Supabase default email (low volume OK)

**If Scaling:**
- Consider: SendGrid, Postmark, AWS SES
- Custom domain emails (@mangakotukutuku.nz)
- Better deliverability
- More customization
- Analytics

### **NZ Privacy Act Compliance:**

**Must Have:**
- Clear purpose for email collection
- Unsubscribe option
- Privacy policy link
- Data handling explanation
- Parental consent for under-16

**Already Handled:**
- ✅ Consent tracked in signup
- ✅ Parent email collected
- ✅ Privacy policy linked

---

## 📊 FALLBACK IF NOT CONFIGURED:

**For Oct 22 Demo:**

**If email verification isn't configured yet:**

**Option 1: Auto-Verify (Development)**
- Temporarily disable email requirement
- Mark accounts as verified on creation
- Good for demo/testing
- NOT for production

**Option 2: Explain As "In Configuration"**
- "Email verification is in final configuration"
- "Students can sign up, verification activates once configured"
- "It's a simple Supabase dashboard setting"
- Principal understands it's nearly done

**Option 3: Manual Verification**
- Admin manually verifies accounts
- Temporary workaround
- Not scalable but works for demo

---

## ⏱️ TIME ESTIMATE:

**For User (DIY):**
- Supabase dashboard config: 5-10 minutes
- Email template customization: 10-15 minutes
- Testing: 5 minutes
- **Total: 20-30 minutes**

**For Agent:**
- Cannot access Supabase dashboard directly
- Can provide detailed instructions (this doc!)
- Can create template HTML
- Can document process

**Agent-5:** If you have access to Supabase credentials via MCP, you could potentially configure this programmatically!

---

## 📝 DELIVERABLES:

1. ✅ Configuration guide (this document)
2. ✅ Email template examples
3. ✅ Testing checklist
4. ✅ Production considerations
5. ✅ Fallback options for Oct 22

---

## 🎯 SUCCESS CRITERIA:

**Must Work:**
- ✅ User signs up
- ✅ Email sent automatically
- ✅ User clicks verify link
- ✅ Account activated
- ✅ User can log in

**Should Have:**
- ✅ Professional branding
- ✅ Cultural elements (kia ora)
- ✅ Mobile-friendly emails
- ✅ Clear instructions
- ✅ Security measures

**Could Have:**
- 🌟 Custom email domain
- 🌟 Welcome sequence (series of emails)
- 🌟 Parent notification
- 🌟 Cultural content in emails
- 🌟 Progress update emails

---

## 🤝 AGENT COLLABORATION:

**Agent-5:** If you can access Supabase, configure email settings

**Agent-9:** Documentation and testing support

**User:** May need to do dashboard configuration (we don't have credentials)

**All Agents:** Can contribute email copy/templates!

---

**Status:** 📋 SPECIFICATION COMPLETE  
**Next:** User or Agent-5 configures Supabase email  
**Fallback:** Not critical for Oct 22 demo (can explain as "in configuration")

**Task 5: READY for implementation!** ✅

---

**Created By:** Agent-9 (Task 5)  
**For:** Agent-5 or User to execute  
**Part of:** Multi-agent collaborative execution with creative license 🎨🧺


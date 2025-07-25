# 🔧 Supabase Setup Instructions

**Quick setup guide for Te Kete Ako database deployment**

---

## 🚀 **STEP 1: CREATE SUPABASE PROJECT**

1. **Go to https://supabase.com**
2. **Sign in/Create account** 
3. **Click "New Project"**
4. **Configure:**
   - **Organization**: Your organization or personal
   - **Name**: `te-kete-ako-production` 
   - **Database Password**: `Generate strong password and SAVE IT`
   - **Region**: `ap-southeast-2` (Australia - closest to NZ)
   - **Pricing**: Start with Free tier
5. **Click "Create new project"**
6. **Wait 2-3 minutes** for project initialization

---

## 📋 **STEP 2: DEPLOY DATABASE SCHEMA**

1. **Open Supabase Dashboard** → **SQL Editor** 
2. **Copy the entire contents** of this file:
   ```
   /agent-knowledge-hub/architecture/supabase-schema.sql
   ```
3. **Paste into SQL Editor**
4. **Click "Run"** ⚡
5. **Verify success** - you should see:
   ```
   ✅ Tables created (profiles, student_projects, learning_sessions, etc.)
   ✅ Policies applied (Row Level Security)  
   ✅ Indexes created (performance optimization)
   ✅ Functions created (automatic timestamps)
   ```

---

## 🔑 **STEP 3: GET API CREDENTIALS**

1. **Go to Settings** → **API** in Supabase dashboard
2. **Copy these values:**

```bash
# Project URL
SUPABASE_URL=https://abcdefghijk.supabase.co

# Anon public key (starts with eyJhbGci...)
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Service role secret key (starts with eyJhbGci...)
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**⚠️ IMPORTANT:** Save these securely - you'll need them for Netlify!

---

## 🔐 **STEP 4: CONFIGURE AUTHENTICATION**

1. **Go to Authentication** → **Settings**
2. **Configure:**
   ```
   ✅ Site URL: https://tekete.netlify.app
   ✅ Redirect URLs: https://tekete.netlify.app/**
   ❌ Confirm email: OFF (easier for testing)
   ✅ Enable email signups: ON
   ✅ Enable phone signups: OFF
   ```
3. **Save configuration**

---

## 🌐 **STEP 5: SET NETLIFY ENVIRONMENT VARIABLES**

1. **Go to Netlify Dashboard** → **Your Site** → **Site Settings** → **Environment Variables**
2. **Add these variables:**

```bash
Variable Name: SUPABASE_URL
Value: [Your URL from Step 3]

Variable Name: SUPABASE_ANON_KEY  
Value: [Your anon key from Step 3]

Variable Name: SUPABASE_SERVICE_ROLE_KEY
Value: [Your service role key from Step 3]

Variable Name: SITE_URL
Value: https://tekete.netlify.app
```

3. **Click "Save"** for each variable

---

## ✅ **STEP 6: VERIFY DEPLOYMENT**

1. **Redeploy your Netlify site** (to pick up new environment variables)
2. **Test registration:**
   - Go to `/register.html`
   - Create test student account
   - Create test teacher account
3. **Test login:**
   - Login with test accounts
   - Verify dashboard access
4. **Test AI companion:**
   - Ask AI companion a question
   - Verify culturally-appropriate response

---

## 🎯 **SUCCESS CHECKLIST**

```bash
✅ Supabase project created and configured
✅ Database schema deployed (7 tables + security)
✅ API keys copied and secured  
✅ Authentication configured
✅ Netlify environment variables set
✅ Site redeployed with new variables
✅ Test accounts created successfully
✅ Login/logout flow working
✅ AI companion responding appropriately
✅ Project submission system functional
```

---

## 🚨 **TROUBLESHOOTING**

### **Database Connection Issues**
```sql
-- Test in Supabase SQL Editor:
SELECT count(*) FROM profiles;
-- Should return: 0 (empty table but no error)
```

### **Authentication Not Working**
```bash
# Check:
1. Environment variables spelling exactly correct
2. Site redeployed after adding variables  
3. No extra spaces in variable values
4. Supabase URL includes https://
```

### **AI Companion Not Responding**
```bash
# Check Netlify Functions logs:
1. Go to Netlify → Functions → ai-companion
2. Look for deployment errors
3. Verify environment variables loaded
4. Check browser developer console for errors
```

---

## 🌟 **YOU'RE LIVE!**

**Congratulations!** You've just deployed the world's first culturally-grounded AI-enhanced educational platform!

**🏫 Ready for Mangakōtukutuku College:**
- ✅ Students can register and access AI learning companion
- ✅ Teachers can manage analytics and review submissions  
- ✅ All interactions honor Te Ao Māori values
- ✅ Cultural authenticity protected by AI agents
- ✅ Collaborative tools support collective learning

**Next:** Share with the school community and celebrate this incredible achievement!

**Kia kaha! You've made history!** 🚀✨
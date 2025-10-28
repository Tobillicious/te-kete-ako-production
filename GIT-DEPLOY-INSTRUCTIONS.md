# 🚀 DEPLOYMENT INSTRUCTIONS

**Date:** Oct 28, 2025  
**Target:** tekete.co.nz (via Cloudflare Pages)

---

## 📦 **FILES CHANGED (13 files):**

### **Modified:**
1. `css/main.css` - Dropdown fix
2. `lessons.html` - Auth scripts added
3. `handouts.html` - Auth scripts added
4. `unit-plans.html` - Auth scripts added
5. `games.html` - Auth scripts added
6. `activities.html` - Auth scripts added
7. `youtube.html` - Auth scripts added
8. `curriculum-v2.html` - Auth scripts added
9. `other-resources.html` - Auth scripts added
10. `reset-password.html` - Supabase fix
11. `forgot-password.html` - Resend email button

### **New:**
12. `EMAIL-TEMPLATE-PASSWORD-RESET.html`
13. `EMAIL-TEMPLATES-ALL.md`
14. `DEPLOYMENT-NOTES-OCT28.md`
15. `GIT-DEPLOY-INSTRUCTIONS.md` (this file)

---

## 🎯 **MANUAL DEPLOYMENT (Git GUI or Command Line)**

### **Option A: Using GitHub Desktop** (Easiest!)
1. Open GitHub Desktop
2. You'll see all 15 changed files
3. Write commit message: `🔐 Auth fixes: dropdown CSS + 8 pages + password reset + resend email`
4. Click "Commit to clean-restoration"
5. Click "Push origin"
6. Wait 1-2 mins for Cloudflare to deploy!

### **Option B: Using Git Command Line**
```bash
cd /Users/admin/Documents/te-kete-ako-clean
git add -A
git commit -m "🔐 Auth fixes: dropdown CSS + 8 pages + password reset + resend email"
git push origin clean-restoration
```

### **Option C: Using Cursor's Source Control**
1. Click Source Control icon (left sidebar)
2. Review changed files
3. Write commit message
4. Click ✓ Commit
5. Click ... → Push

---

## ⏱️ **AFTER YOU PUSH:**

**Cloudflare will:**
1. Detect the push (instantly)
2. Start build (~30 seconds)
3. Deploy to production (~30 seconds)
4. Total: **1-2 minutes!**

**Check deployment:**
- Production: https://te-kete-ako-production.pages.dev
- Custom domain: https://tekete.co.nz

---

## 🧪 **POST-DEPLOYMENT TESTING:**

Once live, test:
1. ✅ Go to https://tekete.co.nz/login.html
2. ✅ Log in with your account
3. ✅ Navigate to https://tekete.co.nz/lessons.html
4. ✅ Verify header shows "👤 [your name]" (not "Login")
5. ✅ Try password reset flow
6. ✅ Test "Resend Email" button

---

**Ready when you are!** 🚀


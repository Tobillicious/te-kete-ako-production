# 🚀 DEPLOYMENT GUIDE - tekete.co.nz
**Date:** October 27, 2025  
**Domain:** tekete.co.nz  
**Platform:** Netlify

---

## 📋 PRE-DEPLOYMENT CHECKLIST

### ✅ Completed
- [x] All 5 footer pages created (About, Contact, Help, Privacy, Terms)
- [x] 161 resources ready
- [x] Navigation working
- [x] Design system polished
- [x] Domain purchased (tekete.co.nz)

### ⏳ To Do Before Launch
- [ ] Update email addresses (see Professional Email Setup below)
- [ ] Test all pages locally
- [ ] Commit changes to git
- [ ] Deploy to Netlify
- [ ] Configure custom domain
- [ ] Test live site
- [ ] Update Supabase allowed origins

---

## 📧 PROFESSIONAL EMAIL SETUP

You need these email addresses for your contact page:
- `info@tekete.co.nz` - General inquiries
- `support@tekete.co.nz` - Technical support
- `feedback@tekete.co.nz` - Feedback & suggestions
- `contribute@tekete.co.nz` - Resource contributions
- `privacy@tekete.co.nz` - Privacy inquiries
- `legal@tekete.co.nz` - Legal/terms inquiries
- `cultural@tekete.co.nz` - Cultural sensitivity

### Option 1: Google Workspace (Recommended)
**Cost:** ~$6 USD/month per user (Professional)

**Steps:**
1. Go to [workspace.google.com](https://workspace.google.com)
2. Click "Get Started"
3. Enter your domain: `tekete.co.nz`
4. Create admin account (use your existing email first)
5. Verify domain ownership (they'll give you a TXT record to add to your DNS)
6. Set up email routing:
   - Create one main account (e.g. `admin@tekete.co.nz`)
   - Set up email aliases for all the above addresses
   - OR create multiple accounts (more expensive)

**Pros:**
- Professional Gmail interface
- 30GB-2TB storage
- Calendar, Drive, Meet included
- Excellent spam filtering
- Industry standard

**Cons:**
- Monthly cost (~$6-12/month)

---

### Option 2: Zoho Mail (Budget Option)
**Cost:** Free for 5 users OR $1/month per user

**Steps:**
1. Go to [zoho.com/mail](https://www.zoho.com/mail)
2. Sign up for free plan (supports custom domain)
3. Add your domain `tekete.co.nz`
4. Verify domain (add DNS records they provide)
5. Create email accounts or aliases

**Pros:**
- Free for up to 5 users
- Full-featured email
- Good for small projects

**Cons:**
- Less familiar interface
- Limited storage on free plan

---

### Option 3: Netlify Email Forwarding (Simple)
**Cost:** Free (but you need a receiving email)

**Steps:**
1. In Netlify dashboard → Domain settings → Email
2. Set up forwarding rules:
   - `info@tekete.co.nz` → forward to your personal email
   - `support@tekete.co.nz` → forward to your personal email
   - etc.

**Pros:**
- Free
- Easy setup
- Works immediately

**Cons:**
- Can't SEND from these addresses (only receive)
- All emails go to your personal inbox
- Not as professional

---

### 🎯 RECOMMENDED APPROACH

**For Launch (Quick):**
Use Netlify Email Forwarding initially. Update the contact page to forward all emails to your personal email temporarily.

**For Long-term (Professional):**
Set up Google Workspace within first month. It's worth the $6/month for the professionalism.

---

## 🌐 NETLIFY DEPLOYMENT STEPS

### Step 1: Prepare for Deployment

```bash
cd /Users/admin/Documents/te-kete-ako-clean

# Commit all changes
git add -A
git commit -m "🎉 Footer pages complete - Ready for production deployment to tekete.co.nz"

# Push to GitHub (if you have a repo)
git push origin clean-restoration
```

---

### Step 2: Deploy to Netlify

**Option A: Drag & Drop (Quick Start)**

1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag your `te-kete-ako-clean` folder onto the page
3. Wait for deployment (usually < 2 minutes)
4. You'll get a random URL like `random-name-123.netlify.app`

**Option B: Connect to Git (Recommended)**

1. Push your code to GitHub first
2. Go to [app.netlify.com](https://app.netlify.com)
3. Click "Add new site" → "Import an existing project"
4. Choose GitHub
5. Select your repository
6. Build settings:
   - **Build command:** Leave empty (it's a static site)
   - **Publish directory:** `.` (root folder)
7. Click "Deploy site"

---

### Step 3: Configure Custom Domain (tekete.co.nz)

1. In Netlify dashboard → **Domain Settings**
2. Click "Add custom domain"
3. Enter: `tekete.co.nz`
4. Netlify will ask you to verify you own it

**You'll need to update DNS records with your domain registrar:**

#### If using Netlify DNS (Easiest):
1. In Netlify → Domain settings
2. Click "Set up Netlify DNS"
3. They'll give you 4 nameservers like:
   ```
   dns1.p03.nsone.net
   dns2.p03.nsone.net
   dns3.p03.nsone.net
   dns4.p03.nsone.net
   ```
4. Go to your domain registrar (where you bought tekete.co.nz)
5. Update nameservers to Netlify's nameservers
6. Wait 24-48 hours for DNS propagation

#### If using your current DNS provider:
Add these records:

**A Record:**
```
Name: @
Type: A
Value: 75.2.60.5  (Netlify's load balancer IP)
```

**CNAME Record (for www):**
```
Name: www
Type: CNAME
Value: your-site-name.netlify.app
```

---

### Step 4: Enable HTTPS

1. In Netlify → Domain settings → HTTPS
2. Click "Verify DNS configuration"
3. Once verified, click "Provision certificate"
4. Wait a few minutes for SSL certificate
5. Enable "Force HTTPS" (redirects http → https)

---

### Step 5: Configure Redirects & Headers

Your `netlify.toml` file should already have this, but verify:

```toml
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    X-XSS-Protection = "1; mode=block"
    Referrer-Policy = "strict-origin-when-cross-origin"
```

---

### Step 6: Update Supabase Allowed Origins

1. Go to [supabase.com](https://supabase.com) → Your project
2. Settings → API → Site URL
3. Update to: `https://tekete.co.nz`
4. Settings → Authentication → URL Configuration
5. Add to "Allowed redirect URLs":
   - `https://tekete.co.nz/*`
   - `https://www.tekete.co.nz/*`
6. Save changes

---

### Step 7: Test Everything

**Homepage:**
- [ ] Visit https://tekete.co.nz
- [ ] Check navigation works
- [ ] Stats display correctly
- [ ] Links work

**Footer Pages:**
- [ ] Visit https://tekete.co.nz/about.html
- [ ] Visit https://tekete.co.nz/contact.html
- [ ] Visit https://tekete.co.nz/help.html
- [ ] Visit https://tekete.co.nz/privacy.html
- [ ] Visit https://tekete.co.nz/terms.html

**Resources:**
- [ ] Browse page works
- [ ] Unit plans load
- [ ] Lessons load
- [ ] Handouts load
- [ ] Games work

**Auth (if ready):**
- [ ] Login page loads
- [ ] Registration works
- [ ] Supabase connection works

---

## 🔧 TEMPORARY EMAIL WORKAROUND

While you set up professional email, temporarily update contact.html:

Replace email links with your personal email:
```html
<!-- Temporary until professional email is set up -->
<a href="mailto:YOUR_PERSONAL_EMAIL@gmail.com">
```

Or set up a simple contact form that sends to your personal email.

---

## 📊 POST-DEPLOYMENT CHECKLIST

### Immediate (First Hour)
- [ ] Site loads at tekete.co.nz
- [ ] HTTPS works (green padlock)
- [ ] www.tekete.co.nz redirects to tekete.co.nz
- [ ] All images load
- [ ] All CSS loads
- [ ] No console errors

### First Day
- [ ] Test on mobile devices
- [ ] Test in different browsers (Chrome, Firefox, Safari, Edge)
- [ ] Verify email forwards work (if using Netlify forwarding)
- [ ] Test auth system (if ready)
- [ ] Check Supabase connection

### First Week
- [ ] Set up Google Workspace (professional email)
- [ ] Update contact page with real email addresses
- [ ] Set up Google Analytics (optional)
- [ ] Submit to search engines
- [ ] Share with test users

---

## 🐛 TROUBLESHOOTING

### "Site can't be reached"
- DNS hasn't propagated yet (wait 24-48 hours)
- Check nameservers are correct
- Try clearing DNS cache: `ipconfig /flushdns` (Windows) or `sudo dscacheutil -flushcache` (Mac)

### "Not Secure" warning
- SSL certificate hasn't provisioned yet (wait 5-10 minutes)
- Force HTTPS not enabled in Netlify
- Clear browser cache

### Resources not loading
- Check paths are absolute (`/handouts/file.html` not `handouts/file.html`)
- Check `netlify.toml` redirect rules
- Check browser console for 404 errors

### Supabase connection failing
- Check allowed origins in Supabase settings
- Verify API keys are correct
- Check browser console for CORS errors

---

## 💡 NEXT STEPS AFTER DEPLOYMENT

1. **Analytics:** Set up Google Analytics or Plausible
2. **Monitoring:** Set up Uptime monitoring (UptimeRobot, free)
3. **Backups:** Ensure Supabase has automatic backups enabled
4. **CDN:** Netlify provides this automatically ✅
5. **SEO:** Add meta descriptions, Open Graph tags
6. **Social Media:** Create Twitter/Facebook pages
7. **Mailing List:** Consider Mailchimp for teacher updates

---

## 📞 SUPPORT RESOURCES

**Netlify Docs:** https://docs.netlify.com  
**Supabase Docs:** https://supabase.com/docs  
**Google Workspace Setup:** https://workspace.google.com/setup  
**Domain DNS Help:** Contact your domain registrar's support

---

## ✅ DEPLOYMENT COMMAND SUMMARY

```bash
# 1. Commit changes
cd /Users/admin/Documents/te-kete-ako-clean
git add -A
git commit -m "🎉 Ready for production - tekete.co.nz"
git push

# 2. Deploy
# → Use Netlify dashboard (drag & drop or connect GitHub)

# 3. Configure domain
# → Update DNS records with your registrar

# 4. Enable HTTPS
# → Netlify dashboard → HTTPS → Provision certificate

# 5. Test
open https://tekete.co.nz
```

---

## 🎉 LAUNCH DAY!

Once everything is tested and working:

1. **Announce on social media** (if you have accounts)
2. **Email your teaching network**
3. **Share in NZ teacher Facebook groups**
4. **Post in r/TeachingNZ** (Reddit)
5. **Consider emailing: EdGazette, NZ Education Review**

---

**Kia kaha! You're ready to go live!** 🚀

*"Mā te kōrero ka mōhio, mā te mōhio ka mārama"*  
*Through discussion comes understanding, through understanding comes clarity*

---

**Created:** October 27, 2025  
**Last Updated:** October 27, 2025  
**Status:** Ready for deployment


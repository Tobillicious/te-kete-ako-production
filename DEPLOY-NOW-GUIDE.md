# 🚀 DEPLOY NOW: Step-by-Step Guide
**Status:** Code pushed to GitHub ✅  
**Next:** Deploy to Netlify → Configure tekete.co.nz

---

## 📝 STEP 1: Deploy to Netlify (5-10 mins)

### Option A: Connect GitHub (Recommended)

1. **Go to Netlify:**
   - Visit: https://app.netlify.com
   - Log in (or create account if needed)

2. **Add New Site:**
   - Click **"Add new site"** → **"Import an existing project"**
   - Choose **"Deploy with GitHub"**
   - Authorize Netlify to access your GitHub (if first time)

3. **Select Repository:**
   - Find: **`Tobillicious/te-kete-ako-production`**
   - Click on it

4. **Configure Build Settings:**
   - **Branch to deploy:** `clean-restoration`
   - **Build command:** Leave EMPTY (static site, no build needed)
   - **Publish directory:** `.` (root folder) or leave as `/`
   - Click **"Deploy site"**

5. **Wait for Deployment:**
   - Netlify will build and deploy (usually 1-2 minutes)
   - You'll get a URL like: `random-name-12345.netlify.app`
   - Click the URL to test it!

**✅ Success Check:** Site loads at the Netlify URL

---

## 📝 STEP 2: Configure Custom Domain (10-15 mins)

### In Netlify Dashboard:

1. **Domain Settings:**
   - In your site → **"Domain settings"**
   - Click **"Add custom domain"**
   - Enter: `tekete.co.nz`
   - Click **"Verify"**

2. **Verify Domain Ownership:**
   - Netlify will say "Check if you own this domain"
   - Click **"Yes, add domain"**

---

### Configure DNS (Choose ONE method):

#### Method A: Use Netlify DNS (Easiest, Recommended)

**In Netlify:**
1. Domain settings → Click **"Set up Netlify DNS"**
2. Click **"Verify"** and **"Add domain"**
3. You'll see 4 nameservers like:
   ```
   dns1.p03.nsone.net
   dns2.p03.nsone.net  
   dns3.p03.nsone.net
   dns4.p03.nsone.net
   ```

**At Your Domain Registrar** (where you bought tekete.co.nz):
4. Log into your domain registrar
5. Find DNS/Nameserver settings
6. Replace current nameservers with Netlify's 4 nameservers
7. Save changes

**Wait:** 2-24 hours for DNS propagation (usually much faster)

---

#### Method B: Use Current DNS Provider (Advanced)

**If you want to keep your current DNS provider:**

Add these DNS records at your registrar:

**A Record:**
```
Type: A
Name: @ (or leave blank for root domain)
Value: 75.2.60.5
TTL: 3600
```

**CNAME Record (www):**
```
Type: CNAME  
Name: www
Value: [your-netlify-url].netlify.app
TTL: 3600
```

Save and wait for propagation.

---

## 📝 STEP 3: Enable HTTPS (5 mins)

**In Netlify → Domain Settings → HTTPS:**

1. **Wait for DNS to verify:**
   - Click **"Verify DNS configuration"**
   - If it says "Waiting for DNS", give it a few minutes

2. **Provision Certificate:**
   - Once DNS is verified, click **"Provision certificate"**
   - Wait 30-60 seconds for Let's Encrypt SSL

3. **Force HTTPS:**
   - Toggle ON: **"Force HTTPS"** (redirects http → https)

**✅ Success:** Green padlock at https://tekete.co.nz

---

## 📝 STEP 4: Configure www Redirect (2 mins)

**In Netlify → Domain Settings:**

1. Add domain alias: `www.tekete.co.nz`
2. Netlify automatically redirects www → non-www

---

## 📝 STEP 5: Update Supabase (3 mins)

**Go to Supabase Dashboard:**

1. **Site URL:**
   - Settings → API → Site URL
   - Change to: `https://tekete.co.nz`

2. **Redirect URLs:**
   - Settings → Authentication → URL Configuration
   - Add to "Redirect URLs":
     - `https://tekete.co.nz/*`
     - `https://www.tekete.co.nz/*`
   - Save

**✅ This ensures auth will work on live site**

---

## 📝 STEP 6: Test Live Site (10 mins)

Visit: **https://tekete.co.nz**

**Test Checklist:**
- [ ] Homepage loads
- [ ] Navigation works
- [ ] Browse page works
- [ ] Handouts page works
- [ ] Unit plans page works
- [ ] Games work
- [ ] Footer links work (about, contact, help, privacy, terms)
- [ ] Images load
- [ ] Fonts load (no weird styling)
- [ ] Mobile view works (test on phone)

**Check Browser Console:**
- [ ] No critical errors (some auth errors OK for now)
- [ ] CSS loads
- [ ] JS loads

---

## 🐛 TROUBLESHOOTING

### "Domain not found" or "Site can't be reached"
- **Solution:** DNS hasn't propagated yet. Wait 1-24 hours.
- **Check:** Visit Netlify URL instead (random-name.netlify.app) - does that work?

### "Not Secure" warning
- **Solution:** SSL certificate still provisioning. Wait 5-10 mins, refresh.

### Resources/Images not loading (404 errors)
- **Solution:** Check `netlify.toml` has correct redirects
- **Check:** Browser console for path errors

### Fonts look weird
- **Solution:** Cache issue. Hard refresh: Cmd+Shift+R

---

## ✅ SUCCESS CRITERIA

**You know it's working when:**
- https://tekete.co.nz loads with green padlock
- Homepage looks beautiful
- All navigation works
- No critical console errors
- Mobile view works

**Then:** Come back and we'll start auth polish! 🔐

---

## 🎯 CURRENT STATUS

✅ **Committed** - Latest code in GitHub  
✅ **Pushed** - Repository updated  
⏳ **Next:** Deploy to Netlify (you do this in dashboard)  
⏳ **Then:** Configure DNS  
⏳ **Then:** Test live site  
⏳ **Finally:** Auth polish

---

**I'll wait while you deploy through Netlify dashboard.**

Tell me when:
1. You've connected GitHub to Netlify
2. Site is deployed (you have the Netlify URL)
3. You're ready to configure the domain

Or let me know if you hit any issues! 🧺


# 🌐 DOMAIN SETUP: tekete.co.nz
## Connect Your New Domain to Netlify + Cloudflare!

**Domain:** tekete.co.nz ✅ PURCHASED!  
**Registrar:** CrazyDomains  
**Time:** 30 minutes total  
**Result:** Professional domain + 2-3x faster! 🚀

---

## 🎯 **STEP 1: CONNECT TO NETLIFY (15 MIN)**

### **A. Get Netlify's IP Address (2 min)**

1. **Go to:** https://app.netlify.com
2. **Select your site**
3. **Go to:** Domain settings
4. **Click:** "Add custom domain"
5. **Enter:** `tekete.co.nz`
6. **Netlify will say:** "Configure DNS records"

**Netlify's Load Balancer IP:** `75.2.60.5`

---

### **B. Update DNS at CrazyDomains (10 min)**

**Go to:** https://crazydomains.co.nz/members/domains/details/29281399/dns

**EDIT These Records:**

**1. Root Domain (A Record):**
- Click **EDIT** on: `tekete.co.nz`
- Change IP from: `27.124.125.171`
- Change to: `75.2.60.5` (Netlify!)
- **SAVE**

**2. WWW Subdomain:**
- Click **EDIT** on: `www.tekete.co.nz`
- Change IP from: `27.124.125.171`
- Change to: `75.2.60.5` (Netlify!)
- **SAVE**

**OR better - use CNAME for www:**
- **DELETE** the www A record
- **ADD RECORD** → CNAME:
  - Sub Domain: `www`
  - Points to: `tekete.netlify.app`
- **SAVE**

---

### **C. Clean Up (Optional - 3 min)**

**DELETE these (not needed for website):**
- ❌ `mail.tekete.co.nz` (unless you want email)
- ❌ `ftp.tekete.co.nz`
- ❌ `pop.tekete.co.nz`
- ❌ `pop3.tekete.co.nz`
- ❌ `smtp.tekete.co.nz`
- ❌ `autoconfig.tekete.co.nz`

**KEEP these (if you want email):**
- ✅ MX Record (for email)

**Your final DNS should look like:**
```
A Record:    tekete.co.nz → 75.2.60.5
CNAME:       www → tekete.netlify.app
MX Record:   (keep if you want email)
```

Clean & simple! ✨

---

### **D. Verify It Works (5 min)**

**Wait:** 5-15 minutes for DNS propagation

**Test:**
1. Visit: `tekete.co.nz` (should show your site!)
2. Visit: `www.tekete.co.nz` (should redirect!)
3. Check HTTPS (should be automatic!)

**If it works:** ✅ PROCEED TO STEP 2!

---

## ☁️ **STEP 2: ADD TO CLOUDFLARE (15 MIN)**

### **A. Add Site to Cloudflare (5 min)**

1. **Go to:** https://dash.cloudflare.com/437d5fb27fa7259b17b0e98407800300

2. **Click:** "Add a site"

3. **Enter:** `tekete.co.nz`

4. **Select:** Free plan

5. **Click:** "Add site"

6. Cloudflare scans your DNS...

---

### **B. Configure DNS in Cloudflare (5 min)**

**Cloudflare shows your current DNS records:**

**Make sure these are present:**
```
A Record:    tekete.co.nz → 75.2.60.5 (☁️ orange cloud ON!)
CNAME:       www → tekete.netlify.app (☁️ orange cloud ON!)
```

**Orange cloud = CDN active!** ✅

**Click:** "Continue"

---

### **C. Update Nameservers (5 min)**

**Cloudflare gives you 2 nameservers like:**
```
adam.ns.cloudflare.com
erin.ns.cloudflare.com
```

**Go back to CrazyDomains:**
1. Find "Nameservers" section (different from DNS Records!)
2. Click "Change Nameservers"
3. Replace with Cloudflare's 2 nameservers
4. **SAVE**

**Wait:** 15 min - 24 hours (usually 1 hour!)

---

### **D. Verify Cloudflare Active (2 min)**

**Go back to Cloudflare dashboard**

**Status will change from:**
- ⏳ "Pending" → ✅ "Active"

**Once active:**
- Site is 2-3x faster! ⚡
- DDoS protection on! 🛡️
- Analytics available! 📊

**DONE!** ☁️✨

---

## 🎊 **TOTAL TIME: 30 MINUTES**

**Step 1:** Netlify DNS (15 min)  
**Step 2:** Cloudflare (15 min)

**Result:**
- Professional domain: `tekete.co.nz` ✅
- Fast globally: 2-3x speed! ⚡
- Secure: DDoS protection! 🛡️
- **FREE!** 🎉

---

## ⚠️ **IMPORTANT:**

**DNS propagation takes time!**
- Minimum: 5-15 minutes
- Maximum: 24-48 hours
- Usually: 1-2 hours

**Be patient!** It will work! ✨

---

**Ready to start?** 🚀

**Kia kaha e hoa! Professional domain incoming!** 🌟💝



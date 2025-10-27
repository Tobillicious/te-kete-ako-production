# 🌐 CRAZY DOMAINS DNS SETUP - tekete.co.nz

**Your Site:** https://te-kete-ako-production.pages.dev/ ✅  
**Your Domain:** tekete.co.nz (Crazy Domains)  
**Goal:** Point domain to Cloudflare Pages

---

## 📋 PART 1: Add Custom Domain in Cloudflare Pages (3 mins)

### **In Cloudflare Pages Dashboard:**

1. **Find Custom Domains:**
   - You should see **"Add custom domain"** card
   - OR go to your project → **"Custom domains"** tab
   - Click **"Set up a custom domain"**

2. **Enter Domain:**
   - Type: `tekete.co.nz`
   - Click **"Continue"** or **"Add domain"**

3. **Cloudflare Will Show DNS Instructions:**
   - Copy these! You'll need them for Crazy Domains
   - Usually looks like:
   ```
   CNAME Record:
   Name: tekete.co.nz (or @)
   Target: te-kete-ako-production.pages.dev
   ```

**Keep this Cloudflare tab open!** You'll need those DNS values.

---

## 📋 PART 2: Configure DNS at Crazy Domains (5 mins)

### **Step 1: Log Into Crazy Domains**

1. Go to: https://www.crazydomains.co.nz
2. Click **"Login"** (top right)
3. Enter your email/password
4. Log in

---

### **Step 2: Find DNS Management**

1. **Go to "My Account"** or **"Domains"**
2. Find **`tekete.co.nz`** in your domain list
3. Click **"Manage"** or **"DNS Settings"** next to it

You'll see options like:
- DNS Settings
- Nameservers
- Domain Settings

**Click "DNS Settings"** or **"Manage DNS"**

---

### **Step 3: Add DNS Records**

Crazy Domains shows a table of DNS records. You need to add:

#### **Record 1: CNAME for Root Domain**

```
Type: CNAME
Host: @ (or leave blank, or type "tekete.co.nz")
Points to: te-kete-ako-production.pages.dev
TTL: 1 Hour (or 3600)
```

**Click "Add Record"** or **"Save"**

---

#### **Record 2: CNAME for www (Optional but Recommended)**

```
Type: CNAME
Host: www
Points to: te-kete-ako-production.pages.dev
TTL: 1 Hour (or 3600)
```

**Click "Add Record"** or **"Save"**

---

### **Step 4: Remove Conflicting Records (Important!)**

**Before adding new records, DELETE these if they exist:**
- Any **A records** pointing to old IPs
- Any **CNAME records** pointing to Netlify
- Keep MX records (email) if you have them

**In Crazy Domains DNS table:**
- Look for rows with `@` or `tekete.co.nz` in Host column
- Delete old A or CNAME records
- Add the new ones above

---

### **Step 5: Save Changes**

1. Click **"Save"** or **"Update DNS"** button
2. Crazy Domains might ask you to confirm
3. **Done!**

---

## ⏱️ **WAIT FOR DNS PROPAGATION**

**Timeline:**
- **Fastest:** 10-30 minutes
- **Typical:** 1-2 hours
- **Maximum:** 24 hours

---

## 🧪 **TEST IF IT'S WORKING**

### **Method 1: Browser**
Just visit: https://tekete.co.nz

**If it works:** You'll see your site! 🎉  
**If it doesn't:** DNS still propagating, wait 10 more mins

---

### **Method 2: Command Line**

```bash
nslookup tekete.co.nz
```

**When working, you'll see:**
```
Name: tekete.co.nz
Address: [Cloudflare IP]
```

---

## 🎯 **SUMMARY OF WHAT TO DO:**

### **Now (Cloudflare):**
1. ✅ Click "Add custom domain" card
2. ✅ Enter `tekete.co.nz`
3. ✅ Note the DNS instructions

### **Now (Crazy Domains):**
4. ✅ Log in to Crazy Domains
5. ✅ Go to tekete.co.nz → DNS Settings
6. ✅ Add CNAME: `@` → `te-kete-ako-production.pages.dev`
7. ✅ Add CNAME: `www` → `te-kete-ako-production.pages.dev`
8. ✅ Save changes

### **Wait (10-60 mins):**
9. ⏳ DNS propagates
10. ✅ Visit https://tekete.co.nz
11. 🎉 YOUR SITE IS LIVE!

---

## 💡 **ABOUT THE TRANSFER:**

**You DON'T need to complete the Cloudflare transfer!**

**With DNS configuration:**
- ✅ tekete.co.nz points to your site
- ✅ Works perfectly
- ✅ No 48-hour wait

**Transfer is only useful if:**
- You want Cloudflare to manage domain renewals
- You want easier DNS changes in future
- You want all services in one place

**For now:** Just configure DNS. Transfer later if you want!

---

## 🚀 **GO DO IT!**

1. In Cloudflare: Add custom domain `tekete.co.nz`
2. In Crazy Domains: Add those CNAME records
3. Tell me when done, I'll help you test!

🧺 Kia kaha!


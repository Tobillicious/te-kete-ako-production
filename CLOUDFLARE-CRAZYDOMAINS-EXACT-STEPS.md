# ☁️ CLOUDFLARE + CRAZY DOMAINS - EXACT STEPS FOR YOU

**Your Registrar:** Crazy Domains (crazydomains.co.nz)  
**Your Domain:** tekete.co.nz  
**Task:** Update nameservers to activate Cloudflare  

---

## 📋 **EXACT STEP-BY-STEP FOR CRAZY DOMAINS**

### **Step 1: Login to Crazy Domains**

1. Go to: https://www.crazydomains.co.nz
2. Click "Sign In" (top right)
3. Enter your email and password
4. Click "Sign In"

---

### **Step 2: Navigate to Domain Management**

1. After login, you'll see your dashboard
2. Look for "Domains" in the menu (or "My Services")
3. Click "Domains" or "Domain Names"
4. You should see `tekete.co.nz` in your list
5. Click on `tekete.co.nz` to manage it

---

### **Step 3: Find Nameservers Section**

**In Crazy Domains, it's usually:**
- Tab called "DNS & Nameservers"
- OR "Advanced Settings" → "Nameservers"
- OR "Domain Settings" → "Name Servers"

**Look for:**
- Section titled "Nameservers" or "Name Servers"
- Radio buttons or dropdown with options like:
  - "Use Crazy Domains nameservers"
  - "Use custom nameservers"

---

### **Step 4: Switch to Custom Nameservers**

1. Select the option: **"Use custom nameservers"** or **"Custom DNS"**
2. You'll see input fields (usually 2 or 4 boxes)
3. Clear any existing nameservers if present

---

### **Step 5: Add Cloudflare Nameservers**

**From your Cloudflare dashboard, you should have 2 nameservers.**

**In the Cloudflare screenshot you showed me, I saw:**
- First one: `gannon.ns.cloudflare.com`
- Second one: (scroll down in Cloudflare to see it)

**Enter in Crazy Domains:**
- **Nameserver 1:** `gannon.ns.cloudflare.com`
- **Nameserver 2:** `[the second one from Cloudflare]` (probably something like `uma.ns.cloudflare.com` or similar)

**Copy them EXACTLY as Cloudflare shows** (Cloudflare has a "Click to copy" button)

---

### **Step 6: Check for DNSSEC**

**In Crazy Domains:**
- Look for "DNSSEC" setting (might be on same page or separate tab)
- If you see it and it's **ON**, turn it **OFF**
- Save that change first
- Wait 5 minutes

**If you don't see DNSSEC:** Perfect! Crazy Domains might not offer it. Skip this step.

---

### **Step 7: Save Changes**

1. Click **"Save"** or **"Update"** or **"Apply Changes"**
2. Crazy Domains might show a confirmation message
3. **Confirmation:** "Nameservers updated successfully" or similar

**Important:** Make sure you click Save! Changes don't apply until you save.

---

### **Step 8: Wait for Propagation**

**What happens now:**
- Crazy Domains sends update to internet's DNS system
- Usually takes **15 minutes to 1 hour** for Crazy Domains
- Can take up to 24 hours in rare cases

**While waiting:**
- ✅ Your site stays online (no downtime!)
- ✅ Continue working on other things
- ✅ Check Cloudflare dashboard every 15-30 min
- ✅ Check your email (Cloudflare sends confirmation)

---

## ✅ **HOW TO VERIFY IT'S WORKING**

### **Check 1: Cloudflare Dashboard**
- Refresh your Cloudflare page
- Look at the orange tag at top
- **"Invalid nameservers"** → Still processing, wait
- **"Active"** → SUCCESS! 🎉

### **Check 2: Your Email**
- Cloudflare sends email when activated
- Subject: "Your site is active on Cloudflare"
- Usually arrives within 15-60 minutes

### **Check 3: DNS Propagation**
- Go to: https://www.whatsmydns.net/
- Enter: `tekete.co.nz`
- Type: NS (nameservers)
- Click Search
- **See Cloudflare nameservers?** ✅ Success!

---

## 🎯 **COMMON CRAZY DOMAINS ISSUES**

### **Issue 1: Can't Find Nameserver Settings**

**Try:**
1. Look under "Advanced Settings"
2. Or "DNS Management"
3. Or click the gear icon ⚙️ next to tekete.co.nz
4. Or contact Crazy Domains chat support (usually quick!)

### **Issue 2: "Premium DNS" or Similar Option**

**If you see:**
- "Use Crazy Domains DNS" (default)
- "Use Premium DNS" (paid option)
- "Use Custom Nameservers" ← **SELECT THIS ONE!**

### **Issue 3: Only 2 Nameserver Fields**

**That's normal!** Cloudflare only gives you 2 nameservers.  
If Crazy Domains shows 4 boxes:
- Fill the first 2 with Cloudflare's
- Leave boxes 3 and 4 empty

---

## 💡 **CURRENT STATUS**

**You said:** "I think I might have set it up now"

**What you probably did:** ✅
- Logged into Crazy Domains
- Found nameserver settings
- Switched to custom nameservers
- Added Cloudflare's nameservers
- Saved changes

**What's happening now:**
- ⏳ Propagating across the internet (15 min - 4 hours)
- ✅ Your site stays online
- ✅ No downtime
- ✅ Wait for "Active" status in Cloudflare

---

## 🎊 **YOU'RE PROBABLY DONE!**

**If you:**
- ✅ Changed nameservers to Cloudflare's
- ✅ Saved the changes
- ✅ See confirmation from Crazy Domains

**Then:**
- ✅ Setup is complete!
- ⏳ Just waiting for DNS propagation
- 🎉 Will be active soon (15-60 min usually)

**Check Cloudflare dashboard in 15 minutes!**  
**Or wait for their email confirmation!**

---

## 🚀 **WHILE YOU WAIT**

**Perfect time to:**
- ✅ Work on other TODOs
- ✅ Test the subscription flow
- ✅ Review GraphRAG-Mapping's features
- ✅ Plan beta teacher invitations
- ✅ Take a break! (You've crushed it today!)

**Your site stays live and functional while propagating!**

---

**Great job setting it up!** 🎉  
**Check back in 15-30 minutes for "Active" status!**  
**Email will confirm when ready!**

**Kia kaha!** 💚🚀


# 🎯 VISUAL TESTING PROTOCOL - MANDATORY FOR ALL AGENTS

**Created:** October 25, 2025  
**Purpose:** Prevent 8-hour debugging cycles by SEEING what users see  
**User Directive:** "Can you get a tool so that you can see that yourself?"

---

## ❌ **THE OLD BROKEN WAY:**

1. Agent makes changes locally ❌
2. Agent assumes "it should work" ❌  
3. User reports "site looks broken" ❌
4. Agent asks "what do you see?" ❌
5. **8 hours of back-and-forth describing visual issues** ❌

**Result:** Frustration, wasted time, obvious problems missed

---

## ✅ **THE NEW VISUAL TESTING WAY:**

### **BEFORE every deployment, agents MUST:**

1. **Navigate to live site** using Playwright:
```javascript
mcp_cursor-playwright_browser_navigate("https://tekete.netlify.app")
```

2. **Take screenshot** to SEE what users see:
```javascript
mcp_cursor-playwright_browser_take_screenshot({
  filename: "pre-deployment-check.png",
  fullPage: true
})
```

3. **Check console errors**:
```javascript
mcp_cursor-playwright_browser_console_messages()
```

4. **Capture page snapshot** (accessibility tree):
```javascript
mcp_cursor-playwright_browser_snapshot()
```

5. **Test key pages:**
- Homepage: https://tekete.netlify.app
- Unit Plans: https://tekete.netlify.app/units/
- Lessons: https://tekete.netlify.app/lessons
- Sample lesson: https://tekete.netlify.app/units/y9-science-ecology/
- Sample hub: https://tekete.netlify.app/mathematics-hub.html

---

## 🚨 **WHAT TO CHECK FOR:**

### **Visual Issues (Screenshot):**
- ❌ Huge empty spaces (hero too big!)
- ❌ Content invisible (pushed off-screen!)
- ❌ Broken layout (CSS not loading!)
- ❌ Missing images/icons
- ❌ Weird scaling ("icons the size of the screen")
- ✅ Professional, usable layout
- ✅ Content visible immediately
- ✅ Navigation works

### **Console Errors:**
- ❌ CSP violations (blocking resources)
- ❌ 404 errors (files not found)
- ❌ JavaScript crashes
- ❌ Failed fetches
- ✅ Clean console or only minor warnings

### **Content Loading:**
- ✅ Navigation renders
- ✅ Hero section reasonable size
- ✅ Main content visible
- ✅ Footer renders
- ✅ Components inject properly

---

## 🛠️ **PLAYWRIGHT TOOLS AVAILABLE:**

```javascript
// Navigation
mcp_cursor-playwright_browser_navigate(url)
mcp_cursor-playwright_browser_navigate_back()

// Visual Testing
mcp_cursor-playwright_browser_take_screenshot(options)
mcp_cursor-playwright_browser_snapshot()

// Debugging
mcp_cursor-playwright_browser_console_messages()
mcp_cursor-playwright_browser_network_requests()

// Interaction Testing
mcp_cursor-playwright_browser_click(element, ref)
mcp_cursor-playwright_browser_type(element, ref, text)
mcp_cursor-playwright_browser_fill_form(fields)

// Waiting
mcp_cursor-playwright_browser_wait_for({ time: 3 })
```

---

## 📊 **EXAMPLE VISUAL TEST WORKFLOW:**

```markdown
### BEFORE Making Changes:
1. Navigate to live site
2. Screenshot current state
3. Note visual issues

### AFTER Making Changes Locally:
1. Deploy to staging/production
2. Wait 3 minutes for deployment
3. Navigate to live site AGAIN
4. Screenshot new state
5. Compare: Did visual issues get fixed?
6. Check console for new errors
7. ONLY THEN confirm to user!
```

---

## 💡 **LESSONS FROM OCT 25 INCIDENT:**

### **What Happened:**
- User: "Site looks broken - empty page, huge icons!"
- Agents: "We fixed CSP! Should work now!"
- Reality: **Hero section 85vh** pushing content off-screen
- User frustration: 8 hours trying to explain visual issue
- Solution: **Agent uses screenshot tool**, sees issue in 30 seconds

### **Root Causes We Missed:**
1. ❌ Tested GraphRAG tools (work for AI) not content pages (for humans)
2. ❌ Assumed CSS loading = layout working
3. ❌ Never looked at live deployed site visually
4. ❌ Relied on user to describe layout problems

### **What We Should Have Done:**
1. ✅ Navigate to https://tekete.netlify.app/units/
2. ✅ Take full-page screenshot
3. ✅ SEE the massive hero section immediately
4. ✅ Fix in 2 minutes instead of 8 hours

---

## 🎯 **MANDATORY CHECKLIST:**

**Before saying "site is ready" or "deployment complete":**

- [ ] Navigated to live site via Playwright ✅
- [ ] Screenshot homepage (looks professional?) ✅
- [ ] Screenshot /units/ page (content visible?) ✅
- [ ] Screenshot /lessons page (layout works?) ✅  
- [ ] Checked console (zero critical errors?) ✅
- [ ] Tested on 5+ different pages ✅
- [ ] Content visible WITHOUT scrolling ✅
- [ ] No "huge empty spaces" ✅
- [ ] Navigation clickable and works ✅

**If ANY checkbox is unchecked → DON'T DEPLOY!**

---

## 🚀 **BENEFITS:**

✅ **Catch visual issues in 30 seconds** instead of 8 hours  
✅ **SEE what users see** without relying on descriptions  
✅ **Test real deployed pages** not just local files  
✅ **Prevent user frustration** from obvious broken layouts  
✅ **Build confidence** in deployments  
✅ **Professional quality** assured before user testing  

---

## 📝 **AGENT COMMITMENT:**

**From now on, ALL agents must:**
1. Use Playwright visual testing BEFORE claiming "site is ready"
2. Screenshot 5+ pages and verify layouts
3. Check console for errors
4. Test as a teacher/student would use the site
5. ONLY deploy if visual testing passes

**No more 8-hour debugging cycles!** 💪

---

**This protocol honors the user's time and ensures we catch "giant obvious problems" ourselves!** 🎯✨

**Generated:** October 25, 2025  
**User Feedback:** "Can you get a tool so that you can see that yourself?"  
**Answer:** YES! Playwright browser automation! We'll use it EVERY TIME now! 🚀


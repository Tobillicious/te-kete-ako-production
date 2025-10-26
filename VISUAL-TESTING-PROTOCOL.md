# 🎨 VISUAL TESTING PROTOCOL

**Mandatory for ALL CSS/Design Changes**  
**Effective:** October 26, 2025

---

## 🚨 THE RULE

**NEVER deploy CSS changes without visual verification and user approval.**

---

## ✅ PRE-DEPLOYMENT CHECKLIST

### **Step 1: Local Preview**
- [ ] Open page in browser locally
- [ ] Check on laptop/desktop (1920x1080)
- [ ] Check on tablet (768x1024)
- [ ] Check on mobile (375x667)

### **Step 2: Visual Inspection**

**Colors:**
- [ ] Primary color consistent (#8b4513 - BMAD brown OR chosen system)
- [ ] Secondary colors harmonious
- [ ] Text readable (contrast ratio > 4.5:1)
- [ ] Links distinguishable

**Typography:**
- [ ] Headings clear hierarchy (h1 > h2 > h3)
- [ ] Body text readable (16px minimum)
- [ ] Line height comfortable (1.5-1.8)
- [ ] Font family loads correctly

**Spacing:**
- [ ] Margins consistent
- [ ] Padding appropriate
- [ ] Components don't overlap
- [ ] White space balanced

**Layout:**
- [ ] Navigation accessible
- [ ] Content readable
- [ ] Footer visible
- [ ] No horizontal scroll (mobile)

**Cultural Elements:**
- [ ] Koru patterns visible (if applicable)
- [ ] Māori text displays correctly
- [ ] Cultural colors respected
- [ ] Whakataukī styling appropriate

### **Step 3: Functional Testing**

- [ ] Navigation works
- [ ] Buttons clickable
- [ ] Forms functional
- [ ] Hover states work
- [ ] Mobile menu toggles
- [ ] Print preview acceptable

### **Step 4: Cross-Browser Check**

- [ ] Chrome/Edge (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Mobile Safari (iOS)
- [ ] Mobile Chrome (Android)

### **Step 5: Screenshot Evidence**

- [ ] Take screenshot of homepage
- [ ] Take screenshot of key page
- [ ] Save to `/docs/visual-tests/YYYY-MM-DD/`
- [ ] Note what changed

### **Step 6: Deploy Preview**

- [ ] Create Netlify deploy preview
- [ ] Share preview URL
- [ ] Test on real devices
- [ ] Get user feedback

### **Step 7: User Approval**

- [ ] Show user the changes
- [ ] Explain what's different
- [ ] Get explicit "YES, deploy this"
- [ ] Document approval

### **Step 8: Deploy to Production**

- [ ] Merge to main
- [ ] Verify deployment
- [ ] Check live site
- [ ] Monitor for errors (Sentry)

---

## 🎯 PAGES TO ALWAYS TEST

**Critical Path:**
1. Homepage (`/index.html`)
2. Teacher landing (`/teachers/index.html`)
3. Student landing (`/students/index.html`)
4. Subject hub (any one)
5. Lesson page (any one)

**Minimum:** Test these 5 pages before ANY CSS deployment.

---

## 📊 WHAT WE'RE AVOIDING

**Never Again:**
- ❌ Blind deployment (not seeing the result)
- ❌ Multiple design systems loading
- ❌ Accumulating CSS without removing old
- ❌ Assuming "it should work"
- ❌ Feature-first, design-never
- ❌ Complex = better

**Always:**
- ✅ Visual verification before deploy
- ✅ ONE design system active
- ✅ Remove old before adding new
- ✅ Test thoroughly
- ✅ Design = equally important as features
- ✅ Simple = better

---

## 🌟 DESIGN SYSTEM LOCK

**Current System:** BMAD Authentic  
**Last Changed:** October 26, 2025  
**Approved By:** User

**To Change Design System:**
1. Create proposal document
2. Build prototype
3. Show user visually
4. Get explicit approval
5. Archive old system FIRST
6. Deploy new system
7. Update this document

**DO NOT:**
- Add another design system "alongside"
- Mix systems
- Create "improvements" without removing old

---

## 📋 VISUAL TEST LOG

| Date | Change | Pages Tested | User Approval | Deployed |
|------|--------|--------------|---------------|----------|
| 2025-10-26 | BMAD-only cleanup | Homepage, 945 files | ✅ YES | ✅ YES |

---

**THIS PROTOCOL IS MANDATORY.**

**Violating it causes:**
- Ugly site
- Inconsistent design
- User disappointment
- Wasted development time

**Following it ensures:**
- Beautiful site
- Consistent design
- User satisfaction
- Efficient development

---

*Visual testing saves everything.*  
*Always see before you ship.*

✅ **PROTOCOL ACTIVE**


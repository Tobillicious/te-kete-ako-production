# ⚡ Quick Start: Testing & Deployment Guide

**Last Updated:** October 21, 2025  
**For:** Next agent or human tester  
**Time Required:** 3-4 hours for complete testing

---

## 🚀 TL;DR - What to Do Now

1. **Start local server:** `cd public && python3 -m http.server 8000`
2. **Open:** `VISUAL-AUDIT-CHECKLIST.md`
3. **Test 25 pages** - Check off items as you go
4. **Run browser tests** - Use `BROWSER-TESTING-PROTOCOL.md`
5. **Run Lighthouse audits** - Use `LIGHTHOUSE-AUDIT-CHECKLIST.md`
6. **Fix any issues found**
7. **Deploy to Netlify** - Follow `NETLIFY-DEPLOYMENT-CHECKLIST.md`

---

## 📂 Key Files (in this directory)

| File | Purpose | Time Needed |
|------|---------|-------------|
| `VISUAL-AUDIT-CHECKLIST.md` | Test 25 pages visually | 60-90 min |
| `BROWSER-TESTING-PROTOCOL.md` | Cross-browser testing | 45-60 min |
| `LIGHTHOUSE-AUDIT-CHECKLIST.md` | Performance/A11y audits | 30-45 min |
| `NETLIFY-DEPLOYMENT-CHECKLIST.md` | Deploy to production | 20-30 min |
| `SESSION-SUMMARY-OCT21-EVENING.md` | What was done tonight | 5 min read |

---

## ✅ Current Status

### COMPLETED ✅
- [x] Content duplication fixed
- [x] Placeholder text removed (79 files)
- [x] Navigation links fixed
- [x] Subject/level metadata cleaned
- [x] Testing framework created

### READY FOR YOU ⏳
- [ ] Visual audit (use checklist)
- [ ] Browser testing (use protocol)
- [ ] Lighthouse audits (use checklist)
- [ ] Fix any issues found
- [ ] Deploy to Netlify

---

## 🎯 3 Critical User Journeys to Test

### Journey 1: Teacher Finding a Lesson
```
1. Open homepage
2. Click "Lessons" 
3. Filter by Year 9, Mathematics
4. Click a lesson
5. Read content
6. Print
```
**Test on:** Desktop Chrome, Mobile Safari, Tablet

### Journey 2: Student Using Interactive Lesson
```
1. Open interactive lesson
2. Use calculator/chart
3. Complete activities
```
**Test on:** Desktop Chrome/Firefox

### Journey 3: Teacher Registration
```
1. Homepage → Register
2. Fill form
3. Submit
4. Login
5. Access dashboard
```
**Test on:** Desktop Chrome, Mobile Safari

---

## 🐛 What to Look For

### Red Flags 🔴
- Broken images
- JavaScript console errors
- Forms that don't submit
- Links that don't work
- Missing CSS (unstyled content)
- Placeholder text like `{VARIABLE}`

### Yellow Flags ⚠️
- Slow page loads (> 3 seconds)
- Poor mobile layout
- Low contrast text
- Missing alt text on images
- Non-semantic HTML

### Green Flags ✅
- Beautiful, professional design
- Fast loading
- Works on all devices
- Accessible (keyboard navigation, screen readers)
- Cultural elements present

---

## 🔧 Testing Tools Setup

### Option A: Quick Visual Test
```bash
# 1. Start server
cd /Users/admin/Documents/te-kete-ako-clean/public
python3 -m http.server 8000

# 2. Open browser
open http://localhost:8000

# 3. Use checklist to test pages
```

### Option B: Comprehensive Test
```bash
# 1. Install Lighthouse
npm install -g lighthouse

# 2. Start server (in terminal 1)
cd /Users/admin/Documents/te-kete-ako-clean/public
python3 -m http.server 8000

# 3. Run audits (in terminal 2)
mkdir -p audits
lighthouse http://localhost:8000/ --output html --output-path ./audits/homepage.html --view
```

---

## 📊 Success Criteria

Before deploying, ensure:
- ✅ All 25 pages in visual audit pass
- ✅ 3 critical user journeys work perfectly
- ✅ Lighthouse scores: P90+ A95+ BP90+ SEO90+
- ✅ No critical bugs (red flags)
- ✅ Tested on Chrome, Firefox, Safari
- ✅ Tested on mobile, tablet, desktop
- ✅ Forms work correctly
- ✅ Authentication flows tested

---

## 🚀 Deploy Shortcut

If testing passes, deploy with:

```bash
# Assuming you have Netlify CLI installed
# npm install -g netlify-cli

# 1. Login to Netlify
netlify login

# 2. Link site (first time only)
netlify link

# 3. Deploy
netlify deploy --prod --dir=public

# 4. Test live site
open https://[your-site].netlify.app
```

---

## 💡 Pro Tips

1. **Start with homepage** - First impressions matter
2. **Test mobile early** - 40%+ users on tablets/phones
3. **Check forms carefully** - Authentication is critical
4. **Don't skip print testing** - Teachers print lessons
5. **Test te reo macrons** - ā, ē, ī, ō, ū must display correctly
6. **Use real devices** - Emulators miss issues
7. **Check console** - Open DevTools, look for errors
8. **Test slow connections** - Throttle to 3G in DevTools

---

## 🆘 If You Find Issues

1. **Document it** - Use bug template in `BROWSER-TESTING-PROTOCOL.md`
2. **Prioritize** - P0 (critical) → P1 (high) → P2 (medium) → P3 (low)
3. **Fix critical first** - Don't deploy with P0 bugs
4. **Re-test after fixing** - Confirm fix doesn't break something else
5. **Update GraphRAG** - Log discoveries in `agent_knowledge`

---

## 📞 Need Help?

- **Read session summary:** `SESSION-SUMMARY-OCT21-EVENING.md`
- **Check GraphRAG:** Query `agent_knowledge` table
- **Read checklists:** Detailed instructions in each checklist
- **Test locally first:** Always test on localhost before deploying

---

## 🎉 When Testing Complete

1. ✅ All checklists completed
2. ✅ All critical issues fixed
3. ✅ Lighthouse scores meet targets
4. ✅ User journeys work perfectly
5. ✅ Deployed to Netlify
6. ✅ Live site tested
7. ✅ Documentation updated
8. ✅ Team notified

**Then:** Celebrate! 🎊 Te Kete Ako is live and ready for beta teachers!

---

**Kia kaha! You've got this!** 💪

---

*Questions? Check agent_knowledge in GraphRAG or read detailed checklists.*


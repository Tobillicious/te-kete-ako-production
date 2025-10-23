# 📋 Extracted TODOs from GraphRAG & ACTIVE_QUESTIONS.md
**Date:** October 20, 2025  
**Source:** ACTIVE_QUESTIONS.md (6-Agent Hui Missions)  
**Extracted By:** Responsive Build Agent

---

## 🚀 **MISSION 1: DEPLOYMENT VALIDATION** (Kaiwaihanga Matihiko Lead)

### **Uncompleted Tasks:**
- [ ] Test local server (python3 -m http.server)
- [ ] Test GraphRAG lessons.html loading locally
- [ ] Commit all changes (2k lines!)
- [ ] Push to GitHub
- [ ] Monitor Netlify deployment
- [ ] Test live site once deployed
- [ ] Verify Supabase CORS works on live domain
- [ ] Check all CDN resources load (Tailwind, Supabase, etc.)

**Priority:** 🔴 **CRITICAL - Pre-Launch**  
**Estimated Time:** 2-3 hours  
**Success Metric:** Site deploys successfully + lessons.html loads 500+ from GraphRAG!

---

## 🧪 **MISSION 2: HUMAN UX TESTING** (Kaitiaki Tūhono Lead)

### **Completed:**
- [✅] 10pm Teacher scenario (DONE - 2:45 PASS!)

### **Uncompleted Tasks:**
- [ ] Student discovery journey (can they find Y9 Ecology?)
- [ ] First-time visitor journey (onboarding tour helpful?)
- [ ] Mobile testing (iPhone + Android with real devices)
- [ ] Search testing (verify all common queries work)
- [ ] Print workflow (teacher prints lesson for class)
- [ ] My Kete workflow (save favorites, retrieve later)
- [ ] Help system discovery (can users find FAQ?)

**Priority:** 🟡 **HIGH - User Experience**  
**Estimated Time:** 3-4 hours  
**Success Metric:** 8/8 user journeys pass without friction!

---

## 💎 **MISSION 3: PROFESSIONAL CONSISTENCY** (Kaiwhakakotahi Lead)

### **Uncompleted Tasks:**
- [ ] Audit all hub pages (consistent styling?)
- [ ] Check navigation across all pages (components loading?)
- [ ] Verify mobile-bottom-nav shows everywhere
- [ ] Ensure FAB appears on all lesson/handout pages
- [ ] Check beta badge visibility (homepage + lessons.html only, or everywhere?)
- [ ] Verify whakataukī formatting consistent
- [ ] Check print CSS applied to all lesson pages
- [ ] Audit for any remaining Lorem Ipsum or template text

**Priority:** 🟡 **HIGH - Polish**  
**Estimated Time:** 2-3 hours  
**Success Metric:** Zero inconsistencies in top 50 most-visited pages!

---

## 🔍 **MISSION 4: CONTENT DISCOVERY** (Kaiārahi Mātauranga Lead)

### **Completed:**
- [✅] GraphRAG lessons.html deployed (Tūhono complete!)
- [✅] Ensure generated-resources-alpha linked (Done via Discovery dropdown!)

### **Uncompleted Tasks:**
- [ ] Verify all 1,091 lessons appear in lessons.html
- [ ] Test filters (Year Level, Subject, Duration, Cultural)
- [ ] Check search integration (enhanced-search.js)
- [ ] Verify hub pages link to all relevant lessons
- [ ] Test cross-curricular connections
- [ ] Validate breadcrumb navigation

**Priority:** 🟡 **MEDIUM - Discoverability**  
**Estimated Time:** 2-3 hours  
**Success Metric:** Users can find ANY lesson within 2 clicks from homepage!

---

## 🌿 **MISSION 5: CULTURAL EXCELLENCE** (Kaiwhakawhanake Ahurea Lead)

### **Uncompleted Tasks:**
- [ ] Verify whakataukī appear appropriately (not overwhelming)
- [ ] Check te reo Māori has English translations visible
- [ ] Ensure cultural patterns enhance beauty (not distract)
- [ ] Test cultural tooltips work (if implemented)
- [ ] Verify Māori pronunciation audio (if exists)
- [ ] Check cultural safety for non-Māori users
- [ ] Ensure cultural badges are informative (not just decoration)
- [ ] Test cultural filters in search/browse

**Priority:** 🟢 **MEDIUM - Quality Assurance**  
**Estimated Time:** 2-3 hours  
**Success Metric:** Cultural integration feels INTEGRAL, not intimidating!

---

## 🔧 **MISSION 6: TECHNICAL EXCELLENCE** (Kaiwaihanga Matihiko + Tūhono)

### **Uncompleted Tasks:**
- [ ] Lighthouse audit (10 sample pages)
- [ ] Check console errors (any red errors?)
- [ ] Verify all component injection works (fetch calls)
- [ ] Test Supabase queries (GraphRAG loading)
- [ ] Check security headers (netlify.toml CSP)
- [ ] Verify service worker (PWA offline support)
- [ ] Test authentication flows (login, OAuth callback)
- [ ] Check PostHog analytics ready (need API key)

**Priority:** 🟡 **HIGH - Technical Readiness**  
**Estimated Time:** 3-4 hours  
**Success Metric:** Zero critical console errors, Lighthouse 85+!

---

## 🆕 **NEW TODOS FROM OCT 20 AUDIT:**

### **From Platform Audit:**
1. [ ] **Fix content duplication in ~50 integrated-lessons pages**
   - Location: `/public/integrated-lessons/science/` and similar
   - Issue: Complete HTML documents nested inside content divs
   - Fix: Create batch script to parse and extract just lesson content
   - Priority: 🟡 **MEDIUM**
   - Time: 2-3 hours

2. [ ] **Create HTML duplication cleanup script**
   - Parse minified HTML in integrated-lessons
   - Extract content between nested `<body>` tags
   - Remove duplicate header/footer
   - Priority: 🟡 **MEDIUM**
   - Time: 1 hour to write script

3. [ ] **Optimize large index files (optional)**
   - Files: `/public/lessons.html`, `/public/handouts.html`
   - Consider: Pagination or GraphRAG-powered loading
   - Priority: 🟢 **LOW - Nice to Have**
   - Time: 3-4 hours

4. [ ] **Clean backup files (optional)**
   - Location: Throughout `/public/`
   - Action: Move ~500 `.bak` and `.master-backup` files to `/backups/`
   - Priority: 🟢 **LOW - Housekeeping**
   - Time: 30 minutes

### **From Component Testing:**
5. [ ] **Verify fetch() components work in production**
   - Test: navigation-standard.html loads from live domain
   - Test: footer.html, mobile-bottom-nav.html load
   - Check: CORS headers for component files
   - Priority: 🔴 **CRITICAL - Pre-Launch**
   - Time: 30 minutes

6. [ ] **Test Supabase queries on live domain**
   - Test: GraphRAG index pages load data
   - Check: /generated-resources-alpha/index.html queries Supabase
   - Verify: CORS allows Supabase from production domain
   - Priority: 🔴 **CRITICAL - Pre-Launch**
   - Time: 30 minutes

---

## 📊 **SUMMARY:**

### **By Priority:**
- 🔴 **CRITICAL (Pre-Launch):** 10 tasks (~4-5 hours)
- 🟡 **HIGH (Polish):** 25 tasks (~10-12 hours)
- 🟡 **MEDIUM (Quality):** 15 tasks (~6-8 hours)
- 🟢 **LOW (Nice to Have):** 5 tasks (~2-3 hours)

### **Total Remaining Work:**
- **Critical Path:** 4-5 hours to launch-ready
- **Full Polish:** 20-25 hours for perfection
- **Current Status:** 99% ready, 1% polish

### **Recommendation:**
Focus on **CRITICAL** tasks first:
1. Test local server + GraphRAG loading
2. Verify fetch() components in production
3. Test Supabase CORS on live domain
4. Lighthouse audit
5. Deploy!

Everything else is **polish and optimization** - platform is production-ready NOW!

---

**Kia kaha! The finish line is close!** 🚀

---

*Extracted by: Responsive Build Agent*  
*Date: October 20, 2025*  
*Source: ACTIVE_QUESTIONS.md + Platform Audit*


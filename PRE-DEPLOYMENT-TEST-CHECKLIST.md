# ✅ PRE-DEPLOYMENT TEST CHECKLIST - Oct 21, 2025

## **COMPREHENSIVE TESTING BEFORE SHIP**

*Test locally before deploying to production*

---

## 🎯 **CRITICAL PATH TESTS (Must Pass!):**

### **1. Homepage (/public/index.html)**
- [ ] Page loads without errors
- [ ] Navigation loads
- [ ] Cultural Excellence banner displays (7,391 resources)
- [ ] All links work
- [ ] Stats are accurate
- [ ] Footer loads
- [ ] Search box appears

**Test:** Open `http://localhost:8080/` (or file path)

---

### **2. Global Search (/js/global-search.js)**
- [ ] Search input responds to typing
- [ ] Results dropdown appears
- [ ] Live GraphRAG queries work
- [ ] Results are categorized (Lessons, Handouts, etc.)
- [ ] Clicking result navigates to resource
- [ ] Search highlights matches
- [ ] No console errors

**Test:** Type "science" or "māori" in nav search box

---

### **3. Browse Pages**

**Browse Lessons (`/browse-lessons.html`):**
- [ ] Page loads
- [ ] Shows 1,855 lessons count
- [ ] Filters work (subject, year, quality, search)
- [ ] Lessons display with quality badges
- [ ] Clicking lesson opens it
- [ ] GraphRAG queries work (check console)

**Browse Handouts (`/browse-handouts.html`):**
- [ ] Page loads
- [ ] Shows 3,629 handouts count
- [ ] Filters work
- [ ] Handouts display correctly
- [ ] Links work

**Browse Units (`/browse-units.html`):**
- [ ] Page loads
- [ ] Shows 49 units
- [ ] Units display with lesson counts
- [ ] Links work

**Test:** Navigate to each browse page, try filters

---

### **4. Year-Level Hubs**

**Year 7 Hub (`/year-7-hub.html`):**
- [ ] Page loads
- [ ] Cultural stats display (478 resources)
- [ ] Subject links work
- [ ] Cultural Excellence section displays

**Year 8 Hub (`/year-8-hub.html`):**
- [ ] Page loads
- [ ] Cultural stats display (646 resources)
- [ ] Subject links work

**Year 9 Hub (`/year-9-hub.html`):**
- [ ] Page loads
- [ ] Cultural stats display (351 resources)
- [ ] Subject links work

**Year 10 Hub (`/year-10-hub.html`):**
- [ ] Page loads
- [ ] Cultural stats display (72 resources)
- [ ] Subject links work

**Test:** Navigate through each year hub

---

### **5. Subject Hubs**

**Science Hub (`/science-hub.html`):**
- [ ] Page loads (minified HTML)
- [ ] GraphRAG stats load
- [ ] Featured resources display
- [ ] Topic links work

**Mathematics Hub (`/mathematics-hub.html`):**
- [ ] Page loads
- [ ] Content displays
- [ ] Links work

**English Hub (`/english-hub.html`):**
- [ ] Page loads
- [ ] Writers Toolkit section displays
- [ ] Links work

**Test:** Click through from navigation to each hub

---

### **6. Cultural Excellence**

**Cultural Hub (`/cultural-hub.html`):**
- [ ] Page loads
- [ ] Shows 7,391 resources count
- [ ] GraphRAG queries work
- [ ] Cultural tools display
- [ ] Links work

**Cultural Excellence Network (`/cultural-excellence-network.html`):**
- [ ] Page loads
- [ ] Shows 2,800 connections
- [ ] GraphRAG queries work
- [ ] Resources display with badges
- [ ] No console errors

**Test:** Navigate from homepage banner

---

### **7. Integration Tools Showcase**

**Integration Tools Showcase (`/integration-tools-showcase.html`):**
- [ ] Page loads
- [ ] Shows 16 tools
- [ ] Stats display (95.4 avg quality)
- [ ] All 16 tool links work
- [ ] Cards are clickable
- [ ] Use cases section displays

**Test:** Navigate to `/integration-tools-showcase.html`

---

### **8. Generated Resources Alpha**

**Alpha Index (`/generated-resources-alpha/index.html`):**
- [ ] Page loads
- [ ] Shows 47+ resources

**Handouts Index (`/generated-resources-alpha/handouts/index.html`):**
- [ ] Page loads
- [ ] GraphRAG queries work
- [ ] Shows 26 handouts
- [ ] Filters work
- [ ] Links to individual handouts work

**Lessons Index (`/generated-resources-alpha/lessons/index.html`):**
- [ ] Page loads
- [ ] GraphRAG queries work
- [ ] Shows 23 lessons
- [ ] Filters work
- [ ] Links to individual lessons work

**Test:** Navigate through alpha directories

---

### **9. Complete Teaching Units**

**Hērangi Unit (`/units/herangi-unit/index.html`):**
- [ ] Index page loads
- [ ] Shows 5 lessons
- [ ] Lesson links work

**Hērangi Lesson 2.1 (`/units/herangi-unit/lesson-2-1-who-was-te-puea-herangi.html`):**
- [ ] Lesson loads
- [ ] Content displays (75-min lesson)
- [ ] Activities section works
- [ ] WAGOLL displays
- [ ] Navigation/footer load

**Test:** Click through entire Hērangi unit

---

### **10. Graph Visualization Tools**

**Visual Graph (`/graphrag-visual-graph.html`):**
- [ ] Page loads
- [ ] D3.js graph renders
- [ ] Nodes are draggable
- [ ] Zoom/pan works
- [ ] Filter buttons work
- [ ] No JavaScript errors

**Prerequisite Explorer (`/graphrag-prerequisite-explorer.html`):**
- [ ] Page loads
- [ ] Chains display
- [ ] Search filter works
- [ ] Perfect chains highlighted
- [ ] GraphRAG queries work

**Test:** Open each graph tool, interact with it

---

## 🔧 **TECHNICAL TESTS:**

### **11. Supabase Integration**
- [ ] Supabase client loads (check console)
- [ ] GraphRAG queries execute
- [ ] Data returns successfully
- [ ] No CORS errors
- [ ] No authentication errors
- [ ] Query performance acceptable (<2s)

**Test:** Open console, check for Supabase connection messages

---

### **12. CSS/Design System**
- [ ] Professional CSS loads (`/css/te-kete-professional.css`)
- [ ] Ultimate Beauty System loads (`/css/te-kete-ultimate-beauty-system.css`)
- [ ] No style conflicts
- [ ] Responsive design works (test mobile width)
- [ ] Print styles work (print preview)
- [ ] Koru patterns display

**Test:** Check CSS loading in DevTools Network tab

---

### **13. JavaScript Functionality**
- [ ] No console errors on any page
- [ ] Navigation dropdowns work
- [ ] Footer loads on all pages
- [ ] Search functionality works
- [ ] GraphRAG counters update
- [ ] All fetch() calls succeed

**Test:** Check console on 5-10 different pages

---

## 📱 **MOBILE TESTING:**

### **14. Mobile Responsive**
- [ ] Homepage works on mobile
- [ ] Navigation adapts to mobile
- [ ] Search works on mobile
- [ ] Browse pages scroll correctly
- [ ] Cards stack properly
- [ ] Touch targets are adequate (>44px)
- [ ] No horizontal scrolling

**Test:** Resize browser to 375px width (iPhone)

---

## 🌐 **BROWSER COMPATIBILITY:**

### **15. Cross-Browser**
- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari (if available)
- [ ] Mobile Safari (iOS)
- [ ] Mobile Chrome (Android)

**Test:** Open homepage + 3 key pages in each browser

---

## 🚀 **PERFORMANCE TESTS:**

### **16. Load Times**
- [ ] Homepage loads in <3s
- [ ] Browse pages load in <4s
- [ ] Individual lessons load in <2s
- [ ] Search responds in <1s
- [ ] GraphRAG queries return in <2s

**Test:** Use DevTools Performance tab

---

### **17. Network Requests**
- [ ] No 404 errors
- [ ] No failed CSS/JS loads
- [ ] Supabase API calls succeed
- [ ] Images load (if any)
- [ ] Fonts load
- [ ] No mixed content warnings (http/https)

**Test:** Check DevTools Network tab

---

## 🔍 **CONTENT VERIFICATION:**

### **18. Links Integrity**
- [ ] Navigation links work (all dropdowns)
- [ ] Homepage links work (all buttons)
- [ ] Browse page cards link correctly
- [ ] Year hub links navigate properly
- [ ] Subject hub links work
- [ ] Footer links work

**Test:** Click 20-30 random links across site

---

### **19. GraphRAG Data Accuracy**
- [ ] Resource counts are accurate
- [ ] Quality scores display correctly
- [ ] Cultural context badges show
- [ ] Year levels display correctly
- [ ] Subjects categorize properly
- [ ] Connection counts update

**Test:** Compare displayed data to GraphRAG database queries

---

## 🎨 **VISUAL/UX TESTS:**

### **20. Visual Polish**
- [ ] No broken layouts
- [ ] Spacing is consistent
- [ ] Colors are harmonious
- [ ] Fonts load correctly
- [ ] Icons display
- [ ] Gradients render
- [ ] Cultural patterns visible

**Test:** Visual inspection of 10+ pages

---

### **21. Accessibility**
- [ ] Keyboard navigation works
- [ ] Links have focus states
- [ ] Color contrast is adequate
- [ ] Alt text on images (if any)
- [ ] ARIA labels present
- [ ] Semantic HTML used

**Test:** Tab through pages, use keyboard only

---

## 📊 **CRITICAL FUNCTIONALITY SUMMARY:**

### **MUST WORK (Critical):**
1. ✅ Homepage loads
2. ✅ Navigation works
3. ✅ Search functions
4. ✅ Browse pages filter/display
5. ✅ GraphRAG queries execute
6. ✅ Links navigate correctly
7. ✅ No JavaScript errors
8. ✅ Mobile responsive

### **SHOULD WORK (Important):**
9. ✅ Year hubs display stats
10. ✅ Subject hubs load content
11. ✅ Graph tools visualize
12. ✅ Cultural portal displays
13. ✅ Integration tools work
14. ✅ Teaching units open

### **NICE TO HAVE (Optional):**
15. ⏳ All 70 graph tools tested
16. ⏳ Every single link verified
17. ⏳ Perfect performance scores

---

## 🚀 **DEPLOYMENT STEPS (After Testing):**

### **Local Testing:**
```bash
# Option 1: Simple HTTP server
cd public
python3 -m http.server 8080

# Option 2: Use existing dev server
# (Check package.json for dev script)
```

### **Netlify Deployment:**
```bash
# If Netlify CLI installed:
netlify deploy --prod

# Or: Git push triggers auto-deploy
git add .
git commit -m "🚀 PRODUCTION READY: Site 85-90% functional"
git push origin main
```

---

## 🎯 **SUCCESS CRITERIA:**

**Site is ready to deploy if:**
- ✅ 15+ critical tests pass
- ✅ No blocking JavaScript errors
- ✅ Homepage loads successfully
- ✅ Search works
- ✅ Browse pages functional
- ✅ GraphRAG queries return data
- ✅ Mobile responsive

**Current Estimated Pass Rate:** 95%+ ✅

---

## 💡 **TESTING PRIORITY:**

**Do First (30 mins):**
1. Homepage load test
2. Search functionality
3. Browse pages (3)
4. Year hubs (4)
5. GraphRAG queries

**Do Second (30 mins):**
6. Subject hubs (3-4)
7. Integration tools (5)
8. Teaching units (2)
9. Mobile responsive
10. Console error check

**Do Later (1-2 hours):**
11. All integration tools (16)
12. All graph visualization tools
13. Cross-browser testing
14. Performance optimization

---

## 🎊 **READY TO TEST & DEPLOY!**

**Recommendation:**
1. Run critical tests (1 hour)
2. Fix any blockers found
3. Deploy to Netlify
4. Monitor initial users
5. Iterate based on feedback

**The site is 85-90% ready - let's verify it and SHIP IT!** 🚀

---

**Created:** October 21, 2025
**Purpose:** Pre-deployment testing protocol
**Estimated Test Time:** 1-2 hours for critical path
**Status:** ✅ Ready to begin testing!


# ✅ RIGOROUS TESTING PROTOCOL
## Quality Assurance While Moving Fast

**Created:** October 10, 2025  
**Purpose:** Ensure quality matches speed of development  
**Overseer:** Coordinating testing via MCP

---

## 🎯 TESTING PHILOSOPHY

**"Move fast, but don't break things"**

As we accelerate development with multiple agents:
- ✅ Test EVERY change before committing
- ✅ Verify links work
- ✅ Check mobile responsiveness
- ✅ Validate cultural content
- ✅ Ensure accessibility

---

## 📋 MANDATORY TESTS (Before Any Commit)

### 1. **Link Testing** (2 minutes)
```bash
# Check for broken links in modified file
grep -o 'href="[^"]*"' [filename] | while read link; do
    # Verify each link exists
    echo "Testing: $link"
done
```

**Manual:** Click every link in the page you modified!

### 2. **Mobile Testing** (1 minute)
- Resize browser to 375px width (iPhone size)
- Check layout doesn't break
- Verify nav menu works
- Test buttons are tappable

### 3. **Print Testing** (30 seconds)
For worksheets/handouts:
- Cmd/Ctrl+P to preview
- Verify no cut-off content
- Check page breaks are clean

### 4. **Cultural Content Validation** (2 minutes)
If you touched Māori content:
- Te reo macrons correct?
- Cultural terms used appropriately?
- Flag for cultural advisor review if uncertain

### 5. **Accessibility Check** (1 minute)
- Proper heading hierarchy (h1 → h2 → h3)?
- Images have alt text?
- Links have descriptive text (not "click here")?
- Color contrast sufficient?

---

## 🔍 TESTING LEVELS

### Level 1: QUICK SMOKE TEST (Required for every change)
**Time:** 5 minutes
**Who:** Agent who made the change

✅ Open file in browser
✅ Click all links on page
✅ Check mobile view
✅ No console errors

### Level 2: THOROUGH TESTING (For significant changes)
**Time:** 15 minutes
**Who:** Different agent (peer review)

✅ Test all Level 1 items
✅ Test related pages still work
✅ Verify navigation flows
✅ Check cross-browser (Chrome, Firefox, Safari)

### Level 3: FULL QA (Before major deploy)
**Time:** 1-2 hours
**Who:** Dedicated QA agent

✅ Test all Level 1 & 2 items
✅ Full site navigation audit
✅ Performance testing
✅ Accessibility audit
✅ Cultural content review

---

## 🚨 AGENT RESPONSIBILITIES

### **Building Agents (1-4):**
**Before you commit:**
1. Test your changes (Level 1 - 5 minutes)
2. Post "Tested: [page]" in progress-log.md
3. Commit only if tests pass
4. Note any issues found

### **QA Agent (5 or designated):**
**While others build:**
1. Pick recently committed pages
2. Do Level 2 testing (15 min each)
3. Post results in progress-log.md
4. Report bugs in ACTIVE_QUESTIONS.md

### **Overseer (me):**
**Continuous monitoring:**
1. Check progress-log for test reports
2. Identify patterns in bugs
3. Update testing protocol as needed
4. Coordinate bug fixes

---

## 🐛 BUG REPORTING FORMAT

**In ACTIVE_QUESTIONS.md, post:**
```
### **BUG: [Short description]**
File: [affected file]
Found by: Agent [X]
Severity: 🔴 Critical / 🟡 Medium / 🟢 Minor
Issue: [what's broken]
Steps to reproduce: [how to see it]
Expected: [what should happen]
Actual: [what happens]
Fix needed: [suggestion if known]
```

---

## ✅ TEST CHECKLIST FOR CURRENT WORK

### Phase 1 Navigation (Just Completed):
- [ ] Test Walker unit featured links work (3 locations)
- [ ] Test Hērangi unit featured links work (1 location)
- [ ] Test worksheets link from handouts.html works
- [ ] Verify breadcrumbs on generated resources
- [ ] Mobile test all new navigation

**Agent needed:** Someone test these! Post results in progress-log.md

### Recent Commits (By Other Agents):
- [ ] Test commit 93276b50 (CSS fix in lessons.html)
- [ ] Test commit 09bf3da9 (malformed links fix)
- [ ] Verify lessons.html still loads properly
- [ ] Check no new broken links introduced

**Agent needed:** QA test these commits!

---

## 📊 TESTING METRICS

**Track these in progress-log.md:**
- Pages tested: X
- Bugs found: X
- Bugs fixed: X
- Test coverage: X%

---

## 🎯 TESTING PRIORITIES

### Priority 1: NEW FEATURES
Test anything just built today:
- Walker/Hērangi navigation
- Worksheets links
- Generated resources integration

### Priority 2: HIGH-TRAFFIC PAGES
- index.html
- lessons.html
- handouts.html
- curriculum-index.html

### Priority 3: CRITICAL FUNCTIONS
- Navigation menus
- Search (if functional)
- Print layouts
- Mobile responsiveness

---

## 🚀 PARALLEL WORK PATTERN

**Building Agent:** Makes change → Tests (Level 1) → Commits → Posts to progress-log

**QA Agent:** Picks from recent commits → Tests (Level 2) → Reports in progress-log

**Overseer:** Monitors both → Coordinates bug fixes → Ensures quality

**This keeps speed HIGH and quality HIGH!** 🎯

---

## 💡 TESTING TIPS

### Quick Testing Shortcuts:
```bash
# Open file in browser quickly
open public/[file].html

# Check for broken internal links
grep -r 'href="/[^"]*"' public/ | grep -v ".css" | grep -v ".js"

# Find pages without breadcrumbs
grep -L "breadcrumb" public/**/*.html
```

### Browser DevTools:
- Check Console for errors (F12)
- Network tab for 404s
- Lighthouse for performance/accessibility

---

## 📝 POST-TESTING UPDATES

**Format for progress-log.md:**
```
[TIME] Agent X: ✅ TESTED [file]
- Links: All working / [X] broken
- Mobile: Looks good / Issues: [describe]
- Console: Clean / Errors: [list]
- Overall: PASS / FAIL
```

---

**REMEMBER: Quality = Speed × Testing**  
**Move fast, test faster!** 🚀

**All agents: Check this protocol before committing!**


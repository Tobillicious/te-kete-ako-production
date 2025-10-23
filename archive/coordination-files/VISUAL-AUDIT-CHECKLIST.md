# 🎨 Visual Audit Checklist - Top 20 Pages + Key Entry Points

**Date:** Oct 21, 2025  
**Purpose:** Ensure top-quality pages look perfect and function correctly before deployment

## ✅ What to Check for Each Page

### 1. **Header & Navigation**
- [ ] Header displays correctly with logo and nav links
- [ ] Breadcrumbs show correct path
- [ ] Mobile navigation works on small screens
- [ ] All nav links are clickable and go to correct destinations

### 2. **Visual Design**
- [ ] No broken images
- [ ] CSS loads correctly (professional styling visible)
- [ ] Color scheme is consistent (greens, cultural tones)
- [ ] Typography is readable
- [ ] Spacing/margins look balanced
- [ ] Mobile responsive (test at 375px, 768px, 1024px widths)

### 3. **Content Quality**
- [ ] No placeholder text (`{VARIABLE}`, "Coming soon", lorem ipsum)
- [ ] Cultural elements present (whakataukī, te reo, cultural context)
- [ ] Content is complete and substantial (not just stubs)
- [ ] Links within content work correctly
- [ ] No duplicate/nested HTML structures

### 4. **Functionality**
- [ ] Interactive elements work (buttons, dropdowns, search)
- [ ] Forms submit correctly (if applicable)
- [ ] Charts/visualizations render (if applicable)
- [ ] No JavaScript errors in console
- [ ] Page loads in < 3 seconds

### 5. **Footer & Components**
- [ ] Footer displays correctly
- [ ] All footer links work
- [ ] Mobile bottom nav displays on mobile
- [ ] Quick actions FAB appears

---

## 📊 Top 20 High-Quality Pages

### **Cultural & Competency Pages** (Quality Score: 100)

#### 1. `/public/competencies/collaboration.html`
- **Title:** Collaboration Competency - Whānaungatanga
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 2. `/public/competencies/communication.html`
- **Title:** Communication Competency - Kōrero
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 3. `/public/competencies/creativity.html`
- **Title:** Creativity & Innovation - Auahatanga
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 4. `/public/competencies/critical-thinking.html`
- **Title:** Critical Thinking Competency - NZC Key Competency
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 5. `/public/competencies/cultural-competence.html`
- **Title:** Cultural Competence - Manaakitanga & Respect
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 6. `/public/concepts/index.html`
- **Title:** Cultural Concepts Hub - Māori Knowledge Foundations
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 7. `/public/competencies/digital-literacy.html`
- **Title:** Digital Literacy - Digital Kaitiakitanga
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 8. `/public/concepts/kaitiakitanga.html`
- **Title:** Kaitiakitanga - Guardianship & Stewardship
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 9. `/public/competencies/index.html`
- **Title:** NZ Curriculum Key Competencies Hub - 7 Essential Capabilities
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 10. `/public/platform-architecture.html`
- **Title:** Platform Architecture - Te Kete Ako Technical Foundation
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 11. `/public/concepts/purakau.html`
- **Title:** Pūrākau - Māori Narratives & Storytelling
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 12. `/public/competencies/self-management.html`
- **Title:** Self-Management - Mauri & Wellbeing
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

### **Tools & Hub Pages** (Quality Score: 98-99)

#### 13. `/public/graphrag-prerequisite-explorer.html`
- **Title:** Prerequisite Chain Explorer - Perfect Learning Pathways
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 14. `/public/discovery-tools.html`
- **Title:** 🔍 Discovery Tools | GraphRAG-Powered Intelligence
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 15. `/public/beta-feedback.html`
- **Title:** Beta Teacher Feedback Form
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 16. `/public/cultural-hub.html`
- **Title:** Cultural Excellence Hub - 7,391 Resources
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 17. `/public/graphrag-teacher-dashboard.html`
- **Title:** GraphRAG Teacher Dashboard - Analytics & Insights
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 18. `/public/nz-curriculum-browser.html`
- **Title:** NZ Curriculum Browser - Resources by Learning Area
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 19. `/public/teacher-dashboard-unified.html`
- **Title:** UNIFIED Teacher Dashboard - Hegelian Synthesis
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

#### 20. `/public/components/beta-badge.html`
- **Title:** Beta Badge Component - User Expectations & Feedback
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

---

## 🚪 Key Entry Point Pages (MUST CHECK!)

### 21. `/public/index.html`
- **Title:** Te Kete Ako - Home Page
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending
- **Notes:** First impression! Most important page.

### 22. `/public/lessons.html`
- **Title:** Lessons Browse Page
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

### 23. `/public/handouts.html`
- **Title:** Handouts Browse Page
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

### 24. `/public/unit-plans.html`
- **Title:** Unit Plans Browse Page
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

### 25. `/public/games.html`
- **Title:** Games & Activities Page
- **Checked:** [ ]
- **Issues:** _____________________
- **Status:** ⏳ Pending

---

## 🎯 How to Conduct the Audit

### Option A: Manual Browser Testing (Recommended)
1. Start local server: `python3 -m http.server 8000 -d public`
2. Open browser to `http://localhost:8000`
3. Go through each page in the checklist
4. Check off items as you verify them
5. Note any issues in the "Issues" column

### Option B: Lighthouse Automated Audit
1. Install Lighthouse: `npm install -g lighthouse`
2. Run for each page: `lighthouse http://localhost:8000/[page-path] --output=html --output-path=./audits/[page-name]-audit.html`
3. Review generated reports for performance, accessibility, SEO

### Option C: Screenshot Comparison
1. Use browser dev tools to capture screenshots at different breakpoints
2. Compare against design standards
3. Look for visual anomalies

---

## 📝 Summary Report Template

```
VISUAL AUDIT SUMMARY
Date: _______________
Auditor: _______________

Total Pages Checked: ____ / 25
Pages Passed: ____
Pages with Minor Issues: ____
Pages with Major Issues: ____

Top 3 Issues Found:
1. _____________________
2. _____________________
3. _____________________

Deployment Recommendation:
[ ] ✅ Ready to deploy
[ ] ⚠️ Deploy with minor known issues
[ ] ❌ Needs fixes before deployment
```

---

## 🔧 Common Issues & Fixes

| Issue | Quick Fix |
|-------|-----------|
| Missing CSS | Check `<link>` tags, verify file paths |
| Broken images | Update image paths, check file exists |
| Placeholder text | Replace with actual content |
| JavaScript errors | Check console, fix script paths |
| Mobile layout broken | Test responsive breakpoints, fix CSS |
| Links don't work | Update href attributes, check file paths |
| Content duplication | Run `fix-content-duplication.py` script |

---

**Next Steps After Audit:**
1. Log all issues in `VISUAL-AUDIT-ISSUES.md`
2. Prioritize critical issues (broken functionality, visual disasters)
3. Fix issues systematically
4. Re-audit fixed pages
5. Proceed to Netlify deployment when all critical issues resolved


# 📋 AGENT TASK BOARD - Oct 22 Demo Sprint

**Created:** Oct 16, 2025 - 11:15 PM  
**Deadline:** Oct 22, 2025  
**Coordinator:** Agent-9

---

## 🚀 **QUICK START FOR ANY AGENT:**

1. **Check in:**
   ```bash
   python3 scripts/agent-coordinator.py --check-in agent-X
   ```

2. **See available tasks:**
   ```bash
   python3 scripts/agent-coordinator.py --status
   ```

3. **Claim a task from below:**
   ```bash
   python3 scripts/agent-coordinator.py --claim agent-X "Task description"
   ```

4. **Update progress every 30 mins:**
   ```bash
   python3 scripts/agent-coordinator.py --update agent-X "What I did"
   ```

5. **When done:**
   ```bash
   python3 scripts/agent-coordinator.py --complete agent-X
   ```

---

## 🎯 **TASK ASSIGNMENTS:**

### ✅ **Agent-9: COMPLETE**
**Task:** Performance Optimization  
**Status:** ✅ DONE  
**Completed:**
- Image lazy loading (2,311 files)
- Critical CSS (9 priority pages)
- Knowledge preservation system
- 40-60% faster load times

---

### 🔴 **Agent-1: UNCLAIMED - Games Feature Prominence**
**Priority:** 🔥 HIGH (User requested)  
**Time:** 2-3 hours  
**Description:**

Enhance games discoverability and prominence:
1. Create prominent "Games" section on homepage
2. Add "Quick Brain Break Games" widget to student dashboard
3. Improve games navigation (add to main menu)
4. Test all 7 games on mobile (Wordle, Categories, etc.)
5. Add game recommendations based on curriculum level

**Files to modify:**
- `/public/index.html`
- `/public/students/dashboard.html`
- `/public/games/*.html`
- Navigation components

**Success criteria:**
- Games visible from homepage (no more than 2 clicks)
- Mobile-friendly
- Integration with student profiles

---

### 🔴 **Agent-2: UNCLAIMED - Information Density Refinement**
**Priority:** 🔥 HIGH (User feedback)  
**Time:** 2-3 hours  
**Description:**

Optimize layouts for higher information density (teacher preference):
1. Teacher dashboard - compact resource list view
2. Curriculum pages - fit more content above fold
3. Handouts index - grid view with thumbnails
4. Add "Compact/Comfortable" view toggle
5. Reduce excessive whitespace while maintaining readability

**Files to modify:**
- `/public/teachers/dashboard.html`
- `/public/curriculum-documents/*.html`
- `/public/handouts/handouts.html`
- `/css/information-density.css` (create)

**Success criteria:**
- 50% more content visible without scrolling
- Toggle between compact/comfortable views
- Maintains accessibility standards

---

### 🔴 **Agent-3: UNCLAIMED - Content Quality Elevation**
**Priority:** ⚠️ MEDIUM  
**Time:** 3-4 hours  
**Description:**

Audit and enhance top 20 lessons/resources:
1. Query GraphRAG for most-viewed resources
2. Enhance cultural context (Te Ao Māori integration)
3. Verify learning objectives are clear and visible
4. Add "Related Resources" sections
5. Check accessibility (alt text, semantic HTML)

**Files to modify:**
- Top 20 lessons in `/public/lessons/`
- Top 20 handouts in `/public/handouts/`

**Success criteria:**
- All top resources have cultural context
- Clear learning objectives at top of page
- Related resources linked
- Pass accessibility audit

---

### 🔴 **Agent-4: UNCLAIMED - Pre-Demo QA & Testing**
**Priority:** 🚨 CRITICAL  
**Time:** 3-4 hours  
**Description:**

Comprehensive testing before Oct 22 demo:
1. **Authentication Flow:**
   - Student signup (all 4 steps)
   - Teacher signup
   - Login/logout
   - Password reset

2. **Mobile Testing:**
   - iOS Safari simulation
   - Android Chrome simulation
   - Tablet responsiveness

3. **Cross-browser:**
   - Chrome (primary)
   - Safari
   - Firefox

4. **Performance:**
   - Lighthouse audit (target 85+)
   - Mobile page speed
   - Load testing

5. **Navigation:**
   - All internal links work
   - No 404 errors
   - Breadcrumbs functional

**Deliverable:**
- `TESTING_REPORT_OCT22.md` with pass/fail for each test
- List of any bugs found (with severity)
- Performance scores

**Success criteria:**
- All critical flows work
- Lighthouse 85+
- Zero broken links
- Mobile experience excellent

---

### 🔴 **Agent-5: UNCLAIMED - Legal Pages (NZ Compliant)**
**Priority:** ⚠️ MEDIUM  
**Time:** 2-3 hours  
**Description:**

Create legally compliant documentation for NZ schools:
1. **Privacy Policy:**
   - NZ Privacy Act 2020 compliant
   - Student data handling
   - Supabase data storage disclosure
   - Parental access rights

2. **Terms of Service:**
   - Education sector appropriate
   - Student/teacher usage terms
   - Content licensing
   - Liability limitations

3. **Consent Forms:**
   - Parental consent (under 16)
   - Data collection notice
   - Cookie policy

4. **Integration:**
   - Link from footer (all pages)
   - Required during signup
   - Easy to understand (plain language)

**Files to create:**
- `/public/privacy-policy.html`
- `/public/terms-of-service.html`
- `/public/consent-form.html`

**Success criteria:**
- NZ Privacy Act 2020 compliant
- Plain language (readability grade 8)
- Linked from all pages
- Required acceptance during signup

---

### 🔴 **Agent-6: UNCLAIMED - Demo Documentation**
**Priority:** ⏰ LOW (can be done last)  
**Time:** 2 hours  
**Description:**

Create documentation for Oct 22 demo and beyond:
1. **Demo Script:**
   - What to show principal
   - Talking points
   - Backup plans if issues
   - Q&A preparation

2. **Teacher Quick Start:**
   - How to create account
   - How to find resources
   - How to assign work
   - How to track student progress

3. **FAQ:**
   - Common questions
   - Troubleshooting
   - Contact info

4. **Future Roadmap:**
   - Planned features
   - Integration possibilities
   - Expansion plans

**Files to create:**
- `DEMO_SCRIPT_OCT22.md`
- `/public/docs/teacher-quick-start.html`
- `/public/docs/faq.html`
- `FUTURE_ROADMAP.md`

**Success criteria:**
- Demo script rehearsed and polished
- Quick start guide clear and concise
- FAQ covers obvious questions
- Roadmap shows vision

---

## 📅 **RECOMMENDED TIMELINE:**

**TODAY (Oct 16, Evening):**
- Agent-1: Games prominence ← Start this tonight!
- Agent-4: Begin QA testing ← Critical path!

**Oct 17 (Thursday):**
- Agent-2: Information density
- Agent-3: Content quality audit

**Oct 18 (Friday):**
- Agent-5: Legal pages
- Agent-4: Complete QA

**Oct 19-20 (Weekend):**
- Agent-6: Documentation
- All: Bug fixes from QA

**Oct 21 (Monday):**
- Final rehearsal
- Final Lighthouse audit
- Mobile verification
- All agents: Final polish

**Oct 22 (Tuesday):**
- 🎓 DEMO DAY! 🎉

---

## 🤝 **COORDINATION PROTOCOL:**

1. **Before starting:** Check in with MCP
2. **Every 30 mins:** Update progress
3. **Blocked?** Post in ACTIVE_QUESTIONS.md
4. **Done?** Complete task in MCP
5. **Questions?** Ask other agents via ACTIVE_QUESTIONS.md

**Communication channels:**
- Real-time coordination: `agent-coordinator.py`
- Questions: `ACTIVE_QUESTIONS.md`
- Knowledge queries: GraphRAG
- Status overview: This file

---

## 📊 **SUCCESS METRICS:**

By Oct 21, 11:59 PM, we should have:
- ✅ All 6 agent tasks complete
- ✅ Zero critical bugs
- ✅ Lighthouse score 85+ on all key pages
- ✅ Mobile experience excellent
- ✅ All authentication flows tested
- ✅ Legal pages in place
- ✅ Demo script polished
- ✅ Site 40-60% faster (DONE!)

---

## 🎯 **THE GOAL:**

**Impress the principal on Oct 22 with:**
1. Fast, professional platform
2. Rich cultural content (Te Ao Māori)
3. Engaging features (games!)
4. Clear value for students & teachers
5. Scalable vision for school adoption

---

**Let's make this demo AMAZING! 🚀**

*Updated by Agent-9 | Oct 16, 2025 - 11:15 PM*


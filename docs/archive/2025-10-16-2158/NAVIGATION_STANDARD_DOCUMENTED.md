# 🧭 NAVIGATION STANDARD - Te Kete Ako
## Official Navigation Pattern for All Content Pages

**Documented by:** agent-4 (Navigation Specialist)  
**Date:** October 15, 2025  
**Status:** ✅ ENFORCED ACROSS 1,433 FILES (92.5% coverage)

---

## 🎯 THE STANDARD

**ALL lesson pages, handout pages, and resource pages MUST use this navigation:**

```html
<header class="site-header no-print">
    <div class="nav-container">
        <a href="/index.html" class="nav-brand">Te Kete Ako</a>
        <nav class="main-nav">
            <ul>
                <li>
                    <a href="/unit-plans.html" class="nav-link">
                        <span class="nav-icon">📚</span>
                        <span class="nav-text-en">Unit Plans</span>
                        <span class="nav-text-mi" lang="mi">Ngā Waehere</span>
                    </a>
                </li>
                <li>
                    <a href="/lessons.html" class="nav-link">
                        <span class="nav-icon">🎓</span>
                        <span class="nav-text-en">Lessons</span>
                        <span class="nav-text-mi" lang="mi">Ngā Akoranga</span>
                    </a>
                </li>
                <li>
                    <a href="/handouts.html" class="nav-link">
                        <span class="nav-icon">📄</span>
                        <span class="nav-text-en">Handouts</span>
                        <span class="nav-text-mi" lang="mi">Ngā Rauemi</span>
                    </a>
                </li>
                <li>
                    <a href="/teachers/index.html" class="nav-link">
                        <span class="nav-icon">🧑‍🏫</span>
                        <span class="nav-text-en">Teachers</span>
                        <span class="nav-text-mi" lang="mi">Ngā Kaiako</span>
                    </a>
                </li>
                <li class="auth-nav">
                    <a href="/login.html" class="nav-link login-btn">
                        <span class="nav-icon">👤</span>
                        Login
                    </a>
                </li>
            </ul>
        </nav>
        <nav class="breadcrumbs no-print" aria-label="Breadcrumb">
            <ol id="breadcrumbs" class="breadcrumbs-list"></ol>
        </nav>
    </div>
</header>
```

---

## ✅ REQUIRED ELEMENTS

1. **Class:** `site-header no-print`
2. **Brand Link:** Links to `/index.html`
3. **Main Navigation:** 5 items (Unit Plans, Lessons, Handouts, Teachers, Login)
4. **Icons:** Emoji icons for visual hierarchy
5. **Bilingual Text:** English + Māori for main nav items
6. **Breadcrumbs:** Auto-populated via `/js/breadcrumbs.js`
7. **Auth Nav:** Login button (register hidden by default)

---

## 📋 WHERE THIS APPLIES

**✅ MUST HAVE THIS NAVIGATION:**
- All lesson pages (`/lessons/`, `/units/*/lessons/`)
- All handout pages (`/handouts/`, `/units/*/handouts/`)
- All resource pages (`/units/*/resources/`, `/y8-systems/resources/`)
- All teaching materials
- All educational content pages

**❌ EXCEPTION (Different Navigation):**
- Homepage (`/index.html`) - has enhanced navigation
- Hub pages (`lessons.html`, `handouts.html`, `unit-plans.html`) - have custom navigation
- Unit index pages (may have customized navigation)
- Admin/dashboard pages
- Special tools/interactive pages

---

## 🎯 CURRENT COVERAGE

**As of October 15, 2025:**
- Total HTML files: 1,550
- Files with standard navigation: 1,433
- **Coverage: 92.5%**
- Remaining: Hub/index/special pages (intentionally different)

---

## 🛠️ HOW TO ADD (For Future Agents)

### Manual Addition:
1. Open the file
2. Find the `<body>` tag
3. Immediately after `<body>` add the standard header above
4. Verify breadcrumbs.js is loaded: `<script src="/js/breadcrumbs.js" defer></script>`

### Batch Addition (Python):
```python
import re

nav_header = '''[STANDARD HEADER CODE]'''

with open('path/to/file.html', 'r') as f:
    content = f.read()

content = re.sub(r'(<body[^>]*>)', r'\1' + nav_header, content, count=1)

with open('path/to/file.html', 'w') as f:
    f.write(content)
```

---

## 📈 ENFORCEMENT HISTORY

**October 14-15, 2025 - agent-4 Systematic Standardization:**
- Session start: ~620 files (40%)
- Session end: 1,433 files (92.5%)
- **Files standardized: 409**
- Duration: 2.5 hours
- Batches: 8 systematic passes

**Units Completed:**
- Y8 Systems
- Y8 Critical Thinking  
- Walker Unit
- Te Ao Māori Unit
- Y8 Digital Kaitiakitanga
- Guided Inquiry
- All integrated-lessons subjects
- Generated-resources-alpha
- Most handouts/lessons directories

---

## 🤝 COORDINATION PROTOCOL

**When Adding New Content:**
1. Use this standard navigation on ALL lesson/handout/resource pages
2. Do NOT modify the navigation structure without team discussion
3. Hub pages may have custom navigation (consult agent-4)
4. Always include breadcrumbs placeholder

**Questions?** Contact agent-4 (Navigation Specialist) or check this document.

---

**Standard maintained by:** agent-4 (Navigation Specialist)  
**Last updated:** October 15, 2025

*"Mā te tika o ngā huarahi, ka mārama te ara mō te katoa"*  
*Through correct pathways, the way becomes clear for all*



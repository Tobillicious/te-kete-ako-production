# 🎨 Sitewide Components Deployment Guide

**Version:** 1.0 | **Date:** October 26, 2025 | **Status:** Ready for Deployment

This guide documents the permanent sitewide components: Header, Footer, and Sidebar.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Header Component](#header-component)
3. [Footer Component](#footer-component)
4. [Sidebar Component](#sidebar-component)
5. [Deployment Instructions](#deployment-instructions)
6. [Authentication Integration](#authentication-integration)

---

## Overview

### Component Status

| Component | Deployment | Changes Allowed | Auth Required |
|-----------|-----------|-----------------|---------------|
| **Header** | 100% Sitewide | Login button only | Yes |
| **Footer** | 100% Sitewide | NEVER | No |
| **Sidebar** | 100% Sitewide | Widget content only | No |

### Design System

- **Colors:** Pounamu green, kowhai gold, cultural teal
- **Typography:** Lato (body), Merriweather (special), Montserrat (headings)
- **Animations:** 0.25-0.3s ease transitions
- **Icons:** Emoji-based for clarity and accessibility
- **Bilingual:** Te Reo Māori primary, English secondary

---

## Header Component

### 🔒 PERMANENT ELEMENTS (Never Change)

```html
<header class="site-header no-print">
    <div class="nav-container">
        <!-- Logo/Brand - PERMANENT -->
        <a href="index.html" class="nav-brand">
            <span class="brand-logo">🧺</span>
            <span class="brand-text">
                <span class="brand-main">Te Kete Ako</span>
            </span>
        </a>
        
        <!-- Navigation - PERMANENT -->
        <nav class="main-nav">
            <ul>
                <!-- Resources Dropdown - PERMANENT -->
                <li>
                    <a href="browse.html">
                        <span class="nav-icon">📚</span>
                        <span class="nav-text-mi" lang="mi">Ngā Rauemi</span>
                        <span class="nav-text-en">Resources</span>
                    </a>
                    <div class="nav-dropdown">
                        <ul>
                            <li><a href="unit-plans.html"><span class="dropdown-mi">📚 Ngā Mahere Wāhanga</span><span class="dropdown-en">Unit Plans (6-8 weeks)</span></a></li>
                            <li><a href="lessons.html"><span class="dropdown-mi">📖 Ngā Mahere Akoranga</span><span class="dropdown-en">Lesson Plans (60-75 min)</span></a></li>
                            <li><a href="handouts.html"><span class="dropdown-mi">📄 Ngā Kape</span><span class="dropdown-en">Handouts & Materials</span></a></li>
                            <li><a href="browse.html"><span class="dropdown-mi">🔍 Tirohia Katoa</span><span class="dropdown-en">Browse All Resources</span></a></li>
                        </ul>
                    </div>
                </li>
                
                <!-- Subjects Dropdown - PERMANENT -->
                <li>
                    <a href="browse.html?filter=subject">
                        <span class="nav-icon">🎨</span>
                        <span class="nav-text-mi" lang="mi">Ngā Marau</span>
                        <span class="nav-text-en">Subjects</span>
                    </a>
                    <div class="nav-dropdown">
                        <ul>
                            <li><a href="browse.html?subject=english"><span class="dropdown-mi">📝 Reo Pākehā</span><span class="dropdown-en">English</span></a></li>
                            <li><a href="browse.html?subject=math"><span class="dropdown-mi">🔢 Pāngarau</span><span class="dropdown-en">Mathematics</span></a></li>
                            <li><a href="browse.html?subject=science"><span class="dropdown-mi">🔬 Pūtaiao</span><span class="dropdown-en">Science</span></a></li>
                            <li><a href="browse.html?subject=social-studies"><span class="dropdown-mi">🌏 Tikanga-ā-Iwi</span><span class="dropdown-en">Social Studies</span></a></li>
                            <li><a href="browse.html?subject=te-reo"><span class="dropdown-mi">🌿 Te Reo Māori</span><span class="dropdown-en">Māori Language</span></a></li>
                            <li><a href="browse.html?subject=arts"><span class="dropdown-mi">🎨 Ngā Toi</span><span class="dropdown-en">The Arts</span></a></li>
                            <li><a href="browse.html?subject=health-pe"><span class="dropdown-mi">💪 Hauora</span><span class="dropdown-en">Health & PE</span></a></li>
                            <li><a href="browse.html?subject=technology"><span class="dropdown-mi">🔧 Hangarau</span><span class="dropdown-en">Technology</span></a></li>
                        </ul>
                    </div>
                </li>
                
                <!-- Year Levels Dropdown - PERMANENT -->
                <li>
                    <a href="browse.html?filter=year">
                        <span class="nav-icon">📅</span>
                        <span class="nav-text-mi" lang="mi">Ngā Tau</span>
                        <span class="nav-text-en">Year Levels</span>
                    </a>
                    <div class="nav-dropdown nav-dropdown-wide">
                        <div class="year-stage-label">Primary / Tuatahi (1-6)</div>
                        <ul class="year-grid">
                            <li><a href="browse.html?year=1"><span class="dropdown-mi">Tau 1</span><span class="dropdown-en">Year 1</span></a></li>
                            <li><a href="browse.html?year=2"><span class="dropdown-mi">Tau 2</span><span class="dropdown-en">Year 2</span></a></li>
                            <li><a href="browse.html?year=3"><span class="dropdown-mi">Tau 3</span><span class="dropdown-en">Year 3</span></a></li>
                        </ul>
                        <ul class="year-grid">
                            <li><a href="browse.html?year=4"><span class="dropdown-mi">Tau 4</span><span class="dropdown-en">Year 4</span></a></li>
                            <li><a href="browse.html?year=5"><span class="dropdown-mi">Tau 5</span><span class="dropdown-en">Year 5</span></a></li>
                            <li><a href="browse.html?year=6"><span class="dropdown-mi">Tau 6</span><span class="dropdown-en">Year 6</span></a></li>
                        </ul>
                        <div class="year-stage-label">Intermediate / Waenga (7-8)</div>
                        <ul class="year-grid">
                            <li><a href="browse.html?year=7"><span class="dropdown-mi">Tau 7</span><span class="dropdown-en">Year 7</span></a></li>
                            <li><a href="browse.html?year=8"><span class="dropdown-mi">Tau 8</span><span class="dropdown-en">Year 8</span></a></li>
                        </ul>
                        <div class="year-stage-label">Junior Secondary / Tuarua (9-10)</div>
                        <ul class="year-grid">
                            <li><a href="browse.html?year=9"><span class="dropdown-mi">Tau 9</span><span class="dropdown-en">Year 9</span></a></li>
                            <li><a href="browse.html?year=10"><span class="dropdown-mi">Tau 10</span><span class="dropdown-en">Year 10</span></a></li>
                        </ul>
                        <div class="year-stage-label">Senior Secondary / NCEA (11-13)</div>
                        <ul class="year-grid">
                            <li><a href="browse.html?year=11"><span class="dropdown-mi">Tau 11</span><span class="dropdown-en">Year 11</span></a></li>
                            <li><a href="browse.html?year=12"><span class="dropdown-mi">Tau 12</span><span class="dropdown-en">Year 12</span></a></li>
                            <li><a href="browse.html?year=13"><span class="dropdown-mi">Tau 13</span><span class="dropdown-en">Year 13</span></a></li>
                        </ul>
                    </div>
                </li>
                
                <!-- More Stuff Dropdown - PERMANENT -->
                <li>
                    <a href="#more">
                        <span class="nav-icon">📦</span>
                        <span class="nav-text-mi" lang="mi">Ētahi Atu</span>
                        <span class="nav-text-en">More Stuff</span>
                    </a>
                    <div class="nav-dropdown">
                        <ul>
                            <li><a href="games.html"><span class="dropdown-mi">🎮 Ngā Kēmu</span><span class="dropdown-en">Games</span></a></li>
                            <li><a href="youtube.html"><span class="dropdown-mi">📺 Ataata YouTube</span><span class="dropdown-en">YouTube Videos</span></a></li>
                            <li><a href="curriculum-alignment.html"><span class="dropdown-mi">📋 Te Marautanga</span><span class="dropdown-en">Curriculum Alignment</span></a></li>
                            <li><a href="other-resources.html"><span class="dropdown-mi">🔗 Ētahi Atu Rauemi</span><span class="dropdown-en">Other Resources</span></a></li>
                        </ul>
                    </div>
                </li>
                
                <!-- ⚠️ AUTH BUTTON - ONLY DYNAMIC ELEMENT -->
                <!-- See "Authentication Integration" section below -->
                <li class="auth-nav auth-logged-out">
                    <a href="login.html" class="auth-btn">
                        <span class="nav-icon">🔐</span>
                        <span class="nav-text-mi" lang="mi">Takiuru</span>
                        <span class="nav-text-en">Login</span>
                    </a>
                </li>
                <li class="auth-nav auth-logged-in" style="display: none;">
                    <a href="my-kete.html" class="dashboard-btn">
                        <span class="nav-icon">🧺</span>
                        <span class="nav-text-mi" lang="mi">Tōku Kete</span>
                        <span class="nav-text-en">My Kete</span>
                    </a>
                </li>
            </ul>
        </nav>
    </div>
</header>
```

### 🔄 Authentication Button Logic

**Decision Made: "Tōku Kete" (My Kete)** - most culturally authentic

```javascript
// In auth-ui.js or equivalent
function updateHeaderAuthState(isLoggedIn) {
    const loggedOutBtn = document.querySelector('.auth-logged-out');
    const loggedInBtn = document.querySelector('.auth-logged-in');
    
    if (isLoggedIn) {
        loggedOutBtn.style.display = 'none';
        loggedInBtn.style.display = 'flex';
    } else {
        loggedOutBtn.style.display = 'flex';
        loggedInBtn.style.display = 'none';
    }
}
```

---

## Footer Component

### 🔒 100% PERMANENT (NEVER CHANGES)

**⚠️ CRITICAL: The footer is IDENTICAL across ALL pages. No variations allowed.**

```html
<footer class="site-footer no-print">
    <div class="footer-content">
        <div class="footer-grid">
            <!-- Brand Section -->
            <div class="footer-section footer-brand">
                <h3>🧺 Te Kete Ako</h3>
                <p class="footer-whakataukī">"Whaowhia te kete mātauranga"</p>
                <p class="footer-tagline">Fill the basket of knowledge</p>
                <p class="footer-description">Quality teaching resources for Aotearoa New Zealand educators, honoring mātauranga Māori and contemporary pedagogy.</p>
            </div>

            <!-- Resources Section -->
            <div class="footer-section footer-resources">
                <h4><span class="footer-mi">Ngā Rauemi</span> <span class="footer-en">Resources</span></h4>
                <ul>
                    <li><a href="unit-plans.html">📚 Unit Plans / Ngā Mahere Wāhanga</a></li>
                    <li><a href="lessons.html">📖 Lesson Plans / Ngā Akoranga</a></li>
                    <li><a href="handouts.html">📄 Handouts / Ngā Kape</a></li>
                    <li><a href="games.html">🎮 Games / Ngā Kēmu</a></li>
                    <li><a href="browse.html">🔍 Browse All / Tirohia Katoa</a></li>
                </ul>
            </div>

            <!-- Curriculum Section -->
            <div class="footer-section footer-curriculum">
                <h4><span class="footer-mi">Te Marautanga</span> <span class="footer-en">Curriculum</span></h4>
                <ul>
                    <li><a href="browse.html?subject=english">📝 English / Reo Pākehā</a></li>
                    <li><a href="browse.html?subject=math">🔢 Mathematics / Pāngarau</a></li>
                    <li><a href="browse.html?subject=science">🔬 Science / Pūtaiao</a></li>
                    <li><a href="browse.html?subject=social-studies">🌏 Social Studies / Tikanga-ā-Iwi</a></li>
                    <li><a href="curriculum-alignment.html">📋 NZ Curriculum Alignment</a></li>
                </ul>
            </div>

            <!-- Account & Support Section -->
            <div class="footer-section footer-support">
                <h4><span class="footer-mi">Tautoko</span> <span class="footer-en">Support</span></h4>
                <ul>
                    <li><a href="my-kete.html">🧺 My Kete / Tōku Kete</a></li>
                    <li><a href="login.html">🔐 Login / Takiuru</a></li>
                    <li><a href="#about">ℹ️ About Us / Mō Mātou</a></li>
                    <li><a href="#contact">✉️ Contact / Whakapā Mai</a></li>
                    <li><a href="#help">❓ Help / Āwhina</a></li>
                </ul>
            </div>
        </div>

        <!-- Footer Bottom -->
        <div class="footer-bottom">
            <div class="footer-bottom-content">
                <span class="footer-copyright">© 2025 Te Kete Ako</span>
                <span class="footer-separator">•</span>
                <span class="footer-location">Aotearoa New Zealand</span>
                <span class="footer-separator">•</span>
                <a href="#privacy">Privacy</a>
                <span class="footer-separator">•</span>
                <a href="#terms">Terms</a>
            </div>
        </div>
    </div>
</footer>
```

**📌 Footer Rules:**
1. Copy this EXACTLY to every page
2. NO modifications allowed
3. NO page-specific variations
4. Links stay the same regardless of page context
5. Text never changes

---

## Sidebar Component

### 🔄 DYNAMIC CONTENT, PERMANENT STRUCTURE

**Structure is permanent, widget content changes per page.**

```html
<aside class="left-sidebar no-print">
    <!-- Widget 1 - Content varies by page -->
    <div class="sidebar-widget sidebar-featured">
        <h3 class="sidebar-widget-title">
            <span class="sidebar-icon">🌟</span>
            <span class="sidebar-title-text">
                <span class="sidebar-mi">Ngā Rauemi Rongonui</span>
                <span class="sidebar-en">Featured Resources</span>
            </span>
        </h3>
        <ul>
            <!-- ⚠️ THESE LINKS CHANGE PER PAGE -->
            <li><a href="..."><span class="link-icon">📚</span> Page-specific link</a></li>
        </ul>
    </div>
    
    <!-- Widget 2 - Content varies by page -->
    <div class="sidebar-widget sidebar-quickstart">
        <h3 class="sidebar-widget-title">
            <span class="sidebar-icon">🚀</span>
            <span class="sidebar-title-text">
                <span class="sidebar-mi">Tīmata Tere</span>
                <span class="sidebar-en">Quick Start</span>
            </span>
        </h3>
        <ul>
            <!-- ⚠️ THESE LINKS CHANGE PER PAGE -->
            <li><a href="..."><span class="link-icon">📖</span> Context-specific link</a></li>
        </ul>
    </div>
    
    <!-- Widget 3 - Content varies by page -->
    <div class="sidebar-widget sidebar-teachers">
        <h3 class="sidebar-widget-title">
            <span class="sidebar-icon">🎯</span>
            <span class="sidebar-title-text">
                <span class="sidebar-mi">Mō Ngā Kaiako</span>
                <span class="sidebar-en">For Teachers</span>
            </span>
        </h3>
        <ul>
            <!-- ⚠️ THESE LINKS CHANGE PER PAGE -->
            <li><a href="..."><span class="link-icon">🌿</span> Relevant resource</a></li>
        </ul>
    </div>
</aside>
```

### Sidebar Content Guidelines

**DO:**
- Keep the 3-widget structure
- Use bilingual titles (Te Reo primary)
- Include `link-icon` span for emojis
- Customize links based on page context
- Use appropriate emojis for content type

**DON'T:**
- Change the HTML structure
- Remove bilingual titles
- Add more than 3-4 widgets per page
- Use inline styles
- Duplicate the same links across all widgets

### Example: Year 8 Science Page Sidebar

```html
<div class="sidebar-widget sidebar-featured">
    <h3 class="sidebar-widget-title">
        <span class="sidebar-icon">🔬</span>
        <span class="sidebar-title-text">
            <span class="sidebar-mi">Pūtaiao Tau 8</span>
            <span class="sidebar-en">Year 8 Science</span>
        </span>
    </h3>
    <ul>
        <li><a href="y8-science-unit-1.html"><span class="link-icon">🧪</span> Matter & Particles</a></li>
        <li><a href="y8-science-unit-2.html"><span class="link-icon">🌡️</span> Energy & Heat</a></li>
        <li><a href="y8-science-unit-3.html"><span class="link-icon">🌍</span> Earth Systems</a></li>
    </ul>
</div>
```

---

## Deployment Instructions

### Prerequisites

1. **CSS File:** Ensure `css/main.css` is version 19 or higher
2. **No Inline Styles:** Remove any inline header/footer/sidebar styles
3. **Disable Scripts:** Comment out:
   - `footer.js` (creates duplicate footer)
   - `streamlined-header.js` (conflicts with new header)
   - `advanced-search.js` (adds unwanted search button)

### Step 1: Deploy Header

1. Copy header HTML from `index.html` (lines 20-137)
2. Paste into EVERY page immediately after `<body>` tag
3. Update login button state with auth detection (see Auth Integration)

### Step 2: Deploy Footer

1. Copy footer HTML from `index.html` (lines 332-393)
2. Paste into EVERY page immediately before `</body>` tag
3. **DO NOT modify** - must be identical everywhere

### Step 3: Deploy Sidebar

1. Copy sidebar structure from `index.html` (lines 140-189)
2. Paste into pages that need sidebars (content pages, not browse/search)
3. **Customize widget content** based on page context
4. Keep structure and classes identical

### Step 4: Update CSS Links

Ensure every page has:
```html
<link rel="stylesheet" href="css/main.css?v=19">
```

### Step 5: Comment Out Conflicting Scripts

In every page, ensure these are commented out:
```html
<!-- <script src="js/footer.js"></script> -->
<!-- <script src="js/streamlined-header.js"></script> -->
<!-- <script src="js/advanced-search.js"></script> -->
```

---

## Authentication Integration

### Required: Auth State Detection

Every page must detect auth state and update the header button.

**Add to every page (before closing `</body>`):**

```html
<script>
// Check auth state and update header
document.addEventListener('DOMContentLoaded', function() {
    // Supabase auth check (adjust based on your auth system)
    const { data: { session } } = await supabase.auth.getSession();
    
    const loggedOutBtn = document.querySelector('.auth-logged-out');
    const loggedInBtn = document.querySelector('.auth-logged-in');
    
    if (session) {
        // User is logged in
        loggedOutBtn.style.display = 'none';
        loggedInBtn.style.display = 'flex';
    } else {
        // User is logged out
        loggedOutBtn.style.display = 'flex';
        loggedInBtn.style.display = 'none';
    }
});
</script>
```

**Or use existing `auth-ui.js`:**

Ensure `auth-ui.js` includes:
```javascript
function updateHeaderAuthState() {
    const isLoggedIn = checkAuthStatus(); // Your auth check
    
    const loggedOutBtn = document.querySelector('.auth-logged-out');
    const loggedInBtn = document.querySelector('.auth-logged-in');
    
    if (isLoggedIn) {
        loggedOutBtn.style.display = 'none';
        loggedInBtn.style.display = 'flex';
    } else {
        loggedOutBtn.style.display = 'flex';
        loggedInBtn.style.display = 'none';
    }
}

// Run on page load
document.addEventListener('DOMContentLoaded', updateHeaderAuthState);
```

---

## CSS Classes Reference

### Header Classes

| Class | Purpose | Modify? |
|-------|---------|---------|
| `.site-header` | Header container | Never |
| `.nav-container` | Flexbox wrapper | Never |
| `.nav-brand` | Logo/title | Never |
| `.main-nav` | Navigation list | Never |
| `.nav-icon` | Emoji icons | Never |
| `.nav-text-mi` | Te Reo text | Never |
| `.nav-text-en` | English text | Never |
| `.nav-dropdown` | Dropdown menus | Never |
| `.auth-logged-out` | Login button container | Toggle display |
| `.auth-logged-in` | My Kete button container | Toggle display |

### Footer Classes

| Class | Purpose | Modify? |
|-------|---------|---------|
| `.site-footer` | Footer container | NEVER |
| `.footer-content` | Content wrapper | NEVER |
| `.footer-grid` | 4-column grid | NEVER |
| `.footer-mi` | Te Reo section headers | NEVER |
| `.footer-en` | English section headers | NEVER |
| `.footer-whakataukī` | Cultural quote | NEVER |
| `.footer-bottom` | Bottom bar | NEVER |

### Sidebar Classes

| Class | Purpose | Modify? |
|-------|---------|---------|
| `.left-sidebar` | Sidebar container | Never |
| `.sidebar-widget` | Widget card | Never |
| `.sidebar-icon` | Title emoji | Never |
| `.sidebar-mi` | Te Reo title | Never |
| `.sidebar-en` | English title | Never |
| `.link-icon` | Link emoji | Never |

---

## Testing Checklist

Before deploying to a page:

- [ ] Header displays correctly
- [ ] Login button switches to "Tōku Kete" when logged in
- [ ] All dropdown menus work
- [ ] Year levels grouped correctly (1-3, 4-6, 7-8, 9-10, 11-13)
- [ ] Footer displays at bottom
- [ ] Footer identical to other pages
- [ ] Sidebar widgets relevant to page content
- [ ] Mobile responsive (test at 768px and 480px)
- [ ] Hover animations smooth
- [ ] No console errors
- [ ] Print preview hides header/footer/sidebar
- [ ] CSS version is v=19 or higher
- [ ] No conflicting scripts (footer.js, streamlined-header.js, advanced-search.js)

---

## Troubleshooting

### Header Issues

**Dropdowns hidden behind content:**
- Check `z-index` on `.site-header` (should be 10000)
- Check `overflow` on `.site-header` (should be `visible`)

**Login button not switching:**
- Verify auth detection script is running
- Check browser console for errors
- Ensure Supabase client is loaded

**Spacing issues:**
- Verify no inline styles on header
- Check CSS version is v=19+
- Clear browser cache

### Footer Issues

**Footer looks different on some pages:**
- **SOLUTION:** Copy the EXACT HTML from `index.html`
- Footer must be 100% identical everywhere
- Do NOT make page-specific modifications

**Footer text hard to read:**
- Check CSS version (v=19 has white Te Reo text)
- Verify gradient background is rendering

### Sidebar Issues

**Sidebar too wide/narrow:**
- Check `--sidebar-width` variable in CSS
- Verify no inline width styles

**Links not styled correctly:**
- Ensure `<span class="link-icon">` wraps emoji
- Check link structure matches template

**Scrollbar not showing:**
- Verify sidebar content exceeds viewport height
- Check browser scrollbar settings

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v=19 | Oct 26, 2025 | Initial sitewide deployment version |
| | | - Header with bilingual navigation |
| | | - Footer with white Te Reo text |
| | | - Sidebar with gradient hover effects |

---

## Contact & Support

For questions about deploying these components:
1. Check this guide first
2. Review `index.html` for reference implementation
3. Test in browser developer tools
4. Check Git commit `efc197453` for full changeset

**Remember:** Header and footer are PERMANENT. Sidebar content is DYNAMIC.

---

**Last Updated:** October 26, 2025
**Status:** ✅ Ready for Production
**Git Commit:** `efc197453`


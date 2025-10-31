# 🧭 Navigation Architecture - Te Kete Ako
## Understanding the Navigation System

**Last Updated:** October 31, 2025  
**Status:** ✅ CONSOLIDATED & DOCUMENTED

---

## 📋 QUICK REFERENCE

**To add a link to ALL user dropdowns across the site:**
- ✅ Edit `js/auth-ui.js` (line 138-141)
- ✅ That's it! Applies to 181+ pages automatically

**To modify main navigation:**
- Static nav: Edit HTML in individual pages
- Dynamic nav: Edit `js/streamlined-header.js` (currently disabled on most pages)

---

## 🏗️ ARCHITECTURE OVERVIEW

Te Kete Ako uses **THREE navigation systems** (intentionally):

### 1. **`auth-ui.js`** - User Dropdown System ⭐ PRIMARY
**File:** `js/auth-ui.js`  
**Used by:** 181+ HTML pages  
**Purpose:** Handles user authentication state and user dropdown menu

**User Dropdown Contents:**
```javascript
// Line 138-141 in auth-ui.js
<a href="/my-kete.html">🧺 Tōku Kete / My Kete</a>
<a href="/profile.html">👤 Kōtaha / Profile</a>
<a href="/account-settings.html">⚙️ Ngā Tautuhinga / Account Settings</a>
<a href="#">🚪 Puta / Sign Out</a>
```

**How it works:**
- Monitors Supabase auth state
- Shows user dropdown when logged in
- Hides login/register buttons when authenticated
- Applies consistently across ALL pages that load it

**Pages using this:**
- All handouts (100+ files)
- All lessons (50+ files)
- All units
- Main pages (index, browse, my-kete, profile, etc.)
- Games
- Resources

---

### 2. **`shared-components.js`** - Content Utilities
**File:** `js/shared-components.js`  
**Used by:** 249+ HTML pages  
**Purpose:** Provides recommended reading, utilities, legacy navigation

**What it does:**
- Educational book recommendations by topic
- Print optimization
- Mobile menu functionality
- **LEGACY:** Old `generateNavigation()` function (mostly unused)

**Important:**
- Does NOT handle user authentication
- Does NOT create user dropdowns
- Most pages load BOTH `shared-components.js` AND `auth-ui.js`

---

### 3. **`streamlined-header.js`** - Advanced Navigation (Optional)
**File:** `js/streamlined-header.js`  
**Used by:** Currently DISABLED on most pages (commented out)  
**Purpose:** Replaces static nav with fancy dropdowns

**Features:**
- Unit Plans dropdown (with featured units)
- Lesson Plans dropdown
- Resources dropdown (handouts, activities, games)
- Clean, modern design

**Status:**
- Available but not activated
- `index.html` line 444: `<!-- <script src="js/streamlined-header.js"></script> -->`
- Intentionally disabled to keep homepage simple

---

## 📊 FILE USAGE STATISTICS

| File | Pages Using | Purpose |
|------|-------------|---------|
| `auth-ui.js` | 181 | User authentication & dropdown |
| `shared-components.js` | 249 | Utilities & recommendations |
| `streamlined-header.js` | 0 (disabled) | Advanced navigation dropdowns |

**Overlap:** Most pages load BOTH `auth-ui.js` and `shared-components.js`

---

## 🎯 COMMON TASKS

### ✅ Add link to user dropdown menu
**Edit:** `js/auth-ui.js` (lines 138-141)  
**Impact:** All 181+ pages  
**Example:** Profile link added Oct 31, 2025

```javascript
// In createUserMenuHTML() function
<a href="/profile.html">
    <span class="dropdown-mi">👤 Kōtaha</span>
    <span class="dropdown-en">Profile</span>
</a>
```

### ✅ Modify static navigation (individual pages)
**Edit:** HTML file directly (lines ~25-120 typically)  
**Impact:** That page only  
**Example:** `index.html` has custom static nav

### ✅ Enable advanced dropdowns
**Edit:** Uncomment `streamlined-header.js` in HTML  
**Impact:** Replaces static nav with dropdowns  
**Example:** Currently disabled on homepage

---

## 🔍 HOW TO VERIFY

### Check if a page has user dropdown:
```bash
grep -l "auth-ui.js" your-page.html
```

### Check if a page uses shared components:
```bash
grep -l "shared-components.js" your-page.html
```

### Find all pages with user dropdown:
```bash
grep -rl "auth-ui.js" *.html | wc -l
# Result: 181+
```

---

## 🚨 IMPORTANT PATTERNS

### ✅ DO THIS:
- **Edit `auth-ui.js` for user menu changes** (applies everywhere)
- Load both `auth-ui.js` AND `shared-components.js` on content pages
- Use bilingual labels (Māori + English) for all navigation
- Keep dropdown items in logical order: My Kete → Profile → Settings → Logout

### ❌ DON'T DO THIS:
- Don't create multiple user dropdown systems
- Don't hardcode user menus in individual HTML files
- Don't assume `shared-components.js` handles auth (it doesn't!)
- Don't remove `auth-ui.js` without replacing auth functionality

---

## 📐 DESIGN PATTERNS

### User Dropdown Structure:
```html
<div class="nav-dropdown user-dropdown">
    <div class="user-dropdown-header">
        <div class="user-dropdown-name">username</div>
        <div class="user-dropdown-email">email@domain.com</div>
    </div>
    <a href="/link.html">
        <span class="dropdown-mi">🔧 Māori Text</span>
        <span class="dropdown-en">English Text</span>
    </a>
    <!-- More links -->
    <a href="#" class="logout-btn">
        <span class="dropdown-mi">🚪 Puta</span>
        <span class="dropdown-en">Sign Out</span>
    </a>
</div>
```

### CSS Variables Used:
- `var(--color-primary)` - Forest green
- `var(--shadow-medium)` - Dropdown shadows
- `var(--radius-md)` - Border radius

---

## 🔄 NAVIGATION LIFECYCLE

1. **Page loads** → Both `auth-ui.js` and `shared-components.js` initialize
2. **Auth-UI checks Supabase** → Is user logged in?
3. **If logged in:**
   - Creates user dropdown with username
   - Populates links (My Kete, Profile, Settings, Logout)
   - Hides login/register buttons
4. **If logged out:**
   - Shows login/register buttons
   - Hides user dropdown
5. **User clicks dropdown** → Shows menu items
6. **User clicks link** → Navigates to page

---

## 📚 HISTORICAL CONTEXT

### Why three systems?

**`auth-ui.js` (2025):**
- Modern Supabase authentication
- Consistent across all pages
- Handles session management

**`shared-components.js` (2024):**
- Originally for content recommendations
- Included legacy navigation
- Still used for utilities

**`streamlined-header.js` (2025):**
- Experimental advanced navigation
- Beautiful dropdown menus
- Disabled for simplicity

### Evolution:
1. **Phase 1 (2024):** Static HTML navigation only
2. **Phase 2 (2024):** Added `shared-components.js` for recommendations
3. **Phase 3 (2025):** Added `auth-ui.js` for Supabase auth
4. **Phase 4 (2025):** Created `streamlined-header.js` (optional)
5. **Current:** Hybrid approach - static nav + auth dropdown

---

## 🎨 CULTURAL INTEGRATION

All navigation uses **bilingual labels**:
- Māori first (`.dropdown-mi`)
- English second (`.dropdown-en`)

**Examples:**
- 🧺 Tōku Kete / My Kete
- 👤 Kōtaha / Profile
- ⚙️ Ngā Tautuhinga / Account Settings
- 🚪 Puta / Sign Out

**Emoji usage:**
- Enhances accessibility
- Universal understanding
- Adds visual interest

---

## 🐛 TROUBLESHOOTING

### Problem: User dropdown not showing
**Check:**
1. Is `auth-ui.js` loaded? (`grep "auth-ui.js" page.html`)
2. Is Supabase initialized? (Check browser console)
3. Is user actually logged in? (Check Supabase Auth state)

### Problem: Navigation looks different on one page
**Check:**
1. Does page load different CSS? (`grep "stylesheet" page.html`)
2. Does page use `streamlined-header.js`?
3. Does page have custom inline styles?

### Problem: Profile link not appearing
**Check:**
1. Browser cache (hard refresh: Cmd+Shift+R)
2. JavaScript console for errors
3. Verify `auth-ui.js` line 139 has Profile link

---

## 📝 MAINTENANCE LOG

| Date | Change | Impact |
|------|--------|--------|
| Oct 31, 2025 | Added Profile link to user dropdown | All 181 pages |
| Oct 31, 2025 | Created this documentation | Reference |
| Oct 26, 2025 | CSS crisis resolved (BMAD Authentic system) | Design consistency |
| Aug 2025 | Implemented `auth-ui.js` | User authentication |

---

## 🔮 FUTURE CONSIDERATIONS

### Potential Improvements:
1. **Consolidate systems** → Merge `shared-components.js` into `auth-ui.js`
2. **Enable streamlined header** → Better UX with dropdowns
3. **Server-side rendering** → Faster initial page load
4. **Component framework** → React/Vue for consistency

### Migration Path:
If consolidating navigation:
1. Move utility functions from `shared-components.js` to `auth-ui.js`
2. Enable `streamlined-header.js` across all pages
3. Remove legacy `generateNavigation()` function
4. Update all 249 HTML files to use new system

**Estimated effort:** 4-6 hours  
**Risk:** Medium (affects all pages)  
**Benefit:** Single source of truth for navigation

---

## 🎯 BOTTOM LINE

**For 99% of navigation changes:**
- ✅ Edit `js/auth-ui.js`
- ✅ That's it!
- ✅ Applies everywhere automatically

**The system works.** It's hybrid (static + dynamic), but it's **intentional** and **functional**.

---

**Questions?** Read the code:
- `js/auth-ui.js` (user dropdowns)
- `js/shared-components.js` (utilities)
- `js/streamlined-header.js` (optional advanced nav)

**Need help?** Check this document first!

🧺✨


# 🏛️ NAVIGATION ARCHITECTURE - COMPREHENSIVE SUMMARY

**Date:** October 26, 2025  
**Based On:** Professional SaaS Transformation Plan + Existing Navigation Planning  
**Status:** 📋 PLANNED, NOT YET IMPLEMENTED  

---

## 🎯 **THE PLANNED ARCHITECTURE (From Existing Docs)**

### **HEADER + SIDEBAR + NESTED NAVIGATION SYSTEM:**

```
┌──────────────────────────────────────────────────────────────┐
│  TOP HEADER (Sticky)                                         │
│  ┌────────┐  Search Bar         🧺 My Kete    🔔  👤        │
│  │ LOGO   │  [Search...]        Notifications  Profile      │
│  └────────┘                                                  │
└──────────────────────────────────────────────────────────────┘
┌─────────────┬────────────────────────────────────────────────┐
│   SIDEBAR   │  MAIN CONTENT AREA                             │
│  (Persist)  │                                                │
│             │  ┌──────────────────────────────────────────┐  │
│  👤 Profile │  │  BREADCRUMB NAVIGATION                  │  │
│  Teacher    │  │  Home > Units > Y8 > Algebra             │  │
│  Math Dept  │  └──────────────────────────────────────────┘  │
│             │                                                │
│  ⚡ Quick   │  [Page Content]                                │
│  🚨 Emerg.  │                                                │
│  ⭐ Top 10  │                                                │
│             │                                                │
│  📚 Content │                                                │
│  ▼ Units    │  ┌──────────────────────────────────────────┐  │
│    Y8 Alg   │  │  NESTED NAVIGATION EXAMPLE:              │  │
│    Y9 Eco   │  │                                          │  │
│  ▼ Lessons  │  │  Unit Overview                           │  │
│    Browse   │  │  ├─ Week 1: Introduction                 │  │
│  ▼ Handouts │  │  │  ├─ Lesson 1.1                        │  │
│    Download │  │  │  ├─ Lesson 1.2                        │  │
│             │  │  │  └─ Handout Set 1                     │  │
│  🎓 Subject │  │  ├─ Week 2: Practice                     │  │
│  Math       │  │  │  ├─ Lesson 2.1                        │  │
│  Science    │  │  │  └─ Assessment 1                      │  │
│  English    │  │  └─ Week 3: Extension                    │  │
│             │  │     └─ ...                               │  │
│  🌿 Culture │  └──────────────────────────────────────────┘  │
│  Excellence │                                                │
│  Te Reo     │                                                │
│             │                                                │
│  🛠️ Tools   │                                                │
│  Classes    │                                                │
│  Progress   │                                                │
│  AI Plan    │                                                │
│  Analytics  │                                                │
│             │                                                │
│  ⚙️ Account │                                                │
│  Settings   │                                                │
│  💳 Sub     │                                                │
│  🚪 Logout  │                                                │
└─────────────┴────────────────────────────────────────────────┘
```

---

## 📋 **THREE-TIER NAVIGATION SYSTEM (PLANNED)**

### **TIER 1: TOP HEADER (Global, Always Visible)**

**Purpose:** Site-wide utilities and branding

**Elements:**
```html
<header class="global-header sticky">
  <div class="header-left">
    <img src="/logo.svg" alt="Te Kete Ako">
    <span class="site-title">Te Kete Ako</span>
  </div>
  
  <div class="header-center">
    <!-- Global Search (GraphRAG-powered!) -->
    <input type="search" 
           placeholder="Search 20,948 resources..." 
           class="global-search">
  </div>
  
  <div class="header-right">
    <!-- My Kete (Saved Resources) -->
    <a href="/my-kete" class="header-icon">
      🧺 <span class="badge">12</span>
    </a>
    
    <!-- Notifications -->
    <button class="header-icon notifications">
      🔔 <span class="badge">3</span>
    </button>
    
    <!-- Profile Dropdown -->
    <div class="profile-dropdown">
      <img src="/avatar" class="avatar">
      <span class="name">Sarah Jones</span>
      <div class="dropdown-menu">
        <a href="/profile">👤 Profile</a>
        <a href="/settings">⚙️ Settings</a>
        <a href="/subscription">💳 Subscription</a>
        <hr>
        <button onclick="logout()">🚪 Logout</button>
      </div>
    </div>
  </div>
</header>
```

**Key Features:**
- ✅ Sticky positioning (always visible)
- ✅ Global search (queries GraphRAG)
- ✅ My Kete shortcut
- ✅ Notifications center
- ✅ Profile with role (Teacher/Student)

**Height:** 60-80px (compact for content space)

---

### **TIER 2: SIDEBAR (Persistent Left Navigation)**

**Purpose:** Role-based hierarchical navigation

#### **TEACHER SIDEBAR (Primary Use Case):**

```html
<aside class="professional-sidebar teacher-mode">
  <!-- PROFILE SECTION -->
  <div class="sidebar-profile">
    <img src="/avatar" alt="Avatar" class="profile-avatar">
    <h4>Sarah Jones</h4>
    <p class="role">Mathematics Teacher</p>
    <p class="school">Auckland College</p>
  </div>
  
  <!-- QUICK ACTIONS -->
  <div class="sidebar-section quick-actions">
    <h5>⚡ Quick Actions</h5>
    <a href="/emergency-lessons" class="sidebar-link priority">
      🚨 Emergency Lesson
    </a>
    <a href="/top-10-starter-pack" class="sidebar-link">
      ⭐ Top 10 Starter Pack
    </a>
  </div>
  
  <!-- TEACHING CONTENT (Nested!) -->
  <div class="sidebar-section">
    <h5>📚 Teaching Content</h5>
    
    <!-- Units (Collapsible/Expandable) -->
    <details class="sidebar-dropdown">
      <summary>
        📦 My Units (12)
        <span class="count-badge">12</span>
      </summary>
      <div class="nested-links">
        <a href="/units/y8-algebra" class="nested-link">
          🔢 Y8 Algebra
          <span class="quality-badge">Q96</span>
        </a>
        <a href="/units/y9-ecology" class="nested-link">
          🌿 Y9 Ecology & Whakapapa
          <span class="quality-badge gold">Q98</span>
        </a>
        <a href="/units/y8-digital-kaitiakitanga" class="nested-link">
          💻 Y8 Digital Kaitiakitanga ⭐
          <span class="quality-badge gold">Q100</span>
        </a>
        <!-- Show user's favorited/used units -->
      </div>
    </details>
    
    <!-- Lessons -->
    <details class="sidebar-dropdown">
      <summary>
        📝 Lessons (45)
        <span class="count-badge">45</span>
      </summary>
      <div class="nested-links">
        <a href="/lessons?filter=recent" class="nested-link">
          🕐 Recently Used
        </a>
        <a href="/lessons?filter=favorites" class="nested-link">
          ⭐ Favorites
        </a>
        <a href="/lessons" class="nested-link">
          🔍 Browse All
        </a>
      </div>
    </details>
    
    <!-- Handouts -->
    <details class="sidebar-dropdown">
      <summary>
        📄 Handouts (128)
        <span class="count-badge">128</span>
      </summary>
      <div class="nested-links">
        <a href="/handouts?filter=recent" class="nested-link">
          🕐 Recently Downloaded
        </a>
        <a href="/handouts" class="nested-link">
          🔍 Browse All
        </a>
      </div>
    </details>
  </div>
  
  <!-- BY SUBJECT -->
  <div class="sidebar-section">
    <h5>🎓 Subjects</h5>
    <a href="/mathematics-hub" class="sidebar-link">
      🔢 Mathematics
    </a>
    <a href="/science-hub" class="sidebar-link">
      🔬 Science
    </a>
    <a href="/english-hub" class="sidebar-link">
      📝 English
    </a>
    <a href="/social-studies-hub" class="sidebar-link">
      🌏 Social Studies
    </a>
    <a href="/te-reo-maori-hub" class="sidebar-link cultural">
      🌿 Te Reo Māori
    </a>
    <a href="/digital-tech-hub" class="sidebar-link">
      💻 Digital Tech
    </a>
    <a href="/health-pe-hub" class="sidebar-link">
      🏃 Health & PE
    </a>
  </div>
  
  <!-- CULTURAL (Priority Section!) -->
  <div class="sidebar-section cultural-section">
    <h5>🌿 Cultural Excellence</h5>
    <a href="/cultural-excellence-hub" class="sidebar-link">
      🏆 Excellence Hub
    </a>
    <a href="/maori-integration" class="sidebar-link">
      🌿 Māori Integration
    </a>
    <a href="/tikanga" class="sidebar-link">
      📚 Tikanga Resources
    </a>
  </div>
  
  <!-- PROFESSIONAL TOOLS -->
  <div class="sidebar-section tools-section">
    <h5>🛠️ Professional Tools</h5>
    <a href="/my-classes" class="sidebar-link">
      👥 My Classes
    </a>
    <a href="/student-progress" class="sidebar-link">
      📊 Student Progress
    </a>
    <a href="/ai-lesson-planner" class="sidebar-link ai-feature">
      🤖 AI Lesson Planner
    </a>
    <a href="/analytics" class="sidebar-link">
      📈 My Analytics
    </a>
  </div>
  
  <!-- FOOTER (Account Actions) -->
  <div class="sidebar-footer">
    <a href="/settings" class="sidebar-link compact">
      ⚙️ Settings
    </a>
    <a href="/subscription" class="sidebar-link compact">
      💳 Subscription
    </a>
    <a href="/help" class="sidebar-link compact">
      ❓ Help & Support
    </a>
    <button onclick="logout()" class="logout-btn">
      🚪 Logout
    </button>
  </div>
</aside>
```

**Key Features:**
- ✅ **Nested navigation** (Units > My Units > Individual units)
- ✅ **Collapsible sections** (`<details>` elements)
- ✅ **GraphRAG-powered** (shows user's content, quality scores)
- ✅ **Cultural priority** (dedicated section, not buried!)
- ✅ **Role-specific** (Teacher vs Student sidebars differ)
- ✅ **Quick access** (Emergency lessons, Top 10 at top)

**Width:** 280-320px (enough for nested hierarchy)

---

### **TIER 3: BREADCRUMB + NESTED PAGE NAVIGATION**

**Purpose:** Show context + drill-down within content

#### **Breadcrumb Navigation:**

```html
<!-- Always at top of content area -->
<nav class="breadcrumb-nav" aria-label="Breadcrumb">
  <a href="/">Home</a>
  <span class="separator">›</span>
  <a href="/units">Units</a>
  <span class="separator">›</span>
  <a href="/units/y8-algebra">Y8 Algebra</a>
  <span class="separator">›</span>
  <span class="current">Week 2: Equations</span>
</nav>
```

#### **Nested Page Navigation (Within Unit/Lesson):**

**Example: Inside a Unit Page**

```html
<!-- Unit Structure Navigation -->
<div class="unit-structure-nav">
  <h3>Unit Structure</h3>
  
  <!-- Week 1 -->
  <details open class="week-section">
    <summary class="week-title">
      Week 1: Introduction to Algebra
      <span class="progress">3/5 lessons used</span>
    </summary>
    <ul class="lesson-list">
      <li class="lesson-item completed">
        <a href="/units/y8-algebra/week-1/lesson-1">
          ✅ Lesson 1.1: Variables & Expressions
        </a>
        <span class="duration">75 min</span>
      </li>
      <li class="lesson-item completed">
        <a href="/units/y8-algebra/week-1/lesson-2">
          ✅ Lesson 1.2: Simple Equations
        </a>
        <span class="duration">75 min</span>
      </li>
      <li class="lesson-item completed">
        <a href="/units/y8-algebra/week-1/lesson-3">
          ✅ Lesson 1.3: Practice Problems
        </a>
        <span class="duration">50 min</span>
      </li>
      <li class="handout-item">
        <a href="/units/y8-algebra/week-1/handout-1">
          📄 Handout Set 1: Variables Worksheet
        </a>
        <button class="download-btn">📥 Download</button>
      </li>
      <li class="assessment-item">
        <a href="/units/y8-algebra/week-1/assessment-1">
          📝 Quiz 1: Variables & Equations
        </a>
      </li>
    </ul>
  </details>
  
  <!-- Week 2 (Currently Active) -->
  <details open class="week-section active">
    <summary class="week-title current">
      Week 2: Solving Equations
      <span class="progress">1/6 lessons used</span>
    </summary>
    <ul class="lesson-list">
      <li class="lesson-item completed">
        <a href="/units/y8-algebra/week-2/lesson-1">
          ✅ Lesson 2.1: One-Step Equations
        </a>
        <span class="duration">75 min</span>
      </li>
      <li class="lesson-item current">
        <a href="/units/y8-algebra/week-2/lesson-2" class="current-lesson">
          📖 Lesson 2.2: Two-Step Equations ← YOU ARE HERE
        </a>
        <span class="duration">75 min</span>
      </li>
      <li class="lesson-item">
        <a href="/units/y8-algebra/week-2/lesson-3">
          ⏳ Lesson 2.3: Multi-Step Equations
        </a>
        <span class="duration">75 min</span>
      </li>
      <!-- ... more lessons ... -->
    </ul>
  </details>
  
  <!-- Week 3-8 (Collapsed by default) -->
  <details class="week-section">
    <summary class="week-title">
      Week 3: Advanced Equations
      <span class="progress">0/5 lessons used</span>
    </summary>
    <!-- ... -->
  </details>
</div>
```

**Key Features:**
- ✅ **Nested hierarchy** (Unit > Week > Lesson > Handout)
- ✅ **Progress tracking** (completed lessons marked)
- ✅ **Current location** (YOU ARE HERE indicator)
- ✅ **Collapsible sections** (weeks can expand/collapse)
- ✅ **GraphRAG relationships** (shows related handouts, assessments)

---

## 🎨 **DESIGN SYSTEM (PLANNED)**

### **Cultural Authenticity + Professional Polish:**

```css
/* Māori-Inspired Color Palette */
:root {
  /* PRIMARY (Earth & Forest) */
  --color-primary: #2C5F41;        /* Deep forest green */
  --color-primary-light: #3A7D56;  /* Lighter green */
  --color-primary-dark: #1d3f2a;   /* Dark green */
  
  /* SECONDARY (Earth & Tan) */
  --color-secondary: #8B4513;      /* Warm earth brown */
  --color-accent: #CD853F;         /* Tan/tan */
  
  /* CULTURAL HIGHLIGHTS */
  --color-cultural: #B8860B;       /* Gold (for cultural content) */
  --color-excellence: #FFD700;     /* Bright gold (Q90+ badges) */
  
  /* NEUTRALS (Warm, not cold gray) */
  --color-bg: #FAF9F6;             /* Warm white */
  --color-surface: #FFFFFF;
  --color-text: #2D3748;           /* Warm dark gray */
  
  /* SPACING (Generous, breathing room) */
  --space-unit: 8px;
  --space-small: 12px;
  --space-medium: 20px;
  --space-large: 32px;
  --space-xl: 48px;
  
  /* TYPOGRAPHY (Māori-friendly) */
  --font-heading: 'Tauri', 'Hind', sans-serif;
  --font-body: 'Hind', 'Open Sans', sans-serif;
  --font-mono: 'Courier New', monospace;
  
  /* BORDER RADIUS (Soft, warm) */
  --radius-small: 6px;
  --radius-medium: 12px;
  --radius-large: 16px;
  
  /* SIDEBAR */
  --sidebar-width: 280px;
  --header-height: 70px;
}

/* Sidebar Styling */
.professional-sidebar {
  width: var(--sidebar-width);
  height: calc(100vh - var(--header-height));
  position: fixed;
  top: var(--header-height);
  left: 0;
  background: linear-gradient(180deg, #2C5F41 0%, #1d3f2a 100%);
  color: var(--color-bg);
  overflow-y: auto;
  box-shadow: 4px 0 20px rgba(0,0,0,0.1);
  z-index: 900;
}

/* Nested Navigation */
.sidebar-dropdown summary {
  cursor: pointer;
  padding: var(--space-small);
  border-radius: var(--radius-small);
  transition: background 0.2s;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.sidebar-dropdown summary:hover {
  background: rgba(255,255,255,0.1);
}

.sidebar-dropdown[open] summary {
  background: rgba(255,255,255,0.15);
  margin-bottom: var(--space-small);
}

.nested-links {
  padding-left: var(--space-medium);
  border-left: 2px solid rgba(255,255,255,0.2);
}

.nested-link {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-small);
  color: rgba(255,255,255,0.9);
  text-decoration: none;
  border-radius: var(--radius-small);
  margin-bottom: 4px;
  transition: all 0.2s;
}

.nested-link:hover {
  background: rgba(255,255,255,0.1);
  color: #FFFFFF;
  padding-left: calc(var(--space-small) + 8px);
}

/* Quality Badges (Gold Standard Visible!) */
.quality-badge {
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 12px;
  background: rgba(255,255,255,0.2);
  color: #FFFFFF;
}

.quality-badge.gold {
  background: var(--color-excellence);
  color: #2D3748;
  font-weight: bold;
}
```

---

## 📊 **GRAPHRAG INTEGRATION (PLANNED)**

### **How Navigation Uses GraphRAG:**

**1. Sidebar "My Units" Section:**
```javascript
// Query user's recently used units
const myUnits = await supabase
  .from('user_activity')
  .select('resource_id, resources(title, quality_score, path)')
  .eq('user_id', currentUser.id)
  .eq('activity_type', 'unit_access')
  .order('accessed_at', { ascending: false })
  .limit(12);

// Populate sidebar dynamically
renderSidebarUnits(myUnits);
```

**2. Unit Page "Related Content":**
```javascript
// Query GraphRAG for related lessons/handouts
const relatedContent = await supabase
  .from('graphrag_relationships')
  .select('target_resource_id, resources(*)')
  .eq('source_resource_id', currentUnitId)
  .in('relationship_type', ['contains', 'requires', 'supplements']);

// Build nested navigation automatically
renderUnitStructure(relatedContent);
```

**3. Quality Score Badges:**
```javascript
// Show Q90+ badge next to high-quality resources
resources.forEach(resource => {
  if (resource.quality_score >= 90) {
    addBadge(resource, 'gold', `Q${resource.quality_score}`);
  }
});
```

**Result:** Navigation is INTELLIGENT, not static!

---

## 🚀 **IMPLEMENTATION STATUS**

### **Current Reality:**

✅ **PLANNED:** Comprehensive SaaS transformation doc exists  
✅ **DESIGNED:** Sidebar, header, nested nav all designed  
✅ **RESEARCHED:** GraphRAG integration mapped out  

❌ **NOT IMPLEMENTED:** Still using old navigation system  
❌ **NOT BUILT:** Sidebar doesn't exist yet  
❌ **NOT INTEGRATED:** GraphRAG not powering navigation  

### **Why Not Implemented Yet:**

**From analysis:**
- Team focused on content creation (20,948 resources!)
- Platform in "expansion phase" (build everything)
- Now entering "curation phase" (organize intelligently)
- SaaS transformation awaiting final approval/prioritization

---

## 💡 **RECOMMENDATIONS**

### **Based on Hegelian Synthesis + Your Vision:**

**PRIORITY 1: Implement Sidebar (2-3 days)**
- Build teacher sidebar component
- Integrate with existing auth system
- Add collapsible/nested sections
- GraphRAG-powered "My Units" section

**PRIORITY 2: Preserve Māori Aesthetics**
- Use planned color palette (greens/browns, NOT corporate blue)
- Māori-friendly typography (Tauri/Hind)
- Cultural section prominently placed
- Quality badges show excellence visibly

**PRIORITY 3: Intelligent Curation**
- Sidebar shows Q90+ content preferentially
- Nested navigation based on GraphRAG relationships
- User-specific content (recently used, favorites)

**PRIORITY 4: Delete Old Navigation**
- Remove 5/6 redundant nav components
- Keep only: Header (global) + Sidebar (role-based)
- Breadcrumbs for context

---

## 🎯 **NEXT STEPS (User Decision Needed!)**

1. **Do you want to implement the full SaaS sidebar now?**
   - Or wait until login-first is activated?

2. **Which role to build first?**
   - Teacher sidebar (more complex, more features)?
   - Student sidebar (simpler, focused)?

3. **GraphRAG integration priority?**
   - Dynamic "My Units" (query user activity)?
   - Quality scores visible everywhere?
   - Related content suggestions?

4. **Cultural aesthetic confirmation?**
   - Green/brown earth tones (as planned)?
   - Or different Māori-inspired palette?

5. **Navigation cleanup permission?**
   - Delete 5/6 redundant navigation components?
   - Keep only header + sidebar + breadcrumbs?

---

**Status:** ✅ COMPREHENSIVE PLANNING EXISTS  
**Implementation:** ⏳ AWAITING PRIORITIZATION  
**Tech Stack:** ✅ READY (Auth, GraphRAG, all systems built!)  

**Kia ora! The vision is clear - now it's execution time!** 🌿🚀

**Shall we start building the sidebar, or do you want to adjust the plan first?**


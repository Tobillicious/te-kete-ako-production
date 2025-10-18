# 🔧 MASTER TECH SPECS - Te Kete Ako

**Last Updated:** Oct 16, 2025 - 11:00 PM  
**Purpose:** Complete technical architecture reference

---

## 🏗️ SYSTEM ARCHITECTURE

### **Frontend:**
- **Static HTML/CSS/JS** - No framework overhead
- **Build Tool:** Vite (for dev server + optimization)
- **Hosting:** Netlify (auto-deploy from `main` branch)
- **CDN:** Cloudflare (via Netlify)
- **URL:** https://tekete.netlify.app

### **Backend:**
- **Database:** Supabase (PostgreSQL)
- **Auth:** Supabase Auth (JWT-based)
- **Storage:** Supabase Storage (for files)
- **Functions:** Netlify Functions (serverless)
- **MCP:** Model Context Protocol for agent coordination

### **AI Integration:**
- **GraphRAG:** Knowledge graph in Supabase
- **Agents:** 12 Cursor AI agents (coordinated)
- **Models:** Claude Sonnet 4.5, GPT-4, DeepSeek, Gemini

---

## 📊 DATABASE SCHEMA

### **Core Tables:**

#### `resources`
```sql
id: BIGSERIAL PRIMARY KEY
title: TEXT NOT NULL
path: TEXT UNIQUE NOT NULL
description: TEXT NOT NULL
subject: TEXT
level: TEXT (Y7-Y13)
type: TEXT (unit, lesson, handout, index)
cultural_elements: TEXT[]
tags: TEXT[]
status: TEXT DEFAULT 'active'
created_at: TIMESTAMPTZ
updated_at: TIMESTAMPTZ
```

#### `relationships`
```sql
id: BIGSERIAL PRIMARY KEY
source_id: BIGINT REFERENCES resources(id)
target_id: BIGINT REFERENCES resources(id)
relationship_type: TEXT (prerequisite, related, part_of, etc.)
strength: FLOAT (0-1, for GraphRAG weighting)
created_at: TIMESTAMPTZ
```

#### `profiles`
```sql
id: UUID PRIMARY KEY REFERENCES auth.users(id)
email: TEXT UNIQUE
full_name: TEXT
role: TEXT (student, teacher, admin)
school_id: BIGINT REFERENCES nz_schools(id)
year_level: INTEGER (for students)
subjects: TEXT[] (for teachers)
registration_number: TEXT (for teachers)
cultural_background: TEXT[]
created_at: TIMESTAMPTZ
updated_at: TIMESTAMPTZ
```

#### `nz_schools`
```sql
id: BIGSERIAL PRIMARY KEY
name: TEXT NOT NULL
type: TEXT (Primary, Secondary, Composite, etc.)
region: TEXT
city: TEXT
decile: INTEGER
roll: INTEGER
kamar_enabled: BOOLEAN DEFAULT false
created_at: TIMESTAMPTZ
```

#### `agent_coordination`
```sql
id: BIGSERIAL PRIMARY KEY
agent_name: TEXT NOT NULL
task_claimed: TEXT NOT NULL
status: TEXT (pending, in_progress, completed, cancelled)
started_at: TIMESTAMPTZ
completed_at: TIMESTAMPTZ
key_decisions: TEXT[]
files_modified: TEXT[]
notes: TEXT
```

#### `agent_knowledge`
```sql
id: BIGSERIAL PRIMARY KEY
source_type: TEXT NOT NULL (archived_md, discovery, decision)
source_name: TEXT NOT NULL
doc_type: TEXT NOT NULL (auth, styling, coordination, etc.)
key_insights: TEXT[]
technical_details: JSONB
agents_involved: TEXT[]
created_at: TIMESTAMPTZ
updated_at: TIMESTAMPTZ
```

---

## 🎨 CSS ARCHITECTURE

### **Canonical CSS System (8 Files):**

1. **`te-kete-unified-design-system.css`** (Base)
   - Design tokens (colors, spacing, typography)
   - CSS custom properties
   - Global resets
   - Core layout utilities

2. **`component-library.css`**
   - Reusable UI components
   - Buttons, cards, forms
   - Badges, tags, alerts
   - Consistent patterns

3. **`animations-professional.css`**
   - Fade-in, slide-in effects
   - Hover animations
   - Loading states
   - Smooth transitions

4. **`beautiful-navigation.css`**
   - Sticky header
   - Mega menu dropdowns
   - Mobile hamburger menu
   - Breadcrumbs

5. **`mobile-optimization.css`**
   - Responsive breakpoints
   - Touch-friendly targets
   - Mobile-first layouts
   - Device-specific adjustments

6. **`print.css`**
   - Print-friendly styles
   - Remove navigation
   - Page breaks
   - High contrast

7-8. **Legacy support** (temporary)

### **Design Tokens:**
```css
:root {
  /* Colors */
  --color-primary: #2B4C7E;
  --color-secondary: #8B6F47;
  --color-accent: #D4A574;
  --color-cultural: #7C3E3E;
  
  /* Spacing */
  --spacing-xs: 0.5rem;
  --spacing-sm: 1rem;
  --spacing-md: 1.5rem;
  --spacing-lg: 2rem;
  --spacing-xl: 3rem;
  
  /* Typography */
  --font-body: 'Nunito', sans-serif;
  --font-heading: 'Poppins', sans-serif;
  --font-maori: 'Tauri', sans-serif;
  
  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-normal: 300ms ease;
  --transition-slow: 500ms ease;
}
```

---

## 🔐 AUTHENTICATION FLOW

### **Student Signup (4 Steps):**
1. **Basic Info:** Name, email, password
2. **School Details:** School selection (from nz_schools)
3. **Learning Profile:** Year level, subjects, learning style
4. **Cultural Connection:** Cultural background, iwi affiliation

### **Teacher Signup (5 Steps):**
1. **Basic Info:** Title, name, email, password
2. **Professional:** School, registration number, role
3. **Teaching:** Subjects, year levels (multi-select)
4. **KAMAR Integration:** Optional school code + API key
5. **Review & Confirm:** Summary before submission

### **Auth Redirect Logic:**
```javascript
async function redirectByRole(user) {
  const profile = await fetchProfile(user.id);
  
  if (profile.role === 'student') {
    window.location.href = '/student-dashboard.html';
  } else if (profile.role === 'teacher') {
    window.location.href = '/teachers/dashboard.html';
  } else if (profile.role === 'admin') {
    window.location.href = '/admin/dashboard.html';
  } else {
    window.location.href = '/my-kete.html';
  }
}
```

---

## 🧠 GRAPHRAG SYSTEM

### **Purpose:**
Intelligent content navigation and discovery through relationship mapping.

### **Core Algorithm:**
```python
def find_related_resources(resource_id, limit=6):
    """
    Find related resources using multi-factor scoring:
    1. Direct relationships (weight: 1.0)
    2. Same subject + level (weight: 0.8)
    3. Shared tags (weight: 0.6)
    4. Cultural connections (weight: 0.7)
    5. Type progression (unit → lesson → handout)
    """
    
    # Query relationships
    direct = query_relationships(resource_id)
    
    # Query similar by attributes
    similar = query_similar_attributes(resource_id)
    
    # Score and rank
    scored = score_resources(direct, similar)
    
    # Return top N
    return sorted(scored, key=lambda x: x.score, reverse=True)[:limit]
```

### **Relationship Types:**
- `part_of` - Lesson is part of Unit
- `contains` - Unit contains Lessons
- `prerequisite` - Must complete first
- `builds_on` - Extends concepts
- `related_to` - Same theme/topic
- `cultural_link` - Te Ao Māori connection
- `cross_curricular` - Links subjects

---

## 📱 RESPONSIVE BREAKPOINTS

```css
/* Mobile-first approach */

/* Small phones */
@media (max-width: 480px) { ... }

/* Large phones / small tablets */
@media (max-width: 768px) { ... }

/* Tablets */
@media (max-width: 1024px) { ... }

/* Small desktops */
@media (max-width: 1280px) { ... }

/* Large desktops */
@media (min-width: 1281px) { ... }
```

---

## 🚀 DEPLOYMENT PIPELINE

### **Git → Netlify (Automatic):**
```
1. Developer commits to main branch
2. Push to GitHub
3. Netlify webhook triggers
4. Build command: npm run build (if needed)
5. Deploy to production
6. CDN cache invalidation
7. Live in ~30 seconds
```

### **Environment Variables:**
```bash
# In Netlify dashboard
SUPABASE_URL=https://nlgldaqtubrlcqddppbq.supabase.co
SUPABASE_ANON_KEY=eyJhbGci...
GOOGLE_AI_API_KEY=AIzaSyC...
```

---

## 🛠️ DEVELOPMENT TOOLS

### **Agent Coordination:**
```bash
# Check what other agents are doing
python3 scripts/agent-coordination-check.py

# Log your work
python3 scripts/log-agent-work.py
```

### **Knowledge Preservation:**
```bash
# Extract knowledge from archived MDs
python3 scripts/synthesize-knowledge-to-graphrag.py
```

### **Content Automation:**
```bash
# Add related resources component
python3 scripts/add-related-resources-component.py

# Index new resources to GraphRAG
python3 scripts/index-generated-resources-to-graphrag.py

# Apply unified design
python3 scripts/apply-unified-design-to-y8.py
```

---

## 📦 DEPENDENCIES

### **Frontend:**
```json
{
  "dependencies": {
    "@supabase/supabase-js": "^2.38.0",
    "vite": "^5.0.0"
  }
}
```

### **Python (Backend/Scripts):**
```txt
supabase==2.0.0
beautifulsoup4==4.12.0
lxml==5.0.0
requests==2.31.0
```

---

## 🔧 API INTEGRATIONS

### **Supabase MCP:**
```json
{
  "mcpServers": {
    "supabase": {
      "url": "https://mcp.supabase.com/mcp?project_ref=nlgldaqtubrlcqddppbq"
    }
  }
}
```

### **KAMAR (Placeholder):**
```javascript
// Future integration for NZ schools
async function fetchKAMARData(schoolCode, apiKey) {
  // Will integrate with KAMAR API
  // For class lists, timetables, etc.
}
```

---

## ♿ ACCESSIBILITY STANDARDS

### **WCAG 2.1 AA Compliance:**
- ✅ Semantic HTML5
- ✅ ARIA labels where needed
- ✅ Keyboard navigation support
- ✅ Color contrast ratios (4.5:1 minimum)
- ✅ Skip navigation links
- ✅ Alt text for images
- ✅ Responsive text sizing
- ✅ Focus indicators

---

## 🎯 PERFORMANCE TARGETS

### **Metrics:**
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Time to Interactive: < 3.0s
- Cumulative Layout Shift: < 0.1

### **Optimizations:**
- ✅ CSS consolidation (86.8% reduction)
- ✅ Image lazy loading
- ✅ Cache-Control headers
- ✅ Minification (via Netlify)
- ✅ CDN delivery

---

## 🔒 SECURITY

### **Authentication:**
- JWT tokens (Supabase)
- Row Level Security (RLS) policies
- Secure password hashing
- Email verification
- Rate limiting

### **Data Protection:**
- HTTPS everywhere
- Secure headers (CSP, HSTS)
- Input sanitization
- SQL injection prevention (parameterized queries)
- XSS protection

---

## 📊 MONITORING

### **Available:**
- Netlify Analytics (traffic)
- Supabase Dashboard (database)
- Browser DevTools (performance)

### **Future:**
⏳ Error tracking (Sentry)  
⏳ User analytics (privacy-respecting)  
⏳ Performance monitoring (real user metrics)  

---

**For questions, check `ACTIVE_QUESTIONS.md` or query GraphRAG!**

**— Maintained by Te Kete Ako Agent Team**

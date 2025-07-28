# 📚 Te Kete Ako - Complete Site Documentation

**Last Updated:** July 28, 2025  
**Resource Count:** ~190 resources  
**Live Site:** https://tekete.netlify.app/  
**Status:** Production Active

---

## 🎯 MISSION STATEMENT

> "These resources could nourish the minds of so many young people if our overall site is good enough. But if we are anything short of great, no one will bother to migrate here at all."

Te Kete Ako serves as a comprehensive educational platform integrating mātauranga Māori with contemporary pedagogy, serving teachers and students across Aotearoa New Zealand.

---

## 📊 RESOURCE INVENTORY OVERVIEW

### Current Resource Distribution

| Category | Live Site Count | Local Development | Status |
|----------|----------------|-------------------|--------|
| **Unit Plans** | 12 complete units | 13+ units | ⚠️ Y8 Systems missing from live |
| **Lesson Plans** | 85+ individual lessons | 90+ lessons | ✅ Mostly synced |
| **Handouts** | 90+ printable resources | 95+ resources | ✅ Well maintained |
| **Activities/Do Nows** | 25+ quick activities | 30+ activities | ✅ Active |
| **Games** | 8 interactive games | 10+ games | ✅ Functional |
| **Assessment Tools** | 15+ rubrics/frameworks | 20+ tools | ⚠️ Some enhanced versions local |
| **Cultural Resources** | 30+ Te Ao Māori materials | 35+ materials | ✅ Strong foundation |

**TOTAL ESTIMATED:** ~190 resources across all categories

---

## 🏗️ TECHNICAL ARCHITECTURE

### Frontend Stack
- **Framework:** Static HTML/CSS/JavaScript
- **Styling:** Custom CSS with CSS Grid/Flexbox
- **PWA:** Service Worker implementation
- **Authentication:** Supabase Auth
- **Hosting:** Netlify with automated deploys

### Backend Infrastructure
- **Database:** Supabase PostgreSQL
- **Authentication:** Supabase Auth with RLS policies
- **File Storage:** Supabase Storage
- **API Functions:** Netlify Functions
- **Content Delivery:** Netlify Edge

---

## 🗄️ ACTUAL SUPABASE DATABASE SCHEMA

**Schema Files:** 
- `agent-knowledge-hub/architecture/supabase-schema.sql` - Main user/analytics schema
- `resources-table-schema.sql` - Resource catalog system

### Core Tables (As Implemented)

#### `profiles` Table (User Management)
```sql
CREATE TABLE profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE UNIQUE NOT NULL,
    email TEXT NOT NULL,
    role TEXT CHECK (role IN ('teacher', 'student', 'admin')) NOT NULL,
    display_name TEXT,
    school_name TEXT DEFAULT 'Mangakōtukutuku College',
    year_level INTEGER CHECK (year_level BETWEEN 7 AND 13),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_login TIMESTAMP WITH TIME ZONE
);
```

#### `resources` Table (Resource Management)
```sql
CREATE TABLE resources (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    path TEXT NOT NULL, -- file path or URL to the resource
    type TEXT NOT NULL CHECK (type IN ('handout', 'lesson', 'game', 'unit-plan', 'assessment', 'activity', 'video', 'interactive')),
    subject TEXT NOT NULL, -- e.g., 'English', 'Social Studies', 'Te Reo Māori'
    level TEXT NOT NULL, -- e.g., 'Year 7', 'Year 8', 'All Levels'
    featured BOOLEAN DEFAULT FALSE,
    tags TEXT[] DEFAULT '{}',
    curriculum_alignment JSONB DEFAULT '{}', -- NZ Curriculum achievement objectives
    cultural_elements JSONB DEFAULT '{}', -- Te Ao Māori integration details
    difficulty_level TEXT CHECK (difficulty_level IN ('beginner', 'intermediate', 'advanced')) DEFAULT 'intermediate',
    estimated_duration_minutes INTEGER,
    author TEXT DEFAULT 'Te Kete Ako Team',
    is_active BOOLEAN DEFAULT TRUE
);
```

#### `student_projects` Table (Project Submissions)
```sql
CREATE TABLE student_projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    teacher_id UUID REFERENCES auth.users(id),
    project_type TEXT NOT NULL, -- 'society-design', 'do-now-response', 'collaborative-project'
    title TEXT NOT NULL,
    description TEXT,
    content JSONB NOT NULL, -- Flexible structure for different project types
    group_members JSONB DEFAULT '[]', -- Array of student IDs for group projects
    submission_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    status TEXT CHECK (status IN ('draft', 'submitted', 'under_review', 'reviewed', 'approved', 'needs_revision')) DEFAULT 'draft',
    teacher_feedback TEXT,
    grade TEXT,
    cultural_elements JSONB DEFAULT '[]', -- Track Te Ao Māori integration
    file_attachments JSONB DEFAULT '[]',
    peer_reviews JSONB DEFAULT '[]'
);
```

#### `learning_sessions` Table (Analytics)
```sql
CREATE TABLE learning_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    session_start TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    session_end TIMESTAMP WITH TIME ZONE,
    page_views JSONB DEFAULT '[]',
    interactions JSONB DEFAULT '[]',
    cultural_engagement_score INTEGER DEFAULT 0,
    total_time_minutes INTEGER DEFAULT 0,
    device_type TEXT,
    ip_address INET
);
```

#### `collaboration_records` Table (Group Work Tracking)
```sql
CREATE TABLE collaboration_records (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID REFERENCES student_projects(id) ON DELETE CASCADE,
    student_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    role TEXT NOT NULL, -- 'design-leader', 'research-coordinator', 'cultural-consultant', etc.
    contribution_log JSONB DEFAULT '[]',
    peer_evaluations JSONB DEFAULT '[]',
    weekly_reflections JSONB DEFAULT '[]',
    collaboration_score INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### `teacher_analytics` Table (Dashboard Data)
```sql
CREATE TABLE teacher_analytics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    teacher_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    date DATE DEFAULT CURRENT_DATE,
    active_students INTEGER DEFAULT 0,
    submissions_pending INTEGER DEFAULT 0,
    submissions_reviewed INTEGER DEFAULT 0,
    engagement_metrics JSONB DEFAULT '{}',
    cultural_integration_score DECIMAL(3,2),
    top_performing_students JSONB DEFAULT '[]',
    areas_needing_support JSONB DEFAULT '[]'
);
```

### Database Functions Available
- `get_resources_by_type(resource_type TEXT)` - Get resources filtered by type
- `search_resources(search_term TEXT)` - Full-text search with relevance scoring
- `update_updated_at_column()` - Automatic timestamp updates

### RLS Policies (Fully Implemented)
- **Complex multi-table policies** with proper teacher/student/admin role separation
- **Group project access** via JSONB array membership checking
- **Year-level targeted announcements** via dynamic policy checking
- **Cultural analytics tracking** with appropriate privacy controls

---

## 📁 CRITICAL FILE LOCATIONS

### Core HTML Pages (Live Site)
```
📁 Root Directory
├── index.html (Main landing page)
├── unit-plans.html (Unit hub with 12 complete units)
├── lessons.html (85+ individual lessons)
├── handouts.html (90+ printable resources)
├── activities.html (25+ do now activities)
├── games.html (8 interactive games)
├── other-resources.html (Assessment tools & external links)
├── teacher-dashboard.html (Teacher analytics - needs Supabase connection)
├── student-dashboard.html (Student portal)
├── login.html (Authentication)
├── register.html (User registration)
└── my-kete.html (Personal resource collection)
```

### Content Hierarchies
```
📁 units/
├── unit-1-te-ao-maori.html
├── unit-2-decolonized-history.html
├── unit-3-media-literacy.html
├── unit-4-economic-justice.html
├── unit-5-environmental-justice.html
├── unit-6-future-rangatiratanga.html
└── lessons/ (Individual lesson files)

📁 handouts/
├── Basic handouts (treaty, comprehension, etc.)
├── enhanced/ (Advanced versions)
└── video-activities/ (Multimedia resources)

📁 games/
├── te-reo-wordle.html (Working Te Reo game)
├── countdown-letters.html (Letter game)
└── categories.html (Word categories)
```

### Critical Missing from Live
```
📁 y8-systems/ (MISSING FROM LIVE SITE)
├── y8-systems-unit.html (Complete 5-week unit)
├── lessons/ (10 detailed lesson plans)
└── resources/ (20+ supporting materials)
```

---

## 🔐 AUTHENTICATION SYSTEM STATUS

### Current Implementation (Live Site)
- **Provider:** Supabase Auth
- **Features Working:**
  - User registration
  - Email/password login
  - My Kete bookmark system
  - Role-based access (student/teacher/admin)
  - Profile management

### Environment Variables (Netlify)
```
SUPABASE_URL=https://nlgldaqtubrlcqddppbq.supabase.co
SUPABASE_ANON_KEY=[Configured in Netlify]
SUPABASE_SERVICE_ROLE_KEY=[Configured in Netlify]
```

### Authentication Flow
1. User registers/logs in via Supabase Auth
2. Profile created automatically via database trigger
3. Role assignment (default: student)
4. Access to personalized features (My Kete, dashboards)

---

## 🎮 INTERACTIVE FEATURES STATUS

### Working Games (Live Site)
- ✅ **Te Reo Māori Wordle** - Fully functional
- ✅ **Countdown Letters** - Working letter game
- ✅ **Categories** - Word categorization game
- ✅ **Spelling Bee** - Educational spelling game

### Enhanced Features (Local Development)
- 🔄 **Society Design Tool** - Interactive planning (needs deployment)
- 🔄 **Enhanced Search** - Improved search functionality (needs deployment)
- 🔄 **Content Hierarchy** - Better resource organization (needs deployment)

---

## 🌍 CULTURAL INTEGRATION

### Te Ao Māori Elements
- **Bilingual Navigation:** English/Te Reo Māori throughout
- **Cultural Protocols:** Respectful integration of mātauranga Māori
- **Whakataukī:** Proverbs integrated into learning contexts
- **Decolonized Pedagogy:** Alternative approaches to Western education
- **Community Connections:** Links to whānau and iwi perspectives

### Cultural Resources Count
- **Te Ao Māori Category:** 30+ dedicated resources
- **Cross-curricular Integration:** Cultural elements in 80%+ of resources
- **Assessment Frameworks:** Culturally responsive evaluation tools

---

## 📈 ANALYTICS & MONITORING

### Current Tracking (Needs Enhancement)
- **Basic Metrics:** Page views, user registrations
- **User Engagement:** Resource bookmarks, game completions
- **Teacher Dashboard:** Student progress tracking (needs Supabase connection)

### Recommended Enhancements
- **Resource Usage Analytics**
- **Learning Pathway Tracking**
- **Cultural Engagement Metrics**
- **Community Impact Measurement**

---

## ⚠️ KNOWN ISSUES & GAPS

### High Priority
1. **Y8 Systems Unit Missing** - Complete 5-week program not on live site
2. **Teacher Dashboard** - Static content, needs Supabase integration
3. **Project Submissions** - Student submission system needs backend connection

### Medium Priority
4. **Search Enhancement** - Better filtering and discovery needed
5. **Mobile Navigation** - Some UX improvements needed for tablets
6. **Resource Tagging** - Inconsistent categorization across resources

### Low Priority
7. **Performance Optimization** - Image compression and lazy loading
8. **Accessibility** - Screen reader and keyboard navigation improvements

---

## 📋 MAINTENANCE CHECKLIST

### Weekly Tasks
- [ ] Check authentication system functionality
- [ ] Verify all games are working
- [ ] Test mobile responsiveness
- [ ] Monitor user feedback

### Monthly Tasks
- [ ] Resource count audit
- [ ] Supabase database health check
- [ ] Performance metrics review
- [ ] Cultural content review with kaumātua

### Quarterly Tasks
- [ ] Comprehensive link checking
- [ ] Curriculum alignment review
- [ ] User experience testing
- [ ] Security audit

---

## 🚨 EMERGENCY CONTACTS & PROCEDURES

### Technical Issues
1. **Netlify Deployment Issues:** Check build logs, verify environment variables
2. **Supabase Outage:** Monitor status page, implement local auth fallback
3. **Authentication Problems:** Verify RLS policies, check user roles
4. **Content Issues:** Revert to last known good deployment

### Content Issues
1. **Cultural Sensitivity Concerns:** Consult with cultural advisors immediately
2. **Curriculum Misalignment:** Review with education specialists
3. **Resource Accuracy:** Fact-check and update as needed

---

## 📚 RESOURCE CATEGORIES BREAKDOWN

### Unit Plans (12+ Complete Units)
1. **Te Ao Māori - Cultural Identity & Knowledge Systems**
2. **Decolonized Aotearoa History** 
3. **Media Literacy Skills**
4. **Economic Justice**
5. **Environmental Justice**
6. **Future Rangatiratanga**
7. **Individual Lesson Plans Collection**
8. **Design Your Society Unit** (Local only)
9. **Living Systems Unit**
10. **Digital Citizenship Unit**
11. **Creative Writing Unit**
12. **Mathematics Integration Unit**
13. **Y8 Systems Unit** ⚠️ (Missing from live)

### Handouts (90+ Resources)
- Treaty of Waitangi materials
- Comprehension activities
- Writing toolkits
- Environmental literacy
- Mathematical reasoning
- Assessment rubrics
- Cultural context materials

### Games & Interactive (8+ Working)
- Te Reo Māori Wordle
- Countdown Letters
- Categories word game
- Spelling Bee
- English Wordle
- Reading comprehension games
- Mathematical games
- Cultural knowledge games

---

## 🔄 DEPLOYMENT NOTES FOR FUTURE AGENTS

### Critical Deployment Steps
1. **Never modify live authentication** without testing
2. **Always backup database** before schema changes
3. **Test cultural content** with appropriate advisors
4. **Verify mobile functionality** after any changes
5. **Maintain resource count tracking** in this document

### Safe Deployment Process
1. Test all changes locally
2. Deploy to staging environment
3. Cultural and educational content review
4. User acceptance testing
5. Production deployment with monitoring

---

**Document Maintained By:** Development Team  
**Next Review:** Monthly  
**Contact:** Technical and Cultural Advisory Team

*This documentation serves as the single source of truth for Te Kete Ako's current state and should be updated with any significant changes.*
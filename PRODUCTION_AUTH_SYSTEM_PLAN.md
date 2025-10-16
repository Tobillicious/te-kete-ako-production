# 🔐 PRODUCTION AUTHENTICATION SYSTEM - NZ EDUCATION

**Date:** October 16, 2025  
**Status:** PLANNING → BUILDING  
**Goal:** Real, working auth for Te Kete Ako production platform

---

## 🎯 **USER REQUIREMENTS:**

### **Student Accounts:**
```
Required Data Collection:
✅ Name (first, last)
✅ Email (school or personal)
✅ School name (dropdown of NZ schools)
✅ Year level (7, 8, 9, 10, 11, 12, 13)
✅ Age/DOB
✅ Gender (inclusive options)
✅ Cultural identity (Māori, Pasifika, Pākehā, Asian, Other)
✅ Iwi affiliation (if Māori)
✅ Preferred language (English, Te Reo Māori, both)

Purpose:
→ Personalize content based on year level
→ Show culturally relevant resources
→ Track learning progression
→ Provide age-appropriate materials
```

### **Teacher Accounts:**
```
Required Data Collection:
✅ Name (title, first, last)
✅ Email (school email required)
✅ School name (must match real NZ school)
✅ Subjects taught (multi-select)
✅ Year levels taught (multi-select 7-13)
✅ Registration number (NZ Teachers Council)
✅ Role (Classroom Teacher, HOD, DP, Principal)

KAMAR Integration:
✅ KAMAR school code
✅ API key/credentials (if available)
✅ Import class lists
✅ Import timetable
✅ Sync student data

Purpose:
→ Manage class lists
→ Assign resources to classes
→ Track student progress
→ Access curriculum-aligned materials
→ Generate reports
```

---

## 📊 **CURRENT STATE AUDIT:**

### **Existing Auth Files (CONFLICTS!):**
```
❌ /public/js/auth-ui.js
❌ /public/js/auth-enhanced.js
❌ /public/js/auth-diagnostics.js
❌ /public/js/auth-resilience.js
❌ /public/js/supabase-auth.js
❌ /public/js/secure-auth.js

Problem: 6 different auth implementations!
```

### **Existing Database:**
```
✅ Supabase connected (nlgldaqtubrlcqddppbq)
✅ auth.users table (Supabase built-in)
✅ public.profiles table (basic)

Current profiles schema:
- id (uuid)
- user_id (uuid)
- email (text)
- role (text) - only 'teacher', 'student', 'admin'
- display_name (text)
- school_name (text)
- year_level (integer) - only one field!
- created_at, updated_at, last_login

❌ MISSING: gender, culture, iwi, subjects, KAMAR data, etc!
```

---

## 🏗️ **ARCHITECTURE PLAN:**

### **Phase 1: Database Schema (30 mins)**

**Extend profiles table:**
```sql
ALTER TABLE public.profiles ADD COLUMN IF NOT EXISTS:
- first_name text
- last_name text
- title text (Mr, Mrs, Ms, Dr, etc)
- date_of_birth date
- gender text (Male, Female, Non-binary, Prefer not to say, Other)
- cultural_identity text[] (array for multiple)
- iwi_affiliation text
- preferred_language text (en, mi, both)
- registration_number text (teachers only)
- teacher_role text (Classroom Teacher, HOD, DP, Principal)
- subjects_taught jsonb (teachers)
- year_levels_taught integer[] (teachers)
- kamar_school_code text (teachers)
- kamar_api_key text (encrypted, teachers)
- class_lists jsonb (teachers)
- timetable jsonb (teachers)
- personalization_settings jsonb (both)
- consent_given boolean
- terms_accepted_at timestamp
```

**New tables:**
```sql
CREATE TABLE nz_schools (
  id uuid PRIMARY KEY,
  name text NOT NULL,
  location text,
  region text,
  school_type text, -- Intermediate, Secondary, Composite
  decile integer,
  kamar_enabled boolean DEFAULT false,
  created_at timestamp DEFAULT now()
);

CREATE TABLE teacher_classes (
  id uuid PRIMARY KEY,
  teacher_id uuid REFERENCES profiles(user_id),
  class_name text,
  year_level integer,
  subject text,
  students jsonb[], -- array of student user_ids
  created_at timestamp DEFAULT now()
);

CREATE TABLE student_progress (
  id uuid PRIMARY KEY,
  student_id uuid REFERENCES profiles(user_id),
  resource_id uuid REFERENCES resources(id),
  progress_percentage integer DEFAULT 0,
  completed_at timestamp,
  score integer,
  time_spent_minutes integer,
  created_at timestamp DEFAULT now()
);
```

### **Phase 2: Auth UI Components (1 hour)**

**Sign Up Flow:**
```
1. /signup.html
   → Choose role: Student or Teacher
   
2a. Student Sign-Up (/signup-student.html)
   Step 1: Basic Info (name, email, password)
   Step 2: School Details (school dropdown, year level)
   Step 3: Personal (DOB, gender, culture, iwi)
   Step 4: Preferences (language, consent)
   Step 5: Email verification
   
2b. Teacher Sign-Up (/signup-teacher.html)
   Step 1: Basic Info (title, name, email, password)
   Step 2: Professional (school, registration #, role)
   Step 3: Teaching (subjects, year levels)
   Step 4: KAMAR (optional, school code + API key)
   Step 5: Email verification
   Step 6: Admin approval (for teachers)
```

**Login Flow:**
```
1. /login.html
   → Email + password
   → Redirect based on role:
      - Students → /student-portal.html
      - Teachers → /teachers/dashboard.html
      - Admin → /admin/dashboard.html
```

### **Phase 3: Student Portal (45 mins)**

**Features:**
```
/student-portal.html
- Personalized greeting ("Kia ora, [Name]!")
- Recommended resources (based on year level, culture)
- Recent activity
- Saved resources (My Kete)
- Progress tracking
- Achievements/badges
- Cultural content highlights
```

### **Phase 4: Teacher Dashboard (1 hour)**

**Features:**
```
/teachers/dashboard.html (REAL, not demo!)
- Class management
  - View all classes
  - Student lists
  - Assign resources
  - Track progress
  
- Timetable view (if KAMAR integrated)
- Resource library (filtered by year levels taught)
- Create/edit custom resources
- Assessment tracking
- Reports generation
- Professional development resources
```

### **Phase 5: KAMAR Integration Research (30 mins)**

**Requirements:**
```
1. Research KAMAR API documentation
2. Identify auth requirements
3. Determine what data can be synced:
   - Class lists
   - Timetables
   - Student info (with permission)
   
4. Build initial integration endpoints:
   - /api/kamar/authenticate
   - /api/kamar/sync-classes
   - /api/kamar/sync-timetable
   
5. Create fallback: Manual CSV upload if KAMAR unavailable
```

---

## 🔧 **IMPLEMENTATION PLAN:**

### **Step 1: Clean Up Auth Conflicts (15 mins)**
```bash
# Consolidate 6 auth files into ONE canonical file
→ /public/js/auth-production.js

# Archive old files
→ Move to /archive/auth-legacy/
```

### **Step 2: Database Migration (30 mins)**
```sql
# Create migration file
→ /supabase/migrations/20251016_nz_education_schema.sql

# Run migration via MCP
→ Apply to production Supabase
```

### **Step 3: NZ Schools Data (20 mins)**
```javascript
# Populate nz_schools table with real NZ schools
→ Import Ministry of Education school list
→ ~2,500 schools
→ Include regions, deciles, school types
```

### **Step 4: Build Sign-Up Forms (1.5 hours)**
```html
# Student sign-up
→ /public/signup-student.html
→ Multi-step form with validation
→ Cultural inclusivity (gender, iwi, etc)
→ Privacy consent clear

# Teacher sign-up
→ /public/signup-teacher.html  
→ Professional validation
→ KAMAR optional integration
→ Admin approval workflow
```

### **Step 5: Build Dashboards (2 hours)**
```html
# Student portal
→ /public/student-portal.html
→ Personalized content
→ Progress tracking
→ Culturally responsive

# Teacher dashboard (PRODUCTION, rename from demo!)
→ /public/teachers/dashboard.html
→ Class management
→ Resource assignment
→ Student progress tracking
→ Real functionality, no placeholders
```

### **Step 6: Role-Based Access Control (30 mins)**
```javascript
# Middleware
→ /public/js/auth-middleware.js
→ Check user role on protected pages
→ Redirect if unauthorized
→ Load role-specific UI
```

---

## 📋 **NZ-SPECIFIC FEATURES:**

### **School Dropdown:**
```javascript
// Real NZ schools from Ministry of Education
[
  "Mangakōtukutuku College",
  "Auckland Grammar School",
  "Wellington High School",
  "Christchurch Boys' High School",
  "Otago Girls' High School",
  // ... ~2,500 more schools
]
```

### **Cultural Identity Options:**
```javascript
[
  "Māori",
  "NZ European/Pākehā",
  "Pacific Peoples",
  "Asian",
  "Middle Eastern",
  "Latin American",
  "African",
  "Other",
  "Prefer not to say"
]
```

### **Iwi Affiliation:**
```javascript
// Major iwi (user can type if not in list)
[
  "Ngāpuhi",
  "Ngāti Porou",
  "Ngāi Tahu",
  "Waikato",
  "Tūhoe",
  "Te Arawa",
  // ... ~100 more iwi
]
```

### **Subjects (NZ Curriculum):**
```javascript
[
  "English",
  "Mathematics",
  "Science",
  "Social Studies",
  "Te Reo Māori",
  "Digital Technologies",
  "Health & Physical Education",
  "The Arts",
  "Technology",
  "Languages (other)"
]
```

---

## ⚡ **QUICK WINS (Start Here):**

### **1. Clean Auth Files (NOW)**
```
Delete/archive 5 of 6 auth files
Keep only ONE: auth-production.js
Update all pages to use canonical auth
```

### **2. Extend Database (30 mins)**
```
Create migration with NZ-specific fields
Apply to Supabase
Test with dummy data
```

### **3. Basic Sign-Up Form (1 hour)**
```
Build student sign-up first
NZ schools dropdown
Year level selector
Cultural identity (inclusive)
Email verification
```

---

## 🎯 **SUCCESS CRITERIA:**

**For Oct 22 Presentation:**
```
✅ Students can sign up with NZ-specific data
✅ Teachers can sign up with professional info
✅ Login works and redirects by role
✅ Student portal shows personalized content
✅ Teacher dashboard has REAL class management
✅ No placeholder text - all functional
✅ KAMAR integration endpoint exists (even if basic)
✅ Data collection complies with NZ Privacy Act
```

---

## 📊 **TIMELINE:**

**Total: ~8 hours work**

```
Hour 1: Clean auth conflicts + database migration
Hour 2: NZ schools data + basic schema
Hour 3-4: Student sign-up form (full featured)
Hour 5: Teacher sign-up form
Hour 6-7: Dashboards (student portal + teacher)
Hour 8: KAMAR research + integration prep + testing
```

---

## 🔐 **PRIVACY & COMPLIANCE:**

### **NZ Privacy Act 2020:**
```
✅ Clear consent for data collection
✅ Explain why each field is collected
✅ Allow users to update/delete data
✅ Secure storage (Supabase encryption)
✅ Age-appropriate (13+ with parental consent)
✅ School approval for under-16 students
```

### **Terms & Conditions:**
```
✅ Create /legal/terms.html
✅ Create /legal/privacy.html
✅ Require acceptance on sign-up
✅ Log acceptance timestamp
```

---

## 🚀 **LET'S BUILD IT!**

**Next Step:** Shall I start with:

**A)** Clean up auth conflicts + database migration (foundation)
**B)** Build student sign-up form first (visible progress)
**C)** Build teacher dashboard (the "real" production feature)

**Your call!** This is REAL production work - exactly what you need! 🧺✨

**— Kaitiaki Aronui V3.0**  
*Building authentic NZ education platform!*


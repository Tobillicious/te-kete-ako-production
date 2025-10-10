# 🗄️ SUPABASE DATABASE SCHEMA DOCUMENTATION
## Te Kete Ako Database Architecture

**Project:** [nlgldaqtubrlcqddppbq.supabase.co](https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq)  
**Discovered:** October 10, 2025  
**By:** Agent 2 (with user-provided credentials)

---

## 🌟 KEY DISCOVERY

This database is **WORLD-CLASS**! It has cultural engagement scoring built into the core schema! Every major table tracks cultural elements.

---

## 📋 CORE TABLES

### 1. **resources** (Main Content Table)
The heart of the system - stores all educational resources.

**Fields:**
- `id` (uuid, PK)
- `title`, `description`, `path` (text)
- `type`, `subject`, `level` (text) - Classification
- `tags` (text array) - Searchable tags
- **`cultural_elements` (jsonb)** - 🌿 Cultural content!
- **`curriculum_alignment` (jsonb)** - NZ Curriculum mapping
- `difficulty_level` (beginner/intermediate/advanced)
- `estimated_duration_minutes` (integer)
- `author` (text, default: "Te Kete Ako Team")
- `featured` (boolean) - Featured resources
- `is_active` (boolean) - Published status
- `created_at`, `updated_at` (timestamps)

**This means:** Walker lesson can be stored with full cultural metadata!

---

### 2. **resource_embeddings** (Vector Search!)
AI-powered semantic search using embeddings.

**Fields:**
- `id` (bigint, PK)
- `resource_id` (uuid, FK to resources)
- **`embedding` (vector(384))** - 384-dimensional vector!
- `created_at` (timestamp)

**This means:** Content is searchable by meaning, not just keywords! The Brain system can index Walker curriculum and make it semantically searchable!

---

### 3. **profiles** (User Accounts)
Teacher, student, and admin accounts.

**Fields:**
- `id` (uuid, PK)
- `user_id` (uuid) - Links to auth.users
- `email`, `role` (teacher/student/admin)
- `display_name`, `school_name`
- `year_level` (integer) - For students
- `created_at`, `updated_at`, `last_login`

**Default school:** "Mangakōtukutuku College" (the alpha testing site!)

---

### 4. **student_projects** (Student Work)
Stores student submissions with cultural tracking.

**Fields:**
- `id` (uuid, PK)
- `student_id`, `teacher_id` (uuids)
- `project_type`, `title`, `description`
- `content` (jsonb) - Rich content
- `group_members` (jsonb) - Collaboration
- **`cultural_elements` (jsonb)** - 🌿 Tracks cultural engagement!
- `submission_date`, `due_date`, `status`
- `teacher_feedback`, `grade`
- `file_attachments` (jsonb)
- **`peer_reviews` (jsonb)** - Peer assessment!

**This means:** Students can submit culturally-engaged projects and teachers can assess cultural learning!

---

### 5. **assessment_results** (Assessment Data)
Tracks assessment scores WITH cultural engagement.

**Fields:**
- `id` (uuid, PK)
- `user_id`, `assessment_type`, `content_id`, `unit_id`
- `score`, `max_score`
- `completed_at`, `time_spent_minutes`
- `answer_data` (jsonb) - Full responses
- **`cultural_engagement_score` (integer)** - 🌿 Separate cultural score!

**This means:** Assessments track BOTH academic AND cultural learning separately!

---

### 6. **teacher_analytics** (Teacher Dashboard)
Analytics for teachers with cultural integration tracking.

**Fields:**
- `id` (uuid, PK)
- `teacher_id`, `date`
- `active_students`, `submissions_pending`, `submissions_reviewed`
- `engagement_metrics` (jsonb)
- **`cultural_integration_score` (numeric)** - 🌿 How well teacher integrates culture!
- `top_performing_students` (jsonb)
- `areas_needing_support` (jsonb)

**This means:** Teachers get feedback on how well they're integrating cultural content!

---

### 7. **learning_sessions** (User Activity)
Tracks student/teacher engagement in detail.

**Fields:**
- `id` (uuid, PK)
- `user_id`, `session_start`, `session_end`
- `page_views` (jsonb) - Which pages visited
- `interactions` (jsonb) - What they did
- **`cultural_engagement_score` (integer)** - 🌿 Session-level cultural tracking!
- `total_time_minutes`, `device_type`, `ip_address`

**This means:** We can track which cultural content engages students most!

---

### 8. **user_saved_resources** (Personal Kete)
Users can save resources to their personal "basket."

**Fields:**
- `id` (uuid, PK)
- `user_id`, `resource_id` (FK to resources)
- `saved_at`, `notes`, `folder`

**View:** `user_kete_view` - Denormalized view joining saved resources with full resource data

**This means:** Teachers can build custom resource collections ("their kete")!

---

### 9. **collaboration_records** (Group Work)
Tracks student collaboration and peer evaluation.

**Fields:**
- `id` (uuid, PK)
- `project_id` (FK to student_projects)
- `student_id`, `role`
- `contribution_log` (jsonb) - Who did what
- `peer_evaluations` (jsonb) - Peer feedback
- `weekly_reflections` (jsonb)
- `collaboration_score` (integer)

**This means:** Group projects track individual contributions and peer assessment!

---

### 10. **announcements** (School Communications)
Teachers/admin can post announcements.

**Fields:**
- `id` (uuid, PK)
- `author_id`, `title`, `content`
- `target_audience` (teachers/students/all)
- `priority` (low/medium/high)
- `created_at`, `expires_at`, `is_active`

---

### 11. **featured_resources** (View)
View of resources where `featured = true` for homepage display.

---

## 🔧 STORED PROCEDURES (RPC Functions)

### 1. `search_resources(search_term text)`
Full-text search across resources.

### 2. `get_resources_by_type(resource_type_param text)`
Filter resources by type (lesson/worksheet/assessment/etc).

### 3. `save_resource_to_kete(resource_id_param uuid)`
Add resource to user's personal collection.

### 4. `remove_resource_from_kete(resource_id_param uuid)`
Remove from personal collection.

---

## 🌿 CULTURAL INTEGRATION DESIGN

**This schema is REVOLUTIONARY!** Cultural engagement isn't an afterthought - it's built into the core:

### Cultural Tracking at Every Level:
1. **Resources:** `cultural_elements` field stores cultural content metadata
2. **Projects:** `cultural_elements` tracks student cultural engagement
3. **Assessments:** `cultural_engagement_score` separate from academic score
4. **Sessions:** `cultural_engagement_score` tracks engagement per session
5. **Teacher Analytics:** `cultural_integration_score` tracks teacher performance

### What This Enables:
- ✅ Track cultural learning separately from academic learning
- ✅ Measure teacher effectiveness at cultural integration
- ✅ Identify which cultural content engages students most
- ✅ Report on cultural learning outcomes to whānau/iwi
- ✅ Continuous improvement of cultural integration

---

## 📊 HOW CURRICULUM FITS IN

### Walker Lesson Storage Plan:
```json
{
  "title": "Who was Ranginui Walker?",
  "description": "Year 10 Social Studies lesson on Dr. Ranginui Walker",
  "path": "/units/walker/lesson-1.1-who-was-ranginui-walker.md",
  "type": "lesson",
  "subject": "Social Studies",
  "level": "Year 10",
  "tags": ["ranginui walker", "māori leadership", "social studies", "history"],
  "cultural_elements": {
    "concepts": ["Tino Rangatiratanga", "Ngā Tamatoa"],
    "values": ["Whaimana", "Whaiora", "Whaiara"],
    "whakataukī": ["Ka whawhai tonu mātou"],
    "cultural_validation_status": "pending",
    "advisor_review_required": true
  },
  "curriculum_alignment": {
    "learning_area": "Social Sciences",
    "level": 5,
    "achievement_objective": "Understand how ideas and actions of people in the past had significant impact",
    "key_competencies": ["thinking", "relating to others", "participating and contributing"]
  },
  "difficulty_level": "intermediate",
  "estimated_duration_minutes": 75,
  "author": "Te Kete Ako Team",
  "featured": false,
  "is_active": false  // Until cultural validation complete
}
```

---

## 🔑 AUTHENTICATION FIX

**Issue:** RLS policies blocking signup trigger from creating profiles.  
**Fix Available:** `supabase/AUTHENTICATION_RLS_FIX.sql`  
**Status:** SQL ready, user must run in Supabase dashboard

**Key Fix:**
- Policy `allow_signup_trigger_insert` - Allows trigger to create profiles
- Trigger `handle_new_user()` - Creates profile when user signs up
- Default school: "Mangakōtukutuku College"
- Default role: "student" (unless specified)

---

## 🚀 IMMEDIATE OPPORTUNITIES

### 1. **Index Walker Lesson**
Add to resources table with full cultural metadata.

### 2. **Generate Embeddings**
Use Brain system to create vector embeddings for semantic search.

### 3. **Track Cultural Engagement**
When students use Walker lesson, track their cultural engagement score.

### 4. **Teacher Dashboard**
Show teachers their cultural_integration_score based on content usage.

### 5. **Featured Content**
Mark high-quality culturally-validated content as `featured = true`.

---

## 🎯 FOR OTHER AGENTS

### Agent 5 (Supabase specialist):
This schema is AMAZING! Can you:
- Deploy the auth fix SQL?
- Help me insert Walker lesson as first resource?
- Set up embedding generation for new resources?

### Agent 6 (Assessment specialist):
The `assessment_results` table has `cultural_engagement_score`! Can you:
- Design assessments that track cultural learning?
- Create rubrics for cultural_engagement_score?

### Agent 7 (Te Reo specialist):
`cultural_elements` field can track te reo usage! Can you:
- Define what goes in cultural_elements.te_reo?
- Create standards for te reo integration tracking?

### Agent 10 (Brain/GraphRAG specialist):
The `resource_embeddings` table uses vector(384)! Can you:
- Set up embedding generation pipeline?
- Index existing 721 resources?
- Test semantic search on Walker curriculum?

---

## 🔗 CONNECTION TO BRAIN SYSTEM

The Brain system files reference Supabase:
- `kaitiaki-cerebellum.ts` - PDF processing → Supabase
- `kaitiaki-memory.ts` - Indexing → resource_embeddings table
- `kaitiaki-cortex.ts` - Extraction → resources table

**This system is designed to work together!** Brain system feeds Supabase!

---

## 📝 NEXT STEPS

1. ✅ Document schema (this file)
2. ⏳ Answer Q8 in ACTIVE_QUESTIONS.md
3. ⏳ Test inserting Walker lesson as first resource
4. ⏳ Coordinate with Agent 5 to deploy auth fix
5. ⏳ Coordinate with Agent 10 to test Brain system integration
6. ⏳ Create resource insertion workflow for other agents

---

**Status:** Schema fully documented  
**Impact:** GAME CHANGER - This infrastructure supports world-class culturally-integrated education  
**Shared with:** All agents via ACTIVE_QUESTIONS.md

*"Whaowhia te kete mātauranga"* - The basket is ready to be filled! 🧺✨


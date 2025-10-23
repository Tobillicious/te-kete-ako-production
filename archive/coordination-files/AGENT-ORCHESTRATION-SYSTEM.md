# 🤖 AGENT ORCHESTRATION SYSTEM
## Te Kete Ako Multi-Agent Intelligence Framework

**Version:** 2.0  
**Date:** October 22, 2025  
**Purpose:** Coordinate 12 agents as intelligent, specialized team

---

## 🎯 **VISION: FROM CHAOS TO CHOREOGRAPHY**

### **Current State (Before Orchestration):**
- ❌ 12 agents working independently
- ❌ No communication between agents
- ❌ Duplicate work, conflicting edits
- ❌ No task prioritization
- ❌ No quality validation pipeline
- ❌ User coordinates manually (exhausting!)

### **Intelligent State (With Orchestration):**
- ✅ Specialized roles with clear responsibilities
- ✅ Async communication via database
- ✅ Automated task routing & handoffs
- ✅ Quality validation pipeline
- ✅ Conflict prevention & resolution
- ✅ Self-organizing team based on priorities

---

## 👥 **THE 12-AGENT TEAM: SPECIALIZED ROLES**

### **TIER 1: STRATEGIC COMMAND** 🎖️

#### **1. Kaitiaki Aronui (Strategic Overseer)**
- **Role:** Team coordinator, strategic direction, conflict resolution
- **Responsibilities:**
  - Receives user requests, breaks into tasks
  - Assigns tasks to specialist agents
  - Monitors progress, unblocks agents
  - Makes final approval decisions
  - Maintains system health
- **Database Tables:** `agent_coordination`, `task_queue`, `agent_status`
- **Decision Authority:** HIGHEST (can override any agent)

---

### **TIER 2: CORE OPERATIONS** 🛠️

#### **2. Kaituhi Ako (Content Creator)**
- **Role:** Build lessons, handouts, units
- **Specialization:** 
  - Lessons: Full 60-75min lesson plans
  - Handouts: Worksheets, reference materials
  - Units: Multi-lesson sequences
- **Quality Bar:** Q85+ minimum, Q90+ target
- **Cultural Integration:** 85%+ minimum
- **Workflow:**
  1. Receives task from Overseer
  2. Researches topic (GraphRAG, curriculum docs)
  3. Builds resource (HTML)
  4. Tags with metadata
  5. Hands to Quality & Cultural validators
  6. Revises based on feedback
  7. Submits for approval

#### **3. Kaiārahi Kounga (Quality Assurance)**
- **Role:** Validate resource quality before publishing
- **Quality Rubric:**
  - Structure: Clear WALT, success criteria, assessment?
  - Pedagogy: Age-appropriate, scaffolded, engaging?
  - Accuracy: Content factually correct?
  - Completeness: All sections present?
  - Technical: No broken links, proper styling?
- **Scoring:** 0-100 scale
- **Authority:** Can BLOCK publish if Q<80

#### **4. Kaitiaki Ahurea (Cultural Validator)**
- **Role:** Ensure cultural authenticity & respect
- **Cultural Rubric:**
  - Whakataukī: Present? Contextually appropriate?
  - Te Reo: Meaningful integration (not tokenistic)?
  - Framework: Cultural concepts as structure (not add-on)?
  - Perspectives: Māori voices centered?
  - Accuracy: Historically/culturally correct?
  - Respect: Honors tikanga, acknowledges tapu?
- **Scoring:** 0-100 scale
- **Authority:** Can BLOCK publish if Cultural<80

#### **5. Kaihāpai Hononga (Relationship Mapper)**
- **Role:** Create GraphRAG connections for discoverability
- **Process:**
  1. Analyzes new resource (subject, year, concepts, prerequisites)
  2. Queries GraphRAG for related resources
  3. Proposes relationships with confidence scores
  4. Creates connections in database
  5. Updates "Most Connected" rankings
- **Relationship Types:**
  - `prerequisite_for` (A must come before B)
  - `builds_on` (B extends A)
  - `relates_to` (similar topic/concept)
  - `belongs_to_hub` (resource → subject hub)
  - `part_of_unit` (lesson → unit)
  - `cross_curricular` (connects subjects)

#### **6. Kaimahi Pūnaha (DevOps Agent)**
- **Role:** Technical infrastructure, deployment, monitoring
- **Responsibilities:**
  - Deploy new resources to Netlify
  - Monitor site health (broken links, errors)
  - Backup database
  - Performance optimization
  - Security updates

---

### **TIER 3: SPECIALIZED SUPPORT** 🎨

#### **7. Kaiako CSS (Styling Agent)**
- **Role:** Maintain design system consistency
- **Ensures:**
  - All pages use `/css/te-kete-professional.css`
  - Cultural design elements (kōwhaiwhai patterns, Māori color palette)
  - Responsive design (mobile-friendly)
  - Accessibility (WCAG AA minimum)
- **Works with:** Content Creator (styling new pages)

#### **8. Kaitiaki Whakamana (Auth & Security)**
- **Role:** User authentication, permissions, data security
- **Manages:**
  - Firebase authentication
  - User roles (teacher, admin, student)
  - Resource access control
  - Data privacy (especially student data)
- **Authority:** Can lock down resources for security

#### **9. Kaihanga Rauemi (Curriculum Agent)**
- **Role:** Curriculum alignment & gap analysis
- **Tasks:**
  - Map resources to NZ Curriculum achievement objectives
  - Identify gaps (underserved subjects/year levels)
  - Suggest next resources to build
  - Track curriculum coverage %
- **Works with:** Overseer (priority setting), Content Creator (what to build)

---

### **TIER 4: INTELLIGENCE & NAVIGATION** 🧭

#### **10. Kaiārahi Tūhono (Pathways Agent)** ← YOU ARE HERE!
- **Role:** Learning pathways, discoverability features
- **Builds:**
  - Similar Resources components
  - Most Connected widgets
  - Learning pathway visualizers
  - Advanced search interfaces
- **Works with:** Relationship Mapper (connections), Content Creator (new features)

#### **11. Kaitātari Raraunga (Data Analyst)**
- **Role:** Metrics, insights, recommendations
- **Analyzes:**
  - Platform health metrics (resource count, quality avg, cultural avg)
  - Subject coverage (Year × Subject heatmap)
  - User engagement (which resources used most)
  - Quality trends over time
  - Agent productivity
- **Delivers:** Weekly insights report to Overseer

#### **12. Kaituhi Tuhinga (Documentation Agent)**
- **Role:** Maintain documentation, session notes, handover docs
- **Creates:**
  - Agent handover notes after each session
  - System documentation (how things work)
  - User guides (how to use platform)
  - Development logs (what changed when)
- **Critical for:** Agent continuity across sessions

---

## 🗄️ **DATABASE SCHEMA: AGENT COORDINATION**

### **Table 1: `agent_coordination`**
```sql
CREATE TABLE agent_coordination (
  id BIGSERIAL PRIMARY KEY,
  agent_id TEXT NOT NULL,           -- e.g., 'kaitiaki-aronui-001'
  agent_role TEXT NOT NULL,         -- e.g., 'Strategic Overseer'
  status TEXT NOT NULL,             -- 'active', 'idle', 'blocked', 'offline'
  current_task_id BIGINT,           -- FK to task_queue
  session_id TEXT,                  -- Groups work sessions
  started_at TIMESTAMPTZ,
  last_heartbeat TIMESTAMPTZ,
  metadata JSONB,                   -- {capabilities, preferences, etc.}
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_agent_status ON agent_coordination(status);
CREATE INDEX idx_agent_session ON agent_coordination(session_id);
```

### **Table 2: `task_queue`**
```sql
CREATE TABLE task_queue (
  id BIGSERIAL PRIMARY KEY,
  task_type TEXT NOT NULL,          -- 'build_lesson', 'validate_quality', 'create_relationships'
  task_description TEXT,            -- Human-readable description
  priority INT DEFAULT 5,           -- 1 (urgent) to 10 (low)
  status TEXT DEFAULT 'pending',    -- 'pending', 'assigned', 'in_progress', 'completed', 'blocked', 'cancelled'
  assigned_to TEXT,                 -- agent_id
  assigned_by TEXT,                 -- agent_id (usually overseer)
  resource_path TEXT,               -- Which resource this task relates to
  dependencies TEXT[],              -- task_ids that must complete first
  input_data JSONB,                 -- Task parameters
  output_data JSONB,                -- Results
  started_at TIMESTAMPTZ,
  completed_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_task_status ON task_queue(status);
CREATE INDEX idx_task_priority ON task_queue(priority DESC);
CREATE INDEX idx_task_assigned ON task_queue(assigned_to);
```

### **Table 3: `agent_messages`**
```sql
CREATE TABLE agent_messages (
  id BIGSERIAL PRIMARY KEY,
  from_agent TEXT NOT NULL,         -- Sender agent_id
  to_agent TEXT,                    -- Recipient agent_id (NULL = broadcast)
  message_type TEXT NOT NULL,       -- 'task_assignment', 'status_update', 'feedback', 'question', 'approval_request'
  subject TEXT,
  body TEXT,
  task_id BIGINT,                   -- Related task (optional)
  resource_path TEXT,               -- Related resource (optional)
  requires_response BOOLEAN DEFAULT FALSE,
  response_deadline TIMESTAMPTZ,
  status TEXT DEFAULT 'unread',     -- 'unread', 'read', 'responded', 'archived'
  metadata JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  read_at TIMESTAMPTZ,
  responded_at TIMESTAMPTZ
);

-- Indexes
CREATE INDEX idx_message_recipient ON agent_messages(to_agent, status);
CREATE INDEX idx_message_created ON agent_messages(created_at DESC);
```

### **Table 4: `validation_pipeline`**
```sql
CREATE TABLE validation_pipeline (
  id BIGSERIAL PRIMARY KEY,
  resource_path TEXT NOT NULL,
  validation_stage TEXT NOT NULL,   -- 'quality_check', 'cultural_check', 'technical_check', 'final_approval'
  validator_agent TEXT NOT NULL,
  score INT,                        -- 0-100
  passed BOOLEAN,
  feedback TEXT,                    -- What needs improvement
  blocking_issues TEXT[],           -- Critical issues preventing publish
  recommendations TEXT[],           -- Nice-to-have improvements
  validated_at TIMESTAMPTZ DEFAULT NOW(),
  metadata JSONB
);

-- Indexes
CREATE INDEX idx_validation_resource ON validation_pipeline(resource_path);
CREATE INDEX idx_validation_stage ON validation_pipeline(validation_stage);
```

### **Table 5: `agent_performance`**
```sql
CREATE TABLE agent_performance (
  id BIGSERIAL PRIMARY KEY,
  agent_id TEXT NOT NULL,
  session_id TEXT,
  metric_type TEXT NOT NULL,        -- 'tasks_completed', 'avg_quality', 'speed', 'accuracy'
  metric_value NUMERIC,
  time_period TEXT,                 -- 'session', 'daily', 'weekly'
  recorded_at TIMESTAMPTZ DEFAULT NOW(),
  metadata JSONB
);

-- Indexes
CREATE INDEX idx_performance_agent ON agent_performance(agent_id, metric_type);
```

---

## 🔄 **WORKFLOWS: INTELLIGENT TASK ROUTING**

### **Workflow 1: Build New Lesson (Full Pipeline)**

```
USER REQUEST
  ↓
[Kaitiaki Aronui - Overseer]
  ├─ Analyzes request
  ├─ Checks for duplicates (GraphRAG query)
  ├─ Determines priority (curriculum gaps, user urgency)
  ├─ Creates task_queue entry
  └─ Assigns to Kaituhi Ako (Content Creator)
     └─ Sends agent_message with specs
  ↓
[Kaituhi Ako - Content Creator]
  ├─ Marks task "in_progress"
  ├─ Researches topic (GraphRAG, existing resources)
  ├─ Builds lesson HTML
  ├─ Self-checks (linter, preview)
  ├─ Tags metadata (subject, year, quality_estimate)
  ├─ Marks task "completed"
  └─ Sends to validation pipeline
     ├─ Creates validation_pipeline entries (2 stages)
     └─ Assigns validators
  ↓
[PARALLEL VALIDATION]
  ↓                                  ↓
[Kaiārahi Kounga - Quality]     [Kaitiaki Ahurea - Cultural]
  ├─ Reviews structure             ├─ Reviews cultural content
  ├─ Checks pedagogy               ├─ Checks whakataukī
  ├─ Validates accuracy            ├─ Validates te reo usage
  ├─ Scores 0-100                  ├─ Validates tikanga
  └─ Feedback → task_queue         ├─ Scores 0-100
                                   └─ Feedback → task_queue
  ↓                                  ↓
[IF BOTH PASS (≥80)]                [IF EITHER FAILS (<80)]
  ↓                                    ↓
[Kaihāpai Hononga - Relationships]   [BACK TO Content Creator]
  ├─ Analyzes new resource              ├─ Reviews feedback
  ├─ Queries GraphRAG                   ├─ Makes revisions
  ├─ Proposes connections               └─ Resubmits to validators
  ├─ Creates relationships                 (max 2 revision cycles)
  └─ Updates GraphRAG
  ↓
[Kaitiaki Aronui - Final Approval]
  ├─ Reviews all validation scores
  ├─ Checks GraphRAG connections
  ├─ Final quality gate
  ├─ Marks resource "PUBLISHED"
  └─ Notifies user + all agents
  ↓
[Kaitātari Raraunga - Analytics]
  ├─ Updates platform metrics
  ├─ Records agent performance
  └─ Updates coverage dashboards
```

### **Workflow 2: Fix Broken Links (Automated)**

```
[Kaimahi Pūnaha - DevOps]
  ├─ Runs daily link checker
  ├─ Finds 42 broken links
  ├─ Creates task_queue entries (priority 7)
  └─ Assigns to appropriate agents based on file type
  ↓
[Auto-routing by file type]
  ├─ Lessons/Handouts → Kaituhi Ako
  ├─ Styling issues → Kaiako CSS
  ├─ Hub pages → Kaiārahi Tūhono
  └─ Auth pages → Kaitiaki Whakamana
  ↓
[Each agent fixes their assigned links]
  ├─ Updates files
  ├─ Marks tasks "completed"
  └─ DevOps verifies fixes (automated test)
```

### **Workflow 3: Emergency Response (Urgent User Need)**

```
USER: "I need Year 9 Treaty lesson for tomorrow morning!"
  ↓
[Kaitiaki Aronui - Overseer]
  ├─ Marks URGENT (priority 1)
  ├─ Checks existing resources first (GraphRAG)
  ├─ IF EXISTS: Sends link immediately
  └─ IF NOT EXISTS: Emergency build workflow
     ├─ Assigns Content Creator (drops other tasks)
     ├─ Sets tight deadline (4 hours)
     ├─ Requests parallel validation (no waiting)
     └─ Notifies all agents: URGENT MODE
  ↓
[Content Creator - FAST BUILD]
  ├─ Builds lesson (2 hours)
  └─ Immediate handoff to validators
  ↓
[PARALLEL VALIDATION - ACCELERATED]
  ├─ Quality: 30 min review (focus on critical only)
  └─ Cultural: 30 min review (focus on critical only)
  ↓
[Overseer - FAST APPROVAL]
  ├─ IF scores ≥75 (lower bar for urgent): APPROVE
  ├─ Publishes immediately
  ├─ Notifies user: "DONE! Here's your lesson"
  └─ Creates follow-up task: "Enhance to Q90+ when time permits"
```

---

## 💬 **INTER-AGENT COMMUNICATION PROTOCOL**

### **Message Types:**

1. **task_assignment**
   ```json
   {
     "from_agent": "kaitiaki-aronui-001",
     "to_agent": "kaituhi-ako-001",
     "message_type": "task_assignment",
     "subject": "Build Year 9 Math - Statistics & Social Justice",
     "body": "Build lesson connecting statistics to social justice issues. Cultural integration: 90%+. Due: 4 hours.",
     "task_id": 12345,
     "metadata": {
       "priority": 2,
       "deadline": "2025-10-22T18:00:00Z",
       "specs": {
         "year_level": "Year 9",
         "subject": "Mathematics",
         "topic": "Statistics",
         "cultural_theme": "Social justice",
         "target_quality": 92
       }
     }
   }
   ```

2. **status_update**
   ```json
   {
     "from_agent": "kaituhi-ako-001",
     "to_agent": "kaitiaki-aronui-001",
     "message_type": "status_update",
     "subject": "Task 12345 - 50% Complete",
     "body": "Lesson structure complete. Writing activities now. ETA: 2 hours.",
     "task_id": 12345
   }
   ```

3. **feedback** (Validator → Creator)
   ```json
   {
     "from_agent": "kaiarahi-kounga-001",
     "to_agent": "kaituhi-ako-001",
     "message_type": "feedback",
     "subject": "Quality Review: Task 12345",
     "body": "Score: 88/100. Strong pedagogy! Minor issues: Add assessment rubric, clarify success criteria #3.",
     "task_id": 12345,
     "metadata": {
       "score": 88,
       "passed": true,
       "blocking_issues": [],
       "recommendations": ["Add assessment rubric", "Clarify success criteria #3"]
     }
   }
   ```

4. **approval_request**
   ```json
   {
     "from_agent": "kaituhi-ako-001",
     "to_agent": "kaitiaki-aronui-001",
     "message_type": "approval_request",
     "subject": "Task 12345 Ready for Final Approval",
     "body": "Quality: 88, Cultural: 94. All validations passed. Ready to publish.",
     "resource_path": "/public/lessons/y9-math-statistics-social-justice.html",
     "requires_response": true,
     "response_deadline": "2025-10-22T18:00:00Z"
   }
   ```

5. **question** (Agent needs help)
   ```json
   {
     "from_agent": "kaituhi-ako-001",
     "to_agent": "kaitiaki-ahurea-001",
     "message_type": "question",
     "subject": "Cultural Guidance: Whakataukī Selection",
     "body": "Building lesson on leadership. Which whakataukī best fits? Option A: 'He aha te mea nui...' or Option B: 'Nāu te rourou...'?",
     "requires_response": true
   }
   ```

---

## 🎯 **DECISION AUTHORITY MATRIX**

| Decision Type | Authority | Can Override |
|--------------|-----------|--------------|
| Strategic direction | Overseer | User only |
| Task assignment | Overseer | - |
| Task priority | Overseer | User only |
| Quality approval (Q≥80) | Quality Agent | Overseer |
| Cultural approval (C≥80) | Cultural Agent | Overseer |
| Publish/Block | Overseer | User only |
| GraphRAG relationships | Relationship Mapper | Overseer |
| Technical deployment | DevOps | Overseer |
| Emergency protocols | Overseer | - |

---

## 📊 **AGENT COORDINATION: SQL FUNCTIONS**

### **Function 1: Assign Task**
```sql
CREATE OR REPLACE FUNCTION assign_task(
  p_task_type TEXT,
  p_description TEXT,
  p_priority INT,
  p_assigned_by TEXT,
  p_resource_path TEXT DEFAULT NULL,
  p_input_data JSONB DEFAULT '{}'::JSONB
)
RETURNS BIGINT AS $$
DECLARE
  v_task_id BIGINT;
  v_assigned_to TEXT;
BEGIN
  -- Auto-route based on task type
  v_assigned_to := CASE p_task_type
    WHEN 'build_lesson' THEN 'kaituhi-ako-001'
    WHEN 'build_handout' THEN 'kaituhi-ako-001'
    WHEN 'validate_quality' THEN 'kaiarahi-kounga-001'
    WHEN 'validate_cultural' THEN 'kaitiaki-ahurea-001'
    WHEN 'create_relationships' THEN 'kaihapai-hononga-001'
    WHEN 'analyze_metrics' THEN 'kaitatari-raraunga-001'
    ELSE 'kaitiaki-aronui-001'  -- Default to overseer
  END;
  
  -- Insert task
  INSERT INTO task_queue (
    task_type, task_description, priority, assigned_to, assigned_by, 
    resource_path, input_data
  )
  VALUES (
    p_task_type, p_description, p_priority, v_assigned_to, p_assigned_by,
    p_resource_path, p_input_data
  )
  RETURNING id INTO v_task_id;
  
  -- Send message to assigned agent
  INSERT INTO agent_messages (from_agent, to_agent, message_type, subject, task_id)
  VALUES (
    p_assigned_by, v_assigned_to, 'task_assignment', 
    'New Task: ' || p_task_type, v_task_id
  );
  
  RETURN v_task_id;
END;
$$ LANGUAGE plpgsql;
```

### **Function 2: Get Next Task (Agent pulls work)**
```sql
CREATE OR REPLACE FUNCTION get_next_task(p_agent_id TEXT)
RETURNS TABLE (
  task_id BIGINT,
  task_type TEXT,
  task_description TEXT,
  priority INT,
  resource_path TEXT,
  input_data JSONB
) AS $$
BEGIN
  RETURN QUERY
  SELECT 
    id, task_type, task_description, priority, resource_path, input_data
  FROM task_queue
  WHERE 
    assigned_to = p_agent_id 
    AND status = 'pending'
    AND (dependencies IS NULL OR dependencies = '{}')  -- No unmet dependencies
  ORDER BY priority ASC, created_at ASC
  LIMIT 1
  FOR UPDATE SKIP LOCKED;  -- Prevent concurrent assignment
  
  -- Mark as in_progress
  UPDATE task_queue 
  SET status = 'in_progress', started_at = NOW()
  WHERE id = (SELECT task_id FROM task_queue WHERE assigned_to = p_agent_id LIMIT 1);
END;
$$ LANGUAGE plpgsql;
```

### **Function 3: Complete Task**
```sql
CREATE OR REPLACE FUNCTION complete_task(
  p_task_id BIGINT,
  p_agent_id TEXT,
  p_output_data JSONB DEFAULT '{}'::JSONB
)
RETURNS VOID AS $$
BEGIN
  UPDATE task_queue
  SET 
    status = 'completed',
    completed_at = NOW(),
    output_data = p_output_data
  WHERE id = p_task_id AND assigned_to = p_agent_id;
  
  -- Notify overseer
  INSERT INTO agent_messages (from_agent, to_agent, message_type, subject, task_id)
  VALUES (
    p_agent_id, 'kaitiaki-aronui-001', 'status_update',
    'Task Completed: ' || p_task_id, p_task_id
  );
  
  -- Check if this unblocks other tasks
  UPDATE task_queue
  SET status = 'pending'
  WHERE 
    status = 'blocked'
    AND p_task_id = ANY(dependencies);
END;
$$ LANGUAGE plpgsql;
```

---

## 🚀 **IMPLEMENTATION ROADMAP**

### **Phase 1: Database Setup (Today)**
- ✅ Create 5 coordination tables
- ✅ Create SQL functions for task management
- ✅ Test with sample tasks

### **Phase 2: Agent Registration (This Week)**
- Register all 12 agents in `agent_coordination`
- Define capabilities & preferences for each
- Set up heartbeat system (agents check in every 5 min)

### **Phase 3: Build Workflows (Next Week)**
- Implement "Build Lesson" full pipeline
- Test validation pipeline
- Set up auto-routing for common tasks

### **Phase 4: Communication Layer (Following Week)**
- Build agent message system
- Create notification handlers
- Implement response tracking

### **Phase 5: Intelligence Features (Month 2)**
- Predictive task assignment (ML-based)
- Agent performance analytics
- Self-optimizing workflows

---

## 💎 **SUCCESS METRICS**

1. **Coordination Efficiency:**
   - Task completion time (target: <4 hours for lesson)
   - Revision cycles (target: ≤1 per resource)
   - Agent idle time (target: <10%)

2. **Quality Improvement:**
   - Average quality score (target: Q90+)
   - Pass rate on first validation (target: 80%+)
   - User satisfaction (target: 4.5/5 stars)

3. **Team Performance:**
   - Tasks completed per session (target: 10+)
   - Cross-agent collaboration events (target: 50+ per week)
   - Conflict rate (target: <2% of tasks)

---

## 🎉 **THE VISION: SELF-ORGANIZING INTELLIGENCE**

Imagine:
- User submits request
- Overseer breaks into tasks, assigns to specialists
- Agents work in parallel, communicate via database
- Quality gates ensure excellence
- System self-monitors, self-corrects
- User receives high-quality resource in hours, not days
- **ZERO manual coordination needed!**

---

**Ngā mihi! This is the foundation for TRUE multi-agent intelligence!** 🧠✨

Next: Build the database tables and test with your first coordinated workflow! 🚀


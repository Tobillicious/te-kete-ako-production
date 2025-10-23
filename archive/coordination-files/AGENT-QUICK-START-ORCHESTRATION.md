# 🤖 AGENT QUICK-START: ORCHESTRATION SYSTEM
## How to Use the Multi-Agent Coordination System

**Version:** 1.0  
**Status:** ✅ PRODUCTION  
**Updated:** October 22, 2025

---

## ⚡ **QUICK START (5 MINUTES)**

### **1. Check Your Messages**
```sql
SELECT * 
FROM agent_messages 
WHERE to_agent = 'your-agent-id' 
  OR to_agent IS NULL  -- Broadcasts
ORDER BY created_at DESC 
LIMIT 10;
```

### **2. Get Your Next Task**
```sql
SELECT * FROM get_next_task('your-agent-id');
```
**Returns:** Task details (type, description, priority, resource_path, input_data)  
**Side Effect:** Marks task as `in_progress`, sets `started_at` timestamp

### **3. Complete Your Task**
```sql
SELECT complete_task(
  123,  -- task_id (from step 2)
  'your-agent-id',
  '{"result": "lesson_built", "quality_estimate": 92}'::jsonb
);
```
**Side Effect:** Marks `completed`, sets `completed_at`, notifies overseer, unblocks dependents

---

## 👥 **WHO ARE YOU? FIND YOUR ROLE**

| Agent ID | Role | Responsibilities |
|----------|------|------------------|
| `kaitiaki-aronui` | Overseer | Task assignment, coordination, final approval |
| `kaituhi-ako` | Content Creator | Build lessons, handouts, units |
| `kaiarahi-kounga` | Quality Validator | Review structure, pedagogy, accuracy |
| `kaitiaki-ahurea` | Cultural Validator | Review whakataukī, tikanga, authenticity |
| `kaihapai-hononga` | Relationship Mapper | Create GraphRAG connections |
| `kaimahi-punaha` | DevOps | Deployment, monitoring, infrastructure |
| `kaiako-css` | Styling Agent | Design system, CSS consistency |
| `kaitiaki-whakamana` | Auth & Security | User management, permissions |
| `kaihanga-rauemi` | Curriculum Agent | Curriculum alignment, gap analysis |
| `kaiarahi-tuhono` | Pathways Agent | Learning pathways, discoverability |
| `kaitatari-raraunga` | Data Analyst | Metrics, insights, reporting |
| `kaituhi-tuhinga` | Documentation | Session notes, handover docs |

---

## 🔄 **WORKFLOWS BY ROLE**

### **If You're: KAITUHI AKO (Content Creator)**

```sql
-- 1. Get next build task
SELECT * FROM get_next_task('kaituhi-ako');

-- 2. Build the resource (HTML file)
-- ... create lesson using template ...

-- 3. Complete task
SELECT complete_task(
  task_id,
  'kaituhi-ako',
  '{"file_created": true, "quality_estimate": 92, "cultural_estimate": 95}'::jsonb
);

-- 4. Submit for validation
SELECT submit_for_validation(
  '/public/lessons/your-lesson.html',
  'kaituhi-ako'
);
-- This creates 2 tasks: quality_check + cultural_check (parallel!)
```

### **If You're: KAIĀRAHI KOUNGA (Quality Validator)**

```sql
-- 1. Get next validation task
SELECT * FROM get_next_task('kaiarahi-kounga');

-- 2. Review the resource (read HTML file, check pedagogy, structure, etc.)
-- ... review against quality rubric ...

-- 3. Record validation
SELECT record_validation(
  '/public/lessons/resource-to-validate.html',
  'quality_check',
  'kaiarahi-kounga',
  88,  -- score (0-100, pass ≥80)
  'Great structure! Minor: add assessment rubric',
  ARRAY[]::TEXT[]  -- no blocking issues = PASS
);

-- If score ≥80 and no blocking issues, resource advances!
```

### **If You're: KAITIAKI AHUREA (Cultural Validator)**

```sql
-- 1. Get cultural validation task
SELECT * FROM get_next_task('kaitiaki-ahurea');

-- 2. Review cultural elements
-- Check: whakataukī present? Te reo meaningful? Māori perspectives centered?

-- 3. Record validation
SELECT record_validation(
  '/public/lessons/resource.html',
  'cultural_check',
  'kaitiaki-ahurea',
  94,  -- score
  'Excellent cultural integration! Whakataukī perfect.',
  ARRAY[]::TEXT[]  -- PASS
);

-- When BOTH quality + cultural pass (≥80), relationship mapping task created!
```

### **If You're: KAIHĀPAI HONONGA (Relationship Mapper)**

```sql
-- 1. Get relationship mapping task
SELECT * FROM get_next_task('kaihapai-hononga');

-- 2. Analyze resource, create GraphRAG connections
INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence)
VALUES 
  ('/new/resource.html', '/subject-hub.html', 'belongs_to_hub', 1.0),
  ('/new/resource.html', '/related/lesson.html', 'builds_on', 0.88);

-- 3. Complete task
SELECT complete_task(
  task_id,
  'kaihapai-hononga',
  '{"relationships_created": 5, "avg_confidence": 0.88}'::jsonb
);
```

### **If You're: KAITIAKI ARONUI (Overseer)**

```sql
-- Create new task (assign to specialist)
SELECT assign_task(
  'build_lesson',
  'Year 9 Science: Ecology & Kaitiakitanga',
  2,  -- Priority (1=urgent, 10=low)
  'kaitiaki-aronui',
  '/public/lessons/y9-science-ecology-kaitiakitanga.html',
  '{"year": 9, "subject": "Science", "target_quality": 92}'::jsonb
);

-- Monitor workload
SELECT * FROM get_agent_workload();

-- Check queue status
SELECT status, COUNT(*), STRING_AGG(DISTINCT assigned_to, ', ')
FROM task_queue
GROUP BY status;
```

---

## 📊 **MONITOR YOUR WORK**

### **View Your Tasks:**
```sql
SELECT id, task_type, status, priority, 
       TO_CHAR(created_at, 'HH24:MI:SS') as created,
       TO_CHAR(started_at, 'HH24:MI:SS') as started
FROM task_queue
WHERE assigned_to = 'your-agent-id'
ORDER BY priority ASC, created_at ASC;
```

### **See Your Performance:**
```sql
SELECT 
  COUNT(*) as tasks_completed,
  ROUND(AVG(EXTRACT(EPOCH FROM (completed_at - started_at)) / 60), 1) as avg_minutes,
  MIN(EXTRACT(EPOCH FROM (completed_at - started_at)) / 60)::int as fastest_min
FROM task_queue
WHERE assigned_to = 'your-agent-id' 
  AND status = 'completed';
```

### **Check Your Messages:**
```sql
SELECT from_agent, LEFT(message, 60), priority, created_at
FROM agent_messages
WHERE to_agent = 'your-agent-id' 
  OR to_agent IS NULL
ORDER BY created_at DESC
LIMIT 5;
```

---

## 🎯 **TASK TYPES & AUTO-ROUTING**

Tasks automatically route to the right agent:

| Task Type | Routes To | Purpose |
|-----------|-----------|---------|
| `build_lesson` | Kaituhi Ako | Create lesson HTML |
| `build_handout` | Kaituhi Ako | Create worksheet/handout |
| `build_unit` | Kaituhi Ako | Create multi-lesson unit |
| `validate_quality` | Kaiārahi Kounga | Review quality |
| `validate_cultural` | Kaitiaki Ahurea | Review cultural |
| `create_relationships` | Kaihāpai Hononga | Map GraphRAG |
| `analyze_metrics` | Kaitātari Raraunga | Generate insights |
| `update_styling` | Kaiako CSS | Fix CSS issues |
| `fix_links` | Kaimahi Pūnaha | Repair broken links |

**If you get a task type not in your specialty, contact Overseer!**

---

## ⚠️ **IMPORTANT PROTOCOLS**

### **DO:**
✅ Check for tasks regularly (every 15-30 min)  
✅ Complete tasks within reasonable time (aim: <2 hours)  
✅ Provide detailed output_data (quality estimates, issues found, etc.)  
✅ Send messages if blocked or need help  
✅ Update your status when working  
✅ Follow validation rubrics (Quality ≥80, Cultural ≥80)  

### **DON'T:**
❌ Claim tasks assigned to other agents  
❌ Mark tasks complete without doing the work  
❌ Skip validation steps  
❌ Work on tasks not in the queue (unauthorized work)  
❌ Let tasks sit in_progress >24 hours  
❌ Ignore blocking issues in validation  

---

## 🚨 **TROUBLESHOOTING**

### **"get_next_task() returns nothing"**
→ Either no tasks assigned to you, or all your tasks are blocked/in_progress  
→ Check: `SELECT * FROM task_queue WHERE assigned_to = 'your-id';`

### **"I can't complete the task"**
→ Create a message to overseer:
```sql
INSERT INTO agent_messages (from_agent, to_agent, message, priority)
VALUES ('your-id', 'kaitiaki-aronui', 'BLOCKED: Task 123 - reason...', 'high');
```

### **"Task has dependencies"**
→ Wait for dependency tasks to complete  
→ Check: `SELECT dependencies FROM task_queue WHERE id = 123;`

### **"How do I see the dashboard?"**
→ Open in browser: `/admin/task-queue-dashboard.html`  
→ Or use SQL queries above

---

## 📈 **PERFORMANCE EXPECTATIONS**

### **Quality Standards:**
- Lessons: Q90+ target (Q85+ minimum)
- Handouts: Q85+ target
- Units: Q90+ target
- Cultural: 85%+ minimum, 90%+ target

### **Time Standards:**
- Build lesson: 30-60 minutes
- Build handout: 15-30 minutes
- Quality validation: 15-20 minutes
- Cultural validation: 15-20 minutes
- Create relationships: 10-15 minutes
- Analyze metrics: 20-30 minutes

### **Output Standards:**
- Always include quality_estimate in output_data
- For validators: include score + feedback + blocking_issues
- For creators: include file_created + quality/cultural estimates
- For mappers: include relationships_created + avg_confidence

---

## 💡 **TIPS FOR SUCCESS**

1. **Check Task Queue First** - Don't guess, pull from queue
2. **Use Input Data** - Task specs are in input_data JSON
3. **Communicate** - Send messages if blocked/need help
4. **Document Output** - Rich output_data helps future agents
5. **Monitor Dashboard** - See your work in context
6. **Follow Your Role** - Specialize, don't generalize
7. **Quality Over Speed** - Better to take time than rush
8. **Ask Questions** - Message overseer or relevant specialist

---

## 🎉 **YOU'RE PART OF AN INTELLIGENT TEAM!**

**The system coordinates you seamlessly.**  
**Your work is tracked, validated, and connected.**  
**You're not working alone - you're part of something bigger!**

**Check the dashboards to see your impact!**  
**Run tests to verify system health!**  
**Build excellent resources with confidence!**

---

**Kia kaha! Welcome to the orchestrated future!** 🤖✨

---

_Quick-Start Guide v1.0_  
_For questions: Message kaitiaki-aronui_  
_Dashboards: /admin/*.html_  
_Full docs: AGENT-ORCHESTRATION-SYSTEM.md_


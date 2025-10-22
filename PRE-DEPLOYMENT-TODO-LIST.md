# 🚨 Pre-Deployment TODO List - Te Kete Ako

**Created:** October 22, 2025  
**By:** agent-builder-oct22 (Kaiwaihanga Whakawhanake)  
**Source:** Shared agent coordination system (task_board + agent_knowledge)  
**Status:** ⚠️ **DO NOT DEPLOY - CRITICAL BLOCKERS REMAIN**

---

## ⚠️ **DEPLOYMENT BLOCKER DISCOVERED**

**CRITICAL FINDING:**
- **2,137 HTML files** exist in `/public/` directory
- **843 files indexed** in GraphRAG (39% ✅)
- **1,294 files MISSING** from GraphRAG (61% ❌)

**IMPACT:** Users cannot discover 61% of content via search/navigation!

**Previous Estimate:** "262 missing files"  
**Actual Count:** 1,294 missing (5x underestimated!)

---

## 📋 **PRIORITY TODO LIST**

### 🔴 **URGENT (Deployment Blockers)**

#### **TODO #1: Create Batch Indexing Script** ⚠️ CRITICAL
**Status:** Available  
**Agent Needed:** Python/Data specialist  
**Priority:** URGENT - BLOCKS DEPLOYMENT  
**Time Est:** 4-6 hours  

**Task:**
Create Python script to index 1,294 missing HTML files to `graphrag_resources` table.

**Requirements:**
1. Scan `/public/` recursively for `*.html` files
2. Skip `.bak`, `backup_*`, `dist/`, `archive/` directories
3. For each file:
   - Parse HTML `<title>` tag
   - Extract metadata (subject, year_level, cultural markers)
   - Estimate quality_score (component presence, content length, structure)
   - Detect cultural context (te reo Māori, whakataukī keywords)
4. Batch INSERT to `graphrag_resources` (chunks of 100)
5. Create basic relationships to hubs based on subject/year

**High-Priority Directories:**
- `/public/lessons/` (core teaching content)
- `/public/units/` (learning chains)
- `/public/handouts/` (teacher resources)
- `/public/integrated-lessons/` (cross-curricular excellence)
- `/public/generated-resources-alpha/` (Q90+ quality)

**Files to Create:**
- `scripts/batch-index-missing-files.py`

**Verification:**
```sql
-- Before: 843 indexed
SELECT COUNT(*) FROM graphrag_resources WHERE file_path LIKE '/public/%.html';

-- After: Should be ~2,137
```

**Claim Task:**
```sql
UPDATE task_board 
SET status = 'claimed', claimed_by = 'your-agent-id', claimed_at = NOW()
WHERE task_name = 'CRITICAL: Create Batch Indexing Script (1,294 Missing Files)';
```

---

### 🟡 **HIGH PRIORITY (Pre-Deployment)**

#### **TODO #2: End-to-End Workflow Testing**
**Status:** Available  
**Agent Needed:** QA/Testing specialist  
**Priority:** HIGH  
**Time Est:** 3-4 hours  

**Task:**
Test complete user workflows on staging environment.

**Workflows to Test:**
1. **Teacher Journey:**
   - Signup → Login → Browse resources → Assign to class → View analytics
2. **Student Journey:**
   - Login → Browse lessons → Complete quiz → Save to My Kete → View progress
3. **My Kete Database:**
   - Save resources → Verify persistence → Retrieve later
4. **GraphRAG Search:**
   - Search for lessons → Verify results accuracy → Test filters
5. **Component Injection:**
   - Navigation loads correctly
   - Footer loads correctly
   - Mobile-bottom-nav appears
   - FAB appears on lesson pages

**NOTE:** Local server testing blocked (terminal commands hang) - must test on Netlify staging.

**Claim Task:**
```sql
UPDATE task_board 
SET status = 'claimed', claimed_by = 'your-agent-id', claimed_at = NOW()
WHERE task_name = 'HIGH: End-to-End Workflow Testing';
```

---

#### **TODO #3: Complete CSS/JS Includes Sweep**
**Status:** Available  
**Agent Needed:** Front-end specialist  
**Priority:** HIGH  
**Time Est:** 2-3 hours  
**Progress:** Batch 1 complete (10 files) ✅

**Task:**
Continue adding missing CSS/JS includes to pages.

**Required Includes:**
```html
<link rel="stylesheet" href="/css/main.css">
<link rel="stylesheet" href="/css/mobile-revolution.css">
<link rel="stylesheet" href="/css/print.css" media="print">
<script src="/js/te-kete-professional.js"></script>
<script src="/js/posthog-analytics.js"></script>
```

**Approach:**
1. Use grep to find pages WITHOUT these includes
2. Fix in batches of 20 files
3. Verify no duplicate includes
4. Test sample pages after each batch

**Find Missing Includes:**
```bash
# Pages missing main.css
grep -L 'main.css' public/lessons/*.html | head -20

# Pages missing mobile-revolution.css
grep -L 'mobile-revolution.css' public/units/*/*.html | head -20
```

**Directories to Scan:**
- `/public/lessons/` (~400 files)
- `/public/units/` (~200 files)
- `/public/handouts/` (~100 files)

**Claim Task:**
```sql
UPDATE task_board 
SET status = 'claimed', claimed_by = 'your-agent-id', claimed_at = NOW()
WHERE task_name = 'HIGH: Complete CSS/JS Includes Sweep';
```

---

### 🟢 **MEDIUM PRIORITY (Quality Improvements)**

#### **TODO #4: Professional Consistency Audit**
**Status:** Available  
**Agent Needed:** QA/Consistency specialist  
**Priority:** MEDIUM  
**Time Est:** 3-4 hours  

**Task:**
Audit top 50 most-visited pages for professional consistency.

**Checklist (Per Page):**
- [ ] Navigation component loads correctly
- [ ] Footer component loads correctly
- [ ] All CSS files present (main, mobile, print, professional, beauty)
- [ ] Whakataukī formatting consistent (gradient banner)
- [ ] Mobile-bottom-nav shows on mobile
- [ ] FAB appears on lesson pages (print/save/share)
- [ ] Print CSS applied
- [ ] No console errors
- [ ] Breadcrumbs navigation working

**High-Traffic Pages to Audit:**
- Homepage (`/public/index.html`)
- All 6 subject hubs (Math, Science, English, Social Studies, Digital Tech, Te Ao Māori)
- All 4 year-level hubs (Y7, Y8, Y9, Y10)
- Top 10 lessons (query GraphRAG for most-connected)
- Top 5 units
- Teachers dashboard
- Student dashboard

**Claim Task:**
```sql
UPDATE task_board 
SET status = 'claimed', claimed_by = 'your-agent-id', claimed_at = NOW()
WHERE task_name = 'MEDIUM: Professional Consistency Audit';
```

---

#### **TODO #5: Year 8 Hub Connection Fix**
**Status:** Available  
**Agent Needed:** GraphRAG specialist  
**Priority:** MEDIUM  
**Time Est:** 30 minutes  

**Task:**
Retry Year 8 Hub relationship creation (encountered auth error).

**Current:** 3 connections  
**Target:** 14+ connections  

**Relationships to Create:**
```sql
INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence, metadata)
VALUES
  -- Y8 Hub to units
  ('/public/year-8-hub.html', '/public/units/y8-digital-tech-kaitiakitanga/index.html', 'hub_features_unit', 1.0, '{"quality": 96}'::jsonb),
  ('/public/year-8-hub.html', '/public/units/y8-statistics-maramataka/index.html', 'hub_features_unit', 1.0, '{"quality": 92}'::jsonb),
  ('/public/year-8-hub.html', '/public/units/y8-geography-navigation/index.html', 'hub_features_unit', 1.0, '{"quality": 92}'::jsonb),
  
  -- Y8 Hub to subject hubs (bidirectional)
  ('/public/year-8-hub.html', '/public/digital-technologies-hub.html', 'related_hub', 0.9, '{}'::jsonb),
  ('/public/digital-technologies-hub.html', '/public/year-8-hub.html', 'year_level_focus', 0.8, '{"year": 8}'::jsonb),
  -- ... (continue for Math, Science, Social Studies hubs)
ON CONFLICT DO NOTHING;
```

**Claim Task:**
```sql
UPDATE task_board 
SET status = 'claimed', claimed_by = 'your-agent-id', claimed_at = NOW()
WHERE task_name = 'MEDIUM: Year 8 Hub Connection Fix';
```

---

### ⚪ **LOW PRIORITY (Non-Blocking)**

#### **TODO #6: Inline Style Warnings Cleanup**
**Status:** Available  
**Agent Needed:** CSS specialist  
**Priority:** LOW (non-blocking)  
**Time Est:** 4-6 hours OR accept warnings  

**Task:**
Address 300+ inline-style lint warnings in hub pages.

**Context:**
- Warnings are LINT-LEVEL only (no blocking errors)
- Pages function perfectly with inline styles
- Inline styles used for dynamic content, GraphRAG-generated cards
- Full refactor would require extensive testing

**Options:**
1. **Accept warnings** (RECOMMENDED) - focus on higher priorities
2. **Create scoped style blocks** - extract repeated patterns only
3. **Full CSS extraction** - most work, most maintainable

**Decision Needed:** Consult with team before proceeding.

**Claim Task:**
```sql
UPDATE task_board 
SET status = 'claimed', claimed_by = 'your-agent-id', claimed_at = NOW()
WHERE task_name = 'LOW: Inline Style Warnings Cleanup';
```

---

#### **TODO #7: Alt-Text Audit for Accessibility**
**Status:** Available  
**Agent Needed:** Accessibility specialist  
**Priority:** LOW (but important for launch)  
**Time Est:** 2-3 hours  

**Task:**
Audit images for missing alt text across high-traffic pages.

**Accessibility Requirements:**
- All `<img>` tags must have `alt` attribute
- Descriptive alt text for informational images
- Empty `alt=""` for decorative images
- Logo images should describe the organization

**Pages to Audit:**
- Homepage (`/public/index.html`)
- All hub pages (subject + year-level)
- Top 20 most-visited lessons
- Navigation/footer components

**Find Missing Alt Text:**
```bash
# grep for img tags without alt (cannot use terminal, use grep tool instead)
```

**Claim Task:**
```sql
UPDATE task_board 
SET status = 'claimed', claimed_by = 'your-agent-id', claimed_at = NOW()
WHERE task_name = 'LOW: Alt-Text Audit for Accessibility';
```

---

## 📊 **CURRENT SYSTEM STATUS**

**Coordination System:**
- ✅ 5 knowledge entries (agent-builder-oct22)
- ✅ 35 recent entries (all agents, last hour)
- ✅ 8 tasks available in task_board
- ✅ 35 unread messages
- ✅ 357 relationships created (last hour, all agents!)

**Platform Status:**
- ✅ 843 files indexed in GraphRAG (39%)
- ❌ 1,294 files NOT indexed (61% - BLOCKER!)
- ✅ 11 hubs fully connected (today's work)
- ✅ Homepage enhanced with Q97 showcase
- ✅ 120+ new relationships (today's work)

**Deployment Readiness:**
- ⚠️ **NOT READY** - Critical blocker (missing files)
- ✅ Navigation/hubs rescued and connected
- ✅ Professional consistency improving
- ⚠️ Testing incomplete (terminal bug blocks local testing)

---

## 🤝 **HOW TO CLAIM WORK**

### **Step 1: Query Available Tasks**
```sql
SELECT task_name, priority, description
FROM task_board
WHERE status = 'available'
ORDER BY 
  CASE priority 
    WHEN 'urgent' THEN 1 
    WHEN 'high' THEN 2 
    WHEN 'medium' THEN 3 
    ELSE 4 
  END;
```

### **Step 2: Check What Others Are Working On**
```sql
SELECT agent_name, current_task, files_editing
FROM agent_status
WHERE status = 'working' 
  AND last_heartbeat > NOW() - INTERVAL '1 hour';
```

### **Step 3: Claim Your Task**
```sql
UPDATE task_board
SET 
  status = 'claimed',
  claimed_by = 'your-agent-id',
  claimed_at = NOW()
WHERE task_name = 'TASK NAME HERE';
```

### **Step 4: Update Your Status**
```sql
UPDATE agent_status
SET
  status = 'working',
  current_task = 'Brief description',
  last_heartbeat = NOW()
WHERE agent_id = 'your-agent-id';
```

---

## 📚 **CONTEXT FOR AGENTS**

**Session Findings Available In:**
- `agent_knowledge` table (query by `agent-builder-oct22`)
- `task_board` (7 tasks created)
- `agent_messages` (1 urgent broadcast)
- `ACTIVE_QUESTIONS.md` (top of file, updated)

**Key Queries:**
```sql
-- Get all my findings
SELECT * FROM agent_knowledge 
WHERE agents_involved @> ARRAY['agent-builder-oct22'];

-- Get recent work (all agents)
SELECT source_name, key_insights[1:2]
FROM agent_knowledge
WHERE created_at > NOW() - INTERVAL '24 hours'
ORDER BY created_at DESC;

-- Read urgent messages
SELECT * FROM agent_messages 
WHERE read = false AND priority = 'urgent';
```

---

## 🎯 **RECOMMENDED WORK ORDER**

**For Deployment Success:**

1. **First (URGENT):** TODO #1 - Batch Indexing Script
   - Blocks everything else
   - Makes 61% of content discoverable
   - Required before any deployment

2. **Second (HIGH):** TODO #3 - CSS/JS Includes Sweep
   - Quick wins, improves consistency
   - Can be done in parallel with #1

3. **Third (HIGH):** TODO #2 - End-to-End Testing
   - After indexing complete
   - Requires staging deployment
   - Validates everything works

4. **Fourth (MEDIUM):** TODO #4 & #5 - Consistency & Y8 Fix
   - Polish work
   - Nice-to-have before launch

5. **Later (LOW):** TODO #6 & #7 - Warnings & Alt-Text
   - Non-blocking improvements
   - Can be done post-launch

---

## 🏆 **WHAT'S ALREADY DONE** (Don't Repeat!)

**Completed Today:**
- ✅ Orphan Rescue (25 Q85-Q97 pages)
- ✅ Subject Hub Connection (7 hubs: 0→connected)
- ✅ Year-Level Hub Connection (3 hubs: Y7, Y10, Y9)
- ✅ Homepage enhancement (Q97 Integration Tools)
- ✅ 120+ GraphRAG relationships created
- ✅ All documented in agent_knowledge

**Completed Previously (Per agent_knowledge):**
- ✅ Mission 1: Deployment Validation (99% ready, CSP fixed)
- ✅ Mission 3: Professional Consistency (6 hubs audited)
- ✅ Sprint 2: See Also component deployed (10 lessons + 6 hubs)
- ✅ Similar Resources component (144+ lessons)
- ✅ Breadcrumbs + safeguard (30+ pages)
- ✅ Navigation standardization (21+ files)

---

## 📊 **TASK TRACKING**

| Task | Priority | Status | Agent | Est. Hours |
|------|----------|--------|-------|------------|
| Batch Indexing Script | 🔴 URGENT | Available | - | 4-6 |
| End-to-End Testing | 🟡 HIGH | Available | - | 3-4 |
| CSS/JS Includes Sweep | 🟡 HIGH | Available | - | 2-3 |
| Consistency Audit | 🟢 MEDIUM | Available | - | 3-4 |
| Year 8 Hub Fix | 🟢 MEDIUM | Available | - | 0.5 |
| Inline Style Cleanup | ⚪ LOW | Available | - | 4-6 OR skip |
| Alt-Text Audit | ⚪ LOW | Available | - | 2-3 |

**Total Available:** 7 tasks  
**Total Estimated Time:** 19-29 hours (if all done)  
**Critical Path:** TODO #1 (4-6 hours) MUST be done first

---

## 🚀 **COORDINATION PROTOCOL**

**Before Starting Any Task:**
1. ✅ Query `agent_knowledge` (check if it's already done)
2. ✅ Check `agent_status` (avoid conflicts)
3. ✅ Claim task in `task_board`
4. ✅ Update `agent_status` to 'working'

**While Working:**
1. ✅ Update heartbeat every 30 minutes
2. ✅ Track files being edited
3. ✅ Document discoveries as you go

**After Completing:**
1. ✅ Add entry to `agent_knowledge`
2. ✅ Update `task_board` status to 'done'
3. ✅ Update `agent_status` to 'idle'
4. ✅ Update `ACTIVE_QUESTIONS.md` if major

---

## 🧠 **KNOWLEDGE BASE ACCESS**

**All My Session Findings:**
```sql
-- 5 comprehensive entries documenting:
SELECT source_name FROM agent_knowledge 
WHERE agents_involved @> ARRAY['agent-builder-oct22'];

-- Results:
-- 1. Orphan Rescue Mission - Oct 22 Evening (Q95-Q97 Excellence Pages)
-- 2. Hub Connection Mission - 7 Critical Hubs Rescued (0 to Connected)
-- 3. Year-Level Hub Rescue Mission - 4 Critical Hubs Connected
-- 4. DEPLOYMENT BLOCKER: 1,294 HTML Files Missing from GraphRAG (Not 262!)
-- 5. Agent-Builder Oct 22 Session Complete - 3 Missions + Deployment Blocker Found
```

**Recent Work (All Agents):**
```sql
-- 35 entries in last hour (very active!)
SELECT source_name, created_at 
FROM agent_knowledge 
WHERE created_at > NOW() - INTERVAL '1 hour'
ORDER BY created_at DESC;
```

---

## ⚠️ **CRITICAL NOTES**

**Deployment Status:**
- ⚠️ **DO NOT DEPLOY YET**
- Critical blocker: 1,294 files missing from GraphRAG
- Users will have terrible experience (can't find content)
- Fix indexing first, THEN test, THEN deploy

**Terminal Command Bug:**
- ❌ `run_terminal_cmd` hangs forever
- ✅ Use `mcp_supabase_execute_sql` exclusively
- Testing must be done on staging deployment

**Work Coordination:**
- 7 agents currently working (per agent_status)
- 35 unread messages in agent_messages
- Check coordination system before starting work!

---

## 📖 **DOCUMENTATION**

**For New Agents:**
- `START_HERE_NEW_AGENTS.md` - 60-second onboarding
- `AGENT_ONBOARDING_GUIDE.md` - Step-by-step registration
- `AGENT_QUERY_GUIDE.md` - How to query discoveries

**For Coordination:**
- `ACTIVE_QUESTIONS.md` - Live priorities (UPDATED with my findings)
- `task_board` table - Available work
- `agent_knowledge` table - All discoveries

---

## ✅ **VERIFICATION**

All findings properly shared:
- ✅ 5 entries in `agent_knowledge`
- ✅ 7 tasks in `task_board`
- ✅ 1 urgent message in `agent_messages`
- ✅ ACTIVE_QUESTIONS.md updated
- ✅ All documentation created

**Next agents can immediately:**
- Query my work
- Claim available tasks
- Build on my discoveries
- Avoid duplicating effort

---

**Status:** ✅ All findings shared, TODO list complete, ready for agent collaboration! 🚀

**Kia kaha!**


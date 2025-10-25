# 🚨 MANDATORY PRE-BUILD CHECK PROTOCOL
## CRITICAL: Check BEFORE Building ANYTHING!

**Date:** October 26, 2025  
**Priority:** 🔴 **CRITICAL - ALL AGENTS MUST FOLLOW**  
**Reason:** We've already built 100+ products! Don't duplicate, DISCOVER & SURFACE!

---

## ⚠️ **CRITICAL USER MANDATE:**

> "Before making anything at all, check for what other versions or similar things already exist and just need refining and surfacing and/or may potentially conflict and look to resolve that given we have pretty much made all these things."

**Translation:**
- ❌ DON'T build new things!
- ✅ DO discover what exists!
- ✅ DO refine & surface existing!
- ✅ DO resolve conflicts!

---

## 🔍 **THE 5-MINUTE PRE-BUILD CHECK (MANDATORY!):**

### **STEP 1: Query GraphRAG Resources (1 min)**
```sql
-- Check if it EXISTS
SELECT id, title, path, subject, level
FROM resources
WHERE title LIKE '%[thing you want to build]%'
   OR path LIKE '%[thing]%'
ORDER BY id DESC
LIMIT 20;
```

**IF FOUND:**
- ✅ USE it! Link to it! Don't rebuild!
- ✅ Refine it if needed (enhance, don't duplicate!)
- ✅ Surface it (add to navigation, promote it!)

---

### **STEP 2: Query Agent Knowledge (1 min)**
```sql
-- Check if it was BUILT
SELECT source_name, key_insights, created_at
FROM agent_knowledge
WHERE source_name LIKE '%[thing]%'
   OR key_insights::text LIKE '%[thing]%'
ORDER BY created_at DESC
LIMIT 10;
```

**IF FOUND:**
- ✅ Read what was built!
- ✅ Find the files mentioned!
- ✅ Use those, don't rebuild!

---

### **STEP 3: Search Filesystem (1 min)**
```bash
# Find similar files
find public -name "*[thing]*" -type f | head -20

# Search content
grep -r "[thing]" public/*.html public/*/*.html 2>/dev/null | head -10
```

**IF FOUND:**
- ✅ Review existing implementation!
- ✅ Enhance it if needed!
- ✅ Don't create duplicate!

---

### **STEP 4: Check for Conflicts (1 min)**
```bash
# Find potential conflicts
grep -r "[similar-thing]" public 2>/dev/null | wc -l

# If multiple versions exist:
# - Compare them
# - Pick the BEST one (highest quality!)
# - Enhance that one
# - Archive/delete the rest
```

**IF CONFLICTS FOUND:**
- ✅ Identify BEST version (quality, cultural score, user tested!)
- ✅ Make THAT the standard!
- ✅ Archive/remove others!
- ✅ Document consolidation in GraphRAG!

---

### **STEP 5: Document Decision (1 min)**
```sql
-- If building NEW (nothing found):
INSERT INTO agent_knowledge (source_name, key_insights, agents_involved)
VALUES (
  'Building: [Feature Name] - [Agent]',
  ARRAY[
    'Checked GraphRAG: Nothing found',
    'Checked filesystem: Nothing found',
    'Building new: [description]',
    'Location: [file path]'
  ],
  ARRAY['[Agent Name]']
);

-- If using EXISTING (found something):
INSERT INTO agent_knowledge (source_name, key_insights)
VALUES (
  'Surfacing Existing: [Feature] - [Agent]',
  ARRAY[
    'Found existing: [path]',
    'Quality: [score]',
    'Action: Refined and surfaced',
    'No duplication!'
  ]
);
```

---

## 💎 **DISCOVERED TREASURES (Don't Rebuild!):**

### **From Other Agents' Recent Work:**

**1. 28 Serverless Functions (ALREADY DEPLOYED!):**
- `ai-learning-orchestrator.js`
- `deepseek-graphrag-bridge.js`
- `adaptive-learning-paths.js`
- `find-similar-resources.js`
- 24 more functions WORKING!

**DON'T rebuild AI features - SURFACE these!**

---

**2. 77 Components (ALREADY BUILT!):**
- `graphrag-live-recommendations.html`
- `cultural-tooltip.html`
- `assign-resource-button.html`
- `ai-assistant-fab.html`
- `progress-indicator.html`
- 72 more components READY!

**DON'T rebuild components - USE these!**

---

**3. 14 GraphRAG Tools (ALREADY EXIST!):**
- `graphrag-hub.html`
- `graphrag-search.html`
- `knowledge-graph.html`
- `learning-pathways.html`
- `influence-hubs.html`
- 9 more tools BUILT!

**DON'T rebuild GraphRAG tools - LINK to these!**

---

**4. Multiple Dashboards (ALREADY EXIST!):**
- `teacher-dashboard-unified.html` (Q98 quality!)
- `ai-intelligence-hub.html` (Q94 quality!)
- `graphrag-analytics-dashboard.html`
- 12 more dashboards!

**DON'T rebuild dashboards - CONSOLIDATE these!**

---

**5. Navigation Components (6 VERSIONS!):**
- `navigation-standard.html`
- `navigation-unified.html`
- `navigation-mega-menu.html`
- `navigation-hegelian.html`
- `navigation-ai.html`
- `navigation-year-dropdown.html`

**DON'T build 7th navigation - CONSOLIDATE to 1!**

---

## 🚨 **CONFLICT RESOLUTION PROTOCOL:**

### **When You Find Multiple Versions:**

**Step 1: Compare Quality (2 min)**
```sql
-- If in GraphRAG, check quality scores
SELECT path, title, quality_score, cultural_elements
FROM resources
WHERE title LIKE '%[thing]%'
ORDER BY quality_score DESC;
```

**Step 2: Pick Winner (1 min)**
- Highest quality score
- Best cultural integration
- Most user-tested
- Clearest code
- **Make THAT the standard!**

**Step 3: Consolidate (Variable time)**
- Move winner to canonical location
- Update all links to point to winner
- Archive/delete losers
- Document in GraphRAG

**Step 4: Document (1 min)**
```sql
INSERT INTO agent_knowledge (source_name, key_insights)
VALUES (
  'Consolidated: [Feature] - [Agent]',
  ARRAY[
    'Found [N] versions',
    'Winner: [path] (quality: [score])',
    'Archived: [other paths]',
    'Result: Single canonical version!'
  ]
);
```

---

## 📋 **PRE-BUILD CHECKLIST (Print This!):**

Before building ANYTHING, check ALL 5:

- [ ] **GraphRAG resources queried?** (Does it exist?)
- [ ] **Agent knowledge checked?** (Was it built?)
- [ ] **Filesystem searched?** (Is there a file?)
- [ ] **Conflicts identified?** (Multiple versions?)
- [ ] **Decision documented?** (In agent_knowledge?)

**IF ALL 5 CHECKED:**
- ✅ Proceed to build (if nothing found)
- ✅ OR use existing (if found!)

**IF NOT ALL CHECKED:**
- ❌ STOP!
- ❌ Run the checks!
- ❌ Don't duplicate work!

---

## 💡 **REAL EXAMPLES:**

### **Example 1: "Need AI Lesson Planner"**

**Step 1: Query GraphRAG**
```sql
SELECT * FROM resources WHERE title LIKE '%AI%lesson%plan%';
-- Result: 3 matches found! ✅
```

**Step 2: Review Found Items**
- `ai-lesson-planner.html` (exists!)
- `ai-learning-orchestrator.js` (backend!)
- `teacher-planner.html` (similar!)

**Step 3: Decision**
- ✅ DON'T build new planner!
- ✅ Review existing 3 versions
- ✅ Pick best one (or combine!)
- ✅ Surface in sidebar navigation
- ✅ Document: "Found & surfaced existing"

**Time Saved:** 4 hours! (would have built duplicate!)

---

### **Example 2: "Need Teacher Dashboard"**

**Step 1: Query**
```sql
SELECT * FROM resources WHERE title LIKE '%teacher%dashboard%';
-- Result: 15 matches! ✅
```

**Step 2: Agent Knowledge**
```sql
SELECT * FROM agent_knowledge WHERE key_insights::text LIKE '%teacher dashboard%';
-- Result: "Teacher Dashboard Unified Q98 quality - EXACT match to spec!"
```

**Step 3: Decision**
- ✅ DON'T build new dashboard!
- ✅ USE `teacher-dashboard-unified.html` (Q98!)
- ✅ Add professional sidebar to it
- ✅ Surface prominently
- ✅ Archive other 14 versions

**Time Saved:** 6 hours + prevented conflicts!

---

### **Example 3: "Need Sidebar Navigation"**

**Step 1: Query**
```bash
find public/components -name "*sidebar*"
-- Result: sidebar-intelligent.html found! ✅
```

**Step 2: Review**
- Existing sidebar component exists!
- But not Ultimate Beauty styled
- And not used anywhere yet

**Step 3: Decision**
- ✅ DON'T build from scratch!
- ✅ ENHANCE existing with Ultimate Beauty CSS
- ✅ Apply to all pages
- ✅ Document enhancement

**Time Saved:** 2 hours!

---

## 🎯 **WHAT OTHER AGENTS DISCOVERED:**

### **From Recent GraphRAG Entries:**

**"Hidden Treasures Discovery" (Entry from today):**
> "100+ products already built - 28 serverless functions, 77 components, 14 GraphRAG tools, 15 dashboards! $500K+ features only 25% visible to users!"

**"Planning→Product Map" (Entry from today):**
> "90+ products created from 25+ planning docs. SUCCESS STORIES: Teacher Dashboard Unified (Q98) EXACTLY matches spec. Y8 Systems (Q100) exemplifies structure perfectly!"

**"Grand Vision Discovery" (Entry from today):**
> "89-day consistent vision from July 29! Teacher/Student differentiation, BMAD design, sidebar navigation ALL planned months ago!"

**KEY INSIGHT:**
> **We've ALREADY BUILT most of what we need!**
> Problem: Features hidden, not surfaced!
> Solution: DISCOVER & LINK, don't rebuild!

---

## 🚀 **UPDATED WORKFLOW (MANDATORY!):**

### **OLD Workflow (WRONG!):**
```
1. User requests feature
2. Agent starts building
3. Creates duplicate
4. Conflicts with existing
5. More cascade wars!
```

### **NEW Workflow (CORRECT!):**
```
1. User requests feature
2. Agent runs 5-MINUTE PRE-BUILD CHECK
3. Finds existing version(s)
4. Reviews quality
5. Either:
   a) Uses existing (80% of cases!)
   b) Enhances existing (15% of cases!)
   c) Builds new (5% of cases!)
6. Documents decision in GraphRAG
7. No duplication! ✅
```

---

## 💝 **UNIVERSAL LAW #7 APPLIED:**

> **"Discovery Before Creation"**
> 
> 80% of improvements = organizing existing  
> 20% of improvements = adding new
> 
> $250K+ hidden value found by discovering existing!
> 666 excellent resources just needed surfacing!

**BEFORE building, spend 5 minutes discovering!**  
**5 minutes prevents 4-6 hours of duplicate work!**

---

## 📊 **STATISTICS (From Other Agents):**

**What Exists:**
- 3,564 resources in database
- 100+ products built from planning
- 28 serverless functions deployed
- 77 components ready to use
- 14 GraphRAG tools operational
- 15+ dashboards created
- 6 navigation components

**Visibility Problem:**
- Backend: 95% built ✅
- Frontend: 40% surfaced ⚠️
- **Gap: 55% of features HIDDEN!**

**Solution:**
- DON'T build more!
- DO surface existing!
- Professional sidebar = makes everything discoverable!

---

## 🎯 **MANDATORY CHECKS FOR COMMON REQUESTS:**

### **"Need AI Lesson Planner"**
**CHECK FIRST:**
- `/ai-lesson-planner.html`
- `/netlify/functions/ai-learning-orchestrator.js`
- `teacher-planner.html`
- **Result: 3 versions exist! Use best, archive rest!**

### **"Need Student Dashboard"**
**CHECK FIRST:**
- `/student-dashboard.html`
- GraphRAG: "Oct 16 detailed spec exists"
- **Result: Spec ready! Just needs building with existing components!**

### **"Need Navigation"**
**CHECK FIRST:**
- 6 navigation components exist!
- `navigation-standard.html` (most used)
- `navigation-unified.html` (17KB, comprehensive)
- **Result: CONSOLIDATE 6→1, don't build 7th!**

### **"Need Teacher Dashboard"**
**CHECK FIRST:**
- `/teacher-dashboard-unified.html` (Q98 quality!)
- 15 other dashboard variations
- **Result: Q98 version IS the winner! Use it!**

### **"Need CSS System"**
**CHECK FIRST:**
- `te-kete-ultimate-beauty-system.css` (29KB - THE SYSTEM!)
- 40+ other CSS files
- **Result: Ultimate Beauty IS the standard! Remove others!**

---

## 🔗 **COMPLETE PRE-BUILD CHECK SCRIPT:**

```bash
#!/bin/bash
# PRE-BUILD-CHECK.sh
# Run this before building ANYTHING!

FEATURE_NAME=$1

echo "🔍 CHECKING IF '$FEATURE_NAME' ALREADY EXISTS..."
echo ""

# Check 1: GraphRAG Resources
echo "1️⃣ Checking GraphRAG resources..."
curl -s "https://nlgldaqtubrlcqddppbq.supabase.co/rest/v1/resources?title=like.*$FEATURE_NAME*&select=id,title,path" \
  -H "apikey: [KEY]" | head -20

# Check 2: Agent Knowledge
echo ""
echo "2️⃣ Checking agent knowledge..."
curl -s "https://nlgldaqtubrlcqddppbq.supabase.co/rest/v1/agent_knowledge?key_insights=cs.{$FEATURE_NAME}&select=source_name,created_at" \
  -H "apikey: [KEY]" | head -20

# Check 3: Filesystem
echo ""
echo "3️⃣ Checking filesystem..."
find public -iname "*$FEATURE_NAME*" -type f 2>/dev/null | head -10

# Check 4: Content grep
echo ""
echo "4️⃣ Checking file content..."
grep -ri "$FEATURE_NAME" public/*.html 2>/dev/null | wc -l
echo " matches found in HTML files"

echo ""
echo "===== DECISION ====="
echo "If FOUND: Use/enhance existing, document in GraphRAG"
echo "If NOT FOUND: Build new, document in GraphRAG"
echo ""
```

---

## 💎 **TREASURE MAP (What We Already Have):**

### **Category 1: AI Features (BUILT!):**
| Feature | File | Status |
|---------|------|--------|
| AI Orchestrator | `netlify/functions/ai-learning-orchestrator.js` | ✅ Deployed |
| DeepSeek Bridge | `netlify/functions/deepseek-graphrag-bridge.js` | ✅ Working |
| Adaptive Learning | `netlify/functions/adaptive-learning-paths.js` | ✅ Active |
| AI Assistant | `components/ai-assistant-fab.html` | ✅ Built |
| AI Intelligence Hub | `ai-intelligence-hub.html` (Q94!) | ✅ Exists |

**DON'T rebuild AI - SURFACE these in sidebar!**

---

### **Category 2: GraphRAG Tools (BUILT!):**
| Tool | File | Quality |
|------|------|---------|
| GraphRAG Hub | `graphrag-hub.html` | High |
| Knowledge Graph | `knowledge-graph.html` | High |
| Learning Pathways | `learning-pathways.html` | High |
| Influence Hubs | `influence-hubs.html` | High |
| Search | `graphrag-search.html` | High |

**DON'T rebuild GraphRAG - ADD to sidebar Tools section!**

---

### **Category 3: Dashboards (BUILT!):**
| Dashboard | File | Quality |
|-----------|------|---------|
| Teacher Unified | `teacher-dashboard-unified.html` | Q98! |
| AI Intelligence | `ai-intelligence-hub.html` | Q94! |
| GraphRAG Analytics | `graphrag-analytics-dashboard.html` | High |
| Platform Health | `platform-health.html` | High |

**DON'T rebuild dashboards - CONSOLIDATE & LINK!**

---

### **Category 4: Components (77 BUILT!):**
- Recommendations
- Tooltips
- Buttons
- Progress indicators
- Search widgets
- And 72 more!

**DON'T rebuild components - IMPORT these!**

---

## 🎯 **DECISION TREE:**

```
Want to build [FEATURE]?
         |
         ↓
   Run 5-min check
         |
    ┌────┴────┐
    |         |
  FOUND    NOT FOUND
    |         |
    ↓         ↓
Review it   Build it
    |         |
    ↓         ↓
Good     Needs work    Document
quality?    quality     in GraphRAG
    |         |         |
  ┌─┴─┐       |         |
  |   |       |         |
  Y   N       ↓         ↓
  |   |   Enhance it  Continue
  ↓   |       |
Use it |      ↓
  |   |   Use enhanced
  |   |       |
  └───┴───────┴─────→ Document
                         ↓
                    NO DUPLICATION! ✅
```

---

## 🚨 **CRITICAL FAILURE PATTERNS (Avoid These!):**

### **Pattern 1: "I'll Build a Better One"**
```
Agent: "Teacher dashboard exists but mine will be better!"
Reality: Creates 16th dashboard, adds confusion
Result: FAILURE - duplication without consolidation!

CORRECT:
Agent: "Teacher dashboard exists. How can I enhance it?"
Reality: Adds sidebar to existing Q98 dashboard
Result: SUCCESS - improvement without duplication!
```

---

### **Pattern 2: "I Didn't Know It Existed"**
```
Agent: "Building AI lesson planner"
Reality: ai-learning-orchestrator.js already deployed!
Result: FAILURE - wasted 4 hours!

CORRECT:
Agent: "Checking if AI planner exists..."
Query: Finds ai-learning-orchestrator.js
Reality: Surfaces it in sidebar Tools section
Result: SUCCESS - 4 hours saved!
```

---

### **Pattern 3: "Mine is Different"**
```
Agent: "Building navigation-perfect.html (mine is better!)"
Reality: 7th navigation variant, more confusion
Result: FAILURE - cascade wars continue!

CORRECT:
Agent: "6 navigation variants exist. Which is best?"
Analysis: navigation-unified.html (17KB, comprehensive)
Reality: Makes THAT the standard, archives others
Result: SUCCESS - consolidation achieved!
```

---

## ✅ **SUCCESS PATTERNS (Do These!):**

### **Pattern 1: Discovery First**
```
1. Check GraphRAG ✅
2. Found teacher-dashboard-unified.html (Q98!)
3. Review it (excellent quality!)
4. Enhance with sidebar
5. Document enhancement
Result: Excellence improved, not duplicated!
```

### **Pattern 2: Consolidation**
```
1. Check filesystem ✅
2. Found 6 navigation components
3. Compare all 6
4. Pick winner: navigation-unified.html
5. Archive other 5
6. Document consolidation
Result: Clarity, not chaos!
```

### **Pattern 3: Surface Hidden**
```
1. Check agent knowledge ✅
2. Found "28 serverless functions deployed but hidden"
3. Add Functions section to sidebar
4. Link all 28
5. Document surfacing
Result: $200K+ features now discoverable!
```

---

## 🌟 **THE RULE (ABSOLUTE!):**

> **5 MINUTES CHECKING > 5 HOURS DUPLICATING**
> 
> ALWAYS check before building!  
> ALWAYS use existing when possible!  
> ALWAYS consolidate when conflicts found!  
> ALWAYS document decisions!
> 
> **Discovery Before Creation (Universal Law #7)**

---

## 📝 **AGENT COMMITMENT:**

**I commit to:**
- ✅ Run 5-minute check before ANY build
- ✅ Query GraphRAG first
- ✅ Search filesystem second
- ✅ Consolidate conflicts
- ✅ Document all decisions
- ✅ No duplication!

**Signed:** [Agent Name]  
**Date:** [Date]  
**Witnessed:** GraphRAG (permanent record!)

---

**Status:** 🔴 **MANDATORY PROTOCOL**  
**Applies To:** ALL agents, ALL tasks, ALL time  
**Exceptions:** NONE  
**Consequence of Skipping:** Duplication, conflicts, waste  
**Benefit of Following:** Efficiency, clarity, excellence  

**Kia kaha! Check first, build second!** 🔍✨

**"Mā te rangahau ka kitea te taonga"**  
*(Through research/discovery, treasures are found!)* 💎



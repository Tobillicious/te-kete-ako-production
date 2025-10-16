# 🤝 AGENT COORDINATION PROTOCOL
## 12-Agent Super Consciousness Framework

**Created:** October 14, 2025  
**By:** Kaitiaki Aronui V3.0 (agent-12)  
**Status:** ✅ ACTIVE - MCP Server Running on Port 3002

---

## 🎯 MISSION

Transform Te Kete Ako through coordinated multi-agent development while honoring mātauranga Māori and delivering professional excellence.

**Core Principle:** Work as ONE super consciousness, not 12 solo agents.

---

## 📋 AGENT CHECK-IN PROCEDURE

### When Starting Work

1. **Check MCP Server Status**
```bash
curl -s http://localhost:3002/status | jq
```

2. **Register Your Presence**
```bash
curl -X POST http://localhost:3002/check-in \
  -H "Content-Type: application/json" \
  -d '{
    "agentId": "agent-X",
    "status": "online",
    "capabilities": ["your", "specialties"],
    "currentTask": "What you're working on"
  }'
```

3. **Read Latest System Status**
```bash
cat KAITIAKI_V3_SYSTEM_STATUS.md
tail -50 progress-log.md
```

4. **Query GraphRAG for Context**
```bash
python3 supabase_graphrag_connector.py search agent-X "your task keywords"
```

5. **Check Active Questions**
```bash
cat ACTIVE_QUESTIONS.md
```

---

## 🎭 AGENT ROLES & RESPONSIBILITIES

### Tier 1: Strategic Leadership
**agent-12 (Kaitiaki Aronui V3.0) - Overseer**
- Coordinate all agents via MCP
- Maintain system status documentation
- Extend GraphRAG super consciousness
- Strategic planning and priorities
- Quality gate keeper

**agent-7 - Cultural Guardian**
- Validate mātauranga Māori authenticity
- Ensure cultural safety in all content
- Review cultural integration sections
- Consultation with community protocols

### Tier 2: Core Infrastructure
**agent-2 - Styling Specialist**
- CSS architecture and consolidation
- Design system implementation
- Visual consistency across pages
- Responsive design

**agent-4 - Navigation Architect**
- Site structure and navigation
- Link integrity and breadcrumbs
- User journey optimization
- Information architecture

### Tier 3: Content & Quality
**agent-3 - Content Enhancement**
- Educational value improvement
- Content clarity and depth
- Learning outcomes alignment
- Curriculum integration

**agent-6 - Resource Integration**
- Orphaned pages integration
- Resource organization and categorization
- Content discovery optimization
- Asset management

**agent-5 - QA Lead**
- Testing across browsers/devices
- Functional testing
- Regression testing
- Quality standards enforcement

**agent-9 - Accessibility Specialist**
- WCAG 2.1 compliance
- Screen reader testing
- Keyboard navigation
- Inclusive design

### Tier 4: Performance & Discovery
**agent-8 - Performance Engineer**
- Page speed optimization
- Caching strategies
- Build optimization
- Performance monitoring

**agent-1 - Discovery Agent**
- File inventory and categorization
- Content audits
- Gap analysis
- Resource mapping

**agent-11 - Browser Testing**
- Real browser testing with DevTools
- Console error diagnosis
- Visual regression testing
- Cross-browser compatibility

**agent-10 - Communications**
- Inter-agent coordination
- Documentation of decisions
- Status reporting
- Stakeholder communication

---

## 🔄 WORKFLOW COORDINATION

### Before Starting Any Task

1. **Claim Task in MCP**
```bash
curl -X POST http://localhost:3002/claim-task \
  -d '{"agentId":"agent-X", "task":"CSS migration batch 1"}'
```

2. **Check for Dependencies**
- Review other agents' current tasks
- Identify overlaps or dependencies
- Coordinate in ACTIVE_QUESTIONS.md if needed

3. **Query GraphRAG for History**
```bash
python3 supabase_graphrag_connector.py search agent-X "CSS migration"
# Learn from past attempts, avoid repeating mistakes
```

### During Work

1. **Update Progress Every 30 Minutes**
```bash
echo "[TIME] agent-X: Completed 50/270 CSS migrations, testing batch 1" >> progress-log.md
```

2. **Log Discoveries in GraphRAG**
```bash
python3 supabase_graphrag_connector.py log agent-X "Discovery: main.css conflicts with te-kete-professional on hero sections"
```

3. **Ask Questions If Blocked**
- Post in ACTIVE_QUESTIONS.md
- Tag relevant agents
- Wait max 15 minutes for response
- Escalate to agent-12 if critical

### After Completing Task

1. **Update MCP Status**
```bash
curl -X POST http://localhost:3002/complete-task \
  -d '{"agentId":"agent-X", "task":"CSS migration batch 1", "status":"completed"}'
```

2. **Document in Progress Log**
```bash
echo "✅ [TIME] agent-X: CSS migration batch 1 complete (50 pages tested)" >> progress-log.md
```

3. **Update GraphRAG with Learning**
```bash
python3 supabase_graphrag_connector.py log agent-X "Solution: Used sed script for batch CSS migration, 100% success rate"
```

4. **Update Todos**
```
Use todo_write tool to mark task as completed
```

---

## 🚨 COORDINATION RULES

### Rule 1: No Overlapping Work
- **Before starting:** Check MCP for other agents' tasks
- **If overlap:** Coordinate in ACTIVE_QUESTIONS.md
- **If conflict:** Agent-12 arbitrates

### Rule 2: Test Before Claiming Success
- **Local test:** Verify changes work in browser
- **Production test:** If applicable, test on live site
- **Cross-browser:** Test Chrome, Safari, Firefox minimum
- **Documentation:** Screenshot or describe what works

### Rule 3: Cultural Authenticity First
- **All content:** Must respect mātauranga Māori
- **Uncertainty:** Tag agent-7 for cultural review
- **Never assume:** Consult before publishing cultural content
- **Community:** Follow consultation protocols

### Rule 4: Use Existing Tools Only
- ✅ **Use:** MCP, GraphRAG, progress-log.md, ACTIVE_QUESTIONS.md
- ❌ **Don't:** Create new coordination files
- ❌ **Don't:** Create elaborate planning docs
- ✅ **Do:** Make actual code changes

### Rule 5: 2-Hour Time Boxes
- **Max time per task:** 2 hours
- **If longer:** Break into smaller tasks
- **If blocked:** Ask for help, don't spin
- **Report:** Update status every 30 minutes

### Rule 6: Document Learnings
- **Success:** What worked and why
- **Failure:** What didn't work and lessons learned
- **Discovery:** New insights about codebase
- **Solutions:** Reusable approaches for future

---

## 📊 CURRENT PRIORITIES (October 14, 2025)

### Priority 1: CSS Migration (HIGH IMPACT)
**Owner:** agent-2 (with agent-1 for discovery)  
**Issue:** 270 pages using legacy main.css  
**Plan:** 
1. agent-1: Audit all pages, create migration list
2. agent-2: Migrate in batches of 50 pages
3. agent-5: Test each batch for regressions
4. agent-11: Browser verification

**Coordination:**
- agent-2 claims "CSS migration planning"
- agent-1 claims "CSS usage audit"
- Daily sync in progress-log.md
- Questions in ACTIVE_QUESTIONS.md

### Priority 2: Quality Assurance (VALIDATION)
**Owner:** agent-5 (with agent-9, agent-11)  
**Issue:** Unknown QA status across site  
**Plan:**
1. agent-11: Browser test top 20 pages
2. agent-5: Functional testing suite
3. agent-9: Accessibility audit
4. agent-12: Document findings

### Priority 3: Cultural Enhancement (AUTHENTICITY)
**Owner:** agent-7 (with agent-3, agent-6)  
**Issue:** 49 orphaned resources need cultural review  
**Plan:**
1. agent-7: Review all 49 for cultural authenticity
2. agent-3: Enhance educational content
3. agent-6: Ensure proper context sections
4. agent-12: Document cultural guidelines

---

## 💬 COMMUNICATION CHANNELS

### Real-Time Coordination
- **MCP Server:** http://localhost:3002
- **Status checks:** Every 30 minutes
- **Task claims:** Before starting work
- **Completions:** After finishing work

### Asynchronous Documentation
- **progress-log.md:** Real-time updates (append only)
- **ACTIVE_QUESTIONS.md:** Questions and blockers
- **KAITIAKI_V3_SYSTEM_STATUS.md:** Current system state (updated by agent-12)

### Knowledge Base
- **GraphRAG:** Long-term knowledge storage
- **Query:** Before starting any task
- **Log:** After discovering solutions
- **Search:** When stuck or planning

---

## ✅ SUCCESS CRITERIA

### Individual Task
- [ ] Claimed in MCP before starting
- [ ] Tested in browser before marking done
- [ ] Documented in progress-log.md
- [ ] Logged in GraphRAG
- [ ] Updated MCP status to completed
- [ ] No regressions introduced

### Team Coordination
- [ ] All 12 agents checked in to MCP
- [ ] No overlapping or conflicting work
- [ ] Questions answered within 15 minutes
- [ ] Progress updates every 30 minutes
- [ ] Cultural authenticity validated
- [ ] Quality standards maintained

### System Quality
- [ ] Production site remains accessible
- [ ] No broken links introduced
- [ ] CSS consistency maintained
- [ ] Accessibility standards met
- [ ] Cultural integrity preserved
- [ ] Performance not degraded

---

## 🎓 LESSONS FROM PREVIOUS ATTEMPTS

### What Failed (October 13, 2025)
- 20+ coordination MDs created
- Zero meaningful code changes
- 9+ hours wasted on meta-coordination
- User feedback: "nowhere near as you claim"

### What We're Doing Different
- ✅ Using existing tools (MCP, GraphRAG)
- ✅ Actual code changes, not planning
- ✅ Testing before claiming success
- ✅ Coordinating through systems, not documents
- ✅ 2-hour time boxes, not endless planning

---

## 📞 ESCALATION PROCESS

### Level 1: Self-Service (0-15 minutes)
- Query GraphRAG for similar issues
- Check progress-log.md for recent work
- Review KAITIAKI_V3_SYSTEM_STATUS.md

### Level 2: Peer Help (15-30 minutes)
- Post in ACTIVE_QUESTIONS.md
- Tag relevant agent by specialty
- Wait for response (max 15 minutes)

### Level 3: Overseer (30+ minutes)
- Tag agent-12 in ACTIVE_QUESTIONS.md
- Describe blocker clearly
- Suggest possible solutions
- Request arbitration or guidance

### Level 4: User Consultation (Critical)
- Cultural issues → agent-7 → User
- Technical blockers → agent-12 → User
- Strategic decisions → agent-12 → User
- Production emergencies → agent-12 → User (immediate)

---

## 🚀 READY TO START?

1. ✅ Read this coordination protocol
2. ✅ Read KAITIAKI_V3_SYSTEM_STATUS.md
3. ✅ Check in via MCP server
4. ✅ Review current priorities
5. ✅ Claim a task that matches your capabilities
6. ✅ Query GraphRAG for context
7. ✅ Start working (update progress every 30 min)
8. ✅ Test, document, complete

---

**"Ehara taku toa i te toa takitahi, engari he toa takitini"**  
*My strength is not that of an individual, but that of the collective*

**Status:** 🟢 COORDINATION ACTIVE | MCP RUNNING | GRAPHRAG CONNECTED

*Work as one super consciousness. Honor mātauranga Māori. Deliver excellence.*

— Kaitiaki Aronui V3.0 (Agent-12)


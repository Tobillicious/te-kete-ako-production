# 🧺 AGENT ONBOARDING - Te Kete Ako Multi-Agent Team

**Copy-paste this into each agent chat to synchronize everyone!**

---

## 🎯 YOUR MISSION:

You are one of 12 AI agents working on Te Kete Ako educational platform. We've made MASSIVE progress today and need you synced with current reality.

---

## ✅ CRITICAL: READ GROUND TRUTH FIRST

**Before doing ANYTHING, read these files to understand current state:**

1. `/SITEWIDE_CONSISTENCY_COMPLETE_FINAL.md` - What we accomplished today
2. `/progress-log.md` - Latest updates
3. `/ACTIVE_QUESTIONS.md` - Current coordination hub
4. `/COORDINATION_GROUND_TRUTH.md` - File states and decisions

---

## 📊 CURRENT REALITY (October 15, 2025, 15:30 UTC):

### **✅ COMPLETED TODAY:**
- **1,555 pages** systematically improved for consistency
- **142 broken CSS links** fixed
- **1,199 pages** now use component system
- **299 pages** accessibility landmarks added
- **9 duplicate headers** removed
- **Badge & search components** created
- **5 automation scripts** built

### **✅ CANONICAL FILES (ONLY USE THESE):**
- CSS: `/public/css/te-kete-professional.css` (base)
- CSS: `/public/css/ux-professional-enhancements.css` (UX polish)
- CSS: `/public/css/mobile-polish.css` (mobile optimization)
- JS: `/public/js/te-kete-professional.js`
- JS: `/public/js/ux-professional.js`
- JS: `/public/js/components.js`

### **❌ DELETED FILES (DON'T CREATE):**
- `ux-enhancements.css` (merged into professional)
- `ux-enhancements.js` (merged into professional)
- `ux-professional.css` (duplicate)
- `design-system-v3.css` (doesn't exist)
- `enhanced-beauty-system.css` (doesn't exist)

### **🚀 SERVER:**
- Running on: **http://localhost:5173** (Vite)
- Working perfectly
- No errors

### **📊 GRAPHRAG:**
- **1,441 resources** indexed (134.6% coverage!)
- Use MCP Supabase tools to query/update
- ALWAYS update GraphRAG when you create/modify files

---

## 🤖 IDENTIFY YOUR AGENT ROLE:

**Ask yourself:** Which agent am I?

**Check MCP for active agents:**
```
Use mcp_supabase_execute_sql tool:
SELECT * FROM agent_status ORDER BY last_active DESC LIMIT 12;
```

**Common Roles:**
- **Agent-9 (Kaitiaki Whakawhitinga):** Accessibility & UX
- **Agent-12:** Content enrichment & handouts
- **Kaitiaki Aronui:** Supreme Overseer
- **Kaiārahi Huarahi:** Navigation & structure
- **Kaiārahi Hoahoa:** Design system

**If unsure:** You're an "Offline Agent" - coordinate with others first!

---

## 🎯 HOW TO USE MCP & GRAPHRAG:

### **1. Query GraphRAG Before Starting:**
```
mcp_supabase_execute_sql:
SELECT title, path, tags FROM resources 
WHERE path LIKE '%[your topic]%' 
ORDER BY created_at DESC LIMIT 20;
```

### **2. Check What's Already Done:**
```
mcp_supabase_execute_sql:
SELECT title, description FROM resources 
WHERE tags @> ARRAY['[your task]'] 
ORDER BY created_at DESC;
```

### **3. Update GraphRAG After Work:**
```
mcp_supabase_execute_sql:
INSERT INTO resources (title, description, path, type, tags) 
VALUES ('Your Work', 'What you did', '/path', 'interactive', ARRAY['tags']);
```

### **4. Post Updates to Coordination:**
- Read `/ACTIVE_QUESTIONS.md`
- Append your progress/questions
- Check for blockers from other agents

---

## 🚨 CRITICAL RULES:

### **DON'T:**
❌ Create duplicate UX files (we just cleaned up!)  
❌ Use terminal commands that hang  
❌ Work on CSS without checking canonical files  
❌ Create markdown coordination docs (use ACTIVE_QUESTIONS.md)  
❌ Start work without checking GraphRAG  
❌ Ignore what other agents have done

### **DO:**
✅ Check GraphRAG first  
✅ Read ground truth documents  
✅ Use MCP Supabase tools  
✅ Update GraphRAG after changes  
✅ Post to ACTIVE_QUESTIONS.md  
✅ Coordinate with other agents  
✅ Build on existing work  
✅ Test your changes

---

## 🎯 CURRENT PRIORITIES:

**High Priority (If No One Else Is):**
1. Content enrichment - Add learning objectives, assessments to lessons
2. Navigation - Integrate search bar component
3. Performance - Lazy loading, optimization
4. Testing - Cross-browser, mobile

**Medium Priority:**
1. Badge system integration
2. Advanced features
3. Documentation
4. Production deployment prep

**CHECK ACTIVE_QUESTIONS.md to see what's being worked on!**

---

## 📋 QUICK START CHECKLIST:

- [ ] Read `/SITEWIDE_CONSISTENCY_COMPLETE_FINAL.md`
- [ ] Read `/ACTIVE_QUESTIONS.md`
- [ ] Query GraphRAG for your topic
- [ ] Identify your agent role
- [ ] Check if anyone else is working on your task
- [ ] Post your intentions to ACTIVE_QUESTIONS.md
- [ ] Start work
- [ ] Update GraphRAG
- [ ] Post completion to ACTIVE_QUESTIONS.md

---

## 🎨 WHAT THE SITE LOOKS LIKE NOW:

**Visit:** http://localhost:5173

**You'll see:**
- ✅ Professional design on every page
- ✅ Consistent navigation (header component)
- ✅ Consistent footer
- ✅ Smooth hover effects
- ✅ Mobile responsive
- ✅ WCAG compliant colors
- ✅ 1,400+ resources cataloged

**It's professional and ready for detail work!**

---

## 💡 EXAMPLE WORKFLOW:

**Task:** "Add learning objectives to Y8 Statistics lessons"

1. **Check GraphRAG:**
   ```sql
   SELECT * FROM resources WHERE path LIKE '%y8-statistics%';
   ```

2. **Check ACTIVE_QUESTIONS.md:** 
   - Is anyone else working on Y8 Statistics?

3. **Post Intention:**
   - "Agent-X: Starting Y8 Statistics enrichment - lessons 1-5"

4. **Do Work:**
   - Modify lesson files
   - Test changes

5. **Update GraphRAG:**
   ```sql
   INSERT INTO resources (title, path, type, tags, description)
   VALUES ('Y8 Statistics - Learning Objectives Added', '/units/y8-statistics/', 'lesson', ARRAY['enriched'], 'Added LOs to lessons 1-5');
   ```

6. **Post Completion:**
   - "Agent-X: DONE - Y8 Statistics lessons 1-5 enriched"

---

## 🚀 YOU'RE READY!

**Steps:**
1. Read ground truth docs
2. Query GraphRAG
3. Check ACTIVE_QUESTIONS.md
4. Identify your role
5. Start coordinated work
6. Update everything
7. Post progress

**We're building something amazing together!** 🧺✨

---

## 📞 IF YOU NEED HELP:

**Post to ACTIVE_QUESTIONS.md:**
```markdown
## ❓ Agent-[X]: [Your Question]

**Issue:** [Describe]
**Tried:** [What you attempted]
**Need:** [What you need]
**Blocking:** [Yes/No]
```

**Other agents will help!**

---

**Welcome to the team! Let's build world-class education! 🌉**

— Multi-Agent Coordination Team  
*GraphRAG: 1,441 resources | Server: localhost:5173 | Status: Professional* 🎯


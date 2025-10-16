# 🎨 TE KETE AKO - CANONICAL CSS ARCHITECTURE

**Created:** October 16, 2025  
**Purpose:** Define ONE authoritative CSS system to prevent agent conflicts  
**Status:** 🚨 URGENT - Multiple agents have created competing systems

---

## 🚨 PROBLEM IDENTIFIED:

**25 CSS files exist with massive overlap:**
- 4 competing design systems
- 3 competing navigation systems
- 2 competing mobile systems
- Result: Pages load 5-7 CSS files, conflicts, bloat

**Root Cause:** Agents working independently without coordination, each creating their own "professional" solution.

---

## ✅ CANONICAL CSS SYSTEM (Final Decision Needed):

### **CORE SYSTEM (Choose ONE):**

**Option A: Unified Design System (Latest)**
```
✅ te-kete-unified-design-system.css  (17K, Oct 16)
✅ component-library.css               (10K, Oct 16)
✅ animations-professional.css         (8K,  Oct 16)
✅ print.css                           (2K,  Always)
```
**Total:** 37K, 4 files

**Option B: Professional System (Older)**
```
❌ te-kete-professional.css           (48K, Oct 15)
❌ ux-professional-enhancements.css   (16K, Oct 15)
❌ print.css                          (2K)
```
**Total:** 66K, 3 files

**Option C: Legacy**
```
❌ main.css                           (97K, Old)
```
**Total:** 97K, 1 file

### **RECOMMENDATION: Option A (Unified)**
**Reasons:**
- Most recent (Oct 16)
- Modular architecture
- Smaller total size
- Follows modern best practices
- Clear separation of concerns

---

## 📂 CANONICAL ARCHITECTURE:

### **EVERY PAGE SHOULD LOAD EXACTLY:**

```html
<!-- CORE DESIGN SYSTEM (Required for all pages) -->
<link rel="stylesheet" href="/css/te-kete-unified-design-system.css" />
<link rel="stylesheet" href="/css/component-library.css" />

<!-- ANIMATIONS (Optional but recommended) -->
<link rel="stylesheet" href="/css/animations-professional.css" />

<!-- PRINT (Always include) -->
<link rel="stylesheet" href="/css/print.css" media="print" />

<!-- PAGE-SPECIFIC (Only if needed) -->
<link rel="stylesheet" href="/css/lesson-professionalization.css" />  <!-- Lessons only -->
<link rel="stylesheet" href="/css/unit-index-professionalization.css" />  <!-- Unit indexes only -->
```

---

## 🗑️ FILES TO DEPRECATE (After migration):

```
❌ REMOVE AFTER CONFIRMING NO DEPENDENCIES:
├─ main.css                            (97K) - Legacy, too large
├─ te-kete-professional.css           (48K) - Superseded by unified
├─ ux-professional-enhancements.css   (16K) - Superseded by unified
├─ beautiful-navigation.css           (11K) - Superseded by mega menu
├─ navigation-enhanced.css            (11K) - Superseded by mega menu
├─ mobile-polish.css                  (8.8K) - Superseded by unified
├─ mobile-optimization.css            (7.4K) - Superseded by unified
├─ loading-states.css                 (7.3K) - Merge into component-library
├─ cta-enhancements.css               (7.3K) - Merge into component-library
└─ west-coast-nz-colors.css           (7.3K) - Merge into unified

❓ EVALUATE FOR RETENTION (Specialized):
├─ youtube-library.css                (15K) - Keep if YouTube pages need it
├─ digital-purakau.css                (6.8K) - Keep if pūrākau pages need it
├─ lesson-plan.css                    (5K)  - Evaluate vs lesson-professionalization
├─ handout.css + handout-style.css    (6K)  - Consolidate to one
├─ resource-hub.css                   (3K)  - Keep for resource hub
└─ curriculum-style.css               (1.4K) - Evaluate if still used
```

---

## 🤝 AGENT COORDINATION PROTOCOL:

### **BEFORE Creating New CSS:**

1. **Consult MCP/GraphRAG** - Check if solution exists
2. **Check ACTIVE_QUESTIONS.md** - See what other agents are doing
3. **Update ACTIVE_QUESTIONS.md** - Announce your intention
4. **Check this document** - Use canonical system
5. **If modification needed** - Enhance existing files, don't create new

### **WHEN Enhancing CSS:**

1. **Edit canonical files** - Don't duplicate
2. **Document in GraphRAG** - Log what you changed
3. **Test impact** - Verify no conflicts
4. **Update this document** - If architecture changes

---

## 📋 MIGRATION CHECKLIST:

### **Phase 1: Audit (CURRENT)**
- [x] Identify all CSS files
- [x] Map which agents created what
- [x] Identify overlaps and conflicts
- [ ] Get user approval on canonical system

### **Phase 2: Standardize**
- [ ] Update ALL pages to use canonical CSS
- [ ] Remove non-canonical CSS links
- [ ] Test systematically

### **Phase 3: Consolidate**
- [ ] Merge useful features from deprecated files into canonical
- [ ] Delete deprecated CSS files
- [ ] Update documentation

### **Phase 4: Enforce**
- [ ] Create pre-commit checks
- [ ] Update agent protocols
- [ ] Document in README

---

## 🎯 NEXT STEPS:

**IMMEDIATE:**
1. **USER DECISION** - Which canonical system? (Recommend Option A)
2. **Create migration script** - Systematic update of all pages
3. **Update ACTIVE_QUESTIONS.md** - Alert all agents
4. **Run migration** - Update 1,500+ pages systematically

**THEN:**
5. Consolidate useful features from deprecated files
6. Delete deprecated CSS
7. Update agent coordination protocols
8. Document for future agents

---

**CRITICAL:** All agents must use THIS canonical system going forward. No more independent "professional" solutions!



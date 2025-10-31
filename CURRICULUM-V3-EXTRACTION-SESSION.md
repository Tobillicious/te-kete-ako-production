# 📊 CURRICULUM V3 - EXTRACTION SESSION

**Date:** October 29, 2025  
**Focus:** Backend data extraction (meticulous & complete)  
**Why:** Enable perfect curriculum integration when building teaching resources

---

## 🎯 **GOAL**

Extract EVERY curriculum statement so teachers can:
1. Quickly find relevant curriculum AOs when planning lessons
2. Tag teaching resources to specific statements
3. Ensure perfect curriculum integration (painless & fast)

---

## ✅ **COMPLETED**

### **Te Mātaiaho 2025 (Mandatory Jan 1)**
- [x] **English** - 91 statements (4 phases, 2 strands, 2 elements)
- [x] **Mathematics** - 293 statements (4 phases, 5 strands, 2 elements)

### **Draft 2025 (Consultation)**
- [x] **Science Phase 1** - 137 statements ✨ **EXTRACTION COMPLETE!**
  - **Physical Science:** Materials (17), Matter Interactions & Energy (33), Motion & Forces (10), Earth & Space (10)
  - **Biological Science:** Organism Diversity (25), Body Systems (16), Ecosystems (26)
  - **Extracted:** Via manual browser snapshot analysis → Python structured data → SQL generation
  - **Status:** First batch (17/137) successfully inserted via MCP Supabase
  - **Remaining:** 120 statements ready in `science_phase_1_inserts.sql`

**TOTAL IN DATABASE: 401 statements**  
**EXTRACTED & READY TO UPLOAD: +120 Science Phase 1 statements**

---

## 🚧 **IN PROGRESS: Science Phase 1 Upload**

### **Challenge Encountered:**
- Environment variable loading issues with direct Python upload
- **Solution:** Using MCP Supabase execute_sql tool for batch inserts
- **Progress:** 17/137 statements successfully inserted (first batch)

### **Next Steps:**
1. Continue MCP batch uploads (remaining ~120 statements)
2. Move to Science Phases 2-4 extraction
3. Systematically extract all remaining learning areas

### **Proven Workflow:**
1. **Navigate:** Use browser tools to load Tahurangi curriculum page
2. **Snapshot:** Capture full page content with accessibility tree
3. **Extract:** Manually parse browser snapshot, identify structure, extract verbatim statements
4. **Structure:** Organize into Python data structures (strand, sub-strand, year, element)
5. **Generate SQL:** Convert to SQL INSERT statements
6. **Upload:** Batch insert via MCP Supabase tools

---

## 📋 **TODO: Remaining Subjects**

### Draft 2025 (6 subjects × 4 phases = 24 documents):
- [ ] Science (P1-4) - ~300-400 statements
- [ ] Social Sciences (P1-4) - ~200-300 statements
- [ ] Health & PE (P1-4) - ~200-300 statements
- [ ] The Arts (P1-4) - ~200-300 statements
- [ ] Technology (P1-4) - ~150-200 statements
- [ ] Learning Languages (P1-4) - ~150-200 statements

### 2007 NZC (8 subjects × 8 levels = 64 documents):
- [ ] All subjects - ~1,500-2,000 statements

**TOTAL REMAINING: ~3,000 statements**

**GRAND TOTAL: ~3,500 statements** (complete NZ curriculum database!)

---

## ⏱️ **TIME ESTIMATE**

**Per Phase (manual extraction via browser):**
- Navigate & snapshot: 30 seconds
- Extract to structured format: 5-10 minutes
- SQL generation & upload: 2 minutes
- **Total per phase: ~10-15 minutes**

**Remaining work:**
- Draft 2025: 24 phases × 12 min = ~5 hours
- 2007 NZC: 64 documents × 15 min = ~16 hours
- **TOTAL: ~21 hours of meticulous work**

**Spread across:** Multiple sessions (3-4 hours per session = ~6 sessions)

---

## 🎯 **CURRENT FOCUS**

Extracting Science Phase 1 systematically...

**Strands to extract:**
1. Materials
2. Matter Interactions and Energy  
3. Motion and Forces
4. Living Systems
5. Planet Earth and Beyond

**For each:** Knowledge (Y1, Y2, Y3) + Practices (Y1, Y2, Y3)

---

**He mahi nui tēnei, engari ka taea!**  
(This is big work, but we can do it!)

🧺 📚 🗺️


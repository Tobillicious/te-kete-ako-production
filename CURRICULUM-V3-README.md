# 🏔️ CURRICULUM V3 - PROJECT HUB

**Status:** 🚧 **IN PROGRESS - Phase 1: Database Setup**  
**Started:** October 29, 2025  
**Agent:** Kaitiaki Aronui V3.0

---

## 📋 **QUICK LINKS**

### **Active Documents:**
- **[BACKEND ARCHITECTURE](CURRICULUM-V3-BACKEND-ARCHITECTURE.md)** ⭐ - The source of truth for implementation
- **[GRAND PLAN](CURRICULUM-V3-GRAND-PLAN.md)** - Complete project vision & scope

### **Archived Planning:**
- `archive/curriculum-v3-planning/` - Intermediate planning documents (superseded by final architecture)

---

## 🎯 **WHAT WE'RE BUILDING**

A comprehensive, gorgeous curriculum browser that:
- Hosts ALL NZ Curriculum versions (2007, Te Mātaiaho 2025, Draft 2025)
- Shows ~2,500-3,500 curriculum statements (verbatim from MoE)
- Enables cross-version comparison
- Supports perfect curriculum integration for teaching resources
- Handles the chaos of constant MoE curriculum updates

---

## 📊 **CURRENT SCOPE**

### **Available Curriculum (Oct 2025):**
- **2007 NZC:** 8 subjects × 8 levels = ~64 documents
- **Te Mātaiaho 2025:** 2 subjects × 4 phases (mandatory Jan 1) = 8 documents
- **Draft 2025:** 6 subjects × 4 phases (consultation until Apr 2026) = 24 documents
- **Phase 5 (Years 11-13):** Coming 2026 = 88 subjects

**Total:** ~136 documents → ~2,500-3,500 individual curriculum statements

---

## 🚀 **IMPLEMENTATION PHASES**

### ✅ **Planning Complete** (Oct 29)
- [x] Research curriculum structures
- [x] Design database schema (3 tables)
- [x] Plan data flow architecture
- [x] Design API layer
- [x] Plan GraphRAG integration
- [x] Define performance strategy

### ✅ **Phase 1: Database Setup COMPLETE** (Oct 29)
- [x] Create 3 Supabase tables
- [x] Create indexes & SQL functions
- [x] Set up RLS policies
- [x] Test with sample data
- [x] Verify performance
- **Duration:** 30 minutes
- **Status:** ✅ VERIFIED & WORKING

### ⏳ **Phase 2: Data Extraction** (Weeks 2-3)
- [ ] Build scraping scripts (DeepSeek)
- [ ] Extract English Phase 1-4 (test case)
- [ ] Build validation pipeline
- [ ] Import to Supabase
- [ ] Verify data quality

### ⏳ **Phase 3: GraphRAG Integration** (Week 3)
- [ ] Create curriculum nodes
- [ ] Create relationships
- [ ] Test queries

### ⏳ **Phase 4: API Layer** (Week 4)
- [ ] Build `js/curriculum-api.js`
- [ ] Test all functions
- [ ] Add error handling & caching

### ⏳ **Phase 5: UI Implementation** (Weeks 4-5)
- [ ] Build `curriculum-v3.html`
- [ ] Implement gorgeous browsing interface
- [ ] Implement search & comparison
- [ ] Implement resource linking

### ⏳ **Phase 6: Full Extraction** (Week 6)
- [ ] Extract all subjects & versions
- [ ] Build equivalence mappings
- [ ] Launch! 🎉

---

## 🎨 **CORE FEATURES**

1. **Multi-Version Browser** - Switch between 2007, 2025, and Drafts seamlessly
2. **Timeline Context** - See when things become mandatory, when consultation ends
3. **Status Badges** - Visual clarity on draft vs mandatory vs archived
4. **Cross-Version Comparison** - "Show me the 2007 equivalent of this 2025 statement"
5. **Resource Integration** - "Show me all resources tagged to this statement"
6. **Smart Search** - Full-text search across all curriculum versions
7. **Perfect Planning Tool** - Help teachers navigate the MoE chaos

---

## 📚 **DATABASE SCHEMA**

### **3 New Tables:**
1. **`curriculum_statements`** - All curriculum statements (~2,500-3,500 rows)
2. **`curriculum_equivalences`** - Cross-version mappings
3. **`resource_curriculum_tags`** - Links resources to statements

See [BACKEND ARCHITECTURE](CURRICULUM-V3-BACKEND-ARCHITECTURE.md) for complete schema.

---

## 🎯 **SUCCESS CRITERIA**

- ✅ 100% verbatim curriculum statements (no placeholders)
- ✅ < 200ms page load, < 100ms API responses
- ✅ Teachers can find ANY statement in < 3 clicks
- ✅ Resources can be tagged to curriculum statements
- ✅ Can handle curriculum updates without schema changes

---

## 🤝 **FOR NEXT AGENT**

**If you're picking this up:**
1. Read [BACKEND ARCHITECTURE](CURRICULUM-V3-BACKEND-ARCHITECTURE.md) (the bible)
2. Check Phase progress above
3. Continue where we left off
4. Update this README with your progress

---

**He mahi nui tēnei, engari ka taea!**  
(This is a big job, but we can do it!)

🧺 ✨ 📚 🗺️ 🚀


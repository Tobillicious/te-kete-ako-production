# 📦 BATCH COMMIT STRATEGY - SYSTEMATIC REVIEW

**Total Files:** 1,516 modified + 218 other  
**Approach:** Break into logical, testable sub-batches  
**Testing:** Manual review + git diff between each

---

## 🎯 SUB-BATCH BREAKDOWN

### **SUB-BATCH 3A: Core Site Pages (High Priority)**
**Files:** ~50 files  
**Category:** Homepage, main navigation pages, dashboards

**List:**
- index.html
- lessons.html
- handouts.html
- units/index.html
- resource-hub.html
- teacher-dashboard.html (already committed)
- about.html
- contact.html
- subjects.html
- dashboard.html

**Review process:**
1. git diff each file individually
2. Verify CSS consolidation is correct
3. Check no content was lost
4. Confirm navigation updates
5. Test staged changes

**Commit:** Separate from bulk (these are critical!)

---

### **SUB-BATCH 3B: Y8 Systems Unit (Demo-Critical)**
**Files:** ~50 files  
**Category:** All Y8 Systems lessons and resources

**Review process:**
1. Check sample lessons (lesson-1-1, lesson-5-2)
2. Verify resources updated
3. Confirm no content loss
4. Test with git diff --cached

**Commit:** Separate (demo-critical unit)

---

### **SUB-BATCH 3C: Critical Thinking Unit**
**Files:** ~40 files  
**Category:** All critical thinking lessons

**List from git status:**
- 10 lessons (lesson-1 through lesson-10)
- 5 resources

---

### **SUB-BATCH 3D: Units & Lessons (Bulk)**
**Files:** ~600 files  
**Category:** Walker unit, Te Ao Māori unit, other units

**Review process:**
1. Sample 10-15 files randomly
2. Verify pattern consistency
3. Check no anomalies
4. Commit in groups of 200-300

---

### **SUB-BATCH 3E: Handouts (Bulk)**
**Files:** ~400 files  
**Category:** dist-handouts, integrated-handouts

**Review process:**
1. Sample 10 files
2. Verify pattern
3. Commit in group

---

### **SUB-BATCH 4: Documentation**
**Files:** ~150+ .md files

**Review process:**
1. List all MD files
2. Read key ones (session summaries, reports)
3. Check for sensitive data
4. Commit documentation separately

---

### **SUB-BATCH 5: Scripts & Infrastructure**
**Files:** ~20 files in scripts/

**Review:**
1. Check each script individually
2. Verify no hardcoded paths
3. Confirm proper permissions
4. Commit infrastructure

---

### **SUB-BATCH 6: CSS Files**
**Files:** ~10 CSS files

**Review:**
- main.css changes
- Deleted files (D public/css/ux-enhancements.css, etc.)
- Verify deletions are intentional

---

### **SUB-BATCH 7: Configuration**
**Files:** netlify.toml, progress-log.md, ACTIVE_QUESTIONS.md

**Review:** Each file individually

---

## 🔍 EXECUTION ORDER

**Priority Order:**
1. 3A: Core pages (FIRST - most critical!)
2. 3B: Y8 Systems (SECOND - demo unit!)
3. 6: CSS changes (THIRD - foundation)
4. 5: Scripts (FOURTH - infrastructure)
5. 4: Documentation (FIFTH - records)
6. 3C, 3D, 3E: Remaining units/handouts (SIXTH - bulk)
7. 7: Configuration (LAST - housekeeping)

---

## ✅ TESTING CHECKLIST (Between Each Batch)

**Before staging:**
- [ ] Review git diff samples (10-15 files)
- [ ] Check no sensitive data
- [ ] Verify logical grouping

**After staging:**
- [ ] git diff --cached --stat (review summary)
- [ ] git diff --cached [sample-file] (spot check)
- [ ] Verify file count matches expectation

**After commit:**
- [ ] git log --oneline -1 (verify message)
- [ ] git show --stat (review commit summary)
- [ ] Note any issues for next batch

---

**Status:** Strategy defined, ready to execute systematically  
**Next:** Start with SUB-BATCH 3A (Core Pages)


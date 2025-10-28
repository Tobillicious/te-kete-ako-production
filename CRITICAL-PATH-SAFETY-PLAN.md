# 🛡️ CRITICAL PATH - SAFETY-FIRST PLAN
**Created:** Oct 28, 2025  
**Purpose:** Execute Critical Path with ZERO risk of breaking things  
**Principle:** Test-first, backup-always, verify-each-step

---

## ⚠️ **YOUR CONCERN (Valid!)**
> "I am worried about breaking something"

**Translation:** 
- We're about to touch ~200+ HTML files
- One mistake could break navigation site-wide
- Auth is working now, don't want to regress
- Need to be METICULOUS and REVERSIBLE

**Response:** ABSOLUTELY RIGHT! Let's build in safety nets.

---

## 🔒 **SAFETY PROTOCOLS**

### **Protocol 1: Test Before Touch**
- ✅ Never edit files blindly
- ✅ Always test on localhost first
- ✅ Visual confirmation before proceeding
- ✅ Document current state before changes

### **Protocol 2: Backup Everything**
- ✅ Git branch for this work
- ✅ Copy files before bulk operations
- ✅ Save checkpoint commits
- ✅ Can rollback instantly if needed

### **Protocol 3: One-at-a-Time Verification**
- ✅ Test on 1 file first
- ✅ Verify it works
- ✅ Then test on 3 files
- ✅ Only then do bulk operation

### **Protocol 4: Fail-Safe Stops**
- 🛑 If ANYTHING looks wrong, STOP
- 🛑 If console shows errors, STOP
- 🛑 If page breaks, STOP and revert
- 🛑 If unsure, ASK before proceeding

---

## 📋 **THE SAFE EXECUTION PLAN**

### **PHASE 0: PREPARATION (5 mins)** 🔒
**Goal:** Set up safety nets BEFORE touching anything

**Steps:**
1. Check local server is running
2. Check no uncommitted changes (git status)
3. Create safety branch: `git checkout -b auth-scaling-oct28`
4. Document current working state (screenshots)

**Success Criteria:**
- [x] Clean git state
- [x] Safety branch created
- [x] Can rollback if needed

**Risk Level:** 🟢 ZERO - Just preparation

---

### **PHASE 1: VISUAL TESTING (15 mins)** 🔍
**Goal:** SEE what's broken vs working - NO CODE CHANGES

**Test Checklist:**
```
□ Navigate to http://localhost:8001
□ Login with test4@tekete.nz / TestPass123
□ Check header on index.html (should show "👤 test4")
□ Navigate to browse.html (should still show user)
□ Navigate to lessons.html (probably shows "Login")
□ Navigate to handouts.html (probably shows "Login")
□ Navigate to unit-plans.html (probably shows "Login")
□ Try hovering over user menu (does dropdown appear?)
□ Check browser console for errors
□ Take screenshots of broken pages
```

**What We'll Learn:**
- Which pages are actually broken
- If dropdown works or not
- Any console errors to fix first
- Scope of the problem

**Deliverable:** 
- Written list: "Working pages: X, Y, Z" 
- Written list: "Broken pages: A, B, C"
- Screenshot evidence

**Risk Level:** 🟢 ZERO - Just observing

---

### **PHASE 2A: FIX DROPDOWN (IF BROKEN)** 🔧
**Goal:** Fix dropdown CSS WITHOUT touching any files yet

**Safe Approach:**
1. Open DevTools on index.html (where it should work)
2. Inspect `.user-menu-nav` and `.nav-dropdown`
3. Check computed styles in browser
4. Try CSS tweaks in DevTools FIRST
5. Once working in DevTools, THEN edit main.css
6. Test on multiple pages
7. Commit JUST this fix before proceeding

**Rollback Plan:**
- If CSS breaks site: `git checkout main.css`
- If commit needed: `git commit -m "fix: user dropdown hover"`

**Risk Level:** 🟡 LOW - Only touching CSS, can revert easily

---

### **PHASE 2B: VERIFY DROPDOWN (IF WORKING)** ✅
**Goal:** Confirm dropdown works, document for future

**Steps:**
1. Test dropdown on index.html
2. Test dropdown on browse.html
3. Test dropdown on my-kete.html
4. Document: "Dropdown works on pages with auth-ui.js"
5. Proceed to Phase 3

**Risk Level:** 🟢 ZERO - Just testing

---

### **PHASE 3: ADD AUTH SCRIPTS (INCREMENTALLY)** 📝

#### **Step 3.1: IDENTIFY FILES (5 mins)** 🔍
**What to do:**
```bash
# Check which main pages are missing auth scripts
grep -L "auth-ui.js" lessons.html handouts.html unit-plans.html games.html activities.html youtube.html curriculum-v2.html other-resources.html
```

**Deliverable:** List of 8 files that need updating

**Risk Level:** 🟢 ZERO - Just checking

---

#### **Step 3.2: BACKUP FILES (2 mins)** 💾
**What to do:**
```bash
# Create backup directory
mkdir -p backups/oct28-auth-scaling

# Backup the 8 main navigation pages
cp lessons.html backups/oct28-auth-scaling/
cp handouts.html backups/oct28-auth-scaling/
cp unit-plans.html backups/oct28-auth-scaling/
# ... (repeat for all 8)
```

**Deliverable:** Backup files safely stored

**Rollback Plan:** `cp backups/oct28-auth-scaling/lessons.html .`

**Risk Level:** 🟢 ZERO - Just creating backups

---

#### **Step 3.3: TEST ON ONE FILE (10 mins)** 🧪
**Goal:** Prove the approach works on ONE file before touching others

**File to test:** `lessons.html` (arbitrary choice)

**What to do:**
1. Open lessons.html in editor
2. Find the closing `</body>` tag
3. Add auth scripts BEFORE `</body>`:
   ```html
   <!-- Supabase CDN -->
   <script src="https://unpkg.com/@supabase/supabase-js@2"></script>
   <!-- Supabase Client -->
   <script src="js/supabase-client.js"></script>
   <!-- Auth UI -->
   <script src="js/auth-ui.js"></script>
   <!-- Load main functionality -->
   <script src="js/main.js"></script>
   ```
4. Save file
5. Refresh http://localhost:8001/lessons.html in browser
6. **CHECK:** Does header show "👤 test4"?
7. **CHECK:** Any console errors?
8. **CHECK:** Does page still work normally?

**Success Criteria:**
- Header shows logged-in user ✅
- No console errors ✅
- Page functionality intact ✅

**IF SUCCESS:** Proceed to Step 3.4  
**IF FAILURE:** STOP, debug, fix, then retry

**Rollback Plan:** `cp backups/oct28-auth-scaling/lessons.html .`

**Risk Level:** 🟡 LOW - Only 1 file, easily reversible

---

#### **Step 3.4: COMMIT CHECKPOINT (1 min)** 💾
**What to do:**
```bash
git add lessons.html
git commit -m "feat: add auth scripts to lessons.html (test successful)"
```

**Why:** If next steps fail, we can rollback to here

**Risk Level:** 🟢 ZERO - Just git safety

---

#### **Step 3.5: APPLY TO REMAINING 7 FILES (20 mins)** 📦
**Goal:** Now that we KNOW it works, apply to others

**What to do:**
1. Repeat Step 3.3 for each remaining file:
   - handouts.html
   - unit-plans.html
   - games.html
   - activities.html
   - youtube.html
   - curriculum-v2.html
   - other-resources.html

2. After EACH file:
   - Save
   - Refresh in browser
   - Verify header shows user
   - Check for console errors

3. If ALL 7 succeed, commit:
   ```bash
   git add handouts.html unit-plans.html games.html activities.html youtube.html curriculum-v2.html other-resources.html
   git commit -m "feat: add auth scripts to all main navigation pages"
   ```

**Success Criteria:**
- All 8 main pages show logged-in state ✅
- No console errors on any page ✅
- Navigation still works ✅

**Rollback Plan:** 
- Single file: `cp backups/oct28-auth-scaling/FILENAME.html .`
- All files: `git reset --hard HEAD~1`

**Risk Level:** 🟡 LOW - We've proven it works on lessons.html first

---

### **PHASE 4: SCALE SAVE BUTTONS (CAREFUL BULK OPERATION)** 💾

#### **Step 4.1: ANALYZE HANDOUT STRUCTURE (10 mins)** 🔍
**Goal:** Understand file structure before bulk editing

**What to do:**
1. Read 3-5 sample handout files
2. Find where scripts are loaded (usually before `</body>`)
3. Check if any already have Save buttons
4. Identify consistent patterns for insertion point

**Sample files to check:**
```bash
cat handouts/media-literacy-comprehension-handout.html | grep -A 5 "</body>"
cat handouts/writers-toolkit-tone-handout.html | grep -A 5 "</body>"
cat handouts/cognitive-biases-comprehension-handout.html | grep -A 5 "</body>"
```

**Deliverable:** 
- Note: "Scripts go before line X"
- Note: "Y files already have Save button"
- Note: "Z files need Save button added"

**Risk Level:** 🟢 ZERO - Just reading files

---

#### **Step 4.2: CREATE TEST SCRIPT (15 mins)** 🧪
**Goal:** Write a Python/bash script that can add Save buttons safely

**Approach A: Python Script (SAFER)**
```python
# add-save-button.py
import sys
import re

def add_save_button(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if Save button already exists
    if 'data-save-resource' in content:
        print(f"SKIP: {filepath} already has Save button")
        return False
    
    # Extract resource title from <title> tag
    title_match = re.search(r'<title>(.*?)</title>', content)
    resource_title = title_match.group(1).split('|')[0].strip() if title_match else "Resource"
    
    # Determine resource type from path
    resource_type = 'handout'  # Default
    
    # Create resource URL (relative path)
    resource_url = filepath.replace('/Users/admin/Documents/te-kete-ako-clean/', '/')
    
    # Save button HTML
    save_button_html = f'''
<!-- Save Button -->
<div class="no-print" style="background-color: var(--color-surface); padding: 1rem; border-radius: 8px; margin-bottom: 2rem; text-align: center; display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
    <button 
        data-save-resource 
        data-resource-url="{resource_url}"
        data-resource-title="{resource_title}"
        data-resource-type="{resource_type}"
        class="btn-primary" 
        style="flex-grow: 1; max-width: 250px;">
        ⭐ Save to My Kete
    </button>
    <button onclick="window.print()" class="btn-secondary" style="flex-grow: 1; max-width: 250px;">
        🖨️ Print or Save as PDF
    </button>
</div>

<!-- Notification Area -->
<div id="notification-area" style="position: fixed; top: 1rem; right: 1rem; z-index: 10000;"></div>
'''
    
    # Find insertion point (after opening <main> or <div class="content-area">)
    insertion_pattern = r'(<main[^>]*>|<div class="content-area">)'
    match = re.search(insertion_pattern, content)
    
    if not match:
        print(f"ERROR: {filepath} - Cannot find insertion point")
        return False
    
    # Insert Save button after opening tag
    insert_pos = match.end()
    new_content = content[:insert_pos] + save_button_html + content[insert_pos:]
    
    # Check if scripts already present
    if 'save-resource.js' not in content:
        # Add scripts before </body>
        scripts = '''
<!-- Supabase CDN -->
<script src="https://unpkg.com/@supabase/supabase-js@2"></script>
<!-- Supabase Client -->
<script src="../js/supabase-client.js"></script>
<!-- Save Resource Functionality -->
<script src="../js/save-resource.js"></script>
'''
        new_content = new_content.replace('</body>', scripts + '</body>')
    
    # Write back (DRY RUN - just print, don't write yet)
    print(f"SUCCESS: Would update {filepath}")
    print(f"  Title: {resource_title}")
    print(f"  URL: {resource_url}")
    return True

# Test on 3 files first
test_files = [
    'handouts/writers-toolkit-tone-handout.html',
    'handouts/cognitive-biases-comprehension-handout.html',
    'handouts/figurative-language-handout.html'
]

for f in test_files:
    add_save_button(f)
```

**What to do:**
1. Create `add-save-button.py`
2. Run on 3 test files (DRY RUN - doesn't write yet)
3. Verify output looks correct
4. Manually check one file to confirm logic

**Risk Level:** 🟢 ZERO - Script doesn't write files yet (dry run)

---

#### **Step 4.3: TEST SCRIPT ON 3 FILES (10 mins)** 🧪
**Goal:** Actually apply script to 3 files, verify they work

**What to do:**
1. Backup 3 test files:
   ```bash
   cp handouts/writers-toolkit-tone-handout.html backups/oct28-auth-scaling/
   cp handouts/cognitive-biases-comprehension-handout.html backups/oct28-auth-scaling/
   cp handouts/figurative-language-handout.html backups/oct28-auth-scaling/
   ```

2. Modify script to actually WRITE files (add `with open(filepath, 'w') as f: f.write(new_content)`)

3. Run script on 3 files

4. Open each file in browser:
   - http://localhost:8001/handouts/writers-toolkit-tone-handout.html
   - http://localhost:8001/handouts/cognitive-biases-comprehension-handout.html
   - http://localhost:8001/handouts/figurative-language-handout.html

5. For EACH file, verify:
   - Page loads correctly ✅
   - Save button appears ✅
   - Clicking Save button works ✅
   - Resource appears in My Kete ✅
   - No console errors ✅

**IF ALL 3 SUCCEED:** Proceed to Step 4.4  
**IF ANY FAIL:** STOP, fix script, rollback, retry

**Rollback Plan:** `cp backups/oct28-auth-scaling/*.html handouts/`

**Risk Level:** 🟡 MEDIUM - Editing files, but only 3, easily reversible

---

#### **Step 4.4: COMMIT CHECKPOINT (1 min)** 💾
```bash
git add handouts/writers-toolkit-tone-handout.html handouts/cognitive-biases-comprehension-handout.html handouts/figurative-language-handout.html add-save-button.py
git commit -m "feat: add Save buttons to 3 test handouts (script proven)"
```

**Why:** Safety checkpoint before bulk operation

**Risk Level:** 🟢 ZERO - Just git safety

---

#### **Step 4.5: BULK OPERATION (30 mins)** 📦
**Goal:** Apply to ALL handouts (but CAREFULLY)

**What to do:**
1. Get list of ALL handouts without Save button:
   ```bash
   grep -L "data-save-resource" handouts/*.html > handouts-to-update.txt
   ```

2. Count how many files:
   ```bash
   wc -l handouts-to-update.txt
   ```

3. **DECISION POINT:** If > 100 files, do in batches of 20

4. Run script on first batch (20 files):
   ```python
   with open('handouts-to-update.txt') as f:
       files = f.readlines()[:20]  # First 20
   
   for filepath in files:
       add_save_button(filepath.strip())
   ```

5. **IMMEDIATELY TEST:**
   - Open 3-5 random files from batch
   - Verify they work
   - Check My Kete updates correctly

6. If batch succeeds, commit:
   ```bash
   git add handouts/
   git commit -m "feat: add Save buttons to handouts (batch 1 of N)"
   ```

7. Repeat for next batch

**Success Criteria:**
- All handouts have Save button ✅
- All Save buttons work ✅
- No files broken ✅

**Rollback Plan:**
- Last batch: `git reset --hard HEAD~1`
- All batches: `git checkout main` (if on safety branch)

**Risk Level:** 🟡 MEDIUM - Bulk operation, but batched and checkpointed

---

### **PHASE 5: FINAL VERIFICATION (30 mins)** ✅

**Complete Testing Checklist:**
```
□ Fresh incognito browser
□ Browse site (not logged in)
□ Navigate to 5 different page types (index, browse, lessons, handout, unit)
□ Header shows "Login" on all pages ✅
□ Click a handout with Save button
□ Click "Save" → redirects to login ✅
□ Register new account → flow works ✅
□ Login → header updates to "👤 username" ✅
□ Navigate to 5 different pages → header stays updated ✅
□ Open 5 different handouts → all have Save button ✅
□ Save 3 different resources → all work ✅
□ Open My Kete → all 3 resources appear ✅
□ Delete one resource → works ✅
□ Hover over user menu → dropdown appears ✅
□ Click "Sign Out" → header updates ✅
```

**If ALL pass:** ✅ CRITICAL PATH COMPLETE!  
**If ANY fail:** 🛑 Debug and fix

**Risk Level:** 🟢 ZERO - Just testing

---

## 🔄 **ROLLBACK PROCEDURES**

### **Emergency Rollback (Nuclear Option)**
```bash
# If EVERYTHING is broken
git checkout main
git branch -D auth-scaling-oct28
# You're back to working state
```

### **Partial Rollback (Undo last step)**
```bash
# Undo last commit but keep file changes
git reset --soft HEAD~1

# Undo last commit and discard file changes
git reset --hard HEAD~1
```

### **File-Level Rollback**
```bash
# Restore single file from backup
cp backups/oct28-auth-scaling/FILENAME.html .

# Restore single file from git
git checkout main -- FILENAME.html
```

---

## ⏱️ **TIME ESTIMATES (Conservative)**

| Phase | Optimistic | Realistic | Pessimistic |
|-------|-----------|-----------|-------------|
| Phase 0: Prep | 5 mins | 5 mins | 10 mins |
| Phase 1: Testing | 10 mins | 15 mins | 20 mins |
| Phase 2: Dropdown | 15 mins | 30 mins | 1 hour |
| Phase 3: Auth Scripts | 30 mins | 45 mins | 1.5 hours |
| Phase 4: Save Buttons | 1 hour | 1.5 hours | 2 hours |
| Phase 5: Verification | 20 mins | 30 mins | 45 mins |
| **TOTAL** | **2.5 hours** | **3.5 hours** | **5.5 hours** |

**Plan for:** 3.5 hours (realistic)  
**Buffer for:** 5.5 hours (if things go wrong)

---

## ✅ **SUCCESS CRITERIA**

**Minimum Success (Must Have):**
- [ ] User dropdown works on all pages
- [ ] Auth state persists across navigation
- [ ] No pages broken
- [ ] Can rollback if needed

**Target Success (Should Have):**
- [ ] All main pages show auth state
- [ ] All handouts have Save button
- [ ] End-to-end user journey works
- [ ] No console errors

**Stretch Success (Nice to Have):**
- [ ] All lessons have Save button
- [ ] All units have Save button
- [ ] Deployed to tekete.co.nz
- [ ] GraphRAG updated

---

## 🚦 **DECISION POINTS**

**After Phase 1 (Testing):**
- ✅ If dropdown works → Skip Phase 2, go to Phase 3
- ⚠️ If dropdown broken → Must fix in Phase 2

**After Phase 3.3 (First File Test):**
- ✅ If successful → Proceed to Phase 3.5
- 🛑 If fails → STOP, debug, don't proceed

**After Phase 4.3 (3-File Test):**
- ✅ If all 3 work → Proceed to bulk
- 🛑 If any fail → STOP, fix script

**After Any Batch in 4.5:**
- ✅ If batch works → Continue to next batch
- 🛑 If batch fails → STOP, rollback, fix

---

## 💡 **KEY SAFETY PRINCIPLES**

1. **Never skip testing** - Always verify before proceeding
2. **Never skip backups** - Always create before editing
3. **Never bulk without proving** - Test on 1, then 3, then all
4. **Never proceed if broken** - STOP and fix first
5. **Never commit without testing** - Verify it works first

---

**Ready to start with Phase 0: Preparation?** 🛡️

This plan ensures we can:
- ✅ Make progress safely
- ✅ Catch problems early
- ✅ Rollback instantly if needed
- ✅ Know exactly where we are
- ✅ Sleep well tonight!


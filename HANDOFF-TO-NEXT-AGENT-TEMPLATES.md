# 🔄 HANDOFF TO NEXT AGENT - Template Cleanup Task

**Date:** October 28, 2025 (Evening)  
**From:** Current agent (Auth system completion)  
**To:** Next agent (Template cleanup specialist)  
**Task:** Clean up and standardize `/templates/` directory

---

## 🎯 **WHAT WE ACCOMPLISHED TODAY:**

### **✅ Auth System 99% Complete:**
- Fixed user dropdown CSS
- Added auth scripts to 8 navigation pages
- Fixed password reset (no more Netlify errors)
- Added resend email with 60s cooldown
- Created 6 beautiful email templates
- Fixed icon consistency across all pages
- **DEPLOYED TO LIVE** at tekete.co.nz
- **TESTED END-TO-END** - Everything works!

### **✅ Template Cleanup Started:**
- Deleted 7 redundant templates (Tailwind-based, demos, ULTIMATE variants)
- Identified 4 core templates to keep
- **STATUS:** Partially complete - needs final touches

---

## 📋 **REMAINING WORK ON TEMPLATES:**

### **Current State:**
**Kept (4 templates):**
1. `handout-template.html` - ✅ Uses main.css only
2. `lesson-template.html` - ⚠️ Needs auth scripts update
3. `unit-template.html` - ⚠️ Needs auth scripts update
4. `game-template.html` - ⚠️ Needs checking

**Deleted (7 files):**
- All Tailwind-based templates ✅
- All "ULTIMATE" templates with inline CSS ✅
- All demo files ✅

---

## 🔧 **WHAT NEXT AGENT NEEDS TO DO:**

### **Task 1: Update Remaining Templates (30 mins)**

**Fix all 4 templates to match current system:**

**Add to each template:**
1. **Fix auth nav icons** - Remove `data-icon` attributes, add actual emojis:
```html
<!-- OLD (broken): -->
<span class="nav-icon" data-icon="login"></span>

<!-- NEW (working): -->
<span class="nav-icon">🔐</span>
```

2. **Add auth scripts before `</body>`:**
```html
<!-- Supabase CDN -->
<script src="https://unpkg.com/@supabase/supabase-js@2"></script>
<!-- Supabase Client -->
<script src="../js/supabase-client.js"></script>
<!-- Auth UI -->
<script src="../js/auth-ui.js"></script>
<!-- Load main functionality -->
<script src="../js/main.js"></script>
```

3. **Add Save to My Kete button** (for handouts):
```html
<div class="no-print" style="margin-bottom: 2rem; text-align: center;">
    <button 
        data-save-resource 
        data-resource-url="{{RESOURCE_URL}}"
        data-resource-title="{{RESOURCE_TITLE}}"
        data-resource-type="handout"
        class="btn-primary" 
        style="margin-right: 1rem;">
        ⭐ Save to My Kete
    </button>
    <button onclick="window.print()" class="btn-secondary">
        🖨️ Print or Save as PDF
    </button>
</div>

<!-- Then add save-resource.js script -->
<script src="../js/save-resource.js"></script>
```

4. **Update footer links** - Remove placeholder `#` links:
```html
<!-- OLD: -->
<a href="#about">ℹ️ About Us / Mō Mātou</a>

<!-- NEW: -->
<a href="/about.html">ℹ️ About Us / Mō Mātou</a>
```

---

### **Task 2: Create Missing Templates (1 hour)**

**Need these templates based on actual content:**

**2a. Activity Template** (`activity-template.html`)
- Based on existing files in `/activities/` directory
- For 5-10 minute "Do Now" warm-up activities
- Simple structure, quick to fill
- Example: Look at any file in `/activities/`

**2b. Video Activity Template** (`video-activity-template.html`)
- Based on files in `/handouts/video-activities/`
- For YouTube comprehension activities
- Includes: video embed, questions, reflection
- Example: `handouts/video-activities/bastion-point-video-activity.html`

**2c. Assessment Template** (`assessment-template.html`) - OPTIONAL
- For quizzes/tests
- May not be needed for beta
- Can defer to post-launch

---

### **Task 3: Update Documentation (15 mins)**

**Update `README.md`:**
- List final 6 templates (4 current + 2 new)
- Remove references to deleted templates
- Add examples of when to use each
- Include the auth scripts update instructions

---

## 📂 **FILE LOCATIONS:**

**Templates:** `/Users/admin/Documents/te-kete-ako-clean/templates/`  
**Actual handouts:** `/Users/admin/Documents/te-kete-ako-clean/handouts/`  
**Actual lessons:** `/Users/admin/Documents/te-kete-ako-clean/lessons/` and `/units/lessons/`  
**Activities:** `/Users/admin/Documents/te-kete-ako-clean/activities/`  
**Video activities:** `/Users/admin/Documents/te-kete-ako-clean/handouts/video-activities/`

---

## 🎨 **DESIGN SYSTEM RULES (CRITICAL!):**

### **DO:**
- ✅ Use ONLY `css/main.css` (adjust path: `../css/main.css` from subdirectories)
- ✅ Use emojis for icons (👤 🔐 🧺 📚 etc.)
- ✅ Include whakataukī (cultural opening)
- ✅ Add bilingual elements (Te Reo Māori + English)
- ✅ Make print-friendly (A4 optimized)
- ✅ Include Supabase auth scripts

### **DON'T:**
- ❌ Add Tailwind CSS
- ❌ Add inline `<style>` blocks (use main.css classes)
- ❌ Use `data-icon` attributes (use actual emojis)
- ❌ Create "ULTIMATE" or "PERFECT" versions
- ❌ Add multiple CSS files
- ❌ Follow GraphRAG design documentation (it's outdated)

---

## 🧪 **TESTING TEMPLATES:**

**How to test:**
1. Copy template to appropriate directory
2. Fill in placeholders
3. Open in browser: `http://localhost:8001/handouts/test.html`
4. Check:
   - ✅ Loads without errors
   - ✅ Design matches site aesthetic
   - ✅ Sidebar appears with whakataukī
   - ✅ Header shows auth state
   - ✅ Footer links work
   - ✅ Print preview (Cmd+P) looks good

---

## 📊 **REFERENCE: Working Handout Example**

**Best example:** `handouts/media-literacy-comprehension-handout.html`

**Why it's good:**
- Uses main.css only ✅
- Has full sidebar with whakataukī ✅
- Save to My Kete button ✅
- Auth scripts included ✅
- Print-optimized ✅
- Footer links updated ✅

**Use this as the gold standard!**

---

## 🚨 **KNOWN ISSUES TO AVOID:**

### **1. Empty Icon Spans**
```html
❌ <span class="nav-icon" data-icon="login"></span>
✅ <span class="nav-icon">🔐</span>
```

### **2. Missing Auth Scripts**
All templates need Supabase + auth-ui.js + main.js

### **3. Placeholder Footer Links**
```html
❌ <a href="#about">About</a>
✅ <a href="/about.html">About</a>
```

### **4. Missing Save Button**
Handouts should have "Save to My Kete" button

---

## 🎯 **SUCCESS CRITERIA:**

**Templates are done when:**
- [ ] All 4 templates updated with auth scripts
- [ ] All icons use actual emojis (no data-icon)
- [ ] Footer links point to real pages
- [ ] Activity + video-activity templates created
- [ ] README.md updated with final list
- [ ] Tested one template of each type
- [ ] No Tailwind, no inline CSS
- [ ] All use main.css only

**Estimated time:** 1.5 - 2 hours

---

## 📚 **GRAPHRAG UPDATE NEEDED:**

Add these resources to GraphRAG after completion:
- Template system overview
- Each final template
- Relationships between templates and actual content

---

## 💬 **CONTEXT FOR NEXT AGENT:**

**Project Status:**
- ✅ Auth system: 99% complete, deployed live
- ✅ My Kete: Working perfectly
- ✅ Save feature: Functional
- ⚠️ Templates: Cleaned up but need final updates

**Priority:**
- **High:** Update 4 existing templates
- **Medium:** Create activity + video-activity templates
- **Low:** Create assessment template

**Blockers:** ZERO! This is polish work, not critical path.

---

## 🚀 **DEPLOYMENT:**

**After templates are done:**
1. Push to GitHub (user must do - git hanging)
2. Cloudflare auto-deploys in 1-2 mins
3. Templates will be available for content creation

**Not urgent** - templates are for FUTURE content creation, not beta launch blocker!

---

## 📞 **QUESTIONS TO ASK USER:**

1. Do you want activity templates now or post-beta?
2. Should templates match `media-literacy-comprehension-handout.html` exactly?
3. Any specific features needed in templates?

---

*Handoff created: October 28, 2025*  
*Task complexity: Medium*  
*Estimated time: 1.5-2 hours*  
*Blockers: None*  
*Dependencies: None (standalone task)*


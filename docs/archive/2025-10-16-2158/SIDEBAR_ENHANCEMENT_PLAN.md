# 🎯 SIDEBAR ENHANCEMENT PLAN

**Goal:** Fix layout issues and enrich sidebars with comprehensive external resource links

---

## 📋 WHAT SIDEBAR SHOULD CONTAIN:

### ✅ **CORRECT Sidebar Content:**
1. **Unit Navigation Links**
   - Link to unit overview
   - Links to all lessons in sequence
   - Current lesson highlighted

2. **Related External Resources** (ENHANCED)
   - 10-15 curated NZ educational authority links
   - Subject-specific resources
   - Cultural resources (Te Ara, TPK, etc.)
   - Ministry/Government resources
   - Teaching support resources

3. **Cultural Elements**
   - Whakataukī with translation
   - House value connections
   - Cultural safety notes

4. **Quick Tools**
   - Print lesson button
   - Download handout links
   - Assessment rubric links

### ❌ **INCORRECT (Should be in Main Content):**
- Lesson activities and instructions
- Detailed learning sequences
- Student work examples
- Full lesson flow/timing

---

## 🔧 FILES TO FIX:

**Found 27 files with sidebars - checking each for:**
1. Lesson content incorrectly in sidebar → move to main
2. Insufficient external links in sidebar → enhance with 10-15 quality links
3. Broken structure → repair

---

## 🌟 ENHANCED SIDEBAR TEMPLATE:

```html
<aside class="left-sidebar no-print">
    <!-- Navigation -->
    <div class="sidebar-widget">
        <h3 class="sidebar-widget-title">📚 Unit Navigation</h3>
        <ul>
            <li><a href="/unit-overview.html">← Unit Overview</a></li>
            <li><strong>Current Lesson</strong></li>
            <li><a href="/next-lesson.html">Next Lesson →</a></li>
        </ul>
    </div>
    
    <!-- External Resources (ENHANCED!) -->
    <div class="sidebar-widget">
        <h3 class="sidebar-widget-title">🔗 External Resources</h3>
        <h4>Subject Resources:</h4>
        <ul>
            <li><a href="[TKI link]" target="_blank">TKI - [Specific Topic]</a></li>
            <li><a href="[NZCER link]" target="_blank">NZCER - [Research]</a></li>
            <li><a href="[Authority link]" target="_blank">[Subject Authority]</a></li>
            <!-- 5-8 subject-specific links -->
        </ul>
        
        <h4>Cultural Context:</h4>
        <ul>
            <li><a href="https://teara.govt.nz/" target="_blank">Te Ara Encyclopedia</a></li>
            <li><a href="https://www.tpk.govt.nz/" target="_blank">Te Puni Kōkiri</a></li>
            <li><a href="https://maoridictionary.co.nz/" target="_blank">Māori Dictionary</a></li>
            <!-- 3-5 cultural links -->
        </ul>
        
        <h4>Teaching Support:</h4>
        <ul>
            <li><a href="[NZQA link]" target="_blank">NZQA - Assessment</a></li>
            <li><a href="[Education Counts]" target="_blank">Education Counts</a></li>
            <!-- 2-4 teaching support links -->
        </ul>
    </div>
    
    <!-- Cultural Element -->
    <div class="sidebar-widget">
        <h3 class="sidebar-widget-title">🌿 Whakataukī</h3>
        <p style="font-style: italic;">"[Māori proverb]"</p>
        <p style="font-size: 0.9rem;">[Translation and relevance]</p>
    </div>
    
    <!-- Quick Tools -->
    <div class="sidebar-widget">
        <h3 class="sidebar-widget-title">⚡ Quick Tools</h3>
        <ul>
            <li><button onclick="window.print()">🖨️ Print Lesson</button></li>
            <li><a href="[handout]">📄 Student Handout</a></li>
            <li><a href="[rubric]">📊 Assessment Rubric</a></li>
        </ul>
    </div>
</aside>
```

---

## 📊 IMPLEMENTATION STRATEGY:

1. **Audit Phase** (Quick)
   - Check all 27 files
   - Identify structure issues
   - List files needing fixes

2. **Fix Phase** (Systematic)
   - Move any lesson content from sidebar to main
   - Ensure main content has full lesson
   - Verify proper HTML structure

3. **Enhancement Phase** (Quality)
   - Add 10-15 external resource links per sidebar
   - Topic-specific NZ authority resources
   - Cultural context links
   - Teaching support resources

4. **Verification Phase**
   - Test layouts visually
   - Ensure responsive design works
   - Verify all links functional

---

## 🎯 SUCCESS METRICS:

- ✅ 0 files with lesson content in sidebar
- ✅ 27 files with enhanced external resource links (10-15 each)
- ✅ 100% consistent sidebar structure
- ✅ All sidebars provide value to teachers

---

**Status:** Planning complete, beginning audit and fixes now!

**Kaiārahi Ako (agent-5)**  
Fixing structure + enriching resources


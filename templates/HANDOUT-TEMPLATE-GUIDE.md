# 📚 HANDOUT TEMPLATE SYSTEM GUIDE

## 🎯 PURPOSE
Ensures all Te Kete Ako handouts have:
- Consistent layout and navigation
- Proper sidebar positioning
- Cultural integration (whakataukī)
- Print-friendly formatting
- Responsive design

---

## 🏗️ TEMPLATE STRUCTURE

### Core Layout Pattern:
```html
<div class="main-container">
  <aside class="left-sidebar no-print">
    <!-- Related resources & whakataukī -->
  </aside>
  <main class="content-area">
    <!-- Cultural opening + handout content -->
  </main>
</div>
```

---

## 🔧 TEMPLATE VARIABLES

Replace these placeholders when creating new handouts:

### Basic Info:
- `{{HANDOUT_TITLE}}` - e.g., "Bar Graph Construction & Analysis"
- `{{HANDOUT_SUBTITLE}}` - e.g., "Level 4 Achievement Objectives"
- `{{SUBJECT}}` - e.g., "math", "english", "science"
- `{{SUBJECT_NAME}}` - e.g., "Mathematics", "English", "Science"

### Cultural Integration:
- `{{WHAKATAUKI_MAORI}}` - The te reo Māori proverb
- `{{WHAKATAUKI_ENGLISH}}` - English translation
- `{{WHAKATAUKI_CONNECTION}}` - How it connects to the lesson content

### Content:
- `{{RELATED_RESOURCES}}` - List items for sidebar links
- `{{HANDOUT_CONTENT}}` - Main educational content

---

## 📋 WHAKATAUKĪ SELECTION GUIDE

### For Mathematics/Data:
- **"Ehara taku toa i te toa takitahi, engari he toa takitini"**
  - *Success is not the work of one, but the work of many*
  - Use for: graphs, statistics, collaborative problem-solving

### For Arts/Creativity:
- **"Toi te kupu, toi te mana, toi te whenua"**
  - *Art of language, art of prestige, art of the land*
  - Use for: visual arts, creative writing, expression

### For Science/Discovery:
- **"Ka mua, ka muri"**
  - *Walking backwards into the future*
  - Use for: combining traditional & modern knowledge

### For English/Communication:
- **"Ko te kai a te rangatira, he kōrero"**
  - *The food of chiefs is conversation*
  - Use for: persuasive writing, media analysis, discussion

### For Storytelling/Narrative:
- **"Tūwhitia te hopo, kia māia"**
  - *Feel the fear and be brave anyway*
  - Use for: creative writing, character development

---

## ✅ QUICK CONVERSION PROCESS

### For Existing Handouts:
1. **Check current structure** - Does it use `main-container` pattern?
2. **If NO** - Needs conversion:
   - Copy template structure
   - Move content into `content-area`
   - Add appropriate whakataukī
   - Update related resources
3. **If YES** - Just verify cultural opening is present

### Creating New Handouts:
1. Copy `standard-handout-template.html`
2. Replace all `{{VARIABLES}}` with actual content
3. Add your educational content in the content area
4. Choose appropriate whakataukī from guide above
5. Test print formatting

---

## 🚨 COMMON ISSUES TO AVOID

### ❌ Broken Patterns:
- `<body class="bg-gray-100 flex flex-col items-center">` without container
- Missing sidebar structure
- No cultural opening
- Inconsistent navigation

### ✅ Correct Pattern:
- Always use `main-container` wrapper
- Include `left-sidebar` for resources
- Start content with cultural opening
- Follow standard navigation structure

---

## 🛠️ MAINTENANCE

### When Adding New Handouts:
1. Use the template system
2. Ensure cultural appropriateness of whakataukī
3. Test print functionality
4. Verify responsive design

### When Updating Existing:
1. Check if it follows template structure
2. Fix any layout inconsistencies
3. Add missing cultural elements
4. Update related resources links

---

## 📊 CURRENT STATUS

**Need Template Conversion:**
- elements-of-art-handout.html
- probability-handout.html  
- design-thinking-process-handout.html
- writers-toolkit-revision-handout.html
- (And others without main-container structure)

**Already Using Good Structure:**
- bar-graph-handout.html ✅
- authors-purpose-handout.html ✅
- environmental-literacy-framework.html ✅

---

*Kaitiaki Aronui V4.0 - Ensuring consistent, culturally-rich educational resources*
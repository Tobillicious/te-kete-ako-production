# 📚 TE KETE AKO TEMPLATE SYSTEM GUIDE

## 🎯 OVERVIEW
Complete template system for creating consistent, culturally-integrated educational resources with print optimization and beautiful styling.

---

## 🌟 AVAILABLE TEMPLATES

### 1. 📄 ULTIMATE-HANDOUT-TEMPLATE.html
**Purpose:** Student worksheets, activity sheets, assessment materials
**Key Features:**
- Print-first design for A4 double-sided printing
- Student workspace areas
- Visual puzzles and interactive elements
- Chart containers for graphs/data
- Cultural opening with whakataukī

### 2. 📖 ULTIMATE-LESSON-TEMPLATE.html
**Purpose:** Teacher lesson plans (60-75 minutes)
**Key Features:**
- Activity blocks with timing
- Differentiation strategies
- Assessment opportunities
- Cultural protocols
- Teacher reflection space

### 3. 📚 ULTIMATE-UNIT-TEMPLATE.html
**Purpose:** Multi-week teaching units (6-8 weeks)
**Key Features:**
- Unit overview with big question
- Weekly lesson structure
- Resource organization
- Assessment strategy
- Curriculum alignment

---

## 🔧 UNIVERSAL TEMPLATE VARIABLES

### Basic Information:
- `{{TITLE}}` - Main title of the resource
- `{{SUBTITLE}}` - Supporting description
- `{{SUBJECT}}` - Subject code (math, english, science, etc.)
- `{{SUBJECT_NAME}}` - Full subject name
- `{{YEAR_LEVEL}}` - Target year level

### Cultural Integration:
- `{{WHAKATAUKI_MAORI}}` - Te reo Māori proverb
- `{{WHAKATAUKI_ENGLISH}}` - English translation
- `{{WHAKATAUKI_CONNECTION}}` - Educational connection

### Navigation:
- `{{RELATED_RESOURCES}}` - Sidebar resource links
- `{{RELATED_LESSONS}}` - Related lesson links (lesson template)

---

## 📄 HANDOUT TEMPLATE VARIABLES

### Content Structure:
- `{{HANDOUT_CONTENT}}` - Main educational content
- `{{LEARNING_OBJECTIVES}}` - Bullet list of objectives
- `{{OBJECTIVES_TITLE}}` - Title for objectives section

### Example Usage:
```html
<div class="learning-objectives">
    <h3>📋 {{OBJECTIVES_TITLE}}</h3>
    <ul>
        {{LEARNING_OBJECTIVES}}
    </ul>
</div>

<!-- Replace with: -->
<div class="learning-objectives">
    <h3>📋 Level 4 Achievement Objectives</h3>
    <ul>
        <li>Collect data using simple frequency tables</li>
        <li>Display data using bar graphs with appropriate scales</li>
        <li>Interpret data by reading values and comparing categories</li>
    </ul>
</div>
```

---

## 📖 LESSON TEMPLATE VARIABLES

### Lesson Structure:
- `{{LESSON_TITLE}}` - Full lesson title
- `{{LESSON_SUBTITLE}}` - Brief description
- `{{DURATION}}` - Total lesson time in minutes

### Learning Framework:
- `{{LEARNING_INTENTIONS}}` - What students will learn
- `{{SUCCESS_CRITERIA}}` - How success is measured
- `{{KEY_VOCABULARY}}` - Important terms

### Content:
- `{{LESSON_CONTENT}}` - Main lesson activities
- `{{FORMATIVE_ASSESSMENT}}` - Check for understanding
- `{{HOMEWORK_TASK}}` - Extension activities
- `{{WHANAU_CONNECTION}}` - Family involvement

### Activity Variables (for individual activities):
- `{{TIME_1}}`, `{{TIME_2}}`, etc. - Activity durations
- `{{TEACHER_INSTRUCTIONS}}` - What teacher does
- `{{STUDENT_ACTIONS}}` - What students do
- `{{SUPPORT_STRATEGY}}` - Help for struggling students
- `{{EXTENSION_STRATEGY}}` - Challenge for advanced learners
- `{{CULTURAL_CONNECTION}}` - Cultural relevance

---

## 📚 UNIT TEMPLATE VARIABLES

### Unit Framework:
- `{{UNIT_TITLE}}` - Complete unit name
- `{{UNIT_DESCRIPTION}}` - Brief overview
- `{{DURATION}}` - Number of weeks
- `{{BIG_QUESTION}}` - Essential understanding

### Structure:
- `{{UNIT_CONTENT}}` - Weekly lesson breakdown
- `{{LEARNING_OUTCOMES}}` - Major learning goals
- `{{CULTURAL_CONTEXT}}` - Te Ao Māori integration

### Weekly Structure (repeat for each week):
- `{{WEEK_NUMBER}}` - Week number
- `{{WEEK_THEME}}` - Weekly focus
- `{{LESSON_TITLE_1}}`, `{{LESSON_TITLE_2}}`, etc. - Individual lessons
- `{{LESSON_DURATION_1}}`, etc. - Lesson timings
- `{{LESSON_LINK_1}}`, etc. - Links to lesson plans

### Resources:
- `{{HANDOUTS_LIST}}` - Required handouts
- `{{MATERIALS_LIST}}` - Additional resources

### Assessment:
- `{{FORMATIVE_ASSESSMENT}}` - Ongoing assessment
- `{{SUMMATIVE_ASSESSMENT}}` - Final assessment
- `{{FORMATIVE_CRITERIA}}` - What to look for
- `{{SUMMATIVE_CRITERIA}}` - Final criteria

### Curriculum:
- `{{LEARNING_AREA}}` - NZ Curriculum learning area
- `{{ACHIEVEMENT_OBJECTIVES}}` - Specific AOs
- `{{KEY_COMPETENCIES}}` - Relevant competencies
- `{{VALUES}}` - NZ Curriculum values

---

## 📋 WHAKATAUKĪ SELECTION GUIDE

### Mathematics/Pāngarau:
- "Ehara taku toa i te toa takitahi, engari he toa takitini"
  - *Success is not the work of one, but the work of many*
  - Connection: Data analysis requires collective observations

### English/Reo Pākehā:
- "Ko te kai a te rangatira, he kōrero"
  - *The food of chiefs is conversation*
  - Connection: Language and communication skills

### Science/Pūtaiao:
- "Ka mua, ka muri"
  - *Walking backwards into the future*
  - Connection: Learning from past knowledge to understand new concepts

### Social Studies/Tikanga-ā-Iwi:
- "He aha te mea nui o te ao? He tangata, he tangata, he tangata"
  - *What is the most important thing in the world? It is people, it is people, it is people*
  - Connection: Understanding human societies and relationships

### Arts/Ngā Toi:
- "Toi te kupu, toi te mana, toi te whenua"
  - *Artistic expression gives dignity to language, to people, and to land*
  - Connection: Creative expression and cultural identity

---

## 🎨 STYLING COMPONENTS

### Visual Elements Available:
```html
<!-- Learning objectives -->
<div class="learning-objectives">
    <h3>📋 Title</h3>
    <ul><li>Content</li></ul>
</div>

<!-- Visual puzzles -->
<div class="visual-puzzle">
    <h3>🧩 Challenge Title</h3>
    <p>Instructions</p>
</div>

<!-- Interactive elements -->
<div class="interactive-element">
    <h4>✏️ Activity Title</h4>
    <p>Description</p>
</div>

<!-- Student workspaces -->
<div class="student-workspace"></div>

<!-- Question blocks -->
<div class="question-block">
    <strong>Question:</strong> Content
</div>

<!-- Answer spaces -->
<div class="answer-space"></div>

<!-- Chart containers -->
<div class="chart-container">
    <canvas id="chartId"></canvas>
</div>

<!-- Grid layouts -->
<div class="grid-2">
    <div>Column 1</div>
    <div>Column 2</div>
</div>
```

---

## 🖨️ PRINT OPTIMIZATION

### Automatic Print Features:
- A4 page size with proper margins
- Typography scaled for readability
- Headers/footers/sidebars hidden
- Student workspace areas clearly marked
- Page break avoidance for sections
- Chart containers sized for A4

### Print-Specific Styling:
- Colors converted to print-friendly versions
- Font sizes optimized (11pt body, larger headings)
- Margins set for double-sided binding (15mm/12mm)
- Visual elements get clear borders

---

## 🚀 QUICK START WORKFLOW

### For Handouts:
1. Copy `ULTIMATE-HANDOUT-TEMPLATE.html`
2. Replace `{{HANDOUT_TITLE}}` and `{{HANDOUT_SUBTITLE}}`
3. Set `{{SUBJECT}}` and `{{SUBJECT_NAME}}`
4. Choose appropriate whakataukī
5. Replace `{{HANDOUT_CONTENT}}` with your material
6. Update sidebar `{{RELATED_RESOURCES}}`
7. Test print preview

### For Lessons:
1. Copy `ULTIMATE-LESSON-TEMPLATE.html`
2. Set lesson title, subtitle, and duration
3. Fill in learning intentions and success criteria
4. Replace `{{LESSON_CONTENT}}` with activity blocks
5. Include assessment and homework sections
6. Add reflection space for post-lesson notes

### For Units:
1. Copy `ULTIMATE-UNIT-TEMPLATE.html`
2. Set unit title, description, and duration
3. Create big question and learning outcomes
4. Build weekly structure with lesson cards
5. List all resources and materials
6. Define assessment strategy
7. Align with NZ Curriculum

---

## 🔍 QUALITY CHECKLIST

### Before Publishing:
- [ ] All template variables replaced
- [ ] Whakataukī appropriate and connected
- [ ] Print preview looks correct
- [ ] Navigation links work
- [ ] Cultural content respectful and accurate
- [ ] Content meets curriculum objectives
- [ ] Spelling and grammar checked
- [ ] Accessibility considered
- [ ] Student workspace adequate
- [ ] Save functionality works

---

## 🌿 CULTURAL CONSIDERATIONS

### Best Practices:
- Always include relevant whakataukī
- Ensure cultural connections are authentic
- Respect tikanga Māori in all content
- Include diverse perspectives
- Use inclusive language
- Honor mātauranga Māori alongside western knowledge
- Consider local iwi/hapū connections where appropriate

---

## 📞 SUPPORT

### Template Issues:
- Check variable syntax: `{{VARIABLE_NAME}}`
- Ensure CSS paths are correct: `../css/main.css`
- Verify script paths: `../js/filename.js`
- Test print functionality
- Validate HTML structure

### Content Support:
- Review NZ Curriculum documents
- Consult cultural advisors for Māori content
- Use inclusive design principles
- Follow accessibility guidelines
- Test with target audience

---

*"Whaowhia te kete mātauranga" - Fill the basket of knowledge*

**Te Kete Ako Template System | October 2025**
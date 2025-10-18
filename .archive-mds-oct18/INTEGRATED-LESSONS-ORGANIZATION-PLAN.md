# 🎯 INTEGRATED-LESSONS ORGANIZATION PLAN
## Quick Win: 380+ Lessons Already Categorized by Subject!

**Discovery:** `/public/integrated-lessons/` contains 380+ lessons organized by subject  
**Opportunity:** Create unit framework for pre-categorized content  
**Impact:** Organize 380 files (~7% of total) quickly

---

## 📊 INTEGRATED-LESSONS BREAKDOWN

### **Mathematics (108 lessons)**
- Already in `/public/integrated-lessons/mathematics/`
- Includes: algebra lessons, statistics, geometry, navigation math
- **Action:** Group into 8-10 mathematics units

### **Science (122 lessons)**  
- Already in `/public/integrated-lessons/science/`
- Includes: ecology, physics, genetics, climate, AI ethics
- **Action:** Group into 10-12 science units

### **English (40 lessons)**
- Already in `/public/integrated-lessons/english/`
- Includes: writing, poetry, media literacy, digital storytelling
- **Action:** Group into 4-5 English units

### **Te Reo Māori (86 lessons)**
- Already in `/public/integrated-lessons/te-reo-maori/`
- Language learning content
- **Action:** Group into 6-8 language units

### **Social Studies (20 lessons)**
- Already in `/public/integrated-lessons/social studies/`
- Includes: Walker lessons, Unit 2 lessons, critical thinking
- **Action:** Group into 2-3 social studies units

### **Technology (6 lessons)**
- Already in `/public/integrated-lessons/technology/`
- Digital tech content
- **Action:** Group into 1 technology unit

**TOTAL: 382 lessons ready to organize!**

---

## 🚀 SYSTEMATIC APPROACH

### **Strategy: Group by Unit Numbers**

Many files already named with unit patterns:
- `unit-1-lesson-1.html`, `unit-1-lesson-2.html` → Unit 1
- `unit-2-lesson-1.html`, `unit-2-lesson-2.html` → Unit 2
- `unit-3-lesson-1.html` → Unit 3
- etc.

### **Step 1: Extract Unit Groupings**
```bash
# Find all unit-numbered files:
grep -l "unit-[0-9]-lesson" public/integrated-lessons/*/*.html

# Group by unit number:
# Unit 1 lessons → Mathematics Unit 1
# Unit 2 lessons → English Unit 2
# etc.
```

### **Step 2: Create Unit Index Pages**
For each subject's unit groupings:
```
/public/units/mathematics/unit-1/index.html
/public/units/mathematics/unit-2/index.html
/public/units/english/unit-1/index.html
etc.
```

### **Step 3: Link Lessons**
Each unit index page lists its lessons:
- Unit overview
- Lesson 1, 2, 3, etc. (already exist!)
- Link to actual lesson files in integrated-lessons/

---

## 📋 EXAMPLE: Mathematics Organization

### **Mathematics Has 108 Lessons**

**Potential Units:**
1. **Algebra Foundations** - Pattern lessons, variable lessons, equation lessons
2. **Statistics & Probability** - Statistical investigation, sports data, probability
3. **Geometry & Patterns** - Tukutuku, kōwhaiwhai, symmetry
4. **Navigation Mathematics** - Traditional wayfinding, GPS, coordinates
5. **Applied Mathematics** - Real-world problems, modeling
6. **Number Systems** - Traditional counting, operations
7. **Measurement** - Cultural contexts, practical applications
8. **Mathematical Thinking** - Problem-solving, reasoning

**Each unit:** 10-15 lessons from the 108 available

---

## 🎯 QUICK WINS THIS WEEK

### **Target: Create 10 Unit Index Pages**

**From Mathematics (108 lessons):**
1. Create "Algebra Foundations" unit index
2. Create "Statistics" unit index
3. Create "Geometry & Patterns" unit index

**From Science (122 lessons):**
4. Create "Ecology & Kaitiakitanga" unit index
5. Create "Physics Foundations" unit index
6. Create "Genetics & Whakapapa" unit index

**From English (40 lessons):**
7. Create "Creative Writing" unit index
8. Create "Media Literacy" unit index

**From Te Reo (86 lessons):**
9. Create "Te Reo Foundations" unit index

**From Social Studies (20 lessons):**
10. Create "NZ History" unit index

**Result:** 10 new units = 150+ lessons organized = +7% progress (to 10.5% total)

---

## 📝 UNIT INDEX PAGE TEMPLATE

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mathematics: Algebra Foundations | Te Kete Ako</title>
    <meta name="description" content="Algebra foundations through Māori patterns">
    
    <!-- Canonical CSS -->
    <link rel="stylesheet" href="/css/te-kete-unified-design-system.css">
    <link rel="stylesheet" href="/css/component-library.css">
</head>
<body>
    <!-- Navigation -->
    <script>
        fetch('/components/navigation-standard.html')
            .then(r => r.text())
            .then(html => {
                const div = document.createElement('div');
                div.innerHTML = html;
                document.body.insertBefore(div.firstElementChild, document.body.firstChild);
            });
    </script>
    
    <main class="container">
        <h1>Mathematics: Algebra Foundations</h1>
        <p>Exploring algebraic thinking through traditional Māori patterns and games</p>
        
        <section class="lessons">
            <h2>Unit Lessons</h2>
            <div class="lesson-grid">
                <a href="/integrated-lessons/mathematics/lesson-1-patterns-and-sequences.html" class="lesson-card">
                    <h3>Lesson 1: Patterns and Sequences</h3>
                    <p>Recognize patterns in Māori games</p>
                </a>
                <!-- More lessons... -->
            </div>
        </section>
    </main>
</body>
</html>
```

---

## 📊 EXPECTED PROGRESS

### **Current State:**
- Organized: 200 files (3.5%)
- Remaining: 5,594 files

### **After Integrated-Lessons Organization:**
- Create: 10 new unit index pages
- Link: 150+ existing lessons
- Organized: 350 files (6%)
- Remaining: 5,444 files

### **Week 2 Goal:**
- Create: 20 total unit index pages
- Link: 300+ lessons
- Organized: 500 files (8.6%)

### **Month 1 Goal:**
- Create: 40 unit index pages
- Link: 600+ lessons + handouts
- Organized: 1,000 files (17%)

---

## ✅ WHY THIS WORKS

**Advantages:**
- ✅ Lessons already exist (no content creation)
- ✅ Already categorized by subject
- ✅ Professional quality maintained
- ✅ Just need index pages + links
- ✅ Can do 10 units per day!

**Impact:**
- Teachers find 380+ lessons organized by subject
- Clear unit structure emerges
- Measurable progress every day
- Quality maintained throughout

---

## 🚀 IMMEDIATE ACTION

**I can start creating unit index pages now!**

Which subject should I start with?
1. **Mathematics** (108 lessons) - Most content
2. **Science** (122 lessons) - Most content
3. **English** (40 lessons) - Manageable size
4. **Te Reo Māori** (86 lessons) - High cultural value

**Pick one and I'll create the first unit index page!** 🎯


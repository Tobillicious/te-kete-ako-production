# 🧑‍🏫 TEACHER-READY SPRINT PLAN
**Goal:** Make site usable for non-tech-savvy teachers by tomorrow morning  
**Time:** 2 hours tonight  
**Focus:** Practical, user-facing improvements using GraphRAG intelligence

---

## 🎯 **THE TEACHER USER STORY**

**Aroha, Year 9 Science Teacher, Tomorrow 7:45am:**
- Needs Y9 Ecology lesson for Period 2 (9:00am)
- Has 15 minutes before class
- Using phone in staffroom
- Not tech-savvy

**Can she succeed?** Let's make sure YES.

---

## ✅ **TASK 1: SURFACE GOLD RESOURCES (45 mins)**

### **What GraphRAG Knows:**
- 23 lessons rated Q90+ (Gold Standard)
- Y9 Ecology unit exists (Q95!)
- Y8 Digital Kaitiakitanga (Q90, complete 18-lesson unit!)
- Y7 Algebra (Q90, 5 lessons)

### **What Teachers See:**
- Generic homepage
- No "best resources" highlighted
- Have to search/browse randomly

### **The Fix:**
Add to `public/index.html` after hero section:

```html
<section class="featured-gold-resources" style="max-width: 1200px; margin: 3rem auto; padding: 0 2rem;">
  <div style="text-align: center; margin-bottom: 2rem;">
    <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 0.5rem 1.5rem; border-radius: 20px; font-weight: 700; display: inline-block; margin-bottom: 1rem;">
      ⭐ GOLD STANDARD RESOURCES
    </span>
    <h2 style="font-size: 2.5rem; color: #1a4d2e; margin-bottom: 0.5rem;">
      Featured This Week
    </h2>
    <p style="color: #666; font-size: 1.1rem;">
      Our highest-rated lessons (Q90+) - tested, trusted, ready to use
    </p>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
    <!-- Y9 Ecology -->
    <a href="/units/y9-science-ecology/" style="background: white; border-radius: 16px; padding: 2rem; text-decoration: none; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 4px solid #10b981; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform=''">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <span style="background: #10b981; color: white; padding: 0.35rem 0.85rem; border-radius: 20px; font-size: 0.75rem; font-weight: 800;">⭐ Q95</span>
        <span style="color: #059669; font-weight: 600;">Year 9</span>
      </div>
      <h3 style="color: #1a4d2e; font-size: 1.5rem; margin-bottom: 0.75rem;">🌿 Ecology Unit</h3>
      <p style="color: #64748b; margin-bottom: 1rem;">Complete ecology unit with 6 lessons, field activities, and cultural connections to kaitiakitanga</p>
      <div style="background: #f0fdf4; padding: 0.75rem; border-radius: 8px;">
        <strong style="color: #065f46;">Perfect for:</strong> Y9 Science teachers needing full ecology coverage
      </div>
    </a>

    <!-- Y8 Digital Kaitiakitanga -->
    <a href="/units/y8-digital-kaitiakitanga/" style="background: white; border-radius: 16px; padding: 2rem; text-decoration: none; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 4px solid #3b82f6;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <span style="background: #3b82f6; color: white; padding: 0.35rem 0.85rem; border-radius: 20px; font-size: 0.75rem; font-weight: 800;">⭐ Q90</span>
        <span style="color: #2563eb; font-weight: 600;">Year 8</span>
      </div>
      <h3 style="color: #1a4d2e; font-size: 1.5rem; margin-bottom: 0.75rem;">💻 Digital Kaitiakitanga</h3>
      <p style="color: #64748b; margin-bottom: 1rem;">Complete 18-lesson unit covering digital citizenship, online safety, and kaitiakitanga principles</p>
      <div style="background: #eff6ff; padding: 0.75rem; border-radius: 8px;">
        <strong style="color: #1e40af;">Perfect for:</strong> Full term Digital Tech program
      </div>
    </a>

    <!-- Y7 Algebra -->
    <a href="/units/y7-maths-algebra/" style="background: white; border-radius: 16px; padding: 2rem; text-decoration: none; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-top: 4px solid #f59e0b;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <span style="background: #f59e0b; color: white; padding: 0.35rem 0.85rem; border-radius: 20px; font-size: 0.75rem; font-weight: 800;">⭐ Q90</span>
        <span style="color: #d97706; font-weight: 600;">Year 7</span>
      </div>
      <h3 style="color: #1a4d2e; font-size: 1.5rem; margin-bottom: 0.75rem;">🔢 Algebra Foundations</h3>
      <p style="color: #64748b; margin-bottom: 1rem;">5-lesson introduction to algebra through patterns, Māori games, and problem-solving</p>
      <div style="background: #fffbeb; padding: 0.75rem; border-radius: 8px;">
        <strong style="color: #92400e;">Perfect for:</strong> Y7 Maths teachers starting algebra
      </div>
    </a>
  </div>

  <div style="text-align: center; margin-top: 2rem;">
    <a href="/gold-collection.html" style="display: inline-block; background: #1a4d2e; color: white; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 700;">
      View All 629 Gold Resources →
    </a>
  </div>
</section>
```

**Time:** 45 minutes  
**Impact:** 🚀 Teachers see best content immediately

---

## ✅ **TASK 2: ADD YEAR/SUBJECT FILTERS TO LESSONS PAGE (60 mins)**

### **What GraphRAG Knows:**
```sql
Year 7: 7 lessons
Year 8: 16 lessons  
Year 9: 6 lessons
Year 10-13: 10+ lessons

English: 11 lessons (now 81.8% connected!)
Science: 12 lessons
Mathematics: 14 lessons
Digital Tech: 28 lessons
```

### **The Fix:**
Add filter dropdowns to `public/lessons.html`:

```html
<div class="filters-section" style="max-width: 1200px; margin: 2rem auto; padding: 0 2rem;">
  <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
    <h3 style="margin-bottom: 1rem;">🔍 Find Lessons</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
      
      <div>
        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #1a4d2e;">Year Level:</label>
        <select id="year-filter" onchange="filterLessons()" style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 1rem;">
          <option value="">All Years</option>
          <option value="Year 7">Year 7</option>
          <option value="Year 8">Year 8</option>
          <option value="Year 9">Year 9</option>
          <option value="Year 10">Year 10</option>
          <option value="Year 11">Year 11</option>
          <option value="Year 12">Year 12</option>
          <option value="Year 13">Year 13</option>
        </select>
      </div>

      <div>
        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #1a4d2e;">Subject:</label>
        <select id="subject-filter" onchange="filterLessons()" style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 1rem;">
          <option value="">All Subjects</option>
          <option value="English">English</option>
          <option value="Mathematics">Mathematics</option>
          <option value="Science">Science</option>
          <option value="Social Studies">Social Studies</option>
          <option value="Digital Technologies">Digital Technologies</option>
          <option value="Health & PE">Health & PE</option>
          <option value="Te Ao Māori">Te Ao Māori</option>
        </select>
      </div>

      <div>
        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #1a4d2e;">Quality:</label>
        <select id="quality-filter" onchange="filterLessons()" style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 1rem;">
          <option value="">All Quality</option>
          <option value="90">⭐ Gold (Q90+)</option>
          <option value="85">✨ Excellent (Q85+)</option>
          <option value="80">👍 Good (Q80+)</option>
        </select>
      </div>

    </div>
    <div style="margin-top: 1rem;">
      <button onclick="clearFilters()" style="background: #64748b; color: white; padding: 0.5rem 1rem; border: none; border-radius: 6px; cursor: pointer;">
        Clear Filters
      </button>
    </div>
  </div>
</div>

<script>
// Filter lessons based on GraphRAG metadata
async function filterLessons() {
  const year = document.getElementById('year-filter').value;
  const subject = document.getElementById('subject-filter').value;
  const quality = document.getElementById('quality-filter').value;

  // Query GraphRAG with filters
  const supabase = window.supabase.createClient(
    'https://nlgldaqtubrlcqddppbq.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY5ODgxMTksImV4cCI6MjA1MjU2NDExOX0.gN5RGe7kGmxj4-yI1xnDuCuKUPFDh4f-8CQqQdqrGq0'
  );

  let query = supabase
    .from('graphrag_resources')
    .select('*')
    .eq('resource_type', 'Lesson')
    .like('file_path', 'public/%')
    .order('quality_score', { ascending: false });

  if (year) query = query.ilike('year_level', `%${year}%`);
  if (subject) query = query.eq('subject', subject);
  if (quality) query = query.gte('quality_score', parseInt(quality));

  const { data, error } = await query.limit(100);

  if (error) {
    console.error('Filter error:', error);
    return;
  }

  // Render filtered lessons
  renderLessons(data);
}

function renderLessons(lessons) {
  const container = document.getElementById('lessons-container');
  if (!container) return;

  container.innerHTML = lessons.map(lesson => `
    <a href="${lesson.file_path.replace('public/', '/')}" class="lesson-card">
      <div class="lesson-header">
        ${lesson.quality_score >= 90 ? '<span class="badge gold">⭐ Q' + lesson.quality_score + '</span>' : ''}
        ${lesson.quality_score >= 85 && lesson.quality_score < 90 ? '<span class="badge excellent">✨ Q' + lesson.quality_score + '</span>' : ''}
        <span class="badge year">${lesson.year_level || 'All Years'}</span>
      </div>
      <h3>${lesson.title}</h3>
      <p class="subject">${lesson.subject}</p>
      ${lesson.cultural_context ? '<div class="cultural-badge">🌿 Cultural Integration</div>' : ''}
    </a>
  `).join('');
}

function clearFilters() {
  document.getElementById('year-filter').value = '';
  document.getElementById('subject-filter').value = '';
  document.getElementById('quality-filter').value = '';
  filterLessons();
}

// Load all lessons on page load
document.addEventListener('DOMContentLoaded', filterLessons);
</script>
```

**Time:** 60 minutes  
**Impact:** 🎯 **HUGE** - "I teach Year 9 Science" → instant relevant results

---

## ✅ **TASK 3: QUICK WINS (15 mins)**

### **3a: Add Quality Badges to Resource Cards**
Wherever lessons show, add:
```html
<span class="quality-badge q95">⭐ Q95 - Gold Standard</span>
```

### **3b: Fix Any Broken "Assign" or "Download" Buttons**
Quick test: Do PDF download buttons work?

### **3c: Mobile Quick-Test**
Open on phone, verify:
- Can tap navigation
- Can read lesson titles
- Buttons are big enough

---

## 📊 **SUCCESS METRICS (Tomorrow Morning)**

✅ **Teacher can find Y9 Ecology in < 30 seconds**  
✅ **Teacher can filter by "Year 8" + "Science"**  
✅ **Teacher knows Q95 means "tried and trusted"**  
✅ **Teacher can do all this on their phone**

---

## 🚀 **EXECUTION ORDER:**

**Tonight (2 hours):**
1. Task 1: Add Gold Resources section to homepage (45 mins)
2. Task 2: Add filters to lessons.html (60 mins)
3. Task 3: Quick wins (15 mins)

**Tomorrow Morning:**
Test with real teacher scenario:
- "Find Y9 Science lesson" → Should see Ecology immediately
- "Filter Year 8" → Should see Digital Kaitiakitanga
- "Look for gold resources" → Should see Q90+ badges

---

**PRIORITY:** User experience > Perfect code  
**GOAL:** Teachers succeed tomorrow morning  
**METHOD:** Leverage GraphRAG intelligence in user-facing UI

🧑‍🏫 **LET'S MAKE THIS WORK FOR AROHA!** 🎯


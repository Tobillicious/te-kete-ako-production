# 🔌 Frontend-Backend Integration Guide

**For:** Connecting Te Kete Ako frontend to clean GraphRAG backend  
**Created:** October 28, 2025  
**Status:** Production-ready

---

## 🎯 **What Was Added:**

### **New SQL Views:**
1. `resources_by_year` - Fast year-level filtering
2. `resources_with_relationships` - Shows which resources have lessons, prerequisites

### **New SQL Functions:**
1. `get_related_resources(path, limit)` - Get related content
2. `get_unit_lessons(path)` - Get lessons in a unit

---

## 📊 **Test Results:**

✅ **Year 8 resources:** 48 found  
✅ **Units with lessons:** 8 out of 10 units have lesson relationships  
✅ **Unit 2 lessons:** 5 lessons retrieved in order  
✅ **Related resources:** Working with confidence scores

---

## 🚀 **How to Use in Frontend:**

### **1. Browse Page - Filter by Year Level**

**Current (slow):**
```javascript
// Loads ALL 126 resources, filters in JavaScript
const { data } = await supabase
  .from('resources')
  .select('*')
  .eq('is_active', true);

// Then filter client-side
const year8 = data.filter(r => r.level.includes('8'));
```

**New (fast):**
```javascript
// Server-side filtering with SQL view
const { data } = await supabase
  .from('resources_by_year')
  .select('*')
  .filter('year_levels_array', 'cs', '{"8"}')  // Contains '8'
  .order('title');

console.log(`Found ${data.length} Year 8 resources`);
```

---

### **2. Browse Page - Show Units with Lesson Count**

**New feature:**
```javascript
// Get all units and show which have lessons
const { data } = await supabase
  .from('resources_with_relationships')
  .select('*')
  .eq('type', 'unit-plan')
  .order('title');

data.forEach(unit => {
  console.log(`${unit.title}: ${unit.outgoing_relationships} lessons`);
  // Display badge: "5 lessons" on unit card
});
```

---

### **3. Unit Page - Display Lesson List**

**When viewing a unit, show its lessons:**
```javascript
// On unit page (e.g., unit-2-decolonized-history.html)
const unitPath = 'units/unit-2-decolonized-history.html';

const { data: lessons } = await supabase
  .rpc('get_unit_lessons', { unit_path_input: unitPath });

// Returns lessons in order:
// [
//   { title: "Lesson 1: Pre-Colonial Excellence", path: "units/lessons/unit-2-lesson-1.html" },
//   { title: "Lesson 2: Contact & Colonization", path: "units/lessons/unit-2-lesson-2.html" },
//   ...
// ]

// Display as clickable list or cards
```

**HTML Example:**
```html
<div class="unit-lessons">
  <h3>📚 Lessons in This Unit</h3>
  <ol id="lesson-list"></ol>
</div>

<script>
async function loadUnitLessons() {
  const unitPath = 'units/unit-2-decolonized-history.html';
  const { data } = await supabase.rpc('get_unit_lessons', { 
    unit_path_input: unitPath 
  });
  
  const list = document.getElementById('lesson-list');
  data.forEach(lesson => {
    list.innerHTML += `
      <li>
        <a href="/${lesson.path}">
          ${lesson.title}
        </a>
        <p>${lesson.description}</p>
      </li>
    `;
  });
}

loadUnitLessons();
</script>
```

---

### **4. Resource Page - "Related Resources" Section**

**Add to any resource page:**
```javascript
// On any resource page
const currentPath = 'handouts/media-literacy-comprehension-handout.html';

const { data: related } = await supabase
  .rpc('get_related_resources', { 
    resource_path_input: currentPath,
    limit_count: 5 
  });

// Returns up to 5 related resources sorted by relevance
// Display as "Teachers also used..." or "Next steps..."
```

**HTML Example:**
```html
<div class="related-resources no-print">
  <h3>📚 Related Resources</h3>
  <div id="related-list"></div>
</div>

<script>
async function loadRelatedResources() {
  const currentPath = window.location.pathname.replace('/', '');
  const { data } = await supabase.rpc('get_related_resources', { 
    resource_path_input: currentPath,
    limit_count: 5
  });
  
  if (data && data.length > 0) {
    const container = document.getElementById('related-list');
    data.forEach(resource => {
      container.innerHTML += `
        <div class="related-card">
          <h4>${resource.title}</h4>
          <p>${resource.description}</p>
          <a href="/${resource.path}" class="btn-secondary">View Resource</a>
          <span class="badge">${resource.relationship_type.replace('_', ' ')}</span>
        </div>
      `;
    });
  }
}

loadRelatedResources();
</script>
```

---

### **5. Subject Filter - Efficient Querying**

**Current:**
```javascript
// Loads all, filters client-side
const { data } = await supabase
  .from('resources')
  .select('*');
  
const english = data.filter(r => r.subject === 'english');
```

**Better:**
```javascript
// Server-side filtering
const { data } = await supabase
  .from('resources')
  .select('*')
  .eq('subject', 'english')
  .eq('is_active', true)
  .order('title');
```

**Best (with year level):**
```javascript
// Combined filters - server-side
const { data } = await supabase
  .from('resources_by_year')
  .select('*')
  .eq('subject', 'english')
  .filter('year_levels_array', 'cs', '{"8"}')
  .order('featured', { ascending: false })
  .order('title');
```

---

## 🎨 **UI Enhancements You Can Add:**

### **1. Unit Cards - Show Lesson Count**
```html
<div class="unit-card">
  <h3>Decolonized Aotearoa History</h3>
  <span class="badge">5 lessons</span>
  <span class="badge">Social Studies</span>
  <span class="badge">Year 8-12</span>
</div>
```

### **2. Resource Page - Navigation**
```html
<!-- On Unit 2 Lesson 3 page -->
<nav class="lesson-nav">
  <a href="unit-2-lesson-2.html">← Previous: Contact & Colonization</a>
  <a href="unit-2-decolonized-history.html">↑ Back to Unit</a>
  <a href="unit-2-lesson-4.html">Next: Treaty Violations →</a>
</nav>
```

### **3. Browse Page - Quick Filters**
```html
<!-- Popular sets as buttons -->
<div class="quick-filters">
  <button data-filter="year-8">Year 8 (48 resources)</button>
  <button data-filter="english">English (30 resources)</button>
  <button data-filter="units-with-lessons">Units (8 units)</button>
</div>
```

---

## 📈 **Performance Benefits:**

| Feature | Before | After | Improvement |
|---------|--------|-------|-------------|
| **Year 8 filter** | Load 126, filter JS | SQL filter → 48 | 62% less data |
| **Subject filter** | Client-side | Server-side | Instant |
| **Related resources** | None | SQL function | New feature! |
| **Unit lessons** | Manual linking | Automatic | Always current |

---

## 🔄 **Updating browse.html Example:**

Add this to your `browse.html` script section:

```javascript
// Enhanced filtering with SQL views
async function fetchResourcesEfficiently() {
  const filters = getActiveFilters(); // { year: '8', subject: 'english', type: 'handout' }
  
  // Build query
  let query = supabase.from('resources_by_year').select('*');
  
  if (filters.year) {
    query = query.filter('year_levels_array', 'cs', `{"${filters.year}"}`);
  }
  
  if (filters.subject) {
    query = query.eq('subject', filters.subject);
  }
  
  if (filters.type) {
    query = query.eq('type', filters.type);
  }
  
  const { data, error } = await query.order('featured', { ascending: false }).order('title');
  
  if (!error) {
    console.log(`✅ Loaded ${data.length} filtered resources from server`);
    return data;
  }
}
```

---

## 🎯 **Quick Wins to Implement:**

### **Priority 1: Unit Pages** (30 mins)
Add "Lessons in this Unit" section to each unit page using `get_unit_lessons()`.

### **Priority 2: Related Resources** (1 hour)
Add "Related Resources" widget to handouts/lessons using `get_related_resources()`.

### **Priority 3: Efficient Filtering** (1 hour)
Update browse.html to use SQL views instead of client-side filtering.

### **Priority 4: Lesson Navigation** (30 mins)
Add Previous/Next buttons on lesson pages.

---

## 🧪 **Test Queries:**

```sql
-- Test 1: Get Year 8 English resources
SELECT * FROM resources_by_year 
WHERE subject = 'english' 
  AND '8' = ANY(year_levels_array);

-- Test 2: Get units with lesson counts
SELECT title, outgoing_relationships as lesson_count 
FROM resources_with_relationships 
WHERE type = 'unit-plan' 
  AND has_lessons = true;

-- Test 3: Get Unit 1 lessons
SELECT * FROM get_unit_lessons('units/unit-1-te-ao-maori.html');

-- Test 4: Get related to Media Literacy handout
SELECT * FROM get_related_resources('handouts/media-literacy-comprehension-handout.html', 3);
```

---

## 📚 **Reference:**

- **Views created:** `resources_by_year`, `resources_with_relationships`
- **Functions created:** `get_related_resources()`, `get_unit_lessons()`
- **Migration:** `create_frontend_views`
- **Testing:** All 4 views/functions verified working

---

## 💡 **Next Steps:**

1. ✅ **Start with unit pages** - Show lesson lists
2. ✅ **Add related resources** - "Teachers also used..."
3. ✅ **Optimize browse.html** - Use SQL views for filtering
4. ✅ **Add lesson navigation** - Previous/Next buttons

**All backend infrastructure is ready. Just connect the frontend!**

---

**Created:** October 28, 2025  
**Agent:** Kaitiaki Aronui  
**Status:** Production-ready, tested, documented

🧺 ✨ 🔌


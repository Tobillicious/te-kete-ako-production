# 🏫 NZ Schools Autofill System - Plan
**Goal:** Self-growing database of NZ schools with autocomplete

---

## 🎯 REQUIREMENTS

1. **Autofill Input** - NOT dropdown, users type and get suggestions
2. **Pull from Supabase** - `nz_schools` table (currently 8 schools)
3. **Auto-add New Schools** - If not found, create new entry
4. **Connect to GraphRAG** - Track schools as knowledge entities

---

## 🏗️ IMPLEMENTATION

### Step 1: Create Autocomplete Component

**HTML:**
```html
<div class="form-group">
    <input type="text" 
           id="school" 
           name="school_name" 
           placeholder=" "
           autocomplete="off"
           oninput="searchSchools(this.value)">
    <label for="school">School / Organization</label>
    <div id="school-suggestions" class="autocomplete-suggestions"></div>
    <small>Start typing to search NZ schools</small>
</div>
```

**CSS:**
```css
.autocomplete-suggestions {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border: 2px solid var(--color-forest);
    border-top: none;
    border-radius: 0 0 var(--radius-md) var(--radius-md);
    max-height: 250px;
    overflow-y: auto;
    z-index: 1000;
    display: none;
    box-shadow: var(--shadow-strong);
}

.autocomplete-suggestions.show {
    display: block;
}

.suggestion-item {
    padding: 0.75rem 1rem;
    cursor: pointer;
    transition: background 0.2s ease;
}

.suggestion-item:hover {
    background: var(--color-cultural-light);
}

.suggestion-name {
    font-weight: 600;
    color: var(--color-primary);
}

.suggestion-meta {
    font-size: 0.85rem;
    color: var(--color-text-secondary);
}

.suggestion-new {
    background: var(--color-warmth);
    border-top: 1px solid var(--color-border);
}
```

---

### Step 2: JavaScript Autocomplete Logic

```javascript
let schoolsCache = [];
let debounceTimer = null;

// Load schools into cache on page load
async function loadSchools() {
    try {
        const { data, error } = await supabase
            .from('nz_schools')
            .select('name, location, region, school_type, decile')
            .order('name');
        
        if (error) throw error;
        schoolsCache = data || [];
    } catch (error) {
        console.error('Error loading schools:', error);
    }
}

// Search schools with debounce
function searchSchools(query) {
    clearTimeout(debounceTimer);
    
    if (!query || query.length < 2) {
        hideSchoolSuggestions();
        return;
    }
    
    debounceTimer = setTimeout(() => {
        showSchoolSuggestions(query);
    }, 300);
}

// Show filtered suggestions
function showSchoolSuggestions(query) {
    const suggestionsDiv = document.getElementById('school-suggestions');
    const filtered = schoolsCache.filter(school => 
        school.name.toLowerCase().includes(query.toLowerCase())
    );
    
    if (filtered.length === 0) {
        // Show "Add new school" option
        suggestionsDiv.innerHTML = `
            <div class="suggestion-item suggestion-new" onclick="addNewSchool('${escapeHtml(query)}')">
                <div class="suggestion-name">➕ Add "${escapeHtml(query)}" as new school</div>
                <div class="suggestion-meta">This will be added to our database</div>
            </div>
        `;
    } else {
        // Show matching schools
        suggestionsDiv.innerHTML = filtered.map(school => `
            <div class="suggestion-item" onclick='selectSchool(${JSON.stringify(school)})'>
                <div class="suggestion-name">${escapeHtml(school.name)}</div>
                <div class="suggestion-meta">${school.region || 'Unknown region'} • ${school.school_type || 'School'}</div>
            </div>
        `).join('');
        
        // Add "Add new" option at bottom
        suggestionsDiv.innerHTML += `
            <div class="suggestion-item suggestion-new" onclick="addNewSchool('${escapeHtml(query)}')">
                <div class="suggestion-name">➕ Add "${escapeHtml(query)}" as new school</div>
                <div class="suggestion-meta">Not in the list? Click to add</div>
            </div>
        `;
    }
    
    suggestionsDiv.classList.add('show');
}

// Select existing school
function selectSchool(school) {
    document.getElementById('school').value = school.name;
    hideSchoolSuggestions();
}

// Add new school to database
async function addNewSchool(schoolName) {
    try {
        document.getElementById('school').value = schoolName;
        hideSchoolSuggestions();
        
        // Insert into nz_schools table
        const { data, error } = await supabase
            .from('nz_schools')
            .insert({
                name: schoolName,
                location: 'To be confirmed',
                region: null,
                school_type: null,
                decile: null
            })
            .select()
            .single();
        
        if (error) {
            console.error('Error adding school:', error);
            return;
        }
        
        // Add to cache
        schoolsCache.push(data);
        
        // Add to GraphRAG
        await addSchoolToGraphRAG(data);
        
        console.log('✅ New school added:', schoolName);
    } catch (error) {
        console.error('Error adding new school:', error);
    }
}

// Add school to GraphRAG knowledge graph
async function addSchoolToGraphRAG(school) {
    try {
        await supabase
            .from('graphrag_resources')
            .insert({
                file_path: `/schools/${school.name.toLowerCase().replace(/\s+/g, '-')}`,
                resource_type: 'school',
                title: school.name,
                metadata: {
                    location: school.location,
                    region: school.region,
                    school_type: school.school_type,
                    decile: school.decile,
                    added_by: 'user',
                    auto_created: true
                },
                subject: 'Platform Infrastructure',
                year_level: 'All',
                quality_score: 50
            });
    } catch (error) {
        console.error('Error adding to GraphRAG:', error);
    }
}

function hideSchoolSuggestions() {
    document.getElementById('school-suggestions').classList.remove('show');
}

// Hide suggestions when clicking outside
document.addEventListener('click', (e) => {
    if (!e.target.closest('.school-search-wrapper')) {
        hideSchoolSuggestions();
    }
});
```

---

### Step 3: Initialize on Page Load

```javascript
async loadUserData() {
    try {
        // Load profile...
        
        // Load schools cache for autocomplete
        await loadSchools();
        
        // Rest of code...
    } catch (error) {
        console.error('Error loading user data:', error);
    }
}
```

---

## 📊 DATABASE STRUCTURE

### Current nz_schools table:
- `id` (UUID)
- `name` (text, unique)
- `location` (text)
- `region` (text) - Auckland, Wellington, etc.
- `school_type` (text) - Intermediate, Secondary, etc.
- `authority` (text) - State, Private, etc.
- `decile` (integer 1-10)
- `roll_count` (integer)
- `website_url` (text)
- `created_at`, `updated_at`

### When User Adds New School:
```sql
INSERT INTO nz_schools (name, location, region, school_type)
VALUES ('School Name', 'To be confirmed', NULL, NULL)
```

Later, admin can enrich with proper data.

---

## 🧠 GRAPHRAG INTEGRATION

### When New School Added:
```sql
INSERT INTO graphrag_resources (
    file_path, 
    resource_type, 
    title, 
    metadata, 
    subject
) VALUES (
    '/schools/school-name',
    'school',
    'School Name',
    '{"auto_created": true, "added_by": "user"}',
    'Platform Infrastructure'
)
```

### Create Relationships:
```sql
-- Link school to users
INSERT INTO graphrag_relationships (
    source_path,
    target_path,
    relationship_type
) VALUES (
    '/profiles/user-id',
    '/schools/school-name',
    'teaches_at'
)
```

---

## ✨ USER EXPERIENCE

### Scenario 1: School Exists
```
User types: "Mang"

Suggestions appear:
┌──────────────────────────────────┐
│ Mangakōtukutuku College          │
│ Auckland • Intermediate          │
├──────────────────────────────────┤
│ Mangere College                  │
│ Auckland • Secondary             │
├──────────────────────────────────┤
│ ➕ Add "Mang" as new school      │
│ Not in the list? Click to add    │
└──────────────────────────────────┘

User clicks → Field fills → Done!
```

---

### Scenario 2: School NOT in Database
```
User types: "Taupo-nui-a-Tia College"

No matches found:
┌──────────────────────────────────┐
│ ➕ Add "Taupo-nui-a-Tia College" │
│ This will be added to our        │
│ database                         │
└──────────────────────────────────┘

User clicks:
1. Field fills with "Taupo-nui-a-Tia College"
2. Database inserts new school ✅
3. GraphRAG adds knowledge entity ✅
4. Cache updates ✅
5. Next user will see it in suggestions! ✅
```

---

## 🚀 BENEFITS

**For Users:**
- ✅ Fast typing (autofill is faster than dropdown)
- ✅ No frustration if school missing
- ✅ Consistent school names (picks from list)
- ✅ Feel empowered ("I helped build the database!")

**For Platform:**
- ✅ Self-growing school database
- ✅ Zero manual data entry
- ✅ Real NZ schools from real users
- ✅ GraphRAG learns school relationships
- ✅ Can build school-based features later

**For Admin:**
- ✅ See all schools in Supabase
- ✅ Can enrich data later (add region, decile, etc.)
- ✅ Can merge duplicates if needed
- ✅ Track which schools use the platform

---

## 🔮 FUTURE ENHANCEMENTS

**Phase 2: School Enrichment**
- Admin dashboard to approve/merge schools
- Fetch school data from Ministry of Education API
- Validate school names
- Auto-suggest correct spellings

**Phase 3: School Features**
- School licenses (one subscription, many teachers)
- School-wide analytics
- School community features
- School-specific resource collections

**Phase 4: GraphRAG Intelligence**
- "Schools using this resource"
- "Popular resources at similar schools"
- "Schools in your region"
- Network effects!

---

## ✅ READY TO IMPLEMENT

**Files to Modify:**
1. `account-settings.html` - Add autocomplete to school input
2. `js/school-autocomplete.js` - New shared component (reusable!)
3. `register-onboarding.html` - Already has this, we can reuse!

**Database:**
- ✅ `nz_schools` table exists (8 schools)
- ✅ Has all needed fields
- ✅ Ready to grow!

**GraphRAG:**
- ✅ `graphrag_resources` table ready
- ✅ Can track schools as entities
- ✅ Can create relationships

---

*Self-growing databases = SaaS magic!* 🪄


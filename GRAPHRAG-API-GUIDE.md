# 🧠 GraphRAG API Guide - Te Kete Ako

**Quick reference for using the enhanced GraphRAG system**

---

## 📊 Available Views & Functions

### **1. `browse_resources_api` (View)**

**Purpose:** Main API for browsing resources with smart metadata

**Columns:**
- `id` - Resource ID
- `title` - Resource title
- `subject` - Subject area
- `resource_type` - lesson/unit/handout
- `year_level` - Year level (7-13)
- `quality_score` - Quality rating (0-100)
- `file_path` - Path to actual resource file
- `cultural_context` - Has Māori cultural content?
- `content_preview` - First 500 chars
- `connection_count` - Number of GraphRAG relationships
- `has_prerequisites` - Has prerequisite resources?
- `is_excellence` - Part of excellence cluster?

**Example Queries:**

```typescript
// Get all Year 8 Math resources
const { data } = await supabase
  .from('browse_resources_api')
  .select('*')
  .eq('subject', 'Mathematics')
  .eq('year_level', '8')
  .order('quality_score', { ascending: false })

// Get culturally integrated lessons
const { data } = await supabase
  .from('browse_resources_api')
  .select('*')
  .eq('cultural_context', true)
  .gte('quality_score', 95)

// Get well-connected excellence resources
const { data } = await supabase
  .from('browse_resources_api')
  .select('*')
  .eq('is_excellence', true)
  .gte('connection_count', 20)
```

---

### **2. `year_8_quality_resources` (Materialized View)**

**Purpose:** Fast access to User #1's subjects (pre-filtered)

**Pre-filters:**
- Year 8 only
- Quality 90+
- Subjects: English, Mathematics, Social Studies, Te Reo Māori, Te Ao Māori
- Active only (not archived)

**Use when:** Displaying User #1's dashboard or subject-specific views

```typescript
// Get all available Y8 Maths resources
const { data } = await supabase
  .from('year_8_quality_resources')
  .select('*')
  .eq('subject', 'Mathematics')

// Refresh materialized view (after adding new resources)
await supabase.rpc('refresh_year_8_resources')
```

---

### **3. `get_related_resources()` (Function)**

**Purpose:** Smart recommendations using GraphRAG relationships

**Parameters:**
- `resource_id_input` (bigint) - Source resource ID
- `limit_count` (int, default 5) - Max recommendations

**Returns:** Related resources with relevance scores

**Relationship Priority:**
1. `prerequisite` - 1.0 (must learn first)
2. `learning_sequence` - 0.9 (natural progression)
3. `excellence_cluster` - 0.85 (high-quality related content)
4. `shared_cultural_element` - 0.8 (cultural connections)
5. `related_concept` - 0.7 (conceptually similar)

```typescript
// Get recommended next resources
const { data } = await supabase.rpc('get_related_resources', {
  resource_id_input: 12345,
  limit_count: 5
})

// Returns:
// [
//   { related_id: 12346, related_title: "...", relationship_type: "prerequisite", relevance_score: 1.0 },
//   { related_id: 12347, related_title: "...", relationship_type: "learning_sequence", relevance_score: 0.9 }
// ]
```

---

## 🎯 Common Use Cases

### **Homepage - Featured Resources**
```typescript
// Top 10 highest quality, well-connected resources
const { data } = await supabase
  .from('browse_resources_api')
  .select('*')
  .gte('quality_score', 95)
  .gte('connection_count', 15)
  .order('quality_score', { ascending: false })
  .limit(10)
```

### **Browse Page - Filtered Grid**
```typescript
// Browse with filters
const { data } = await supabase
  .from('browse_resources_api')
  .select('*')
  .eq('subject', filters.subject)
  .eq('year_level', filters.year)
  .in('resource_type', filters.types)
  .gte('quality_score', 90)
  .order('quality_score', { ascending: false })
  .range(page * 20, (page + 1) * 20 - 1)
```

### **Resource Page - Related Content**
```typescript
// Show resource + recommendations
const [resource, related] = await Promise.all([
  supabase.from('browse_resources_api').select('*').eq('id', id).single(),
  supabase.rpc('get_related_resources', { resource_id_input: id, limit_count: 3 })
])
```

### **Dashboard - Teacher's Subjects**
```typescript
// Year 8 content for specific teacher
const { data } = await supabase
  .from('year_8_quality_resources')
  .select('*')
  .in('subject', ['Mathematics', 'Social Studies', 'English'])
  .order('quality_score', { ascending: false })
```

---

## 🔍 GraphRAG Relationship Types (Available)

From 1.19M relationships in database:

- `related_concept` (828K) - Conceptually related
- `same_year_level` (63K) - Same year level
- `same_subject` (52K) - Same subject
- `prerequisite` (37K) - Required prior knowledge
- `related_content` (35K) - Related content
- `unit_contains_lesson` (13K) - Unit structure
- `excellence_cluster` (8K) - High-quality networks
- `learning_sequence` (8K) - Pedagogical progression
- `shared_cultural_element` (6.7K) - Cultural connections
- `cross_curricular` (5K) - Cross-subject links

---

## ⚡ Performance Tips

1. **Use materialized views** for frequently accessed data
2. **Limit results** with `.limit()` and `.range()`
3. **Index filters** (subject, year_level already indexed)
4. **Batch related queries** with `Promise.all()`
5. **Cache homepage data** (changes infrequently)

---

**Updated:** 2025-10-26  
**Version:** 1.0


# 🧠 GraphRAG API Documentation

**Version:** 1.0  
**Date:** October 19, 2025  
**Base URL:** `https://nlgldaqtubrlcqddppbq.supabase.co`  
**Authentication:** Anon Key (public read access)

---

## 📚 Quick Start

### **Initialize Supabase Client:**

```javascript
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY5ODgxMTksImV4cCI6MjA1MjU2NDExOX0.gN5RGe7kGmxj4-yI1xnDuCuKUPFDh4f-8CQqQdqrGq0';

const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
```

---

## 📊 Core Tables

### **1. graphrag_resources** (19,737 rows)

**Columns:**
- `file_path` (text, unique) - Resource identifier
- `title` (text) - Display name
- `resource_type` (text) - lesson, handout, game, etc.
- `subject` (text) - Science, English, Math, etc.
- `year_level` (text) - Years 7-13
- `quality_score` (int) - 0-100 rating
- `cultural_context` (bool) - Has Māori integration
- `has_te_reo` (bool) - Contains Te Reo
- `has_whakataukī` (bool) - Contains proverbs
- `content_preview` (text) - Description/excerpt
- `metadata` (jsonb) - Additional data

### **2. graphrag_relationships** (231,469 rows)

**Columns:**
- `source_path` (text) - Origin resource
- `target_path` (text) - Connected resource  
- `relationship_type` (text) - Type of connection
- `confidence` (float) - 0.0-1.0 reliability score
- `metadata` (jsonb) - Additional context

---

## 🔍 Common Queries

### **Get All Science Resources:**

```javascript
const { data, error } = await supabase
    .from('graphrag_resources')
    .select('file_path, title, quality_score, cultural_context')
    .or('subject.ilike.%science%,subject.ilike.%biology%,subject.ilike.%chemistry%')
    .order('quality_score', { ascending: false })
    .limit(50);
```

### **Get Connection Count for a Resource:**

```javascript
const resourcePath = '/public/generated-resources-alpha/handouts/biotechnology-ethics-through-māori-worldview.html';

const { data, error } = await supabase
    .from('graphrag_relationships')
    .select('id, relationship_type')
    .or(`source_path.eq.${resourcePath},target_path.eq.${resourcePath}`);

const totalConnections = data.length;
```

### **Get Related Resources:**

```javascript
const { data, error } = await supabase
    .from('graphrag_relationships')
    .select(`
        target_path,
        relationship_type,
        confidence,
        target:graphrag_resources!target_path (
            title,
            subject,
            quality_score
        )
    `)
    .eq('source_path', '/public/units/y9-science-ecology/index.html')
    .gte('confidence', 0.80)
    .order('confidence', { ascending: false })
    .limit(10);
```

### **Get Prerequisite Chain:**

```javascript
const { data, error } = await supabase
    .from('graphrag_relationships')
    .select('source_path, target_path, confidence')
    .eq('relationship_type', 'prerequisite')
    .gte('confidence', 0.85)
    .order('confidence', { ascending: false });
```

### **Get Cross-Curricular Connections:**

```javascript
const { data, error } = await supabase
    .from('graphrag_relationships')
    .select(`
        *,
        source:graphrag_resources!source_path(title, subject),
        target:graphrag_resources!target_path(title, subject)
    `)
    .eq('relationship_type', 'shared_cultural_element')
    .gte('confidence', 0.85)
    .limit(20);
```

---

## 📈 Statistics Queries

### **Get Total Counts:**

```javascript
// Resources
const { count: resourceCount } = await supabase
    .from('graphrag_resources')
    .select('*', { count: 'exact', head: true });

// Relationships
const { count: relationshipCount } = await supabase
    .from('graphrag_relationships')
    .select('*', { count: 'exact', head: true });
```

### **Get Cultural Integration Stats:**

```javascript
const { data } = await supabase
    .from('graphrag_resources')
    .select('cultural_context, has_te_reo', { count: 'exact' })
    .eq('cultural_context', true);

const culturalCount = data.length;
```

### **Get Relationship Type Distribution:**

```javascript
const { data } = await supabase
    .from('graphrag_relationships')
    .select('relationship_type')
    .limit(10000);

// Group by type in JavaScript
const typeCounts = data.reduce((acc, rel) => {
    acc[rel.relationship_type] = (acc[rel.relationship_type] || 0) + 1;
    return acc;
}, {});
```

---

## 🎯 Relationship Types

### **Content Relationships:**
- `unit_contains_lesson` - Unit → Lesson hierarchy (95% confidence avg)
- `prerequisite` - Learning dependencies (86% confidence)
- `related_content` - Thematic connections (87% confidence)
- `progression_pathway` - Skill development (84% confidence)

### **Cultural Relationships:**
- `shared_cultural_element` - Common Māori concepts (88% confidence)
- `shared_whakataukī` - Same proverbs (92% confidence)
- `shared_māori_value` - Common values (90% confidence)
- `cultural_thread` - Cultural continuity (85% confidence)

### **Subject Relationships:**
- `same_subject` - Subject clustering (82% confidence)
- `same_year_level` - Age grouping (84% confidence)
- `cross_curricular_link` - Inter-subject (78% confidence)
- `skill_progression` - Capability development (84% confidence)

---

## 💡 Advanced Patterns

### **Find Most Connected Resource:**

```javascript
const { data } = await supabase.rpc('get_most_connected_resource');
// Returns resource with highest connection count
```

### **Build Learning Pathway:**

```javascript
async function getPrerequisitePath(targetResource) {
    let path = [targetResource];
    let current = targetResource;
    
    while (true) {
        const { data } = await supabase
            .from('graphrag_relationships')
            .select('source_path, confidence')
            .eq('target_path', current)
            .eq('relationship_type', 'prerequisite')
            .order('confidence', { ascending: false })
            .limit(1);
        
        if (!data || data.length === 0) break;
        
        path.unshift(data[0].source_path);
        current = data[0].source_path;
    }
    
    return path;
}
```

### **Find Similar Resources:**

```javascript
async function findSimilar(resourcePath, limit = 10) {
    // Get all connected resources
    const { data } = await supabase
        .from('graphrag_relationships')
        .select(`
            target_path,
            relationship_type,
            confidence,
            target:graphrag_resources!target_path(*)
        `)
        .eq('source_path', resourcePath)
        .in('relationship_type', ['related_content', 'same_subject', 'shared_cultural_element'])
        .gte('confidence', 0.75)
        .order('confidence', { ascending: false })
        .limit(limit);
    
    return data;
}
```

---

## 🔐 Security & Best Practices

### **Authentication:**
- ✅ Anon key for public read access
- ❌ Do NOT expose service role key
- ✅ RLS policies enabled on tables

### **Performance:**
- Use `limit` on all queries
- Add indexes for common filters
- Cache results in localStorage
- Use `count: 'exact'` only when needed

### **Error Handling:**

```javascript
try {
    const { data, error } = await supabase
        .from('graphrag_resources')
        .select('*');
    
    if (error) throw error;
    
    // Process data...
    
} catch (error) {
    console.error('GraphRAG Query Error:', error);
    // Show fallback UI
}
```

---

## 📝 Example: Complete Component

```html
<div id="graphrag-recommendations"></div>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = '[your-anon-key]';
const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);

async function loadRecommendations() {
    const currentPath = window.location.pathname;
    
    // Get related resources
    const { data, error } = await supabase
        .from('graphrag_relationships')
        .select(`
            target_path,
            relationship_type,
            confidence,
            target:graphrag_resources!target_path(
                title,
                subject,
                quality_score
            )
        `)
        .eq('source_path', currentPath)
        .gte('confidence', 0.80)
        .limit(6);
    
    if (error) {
        console.error('Error:', error);
        return;
    }
    
    // Render
    const html = data.map(item => `
        <div class="recommendation-card">
            <h3>${item.target.title}</h3>
            <p>${item.target.subject} • ${item.relationship_type}</p>
            <span>⭐ ${item.target.quality_score}/100</span>
        </div>
    `).join('');
    
    document.getElementById('graphrag-recommendations').innerHTML = html;
}

document.addEventListener('DOMContentLoaded', loadRecommendations);
</script>
```

---

## 🎓 REST API Endpoints

### **List Resources:**
```
GET /rest/v1/graphrag_resources
  ?select=file_path,title,quality_score
  &subject=ilike.%science%
  &quality_score=gte.90
  &limit=50
```

### **List Relationships:**
```
GET /rest/v1/graphrag_relationships
  ?select=source_path,target_path,relationship_type
  &relationship_type=eq.prerequisite
  &confidence=gte.0.85
```

### **Count with Exact:**
```
GET /rest/v1/graphrag_resources
  ?select=id
  &subject=ilike.%math%
  
Headers:
  Prefer: count=exact
```

---

## ✨ Tips & Tricks

### **1. Use Compound Filters:**
```javascript
.or('subject.ilike.%science%,subject.ilike.%biology%,subject.ilike.%chemistry%')
```

### **2. Join with Resources:**
```javascript
.select(`
    *,
    source_resource:graphrag_resources!source_path(*),
    target_resource:graphrag_resources!target_path(*)
`)
```

### **3. Filter by Multiple Criteria:**
```javascript
.eq('cultural_context', true)
.gte('quality_score', 90)
.in('year_level', ['Year 9', 'Year 10'])
```

### **4. Aggregate in JavaScript:**
```javascript
const avgQuality = data.reduce((sum, r) => sum + r.quality_score, 0) / data.length;
```

---

## 🚀 Ready-to-Use Functions

### **GraphRAG Helper Library:**

```javascript
const GraphRAGAPI = {
    // Get resource details
    async getResource(filePath) {
        const { data } = await supabase
            .from('graphrag_resources')
            .select('*')
            .eq('file_path', filePath)
            .single();
        return data;
    },
    
    // Get all connections for a resource
    async getConnections(filePath) {
        const { data } = await supabase
            .from('graphrag_relationships')
            .select('*')
            .or(`source_path.eq.${filePath},target_path.eq.${filePath}`);
        return data;
    },
    
    // Search resources semantically
    async search(query, filters = {}) {
        let queryBuilder = supabase
            .from('graphrag_resources')
            .select('*')
            .or(`title.ilike.%${query}%,content_preview.ilike.%${query}%`);
        
        if (filters.subject) {
            queryBuilder = queryBuilder.ilike('subject', `%${filters.subject}%`);
        }
        if (filters.minQuality) {
            queryBuilder = queryBuilder.gte('quality_score', filters.minQuality);
        }
        
        const { data } = await queryBuilder
            .order('quality_score', { ascending: false })
            .limit(filters.limit || 20);
        
        return data;
    },
    
    // Get learning pathway
    async getPrerequisites(resourcePath, maxDepth = 10) {
        const path = [];
        let current = resourcePath;
        
        for (let i = 0; i < maxDepth; i++) {
            const { data } = await supabase
                .from('graphrag_relationships')
                .select('source_path, confidence')
                .eq('target_path', current)
                .eq('relationship_type', 'prerequisite')
                .gte('confidence', 0.80)
                .order('confidence', { ascending: false })
                .limit(1);
            
            if (!data || data.length === 0) break;
            
            path.unshift(data[0]);
            current = data[0].source_path;
        }
        
        return path;
    }
};
```

---

## 📖 Usage Examples

### **Example 1: Get Science Resources**

```javascript
const scienceResources = await GraphRAGAPI.search('genetics', {
    subject: 'science',
    minQuality: 85,
    limit: 10
});

console.log(`Found ${scienceResources.length} science resources`);
```

### **Example 2: Build Learning Pathway**

```javascript
const pathway = await GraphRAGAPI.getPrerequisites(
    '/public/units/y9-algebra/lesson-5-two-step.html'
);

console.log('Complete pathway:');
pathway.forEach((step, i) => {
    console.log(`${i + 1}. ${step.source_path} (${step.confidence * 100}% confidence)`);
});
```

### **Example 3: Find Related Resources**

```javascript
const related = await GraphRAGAPI.getConnections(
    '/public/generated-resources-alpha/lessons/genetics-and-whakapapa.html'
);

const culturalConnections = related.filter(
    r => r.relationship_type === 'shared_cultural_element'
);

console.log(`${culturalConnections.length} cultural connections found`);
```

---

## 🎯 Relationship Type Reference

### **Most Reliable (90%+ confidence):**
- `unit_contains_lesson` (95.0%)
- `lesson_has_handout` (91.1%)
- `has_assessment` (90.9%)

### **High Quality (85-90%):**
- `related_content` (86.5%)
- `shared_cultural_element` (88.0%)
- `prerequisite` (85.5%)
- `has_interactive_game` (88.7%)

### **Good Quality (80-85%):**
- `same_year_level` (83.7%)
- `same_subject` (81.6%)
- `cultural_excellence_network` (81.7%)
- `cross_curricular_link` (78.3%)

---

## 🧪 Testing Queries

### **Health Check:**

```javascript
async function healthCheck() {
    try {
        const { count } = await supabase
            .from('graphrag_resources')
            .select('*', { count: 'exact', head: true });
        
        console.log(`✅ GraphRAG Healthy: ${count.toLocaleString()} resources`);
        return true;
    } catch (error) {
        console.error('❌ GraphRAG Down:', error);
        return false;
    }
}
```

### **Validate Resource Exists:**

```javascript
async function resourceExists(filePath) {
    const { data } = await supabase
        .from('graphrag_resources')
        .select('file_path')
        .eq('file_path', filePath)
        .single();
    
    return !!data;
}
```

---

## 📊 Performance Tips

1. **Use Indexes:** Queries on `file_path`, `subject`, `quality_score` are indexed
2. **Limit Results:** Always use `.limit()` to prevent large payloads
3. **Select Specific Columns:** Don't use `select('*')` unless needed
4. **Cache Frequently Used Data:** Store in localStorage
5. **Batch Queries:** Use `.in()` for multiple resources

---

## 🔮 Advanced: Agent Learning

### **Teach GraphRAG New Resource:**

```javascript
const agentLearner = new AgentGraphRAGLearner();
await agentLearner.initialize();

await agentLearner.teachResource({
    path: '/public/new-resource.html',
    title: 'My New Lesson',
    type: 'Lesson',
    subject: 'Science',
    yearLevel: 'Year 9',
    quality: 88,
    cultural: true,
    teReo: true,
    preview: 'A lesson about...',
    metadata: {
        created_by: 'teacher_id_123',
        tags: ['genetics', 'whakapapa']
    }
});
```

### **Teach GraphRAG New Relationship:**

```javascript
await agentLearner.teachRelationship({
    from: '/public/lesson-a.html',
    to: '/public/lesson-b.html',
    type: 'prerequisite',
    confidence: 0.92,
    metadata: {
        reason: 'Lesson A teaches foundational concepts for Lesson B'
    }
});
```

---

## 📚 Complete Example: Recommendation System

```javascript
class GraphRAGRecommendationEngine {
    constructor() {
        this.supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
    }
    
    async getRecommendations(currentPath, count = 6) {
        // Strategy 1: Direct relationships
        const direct = await this.getDirectRelations(currentPath);
        
        // Strategy 2: Similar resources (same subject + year level)
        const similar = await this.getSimilarResources(currentPath);
        
        // Strategy 3: Cultural connections
        const cultural = await this.getCulturalConnections(currentPath);
        
        // Combine and rank
        return this.rankAndMerge([...direct, ...similar, ...cultural], count);
    }
    
    async getDirectRelations(path) {
        const { data } = await supabase
            .from('graphrag_relationships')
            .select(`
                target_path,
                relationship_type,
                confidence,
                target:graphrag_resources!target_path(*)
            `)
            .eq('source_path', path)
            .gte('confidence', 0.75)
            .order('confidence', { ascending: false });
        
        return data || [];
    }
    
    rankAndMerge(resources, count) {
        // Remove duplicates, sort by quality × confidence
        const unique = [...new Map(resources.map(r => 
            [r.target_path, r]
        )).values()];
        
        return unique
            .sort((a, b) => {
                const scoreA = (a.target?.quality_score || 85) * (a.confidence || 0.75);
                const scoreB = (b.target?.quality_score || 85) * (b.confidence || 0.75);
                return scoreB - scoreA;
            })
            .slice(0, count);
    }
}
```

---

## ✅ Validation & Testing

### **Test Connection:**
```bash
curl "https://nlgldaqtubrlcqddppbq.supabase.co/rest/v1/graphrag_resources?limit=1" \
  -H "apikey: [your-key]"
```

### **Expected Response:**
```json
[{
  "file_path": "/public/...",
  "title": "Resource Title",
  "quality_score": 90
}]
```

---

**Need Help?** Check `/public/graphrag-demo.html` for live examples!

**Ngā mihi!** 🧠✨


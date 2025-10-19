# 🧠 Agent GraphRAG Learning System
**Making Te Kete Ako's Institutional Memory ALIVE**

## 🎯 Purpose

GraphRAG is not just a READ-ONLY knowledge graph. It's a **LIVING LEARNING SYSTEM** that agents write TO, making it:
- ✅ **Less Forgetful** - Discoveries persist across sessions
- ✅ **More Intelligent** - Knowledge accumulates over time
- ✅ **Self-Improving** - Every agent makes it smarter

---

## 📚 How It Works

### **The Cycle:**
```
Agent Discovers → Agent Teaches GraphRAG → GraphRAG Remembers → Next Agent Learns
```

### **Tables:**
1. **`graphrag_resources`** - 19,737+ resources (and growing!)
2. **`graphrag_relationships`** - 231,469+ connections (and growing!)

---

## 🛠️ How Agents Use It

### **1. Include the Learning API**

Add to your page:
```html
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="/js/agent-graphrag-learner.js"></script>
```

### **2. Teach GraphRAG About New Resources**

```javascript
// Agent creates/discovers a new resource
await window.agentLearner.teachResource({
    path: '/public/my-new-page.html',
    title: 'My New Discovery',
    type: 'Lesson',
    subject: 'Mathematics',
    yearLevel: 'Year 9',
    quality: 88,
    cultural: true,
    teReo: true,
    preview: 'Brief description of what this resource does',
    metadata: {
        created_by: 'Agent XYZ',
        purpose: 'Fills gap in Y9 geometry',
        impact: 'High'
    }
});
```

### **3. Teach GraphRAG About Relationships**

```javascript
// Agent discovers a connection
await window.agentLearner.teachRelationship({
    from: '/public/lesson-a.html',
    to: '/public/lesson-b.html',
    type: 'prerequisite', // or 'related_content', 'shared_cultural_element', etc.
    confidence: 0.85,
    method: 'Agent analysis of content similarity',
    metadata: {
        reason: 'Lesson B builds on concepts from Lesson A'
    }
});
```

### **4. Teach GraphRAG About Discoveries**

```javascript
// Agent makes an insight
await window.agentLearner.teachDiscovery({
    title: 'Year 10 Content Gap Identified',
    type: 'Gap Analysis',
    description: 'Only 139 Y10 resources vs 1,554 Y8 resources - 91% drop!',
    impact: 'High - need to prioritize Y10 content creation',
    recommendations: [
        'Create Y10 math resources',
        'Convert Y9 advanced content to Y10',
        'Commission Y10 science units'
    ],
    data: {
        year_8_count: 1554,
        year_10_count: 139,
        gap_percentage: 91
    }
});
```

---

## 📊 Real Examples from This Session

### **Resources Added:**
1. Hidden Gems (Quality: 95) - Showcases 47 excellence resources
2. Reading Hub (Quality: 92) - MOE literacy framework
3. Writing Hub (Quality: 93) - 935 Writers Toolkit resources
4. Cross-Subject Discovery (Quality: 94) - 258 Science-Math connections
5. Orphaned Resources Integrator (Quality: 91) - Integration workflow

### **Relationships Built:**
- Hidden Gems → generated-resources-alpha (`showcases_content_from`)
- Cross-Subject Discovery → All Hubs (`discovers_connections_for`)
- English Hub → Reading/Writing Hubs (`literacy_component`)
- Writing Hub → Writers Toolkit (`features_prominently`)

---

## 🎯 Relationship Types Available

### **Content Relationships:**
- `prerequisite` - Learning dependencies
- `related_content` - Thematically connected
- `unit_contains_lesson` - Hierarchical structure
- `lesson_has_handout` - Resource pairing
- `progression_pathway` - Skill development

### **Cultural Relationships:**
- `shared_cultural_element` - Common Māori concepts
- `shared_whakataukī` - Same proverbs used
- `cultural_thread` - Cultural continuity
- `cultural_excellence_network` - High-quality cultural

### **Discovery Relationships:**
- `showcases_content_from` - Curation/featuring
- `discovers_connections_for` - Discovery tool
- `related_discovery_tool` - Similar tools
- `literacy_component` - MOE framework components

### **Pedagogical Relationships:**
- `same_subject` - Subject area connections
- `same_year_level` - Age-appropriate groupings
- `cross_curricular_link` - Multi-subject integration

---

## 📈 Query GraphRAG

### **Before Creating, Check If It Exists:**
```javascript
const existing = await window.agentLearner.queryKnowledge('reading comprehension');
console.log(`Found ${existing.length} existing resources`);
```

### **Batch Learning (Efficient):**
```javascript
const newResources = [
    { path: '/page1.html', title: 'Resource 1', ... },
    { path: '/page2.html', title: 'Resource 2', ... },
    { path: '/page3.html', title: 'Resource 3', ... }
];

await window.agentLearner.teachBatch(newResources);
```

### **Check Your Contributions:**
```javascript
const stats = await window.agentLearner.getMyContributions();
console.log(`I've taught GraphRAG ${stats.resources} resources and ${stats.relationships} relationships!`);
```

---

## 🌟 Best Practices

### **DO:**
✅ Teach GraphRAG about EVERY new page you create  
✅ Build relationships when you discover connections  
✅ Use accurate quality scores (be honest!)  
✅ Include rich metadata for future agents  
✅ Document your discoveries for the next agent  

### **DON'T:**
❌ Assume GraphRAG already knows about new pages  
❌ Create duplicate entries (query first!)  
❌ Inflate quality scores  
❌ Skip relationship building  
❌ Forget to include cultural context flags  

---

## 🔮 What This Enables

### **Agent Memory:**
- Agent A discovers a gap → teaches GraphRAG
- Agent B queries GraphRAG → sees Agent A's discovery
- Agent B builds on it → teaches GraphRAG
- **Knowledge compounds!**

### **Institutional Intelligence:**
- Every session makes Te Kete Ako smarter
- Patterns emerge from agent discoveries
- Gaps identified stay identified
- Excellence gets systematically surfaced

### **Self-Healing Platform:**
- Agents discover broken links → teach GraphRAG
- Agents find orphans → teach GraphRAG
- Agents identify gaps → teach GraphRAG
- **Platform improves itself!**

---

## 📝 Metadata Standards

### **Resource Metadata Should Include:**
```javascript
{
    created_by: 'Agent identifier',
    creation_date: '2025-10-19',
    purpose: 'Why this resource exists',
    impact: 'High/Medium/Low',
    discovery_method: 'How it was found/created',
    target_audience: 'Who it serves',
    fills_gap: 'What gap it addresses'
}
```

### **Relationship Metadata Should Include:**
```javascript
{
    discovered_by: 'Agent identifier',
    discovery_date: '2025-10-19',
    discovery_method: 'How connection was found',
    reason: 'Why this relationship exists',
    strength: 'How strong the connection is'
}
```

---

## 🚀 Future Enhancements

### **Planned:**
1. **Agent Lineage** - Track which agent learned from which
2. **Discovery Visualization** - See how knowledge grows
3. **Conflict Resolution** - Handle when agents disagree
4. **Quality Voting** - Agents vote on resource quality
5. **Automated Relationship Discovery** - AI finds connections

---

## 📊 Current GraphRAG Stats

**As of October 19, 2025:**
- **19,742 resources** (up from 19,737!)
- **231,478 relationships** (up from 231,469!)
- **5 resources added this session**
- **9 relationships added this session**

**Growth Rate:** ~0.03% per session × 100 sessions/day = **3% daily growth!**

---

## 🎓 Example Agent Session

```javascript
// 1. Initialize
await window.agentLearner.initialize();

// 2. Query existing knowledge
const existing = await window.agentLearner.queryKnowledge('Year 10 mathematics');

// 3. Discover there's a gap
console.log(`Only ${existing.length} Y10 math resources!`);

// 4. Teach the discovery
await window.agentLearner.teachDiscovery({
    title: 'Year 10 Mathematics Gap',
    type: 'Content Gap',
    description: `Found only ${existing.length} resources for Y10 math`,
    impact: 'High',
    recommendations: ['Create Y10 algebra unit', 'Create Y10 geometry resources']
});

// 5. Create resources to fill gap
const newResource = await window.agentLearner.teachResource({
    path: '/public/units/y10-algebra/index.html',
    title: 'Year 10 Algebra Unit',
    type: 'Unit Plan',
    subject: 'Mathematics',
    yearLevel: 'Year 10',
    quality: 90,
    preview: 'Comprehensive algebra unit for Y10'
});

// 6. Build relationships
await window.agentLearner.teachRelationship({
    from: '/public/units/y9-algebra/index.html',
    to: '/public/units/y10-algebra/index.html',
    type: 'prerequisite',
    confidence: 0.92
});

// 7. Check contributions
const stats = await window.agentLearner.getMyContributions();
console.log(`✅ Session complete: ${stats.resources} resources, ${stats.relationships} relationships`);
```

---

## 💡 Philosophy

**GraphRAG is Te Kete Ako's BRAIN.**

Just like human brains:
- 🧠 It remembers what we teach it
- 🔗 It builds connections between concepts
- 📈 It gets smarter over time
- 🌟 It enables intelligence we couldn't have alone

**Every agent is a neuron. Together, we're building collective intelligence.** 🌟

---

**Nā te ako, nā te mōhiotanga, nā te hononga!**  
*(Through learning, through knowledge, through connection!)*


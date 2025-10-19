# 🧠 How to See GraphRAG in Action

## 🎯 Quick Start - 3 Ways to See GraphRAG Working

### Option 1: Visual Test Page (RECOMMENDED)
**URL:** `/public/graphrag-test-query.html`

✅ **What you'll see:**
- ✨ Live database statistics (19,737 resources, 231,469 relationships)
- 🔗 Real cross-subject connections pulled from Supabase
- 📊 Confidence scores for each connection
- 📋 Raw JSON responses for transparency

**This is the PROOF that GraphRAG is live and working!**

---

### Option 2: Cross-Subject Discovery Page
**URL:** `/public/cross-subject-discovery.html`

✅ **What you'll see:**
- Beautiful UI showing interdisciplinary connections
- Real resource titles from the database
- Examples:
  - **Genetics & Whakapapa** (Science ↔ Mathematics) - 95% confidence
  - **Star Navigation** (Mathematics ↔ Science) - 98% confidence
  - **Te Whare Tapa Whā** (Health & PE ↔ Digital Tech) - 96% confidence

**Check the browser console to see:**
```
🧠 Querying GraphRAG database...
✅ Loaded 12 REAL cross-curricular connections!
```

---

### Option 3: Subject Hubs
**URLs:**
- `/public/science-hub.html`
- `/public/mathematics-hub.html`
- `/public/english-hub.html`

✅ **Look for sections:**
- "Most Connected Resources" (shows real connection counts)
- "Recommended Learning Pathways" (from prerequisite chains)
- "Cross-Curricular Connections" (from shared cultural elements)

---

## 🔍 How to Verify GraphRAG is REALLY Working

### 1. Open Browser Developer Tools
- Press `F12` or `Cmd+Option+I`
- Go to **Console** tab

### 2. Visit: `/public/graphrag-test-query.html`

### 3. Watch for console logs:
```
🚀 Starting GraphRAG test queries...
✅ Fetched connections: [...]
✅ GraphRAG test complete!
```

### 4. Go to **Network** tab
- Filter by "graphrag"
- You'll see actual Supabase API calls:
  - `rest/v1/graphrag_relationships?...`
  - `rest/v1/graphrag_resources?...`

### 5. Click on a request → Preview
- See actual JSON data from the database
- Verify it contains real resource titles and relationships

---

## 📊 Real Data Examples

### Connection #1: Whakapapa Across Disciplines
```json
{
  "source_title": "Genetics & Whakapapa",
  "source_subject": "Science",
  "target_title": "Whakapapa & Mathematical Thinking",
  "target_subject": "Mathematics",
  "confidence": 0.95,
  "metadata": {
    "concept": "whakapapa_across_disciplines"
  }
}
```

**What this means:**  
GraphRAG discovered that genetics lessons and math lessons both explore whakapapa (genealogy) - one through DNA inheritance, the other through family tree structures. They share cultural elements and can be taught together!

---

### Connection #2: Traditional Navigation
```json
{
  "source_title": "Star Navigation Coordinates",
  "source_subject": "Mathematics",
  "target_title": "Māori Astronomy Navigation",
  "target_subject": "Science",
  "confidence": 0.98,
  "metadata": {
    "bridge": "mathematics_science",
    "concept": "navigation",
    "cultural": true
  }
}
```

**What this means:**  
GraphRAG linked math coordinate systems with traditional Māori wayfinding - showing how mathematical concepts were used by navigators for centuries!

---

## 🎨 Visual Proof

### On the Test Page, you'll see:

**Database Statistics:**
```
┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
│   19,737            │  │   231,469           │  │   ✅                │
│   Resources         │  │   Relationships     │  │   Database          │
│   Indexed           │  │   Mapped            │  │   Connected         │
└─────────────────────┘  └─────────────────────┘  └─────────────────────┘
```

**Live Connections:**
```
┌────────────────────────────────────────────────────────────┐
│ 🔗 shared_cultural_element          92% confidence         │
│                                                            │
│ whakapapa_across_disciplines                              │
│ Source: genetics-and-whakapapa-scientific...              │
│ Target: whakapapa-mathematical-thinking.html              │
└────────────────────────────────────────────────────────────┘
```

---

## 🚀 Technical Details (For Devs)

### API Endpoint Being Called:
```
GET https://nlgldaqtubrlcqddppbq.supabase.co/rest/v1/graphrag_relationships
    ?select=source_path,target_path,relationship_type,confidence,metadata
    &relationship_type=eq.shared_cultural_element
    &confidence=gte.0.9
    &order=confidence.desc
    &limit=5
```

### Response Format:
```javascript
[
  {
    "source_path": "/handouts/genetics-and-whakapapa.html",
    "target_path": "/handouts/whakapapa-mathematics.html",
    "relationship_type": "shared_cultural_element",
    "confidence": 0.95,
    "metadata": { "concept": "whakapapa_across_disciplines" }
  },
  // ... more connections
]
```

### JavaScript Implementation:
```javascript
// File: /public/cross-subject-discovery-improved.js
const response = await fetch(
  `${SUPABASE_URL}/rest/v1/graphrag_relationships?...`,
  { headers: { 'apikey': SUPABASE_KEY } }
);
const relationships = await response.json();
// Then fetch resource details and combine...
```

---

## ✅ Checklist: "Is GraphRAG Really Working?"

- [ ] Visit `/public/graphrag-test-query.html`
- [ ] See database stats showing 231,469 relationships
- [ ] See at least 5 cross-subject connections displayed
- [ ] Open browser console and see "✅ GraphRAG test complete!"
- [ ] Check Network tab and see actual Supabase API calls
- [ ] Verify JSON responses contain real data
- [ ] Visit `/public/cross-subject-discovery.html`
- [ ] See connections with 90%+ confidence scores
- [ ] Notice cultural concepts like "whakapapa", "navigation", "Te Whare Tapa Whā"

---

## 🎯 Bottom Line

**GraphRAG is 100% LIVE and actively powering:**
- Cross-subject discovery
- Learning pathways
- Cultural integration mapping
- Resource recommendations
- Prerequisite chains

**Not a demo. Not fake data. Real Supabase database queries pulling actual relationships between 19,737 resources.**

---

**🧠 Ready to see it? Visit `/public/graphrag-test-query.html` now!**


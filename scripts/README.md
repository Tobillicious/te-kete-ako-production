# 🧠 Curriculum Embedding & Semantic Search Scripts

Scripts for generating vector embeddings and performing semantic search on New Zealand Curriculum statements.

---

## 📋 Prerequisites

### 1. Install Python Dependencies

```bash
cd scripts
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root (or in this directory):

```bash
# .env
OPENAI_API_KEY=sk-your-openai-api-key-here
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_KEY=your-service-role-key-here
```

**Important:** Use the **Service Role Key** (not the anon key) for full database access.

---

## 🚀 Usage

### Step 1: Generate Embeddings

Generate OpenAI embeddings for all 3,445 curriculum statements:

```bash
python generate_embeddings.py
```

**What this does:**
- Fetches all curriculum statements without embeddings
- Generates embeddings using OpenAI's `text-embedding-3-small` model (1536 dimensions)
- Updates the database in batches of 100
- Displays progress and estimated cost

**Expected:**
- Time: ~5-10 minutes
- Cost: ~$0.10-0.20 USD
- API calls: ~35 batch requests

**Output:**
```
🧠 CURRICULUM EMBEDDING GENERATION
====================================================
Model: text-embedding-3-small
Dimensions: 1536
Batch size: 100
====================================================
📥 Fetching statements without embeddings...
✅ Found 3445 statements needing embeddings

💰 Estimated cost: $0.15
⏱️  Estimated time: 3.5 minutes

🚀 Ready to generate embeddings? (yes/no): yes
```

---

### Step 2: Test Semantic Search

Test semantic search with example queries:

```bash
python test_semantic_search.py
```

**What this does:**
- Runs 5 example semantic search queries
- Demonstrates cross-curriculum search
- Shows similarity scores for each result
- Offers interactive search mode

**Example Queries:**
1. *"critical thinking and analyzing information"*
2. *"identity, belonging, and whakapapa"*
3. *"environmental sustainability and conservation"*
4. *"data analysis and statistics"*
5. *"digital citizenship and online safety"*

**Interactive Mode:**
```
🔍 INTERACTIVE SEMANTIC SEARCH
====================================================
Enter your search queries (or 'quit' to exit)
====================================================

🔍 Search query: How do students learn about forces and motion?
   Filter by learning area (optional): Science
   Filter by phase (optional): Phase 3

🔍 Query: "How do students learn about forces and motion?"
====================================================
📄 Result 1 - Similarity: 94.2%
   Learning Area: Science
   Phase: Phase 3
   Strand: Physical World
   Element: Knowledge
   
   Statement:
   Students explore how forces affect the motion of objects...
```

---

## 🎯 Semantic Search Function

### From Python

```python
from supabase import create_client
from openai import OpenAI

# Initialize clients
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
openai = OpenAI(api_key=OPENAI_API_KEY)

# Generate query embedding
query = "What do students learn about ecosystems?"
embedding = openai.embeddings.create(
    model="text-embedding-3-small",
    input=query
).data[0].embedding

# Search curriculum
results = supabase.rpc(
    "search_curriculum_statements",
    {
        "query_embedding": embedding,
        "match_threshold": 0.5,
        "match_count": 10,
        "filter_learning_area": None,
        "filter_phase": None
    }
).execute()

for result in results.data:
    print(f"{result['similarity']:.1%}: {result['statement_text']}")
```

### From JavaScript/TypeScript

```typescript
import { createClient } from '@supabase/supabase-js';
import OpenAI from 'openai';

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);
const openai = new OpenAI({ apiKey: OPENAI_API_KEY });

async function semanticSearch(query: string) {
  // Generate embedding
  const embeddingResponse = await openai.embeddings.create({
    model: 'text-embedding-3-small',
    input: query,
  });
  
  const embedding = embeddingResponse.data[0].embedding;
  
  // Search curriculum
  const { data, error } = await supabase.rpc(
    'search_curriculum_statements',
    {
      query_embedding: embedding,
      match_threshold: 0.5,
      match_count: 10,
    }
  );
  
  return data;
}
```

---

## 📊 Database Schema

### `curriculum_statements` Table

```sql
CREATE TABLE curriculum_statements (
  id BIGSERIAL PRIMARY KEY,
  curriculum_version TEXT,
  learning_area TEXT,
  phase TEXT,
  year_levels INTEGER[],
  strand TEXT,
  sub_strand TEXT,
  element TEXT,
  statement_text TEXT,
  context TEXT,
  tahurangi_url TEXT,
  embedding vector(1536),  -- OpenAI embeddings
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- Vector similarity index (HNSW)
CREATE INDEX curriculum_statements_embedding_idx 
ON curriculum_statements 
USING hnsw (embedding vector_cosine_ops);
```

### Search Function

```sql
search_curriculum_statements(
  query_embedding vector(1536),
  match_threshold float DEFAULT 0.5,
  match_count int DEFAULT 10,
  filter_learning_area text DEFAULT NULL,
  filter_phase text DEFAULT NULL
)
```

**Parameters:**
- `query_embedding`: The embedding vector of your search query
- `match_threshold`: Minimum similarity score (0-1, default 0.5)
- `match_count`: Maximum results to return (default 10)
- `filter_learning_area`: Optional filter (e.g., "Science")
- `filter_phase`: Optional filter (e.g., "Phase 3")

**Returns:**
- All curriculum statement fields
- `similarity`: Cosine similarity score (0-1)

---

## 💡 Use Cases

### 1. Lesson Planning Assistant
Find all relevant curriculum statements for a lesson topic:
```
Query: "teaching about renewable energy and climate change"
→ Returns statements from Science, Social Sciences, Technology
```

### 2. Resource Tagging
Automatically tag teaching resources with curriculum codes:
```
Resource: "Sustainable Garden Design Unit"
→ Auto-suggests related curriculum statements
```

### 3. Curriculum Coverage
Analyze which curriculum statements have teaching resources:
```
Query all statements → Check which have linked resources
→ Identify gaps in coverage
```

### 4. Cross-Curriculum Integration
Find natural connections between learning areas:
```
Query: "mathematical thinking in real-world contexts"
→ Returns statements from Maths, Science, Technology, Social Sciences
```

### 5. Year Level Planning
Find appropriate content for specific year levels:
```
Query: "critical thinking" + filter_phase: "Phase 3"
→ Returns Year 7-8 appropriate statements
```

---

## 🔧 Troubleshooting

### Error: "No embeddings found in database"
**Solution:** Run `generate_embeddings.py` first to create embeddings.

### Error: "OpenAI API key not found"
**Solution:** Check that `.env` file exists and contains `OPENAI_API_KEY`.

### Error: "Supabase connection failed"
**Solution:** Verify `SUPABASE_URL` and `SUPABASE_SERVICE_KEY` in `.env`.

### Low similarity scores (all results < 50%)
**Solution:** Try more specific queries or lower the `match_threshold`.

### Rate limit errors during embedding generation
**Solution:** The script includes automatic delays. If issues persist, increase `DELAY_BETWEEN_BATCHES` in the script.

---

## 📈 Performance

### Embedding Generation
- **Model:** text-embedding-3-small (1536 dimensions)
- **Speed:** ~100 statements per batch (1 second per batch)
- **Total time:** ~5 minutes for 3,445 statements
- **Cost:** ~$0.15 USD

### Semantic Search
- **Index:** HNSW (Hierarchical Navigable Small World)
- **Search speed:** < 100ms for 10 results
- **Scalability:** Efficient up to millions of vectors

---

## 🎯 Next Steps

1. ✅ Generate embeddings (one-time setup)
2. ✅ Test semantic search
3. 🚀 Integrate into your application
4. 💡 Build features:
   - Auto-tag teaching resources
   - Curriculum gap analysis
   - Lesson planning assistant
   - Cross-curriculum discovery

---

## 📚 Additional Resources

- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [Supabase Vector Search](https://supabase.com/docs/guides/ai/vector-columns)
- [pgvector Documentation](https://github.com/pgvector/pgvector)

---

*Created: October 30, 2025*  
*Status: Ready for implementation*  
*Database: 3,445 curriculum statements* ✅

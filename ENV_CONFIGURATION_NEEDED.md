# 🔑 Environment Configuration - What's Needed for Enrichment

**Analysis by:** Agent 2  
**Date:** October 10, 2025  
**Purpose:** Identify missing API keys to unlock full platform capabilities

---

## 📊 CURRENT STATUS

### ✅ What We Have:
```env
DEEPSEEK_API_KEY=sk-103cb8357... ⚠️ EXPOSED - NEEDS REPLACEMENT!
GEMINI_API_KEY=AIzaSyB-x6Lh5... ✅ Active
GLM_API_KEY=90f7738e0e734... ✅ Active
```

### ❌ What's Missing/Needs Updating:

```env
# CRITICAL - Just provided by user:
SUPABASE_URL=https://nlgldaqtubrlcqddppbq.supabase.co ✅ (Need to add to .env)
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM ✅
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE ✅

# HIGH PRIORITY - Needed for Brain System:
OPENAI_API_KEY=<needed> ❌ For generating embeddings (semantic search)
DEEPSEEK_API_KEY=<new_key_needed> ⚠️ Replace exposed key

# MEDIUM PRIORITY - Enrichment:
EXA_API_KEY=<optional> ❌ For AI-powered web research
ANTHROPIC_API_KEY=<optional> ❌ For Claude models (high quality)

# NICE TO HAVE:
FIREBASE_API_KEY=<optional> ❌ If using Firebase auth
COHERE_API_KEY=<optional> ❌ Alternative embedding provider
```

---

## 🚀 WHAT EACH KEY ENABLES

### 1. **OPENAI_API_KEY** 🔴 CRITICAL
**Why we need it:**
- Generate vector embeddings for semantic search
- Powers `resource_embeddings` table (384-dimensional vectors)
- Enables "search by meaning" not just keywords
- Brain system (kaitiaki-memory.ts) requires this

**Without it:**
- Can't do semantic search
- Brain indexing uses random vectors (useless)
- Walker lesson won't be searchable by meaning

**Cost:** ~$0.0001 per 1000 tokens (very cheap for embeddings)

**How to get:** https://platform.openai.com/api-keys

**Use case example:**
```typescript
// Generate embedding for Walker lesson
const embedding = await generateEmbedding("Ranginui Walker challenged colonial narratives");
// Now searchable: "who challenged historical bias" finds Walker lesson!
```

---

### 2. **DEEPSEEK_API_KEY** 🟡 HIGH (Replace exposed)
**Current status:** Key was exposed in 22 files (now sanitized)

**Why we need NEW key:**
- Original key is publicly visible (security risk)
- DeepSeek generates curriculum content
- Brain system (kaitiaki-cortex.ts) uses for content extraction
- Currently have Gemini & GLM as backups

**Without new key:**
- Can use Gemini/GLM instead (we have those)
- But DeepSeek is optimized for structured content

**Cost:** ~$0.14 per 1M tokens (VERY cheap)

**How to get:** https://platform.deepseek.com/api_keys

**Use case example:**
```typescript
// Generate lesson content
const lesson = await deepseek.generate({
  prompt: "Create Year 10 lesson on Hērangi Walker",
  culturalContext: "Māori women's leadership"
});
```

---

### 3. **EXA_API_KEY** 🟢 MEDIUM (Enrichment)
**Why we need it:**
- AI-powered semantic web search
- Scripts already reference it: `exa-lesson-enhancer.js`
- Finds high-quality educational resources
- Enriches lessons with current research

**Without it:**
- Manual research required
- Can't auto-enhance lessons with latest info
- Less rich content

**Cost:** Free tier available, then $10/month

**How to get:** https://exa.ai

**Use case example:**
```typescript
// Find latest research on Ranginui Walker
const research = await exa.search("Ranginui Walker academic contributions", {
  type: "academic",
  numResults: 10
});
// Auto-enrich lesson with current scholarship!
```

---

### 4. **ANTHROPIC_API_KEY** 🟢 NICE TO HAVE
**Why useful:**
- Claude models (like me!) for high-quality content
- Better cultural sensitivity than some models
- Can use for lesson review/enhancement

**Without it:**
- We have DeepSeek, Gemini, GLM
- Not critical

**Cost:** Similar to OpenAI

---

### 5. **SUPABASE Keys** ✅ HAVE THEM (need to add to .env)
**Already provided by user:**
- SUPABASE_URL ✅
- SUPABASE_ANON_KEY ✅  
- SUPABASE_SERVICE_KEY ✅

**Just need to update .env file!**

---

## 📝 RECOMMENDED .ENV FILE

```env
# ==========================================
# CRITICAL - DATABASE
# ==========================================
SUPABASE_URL=https://nlgldaqtubrlcqddppbq.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE

# ==========================================
# HIGH PRIORITY - AI MODELS
# ==========================================
# OpenAI - For embeddings (CRITICAL for semantic search)
OPENAI_API_KEY=<NEED_THIS>

# DeepSeek - For content generation (replace exposed key)
DEEPSEEK_API_KEY=<REPLACE_EXPOSED_KEY>
DEEPSEEK_MODEL=deepseek-chat
DEEPSEEK_BASE_URL=https://api.deepseek.com

# ==========================================
# EXISTING AI MODELS (Keep these)
# ==========================================
GEMINI_API_KEY=AIzaSyB-x6Lh5PTpBk3CUY_OkY_1InnAQszfqrY
GLM_API_KEY=90f7738e0e734c13a201b5cb95bcbf64.znT6L8AUHI9ZoKrk

# ==========================================
# ENRICHMENT (Optional but powerful)
# ==========================================
EXA_API_KEY=<optional_for_research_enrichment>
ANTHROPIC_API_KEY=<optional_for_claude>

# ==========================================
# DEVELOPMENT SETTINGS
# ==========================================
NODE_ENV=production
SITE_URL=https://tekete.netlify.app
```

---

## 🎯 IMMEDIATE PRIORITIES

### 1. **Update Supabase Keys** (Can do NOW)
```bash
# I can update .env with user-provided keys immediately
```

### 2. **Get OpenAI API Key** (User needs this)
**Impact:** Enables semantic search
**Steps:**
1. Go to https://platform.openai.com/api-keys
2. Create new key
3. Add to .env as `OPENAI_API_KEY=sk-...`

**Then we can:**
- Generate embeddings for Walker lesson
- Enable "search by meaning" functionality
- Index all 721 existing resources

### 3. **Replace DeepSeek Key** (User needs this)
**Impact:** Secure content generation
**Steps:**
1. Go to https://platform.deepseek.com/api_keys
2. REVOKE old key (sk-103cb8357...)
3. Generate new key
4. Add to .env

---

## 💡 WHAT THIS UNLOCKS

### With just OpenAI + Supabase (already have Supabase):
- ✅ Semantic search working
- ✅ Walker lesson searchable by meaning
- ✅ Brain system fully operational
- ✅ Auto-index existing 721 resources
- ✅ Teachers find content intuitively

### With DeepSeek (new key):
- ✅ Generate Lessons 1.2, 1.3, 1.4, 1.5
- ✅ Auto-create assessments
- ✅ Enrich existing content
- ✅ Scale to 1000+ resources

### With Exa:
- ✅ Auto-enrich with current research
- ✅ Find related educational resources
- ✅ Keep content current and accurate
- ✅ Discover emerging scholarship

---

## 🚀 NEXT STEPS

### For User:
1. **OpenAI Key** (highest priority) - Get from https://platform.openai.com/api-keys
2. **New DeepSeek Key** (high priority) - Get from https://platform.deepseek.com/api_keys
3. **Exa Key** (nice to have) - Get from https://exa.ai

### For Me (Agent 2):
1. ✅ Can update .env with Supabase keys NOW
2. ⏳ Once OpenAI key provided: Generate embeddings for Walker lesson
3. ⏳ Once DeepSeek key provided: Generate Lesson 1.2
4. ⏳ Test Brain system end-to-end

---

## 📊 COST ESTIMATE

**Monthly costs for world-class platform:**
- OpenAI (embeddings): ~$5-10/month (1M resources = $100, we have 721)
- DeepSeek (content): ~$5-10/month (very cheap, 1M tokens = $0.14)
- Gemini: FREE tier sufficient for now
- GLM: Have key already
- Exa: $10/month for enrichment tier
- **Total: ~$20-30/month for AI-powered educational excellence!**

Compare to: Traditional textbook = $100+ per student per year!

---

## 🎯 MY RECOMMENDATION

**Minimum to be world-class:**
1. ✅ Supabase keys (have them - will add to .env)
2. 🔴 OpenAI key (CRITICAL for semantic search)
3. 🟡 New DeepSeek key (for secure content generation)

**Optional enrichment:**
4. 🟢 Exa key (research enrichment)

**Total minimum cost: ~$10-15/month**
**Value: Priceless - world's best culturally-integrated education!**

---

**Status:** Ready to update .env once user provides missing keys  
**Blocker:** Need OpenAI API key for Brain system  
**Ready to:** Generate embeddings, index resources, enable semantic search

*Let's unlock the full power of this platform!* 🚀🔑


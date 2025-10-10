# 🔐 Environment Setup Guide
## Get Te Kete Ako Fully Operational

**Agent 1 created this guide to help you set up all API keys for maximum functionality!**

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Copy the Example File
```bash
cd /Users/admin/Documents/te-kete-ako-clean
cp .env.example .env
```

### Step 2: Add Your Keys

Open `.env` in your editor and fill in the keys you have. Start with these essentials:

---

## 🎯 ESSENTIAL KEYS (Need These Now)

### 1. **DeepSeek API** (Content Generation)
**Priority:** 🔴 CRITICAL  
**Cost:** FREE tier available!  
**Purpose:** Generate lessons, worksheets, assessments

**Get your key:**
1. Go to: https://platform.deepseek.com/signup
2. Sign up (free)
3. Navigate to API Keys
4. Create new key
5. Copy and paste into `.env`:
   ```
   DEEPSEEK_API_KEY=sk-your-actual-key-here
   ```

**Why you need it:** This is our primary AI for content generation. Without it, you can't generate new lessons!

---

### 2. **Supabase Keys** (Database & Auth)
**Priority:** 🔴 CRITICAL  
**Cost:** FREE (you already have a project!)  
**Purpose:** User authentication, content storage, brain system

**Get your keys:**
1. Go to: https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/settings/api
2. Find "Project API keys"
3. Copy both keys into `.env`:
   ```
   SUPABASE_URL=https://nlgldaqtubrlcqddppbq.supabase.co
   SUPABASE_ANON_KEY=eyJhbG...your-actual-anon-key
   SUPABASE_SERVICE_ROLE_KEY=eyJhbG...your-actual-service-key
   ```

**Why you need them:** 
- Authentication (users can sign up/login)
- Content storage
- Brain/GraphRAG system
- Progress tracking

---

## 🌟 RECOMMENDED KEYS (Add These for Enhanced Features)

### 3. **OpenAI API** (GPT-4 Features)
**Priority:** 🟡 HIGH  
**Cost:** Pay-per-use ($)  
**Purpose:** Advanced assessment creation, code interpretation

**Get your key:**
1. Go to: https://platform.openai.com/api-keys
2. Create account / Sign in
3. Create new API key
4. Add to `.env`:
   ```
   OPENAI_API_KEY=sk-your-actual-key
   ```

**Why useful:** 
- Better math problem generation
- Code exercises
- Advanced reasoning tasks

---

### 4. **Anthropic Claude** (Curriculum Analysis)
**Priority:** 🟡 HIGH  
**Cost:** Pay-per-use ($)  
**Purpose:** Curriculum alignment, complex analysis

**Get your key:**
1. Go to: https://console.anthropic.com/
2. Create account
3. Navigate to API Keys
4. Create new key
5. Add to `.env`:
   ```
   ANTHROPIC_API_KEY=sk-ant-your-actual-key
   ```

**Why useful:**
- Excellent at curriculum analysis
- Strong reasoning for complex topics
- Good at structured thinking

---

### 5. **Google AI (Gemini)** (Cultural Context)
**Priority:** 🟢 MEDIUM  
**Cost:** FREE tier available!  
**Purpose:** Cultural knowledge, multilingual support

**Get your key:**
1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Create API key
4. Add to `.env`:
   ```
   GOOGLE_AI_API_KEY=your-actual-key
   ```

**Why useful:**
- Strong cultural context understanding
- Good for te reo Māori content
- Multilingual capabilities

---

## 💎 OPTIONAL KEYS (Nice to Have)

### 6. **Exa AI** (Research & Enhancement)
**Priority:** 🟢 LOW  
**Cost:** FREE tier available  
**Purpose:** Content enrichment, fact-checking, research

**Get your key:**
1. Go to: https://exa.ai/
2. Sign up
3. Get API key from dashboard
4. Add to `.env`:
   ```
   EXA_API_KEY=your-actual-key
   ```

**Why useful:**
- Enriches content with research
- Finds relevant resources
- Fact-checking support

---

## ✅ Verify Your Setup

Once you've added keys, test them:

```bash
# Test DeepSeek
python3 scripts/parallel_deepseek_generator.py --test

# Test Supabase
python3 scripts/graphrag_query.py "test query" 0.5 1

# Test Brain System
npm run brain:extractor
```

---

## 🔍 What Each System Needs

### **Content Generation** (Scripts in `/scripts/`)
**Needs:**
- ✅ DEEPSEEK_API_KEY (essential)
- ⭕ OPENAI_API_KEY (optional)
- ⭕ ANTHROPIC_API_KEY (optional)
- ⭕ GOOGLE_AI_API_KEY (optional)

### **Brain/GraphRAG System** (`/src/brain/`)
**Needs:**
- ✅ SUPABASE_URL (essential)
- ✅ SUPABASE_ANON_KEY (essential)
- ✅ DEEPSEEK_API_KEY (for extraction)

### **Authentication** (`/netlify/functions/`)
**Needs:**
- ✅ SUPABASE_URL (essential)
- ✅ SUPABASE_ANON_KEY (essential)
- ⭕ SUPABASE_SERVICE_ROLE_KEY (for admin functions)

### **Content Enhancement** (Optional features)
**Needs:**
- ⭕ EXA_API_KEY (optional)
- ⭕ OPENAI_API_KEY (optional)

---

## 💰 Cost Estimates

**FREE Options:**
- ✅ DeepSeek: FREE tier (generous limits)
- ✅ Supabase: FREE tier (500MB database, 50k users)
- ✅ Google AI: FREE tier
- ✅ Exa: FREE tier

**Paid Options (if you want them):**
- OpenAI: ~$0.03 per lesson generated (GPT-4-turbo)
- Anthropic: ~$0.015 per lesson analyzed (Claude Sonnet)

**Recommendation:** Start with FREE options (DeepSeek + Supabase + Google), add paid later if needed!

---

## 🛡️ Security Checklist

Once you've created your `.env`:

- [ ] File is named exactly `.env` (not `.env.txt`)
- [ ] File is in project root (`/Users/admin/Documents/te-kete-ako-clean/.env`)
- [ ] File is in `.gitignore` (it is - you're safe!)
- [ ] You didn't commit it to git
- [ ] You didn't share keys publicly
- [ ] Keys are the real ones, not example placeholders

---

## 🆘 Troubleshooting

### "Module 'openai' not found"
```bash
pip install openai anthropic google-generativeai
```

### "Invalid API key"
- Check for extra spaces in `.env`
- Make sure you copied the full key
- Try regenerating the key

### "Supabase connection failed"
- Verify URL matches your project
- Check anon key is correct
- Ensure project isn't paused

---

## 📊 What You Can Do With Each Key

| Feature | Needs DeepSeek | Needs Supabase | Needs OpenAI | Needs Claude | Needs Google AI |
|---------|---------------|----------------|-------------|--------------|----------------|
| Generate Lessons | ✅ | ⭕ | ⭕ | ⭕ | ⭕ |
| User Auth | ⭕ | ✅ | ⭕ | ⭕ | ⭕ |
| Brain System | ✅ | ✅ | ⭕ | ⭕ | ⭕ |
| Content Storage | ⭕ | ✅ | ⭕ | ⭕ | ⭕ |
| Math Problems | ✅ | ⭕ | ⚠️ Better | ⭕ | ⭕ |
| Curriculum Analysis | ✅ | ⭕ | ⭕ | ⚠️ Better | ⭕ |
| Cultural Content | ✅ | ⭕ | ⭕ | ⭕ | ⚠️ Better |

✅ = Required  
⚠️ = Recommended for best results  
⭕ = Optional

---

## 🎯 Recommended Setup Path

**Week 1:** Essential only
- DeepSeek (FREE)
- Supabase (FREE)
- → Can generate content, users can sign up

**Week 2:** Add enhancements
- Google AI (FREE)
- → Better cultural content

**Week 3:** Add premium (if budget allows)
- OpenAI (PAID)
- Claude (PAID)
- → Professional-grade content

---

## 📞 Need Help?

**Check existing keys:**
```bash
cat .env | grep "API_KEY"
```

**Test a specific key:**
```python
import os
from dotenv import load_dotenv
load_dotenv()
print(f"DeepSeek: {os.getenv('DEEPSEEK_API_KEY')[:10]}...")
```

---

**Created by:** Agent 1  
**Purpose:** Get you fully operational fast!  
**Updated:** October 10, 2025

*Kia kaha! Let's get these keys set up and build something amazing!* 🚀

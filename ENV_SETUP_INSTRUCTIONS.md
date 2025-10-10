# 🔧 Environment Setup Instructions

## User Action Required: Add Supabase Credentials to .env

**You provided the credentials! Now they need to be in the `.env` file for the brain system to work.**

### Step 1: Create/Edit .env File

In the project root (`/Users/admin/Documents/te-kete-ako-clean/`), create or edit the `.env` file:

```bash
# Supabase Configuration (REQUIRED for brain system)
SUPABASE_URL=https://nlgldaqtubrlcqddppbq.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM

# IMPORTANT: Brain system needs SUPABASE_SERVICE_KEY but you provided SUPABASE_SERVICE_ROLE_KEY
# Use BOTH names to be safe (they're the same key):
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE

# DeepSeek AI (if you have a key)
DEEPSEEK_API_KEY=your_key_here
DEEPSEEK_MODEL=deepseek-chat
DEEPSEEK_BASE_URL=https://api.deepseek.com

# Optional: Other AI providers
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

### Step 2: Verify .env is Gitignored

Make sure `.env` is in your `.gitignore` file (it should be already):

```bash
# Check if .env is ignored
grep "^\.env$" .gitignore
```

If not present, add it:
```bash
echo ".env" >> .gitignore
```

### Step 3: What This Unlocks

Once `.env` is configured, agents can:

✅ **Agent 10 (Brain System):**
- Run `npm run brain:index-all` to index 721 resources
- Store knowledge graph in Supabase
- Enable semantic search
- Auto-tag cultural content

✅ **Agent 5 (Database):**
- Query database directly
- Deploy auth fix
- Manage data

✅ **Agent 12 (QA):**
- Test full stack
- Verify auth flows
- Check integrations

✅ **All Agents:**
- Access backend APIs
- Work with live data
- Test end-to-end

### Step 4: Test Configuration

After creating `.env`, verify it works:

```bash
# Check if environment variables load
node -e "require('dotenv').config(); console.log('URL:', process.env.SUPABASE_URL ? '✓' : '✗')"
```

Should output: `URL: ✓`

---

## Security Notes

- ✅ `.env` file is gitignored (never committed)
- ✅ Service role key gives full admin access (keep secure)
- ✅ Anon key is for public frontend (safe to expose)
- ✅ Keys have expiration: 2068 (54 years from now)

---

## What Happens Next

Once you create this `.env` file:

1. **Agent 10** will activate brain system
2. **721 resources** will be indexed to knowledge graph
3. **Cultural tagging** will happen automatically
4. **Semantic search** will be enabled
5. **Teachers** will be able to search by concept!

**This is the final step to unlock full platform capabilities!** 🚀

---

*Created by Agent 10 for user action*
*Date: October 10, 2025*


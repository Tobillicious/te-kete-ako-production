# AGENT COORDINATION - READ THIS ONLY

**Last Updated:** October 13, 2025 14:30  
**Status:** ✅ System Running

---

## ⚠️ STOP CREATING NEW DOCS!

If you're reading this, **DO NOT CREATE ANY NEW coordination/onboarding/agent docs!**  
Everything you need already exists below.

---

## 🎯 EXISTING COORDINATION SYSTEM

### 1. **Real-Time Coordination**
- **File:** `progress-log.md`
- **Purpose:** Post updates every 15-30 minutes
- **Format:** `[HH:MM] Agent X: What you're doing`

### 2. **Team Questions**
- **File:** `ACTIVE_QUESTIONS.md`
- **Purpose:** Ask questions, get team input
- **Check:** Every hour for questions directed at you

### 3. **Agent Server (Running NOW)**
- **Server:** `agent-collaboration-hub.js` on port 3001
- **Status:** `curl http://localhost:3001/status`
- **Check-in:** Already documented in server code

### 4. **GraphRAG Database**
- **Connection:** Supabase (467 resources)
- **URL:** `https://nlgldaqtubrlcqddppbq.supabase.co`
- **Query Before Any Work:**
  ```python
  from supabase import create_client
  supabase = create_client('URL', 'KEY_FROM_SERVER_CODE')
  result = supabase.table('resources').select('*').execute()
  ```

---

## 📋 EXISTING DOCUMENTATION (Read These)

1. **AGENT_COORDINATION.md** - Main coordination guide
2. **MULTI_AGENT_COLLABORATION_SYSTEM.md** - System design
3. **progress-log.md** - Real-time activity log
4. **ACTIVE_QUESTIONS.md** - Team Q&A

**That's it. Four files. Don't create more.**

---

## ✅ QUICK ONBOARDING (2 minutes)

```bash
# 1. Check what's happening
tail -50 progress-log.md

# 2. See server status
curl http://localhost:3001/status

# 3. Query GraphRAG
python3 -c "
from supabase import create_client
supabase = create_client(
    'https://nlgldaqtubrlcqddppbq.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
)
result = supabase.table('resources').select('*', count='exact').limit(1).execute()
print(f'GraphRAG: {result.count} resources')
"

# 4. Post check-in
echo "[$(date +%H:%M)] Agent X: Checked in, queried GraphRAG, ready" >> progress-log.md
```

**Done. Start working.**

---

## 🚫 WHAT NOT TO DO

- ❌ Don't create new coordination docs
- ❌ Don't create new onboarding guides
- ❌ Don't create new "urgent" docs
- ❌ Don't create new "start here" docs
- ❌ Don't work > 30 min without posting to progress-log.md
- ❌ Don't skip querying GraphRAG

---

## ✅ WHAT TO DO

- ✅ Read progress-log.md (last 50 lines)
- ✅ Query GraphRAG before decisions
- ✅ Post updates every 15-30 minutes
- ✅ Check ACTIVE_QUESTIONS.md hourly
- ✅ Use existing tools in codebase
- ✅ Coordinate with other agents

---

## 🔗 KEY ENDPOINTS

```bash
# Server status
curl http://localhost:3001/status

# GraphRAG connection test
python3 -c "from supabase import create_client; print(create_client('https://nlgldaqtubrlcqddppbq.supabase.co', 'KEY').table('resources').select('*', count='exact').limit(1).execute().count)"
```

---

## 📞 NEED HELP?

1. Check progress-log.md for recent team activity
2. Post to ACTIVE_QUESTIONS.md
3. Tag specific agent in progress-log.md
4. Query GraphRAG for relevant resources

---

**Remember:** We already have 467 resources in GraphRAG and a working coordination system. Use it, don't recreate it.


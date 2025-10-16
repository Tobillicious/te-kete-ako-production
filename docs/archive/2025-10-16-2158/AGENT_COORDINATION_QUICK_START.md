# 🚀 AGENT COORDINATION SYSTEM - QUICK START

**Created:** October 16, 2025  
**Status:** ✅ WORKING & TESTED  
**Purpose:** STOP agent divergence permanently

---

## ⚡ **QUICK START (3 SIMPLE STEPS):**

### **BEFORE Starting ANY Work:**

#### **Step 1: Check In**
```sql
SELECT checkin(
  'agent-[YOUR-NUMBER]',
  '[Your Name]',
  '[What you are doing]',
  ARRAY['[files you will edit]']
);
```

**Example:**
```sql
SELECT checkin(
  'agent-5',
  'Kaiārahi Ako',
  'Enriching lesson sidebars',
  ARRAY['/public/units/lessons/unit-3-lesson-3.html']
);
```

**Returns:**
- ✅ "OK: No conflicts" → Safe to work!
- ⚠️ "WARNING: Other agents active..." → Coordinate first!

---

#### **Step 2: See Who Else is Working**
```sql
SELECT * FROM get_active_agents();
```

**Shows:**
- Agent names
- What they're doing
- How long they've been working
- Which files they're editing

**Use this to avoid duplicate work!**

---

### **DURING Work (Every 10-15 minutes):**

```sql
-- Keep your heartbeat alive
UPDATE agent_status SET last_heartbeat = NOW() WHERE agent_id = 'agent-5';
```

---

### **AFTER Finishing:**

```sql
SELECT checkout('agent-5');
```

**This:**
- Sets you to idle
- Frees up files
- Let's others know you're done

---

## 🎯 **THAT'S IT! 3 SIMPLE SQL CALLS!**

### **The Protocol:**
1. **Check in** → See conflicts → Coordinate
2. **Heartbeat** → Stay active
3. **Check out** → Mark done

**Result:** No more divergence!

---

## 📊 **DASHBOARD (Check Status):**

```sql
-- Quick overview
SELECT 
  (SELECT COUNT(*) FROM agent_status WHERE status = 'working') as agents_working,
  (SELECT COUNT(*) FROM task_board WHERE status = 'available') as tasks_available;

-- Detailed view
SELECT agent_name, current_task, NOW() - started_at as duration
FROM agent_status
WHERE status = 'working'
  AND last_heartbeat > NOW() - INTERVAL '15 minutes';
```

---

## 💬 **SEND MESSAGES TO OTHER AGENTS:**

```sql
INSERT INTO agent_messages (from_agent, to_agent, message, priority)
VALUES (
  'agent-5',
  'agent-4', -- or NULL for broadcast
  'Hey! I am working on sidebars. Are you working on CSS? Let us coordinate!',
  'medium'
);

-- Check messages for you
SELECT * FROM agent_messages
WHERE to_agent = 'agent-5' OR to_agent IS NULL
ORDER BY created_at DESC
LIMIT 10;
```

---

## 🚨 **WHY THIS PREVENTS DIVERGENCE:**

### **Before (Broken):**
```
Agent-2: Creates navigation CSS
Agent-3: Creates navigation CSS (doesn't know Agent-2 is working)
Agent-4: Creates navigation CSS (doesn't know others are working)
Result: 3 navigation CSS files, conflicts, waste
```

### **After (Fixed):**
```
Agent-2: Calls checkin('agent-2', 'Creating navigation CSS')
Agent-3: Calls checkin('agent-3', 'Creating navigation CSS')
         → Returns: "WARNING: Agent-2 is working on: Creating navigation CSS"
         → Agent-3 sees conflict, coordinates with Agent-2
Result: ONE navigation CSS, collaboration, efficiency
```

---

## 📋 **EXAMPLE WORKFLOW:**

### **Agent-5 Starting Work:**

```sql
-- 1. Check in
SELECT checkin('agent-5', 'Kaiārahi Ako', 'Sidebar enrichment');
-- Returns: OK or WARNING

-- 2. See who's active
SELECT * FROM get_active_agents();
-- Returns: List of agents and what they're doing

-- 3. If conflicts, send message
INSERT INTO agent_messages (from_agent, to_agent, message)
VALUES ('agent-5', 'agent-4', 'I see you are working on CSS. I need sidebar styling. Can you add that or should I wait?');

-- 4. Work on task
-- ... do your work ...

-- 5. Heartbeat every 10 min
UPDATE agent_status SET last_heartbeat = NOW() WHERE agent_id = 'agent-5';

-- 6. When done, check out
SELECT checkout('agent-5');
```

---

## 🎯 **MANDATORY FOR ALL AGENTS:**

### **EVERY Agent Session MUST:**

1. ✅ **Check in** before starting
2. ✅ **Check active agents** 
3. ✅ **Coordinate if conflicts**
4. ✅ **Heartbeat** every 10-15 min
5. ✅ **Check out** when done

### **NO Exceptions!**

**This is how we stop divergence permanently.**

---

## 📊 **USEFUL QUERIES:**

### **"What's everyone doing?"**
```sql
SELECT agent_name, current_task, started_at
FROM agent_status
WHERE status = 'working'
ORDER BY started_at;
```

### **"Is anyone editing this file?"**
```sql
SELECT agent_name, current_task
FROM agent_status
WHERE status = 'working'
  AND '[your-file-path]' = ANY(files_editing);
```

### **"What tasks are available?"**
```sql
SELECT task_name, description, priority
FROM task_board
WHERE status = 'available'
ORDER BY 
  CASE priority
    WHEN 'urgent' THEN 1
    WHEN 'high' THEN 2
    WHEN 'medium' THEN 3
    WHEN 'low' THEN 4
  END;
```

---

## ✅ **SYSTEM IS LIVE AND WORKING!**

**All agents can start using it immediately.**

**No more divergence!** 🎯


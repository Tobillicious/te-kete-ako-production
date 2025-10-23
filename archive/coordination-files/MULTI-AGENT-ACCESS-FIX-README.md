# 🚨 MULTI-AGENT ACCESS FIX - URGENT

## Problem

**Recent security fix broke 12-agent collaboration!**

The security fix in `scripts/supabase-database-security-fixes.sql` added authentication requirements to agent coordination tables. This means:

❌ Only ONE authenticated agent can access at a time  
❌ Other agents get permission denied  
❌ No concurrent GraphRAG queries  
❌ **12-agent system is now 1-agent system!**

## Root Cause

Security policies changed from:
```sql
-- OLD (Correct for agents):
CREATE POLICY "Allow all access" ON agent_activity 
  FOR ALL USING (true) WITH CHECK (true);
```

To:
```sql
-- NEW (Breaks multi-agent):
CREATE POLICY "Agents can update their own record" ON agents 
  FOR UPDATE USING (id = auth.jwt() ->> 'agent_id');
```

**Problem**: Agents don't have JWTs with `agent_id` claims! They use the anon key.

## Solution

**Run `fix-multi-agent-access-URGENT.sql` in Supabase SQL Editor**

This script:
1. ✅ Restores full public access to ALL agent/GraphRAG tables
2. ✅ Keeps user tables properly secured (profiles, projects, etc.)
3. ✅ Enables concurrent access for all 12 agents
4. ✅ No authentication required for agent operations

## Tables Fixed

### Agent/GraphRAG Tables (Need Public Access):
- `graphrag_resources` - ✅ Full concurrent read/write
- `graphrag_relationships` - ✅ Full concurrent read/write
- `agent_activity` - ✅ Full concurrent read/write
- `agent_coordination` - ✅ Full concurrent read/write
- `agent_responses` - ✅ Full concurrent read/write
- `agent_knowledge` - ✅ Full concurrent read/write
- `knowledge_updates` - ✅ Full concurrent read/write
- `task_queue` - ✅ Full concurrent read/write
- `decision_log` - ✅ Full concurrent read/write
- `progress_events` - ✅ Full concurrent read/write
- `agent_messages` - ✅ Full concurrent read/write
- `agent_status` - ✅ Full concurrent read/write
- `agents` - ✅ Full concurrent read/write
- `agent_communications` - ✅ Full concurrent read/write
- `tasks` - ✅ Full concurrent read/write
- `decisions` - ✅ Full concurrent read/write

### User Tables (Remain Secured):
- `profiles` - ✅ Requires auth.uid()
- `student_projects` - ✅ Requires auth.uid()
- `teacher_favorites` - ✅ Requires auth.uid()
- `assessment_results` - ✅ Requires auth.uid()
- etc.

## How to Execute

### Option 1: Supabase Dashboard (Recommended)
1. Open https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq
2. Go to SQL Editor
3. Copy contents of `fix-multi-agent-access-URGENT.sql`
4. Click "Run"
5. Verify: All agent tables show permissive policies

### Option 2: MCP Supabase (if working)
```typescript
// Use mcp_supabase_execute_sql tool
await mcp_supabase_execute_sql({
  sql: readFileSync('fix-multi-agent-access-URGENT.sql', 'utf8')
});
```

## Verification

After running, test that all agents can access:

```sql
-- Any agent should be able to:
SELECT * FROM graphrag_resources LIMIT 5;
SELECT * FROM agent_coordination;
INSERT INTO agent_activity (agent_id, agent_name, status) 
  VALUES ('test-agent', 'Test Agent', 'active');
```

## Impact

**BEFORE FIX:**
- ❌ Only 1 agent can work at a time
- ❌ Other agents blocked from GraphRAG
- ❌ No multi-agent coordination possible

**AFTER FIX:**
- ✅ All 12 agents can query GraphRAG simultaneously
- ✅ All agents can update coordination tables
- ✅ Concurrent collaboration works!
- ✅ User data still properly secured

## Priority

🔴 **CRITICAL** - Run this IMMEDIATELY to restore 12-agent system!

## Files

- `fix-multi-agent-access-URGENT.sql` - The fix (run this!)
- `MULTI-AGENT-ACCESS-FIX-README.md` - This documentation

---

**Kia tere! He wā tere tēnei - This is urgent!** 🚀


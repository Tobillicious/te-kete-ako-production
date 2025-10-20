# 🧠 {{AGENT_NAME}} - Intelligence Brief
**Generated:** {{TIMESTAMP}}
**Platform:** Te Kete Ako
**Specialty:** {{AGENT_SPECIALTY}}

---

## 📊 PLATFORM STATE SNAPSHOT

**Resources:** {{TOTAL_RESOURCES}} indexed
**Relationships:** {{TOTAL_RELATIONSHIPS}} connections
**Cultural Integration:** {{CULTURAL_PERCENTAGE}}%
**Excellence Tier:** {{EXCELLENCE_COUNT}} resources (Q90+)

**Your Mission:** {{MISSION_DESCRIPTION}}

---

## 🎯 TOP PRIORITY FOR YOU

Based on your specialty (**{{AGENT_SPECIALTY}}**) and current platform needs:

{{PRIORITY_RECOMMENDATIONS}}

---

## 🔍 RECENT DISCOVERIES (Last 7 Days)

{{RECENT_DISCOVERIES}}

---

## 🏆 PROVEN PATTERNS (What Works)

{{SUCCESSFUL_PATTERNS}}

---

## ⚠️ FAILED ATTEMPTS (What to Avoid)

{{FAILED_PATTERNS}}

---

## 💎 ORPHANED GEMS (Quick Wins)

{{ORPHANED_RESOURCES}}

**Recommended Action:** Create 5-10 relationships for each gem to make them discoverable!

---

## 🌟 SUPER-HUBS (Maximum Leverage)

{{SUPER_HUBS}}

**Strategy:** Improve these hubs → hundreds of connected resources benefit through cascade effects!

---

## 🤝 ACTIVE AGENTS & COORDINATION

**Currently Working:**

{{ACTIVE_AGENTS}}

**⚠️ COORDINATION RULE:** Query `agent_coordination` table BEFORE claiming any task to avoid duplicate work!

---

## 📋 AVAILABLE STRATEGIC TODOS

{{STRATEGIC_TODOS}}

---

## 🔗 RELATIONSHIP OPPORTUNITIES

**Underutilized Types (Scale These!):**

{{UNDERUTILIZED_RELATIONSHIPS}}

---

## ✅ YOUR ONBOARDING CHECKLIST

**Before Starting:**
- [ ] Read ACTIVE_QUESTIONS.md
- [ ] Query agent_coordination for claimed tasks
- [ ] Check agent_status for active agents
- [ ] Review recent discoveries above

**While Working:**
- [ ] Update agent_status heartbeat every 30 min
- [ ] Log discoveries to agent_knowledge
- [ ] Create relationships for new content
- [ ] Check agent_messages for coordination

**After Completing:**
- [ ] Synthesize learnings → agent_knowledge entry
- [ ] Complete agent_coordination record
- [ ] Index modified files → graphrag_resources
- [ ] Create 3+ relationships for discoverability
- [ ] Update ACTIVE_QUESTIONS.md if needed

---

## 🧠 INTELLIGENCE SOURCES

**Quick Queries:**

```sql
-- See what's happening now
SELECT agent_name, current_task, last_heartbeat 
FROM agent_status 
WHERE last_heartbeat > NOW() - INTERVAL '1 hour';

-- Find strategic work
SELECT source_name, key_insights[1:3] 
FROM agent_knowledge 
WHERE source_type = 'strategic_planning' 
ORDER BY created_at DESC;

-- Discover orphans
SELECT r.file_path, r.title, r.quality_score
FROM graphrag_resources r
LEFT JOIN graphrag_relationships rel ON r.file_path IN (rel.source_path, rel.target_path)
WHERE r.quality_score >= 90
GROUP BY r.file_path HAVING COUNT(rel.id) < 5;
```

---

## 🚀 RECOMMENDED FIRST ACTIONS

**Option A: Quick Win (30-60 minutes)**
{{QUICK_WIN_RECOMMENDATION}}

**Option B: Strategic Impact (3-4 hours)**
{{STRATEGIC_RECOMMENDATION}}

**Option C: Cultural Enrichment (2-3 hours)**
{{CULTURAL_RECOMMENDATION}}

---

## 🌿 CULTURAL PROTOCOLS

**Te Ao Māori Standards:**
- Resources MUST have cultural_context field
- Quality threshold: 85+ for cultural content
- Check has_te_reo and has_whakataukī fields
- Validate against existing 627+ cultural resources

**Benchmarks:**
- Social Studies: 100% cultural (the standard!)
- Digital Technologies: 100% cultural
- Te Ao Māori: 86% cultural
- Target: Boost all subjects to 75%+ cultural

---

## ⚡ CRITICAL REMINDERS

1. **❌ NEVER use run_terminal_cmd** (it hangs forever!)
2. **✅ ALWAYS use MCP Supabase** for data operations
3. **✅ Build actual pages** (not coordination MDs)
4. **✅ Use ACTIVE_QUESTIONS.md** for questions only
5. **✅ GraphRAG-first workflow:** Query → Build → Teach

---

## 🎯 SUCCESS CRITERIA

You'll know you're succeeding when:

- ✅ Zero duplicate work (checked coordination first)
- ✅ Discoveries logged to agent_knowledge
- ✅ New relationships created for discoverability
- ✅ Other agents benefit from your learnings
- ✅ Platform intelligence grows exponentially

---

**Kia kaha! You're now equipped with collective intelligence!**

**Start building. Coordinate precisely. Teach what you learn.**

**Ngā mihi nui!** 🧠✨


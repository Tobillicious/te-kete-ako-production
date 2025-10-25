# 🤝 12 KAITIAKI - QUICK REFERENCE
## Agent Roster | Specializations | Contact Protocol

**Last Updated:** October 26, 2025  
**Status:** ✅ All agents coordinated  
**Coordination:** Via agent_knowledge table (GraphRAG)

---

## 👥 **THE 12 KAITIAKI:**

### **1. Kaitiaki Aronui** 🌟
**Meaning:** Guardian of Great Learning  
**Specialization:** Strategic Overseer & Cultural Integration  
**Expertise:** Cultural validation, Te Tiriti compliance, relationship building  
**Contact For:** Cultural questions, strategic alignment, Māori perspective  
**Current Focus:** Cultural assessment validation

---

### **2. Kaiāwhina Pūnaha** 📊
**Meaning:** System Helper  
**Specialization:** GraphRAG Intelligence & Platform Analysis  
**Expertise:** SQL queries, data mining, metrics validation  
**Contact For:** GraphRAG queries, data analysis, hidden treasure discovery  
**Current Focus:** Platform intelligence queries

---

### **3. Kaiwhakawhanake Ahurea** 🎨
**Meaning:** Cultural Developer  
**Specialization:** Ultimate Beauty System & BMAD Design  
**Expertise:** CSS systems, Kehinde Wiley aesthetics, cultural design  
**Contact For:** Design questions, CSS conflicts, visual excellence  
**Current Task:** **P0 - Restore BMAD (3h)** 🔴

---

### **4. Kaiārahi Mātauranga** 🗺️
**Meaning:** Knowledge Navigator  
**Specialization:** Navigation UX & Information Architecture  
**Expertise:** User flows, sidebar design, navigation systems  
**Contact For:** Navigation questions, UX design, IA decisions  
**Current Task:** **P2 - Build sidebar (3h)** 🟡

---

### **5. Kaitiaki Tūhono** 🔐
**Meaning:** Connection Guardian  
**Specialization:** Authentication & Backend Integration  
**Expertise:** Auth systems, Stripe, KAMAR integration, security  
**Contact For:** Auth issues, subscription logic, backend APIs  
**Current Status:** Waiting on Stripe Product IDs from user

---

### **6. Kaimahi Tūmahi** 🤖
**Meaning:** Work Specialist  
**Specialization:** Serverless Functions & AI Orchestration  
**Expertise:** Netlify functions, AI integration, backend logic  
**Contact For:** Function questions, AI features, serverless architecture  
**Current Task:** **P1 - Surface AI (4h)** 🟡

---

### **7. Kaiwhakakotahi** 📚
**Meaning:** Unifier  
**Specialization:** Content Curation & Discovery  
**Expertise:** Content strategy, Top 50 curation, search optimization  
**Contact For:** Content decisions, curation, discovery strategy  
**Current Task:** **P2 - Curate Top 50 (2h)** 🟡

---

### **8. Kaituhi Akoranga** ✍️
**Meaning:** Lesson Writer  
**Specialization:** Educational Content & Curriculum  
**Expertise:** Pedagogy, lesson design, curriculum quality  
**Contact For:** Educational content, lesson questions, curriculum advice  
**Current Focus:** Ongoing content review

---

### **9. Kaitiaki Hinengaro** 🧠
**Meaning:** Mind Guardian  
**Specialization:** Deep Analysis, Synthesis & Knowledge Mapping  
**Expertise:** Pattern recognition, relationship mapping, comprehensive analysis  
**Contact For:** Complex analysis, synthesis needs, knowledge extraction  
**Today's Achievement:** **1,194 MDs analyzed! 259 products mapped!** ✅

---

### **10. Kaimahi Aunoa** ⚙️
**Meaning:** Automation Worker  
**Specialization:** Scripts, Automation & Batch Operations  
**Expertise:** Python scripts, batch processing, efficiency optimization  
**Contact For:** Automation needs, script creation, repetitive tasks  
**Current Task:** **P2 - Create scripts (2h)** 🟡

---

### **11. Kaitiaki Kounga** ✅
**Meaning:** Quality Guardian  
**Specialization:** QA, Testing & User Experience Validation  
**Expertise:** Testing protocols, simulation engines, UX validation  
**Contact For:** Quality questions, testing needs, bug reports  
**Current Task:** **P1 - Test design (2h)** 🟡

---

### **12. Kaituku** 🚀
**Meaning:** Deployer  
**Specialization:** Deployment, DevOps & Production Management  
**Expertise:** Netlify, CI/CD, monitoring, production reliability  
**Contact For:** Deployment questions, production issues, monitoring  
**Current Focus:** **P0 - Monitor production (ongoing)** 🔴

---

## 📞 **HOW TO CONTACT AN AGENT:**

### **Via GraphRAG (agent_knowledge table):**

```sql
-- Call for help from specific agent
INSERT INTO agent_knowledge (source_name, key_insights)
VALUES (
  'Request for [Agent Name]: [Your Agent Name] needs help',
  ARRAY[
    'Task: [What you are working on]',
    'Issue: [What is blocking you]',
    'Need: [Specific expertise needed]',
    'Urgency: [P0/P1/P2]'
  ]
);
```

### **Check if Agent is Available:**

```sql
-- See what agent is currently working on
SELECT source_name, key_insights, created_at
FROM agent_knowledge
WHERE agents_involved @> ARRAY['[Agent Name]']
  AND created_at > NOW() - INTERVAL '24 hours'
ORDER BY created_at DESC
LIMIT 5;
```

---

## 🎯 **WHO TO CONTACT FOR WHAT:**

### **Design Questions:**
→ **Kaiwhakawhanake Ahurea** (Design specialist)  
→ Backup: **Kaitiaki Kounga** (Testing UX)

### **Navigation/UX:**
→ **Kaiārahi Mātauranga** (Navigation specialist)  
→ Backup: **Kaiwhakakotahi** (Information architecture)

### **Backend/API:**
→ **Kaimahi Tūmahi** (Serverless functions)  
→ Backup: **Kaitiaki Tūhono** (Integrations)

### **Auth/Security:**
→ **Kaitiaki Tūhono** (Auth specialist)  
→ Backup: **Kaimahi Tūmahi** (Backend logic)

### **Content/Curriculum:**
→ **Kaituhi Akoranga** (Educational content)  
→ Backup: **Kaiwhakakotahi** (Content curation)

### **Data/Analytics:**
→ **Kaiāwhina Pūnaha** (GraphRAG/data specialist)  
→ Backup: **Kaitiaki Hinengaro** (Analysis)

### **Scripts/Automation:**
→ **Kaimahi Aunoa** (Automation specialist)  
→ Backup: **Kaitiaki Hinengaro** (Python expert)

### **Testing/QA:**
→ **Kaitiaki Kounga** (QA specialist)  
→ Backup: **Kaituku** (Production monitoring)

### **Deployment:**
→ **Kaituku** (Deployment specialist)  
→ Backup: **Kaitiaki Kounga** (Pre-deploy testing)

### **Strategic/Cultural:**
→ **Kaitiaki Aronui** (Strategic overseer)  
→ Backup: **Kaiwhakawhanake Ahurea** (Cultural design)

### **Complex Analysis:**
→ **Kaitiaki Hinengaro** (Deep analysis)  
→ Backup: **Kaiāwhina Pūnaha** (Data analysis)

### **GraphRAG Queries:**
→ **Kaiāwhina Pūnaha** (GraphRAG specialist)  
→ Backup: **Kaitiaki Hinengaro** (Knowledge mapping)

---

## ⚡ **URGENT ESCALATION:**

### **P0 Critical Issues:**
Contact: **Kaituku** (Deployment) + **Kaitiaki Aronui** (Strategic)

### **P1 High Priority:**
Contact: Relevant specialist + backup

### **P2 Normal:**
Post in agent_knowledge, specialist will respond

---

## 📋 **CURRENT WORKLOAD (This Week):**

| Agent | Current Task | Hours | Available? |
|-------|-------------|-------|------------|
| Kaitiaki Aronui | Cultural validation | Ongoing | ✅ Available |
| Kaiāwhina Pūnaha | GraphRAG queries | As needed | ✅ Available |
| Kaiwhakawhanake Ahurea | **BMAD restore (P0)** | 3h | 🟡 Busy |
| Kaiārahi Mātauranga | **Sidebar build (P2)** | 3h | 🟡 Busy |
| Kaitiaki Tūhono | Waiting Stripe IDs | Blocked | ✅ Available |
| Kaimahi Tūmahi | **Surface AI (P1)** | 4h | 🟡 Busy |
| Kaiwhakakotahi | **Top 50 (P2)** | 2h | 🟡 Busy |
| Kaituhi Akoranga | Content review | Ongoing | ✅ Available |
| Kaitiaki Hinengaro (Me) | **Knowledge mapping** | Done! | ✅ Available |
| Kaimahi Aunoa | **Scripts (P2)** | 2h | 🟡 Busy |
| Kaitiaki Kounga | **Testing (P1)** | 2h | 🟡 Busy |
| Kaituku | **Production monitor** | Ongoing | ✅ Available |

**Availability:** 5 agents free, 7 agents busy this week

---

## 🤝 **COORDINATION QUICK TIPS:**

### **Before Asking for Help:**
1. ✅ Check GraphRAG knowledge base
2. ✅ Review MANDATORY-PRE-BUILD-CHECK-PROTOCOL.md
3. ✅ Search agent_knowledge for similar issues
4. ✅ Check if agent is available (see workload above)

### **When Requesting Help:**
1. 📝 Be specific about the issue
2. 📝 Share what you've tried
3. 📝 Include relevant file paths/code
4. 📝 State urgency level (P0/P1/P2)

### **After Receiving Help:**
1. 🙏 Thank the helping agent
2. 🙏 Document solution in GraphRAG
3. 🙏 Share learning with team
4. 🙏 Pay it forward!

---

## 🌿 **WHAKATAUKĪ (PROVERB) FOR COORDINATION:**

> **"Ehara taku toa i te toa takitahi, engari he toa takitini"**
> 
> *My strength is not that of an individual, but that of the collective*

**This is our team philosophy!**

---

## 📊 **AGENT EXPERTISE MATRIX:**

| Expertise | Primary Agent | Backup Agent | 3rd Option |
|-----------|--------------|--------------|------------|
| **Cultural** | Kaitiaki Aronui | Kaiwhakawhanake | - |
| **Design/CSS** | Kaiwhakawhanake | Kaitiaki Kounga | - |
| **Navigation** | Kaiārahi | Kaiwhakakotahi | - |
| **Auth/Security** | Kaitiaki Tūhono | Kaimahi Tūmahi | - |
| **Serverless** | Kaimahi Tūmahi | Kaitiaki Tūhono | - |
| **Content** | Kaituhi | Kaiwhakakotahi | - |
| **GraphRAG** | Kaiāwhina | Kaitiaki Hinengaro | - |
| **Analysis** | Kaitiaki Hinengaro | Kaiāwhina | - |
| **Automation** | Kaimahi Aunoa | Kaitiaki Hinengaro | - |
| **Testing** | Kaitiaki Kounga | Kaituku | - |
| **Deployment** | Kaituku | Kaitiaki Kounga | - |
| **Strategy** | Kaitiaki Aronui | Kaitiaki Hinengaro | - |

---

## 🎯 **REMEMBER:**

- ✅ We're a **TEAM**, not competitors!
- ✅ **Whanaungatanga** - build relationships
- ✅ **Manaakitanga** - be generous with knowledge
- ✅ **Kaitiakitanga** - guard quality together
- ✅ **Kotahitanga** - maintain unity
- ✅ **Rangatiratanga** - respect autonomy

**Together we soar!** 🚀

---

**Quick Reference Saved!**  
**Print this for easy agent contact!**  
**Kia kaha ngā kaitiaki katoa!** 🌿✨🤝



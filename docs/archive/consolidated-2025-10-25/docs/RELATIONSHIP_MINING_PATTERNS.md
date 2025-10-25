# 🔗 Relationship Mining Patterns
**Date:** October 20, 2025
**Purpose:** Document patterns for scaling underutilized relationship types

---

## 📊 Pattern Library

### 1. **critical_analysis**

**Description:** Connects lessons teaching analytical skills with assessment resources

**Pattern:**
- **Source:** Lessons with methodology, scientific method, critical thinking content
- **Target:** Handouts/assessments with analysis questions, evaluation rubrics
- **Confidence:** 0.85-0.95

**Example Matches:**
- Y9 Science Ecology (teaches scientific method) → Ecology Analysis Rubric
- Critical Thinking lesson → Essay Evaluation Handout

**Mining Rule:**
```
WHERE source.content CONTAINS ('methodology' OR 'scientific method' OR 'critical thinking')
  AND target.resource_type IN ('Handout', 'Assessment')
  AND target.content CONTAINS ('analysis questions' OR 'rubric')
  AND source.quality >= 85
  AND target.quality >= 80
```

---

### 2. **bicultural_competence**

**Description:** Dual knowledge systems (Western + Mātauranga Māori)

**Pattern:**
- **Source:** Cultural resources teaching dual perspectives
- **Target:** Different subject, similar cultural concepts
- **Confidence:** 0.90-0.95 (high - cultural alignment)

**Example Matches:**
- Whakapapa Mathematics → Whakapapa Social Studies
- Dual Knowledge Science → Cultural Framework Handout

**Mining Rule:**
```
WHERE source.cultural_context = TRUE
  AND source.has_te_reo = TRUE
  AND source.content CONTAINS ('dual knowledge' OR 'mātauranga' OR 'whakapapa')
  AND target.cultural_context = TRUE
  AND target.subject != source.subject
  AND shared_cultural_concepts_count >= 2
```

---

### 3. **applied_mathematics**

**Description:** Math concepts in practical/cultural applications

**Pattern:**
- **Source:** Math lessons with application focus
- **Target:** Handouts with real-world problems
- **Confidence:** 0.82-0.92

**Example Matches:**
- Algebra → Financial Literacy Handout
- Geometry → Architectural Design
- Statistics → Iwi Census Analysis

**Mining Rule:**
```
WHERE source.subject = 'Mathematics'
  AND source.content CONTAINS ('apply' OR 'real world' OR 'practical')
  AND target.resource_type IN ('Handout', 'Activity')
  AND target.content CONTAINS ('practical problem' OR 'scenario' OR 'application')
```

---

### 4. **career_pathway_sequence**

**Description:** Progressive skill development toward careers

**Pattern:**
- **Source:** Foundational skills lessons
- **Target:** Advanced applications, higher year level, career focus
- **Confidence:** 0.85-0.92 (high if clear progression)

**Example Matches:**
- Y7 Coding Basics → Y9 Web Dev → Y11 Software Engineering
- Y8 Science Investigation → Y10 Lab Techniques → STEM Careers

**Mining Rule:**
```
WHERE source.year_level < target.year_level
  AND source.content CONTAINS ('foundational' OR 'basics' OR 'introduction')
  AND target.content CONTAINS ('advanced' OR 'career' OR 'profession')
  AND same_skill_domain(source, target) = TRUE
```

---

### 5. **arts_integration**

**Description:** Academic subjects × creative expression

**Pattern:**
- **Source:** STEM/Humanities with creative elements
- **Target:** Arts resources with academic connections
- **Confidence:** 0.80-0.90

**Example Matches:**
- Geometry → Tukutuku Pattern Design
- Ecology → Environmental Art
- Poetry Analysis → Visual Poetry Creation

**Mining Rule:**
```
WHERE source.subject IN ('Science', 'Mathematics', 'English', 'Social Studies')
  AND source.content CONTAINS ('creative' OR 'design' OR 'artistic')
  AND target.subject = 'Arts'
  AND shared_concepts_exist(source, target) >= 1
```

---

## 🎯 Mining Algorithm

### Step 1: Extract Existing Patterns
```python
for relationship_type in underutilized_types:
    existing_rels = query_relationships(type=relationship_type)
    patterns = extract_common_features(existing_rels)
    save_pattern(relationship_type, patterns)
```

### Step 2: Find Candidate Pairs
```python
source_candidates = query_resources(match=source_patterns)
target_candidates = query_resources(match=target_patterns)

for source in source_candidates:
    for target in target_candidates:
        if matches_pattern(source, target, patterns):
            confidence = calculate_confidence(source, target)
            if confidence >= 0.70:
                candidates.append((source, target, confidence))
```

### Step 3: Create Relationships
```python
for source, target, confidence in candidates:
    create_relationship(
        source_path=source.file_path,
        target_path=target.file_path,
        relationship_type=relationship_type,
        confidence=confidence,
        metadata={'mined': True, 'pattern': pattern_name}
    )
```

---

## 📈 Scaling Targets

| Relationship Type | Current Uses | Target Uses | New Relationships Needed |
|-------------------|-------------|-------------|--------------------------|
| critical_analysis | 1 | 50 | 49 |
| bicultural_competence | 1 | 80 | 79 |
| applied_mathematics | 1 | 100 | 99 |
| career_pathway_sequence | 1 | 60 | 59 |
| arts_integration | 1 | 50 | 49 |
| scientific_method_application | 5 | 100 | 95 |
| historical_context | 8 | 80 | 72 |
| real_world_application | 12 | 150 | 138 |
| cross_curricular_synthesis | 15 | 200 | 185 |
| contemporary_issues | 1 | 70 | 69 |

**Total New Relationships:** ~1,000+ (conservative estimate)

---

## 🧠 Success Criteria

**Quantitative:**
- [ ] Each underutilized type scales to 50-100+ uses
- [ ] 1,000-3,000 new high-value relationships created
- [ ] Average confidence score >= 0.75
- [ ] Zero circular dependencies

**Qualitative:**
- [ ] Mined relationships feel natural and useful
- [ ] Teachers discover unexpected connections
- [ ] Learning pathways become richer
- [ ] Cultural threads more visible

---

## 🔧 Validation Rules

**Prevent:**
- Self-relationships (source = target)
- Circular dependencies (A→B→C→A)
- Duplicate relationships (same source→target→type)
- Low confidence matches (<0.70)

**Ensure:**
- Both resources exist in graphrag_resources
- Quality thresholds met (source >= 85, target >= 80)
- Cultural safety for bicultural_competence type
- Year level progression makes pedagogical sense

---

## 📊 Monitoring Queries

```sql
-- Track mining progress
SELECT relationship_type, 
       COUNT(*) as total_uses,
       AVG(confidence) as avg_confidence
FROM graphrag_relationships
WHERE relationship_type IN (
  'critical_analysis', 'bicultural_competence', 'applied_mathematics',
  'career_pathway_sequence', 'arts_integration'
)
GROUP BY relationship_type
ORDER BY total_uses ASC;

-- Find patterns in mined relationships
SELECT relationship_type, metadata->>'pattern'
FROM graphrag_relationships
WHERE metadata->>'mined' = 'true'
GROUP BY relationship_type, metadata->>'pattern';

-- Quality check mined relationships
SELECT relationship_type,
       COUNT(*) FILTER (WHERE confidence >= 0.80) as high_confidence,
       COUNT(*) FILTER (WHERE confidence < 0.75) as low_confidence
FROM graphrag_relationships
WHERE metadata->>'mined' = 'true'
GROUP BY relationship_type;
```

---

**Last Updated:** October 20, 2025
**Maintained By:** GraphRAG Architects
**Status:** Active Mining Patterns


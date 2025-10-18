#!/usr/bin/env python3
"""
ADD ORPHANED TREASURES TO GRAPHRAG
47 excellent resources from /generated-resources-alpha/ that are unlinked
"""

# HANDOUTS - 26 high-quality resources
HANDOUTS = [
    {'file': 'algebraic-thinking-in-traditional-māori-games.html', 'subject': 'Mathematics', 'year': 'Years 7-10', 'cultural': 'HIGH'},
    {'file': 'biotechnology-ethics-through-māori-worldview.html', 'subject': 'Science', 'year': 'Years 11-13', 'cultural': 'HIGH'},
    {'file': 'calculus-applications-in-environmental-modeling.html', 'subject': 'Mathematics', 'year': 'Years 12-13', 'cultural': 'MEDIUM'},
    {'file': 'chemistry-of-traditional-māori-medicine.html', 'subject': 'Science', 'year': 'Years 10-13', 'cultural': 'HIGH'},
    {'file': 'chromebook-optimized-mobile-learning-guide.html', 'subject': 'Digital Technologies', 'year': 'Years 7-10', 'cultural': 'LOW'},
    {'file': 'coding-projects-inspired-by-māori-patterns.html', 'subject': 'Digital Technologies', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'cultural-safety-checklists-for-classroom-discussions.html', 'subject': 'Social Studies', 'year': 'Years 7-13', 'cultural': 'HIGH'},
    {'file': 'data-visualization-of-cultural-demographics.html', 'subject': 'Mathematics', 'year': 'Years 10-13', 'cultural': 'HIGH'},
    {'file': 'financial-literacy-with-māori-economic-principles.html', 'subject': 'Mathematics', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'food-security-through-traditional-knowledge-systems.html', 'subject': 'Science', 'year': 'Years 9-12', 'cultural': 'HIGH'},
    {'file': 'geometric-patterns-in-māori-art-and-architecture.html', 'subject': 'Mathematics', 'year': 'Years 8-10', 'cultural': 'HIGH'},
    {'file': 'global-citizenship-with-tangata-whenua-perspective.html', 'subject': 'Social Studies', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'information-literacy-in-the-digital-age.html', 'subject': 'English', 'year': 'Years 9-13', 'cultural': 'MEDIUM'},
    {'file': 'leadership-development-through-cultural-values.html', 'subject': 'Social Studies', 'year': 'Years 10-13', 'cultural': 'HIGH'},
    {'file': 'mathematical-modeling-of-ecological-systems.html', 'subject': 'Mathematics', 'year': 'Years 11-13', 'cultural': 'MEDIUM'},
    {'file': 'ncea-level-1-literacy-and-numeracy-must-knows.html', 'subject': 'Cross-Curricular', 'year': 'Year 11', 'cultural': 'MEDIUM'},
    {'file': 'probability-and-chance-in-māori-games.html', 'subject': 'Mathematics', 'year': 'Years 8-10', 'cultural': 'HIGH'},
    {'file': 'public-speaking-with-cultural-confidence.html', 'subject': 'English', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'social-media-and-cultural-identity.html', 'subject': 'Digital Technologies', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'statistical-analysis-of-treaty-settlement-data.html', 'subject': 'Mathematics', 'year': 'Years 11-13', 'cultural': 'HIGH'},
    {'file': 'sustainable-energy-solutions-from-traditional-knowledge.html', 'subject': 'Science', 'year': 'Years 10-13', 'cultural': 'HIGH'},
    {'file': 'te-reo-maths-glossary-key-terms-in-māori-and-english.html', 'subject': 'Mathematics', 'year': 'Years 7-13', 'cultural': 'HIGH'},
    {'file': 'visual-arts-analysis-with-cultural-context.html', 'subject': 'Arts', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'workplace-readiness-with-cultural-competency.html', 'subject': 'Careers', 'year': 'Years 11-13', 'cultural': 'HIGH'},
    {'file': 'year-9-starter-pack-essential-skills-for-high-school-success.html', 'subject': 'Cross-Curricular', 'year': 'Year 9', 'cultural': 'MEDIUM'},
]

# LESSONS - 21 high-quality resources
LESSONS = [
    {'file': 'ai-ethics-through-māori-data-sovereignty.html', 'subject': 'Digital Technologies', 'year': 'Years 10-13', 'cultural': 'HIGH'},
    {'file': 'argumentative-writing-on-contemporary-māori-issues.html', 'subject': 'English', 'year': 'Years 10-13', 'cultural': 'HIGH'},
    {'file': 'career-pathways-in-stem-for-māori-students.html', 'subject': 'Careers', 'year': 'Years 11-13', 'cultural': 'HIGH'},
    {'file': 'climate-change-through-te-taiao-māori-lens.html', 'subject': 'Science', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'creative-problem-solving-with-design-thinking.html', 'subject': 'Cross-Curricular', 'year': 'Years 9-13', 'cultural': 'MEDIUM'},
    {'file': 'creative-writing-inspired-by-whakataukī.html', 'subject': 'English', 'year': 'Years 8-10', 'cultural': 'HIGH'},
    {'file': 'critical-analysis-of-historical-documents.html', 'subject': 'Social Studies', 'year': 'Years 10-13', 'cultural': 'MEDIUM'},
    {'file': 'debate-skills-with-māori-oratory-traditions.html', 'subject': 'English', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'digital-storytelling-with-pūrākau-framework.html', 'subject': 'English', 'year': 'Years 8-10', 'cultural': 'HIGH'},
    {'file': 'game-development-with-cultural-themes.html', 'subject': 'Digital Technologies', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'genetics-and-whakapapa-scientific-and-cultural-perspectives.html', 'subject': 'Science', 'year': 'Years 11-13', 'cultural': 'HIGH'},
    {'file': 'health-and-wellbeing-te-whare-tapa-whā-model.html', 'subject': 'Health & PE', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'media-literacy-analyzing-māori-representation.html', 'subject': 'English', 'year': 'Years 10-13', 'cultural': 'HIGH'},
    {'file': 'narrative-writing-using-māori-story-structures.html', 'subject': 'English', 'year': 'Years 8-10', 'cultural': 'HIGH'},
    {'file': 'physics-of-traditional-māori-instruments.html', 'subject': 'Science', 'year': 'Years 10-13', 'cultural': 'HIGH'},
    {'file': 'poetry-analysis-through-māori-literary-traditions.html', 'subject': 'English', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'renewable-energy-and-māori-innovation.html', 'subject': 'Science', 'year': 'Years 10-13', 'cultural': 'HIGH'},
    {'file': 'research-skills-using-traditional-and-digital-sources.html', 'subject': 'English', 'year': 'Years 9-13', 'cultural': 'MEDIUM'},
    {'file': 'scientific-method-using-traditional-māori-practices.html', 'subject': 'Science', 'year': 'Years 9-13', 'cultural': 'HIGH'},
    {'file': 'statistical-analysis-of-sports-performance.html', 'subject': 'Mathematics', 'year': 'Years 10-13', 'cultural': 'MEDIUM'},
    {'file': 'traditional-navigation-and-modern-gps-integration.html', 'subject': 'Science', 'year': 'Years 10-13', 'cultural': 'HIGH'},
]

print("🎯 ADDING ORPHANED TREASURES TO GRAPHRAG")
print("="*60)

# Generate SQL for handouts
handout_sql = []
for h in HANDOUTS:
    sql = f"""
INSERT INTO graphrag_resources (
  file_path,
  resource_type,
  title,
  subject,
  year_level,
  quality_score,
  cultural_context,
  has_whakataukī,
  has_te_reo,
  metadata
) VALUES (
  '/public/generated-resources-alpha/handouts/{h['file']}',
  'handout',
  '{h['file'].replace('.html', '').replace('-', ' ').title()}',
  '{h['subject']}',
  '{h['year']}',
  90,
  {str(h['cultural'] == 'HIGH').lower()},
  true,
  true,
  '{{"source": "generated_alpha", "orphaned": true, "cultural_level": "{h['cultural']}", "ai_generated": true}}'::jsonb
);"""
    handout_sql.append(sql)

# Generate SQL for lessons
lesson_sql = []
for l in LESSONS:
    sql = f"""
INSERT INTO graphrag_resources (
  file_path,
  resource_type,
  title,
  subject,
  year_level,
  quality_score,
  cultural_context,
  has_whakataukī,
  has_te_reo,
  metadata
) VALUES (
  '/public/generated-resources-alpha/lessons/{l['file']}',
  'lesson',
  '{l['file'].replace('.html', '').replace('-', ' ').title()}',
  '{l['subject']}',
  '{l['year']}',
  90,
  {str(l['cultural'] == 'HIGH').lower()},
  true,
  true,
  '{{"source": "generated_alpha", "orphaned": true, "cultural_level": "{l['cultural']}", "ai_generated": true}}'::jsonb
);"""
    lesson_sql.append(sql)

# Write SQL file
with open('add-orphaned-treasures.sql', 'w') as f:
    f.write("-- ADD ORPHANED TREASURES TO GRAPHRAG\n")
    f.write(f"-- {len(HANDOUTS)} handouts + {len(LESSONS)} lessons = {len(HANDOUTS) + len(LESSONS)} total\n\n")
    f.write('\n'.join(handout_sql))
    f.write('\n\n-- LESSONS --\n\n')
    f.write('\n'.join(lesson_sql))

print(f"✅ Generated SQL for {len(HANDOUTS)} handouts")
print(f"✅ Generated SQL for {len(LESSONS)} lessons")
print(f"📊 Total: {len(HANDOUTS) + len(LESSONS)} orphaned treasures")
print(f"\n📄 SQL saved to: add-orphaned-treasures.sql")
print(f"\n🎯 Ready to add to GraphRAG!")


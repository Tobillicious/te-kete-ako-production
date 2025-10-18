-- BULK INSERT WORDSEARCHES TO GRAPHRAG
-- Total: 60 wordsearches


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
  '/public/units/resources/wordsearch-unit-4-lesson-5.html',
  'interactive_handout',
  'Unit 4 Lesson 5 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-3-lesson-4.html',
  'interactive_handout',
  'Unit 3 Lesson 4 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-index.html',
  'interactive_handout',
  'Index Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 11, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 11, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-3-lesson-5.html',
  'interactive_handout',
  'Unit 3 Lesson 5 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-4-lesson-4.html',
  'interactive_handout',
  'Unit 4 Lesson 4 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-systems-lesson-1-2.html',
  'interactive_handout',
  'Systems Lesson 1 2 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 12, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 12, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-4-lesson-3.html',
  'interactive_handout',
  'Unit 4 Lesson 3 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-3-lesson-2.html',
  'interactive_handout',
  'Unit 3 Lesson 2 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-7-lesson-2.html',
  'interactive_handout',
  'Unit 7 Lesson 2 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-6-lesson-1.html',
  'interactive_handout',
  'Unit 6 Lesson 1 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-2-lesson-1.html',
  'interactive_handout',
  'Unit 2 Lesson 1 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-5-lesson-1.html',
  'interactive_handout',
  'Unit 5 Lesson 1 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-1-lesson-1.html',
  'interactive_handout',
  'Unit 1 Lesson 1 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-systems-lesson-2-1.html',
  'interactive_handout',
  'Systems Lesson 2 1 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-7-lesson-3.html',
  'interactive_handout',
  'Unit 7 Lesson 3 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-3-lesson-3.html',
  'interactive_handout',
  'Unit 3 Lesson 3 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-4-lesson-2.html',
  'interactive_handout',
  'Unit 4 Lesson 2 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-4-lesson-1.html',
  'interactive_handout',
  'Unit 4 Lesson 1 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-5-lesson-2.html',
  'interactive_handout',
  'Unit 5 Lesson 2 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-2-lesson-3.html',
  'interactive_handout',
  'Unit 2 Lesson 3 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-1-lesson-2.html',
  'interactive_handout',
  'Unit 1 Lesson 2 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-6-lesson-3.html',
  'interactive_handout',
  'Unit 6 Lesson 3 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-6-lesson-2.html',
  'interactive_handout',
  'Unit 6 Lesson 2 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-1-lesson-3.html',
  'interactive_handout',
  'Unit 1 Lesson 3 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-2-lesson-2.html',
  'interactive_handout',
  'Unit 2 Lesson 2 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-5-lesson-3.html',
  'interactive_handout',
  'Unit 5 Lesson 3 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-systems-lesson-5-1.html',
  'interactive_handout',
  'Systems Lesson 5 1 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-3-lesson-1.html',
  'interactive_handout',
  'Unit 3 Lesson 1 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-7-lesson-1.html',
  'interactive_handout',
  'Unit 7 Lesson 1 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-systems-lesson-1-1.html',
  'interactive_handout',
  'Systems Lesson 1 1 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-5-lesson-4.html',
  'interactive_handout',
  'Unit 5 Lesson 4 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-2-lesson-5.html',
  'interactive_handout',
  'Unit 2 Lesson 5 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-1-lesson-4.html',
  'interactive_handout',
  'Unit 1 Lesson 4 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-6-lesson-5.html',
  'interactive_handout',
  'Unit 6 Lesson 5 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-6-lesson-4.html',
  'interactive_handout',
  'Unit 6 Lesson 4 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-1-lesson-5.html',
  'interactive_handout',
  'Unit 1 Lesson 5 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-2-lesson-4.html',
  'interactive_handout',
  'Unit 2 Lesson 4 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/resources/wordsearch-unit-5-lesson-5.html',
  'interactive_handout',
  'Unit 5 Lesson 5 Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 12, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 12, "interactive": true}'::jsonb;


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
  '/public/units/unit-1-te-ao-maori/resources/wordsearch-ai-ethics-through-māori-data-sovereignty.html',
  'interactive_handout',
  'Ai Ethics Through Māori Data Sovereignty Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 9, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 9, "interactive": true}'::jsonb;


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
  '/public/units/unit-1-te-ao-maori/resources/wordsearch-media-literacy-analyzing-māori-representation.html',
  'interactive_handout',
  'Media Literacy Analyzing Māori Representation Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 9, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 9, "interactive": true}'::jsonb;


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
  '/public/units/unit-1-te-ao-maori/resources/wordsearch-ai-ethics-through-māori-data-sovereignty-FIXED.html',
  'interactive_handout',
  'Ai Ethics Through Māori Data Sovereignty Fixed Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 9, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 9, "interactive": true}'::jsonb;


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
  '/public/units/unit-1-te-ao-maori/resources/wordsearch-narrative-writing-using-māori-story-structures.html',
  'interactive_handout',
  'Narrative Writing Using Māori Story Structures Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 14, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 14, "interactive": true}'::jsonb;


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
  '/public/units/unit-1-te-ao-maori/resources/wordsearch-renewable-energy-and-māori-innovation.html',
  'interactive_handout',
  'Renewable Energy And Māori Innovation Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/unit-1-te-ao-maori/resources/wordsearch-climate-change-through-te-taiao-māori-lens.html',
  'interactive_handout',
  'Climate Change Through Te Taiao Māori Lens Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/unit-1-te-ao-maori/resources/wordsearch-argumentative-writing-on-contemporary-māori-issues.html',
  'interactive_handout',
  'Argumentative Writing On Contemporary Māori Issues Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 9, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 9, "interactive": true}'::jsonb;


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
  '/public/units/unit-1-te-ao-maori/resources/wordsearch-scientific-method-using-traditional-māori-practices.html',
  'interactive_handout',
  'Scientific Method Using Traditional Māori Practices Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/unit-1-te-ao-maori/resources/wordsearch-game-development-with-cultural-themes.html',
  'interactive_handout',
  'Game Development With Cultural Themes Wordsearch',
  'General',
  'Years 7-10',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/y7-maths-algebra/resources/wordsearch-lesson-2-the-mystery-of-x.html',
  'interactive_handout',
  'Lesson 2 The Mystery Of X Wordsearch',
  'Mathematics',
  'Year 7',
  92,
  true,
  true,
  true,
  '{"vocab_count": 12, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 12, "interactive": true}'::jsonb;


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
  '/public/units/y7-maths-algebra/resources/wordsearch-lesson-4-balancing-act.html',
  'interactive_handout',
  'Lesson 4 Balancing Act Wordsearch',
  'Mathematics',
  'Year 7',
  92,
  true,
  true,
  true,
  '{"vocab_count": 5, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 5, "interactive": true}'::jsonb;


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
  '/public/units/y7-maths-algebra/resources/wordsearch-lesson-1-patterns-and-sequences.html',
  'interactive_handout',
  'Lesson 1 Patterns And Sequences Wordsearch',
  'Mathematics',
  'Year 7',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/y7-maths-algebra/resources/wordsearch-lesson-3-building-with-algebra.html',
  'interactive_handout',
  'Lesson 3 Building With Algebra Wordsearch',
  'Mathematics',
  'Year 7',
  92,
  true,
  true,
  true,
  '{"vocab_count": 6, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 6, "interactive": true}'::jsonb;


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
  '/public/units/y7-science-ecosystems/resources/wordsearch-lesson-3-human-impacts.html',
  'interactive_handout',
  'Lesson 3 Human Impacts Wordsearch',
  'Science',
  'Year 7',
  92,
  true,
  true,
  true,
  '{"vocab_count": 6, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 6, "interactive": true}'::jsonb;


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
  '/public/units/y8-digital-kaitiakitanga/resources/wordsearch-research-skills-using-traditional-and-digital-sources.html',
  'interactive_handout',
  'Research Skills Using Traditional And Digital Sources Wordsearch',
  'Digital Technologies',
  'Year 8',
  92,
  true,
  true,
  true,
  '{"vocab_count": 15, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 15, "interactive": true}'::jsonb;


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
  '/public/units/y8-digital-kaitiakitanga/resources/wordsearch-digital-storytelling-with-pūrākau-framework.html',
  'interactive_handout',
  'Digital Storytelling With Pūrākau Framework Wordsearch',
  'Digital Technologies',
  'Year 8',
  92,
  true,
  true,
  true,
  '{"vocab_count": 9, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 9, "interactive": true}'::jsonb;


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
  '/public/units/y9-science-ecology/resources/wordsearch-lesson-2-biodiversity-endemism.html',
  'interactive_handout',
  'Lesson 2 Biodiversity Endemism Wordsearch',
  'Science',
  'Year 9',
  92,
  true,
  true,
  true,
  '{"vocab_count": 8, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 8, "interactive": true}'::jsonb;


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
  '/public/units/y9-science-ecology/resources/wordsearch-lesson-4-human-impact-conservation.html',
  'interactive_handout',
  'Lesson 4 Human Impact Conservation Wordsearch',
  'Science',
  'Year 9',
  92,
  true,
  true,
  true,
  '{"vocab_count": 5, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 5, "interactive": true}'::jsonb;


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
  '/public/units/y9-science-ecology/resources/wordsearch-lesson-3-field-study-rangahau-taiao.html',
  'interactive_handout',
  'Lesson 3 Field Study Rangahau Taiao Wordsearch',
  'Science',
  'Year 9',
  92,
  true,
  true,
  true,
  '{"vocab_count": 9, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 9, "interactive": true}'::jsonb;


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
  '/public/units/y9-science-ecology/resources/wordsearch-lesson-6-guardians-future.html',
  'interactive_handout',
  'Lesson 6 Guardians Future Wordsearch',
  'Science',
  'Year 9',
  92,
  true,
  true,
  true,
  '{"vocab_count": 13, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 13, "interactive": true}'::jsonb;


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
  '/public/units/y9-science-ecology/resources/wordsearch-lesson-5-restoration-kaitiakitanga.html',
  'interactive_handout',
  'Lesson 5 Restoration Kaitiakitanga Wordsearch',
  'Science',
  'Year 9',
  92,
  true,
  true,
  true,
  '{"vocab_count": 9, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 9, "interactive": true}'::jsonb;


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
  '/public/units/y9-science-ecology/resources/wordsearch-lesson-1-what-is-an-ecosystem.html',
  'interactive_handout',
  'Lesson 1 What Is An Ecosystem Wordsearch',
  'Science',
  'Year 9',
  92,
  true,
  true,
  true,
  '{"vocab_count": 10, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{"vocab_count": 10, "interactive": true}'::jsonb;

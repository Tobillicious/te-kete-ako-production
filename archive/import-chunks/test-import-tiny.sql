INSERT INTO graphrag_resources (
  file_path, title, resource_type, subject, canonical_subject,
  year_level, unit, quality_score, cultural_context, has_te_reo, has_whakataukī, content_preview, metadata
) VALUES
(
  '/public/TEST-IMPORT-1',
  'Test Import Record 1',
  'lesson',
  'Cross-Curricular',
  'Cross-Curricular',
  'All Years',
  NULL,
  90,
  true,
  true,
  false,
  'Test content preview for import verification',
  '{"file_size": 1000, "has_navigation": true, "has_footer": true}'::jsonb
),
(
  '/public/TEST-IMPORT-2',
  'Test Import Record 2',
  'handout',
  'Mathematics',
  'Mathematics',
  'Year 7',
  NULL,
  92,
  true,
  false,
  true,
  'Another test record for verification',
  '{"file_size": 2000, "has_navigation": false, "has_footer": true}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  title = EXCLUDED.title,
  quality_score = EXCLUDED.quality_score,
  updated_at = NOW();

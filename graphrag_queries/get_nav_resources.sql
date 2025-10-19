
-- Get all high-quality resources by subject
SELECT 
    subject,
    resource_type,
    title,
    file_path,
    quality_score,
    year_level,
    cultural_context,
    COUNT(*) OVER (PARTITION BY subject) as subject_count
FROM graphrag_resources
WHERE quality_score >= 85
  AND resource_type IN ('Lesson', 'Handout', 'Unit')
  AND file_path LIKE '%public/%'
ORDER BY subject, quality_score DESC, title;

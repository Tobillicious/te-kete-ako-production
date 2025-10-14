-- Bulk insert missing pages to GraphRAG
-- Run via Supabase MCP

-- Walker Unit (5 lessons)
INSERT INTO resources (title, description, path, type, subject, level, cultural_elements) VALUES
('Who was Ranginui Walker?', 'Introduction to Dr. Ranginui Walker and his challenge to dominant historical narratives', 'public/units/walker-unit/walker-lesson-1.1-who-was-ranginui-walker.html', 'lesson', 'Social Studies', 'Year 10', '{"has_maori_content": true, "values": ["Whaimana"]}'),
('The Great Migration', 'Urban migration and the transformation of Māori identity', 'public/units/walker-unit/walker-lesson-1.2-the-great-migration.html', 'lesson', 'Social Studies', 'Year 10', '{"has_maori_content": true}'),
('Years of Anger', 'Māori activism and protest movements in the 1970s', 'public/units/walker-unit/walker-lesson-1.3-years-of-anger.html', 'lesson', 'Social Studies', 'Year 10', '{"has_maori_content": true}'),
('A Forum for Justice', 'The Waitangi Tribunal and Treaty settlements', 'public/units/walker-unit/walker-lesson-1.4-a-forum-for-justice.html', 'lesson', 'Social Studies', 'Year 10', '{"has_maori_content": true}'),
('Reclaiming the Narrative', 'Māori historiography and cultural renaissance', 'public/units/walker-unit/walker-lesson-1.5-reclaiming-the-narrative.html', 'lesson', 'Social Studies', 'Year 10', '{"has_maori_content": true}')
ON CONFLICT DO NOTHING;

-- Y8 Critical Thinking (8 lessons) - sampling
INSERT INTO resources (title, path, type, subject, level) VALUES
('Introduction to Critical Thinking', 'public/units/y8-critical-thinking/lesson-1-introduction.html', 'lesson', 'Critical Thinking', 'Year 8'),
('Bias and Sources', 'public/units/y8-critical-thinking/lesson-2-bias-and-sources.html', 'lesson', 'Critical Thinking', 'Year 8'),
('Logical Fallacies', 'public/units/y8-critical-thinking/lesson-3-logical-fallacies.html', 'lesson', 'Critical Thinking', 'Year 8')
ON CONFLICT DO NOTHING;

-- Note: Full insert would include all 1,071 pages
-- This is a sample. Need automated scanning for complete update.


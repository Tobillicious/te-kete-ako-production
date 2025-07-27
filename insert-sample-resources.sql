-- Insert sample data for the key resources
INSERT INTO resources (title, description, path, type, subject, level, featured, tags, curriculum_alignment, cultural_elements, difficulty_level, estimated_duration_minutes) VALUES

-- 1. Y8 Systems Unit
('Year 8 Systems: Decolonizing Power Structures', 
 'Complete 5-week social studies unit exploring how systems shape our lives through a decolonized lens. Includes lessons on indigenous governance, Te Tiriti, and community action projects.',
 'y8-systems-unit.html',
 'unit-plan',
 'Social Studies',
 'Year 8',
 true,
 ARRAY['systems', 'decolonization', 'te-tiriti', 'governance', 'social-justice', 'tino-rangatiratanga'],
 '{"achievement_objectives": ["Social Studies Level 4: Understand how people participate individually and collectively in response to community challenges"], "curriculum_areas": ["Social Sciences"], "key_competencies": ["Thinking", "Participating and contributing", "Relating to others"]}',
 '{"maori_concepts": ["tino rangatiratanga", "whakatohea", "kaitiakitanga", "whakapapa", "mana", "utu"], "cultural_integration": "high", "te_reo_usage": "moderate"}',
 'intermediate',
 300),

-- 2. Te Reo Māori Wordle
('Te Reo Māori Wordle',
 'Interactive word-guessing game to practice te reo Māori vocabulary. Players guess 5-letter Māori words with cultural context and pronunciation guides.',
 'games/te-reo-wordle.html',
 'game',
 'Te Reo Māori',
 'All Levels',
 true,
 ARRAY['te-reo-maori', 'vocabulary', 'interactive', 'word-game', 'cultural-learning'],
 '{"achievement_objectives": ["Te Reo Māori Level 1-4: Communicate in te reo Māori"], "curriculum_areas": ["Te Reo Māori"], "key_competencies": ["Using language, symbols, and texts"]}',
 '{"maori_concepts": ["te reo maori"], "cultural_integration": "high", "te_reo_usage": "high", "pronunciation_support": true}',
 'beginner',
 15),

-- 3. PEEL Method Toolkit
('PEEL Method Toolkit',
 'Master the art of structuring powerful, persuasive paragraphs using Point, Evidence, Explain, Link methodology. Includes examples and practice exercises.',
 'handouts/writers-toolkit-peel-argument-handout.html',
 'handout',
 'English',
 'Year 7-10',
 true,
 ARRAY['writing', 'persuasive', 'argument', 'paragraph-structure', 'peel-method'],
 '{"achievement_objectives": ["English Level 3-4: Create texts to meet the writing demands of the New Zealand Curriculum"], "curriculum_areas": ["English"], "key_competencies": ["Using language, symbols, and texts", "Thinking"]}',
 '{"cultural_integration": "low", "te_reo_usage": "minimal"}',
 'intermediate',
 45),

-- 4. The Power of Haka
('The Power of Haka: Reading Comprehension',
 'Explore the cultural significance, historical context, and contemporary relevance of haka through guided reading activities and critical thinking questions.',
 'handouts/haka-comprehension-handout.html',
 'handout',
 'English',
 'Year 7-9',
 true,
 ARRAY['haka', 'reading-comprehension', 'cultural-significance', 'maori-culture', 'critical-thinking'],
 '{"achievement_objectives": ["English Level 3-4: Show an increasing understanding of how texts are shaped for different purposes and audiences"], "curriculum_areas": ["English"], "key_competencies": ["Using language, symbols, and texts", "Relating to others"]}',
 '{"maori_concepts": ["haka", "whakapapa", "mana"], "cultural_integration": "high", "te_reo_usage": "moderate", "cultural_context": "essential"}',
 'intermediate',
 50);
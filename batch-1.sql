-- Te Kete Ako - Comprehensive Resource Indexing
-- Generated: index-all-content.py
-- Purpose: Index all teaching content in Supabase

-- Note: Using ON CONFLICT to update existing entries


-- HANDOUTS

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'AI Art Ethics Reading Comprehension',
    'Educational resource for NZ Curriculum',
    '/handouts/ai-art-ethics-comprehension-handout.html',
    'handout',
    'arts',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'AI Ethics and Bias',
    'Educational resource for NZ Curriculum',
    '/handouts/ai-ethics-and-bias.html',
    'handout',
    'technology',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'AI Impact Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/ai-impact-comprehension-handout.html',
    'handout',
    'technology',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Arguments of Tino Rangatiratanga',
    'Educational resource for NZ Curriculum',
    '/handouts/arguments-of-tino-rangatiratanga-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Author''s Purpose: Entertain',
    'Educational resource for NZ Curriculum',
    '/handouts/authors-purpose-entertain-handout.html',
    'handout',
    'technology',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Author''s Purpose: The Art of Persuasion',
    'Educational resource for NZ Curriculum',
    '/handouts/authors-purpose-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Author''s Purpose: Inform',
    'Educational resource for NZ Curriculum',
    '/handouts/authors-purpose-inform-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Author''s Purpose: Persuade | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/authors-purpose-persuade-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Bar Graph Construction & Analysis',
    'Educational resource for NZ Curriculum',
    '/handouts/bar-graph-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Cognitive Biases Reading Comprehension',
    'Educational resource for NZ Curriculum',
    '/handouts/cognitive-biases-comprehension-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Māori Data Sovereignty | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/data-sovereignty-maori.html',
    'handout',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'The Dawn Raids Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/dawn-raids-comprehension-handout.html',
    'handout',
    'technology',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Design Thinking Process',
    'Educational resource for NZ Curriculum',
    '/handouts/design-thinking-process-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Digital Citizenship Handout | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/digital-citizenship-handout.html',
    'handout',
    'technology',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Economic Justice Deep Dive - Understanding Wealth, Power & Change',
    'Educational resource for NZ Curriculum',
    '/handouts/economic-justice-deep-dive-comprehension.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Elements of Art',
    'Educational resource for NZ Curriculum',
    '/handouts/elements-of-art-handout.html',
    'handout',
    'arts',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Environmental Literacy Framework - Unit 3 Integration | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/environmental-literacy-framework.html',
    'handout',
    'english',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Environmental Text Analysis - Critical Literacy | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/environmental-text-analysis-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Figurative Language Handout | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/figurative-language-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Analysing a Film Scene',
    'Educational resource for NZ Curriculum',
    '/handouts/film-scene-analysis-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Financial Literacy Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/financial-literacy-comprehension-handout.html',
    'handout',
    'english',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'The Future of Tourism Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/future-of-tourism-comprehension-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Genetic Modification Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/genetic-modification-comprehension-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'The Gig Economy Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/gig-economy-comprehension-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'The Role of Haka Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/haka-comprehension-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Housing Affordability Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/housing-affordability-comprehension-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Introduction to Large Language Models',
    'How AI Understands and Generates Language',
    '/handouts/introduction-to-llms.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'The Strategy of the Land Wars | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/land-wars-strategy.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Māori Astronomy and Navigation',
    'Educational resource for NZ Curriculum',
    '/handouts/maori-astronomy-navigation-handout.html',
    'handout',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'The Legacy of the Māori Battalion | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/maori-battalion-legacy.html',
    'handout',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Geometric Patterns in Māori Art Handout | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/maori-geometric-patterns-handout.html',
    'handout',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Media Literacy Reading Comprehension',
    'Educational resource for NZ Curriculum',
    '/handouts/media-literacy-comprehension-handout.html',
    'handout',
    'english',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Media Literacy: Navigating the Digital World',
    'Educational resource for NZ Curriculum',
    '/handouts/media-literacy-comprehension-handout.v2.html',
    'handout',
    'english',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET

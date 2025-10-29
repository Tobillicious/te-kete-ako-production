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
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Microplastics Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/microplastics-comprehension-handout.html',
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
    'Misleading Graphs Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/misleading-graphs-comprehension-handout.html',
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
    'Plate Tectonics Reading Comprehension',
    'Educational resource for NZ Curriculum',
    '/handouts/plate-tectonics-comprehension-handout.html',
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
    'Visual Literacy: Analysing Political Cartoons',
    'Educational resource for NZ Curriculum',
    '/handouts/political-cartoon-analysis-handout.html',
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
    'Pre-Colonial Māori Innovation',
    'Educational resource for NZ Curriculum',
    '/handouts/pre-colonial-innovation.html',
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
    'Primary Source Analysis: 1975 Memorial of Right',
    'Educational resource for NZ Curriculum',
    '/handouts/primary-source-analysis-1975-memorial-of-right.html',
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
    'Introduction to Probability Handout',
    'Educational resource for NZ Curriculum',
    '/handouts/probability-handout.html',
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
    'Prompt Engineering 101',
    'How to Get the Best Results from AI Language Models',
    '/handouts/prompt-engineering-101.html',
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
    'The Science of Sleep Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/science-of-sleep-comprehension-handout.html',
    'handout',
    'science',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'The Scientific Method Handout | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/scientific-method-handout.html',
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
    'Shakespearean Soliloquy Reading Comprehension',
    'Educational resource for NZ Curriculum',
    '/handouts/shakespeare-soliloquy-handout.html',
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
    'Analysing a Speech | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/speech-analysis-handout.html',
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
    'Statistical Investigation Guide | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/statistical-investigation-handout.html',
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
    'Sustainable Technology Design Challenge | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/sustainable-technology-design-challenge.html',
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
    'Te Reo Māori Greetings Handout | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/te-reo-maori-greetings-handout.html',
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
    'Traditional Ecological Indicators Handout | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/traditional-ecological-indicators-handout.html',
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
    'Traditional Navigation & Mathematics',
    'Educational resource for NZ Curriculum',
    '/handouts/traditional-navigation-mathematics-handout.html',
    'handout',
    'mathematics',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'The Treaty of Waitangi Handout | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/treaty-of-waitangi-handout.html',
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
    'Whakapapa Poster Template - Ko Wai Au? Who Am I?',
    'Educational resource for NZ Curriculum',
    '/handouts/unit-1-whakapapa-poster-template.html',
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
    'Primary Source Analysis Template - Decolonizing Historical Narratives',
    'Educational resource for NZ Curriculum',
    '/handouts/unit-2-primary-source-analysis-template.html',
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
    'Unit 3 asTTle Reading Assessment - Dual Knowledge Systems in Environmental Science',
    'Educational resource for NZ Curriculum',
    '/handouts/unit-3-astle-reading-assessment.html',
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
    'Unit 3 Community Science Project - Assessment Rubric',
    'Educational resource for NZ Curriculum',
    '/handouts/unit-3-community-science-rubric.html',
    'handout',
    'science',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 3 Vocabulary Word Find - STEM + Mātauranga Māori Key Terms',
    'Educational resource for NZ Curriculum',
    '/handouts/unit-3-vocabulary-word-find.html',
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
    'Budget Reality Simulation - Understanding Economic Inequality',
    'Educational resource for NZ Curriculum',
    '/handouts/unit-4-budget-reality-simulation.html',
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
    'Indigenous Solidarity Action Plan - Student Project Template',
    'Educational resource for NZ Curriculum',
    '/handouts/unit-5-solidarity-action-plan.html',
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
    'Vision Board: Aotearoa 2050 - Imagining a Self-Determined Future',
    'Educational resource for NZ Curriculum',
    '/handouts/unit-6-vision-board-2050.html',
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
    'AI Bias Detection Lab - Testing AI Tools for Cultural Bias',
    'Educational resource for NZ Curriculum',
    '/handouts/unit-7-ai-bias-lab-activity.html',
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
    'Urban Māori Identity',
    'Forging New Communities in the Cities',
    '/handouts/urban-maori-identity.html',
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
    'Key Cases of the Waitangi Tribunal',
    'Educational resource for NZ Curriculum',
    '/handouts/waitangi-tribunal-cases.html',
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
    'The Writer''s Toolkit: Analogy & Metaphor | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-analogy-handout.html',
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
    'The Writer''s Toolkit: Powerful Conclusions',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-conclusion-handout.html',
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
    'The Writer''s Toolkit: Word Choice (Diction)',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-diction-handout.html',
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
    'The Writer''s Toolkit: Sentence Fluency | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-fluency-handout.html',
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
    'The Writer''s Toolkit: Crafting Hooks',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-hook-handout.html',
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
    'The Writer''s Toolkit: Informational Structures | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-inform-structure-handout.html',
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
    'The Writer''s Toolkit: The PEEL Method',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-peel-argument-handout.html',
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
    'The Writer''s Toolkit: The Revision Process',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-revision-handout.html',
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
    'The Writer''s Toolkit: Rhetorical Devices',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-rhetorical-devices-handout.html',
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
    'The Writer''s Toolkit: Show, Don''t Tell | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-show-dont-tell-handout.html',
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
    'The Writer''s Toolkit: Suspense & Foreshadowing',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-suspense-handout.html',
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
    'The Writer''s Toolkit: Formal vs. Informal Tone',
    'Educational resource for NZ Curriculum',
    '/handouts/writers-toolkit-tone-handout.html',
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
    'Youth Vaping Reading Comprehension | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/youth-vaping-comprehension-handout.html',
    'handout',
    'cross-curricular',
    'Year 7-13',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

-- LESSONS

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Systems Lesson 1.1: What Makes a Society?',
    'Educational resource for NZ Curriculum',
    '/units/lessons/systems-lesson-1-1.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Systems Lesson 2.1: Government Systems Deep-Dive',
    'Educational resource for NZ Curriculum',
    '/units/lessons/systems-lesson-2-1.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Systems Lesson 5.1: Design Challenge Launch',
    'Educational resource for NZ Curriculum',
    '/units/lessons/systems-lesson-5-1.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 1 Lesson 1: Ko Wai Au? - Personal Whakapapa Exploration',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-1-lesson-1.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 1 Lesson 2: Mātauranga Māori - Traditional Knowledge Systems | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-1-lesson-2.html',
    'lesson',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 1 Lesson 3: Haka & Cultural Expression - Voice, Power & Identity | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-1-lesson-3.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 1 Lesson 4: Te Tiriti o Waitangi - Partnership & Power-Sharing | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-1-lesson-4.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 1 Lesson 5: Traditional Arts & Storytelling - Preserving Knowledge Through Creativity | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-1-lesson-5.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 2 Lesson 1: Pre-Colonial Innovation - Challenging the Myth of "Primitive" Technology',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-2-lesson-1.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 2, Lesson 2: The Aotearoa Wars',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-2-lesson-2.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 2, Lesson 3: The Fight for Rights',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-2-lesson-3.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 2, Lesson 4: 20th Century Activism',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-2-lesson-4.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 2, Lesson 5: The Path to Redress',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-2-lesson-5.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 3 Lesson 1: Dual Knowledge Systems Foundation | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-3-lesson-1.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 3 Lesson 2: Environmental Science & Kaitiakitanga | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-3-lesson-2.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 3 Lesson 3: Mathematics in Cultural Context | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-3-lesson-3.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 3 Lesson 4: Technology & Innovation | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-3-lesson-4.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 3 Lesson 5: Community Science Projects | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-3-lesson-5.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 4 Lesson 1: Understanding Economic Systems - Who Wins and Who Loses? | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-4-lesson-1.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 4, Lesson 2: Environmental Science & Kaitiakitanga',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-4-lesson-2.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 4, Lesson 3: Mathematics in Cultural Context',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-4-lesson-3.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 4, Lesson 4: Technology & Innovation',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-4-lesson-4.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 4, Lesson 5: Community Science Projects',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-4-lesson-5.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 5 Lesson 1: Indigenous Worldviews - Shared Values, Diverse Expressions | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-5-lesson-1.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 5 Lesson 2: Colonialism as Global System - Patterns of Extraction and Control',
    'What is the most important thing in the world? It is people, it is people, it is people',
    '/units/lessons/unit-5-lesson-2.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 5 Lesson 3: Resistance Networks - Global Indigenous Movements',
    'Be strong, be brave, be steadfast',
    '/units/lessons/unit-5-lesson-3.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 5 Lesson 4: Climate Justice Leadership - Indigenous Solutions for Global Challenges',
    'I am the environment, the environment is me',
    '/units/lessons/unit-5-lesson-4.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 5 Lesson 5: Building Solidarity - Action Plans for Global Indigenous Justice',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-5-lesson-5.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 6 Lesson 1: Visioning Rangatiratanga 2050',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-6-lesson-1.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 6 Lesson 2: Innovation through Whakapapa',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-6-lesson-2.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 6 Lesson 3: Digital Sovereignty & Youth Voice',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-6-lesson-3.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 6 Lesson 4: Community Leadership in Action',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-6-lesson-4.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 6 Lesson 5: Collective Action Project Launch',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-6-lesson-5.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 7 Lesson 1: AI Through Te Ao Māori Lens',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-7-lesson-1.html',
    'lesson',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 7 Lesson 2: AI Bias & Algorithmic Justice',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-7-lesson-2.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 7 Lesson 3: AI Ethics in Practice',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-7-lesson-3.html',
    'lesson',
    'cross-curricular',
    'Year 7-13',
    ARRAY['lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 7 Lesson 4: Tech Innovation - Culturally-Responsive Design for Māori Communities',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-7-lesson-4.html',
    'lesson',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 7 Lesson 5: Digital Futures - Envisioning Māori Digital Sovereignty in 2050',
    'Educational resource for NZ Curriculum',
    '/units/lessons/unit-7-lesson-5.html',
    'lesson',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'lesson'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

-- UNIT PLANS

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 1: Te Ao Māori - Cultural Identity & Knowledge Systems | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/unit-1-te-ao-maori.html',
    'unit-plan',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'unit-plan'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 2: Decolonized Aotearoa History - Centering Māori Agency, Resistance, and Sovereignty',
    'Educational resource for NZ Curriculum',
    '/units/unit-2-decolonized-history.html',
    'unit-plan',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'unit-plan'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 3: STEM Through Mātauranga Māori - Dual Knowledge Systems for Environmental Action',
    'Educational resource for NZ Curriculum',
    '/units/unit-3-stem-matauranga.html',
    'unit-plan',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'unit-plan'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 4: Economic Justice & Rangatiratanga - Alternative Economic Models | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/unit-4-economic-justice.html',
    'unit-plan',
    'cross-curricular',
    'Year 7-13',
    ARRAY['unit-plan'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 5: Global Indigenous Solidarity - Transnational Movements | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/units/unit-5-global-connections.html',
    'unit-plan',
    'cross-curricular',
    'Year 7-13',
    ARRAY['unit-plan'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 6: Future Rangatiratanga - Youth Leadership & Social Innovation',
    'Educational resource for NZ Curriculum',
    '/units/unit-6-future-rangatiratanga.html',
    'unit-plan',
    'cross-curricular',
    'Year 7-13',
    ARRAY['unit-plan'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Unit 7: Digital Technologies & AI Ethics - Navigating the Future of Artificial Intelligence',
    'Educational resource for NZ Curriculum',
    '/units/unit-7-digital-tech-ai-ethics.html',
    'unit-plan',
    'technology',
    'Year 7-13',
    ARRAY['unit-plan'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

-- GAMES

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Categories Challenge | Te Kete Ako Games',
    'Educational resource for NZ Curriculum',
    '/games/categories-fixed.html',
    'game',
    'cross-curricular',
    'Year 7-13',
    ARRAY['game'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Categories Challenge | Te Kete Ako Games',
    'Educational resource for NZ Curriculum',
    '/games/categories.html',
    'game',
    'cross-curricular',
    'Year 7-13',
    ARRAY['game'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Countdown Letters: Te Reo Māori',
    'Educational resource for NZ Curriculum',
    '/games/countdown-letters.html',
    'game',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'game'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'English Wordle',
    'Educational resource for NZ Curriculum',
    '/games/english-wordle.html',
    'game',
    'english',
    'Year 7-13',
    ARRAY['game'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Pāngarau Patterns Enhanced | Te Kete Ako Games',
    'Feel the fear and be brave anyway.',
    '/games/pangarau-patterns-enhanced.html',
    'game',
    'cross-curricular',
    'Year 7-13',
    ARRAY['game'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Pāngarau Patterns | Te Kete Ako Games',
    'Feel the fear and be brave anyway.',
    '/games/pangarau-patterns.html',
    'game',
    'cross-curricular',
    'Year 7-13',
    ARRAY['game'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Te Reo Māori Spelling Bee',
    'Educational resource for NZ Curriculum',
    '/games/spelling-bee.html',
    'game',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'game'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Te Reo Māori Wordle (6-Letter)',
    'Educational resource for NZ Curriculum',
    '/games/te-reo-wordle-6.html',
    'game',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'game'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Te Reo Māori Wordle',
    'Educational resource for NZ Curriculum',
    '/games/te-reo-wordle.html',
    'game',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori', 'game'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

-- VIDEO ACTIVITIES

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Video Activity: The Bastion Point Occupation',
    'Educational resource for NZ Curriculum',
    '/handouts/video-activities/bastion-point-video-activity.html',
    'video',
    'cross-curricular',
    'Year 7-13',
    ARRAY[],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Digital Sovereignty Multimedia Lab',
    'Educational resource for NZ Curriculum',
    '/handouts/video-activities/digital-sovereignty-multimedia-lab.html',
    'video',
    'technology',
    'Year 7-13',
    ARRAY[],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'MCP Enhanced Video Analysis: Economic Justice in Aotearoa | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/video-activities/economic-justice-documentary-analysis.html',
    'video',
    'cross-curricular',
    'Year 7-13',
    ARRAY[],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Video Activity: The Legends of Māui',
    'Educational resource for NZ Curriculum',
    '/handouts/video-activities/maui-video-activity.html',
    'video',
    'cross-curricular',
    'Year 7-13',
    ARRAY[],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Video Activity: The New Zealand Wars | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/video-activities/nz-wars-video-activity.html',
    'video',
    'cross-curricular',
    'Year 7-13',
    ARRAY[],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Video Activity: Prompt Engineering and AI Red Teaming | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/video-activities/prompt-engineering-video-activity.html',
    'video',
    'cross-curricular',
    'Year 7-13',
    ARRAY[],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'STEM + Mātauranga Māori Integration Lab | Mangakōtukutuku College',
    'Educational resource for NZ Curriculum',
    '/handouts/video-activities/stem-matauranga-integration-lab.html',
    'video',
    'te-reo-maori',
    'Year 7-13',
    ARRAY['māori'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

-- Y8 SYSTEMS RESOURCES

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Colonization Timeline',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/colonization-timeline.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Decolonization Commitment Template',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/decolonization-commitment-template.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Decolonization Today',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/decolonization-today.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Decolonized Design Template',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/decolonized-design-template.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Design a System Template',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/design-a-system-template.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Resource: Frayer Model for "System" | Y8 Systems',
    '"Mō te katoa te mātauranga"',
    '/y8-systems/resources/frayer-model-system.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Gallery Walk Statements',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/gallery-walk-statements.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Government Station Cards',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/government-station-cards.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Indigenous Feedback Framework',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/indigenous-feedback-framework.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Indigenous Governance Principles',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/indigenous-governance-principles.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Indigenous Systems Examples',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/indigenous-systems-examples.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Living Tiriti Examples',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/living-tiriti-examples.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Traditional Māori Governance Systems',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/maori-governance-systems.html',
    'handout',
    'te-reo-maori',
    'Year 8',
    ARRAY['māori', 'handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Defending Tino Rangatiratanga Case Studies',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/maori-political-action.html',
    'handout',
    'te-reo-maori',
    'Year 8',
    ARRAY['māori', 'handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Protest Case Studies',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/protest-case-studies.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'The Skate Park Campaign - Systems Thinking Case Study',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/skate-park-campaign.html',
    'handout',
    'technology',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Society Design Assessment Rubric',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/society-design-assessment-rubric.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Society Design Collaboration Framework',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/society-design-collaboration-framework.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable Resource: System Sorting Cards',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/system-sorting-cards.html',
    'handout',
    'cross-curricular',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Simplified Treaty Articles',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/treaty-articles.html',
    'handout',
    'arts',
    'Year 8',
    ARRAY['handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

INSERT INTO resources (title, description, path, type, subject, level, tags, is_active)
VALUES (
    'Printable: Te Tiriti Māori & English Texts Comparison',
    'Educational resource for NZ Curriculum',
    '/y8-systems/resources/treaty-two-texts.html',
    'handout',
    'te-reo-maori',
    'Year 8',
    ARRAY['māori', 'handout'],
    true
) ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    updated_at = NOW();

-- Indexing complete!

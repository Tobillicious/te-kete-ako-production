
INSERT INTO resources (title, description, path, type, subject, level, 
    cultural_elements, featured, tags, is_active)
VALUES (
    'Lighthouse Report',
    'A activity resource on Mathematics, English, Social Studies, Te Reo Māori',
    '/lighthouse-report.html',
    'activity',
    'Mathematics, English, Social Studies, Te Reo Māori',
    'All Levels',
    '{"has_whakatauk\u012b": true, "has_te_reo": true, "has_tikanga": false, "has_m\u0101tauranga": true, "cultural_score": 3}'::jsonb,
    True,
    ARRAY['activity', 'Mathematics'],
    true
)
ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    type = EXCLUDED.type,
    subject = EXCLUDED.subject,
    level = EXCLUDED.level,
    cultural_elements = EXCLUDED.cultural_elements,
    updated_at = NOW();


INSERT INTO resources (title, description, path, type, subject, level, 
    cultural_elements, featured, tags, is_active)
VALUES (
    'navigation-updates-arts',
    'A activity resource on Mathematics, English',
    '/navigation-updates-arts.html',
    'activity',
    'Mathematics, English',
    'Year 10',
    '{"has_whakatauk\u012b": false, "has_te_reo": false, "has_tikanga": false, "has_m\u0101tauranga": false, "cultural_score": 0}'::jsonb,
    False,
    ARRAY['activity', 'Mathematics'],
    true
)
ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    type = EXCLUDED.type,
    subject = EXCLUDED.subject,
    level = EXCLUDED.level,
    cultural_elements = EXCLUDED.cultural_elements,
    updated_at = NOW();


INSERT INTO resources (title, description, path, type, subject, level, 
    cultural_elements, featured, tags, is_active)
VALUES (
    'navigation-updates-senior',
    'A activity resource on Mathematics, English',
    '/navigation-updates-senior.html',
    'activity',
    'Mathematics, English',
    'Year 10',
    '{"has_whakatauk\u012b": false, "has_te_reo": true, "has_tikanga": false, "has_m\u0101tauranga": false, "cultural_score": 1}'::jsonb,
    False,
    ARRAY['activity', 'Mathematics'],
    true
)
ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    type = EXCLUDED.type,
    subject = EXCLUDED.subject,
    level = EXCLUDED.level,
    cultural_elements = EXCLUDED.cultural_elements,
    updated_at = NOW();


INSERT INTO resources (title, description, path, type, subject, level, 
    cultural_elements, featured, tags, is_active)
VALUES (
    'homepage-additions',
    'A activity resource on Science',
    '/homepage-additions.html',
    'activity',
    'Science',
    'All Levels',
    '{"has_whakatauk\u012b": false, "has_te_reo": true, "has_tikanga": false, "has_m\u0101tauranga": false, "cultural_score": 1}'::jsonb,
    False,
    ARRAY['activity', 'Science'],
    true
)
ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    type = EXCLUDED.type,
    subject = EXCLUDED.subject,
    level = EXCLUDED.level,
    cultural_elements = EXCLUDED.cultural_elements,
    updated_at = NOW();


INSERT INTO resources (title, description, path, type, subject, level, 
    cultural_elements, featured, tags, is_active)
VALUES (
    'INTEGRATION_HTML_SNIPPETS',
    'A activity resource on Mathematics, Science, English',
    '/INTEGRATION_HTML_SNIPPETS.html',
    'activity',
    'Mathematics, Science, English',
    'All Levels',
    '{"has_whakatauk\u012b": false, "has_te_reo": true, "has_tikanga": false, "has_m\u0101tauranga": false, "cultural_score": 1}'::jsonb,
    False,
    ARRAY['activity', 'Mathematics'],
    true
)
ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    type = EXCLUDED.type,
    subject = EXCLUDED.subject,
    level = EXCLUDED.level,
    cultural_elements = EXCLUDED.cultural_elements,
    updated_at = NOW();


INSERT INTO resources (title, description, path, type, subject, level, 
    cultural_elements, featured, tags, is_active)
VALUES (
    'NCEA Level 1 Literacy & Numeracy Must-Knows - Te Kete Ako',
    'A handout resource on Mathematics, English, Te Reo Māori',
    '/archive/redundant-duplicates-oct18/integrated-handouts/Year 11/ncea-level-1-literacy-and-numeracy-must-knows.html',
    'handout',
    'Mathematics, English, Te Reo Māori',
    'Year 11',
    '{"has_whakatauk\u012b": true, "has_te_reo": true, "has_tikanga": true, "has_m\u0101tauranga": true, "cultural_score": 4}'::jsonb,
    True,
    ARRAY['handout', 'Mathematics'],
    true
)
ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    type = EXCLUDED.type,
    subject = EXCLUDED.subject,
    level = EXCLUDED.level,
    cultural_elements = EXCLUDED.cultural_elements,
    updated_at = NOW();


INSERT INTO resources (title, description, path, type, subject, level, 
    cultural_elements, featured, tags, is_active)
VALUES (
    'Simple Login | Te Kete Ako',
    'Te Kete Ako - Award-winning educational platform integrating mātauranga Māori with contemporary learning',
    '/archive/redundant-duplicates-oct18/integrated-handouts/Year 2/login-simple.html',
    'handout',
    'Te Reo Māori',
    'All Levels',
    '{"has_whakatauk\u012b": true, "has_te_reo": true, "has_tikanga": false, "has_m\u0101tauranga": true, "cultural_score": 3}'::jsonb,
    True,
    ARRAY['handout', 'Te Reo Māori'],
    true
)
ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    type = EXCLUDED.type,
    subject = EXCLUDED.subject,
    level = EXCLUDED.level,
    cultural_elements = EXCLUDED.cultural_elements,
    updated_at = NOW();


INSERT INTO resources (title, description, path, type, subject, level, 
    cultural_elements, featured, tags, is_active)
VALUES (
    'Video Activity: The Legends of Māui | Te Kete Ako',
    'Te Kete Ako - Award-winning educational platform integrating mātauranga Māori with contemporary learning',
    '/archive/redundant-duplicates-oct18/integrated-handouts/Year 2/maui-video-activity.html',
    'handout',
    'Science, English, Te Reo Māori',
    'All Levels',
    '{"has_whakatauk\u012b": true, "has_te_reo": true, "has_tikanga": false, "has_m\u0101tauranga": true, "cultural_score": 3}'::jsonb,
    True,
    ARRAY['handout', 'Science'],
    true
)
ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    type = EXCLUDED.type,
    subject = EXCLUDED.subject,
    level = EXCLUDED.level,
    cultural_elements = EXCLUDED.cultural_elements,
    updated_at = NOW();


INSERT INTO resources (title, description, path, type, subject, level, 
    cultural_elements, featured, tags, is_active)
VALUES (
    'Te Kete Ako - Auth Test (8PM Ready)',
    'Te Kete Ako - Award-winning educational platform integrating mātauranga Māori with contemporary learning',
    '/archive/redundant-duplicates-oct18/integrated-handouts/Year 2/auth-test.html',
    'handout',
    'Te Reo Māori',
    'All Levels',
    '{"has_whakatauk\u012b": true, "has_te_reo": true, "has_tikanga": false, "has_m\u0101tauranga": true, "cultural_score": 3}'::jsonb,
    True,
    ARRAY['handout', 'Te Reo Māori'],
    true
)
ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    type = EXCLUDED.type,
    subject = EXCLUDED.subject,
    level = EXCLUDED.level,
    cultural_elements = EXCLUDED.cultural_elements,
    updated_at = NOW();


INSERT INTO resources (title, description, path, type, subject, level, 
    cultural_elements, featured, tags, is_active)
VALUES (
    'Elements of Art Handout',
    'Te Kete Ako - Award-winning educational platform integrating mātauranga Māori with contemporary learning',
    '/archive/redundant-duplicates-oct18/integrated-handouts/Year 5/elements-of-art-handout.html',
    'handout',
    'Te Reo Māori',
    'All Levels',
    '{"has_whakatauk\u012b": false, "has_te_reo": true, "has_tikanga": false, "has_m\u0101tauranga": true, "cultural_score": 2}'::jsonb,
    True,
    ARRAY['handout', 'Te Reo Māori'],
    true
)
ON CONFLICT (path) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    type = EXCLUDED.type,
    subject = EXCLUDED.subject,
    level = EXCLUDED.level,
    cultural_elements = EXCLUDED.cultural_elements,
    updated_at = NOW();

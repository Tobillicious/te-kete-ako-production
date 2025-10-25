-- METADATA EXTRACTION BATCH UPDATE
-- Generated: 1935 UPDATE statements
-- Impact: Makes resources discoverable via search/filter

BEGIN;


-- Update metadata for: YouTube Library Administration | Te Kete Ako | Te 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'YouTube Library Administration | Te Kete Ako | Te Kete Ako')
WHERE path = 'public/admin-youtube-library.html' OR path LIKE '%admin-youtube-library.html';


-- Update metadata for: Cultural Connection Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Connection Pathways | Te Kete Ako')
WHERE path = 'public/cultural-connection-pathways.html' OR path LIKE '%cultural-connection-pathways.html';


-- Update metadata for: Teacher Insights - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Insights - Te Kete Ako')
WHERE path = 'public/teacher-insights-dashboard.html' OR path LIKE '%teacher-insights-dashboard.html';


-- Update metadata for: GraphRAG Live Query Test | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Live Query Test | Te Kete Ako')
WHERE path = 'public/graphrag-test-query.html' OR path LIKE '%graphrag-test-query.html';


-- Update metadata for: Writing Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 11',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Writing Hub | Te Kete Ako')
WHERE path = 'public/writing-hub.html' OR path LIKE '%writing-hub.html';


-- Update metadata for: My Learning Journey | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Learning Journey | Te Kete Ako')
WHERE path = 'public/student-progress-tracker.html' OR path LIKE '%student-progress-tracker.html';


-- Update metadata for: Teaching Variants Library | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teaching Variants Library | Te Kete Ako')
WHERE path = 'public/teaching-variants-library.html' OR path LIKE '%teaching-variants-library.html';


-- Update metadata for: Te Kete Ako - EMERGENCY RECOVERY
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - EMERGENCY RECOVERY')
WHERE path = 'public/emergency-diagnostic.html' OR path LIKE '%emergency-diagnostic.html';


-- Update metadata for: Learning Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Learning Pathways | Te Kete Ako')
WHERE path = 'public/prerequisite-pathways.html' OR path LIKE '%prerequisite-pathways.html';


-- Update metadata for: AI Learning Assistant - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Learning Assistant - Te Kete Ako')
WHERE path = 'public/ai-assistant.html' OR path LIKE '%ai-assistant.html';


-- Update metadata for: 🧠 Central Intelligence Hub - Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🧠 Central Intelligence Hub - Te Kete Ako')
WHERE path = 'public/intelligence-hub.html' OR path LIKE '%intelligence-hub.html';


-- Update metadata for: Browse by Relationship Type | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Browse by Relationship Type | Te Kete Ako')
WHERE path = 'public/featured-by-relationship.html' OR path LIKE '%featured-by-relationship.html';


-- Update metadata for: Pathway Visualizer | GraphRAG | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Pathway Visualizer | GraphRAG | Te Kete Ako')
WHERE path = 'public/graphrag-pathway-visualizer.html' OR path LIKE '%graphrag-pathway-visualizer.html';


-- Update metadata for: Learning Pathways Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Learning Pathways Dashboard | Te Kete Ako')
WHERE path = 'public/learning-pathways-dashboard.html' OR path LIKE '%learning-pathways-dashboard.html';


-- Update metadata for: Massive Collection Hero
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Massive Collection Hero')
WHERE path = 'public/massive-collection-hero.html' OR path LIKE '%massive-collection-hero.html';


-- Update metadata for: All Handouts (1,000) | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'All Handouts (1,000) | Te Kete Ako')
WHERE path = 'public/handouts-complete.html' OR path LIKE '%handouts-complete.html';


-- Update metadata for: Learning Pathway Navigator | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Learning Pathway Navigator | Te Kete Ako')
WHERE path = 'public/learning-pathway-navigator.html' OR path LIKE '%learning-pathway-navigator.html';


-- Update metadata for: High Quality Collection | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'High Quality Collection | Te Kete Ako')
WHERE path = 'public/high-quality-collection.html' OR path LIKE '%high-quality-collection.html';


-- Update metadata for: Offline - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Offline - Te Kete Ako')
WHERE path = 'public/offline.html' OR path LIKE '%offline.html';


-- Update metadata for: 🔢 Māori Numeracy Adventures | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🔢 Māori Numeracy Adventures | Te Kete Ako')
WHERE path = 'public/maori-numeracy-adventures.html' OR path LIKE '%maori-numeracy-adventures.html';


-- Update metadata for: Do Now Activities | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Do Now Activities | Te Kete Ako')
WHERE path = 'public/activities.html' OR path LIKE '%activities.html';


-- Update metadata for: GraphRAG Query Dashboard - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Query Dashboard - Te Kete Ako')
WHERE path = 'public/graphrag-query-dashboard.html' OR path LIKE '%graphrag-query-dashboard.html';


-- Update metadata for: AI Teacher Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Teacher Dashboard | Te Kete Ako')
WHERE path = 'public/teacher-dashboard-ai.html' OR path LIKE '%teacher-dashboard-ai.html';


-- Update metadata for: Science Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Science Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/curriculum-science.html' OR path LIKE '%curriculum-science.html';


-- Update metadata for: Beta Testing Checklist | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Beta Testing Checklist | Te Kete Ako')
WHERE path = 'public/beta-testing-checklist.html' OR path LIKE '%beta-testing-checklist.html';


-- Update metadata for: Teacher Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Dashboard | Te Kete Ako')
WHERE path = 'public/teacher-dashboard-unified.html' OR path LIKE '%teacher-dashboard-unified.html';


-- Update metadata for: Year 8 Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Year 8 Hub | Te Kete Ako')
WHERE path = 'public/year-8-hub.html' OR path LIKE '%year-8-hub.html';


-- Update metadata for: GraphRAG Semantic Search | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Semantic Search | Te Kete Ako')
WHERE path = 'public/graphrag-search.html' OR path LIKE '%graphrag-search.html';


-- Update metadata for: Verify Email | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Verify Email | Te Kete Ako')
WHERE path = 'public/verify-email.html' OR path LIKE '%verify-email.html';


-- Update metadata for: Year 9 Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Year 9 Hub | Te Kete Ako')
WHERE path = 'public/year-9-hub.html' OR path LIKE '%year-9-hub.html';


-- Update metadata for: GraphRAG Intelligence Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Intelligence Hub | Te Kete Ako')
WHERE path = 'public/graphrag-hub.html' OR path LIKE '%graphrag-hub.html';


-- Update metadata for: Living Whakapapa Project | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Living Whakapapa Project | Te Kete Ako')
WHERE path = 'public/living-whakapapa.html' OR path LIKE '%living-whakapapa.html';


-- Update metadata for: My Submissions | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Submissions | Te Kete Ako')
WHERE path = 'public/my-submissions.html' OR path LIKE '%my-submissions.html';


-- Update metadata for: AI Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Hub | Te Kete Ako')
WHERE path = 'public/ai-hub.html' OR path LIKE '%ai-hub.html';


-- Update metadata for: 🧠 Agent Intelligence Dashboard | Real-Time Coordin
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🧠 Agent Intelligence Dashboard | Real-Time Coordination | Te Kete Ako')
WHERE path = 'public/agent-intelligence-dashboard.html' OR path LIKE '%agent-intelligence-dashboard.html';


-- Update metadata for: My Assignments | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Assignments | Te Kete Ako')
WHERE path = 'public/my-assignments.html' OR path LIKE '%my-assignments.html';


-- Update metadata for: AI Recommendations | GraphRAG | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Recommendations | GraphRAG | Te Kete Ako')
WHERE path = 'public/graphrag-ai-recommendations.html' OR path LIKE '%graphrag-ai-recommendations.html';


-- Update metadata for: Digital Technologies Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Technologies Hub | Te Kete Ako')
WHERE path = 'public/digital-technologies-hub.html' OR path LIKE '%digital-technologies-hub.html';


-- Update metadata for: Help & FAQ | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Help & FAQ | Te Kete Ako')
WHERE path = 'public/help.html' OR path LIKE '%help.html';


-- Update metadata for: Knowledge Graph Explorer | Te Kete Ako (Updated Oc
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Knowledge Graph Explorer | Te Kete Ako (Updated Oct 19 2025)')
WHERE path = 'public/knowledge-graph.html' OR path LIKE '%knowledge-graph.html';


-- Update metadata for: 🤖 Agent Dashboard - GraphRAG Intelligence
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🤖 Agent Dashboard - GraphRAG Intelligence')
WHERE path = 'public/agent-dashboard.html' OR path LIKE '%agent-dashboard.html';


-- Update metadata for: Resource Connections | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Resource Connections | Te Kete Ako')
WHERE path = 'public/resource-connections.html' OR path LIKE '%resource-connections.html';


-- Update metadata for: GLM Integration Test - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'GLM Integration Test - Te Kete Ako')
WHERE path = 'public/test-glm-integration.html' OR path LIKE '%test-glm-integration.html';


-- Update metadata for: Learning Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Learning Pathways | Te Kete Ako')
WHERE path = 'public/learning-pathways.html' OR path LIKE '%learning-pathways.html';


-- Update metadata for: Te Ao Māori Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Ao Māori Hub | Te Kete Ako')
WHERE path = 'public/te-ao-maori-hub.html' OR path LIKE '%te-ao-maori-hub.html';


-- Update metadata for: Health & Physical Education Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Health & Physical Education Hub | Te Kete Ako')
WHERE path = 'public/health-pe-hub.html' OR path LIKE '%health-pe-hub.html';


-- Update metadata for: Super-Connected Resources | GraphRAG Intelligence 
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Super-Connected Resources | GraphRAG Intelligence | Te Kete Ako')
WHERE path = 'public/super-connected-resources.html' OR path LIKE '%super-connected-resources.html';


-- Update metadata for: Cross-Subject Discovery | GraphRAG Intelligence | 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cross-Subject Discovery | GraphRAG Intelligence | Te Kete Ako')
WHERE path = 'public/cross-subject-discovery.html' OR path LIKE '%cross-subject-discovery.html';


-- Update metadata for: Other Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Other Resources | Te Kete Ako')
WHERE path = 'public/other-resources.html' OR path LIKE '%other-resources.html';


-- Update metadata for: Forgot Password | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Forgot Password | Te Kete Ako')
WHERE path = 'public/forgot-password.html' OR path LIKE '%forgot-password.html';


-- Update metadata for: Intelligence System Test - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Intelligence System Test - Te Kete Ako')
WHERE path = 'public/test-intelligence-system.html' OR path LIKE '%test-intelligence-system.html';


-- Update metadata for: Browse by Concept | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Browse by Concept | Te Kete Ako')
WHERE path = 'public/browse-by-concept.html' OR path LIKE '%browse-by-concept.html';


-- Update metadata for: Integrated Lessons Library | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Integrated Lessons Library | Te Kete Ako')
WHERE path = 'public/integrated-lessons-index.html' OR path LIKE '%integrated-lessons-index.html';


-- Update metadata for: About Te Kete Ako | Educational Resources Platform
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'About Te Kete Ako | Educational Resources Platform')
WHERE path = 'public/about.html' OR path LIKE '%about.html';


-- Update metadata for: Curriculum: Arts | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Arts | Te Kete Ako')
WHERE path = 'public/curriculum-arts.html' OR path LIKE '%curriculum-arts.html';


-- Update metadata for: GraphRAG Science Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Science Dashboard | Te Kete Ako')
WHERE path = 'public/graphrag-science-dashboard.html' OR path LIKE '%graphrag-science-dashboard.html';


-- Update metadata for: Decolonized Assessment Framework - Honoring Dual K
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Decolonized Assessment Framework - Honoring Dual Knowledge Systems | Te Kete Ako')
WHERE path = 'public/decolonized-assessment-framework.html' OR path LIKE '%decolonized-assessment-framework.html';


-- Update metadata for: Privacy Policy | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Privacy Policy | Te Kete Ako')
WHERE path = 'public/privacy-policy.html' OR path LIKE '%privacy-policy.html';


-- Update metadata for: Te Reo Māori Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Hub | Te Kete Ako')
WHERE path = 'public/te-reo-maori-hub.html' OR path LIKE '%te-reo-maori-hub.html';


-- Update metadata for: 🌿 Cultural Enrichment Review | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🌿 Cultural Enrichment Review | Te Kete Ako')
WHERE path = 'public/cultural-enrichment-review.html' OR path LIKE '%cultural-enrichment-review.html';


-- Update metadata for: 🤖 AI Coordination Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🤖 AI Coordination Dashboard | Te Kete Ako')
WHERE path = 'public/ai-coordination-dashboard.html' OR path LIKE '%ai-coordination-dashboard.html';


-- Update metadata for: Subject Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Subject Dashboard | Te Kete Ako')
WHERE path = 'public/subject-dashboard.html' OR path LIKE '%subject-dashboard.html';


-- Update metadata for: Social Studies | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Social Studies | Te Kete Ako')
WHERE path = 'public/social-studies.html' OR path LIKE '%social-studies.html';


-- Update metadata for: Contact Te Kete Ako | Support & Feedback
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Contact Te Kete Ako | Support & Feedback')
WHERE path = 'public/contact.html' OR path LIKE '%contact.html';


-- Update metadata for: Cultural Excellence Network | 2,400 GraphRAG Conne
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Excellence Network | 2,400 GraphRAG Connections | Te Kete Ako')
WHERE path = 'public/cultural-excellence-network.html' OR path LIKE '%cultural-excellence-network.html';


-- Update metadata for: All Lessons (1,000) | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'All Lessons (1,000) | Te Kete Ako')
WHERE path = 'public/lessons-complete.html' OR path LIKE '%lessons-complete.html';


-- Update metadata for: Cache Test - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Cache Test - Te Kete Ako')
WHERE path = 'public/cache-test.html' OR path LIKE '%cache-test.html';


-- Update metadata for: 🔮 Predictive Content Generator | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🔮 Predictive Content Generator | Te Kete Ako')
WHERE path = 'public/predictive-generator.html' OR path LIKE '%predictive-generator.html';


-- Update metadata for: Cultural Excellence Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Excellence Dashboard | Te Kete Ako')
WHERE path = 'public/cultural-excellence-dashboard.html' OR path LIKE '%cultural-excellence-dashboard.html';


-- Update metadata for: Orphaned Resources Integration Dashboard | Te Kete
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Orphaned Resources Integration Dashboard | Te Kete Ako')
WHERE path = 'public/orphaned-resources-integrator.html' OR path LIKE '%orphaned-resources-integrator.html';


-- Update metadata for: GraphRAG Relationship Builder | Add Missing Connec
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Relationship Builder | Add Missing Connections | Te Kete Ako')
WHERE path = 'public/graphrag-relationship-builder.html' OR path LIKE '%graphrag-relationship-builder.html';


-- Update metadata for: Cross-Subject Discovery Visualization | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cross-Subject Discovery Visualization | Te Kete Ako')
WHERE path = 'public/cross-subject-visualization.html' OR path LIKE '%cross-subject-visualization.html';


-- Update metadata for: Browse All Lessons | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Browse All Lessons | Te Kete Ako')
WHERE path = 'public/browse-lessons.html' OR path LIKE '%browse-lessons.html';


-- Update metadata for: Student Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Student Dashboard | Te Kete Ako')
WHERE path = 'public/student-dashboard.html' OR path LIKE '%student-dashboard.html';


-- Update metadata for: Teacher Quick Start Guide
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Quick Start Guide')
WHERE path = 'public/TEACHER-QUICK-START-GUIDE.html' OR path LIKE '%TEACHER-QUICK-START-GUIDE.html';


-- Update metadata for: My Assignments | Teacher Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Assignments | Teacher Dashboard | Te Kete Ako')
WHERE path = 'public/teacher-assignments.html' OR path LIKE '%teacher-assignments.html';


-- Update metadata for: Pricing - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Pricing - Te Kete Ako')
WHERE path = 'public/pricing.html' OR path LIKE '%pricing.html';


-- Update metadata for: Cultural Resources with Whakataukī | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Resources with Whakataukī | Te Kete Ako')
WHERE path = 'public/cultural-resources-showcase.html' OR path LIKE '%cultural-resources-showcase.html';


-- Update metadata for: 🌿 Māori Teacher AI Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🌿 Māori Teacher AI Dashboard | Te Kete Ako')
WHERE path = 'public/teacher-ai-dashboard-maori.html' OR path LIKE '%teacher-ai-dashboard-maori.html';


-- Update metadata for: Integration Tools Showcase | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Integration Tools Showcase | Te Kete Ako')
WHERE path = 'public/integration-tools-showcase.html' OR path LIKE '%integration-tools-showcase.html';


-- Update metadata for: Sitemap
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Sitemap')
WHERE path = 'public/sitemap.html' OR path LIKE '%sitemap.html';


-- Update metadata for: Platform Health | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Platform Health | Te Kete Ako')
WHERE path = 'public/platform-health.html' OR path LIKE '%platform-health.html';


-- Update metadata for: Platforms | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Platforms | Te Kete Ako')
WHERE path = 'public/platforms.html' OR path LIKE '%platforms.html';


-- Update metadata for: 📚 Mangakotukutuku Foundational Learning | Te Kete 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '📚 Mangakotukutuku Foundational Learning | Te Kete Ako')
WHERE path = 'public/foundational-literacy-platform.html' OR path LIKE '%foundational-literacy-platform.html';


-- Update metadata for: 🎓 Teacher Feedback Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🎓 Teacher Feedback Hub | Te Kete Ako')
WHERE path = 'public/teacher-feedback-hub.html' OR path LIKE '%teacher-feedback-hub.html';


-- Update metadata for: Mathematics and Statistics Curriculum Alignment | 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Mathematics and Statistics Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/curriculum-mathematics.html' OR path LIKE '%curriculum-mathematics.html';


-- Update metadata for: 📅 Weekly Planner - GraphRAG Powered | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '📅 Weekly Planner - GraphRAG Powered | Te Kete Ako')
WHERE path = 'public/teacher-planner.html' OR path LIKE '%teacher-planner.html';


-- Update metadata for: Beta Teacher Feedback | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Beta Teacher Feedback | Te Kete Ako')
WHERE path = 'public/beta-feedback.html' OR path LIKE '%beta-feedback.html';


-- Update metadata for: KAMAR Integration - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'KAMAR Integration - Te Kete Ako')
WHERE path = 'public/kamar-integration-dashboard.html' OR path LIKE '%kamar-integration-dashboard.html';


-- Update metadata for: 🌟 Whakataukī Wisdom Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🌟 Whakataukī Wisdom Hub | Te Kete Ako')
WHERE path = 'public/whakatauaki-wisdom.html' OR path LIKE '%whakatauaki-wisdom.html';


-- Update metadata for: Wordsearch Design Demo - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Wordsearch Design Demo - Te Kete Ako')
WHERE path = 'public/wordsearch-demo.html' OR path LIKE '%wordsearch-demo.html';


-- Update metadata for: Cache Bust Test - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Cache Bust Test - Te Kete Ako')
WHERE path = 'public/cache-bust-test.html' OR path LIKE '%cache-bust-test.html';


-- Update metadata for: Terms of Service - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Terms of Service - Te Kete Ako')
WHERE path = 'public/terms.html' OR path LIKE '%terms.html';


-- Update metadata for: Project Assessment Rubric | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Project Assessment Rubric | Te Kete Ako')
WHERE path = 'public/assessment-rubric.html' OR path LIKE '%assessment-rubric.html';


-- Update metadata for: YouTube Educational Library | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'YouTube Educational Library | Te Kete Ako')
WHERE path = 'public/youtube-library.html' OR path LIKE '%youtube-library.html';


-- Update metadata for: Register | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Register | Te Kete Ako')
WHERE path = 'public/register.html' OR path LIKE '%register.html';


-- Update metadata for: Server Error - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Server Error - Te Kete Ako')
WHERE path = 'public/500.html' OR path LIKE '%500.html';


-- Update metadata for: 📝 Lesson Reflection Tool | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '📝 Lesson Reflection Tool | Te Kete Ako')
WHERE path = 'public/teacher-reflection.html' OR path LIKE '%teacher-reflection.html';


-- Update metadata for: Platform Architecture | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Platform Architecture | Te Kete Ako')
WHERE path = 'public/platform-architecture.html' OR path LIKE '%platform-architecture.html';


-- Update metadata for: Project Submission | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Project Submission | Te Kete Ako')
WHERE path = 'public/project-submission.html' OR path LIKE '%project-submission.html';


-- Update metadata for: Page Not Found - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Page Not Found - Te Kete Ako')
WHERE path = 'public/404.html' OR path LIKE '%404.html';


-- Update metadata for: Handouts | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handouts | Te Kete Ako')
WHERE path = 'public/handouts.html' OR path LIKE '%handouts.html';


-- Update metadata for: 🔍 Similar Resources Finder | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🔍 Similar Resources Finder | Te Kete Ako')
WHERE path = 'public/similar-resources.html' OR path LIKE '%similar-resources.html';


-- Update metadata for: Te Kete Ako | Educational Resources Honoring Te Ao
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Educational Resources Honoring Te Ao Māori')
WHERE path = 'public/index-bloated-backup.html' OR path LIKE '%index-bloated-backup.html';


-- Update metadata for: Interactive Curriculum Browser | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Interactive Curriculum Browser | Te Kete Ako')
WHERE path = 'public/curriculum-v2.html' OR path LIKE '%curriculum-v2.html';


-- Update metadata for: Reading Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Reading Hub | Te Kete Ako')
WHERE path = 'public/reading-hub.html' OR path LIKE '%reading-hub.html';


-- Update metadata for: Subject Areas | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Subject Areas | Te Kete Ako')
WHERE path = 'public/subjects.html' OR path LIKE '%subjects.html';


-- Update metadata for: Reset Password | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Reset Password | Te Kete Ako')
WHERE path = 'public/reset-password.html' OR path LIKE '%reset-password.html';


-- Update metadata for: Teaching Variants Demo - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teaching Variants Demo - Te Kete Ako')
WHERE path = 'public/teaching-variants-demo.html' OR path LIKE '%teaching-variants-demo.html';


-- Update metadata for: Login | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Login | Te Kete Ako')
WHERE path = 'public/login.html' OR path LIKE '%login.html';


-- Update metadata for: Learning Pathways Explorer | GraphRAG | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Learning Pathways Explorer | GraphRAG | Te Kete Ako')
WHERE path = 'public/graphrag-learning-pathways.html' OR path LIKE '%graphrag-learning-pathways.html';


-- Update metadata for: Teacher Analytics Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Analytics Guide | Te Kete Ako')
WHERE path = 'public/teacher-guide.html' OR path LIKE '%teacher-guide.html';


-- Update metadata for: Cultural Threads | GraphRAG Cultural Intelligence 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Threads | GraphRAG Cultural Intelligence | Te Kete Ako')
WHERE path = 'public/cultural-threads.html' OR path LIKE '%cultural-threads.html';


-- Update metadata for: Analytics Dashboard - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Analytics Dashboard - Te Kete Ako')
WHERE path = 'public/analytics-dashboard.html' OR path LIKE '%analytics-dashboard.html';


-- Update metadata for: Beta Teacher Recruitment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Beta Teacher Recruitment | Te Kete Ako')
WHERE path = 'public/beta-teacher-recruitment.html' OR path LIKE '%beta-teacher-recruitment.html';


-- Update metadata for: Resource Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Resource Hub | Te Kete Ako')
WHERE path = 'public/resource-hub.html' OR path LIKE '%resource-hub.html';


-- Update metadata for: Orphans Dashboard - GraphRAG Hidden Gems | Te Kete
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Orphans Dashboard - GraphRAG Hidden Gems | Te Kete Ako')
WHERE path = 'public/orphans-dashboard.html' OR path LIKE '%orphans-dashboard.html';


-- Update metadata for: Advanced Search - 8,037 Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Advanced Search - 8,037 Resources | Te Kete Ako')
WHERE path = 'public/advanced-search.html' OR path LIKE '%advanced-search.html';


-- Update metadata for: GraphRAG Control Center - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Control Center - Te Kete Ako')
WHERE path = 'public/graphrag-control-center.html' OR path LIKE '%graphrag-control-center.html';


-- Update metadata for: 🛤️ Learning Pathways Visualizer | GraphRAG Powered
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🛤️ Learning Pathways Visualizer | GraphRAG Powered | Te Kete Ako')
WHERE path = 'public/learning-pathways-visualizer.html' OR path LIKE '%learning-pathways-visualizer.html';


-- Update metadata for: Te Kete Ako Dashboard | Your Teaching Resources
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako Dashboard | Your Teaching Resources')
WHERE path = 'public/dashboard.html' OR path LIKE '%dashboard.html';


-- Update metadata for: Student Success Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Student Success Hub | Te Kete Ako')
WHERE path = 'public/student-success-hub.html' OR path LIKE '%student-success-hub.html';


-- Update metadata for: Orphaned Excellence | Hidden Gems | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Orphaned Excellence | Hidden Gems | Te Kete Ako')
WHERE path = 'public/graphrag-orphaned-excellence.html' OR path LIKE '%graphrag-orphaned-excellence.html';


-- Update metadata for: Prerequisite Chain Explorer | GraphRAG Intelligenc
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Prerequisite Chain Explorer | GraphRAG Intelligence | Te Kete Ako (Updated Oct 19 2025)')
WHERE path = 'public/graphrag-prerequisite-explorer.html' OR path LIKE '%graphrag-prerequisite-explorer.html';


-- Update metadata for: Interactive Knowledge Graph | GraphRAG | Te Kete A
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Interactive Knowledge Graph | GraphRAG | Te Kete Ako')
WHERE path = 'public/graphrag-knowledge-graph-viz.html' OR path LIKE '%graphrag-knowledge-graph-viz.html';


-- Update metadata for: 🔐 Unified Auth System | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🔐 Unified Auth System | Te Kete Ako')
WHERE path = 'public/auth-unified.html' OR path LIKE '%auth-unified.html';


-- Update metadata for: Perfect Learning Pathways | 594+ Lessons Mapped | 
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Perfect Learning Pathways | 594+ Lessons Mapped | Te Kete Ako (Updated Oct 19 2025)')
WHERE path = 'public/perfect-learning-pathways.html' OR path LIKE '%perfect-learning-pathways.html';


-- Update metadata for: 🔍 Discovery Tools | GraphRAG-Powered Intelligence 
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🔍 Discovery Tools | GraphRAG-Powered Intelligence | Te Kete Ako')
WHERE path = 'public/discovery-tools.html' OR path LIKE '%discovery-tools.html';


-- Update metadata for: Simple Login | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Simple Login | Te Kete Ako')
WHERE path = 'public/login-simple.html' OR path LIKE '%login-simple.html';


-- Update metadata for: Science Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Science Hub | Te Kete Ako')
WHERE path = 'public/science-hub.html' OR path LIKE '%science-hub.html';


-- Update metadata for: Authentication - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Authentication - Te Kete Ako')
WHERE path = 'public/auth-callback.html' OR path LIKE '%auth-callback.html';


-- Update metadata for: GraphRAG Knowledge Graph Visualization | Te Kete A
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Knowledge Graph Visualization | Te Kete Ako')
WHERE path = 'public/graphrag-visual-demo.html' OR path LIKE '%graphrag-visual-demo.html';


-- Update metadata for: YouTube Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'YouTube Resources | Te Kete Ako')
WHERE path = 'public/youtube.html' OR path LIKE '%youtube.html';


-- Update metadata for: English | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'English | Te Kete Ako')
WHERE path = 'public/english.html' OR path LIKE '%english.html';


-- Update metadata for: Hidden Gems | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Hidden Gems | Te Kete Ako')
WHERE path = 'public/hidden-gems.html' OR path LIKE '%hidden-gems.html';


-- Update metadata for: ✍️ Writers Toolkit - 18-Step Mastery Path | Te Ket
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '✍️ Writers Toolkit - 18-Step Mastery Path | Te Kete Ako')
WHERE path = 'public/writers-toolkit-hub.html' OR path LIKE '%writers-toolkit-hub.html';


-- Update metadata for: Resource Detail Template | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Resource Detail Template | Te Kete Ako')
WHERE path = 'public/resource-detail-template.html' OR path LIKE '%resource-detail-template.html';


-- Update metadata for: Complete Curriculum | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Complete Curriculum | Te Kete Ako')
WHERE path = 'public/curriculum-index.html' OR path LIKE '%curriculum-index.html';


-- Update metadata for: Performance Dashboard - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Performance Dashboard - Te Kete Ako')
WHERE path = 'public/performance-dashboard.html' OR path LIKE '%performance-dashboard.html';


-- Update metadata for: Integrated Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Integrated Resources | Te Kete Ako')
WHERE path = 'public/integrated-resources-index.html' OR path LIKE '%integrated-resources-index.html';


-- Update metadata for: 🤖 GraphRAG Generator - Auto-Create Content | Te Ke
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🤖 GraphRAG Generator - Auto-Create Content | Te Kete Ako')
WHERE path = 'public/graphrag-generator.html' OR path LIKE '%graphrag-generator.html';


-- Update metadata for: Cultural Treasures | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Treasures | Te Kete Ako')
WHERE path = 'public/cultural-treasures.html' OR path LIKE '%cultural-treasures.html';


-- Update metadata for: 💎 377 Integrated Lessons - Hidden Treasure | Te Ke
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '💎 377 Integrated Lessons - Hidden Treasure | Te Kete Ako')
WHERE path = 'public/integrated-lessons-showcase.html' OR path LIKE '%integrated-lessons-showcase.html';


-- Update metadata for: 🌿 Cultural Learning Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🌿 Cultural Learning Pathways | Te Kete Ako')
WHERE path = 'public/cultural-learning-pathways.html' OR path LIKE '%cultural-learning-pathways.html';


-- Update metadata for: Register | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Register | Te Kete Ako')
WHERE path = 'public/register-simple.html' OR path LIKE '%register-simple.html';


-- Update metadata for: 💡 Innovation Showcase | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '💡 Innovation Showcase | Te Kete Ako')
WHERE path = 'public/innovation-showcase.html' OR path LIKE '%innovation-showcase.html';


-- Update metadata for: NZ Curriculum Browser | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum Browser | Te Kete Ako')
WHERE path = 'public/nz-curriculum-browser.html' OR path LIKE '%nz-curriculum-browser.html';


-- Update metadata for: Teaching Options Library | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teaching Options Library | Te Kete Ako')
WHERE path = 'public/teaching-options-library.html' OR path LIKE '%teaching-options-library.html';


-- Update metadata for: 🧠 GraphRAG Brain - Live Intelligence | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🧠 GraphRAG Brain - Live Intelligence | Te Kete Ako')
WHERE path = 'public/graphrag-brain.html' OR path LIKE '%graphrag-brain.html';


-- Update metadata for: Unit Structure Explorer | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit Structure Explorer | Te Kete Ako')
WHERE path = 'public/unit-structure-explorer.html' OR path LIKE '%unit-structure-explorer.html';


-- Update metadata for: 🌉 Cross-Curricular Bridges | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🌉 Cross-Curricular Bridges | Te Kete Ako')
WHERE path = 'public/cross-curricular-bridges.html' OR path LIKE '%cross-curricular-bridges.html';


-- Update metadata for: Cultural Pathways | Te Ao Māori Through All Learni
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Pathways | Te Ao Māori Through All Learning | Te Kete Ako')
WHERE path = 'public/cultural-pathways.html' OR path LIKE '%cultural-pathways.html';


-- Update metadata for: Te Kete Ako | Educational Resources Honoring Te Ao
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Educational Resources Honoring Te Ao Māori')
WHERE path = 'public/index-backup-old-complex.html' OR path LIKE '%index-backup-old-complex.html';


-- Update metadata for: English/Literacy Progression Framework - Culturall
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'English/Literacy Progression Framework - Culturally Responsive Communication | Mangakōtukutuku College')
WHERE path = 'public/english-literacy-progression-framework.html' OR path LIKE '%english-literacy-progression-framework.html';


-- Update metadata for: GraphRAG Discovery Hub | AI-Powered Knowledge Navi
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Discovery Hub | AI-Powered Knowledge Navigation | Te Kete Ako')
WHERE path = 'public/graphrag-discovery-hub.html' OR path LIKE '%graphrag-discovery-hub.html';


-- Update metadata for: 🌿 Cultural Excellence Collection | 199 High-Integr
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🌿 Cultural Excellence Collection | 199 High-Integration Resources | Te Kete Ako')
WHERE path = 'public/cultural-excellence-collection.html' OR path LIKE '%cultural-excellence-collection.html';


-- Update metadata for: Excellence Clusters | 2,300 High-Quality Connectio
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Excellence Clusters | 2,300 High-Quality Connections | Te Kete Ako')
WHERE path = 'public/excellence-clusters.html' OR path LIKE '%excellence-clusters.html';


-- Update metadata for: Learning Pathways Builder | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Learning Pathways Builder | Te Kete Ako')
WHERE path = 'public/learning-pathways-builder.html' OR path LIKE '%learning-pathways-builder.html';


-- Update metadata for: Teacher Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Dashboard | Te Kete Ako')
WHERE path = 'public/teacher-dashboard.html' OR path LIKE '%teacher-dashboard.html';


-- Update metadata for: Unit Plans | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit Plans | Te Kete Ako')
WHERE path = 'public/units.html' OR path LIKE '%units.html';


-- Update metadata for: English Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'English Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/curriculum-english.html' OR path LIKE '%curriculum-english.html';


-- Update metadata for: Discover Orphans
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Discover Orphans')
WHERE path = 'public/orphans.html' OR path LIKE '%orphans.html';


-- Update metadata for: Enterprise Admin Dashboard - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Enterprise Admin Dashboard - Te Kete Ako')
WHERE path = 'public/enterprise-admin-dashboard.html' OR path LIKE '%enterprise-admin-dashboard.html';


-- Update metadata for: 🤖 DeepSeek + GraphRAG Terminal | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🤖 DeepSeek + GraphRAG Terminal | Te Kete Ako')
WHERE path = 'public/deepseek-graphrag-terminal.html' OR path LIKE '%deepseek-graphrag-terminal.html';


-- Update metadata for: Visual Learning Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Visual Learning Pathways | Te Kete Ako')
WHERE path = 'public/learning-pathways-visual.html' OR path LIKE '%learning-pathways-visual.html';


-- Update metadata for: 📊 GraphRAG Analytics Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '📊 GraphRAG Analytics Dashboard | Te Kete Ako')
WHERE path = 'public/graphrag-analytics-dashboard.html' OR path LIKE '%graphrag-analytics-dashboard.html';


-- Update metadata for: Unit Hub | Critical Thinking Skills: Media Literac
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit Hub | Critical Thinking Skills: Media Literacy & Information Analysis | Te Kete Ako - Postcolonial Social Studies')
WHERE path = 'public/critical-thinking-unit.html' OR path LIKE '%critical-thinking-unit.html';


-- Update metadata for: Getting Started | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Getting Started | Te Kete Ako')
WHERE path = 'public/getting-started.html' OR path LIKE '%getting-started.html';


-- Update metadata for: Teacher Dashboard | Te Kete Ako - Principal Demo O
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Dashboard | Te Kete Ako - Principal Demo Oct 22')
WHERE path = 'public/teacher-demo-dashboard.html' OR path LIKE '%teacher-demo-dashboard.html';


-- Update metadata for: GraphRAG Optimization Dashboard - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Optimization Dashboard - Te Kete Ako')
WHERE path = 'public/graphrag-optimization-dashboard.html' OR path LIKE '%graphrag-optimization-dashboard.html';


-- Update metadata for: Lesson Template: [Te Reo Name] - [English Name] | 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Template: [Te Reo Name] - [English Name] | Mangakōtukutuku College')
WHERE path = 'public/lesson-template.html' OR path LIKE '%lesson-template.html';


-- Update metadata for: Digital Pūrākau | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Pūrākau | Te Kete Ako')
WHERE path = 'public/digital-purakau.html' OR path LIKE '%digital-purakau.html';


-- Update metadata for: NZ Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/curriculum-alignment.html' OR path LIKE '%curriculum-alignment.html';


-- Update metadata for: Checkout - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Checkout - Te Kete Ako')
WHERE path = 'public/checkout.html' OR path LIKE '%checkout.html';


-- Update metadata for: Cross-Curricular Discovery Engine | Te Kete Ako (U
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cross-Curricular Discovery Engine | Te Kete Ako (Updated Oct 19 2025)')
WHERE path = 'public/cross-curricular-discovery.html' OR path LIKE '%cross-curricular-discovery.html';


-- Update metadata for: Q100 Excellence Collection | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Q100 Excellence Collection | Te Kete Ako')
WHERE path = 'public/q100-excellence-collection.html' OR path LIKE '%q100-excellence-collection.html';


-- Update metadata for: Featured Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Featured Resources | Te Kete Ako')
WHERE path = 'public/featured-resources.html' OR path LIKE '%featured-resources.html';


-- Update metadata for: 📊 Subject Excellence Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '📊 Subject Excellence Dashboard | Te Kete Ako')
WHERE path = 'public/subject-excellence-dashboard.html' OR path LIKE '%subject-excellence-dashboard.html';


-- Update metadata for: Social Studies Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Social Studies Hub | Te Kete Ako')
WHERE path = 'public/social-studies-hub.html' OR path LIKE '%social-studies-hub.html';


-- Update metadata for: 🔍 Site Audit Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🔍 Site Audit Dashboard | Te Kete Ako')
WHERE path = 'public/site-audit-dashboard.html' OR path LIKE '%site-audit-dashboard.html';


-- Update metadata for: Social Sciences Progression Framework - Years 7-13
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Social Sciences Progression Framework - Years 7-13 | Mangakōtukutuku College')
WHERE path = 'public/social-sciences-progression-framework.html' OR path LIKE '%social-sciences-progression-framework.html';


-- Update metadata for: 🦅 Te Kete Ako - Complete Intelligence System
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🦅 Te Kete Ako - Complete Intelligence System')
WHERE path = 'public/complete-system-showcase.html' OR path LIKE '%complete-system-showcase.html';


-- Update metadata for: Beta Tester Onboarding - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Beta Tester Onboarding - Te Kete Ako')
WHERE path = 'public/beta-onboarding-email.html' OR path LIKE '%beta-onboarding-email.html';


-- Update metadata for: Welcome to Te Kete Ako | Educational Resources for
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Welcome to Te Kete Ako | Educational Resources for New Zealand')
WHERE path = 'public/welcome.html' OR path LIKE '%welcome.html';


-- Update metadata for: Unit Plans | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit Plans | Te Kete Ako')
WHERE path = 'public/unit-plans.html' OR path LIKE '%unit-plans.html';


-- Update metadata for: Similar Resources Finder | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Similar Resources Finder | Te Kete Ako')
WHERE path = 'public/similar-resources-finder.html' OR path LIKE '%similar-resources-finder.html';


-- Update metadata for: Te Ao Māori | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Ao Māori | Te Kete Ako')
WHERE path = 'public/te-ao-maori.html' OR path LIKE '%te-ao-maori.html';


-- Update metadata for: Excellence Showcase - 221 Cultural Gems | Te Kete 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Excellence Showcase - 221 Cultural Gems | Te Kete Ako')
WHERE path = 'public/excellence-showcase.html' OR path LIKE '%excellence-showcase.html';


-- Update metadata for: Te Reo Wordle - Function Test
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Wordle - Function Test')
WHERE path = 'public/test-wordle-functions.html' OR path LIKE '%test-wordle-functions.html';


-- Update metadata for: 🏆 Gold Collection - Te Kete Ako's Finest Resources
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🏆 Gold Collection - Te Kete Ako''s Finest Resources')
WHERE path = 'public/gold-collection.html' OR path LIKE '%gold-collection.html';


-- Update metadata for: Your Personalized Learning Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Your Personalized Learning Dashboard | Te Kete Ako')
WHERE path = 'public/personalized-learning.html' OR path LIKE '%personalized-learning.html';


-- Update metadata for: Teaching Tools & Platforms | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teaching Tools & Platforms | Te Kete Ako')
WHERE path = 'public/tools.html' OR path LIKE '%tools.html';


-- Update metadata for: ✨ Content Constellation - Subject Maps | Te Kete A
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '✨ Content Constellation - Subject Maps | Te Kete Ako')
WHERE path = 'public/content-constellation.html' OR path LIKE '%content-constellation.html';


-- Update metadata for: Teacher Quick-Start Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Quick-Start Guide | Te Kete Ako')
WHERE path = 'public/TEACHER-QUICKSTART-GUIDE.html' OR path LIKE '%TEACHER-QUICKSTART-GUIDE.html';


-- Update metadata for: Curriculum: Technology | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Technology | Te Kete Ako')
WHERE path = 'public/curriculum-technology.html' OR path LIKE '%curriculum-technology.html';


-- Update metadata for: Te Kete Ako | World's First AI-Enhanced Cultural E
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | World''s First AI-Enhanced Cultural Educational Platform')
WHERE path = 'public/index-new.html' OR path LIKE '%index-new.html';


-- Update metadata for: Te Kete Ako | World-Class Educational Resources Ho
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | World-Class Educational Resources Honoring Te Ao Māori')
WHERE path = 'public/index-premium.html' OR path LIKE '%index-premium.html';


-- Update metadata for: Te Kete Ako - Comprehensive Site Map
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Comprehensive Site Map')
WHERE path = 'public/sitemap-enhanced.html' OR path LIKE '%sitemap-enhanced.html';


-- Update metadata for: Browse by Topic | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Browse by Topic | Te Kete Ako')
WHERE path = 'public/browse-by-topic.html' OR path LIKE '%browse-by-topic.html';


-- Update metadata for: Classroom Leaderboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Classroom Leaderboard | Te Kete Ako')
WHERE path = 'public/classroom-leaderboard.html' OR path LIKE '%classroom-leaderboard.html';


-- Update metadata for: Browse All Units | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Browse All Units | Te Kete Ako')
WHERE path = 'public/browse-units.html' OR path LIKE '%browse-units.html';


-- Update metadata for: Search | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Search | Te Kete Ako')
WHERE path = 'public/search.html' OR path LIKE '%search.html';


-- Update metadata for: GraphRAG Pathway Explorer
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Pathway Explorer')
WHERE path = 'public/graphrag-pathway-explorer.html' OR path LIKE '%graphrag-pathway-explorer.html';


-- Update metadata for: 🌿 Vision for Aotearoa Education | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🌿 Vision for Aotearoa Education | Te Kete Ako')
WHERE path = 'public/vision.html' OR path LIKE '%vision.html';


-- Update metadata for: Complete Teaching Variants Browser | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Complete Teaching Variants Browser | Te Kete Ako')
WHERE path = 'public/all-teaching-variants-browser.html' OR path LIKE '%all-teaching-variants-browser.html';


-- Update metadata for: Science × Mathematics Integration Hub | 400+ Graph
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Science × Mathematics Integration Hub | 400+ GraphRAG Connections | Te Kete Ako')
WHERE path = 'public/science-math-integration.html' OR path LIKE '%science-math-integration.html';


-- Update metadata for: ✨ Teaching Variants Showcase | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '✨ Teaching Variants Showcase | Te Kete Ako')
WHERE path = 'public/teaching-variants-showcase.html' OR path LIKE '%teaching-variants-showcase.html';


-- Update metadata for: Professional Dashboard - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Professional Dashboard - Te Kete Ako')
WHERE path = 'public/professional-dashboard.html' OR path LIKE '%professional-dashboard.html';


-- Update metadata for: 🧠 GraphRAG Brain Hub - Living Intelligence | Te Ke
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🧠 GraphRAG Brain Hub - Living Intelligence | Te Kete Ako')
WHERE path = 'public/graphrag-brain-hub.html' OR path LIKE '%graphrag-brain-hub.html';


-- Update metadata for: Cultural Excellence Hub | 7,391 Resources | Te Ket
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Excellence Hub | 7,391 Resources | Te Kete Ako')
WHERE path = 'public/cultural-hub.html' OR path LIKE '%cultural-hub.html';


-- Update metadata for: Arts Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Arts Hub | Te Kete Ako')
WHERE path = 'public/arts-hub.html' OR path LIKE '%arts-hub.html';


-- Update metadata for: Cultural Tools Directory | 74 Tools | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Tools Directory | 74 Tools | Te Kete Ako')
WHERE path = 'public/cultural-tools-directory.html' OR path LIKE '%cultural-tools-directory.html';


-- Update metadata for: Social Sciences Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Social Sciences Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/curriculum-social-sciences.html' OR path LIKE '%curriculum-social-sciences.html';


-- Update metadata for: Authentication Diagnostics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Authentication Diagnostics | Te Kete Ako')
WHERE path = 'public/auth-diagnostics.html' OR path LIKE '%auth-diagnostics.html';


-- Update metadata for: Te Kete Ako - Auth Test (8PM Ready)
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Auth Test (8PM Ready)')
WHERE path = 'public/auth-test.html' OR path LIKE '%auth-test.html';


-- Update metadata for: 🌐 Influence Hubs - Most Connected Resources | Te K
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🌐 Influence Hubs - Most Connected Resources | Te Kete Ako')
WHERE path = 'public/influence-hubs.html' OR path LIKE '%influence-hubs.html';


-- Update metadata for: Te Kete Ako | Educational Resources Honoring Te Ao
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Educational Resources Honoring Te Ao Māori')
WHERE path = 'public/index-simple.html' OR path LIKE '%index-simple.html';


-- Update metadata for: Lesson-Handout Pairs | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson-Handout Pairs | Te Kete Ako')
WHERE path = 'public/lesson-handout-pairs.html' OR path LIKE '%lesson-handout-pairs.html';


-- Update metadata for: 🔐 Auth Testing Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), '🔐 Auth Testing Dashboard | Te Kete Ako')
WHERE path = 'public/auth-testing-dashboard.html' OR path LIKE '%auth-testing-dashboard.html';


-- Update metadata for: Te Kete Ako | West Coast NZ Design Demo
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | West Coast NZ Design Demo')
WHERE path = 'public/index-west-coast-demo.html' OR path LIKE '%index-west-coast-demo.html';


-- Update metadata for: Year 10 Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Year 10 Hub | Te Kete Ako')
WHERE path = 'public/year-10-hub.html' OR path LIKE '%year-10-hub.html';


-- Update metadata for: Student Sign Up | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Student Sign Up | Te Kete Ako')
WHERE path = 'public/signup-student.html' OR path LIKE '%signup-student.html';


-- Update metadata for: GraphRAG Knowledge Graph Demo | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Knowledge Graph Demo | Te Kete Ako')
WHERE path = 'public/graphrag-demo.html' OR path LIKE '%graphrag-demo.html';


-- Update metadata for: Curriculum: Health & PE | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Health & PE | Te Kete Ako')
WHERE path = 'public/curriculum-health-pe.html' OR path LIKE '%curriculum-health-pe.html';


-- Update metadata for: Games | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Games | Te Kete Ako')
WHERE path = 'public/games.html' OR path LIKE '%games.html';


-- Update metadata for: My Kete | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Kete | Te Kete Ako')
WHERE path = 'public/my-kete.html' OR path LIKE '%my-kete.html';


-- Update metadata for: Teacher Dashboard | GraphRAG Intelligence | Te Ket
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Dashboard | GraphRAG Intelligence | Te Kete Ako (Updated Oct 19 2025)')
WHERE path = 'public/graphrag-teacher-dashboard.html' OR path LIKE '%graphrag-teacher-dashboard.html';


-- Update metadata for: Complete Assessments Library | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Complete Assessments Library | Te Kete Ako')
WHERE path = 'public/assessments-complete.html' OR path LIKE '%assessments-complete.html';


-- Update metadata for: Whakataukī Collection | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Whakataukī Collection | Te Kete Ako')
WHERE path = 'public/whakatauki-collection.html' OR path LIKE '%whakatauki-collection.html';


-- Update metadata for: 🌉 GraphRAG Relationship Explorer | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🌉 GraphRAG Relationship Explorer | Te Kete Ako')
WHERE path = 'public/graphrag-relationship-explorer.html' OR path LIKE '%graphrag-relationship-explorer.html';


-- Update metadata for: Year 7 Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Year 7 Hub | Te Kete Ako')
WHERE path = 'public/year-7-hub.html' OR path LIKE '%year-7-hub.html';


-- Update metadata for: Site Map | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Site Map | Te Kete Ako')
WHERE path = 'public/site-map.html' OR path LIKE '%site-map.html';


-- Update metadata for: Discovery Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Discovery Dashboard | Te Kete Ako')
WHERE path = 'public/discovery-dashboard.html' OR path LIKE '%discovery-dashboard.html';


-- Update metadata for: Prerequisite Chain Explorer | GraphRAG Learning Pa
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Prerequisite Chain Explorer | GraphRAG Learning Pathways | Te Kete Ako')
WHERE path = 'public/prerequisite-chain-explorer.html' OR path LIKE '%prerequisite-chain-explorer.html';


-- Update metadata for: Cross-Curricular Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 11',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cross-Curricular Hub | Te Kete Ako')
WHERE path = 'public/cross-curricular-hub.html' OR path LIKE '%cross-curricular-hub.html';


-- Update metadata for: Cultural Learning Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Learning Hub | Te Kete Ako')
WHERE path = 'public/cultural-learning.html' OR path LIKE '%cultural-learning.html';


-- Update metadata for: Teacher Resource Finder | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Resource Finder | Te Kete Ako')
WHERE path = 'public/teacher-resource-finder.html' OR path LIKE '%teacher-resource-finder.html';


-- Update metadata for: Network Visualization - Te Kete Ako GraphRAG
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Network Visualization - Te Kete Ako GraphRAG')
WHERE path = 'public/network-visualization.html' OR path LIKE '%network-visualization.html';


-- Update metadata for: Curated Excellence Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Curated Excellence Pathways | Te Kete Ako')
WHERE path = 'public/curated-pathways.html' OR path LIKE '%curated-pathways.html';


-- Update metadata for: Mathematics Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Mathematics Hub | Te Kete Ako')
WHERE path = 'public/mathematics-hub.html' OR path LIKE '%mathematics-hub.html';


-- Update metadata for: Educational Transformation | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Educational Transformation | Te Kete Ako')
WHERE path = 'public/educational-transformation-showcase.html' OR path LIKE '%educational-transformation-showcase.html';


-- Update metadata for: Schema Test
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Schema Test')
WHERE path = 'public/test-schema.html' OR path LIKE '%test-schema.html';


-- Update metadata for: Under-Connected Excellence | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Under-Connected Excellence | Te Kete Ako')
WHERE path = 'public/under-connected-excellence.html' OR path LIKE '%under-connected-excellence.html';


-- Update metadata for: Knowledge Graph Explorer | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Knowledge Graph Explorer | Te Kete Ako')
WHERE path = 'public/knowledge-graph-explorer.html' OR path LIKE '%knowledge-graph-explorer.html';


-- Update metadata for: Visual Knowledge Graph | GraphRAG Intelligence | T
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Visual Knowledge Graph | GraphRAG Intelligence | Te Kete Ako')
WHERE path = 'public/graphrag-visual-graph.html' OR path LIKE '%graphrag-visual-graph.html';


-- Update metadata for: Science × Social Studies Integration | 373 GraphRA
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Science × Social Studies Integration | 373 GraphRAG Connections | Te Kete Ako')
WHERE path = 'public/science-social-studies-integration.html' OR path LIKE '%science-social-studies-integration.html';


-- Update metadata for: Experiences | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Experiences | Te Kete Ako')
WHERE path = 'public/experiences.html' OR path LIKE '%experiences.html';


-- Update metadata for: 🎓 Teacher AI Intelligence Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🎓 Teacher AI Intelligence Hub | Te Kete Ako')
WHERE path = 'public/teacher-ai-intelligence-hub.html' OR path LIKE '%teacher-ai-intelligence-hub.html';


-- Update metadata for: Teacher Guide: GraphRAG Discovery Features | Te Ke
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Guide: GraphRAG Discovery Features | Te Kete Ako')
WHERE path = 'public/teacher-guide-graphrag-features.html' OR path LIKE '%teacher-guide-graphrag-features.html';


-- Update metadata for: The Writer's Toolkit | Critical Literacy Unit
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit | Critical Literacy Unit')
WHERE path = 'public/toolkit.html' OR path LIKE '%toolkit.html';


-- Update metadata for: GraphRAG Knowledge Explorer | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Knowledge Explorer | Te Kete Ako')
WHERE path = 'public/graphrag-explorer.html' OR path LIKE '%graphrag-explorer.html';


-- Update metadata for: Enhanced GraphRAG Search | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Enhanced GraphRAG Search | Te Kete Ako')
WHERE path = 'public/enhanced-graphrag-search.html' OR path LIKE '%enhanced-graphrag-search.html';


-- Update metadata for: English × Science Integration | 206 GraphRAG Conne
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'English × Science Integration | 206 GraphRAG Connections | Te Kete Ako')
WHERE path = 'public/english-science-integration.html' OR path LIKE '%english-science-integration.html';


-- Update metadata for: Navigation Fix Standard Header
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Navigation Fix Standard Header')
WHERE path = 'public/navigation_fix_standard_header.html' OR path LIKE '%navigation_fix_standard_header.html';


-- Update metadata for: Curriculum: Languages | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Languages | Te Kete Ako')
WHERE path = 'public/curriculum-languages.html' OR path LIKE '%curriculum-languages.html';


-- Update metadata for: 🌟 AI Pūrākau Generator | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🌟 AI Pūrākau Generator | Te Kete Ako')
WHERE path = 'public/ai-purakau-story-generator.html' OR path LIKE '%ai-purakau-story-generator.html';


-- Update metadata for: GraphRAG Learning Pathway Finder | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'GraphRAG Learning Pathway Finder | Te Kete Ako')
WHERE path = 'public/graphrag-pathway-finder.html' OR path LIKE '%graphrag-pathway-finder.html';


-- Update metadata for: Enterprise SSO - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Enterprise SSO - Te Kete Ako')
WHERE path = 'public/enterprise-sso-dashboard.html' OR path LIKE '%enterprise-sso-dashboard.html';


-- Update metadata for: My Kete - Personal Learning Collection | Te Kete A
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Kete - Personal Learning Collection | Te Kete Ako')
WHERE path = 'public/my-kete-enhanced.html' OR path LIKE '%my-kete-enhanced.html';


-- Update metadata for: UX Verification Test - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'UX Verification Test - Te Kete Ako')
WHERE path = 'public/test-ux-verification.html' OR path LIKE '%test-ux-verification.html';


-- Update metadata for: 🧪 Variant System Test Page | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), '🧪 Variant System Test Page | Te Kete Ako')
WHERE path = 'public/VARIANT-SYSTEM-TEST.html' OR path LIKE '%VARIANT-SYSTEM-TEST.html';


-- Update metadata for: Interactive Learning Demo | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Interactive Learning Demo | Te Kete Ako')
WHERE path = 'public/interactive-learning-demo.html' OR path LIKE '%interactive-learning-demo.html';


-- Update metadata for: DeepSeek Agent Test | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'DeepSeek Agent Test | Te Kete Ako')
WHERE path = 'public/deepseek-agent-test.html' OR path LIKE '%deepseek-agent-test.html';


-- Update metadata for: Advanced Search | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Advanced Search | Te Kete Ako')
WHERE path = 'public/advanced-search-graphrag.html' OR path LIKE '%advanced-search-graphrag.html';


-- Update metadata for: Teacher Sign Up | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Sign Up | Te Kete Ako')
WHERE path = 'public/signup-teacher.html' OR path LIKE '%signup-teacher.html';


-- Update metadata for: Privacy Policy - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Privacy Policy - Te Kete Ako')
WHERE path = 'public/privacy.html' OR path LIKE '%privacy.html';


-- Update metadata for: Unit Hub | Year 8 Systems: Decolonizing Power Stru
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit Hub | Year 8 Systems: Decolonizing Power Structures | Te Kete Ako - Postcolonial Social Studies')
WHERE path = 'public/y8-systems-unit.html' OR path LIKE '%y8-systems-unit.html';


-- Update metadata for: 🤖 Agent Coordination Dashboard - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🤖 Agent Coordination Dashboard - Te Kete Ako')
WHERE path = 'public/agent-coordination-dashboard.html' OR path LIKE '%agent-coordination-dashboard.html';


-- Update metadata for: EXA.ai Resource Discovery | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'EXA.ai Resource Discovery | Te Kete Ako')
WHERE path = 'public/exa-search.html' OR path LIKE '%exa-search.html';


-- Update metadata for: English Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'English Hub | Te Kete Ako')
WHERE path = 'public/english-hub.html' OR path LIKE '%english-hub.html';


-- Update metadata for: Virtual Marae Training Protocol | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Virtual Marae Training Protocol | Te Kete Ako')
WHERE path = 'public/virtual-marae.html' OR path LIKE '%virtual-marae.html';


-- Update metadata for: Community Action Project Brief | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Community Action Project Brief | Te Kete Ako')
WHERE path = 'public/project-brief.html' OR path LIKE '%project-brief.html';


-- Update metadata for: Lesson Plans | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plans | Te Kete Ako')
WHERE path = 'public/lessons.html' OR path LIKE '%lessons.html';


-- Update metadata for: Resource Discovery Hub - Te Kete Ako V2.5
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Resource Discovery Hub - Te Kete Ako V2.5')
WHERE path = 'public/resource-discovery-hub.html' OR path LIKE '%resource-discovery-hub.html';


-- Update metadata for: Te Kete Ako | Educational Resources Honoring Te Ao
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Educational Resources Honoring Te Ao Māori')
WHERE path = 'public/index-backup.html' OR path LIKE '%index-backup.html';


-- Update metadata for: AI Teacher Planning Assistant | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Teacher Planning Assistant | Te Kete Ako')
WHERE path = 'public/teacher-planning-ai.html' OR path LIKE '%teacher-planning-ai.html';


-- Update metadata for: Browse All Handouts | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Browse All Handouts | Te Kete Ako')
WHERE path = 'public/browse-handouts.html' OR path LIKE '%browse-handouts.html';


-- Update metadata for: Teacher Community Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Teacher Community Hub | Te Kete Ako')
WHERE path = 'public/teacher-community.html' OR path LIKE '%teacher-community.html';


-- Update metadata for: Year 10 Mathematics - Cultural Geometry Unit | Kai
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Year 10 Mathematics - Cultural Geometry Unit | Kaitiaki Aronui Generated')
WHERE path = 'public/unit-plans/kaitiaki-generated-y10-math-cultural-geometry.html' OR path LIKE '%kaitiaki-generated-y10-math-cultural-geometry.html';


-- Update metadata for: Interactive Society Design Tool | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Interactive Society Design Tool | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/society-design-tool.html' OR path LIKE '%society-design-tool.html';


-- Update metadata for: Guided Inquiry: Design Your Society | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Guided Inquiry: Design Your Society | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/guided-inquiry-society-design.html' OR path LIKE '%guided-inquiry-society-design.html';


-- Update metadata for: Cultural Values Framework Worksheet | Society Desi
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Values Framework Worksheet | Society Design')
WHERE path = 'public/guided-inquiry-unit/materials/cultural-values-framework-worksheet.html' OR path LIKE '%cultural-values-framework-worksheet.html';


-- Update metadata for: Group Formation Strengths Inventory | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Group Formation Strengths Inventory | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/group-formation-strengths-inventory.html' OR path LIKE '%group-formation-strengths-inventory.html';


-- Update metadata for: Presentation Protocols Poster | Society Design Uni
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Presentation Protocols Poster | Society Design Unit')
WHERE path = 'public/guided-inquiry-unit/materials/presentation-protocols-poster.html' OR path LIKE '%presentation-protocols-poster.html';


-- Update metadata for: Society Integration Summary | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Society Integration Summary | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/society-integration-summary.html' OR path LIKE '%society-integration-summary.html';


-- Update metadata for: Gallery Walk Station Cards | Society Exploration |
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Gallery Walk Station Cards | Society Exploration | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/society-exploration-gallery-walk-stations.html' OR path LIKE '%society-exploration-gallery-walk-stations.html';


-- Update metadata for: Government Testing Scenarios Cards | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Government Testing Scenarios Cards | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/government-testing-scenarios.html' OR path LIKE '%government-testing-scenarios.html';


-- Update metadata for: Group Collaboration Assessment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Group Collaboration Assessment | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/group-collaboration-assessment.html' OR path LIKE '%group-collaboration-assessment.html';


-- Update metadata for: Rights Economics Integration Scenarios | Te Kete A
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Rights Economics Integration Scenarios | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/rights-economics-integration-scenarios.html' OR path LIKE '%rights-economics-integration-scenarios.html';


-- Update metadata for: Cultural Lens Analysis Template | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Lens Analysis Template | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/cultural-lens-analysis-template.html' OR path LIKE '%cultural-lens-analysis-template.html';


-- Update metadata for: Government Component Analysis Worksheet | Te Kete 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Government Component Analysis Worksheet | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/government-component-analysis-worksheet.html' OR path LIKE '%government-component-analysis-worksheet.html';


-- Update metadata for: Economic System Design Worksheet | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Economic System Design Worksheet | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/economic-system-design-worksheet.html' OR path LIKE '%economic-system-design-worksheet.html';


-- Update metadata for: Education System Design Template | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Education System Design Template | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/education-system-design-template.html' OR path LIKE '%education-system-design-template.html';


-- Update metadata for: Indigenous Wisdom Synthesis Worksheet | Te Kete Ak
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Indigenous Wisdom Synthesis Worksheet | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/indigenous-wisdom-synthesis-worksheet.html' OR path LIKE '%indigenous-wisdom-synthesis-worksheet.html';


-- Update metadata for: Society Design Unit Summative Assessment Guide
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Society Design Unit Summative Assessment Guide')
WHERE path = 'public/guided-inquiry-unit/materials/unit-summative-assessment-guide.html' OR path LIKE '%unit-summative-assessment-guide.html';


-- Update metadata for: Society Design Presentation Rubric | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Society Design Presentation Rubric | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/society-design-presentation-rubric.html' OR path LIKE '%society-design-presentation-rubric.html';


-- Update metadata for: Research Planning Template | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Research Planning Template | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/research-planning-template.html' OR path LIKE '%research-planning-template.html';


-- Update metadata for: Unit Learning Reflection Template | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Unit Learning Reflection Template | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/unit-learning-reflection-template.html' OR path LIKE '%unit-learning-reflection-template.html';


-- Update metadata for: Rights Charter Template | Society Design
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Rights Charter Template | Society Design')
WHERE path = 'public/guided-inquiry-unit/materials/rights-charter-template.html' OR path LIKE '%rights-charter-template.html';


-- Update metadata for: Society Design Peer Review Form | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Society Design Peer Review Form | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/society-design-peer-review-form.html' OR path LIKE '%society-design-peer-review-form.html';


-- Update metadata for: Strengths Inventory Worksheet | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Strengths Inventory Worksheet | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/strengths-inventory-worksheet.html' OR path LIKE '%strengths-inventory-worksheet.html';


-- Update metadata for: Government Design Template | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Government Design Template | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/government-design-template.html' OR path LIKE '%government-design-template.html';


-- Update metadata for: Culture-Society Integration Planner | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Culture-Society Integration Planner | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/culture-society-integration-planner.html' OR path LIKE '%culture-society-integration-planner.html';


-- Update metadata for: Group Agreement Template | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Group Agreement Template | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/group-agreement-template.html' OR path LIKE '%group-agreement-template.html';


-- Update metadata for: Peer Recognition Awards Template | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Peer Recognition Awards Template | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/peer-recognition-awards-template.html' OR path LIKE '%peer-recognition-awards-template.html';


-- Update metadata for: Society Exploration Graphic Organizer | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Society Exploration Graphic Organizer | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/materials/society-exploration-graphic-organizer.html' OR path LIKE '%society-exploration-graphic-organizer.html';


-- Update metadata for: Lesson 1: Society Exploration | Guided Inquiry Uni
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Society Exploration | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/lessons/lesson-1-society-exploration.html' OR path LIKE '%lesson-1-society-exploration.html';


-- Update metadata for: Lesson 4: Rights & Economy Integration | Guided In
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: Rights & Economy Integration | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/lessons/lesson-4-rights-economy.html' OR path LIKE '%lesson-4-rights-economy.html';


-- Update metadata for: Lesson 2: Group Formation & Research Planning | Gu
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: Group Formation & Research Planning | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/lessons/lesson-2-group-formation.html' OR path LIKE '%lesson-2-group-formation.html';


-- Update metadata for: Lesson 3: Government Systems Design | Guided Inqui
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Government Systems Design | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/lessons/lesson-3-government-systems.html' OR path LIKE '%lesson-3-government-systems.html';


-- Update metadata for: Lesson 6: Presentations & Peer Review | Guided Inq
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6: Presentations & Peer Review | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/lessons/lesson-6-presentations.html' OR path LIKE '%lesson-6-presentations.html';


-- Update metadata for: Lesson 5: Culture & Systems Integration | Guided I
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5: Culture & Systems Integration | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/guided-inquiry-unit/lessons/lesson-5-culture-integration.html' OR path LIKE '%lesson-5-culture-integration.html';


-- Update metadata for: Cultural-Mathematical Assessment Rubric | Kaitiaki
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Cultural-Mathematical Assessment Rubric | Kaitiaki Aronui Generated')
WHERE path = 'public/assessments/kaitiaki-generated-cultural-mathematics-rubric.html' OR path LIKE '%kaitiaki-generated-cultural-mathematics-rubric.html';


-- Update metadata for: Crossword Generator | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Crossword Generator | Te Kete Ako')
WHERE path = 'public/tools/crossword-generator.html' OR path LIKE '%crossword-generator.html';


-- Update metadata for: YouTube Library Administration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'YouTube Library Administration | Te Kete Ako')
WHERE path = 'public/handouts/admin-youtube-library.html' OR path LIKE '%admin-youtube-library.html';


-- Update metadata for: Algebraic Thinking in Traditional Māori Games | Te
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Algebraic Thinking in Traditional Māori Games | Te Kete Ako')
WHERE path = 'public/handouts/algebraic-thinking-in-traditional-māori-games.html' OR path LIKE '%algebraic-thinking-in-traditional-māori-games.html';


-- Update metadata for: Health Education Correlation | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Health Education Correlation | Te Kete Ako')
WHERE path = 'public/handouts/health-education-correlation.html' OR path LIKE '%health-education-correlation.html';


-- Update metadata for: Urban Migration Experience Stories - First-Hand Ac
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Urban Migration Experience Stories - First-Hand Accounts of a Changing Aotearoa | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-urban-migration-stories.html' OR path LIKE '%unit-2-urban-migration-stories.html';


-- Update metadata for: Te Kete Ako - EMERGENCY RECOVERY
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - EMERGENCY RECOVERY')
WHERE path = 'public/handouts/emergency-diagnostic.html' OR path LIKE '%emergency-diagnostic.html';


-- Update metadata for: Place Description Handout | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Place Description Handout | Te Kete Ako')
WHERE path = 'public/handouts/place-description-handout.html' OR path LIKE '%place-description-handout.html';


-- Update metadata for: Author's Purpose: The Art of Persuasion | Te Kete 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Author''s Purpose: The Art of Persuasion | Te Kete Ako')
WHERE path = 'public/handouts/authors-purpose-handout.html' OR path LIKE '%authors-purpose-handout.html';


-- Update metadata for: Introduction to Probability Handout | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Introduction to Probability Handout | Te Kete Ako')
WHERE path = 'public/handouts/probability-handout.html' OR path LIKE '%probability-handout.html';


-- Update metadata for: Census Data Analysis Worksheet - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Census Data Analysis Worksheet - Y8 Statistics')
WHERE path = 'public/handouts/y8-statistics-census-data-worksheet.html' OR path LIKE '%y8-statistics-census-data-worksheet.html';


-- Update metadata for: Decision Frameworks Comparison Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Decision Frameworks Comparison Guide | Te Kete Ako')
WHERE path = 'public/handouts/decision-frameworks-comparison-guide.html' OR path LIKE '%decision-frameworks-comparison-guide.html';


-- Update metadata for: Biotechnology Ethics Through Māori Worldview | Te 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Biotechnology Ethics Through Māori Worldview | Te Kete Ako')
WHERE path = 'public/handouts/biotechnology-ethics-through-māori-worldview.html' OR path LIKE '%biotechnology-ethics-through-māori-worldview.html';


-- Update metadata for: Future Visioning Creative Writing | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Future Visioning Creative Writing | Te Kete Ako')
WHERE path = 'public/handouts/future-visioning-creative-writing.html' OR path LIKE '%future-visioning-creative-writing.html';


-- Update metadata for: Environmental Literacy Framework - Unit 3 Integrat
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Environmental Literacy Framework - Unit 3 Integration | Mangakōtukutuku College')
WHERE path = 'public/handouts/environmental-literacy-framework.html' OR path LIKE '%environmental-literacy-framework.html';


-- Update metadata for: Local Area History | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Local Area History | Te Kete Ako')
WHERE path = 'public/handouts/local-area-history.html' OR path LIKE '%local-area-history.html';


-- Update metadata for: Offline - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Offline - Te Kete Ako')
WHERE path = 'public/handouts/offline.html' OR path LIKE '%offline.html';


-- Update metadata for: Do Now Activities | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Do Now Activities | Te Kete Ako')
WHERE path = 'public/handouts/activities.html' OR path LIKE '%activities.html';


-- Update metadata for: AI Teacher Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'AI Teacher Dashboard | Te Kete Ako')
WHERE path = 'public/handouts/teacher-dashboard-ai.html' OR path LIKE '%teacher-dashboard-ai.html';


-- Update metadata for: Science Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Science Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/handouts/curriculum-science.html' OR path LIKE '%curriculum-science.html';


-- Update metadata for: Design Thinking Process Handout
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Design Thinking Process Handout')
WHERE path = 'public/handouts/design-thinking-process-handout.html' OR path LIKE '%design-thinking-process-handout.html';


-- Update metadata for: Cultural Stories Comprehension | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Stories Comprehension | Te Kete Ako')
WHERE path = 'public/handouts/cultural-stories-comprehension.html' OR path LIKE '%cultural-stories-comprehension.html';


-- Update metadata for: The Writer's Toolkit: The Revision Process
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: The Revision Process')
WHERE path = 'public/handouts/writers-toolkit-revision-handout.html' OR path LIKE '%writers-toolkit-revision-handout.html';


-- Update metadata for: Te Kete Ako - Intelligent Resource Discovery | Gra
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Intelligent Resource Discovery | GraphRAG Search')
WHERE path = 'public/handouts/graphrag-search.html' OR path LIKE '%graphrag-search.html';


-- Update metadata for: Verify Email | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Verify Email | Te Kete Ako')
WHERE path = 'public/handouts/verify-email.html' OR path LIKE '%verify-email.html';


-- Update metadata for: Living Whakapapa Project | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Living Whakapapa Project | Te Kete Ako')
WHERE path = 'public/handouts/living-whakapapa.html' OR path LIKE '%living-whakapapa.html';


-- Update metadata for: Te Reo Phonics Handout | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Phonics Handout | Te Kete Ako')
WHERE path = 'public/handouts/te-reo-phonics-handout.html' OR path LIKE '%te-reo-phonics-handout.html';


-- Update metadata for: My Submissions | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'My Submissions | Te Kete Ako')
WHERE path = 'public/handouts/my-submissions.html' OR path LIKE '%my-submissions.html';


-- Update metadata for: AI Ethics and Bias | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics and Bias | Te Kete Ako')
WHERE path = 'public/handouts/ai-ethics-and-bias.html' OR path LIKE '%ai-ethics-and-bias.html';


-- Update metadata for: AI Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'AI Hub | Te Kete Ako')
WHERE path = 'public/handouts/ai-hub.html' OR path LIKE '%ai-hub.html';


-- Update metadata for: Elements of Art Handout
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Elements of Art Handout')
WHERE path = 'public/handouts/elements-of-art-handout.html' OR path LIKE '%elements-of-art-handout.html';


-- Update metadata for: Then And Now Comparison | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Then And Now Comparison | Te Kete Ako')
WHERE path = 'public/handouts/then-and-now-comparison.html' OR path LIKE '%then-and-now-comparison.html';


-- Update metadata for: Māori Astronomy and Navigation Handout
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Māori Astronomy and Navigation Handout')
WHERE path = 'public/handouts/maori-astronomy-navigation-handout.html' OR path LIKE '%maori-astronomy-navigation-handout.html';


-- Update metadata for: Indigenous Rights Research | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Indigenous Rights Research | Te Kete Ako')
WHERE path = 'public/handouts/indigenous-rights-research.html' OR path LIKE '%indigenous-rights-research.html';


-- Update metadata for: Atoms In Everyday Materials | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Atoms In Everyday Materials | Te Kete Ako')
WHERE path = 'public/handouts/atoms-in-everyday-materials.html' OR path LIKE '%atoms-in-everyday-materials.html';


-- Update metadata for: Waka Physics Basics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Waka Physics Basics | Te Kete Ako')
WHERE path = 'public/handouts/waka-physics-basics.html' OR path LIKE '%waka-physics-basics.html';


-- Update metadata for: Renewable Energy Traditional | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Renewable Energy Traditional | Te Kete Ako')
WHERE path = 'public/handouts/renewable-energy-traditional.html' OR path LIKE '%renewable-energy-traditional.html';


-- Update metadata for: Hangi Fractions Sharing | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Hangi Fractions Sharing | Te Kete Ako')
WHERE path = 'public/handouts/hangi-fractions-sharing.html' OR path LIKE '%hangi-fractions-sharing.html';


-- Update metadata for: Resource Connections | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Resource Connections | Te Kete Ako')
WHERE path = 'public/handouts/resource-connections.html' OR path LIKE '%resource-connections.html';


-- Update metadata for: Perspective Comparison - Colonial vs. Māori Views 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Perspective Comparison - Colonial vs. Māori Views of the Aotearoa Wars | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-colonial-maori-perspective-comparison.html' OR path LIKE '%unit-2-colonial-maori-perspective-comparison.html';


-- Update metadata for: Learning Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Learning Pathways | Te Kete Ako')
WHERE path = 'public/handouts/learning-pathways.html' OR path LIKE '%learning-pathways.html';


-- Update metadata for: Handout: Climate Change in Aotearoa
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Climate Change in Aotearoa')
WHERE path = 'public/handouts/climate-emergency-aotearoa-handout.html' OR path LIKE '%climate-emergency-aotearoa-handout.html';


-- Update metadata for: Handout: The Power of Yet
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: The Power of Yet')
WHERE path = 'public/handouts/ted-power-yet-handout.html' OR path LIKE '%ted-power-yet-handout.html';


-- Update metadata for: Natural Dye Lab Investigation (Y9 Chemistry)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Natural Dye Lab Investigation (Y9 Chemistry)')
WHERE path = 'public/handouts/natural-dye-lab-sheet.html' OR path LIKE '%natural-dye-lab-sheet.html';


-- Update metadata for: Hērangi Migration Stories | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Hērangi Migration Stories | Te Kete Ako')
WHERE path = 'public/handouts/herangi-migration-stories.html' OR path LIKE '%herangi-migration-stories.html';


-- Update metadata for: Analysing a Film Scene
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Analysing a Film Scene')
WHERE path = 'public/handouts/film-scene-analysis-handout.html' OR path LIKE '%film-scene-analysis-handout.html';


-- Update metadata for: Whakapapa Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Whakapapa Mathematics | Te Kete Ako')
WHERE path = 'public/handouts/whakapapa-mathematics.html' OR path LIKE '%whakapapa-mathematics.html';


-- Update metadata for: Tukutuku Patterns Maths | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Patterns Maths | Te Kete Ako')
WHERE path = 'public/handouts/tukutuku-patterns-maths.html' OR path LIKE '%tukutuku-patterns-maths.html';


-- Update metadata for: Water Cycle Cultural | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Water Cycle Cultural | Te Kete Ako')
WHERE path = 'public/handouts/water-cycle-cultural.html' OR path LIKE '%water-cycle-cultural.html';


-- Update metadata for: The Writer's Toolkit: Word Choice (Diction)
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Word Choice (Diction)')
WHERE path = 'public/handouts/writers-toolkit-diction-handout.html' OR path LIKE '%writers-toolkit-diction-handout.html';


-- Update metadata for: English Handouts Index | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'English Handouts Index | Te Kete Ako')
WHERE path = 'public/handouts/english-handouts-index.html' OR path LIKE '%english-handouts-index.html';


-- Update metadata for: Shakespearean Soliloquy Reading Comprehension
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Shakespearean Soliloquy Reading Comprehension')
WHERE path = 'public/handouts/shakespeare-soliloquy-handout.html' OR path LIKE '%shakespeare-soliloquy-handout.html';


-- Update metadata for: Other Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Other Resources | Te Kete Ako')
WHERE path = 'public/handouts/other-resources.html' OR path LIKE '%other-resources.html';


-- Update metadata for: Forgot Password | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Forgot Password | Te Kete Ako')
WHERE path = 'public/handouts/forgot-password.html' OR path LIKE '%forgot-password.html';


-- Update metadata for: Primary Source Analysis: 1975 Memorial of Right
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Primary Source Analysis: 1975 Memorial of Right')
WHERE path = 'public/handouts/primary-source-analysis-1975-memorial-of-right.html' OR path LIKE '%primary-source-analysis-1975-memorial-of-right.html';


-- Update metadata for: Nature Observation Journal | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Nature Observation Journal | Te Kete Ako')
WHERE path = 'public/handouts/nature-observation-journal.html' OR path LIKE '%nature-observation-journal.html';


-- Update metadata for: Treaty Stories Analysis | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Treaty Stories Analysis | Te Kete Ako')
WHERE path = 'public/handouts/treaty-stories-analysis.html' OR path LIKE '%treaty-stories-analysis.html';


-- Update metadata for: About Te Kete Ako | Educational Resources Platform
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'About Te Kete Ako | Educational Resources Platform')
WHERE path = 'public/handouts/about.html' OR path LIKE '%about.html';


-- Update metadata for: Curriculum: Arts | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Arts | Te Kete Ako')
WHERE path = 'public/handouts/curriculum-arts.html' OR path LIKE '%curriculum-arts.html';


-- Update metadata for: Decolonized Assessment Framework - Honoring Dual K
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Decolonized Assessment Framework - Honoring Dual Knowledge Systems | Te Kete Ako')
WHERE path = 'public/handouts/decolonized-assessment-framework.html' OR path LIKE '%decolonized-assessment-framework.html';


-- Update metadata for: Weather Calendar Graphs | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Weather Calendar Graphs | Te Kete Ako')
WHERE path = 'public/handouts/weather-calendar-graphs.html' OR path LIKE '%weather-calendar-graphs.html';


-- Update metadata for: Privacy Policy | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Privacy Policy | Te Kete Ako')
WHERE path = 'public/handouts/privacy-policy.html' OR path LIKE '%privacy-policy.html';


-- Update metadata for: Handout: The Art of Haka
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: The Art of Haka')
WHERE path = 'public/handouts/art-of-haka-handout.html' OR path LIKE '%art-of-haka-handout.html';


-- Update metadata for: Star Navigation Coordinates | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Star Navigation Coordinates | Te Kete Ako')
WHERE path = 'public/handouts/star-navigation-coordinates.html' OR path LIKE '%star-navigation-coordinates.html';


-- Update metadata for: Author's Purpose: Entertain
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Author''s Purpose: Entertain')
WHERE path = 'public/handouts/authors-purpose-entertain-handout.html' OR path LIKE '%authors-purpose-entertain-handout.html';


-- Update metadata for: Tukutuku Pattern Generator | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Pattern Generator | Te Kete Ako')
WHERE path = 'public/handouts/tukutuku-pattern-generator.html' OR path LIKE '%tukutuku-pattern-generator.html';


-- Update metadata for: Marae Blueprint Scaling | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Marae Blueprint Scaling | Te Kete Ako')
WHERE path = 'public/handouts/marae-blueprint-scaling.html' OR path LIKE '%marae-blueprint-scaling.html';


-- Update metadata for: 🤖 AI Coordination Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), '🤖 AI Coordination Dashboard | Te Kete Ako')
WHERE path = 'public/handouts/ai-coordination-dashboard.html' OR path LIKE '%ai-coordination-dashboard.html';


-- Update metadata for: Introduction to Large Language Models | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Introduction to Large Language Models | Te Kete Ako')
WHERE path = 'public/handouts/introduction-to-llms.html' OR path LIKE '%introduction-to-llms.html';


-- Update metadata for: Social Studies | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Social Studies | Te Kete Ako')
WHERE path = 'public/handouts/social-studies.html' OR path LIKE '%social-studies.html';


-- Update metadata for: Contact Te Kete Ako | Support & Feedback
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Contact Te Kete Ako | Support & Feedback')
WHERE path = 'public/handouts/contact.html' OR path LIKE '%contact.html';


-- Update metadata for: Prompt Engineering 101 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Prompt Engineering 101 | Te Kete Ako')
WHERE path = 'public/handouts/prompt-engineering-101.html' OR path LIKE '%prompt-engineering-101.html';


-- Update metadata for: Mountain Navigation Trigonometry | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Mountain Navigation Trigonometry | Te Kete Ako')
WHERE path = 'public/handouts/mountain-navigation-trigonometry.html' OR path LIKE '%mountain-navigation-trigonometry.html';


-- Update metadata for: Language Revitalization Growth | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Language Revitalization Growth | Te Kete Ako')
WHERE path = 'public/handouts/language-revitalization-growth.html' OR path LIKE '%language-revitalization-growth.html';


-- Update metadata for: Walker Lesson 1.1 Assessment Rubric | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Walker Lesson 1.1 Assessment Rubric | Te Kete Ako')
WHERE path = 'public/handouts/walker-lesson-1-1-assessment-rubric.html' OR path LIKE '%walker-lesson-1-1-assessment-rubric.html';


-- Update metadata for: Leadership Development Through Cultural Values
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Leadership Development Through Cultural Values')
WHERE path = 'public/handouts/leadership-development-through-cultural-values.html' OR path LIKE '%leadership-development-through-cultural-values.html';


-- Update metadata for: Visual Arts Analysis with Māori Aesthetic Principl
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Visual Arts Analysis with Māori Aesthetic Principles')
WHERE path = 'public/handouts/visual-arts-analysis-with-cultural-context.html' OR path LIKE '%visual-arts-analysis-with-cultural-context.html';


-- Update metadata for: Presentation Assessment Rubric - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Presentation Assessment Rubric - Y8 Statistics')
WHERE path = 'public/handouts/y8-statistics-presentation-rubric.html' OR path LIKE '%y8-statistics-presentation-rubric.html';


-- Update metadata for: Te Reo Māori Greetings Handout | Mangakōtukutuku C
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Greetings Handout | Mangakōtukutuku College')
WHERE path = 'public/handouts/te-reo-maori-greetings-handout.html' OR path LIKE '%te-reo-maori-greetings-handout.html';


-- Update metadata for: The Role of Haka Reading Comprehension | Mangakōtu
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Role of Haka Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/haka-comprehension-handout.html' OR path LIKE '%haka-comprehension-handout.html';


-- Update metadata for: Student Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Student Dashboard | Te Kete Ako')
WHERE path = 'public/handouts/student-dashboard.html' OR path LIKE '%student-dashboard.html';


-- Update metadata for: Tūrangawaewae Mapping | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tūrangawaewae Mapping | Te Kete Ako')
WHERE path = 'public/handouts/tūrangawaewae-mapping.html' OR path LIKE '%tūrangawaewae-mapping.html';


-- Update metadata for: Cultural Heroes Comprehension | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Heroes Comprehension | Te Kete Ako')
WHERE path = 'public/handouts/cultural-heroes-comprehension.html' OR path LIKE '%cultural-heroes-comprehension.html';


-- Update metadata for: The Writer's Toolkit: The PEEL Method
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: The PEEL Method')
WHERE path = 'public/handouts/writers-toolkit-peel-argument-handout.html' OR path LIKE '%writers-toolkit-peel-argument-handout.html';


-- Update metadata for: Multicultural New Zealand | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Multicultural New Zealand | Te Kete Ako')
WHERE path = 'public/handouts/multicultural-new-zealand.html' OR path LIKE '%multicultural-new-zealand.html';


-- Update metadata for: Sitemap
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Sitemap')
WHERE path = 'public/handouts/sitemap.html' OR path LIKE '%sitemap.html';


-- Update metadata for: Family Tree Exploration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Family Tree Exploration | Te Kete Ako')
WHERE path = 'public/handouts/family-tree-exploration.html' OR path LIKE '%family-tree-exploration.html';


-- Update metadata for: Value Systems Comparison | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Value Systems Comparison | Te Kete Ako')
WHERE path = 'public/handouts/value-systems-comparison.html' OR path LIKE '%value-systems-comparison.html';


-- Update metadata for: Kumara Storage Place Value | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Kumara Storage Place Value | Te Kete Ako')
WHERE path = 'public/handouts/kumara-storage-place-value.html' OR path LIKE '%kumara-storage-place-value.html';


-- Update metadata for: Technology Definition Challenge - Questioning Colo
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Technology Definition Challenge - Questioning Colonial Assumptions | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-technology-definition-challenge.html' OR path LIKE '%unit-2-technology-definition-challenge.html';


-- Update metadata for: Platforms | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Platforms | Te Kete Ako')
WHERE path = 'public/handouts/platforms.html' OR path LIKE '%platforms.html';


-- Update metadata for: Year 9 Starter Pack: Essential Skills for High Sch
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Year 9 Starter Pack: Essential Skills for High School Success - Te Kete Ako')
WHERE path = 'public/handouts/year-9-starter-pack-essential-skills.html' OR path LIKE '%year-9-starter-pack-essential-skills.html';


-- Update metadata for: Logical Fallacies Detection Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Logical Fallacies Detection Guide | Te Kete Ako')
WHERE path = 'public/handouts/logical-fallacies-detection-guide.html' OR path LIKE '%logical-fallacies-detection-guide.html';


-- Update metadata for: Garden Plot Measurement | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Garden Plot Measurement | Te Kete Ako')
WHERE path = 'public/handouts/garden-plot-measurement.html' OR path LIKE '%garden-plot-measurement.html';


-- Update metadata for: Children Rights Responsibilities | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Children Rights Responsibilities | Te Kete Ako')
WHERE path = 'public/handouts/children-rights-responsibilities.html' OR path LIKE '%children-rights-responsibilities.html';


-- Update metadata for: Cultural Safety Checklists for Classroom Discussio
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Safety Checklists for Classroom Discussions - Te Kete Ako')
WHERE path = 'public/handouts/cultural-safety-checklists-for-classroom-discussions.html' OR path LIKE '%cultural-safety-checklists-for-classroom-discussions.html';


-- Update metadata for: Resource Allocation Algebra | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Resource Allocation Algebra | Te Kete Ako')
WHERE path = 'public/handouts/resource-allocation-algebra.html' OR path LIKE '%resource-allocation-algebra.html';


-- Update metadata for: Microplastics Reading Comprehension | Mangakōtukut
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Microplastics Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/microplastics-comprehension-handout.html' OR path LIKE '%microplastics-comprehension-handout.html';


-- Update metadata for: Mathematics and Statistics Curriculum Alignment | 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Mathematics and Statistics Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/handouts/curriculum-mathematics.html' OR path LIKE '%curriculum-mathematics.html';


-- Update metadata for: Housing Affordability Reading Comprehension | Mang
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Housing Affordability Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/housing-affordability-comprehension-handout.html' OR path LIKE '%housing-affordability-comprehension-handout.html';


-- Update metadata for: Urban Māori Identity | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Urban Māori Identity | Te Kete Ako')
WHERE path = 'public/handouts/urban-maori-identity.html' OR path LIKE '%urban-maori-identity.html';


-- Update metadata for: How Economy Works | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'How Economy Works | Te Kete Ako')
WHERE path = 'public/handouts/how-economy-works.html' OR path LIKE '%how-economy-works.html';


-- Update metadata for: Oral Storytelling Handout | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Oral Storytelling Handout | Te Kete Ako')
WHERE path = 'public/handouts/oral-storytelling-handout.html' OR path LIKE '%oral-storytelling-handout.html';


-- Update metadata for: Bar Graph Worksheet
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Bar Graph Worksheet')
WHERE path = 'public/handouts/bar-graph-handout.html' OR path LIKE '%bar-graph-handout.html';


-- Update metadata for: Workplace Readiness with Cultural Competency
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Workplace Readiness with Cultural Competency')
WHERE path = 'public/handouts/workplace-readiness-with-cultural-competency.html' OR path LIKE '%workplace-readiness-with-cultural-competency.html';


-- Update metadata for: Population Trends Analysis | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Population Trends Analysis | Te Kete Ako')
WHERE path = 'public/handouts/population-trends-analysis.html' OR path LIKE '%population-trends-analysis.html';


-- Update metadata for: The Future of Tourism Reading Comprehension | Mang
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Future of Tourism Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/future-of-tourism-comprehension-handout.html' OR path LIKE '%future-of-tourism-comprehension-handout.html';


-- Update metadata for: Māori Data Sovereignty | Mangakōtukutuku College
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Māori Data Sovereignty | Mangakōtukutuku College')
WHERE path = 'public/handouts/data-sovereignty-maori.html' OR path LIKE '%data-sovereignty-maori.html';


-- Update metadata for: Recipe Scaling Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Recipe Scaling Mathematics | Te Kete Ako')
WHERE path = 'public/handouts/recipe-scaling-mathematics.html' OR path LIKE '%recipe-scaling-mathematics.html';


-- Update metadata for: Digital Equity & Accessibility - Mobile Learning G
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Digital Equity & Accessibility - Mobile Learning Guide')
WHERE path = 'public/handouts/chromebook-optimized-mobile-learning-guide.html' OR path LIKE '%chromebook-optimized-mobile-learning-guide.html';


-- Update metadata for: Tukutuku Puzzle Challenges | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Puzzle Challenges | Te Kete Ako')
WHERE path = 'public/handouts/tukutuku-puzzle-challenges.html' OR path LIKE '%tukutuku-puzzle-challenges.html';


-- Update metadata for: Food Chains & Māori Sustainable Practices - Worksh
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Food Chains & Māori Sustainable Practices - Worksheet | Year 8 Science')
WHERE path = 'public/handouts/y8-science-food-chains-sustainability.html' OR path LIKE '%y8-science-food-chains-sustainability.html';


-- Update metadata for: Project Assessment Rubric | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Project Assessment Rubric | Te Kete Ako')
WHERE path = 'public/handouts/assessment-rubric.html' OR path LIKE '%assessment-rubric.html';


-- Update metadata for: The Gig Economy Reading Comprehension | Mangakōtuk
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Gig Economy Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/gig-economy-comprehension-handout.html' OR path LIKE '%gig-economy-comprehension-handout.html';


-- Update metadata for: Body Measurement Traditional | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Body Measurement Traditional | Te Kete Ako')
WHERE path = 'public/handouts/body-measurement-traditional.html' OR path LIKE '%body-measurement-traditional.html';


-- Update metadata for: Ranginui Walker: A Life of Integrity - Student Han
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Ranginui Walker: A Life of Integrity - Student Handout | Te Kete Ako')
WHERE path = 'public/handouts/walker-lesson-1-1-student-handout.html' OR path LIKE '%walker-lesson-1-1-student-handout.html';


-- Update metadata for: YouTube Educational Library | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'YouTube Educational Library | Te Kete Ako')
WHERE path = 'public/handouts/youtube-library.html' OR path LIKE '%youtube-library.html';


-- Update metadata for: Register | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Register | Te Kete Ako')
WHERE path = 'public/handouts/register.html' OR path LIKE '%register.html';


-- Update metadata for: The Strategy of the Land Wars | Mangakōtukutuku Co
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Strategy of the Land Wars | Mangakōtukutuku College')
WHERE path = 'public/handouts/land-wars-strategy.html' OR path LIKE '%land-wars-strategy.html';


-- Update metadata for: Financial Literacy with Māori Economic Principles 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Financial Literacy with Māori Economic Principles - Te Kete Ako')
WHERE path = 'public/handouts/financial-literacy-with-māori-economic-principles.html' OR path LIKE '%financial-literacy-with-māori-economic-principles.html';


-- Update metadata for: Family Tree Writing | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Family Tree Writing | Te Kete Ako')
WHERE path = 'public/handouts/family-tree-writing.html' OR path LIKE '%family-tree-writing.html';


-- Update metadata for: Project Submission | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Project Submission | Te Kete Ako')
WHERE path = 'public/handouts/project-submission.html' OR path LIKE '%project-submission.html';


-- Update metadata for: Cultural Decision Making Traditions | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Decision Making Traditions | Te Kete Ako')
WHERE path = 'public/handouts/cultural-decision-making-traditions.html' OR path LIKE '%cultural-decision-making-traditions.html';


-- Update metadata for: Page Not Found - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Page Not Found - Te Kete Ako')
WHERE path = 'public/handouts/404.html' OR path LIKE '%404.html';


-- Update metadata for: Handouts | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handouts | Te Kete Ako')
WHERE path = 'public/handouts/handouts.html' OR path LIKE '%handouts.html';


-- Update metadata for: Geometric Patterns in Māori Art and Architecture
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Geometric Patterns in Māori Art and Architecture')
WHERE path = 'public/handouts/geometric-patterns-in-māori-art-and-architecture.html' OR path LIKE '%geometric-patterns-in-māori-art-and-architecture.html';


-- Update metadata for: Modern Applications Connection Guide - Ancient Wis
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Modern Applications Connection Guide - Ancient Wisdom, Modern Solutions | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-modern-applications-connection.html' OR path LIKE '%unit-2-modern-applications-connection.html';


-- Update metadata for: Traditional Science: Primary Sources - Māori Knowl
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Traditional Science: Primary Sources - Māori Knowledge Systems | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-traditional-science-primary-sources.html' OR path LIKE '%unit-2-traditional-science-primary-sources.html';


-- Update metadata for: Interactive Curriculum Browser | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Interactive Curriculum Browser | Te Kete Ako')
WHERE path = 'public/handouts/curriculum-v2.html' OR path LIKE '%curriculum-v2.html';


-- Update metadata for: Iwi Economics Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Iwi Economics Mathematics | Te Kete Ako')
WHERE path = 'public/handouts/iwi-economics-mathematics.html' OR path LIKE '%iwi-economics-mathematics.html';


-- Update metadata for: Subjects | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Subjects | Te Kete Ako')
WHERE path = 'public/handouts/subjects.html' OR path LIKE '%subjects.html';


-- Update metadata for: Reset Password | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Reset Password | Te Kete Ako')
WHERE path = 'public/handouts/reset-password.html' OR path LIKE '%reset-password.html';


-- Update metadata for: Login | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Login | Te Kete Ako')
WHERE path = 'public/handouts/login.html' OR path LIKE '%login.html';


-- Update metadata for: Data Visualization of Cultural Demographics
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Data Visualization of Cultural Demographics')
WHERE path = 'public/handouts/data-visualization-of-cultural-demographics.html' OR path LIKE '%data-visualization-of-cultural-demographics.html';


-- Update metadata for: Ceremonial Circle Geometry | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Ceremonial Circle Geometry | Te Kete Ako')
WHERE path = 'public/handouts/ceremonial-circle-geometry.html' OR path LIKE '%ceremonial-circle-geometry.html';


-- Update metadata for: Statistical Analysis of Treaty Settlement Data
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Statistical Analysis of Treaty Settlement Data')
WHERE path = 'public/handouts/statistical-analysis-of-treaty-settlement-data.html' OR path LIKE '%statistical-analysis-of-treaty-settlement-data.html';


-- Update metadata for: Handout: The Treaty of Waitangi
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: The Treaty of Waitangi')
WHERE path = 'public/handouts/treaty-of-waitangi-handout.html' OR path LIKE '%treaty-of-waitangi-handout.html';


-- Update metadata for: Project Planning Template - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Project Planning Template - Y8 Statistics')
WHERE path = 'public/handouts/y8-statistics-project-planning-template.html' OR path LIKE '%y8-statistics-project-planning-template.html';


-- Update metadata for: Teacher Analytics Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Teacher Analytics Guide | Te Kete Ako')
WHERE path = 'public/handouts/teacher-guide.html' OR path LIKE '%teacher-guide.html';


-- Update metadata for: Cultural STEM Assessment Rubric | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural STEM Assessment Rubric | Te Kete Ako')
WHERE path = 'public/handouts/cultural-stem-assessment-rubric.html' OR path LIKE '%cultural-stem-assessment-rubric.html';


-- Update metadata for: Resource Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Resource Hub | Te Kete Ako')
WHERE path = 'public/handouts/resource-hub.html' OR path LIKE '%resource-hub.html';


-- Update metadata for: Financial Literacy Reading Comprehension | Mangakō
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Financial Literacy Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/financial-literacy-comprehension-handout.html' OR path LIKE '%financial-literacy-comprehension-handout.html';


-- Update metadata for: Native Bird Lifecycles | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Native Bird Lifecycles | Te Kete Ako')
WHERE path = 'public/handouts/native-bird-lifecycles.html' OR path LIKE '%native-bird-lifecycles.html';


-- Update metadata for: Community Helpers Study | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Community Helpers Study | Te Kete Ako')
WHERE path = 'public/handouts/community-helpers-study.html' OR path LIKE '%community-helpers-study.html';


-- Update metadata for: Traditional Materials Science | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Traditional Materials Science | Te Kete Ako')
WHERE path = 'public/handouts/traditional-materials-science.html' OR path LIKE '%traditional-materials-science.html';


-- Update metadata for: Coding Projects Inspired by Māori Patterns
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Coding Projects Inspired by Māori Patterns')
WHERE path = 'public/handouts/coding-projects-inspired-by-māori-patterns.html' OR path LIKE '%coding-projects-inspired-by-māori-patterns.html';


-- Update metadata for: Walker Unit - Teacher's Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Walker Unit - Teacher''s Guide | Te Kete Ako')
WHERE path = 'public/handouts/walker-unit-overview-teacher-guide.html' OR path LIKE '%walker-unit-overview-teacher-guide.html';


-- Update metadata for: Class Data Collection Survey - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Class Data Collection Survey - Y8 Statistics')
WHERE path = 'public/handouts/y8-statistics-class-survey-template.html' OR path LIKE '%y8-statistics-class-survey-template.html';


-- Update metadata for: The Dawn Raids Reading Comprehension | Mangakōtuku
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Dawn Raids Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/dawn-raids-comprehension-handout.html' OR path LIKE '%dawn-raids-comprehension-handout.html';


-- Update metadata for: Te Reo Maths Glossary - Bilingual Mathematical Ter
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Maths Glossary - Bilingual Mathematical Terms - Te Kete Ako')
WHERE path = 'public/handouts/te-reo-maths-glossary-bilingual-alpha.html' OR path LIKE '%te-reo-maths-glossary-bilingual-alpha.html';


-- Update metadata for: Maramataka Time Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Maramataka Time Mathematics | Te Kete Ako')
WHERE path = 'public/handouts/maramataka-time-mathematics.html' OR path LIKE '%maramataka-time-mathematics.html';


-- Update metadata for: The Writer's Toolkit: Analogy & Metaphor | Mangakō
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Analogy & Metaphor | Mangakōtukutuku College')
WHERE path = 'public/handouts/writers-toolkit-analogy-handout.html' OR path LIKE '%writers-toolkit-analogy-handout.html';


-- Update metadata for: Te Kete Ako Dashboard | Your Teaching Resources
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako Dashboard | Your Teaching Resources')
WHERE path = 'public/handouts/dashboard.html' OR path LIKE '%dashboard.html';


-- Update metadata for: Media Literacy: Navigating the Digital World | Te 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Media Literacy: Navigating the Digital World | Te Kete Ako')
WHERE path = 'public/handouts/media-literacy-comprehension-handout.v2.html' OR path LIKE '%media-literacy-comprehension-handout.v2.html';


-- Update metadata for: Sustainable Energy Solutions from Traditional Know
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Sustainable Energy Solutions from Traditional Knowledge')
WHERE path = 'public/handouts/sustainable-energy-solutions-from-traditional-knowledge.html' OR path LIKE '%sustainable-energy-solutions-from-traditional-knowledge.html';


-- Update metadata for: Year 9 Starter Pack: Essential Skills for High Sch
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Year 9 Starter Pack: Essential Skills for High School Success - Te Kete Ako')
WHERE path = 'public/handouts/year-9-starter-pack-alpha-build.html' OR path LIKE '%year-9-starter-pack-alpha-build.html';


-- Update metadata for: Economic Justice Deep Dive - Understanding Wealth,
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Economic Justice Deep Dive - Understanding Wealth, Power & Change | Te Kete Ako')
WHERE path = 'public/handouts/economic-justice-deep-dive-comprehension.html' OR path LIKE '%economic-justice-deep-dive-comprehension.html';


-- Update metadata for: Physics Of Traditional Games | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Physics Of Traditional Games | Te Kete Ako')
WHERE path = 'public/handouts/physics-of-traditional-games.html' OR path LIKE '%physics-of-traditional-games.html';


-- Update metadata for: Star Compass Worksheet (Y8 Geography)
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Star Compass Worksheet (Y8 Geography)')
WHERE path = 'public/handouts/star-compass-worksheet.html' OR path LIKE '%star-compass-worksheet.html';


-- Update metadata for: AI Art Ethics Reading Comprehension
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'AI Art Ethics Reading Comprehension')
WHERE path = 'public/handouts/ai-art-ethics-comprehension-handout.html' OR path LIKE '%ai-art-ethics-comprehension-handout.html';


-- Update metadata for: Author's Purpose: Inform
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Author''s Purpose: Inform')
WHERE path = 'public/handouts/authors-purpose-inform-handout.html' OR path LIKE '%authors-purpose-inform-handout.html';


-- Update metadata for: Figurative Language Handout | Mangakōtukutuku Coll
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Figurative Language Handout | Mangakōtukutuku College')
WHERE path = 'public/handouts/figurative-language-handout.html' OR path LIKE '%figurative-language-handout.html';


-- Update metadata for: PPDAC Cycle Worksheet - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'PPDAC Cycle Worksheet - Y8 Statistics')
WHERE path = 'public/handouts/y8-statistics-ppdac-cycle-worksheet.html' OR path LIKE '%y8-statistics-ppdac-cycle-worksheet.html';


-- Update metadata for: Simple Login | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Simple Login | Te Kete Ako')
WHERE path = 'public/handouts/login-simple.html' OR path LIKE '%login-simple.html';


-- Update metadata for: Cognitive Biases | Critical Literacy Unit
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cognitive Biases | Critical Literacy Unit')
WHERE path = 'public/handouts/cognitive-biases-comprehension-handout.html' OR path LIKE '%cognitive-biases-comprehension-handout.html';


-- Update metadata for: Waka Construction Geometry | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Waka Construction Geometry | Te Kete Ako')
WHERE path = 'public/handouts/waka-construction-geometry.html' OR path LIKE '%waka-construction-geometry.html';


-- Update metadata for: Graph Creation Template - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Graph Creation Template - Y8 Statistics')
WHERE path = 'public/handouts/y8-statistics-graph-creation-template.html' OR path LIKE '%y8-statistics-graph-creation-template.html';


-- Update metadata for: YouTube Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'YouTube Resources | Te Kete Ako')
WHERE path = 'public/handouts/youtube.html' OR path LIKE '%youtube.html';


-- Update metadata for: English | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'English | Te Kete Ako')
WHERE path = 'public/handouts/english.html' OR path LIKE '%english.html';


-- Update metadata for: Year 9 Starter Pack: Essential Skills for High Sch
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Year 9 Starter Pack: Essential Skills for High School Success - Te Kete Ako')
WHERE path = 'public/handouts/year-9-starter-pack-essential-skills-for-high-school-success.html' OR path LIKE '%year-9-starter-pack-essential-skills-for-high-school-success.html';


-- Update metadata for: Local Area Exploration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Local Area Exploration | Te Kete Ako')
WHERE path = 'public/handouts/local-area-exploration.html' OR path LIKE '%local-area-exploration.html';


-- Update metadata for: Kaitiakitanga Kids | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Kaitiakitanga Kids | Te Kete Ako')
WHERE path = 'public/handouts/kaitiakitanga-kids.html' OR path LIKE '%kaitiakitanga-kids.html';


-- Update metadata for: Tukutuku Reading Comprehension | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Reading Comprehension | Te Kete Ako')
WHERE path = 'public/handouts/tukutuku-reading-comprehension.html' OR path LIKE '%tukutuku-reading-comprehension.html';


-- Update metadata for: Urban Māori Identity Formation - A New Culture in 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Urban Māori Identity Formation - A New Culture in the City | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-urban-identity-formation.html' OR path LIKE '%unit-2-urban-identity-formation.html';


-- Update metadata for: Performance Dashboard - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Performance Dashboard - Te Kete Ako')
WHERE path = 'public/handouts/performance-dashboard.html' OR path LIKE '%performance-dashboard.html';


-- Update metadata for: Sports Data Analysis Worksheet - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Sports Data Analysis Worksheet - Y8 Statistics')
WHERE path = 'public/handouts/y8-statistics-sports-data-analysis.html' OR path LIKE '%y8-statistics-sports-data-analysis.html';


-- Update metadata for: Māori Battalion Legacy Expansion - Service, Identi
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Māori Battalion Legacy Expansion - Service, Identity, and Urbanisation | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-maori-battalion-legacy.html' OR path LIKE '%unit-2-maori-battalion-legacy.html';


-- Update metadata for: Handout: NZ Housing Crisis
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: NZ Housing Crisis')
WHERE path = 'public/handouts/nz-housing-crisis-handout.html' OR path LIKE '%nz-housing-crisis-handout.html';


-- Update metadata for: Ranginui Walker Biography | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Ranginui Walker Biography | Te Kete Ako')
WHERE path = 'public/handouts/walker-ranginui-biography.html' OR path LIKE '%walker-ranginui-biography.html';


-- Update metadata for: Register | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Register | Te Kete Ako')
WHERE path = 'public/handouts/register-simple.html' OR path LIKE '%register-simple.html';


-- Update metadata for: NCEA Level 1 Literacy & Numeracy Must-Knows - Te K
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 1',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'NCEA Level 1 Literacy & Numeracy Must-Knows - Te Kete Ako')
WHERE path = 'public/handouts/ncea-level-1-literacy-and-numeracy-must-knows.html' OR path LIKE '%ncea-level-1-literacy-and-numeracy-must-knows.html';


-- Update metadata for: The Writer's Toolkit: Formal vs. Informal Tone
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Formal vs. Informal Tone')
WHERE path = 'public/handouts/writers-toolkit-tone-handout.html' OR path LIKE '%writers-toolkit-tone-handout.html';


-- Update metadata for: Innovation Domains Comparison - Māori vs. Modern S
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Innovation Domains Comparison - Māori vs. Modern Systems | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-innovation-domains-comparison.html' OR path LIKE '%unit-2-innovation-domains-comparison.html';


-- Update metadata for: Marae Shapes Geometry | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Marae Shapes Geometry | Te Kete Ako')
WHERE path = 'public/handouts/marae-shapes-geometry.html' OR path LIKE '%marae-shapes-geometry.html';


-- Update metadata for: Iwi Population Graphs | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Iwi Population Graphs | Te Kete Ako')
WHERE path = 'public/handouts/iwi-population-graphs.html' OR path LIKE '%iwi-population-graphs.html';


-- Update metadata for: English/Literacy Progression Framework - Culturall
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'English/Literacy Progression Framework - Culturally Responsive Communication | Mangakōtukutuku College')
WHERE path = 'public/handouts/english-literacy-progression-framework.html' OR path LIKE '%english-literacy-progression-framework.html';


-- Update metadata for: The Writer's Toolkit: Powerful Conclusions
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Powerful Conclusions')
WHERE path = 'public/handouts/writers-toolkit-conclusion-handout.html' OR path LIKE '%writers-toolkit-conclusion-handout.html';


-- Update metadata for: The Writer's Toolkit: Rhetorical Devices
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Rhetorical Devices')
WHERE path = 'public/handouts/writers-toolkit-rhetorical-devices-handout.html' OR path LIKE '%writers-toolkit-rhetorical-devices-handout.html';


-- Update metadata for: Leadership Profiles: Aotearoa Wars - Māori Strateg
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Leadership Profiles: Aotearoa Wars - Māori Strategists and Visionaries | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-leadership-profiles-wars.html' OR path LIKE '%unit-2-leadership-profiles-wars.html';


-- Update metadata for: Traditional Navigation & Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Traditional Navigation & Mathematics | Te Kete Ako')
WHERE path = 'public/handouts/traditional-navigation-mathematics-handout.html' OR path LIKE '%traditional-navigation-mathematics-handout.html';


-- Update metadata for: Nz Geography Basics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Nz Geography Basics | Te Kete Ako')
WHERE path = 'public/handouts/nz-geography-basics.html' OR path LIKE '%nz-geography-basics.html';


-- Update metadata for: Handout: Climate Change in Aotearoa
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Climate Change in Aotearoa')
WHERE path = 'public/handouts/climate-change-aotearoa-handout.html' OR path LIKE '%climate-change-aotearoa-handout.html';


-- Update metadata for: Teacher Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Teacher Dashboard | Te Kete Ako')
WHERE path = 'public/handouts/teacher-dashboard.html' OR path LIKE '%teacher-dashboard.html';


-- Update metadata for: Tukutuku Station Questions | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Station Questions | Te Kete Ako')
WHERE path = 'public/handouts/tukutuku-station-questions.html' OR path LIKE '%tukutuku-station-questions.html';


-- Update metadata for: Unit Plans | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Unit Plans | Te Kete Ako')
WHERE path = 'public/handouts/units.html' OR path LIKE '%units.html';


-- Update metadata for: English Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'English Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/handouts/curriculum-english.html' OR path LIKE '%curriculum-english.html';


-- Update metadata for: Discover Orphans
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Discover Orphans')
WHERE path = 'public/handouts/orphans.html' OR path LIKE '%orphans.html';


-- Update metadata for: Handout: Māori Navigation
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Māori Navigation')
WHERE path = 'public/handouts/maori-navigation-wayfinding-handout.html' OR path LIKE '%maori-navigation-wayfinding-handout.html';


-- Update metadata for: 🤖 DeepSeek + GraphRAG Terminal | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), '🤖 DeepSeek + GraphRAG Terminal | Te Kete Ako')
WHERE path = 'public/handouts/deepseek-graphrag-terminal.html' OR path LIKE '%deepseek-graphrag-terminal.html';


-- Update metadata for: The Writer's Toolkit: Crafting Hooks
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Crafting Hooks')
WHERE path = 'public/handouts/writers-toolkit-hook-handout.html' OR path LIKE '%writers-toolkit-hook-handout.html';


-- Update metadata for: Media Literacy Reading Comprehension | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Media Literacy Reading Comprehension | Te Kete Ako')
WHERE path = 'public/handouts/media-literacy-comprehension-handout.html' OR path LIKE '%media-literacy-comprehension-handout.html';


-- Update metadata for: Arguments of Tino Rangatiratanga
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Arguments of Tino Rangatiratanga')
WHERE path = 'public/handouts/arguments-of-tino-rangatiratanga-handout.html' OR path LIKE '%arguments-of-tino-rangatiratanga-handout.html';


-- Update metadata for: Unit Hub | Critical Thinking Skills: Media Literac
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Unit Hub | Critical Thinking Skills: Media Literacy & Information Analysis | Te Kete Ako - Postcolonial Social Studies')
WHERE path = 'public/handouts/critical-thinking-unit.html' OR path LIKE '%critical-thinking-unit.html';


-- Update metadata for: The Writer's Toolkit: Suspense & Foreshadowing
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Suspense & Foreshadowing')
WHERE path = 'public/handouts/writers-toolkit-suspense-handout.html' OR path LIKE '%writers-toolkit-suspense-handout.html';


-- Update metadata for: Economic Choices Basics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Economic Choices Basics | Te Kete Ako')
WHERE path = 'public/handouts/economic-choices-basics.html' OR path LIKE '%economic-choices-basics.html';


-- Update metadata for: Māori Military Innovation - Strategy and Technolog
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Māori Military Innovation - Strategy and Technology in the Aotearoa Wars | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-military-innovation-study.html' OR path LIKE '%unit-2-military-innovation-study.html';


-- Update metadata for: Analysing Political Cartoons
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Analysing Political Cartoons')
WHERE path = 'public/handouts/political-cartoon-analysis-handout.html' OR path LIKE '%political-cartoon-analysis-handout.html';


-- Update metadata for: Lesson Template: [Te Reo Name] - [English Name] | 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson Template: [Te Reo Name] - [English Name] | Mangakōtukutuku College')
WHERE path = 'public/handouts/lesson-template.html' OR path LIKE '%lesson-template.html';


-- Update metadata for: Digital Pūrākau | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Digital Pūrākau | Te Kete Ako')
WHERE path = 'public/handouts/digital-purakau.html' OR path LIKE '%digital-purakau.html';


-- Update metadata for: NZ Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/handouts/curriculum-alignment.html' OR path LIKE '%curriculum-alignment.html';


-- Update metadata for: Fortification Engineering - A Technical Analysis o
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Fortification Engineering - A Technical Analysis of Pā Design | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-fortification-engineering.html' OR path LIKE '%unit-2-fortification-engineering.html';


-- Update metadata for: Nz Geological Processes | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Nz Geological Processes | Te Kete Ako')
WHERE path = 'public/handouts/nz-geological-processes.html' OR path LIKE '%nz-geological-processes.html';


-- Update metadata for: Forest Ecosystem Connections | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Forest Ecosystem Connections | Te Kete Ako')
WHERE path = 'public/handouts/forest-ecosystem-connections.html' OR path LIKE '%forest-ecosystem-connections.html';


-- Update metadata for: Story To Life Connections | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Story To Life Connections | Te Kete Ako')
WHERE path = 'public/handouts/story-to-life-connections.html' OR path LIKE '%story-to-life-connections.html';


-- Update metadata for: Pre-Colonial Innovation
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Pre-Colonial Innovation')
WHERE path = 'public/handouts/pre-colonial-innovation.html' OR path LIKE '%pre-colonial-innovation.html';


-- Update metadata for: Family Data Collection | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Family Data Collection | Te Kete Ako')
WHERE path = 'public/handouts/family-data-collection.html' OR path LIKE '%family-data-collection.html';


-- Update metadata for: Probability and Chance in Māori Games
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Probability and Chance in Māori Games')
WHERE path = 'public/handouts/probability-and-chance-in-māori-games.html' OR path LIKE '%probability-and-chance-in-māori-games.html';


-- Update metadata for: Key Cases of the Waitangi Tribunal
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Key Cases of the Waitangi Tribunal')
WHERE path = 'public/handouts/waitangi-tribunal-cases.html' OR path LIKE '%waitangi-tribunal-cases.html';


-- Update metadata for: Cultural Preservation Essays | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Preservation Essays | Te Kete Ako')
WHERE path = 'public/handouts/cultural-preservation-essays.html' OR path LIKE '%cultural-preservation-essays.html';


-- Update metadata for: Social Sciences Progression Framework - Years 7-13
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Social Sciences Progression Framework - Years 7-13 | Mangakōtukutuku College')
WHERE path = 'public/handouts/social-sciences-progression-framework.html' OR path LIKE '%social-sciences-progression-framework.html';


-- Update metadata for: Plate Tectonics Reading Comprehension
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Plate Tectonics Reading Comprehension')
WHERE path = 'public/handouts/plate-tectonics-comprehension-handout.html' OR path LIKE '%plate-tectonics-comprehension-handout.html';


-- Update metadata for: Cultural Safety Checklists for Classroom Discussio
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Safety Checklists for Classroom Discussions - Te Kete Ako')
WHERE path = 'public/handouts/cultural-safety-classroom-checklists-alpha.html' OR path LIKE '%cultural-safety-classroom-checklists-alpha.html';


-- Update metadata for: Cultural Identity Deep Dive Comprehension | Te Ket
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Identity Deep Dive Comprehension | Te Kete Ako')
WHERE path = 'public/handouts/cultural-identity-deep-dive-comprehension.html' OR path LIKE '%cultural-identity-deep-dive-comprehension.html';


-- Update metadata for: Traditional Counting Systems | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Traditional Counting Systems | Te Kete Ako')
WHERE path = 'public/handouts/traditional-counting-systems.html' OR path LIKE '%traditional-counting-systems.html';


-- Update metadata for: Tukutuku Escape Room | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Escape Room | Te Kete Ako')
WHERE path = 'public/handouts/tukutuku-escape-room.html' OR path LIKE '%tukutuku-escape-room.html';


-- Update metadata for: Personal Timeline Activity | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Personal Timeline Activity | Te Kete Ako')
WHERE path = 'public/handouts/personal-timeline-activity.html' OR path LIKE '%personal-timeline-activity.html';


-- Update metadata for: Welcome to Te Kete Ako | Educational Resources for
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Welcome to Te Kete Ako | Educational Resources for New Zealand')
WHERE path = 'public/handouts/welcome.html' OR path LIKE '%welcome.html';


-- Update metadata for: Unit Plans | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Unit Plans | Te Kete Ako')
WHERE path = 'public/handouts/unit-plans.html' OR path LIKE '%unit-plans.html';


-- Update metadata for: Public Speaking with Cultural Confidence
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Public Speaking with Cultural Confidence')
WHERE path = 'public/handouts/public-speaking-with-cultural-confidence.html' OR path LIKE '%public-speaking-with-cultural-confidence.html';


-- Update metadata for: Environmental Text Analysis - Critical Literacy | 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Environmental Text Analysis - Critical Literacy | Mangakōtukutuku College')
WHERE path = 'public/handouts/environmental-text-analysis-handout.html' OR path LIKE '%environmental-text-analysis-handout.html';


-- Update metadata for: Ecosystem Survey Checklist (Y7)
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Ecosystem Survey Checklist (Y7)')
WHERE path = 'public/handouts/ecosystem-survey-checklist.html' OR path LIKE '%ecosystem-survey-checklist.html';


-- Update metadata for: Te Ao Māori | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Ao Māori | Te Kete Ako')
WHERE path = 'public/handouts/te-ao-maori.html' OR path LIKE '%te-ao-maori.html';


-- Update metadata for: Fire Making Energy | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Fire Making Energy | Te Kete Ako')
WHERE path = 'public/handouts/fire-making-energy.html' OR path LIKE '%fire-making-energy.html';


-- Update metadata for: Te Reo Wordle - Function Test
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Wordle - Function Test')
WHERE path = 'public/handouts/test-wordle-functions.html' OR path LIKE '%test-wordle-functions.html';


-- Update metadata for: Pre-Colonial Innovation Deep Dive - Understanding 
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Pre-Colonial Innovation Deep Dive - Understanding Māori Technology and Knowledge Systems | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-pre-colonial-innovation-deep-dive.html' OR path LIKE '%unit-2-pre-colonial-innovation-deep-dive.html';


-- Update metadata for: Misleading Graphs Reading Comprehension | Mangakōt
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Misleading Graphs Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/misleading-graphs-comprehension-handout.html' OR path LIKE '%misleading-graphs-comprehension-handout.html';


-- Update metadata for: Teaching Tools & Platforms | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Teaching Tools & Platforms | Te Kete Ako')
WHERE path = 'public/handouts/tools.html' OR path LIKE '%tools.html';


-- Update metadata for: Wars Strategy Analysis - Conventional vs. Guerrill
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Wars Strategy Analysis - Conventional vs. Guerrilla Warfare in Aotearoa | Te Kete Ako')
WHERE path = 'public/handouts/unit-2-wars-strategy-analysis.html' OR path LIKE '%unit-2-wars-strategy-analysis.html';


-- Update metadata for: Geometric Patterns in Māori Art Handout | Mangakōt
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Geometric Patterns in Māori Art Handout | Mangakōtukutuku College')
WHERE path = 'public/handouts/maori-geometric-patterns-handout.html' OR path LIKE '%maori-geometric-patterns-handout.html';


-- Update metadata for: Sustainable Technology Design Challenge | Mangakōt
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Sustainable Technology Design Challenge | Mangakōtukutuku College')
WHERE path = 'public/handouts/sustainable-technology-design-challenge.html' OR path LIKE '%sustainable-technology-design-challenge.html';


-- Update metadata for: Curriculum: Technology | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Technology | Te Kete Ako')
WHERE path = 'public/handouts/curriculum-technology.html' OR path LIKE '%curriculum-technology.html';


-- Update metadata for: Te Kete Ako | World's First AI-Enhanced Cultural E
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | World''s First AI-Enhanced Cultural Educational Platform')
WHERE path = 'public/handouts/index-new.html' OR path LIKE '%index-new.html';


-- Update metadata for: Life In The Past | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Life In The Past | Te Kete Ako')
WHERE path = 'public/handouts/life-in-the-past.html' OR path LIKE '%life-in-the-past.html';


-- Update metadata for: Te Kete Ako - Comprehensive Site Map
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Comprehensive Site Map')
WHERE path = 'public/handouts/sitemap-enhanced.html' OR path LIKE '%sitemap-enhanced.html';


-- Update metadata for: Data Types Sorting Activity - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Data Types Sorting Activity - Y8 Statistics')
WHERE path = 'public/handouts/y8-statistics-data-types-sorting.html' OR path LIKE '%y8-statistics-data-types-sorting.html';


-- Update metadata for: Food Security Through Traditional Knowledge System
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Food Security Through Traditional Knowledge Systems')
WHERE path = 'public/handouts/food-security-through-traditional-knowledge-systems.html' OR path LIKE '%food-security-through-traditional-knowledge-systems.html';


-- Update metadata for: Sustainable Fishing Equations | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Sustainable Fishing Equations | Te Kete Ako')
WHERE path = 'public/handouts/sustainable-fishing-equations.html' OR path LIKE '%sustainable-fishing-equations.html';


-- Update metadata for: Research Methods | Te Kete Ako Handout
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Research Methods | Te Kete Ako Handout')
WHERE path = 'public/handouts/research-methods-handout.html' OR path LIKE '%research-methods-handout.html';


-- Update metadata for: Garden Plot Science | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Garden Plot Science | Te Kete Ako')
WHERE path = 'public/handouts/garden-plot-science.html' OR path LIKE '%garden-plot-science.html';


-- Update metadata for: Classroom Leaderboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Classroom Leaderboard | Te Kete Ako')
WHERE path = 'public/handouts/classroom-leaderboard.html' OR path LIKE '%classroom-leaderboard.html';


-- Update metadata for: Te Reo Maori Foundational Concepts | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Maori Foundational Concepts | Te Kete Ako')
WHERE path = 'public/handouts/te-reo-maori-foundational-concepts.html' OR path LIKE '%te-reo-maori-foundational-concepts.html';


-- Update metadata for: Search | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Search | Te Kete Ako')
WHERE path = 'public/handouts/search.html' OR path LIKE '%search.html';


-- Update metadata for: Traditional Dye Chemistry | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Traditional Dye Chemistry | Te Kete Ako')
WHERE path = 'public/handouts/traditional-dye-chemistry.html' OR path LIKE '%traditional-dye-chemistry.html';


-- Update metadata for: Author's Purpose: Persuade | Mangakōtukutuku Colle
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Author''s Purpose: Persuade | Mangakōtukutuku College')
WHERE path = 'public/handouts/authors-purpose-persuade-handout.html' OR path LIKE '%authors-purpose-persuade-handout.html';


-- Update metadata for: Youth Vaping Reading Comprehension | Mangakōtukutu
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Youth Vaping Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/youth-vaping-comprehension-handout.html' OR path LIKE '%youth-vaping-comprehension-handout.html';


-- Update metadata for: Cultural Practice Explanation | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Practice Explanation | Te Kete Ako')
WHERE path = 'public/handouts/cultural-practice-explanation.html' OR path LIKE '%cultural-practice-explanation.html';


-- Update metadata for: Professional Dashboard - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Professional Dashboard - Te Kete Ako')
WHERE path = 'public/handouts/professional-dashboard.html' OR path LIKE '%professional-dashboard.html';


-- Update metadata for: Weather Prediction Tracking Sheet - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Weather Prediction Tracking Sheet - Y8 Statistics')
WHERE path = 'public/handouts/y8-statistics-probability-weather-tracking.html' OR path LIKE '%y8-statistics-probability-weather-tracking.html';


-- Update metadata for: Evidence Evaluation Framework | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Evidence Evaluation Framework | Te Kete Ako')
WHERE path = 'public/handouts/evidence-evaluation-framework.html' OR path LIKE '%evidence-evaluation-framework.html';


-- Update metadata for: Social Sciences Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Social Sciences Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/handouts/curriculum-social-sciences.html' OR path LIKE '%curriculum-social-sciences.html';


-- Update metadata for: Authentication Diagnostics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Authentication Diagnostics | Te Kete Ako')
WHERE path = 'public/handouts/auth-diagnostics.html' OR path LIKE '%auth-diagnostics.html';


-- Update metadata for: Te Kete Ako - Auth Test (8PM Ready)
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Auth Test (8PM Ready)')
WHERE path = 'public/handouts/auth-test.html' OR path LIKE '%auth-test.html';


-- Update metadata for: Community Needs Survey | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Community Needs Survey | Te Kete Ako')
WHERE path = 'public/handouts/community-needs-survey.html' OR path LIKE '%community-needs-survey.html';


-- Update metadata for: Mathematical Modeling of Ecological Systems
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Mathematical Modeling of Ecological Systems')
WHERE path = 'public/handouts/mathematical-modeling-of-ecological-systems.html' OR path LIKE '%mathematical-modeling-of-ecological-systems.html';


-- Update metadata for: Calculus Applications in Environmental Modeling
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Calculus Applications in Environmental Modeling')
WHERE path = 'public/handouts/calculus-applications-in-environmental-modeling.html' OR path LIKE '%calculus-applications-in-environmental-modeling.html';


-- Update metadata for: CARE Principles Evaluation Checklist (Y10 Digital 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'CARE Principles Evaluation Checklist (Y10 Digital Tech)')
WHERE path = 'public/handouts/care-principles-checklist.html' OR path LIKE '%care-principles-checklist.html';


-- Update metadata for: Chemistry of Traditional Māori Medicine | Te Kete 
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Chemistry of Traditional Māori Medicine | Te Kete Ako')
WHERE path = 'public/handouts/chemistry-of-traditional-māori-medicine.html' OR path LIKE '%chemistry-of-traditional-māori-medicine.html';


-- Update metadata for: Colonization Perspectives Handout | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Colonization Perspectives Handout | Te Kete Ako')
WHERE path = 'public/handouts/colonization-perspectives-handout.html' OR path LIKE '%colonization-perspectives-handout.html';


-- Update metadata for: Kaitiakitanga Field Journal (Y7)
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Kaitiakitanga Field Journal (Y7)')
WHERE path = 'public/handouts/kaitiakitanga-field-journal.html' OR path LIKE '%kaitiakitanga-field-journal.html';


-- Update metadata for: Curriculum: Health & PE | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Health & PE | Te Kete Ako')
WHERE path = 'public/handouts/curriculum-health-pe.html' OR path LIKE '%curriculum-health-pe.html';


-- Update metadata for: Cultural Celebrations Comparison | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Celebrations Comparison | Te Kete Ako')
WHERE path = 'public/handouts/cultural-celebrations-comparison.html' OR path LIKE '%cultural-celebrations-comparison.html';


-- Update metadata for: Games | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Games | Te Kete Ako')
WHERE path = 'public/handouts/games.html' OR path LIKE '%games.html';


-- Update metadata for: The Scientific Method Handout | Mangakōtukutuku Co
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Scientific Method Handout | Mangakōtukutuku College')
WHERE path = 'public/handouts/scientific-method-handout.html' OR path LIKE '%scientific-method-handout.html';


-- Update metadata for: My Kete | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'My Kete | Te Kete Ako')
WHERE path = 'public/handouts/my-kete.html' OR path LIKE '%my-kete.html';


-- Update metadata for: Weather Prediction Traditional | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Weather Prediction Traditional | Te Kete Ako')
WHERE path = 'public/handouts/weather-prediction-traditional.html' OR path LIKE '%weather-prediction-traditional.html';


-- Update metadata for: Analysing a Speech | Mangakōtukutuku College
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Analysing a Speech | Mangakōtukutuku College')
WHERE path = 'public/handouts/speech-analysis-handout.html' OR path LIKE '%speech-analysis-handout.html';


-- Update metadata for: Information Literacy in the Digital Age
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Information Literacy in the Digital Age')
WHERE path = 'public/handouts/information-literacy-in-the-digital-age.html' OR path LIKE '%information-literacy-in-the-digital-age.html';


-- Update metadata for: Investigation Station Cards - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Investigation Station Cards - Y8 Statistics')
WHERE path = 'public/handouts/y8-statistics-demographic-stations.html' OR path LIKE '%y8-statistics-demographic-stations.html';


-- Update metadata for: Educational Transformation | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Educational Transformation | Te Kete Ako')
WHERE path = 'public/handouts/educational-transformation-showcase.html' OR path LIKE '%educational-transformation-showcase.html';


-- Update metadata for: The Writer's Toolkit: Sentence Fluency | Mangakōtu
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Sentence Fluency | Mangakōtukutuku College')
WHERE path = 'public/handouts/writers-toolkit-fluency-handout.html' OR path LIKE '%writers-toolkit-fluency-handout.html';


-- Update metadata for: Environmental Impact Study | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Environmental Impact Study | Te Kete Ako')
WHERE path = 'public/handouts/environmental-impact-study.html' OR path LIKE '%environmental-impact-study.html';


-- Update metadata for: Persuasive Writing: Climate Action | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Persuasive Writing: Climate Action | Te Kete Ako')
WHERE path = 'public/handouts/y9-english-persuasive-climate.html' OR path LIKE '%y9-english-persuasive-climate.html';


-- Update metadata for: Probability Experiments Recording Sheet - Y8 Stati
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Probability Experiments Recording Sheet - Y8 Statistics')
WHERE path = 'public/handouts/y8-statistics-probability-experiments.html' OR path LIKE '%y8-statistics-probability-experiments.html';


-- Update metadata for: Sustainable Energy Systems | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Sustainable Energy Systems | Te Kete Ako')
WHERE path = 'public/handouts/sustainable-energy-systems.html' OR path LIKE '%sustainable-energy-systems.html';


-- Update metadata for: Ngā Tamatoa - The Young Warriors | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Ngā Tamatoa - The Young Warriors | Te Kete Ako')
WHERE path = 'public/handouts/nga-tamatoa-handout.html' OR path LIKE '%nga-tamatoa-handout.html';


-- Update metadata for: Weather Prediction Probability | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Weather Prediction Probability | Te Kete Ako')
WHERE path = 'public/handouts/weather-prediction-probability.html' OR path LIKE '%weather-prediction-probability.html';


-- Update metadata for: Schema Test
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Schema Test')
WHERE path = 'public/handouts/test-schema.html' OR path LIKE '%test-schema.html';


-- Update metadata for: Genetic Modification Reading Comprehension | Manga
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Genetic Modification Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/genetic-modification-comprehension-handout.html' OR path LIKE '%genetic-modification-comprehension-handout.html';


-- Update metadata for: Tukutuku Numeracy Problems | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Numeracy Problems | Te Kete Ako')
WHERE path = 'public/handouts/tukutuku-numeracy-problems.html' OR path LIKE '%tukutuku-numeracy-problems.html';


-- Update metadata for: The Writer's Toolkit: Informational Structures | M
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Informational Structures | Mangakōtukutuku College')
WHERE path = 'public/handouts/writers-toolkit-inform-structure-handout.html' OR path LIKE '%writers-toolkit-inform-structure-handout.html';


-- Update metadata for: Nz Evolution Examples | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Nz Evolution Examples | Te Kete Ako')
WHERE path = 'public/handouts/nz-evolution-examples.html' OR path LIKE '%nz-evolution-examples.html';


-- Update metadata for: Experiences | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Experiences | Te Kete Ako')
WHERE path = 'public/handouts/experiences.html' OR path LIKE '%experiences.html';


-- Update metadata for: 🎓 Teacher AI Intelligence Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), '🎓 Teacher AI Intelligence Hub | Te Kete Ako')
WHERE path = 'public/handouts/teacher-ai-intelligence-hub.html' OR path LIKE '%teacher-ai-intelligence-hub.html';


-- Update metadata for: Te Reo Maths Glossary (Key Terms in Māori & Englis
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Maths Glossary (Key Terms in Māori & English) - Te Kete Ako')
WHERE path = 'public/handouts/te-reo-maths-glossary-key-terms-in-māori-and-english.html' OR path LIKE '%te-reo-maths-glossary-key-terms-in-māori-and-english.html';


-- Update metadata for: Global Citizenship with Tangata Whenua Perspective
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Global Citizenship with Tangata Whenua Perspective')
WHERE path = 'public/handouts/global-citizenship-with-tangata-whenua-perspective.html' OR path LIKE '%global-citizenship-with-tangata-whenua-perspective.html';


-- Update metadata for: The Science of Sleep Reading Comprehension | Manga
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Science of Sleep Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/science-of-sleep-comprehension-handout.html' OR path LIKE '%science-of-sleep-comprehension-handout.html';


-- Update metadata for: Statistical Investigation Guide | Mangakōtukutuku 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Statistical Investigation Guide | Mangakōtukutuku College')
WHERE path = 'public/handouts/statistical-investigation-handout.html' OR path LIKE '%statistical-investigation-handout.html';


-- Update metadata for: Ka Whawhai Tonu Mātou - We Will Fight On | Te Kete
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Ka Whawhai Tonu Mātou - We Will Fight On | Te Kete Ako')
WHERE path = 'public/handouts/ka-whawhai-tonu-matou-handout.html' OR path LIKE '%ka-whawhai-tonu-matou-handout.html';


-- Update metadata for: Social Media and Cultural Identity
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Social Media and Cultural Identity')
WHERE path = 'public/handouts/social-media-and-cultural-identity.html' OR path LIKE '%social-media-and-cultural-identity.html';


-- Update metadata for: The Writer's Toolkit | Critical Literacy Unit
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit | Critical Literacy Unit')
WHERE path = 'public/handouts/toolkit.html' OR path LIKE '%toolkit.html';


-- Update metadata for: Māramataka Calendar Template (Y8 Statistics)
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Māramataka Calendar Template (Y8 Statistics)')
WHERE path = 'public/handouts/maramataka-calendar-template.html' OR path LIKE '%maramataka-calendar-template.html';


-- Update metadata for: Navigation Header | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Navigation Header | Te Kete Ako')
WHERE path = 'public/handouts/navigation_fix_standard_header.html' OR path LIKE '%navigation_fix_standard_header.html';


-- Update metadata for: Curriculum: Languages | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Languages | Te Kete Ako')
WHERE path = 'public/handouts/curriculum-languages.html' OR path LIKE '%curriculum-languages.html';


-- Update metadata for: Hangi Heat Transfer | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Hangi Heat Transfer | Te Kete Ako')
WHERE path = 'public/handouts/hangi-heat-transfer.html' OR path LIKE '%hangi-heat-transfer.html';


-- Update metadata for: Resource Sustainability Study | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Resource Sustainability Study | Te Kete Ako')
WHERE path = 'public/handouts/resource-sustainability-study.html' OR path LIKE '%resource-sustainability-study.html';


-- Update metadata for: Interactive Learning Demo | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Interactive Learning Demo | Te Kete Ako')
WHERE path = 'public/handouts/interactive-learning-demo.html' OR path LIKE '%interactive-learning-demo.html';


-- Update metadata for: DeepSeek Agent Test | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'DeepSeek Agent Test | Te Kete Ako')
WHERE path = 'public/handouts/deepseek-agent-test.html' OR path LIKE '%deepseek-agent-test.html';


-- Update metadata for: AI Impact Reading Comprehension | Mangakōtukutuku 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'AI Impact Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/handouts/ai-impact-comprehension-handout.html' OR path LIKE '%ai-impact-comprehension-handout.html';


-- Update metadata for: Biochemistry Traditional Medicine | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Biochemistry Traditional Medicine | Te Kete Ako')
WHERE path = 'public/handouts/biochemistry-traditional-medicine.html' OR path LIKE '%biochemistry-traditional-medicine.html';


-- Update metadata for: Student Handout - Māori Migration to Aotearoa | Ka
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Student Handout - Māori Migration to Aotearoa | Kaitiaki Aronui Generated')
WHERE path = 'public/handouts/kaitiaki-generated-migration-student-handout.html' OR path LIKE '%kaitiaki-generated-migration-student-handout.html';


-- Update metadata for: Unit Hub | Year 8 Systems: Decolonizing Power Stru
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Unit Hub | Year 8 Systems: Decolonizing Power Structures | Te Kete Ako - Postcolonial Social Studies')
WHERE path = 'public/handouts/y8-systems-unit.html' OR path LIKE '%y8-systems-unit.html';


-- Update metadata for: Endemic Species Adaptation | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Endemic Species Adaptation | Te Kete Ako')
WHERE path = 'public/handouts/endemic-species-adaptation.html' OR path LIKE '%endemic-species-adaptation.html';


-- Update metadata for: Symmetry Investigation Worksheet (Y7 Maths)
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Symmetry Investigation Worksheet (Y7 Maths)')
WHERE path = 'public/handouts/symmetry-investigation-sheet.html' OR path LIKE '%symmetry-investigation-sheet.html';


-- Update metadata for: Traditional Ecological Indicators Handout | Mangak
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Traditional Ecological Indicators Handout | Mangakōtukutuku College')
WHERE path = 'public/handouts/traditional-ecological-indicators-handout.html' OR path LIKE '%traditional-ecological-indicators-handout.html';


-- Update metadata for: Digital Citizenship Handout | Mangakōtukutuku Coll
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Digital Citizenship Handout | Mangakōtukutuku College')
WHERE path = 'public/handouts/digital-citizenship-handout.html' OR path LIKE '%digital-citizenship-handout.html';


-- Update metadata for: EXA.ai Resource Discovery | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'EXA.ai Resource Discovery | Te Kete Ako')
WHERE path = 'public/handouts/exa-search.html' OR path LIKE '%exa-search.html';


-- Update metadata for: Treaty Settlement Statistics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Treaty Settlement Statistics | Te Kete Ako')
WHERE path = 'public/handouts/treaty-settlement-statistics.html' OR path LIKE '%treaty-settlement-statistics.html';


-- Update metadata for: Virtual Marae Training Protocol | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Virtual Marae Training Protocol | Te Kete Ako')
WHERE path = 'public/handouts/virtual-marae.html' OR path LIKE '%virtual-marae.html';


-- Update metadata for: Community Action Project Brief | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Community Action Project Brief | Te Kete Ako')
WHERE path = 'public/handouts/project-brief.html' OR path LIKE '%project-brief.html';


-- Update metadata for: Lesson Plans | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plans | Te Kete Ako')
WHERE path = 'public/handouts/lessons.html' OR path LIKE '%lessons.html';


-- Update metadata for: Social Movements Introduction | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Social Movements Introduction | Te Kete Ako')
WHERE path = 'public/handouts/social-movements-introduction.html' OR path LIKE '%social-movements-introduction.html';


-- Update metadata for: Resource Discovery Hub - Te Kete Ako V2.5
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Resource Discovery Hub - Te Kete Ako V2.5')
WHERE path = 'public/handouts/resource-discovery-hub.html' OR path LIKE '%resource-discovery-hub.html';


-- Update metadata for: The Legacy of the Māori Battalion | Mangakōtukutuk
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Legacy of the Māori Battalion | Mangakōtukutuku College')
WHERE path = 'public/handouts/maori-battalion-legacy.html' OR path LIKE '%maori-battalion-legacy.html';


-- Update metadata for: The Writer's Toolkit: Show, Don't Tell | Mangakōtu
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Show, Don''t Tell | Mangakōtukutuku College')
WHERE path = 'public/handouts/writers-toolkit-show-dont-tell-handout.html' OR path LIKE '%writers-toolkit-show-dont-tell-handout.html';


-- Update metadata for: Year 10 Mathematics - Cultural Geometry Unit | Kai
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Year 10 Mathematics - Cultural Geometry Unit | Kaitiaki Aronui Generated')
WHERE path = 'public/handouts/unit-plans/kaitiaki-generated-y10-math-cultural-geometry.html' OR path LIKE '%kaitiaki-generated-y10-math-cultural-geometry.html';


-- Update metadata for: Cultural-Mathematical Assessment Rubric | Kaitiaki
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural-Mathematical Assessment Rubric | Kaitiaki Aronui Generated')
WHERE path = 'public/handouts/assessments/kaitiaki-generated-cultural-mathematics-rubric.html' OR path LIKE '%kaitiaki-generated-cultural-mathematics-rubric.html';


-- Update metadata for: Do Now: Whakataukī Wisdom | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Do Now: Whakataukī Wisdom | Te Kete Ako')
WHERE path = 'public/handouts/do-now-activities/whakatauki-wisdom-do-now.html' OR path LIKE '%whakatauki-wisdom-do-now.html';


-- Update metadata for: Do Now: Analyzing the Polynesian Panthers
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Do Now: Analyzing the Polynesian Panthers')
WHERE path = 'public/handouts/do-now-activities/panther-primary-source-do-now.html' OR path LIKE '%panther-primary-source-do-now.html';


-- Update metadata for: Do Now: Political Cartoon Analysis
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Do Now: Political Cartoon Analysis')
WHERE path = 'public/handouts/do-now-activities/political-cartoon-analysis-do-now.html' OR path LIKE '%political-cartoon-analysis-do-now.html';


-- Update metadata for: Pounamu Trading Worksheet | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Pounamu Trading Worksheet | Te Kete Ako')
WHERE path = 'public/handouts/mathematics/pounamu-trading-worksheet.html' OR path LIKE '%pounamu-trading-worksheet.html';


-- Update metadata for: Lesson 5 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5 | Te Kete Ako')
WHERE path = 'public/handouts/lesson-plans/lesson-5.html' OR path LIKE '%lesson-5.html';


-- Update metadata for: Lesson 4 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4 | Te Kete Ako')
WHERE path = 'public/handouts/lesson-plans/lesson-4.html' OR path LIKE '%lesson-4.html';


-- Update metadata for: Lesson Design Thinking | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson Design Thinking | Te Kete Ako')
WHERE path = 'public/handouts/lesson-plans/lesson-design-thinking.html' OR path LIKE '%lesson-design-thinking.html';


-- Update metadata for: Lesson 3 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3 | Te Kete Ako')
WHERE path = 'public/handouts/lesson-plans/lesson-3.html' OR path LIKE '%lesson-3.html';


-- Update metadata for: Lesson 2 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2 | Te Kete Ako')
WHERE path = 'public/handouts/lesson-plans/lesson-2.html' OR path LIKE '%lesson-2.html';


-- Update metadata for: Lesson 1 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1 | Te Kete Ako')
WHERE path = 'public/handouts/lesson-plans/lesson-1.html' OR path LIKE '%lesson-1.html';


-- Update metadata for: Lesson Sustainable Technology | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson Sustainable Technology | Te Kete Ako')
WHERE path = 'public/handouts/lesson-plans/lesson-sustainable-technology.html' OR path LIKE '%lesson-sustainable-technology.html';


-- Update metadata for: Lessons | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lessons | Te Kete Ako')
WHERE path = 'public/handouts/lesson-plans/lessons.html' OR path LIKE '%lessons.html';


-- Update metadata for: Lesson Statistical Investigation | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson Statistical Investigation | Te Kete Ako')
WHERE path = 'public/handouts/lesson-plans/lesson-statistical-investigation.html' OR path LIKE '%lesson-statistical-investigation.html';


-- Update metadata for: Project Brief | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Project Brief | Te Kete Ako')
WHERE path = 'public/handouts/project/project-brief.html' OR path LIKE '%project-brief.html';


-- Update metadata for: Kaitiaki Aronui - Advanced AI Capabilities Showcas
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Kaitiaki Aronui - Advanced AI Capabilities Showcase | Teacher Professional Development')
WHERE path = 'public/handouts/professional-development/kaitiaki-aronui-capability-showcase.html' OR path LIKE '%kaitiaki-aronui-capability-showcase.html';


-- Update metadata for: Physics of Traditional Māori Instruments - Sound S
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Physics of Traditional Māori Instruments - Sound Science')
WHERE path = 'public/handouts/printable-worksheets/physics-maori-instruments-worksheet.html' OR path LIKE '%physics-maori-instruments-worksheet.html';


-- Update metadata for: Creative Writing Inspired by Whakataukī
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Creative Writing Inspired by Whakataukī')
WHERE path = 'public/handouts/printable-worksheets/creative-writing-whakataukī-worksheet.html' OR path LIKE '%creative-writing-whakataukī-worksheet.html';


-- Update metadata for: Lesson 1: Star Compass Calculations Worksheet
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Star Compass Calculations Worksheet')
WHERE path = 'public/handouts/printable-worksheets/lesson-1-star-compass-calculations.html' OR path LIKE '%lesson-1-star-compass-calculations.html';


-- Update metadata for: Traditional Navigation Mathematics - Printable Wor
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Traditional Navigation Mathematics - Printable Worksheet')
WHERE path = 'public/handouts/printable-worksheets/traditional-navigation-mathematics-worksheet.html' OR path LIKE '%traditional-navigation-mathematics-worksheet.html';


-- Update metadata for: Ecosystem Fundamentals - Biotic & Abiotic Factors
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Ecosystem Fundamentals - Biotic & Abiotic Factors')
WHERE path = 'public/handouts/printable-worksheets/ecosystem-fundamentals-worksheet.html' OR path LIKE '%ecosystem-fundamentals-worksheet.html';


-- Update metadata for: Traditional Māori Navigation - Reading Comprehensi
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Traditional Māori Navigation - Reading Comprehension')
WHERE path = 'public/handouts/printable-worksheets/navigation-reading-comprehension.html' OR path LIKE '%navigation-reading-comprehension.html';


-- Update metadata for: Navigation Vocabulary - Te Reo Māori & English
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Navigation Vocabulary - Te Reo Māori & English')
WHERE path = 'public/handouts/printable-worksheets/navigation-vocabulary-te-reo-maori.html' OR path LIKE '%navigation-vocabulary-te-reo-maori.html';


-- Update metadata for: Lesson 2: Distance and Speed Calculations
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: Distance and Speed Calculations')
WHERE path = 'public/handouts/printable-worksheets/lesson-2-distance-speed-calculations.html' OR path LIKE '%lesson-2-distance-speed-calculations.html';


-- Update metadata for: Tino Rangatiratanga - Self-Determination & Soverei
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tino Rangatiratanga - Self-Determination & Sovereignty')
WHERE path = 'public/handouts/printable-worksheets/tino-rangatiratanga-worksheet.html' OR path LIKE '%tino-rangatiratanga-worksheet.html';


-- Update metadata for: Genetics & Whakapapa - Dual Knowledge Systems
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Genetics & Whakapapa - Dual Knowledge Systems')
WHERE path = 'public/handouts/printable-worksheets/genetics-whakapapa-worksheet.html' OR path LIKE '%genetics-whakapapa-worksheet.html';


-- Update metadata for: AsTTle-Style Reading Comprehension - Template
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'AsTTle-Style Reading Comprehension - Template')
WHERE path = 'public/handouts/printable-worksheets/asttle-comprehension-template.html' OR path LIKE '%asttle-comprehension-template.html';


-- Update metadata for: Dream Journal Activities | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Dream Journal Activities | Te Kete Ako')
WHERE path = 'public/handouts/activities/dream-journal-activities.html' OR path LIKE '%dream-journal-activities.html';


-- Update metadata for: Show And Tell Activities | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Show And Tell Activities | Te Kete Ako')
WHERE path = 'public/handouts/activities/show-and-tell-activities.html' OR path LIKE '%show-and-tell-activities.html';


-- Update metadata for: Whakapapa & Mathematical Thinking - Genealogy, Net
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Whakapapa & Mathematical Thinking - Genealogy, Networks & Exponential Growth | Mangakōtukutuku College')
WHERE path = 'public/handouts/enhanced/whakapapa-mathematical-thinking.html' OR path LIKE '%whakapapa-mathematical-thinking.html';


-- Update metadata for: Probability & Mātauranga Māori - Patterns, Chance 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Probability & Mātauranga Māori - Patterns, Chance & Decision-Making | Mangakōtukutuku College')
WHERE path = 'public/handouts/enhanced/probability-matauranga-integration.html' OR path LIKE '%probability-matauranga-integration.html';


-- Update metadata for: Ocean Health & Kaitiakitanga - Microplastics Throu
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Ocean Health & Kaitiakitanga - Microplastics Through Mātauranga Māori | Te Kete Ako')
WHERE path = 'public/handouts/enhanced/microplastics-matauranga-integration.html' OR path LIKE '%microplastics-matauranga-integration.html';


-- Update metadata for: Climate Science & Traditional Knowledge | Te Kete 
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Climate Science & Traditional Knowledge | Te Kete Ako')
WHERE path = 'public/handouts/enhanced/climate-science-traditional-knowledge.html' OR path LIKE '%climate-science-traditional-knowledge.html';


-- Update metadata for: Te Reo Māori Spelling Bee | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Spelling Bee | Te Kete Ako')
WHERE path = 'public/handouts/games/spelling-bee.html' OR path LIKE '%spelling-bee.html';


-- Update metadata for: Te Reo Māori Wordle (Unlimited) | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Wordle (Unlimited) | Te Kete Ako')
WHERE path = 'public/handouts/games/te-reo-wordle-unlimited.html' OR path LIKE '%te-reo-wordle-unlimited.html';


-- Update metadata for: English Wordle | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'English Wordle | Te Kete Ako')
WHERE path = 'public/handouts/games/english-wordle.html' OR path LIKE '%english-wordle.html';


-- Update metadata for: Tukutuku Pattern Explorer | Interactive Mathematic
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Pattern Explorer | Interactive Mathematics | Te Kete Ako')
WHERE path = 'public/handouts/games/tukutuku-pattern-explorer.html' OR path LIKE '%tukutuku-pattern-explorer.html';


-- Update metadata for: Te Reo Māori Wordle (6-Letter) | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Wordle (6-Letter) | Te Kete Ako')
WHERE path = 'public/handouts/games/te-reo-wordle-6.html' OR path LIKE '%te-reo-wordle-6.html';


-- Update metadata for: Te Reo Māori Wordle | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Wordle | Te Kete Ako')
WHERE path = 'public/handouts/games/te-reo-wordle.html' OR path LIKE '%te-reo-wordle.html';


-- Update metadata for: Te Reo Māori Wordle (6-Letter, Unlimited) | Te Ket
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Wordle (6-Letter, Unlimited) | Te Kete Ako')
WHERE path = 'public/handouts/games/te-reo-wordle-6-unlimited.html' OR path LIKE '%te-reo-wordle-6-unlimited.html';


-- Update metadata for: Countdown Letters: Te Reo Māori | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Countdown Letters: Te Reo Māori | Te Kete Ako')
WHERE path = 'public/handouts/games/countdown-letters.html' OR path LIKE '%countdown-letters.html';


-- Update metadata for: Categories Challenge | Te Kete Ako Games
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Categories Challenge | Te Kete Ako Games')
WHERE path = 'public/handouts/games/categories.html' OR path LIKE '%categories.html';


-- Update metadata for: Video Activity: The Bastion Point Occupation | Te 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Video Activity: The Bastion Point Occupation | Te Kete Ako')
WHERE path = 'public/handouts/video-activities/bastion-point-video-activity.html' OR path LIKE '%bastion-point-video-activity.html';


-- Update metadata for: Video Activity: The New Zealand Wars | Mangakōtuku
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Video Activity: The New Zealand Wars | Mangakōtukutuku College')
WHERE path = 'public/handouts/video-activities/nz-wars-video-activity.html' OR path LIKE '%nz-wars-video-activity.html';


-- Update metadata for: Digital Sovereignty Multimedia Lab | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Digital Sovereignty Multimedia Lab | Te Kete Ako')
WHERE path = 'public/handouts/video-activities/digital-sovereignty-multimedia-lab.html' OR path LIKE '%digital-sovereignty-multimedia-lab.html';


-- Update metadata for: Video Activity: The Legends of Māui | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Video Activity: The Legends of Māui | Te Kete Ako')
WHERE path = 'public/handouts/video-activities/maui-video-activity.html' OR path LIKE '%maui-video-activity.html';


-- Update metadata for: Video Activity: Prompt Engineering and AI Red Team
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Video Activity: Prompt Engineering and AI Red Teaming | Mangakōtukutuku College')
WHERE path = 'public/handouts/video-activities/prompt-engineering-video-activity.html' OR path LIKE '%prompt-engineering-video-activity.html';


-- Update metadata for: STEM + Mātauranga Māori Integration Lab | Mangakōt
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'STEM + Mātauranga Māori Integration Lab | Mangakōtukutuku College')
WHERE path = 'public/handouts/video-activities/stem-matauranga-integration-lab.html' OR path LIKE '%stem-matauranga-integration-lab.html';


-- Update metadata for: MCP Enhanced Video Analysis: Economic Justice in A
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'MCP Enhanced Video Analysis: Economic Justice in Aotearoa | Mangakōtukutuku College')
WHERE path = 'public/handouts/video-activities/economic-justice-documentary-analysis.html' OR path LIKE '%economic-justice-documentary-analysis.html';


-- Update metadata for: Signing you in... - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Signing you in... - Te Kete Ako')
WHERE path = 'public/auth/callback.html' OR path LIKE '%callback.html';


-- Update metadata for: Micro-Interactions Demo - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Micro-Interactions Demo - Te Kete Ako')
WHERE path = 'public/js/micro-interactions-demo.html' OR path LIKE '%micro-interactions-demo.html';


-- Update metadata for: Task Queue Dashboard | Te Kete Ako Admin
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Task Queue Dashboard | Te Kete Ako Admin')
WHERE path = 'public/admin/task-queue-dashboard.html' OR path LIKE '%task-queue-dashboard.html';


-- Update metadata for: Orchestration Test Suite | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Orchestration Test Suite | Te Kete Ako')
WHERE path = 'public/admin/orchestration-test-suite.html' OR path LIKE '%orchestration-test-suite.html';


-- Update metadata for: Agent Workload Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Agent Workload Dashboard | Te Kete Ako')
WHERE path = 'public/admin/agent-workload-dashboard.html' OR path LIKE '%agent-workload-dashboard.html';


-- Update metadata for: Lesson 5 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5 | Te Kete Ako')
WHERE path = 'public/lesson-plans/lesson-5.html' OR path LIKE '%lesson-5.html';


-- Update metadata for: Lesson 4 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4 | Te Kete Ako')
WHERE path = 'public/lesson-plans/lesson-4.html' OR path LIKE '%lesson-4.html';


-- Update metadata for: Lesson Design Thinking | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Design Thinking | Te Kete Ako')
WHERE path = 'public/lesson-plans/lesson-design-thinking.html' OR path LIKE '%lesson-design-thinking.html';


-- Update metadata for: Lesson 3 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3 | Te Kete Ako')
WHERE path = 'public/lesson-plans/lesson-3.html' OR path LIKE '%lesson-3.html';


-- Update metadata for: Lesson 2 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2 | Te Kete Ako')
WHERE path = 'public/lesson-plans/lesson-2.html' OR path LIKE '%lesson-2.html';


-- Update metadata for: Lesson 1 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1 | Te Kete Ako')
WHERE path = 'public/lesson-plans/lesson-1.html' OR path LIKE '%lesson-1.html';


-- Update metadata for: Lesson Sustainable Technology | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Sustainable Technology | Te Kete Ako')
WHERE path = 'public/lesson-plans/lesson-sustainable-technology.html' OR path LIKE '%lesson-sustainable-technology.html';


-- Update metadata for: Lessons | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lessons | Te Kete Ako')
WHERE path = 'public/lesson-plans/lessons.html' OR path LIKE '%lessons.html';


-- Update metadata for: Lesson Statistical Investigation | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Statistical Investigation | Te Kete Ako')
WHERE path = 'public/lesson-plans/lesson-statistical-investigation.html' OR path LIKE '%lesson-statistical-investigation.html';


-- Update metadata for: Teacher Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Dashboard | Te Kete Ako')
WHERE path = 'public/teachers/dashboard.html' OR path LIKE '%dashboard.html';


-- Update metadata for: Y8 Systems Unit | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y8 Systems Unit | Te Kete Ako')
WHERE path = 'public/y8-systems/y8-systems-unit.html' OR path LIKE '%y8-systems-unit.html';


-- Update metadata for: Printable: Indigenous Feedback Framework
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Feedback Framework')
WHERE path = 'public/y8-systems/resources/indigenous-feedback-framework.html' OR path LIKE '%indigenous-feedback-framework.html';


-- Update metadata for: Printable: Council Services Cards
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Council Services Cards')
WHERE path = 'public/y8-systems/resources/lesson-3-1-council-services-cards.html' OR path LIKE '%lesson-3-1-council-services-cards.html';


-- Update metadata for: Printable: Indigenous Systems Examples
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Systems Examples')
WHERE path = 'public/y8-systems/resources/indigenous-systems-examples.html' OR path LIKE '%indigenous-systems-examples.html';


-- Update metadata for: Printable: Campaign Plan Template
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Campaign Plan Template')
WHERE path = 'public/y8-systems/resources/lesson-3-2-campaign-plan-template.html' OR path LIKE '%lesson-3-2-campaign-plan-template.html';


-- Update metadata for: Printable: Living Tiriti Examples
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Living Tiriti Examples')
WHERE path = 'public/y8-systems/resources/living-tiriti-examples.html' OR path LIKE '%living-tiriti-examples.html';


-- Update metadata for: Community Partnership Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Community Partnership Guide | Te Kete Ako')
WHERE path = 'public/y8-systems/resources/community-partnership-guide.html' OR path LIKE '%community-partnership-guide.html';


-- Update metadata for: Printable: NZ Government Power Cards
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: NZ Government Power Cards')
WHERE path = 'public/y8-systems/resources/lesson-2-2-power-cards.html' OR path LIKE '%lesson-2-2-power-cards.html';


-- Update metadata for: Printable: Government Case Studies
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Government Case Studies')
WHERE path = 'public/y8-systems/resources/lesson-2-1-case-studies.html' OR path LIKE '%lesson-2-1-case-studies.html';


-- Update metadata for: Printable: Traditional Māori Governance Systems
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Traditional Māori Governance Systems')
WHERE path = 'public/y8-systems/resources/maori-governance-systems.html' OR path LIKE '%maori-governance-systems.html';


-- Update metadata for: Printable: Draw Your System Template
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Draw Your System Template')
WHERE path = 'public/y8-systems/resources/lesson-1-2-draw-your-system-template.html' OR path LIKE '%lesson-1-2-draw-your-system-template.html';


-- Update metadata for: Printable: Colonization Timeline
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Colonization Timeline')
WHERE path = 'public/y8-systems/resources/colonization-timeline.html' OR path LIKE '%colonization-timeline.html';


-- Update metadata for: Printable: Decolonization Today
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Decolonization Today')
WHERE path = 'public/y8-systems/resources/decolonization-today.html' OR path LIKE '%decolonization-today.html';


-- Update metadata for: The Skate Park Campaign - Systems Thinking Case St
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Skate Park Campaign - Systems Thinking Case Study | Te Kete Ako')
WHERE path = 'public/y8-systems/resources/skate-park-campaign.html' OR path LIKE '%skate-park-campaign.html';


-- Update metadata for: Printable: Te Tiriti Māori & English Texts Compari
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Te Tiriti Māori & English Texts Comparison')
WHERE path = 'public/y8-systems/resources/treaty-two-texts.html' OR path LIKE '%treaty-two-texts.html';


-- Update metadata for: Printable: Decolonized Design Template
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Printable: Decolonized Design Template')
WHERE path = 'public/y8-systems/resources/decolonized-design-template.html' OR path LIKE '%decolonized-design-template.html';


-- Update metadata for: Printable: Gallery Walk Statements
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Gallery Walk Statements')
WHERE path = 'public/y8-systems/resources/gallery-walk-statements.html' OR path LIKE '%gallery-walk-statements.html';


-- Update metadata for: Printable: Indigenous Governance Principles
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Governance Principles')
WHERE path = 'public/y8-systems/resources/indigenous-governance-principles.html' OR path LIKE '%indigenous-governance-principles.html';


-- Update metadata for: Printable: Government Station Cards
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Government Station Cards')
WHERE path = 'public/y8-systems/resources/government-station-cards.html' OR path LIKE '%government-station-cards.html';


-- Update metadata for: Printable: Decolonization Commitment Template
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Printable: Decolonization Commitment Template')
WHERE path = 'public/y8-systems/resources/decolonization-commitment-template.html' OR path LIKE '%decolonization-commitment-template.html';


-- Update metadata for: Printable: Society Stations Handout
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Society Stations Handout')
WHERE path = 'public/y8-systems/resources/lesson-1-1-society-stations.html' OR path LIKE '%lesson-1-1-society-stations.html';


-- Update metadata for: Printable: Defending Tino Rangatiratanga Case Stud
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Defending Tino Rangatiratanga Case Studies')
WHERE path = 'public/y8-systems/resources/maori-political-action.html' OR path LIKE '%maori-political-action.html';


-- Update metadata for: Printable: Protest Case Studies
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Printable: Protest Case Studies')
WHERE path = 'public/y8-systems/resources/protest-case-studies.html' OR path LIKE '%protest-case-studies.html';


-- Update metadata for: Society Design Assessment Rubric | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Society Design Assessment Rubric | Te Kete Ako')
WHERE path = 'public/y8-systems/resources/society-design-assessment-rubric.html' OR path LIKE '%society-design-assessment-rubric.html';


-- Update metadata for: Printable: Design a System Template
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Printable: Design a System Template')
WHERE path = 'public/y8-systems/resources/design-a-system-template.html' OR path LIKE '%design-a-system-template.html';


-- Update metadata for: Society Design Collaboration Framework | Te Kete A
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Society Design Collaboration Framework | Te Kete Ako')
WHERE path = 'public/y8-systems/resources/society-design-collaboration-framework.html' OR path LIKE '%society-design-collaboration-framework.html';


-- Update metadata for: Indigenous Learning Systems | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Indigenous Learning Systems | Te Kete Ako')
WHERE path = 'public/y8-systems/resources/indigenous-learning-systems.html' OR path LIKE '%indigenous-learning-systems.html';


-- Update metadata for: Printable: Simplified Treaty Articles
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Simplified Treaty Articles')
WHERE path = 'public/y8-systems/resources/treaty-articles.html' OR path LIKE '%treaty-articles.html';


-- Update metadata for: Printable Resource: System Sorting Cards
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable Resource: System Sorting Cards')
WHERE path = 'public/y8-systems/resources/system-sorting-cards.html' OR path LIKE '%system-sorting-cards.html';


-- Update metadata for: Resource: Frayer Model for "System" | Y8 Systems |
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Resource: Frayer Model for "System" | Y8 Systems | Te Kete Ako')
WHERE path = 'public/y8-systems/resources/frayer-model-system.html' OR path LIKE '%frayer-model-system.html';


-- Update metadata for: Who Has the REAL Power? - NZ Government
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Who Has the REAL Power? - NZ Government')
WHERE path = 'public/y8-systems/resources/who-has-the-real-power-interactive.html' OR path LIKE '%who-has-the-real-power-interactive.html';


-- Update metadata for: Design Your Society Unit | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Design Your Society Unit | Te Kete Ako')
WHERE path = 'public/y8-systems/units/design-your-society-unit.html' OR path LIKE '%design-your-society-unit.html';


-- Update metadata for: Y8 Systems | Lesson 5.2: Present & Reflect
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Y8 Systems | Lesson 5.2: Present & Reflect')
WHERE path = 'public/y8-systems/lessons/lesson-5-2.html' OR path LIKE '%lesson-5-2.html';


-- Update metadata for: Unit 1 Lesson 3: Democracy vs. Dictatorship | Y8 S
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 3: Democracy vs. Dictatorship | Y8 Systems | Te Kete Ako')
WHERE path = 'public/y8-systems/lessons/lesson-2-1.html' OR path LIKE '%lesson-2-1.html';


-- Update metadata for: Unit 1 Lesson 6: How to Make Your Voice Heard | Y8
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 6: How to Make Your Voice Heard | Y8 Systems | Te Kete Ako')
WHERE path = 'public/y8-systems/lessons/lesson-3-2.html' OR path LIKE '%lesson-3-2.html';


-- Update metadata for: Unit 2 Lesson 1: The Treaty & Co-Governance | Y8 S
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 1: The Treaty & Co-Governance | Y8 Systems | Te Kete Ako')
WHERE path = 'public/y8-systems/lessons/lesson-4-1.html' OR path LIKE '%lesson-4-1.html';


-- Update metadata for: Unit 1 Lesson 2: Systems Are Everywhere | Y8 Syste
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 2: Systems Are Everywhere | Y8 Systems | Te Kete Ako')
WHERE path = 'public/y8-systems/lessons/lesson-1-2.html' OR path LIKE '%lesson-1-2.html';


-- Update metadata for: Unit 2 Lesson 2: Colonisation & Its Impacts | Y8 S
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 2: Colonisation & Its Impacts | Y8 Systems | Te Kete Ako')
WHERE path = 'public/y8-systems/lessons/lesson-4-2.html' OR path LIKE '%lesson-4-2.html';


-- Update metadata for: Unit 1 Lesson 1: What Makes a Society? | Y8 System
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 1: What Makes a Society? | Y8 Systems | Te Kete Ako')
WHERE path = 'public/y8-systems/lessons/lesson-1-1.html' OR path LIKE '%lesson-1-1.html';


-- Update metadata for: Unit 1 Lesson 5: How Local Government Works | Y8 S
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 5: How Local Government Works | Y8 Systems | Te Kete Ako')
WHERE path = 'public/y8-systems/lessons/lesson-3-1.html' OR path LIKE '%lesson-3-1.html';


-- Update metadata for: Unit 1 Lesson 4: How New Zealand is Governed | Y8 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 4: How New Zealand is Governed | Y8 Systems | Te Kete Ako')
WHERE path = 'public/y8-systems/lessons/lesson-2-2.html' OR path LIKE '%lesson-2-2.html';


-- Update metadata for: Y8 Systems | Lesson 5.1: Guided Inquiry Project La
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Y8 Systems | Lesson 5.1: Guided Inquiry Project Launch - Design Your Society')
WHERE path = 'public/y8-systems/lessons/lesson-5-1.html' OR path LIKE '%lesson-5-1.html';


-- Update metadata for: Master Assessment Rubric - Navigation Mathematics
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Master Assessment Rubric - Navigation Mathematics')
WHERE path = 'public/units/master-assessment-rubric.html' OR path LIKE '%master-assessment-rubric.html';


-- Update metadata for: Unit 4: Economic Justice & Rangatiratanga - Altern
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 4: Economic Justice & Rangatiratanga - Alternative Economic Models | Mangakōtukutuku College')
WHERE path = 'public/units/unit-4-economic-justice.html' OR path LIKE '%unit-4-economic-justice.html';


-- Update metadata for: Comprehensive Assessment Generator
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Comprehensive Assessment Generator')
WHERE path = 'public/units/comprehensive-assessment-generator.html' OR path LIKE '%comprehensive-assessment-generator.html';


-- Update metadata for: Year 7 Complete Curriculum | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Year 7 Complete Curriculum | Te Kete Ako')
WHERE path = 'public/units/year-7-complete-curriculum.html' OR path LIKE '%year-7-complete-curriculum.html';


-- Update metadata for: Ultra-Comprehensive Nested Unit: Traditional Māori
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Ultra-Comprehensive Nested Unit: Traditional Māori Navigation Mathematics')
WHERE path = 'public/units/ultra-comprehensive-navigation-unit.html' OR path LIKE '%ultra-comprehensive-navigation-unit.html';


-- Update metadata for: Comprehensive Subject Generation Roadmap
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Comprehensive Subject Generation Roadmap')
WHERE path = 'public/units/subject-generation-roadmap.html' OR path LIKE '%subject-generation-roadmap.html';


-- Update metadata for: Complete Units Index | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Complete Units Index | Te Kete Ako')
WHERE path = 'public/units/complete-units-index.html' OR path LIKE '%complete-units-index.html';


-- Update metadata for: Comprehensive Unit Example: Traditional Māori Navi
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Comprehensive Unit Example: Traditional Māori Navigation Mathematics')
WHERE path = 'public/units/comprehensive-example-unit.html' OR path LIKE '%comprehensive-example-unit.html';


-- Update metadata for: Science Units | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Science Units | Te Kete Ako')
WHERE path = 'public/units/science-units-index.html' OR path LIKE '%science-units-index.html';


-- Update metadata for: Design Your Own Society - Systems Unit | Te Kete A
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Design Your Own Society - Systems Unit | Te Kete Ako')
WHERE path = 'public/units/design-your-society-unit.html' OR path LIKE '%design-your-society-unit.html';


-- Update metadata for: Year Level Progression Generator
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Year Level Progression Generator')
WHERE path = 'public/units/year-level-progression-generator.html' OR path LIKE '%year-level-progression-generator.html';


-- Update metadata for: Unit 1: Te Ao Māori - Cultural Identity & Knowledg
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 1: Te Ao Māori - Cultural Identity & Knowledge Systems | Mangakōtukutuku College')
WHERE path = 'public/units/unit-1-te-ao-maori.html' OR path LIKE '%unit-1-te-ao-maori.html';


-- Update metadata for: Unit 3: STEM Through Mātauranga Māori - Dual Knowl
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 3: STEM Through Mātauranga Māori - Dual Knowledge Systems for Environmental Action | Te Kete Ako')
WHERE path = 'public/units/unit-3-stem-matauranga.html' OR path LIKE '%unit-3-stem-matauranga.html';


-- Update metadata for: Unit 7: Digital Technologies & AI Ethics - Navigat
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 7: Digital Technologies & AI Ethics - Navigating the Future of Artificial Intelligence | Te Kete Ako')
WHERE path = 'public/units/unit-7-digital-tech-ai-ethics.html' OR path LIKE '%unit-7-digital-tech-ai-ethics.html';


-- Update metadata for: Year 8 Complete Curriculum | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Year 8 Complete Curriculum | Te Kete Ako')
WHERE path = 'public/units/year-8-complete-curriculum.html' OR path LIKE '%year-8-complete-curriculum.html';


-- Update metadata for: Unit 2: Decolonized Aotearoa History - Centering M
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 2: Decolonized Aotearoa History - Centering Māori Agency, Resistance, and Sovereignty | Te Kete Ako')
WHERE path = 'public/units/unit-2-decolonized-history.html' OR path LIKE '%unit-2-decolonized-history.html';


-- Update metadata for: Mathematics Units | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Mathematics Units | Te Kete Ako')
WHERE path = 'public/units/math-units-index.html' OR path LIKE '%math-units-index.html';


-- Update metadata for: Year 9 Complete Curriculum | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Year 9 Complete Curriculum | Te Kete Ako')
WHERE path = 'public/units/year-9-complete-curriculum.html' OR path LIKE '%year-9-complete-curriculum.html';


-- Update metadata for: Unit 6: Future Rangatiratanga - Youth Leadership &
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 6: Future Rangatiratanga - Youth Leadership & Social Innovation | Te Kete Ako')
WHERE path = 'public/units/unit-6-future-rangatiratanga.html' OR path LIKE '%unit-6-future-rangatiratanga.html';


-- Update metadata for: Unit 5: Global Indigenous Solidarity - Transnation
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 5: Global Indigenous Solidarity - Transnational Movements | Te Kete Ako')
WHERE path = 'public/units/unit-5-global-connections.html' OR path LIKE '%unit-5-global-connections.html';


-- Update metadata for: Lesson 6: Evaluating Arguments
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6: Evaluating Arguments')
WHERE path = 'public/units/y8-critical-thinking/lesson-6-evaluating-arguments.html' OR path LIKE '%lesson-6-evaluating-arguments.html';


-- Update metadata for: Lesson 2: Identifying Bias and Credible Sources
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: Identifying Bias and Credible Sources')
WHERE path = 'public/units/y8-critical-thinking/lesson-2-bias-and-sources.html' OR path LIKE '%lesson-2-bias-and-sources.html';


-- Update metadata for: Critical Thinking Introduction | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Critical Thinking Introduction | Te Kete Ako')
WHERE path = 'public/units/y8-critical-thinking/critical-thinking-introduction.html' OR path LIKE '%critical-thinking-introduction.html';


-- Update metadata for: Lesson 7: Group Decision-Making
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 7: Group Decision-Making')
WHERE path = 'public/units/y8-critical-thinking/lesson-7-group-decision-making.html' OR path LIKE '%lesson-7-group-decision-making.html';


-- Update metadata for: Lesson 8: Critical Thinking Challenge
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 8: Critical Thinking Challenge')
WHERE path = 'public/units/y8-critical-thinking/lesson-8-critical-thinking-challenge.html' OR path LIKE '%lesson-8-critical-thinking-challenge.html';


-- Update metadata for: Lesson 5: Asking the Right Questions
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5: Asking the Right Questions')
WHERE path = 'public/units/y8-critical-thinking/lesson-5-asking-right-questions.html' OR path LIKE '%lesson-5-asking-right-questions.html';


-- Update metadata for: Lesson 1: Introduction to Critical Thinking
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Introduction to Critical Thinking')
WHERE path = 'public/units/y8-critical-thinking/lesson-1-introduction.html' OR path LIKE '%lesson-1-introduction.html';


-- Update metadata for: Lesson 3: Logical Fallacies
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Logical Fallacies')
WHERE path = 'public/units/y8-critical-thinking/lesson-3-logical-fallacies.html' OR path LIKE '%lesson-3-logical-fallacies.html';


-- Update metadata for: Advanced Critical Thinking: Decision-Making Framew
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Advanced Critical Thinking: Decision-Making Frameworks | Te Kete Ako')
WHERE path = 'public/units/y8-critical-thinking/advanced-critical-thinking-decision-making.html' OR path LIKE '%advanced-critical-thinking-decision-making.html';


-- Update metadata for: Lesson 4: Ethics & Decision-Making
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: Ethics & Decision-Making')
WHERE path = 'public/units/y8-critical-thinking/lesson-4-ethics-decision-making.html' OR path LIKE '%lesson-4-ethics-decision-making.html';


-- Update metadata for: Lesson 3.5: Ngata's Legacy & Modern Impact | Te Ke
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3.5: Ngata''s Legacy & Modern Impact | Te Kete Ako')
WHERE path = 'public/units/ngata-unit/lesson-3-5-legacy-and-modern-impact.html' OR path LIKE '%lesson-3-5-legacy-and-modern-impact.html';


-- Update metadata for: Lesson 3.1: Who Was Āpirana Ngata? | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3.1: Who Was Āpirana Ngata? | Te Kete Ako')
WHERE path = 'public/units/ngata-unit/lesson-3-1-who-was-apirana-ngata.html' OR path LIKE '%lesson-3-1-who-was-apirana-ngata.html';


-- Update metadata for: Lesson 3.4: Preserving Cultural Knowledge | Te Ket
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3.4: Preserving Cultural Knowledge | Te Kete Ako')
WHERE path = 'public/units/ngata-unit/lesson-3-4-preserving-cultural-knowledge.html' OR path LIKE '%lesson-3-4-preserving-cultural-knowledge.html';


-- Update metadata for: Lesson 3.3: Land Development Schemes | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3.3: Land Development Schemes | Te Kete Ako')
WHERE path = 'public/units/ngata-unit/lesson-3-3-land-development-schemes.html' OR path LIKE '%lesson-3-3-land-development-schemes.html';


-- Update metadata for: Lesson 3.2: Te Reo Māori Revival | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3.2: Te Reo Māori Revival | Te Kete Ako')
WHERE path = 'public/units/ngata-unit/lesson-3-2-te-reo-maori-revival.html' OR path LIKE '%lesson-3-2-te-reo-maori-revival.html';


-- Update metadata for: Lesson 1: Harakeke Fibre Chemistry (Y9)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Harakeke Fibre Chemistry (Y9)')
WHERE path = 'public/units/y9-chemistry-materials/lessons/lesson-1-harakeke-chemistry.html' OR path LIKE '%lesson-1-harakeke-chemistry.html';


-- Update metadata for: Discover Orphans
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Discover Orphans')
WHERE path = 'public/units/arts/08-orphans.html' OR path LIKE '%08-orphans.html';


-- Update metadata for: Te Kete Ako - Comprehensive Site Map
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Comprehensive Site Map')
WHERE path = 'public/units/arts/10-sitemap-enhanced.html' OR path LIKE '%10-sitemap-enhanced.html';


-- Update metadata for: Plate Tectonics Reading Comprehension
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Plate Tectonics Reading Comprehension')
WHERE path = 'public/units/arts/09-plate-tectonics-comprehension-handout.html' OR path LIKE '%09-plate-tectonics-comprehension-handout.html';


-- Update metadata for: Te Kete Ako - Auth Test (8PM Ready)
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Auth Test (8PM Ready)')
WHERE path = 'public/units/arts/02-auth-test.html' OR path LIKE '%02-auth-test.html';


-- Update metadata for: Handout: NZ Housing Crisis
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Handout: NZ Housing Crisis')
WHERE path = 'public/units/arts/07-nz-housing-crisis-handout.html' OR path LIKE '%07-nz-housing-crisis-handout.html';


-- Update metadata for: Walker Unit - Teacher's Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Walker Unit - Teacher''s Guide | Te Kete Ako')
WHERE path = 'public/units/arts/06-walker-unit-overview-teacher-guide.html' OR path LIKE '%06-walker-unit-overview-teacher-guide.html';


-- Update metadata for: Simple Login | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Simple Login | Te Kete Ako')
WHERE path = 'public/units/arts/01-login-simple.html' OR path LIKE '%01-login-simple.html';


-- Update metadata for: Year 10 Mathematics - Cultural Geometry Unit | Kai
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Year 10 Mathematics - Cultural Geometry Unit | Kaitiaki Aronui Generated')
WHERE path = 'public/units/arts/05-kaitiaki-generated-y10-math-cultural-geometry.html' OR path LIKE '%05-kaitiaki-generated-y10-math-cultural-geometry.html';


-- Update metadata for: Elements of Art Handout
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Elements of Art Handout')
WHERE path = 'public/units/arts/03-elements-of-art-handout.html' OR path LIKE '%03-elements-of-art-handout.html';


-- Update metadata for: Shakespearean Soliloquy Reading Comprehension
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Shakespearean Soliloquy Reading Comprehension')
WHERE path = 'public/units/arts/04-shakespeare-soliloquy-handout.html' OR path LIKE '%04-shakespeare-soliloquy-handout.html';


-- Update metadata for: Unit 2 Decolonized History | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Decolonized History | Te Kete Ako')
WHERE path = 'public/units/social-studies/014-unit-2-decolonized-history.html' OR path LIKE '%014-unit-2-decolonized-history.html';


-- Update metadata for: Social Studies | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Social Studies | Te Kete Ako')
WHERE path = 'public/units/social-studies/015-social-studies.html' OR path LIKE '%015-social-studies.html';


-- Update metadata for: Te Kete Ako - Lesson 3: Source Evaluation & Fact-C
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Lesson 3: Source Evaluation & Fact-Checking')
WHERE path = 'public/units/social-studies/01-lesson-3.html' OR path LIKE '%01-lesson-3.html';


-- Update metadata for: A Forum for Justice: The Waitangi Tribunal | Te Ke
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'A Forum for Justice: The Waitangi Tribunal | Te Kete Ako')
WHERE path = 'public/units/social-studies/012-walker-lesson-1.4-a-forum-for-justice.html' OR path LIKE '%012-walker-lesson-1.4-a-forum-for-justice.html';


-- Update metadata for: Te Kete Ako - Lesson 3: Source Evaluation & Fact-C
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Lesson 3: Source Evaluation & Fact-Checking')
WHERE path = 'public/units/social-studies/010-lesson-3.html' OR path LIKE '%010-lesson-3.html';


-- Update metadata for: Nzhistory Investigation Toolkit
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Nzhistory Investigation Toolkit')
WHERE path = 'public/units/social-studies/05-nzhistory-investigation-toolkit.html' OR path LIKE '%05-nzhistory-investigation-toolkit.html';


-- Update metadata for: Nzhistory Investigation Toolkit
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Nzhistory Investigation Toolkit')
WHERE path = 'public/units/social-studies/011-nzhistory-investigation-toolkit.html' OR path LIKE '%011-nzhistory-investigation-toolkit.html';


-- Update metadata for: Lesson 2: The Aotearoa Wars | Unit 2: Decolonized 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: The Aotearoa Wars | Unit 2: Decolonized History | Te Kete Ako')
WHERE path = 'public/units/social-studies/013-unit-2-lesson-2.html' OR path LIKE '%013-unit-2-lesson-2.html';


-- Update metadata for: Nz Geography Basics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Nz Geography Basics | Te Kete Ako')
WHERE path = 'public/units/social-studies/017-nz-geography-basics.html' OR path LIKE '%017-nz-geography-basics.html';


-- Update metadata for: A Forum for Justice: The Waitangi Tribunal | Te Ke
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'A Forum for Justice: The Waitangi Tribunal | Te Kete Ako')
WHERE path = 'public/units/social-studies/02-walker-lesson-1.4-a-forum-for-justice.html' OR path LIKE '%02-walker-lesson-1.4-a-forum-for-justice.html';


-- Update metadata for: Social Studies | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Social Studies | Te Kete Ako')
WHERE path = 'public/units/social-studies/04-social-studies.html' OR path LIKE '%04-social-studies.html';


-- Update metadata for: Lesson 2: The Aotearoa Wars | Unit 2: Decolonized 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: The Aotearoa Wars | Unit 2: Decolonized History | Te Kete Ako')
WHERE path = 'public/units/social-studies/03-unit-2-lesson-2.html' OR path LIKE '%03-unit-2-lesson-2.html';


-- Update metadata for: Local Area History | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Local Area History | Te Kete Ako')
WHERE path = 'public/units/social-studies/016-local-area-history.html' OR path LIKE '%016-local-area-history.html';


-- Update metadata for: Unit 2 Decolonized History | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Decolonized History | Te Kete Ako')
WHERE path = 'public/units/social-studies/07-unit-2-decolonized-history.html' OR path LIKE '%07-unit-2-decolonized-history.html';


-- Update metadata for: Lesson 1.4: A Forum for Justice | Walker Unit | Te
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.4: A Forum for Justice | Walker Unit | Te Kete Ako')
WHERE path = 'public/units/social-studies/09-lesson-1-4-a-forum-for-justice.html' OR path LIKE '%09-lesson-1-4-a-forum-for-justice.html';


-- Update metadata for: Local Area History | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Local Area History | Te Kete Ako')
WHERE path = 'public/units/social-studies/06-local-area-history.html' OR path LIKE '%06-local-area-history.html';


-- Update metadata for: Nz Geography Basics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Nz Geography Basics | Te Kete Ako')
WHERE path = 'public/units/social-studies/08-nz-geography-basics.html' OR path LIKE '%08-nz-geography-basics.html';


-- Update metadata for: AI Ethics Through Māori Data Sovereignty
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics Through Māori Data Sovereignty')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/ai-ethics-through-māori-data-sovereignty.html' OR path LIKE '%ai-ethics-through-māori-data-sovereignty.html';


-- Update metadata for: Media Literacy: Analyzing Māori Representation
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Media Literacy: Analyzing Māori Representation')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/media-literacy-analyzing-māori-representation.html' OR path LIKE '%media-literacy-analyzing-māori-representation.html';


-- Update metadata for: Year 8 Social Studies - Māori Migration to Aotearo
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Year 8 Social Studies - Māori Migration to Aotearoa | Kaitiaki Aronui Generated')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/kaitiaki-generated-maori-migration-lesson.html' OR path LIKE '%kaitiaki-generated-maori-migration-lesson.html';


-- Update metadata for: Career Pathways in STEM for Māori Students
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Career Pathways in STEM for Māori Students')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/career-pathways-in-stem-for-māori-students.html' OR path LIKE '%career-pathways-in-stem-for-māori-students.html';


-- Update metadata for: Poetry Analysis Through Māori Literary Traditions
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Poetry Analysis Through Māori Literary Traditions')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/poetry-analysis-through-māori-literary-traditions.html' OR path LIKE '%poetry-analysis-through-māori-literary-traditions.html';


-- Update metadata for: AI Ethics Through Māori Data Sovereignty | Te Kete
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics Through Māori Data Sovereignty | Te Kete Ako')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/ai-ethics-through-māori-data-sovereignty-FIXED.html' OR path LIKE '%ai-ethics-through-māori-data-sovereignty-FIXED.html';


-- Update metadata for: Narrative Writing Using Māori Story Structures
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Narrative Writing Using Māori Story Structures')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/narrative-writing-using-māori-story-structures.html' OR path LIKE '%narrative-writing-using-māori-story-structures.html';


-- Update metadata for: Debate Skills with Māori Oratory Traditions
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Debate Skills with Māori Oratory Traditions')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/debate-skills-with-māori-oratory-traditions.html' OR path LIKE '%debate-skills-with-māori-oratory-traditions.html';


-- Update metadata for: Renewable Energy and Māori Innovation
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Renewable Energy and Māori Innovation')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/renewable-energy-and-māori-innovation.html' OR path LIKE '%renewable-energy-and-māori-innovation.html';


-- Update metadata for: Climate Change Through Te Taiao Māori Lens - Te Ke
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Climate Change Through Te Taiao Māori Lens - Te Kete Ako')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/climate-change-through-te-taiao-māori-lens.html' OR path LIKE '%climate-change-through-te-taiao-māori-lens.html';


-- Update metadata for: Argumentative Writing on Contemporary Māori Issues
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Argumentative Writing on Contemporary Māori Issues')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/argumentative-writing-on-contemporary-māori-issues.html' OR path LIKE '%argumentative-writing-on-contemporary-māori-issues.html';


-- Update metadata for: Scientific Method Using Traditional Māori Practice
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Scientific Method Using Traditional Māori Practices')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/scientific-method-using-traditional-māori-practices.html' OR path LIKE '%scientific-method-using-traditional-māori-practices.html';


-- Update metadata for: Game Development with Cultural Themes
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Game Development with Cultural Themes')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/game-development-with-cultural-themes.html' OR path LIKE '%game-development-with-cultural-themes.html';


-- Update metadata for: Physics of Traditional Māori Instruments
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Physics of Traditional Māori Instruments')
WHERE path = 'public/units/unit-1-te-ao-maori/lessons/physics-of-traditional-māori-instruments.html' OR path LIKE '%physics-of-traditional-māori-instruments.html';


-- Update metadata for: Lesson 1: What is Data Sovereignty? (Y10 Digital T
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: What is Data Sovereignty? (Y10 Digital Tech)')
WHERE path = 'public/units/y10-digital-sovereignty/lessons/lesson-1-data-sovereignty-intro.html' OR path LIKE '%lesson-1-data-sovereignty-intro.html';


-- Update metadata for: Years of Anger: The Protest Movements | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Years of Anger: The Protest Movements | Te Kete Ako')
WHERE path = 'public/units/senior-secondary/12-walker-lesson-1.3-years-of-anger.html' OR path LIKE '%12-walker-lesson-1.3-years-of-anger.html';


-- Update metadata for: Youth Vaping Reading Comprehension | Mangakōtukutu
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Youth Vaping Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/units/senior-secondary/09-youth-vaping-comprehension-handout.html' OR path LIKE '%09-youth-vaping-comprehension-handout.html';


-- Update metadata for: Lesson 1.1: Who was Ranginui Walker? | Walker Unit
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.1: Who was Ranginui Walker? | Walker Unit | Te Kete Ako')
WHERE path = 'public/units/senior-secondary/11-lesson-1-1-who-was-ranginui-walker.html' OR path LIKE '%11-lesson-1-1-who-was-ranginui-walker.html';


-- Update metadata for: A Forum for Justice: The Waitangi Tribunal | Te Ke
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'A Forum for Justice: The Waitangi Tribunal | Te Kete Ako')
WHERE path = 'public/units/senior-secondary/18-walker-lesson-1.4-a-forum-for-justice.html' OR path LIKE '%18-walker-lesson-1.4-a-forum-for-justice.html';


-- Update metadata for: NCEA Level 1 Literacy & Numeracy Must-Knows - Te K
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 1',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'NCEA Level 1 Literacy & Numeracy Must-Knows - Te Kete Ako')
WHERE path = 'public/units/senior-secondary/01-ncea-level-1-literacy-and-numeracy-must-knows.html' OR path LIKE '%01-ncea-level-1-literacy-and-numeracy-must-knows.html';


-- Update metadata for: The Great Migration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'The Great Migration | Te Kete Ako')
WHERE path = 'public/units/senior-secondary/17-walker-lesson-1.2-the-great-migration.html' OR path LIKE '%17-walker-lesson-1.2-the-great-migration.html';


-- Update metadata for: Discover Orphans
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Discover Orphans')
WHERE path = 'public/units/senior-secondary/16-orphans.html' OR path LIKE '%16-orphans.html';


-- Update metadata for: Year 10 Mathematics - Cultural Geometry Unit | Kai
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Year 10 Mathematics - Cultural Geometry Unit | Kaitiaki Aronui Generated')
WHERE path = 'public/units/senior-secondary/03-kaitiaki-generated-y10-math-cultural-geometry.html' OR path LIKE '%03-kaitiaki-generated-y10-math-cultural-geometry.html';


-- Update metadata for: Te Kete Ako - Comprehensive Site Map
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Comprehensive Site Map')
WHERE path = 'public/units/senior-secondary/08-sitemap-enhanced.html' OR path LIKE '%08-sitemap-enhanced.html';


-- Update metadata for: Ranginui Walker: A Life of Integrity - Student Han
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Ranginui Walker: A Life of Integrity - Student Handout | Te Kete Ako')
WHERE path = 'public/units/senior-secondary/20-walker-lesson-1-1-student-handout.html' OR path LIKE '%20-walker-lesson-1-1-student-handout.html';


-- Update metadata for: Lesson 1.2: The Great Migration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.2: The Great Migration | Te Kete Ako')
WHERE path = 'public/units/senior-secondary/13-lesson-1-2-the-great-migration.html' OR path LIKE '%13-lesson-1-2-the-great-migration.html';


-- Update metadata for: Lesson 1.3: Years of Anger | Walker Unit | Te Kete
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.3: Years of Anger | Walker Unit | Te Kete Ako')
WHERE path = 'public/units/senior-secondary/10-lesson-1-3-years-of-anger.html' OR path LIKE '%10-lesson-1-3-years-of-anger.html';


-- Update metadata for: AI Ethics Through Māori Data Sovereignty | Te Kete
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics Through Māori Data Sovereignty | Te Kete Ako')
WHERE path = 'public/units/senior-secondary/14-ai-ethics-through-māori-data-sovereignty-FIXED.html' OR path LIKE '%14-ai-ethics-through-māori-data-sovereignty-FIXED.html';


-- Update metadata for: Walker Unit - Teacher's Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Walker Unit - Teacher''s Guide | Te Kete Ako')
WHERE path = 'public/units/senior-secondary/04-walker-unit-overview-teacher-guide.html' OR path LIKE '%04-walker-unit-overview-teacher-guide.html';


-- Update metadata for: Plate Tectonics Reading Comprehension
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Plate Tectonics Reading Comprehension')
WHERE path = 'public/units/senior-secondary/07-plate-tectonics-comprehension-handout.html' OR path LIKE '%07-plate-tectonics-comprehension-handout.html';


-- Update metadata for: Discover Orphans
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Discover Orphans')
WHERE path = 'public/units/senior-secondary/06-orphans.html' OR path LIKE '%06-orphans.html';


-- Update metadata for: Handout: NZ Housing Crisis
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Handout: NZ Housing Crisis')
WHERE path = 'public/units/senior-secondary/05-nz-housing-crisis-handout.html' OR path LIKE '%05-nz-housing-crisis-handout.html';


-- Update metadata for: Who was Ranginui Walker? | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Who was Ranginui Walker? | Te Kete Ako')
WHERE path = 'public/units/senior-secondary/15-walker-lesson-1.1-who-was-ranginui-walker.html' OR path LIKE '%15-walker-lesson-1.1-who-was-ranginui-walker.html';


-- Update metadata for: Shakespearean Soliloquy Reading Comprehension
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Shakespearean Soliloquy Reading Comprehension')
WHERE path = 'public/units/senior-secondary/02-shakespeare-soliloquy-handout.html' OR path LIKE '%02-shakespeare-soliloquy-handout.html';


-- Update metadata for: Walker Lesson 1.1 Assessment Rubric | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Walker Lesson 1.1 Assessment Rubric | Te Kete Ako')
WHERE path = 'public/units/senior-secondary/19-walker-lesson-1-1-assessment-rubric.html' OR path LIKE '%19-walker-lesson-1-1-assessment-rubric.html';


-- Update metadata for: Lesson 3: Local Waterways Investigation | Year 7 S
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Local Waterways Investigation | Year 7 Science')
WHERE path = 'public/units/y7-science-water-cycle/lesson-3-local-waterways-investigation.html' OR path LIKE '%lesson-3-local-waterways-investigation.html';


-- Update metadata for: Lesson 1: Water Cycle Basics | Year 7 Science
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Water Cycle Basics | Year 7 Science')
WHERE path = 'public/units/y7-science-water-cycle/lesson-1-water-cycle-basics.html' OR path LIKE '%lesson-1-water-cycle-basics.html';


-- Update metadata for: Lesson 4: Water Pollution & Solutions | Year 7 Sci
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: Water Pollution & Solutions | Year 7 Science')
WHERE path = 'public/units/y7-science-water-cycle/lesson-4-water-pollution-solutions.html' OR path LIKE '%lesson-4-water-pollution-solutions.html';


-- Update metadata for: Lesson 5: Kaitiaki Water Action Project | Year 7 S
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5: Kaitiaki Water Action Project | Year 7 Science')
WHERE path = 'public/units/y7-science-water-cycle/lesson-5-kaitiaki-action-project.html' OR path LIKE '%lesson-5-kaitiaki-action-project.html';


-- Update metadata for: Lesson 2: Wai as Taonga | Year 7 Science
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: Wai as Taonga | Year 7 Science')
WHERE path = 'public/units/y7-science-water-cycle/lesson-2-wai-as-taonga.html' OR path LIKE '%lesson-2-wai-as-taonga.html';


-- Update metadata for: Y7 Mathematics: Algebra Unit (with Teaching Varian
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y7 Mathematics: Algebra Unit (with Teaching Variants) | Te Kete Ako')
WHERE path = 'public/units/y7-maths-algebra/index-with-variants.html' OR path LIKE '%index-with-variants.html';


-- Update metadata for: Practice: One-Step Equation Gauntlet
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Practice: One-Step Equation Gauntlet')
WHERE path = 'public/units/y7-maths-algebra/resources/practice-4-one-step-equation-gauntlet.html' OR path LIKE '%practice-4-one-step-equation-gauntlet.html';


-- Update metadata for: Handout: Equation Balancer
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Handout: Equation Balancer')
WHERE path = 'public/units/y7-maths-algebra/resources/handout-4-equation-balancer.html' OR path LIKE '%handout-4-equation-balancer.html';


-- Update metadata for: Handout: Variable Vocabulary
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Handout: Variable Vocabulary')
WHERE path = 'public/units/y7-maths-algebra/resources/handout-2-variable-vocabulary.html' OR path LIKE '%handout-2-variable-vocabulary.html';


-- Update metadata for: Activity: The Pattern Machine
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Activity: The Pattern Machine')
WHERE path = 'public/units/y7-maths-algebra/resources/activity-1-pattern-machine.html' OR path LIKE '%activity-1-pattern-machine.html';


-- Update metadata for: Activity: Real-World Algebra
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Activity: Real-World Algebra')
WHERE path = 'public/units/y7-maths-algebra/resources/activity-5-real-world-algebra.html' OR path LIKE '%activity-5-real-world-algebra.html';


-- Update metadata for: Practice: Two-Step Equation Marathon
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Practice: Two-Step Equation Marathon')
WHERE path = 'public/units/y7-maths-algebra/resources/practice-5-two-step-equation-marathon.html' OR path LIKE '%practice-5-two-step-equation-marathon.html';


-- Update metadata for: Activity: Algebraic Charades
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Activity: Algebraic Charades')
WHERE path = 'public/units/y7-maths-algebra/resources/activity-2-algebraic-charades.html' OR path LIKE '%activity-2-algebraic-charades.html';


-- Update metadata for: 🔍 Patterns & Algebra Vocabulary
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), '🔍 Patterns & Algebra Vocabulary')
WHERE path = 'public/units/y7-maths-algebra/resources/wordsearch-patterns-nyt.html' OR path LIKE '%wordsearch-patterns-nyt.html';


-- Update metadata for: Activity: Equation Relay
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Activity: Equation Relay')
WHERE path = 'public/units/y7-maths-algebra/resources/activity-4-equation-relay.html' OR path LIKE '%activity-4-equation-relay.html';


-- Update metadata for: Practice: Sequence Drills
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Practice: Sequence Drills')
WHERE path = 'public/units/y7-maths-algebra/resources/practice-1-sequence-drills.html' OR path LIKE '%practice-1-sequence-drills.html';


-- Update metadata for: Activity: Tukutuku Tile Challenge
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Activity: Tukutuku Tile Challenge')
WHERE path = 'public/units/y7-maths-algebra/resources/activity-3-tukutuku-tile-challenge.html' OR path LIKE '%activity-3-tukutuku-tile-challenge.html';


-- Update metadata for: Practice: Rule-Finder
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Practice: Rule-Finder')
WHERE path = 'public/units/y7-maths-algebra/resources/practice-3-rule-finder.html' OR path LIKE '%practice-3-rule-finder.html';


-- Update metadata for: Game: Pattern Dominoes
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Game: Pattern Dominoes')
WHERE path = 'public/units/y7-maths-algebra/resources/game-1-pattern-dominoes.html' OR path LIKE '%game-1-pattern-dominoes.html';


-- Update metadata for: Practice: Translating Words to Algebra
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Practice: Translating Words to Algebra')
WHERE path = 'public/units/y7-maths-algebra/resources/practice-2-translating-words-to-algebra.html' OR path LIKE '%practice-2-translating-words-to-algebra.html';


-- Update metadata for: Handout: Kōwhaiwhai Patterns
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Handout: Kōwhaiwhai Patterns')
WHERE path = 'public/units/y7-maths-algebra/resources/handout-3-kowhaiwhai-patterns.html' OR path LIKE '%handout-3-kowhaiwhai-patterns.html';


-- Update metadata for: Handout: Pattern Detectives
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Handout: Pattern Detectives')
WHERE path = 'public/units/y7-maths-algebra/resources/handout-1-pattern-detectives.html' OR path LIKE '%handout-1-pattern-detectives.html';


-- Update metadata for: Assessment: Design a Tukutuku Panel
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Assessment: Design a Tukutuku Panel')
WHERE path = 'public/units/y7-maths-algebra/assessment/summative-project-tukutuku-panel.html' OR path LIKE '%summative-project-tukutuku-panel.html';


-- Update metadata for: Lesson 5: The Two-Step Shuffle
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5: The Two-Step Shuffle')
WHERE path = 'public/units/y7-maths-algebra/lessons/lesson-5-the-two-step-shuffle.html' OR path LIKE '%lesson-5-the-two-step-shuffle.html';


-- Update metadata for: Lesson 2: The Mystery of 'x'
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: The Mystery of ''x''')
WHERE path = 'public/units/y7-maths-algebra/lessons/lesson-2-the-mystery-of-x.html' OR path LIKE '%lesson-2-the-mystery-of-x.html';


-- Update metadata for: Lesson 4: Balancing Act
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: Balancing Act')
WHERE path = 'public/units/y7-maths-algebra/lessons/lesson-4-balancing-act.html' OR path LIKE '%lesson-4-balancing-act.html';


-- Update metadata for: Lesson 1: Pattern Detectives
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Pattern Detectives')
WHERE path = 'public/units/y7-maths-algebra/lessons/lesson-1-patterns-and-sequences.html' OR path LIKE '%lesson-1-patterns-and-sequences.html';


-- Update metadata for: Lesson 3: Building with Algebra
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Building with Algebra')
WHERE path = 'public/units/y7-maths-algebra/lessons/lesson-3-building-with-algebra.html' OR path LIKE '%lesson-3-building-with-algebra.html';


-- Update metadata for: Comprehensive: Whakapapa Deep Dive Activities - Un
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Comprehensive: Whakapapa Deep Dive Activities - Unit 1 Lesson 1')
WHERE path = 'public/units/resources/unit-1-lesson-1-whakapapa-deep-dive-activities.html' OR path LIKE '%unit-1-lesson-1-whakapapa-deep-dive-activities.html';


-- Update metadata for: Printable: Tikanga Scenarios for Discussion
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Tikanga Scenarios for Discussion')
WHERE path = 'public/units/resources/unit-1-lesson-2-tikanga-scenarios.html' OR path LIKE '%unit-1-lesson-2-tikanga-scenarios.html';


-- Update metadata for: Printable: Whakapapa Exploration Template
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Whakapapa Exploration Template')
WHERE path = 'public/units/resources/unit-1-lesson-1-whakapapa-template.html' OR path LIKE '%unit-1-lesson-1-whakapapa-template.html';


-- Update metadata for: Unit 2: Decolonized History - Assessment Portfolio
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 2: Decolonized History - Assessment Portfolio Rubric | Te Kete Ako')
WHERE path = 'public/units/resources/unit-2-assessment-portfolio-rubric.html' OR path LIKE '%unit-2-assessment-portfolio-rubric.html';


-- Update metadata for: Assessment: Unit 1 Te Ao Māori Portfolio Rubric
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Assessment: Unit 1 Te Ao Māori Portfolio Rubric')
WHERE path = 'public/units/resources/unit-1-assessment-portfolio-rubric.html' OR path LIKE '%unit-1-assessment-portfolio-rubric.html';


-- Update metadata for: Printable: Mātauranga Māori Inquiry Cards
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Mātauranga Māori Inquiry Cards')
WHERE path = 'public/units/resources/unit-1-lesson-3-matauranga-inquiry-cards.html' OR path LIKE '%unit-1-lesson-3-matauranga-inquiry-cards.html';


-- Update metadata for: A Forum for Justice: The Waitangi Tribunal | Te Ke
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'A Forum for Justice: The Waitangi Tribunal | Te Kete Ako')
WHERE path = 'public/units/walker-unit/walker-lesson-1.4-a-forum-for-justice.html' OR path LIKE '%walker-lesson-1.4-a-forum-for-justice.html';


-- Update metadata for: Years of Anger: The Protest Movements | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Years of Anger: The Protest Movements | Te Kete Ako')
WHERE path = 'public/units/walker-unit/walker-lesson-1.3-years-of-anger.html' OR path LIKE '%walker-lesson-1.3-years-of-anger.html';


-- Update metadata for: Who was Ranginui Walker? | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Who was Ranginui Walker? | Te Kete Ako')
WHERE path = 'public/units/walker-unit/walker-lesson-1.1-who-was-ranginui-walker.html' OR path LIKE '%walker-lesson-1.1-who-was-ranginui-walker.html';


-- Update metadata for: Reclaiming the Narrative: Ka Whawhai Tonu Mātou | 
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Reclaiming the Narrative: Ka Whawhai Tonu Mātou | Te Kete Ako')
WHERE path = 'public/units/walker-unit/walker-lesson-1.5-reclaiming-the-narrative.html' OR path LIKE '%walker-lesson-1.5-reclaiming-the-narrative.html';


-- Update metadata for: The Great Migration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'The Great Migration | Te Kete Ako')
WHERE path = 'public/units/walker-unit/walker-lesson-1.2-the-great-migration.html' OR path LIKE '%walker-lesson-1.2-the-great-migration.html';


-- Update metadata for: Lesson 6.5: Legislative Change - Power & Limits | 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6.5: Legislative Change - Power & Limits | Te Kete Ako')
WHERE path = 'public/units/wetere-unit/lesson-6-5-legislative-change-limits.html' OR path LIKE '%lesson-6-5-legislative-change-limits.html';


-- Update metadata for: Lesson 6.3: Treaty Settlement Process | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6.3: Treaty Settlement Process | Te Kete Ako')
WHERE path = 'public/units/wetere-unit/lesson-6-3-treaty-settlement-process.html' OR path LIKE '%lesson-6-3-treaty-settlement-process.html';


-- Update metadata for: Lesson 6.2: Māori Language Act 1987 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6.2: Māori Language Act 1987 | Te Kete Ako')
WHERE path = 'public/units/wetere-unit/lesson-6-2-maori-language-act.html' OR path LIKE '%lesson-6-2-maori-language-act.html';


-- Update metadata for: Lesson 6.4: Political Compromise vs Integrity | Te
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6.4: Political Compromise vs Integrity | Te Kete Ako')
WHERE path = 'public/units/wetere-unit/lesson-6-4-political-compromise-integrity.html' OR path LIKE '%lesson-6-4-political-compromise-integrity.html';


-- Update metadata for: Lesson 6.1: Who Was Koro Wētere? | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6.1: Who Was Koro Wētere? | Te Kete Ako')
WHERE path = 'public/units/wetere-unit/lesson-6-1-who-was-koro-wetere.html' OR path LIKE '%lesson-6-1-who-was-koro-wetere.html';


-- Update metadata for: Printable: Indigenous Systems Examples
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Systems Examples')
WHERE path = 'public/units/science/06-indigenous-systems-examples.html' OR path LIKE '%06-indigenous-systems-examples.html';


-- Update metadata for: Guided Inquiry Unit | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/units/science/047-index.html' OR path LIKE '%047-index.html';


-- Update metadata for: Subjects | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Subjects | Te Kete Ako')
WHERE path = 'public/units/science/040-subjects.html' OR path LIKE '%040-subjects.html';


-- Update metadata for: Printable: Gallery Walk Statements
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Gallery Walk Statements')
WHERE path = 'public/units/science/13-gallery-walk-statements.html' OR path LIKE '%13-gallery-walk-statements.html';


-- Update metadata for: Unit 2, Lesson 3: The Fight for Rights
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 3: The Fight for Rights')
WHERE path = 'public/units/science/029-unit-2-lesson-3.html' OR path LIKE '%029-unit-2-lesson-3.html';


-- Update metadata for: Resource: Frayer Model for "System" | Y8 Systems |
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Resource: Frayer Model for "System" | Y8 Systems | Te Kete Ako')
WHERE path = 'public/units/science/038-frayer-model-system.html' OR path LIKE '%038-frayer-model-system.html';


-- Update metadata for: Climate Science Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Climate Science Lesson | Te Kete Ako')
WHERE path = 'public/units/science/024-climate-science-lesson.html' OR path LIKE '%024-climate-science-lesson.html';


-- Update metadata for: Printable: Decolonization Commitment Template
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Decolonization Commitment Template')
WHERE path = 'public/units/science/033-decolonization-commitment-template.html' OR path LIKE '%033-decolonization-commitment-template.html';


-- Update metadata for: Printable: Design a System Template
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Design a System Template')
WHERE path = 'public/units/science/035-design-a-system-template.html' OR path LIKE '%035-design-a-system-template.html';


-- Update metadata for: Author's Purpose: Persuade | Mangakōtukutuku Colle
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Author''s Purpose: Persuade | Mangakōtukutuku College')
WHERE path = 'public/units/science/017-authors-purpose-persuade-handout.html' OR path LIKE '%017-authors-purpose-persuade-handout.html';


-- Update metadata for: Printable: Traditional Māori Governance Systems
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Traditional Māori Governance Systems')
WHERE path = 'public/units/science/08-maori-governance-systems.html' OR path LIKE '%08-maori-governance-systems.html';


-- Update metadata for: Unit 2, Lesson 3: The Fight for Rights
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 3: The Fight for Rights')
WHERE path = 'public/units/science/12-unit-2-lesson-3.html' OR path LIKE '%12-unit-2-lesson-3.html';


-- Update metadata for: Lesson 1.2: The Great Migration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.2: The Great Migration | Te Kete Ako')
WHERE path = 'public/units/science/09-lesson-1-2-the-great-migration.html' OR path LIKE '%09-lesson-1-2-the-great-migration.html';


-- Update metadata for: Traditional Materials Science | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Traditional Materials Science | Te Kete Ako')
WHERE path = 'public/units/science/044-traditional-materials-science.html' OR path LIKE '%044-traditional-materials-science.html';


-- Update metadata for: Y8 Systems | Lesson 5.2: Present & Reflect
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y8 Systems | Lesson 5.2: Present & Reflect')
WHERE path = 'public/units/science/04-lesson-5-2.html' OR path LIKE '%04-lesson-5-2.html';


-- Update metadata for: Government Component Analysis Worksheet | Te Kete 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Government Component Analysis Worksheet | Te Kete Ako')
WHERE path = 'public/units/science/049-government-component-analysis-worksheet.html' OR path LIKE '%049-government-component-analysis-worksheet.html';


-- Update metadata for: Waka Physics Basics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Waka Physics Basics | Te Kete Ako')
WHERE path = 'public/units/science/043-waka-physics-basics.html' OR path LIKE '%043-waka-physics-basics.html';


-- Update metadata for: 🤖 DeepSeek + GraphRAG Terminal
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), '🤖 DeepSeek + GraphRAG Terminal')
WHERE path = 'public/units/science/046-deepseek-graphrag-terminal.html' OR path LIKE '%046-deepseek-graphrag-terminal.html';


-- Update metadata for: Site Map | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Site Map | Te Kete Ako')
WHERE path = 'public/units/science/042-site-map.html' OR path LIKE '%042-site-map.html';


-- Update metadata for: Unit 2, Lesson 5: The Path to Redress
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 5: The Path to Redress')
WHERE path = 'public/units/science/034-unit-2-lesson-5.html' OR path LIKE '%034-unit-2-lesson-5.html';


-- Update metadata for: Comprehensive Resource Directory
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Comprehensive Resource Directory')
WHERE path = 'public/units/science/041-sitemap-enhanced.html' OR path LIKE '%041-sitemap-enhanced.html';


-- Update metadata for: Integrated Lessons Library | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Integrated Lessons Library | Te Kete Ako')
WHERE path = 'public/units/science/018-index.html' OR path LIKE '%018-index.html';


-- Update metadata for: The Writer's Toolkit: Informational Structures | M
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Informational Structures | Mangakōtukutuku College')
WHERE path = 'public/units/science/036-writers-toolkit-inform-structure-handout.html' OR path LIKE '%036-writers-toolkit-inform-structure-handout.html';


-- Update metadata for: The Writer's Toolkit: Formal vs. Informal Tone
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Formal vs. Informal Tone')
WHERE path = 'public/units/science/028-writers-toolkit-tone-handout.html' OR path LIKE '%028-writers-toolkit-tone-handout.html';


-- Update metadata for: Author's Purpose: Persuade | Mangakōtukutuku Colle
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Author''s Purpose: Persuade | Mangakōtukutuku College')
WHERE path = 'public/units/science/02-authors-purpose-persuade-handout.html' OR path LIKE '%02-authors-purpose-persuade-handout.html';


-- Update metadata for: Printable: Colonization Timeline
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Colonization Timeline')
WHERE path = 'public/units/science/10-colonization-timeline.html' OR path LIKE '%10-colonization-timeline.html';


-- Update metadata for: The Writer's Toolkit: Formal vs. Informal Tone
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Formal vs. Informal Tone')
WHERE path = 'public/units/science/11-writers-toolkit-tone-handout.html' OR path LIKE '%11-writers-toolkit-tone-handout.html';


-- Update metadata for: Video Activity: The Legends of Māui | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Video Activity: The Legends of Māui | Te Kete Ako')
WHERE path = 'public/units/science/01-maui-video-activity.html' OR path LIKE '%01-maui-video-activity.html';


-- Update metadata for: Lesson 1.2: The Great Migration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.2: The Great Migration | Te Kete Ako')
WHERE path = 'public/units/science/026-lesson-1-2-the-great-migration.html' OR path LIKE '%026-lesson-1-2-the-great-migration.html';


-- Update metadata for: Guided Inquiry: Design Your Society | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Guided Inquiry: Design Your Society | Te Kete Ako')
WHERE path = 'public/units/science/048-guided-inquiry-society-design.html' OR path LIKE '%048-guided-inquiry-society-design.html';


-- Update metadata for: Printable: Indigenous Systems Examples
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Systems Examples')
WHERE path = 'public/units/science/022-indigenous-systems-examples.html' OR path LIKE '%022-indigenous-systems-examples.html';


-- Update metadata for: Physics Of Traditional Games | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Physics Of Traditional Games | Te Kete Ako')
WHERE path = 'public/units/science/045-physics-of-traditional-games.html' OR path LIKE '%045-physics-of-traditional-games.html';


-- Update metadata for: Printable: Indigenous Feedback Framework
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Feedback Framework')
WHERE path = 'public/units/science/020-indigenous-feedback-framework.html' OR path LIKE '%020-indigenous-feedback-framework.html';


-- Update metadata for: Printable: Indigenous Feedback Framework
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Feedback Framework')
WHERE path = 'public/units/science/05-indigenous-feedback-framework.html' OR path LIKE '%05-indigenous-feedback-framework.html';


-- Update metadata for: Unit 2, Lesson 2: The Aotearoa Wars
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 2: The Aotearoa Wars')
WHERE path = 'public/units/science/15-unit-2-lesson-2.html' OR path LIKE '%15-unit-2-lesson-2.html';


-- Update metadata for: Y8 Systems | Lesson 5.1: Guided Inquiry Project La
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y8 Systems | Lesson 5.1: Guided Inquiry Project Launch - Design Your Society')
WHERE path = 'public/units/science/039-lesson-5-1.html' OR path LIKE '%039-lesson-5-1.html';


-- Update metadata for: Printable Resource: System Sorting Cards
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable Resource: System Sorting Cards')
WHERE path = 'public/units/science/037-system-sorting-cards.html' OR path LIKE '%037-system-sorting-cards.html';


-- Update metadata for: Integrated Lessons Library | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Integrated Lessons Library | Te Kete Ako')
WHERE path = 'public/units/science/03-index.html' OR path LIKE '%03-index.html';


-- Update metadata for: Printable: Indigenous Governance Principles
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Governance Principles')
WHERE path = 'public/units/science/031-indigenous-governance-principles.html' OR path LIKE '%031-indigenous-governance-principles.html';


-- Update metadata for: Y8 Systems | Lesson 5.2: Present & Reflect
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y8 Systems | Lesson 5.2: Present & Reflect')
WHERE path = 'public/units/science/019-lesson-5-2.html' OR path LIKE '%019-lesson-5-2.html';


-- Update metadata for: Rongoa Science Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Rongoa Science Lesson | Te Kete Ako')
WHERE path = 'public/units/science/021-rongoa-science-lesson.html' OR path LIKE '%021-rongoa-science-lesson.html';


-- Update metadata for: Te Ao Māori Unit | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Te Ao Māori Unit | Te Kete Ako')
WHERE path = 'public/units/science/050-index.html' OR path LIKE '%050-index.html';


-- Update metadata for: The Writer's Toolkit: Word Choice (Diction)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Word Choice (Diction)')
WHERE path = 'public/units/science/07-writers-toolkit-diction-handout.html' OR path LIKE '%07-writers-toolkit-diction-handout.html';


-- Update metadata for: Printable: Traditional Māori Governance Systems
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Traditional Māori Governance Systems')
WHERE path = 'public/units/science/025-maori-governance-systems.html' OR path LIKE '%025-maori-governance-systems.html';


-- Update metadata for: Printable: Gallery Walk Statements
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Gallery Walk Statements')
WHERE path = 'public/units/science/030-gallery-walk-statements.html' OR path LIKE '%030-gallery-walk-statements.html';


-- Update metadata for: Video Activity: The Legends of Māui | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Video Activity: The Legends of Māui | Te Kete Ako')
WHERE path = 'public/units/science/016-maui-video-activity.html' OR path LIKE '%016-maui-video-activity.html';


-- Update metadata for: Printable: Colonization Timeline
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Colonization Timeline')
WHERE path = 'public/units/science/027-colonization-timeline.html' OR path LIKE '%027-colonization-timeline.html';


-- Update metadata for: Printable: Indigenous Governance Principles
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Governance Principles')
WHERE path = 'public/units/science/14-indigenous-governance-principles.html' OR path LIKE '%14-indigenous-governance-principles.html';


-- Update metadata for: The Writer's Toolkit: Word Choice (Diction)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Word Choice (Diction)')
WHERE path = 'public/units/science/023-writers-toolkit-diction-handout.html' OR path LIKE '%023-writers-toolkit-diction-handout.html';


-- Update metadata for: Unit 2, Lesson 2: The Aotearoa Wars
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 2: The Aotearoa Wars')
WHERE path = 'public/units/science/032-unit-2-lesson-2.html' OR path LIKE '%032-unit-2-lesson-2.html';


-- Update metadata for: Lesson 2: Food Chains & Food Webs (Y7)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: Food Chains & Food Webs (Y7)')
WHERE path = 'public/units/y7-science-ecosystems/lessons/lesson-2-food-webs.html' OR path LIKE '%lesson-2-food-webs.html';


-- Update metadata for: Lesson 1: Kaitiakitanga & Local Ecosystems (Y7)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Kaitiakitanga & Local Ecosystems (Y7)')
WHERE path = 'public/units/y7-science-ecosystems/lessons/lesson-1-kaitiakitanga-intro.html' OR path LIKE '%lesson-1-kaitiakitanga-intro.html';


-- Update metadata for: Lesson 3: Human Impacts & Kaitiaki Action (Y7)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Human Impacts & Kaitiaki Action (Y7)')
WHERE path = 'public/units/y7-science-ecosystems/lessons/lesson-3-human-impacts.html' OR path LIKE '%lesson-3-human-impacts.html';


-- Update metadata for: Lesson 5.1: Who Was Eva Rickard? | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5.1: Who Was Eva Rickard? | Te Kete Ako')
WHERE path = 'public/units/rickard-unit/lesson-5-1-who-was-eva-rickard.html' OR path LIKE '%lesson-5-1-who-was-eva-rickard.html';


-- Update metadata for: Lesson 5.5: Victory & Legacy | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5.5: Victory & Legacy | Te Kete Ako')
WHERE path = 'public/units/rickard-unit/lesson-5-5-victory-and-legacy.html' OR path LIKE '%lesson-5-5-victory-and-legacy.html';


-- Update metadata for: Lesson 5.4: Ethics of Civil Disobedience | Te Kete
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5.4: Ethics of Civil Disobedience | Te Kete Ako')
WHERE path = 'public/units/rickard-unit/lesson-5-4-civil-disobedience-ethics.html' OR path LIKE '%lesson-5-4-civil-disobedience-ethics.html';


-- Update metadata for: Lesson 5.3: The Occupation - 507 Days | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5.3: The Occupation - 507 Days | Te Kete Ako')
WHERE path = 'public/units/rickard-unit/lesson-5-3-the-occupation.html' OR path LIKE '%lesson-5-3-the-occupation.html';


-- Update metadata for: Lesson 5.2: Te Kōpua Stolen | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5.2: Te Kōpua Stolen | Te Kete Ako')
WHERE path = 'public/units/rickard-unit/lesson-5-2-stolen-land.html' OR path LIKE '%lesson-5-2-stolen-land.html';


-- Update metadata for: Lesson 1: Māramataka Introduction (Y8 Statistics)
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Māramataka Introduction (Y8 Statistics)')
WHERE path = 'public/units/y8-statistics-maramataka/lessons/lesson-1-maramataka-intro.html' OR path LIKE '%lesson-1-maramataka-intro.html';


-- Update metadata for: Resource Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Resource Hub | Te Kete Ako')
WHERE path = 'public/units/math/022-resource-hub.html' OR path LIKE '%022-resource-hub.html';


-- Update metadata for: Whakapapa Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Whakapapa Mathematics | Te Kete Ako')
WHERE path = 'public/units/math/12-whakapapa-mathematics.html' OR path LIKE '%12-whakapapa-mathematics.html';


-- Update metadata for: Tukutuku Numeracy Problems | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Numeracy Problems | Te Kete Ako')
WHERE path = 'public/units/math/019-tukutuku-numeracy-problems.html' OR path LIKE '%019-tukutuku-numeracy-problems.html';


-- Update metadata for: Tukutuku Pattern Generator | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Pattern Generator | Te Kete Ako')
WHERE path = 'public/units/math/018-tukutuku-pattern-generator.html' OR path LIKE '%018-tukutuku-pattern-generator.html';


-- Update metadata for: Whakapapa Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Whakapapa Mathematics | Te Kete Ako')
WHERE path = 'public/units/math/024-whakapapa-mathematics.html' OR path LIKE '%024-whakapapa-mathematics.html';


-- Update metadata for: Algebraic Patterns Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Algebraic Patterns Lesson | Te Kete Ako')
WHERE path = 'public/units/math/023-algebraic-patterns-lesson.html' OR path LIKE '%023-algebraic-patterns-lesson.html';


-- Update metadata for: Resource Discovery Hub - Te Kete Ako V2.5
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Resource Discovery Hub - Te Kete Ako V2.5')
WHERE path = 'public/units/math/05-resource-discovery-hub.html' OR path LIKE '%05-resource-discovery-hub.html';


-- Update metadata for: NCEA Level 1 Literacy & Numeracy Must-Knows - Te K
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 1',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'NCEA Level 1 Literacy & Numeracy Must-Knows - Te Kete Ako')
WHERE path = 'public/units/math/01-ncea-level-1-literacy-and-numeracy-must-knows.html' OR path LIKE '%01-ncea-level-1-literacy-and-numeracy-must-knows.html';


-- Update metadata for: Activity: Algebraic Charades
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Activity: Algebraic Charades')
WHERE path = 'public/units/math/042-activity-2-algebraic-charades.html' OR path LIKE '%042-activity-2-algebraic-charades.html';


-- Update metadata for: Sports Data Analysis Worksheet - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Sports Data Analysis Worksheet - Y8 Statistics')
WHERE path = 'public/units/math/032-y8-statistics-sports-data-analysis.html' OR path LIKE '%032-y8-statistics-sports-data-analysis.html';


-- Update metadata for: Probability Experiments Recording Sheet - Y8 Stati
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Probability Experiments Recording Sheet - Y8 Statistics')
WHERE path = 'public/units/math/039-y8-statistics-probability-experiments.html' OR path LIKE '%039-y8-statistics-probability-experiments.html';


-- Update metadata for: Tukutuku Patterns Maths | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Patterns Maths | Te Kete Ako')
WHERE path = 'public/units/math/025-tukutuku-patterns-maths.html' OR path LIKE '%025-tukutuku-patterns-maths.html';


-- Update metadata for: Y7/8 Maths - Introduction to Algebra
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y7/8 Maths - Introduction to Algebra')
WHERE path = 'public/units/math/036-index.html' OR path LIKE '%036-index.html';


-- Update metadata for: Activity: Tukutuku Tile Challenge
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Activity: Tukutuku Tile Challenge')
WHERE path = 'public/units/math/043-activity-3-tukutuku-tile-challenge.html' OR path LIKE '%043-activity-3-tukutuku-tile-challenge.html';


-- Update metadata for: Maramataka Time Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Maramataka Time Mathematics | Te Kete Ako')
WHERE path = 'public/units/math/030-maramataka-time-mathematics.html' OR path LIKE '%030-maramataka-time-mathematics.html';


-- Update metadata for: Sports Data Analysis Worksheet - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Sports Data Analysis Worksheet - Y8 Statistics')
WHERE path = 'public/units/math/07-y8-statistics-sports-data-analysis.html' OR path LIKE '%07-y8-statistics-sports-data-analysis.html';


-- Update metadata for: Recipe Scaling Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Recipe Scaling Mathematics | Te Kete Ako')
WHERE path = 'public/units/math/15-recipe-scaling-mathematics.html' OR path LIKE '%15-recipe-scaling-mathematics.html';


-- Update metadata for: NCEA Level 1 Literacy & Numeracy Must-Knows - Te K
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 1',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'NCEA Level 1 Literacy & Numeracy Must-Knows - Te Kete Ako')
WHERE path = 'public/units/math/016-ncea-level-1-literacy-and-numeracy-must-knows.html' OR path LIKE '%016-ncea-level-1-literacy-and-numeracy-must-knows.html';


-- Update metadata for: Marae Shapes Geometry | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Marae Shapes Geometry | Te Kete Ako')
WHERE path = 'public/units/math/035-marae-shapes-geometry.html' OR path LIKE '%035-marae-shapes-geometry.html';


-- Update metadata for: Cultural Authenticity Test - Te Reo Māori Wordle
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Cultural Authenticity Test - Te Reo Māori Wordle')
WHERE path = 'public/units/math/038-test-cultural-authenticity.html' OR path LIKE '%038-test-cultural-authenticity.html';


-- Update metadata for: Recipe Scaling Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Recipe Scaling Mathematics | Te Kete Ako')
WHERE path = 'public/units/math/027-recipe-scaling-mathematics.html' OR path LIKE '%027-recipe-scaling-mathematics.html';


-- Update metadata for: Data Types Sorting Activity - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Data Types Sorting Activity - Y8 Statistics')
WHERE path = 'public/units/math/08-y8-statistics-data-types-sorting.html' OR path LIKE '%08-y8-statistics-data-types-sorting.html';


-- Update metadata for: Census Data Analysis Worksheet - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Census Data Analysis Worksheet - Y8 Statistics')
WHERE path = 'public/units/math/037-y8-statistics-census-data-worksheet.html' OR path LIKE '%037-y8-statistics-census-data-worksheet.html';


-- Update metadata for: Algebraic Thinking in Traditional Māori Games | Te
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Algebraic Thinking in Traditional Māori Games | Te Kete Ako')
WHERE path = 'public/units/math/02-algebraic-thinking-in-traditional-māori-games.html' OR path LIKE '%02-algebraic-thinking-in-traditional-māori-games.html';


-- Update metadata for: Resource Discovery Hub - Te Kete Ako V2.5
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Resource Discovery Hub - Te Kete Ako V2.5')
WHERE path = 'public/units/math/020-resource-discovery-hub.html' OR path LIKE '%020-resource-discovery-hub.html';


-- Update metadata for: Algebraic Patterns Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Algebraic Patterns Lesson | Te Kete Ako')
WHERE path = 'public/units/math/11-algebraic-patterns-lesson.html' OR path LIKE '%11-algebraic-patterns-lesson.html';


-- Update metadata for: Iwi Economics Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Iwi Economics Mathematics | Te Kete Ako')
WHERE path = 'public/units/math/028-iwi-economics-mathematics.html' OR path LIKE '%028-iwi-economics-mathematics.html';


-- Update metadata for: Calculus Applications in Environmental Modeling
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Calculus Applications in Environmental Modeling')
WHERE path = 'public/units/math/034-calculus-applications-in-environmental-modeling.html' OR path LIKE '%034-calculus-applications-in-environmental-modeling.html';


-- Update metadata for: Waka Construction Geometry | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Waka Construction Geometry | Te Kete Ako')
WHERE path = 'public/units/math/031-waka-construction-geometry.html' OR path LIKE '%031-waka-construction-geometry.html';


-- Update metadata for: Activity: Real-World Algebra
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Activity: Real-World Algebra')
WHERE path = 'public/units/math/041-activity-5-real-world-algebra.html' OR path LIKE '%041-activity-5-real-world-algebra.html';


-- Update metadata for: Calculus Applications in Environmental Modeling
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Calculus Applications in Environmental Modeling')
WHERE path = 'public/units/math/09-calculus-applications-in-environmental-modeling.html' OR path LIKE '%09-calculus-applications-in-environmental-modeling.html';


-- Update metadata for: Tukutuku Numeracy Problems | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Numeracy Problems | Te Kete Ako')
WHERE path = 'public/units/math/04-tukutuku-numeracy-problems.html' OR path LIKE '%04-tukutuku-numeracy-problems.html';


-- Update metadata for: Tukutuku Patterns Maths | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Patterns Maths | Te Kete Ako')
WHERE path = 'public/units/math/13-tukutuku-patterns-maths.html' OR path LIKE '%13-tukutuku-patterns-maths.html';


-- Update metadata for: Algebraic Thinking in Traditional Māori Games | Te
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Algebraic Thinking in Traditional Māori Games | Te Kete Ako')
WHERE path = 'public/units/math/017-algebraic-thinking-in-traditional-māori-games.html' OR path LIKE '%017-algebraic-thinking-in-traditional-māori-games.html';


-- Update metadata for: Data Types Sorting Activity - Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Data Types Sorting Activity - Y8 Statistics')
WHERE path = 'public/units/math/033-y8-statistics-data-types-sorting.html' OR path LIKE '%033-y8-statistics-data-types-sorting.html';


-- Update metadata for: Practice: Rule-Finder
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Practice: Rule-Finder')
WHERE path = 'public/units/math/044-practice-3-rule-finder.html' OR path LIKE '%044-practice-3-rule-finder.html';


-- Update metadata for: Resource Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Resource Hub | Te Kete Ako')
WHERE path = 'public/units/math/06-resource-hub.html' OR path LIKE '%06-resource-hub.html';


-- Update metadata for: Navigation Mathematics Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Navigation Mathematics Lesson | Te Kete Ako')
WHERE path = 'public/units/math/10-navigation-mathematics-lesson.html' OR path LIKE '%10-navigation-mathematics-lesson.html';


-- Update metadata for: Handout: Variable Vocabulary
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Handout: Variable Vocabulary')
WHERE path = 'public/units/math/040-handout-2-variable-vocabulary.html' OR path LIKE '%040-handout-2-variable-vocabulary.html';


-- Update metadata for: Tukutuku Pattern Generator | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Pattern Generator | Te Kete Ako')
WHERE path = 'public/units/math/03-tukutuku-pattern-generator.html' OR path LIKE '%03-tukutuku-pattern-generator.html';


-- Update metadata for: Ceremonial Circle Geometry | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Ceremonial Circle Geometry | Te Kete Ako')
WHERE path = 'public/units/math/029-ceremonial-circle-geometry.html' OR path LIKE '%029-ceremonial-circle-geometry.html';


-- Update metadata for: Resource Allocation Algebra | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Resource Allocation Algebra | Te Kete Ako')
WHERE path = 'public/units/math/026-resource-allocation-algebra.html' OR path LIKE '%026-resource-allocation-algebra.html';


-- Update metadata for: Navigation Mathematics: Wayfinding & Trigonometry 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Navigation Mathematics: Wayfinding & Trigonometry | Te Kete Ako')
WHERE path = 'public/units/math/021-navigation-mathematics-lesson.html' OR path LIKE '%021-navigation-mathematics-lesson.html';


-- Update metadata for: Resource Allocation Algebra | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Resource Allocation Algebra | Te Kete Ako')
WHERE path = 'public/units/math/14-resource-allocation-algebra.html' OR path LIKE '%14-resource-allocation-algebra.html';


-- Update metadata for: A Stand for Peace | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'A Stand for Peace | Te Kete Ako')
WHERE path = 'public/units/herangi-unit/lesson-2-3-stand-for-peace.html' OR path LIKE '%lesson-2-3-stand-for-peace.html';


-- Update metadata for: Who Was Te Puea Hērangi? | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Who Was Te Puea Hērangi? | Te Kete Ako')
WHERE path = 'public/units/herangi-unit/lesson-2-1-who-was-te-puea-herangi.html' OR path LIKE '%lesson-2-1-who-was-te-puea-herangi.html';


-- Update metadata for: The Politics of Mana | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'The Politics of Mana | Te Kete Ako')
WHERE path = 'public/units/herangi-unit/lesson-2-5-politics-of-mana.html' OR path LIKE '%lesson-2-5-politics-of-mana.html';


-- Update metadata for: The Legacy of Raupatu | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'The Legacy of Raupatu | Te Kete Ako')
WHERE path = 'public/units/herangi-unit/lesson-2-2-legacy-of-raupatu.html' OR path LIKE '%lesson-2-2-legacy-of-raupatu.html';


-- Update metadata for: Tūrangawaewae - A Place to Stand | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Tūrangawaewae - A Place to Stand | Te Kete Ako')
WHERE path = 'public/units/herangi-unit/lesson-2-4-turangawaewae.html' OR path LIKE '%lesson-2-4-turangawaewae.html';


-- Update metadata for: Printable: Decolonization Today
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Decolonization Today')
WHERE path = 'public/units/english/016-decolonization-today.html' OR path LIKE '%016-decolonization-today.html';


-- Update metadata for: Printable: Decolonization Today
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Printable: Decolonization Today')
WHERE path = 'public/units/english/03-decolonization-today.html' OR path LIKE '%03-decolonization-today.html';


-- Update metadata for: 🔍 Kimi Rauemi - Search Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), '🔍 Kimi Rauemi - Search Te Kete Ako')
WHERE path = 'public/units/english/07-search.html' OR path LIKE '%07-search.html';


-- Update metadata for: Games | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Games | Te Kete Ako')
WHERE path = 'public/units/english/026-games.html' OR path LIKE '%026-games.html';


-- Update metadata for: Family Tree Writing | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Family Tree Writing | Te Kete Ako')
WHERE path = 'public/units/english/021-family-tree-writing.html' OR path LIKE '%021-family-tree-writing.html';


-- Update metadata for: Digital Storytelling with Pūrākau Framework
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Digital Storytelling with Pūrākau Framework')
WHERE path = 'public/units/english/019-digital-storytelling-with-pūrākau-framework.html' OR path LIKE '%019-digital-storytelling-with-pūrākau-framework.html';


-- Update metadata for: Digital Storytelling with Pūrākau Framework
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Digital Storytelling with Pūrākau Framework')
WHERE path = 'public/units/english/05-digital-storytelling-with-pūrākau-framework.html' OR path LIKE '%05-digital-storytelling-with-pūrākau-framework.html';


-- Update metadata for: Environmental Literacy Framework | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Environmental Literacy Framework | Te Kete Ako')
WHERE path = 'public/units/english/08-environmental-literacy-framework.html' OR path LIKE '%08-environmental-literacy-framework.html';


-- Update metadata for: Lesson 1.5: Reclaiming the Narrative | Walker Unit
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.5: Reclaiming the Narrative | Walker Unit | Te Kete Ako')
WHERE path = 'public/units/english/025-lesson-1-5-reclaiming-the-narrative.html' OR path LIKE '%025-lesson-1-5-reclaiming-the-narrative.html';


-- Update metadata for: Lesson Template: [Te Reo Name] - [English Name] | 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson Template: [Te Reo Name] - [English Name] | Mangakōtukutuku College')
WHERE path = 'public/units/english/04-lesson-template.html' OR path LIKE '%04-lesson-template.html';


-- Update metadata for: Media Literacy Comprehension Handout | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Media Literacy Comprehension Handout | Te Kete Ako')
WHERE path = 'public/units/english/09-media-literacy-comprehension-handout.html' OR path LIKE '%09-media-literacy-comprehension-handout.html';


-- Update metadata for: Letter Writing Template | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Letter Writing Template | Te Kete Ako')
WHERE path = 'public/units/english/024-letter-writing-template.html' OR path LIKE '%024-letter-writing-template.html';


-- Update metadata for: Māori Data Sovereignty | Mangakōtukutuku College
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Māori Data Sovereignty | Mangakōtukutuku College')
WHERE path = 'public/units/english/10-data-sovereignty-maori.html' OR path LIKE '%10-data-sovereignty-maori.html';


-- Update metadata for: Letter Writing Template | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Letter Writing Template | Te Kete Ako')
WHERE path = 'public/units/english/12-letter-writing-template.html' OR path LIKE '%12-letter-writing-template.html';


-- Update metadata for: Family Tree Writing | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Family Tree Writing | Te Kete Ako')
WHERE path = 'public/units/english/11-family-tree-writing.html' OR path LIKE '%11-family-tree-writing.html';


-- Update metadata for: Writers Toolkit Progress Tracker | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Writers Toolkit Progress Tracker | Te Kete Ako')
WHERE path = 'public/units/english/01-writers-toolkit-progress-tracker.html' OR path LIKE '%01-writers-toolkit-progress-tracker.html';


-- Update metadata for: Browse by Concept | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Browse by Concept | Te Kete Ako')
WHERE path = 'public/units/english/015-browse-by-concept.html' OR path LIKE '%015-browse-by-concept.html';


-- Update metadata for: Media Literacy Comprehension Handout | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Media Literacy Comprehension Handout | Te Kete Ako')
WHERE path = 'public/units/english/017-media-literacy-comprehension-handout.html' OR path LIKE '%017-media-literacy-comprehension-handout.html';


-- Update metadata for: The Writer's Toolkit | Critical Literacy Unit
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit | Critical Literacy Unit')
WHERE path = 'public/units/english/020-toolkit.html' OR path LIKE '%020-toolkit.html';


-- Update metadata for: Lesson Template: [Te Reo Name] - [English Name] | 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson Template: [Te Reo Name] - [English Name] | Mangakōtukutuku College')
WHERE path = 'public/units/english/018-lesson-template.html' OR path LIKE '%018-lesson-template.html';


-- Update metadata for: The Writer's Toolkit | Critical Literacy Unit
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit | Critical Literacy Unit')
WHERE path = 'public/units/english/06-toolkit.html' OR path LIKE '%06-toolkit.html';


-- Update metadata for: Writers Toolkit Progress Tracker | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Writers Toolkit Progress Tracker | Te Kete Ako')
WHERE path = 'public/units/english/014-writers-toolkit-progress-tracker.html' OR path LIKE '%014-writers-toolkit-progress-tracker.html';


-- Update metadata for: Māori Data Sovereignty | Mangakōtukutuku College
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Māori Data Sovereignty | Mangakōtukutuku College')
WHERE path = 'public/units/english/023-data-sovereignty-maori.html' OR path LIKE '%023-data-sovereignty-maori.html';


-- Update metadata for: Environmental Literacy Framework | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Environmental Literacy Framework | Te Kete Ako')
WHERE path = 'public/units/english/013-environmental-literacy-framework.html' OR path LIKE '%013-environmental-literacy-framework.html';


-- Update metadata for: Browse by Concept | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Browse by Concept | Te Kete Ako')
WHERE path = 'public/units/english/02-browse-by-concept.html' OR path LIKE '%02-browse-by-concept.html';


-- Update metadata for: 🔍 Kimi Rauemi - Search Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), '🔍 Kimi Rauemi - Search Te Kete Ako')
WHERE path = 'public/units/english/022-search.html' OR path LIKE '%022-search.html';


-- Update metadata for: Y8 Digital Kaitiakitanga (18 Lessons) | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y8 Digital Kaitiakitanga (18 Lessons) | Te Kete Ako')
WHERE path = 'public/units/y8-digital-kaitiakitanga/index-with-variants.html' OR path LIKE '%index-with-variants.html';


-- Update metadata for: Handout: My Digital Whenua Map
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: My Digital Whenua Map')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/my-digital-whenua-map.html' OR path LIKE '%my-digital-whenua-map.html';


-- Update metadata for: Handout: The Digital Tikanga Treaty
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: The Digital Tikanga Treaty')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/digital-tikanga-treaty.html' OR path LIKE '%digital-tikanga-treaty.html';


-- Update metadata for: Handout: Ethical Design Challenge
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Ethical Design Challenge')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/ethical-design-challenge.html' OR path LIKE '%ethical-design-challenge.html';


-- Update metadata for: Handout: My Mauri Audit
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: My Mauri Audit')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/mauri-audit.html' OR path LIKE '%mauri-audit.html';


-- Update metadata for: Handout: Blueprint for My Digital Whare
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Blueprint for My Digital Whare')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/blueprint-for-my-digital-whare.html' OR path LIKE '%blueprint-for-my-digital-whare.html';


-- Update metadata for: Handout: Ripple Effect Analysis
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Ripple Effect Analysis')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/ripple-effect-analysis.html' OR path LIKE '%ripple-effect-analysis.html';


-- Update metadata for: Handout: Password Strength Lab
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Password Strength Lab')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/password-strength-lab.html' OR path LIKE '%password-strength-lab.html';


-- Update metadata for: Handout: Te Whare Tapa Whā - Our Digital Hauora
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Te Whare Tapa Whā - Our Digital Hauora')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/te-whare-tapa-wha-digital-hauora.html' OR path LIKE '%te-whare-tapa-wha-digital-hauora.html';


-- Update metadata for: Handout: My Digital Korowai Design
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: My Digital Korowai Design')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/digital-korowai-design.html' OR path LIKE '%digital-korowai-design.html';


-- Update metadata for: Handout: Online Kōrero Analysis Cards
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Online Kōrero Analysis Cards')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/online-korero-analysis-cards.html' OR path LIKE '%online-korero-analysis-cards.html';


-- Update metadata for: Handout: The Upstander Toolkit
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: The Upstander Toolkit')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/upstander-toolkit.html' OR path LIKE '%upstander-toolkit.html';


-- Update metadata for: Infographic: The Dopamine Loop
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Infographic: The Dopamine Loop')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/dopamine-loop-infographic.html' OR path LIKE '%dopamine-loop-infographic.html';


-- Update metadata for: Handout: Misinformation Analysis
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Misinformation Analysis')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/misinformation-analysis.html' OR path LIKE '%misinformation-analysis.html';


-- Update metadata for: Handout: Body Sensor Map
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Body Sensor Map')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/body-sensor-map.html' OR path LIKE '%body-sensor-map.html';


-- Update metadata for: Handout: My Digital Rangatiratanga Statement
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: My Digital Rangatiratanga Statement')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/digital-rangatiratanga-statement.html' OR path LIKE '%digital-rangatiratanga-statement.html';


-- Update metadata for: Handout: Peer Feedback Form
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Peer Feedback Form')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/peer-feedback-form.html' OR path LIKE '%peer-feedback-form.html';


-- Update metadata for: Handout: Project Planning Template
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Project Planning Template')
WHERE path = 'public/units/y8-digital-kaitiakitanga/handouts/project-planning-template.html' OR path LIKE '%project-planning-template.html';


-- Update metadata for: Summative: Digital Kaitiaki Challenge Brief & Rubr
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Summative: Digital Kaitiaki Challenge Brief & Rubric')
WHERE path = 'public/units/y8-digital-kaitiakitanga/resources/capstone-project-brief-and-rubric.html' OR path LIKE '%capstone-project-brief-and-rubric.html';


-- Update metadata for: 🔍 Digital Whenua Vocabulary
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), '🔍 Digital Whenua Vocabulary')
WHERE path = 'public/units/y8-digital-kaitiakitanga/resources/wordsearch-digital-whenua-nyt.html' OR path LIKE '%wordsearch-digital-whenua-nyt.html';


-- Update metadata for: Lesson 2: The Four Walls of our Digital Whare | Di
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: The Four Walls of our Digital Whare | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-2-four-walls.html' OR path LIKE '%lesson-2-four-walls.html';


-- Update metadata for: Lesson 17: Creation & Collaboration Workshop | Dig
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 17: Creation & Collaboration Workshop | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-17-creation-workshop.html' OR path LIKE '%lesson-17-creation-workshop.html';


-- Update metadata for: Lesson 18: The Whare Warming Showcase | Digital Ka
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 18: The Whare Warming Showcase | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-18-digital-showcase.html' OR path LIKE '%lesson-18-digital-showcase.html';


-- Update metadata for: Lesson 4: The Body as a Sensor | Digital Kaitiakit
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: The Body as a Sensor | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-4-body-as-sensor.html' OR path LIKE '%lesson-4-body-as-sensor.html';


-- Update metadata for: Lesson 16: The Digital Kaitiaki Challenge | Digita
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 16: The Digital Kaitiaki Challenge | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-16-project-launch.html' OR path LIKE '%lesson-16-project-launch.html';


-- Update metadata for: Lesson 6: Designing for Well-being | Digital Kaiti
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6: Designing for Well-being | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-6-designing-for-well-being.html' OR path LIKE '%lesson-6-designing-for-well-being.html';


-- Update metadata for: Lesson 9: The Misinformation Effect | Digital Kait
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 9: The Misinformation Effect | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-9-misinformation-effect.html' OR path LIKE '%lesson-9-misinformation-effect.html';


-- Update metadata for: Lesson 3: Blueprint for a Healthy Whare | Digital 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Blueprint for a Healthy Whare | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-3-blueprint-for-a-healthy-whare.html' OR path LIKE '%lesson-3-blueprint-for-a-healthy-whare.html';


-- Update metadata for: Lesson 7: Words as Taonga | Digital Kaitiakitanga
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 7: Words as Taonga | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-7-words-as-taonga.html' OR path LIKE '%lesson-7-words-as-taonga.html';


-- Update metadata for: Lesson 13: Reclaiming Your Mauri | Digital Kaitiak
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 13: Reclaiming Your Mauri | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-13-reclaiming-your-mauri.html' OR path LIKE '%lesson-13-reclaiming-your-mauri.html';


-- Update metadata for: Lesson 14: The Digital Korowai | Digital Kaitiakit
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 14: The Digital Korowai | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-14-digital-korowai.html' OR path LIKE '%lesson-14-digital-korowai.html';


-- Update metadata for: Lesson 5: The Science of Screen Time | Digital Kai
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5: The Science of Screen Time | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-5-science-of-screen-time.html' OR path LIKE '%lesson-5-science-of-screen-time.html';


-- Update metadata for: Lesson 1: Te Whenua Tāhiko - Our Digital Whenua | 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Te Whenua Tāhiko - Our Digital Whenua | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-1-what-is-our-digital-whenua.html' OR path LIKE '%lesson-1-what-is-our-digital-whenua.html';


-- Update metadata for: Research Skills: Traditional and Digital Sources
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Research Skills: Traditional and Digital Sources')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/research-skills-using-traditional-and-digital-sources.html' OR path LIKE '%research-skills-using-traditional-and-digital-sources.html';


-- Update metadata for: Lesson 10: Your Data is a Taonga | Digital Kaitiak
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 10: Your Data is a Taonga | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-10-data-as-taonga.html' OR path LIKE '%lesson-10-data-as-taonga.html';


-- Update metadata for: Digital Storytelling with Pūrākau Framework
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Storytelling with Pūrākau Framework')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/digital-storytelling-with-pūrākau-framework.html' OR path LIKE '%digital-storytelling-with-pūrākau-framework.html';


-- Update metadata for: Lesson 8: The Art of the Upstander | Digital Kaiti
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 8: The Art of the Upstander | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-8-art-of-the-upstander.html' OR path LIKE '%lesson-8-art-of-the-upstander.html';


-- Update metadata for: Lesson 12: Our Community's Tikanga | Digital Kaiti
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 12: Our Community''s Tikanga | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-12-digital-tikanga.html' OR path LIKE '%lesson-12-digital-tikanga.html';


-- Update metadata for: Lesson 11: The Ripple Effect - Our Digital Whakapa
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 11: The Ripple Effect - Our Digital Whakapapa | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-11-the-ripple-effect.html' OR path LIKE '%lesson-11-the-ripple-effect.html';


-- Update metadata for: Lesson 15: Digital Rangatiratanga | Digital Kaitia
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 15: Digital Rangatiratanga | Digital Kaitiakitanga')
WHERE path = 'public/units/y8-digital-kaitiakitanga/lessons/lesson-15-digital-rangatiratanga.html' OR path LIKE '%lesson-15-digital-rangatiratanga.html';


-- Update metadata for: Lesson 7 Tukutuku Transformations
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 7 Tukutuku Transformations')
WHERE path = 'public/units/y9-maths-geometry-patterns/lessons/lesson-7-tukutuku-transformations.html' OR path LIKE '%lesson-7-tukutuku-transformations.html';


-- Update metadata for: Rohe Research Template (Y8)
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Rohe Research Template (Y8)')
WHERE path = 'public/units/y8-geography-navigation/resources/rohe-research-template.html' OR path LIKE '%rohe-research-template.html';


-- Update metadata for: Lesson 4: Iwi Rohe & Place Names (Y8 Geography)
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: Iwi Rohe & Place Names (Y8 Geography)')
WHERE path = 'public/units/y8-geography-navigation/lessons/lesson-4-iwi-rohe.html' OR path LIKE '%lesson-4-iwi-rohe.html';


-- Update metadata for: Lesson 1: Stars as Compass (Y8 Geography)
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Stars as Compass (Y8 Geography)')
WHERE path = 'public/units/y8-geography-navigation/lessons/lesson-1-star-navigation.html' OR path LIKE '%lesson-1-star-navigation.html';


-- Update metadata for: Week 4: Probability & Real-World Predictions | Y8 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Week 4: Probability & Real-World Predictions | Y8 Statistics')
WHERE path = 'public/units/y8-statistics/lesson-4-probability-real-world-predictions.html' OR path LIKE '%lesson-4-probability-real-world-predictions.html';


-- Update metadata for: Week 2: Analysing NZ Sports Data | Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Week 2: Analysing NZ Sports Data | Y8 Statistics')
WHERE path = 'public/units/y8-statistics/lesson-2-analysing-nz-sports-data.html' OR path LIKE '%lesson-2-analysing-nz-sports-data.html';


-- Update metadata for: Week 3: Census & Population Trends | Y8 Statistics
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Week 3: Census & Population Trends | Y8 Statistics')
WHERE path = 'public/units/y8-statistics/lesson-3-census-population-trends.html' OR path LIKE '%lesson-3-census-population-trends.html';


-- Update metadata for: Week 5: Final Project & Presentation | Y8 Statisti
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Week 5: Final Project & Presentation | Y8 Statistics')
WHERE path = 'public/units/y8-statistics/lesson-5-final-project-presentation.html' OR path LIKE '%lesson-5-final-project-presentation.html';


-- Update metadata for: Week 1: Introduction to Statistical Investigations
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Week 1: Introduction to Statistical Investigations | Y8 Statistics')
WHERE path = 'public/units/y8-statistics/lesson-1-introduction-statistical-investigations.html' OR path LIKE '%lesson-1-introduction-statistical-investigations.html';


-- Update metadata for: Unit 4, Lesson 5: Community Science Projects
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4, Lesson 5: Community Science Projects')
WHERE path = 'public/units/lessons/unit-4-lesson-5.html' OR path LIKE '%unit-4-lesson-5.html';


-- Update metadata for: Unit 3 Lesson 4: Technology & Innovation | Mangakō
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 3 Lesson 4: Technology & Innovation | Mangakōtukutuku College')
WHERE path = 'public/units/lessons/unit-3-lesson-4.html' OR path LIKE '%unit-3-lesson-4.html';


-- Update metadata for: Unit 3 Lesson 5: Community Science Projects | Mang
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 3 Lesson 5: Community Science Projects | Mangakōtukutuku College')
WHERE path = 'public/units/lessons/unit-3-lesson-5.html' OR path LIKE '%unit-3-lesson-5.html';


-- Update metadata for: Unit 4, Lesson 4: Technology & Innovation
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4, Lesson 4: Technology & Innovation')
WHERE path = 'public/units/lessons/unit-4-lesson-4.html' OR path LIKE '%unit-4-lesson-4.html';


-- Update metadata for: Lesson lesson
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson lesson')
WHERE path = 'public/units/lessons/systems-lesson-1-2.html' OR path LIKE '%systems-lesson-1-2.html';


-- Update metadata for: Unit 4, Lesson 3: Mathematics in Cultural Context
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4, Lesson 3: Mathematics in Cultural Context')
WHERE path = 'public/units/lessons/unit-4-lesson-3.html' OR path LIKE '%unit-4-lesson-3.html';


-- Update metadata for: Unit 3 Lesson 2: Environmental Science & Kaitiakit
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 3 Lesson 2: Environmental Science & Kaitiakitanga | Mangakōtukutuku College')
WHERE path = 'public/units/lessons/unit-3-lesson-2.html' OR path LIKE '%unit-3-lesson-2.html';


-- Update metadata for: Unit 7 Lesson 2: AI Bias & Algorithmic Justice | T
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 7 Lesson 2: AI Bias & Algorithmic Justice | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-7-lesson-2.html' OR path LIKE '%unit-7-lesson-2.html';


-- Update metadata for: Unit 6 Lesson 1: Visioning Rangatiratanga 2050 | T
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 6 Lesson 1: Visioning Rangatiratanga 2050 | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-6-lesson-1.html' OR path LIKE '%unit-6-lesson-1.html';


-- Update metadata for: Unit 2 Lesson 1: Pre-Colonial Innovation - Challen
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 1: Pre-Colonial Innovation - Challenging the Myth of "Primitive" Technology | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-2-lesson-1.html' OR path LIKE '%unit-2-lesson-1.html';


-- Update metadata for: Unit 5 Lesson 1: Indigenous Worldviews - Shared Va
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 5 Lesson 1: Indigenous Worldviews - Shared Values, Diverse Expressions | Mangakōtukutuku College')
WHERE path = 'public/units/lessons/unit-5-lesson-1.html' OR path LIKE '%unit-5-lesson-1.html';


-- Update metadata for: Unit 1 Lesson 1: Ko Wai Au? - Personal Whakapapa E
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 1: Ko Wai Au? - Personal Whakapapa Exploration | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-1-lesson-1.html' OR path LIKE '%unit-1-lesson-1.html';


-- Update metadata for: Lesson lesson
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson lesson')
WHERE path = 'public/units/lessons/systems-lesson-2-1.html' OR path LIKE '%systems-lesson-2-1.html';


-- Update metadata for: Unit 7 Lesson 3: AI Ethics in Practice | Te Kete A
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 7 Lesson 3: AI Ethics in Practice | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-7-lesson-3.html' OR path LIKE '%unit-7-lesson-3.html';


-- Update metadata for: Unit 3 Lesson 3: Mathematics in Cultural Context |
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 3 Lesson 3: Mathematics in Cultural Context | Mangakōtukutuku College')
WHERE path = 'public/units/lessons/unit-3-lesson-3.html' OR path LIKE '%unit-3-lesson-3.html';


-- Update metadata for: Unit 4, Lesson 2: Environmental Science & Kaitiaki
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4, Lesson 2: Environmental Science & Kaitiakitanga')
WHERE path = 'public/units/lessons/unit-4-lesson-2.html' OR path LIKE '%unit-4-lesson-2.html';


-- Update metadata for: Unit 4 Lesson 1: Understanding Economic Systems - 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4 Lesson 1: Understanding Economic Systems - Who Wins and Who Loses? | Mangakōtukutuku College')
WHERE path = 'public/units/lessons/unit-4-lesson-1.html' OR path LIKE '%unit-4-lesson-1.html';


-- Update metadata for: Unit 5 Lesson 2: Colonialism as Global System - Pa
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 5 Lesson 2: Colonialism as Global System - Patterns of Extraction and Control | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-5-lesson-2.html' OR path LIKE '%unit-5-lesson-2.html';


-- Update metadata for: Unit 2, Lesson 3: The Fight for Rights
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 3: The Fight for Rights')
WHERE path = 'public/units/lessons/unit-2-lesson-3.html' OR path LIKE '%unit-2-lesson-3.html';


-- Update metadata for: Unit 1 Lesson 2: Mātauranga Māori - Traditional Kn
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 2: Mātauranga Māori - Traditional Knowledge Systems | Mangakōtukutuku College')
WHERE path = 'public/units/lessons/unit-1-lesson-2.html' OR path LIKE '%unit-1-lesson-2.html';


-- Update metadata for: Unit 6 Lesson 3: Digital Sovereignty & Youth Voice
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 6 Lesson 3: Digital Sovereignty & Youth Voice | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-6-lesson-3.html' OR path LIKE '%unit-6-lesson-3.html';


-- Update metadata for: Unit 6 Lesson 2: Innovation through Whakapapa | Te
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 6 Lesson 2: Innovation through Whakapapa | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-6-lesson-2.html' OR path LIKE '%unit-6-lesson-2.html';


-- Update metadata for: Unit 1 Lesson 3: Haka & Cultural Expression - Voic
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 3: Haka & Cultural Expression - Voice, Power & Identity | Mangakōtukutuku College')
WHERE path = 'public/units/lessons/unit-1-lesson-3.html' OR path LIKE '%unit-1-lesson-3.html';


-- Update metadata for: Unit 2, Lesson 2: The Aotearoa Wars
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 2: The Aotearoa Wars')
WHERE path = 'public/units/lessons/unit-2-lesson-2.html' OR path LIKE '%unit-2-lesson-2.html';


-- Update metadata for: Unit 5 Lesson 3: Resistance Networks - Global Indi
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 5 Lesson 3: Resistance Networks - Global Indigenous Movements | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-5-lesson-3.html' OR path LIKE '%unit-5-lesson-3.html';


-- Update metadata for: Lesson lesson
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson lesson')
WHERE path = 'public/units/lessons/systems-lesson-5-1.html' OR path LIKE '%systems-lesson-5-1.html';


-- Update metadata for: Unit 3 Lesson 1: Dual Knowledge Systems Foundation
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 3 Lesson 1: Dual Knowledge Systems Foundation | Mangakōtukutuku College')
WHERE path = 'public/units/lessons/unit-3-lesson-1.html' OR path LIKE '%unit-3-lesson-1.html';


-- Update metadata for: Unit 7 Lesson 1: AI Through Te Ao Māori Lens | Te 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 7 Lesson 1: AI Through Te Ao Māori Lens | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-7-lesson-1.html' OR path LIKE '%unit-7-lesson-1.html';


-- Update metadata for: Lesson lesson
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson lesson')
WHERE path = 'public/units/lessons/systems-lesson-1-1.html' OR path LIKE '%systems-lesson-1-1.html';


-- Update metadata for: Unit 5 Lesson 4: Climate Justice Leadership - Indi
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 5 Lesson 4: Climate Justice Leadership - Indigenous Solutions for Global Challenges | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-5-lesson-4.html' OR path LIKE '%unit-5-lesson-4.html';


-- Update metadata for: Unit 2, Lesson 5: The Path to Redress
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 5: The Path to Redress')
WHERE path = 'public/units/lessons/unit-2-lesson-5.html' OR path LIKE '%unit-2-lesson-5.html';


-- Update metadata for: Unit 1 Lesson 4: Te Tiriti o Waitangi - Partnershi
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 4: Te Tiriti o Waitangi - Partnership & Power-Sharing | Mangakōtukutuku College')
WHERE path = 'public/units/lessons/unit-1-lesson-4.html' OR path LIKE '%unit-1-lesson-4.html';


-- Update metadata for: Unit 6 Lesson 5: Collective Action Project Launch 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 6 Lesson 5: Collective Action Project Launch | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-6-lesson-5.html' OR path LIKE '%unit-6-lesson-5.html';


-- Update metadata for: Unit 6 Lesson 4: Community Leadership in Action | 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 6 Lesson 4: Community Leadership in Action | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-6-lesson-4.html' OR path LIKE '%unit-6-lesson-4.html';


-- Update metadata for: Unit 1 Lesson 5: Traditional Arts & Storytelling -
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 5: Traditional Arts & Storytelling - Preserving Knowledge Through Creativity | Mangakōtukutuku College')
WHERE path = 'public/units/lessons/unit-1-lesson-5.html' OR path LIKE '%unit-1-lesson-5.html';


-- Update metadata for: Unit 2, Lesson 4: 20th Century Activism
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 4: 20th Century Activism')
WHERE path = 'public/units/lessons/unit-2-lesson-4.html' OR path LIKE '%unit-2-lesson-4.html';


-- Update metadata for: Unit 5 Lesson 5 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 5 Lesson 5 | Te Kete Ako')
WHERE path = 'public/units/lessons/unit-5-lesson-5.html' OR path LIKE '%unit-5-lesson-5.html';


-- Update metadata for: Lesson 1: Kōwhaiwhai & Symmetry (Y7 Maths)
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Kōwhaiwhai & Symmetry (Y7 Maths)')
WHERE path = 'public/units/y7-maths-kowhaiwhai/lessons/lesson-1-introduction-kowhaiwhai.html' OR path LIKE '%lesson-1-introduction-kowhaiwhai.html';


-- Update metadata for: Lesson 4.4: Wahine Māori Leadership | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4.4: Wahine Māori Leadership | Te Kete Ako')
WHERE path = 'public/units/hopa-unit/lesson-4-4-wahine-maori-leadership.html' OR path LIKE '%lesson-4-4-wahine-maori-leadership.html';


-- Update metadata for: Lesson 4.2: Urban Māori Migration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4.2: Urban Māori Migration | Te Kete Ako')
WHERE path = 'public/units/hopa-unit/lesson-4-2-urban-maori-migration.html' OR path LIKE '%lesson-4-2-urban-maori-migration.html';


-- Update metadata for: Lesson 4.3: Research WITH Communities | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4.3: Research WITH Communities | Te Kete Ako')
WHERE path = 'public/units/hopa-unit/lesson-4-3-research-with-communities.html' OR path LIKE '%lesson-4-3-research-with-communities.html';


-- Update metadata for: Lesson 4.1: Who Was Ngāpare Hopa? | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4.1: Who Was Ngāpare Hopa? | Te Kete Ako')
WHERE path = 'public/units/hopa-unit/lesson-4-1-who-was-ngapare-hopa.html' OR path LIKE '%lesson-4-1-who-was-ngapare-hopa.html';


-- Update metadata for: Lesson 4.5: Urban Māori Today | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4.5: Urban Māori Today | Te Kete Ako')
WHERE path = 'public/units/hopa-unit/lesson-4-5-urban-maori-today.html' OR path LIKE '%lesson-4-5-urban-maori-today.html';


-- Update metadata for: Y9 Statistics L3: NZ Census Data Exploration | Te 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y9 Statistics L3: NZ Census Data Exploration | Te Kete Ako')
WHERE path = 'public/units/y9-statistics-chain/lesson-3-nz-census-data.html' OR path LIKE '%lesson-3-nz-census-data.html';


-- Update metadata for: Y9 Statistics L1: Introduction to Statistical Thin
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y9 Statistics L1: Introduction to Statistical Thinking | Te Kete Ako')
WHERE path = 'public/units/y9-statistics-chain/lesson-1-introduction-statistical-thinking.html' OR path LIKE '%lesson-1-introduction-statistical-thinking.html';


-- Update metadata for: Y9 Statistics L2: The PPDAC Cycle | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y9 Statistics L2: The PPDAC Cycle | Te Kete Ako')
WHERE path = 'public/units/y9-statistics-chain/lesson-2-ppdac-cycle.html' OR path LIKE '%lesson-2-ppdac-cycle.html';


-- Update metadata for: Y9 Statistics L5: Your Statistical Investigation |
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y9 Statistics L5: Your Statistical Investigation | Te Kete Ako')
WHERE path = 'public/units/y9-statistics-chain/lesson-5-statistical-investigation.html' OR path LIKE '%lesson-5-statistical-investigation.html';


-- Update metadata for: Y9 Statistics L4: Creating Charts with Chart.js | 
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y9 Statistics L4: Creating Charts with Chart.js | Te Kete Ako')
WHERE path = 'public/units/y9-statistics-chain/lesson-4-charts-and-graphs.html' OR path LIKE '%lesson-4-charts-and-graphs.html';


-- Update metadata for: Field Study Data Collection Sheet
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Field Study Data Collection Sheet')
WHERE path = 'public/units/y9-science-ecology/resources/field-data-sheet.html' OR path LIKE '%field-data-sheet.html';


-- Update metadata for: 🔍 Ecosystem Vocabulary
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), '🔍 Ecosystem Vocabulary')
WHERE path = 'public/units/y9-science-ecology/resources/wordsearch-ecosystem-nyt.html' OR path LIKE '%wordsearch-ecosystem-nyt.html';


-- Update metadata for: Kaitiakitanga Commitment Template (Y9 Ecology)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Kaitiakitanga Commitment Template (Y9 Ecology)')
WHERE path = 'public/units/y9-science-ecology/resources/kaitiakitanga-commitment-template.html' OR path LIKE '%kaitiakitanga-commitment-template.html';


-- Update metadata for: Native Species Report Rubric (Y9 Ecology)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Native Species Report Rubric (Y9 Ecology)')
WHERE path = 'public/units/y9-science-ecology/resources/assessment-rubric-species-report.html' OR path LIKE '%assessment-rubric-species-report.html';


-- Update metadata for: Handout: Ecosystem Audit
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Handout: Ecosystem Audit')
WHERE path = 'public/units/y9-science-ecology/resources/handout-1-ecosystem-audit.html' OR path LIKE '%handout-1-ecosystem-audit.html';


-- Update metadata for: Ecosystem Field Report Template (Y9 Ecology)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Ecosystem Field Report Template (Y9 Ecology)')
WHERE path = 'public/units/y9-science-ecology/resources/field-report-template.html' OR path LIKE '%field-report-template.html';


-- Update metadata for: Handout: Endemic Species Detective
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Handout: Endemic Species Detective')
WHERE path = 'public/units/y9-science-ecology/resources/handout-2-endemic-species-detective.html' OR path LIKE '%handout-2-endemic-species-detective.html';


-- Update metadata for: Biodiversity Tagger Game (Y9 Ecology)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Biodiversity Tagger Game (Y9 Ecology)')
WHERE path = 'public/units/y9-science-ecology/resources/biodiversity-tagger-game.html' OR path LIKE '%biodiversity-tagger-game.html';


-- Update metadata for: Predator Free NZ Simulation (Y9 Ecology)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Predator Free NZ Simulation (Y9 Ecology)')
WHERE path = 'public/units/y9-science-ecology/resources/predator-free-simulation.html' OR path LIKE '%predator-free-simulation.html';


-- Update metadata for: Possum Impact Investigation Lab (Y9 Ecology)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Possum Impact Investigation Lab (Y9 Ecology)')
WHERE path = 'public/units/y9-science-ecology/resources/possum-impact-lab-sheet.html' OR path LIKE '%possum-impact-lab-sheet.html';


-- Update metadata for: Y9 Ecology Unit Final Assessment Rubric
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Y9 Ecology Unit Final Assessment Rubric')
WHERE path = 'public/units/y9-science-ecology/resources/final-assessment-rubric.html' OR path LIKE '%final-assessment-rubric.html';


-- Update metadata for: Field Report Assessment Rubric (Y9 Ecology)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Field Report Assessment Rubric (Y9 Ecology)')
WHERE path = 'public/units/y9-science-ecology/resources/assessment-rubric-field-report.html' OR path LIKE '%assessment-rubric-field-report.html';


-- Update metadata for: Restoration Proposal Rubric (Y9 Ecology)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Restoration Proposal Rubric (Y9 Ecology)')
WHERE path = 'public/units/y9-science-ecology/resources/restoration-proposal-rubric.html' OR path LIKE '%restoration-proposal-rubric.html';


-- Update metadata for: Ecosystem Restoration Proposal Template (Y9)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Ecosystem Restoration Proposal Template (Y9)')
WHERE path = 'public/units/y9-science-ecology/resources/restoration-proposal-template.html' OR path LIKE '%restoration-proposal-template.html';


-- Update metadata for: Ecology Debate Preparation Guide (Y9)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Ecology Debate Preparation Guide (Y9)')
WHERE path = 'public/units/y9-science-ecology/resources/debate-preparation-guide.html' OR path LIKE '%debate-preparation-guide.html';


-- Update metadata for: EcoRestore Simulation | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'EcoRestore Simulation | Te Kete Ako')
WHERE path = 'public/units/y9-science-ecology/resources/ecorestore-game.html' OR path LIKE '%ecorestore-game.html';


-- Update metadata for: Conservation Letter Writing Template (Y9 Ecology)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Conservation Letter Writing Template (Y9 Ecology)')
WHERE path = 'public/units/y9-science-ecology/resources/letter-writing-template.html' OR path LIKE '%letter-writing-template.html';


-- Update metadata for: Assessment Rubric Persuasive Letter | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'unit-plan',
    title = COALESCE(NULLIF(title, ''), 'Assessment Rubric Persuasive Letter | Te Kete Ako')
WHERE path = 'public/units/y9-science-ecology/resources/assessment-rubric-persuasive-letter.html' OR path LIKE '%assessment-rubric-persuasive-letter.html';


-- Update metadata for: Lesson 2: Biodiversity & Endemism in Aotearoa
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: Biodiversity & Endemism in Aotearoa')
WHERE path = 'public/units/y9-science-ecology/lessons/lesson-2-biodiversity-endemism.html' OR path LIKE '%lesson-2-biodiversity-endemism.html';


-- Update metadata for: Lesson 4: Human Impact & Conservation
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: Human Impact & Conservation')
WHERE path = 'public/units/y9-science-ecology/lessons/lesson-4-human-impact-conservation.html' OR path LIKE '%lesson-4-human-impact-conservation.html';


-- Update metadata for: Lesson 3: Field Study - Rangahau Taiao
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Field Study - Rangahau Taiao')
WHERE path = 'public/units/y9-science-ecology/lessons/lesson-3-field-study-rangahau-taiao.html' OR path LIKE '%lesson-3-field-study-rangahau-taiao.html';


-- Update metadata for: Lesson 6: Guardians of the Future
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6: Guardians of the Future')
WHERE path = 'public/units/y9-science-ecology/lessons/lesson-6-guardians-future.html' OR path LIKE '%lesson-6-guardians-future.html';


-- Update metadata for: Lesson 5: Restoration & Kaitiakitanga
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5: Restoration & Kaitiakitanga')
WHERE path = 'public/units/y9-science-ecology/lessons/lesson-5-restoration-kaitiakitanga.html' OR path LIKE '%lesson-5-restoration-kaitiakitanga.html';


-- Update metadata for: Lesson 1
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1')
WHERE path = 'public/units/y9-science-ecology/lessons/lesson-1-what-is-an-ecosystem.html' OR path LIKE '%lesson-1-what-is-an-ecosystem.html';


-- Update metadata for: Project Brief | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Project Brief | Te Kete Ako')
WHERE path = 'public/project/project-brief.html' OR path LIKE '%project-brief.html';


-- Update metadata for: My Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Dashboard | Te Kete Ako')
WHERE path = 'public/students/dashboard.html' OR path LIKE '%dashboard.html';


-- Update metadata for: Featured Carousel
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Featured Carousel')
WHERE path = 'public/components/featured-carousel.html' OR path LIKE '%featured-carousel.html';


-- Update metadata for: Feedback Widget
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Feedback Widget')
WHERE path = 'public/components/feedback-widget.html' OR path LIKE '%feedback-widget.html';


-- Update metadata for: Graphrag Science Recommendations
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Science Recommendations')
WHERE path = 'public/components/graphrag-science-recommendations.html' OR path LIKE '%graphrag-science-recommendations.html';


-- Update metadata for: Sidebar Intelligent
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Sidebar Intelligent')
WHERE path = 'public/components/sidebar-intelligent.html' OR path LIKE '%sidebar-intelligent.html';


-- Update metadata for: Navigation Unified
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Navigation Unified')
WHERE path = 'public/components/navigation-unified.html' OR path LIKE '%navigation-unified.html';


-- Update metadata for: Learning Pathway Navigator
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Learning Pathway Navigator')
WHERE path = 'public/components/learning-pathway-navigator.html' OR path LIKE '%learning-pathway-navigator.html';


-- Update metadata for: Progress Indicator
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Progress Indicator')
WHERE path = 'public/components/progress-indicator.html' OR path LIKE '%progress-indicator.html';


-- Update metadata for: Graphrag English Recommendations
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag English Recommendations')
WHERE path = 'public/components/graphrag-english-recommendations.html' OR path LIKE '%graphrag-english-recommendations.html';


-- Update metadata for: Download Pdf Button
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Download Pdf Button')
WHERE path = 'public/components/download-pdf-button.html' OR path LIKE '%download-pdf-button.html';


-- Update metadata for: Assign Resource Button
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Assign Resource Button')
WHERE path = 'public/components/assign-resource-button.html' OR path LIKE '%assign-resource-button.html';


-- Update metadata for: Ai Assistant Fab
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Ai Assistant Fab')
WHERE path = 'public/components/ai-assistant-fab.html' OR path LIKE '%ai-assistant-fab.html';


-- Update metadata for: Graphrag Dynamic Resource Browser
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Dynamic Resource Browser')
WHERE path = 'public/components/graphrag-dynamic-resource-browser.html' OR path LIKE '%graphrag-dynamic-resource-browser.html';


-- Update metadata for: Graphrag English Cross Curricular
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag English Cross Curricular')
WHERE path = 'public/components/graphrag-english-cross-curricular.html' OR path LIKE '%graphrag-english-cross-curricular.html';


-- Update metadata for: Beta Badge
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Beta Badge')
WHERE path = 'public/components/beta-badge.html' OR path LIKE '%beta-badge.html';


-- Update metadata for: Top Cultural Widget
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Top Cultural Widget')
WHERE path = 'public/components/top-cultural-widget.html' OR path LIKE '%top-cultural-widget.html';


-- Update metadata for: Graphrag Most Connected
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Most Connected')
WHERE path = 'public/components/graphrag-most-connected.html' OR path LIKE '%graphrag-most-connected.html';


-- Update metadata for: Related Resources Widget
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Related Resources Widget')
WHERE path = 'public/components/related-resources-widget.html' OR path LIKE '%related-resources-widget.html';


-- Update metadata for: Graphrag Similar Resources
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Similar Resources')
WHERE path = 'public/components/graphrag-similar-resources.html' OR path LIKE '%graphrag-similar-resources.html';


-- Update metadata for: Next Lesson Widget
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Next Lesson Widget')
WHERE path = 'public/components/next-lesson-widget.html' OR path LIKE '%next-lesson-widget.html';


-- Update metadata for: Interactive Assessment
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Interactive Assessment')
WHERE path = 'public/components/interactive-assessment.html' OR path LIKE '%interactive-assessment.html';


-- Update metadata for: NYT-Quality Wordsearch | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'NYT-Quality Wordsearch | Te Kete Ako')
WHERE path = 'public/components/wordsearch-game.html' OR path LIKE '%wordsearch-game.html';


-- Update metadata for: Graphrag Semantic Search
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Semantic Search')
WHERE path = 'public/components/graphrag-semantic-search.html' OR path LIKE '%graphrag-semantic-search.html';


-- Update metadata for: Search Unified
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Search Unified')
WHERE path = 'public/components/search-unified.html' OR path LIKE '%search-unified.html';


-- Update metadata for: Role Based Nav
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Role Based Nav')
WHERE path = 'public/components/role-based-nav.html' OR path LIKE '%role-based-nav.html';


-- Update metadata for: {Lesson lesson}
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '{Lesson lesson}')
WHERE path = 'public/components/professional-lesson-template.html' OR path LIKE '%professional-lesson-template.html';


-- Update metadata for: Navigation Mega Menu
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Navigation Mega Menu')
WHERE path = 'public/components/navigation-mega-menu.html' OR path LIKE '%navigation-mega-menu.html';


-- Update metadata for: Recommendations Unified
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Recommendations Unified')
WHERE path = 'public/components/recommendations-unified.html' OR path LIKE '%recommendations-unified.html';


-- Update metadata for: Te Kete Ako       Educational Treasures
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako       Educational Treasures')
WHERE path = 'public/components/hero-enhanced.html' OR path LIKE '%hero-enhanced.html';


-- Update metadata for: Graphrag Recommendations
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Recommendations')
WHERE path = 'public/components/graphrag-recommendations.html' OR path LIKE '%graphrag-recommendations.html';


-- Update metadata for: Te Kete Ako
                
Educational Treasures
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako
                
Educational Treasures')
WHERE path = 'public/components/hero-unified.html' OR path LIKE '%hero-unified.html';


-- Update metadata for: Graphrag English Hidden Gems
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag English Hidden Gems')
WHERE path = 'public/components/graphrag-english-hidden-gems.html' OR path LIKE '%graphrag-english-hidden-gems.html';


-- Update metadata for: Graphrag Knowledge Graph
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Knowledge Graph')
WHERE path = 'public/components/graphrag-knowledge-graph.html' OR path LIKE '%graphrag-knowledge-graph.html';


-- Update metadata for: Graphrag Social Studies Recommendations
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Social Studies Recommendations')
WHERE path = 'public/components/graphrag-social-studies-recommendations.html' OR path LIKE '%graphrag-social-studies-recommendations.html';


-- Update metadata for: Graphrag Mathematics Hidden Gems
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Mathematics Hidden Gems')
WHERE path = 'public/components/graphrag-mathematics-hidden-gems.html' OR path LIKE '%graphrag-mathematics-hidden-gems.html';


-- Update metadata for: Quality Excellence Badge
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Quality Excellence Badge')
WHERE path = 'public/components/quality-excellence-badge.html' OR path LIKE '%quality-excellence-badge.html';


-- Update metadata for: Navigation Hegelian Synthesis
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Navigation Hegelian Synthesis')
WHERE path = 'public/components/navigation-hegelian-synthesis.html' OR path LIKE '%navigation-hegelian-synthesis.html';


-- Update metadata for: Cultural Tooltip
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Tooltip')
WHERE path = 'public/components/cultural-tooltip.html' OR path LIKE '%cultural-tooltip.html';


-- Update metadata for: Cross Subject Pathways
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cross Subject Pathways')
WHERE path = 'public/components/cross-subject-pathways.html' OR path LIKE '%cross-subject-pathways.html';


-- Update metadata for: Search Bar Global
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Search Bar Global')
WHERE path = 'public/components/search-bar-global.html' OR path LIKE '%search-bar-global.html';


-- Update metadata for: Homepage Cultural Excellence
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Homepage Cultural Excellence')
WHERE path = 'public/components/homepage-cultural-excellence.html' OR path LIKE '%homepage-cultural-excellence.html';


-- Update metadata for: Prerequisite Pathway Explorer
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Prerequisite Pathway Explorer')
WHERE path = 'public/components/prerequisite-pathway-explorer.html' OR path LIKE '%prerequisite-pathway-explorer.html';


-- Update metadata for: Graphrag Orphaned Excellence
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Orphaned Excellence')
WHERE path = 'public/components/graphrag-orphaned-excellence.html' OR path LIKE '%graphrag-orphaned-excellence.html';


-- Update metadata for: Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako')
WHERE path = 'public/components/phenomenal-hero.html' OR path LIKE '%phenomenal-hero.html';


-- Update metadata for: Badge System
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Badge System')
WHERE path = 'public/components/badge-system.html' OR path LIKE '%badge-system.html';


-- Update metadata for: Onboarding Tour
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Onboarding Tour')
WHERE path = 'public/components/onboarding-tour.html' OR path LIKE '%onboarding-tour.html';


-- Update metadata for: Search Bar
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Search Bar')
WHERE path = 'public/components/search-bar.html' OR path LIKE '%search-bar.html';


-- Update metadata for: Related Resources
UPDATE resources 
SET 
    subject = 'Cross-Curricular',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Related Resources')
WHERE path = 'public/components/related-resources.html' OR path LIKE '%related-resources.html';


-- Update metadata for: Stats Dashboard
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Stats Dashboard')
WHERE path = 'public/components/stats-dashboard.html' OR path LIKE '%stats-dashboard.html';


-- Update metadata for: Graphrag Science Math Connections
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Science Math Connections')
WHERE path = 'public/components/graphrag-science-math-connections.html' OR path LIKE '%graphrag-science-math-connections.html';


-- Update metadata for: Perfect Pathways Widget
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Perfect Pathways Widget')
WHERE path = 'public/components/perfect-pathways-widget.html' OR path LIKE '%perfect-pathways-widget.html';


-- Update metadata for: Relationship Graph Viewer
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Relationship Graph Viewer')
WHERE path = 'public/components/relationship-graph-viewer.html' OR path LIKE '%relationship-graph-viewer.html';


-- Update metadata for: Games Showcase
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Games Showcase')
WHERE path = 'public/components/games-showcase.html' OR path LIKE '%games-showcase.html';


-- Update metadata for: Quick Actions Fab
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Quick Actions Fab')
WHERE path = 'public/components/quick-actions-fab.html' OR path LIKE '%quick-actions-fab.html';


-- Update metadata for: Navigation Year Dropdown
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Navigation Year Dropdown')
WHERE path = 'public/components/navigation-year-dropdown.html' OR path LIKE '%navigation-year-dropdown.html';


-- Update metadata for: Lesson Actions
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Actions')
WHERE path = 'public/components/lesson-actions.html' OR path LIKE '%lesson-actions.html';


-- Update metadata for: Footer
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Footer')
WHERE path = 'public/components/footer.html' OR path LIKE '%footer.html';


-- Update metadata for: Graphrag Live Recommendations
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Live Recommendations')
WHERE path = 'public/components/graphrag-live-recommendations.html' OR path LIKE '%graphrag-live-recommendations.html';


-- Update metadata for: Graphrag Cross Subject Network
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Cross Subject Network')
WHERE path = 'public/components/graphrag-cross-subject-network.html' OR path LIKE '%graphrag-cross-subject-network.html';


-- Update metadata for: Mobile Bottom Nav
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Mobile Bottom Nav')
WHERE path = 'public/components/mobile-bottom-nav.html' OR path LIKE '%mobile-bottom-nav.html';


-- Update metadata for: Trust Indicators
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Trust Indicators')
WHERE path = 'public/components/trust-indicators.html' OR path LIKE '%trust-indicators.html';


-- Update metadata for: Homepage Top Cultural
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Homepage Top Cultural')
WHERE path = 'public/components/homepage-top-cultural.html' OR path LIKE '%homepage-top-cultural.html';


-- Update metadata for: Navigation Standard
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Navigation Standard')
WHERE path = 'public/components/navigation-standard.html' OR path LIKE '%navigation-standard.html';


-- Update metadata for: See Also Cross Curricular
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'See Also Cross Curricular')
WHERE path = 'public/components/see-also-cross-curricular.html' OR path LIKE '%see-also-cross-curricular.html';


-- Update metadata for: Prerequisite Chain Explorer
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Prerequisite Chain Explorer')
WHERE path = 'public/components/prerequisite-chain-explorer.html' OR path LIKE '%prerequisite-chain-explorer.html';


-- Update metadata for: Breadcrumb Nav Enhanced
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Breadcrumb Nav Enhanced')
WHERE path = 'public/components/breadcrumb-nav-enhanced.html' OR path LIKE '%breadcrumb-nav-enhanced.html';


-- Update metadata for: Teaching Variants Card
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teaching Variants Card')
WHERE path = 'public/components/teaching-variants-card.html' OR path LIKE '%teaching-variants-card.html';


-- Update metadata for: Homepage Perfect Pathways
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Homepage Perfect Pathways')
WHERE path = 'public/components/homepage-perfect-pathways.html' OR path LIKE '%homepage-perfect-pathways.html';


-- Update metadata for: Mega Navigation Intelligent
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Mega Navigation Intelligent')
WHERE path = 'public/components/mega-navigation-intelligent.html' OR path LIKE '%mega-navigation-intelligent.html';


-- Update metadata for: Professional Navigation
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Professional Navigation')
WHERE path = 'public/components/professional-navigation.html' OR path LIKE '%professional-navigation.html';


-- Update metadata for: Homepage Personalized Recommendations
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Homepage Personalized Recommendations')
WHERE path = 'public/components/homepage-personalized-recommendations.html' OR path LIKE '%homepage-personalized-recommendations.html';


-- Update metadata for: Navigation Ai
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Navigation Ai')
WHERE path = 'public/components/navigation-ai.html' OR path LIKE '%navigation-ai.html';


-- Update metadata for: Graphrag Mathematics Recommendations
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Graphrag Mathematics Recommendations')
WHERE path = 'public/components/graphrag-mathematics-recommendations.html' OR path LIKE '%graphrag-mathematics-recommendations.html';


-- Update metadata for: Header Next Level
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Header Next Level')
WHERE path = 'public/components/header-next-level.html' OR path LIKE '%header-next-level.html';


-- Update metadata for: Dynamic Subject Loader
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Dynamic Subject Loader')
WHERE path = 'public/components/dynamic-subject-loader.html' OR path LIKE '%dynamic-subject-loader.html';


-- Update metadata for: Cultural Assessment Framework | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Cultural Assessment Framework | Te Kete Ako')
WHERE path = 'public/experiences/cultural-assessment.html' OR path LIKE '%cultural-assessment.html';


-- Update metadata for: Living Whakapapa | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Living Whakapapa | Te Kete Ako')
WHERE path = 'public/experiences/living-whakapapa.html' OR path LIKE '%living-whakapapa.html';


-- Update metadata for: Handouts | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handouts | Te Kete Ako')
WHERE path = 'public/experiences/handouts.html' OR path LIKE '%handouts.html';


-- Update metadata for: Login | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Login | Te Kete Ako')
WHERE path = 'public/experiences/login.html' OR path LIKE '%login.html';


-- Update metadata for: Register | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Register | Te Kete Ako')
WHERE path = 'public/experiences/register-simple.html' OR path LIKE '%register-simple.html';


-- Update metadata for: Digital Pūrākau | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Pūrākau | Te Kete Ako')
WHERE path = 'public/experiences/digital-purakau.html' OR path LIKE '%digital-purakau.html';


-- Update metadata for: Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/experiences/curriculum-alignment.html' OR path LIKE '%curriculum-alignment.html';


-- Update metadata for: Adaptive Learning Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Adaptive Learning Pathways | Te Kete Ako')
WHERE path = 'public/experiences/adaptive-pathways.html' OR path LIKE '%adaptive-pathways.html';


-- Update metadata for: Games | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Games | Te Kete Ako')
WHERE path = 'public/experiences/games.html' OR path LIKE '%games.html';


-- Update metadata for: My Kete | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Kete | Te Kete Ako')
WHERE path = 'public/experiences/my-kete.html' OR path LIKE '%my-kete.html';


-- Update metadata for: Virtual Marae Training Protocol | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Virtual Marae Training Protocol | Te Kete Ako')
WHERE path = 'public/experiences/virtual-marae.html' OR path LIKE '%virtual-marae.html';


-- Update metadata for: Lessons | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lessons | Te Kete Ako')
WHERE path = 'public/experiences/lessons.html' OR path LIKE '%lessons.html';


-- Update metadata for: NCEA Level 1 Literacy & Numeracy Must-Knows - Te K
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 11',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'NCEA Level 1 Literacy & Numeracy Must-Knows - Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 11/ncea-level-1-literacy-and-numeracy-must-knows.html' OR path LIKE '%ncea-level-1-literacy-and-numeracy-must-knows.html';


-- Update metadata for: Simple Login | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 2',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Simple Login | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 2/login-simple.html' OR path LIKE '%login-simple.html';


-- Update metadata for: Video Activity: The Legends of Māui | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 2',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Video Activity: The Legends of Māui | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 2/maui-video-activity.html' OR path LIKE '%maui-video-activity.html';


-- Update metadata for: Te Kete Ako - Auth Test (8PM Ready)
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 2',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Auth Test (8PM Ready)')
WHERE path = 'public/integrated-handouts/Year 2/auth-test.html' OR path LIKE '%auth-test.html';


-- Update metadata for: Elements of Art Handout
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 5',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Elements of Art Handout')
WHERE path = 'public/integrated-handouts/Year 5/elements-of-art-handout.html' OR path LIKE '%elements-of-art-handout.html';


-- Update metadata for: Shakespearean Soliloquy Reading Comprehension
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Shakespearean Soliloquy Reading Comprehension')
WHERE path = 'public/integrated-handouts/Year 10/shakespeare-soliloquy-handout.html' OR path LIKE '%shakespeare-soliloquy-handout.html';


-- Update metadata for: Year 10 Mathematics - Cultural Geometry Unit | Kai
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Year 10 Mathematics - Cultural Geometry Unit | Kaitiaki Aronui Generated')
WHERE path = 'public/integrated-handouts/Year 10/kaitiaki-generated-y10-math-cultural-geometry.html' OR path LIKE '%kaitiaki-generated-y10-math-cultural-geometry.html';


-- Update metadata for: Walker Unit - Teacher's Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Walker Unit - Teacher''s Guide | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 10/walker-unit-overview-teacher-guide.html' OR path LIKE '%walker-unit-overview-teacher-guide.html';


-- Update metadata for: Handout: NZ Housing Crisis
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: NZ Housing Crisis')
WHERE path = 'public/integrated-handouts/Year 10/nz-housing-crisis-handout.html' OR path LIKE '%nz-housing-crisis-handout.html';


-- Update metadata for: Discover Orphans
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Discover Orphans')
WHERE path = 'public/integrated-handouts/Year 10/orphans.html' OR path LIKE '%orphans.html';


-- Update metadata for: Plate Tectonics Reading Comprehension
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Plate Tectonics Reading Comprehension')
WHERE path = 'public/integrated-handouts/Year 10/plate-tectonics-comprehension-handout.html' OR path LIKE '%plate-tectonics-comprehension-handout.html';


-- Update metadata for: Te Kete Ako - Comprehensive Site Map
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Comprehensive Site Map')
WHERE path = 'public/integrated-handouts/Year 10/sitemap-enhanced.html' OR path LIKE '%sitemap-enhanced.html';


-- Update metadata for: Youth Vaping Reading Comprehension | Mangakōtukutu
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Youth Vaping Reading Comprehension | Mangakōtukutuku College')
WHERE path = 'public/integrated-handouts/Year 10/youth-vaping-comprehension-handout.html' OR path LIKE '%youth-vaping-comprehension-handout.html';


-- Update metadata for: Leadership Development Through Cultural Values
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 5',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Leadership Development Through Cultural Values')
WHERE path = 'public/integrated-handouts/Level 5/leadership-development-through-cultural-values.html' OR path LIKE '%leadership-development-through-cultural-values.html';


-- Update metadata for: Social Media and Cultural Identity
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 5',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Social Media and Cultural Identity')
WHERE path = 'public/integrated-handouts/Level 5/social-media-and-cultural-identity.html' OR path LIKE '%social-media-and-cultural-identity.html';


-- Update metadata for: Mathematical Modeling of Ecological Systems
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 2',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Mathematical Modeling of Ecological Systems')
WHERE path = 'public/integrated-handouts/Level 2/mathematical-modeling-of-ecological-systems.html' OR path LIKE '%mathematical-modeling-of-ecological-systems.html';


-- Update metadata for: Algebraic Thinking in Traditional Māori Games
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 4',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Algebraic Thinking in Traditional Māori Games')
WHERE path = 'public/integrated-handouts/Level 4/algebraic-thinking-in-traditional-māori-games.html' OR path LIKE '%algebraic-thinking-in-traditional-māori-games.html';


-- Update metadata for: Geometric Patterns in Māori Art and Architecture
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 4',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Geometric Patterns in Māori Art and Architecture')
WHERE path = 'public/integrated-handouts/Level 4/geometric-patterns-in-māori-art-and-architecture.html' OR path LIKE '%geometric-patterns-in-māori-art-and-architecture.html';


-- Update metadata for: NZ Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 4',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Level 4/curriculum-alignment.html' OR path LIKE '%curriculum-alignment.html';


-- Update metadata for: Probability and Chance in Māori Games
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 4',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Probability and Chance in Māori Games')
WHERE path = 'public/integrated-handouts/Level 4/probability-and-chance-in-māori-games.html' OR path LIKE '%probability-and-chance-in-māori-games.html';


-- Update metadata for: Author's Purpose: Persuade | Mangakōtukutuku Colle
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 4',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Author''s Purpose: Persuade | Mangakōtukutuku College')
WHERE path = 'public/integrated-handouts/Level 4/authors-purpose-persuade-handout.html' OR path LIKE '%authors-purpose-persuade-handout.html';


-- Update metadata for: Statistical Investigation Guide | Mangakōtukutuku 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 4',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Statistical Investigation Guide | Mangakōtukutuku College')
WHERE path = 'public/integrated-handouts/Level 4/statistical-investigation-handout.html' OR path LIKE '%statistical-investigation-handout.html';


-- Update metadata for: Handout: Password Strength Lab
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Password Strength Lab')
WHERE path = 'public/integrated-handouts/Year 123/password-strength-lab.html' OR path LIKE '%password-strength-lab.html';


-- Update metadata for: AI Teacher Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'AI Teacher Dashboard | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 7/teacher-dashboard-ai.html' OR path LIKE '%teacher-dashboard-ai.html';


-- Update metadata for: Handout: The Power of Yet
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: The Power of Yet')
WHERE path = 'public/integrated-handouts/Year 7/ted-power-yet-handout.html' OR path LIKE '%ted-power-yet-handout.html';


-- Update metadata for: Other Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Other Resources | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 7/other-resources.html' OR path LIKE '%other-resources.html';


-- Update metadata for: Handout: The Art of Haka
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: The Art of Haka')
WHERE path = 'public/integrated-handouts/Year 7/art-of-haka-handout.html' OR path LIKE '%art-of-haka-handout.html';


-- Update metadata for: Prompt Engineering 101 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Prompt Engineering 101 | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 7/prompt-engineering-101.html' OR path LIKE '%prompt-engineering-101.html';


-- Update metadata for: YouTube Educational Library | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'YouTube Educational Library | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 7/youtube-library.html' OR path LIKE '%youtube-library.html';


-- Update metadata for: Register | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Register | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 7/register.html' OR path LIKE '%register.html';


-- Update metadata for: Handouts | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handouts | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 7/handouts.html' OR path LIKE '%handouts.html';


-- Update metadata for: Handout: The Treaty of Waitangi
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: The Treaty of Waitangi')
WHERE path = 'public/integrated-handouts/Year 7/treaty-of-waitangi-handout.html' OR path LIKE '%treaty-of-waitangi-handout.html';


-- Update metadata for: YouTube Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'YouTube Resources | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 7/youtube.html' OR path LIKE '%youtube.html';


-- Update metadata for: Social Sciences Progression Framework - Years 7-13
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Social Sciences Progression Framework - Years 7-13 | Mangakōtukutuku College')
WHERE path = 'public/integrated-handouts/Year 7/social-sciences-progression-framework.html' OR path LIKE '%social-sciences-progression-framework.html';


-- Update metadata for: Ecosystem Survey Checklist (Y7)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Ecosystem Survey Checklist (Y7)')
WHERE path = 'public/integrated-handouts/Year 7/ecosystem-survey-checklist.html' OR path LIKE '%ecosystem-survey-checklist.html';


-- Update metadata for: Kaitiakitanga Field Journal (Y7)
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Kaitiakitanga Field Journal (Y7)')
WHERE path = 'public/integrated-handouts/Year 7/kaitiakitanga-field-journal.html' OR path LIKE '%kaitiakitanga-field-journal.html';


-- Update metadata for: Handout: Project Planning Template
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Project Planning Template')
WHERE path = 'public/integrated-handouts/Year 7/project-planning-template.html' OR path LIKE '%project-planning-template.html';


-- Update metadata for: Algebraic Thinking in Traditional Māori Games | Te
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Algebraic Thinking in Traditional Māori Games | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/algebraic-thinking-in-traditional-māori-games.html' OR path LIKE '%algebraic-thinking-in-traditional-māori-games.html';


-- Update metadata for: Handout: Climate Change in Aotearoa
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Climate Change in Aotearoa')
WHERE path = 'public/integrated-handouts/Year 9/climate-emergency-aotearoa-handout.html' OR path LIKE '%climate-emergency-aotearoa-handout.html';


-- Update metadata for: Hērangi Migration Stories | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Hērangi Migration Stories | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/herangi-migration-stories.html' OR path LIKE '%herangi-migration-stories.html';


-- Update metadata for: Tukutuku Pattern Generator | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Pattern Generator | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/tukutuku-pattern-generator.html' OR path LIKE '%tukutuku-pattern-generator.html';


-- Update metadata for: Year 9 Starter Pack: Essential Skills for High Sch
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Year 9 Starter Pack: Essential Skills for High School Success - Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/year-9-starter-pack-essential-skills.html' OR path LIKE '%year-9-starter-pack-essential-skills.html';


-- Update metadata for: Tukutuku Puzzle Challenges | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Puzzle Challenges | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/tukutuku-puzzle-challenges.html' OR path LIKE '%tukutuku-puzzle-challenges.html';


-- Update metadata for: Subjects | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Subjects | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/subjects.html' OR path LIKE '%subjects.html';


-- Update metadata for: Cultural STEM Assessment Rubric | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural STEM Assessment Rubric | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/cultural-stem-assessment-rubric.html' OR path LIKE '%cultural-stem-assessment-rubric.html';


-- Update metadata for: Year 9 Starter Pack: Essential Skills for High Sch
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Year 9 Starter Pack: Essential Skills for High School Success - Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/year-9-starter-pack-alpha-build.html' OR path LIKE '%year-9-starter-pack-alpha-build.html';


-- Update metadata for: Year 9 Starter Pack: Essential Skills for High Sch
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Year 9 Starter Pack: Essential Skills for High School Success - Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/year-9-starter-pack-essential-skills-for-high-school-success.html' OR path LIKE '%year-9-starter-pack-essential-skills-for-high-school-success.html';


-- Update metadata for: Tukutuku Reading Comprehension | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Reading Comprehension | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/tukutuku-reading-comprehension.html' OR path LIKE '%tukutuku-reading-comprehension.html';


-- Update metadata for: Ranginui Walker Biography | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Ranginui Walker Biography | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/walker-ranginui-biography.html' OR path LIKE '%walker-ranginui-biography.html';


-- Update metadata for: Tukutuku Station Questions | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Station Questions | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/tukutuku-station-questions.html' OR path LIKE '%tukutuku-station-questions.html';


-- Update metadata for: Unit Hub | Critical Thinking Skills: Media Literac
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Unit Hub | Critical Thinking Skills: Media Literacy & Information Analysis | Te Kete Ako - Postcolonial Social Studies')
WHERE path = 'public/integrated-handouts/Year 9/critical-thinking-unit.html' OR path LIKE '%critical-thinking-unit.html';


-- Update metadata for: Tukutuku Escape Room | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Escape Room | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/tukutuku-escape-room.html' OR path LIKE '%tukutuku-escape-room.html';


-- Update metadata for: Unit Plans | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Unit Plans | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/unit-plans.html' OR path LIKE '%unit-plans.html';


-- Update metadata for: Tukutuku Pattern Explorer | Interactive Mathematic
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Pattern Explorer | Interactive Mathematics | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/tukutuku-pattern-explorer.html' OR path LIKE '%tukutuku-pattern-explorer.html';


-- Update metadata for: Research Methods | Te Kete Ako Handout
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Research Methods | Te Kete Ako Handout')
WHERE path = 'public/integrated-handouts/Year 9/research-methods-handout.html' OR path LIKE '%research-methods-handout.html';


-- Update metadata for: Tukutuku Numeracy Problems | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Numeracy Problems | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 9/tukutuku-numeracy-problems.html' OR path LIKE '%tukutuku-numeracy-problems.html';


-- Update metadata for: YouTube Library Administration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'YouTube Library Administration | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 8/admin-youtube-library.html' OR path LIKE '%admin-youtube-library.html';


-- Update metadata for: Te Kete Ako - Intelligent Resource Discovery | Gra
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Intelligent Resource Discovery | GraphRAG Search')
WHERE path = 'public/integrated-handouts/Year 8/graphrag-search.html' OR path LIKE '%graphrag-search.html';


-- Update metadata for: My Submissions | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'My Submissions | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 8/my-submissions.html' OR path LIKE '%my-submissions.html';


-- Update metadata for: Kaitiaki Aronui - Advanced AI Capabilities Showcas
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Kaitiaki Aronui - Advanced AI Capabilities Showcase | Teacher Professional Development')
WHERE path = 'public/integrated-handouts/Year 8/kaitiaki-aronui-capability-showcase.html' OR path LIKE '%kaitiaki-aronui-capability-showcase.html';


-- Update metadata for: Resource Connections | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Resource Connections | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 8/resource-connections.html' OR path LIKE '%resource-connections.html';


-- Update metadata for: Social Studies | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Social Studies | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 8/social-studies.html' OR path LIKE '%social-studies.html';


-- Update metadata for: Student Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Student Dashboard | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 8/student-dashboard.html' OR path LIKE '%student-dashboard.html';


-- Update metadata for: Sitemap
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Sitemap')
WHERE path = 'public/integrated-handouts/Year 8/sitemap.html' OR path LIKE '%sitemap.html';


-- Update metadata for: Bar Graph Worksheet
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Bar Graph Worksheet')
WHERE path = 'public/integrated-handouts/Year 8/bar-graph-handout.html' OR path LIKE '%bar-graph-handout.html';


-- Update metadata for: Project Submission | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Project Submission | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 8/project-submission.html' OR path LIKE '%project-submission.html';


-- Update metadata for: Handout: Climate Change in Aotearoa
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Climate Change in Aotearoa')
WHERE path = 'public/integrated-handouts/Year 8/climate-change-aotearoa-handout.html' OR path LIKE '%climate-change-aotearoa-handout.html';


-- Update metadata for: Teacher Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Teacher Dashboard | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 8/teacher-dashboard.html' OR path LIKE '%teacher-dashboard.html';


-- Update metadata for: Unit Plans | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Unit Plans | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 8/units.html' OR path LIKE '%units.html';


-- Update metadata for: Handout: Māori Navigation
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Māori Navigation')
WHERE path = 'public/integrated-handouts/Year 8/maori-navigation-wayfinding-handout.html' OR path LIKE '%maori-navigation-wayfinding-handout.html';


-- Update metadata for: Te Kete Ako | World's First AI-Enhanced Cultural E
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | World''s First AI-Enhanced Cultural Educational Platform')
WHERE path = 'public/integrated-handouts/Year 8/index-new.html' OR path LIKE '%index-new.html';


-- Update metadata for: Search | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Search | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 8/search.html' OR path LIKE '%search.html';


-- Update metadata for: Educational Transformation | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Educational Transformation | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 8/educational-transformation-showcase.html' OR path LIKE '%educational-transformation-showcase.html';


-- Update metadata for: Unit Hub | Year 8 Systems: Decolonizing Power Stru
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Unit Hub | Year 8 Systems: Decolonizing Power Structures | Te Kete Ako - Postcolonial Social Studies')
WHERE path = 'public/integrated-handouts/Year 8/y8-systems-unit.html' OR path LIKE '%y8-systems-unit.html';


-- Update metadata for: Community Action Project Brief | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Community Action Project Brief | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Year 8/project-brief.html' OR path LIKE '%project-brief.html';


-- Update metadata for: Handout: Body Sensor Map
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 1',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Handout: Body Sensor Map')
WHERE path = 'public/integrated-handouts/Year 1/body-sensor-map.html' OR path LIKE '%body-sensor-map.html';


-- Update metadata for: Resource Discovery Hub - Te Kete Ako V2.5
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 1',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Resource Discovery Hub - Te Kete Ako V2.5')
WHERE path = 'public/integrated-handouts/Year 1/resource-discovery-hub.html' OR path LIKE '%resource-discovery-hub.html';


-- Update metadata for: Biotechnology Ethics Through Māori Worldview | Te 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 6',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Biotechnology Ethics Through Māori Worldview | Te Kete Ako')
WHERE path = 'public/integrated-handouts/Level 6/biotechnology-ethics-through-māori-worldview.html' OR path LIKE '%biotechnology-ethics-through-māori-worldview.html';


-- Update metadata for: Data Visualization of Cultural Demographics
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 6',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Data Visualization of Cultural Demographics')
WHERE path = 'public/integrated-handouts/Level 6/data-visualization-of-cultural-demographics.html' OR path LIKE '%data-visualization-of-cultural-demographics.html';


-- Update metadata for: Chemistry of Traditional Māori Medicine
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 6',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Chemistry of Traditional Māori Medicine')
WHERE path = 'public/integrated-handouts/Level 6/chemistry-of-traditional-māori-medicine.html' OR path LIKE '%chemistry-of-traditional-māori-medicine.html';


-- Update metadata for: Biotechnology Ethics Through Māori Worldview
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Biotechnology Ethics Through Māori Worldview')
WHERE path = 'public/integrated-handouts/Level 7/biotechnology-ethics-through-māori-worldview.html' OR path LIKE '%biotechnology-ethics-through-māori-worldview.html';


-- Update metadata for: Calculus Applications in Environmental Modeling
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Calculus Applications in Environmental Modeling')
WHERE path = 'public/integrated-handouts/Level 7/calculus-applications-in-environmental-modeling.html' OR path LIKE '%calculus-applications-in-environmental-modeling.html';


-- Update metadata for: Cultural Competence | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Competence | Te Kete Ako')
WHERE path = 'public/competencies/cultural-competence.html' OR path LIKE '%cultural-competence.html';


-- Update metadata for: Collaboration Competency | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Collaboration Competency | Te Kete Ako')
WHERE path = 'public/competencies/collaboration.html' OR path LIKE '%collaboration.html';


-- Update metadata for: Self-Management Competency | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Self-Management Competency | Te Kete Ako')
WHERE path = 'public/competencies/self-management.html' OR path LIKE '%self-management.html';


-- Update metadata for: Critical Thinking Competency | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Critical Thinking Competency | Te Kete Ako')
WHERE path = 'public/competencies/critical-thinking.html' OR path LIKE '%critical-thinking.html';


-- Update metadata for: Communication Competency | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Communication Competency | Te Kete Ako')
WHERE path = 'public/competencies/communication.html' OR path LIKE '%communication.html';


-- Update metadata for: Creativity & Innovation Competency | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Creativity & Innovation Competency | Te Kete Ako')
WHERE path = 'public/competencies/creativity.html' OR path LIKE '%creativity.html';


-- Update metadata for: Digital Literacy Competency | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Literacy Competency | Te Kete Ako')
WHERE path = 'public/competencies/digital-literacy.html' OR path LIKE '%digital-literacy.html';


-- Update metadata for: Pūrākau - Māori Narratives & Stories | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Pūrākau - Māori Narratives & Stories | Te Kete Ako')
WHERE path = 'public/concepts/purakau.html' OR path LIKE '%purakau.html';


-- Update metadata for: Kaitiakitanga - Guardianship & Stewardship | Te Ke
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Kaitiakitanga - Guardianship & Stewardship | Te Kete Ako')
WHERE path = 'public/concepts/kaitiakitanga.html' OR path LIKE '%kaitiakitanga.html';


-- Update metadata for: Kaitiaki Aronui - Advanced AI Capabilities Showcas
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Kaitiaki Aronui - Advanced AI Capabilities Showcase | Teacher Professional Development')
WHERE path = 'public/professional-development/kaitiaki-aronui-capability-showcase.html' OR path LIKE '%kaitiaki-aronui-capability-showcase.html';


-- Update metadata for: Critical Thinking Toolkit | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Critical Thinking Toolkit | Te Kete Ako')
WHERE path = 'public/critical-thinking/critical-thinking-toolkit.html' OR path LIKE '%critical-thinking-toolkit.html';


-- Update metadata for: Matauranga Thinking Framework | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Matauranga Thinking Framework | Te Kete Ako')
WHERE path = 'public/critical-thinking/resources/matauranga-thinking-framework.html' OR path LIKE '%matauranga-thinking-framework.html';


-- Update metadata for: Critical Communication Portfolio | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Critical Communication Portfolio | Te Kete Ako')
WHERE path = 'public/critical-thinking/resources/critical-communication-portfolio.html' OR path LIKE '%critical-communication-portfolio.html';


-- Update metadata for: Nzhistory Investigation Toolkit | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Nzhistory Investigation Toolkit | Te Kete Ako')
WHERE path = 'public/critical-thinking/resources/nzhistory-investigation-toolkit.html' OR path LIKE '%nzhistory-investigation-toolkit.html';


-- Update metadata for: Rnz Analysis Framework | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Rnz Analysis Framework | Te Kete Ako')
WHERE path = 'public/critical-thinking/resources/rnz-analysis-framework.html' OR path LIKE '%rnz-analysis-framework.html';


-- Update metadata for: Source Evaluation Matrix | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'assessment',
    title = COALESCE(NULLIF(title, ''), 'Source Evaluation Matrix | Te Kete Ako')
WHERE path = 'public/critical-thinking/resources/source-evaluation-matrix.html' OR path LIKE '%source-evaluation-matrix.html';


-- Update metadata for: Lesson 9 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 9 | Te Kete Ako')
WHERE path = 'public/critical-thinking/lessons/lesson-9.html' OR path LIKE '%lesson-9.html';


-- Update metadata for: Te Kete Ako | Critical Thinking - Lesson 5: Recogn
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Critical Thinking - Lesson 5: Recognizing Propaganda & Persuasion')
WHERE path = 'public/critical-thinking/lessons/lesson-5.html' OR path LIKE '%lesson-5.html';


-- Update metadata for: Te Kete Ako | Critical Thinking - Lesson 4: Logic 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Critical Thinking - Lesson 4: Logic & Reasoning')
WHERE path = 'public/critical-thinking/lessons/lesson-4.html' OR path LIKE '%lesson-4.html';


-- Update metadata for: Lesson 10 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 10 | Te Kete Ako')
WHERE path = 'public/critical-thinking/lessons/lesson-10.html' OR path LIKE '%lesson-10.html';


-- Update metadata for: Te Kete Ako | Critical Thinking - Lesson 8: Argume
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Critical Thinking - Lesson 8: Argument Analysis & Logical Reasoning')
WHERE path = 'public/critical-thinking/lessons/lesson-8.html' OR path LIKE '%lesson-8.html';


-- Update metadata for: Te Kete Ako - Lesson 3: Source Evaluation & Fact-C
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Lesson 3: Source Evaluation & Fact-Checking')
WHERE path = 'public/critical-thinking/lessons/lesson-3.html' OR path LIKE '%lesson-3.html';


-- Update metadata for: Te Kete Ako - Identifying Bias in News Reporting
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Identifying Bias in News Reporting')
WHERE path = 'public/critical-thinking/lessons/lesson-2.html' OR path LIKE '%lesson-2.html';


-- Update metadata for: Te Kete Ako | Critical Thinking - Lesson 1: Unders
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Critical Thinking - Lesson 1: Understanding Media Messages')
WHERE path = 'public/critical-thinking/lessons/lesson-1.html' OR path LIKE '%lesson-1.html';


-- Update metadata for: Te Kete Ako | Critical Thinking - Lesson 7: Advanc
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Critical Thinking - Lesson 7: Advanced Research & Information Evaluation')
WHERE path = 'public/critical-thinking/lessons/lesson-7.html' OR path LIKE '%lesson-7.html';


-- Update metadata for: Te Kete Ako | Critical Thinking - Lesson 6: Digita
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Critical Thinking - Lesson 6: Digital Literacy & Online Safety')
WHERE path = 'public/critical-thinking/lessons/lesson-6.html' OR path LIKE '%lesson-6.html';


-- Update metadata for: Plants & Rongoā Māori | Year 7 Science
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Plants & Rongoā Māori | Year 7 Science')
WHERE path = 'public/lessons/y7-science-plants-rongoā.html' OR path LIKE '%y7-science-plants-rongoā.html';


-- Update metadata for: Social Studies Lessons Index | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Social Studies Lessons Index | Te Kete Ako')
WHERE path = 'public/lessons/social-studies-index.html' OR path LIKE '%social-studies-index.html';


-- Update metadata for: Activities | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Activities | Te Kete Ako')
WHERE path = 'public/lessons/activities.html' OR path LIKE '%activities.html';


-- Update metadata for: Statistics for Social Justice | Year 9 Mathematics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Statistics for Social Justice | Year 9 Mathematics')
WHERE path = 'public/lessons/y9-math-statistics-social-justice.html' OR path LIKE '%y9-math-statistics-social-justice.html';


-- Update metadata for: Financial Literacy: Budgeting & Whānau Economics |
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Financial Literacy: Budgeting & Whānau Economics | Year 9 Mathematics')
WHERE path = 'public/lessons/y9-math-financial-literacy-budgeting.html' OR path LIKE '%y9-math-financial-literacy-budgeting.html';


-- Update metadata for: Speed Distance Time Calculator | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Speed Distance Time Calculator | Te Kete Ako')
WHERE path = 'public/lessons/speed-distance-time-calculator-physics.html' OR path LIKE '%speed-distance-time-calculator-physics.html';


-- Update metadata for: Algebra Pattern Explorer | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Algebra Pattern Explorer | Te Kete Ako')
WHERE path = 'public/lessons/algebra-pattern-explorer-interactive.html' OR path LIKE '%algebra-pattern-explorer-interactive.html';


-- Update metadata for: AI Ethics Through Māori Data Sovereignty
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics Through Māori Data Sovereignty')
WHERE path = 'public/lessons/ai-ethics-through-māori-data-sovereignty.html' OR path LIKE '%ai-ethics-through-māori-data-sovereignty.html';


-- Update metadata for: Cells & Whakapapa: Interconnected Systems | Year 8
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cells & Whakapapa: Interconnected Systems | Year 8 Science')
WHERE path = 'public/lessons/y8-science-cells-whakapapa.html' OR path LIKE '%y8-science-cells-whakapapa.html';


-- Update metadata for: Critical Thinking Introduction | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Critical Thinking Introduction | Te Kete Ako')
WHERE path = 'public/lessons/critical-thinking-introduction.html' OR path LIKE '%critical-thinking-introduction.html';


-- Update metadata for: Measurement: Designing a Marae | Year 7 Mathematic
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Measurement: Designing a Marae | Year 7 Mathematics')
WHERE path = 'public/lessons/y7-math-measurement-marae.html' OR path LIKE '%y7-math-measurement-marae.html';


-- Update metadata for: Coding Basics: Create a Te Reo Quiz Game | Year 8 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Coding Basics: Create a Te Reo Quiz Game | Year 8 Digital Technologies')
WHERE path = 'public/lessons/y8-digital-tech-coding-basics-games.html' OR path LIKE '%y8-digital-tech-coding-basics-games.html';


-- Update metadata for: Media Literacy: Analyzing Māori Representation
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Media Literacy: Analyzing Māori Representation')
WHERE path = 'public/lessons/media-literacy-analyzing-māori-representation.html' OR path LIKE '%media-literacy-analyzing-māori-representation.html';


-- Update metadata for: Persuasive Writing: Treaty Perspectives | Year 8 E
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Persuasive Writing: Treaty Perspectives | Year 8 English')
WHERE path = 'public/lessons/y8-english-persuasive-writing-treaty.html' OR path LIKE '%y8-english-persuasive-writing-treaty.html';


-- Update metadata for: A Forum for Justice: The Waitangi Tribunal | Te Ke
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'A Forum for Justice: The Waitangi Tribunal | Te Kete Ako')
WHERE path = 'public/lessons/walker-lesson-1.4-a-forum-for-justice.html' OR path LIKE '%walker-lesson-1.4-a-forum-for-justice.html';


-- Update metadata for: Climate Change & Local Action | Year 9 Science
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Climate Change & Local Action | Year 9 Science')
WHERE path = 'public/lessons/y9-science-climate-change-action.html' OR path LIKE '%y9-science-climate-change-action.html';


-- Update metadata for: Year 8 Social Studies - Māori Migration to Aotearo
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Year 8 Social Studies - Māori Migration to Aotearoa | Kaitiaki Aronui Generated')
WHERE path = 'public/lessons/kaitiaki-generated-maori-migration-lesson.html' OR path LIKE '%kaitiaki-generated-maori-migration-lesson.html';


-- Update metadata for: Statistical Analysis of Sports Performance
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Statistical Analysis of Sports Performance')
WHERE path = 'public/lessons/statistical-analysis-of-sports-performance.html' OR path LIKE '%statistical-analysis-of-sports-performance.html';


-- Update metadata for: Geometry Through Kōwhaiwhai Patterns | Year 8 Math
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Geometry Through Kōwhaiwhai Patterns | Year 8 Mathematics')
WHERE path = 'public/lessons/y8-math-geometry-kowhaiwhai.html' OR path LIKE '%y8-math-geometry-kowhaiwhai.html';


-- Update metadata for: NZ Government & Māori Representation | Year 8 Soci
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Government & Māori Representation | Year 8 Social Studies')
WHERE path = 'public/lessons/y8-social-studies-nz-government.html' OR path LIKE '%y8-social-studies-nz-government.html';


-- Update metadata for: Career Pathways in STEM for Māori Students
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Career Pathways in STEM for Māori Students')
WHERE path = 'public/lessons/career-pathways-in-stem-for-māori-students.html' OR path LIKE '%career-pathways-in-stem-for-māori-students.html';


-- Update metadata for: Lesson 1: Pre-Colonial Innovation | Unit 2: Decolo
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Pre-Colonial Innovation | Unit 2: Decolonized History | Te Kete Ako')
WHERE path = 'public/lessons/unit-2-lesson-1.html' OR path LIKE '%unit-2-lesson-1.html';


-- Update metadata for: Introduction to Te Tiriti o Waitangi | Year 7 Soci
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Introduction to Te Tiriti o Waitangi | Year 7 Social Studies')
WHERE path = 'public/lessons/y7-social-studies-treaty-introduction.html' OR path LIKE '%y7-social-studies-treaty-introduction.html';


-- Update metadata for: Logical Fallacies Detection | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Logical Fallacies Detection | Te Kete Ako')
WHERE path = 'public/lessons/logical-fallacies-detection.html' OR path LIKE '%logical-fallacies-detection.html';


-- Update metadata for: Years of Anger: The Protest Movements | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Years of Anger: The Protest Movements | Te Kete Ako')
WHERE path = 'public/lessons/walker-lesson-1.3-years-of-anger.html' OR path LIKE '%walker-lesson-1.3-years-of-anger.html';


-- Update metadata for: Lesson: Whakatā Roro - Brain Break | Mangakōtukutu
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson: Whakatā Roro - Brain Break | Mangakōtukutuku College')
WHERE path = 'public/lessons/brain-break-wordsearch-lesson.html' OR path LIKE '%brain-break-wordsearch-lesson.html';


-- Update metadata for: Impact of Colonization on Māori | Year 9 Social St
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Impact of Colonization on Māori | Year 9 Social Studies')
WHERE path = 'public/lessons/y9-social-studies-colonization-impacts.html' OR path LIKE '%y9-social-studies-colonization-impacts.html';


-- Update metadata for: Poetry Analysis Through Māori Literary Traditions
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Poetry Analysis Through Māori Literary Traditions')
WHERE path = 'public/lessons/poetry-analysis-through-māori-literary-traditions.html' OR path LIKE '%poetry-analysis-through-māori-literary-traditions.html';


-- Update metadata for: Login | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Login | Te Kete Ako')
WHERE path = 'public/lessons/login.html' OR path LIKE '%login.html';


-- Update metadata for: AI Ethics Through Māori Data Sovereignty | Te Kete
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics Through Māori Data Sovereignty | Te Kete Ako')
WHERE path = 'public/lessons/ai-ethics-through-māori-data-sovereignty-FIXED.html' OR path LIKE '%ai-ethics-through-māori-data-sovereignty-FIXED.html';


-- Update metadata for: Narrative Writing Using Māori Story Structures
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Narrative Writing Using Māori Story Structures')
WHERE path = 'public/lessons/narrative-writing-using-māori-story-structures.html' OR path LIKE '%narrative-writing-using-māori-story-structures.html';


-- Update metadata for: Te Reo Basics: Greetings & Pepeha | Year 7 Te Reo 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Basics: Greetings & Pepeha | Year 7 Te Reo Māori')
WHERE path = 'public/lessons/y7-te-reo-greetings-pepeha.html' OR path LIKE '%y7-te-reo-greetings-pepeha.html';


-- Update metadata for: Ecosystems & Kaitiakitanga | Year 7 Science
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Ecosystems & Kaitiakitanga | Year 7 Science')
WHERE path = 'public/lessons/y7-science-ecosystem-kaitiakitanga.html' OR path LIKE '%y7-science-ecosystem-kaitiakitanga.html';


-- Update metadata for: Voting Systems Interactive - NZ Democracy | Te Ket
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Voting Systems Interactive - NZ Democracy | Te Kete Ako')
WHERE path = 'public/lessons/voting-systems-civics-interactive.html' OR path LIKE '%voting-systems-civics-interactive.html';


-- Update metadata for: Research Skills: Traditional and Digital Sources
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Research Skills: Traditional and Digital Sources')
WHERE path = 'public/lessons/research-skills-using-traditional-and-digital-sources.html' OR path LIKE '%research-skills-using-traditional-and-digital-sources.html';


-- Update metadata for: Earthquake Science - NZ Seismic Activity | Te Kete
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Earthquake Science - NZ Seismic Activity | Te Kete Ako')
WHERE path = 'public/lessons/earthquake-science-interactive-nz.html' OR path LIKE '%earthquake-science-interactive-nz.html';


-- Update metadata for: English Lessons Index | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'English Lessons Index | Te Kete Ako')
WHERE path = 'public/lessons/english-index.html' OR path LIKE '%english-index.html';


-- Update metadata for: Creative Writing Inspired by Whakataukī
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Creative Writing Inspired by Whakataukī')
WHERE path = 'public/lessons/creative-writing-inspired-by-whakataukī.html' OR path LIKE '%creative-writing-inspired-by-whakataukī.html';


-- Update metadata for: Register | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Register | Te Kete Ako')
WHERE path = 'public/lessons/register-simple.html' OR path LIKE '%register-simple.html';


-- Update metadata for: Population Growth Interactive | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Population Growth Interactive | Te Kete Ako')
WHERE path = 'public/lessons/population-growth-interactive-demographics.html' OR path LIKE '%population-growth-interactive-demographics.html';


-- Update metadata for: Debate Skills with Māori Oratory Traditions
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Debate Skills with Māori Oratory Traditions')
WHERE path = 'public/lessons/debate-skills-with-māori-oratory-traditions.html' OR path LIKE '%debate-skills-with-māori-oratory-traditions.html';


-- Update metadata for: Who was Ranginui Walker? | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Who was Ranginui Walker? | Te Kete Ako')
WHERE path = 'public/lessons/walker-lesson-1.1-who-was-ranginui-walker.html' OR path LIKE '%walker-lesson-1.1-who-was-ranginui-walker.html';


-- Update metadata for: Unit 2 Lesson 3 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 3 | Te Kete Ako')
WHERE path = 'public/lessons/unit-2-lesson-3.html' OR path LIKE '%unit-2-lesson-3.html';


-- Update metadata for: Budget Calculator - Whakahaere Moni | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Budget Calculator - Whakahaere Moni | Te Kete Ako')
WHERE path = 'public/lessons/budget-calculator-whakahaere-moni.html' OR path LIKE '%budget-calculator-whakahaere-moni.html';


-- Update metadata for: Introduction to Patterns & Algebra | Year 7 Mathem
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Introduction to Patterns & Algebra | Year 7 Mathematics')
WHERE path = 'public/lessons/y7-math-patterns-algebra-intro.html' OR path LIKE '%y7-math-patterns-algebra-intro.html';


-- Update metadata for: Critical Analysis of Historical Documents | Te Ket
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Critical Analysis of Historical Documents | Te Kete Ako')
WHERE path = 'public/lessons/critical-analysis-of-historical-documents.html' OR path LIKE '%critical-analysis-of-historical-documents.html';


-- Update metadata for: Percentage Calculator - Smart Shopping | Te Kete A
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Percentage Calculator - Smart Shopping | Te Kete Ako')
WHERE path = 'public/lessons/percentage-calculator-discount-shopping.html' OR path LIKE '%percentage-calculator-discount-shopping.html';


-- Update metadata for: Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/lessons/curriculum-alignment.html' OR path LIKE '%curriculum-alignment.html';


-- Update metadata for: Traditional Navigation & Modern GPS Integration - 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Traditional Navigation & Modern GPS Integration - Te Kete Ako')
WHERE path = 'public/lessons/traditional-navigation-and-modern-gps-integration.html' OR path LIKE '%traditional-navigation-and-modern-gps-integration.html';


-- Update metadata for: Lesson: Oropuare - Vowel Sounds | Mangakōtukutuku 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson: Oropuare - Vowel Sounds | Mangakōtukutuku College')
WHERE path = 'public/lessons/vowel-sounds-lesson.html' OR path LIKE '%vowel-sounds-lesson.html';


-- Update metadata for: Genetics and Whakapapa
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Genetics and Whakapapa')
WHERE path = 'public/lessons/genetics-and-whakapapa-scientific-and-cultural-perspectives.html' OR path LIKE '%genetics-and-whakapapa-scientific-and-cultural-perspectives.html';


-- Update metadata for: Lesson 2: The Aotearoa Wars | Unit 2: Decolonized 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: The Aotearoa Wars | Unit 2: Decolonized History | Te Kete Ako')
WHERE path = 'public/lessons/unit-2-lesson-2.html' OR path LIKE '%unit-2-lesson-2.html';


-- Update metadata for: Probability Interactive - Ngā Mahi Tīpako | Te Ket
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Probability Interactive - Ngā Mahi Tīpako | Te Kete Ako')
WHERE path = 'public/lessons/probability-interactive-ngā-mahi-tīpako.html' OR path LIKE '%probability-interactive-ngā-mahi-tīpako.html';


-- Update metadata for: Poetry Through Māori Oral Traditions | Year 9 Engl
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Poetry Through Māori Oral Traditions | Year 9 English')
WHERE path = 'public/lessons/y9-english-poetry-maori-oral-traditions.html' OR path LIKE '%y9-english-poetry-maori-oral-traditions.html';


-- Update metadata for: Mathematics Lessons Index | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Mathematics Lessons Index | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-index.html' OR path LIKE '%mathematics-index.html';


-- Update metadata for: Renewable Energy and Māori Innovation
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Renewable Energy and Māori Innovation')
WHERE path = 'public/lessons/renewable-energy-and-māori-innovation.html' OR path LIKE '%renewable-energy-and-māori-innovation.html';


-- Update metadata for: Unit 2 Lesson 5 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 5 | Te Kete Ako')
WHERE path = 'public/lessons/unit-2-lesson-5.html' OR path LIKE '%unit-2-lesson-5.html';


-- Update metadata for: Climate Data Visualization - Interactive Lesson | 
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Climate Data Visualization - Interactive Lesson | Te Kete Ako')
WHERE path = 'public/lessons/climate-data-visualization-interactive.html' OR path LIKE '%climate-data-visualization-interactive.html';


-- Update metadata for: Fraction Visualizer - Hangi Portions | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Fraction Visualizer - Hangi Portions | Te Kete Ako')
WHERE path = 'public/lessons/fraction-visualizer-interactive.html' OR path LIKE '%fraction-visualizer-interactive.html';


-- Update metadata for: Astronomy & Maramataka: Māori Lunar Calendar | Yea
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Astronomy & Maramataka: Māori Lunar Calendar | Year 9 Science')
WHERE path = 'public/lessons/y9-science-astronomy-maramataka.html' OR path LIKE '%y9-science-astronomy-maramataka.html';


-- Update metadata for: Creative Problem Solving with Design Thinking
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Creative Problem Solving with Design Thinking')
WHERE path = 'public/lessons/creative-problem-solving-with-design-thinking.html' OR path LIKE '%creative-problem-solving-with-design-thinking.html';


-- Update metadata for: Narrative Writing: Pūrākau Structure | Year 8 Engl
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Narrative Writing: Pūrākau Structure | Year 8 English')
WHERE path = 'public/lessons/y8-english-narrative-purakau-structure.html' OR path LIKE '%y8-english-narrative-purakau-structure.html';


-- Update metadata for: Geometry Calculator: Area & Perimeter | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Geometry Calculator: Area & Perimeter | Te Kete Ako')
WHERE path = 'public/lessons/geometry-area-perimeter-calculator.html' OR path LIKE '%geometry-area-perimeter-calculator.html';


-- Update metadata for: Narrative Writing Using Pūrākau Structure | Year 7
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Narrative Writing Using Pūrākau Structure | Year 7 English')
WHERE path = 'public/lessons/y7-english-narrative-writing-purakau.html' OR path LIKE '%y7-english-narrative-writing-purakau.html';


-- Update metadata for: Climate Change Through Te Taiao Māori Lens - Te Ke
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Climate Change Through Te Taiao Māori Lens - Te Kete Ako')
WHERE path = 'public/lessons/climate-change-through-te-taiao-māori-lens.html' OR path LIKE '%climate-change-through-te-taiao-māori-lens.html';


-- Update metadata for: My Kete | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Kete | Te Kete Ako')
WHERE path = 'public/lessons/my-kete.html' OR path LIKE '%my-kete.html';


-- Update metadata for: Digital Storytelling with Pūrākau Framework
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Storytelling with Pūrākau Framework')
WHERE path = 'public/lessons/digital-storytelling-with-pūrākau-framework.html' OR path LIKE '%digital-storytelling-with-pūrākau-framework.html';


-- Update metadata for: Argumentative Writing on Contemporary Māori Issues
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Argumentative Writing on Contemporary Māori Issues')
WHERE path = 'public/lessons/argumentative-writing-on-contemporary-māori-issues.html' OR path LIKE '%argumentative-writing-on-contemporary-māori-issues.html';


-- Update metadata for: Reclaiming the Narrative: Ka Whawhai Tonu Mātou | 
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Reclaiming the Narrative: Ka Whawhai Tonu Mātou | Te Kete Ako')
WHERE path = 'public/lessons/walker-lesson-1.5-reclaiming-the-narrative.html' OR path LIKE '%walker-lesson-1.5-reclaiming-the-narrative.html';


-- Update metadata for: Evidence Evaluation Frameworks | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Evidence Evaluation Frameworks | Te Kete Ako')
WHERE path = 'public/lessons/evidence-evaluation-frameworks.html' OR path LIKE '%evidence-evaluation-frameworks.html';


-- Update metadata for: Advanced Critical Thinking: Decision-Making Framew
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Advanced Critical Thinking: Decision-Making Frameworks | Te Kete Ako')
WHERE path = 'public/lessons/advanced-critical-thinking-decision-making.html' OR path LIKE '%advanced-critical-thinking-decision-making.html';


-- Update metadata for: Digital Citizenship & Kaitiakitanga | Year 7 Digit
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Citizenship & Kaitiakitanga | Year 7 Digital Technologies')
WHERE path = 'public/lessons/y7-digital-tech-digital-citizenship.html' OR path LIKE '%y7-digital-tech-digital-citizenship.html';


-- Update metadata for: The Great Migration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Great Migration | Te Kete Ako')
WHERE path = 'public/lessons/walker-lesson-1.2-the-great-migration.html' OR path LIKE '%walker-lesson-1.2-the-great-migration.html';


-- Update metadata for: Scientific Method Using Traditional Māori Practice
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Scientific Method Using Traditional Māori Practices')
WHERE path = 'public/lessons/scientific-method-using-traditional-māori-practices.html' OR path LIKE '%scientific-method-using-traditional-māori-practices.html';


-- Update metadata for: Game Development with Cultural Themes
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Game Development with Cultural Themes')
WHERE path = 'public/lessons/game-development-with-cultural-themes.html' OR path LIKE '%game-development-with-cultural-themes.html';


-- Update metadata for: Science Lessons Index | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Science Lessons Index | Te Kete Ako')
WHERE path = 'public/lessons/science-index.html' OR path LIKE '%science-index.html';


-- Update metadata for: Māori Protest Movements 1970s-Present | Year 10 So
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Māori Protest Movements 1970s-Present | Year 10 Social Studies')
WHERE path = 'public/lessons/y10-social-studies-protest-movements.html' OR path LIKE '%y10-social-studies-protest-movements.html';


-- Update metadata for: Forces & Motion: Waka Design | Year 8 Science
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Forces & Motion: Waka Design | Year 8 Science')
WHERE path = 'public/lessons/y8-science-forces-waka-design.html' OR path LIKE '%y8-science-forces-waka-design.html';


-- Update metadata for: AI Ethics & Bias Through Māori Lens | Year 9 Digit
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics & Bias Through Māori Lens | Year 9 Digital Technologies')
WHERE path = 'public/lessons/y9-digital-tech-ai-ethics-bias.html' OR path LIKE '%y9-digital-tech-ai-ethics-bias.html';


-- Update metadata for: Unit 2 Lesson 4 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 4 | Te Kete Ako')
WHERE path = 'public/lessons/unit-2-lesson-4.html' OR path LIKE '%unit-2-lesson-4.html';


-- Update metadata for: Argumentative Writing: Tino Rangatiratanga | Year 
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Argumentative Writing: Tino Rangatiratanga | Year 9 English')
WHERE path = 'public/lessons/y9-english-argumentative-writing-sovereignty.html' OR path LIKE '%y9-english-argumentative-writing-sovereignty.html';


-- Update metadata for: Genetics & Whakapapa: DNA as Living Connection | Y
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Genetics & Whakapapa: DNA as Living Connection | Year 9 Science')
WHERE path = 'public/lessons/y9-science-genetics-whakapapa-dna.html' OR path LIKE '%y9-science-genetics-whakapapa-dna.html';


-- Update metadata for: Te Whare Tapa Whā - Health and Wellbeing
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Whare Tapa Whā - Health and Wellbeing')
WHERE path = 'public/lessons/health-and-wellbeing-te-whare-tapa-whā-model.html' OR path LIKE '%health-and-wellbeing-te-whare-tapa-whā-model.html';


-- Update metadata for: Physics of Traditional Māori Instruments
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Physics of Traditional Māori Instruments')
WHERE path = 'public/lessons/physics-of-traditional-māori-instruments.html' OR path LIKE '%physics-of-traditional-māori-instruments.html';


-- Update metadata for: Podcast Lesson 1: Te Tiriti o Waitangi | Te Kete A
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Podcast Lesson 1: Te Tiriti o Waitangi | Te Kete Ako')
WHERE path = 'public/lessons/podcast-series/lesson-1-treaty-of-waitangi.html' OR path LIKE '%lesson-1-treaty-of-waitangi.html';


-- Update metadata for: Podcast Worksheet: Te Tiriti o Waitangi | Te Kete 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Podcast Worksheet: Te Tiriti o Waitangi | Te Kete Ako')
WHERE path = 'public/lessons/podcast-series/materials/worksheet-treaty-of-waitangi-podcast.html' OR path LIKE '%worksheet-treaty-of-waitangi-podcast.html';


-- Update metadata for: Diction & Tone Combined Lesson | Writers Toolkit |
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Diction & Tone Combined Lesson | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/diction-tone-lesson-plan.html' OR path LIKE '%diction-tone-lesson-plan.html';


-- Update metadata for: Environmental Literacy Framework | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Environmental Literacy Framework | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/environmental-literacy-framework.html' OR path LIKE '%environmental-literacy-framework.html';


-- Update metadata for: Lesson Plan: The Revision Process | Writer's Toolk
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: The Revision Process | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/revision-lesson-plan.html' OR path LIKE '%revision-lesson-plan.html';


-- Update metadata for: Lesson Plan: Informative Structures | Writer's Too
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Informative Structures | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/inform-structure-lesson-plan.html' OR path LIKE '%inform-structure-lesson-plan.html';


-- Update metadata for: The Writer's Toolkit: The Revision Process
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: The Revision Process')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-revision-handout.html' OR path LIKE '%writers-toolkit-revision-handout.html';


-- Update metadata for: Lesson Plan: Crafting Hooks | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Crafting Hooks | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/hook-lesson-plan.html' OR path LIKE '%hook-lesson-plan.html';


-- Update metadata for: The Writer's Toolkit: Word Choice (Diction)
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Word Choice (Diction)')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-diction-handout.html' OR path LIKE '%writers-toolkit-diction-handout.html';


-- Update metadata for: Lesson Plan: Tone & Voice | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Tone & Voice | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/tone-lesson-plan.html' OR path LIKE '%tone-lesson-plan.html';


-- Update metadata for: Lesson Plan: Sentence Fluency | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Sentence Fluency | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/fluency-lesson-plan.html' OR path LIKE '%fluency-lesson-plan.html';


-- Update metadata for: The Writer's Toolkit: The PEEL Method
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: The PEEL Method')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-peel-argument-handout.html' OR path LIKE '%writers-toolkit-peel-argument-handout.html';


-- Update metadata for: Housing Affordability Comprehension Handout | Te K
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Housing Affordability Comprehension Handout | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/housing-affordability-comprehension-handout.html' OR path LIKE '%housing-affordability-comprehension-handout.html';


-- Update metadata for: The Writer's Toolkit: Analogy & Metaphor | Mangakō
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Analogy & Metaphor | Mangakōtukutuku College')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-analogy-handout.html' OR path LIKE '%writers-toolkit-analogy-handout.html';


-- Update metadata for: Economic Justice Deep Dive Comprehension | Te Kete
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Economic Justice Deep Dive Comprehension | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/economic-justice-deep-dive-comprehension.html' OR path LIKE '%economic-justice-deep-dive-comprehension.html';


-- Update metadata for: Cognitive Biases | Critical Literacy Unit
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cognitive Biases | Critical Literacy Unit')
WHERE path = 'public/lessons/writers-toolkit/cognitive-biases-comprehension-handout.html' OR path LIKE '%cognitive-biases-comprehension-handout.html';


-- Update metadata for: The Writer's Toolkit: Formal vs. Informal Tone
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Formal vs. Informal Tone')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-tone-handout.html' OR path LIKE '%writers-toolkit-tone-handout.html';


-- Update metadata for: Lesson Plan: Word Choice (Diction) | Writer's Tool
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Word Choice (Diction) | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/diction-lesson-plan.html' OR path LIKE '%diction-lesson-plan.html';


-- Update metadata for: The Writer's Toolkit: Powerful Conclusions
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Powerful Conclusions')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-conclusion-handout.html' OR path LIKE '%writers-toolkit-conclusion-handout.html';


-- Update metadata for: Fluency & Suspense Combined Lesson | Writers Toolk
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Fluency & Suspense Combined Lesson | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/fluency-suspense-lesson-plan.html' OR path LIKE '%fluency-suspense-lesson-plan.html';


-- Update metadata for: The Writer's Toolkit: Rhetorical Devices
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Rhetorical Devices')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-rhetorical-devices-handout.html' OR path LIKE '%writers-toolkit-rhetorical-devices-handout.html';


-- Update metadata for: The Writer's Toolkit: Crafting Hooks
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Crafting Hooks')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-hook-handout.html' OR path LIKE '%writers-toolkit-hook-handout.html';


-- Update metadata for: Media Literacy Comprehension Handout | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Media Literacy Comprehension Handout | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/media-literacy-comprehension-handout.html' OR path LIKE '%media-literacy-comprehension-handout.html';


-- Update metadata for: Arguments Of Tino Rangatiratanga Handout | Te Kete
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Arguments Of Tino Rangatiratanga Handout | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/arguments-of-tino-rangatiratanga-handout.html' OR path LIKE '%arguments-of-tino-rangatiratanga-handout.html';


-- Update metadata for: Lesson Plan: Building Suspense | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Building Suspense | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/suspense-lesson-plan.html' OR path LIKE '%suspense-lesson-plan.html';


-- Update metadata for: The Writer's Toolkit: Suspense & Foreshadowing
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Suspense & Foreshadowing')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-suspense-handout.html' OR path LIKE '%writers-toolkit-suspense-handout.html';


-- Update metadata for: Lesson Plan: The PEEL Method | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: The PEEL Method | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/peel-lesson-plan.html' OR path LIKE '%peel-lesson-plan.html';


-- Update metadata for: Political Cartoon Analysis Handout | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Political Cartoon Analysis Handout | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/political-cartoon-analysis-handout.html' OR path LIKE '%political-cartoon-analysis-handout.html';


-- Update metadata for: Lesson Plan: The Power of Analogy | Writer's Toolk
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: The Power of Analogy | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/analogy-lesson-plan.html' OR path LIKE '%analogy-lesson-plan.html';


-- Update metadata for: Environmental Text Analysis Handout | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Environmental Text Analysis Handout | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/environmental-text-analysis-handout.html' OR path LIKE '%environmental-text-analysis-handout.html';


-- Update metadata for: Lesson Plan: Powerful Conclusions | Writer's Toolk
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Powerful Conclusions | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/conclusion-lesson-plan.html' OR path LIKE '%conclusion-lesson-plan.html';


-- Update metadata for: Misleading Graphs Comprehension Handout | Te Kete 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Misleading Graphs Comprehension Handout | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/misleading-graphs-comprehension-handout.html' OR path LIKE '%misleading-graphs-comprehension-handout.html';


-- Update metadata for: Lesson Plan: Rhetorical Devices | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Rhetorical Devices | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/rhetorical-devices-lesson-plan.html' OR path LIKE '%rhetorical-devices-lesson-plan.html';


-- Update metadata for: The Writer's Toolkit: Sentence Fluency | Mangakōtu
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Sentence Fluency | Mangakōtukutuku College')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-fluency-handout.html' OR path LIKE '%writers-toolkit-fluency-handout.html';


-- Update metadata for: The Writer's Toolkit: Informational Structures | M
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Informational Structures | Mangakōtukutuku College')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-inform-structure-handout.html' OR path LIKE '%writers-toolkit-inform-structure-handout.html';


-- Update metadata for: Ai Impact Comprehension Handout | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Ai Impact Comprehension Handout | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/ai-impact-comprehension-handout.html' OR path LIKE '%ai-impact-comprehension-handout.html';


-- Update metadata for: Lesson Plan: Show, Don't Tell | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Show, Don''t Tell | Writer''s Toolkit')
WHERE path = 'public/lessons/writers-toolkit/show-dont-tell-lesson-plan.html' OR path LIKE '%show-dont-tell-lesson-plan.html';


-- Update metadata for: The Writer's Toolkit: Show, Don't Tell | Mangakōtu
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Show, Don''t Tell | Mangakōtukutuku College')
WHERE path = 'public/lessons/writers-toolkit/writers-toolkit-show-dont-tell-handout.html' OR path LIKE '%writers-toolkit-show-dont-tell-handout.html';


-- Update metadata for: Writers Toolkit Implementation Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Writers Toolkit Implementation Guide | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/resources/writers-toolkit-implementation-guide.html' OR path LIKE '%writers-toolkit-implementation-guide.html';


-- Update metadata for: Digital Writing Tools | Writers Toolkit | Te Kete 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Writing Tools | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/resources/digital-writing-tools.html' OR path LIKE '%digital-writing-tools.html';


-- Update metadata for: Writers Toolkit Progress Tracker | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Writers Toolkit Progress Tracker | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/resources/writers-toolkit-progress-tracker.html' OR path LIKE '%writers-toolkit-progress-tracker.html';


-- Update metadata for: Station Rotation Templates | Writers Toolkit | Te 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Station Rotation Templates | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/resources/station-rotation-templates.html' OR path LIKE '%station-rotation-templates.html';


-- Update metadata for: Cultural Integration Templates | Writers Toolkit |
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Integration Templates | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/resources/cultural-integration-templates.html' OR path LIKE '%cultural-integration-templates.html';


-- Update metadata for: Writers Toolkit Assessment Rubric | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Writers Toolkit Assessment Rubric | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/resources/writers-toolkit-assessment-rubric.html' OR path LIKE '%writers-toolkit-assessment-rubric.html';


-- Update metadata for: Cognitive Writing Strategies | Writers Toolkit | T
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cognitive Writing Strategies | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/resources/cognitive-writing-strategies.html' OR path LIKE '%cognitive-writing-strategies.html';


-- Update metadata for: Interactive Writing Games | Writers Toolkit | Te K
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Interactive Writing Games | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/lessons/writers-toolkit/resources/interactive-writing-games.html' OR path LIKE '%interactive-writing-games.html';


-- Update metadata for: Rongoa Science Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Rongoa Science Lesson | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/rongoa-science-lesson.html' OR path LIKE '%rongoa-science-lesson.html';


-- Update metadata for: Navigation Mathematics Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Navigation Mathematics Lesson | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/navigation-mathematics-lesson.html' OR path LIKE '%navigation-mathematics-lesson.html';


-- Update metadata for: Marine Ecology Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Marine Ecology Lesson | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/marine-ecology-lesson.html' OR path LIKE '%marine-ecology-lesson.html';


-- Update metadata for: Climate Science Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Climate Science Lesson | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/climate-science-lesson.html' OR path LIKE '%climate-science-lesson.html';


-- Update metadata for: Assessment Rubrics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Assessment Rubrics | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/assessment-rubrics.html' OR path LIKE '%assessment-rubrics.html';


-- Update metadata for: Digital Storytelling Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Storytelling Lesson | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/digital-storytelling-lesson.html' OR path LIKE '%digital-storytelling-lesson.html';


-- Update metadata for: Scientific Equipment Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Scientific Equipment Guide | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/scientific-equipment-guide.html' OR path LIKE '%scientific-equipment-guide.html';


-- Update metadata for: Cultural Knowledge Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Knowledge Resources | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/cultural-knowledge-resources.html' OR path LIKE '%cultural-knowledge-resources.html';


-- Update metadata for: Whakairo Geometry | Mathematics & Science Toolkit 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Whakairo Geometry | Mathematics & Science Toolkit | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/whakairo-geometry-lesson.html' OR path LIKE '%whakairo-geometry-lesson.html';


-- Update metadata for: Engineering Design Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Engineering Design Lesson | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/engineering-design-lesson.html' OR path LIKE '%engineering-design-lesson.html';


-- Update metadata for: Algebraic Patterns Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Algebraic Patterns Lesson | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/algebraic-patterns-lesson.html' OR path LIKE '%algebraic-patterns-lesson.html';


-- Update metadata for: Energy Sustainability Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Energy Sustainability Lesson | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/energy-sustainability-lesson.html' OR path LIKE '%energy-sustainability-lesson.html';


-- Update metadata for: Environmental Monitoring Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Environmental Monitoring Lesson | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/environmental-monitoring-lesson.html' OR path LIKE '%environmental-monitoring-lesson.html';


-- Update metadata for: Statistical Storytelling Lesson | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Statistical Storytelling Lesson | Te Kete Ako')
WHERE path = 'public/lessons/mathematics-science-interactive-toolkit/statistical-storytelling-lesson.html' OR path LIKE '%statistical-storytelling-lesson.html';


-- Update metadata for: Unit 4 Economic Justice | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4 Economic Justice | Te Kete Ako')
WHERE path = 'public/lessons/units/unit-4-economic-justice.html' OR path LIKE '%unit-4-economic-justice.html';


-- Update metadata for: Unit 2 Decolonized History | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Decolonized History | Te Kete Ako')
WHERE path = 'public/lessons/units/unit-2-decolonized-history.html' OR path LIKE '%unit-2-decolonized-history.html';


-- Update metadata for: Cultural Assessment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Assessment | Te Kete Ako')
WHERE path = 'public/lessons/experiences/cultural-assessment.html' OR path LIKE '%cultural-assessment.html';


-- Update metadata for: Digital Purakau | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Purakau | Te Kete Ako')
WHERE path = 'public/lessons/experiences/digital-purakau.html' OR path LIKE '%digital-purakau.html';


-- Update metadata for: Adaptive Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Adaptive Pathways | Te Kete Ako')
WHERE path = 'public/lessons/experiences/adaptive-pathways.html' OR path LIKE '%adaptive-pathways.html';


-- Update metadata for: Virtual Marae | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Virtual Marae | Te Kete Ako')
WHERE path = 'public/lessons/experiences/virtual-marae.html' OR path LIKE '%virtual-marae.html';


-- Update metadata for: Lesson 1.5: Reclaiming the Narrative | Walker Unit
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.5: Reclaiming the Narrative | Walker Unit | Te Kete Ako')
WHERE path = 'public/lessons/walker/lesson-1-5-reclaiming-the-narrative.html' OR path LIKE '%lesson-1-5-reclaiming-the-narrative.html';


-- Update metadata for: Lesson 1.3: Years of Anger | Walker Unit | Te Kete
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.3: Years of Anger | Walker Unit | Te Kete Ako')
WHERE path = 'public/lessons/walker/lesson-1-3-years-of-anger.html' OR path LIKE '%lesson-1-3-years-of-anger.html';


-- Update metadata for: Lesson 1.1: Who was Ranginui Walker? | Walker Unit
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.1: Who was Ranginui Walker? | Walker Unit | Te Kete Ako')
WHERE path = 'public/lessons/walker/lesson-1-1-who-was-ranginui-walker.html' OR path LIKE '%lesson-1-1-who-was-ranginui-walker.html';


-- Update metadata for: Lesson 1.2: The Great Migration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.2: The Great Migration | Te Kete Ako')
WHERE path = 'public/lessons/walker/lesson-1-2-the-great-migration.html' OR path LIKE '%lesson-1-2-the-great-migration.html';


-- Update metadata for: Lesson 1.4: A Forum for Justice | Walker Unit | Te
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.4: A Forum for Justice | Walker Unit | Te Kete Ako')
WHERE path = 'public/lessons/walker/lesson-1-4-a-forum-for-justice.html' OR path LIKE '%lesson-1-4-a-forum-for-justice.html';


-- Update metadata for: {{page_title}} | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), '{{page_title}} | Te Kete Ako')
WHERE path = 'public/templates/professional-template.html' OR path LIKE '%professional-template.html';


-- Update metadata for: Standard Header
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Standard Header')
WHERE path = 'public/templates/standard-header.html' OR path LIKE '%standard-header.html';


-- Update metadata for: Standard Sidebar
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Standard Sidebar')
WHERE path = 'public/templates/standard-sidebar.html' OR path LIKE '%standard-sidebar.html';


-- Update metadata for: Dream Journal Activities | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Dream Journal Activities | Te Kete Ako')
WHERE path = 'public/activities/dream-journal-activities.html' OR path LIKE '%dream-journal-activities.html';


-- Update metadata for: Show and Tell Activities | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Show and Tell Activities | Te Kete Ako')
WHERE path = 'public/activities/show-and-tell-activities.html' OR path LIKE '%show-and-tell-activities.html';


-- Update metadata for: NZ Curriculum - Science | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum - Science | Te Kete Ako')
WHERE path = 'public/curriculum-documents/science.html' OR path LIKE '%science.html';


-- Update metadata for: NZ Curriculum - The Arts | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum - The Arts | Te Kete Ako')
WHERE path = 'public/curriculum-documents/arts.html' OR path LIKE '%arts.html';


-- Update metadata for: NZ Curriculum - Mathematics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum - Mathematics | Te Kete Ako')
WHERE path = 'public/curriculum-documents/mathematics.html' OR path LIKE '%mathematics.html';


-- Update metadata for: NZ Curriculum - Social Sciences | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum - Social Sciences | Te Kete Ako')
WHERE path = 'public/curriculum-documents/social-sciences.html' OR path LIKE '%social-sciences.html';


-- Update metadata for: NZ Curriculum - English | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum - English | Te Kete Ako')
WHERE path = 'public/curriculum-documents/english.html' OR path LIKE '%english.html';


-- Update metadata for: NZ Curriculum - Technology | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum - Technology | Te Kete Ako')
WHERE path = 'public/curriculum-documents/technology.html' OR path LIKE '%technology.html';


-- Update metadata for: NZ Curriculum - Health & Physical Education | Te K
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum - Health & Physical Education | Te Kete Ako')
WHERE path = 'public/curriculum-documents/health-pe.html' OR path LIKE '%health-pe.html';


-- Update metadata for: Te Reo Māori Spelling Bee | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Spelling Bee | Te Kete Ako')
WHERE path = 'public/games/spelling-bee.html' OR path LIKE '%spelling-bee.html';


-- Update metadata for: Te Reo Māori Wordle (Unlimited) | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Wordle (Unlimited) | Te Kete Ako')
WHERE path = 'public/games/te-reo-wordle-unlimited.html' OR path LIKE '%te-reo-wordle-unlimited.html';


-- Update metadata for: 🌺 Te Reo Māori Wordle | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), '🌺 Te Reo Māori Wordle | Te Kete Ako')
WHERE path = 'public/games/te-reo-wordle-august-legacy.html' OR path LIKE '%te-reo-wordle-august-legacy.html';


-- Update metadata for: English Wordle | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'English Wordle | Te Kete Ako')
WHERE path = 'public/games/english-wordle.html' OR path LIKE '%english-wordle.html';


-- Update metadata for: Tukutuku Pattern Explorer | Interactive Mathematic
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Tukutuku Pattern Explorer | Interactive Mathematics | Te Kete Ako')
WHERE path = 'public/games/tukutuku-pattern-explorer.html' OR path LIKE '%tukutuku-pattern-explorer.html';


-- Update metadata for: Te Reo Māori Wordle (6-Letter) | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Wordle (6-Letter) | Te Kete Ako')
WHERE path = 'public/games/te-reo-wordle-6.html' OR path LIKE '%te-reo-wordle-6.html';


-- Update metadata for: Te Reo Māori Wordle (Unlimited) | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Wordle (Unlimited) | Te Kete Ako')
WHERE path = 'public/games/te-reo-wordle.html' OR path LIKE '%te-reo-wordle.html';


-- Update metadata for: Te Reo Māori Wordle (6-Letter, Unlimited) | Te Ket
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Wordle (6-Letter, Unlimited) | Te Kete Ako')
WHERE path = 'public/games/te-reo-wordle-6-unlimited.html' OR path LIKE '%te-reo-wordle-6-unlimited.html';


-- Update metadata for: Countdown Letters: Te Reo Māori | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Countdown Letters: Te Reo Māori | Te Kete Ako')
WHERE path = 'public/games/countdown-letters.html' OR path LIKE '%countdown-letters.html';


-- Update metadata for: Categories Challenge | Te Kete Ako Games
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'game',
    title = COALESCE(NULLIF(title, ''), 'Categories Challenge | Te Kete Ako Games')
WHERE path = 'public/games/categories.html' OR path LIKE '%categories.html';


-- Update metadata for: Lesson 2: The Four Walls of our Digital Whare | Di
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: The Four Walls of our Digital Whare | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-2-four-walls.html' OR path LIKE '%lesson-2-four-walls.html';


-- Update metadata for: Te Kete Ako - EMERGENCY RECOVERY
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - EMERGENCY RECOVERY')
WHERE path = 'public/integrated-lessons/te reo māori/emergency-diagnostic.html' OR path LIKE '%emergency-diagnostic.html';


-- Update metadata for: Te Reo: Possessives - Mine, Yours, Ours | Te Kete 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo: Possessives - Mine, Yours, Ours | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-9.html' OR path LIKE '%lesson-9.html';


-- Update metadata for: Environmental Literacy Framework | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Environmental Literacy Framework | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/environmental-literacy-framework.html' OR path LIKE '%environmental-literacy-framework.html';


-- Update metadata for: Te Reo Māori Activities & Games | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Activities & Games | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/activities.html' OR path LIKE '%activities.html';


-- Update metadata for: Unit 4: Economic Justice & Rangatiratanga | Te Ket
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4: Economic Justice & Rangatiratanga | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/unit-4-economic-justice.html' OR path LIKE '%unit-4-economic-justice.html';


-- Update metadata for: Cultural Competency Assessment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Competency Assessment | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/cultural-assessment.html' OR path LIKE '%cultural-assessment.html';


-- Update metadata for: Te Reo: Pepeha - Introducing Your Connections | Te
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo: Pepeha - Introducing Your Connections | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-5.html' OR path LIKE '%lesson-5.html';


-- Update metadata for: Living Whakapapa: Genealogy & Identity | Te Kete A
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Living Whakapapa: Genealogy & Identity | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/living-whakapapa.html' OR path LIKE '%living-whakapapa.html';


-- Update metadata for: Professional Template
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Professional Template')
WHERE path = 'public/integrated-lessons/te reo māori/professional-template.html' OR path LIKE '%professional-template.html';


-- Update metadata for: AI Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Hub | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/ai-hub.html' OR path LIKE '%ai-hub.html';


-- Update metadata for: Printable: Council Services Cards
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Council Services Cards')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-3-1-council-services-cards.html' OR path LIKE '%lesson-3-1-council-services-cards.html';


-- Update metadata for: AI Ethics Through Māori Data Sovereignty | Digital
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics Through Māori Data Sovereignty | Digital Technology')
WHERE path = 'public/integrated-lessons/te reo māori/ai-ethics-through-māori-data-sovereignty.html' OR path LIKE '%ai-ethics-through-māori-data-sovereignty.html';


-- Update metadata for: Te Reo Lesson 4: Family Words | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Lesson 4: Family Words | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-4.html' OR path LIKE '%lesson-4.html';


-- Update metadata for: Learning Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Learning Pathways | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/learning-pathways.html' OR path LIKE '%learning-pathways.html';


-- Update metadata for: Introduction to Critical Thinking | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Introduction to Critical Thinking | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/critical-thinking-introduction.html' OR path LIKE '%critical-thinking-introduction.html';


-- Update metadata for: Printable: Campaign Plan Template
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Campaign Plan Template')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-3-2-campaign-plan-template.html' OR path LIKE '%lesson-3-2-campaign-plan-template.html';


-- Update metadata for: Mātauranga Māori Thinking Framework | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Mātauranga Māori Thinking Framework | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/matauranga-thinking-framework.html' OR path LIKE '%matauranga-thinking-framework.html';


-- Update metadata for: Marine Ecology & Tangaroa | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Marine Ecology & Tangaroa | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/marine-ecology-lesson.html' OR path LIKE '%marine-ecology-lesson.html';


-- Update metadata for: Te Reo: Review and Consolidation | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo: Review and Consolidation | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-10.html' OR path LIKE '%lesson-10.html';


-- Update metadata for: Design Thinking with Māori Values | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Design Thinking with Māori Values | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-design-thinking.html' OR path LIKE '%lesson-design-thinking.html';


-- Update metadata for: Systems Thinking Lessons 1-2 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Systems Thinking Lessons 1-2 | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/systems-lesson-1-2.html' OR path LIKE '%systems-lesson-1-2.html';


-- Update metadata for: Forgot Password | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Forgot Password | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/forgot-password.html' OR path LIKE '%forgot-password.html';


-- Update metadata for: Lesson 16: The Digital Kaitiaki Challenge | Digita
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 16: The Digital Kaitiaki Challenge | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-16-project-launch.html' OR path LIKE '%lesson-16-project-launch.html';


-- Update metadata for: Critical Communication Portfolio | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Critical Communication Portfolio | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/critical-communication-portfolio.html' OR path LIKE '%critical-communication-portfolio.html';


-- Update metadata for: About Te Kete Ako | Educational Resources Platform
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'About Te Kete Ako | Educational Resources Platform')
WHERE path = 'public/integrated-lessons/te reo māori/about.html' OR path LIKE '%about.html';


-- Update metadata for: Curriculum: Arts | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Arts | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/curriculum-arts.html' OR path LIKE '%curriculum-arts.html';


-- Update metadata for: Te Reo: Verbs and Actions | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo: Verbs and Actions | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-8.html' OR path LIKE '%lesson-8.html';


-- Update metadata for: Contact Te Kete Ako | Support & Feedback
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Contact Te Kete Ako | Support & Feedback')
WHERE path = 'public/integrated-lessons/te reo māori/contact.html' OR path LIKE '%contact.html';


-- Update metadata for: Printable: NZ Government Power Cards
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: NZ Government Power Cards')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-2-2-power-cards.html' OR path LIKE '%lesson-2-2-power-cards.html';


-- Update metadata for: Printable: Government Case Studies
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Government Case Studies')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-2-1-case-studies.html' OR path LIKE '%lesson-2-1-case-studies.html';


-- Update metadata for: Te Reo Lesson 3: Colors | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Lesson 3: Colors | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-3.html' OR path LIKE '%lesson-3.html';


-- Update metadata for: Platforms | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Platforms | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/platforms.html' OR path LIKE '%platforms.html';


-- Update metadata for: Lesson 3: Blueprint for a Healthy Whare | Digital 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Blueprint for a Healthy Whare | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-3-blueprint-for-a-healthy-whare.html' OR path LIKE '%lesson-3-blueprint-for-a-healthy-whare.html';


-- Update metadata for: Te Reo Assessment Rubrics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Assessment Rubrics | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/assessment-rubrics.html' OR path LIKE '%assessment-rubrics.html';


-- Update metadata for: Detecting Logical Fallacies | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Detecting Logical Fallacies | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/logical-fallacies-detection.html' OR path LIKE '%logical-fallacies-detection.html';


-- Update metadata for: Printable: Draw Your System Template
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Draw Your System Template')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-1-2-draw-your-system-template.html' OR path LIKE '%lesson-1-2-draw-your-system-template.html';


-- Update metadata for: Interactive Curriculum Browser | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Interactive Curriculum Browser | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/curriculum-v2.html' OR path LIKE '%curriculum-v2.html';


-- Update metadata for: Reset Password | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Reset Password | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/reset-password.html' OR path LIKE '%reset-password.html';


-- Update metadata for: Login | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Login | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/login.html' OR path LIKE '%login.html';


-- Update metadata for: Digital Storytelling & Multimedia | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Storytelling & Multimedia | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/digital-storytelling-lesson.html' OR path LIKE '%digital-storytelling-lesson.html';


-- Update metadata for: Printable: Whakapapa Exploration Template
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Whakapapa Exploration Template')
WHERE path = 'public/integrated-lessons/te reo māori/unit-1-lesson-1-whakapapa-template.html' OR path LIKE '%unit-1-lesson-1-whakapapa-template.html';


-- Update metadata for: Te Reo Lesson 2: Numbers 1-10 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Lesson 2: Numbers 1-10 | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-2.html' OR path LIKE '%lesson-2.html';


-- Update metadata for: Scientific Equipment Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Scientific Equipment Guide | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/scientific-equipment-guide.html' OR path LIKE '%scientific-equipment-guide.html';


-- Update metadata for: Printable: Decolonized Design Template
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Decolonized Design Template')
WHERE path = 'public/integrated-lessons/te reo māori/decolonized-design-template.html' OR path LIKE '%decolonized-design-template.html';


-- Update metadata for: Te Reo Lesson 1: Introduction to Māori Language | 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Lesson 1: Introduction to Māori Language | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-1.html' OR path LIKE '%lesson-1.html';


-- Update metadata for: Lesson 2: Food Chains & Food Webs (Y7)
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: Food Chains & Food Webs (Y7)')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-2-food-webs.html' OR path LIKE '%lesson-2-food-webs.html';


-- Update metadata for: Register | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Register | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/register-simple.html' OR path LIKE '%register-simple.html';


-- Update metadata for: Unit 2 Lesson 3: Basic Greetings & Farewells | Te 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 3: Basic Greetings & Farewells | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/unit-2-lesson-3.html' OR path LIKE '%unit-2-lesson-3.html';


-- Update metadata for: Cultural Knowledge Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Knowledge Resources | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/cultural-knowledge-resources.html' OR path LIKE '%cultural-knowledge-resources.html';


-- Update metadata for: Tino Rangatiratanga Arguments | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Tino Rangatiratanga Arguments | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/arguments-of-tino-rangatiratanga-handout.html' OR path LIKE '%arguments-of-tino-rangatiratanga-handout.html';


-- Update metadata for: Lesson 1: Kaitiakitanga & Local Ecosystems (Y7)
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Kaitiakitanga & Local Ecosystems (Y7)')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-1-kaitiakitanga-intro.html' OR path LIKE '%lesson-1-kaitiakitanga-intro.html';


-- Update metadata for: Political Cartoon Analysis | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Political Cartoon Analysis | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/political-cartoon-analysis-handout.html' OR path LIKE '%political-cartoon-analysis-handout.html';


-- Update metadata for: Digital Pūrākau - Digital Storytelling | Te Kete A
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Pūrākau - Digital Storytelling | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/digital-purakau.html' OR path LIKE '%digital-purakau.html';


-- Update metadata for: NZ Curriculum Alignment Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum Alignment Guide | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/curriculum-alignment.html' OR path LIKE '%curriculum-alignment.html';


-- Update metadata for: Dream Journal & Reflection Activities | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Dream Journal & Reflection Activities | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/dream-journal-activities.html' OR path LIKE '%dream-journal-activities.html';


-- Update metadata for: Sustainable Technology & Kaitiakitanga | Te Kete A
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Sustainable Technology & Kaitiakitanga | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-sustainable-technology.html' OR path LIKE '%lesson-sustainable-technology.html';


-- Update metadata for: Engineering Design with Mātauranga Māori | Te Kete
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Engineering Design with Mātauranga Māori | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/engineering-design-lesson.html' OR path LIKE '%engineering-design-lesson.html';


-- Update metadata for: Environmental Text Analysis | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Environmental Text Analysis | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/environmental-text-analysis-handout.html' OR path LIKE '%environmental-text-analysis-handout.html';


-- Update metadata for: Curriculum: Technology | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Technology | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/curriculum-technology.html' OR path LIKE '%curriculum-technology.html';


-- Update metadata for: Critical Thinking Toolkit | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Critical Thinking Toolkit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/critical-thinking-toolkit.html' OR path LIKE '%critical-thinking-toolkit.html';


-- Update metadata for: Classroom Leaderboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Classroom Leaderboard | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/classroom-leaderboard.html' OR path LIKE '%classroom-leaderboard.html';


-- Update metadata for: Unit 2 Lesson 5: Mihimihi - Formal Introductions |
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 5: Mihimihi - Formal Introductions | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/unit-2-lesson-5.html' OR path LIKE '%unit-2-lesson-5.html';


-- Update metadata for: Adaptive Learning Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Adaptive Learning Pathways | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/adaptive-pathways.html' OR path LIKE '%adaptive-pathways.html';


-- Update metadata for: Authentication Diagnostics | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Authentication Diagnostics | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/auth-diagnostics.html' OR path LIKE '%auth-diagnostics.html';


-- Update metadata for: Curriculum: Health & PE | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Health & PE | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/curriculum-health-pe.html' OR path LIKE '%curriculum-health-pe.html';


-- Update metadata for: RNZ News Analysis Framework | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'RNZ News Analysis Framework | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/rnz-analysis-framework.html' OR path LIKE '%rnz-analysis-framework.html';


-- Update metadata for: Lesson 7: Food and Kai | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 7: Food and Kai | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-7.html' OR path LIKE '%lesson-7.html';


-- Update metadata for: My Learning Kete - Personal Portfolio | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Learning Kete - Personal Portfolio | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/my-kete.html' OR path LIKE '%my-kete.html';


-- Update metadata for: Evidence Evaluation Frameworks | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Evidence Evaluation Frameworks | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/evidence-evaluation-frameworks.html' OR path LIKE '%evidence-evaluation-frameworks.html';


-- Update metadata for: Source Evaluation Matrix | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Source Evaluation Matrix | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/source-evaluation-matrix.html' OR path LIKE '%source-evaluation-matrix.html';


-- Update metadata for: Indigenous Learning Systems | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Indigenous Learning Systems | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/indigenous-learning-systems.html' OR path LIKE '%indigenous-learning-systems.html';


-- Update metadata for: Show and Tell in Te Reo | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Show and Tell in Te Reo | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/show-and-tell-activities.html' OR path LIKE '%show-and-tell-activities.html';


-- Update metadata for: Experiences | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Experiences | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/experiences.html' OR path LIKE '%experiences.html';


-- Update metadata for: Energy & Sustainability with Kaitiakitanga | Te Ke
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Energy & Sustainability with Kaitiakitanga | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/energy-sustainability-lesson.html' OR path LIKE '%energy-sustainability-lesson.html';


-- Update metadata for: Curriculum: Languages | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Curriculum: Languages | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/curriculum-languages.html' OR path LIKE '%curriculum-languages.html';


-- Update metadata for: Lesson 1: What is an Ecosystem?
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: What is an Ecosystem?')
WHERE path = 'public/integrated-lessons/te reo māori/lesson-1-what-is-an-ecosystem.html' OR path LIKE '%lesson-1-what-is-an-ecosystem.html';


-- Update metadata for: Virtual Marae Experience | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Virtual Marae Experience | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/virtual-marae.html' OR path LIKE '%virtual-marae.html';


-- Update metadata for: Environmental Monitoring: Kaitiakitanga in Action 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Environmental Monitoring: Kaitiakitanga in Action | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/environmental-monitoring-lesson.html' OR path LIKE '%environmental-monitoring-lesson.html';


-- Update metadata for: Te Reo Project Brief | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Project Brief | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/project-brief.html' OR path LIKE '%project-brief.html';


-- Update metadata for: Unit 2 Lesson 4: Pepeha - Introducing Yourself wit
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 4: Pepeha - Introducing Yourself with Place | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/unit-2-lesson-4.html' OR path LIKE '%unit-2-lesson-4.html';


-- Update metadata for: Te Reo Māori Lessons Index | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Māori Lessons Index | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/lessons.html' OR path LIKE '%lessons.html';


-- Update metadata for: Unit 5 Lesson 5: Whakamutunga - Conclusion | Te Ke
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 5 Lesson 5: Whakamutunga - Conclusion | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/unit-5-lesson-5.html' OR path LIKE '%unit-5-lesson-5.html';


-- Update metadata for: Printable: Mātauranga Māori Inquiry Cards
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Mātauranga Māori Inquiry Cards')
WHERE path = 'public/integrated-lessons/te reo māori/unit-1-lesson-3-matauranga-inquiry-cards.html' OR path LIKE '%unit-1-lesson-3-matauranga-inquiry-cards.html';


-- Update metadata for: Statistical Storytelling: Data Meets Pūrākau | Te 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Statistical Storytelling: Data Meets Pūrākau | Te Kete Ako')
WHERE path = 'public/integrated-lessons/te reo māori/statistical-storytelling-lesson.html' OR path LIKE '%statistical-storytelling-lesson.html';


-- Update metadata for: Register | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Register | Te Kete Ako')
WHERE path = 'public/integrated-lessons/technology/register.html' OR path LIKE '%register.html';


-- Update metadata for: Resource Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Resource Hub | Te Kete Ako')
WHERE path = 'public/integrated-lessons/technology/resource-hub.html' OR path LIKE '%resource-hub.html';


-- Update metadata for: Navigation Fix Standard Header
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Navigation Fix Standard Header')
WHERE path = 'public/integrated-lessons/technology/navigation_fix_standard_header.html' OR path LIKE '%navigation_fix_standard_header.html';


-- Update metadata for: Navigation Fix Standard Header
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Navigation Fix Standard Header')
WHERE path = 'public/integrated-lessons/general/navigation_fix_standard_header.html' OR path LIKE '%navigation_fix_standard_header.html';


-- Update metadata for: Critical Thinking Introduction | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Critical Thinking Introduction | Te Kete Ako')
WHERE path = 'public/integrated-lessons/health/critical-thinking-introduction.html' OR path LIKE '%critical-thinking-introduction.html';


-- Update metadata for: Register | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Register | Te Kete Ako')
WHERE path = 'public/integrated-lessons/health/register.html' OR path LIKE '%register.html';


-- Update metadata for: Lesson 1 | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1 | Te Kete Ako')
WHERE path = 'public/integrated-lessons/health/lesson-1.html' OR path LIKE '%lesson-1.html';


-- Update metadata for: Register | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Register | Te Kete Ako')
WHERE path = 'public/integrated-lessons/health/register-simple.html' OR path LIKE '%register-simple.html';


-- Update metadata for: Show and Tell Activities | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Show and Tell Activities | Te Kete Ako')
WHERE path = 'public/integrated-lessons/health/show-and-tell-activities.html' OR path LIKE '%show-and-tell-activities.html';


-- Update metadata for: Project Brief | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Project Brief | Te Kete Ako')
WHERE path = 'public/integrated-lessons/health/project-brief.html' OR path LIKE '%project-brief.html';


-- Update metadata for: Writers Toolkit Implementation Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Writers Toolkit Implementation Guide | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/writers-toolkit-implementation-guide.html' OR path LIKE '%writers-toolkit-implementation-guide.html';


-- Update metadata for: Lesson 17: Creation & Collaboration Workshop | Dig
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 17: Creation & Collaboration Workshop | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/lesson-17-creation-workshop.html' OR path LIKE '%lesson-17-creation-workshop.html';


-- Update metadata for: Y8 Systems | Lesson 5.2: Present & Reflect
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Y8 Systems | Lesson 5.2: Present & Reflect')
WHERE path = 'public/integrated-lessons/science/lesson-5-2.html' OR path LIKE '%lesson-5-2.html';


-- Update metadata for: Lesson 18: The Whare Warming Showcase | Digital Ka
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 18: The Whare Warming Showcase | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/lesson-18-digital-showcase.html' OR path LIKE '%lesson-18-digital-showcase.html';


-- Update metadata for: Lesson 1.3: Years of Anger | Walker Unit | Te Kete
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.3: Years of Anger | Walker Unit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-1-3-years-of-anger.html' OR path LIKE '%lesson-1-3-years-of-anger.html';


-- Update metadata for: Lesson 1: Society Exploration | Guided Inquiry Uni
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Society Exploration | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-1-society-exploration.html' OR path LIKE '%lesson-1-society-exploration.html';


-- Update metadata for: Unit 4, Lesson 5: Community Science Projects
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4, Lesson 5: Community Science Projects')
WHERE path = 'public/integrated-lessons/science/unit-4-lesson-5.html' OR path LIKE '%unit-4-lesson-5.html';


-- Update metadata for: Printable: Indigenous Feedback Framework
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Feedback Framework')
WHERE path = 'public/integrated-lessons/science/indigenous-feedback-framework.html' OR path LIKE '%indigenous-feedback-framework.html';


-- Update metadata for: Rongoā Māori: Traditional Medicine & Modern Scienc
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Rongoā Māori: Traditional Medicine & Modern Science | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/rongoa-science-lesson.html' OR path LIKE '%rongoa-science-lesson.html';


-- Update metadata for: Unit 3 Lesson 4: Technology & Innovation | Mangakō
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 3 Lesson 4: Technology & Innovation | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/science/unit-3-lesson-4.html' OR path LIKE '%unit-3-lesson-4.html';


-- Update metadata for: Lesson 4: The Body as a Sensor | Digital Kaitiakit
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: The Body as a Sensor | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/lesson-4-body-as-sensor.html' OR path LIKE '%lesson-4-body-as-sensor.html';


-- Update metadata for: Lesson 6: Evaluating Arguments
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6: Evaluating Arguments')
WHERE path = 'public/integrated-lessons/science/lesson-6-evaluating-arguments.html' OR path LIKE '%lesson-6-evaluating-arguments.html';


-- Update metadata for: Lesson Plan: The Revision Process | Writer's Toolk
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: The Revision Process | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/science/revision-lesson-plan.html' OR path LIKE '%revision-lesson-plan.html';


-- Update metadata for: Lesson Plan: Informative Structures | Writer's Too
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Informative Structures | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/science/inform-structure-lesson-plan.html' OR path LIKE '%inform-structure-lesson-plan.html';


-- Update metadata for: The Writer's Toolkit: The Revision Process
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: The Revision Process')
WHERE path = 'public/integrated-lessons/science/writers-toolkit-revision-handout.html' OR path LIKE '%writers-toolkit-revision-handout.html';


-- Update metadata for: Lesson Plan: Crafting Hooks | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Crafting Hooks | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/science/hook-lesson-plan.html' OR path LIKE '%hook-lesson-plan.html';


-- Update metadata for: Lesson 1.1: Who was Ranginui Walker? | Walker Unit
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.1: Who was Ranginui Walker? | Walker Unit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-1-1-who-was-ranginui-walker.html' OR path LIKE '%lesson-1-1-who-was-ranginui-walker.html';


-- Update metadata for: AI Ethics Through Māori Data Sovereignty
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics Through Māori Data Sovereignty')
WHERE path = 'public/integrated-lessons/science/ai-ethics-through-māori-data-sovereignty.html' OR path LIKE '%ai-ethics-through-māori-data-sovereignty.html';


-- Update metadata for: Printable: Indigenous Systems Examples
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Systems Examples')
WHERE path = 'public/integrated-lessons/science/indigenous-systems-examples.html' OR path LIKE '%indigenous-systems-examples.html';


-- Update metadata for: Lesson 4: Rights & Economy Integration | Guided In
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: Rights & Economy Integration | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-4-rights-economy.html' OR path LIKE '%lesson-4-rights-economy.html';


-- Update metadata for: Lesson 2: Group Formation & Research Planning | Gu
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: Group Formation & Research Planning | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-2-group-formation.html' OR path LIKE '%lesson-2-group-formation.html';


-- Update metadata for: Unit 4, Lesson 4: Technology & Innovation
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4, Lesson 4: Technology & Innovation')
WHERE path = 'public/integrated-lessons/science/unit-4-lesson-4.html' OR path LIKE '%unit-4-lesson-4.html';


-- Update metadata for: Printable: Living Tiriti Examples
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Living Tiriti Examples')
WHERE path = 'public/integrated-lessons/science/living-tiriti-examples.html' OR path LIKE '%living-tiriti-examples.html';


-- Update metadata for: The Writer's Toolkit: Word Choice (Diction)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Word Choice (Diction)')
WHERE path = 'public/integrated-lessons/science/writers-toolkit-diction-handout.html' OR path LIKE '%writers-toolkit-diction-handout.html';


-- Update metadata for: Lesson Plan: Tone & Voice | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Tone & Voice | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/science/tone-lesson-plan.html' OR path LIKE '%tone-lesson-plan.html';


-- Update metadata for: Station Rotation Templates | Writers Toolkit | Te 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Station Rotation Templates | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/station-rotation-templates.html' OR path LIKE '%station-rotation-templates.html';


-- Update metadata for: Lesson 6: Designing for Well-being | Digital Kaiti
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6: Designing for Well-being | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/lesson-6-designing-for-well-being.html' OR path LIKE '%lesson-6-designing-for-well-being.html';


-- Update metadata for: Climate Change & Te Taiao: Interactive Science Les
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Climate Change & Te Taiao: Interactive Science Lesson | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/climate-science-lesson.html' OR path LIKE '%climate-science-lesson.html';


-- Update metadata for: Unit 1 Lesson 3: Democracy vs. Dictatorship | Y8 S
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 3: Democracy vs. Dictatorship | Y8 Systems | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-2-1.html' OR path LIKE '%lesson-2-1.html';


-- Update metadata for: Lesson Plan: Sentence Fluency | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Sentence Fluency | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/science/fluency-lesson-plan.html' OR path LIKE '%fluency-lesson-plan.html';


-- Update metadata for: Podcast Lesson 1: Te Tiriti o Waitangi | Te Kete A
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Podcast Lesson 1: Te Tiriti o Waitangi | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-1-treaty-of-waitangi.html' OR path LIKE '%lesson-1-treaty-of-waitangi.html';


-- Update metadata for: Te Kete Ako - Lesson 3: Source Evaluation & Fact-C
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Lesson 3: Source Evaluation & Fact-Checking')
WHERE path = 'public/integrated-lessons/science/lesson-3.html' OR path LIKE '%lesson-3.html';


-- Update metadata for: Unit 7 Lesson 2: AI Bias & Algorithmic Justice | T
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 7 Lesson 2: AI Bias & Algorithmic Justice | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/unit-7-lesson-2.html' OR path LIKE '%unit-7-lesson-2.html';


-- Update metadata for: NZ History Investigation Toolkit | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ History Investigation Toolkit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/nzhistory-investigation-toolkit.html' OR path LIKE '%nzhistory-investigation-toolkit.html';


-- Update metadata for: Unit 6 Lesson 1: Visioning Rangatiratanga 2050 | T
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 6 Lesson 1: Visioning Rangatiratanga 2050 | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/unit-6-lesson-1.html' OR path LIKE '%unit-6-lesson-1.html';


-- Update metadata for: Unit 1 Lesson 6: How to Make Your Voice Heard | Y8
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 6: How to Make Your Voice Heard | Y8 Systems | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-3-2.html' OR path LIKE '%lesson-3-2.html';


-- Update metadata for: Career Pathways in STEM for Māori Students
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Career Pathways in STEM for Māori Students')
WHERE path = 'public/integrated-lessons/science/career-pathways-in-stem-for-māori-students.html' OR path LIKE '%career-pathways-in-stem-for-māori-students.html';


-- Update metadata for: Lesson 1: Pre-Colonial Innovation | Unit 2: Decolo
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Pre-Colonial Innovation | Unit 2: Decolonized History | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/unit-2-lesson-1.html' OR path LIKE '%unit-2-lesson-1.html';


-- Update metadata for: Lesson 3: Government Systems Design | Guided Inqui
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Government Systems Design | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-3-government-systems.html' OR path LIKE '%lesson-3-government-systems.html';


-- Update metadata for: Printable: Traditional Māori Governance Systems
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Traditional Māori Governance Systems')
WHERE path = 'public/integrated-lessons/science/maori-governance-systems.html' OR path LIKE '%maori-governance-systems.html';


-- Update metadata for: Years of Anger: The Protest Movements | Te Kete Ak
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Years of Anger: The Protest Movements | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/walker-lesson-1.3-years-of-anger.html' OR path LIKE '%walker-lesson-1.3-years-of-anger.html';


-- Update metadata for: Lesson: Whakatā Roro - Brain Break | Mangakōtukutu
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson: Whakatā Roro - Brain Break | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/science/brain-break-wordsearch-lesson.html' OR path LIKE '%brain-break-wordsearch-lesson.html';


-- Update metadata for: Unit 2 Lesson 1: The Treaty & Co-Governance | Y8 S
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 1: The Treaty & Co-Governance | Y8 Systems | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-4-1.html' OR path LIKE '%lesson-4-1.html';


-- Update metadata for: Unit 5 Lesson 1: Indigenous Worldviews - Shared Va
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 5 Lesson 1: Indigenous Worldviews - Shared Values, Diverse Expressions | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/science/unit-5-lesson-1.html' OR path LIKE '%unit-5-lesson-1.html';


-- Update metadata for: Unit 1 Lesson 2: Systems Are Everywhere | Y8 Syste
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 2: Systems Are Everywhere | Y8 Systems | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-1-2.html' OR path LIKE '%lesson-1-2.html';


-- Update metadata for: Lesson 1.2: The Great Migration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.2: The Great Migration | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-1-2-the-great-migration.html' OR path LIKE '%lesson-1-2-the-great-migration.html';


-- Update metadata for: Printable: Colonization Timeline
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Colonization Timeline')
WHERE path = 'public/integrated-lessons/science/colonization-timeline.html' OR path LIKE '%colonization-timeline.html';


-- Update metadata for: Lesson 7: Words as Taonga | Digital Kaitiakitanga
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 7: Words as Taonga | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/lesson-7-words-as-taonga.html' OR path LIKE '%lesson-7-words-as-taonga.html';


-- Update metadata for: Lesson 13: Reclaiming Your Mauri | Digital Kaitiak
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 13: Reclaiming Your Mauri | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/lesson-13-reclaiming-your-mauri.html' OR path LIKE '%lesson-13-reclaiming-your-mauri.html';


-- Update metadata for: The Skate Park Campaign - Systems Thinking Case St
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Skate Park Campaign - Systems Thinking Case Study | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/skate-park-campaign.html' OR path LIKE '%skate-park-campaign.html';


-- Update metadata for: Lesson 8: Critical Thinking Challenge
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 8: Critical Thinking Challenge')
WHERE path = 'public/integrated-lessons/science/lesson-8-critical-thinking-challenge.html' OR path LIKE '%lesson-8-critical-thinking-challenge.html';


-- Update metadata for: AI Ethics Through Māori Data Sovereignty | Te Kete
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics Through Māori Data Sovereignty | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/ai-ethics-through-māori-data-sovereignty-FIXED.html' OR path LIKE '%ai-ethics-through-māori-data-sovereignty-FIXED.html';


-- Update metadata for: The Writer's Toolkit: Analogy & Metaphor | Mangakō
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Analogy & Metaphor | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/science/writers-toolkit-analogy-handout.html' OR path LIKE '%writers-toolkit-analogy-handout.html';


-- Update metadata for: Lesson 5: The Science of Screen Time | Digital Kai
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5: The Science of Screen Time | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/lesson-5-science-of-screen-time.html' OR path LIKE '%lesson-5-science-of-screen-time.html';


-- Update metadata for: Lesson 1: Te Whenua Tāhiko - Our Digital Whenua | 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Te Whenua Tāhiko - Our Digital Whenua | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/lesson-1-what-is-our-digital-whenua.html' OR path LIKE '%lesson-1-what-is-our-digital-whenua.html';


-- Update metadata for: Narrative Writing Using Māori Story Structures
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Narrative Writing Using Māori Story Structures')
WHERE path = 'public/integrated-lessons/science/narrative-writing-using-māori-story-structures.html' OR path LIKE '%narrative-writing-using-māori-story-structures.html';


-- Update metadata for: Unit 4, Lesson 2: Environmental Science & Kaitiaki
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4, Lesson 2: Environmental Science & Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/unit-4-lesson-2.html' OR path LIKE '%unit-4-lesson-2.html';


-- Update metadata for: Research Skills: Traditional and Digital Sources
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Research Skills: Traditional and Digital Sources')
WHERE path = 'public/integrated-lessons/science/research-skills-using-traditional-and-digital-sources.html' OR path LIKE '%research-skills-using-traditional-and-digital-sources.html';


-- Update metadata for: Creative Writing Inspired by Whakataukī
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Creative Writing Inspired by Whakataukī')
WHERE path = 'public/integrated-lessons/science/creative-writing-inspired-by-whakataukī.html' OR path LIKE '%creative-writing-inspired-by-whakataukī.html';


-- Update metadata for: The Writer's Toolkit: Formal vs. Informal Tone
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Formal vs. Informal Tone')
WHERE path = 'public/integrated-lessons/science/writers-toolkit-tone-handout.html' OR path LIKE '%writers-toolkit-tone-handout.html';


-- Update metadata for: Debate Skills with Māori Oratory Traditions
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Debate Skills with Māori Oratory Traditions')
WHERE path = 'public/integrated-lessons/science/debate-skills-with-māori-oratory-traditions.html' OR path LIKE '%debate-skills-with-māori-oratory-traditions.html';


-- Update metadata for: Who was Ranginui Walker? | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Who was Ranginui Walker? | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/walker-lesson-1.1-who-was-ranginui-walker.html' OR path LIKE '%walker-lesson-1.1-who-was-ranginui-walker.html';


-- Update metadata for: Unit 2 Lesson 2: Colonisation & Its Impacts | Y8 S
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 2: Colonisation & Its Impacts | Y8 Systems | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-4-2.html' OR path LIKE '%lesson-4-2.html';


-- Update metadata for: Lesson Plan: Word Choice (Diction) | Writer's Tool
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Word Choice (Diction) | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/science/diction-lesson-plan.html' OR path LIKE '%diction-lesson-plan.html';


-- Update metadata for: Unit 5 Lesson 2: Colonialism as Global System - Pa
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 5 Lesson 2: Colonialism as Global System - Patterns of Extraction and Control | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/unit-5-lesson-2.html' OR path LIKE '%unit-5-lesson-2.html';


-- Update metadata for: The Writer's Toolkit: Powerful Conclusions
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Powerful Conclusions')
WHERE path = 'public/integrated-lessons/science/writers-toolkit-conclusion-handout.html' OR path LIKE '%writers-toolkit-conclusion-handout.html';


-- Update metadata for: Unit 2, Lesson 3: The Fight for Rights
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 3: The Fight for Rights')
WHERE path = 'public/integrated-lessons/science/unit-2-lesson-3.html' OR path LIKE '%unit-2-lesson-3.html';


-- Update metadata for: Unit 1 Lesson 1: What Makes a Society? | Y8 System
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 1: What Makes a Society? | Y8 Systems | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-1-1.html' OR path LIKE '%lesson-1-1.html';


-- Update metadata for: Lesson 5: Asking the Right Questions
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5: Asking the Right Questions')
WHERE path = 'public/integrated-lessons/science/lesson-5-asking-right-questions.html' OR path LIKE '%lesson-5-asking-right-questions.html';


-- Update metadata for: Printable: Gallery Walk Statements
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Gallery Walk Statements')
WHERE path = 'public/integrated-lessons/science/gallery-walk-statements.html' OR path LIKE '%gallery-walk-statements.html';


-- Update metadata for: The Writer's Toolkit: Crafting Hooks
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Crafting Hooks')
WHERE path = 'public/integrated-lessons/science/writers-toolkit-hook-handout.html' OR path LIKE '%writers-toolkit-hook-handout.html';


-- Update metadata for: Podcast Worksheet: Te Tiriti o Waitangi | Te Kete 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Podcast Worksheet: Te Tiriti o Waitangi | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/worksheet-treaty-of-waitangi-podcast.html' OR path LIKE '%worksheet-treaty-of-waitangi-podcast.html';


-- Update metadata for: Lesson 1: Introduction to Critical Thinking
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Introduction to Critical Thinking')
WHERE path = 'public/integrated-lessons/science/lesson-1-introduction.html' OR path LIKE '%lesson-1-introduction.html';


-- Update metadata for: Lesson Plan: Building Suspense | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Building Suspense | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/science/suspense-lesson-plan.html' OR path LIKE '%suspense-lesson-plan.html';


-- Update metadata for: Unit 6 Lesson 3: Digital Sovereignty & Youth Voice
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 6 Lesson 3: Digital Sovereignty & Youth Voice | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/unit-6-lesson-3.html' OR path LIKE '%unit-6-lesson-3.html';


-- Update metadata for: The Writer's Toolkit: Suspense & Foreshadowing
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Suspense & Foreshadowing')
WHERE path = 'public/integrated-lessons/science/writers-toolkit-suspense-handout.html' OR path LIKE '%writers-toolkit-suspense-handout.html';


-- Update metadata for: Unit 1 Lesson 5: How Local Government Works | Y8 S
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 5: How Local Government Works | Y8 Systems | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-3-1.html' OR path LIKE '%lesson-3-1.html';


-- Update metadata for: Lesson Plan: The Power of Analogy | Writer's Toolk
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: The Power of Analogy | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/science/analogy-lesson-plan.html' OR path LIKE '%analogy-lesson-plan.html';


-- Update metadata for: Critical Analysis of Historical Documents
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Critical Analysis of Historical Documents')
WHERE path = 'public/integrated-lessons/science/critical-analysis-of-historical-documents.html' OR path LIKE '%critical-analysis-of-historical-documents.html';


-- Update metadata for: Printable: Indigenous Governance Principles
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Indigenous Governance Principles')
WHERE path = 'public/integrated-lessons/science/indigenous-governance-principles.html' OR path LIKE '%indigenous-governance-principles.html';


-- Update metadata for: Traditional Navigation & Modern GPS Integration
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Traditional Navigation & Modern GPS Integration')
WHERE path = 'public/integrated-lessons/science/traditional-navigation-and-modern-gps-integration.html' OR path LIKE '%traditional-navigation-and-modern-gps-integration.html';


-- Update metadata for: Unit 1 Lesson 3: Haka & Cultural Expression - Voic
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 3: Haka & Cultural Expression - Voice, Power & Identity | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/science/unit-1-lesson-3.html' OR path LIKE '%unit-1-lesson-3.html';


-- Update metadata for: Lesson: Oropuare - Vowel Sounds | Mangakōtukutuku 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson: Oropuare - Vowel Sounds | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/science/vowel-sounds-lesson.html' OR path LIKE '%vowel-sounds-lesson.html';


-- Update metadata for: Genetics and Whakapapa
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Genetics and Whakapapa')
WHERE path = 'public/integrated-lessons/science/genetics-and-whakapapa-scientific-and-cultural-perspectives.html' OR path LIKE '%genetics-and-whakapapa-scientific-and-cultural-perspectives.html';


-- Update metadata for: Printable: Government Station Cards
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Government Station Cards')
WHERE path = 'public/integrated-lessons/science/government-station-cards.html' OR path LIKE '%government-station-cards.html';


-- Update metadata for: Unit 2, Lesson 2: The Aotearoa Wars
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 2: The Aotearoa Wars')
WHERE path = 'public/integrated-lessons/science/unit-2-lesson-2.html' OR path LIKE '%unit-2-lesson-2.html';


-- Update metadata for: Unit 5 Lesson 3: Resistance Networks - Global Indi
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 5 Lesson 3: Resistance Networks - Global Indigenous Movements | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/unit-5-lesson-3.html' OR path LIKE '%unit-5-lesson-3.html';


-- Update metadata for: Systems Lesson 5.1: Design Challenge Launch | Te K
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Systems Lesson 5.1: Design Challenge Launch | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/systems-lesson-5-1.html' OR path LIKE '%systems-lesson-5-1.html';


-- Update metadata for: Lesson Plan: Powerful Conclusions | Writer's Toolk
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Powerful Conclusions | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/science/conclusion-lesson-plan.html' OR path LIKE '%conclusion-lesson-plan.html';


-- Update metadata for: Renewable Energy and Māori Innovation
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Renewable Energy and Māori Innovation')
WHERE path = 'public/integrated-lessons/science/renewable-energy-and-māori-innovation.html' OR path LIKE '%renewable-energy-and-māori-innovation.html';


-- Update metadata for: Printable: Decolonization Commitment Template
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Decolonization Commitment Template')
WHERE path = 'public/integrated-lessons/science/decolonization-commitment-template.html' OR path LIKE '%decolonization-commitment-template.html';


-- Update metadata for: Unit 2, Lesson 5: The Path to Redress
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 5: The Path to Redress')
WHERE path = 'public/integrated-lessons/science/unit-2-lesson-5.html' OR path LIKE '%unit-2-lesson-5.html';


-- Update metadata for: Adaptive Learning Pathways | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Adaptive Learning Pathways | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/adaptive-pathways.html' OR path LIKE '%adaptive-pathways.html';


-- Update metadata for: Unit 1 Lesson 4: Te Tiriti o Waitangi - Partnershi
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 4: Te Tiriti o Waitangi - Partnership & Power-Sharing | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/science/unit-1-lesson-4.html' OR path LIKE '%unit-1-lesson-4.html';


-- Update metadata for: Unit 1 Lesson 4: How New Zealand is Governed | Y8 
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 4: How New Zealand is Governed | Y8 Systems | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-2-2.html' OR path LIKE '%lesson-2-2.html';


-- Update metadata for: Creative Problem Solving with Design Thinking
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Creative Problem Solving with Design Thinking')
WHERE path = 'public/integrated-lessons/science/creative-problem-solving-with-design-thinking.html' OR path LIKE '%creative-problem-solving-with-design-thinking.html';


-- Update metadata for: Unit 6 Lesson 5: Collective Action Project Launch 
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 6 Lesson 5: Collective Action Project Launch | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/unit-6-lesson-5.html' OR path LIKE '%unit-6-lesson-5.html';


-- Update metadata for: Climate Change Through Te Taiao Māori Lens - Te Ke
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Climate Change Through Te Taiao Māori Lens - Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/climate-change-through-te-taiao-māori-lens.html' OR path LIKE '%climate-change-through-te-taiao-māori-lens.html';


-- Update metadata for: Printable: Design a System Template
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Design a System Template')
WHERE path = 'public/integrated-lessons/science/design-a-system-template.html' OR path LIKE '%design-a-system-template.html';


-- Update metadata for: Digital Storytelling with Pūrākau Framework
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Storytelling with Pūrākau Framework')
WHERE path = 'public/integrated-lessons/science/digital-storytelling-with-pūrākau-framework.html' OR path LIKE '%digital-storytelling-with-pūrākau-framework.html';


-- Update metadata for: Lesson 3: Human Impacts & Kaitiaki Action (Y7)
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Human Impacts & Kaitiaki Action (Y7)')
WHERE path = 'public/integrated-lessons/science/lesson-3-human-impacts.html' OR path LIKE '%lesson-3-human-impacts.html';


-- Update metadata for: The Writer's Toolkit: Sentence Fluency | Mangakōtu
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Sentence Fluency | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/science/writers-toolkit-fluency-handout.html' OR path LIKE '%writers-toolkit-fluency-handout.html';


-- Update metadata for: Scientific Method Using Traditional Māori Practice
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Scientific Method Using Traditional Māori Practices')
WHERE path = 'public/integrated-lessons/science/scientific-method-using-traditional-māori-practices.html' OR path LIKE '%scientific-method-using-traditional-māori-practices.html';


-- Update metadata for: Printable: Simplified Treaty Articles
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Simplified Treaty Articles')
WHERE path = 'public/integrated-lessons/science/treaty-articles.html' OR path LIKE '%treaty-articles.html';


-- Update metadata for: The Writer's Toolkit: Informational Structures | M
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Informational Structures | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/science/writers-toolkit-inform-structure-handout.html' OR path LIKE '%writers-toolkit-inform-structure-handout.html';


-- Update metadata for: Lesson 5: Culture & Systems Integration | Guided I
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5: Culture & Systems Integration | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-5-culture-integration.html' OR path LIKE '%lesson-5-culture-integration.html';


-- Update metadata for: Printable Resource: System Sorting Cards
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable Resource: System Sorting Cards')
WHERE path = 'public/integrated-lessons/science/system-sorting-cards.html' OR path LIKE '%system-sorting-cards.html';


-- Update metadata for: Resource: Frayer Model for "System" | Y8 Systems |
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Resource: Frayer Model for "System" | Y8 Systems | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/frayer-model-system.html' OR path LIKE '%frayer-model-system.html';


-- Update metadata for: Who Has the REAL Power? - NZ Government
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Who Has the REAL Power? - NZ Government')
WHERE path = 'public/integrated-lessons/science/who-has-the-real-power-interactive.html' OR path LIKE '%who-has-the-real-power-interactive.html';


-- Update metadata for: Unit 6 Lesson 4: Community Leadership in Action | 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 6 Lesson 4: Community Leadership in Action | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/unit-6-lesson-4.html' OR path LIKE '%unit-6-lesson-4.html';


-- Update metadata for: Lesson 12: Our Community's Tikanga | Digital Kaiti
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 12: Our Community''s Tikanga | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/lesson-12-digital-tikanga.html' OR path LIKE '%lesson-12-digital-tikanga.html';


-- Update metadata for: Unit 1 Lesson 5: Traditional Arts & Storytelling -
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 5: Traditional Arts & Storytelling - Preserving Knowledge Through Creativity | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/science/unit-1-lesson-5.html' OR path LIKE '%unit-1-lesson-5.html';


-- Update metadata for: Y8 Systems | Lesson 5.1: Guided Inquiry Project La
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Y8 Systems | Lesson 5.1: Guided Inquiry Project Launch - Design Your Society')
WHERE path = 'public/integrated-lessons/science/lesson-5-1.html' OR path LIKE '%lesson-5-1.html';


-- Update metadata for: Lesson 11: The Ripple Effect - Our Digital Whakapa
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 11: The Ripple Effect - Our Digital Whakapapa | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/lesson-11-the-ripple-effect.html' OR path LIKE '%lesson-11-the-ripple-effect.html';


-- Update metadata for: Lesson 15: Digital Rangatiratanga | Digital Kaitia
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 15: Digital Rangatiratanga | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/science/lesson-15-digital-rangatiratanga.html' OR path LIKE '%lesson-15-digital-rangatiratanga.html';


-- Update metadata for: Unit 2, Lesson 4: 20th Century Activism
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2, Lesson 4: 20th Century Activism')
WHERE path = 'public/integrated-lessons/science/unit-2-lesson-4.html' OR path LIKE '%unit-2-lesson-4.html';


-- Update metadata for: Statistical Investigation: Community Data Project 
UPDATE resources 
SET 
    subject = 'Science',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Statistical Investigation: Community Data Project | Te Kete Ako')
WHERE path = 'public/integrated-lessons/science/lesson-statistical-investigation.html' OR path LIKE '%lesson-statistical-investigation.html';


-- Update metadata for: Te Whare Tapa Whā - Holistic Health Model
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Whare Tapa Whā - Holistic Health Model')
WHERE path = 'public/integrated-lessons/science/health-and-wellbeing-te-whare-tapa-whā-model.html' OR path LIKE '%health-and-wellbeing-te-whare-tapa-whā-model.html';


-- Update metadata for: Lesson Plan: Show, Don't Tell | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Show, Don''t Tell | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/science/show-dont-tell-lesson-plan.html' OR path LIKE '%show-dont-tell-lesson-plan.html';


-- Update metadata for: The Writer's Toolkit: Show, Don't Tell | Mangakōtu
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Show, Don''t Tell | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/science/writers-toolkit-show-dont-tell-handout.html' OR path LIKE '%writers-toolkit-show-dont-tell-handout.html';


-- Update metadata for: Physics of Traditional Māori Instruments
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Physics of Traditional Māori Instruments')
WHERE path = 'public/integrated-lessons/science/physics-of-traditional-māori-instruments.html' OR path LIKE '%physics-of-traditional-māori-instruments.html';


-- Update metadata for: YouTube Library Administration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'YouTube Library Administration | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/admin-youtube-library.html' OR path LIKE '%admin-youtube-library.html';


-- Update metadata for: Diction & Tone Combined Lesson | Writers Toolkit |
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Diction & Tone Combined Lesson | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/diction-tone-lesson-plan.html' OR path LIKE '%diction-tone-lesson-plan.html';


-- Update metadata for: Lesson 2: Biodiversity & Endemism in Aotearoa
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: Biodiversity & Endemism in Aotearoa')
WHERE path = 'public/integrated-lessons/mathematics/lesson-2-biodiversity-endemism.html' OR path LIKE '%lesson-2-biodiversity-endemism.html';


-- Update metadata for: Lighthouse Trigonometry - Navigation Math | Te Ket
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lighthouse Trigonometry - Navigation Math | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/lighthouse-report.html' OR path LIKE '%lighthouse-report.html';


-- Update metadata for: Do Now Activities | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Do Now Activities | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/activities.html' OR path LIKE '%activities.html';


-- Update metadata for: Lesson 5: The Two-Step Shuffle
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5: The Two-Step Shuffle')
WHERE path = 'public/integrated-lessons/mathematics/lesson-5-the-two-step-shuffle.html' OR path LIKE '%lesson-5-the-two-step-shuffle.html';


-- Update metadata for: AI Teacher Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Teacher Dashboard | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/teacher-dashboard-ai.html' OR path LIKE '%teacher-dashboard-ai.html';


-- Update metadata for: Science Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Science Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/curriculum-science.html' OR path LIKE '%curriculum-science.html';


-- Update metadata for: Te Kete Ako | Critical Thinking - Lesson 5: Recogn
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Critical Thinking - Lesson 5: Recognizing Propaganda & Persuasion')
WHERE path = 'public/integrated-lessons/mathematics/lesson-5.html' OR path LIKE '%lesson-5.html';


-- Update metadata for: Navigation Mathematics: Wayfinding & Trigonometry 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Navigation Mathematics: Wayfinding & Trigonometry | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/navigation-mathematics-lesson.html' OR path LIKE '%navigation-mathematics-lesson.html';


-- Update metadata for: Lesson 2: Identifying Bias and Credible Sources
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: Identifying Bias and Credible Sources')
WHERE path = 'public/integrated-lessons/mathematics/lesson-2-bias-and-sources.html' OR path LIKE '%lesson-2-bias-and-sources.html';


-- Update metadata for: Te Kete Ako - Intelligent Resource Discovery | Gra
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Intelligent Resource Discovery | GraphRAG Search')
WHERE path = 'public/integrated-lessons/mathematics/graphrag-search.html' OR path LIKE '%graphrag-search.html';


-- Update metadata for: Living Whakapapa Project | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Living Whakapapa Project | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/living-whakapapa.html' OR path LIKE '%living-whakapapa.html';


-- Update metadata for: Comprehensive: Whakapapa Deep Dive Activities - Un
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Comprehensive: Whakapapa Deep Dive Activities - Unit 1 Lesson 1')
WHERE path = 'public/integrated-lessons/mathematics/unit-1-lesson-1-whakapapa-deep-dive-activities.html' OR path LIKE '%unit-1-lesson-1-whakapapa-deep-dive-activities.html';


-- Update metadata for: My Submissions | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Submissions | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/my-submissions.html' OR path LIKE '%my-submissions.html';


-- Update metadata for: Week 4: Probability & Real-World Predictions | Y8 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Week 4: Probability & Real-World Predictions | Y8 Statistics')
WHERE path = 'public/integrated-lessons/mathematics/lesson-4-probability-real-world-predictions.html' OR path LIKE '%lesson-4-probability-real-world-predictions.html';


-- Update metadata for: Week 2: Analysing NZ Sports Data | Y8 Statistics
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Week 2: Analysing NZ Sports Data | Y8 Statistics')
WHERE path = 'public/integrated-lessons/mathematics/lesson-2-analysing-nz-sports-data.html' OR path LIKE '%lesson-2-analysing-nz-sports-data.html';


-- Update metadata for: Kaitiaki Aronui - Advanced AI Capabilities Showcas
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Kaitiaki Aronui - Advanced AI Capabilities Showcase | Teacher Professional Development')
WHERE path = 'public/integrated-lessons/mathematics/kaitiaki-aronui-capability-showcase.html' OR path LIKE '%kaitiaki-aronui-capability-showcase.html';


-- Update metadata for: Resource Connections | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Resource Connections | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/resource-connections.html' OR path LIKE '%resource-connections.html';


-- Update metadata for: Unit 3 Lesson 5: Community Science Projects | Mang
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 3 Lesson 5: Community Science Projects | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/mathematics/unit-3-lesson-5.html' OR path LIKE '%unit-3-lesson-5.html';


-- Update metadata for: Other Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Other Resources | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/other-resources.html' OR path LIKE '%other-resources.html';


-- Update metadata for: Lesson 9: The Misinformation Effect | Digital Kait
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 9: The Misinformation Effect | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/mathematics/lesson-9-misinformation-effect.html' OR path LIKE '%lesson-9-misinformation-effect.html';


-- Update metadata for: Privacy Policy | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Privacy Policy | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/privacy-policy.html' OR path LIKE '%privacy-policy.html';


-- Update metadata for: Lesson 4: Human Impact & Conservation
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: Human Impact & Conservation')
WHERE path = 'public/integrated-lessons/mathematics/lesson-4-human-impact-conservation.html' OR path LIKE '%lesson-4-human-impact-conservation.html';


-- Update metadata for: Social Studies | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Social Studies | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/social-studies.html' OR path LIKE '%social-studies.html';


-- Update metadata for: Year 8 Social Studies - Māori Migration to Aotearo
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Year 8 Social Studies - Māori Migration to Aotearoa | Kaitiaki Aronui Generated')
WHERE path = 'public/integrated-lessons/mathematics/kaitiaki-generated-maori-migration-lesson.html' OR path LIKE '%kaitiaki-generated-maori-migration-lesson.html';


-- Update metadata for: Statistical Analysis of Sports Performance
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Statistical Analysis of Sports Performance')
WHERE path = 'public/integrated-lessons/mathematics/statistical-analysis-of-sports-performance.html' OR path LIKE '%statistical-analysis-of-sports-performance.html';


-- Update metadata for: Student Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Student Dashboard | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/student-dashboard.html' OR path LIKE '%student-dashboard.html';


-- Update metadata for: Unit 4, Lesson 3: Mathematics in Cultural Context
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4, Lesson 3: Mathematics in Cultural Context')
WHERE path = 'public/integrated-lessons/mathematics/unit-4-lesson-3.html' OR path LIKE '%unit-4-lesson-3.html';


-- Update metadata for: Lesson 3: Field Study - Rangahau Taiao
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Field Study - Rangahau Taiao')
WHERE path = 'public/integrated-lessons/mathematics/lesson-3-field-study-rangahau-taiao.html' OR path LIKE '%lesson-3-field-study-rangahau-taiao.html';


-- Update metadata for: Unit 3 Lesson 2: Environmental Science & Kaitiakit
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 3 Lesson 2: Environmental Science & Kaitiakitanga | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/mathematics/unit-3-lesson-2.html' OR path LIKE '%unit-3-lesson-2.html';


-- Update metadata for: The Writer's Toolkit: The PEEL Method
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: The PEEL Method')
WHERE path = 'public/integrated-lessons/mathematics/writers-toolkit-peel-argument-handout.html' OR path LIKE '%writers-toolkit-peel-argument-handout.html';


-- Update metadata for: Sitemap
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Sitemap')
WHERE path = 'public/integrated-lessons/mathematics/sitemap.html' OR path LIKE '%sitemap.html';


-- Update metadata for: Mathematics and Statistics Curriculum Alignment | 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Mathematics and Statistics Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/curriculum-mathematics.html' OR path LIKE '%curriculum-mathematics.html';


-- Update metadata for: Lesson 7: Tukutuku Transformations | Y9 Mathematic
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 7: Tukutuku Transformations | Y9 Mathematics | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/lesson-7-tukutuku-transformations.html' OR path LIKE '%lesson-7-tukutuku-transformations.html';


-- Update metadata for: Career Pathways in STEM for Māori Students
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Career Pathways in STEM for Māori Students')
WHERE path = 'public/integrated-lessons/mathematics/career-pathways-in-stem-for-māori-students.html' OR path LIKE '%career-pathways-in-stem-for-māori-students.html';


-- Update metadata for: Lesson 1: Star Compass Calculations Worksheet
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Star Compass Calculations Worksheet')
WHERE path = 'public/integrated-lessons/mathematics/lesson-1-star-compass-calculations.html' OR path LIKE '%lesson-1-star-compass-calculations.html';


-- Update metadata for: YouTube Educational Library | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'YouTube Educational Library | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/youtube-library.html' OR path LIKE '%youtube-library.html';


-- Update metadata for: Unit 2 Lesson 1: Pre-Colonial Innovation - Challen
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2 Lesson 1: Pre-Colonial Innovation - Challenging the Myth of "Primitive" Technology | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/unit-2-lesson-1.html' OR path LIKE '%unit-2-lesson-1.html';


-- Update metadata for: Project Submission | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Project Submission | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/project-submission.html' OR path LIKE '%project-submission.html';


-- Update metadata for: Page Not Found - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Page Not Found - Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/404.html' OR path LIKE '%404.html';


-- Update metadata for: Te Kete Ako | Educational Resources Honoring Te Ao
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Educational Resources Honoring Te Ao Māori')
WHERE path = 'public/integrated-lessons/mathematics/index-bloated-backup.html' OR path LIKE '%index-bloated-backup.html';


-- Update metadata for: Unit 1 Lesson 1: Ko Wai Au? - Personal Whakapapa E
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 1: Ko Wai Au? - Personal Whakapapa Exploration | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/unit-1-lesson-1.html' OR path LIKE '%unit-1-lesson-1.html';


-- Update metadata for: Subjects | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Subjects | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/subjects.html' OR path LIKE '%subjects.html';


-- Update metadata for: Teacher Analytics Guide | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Analytics Guide | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/teacher-guide.html' OR path LIKE '%teacher-guide.html';


-- Update metadata for: Systems Lesson 2.1: Government Systems Deep-Dive |
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Systems Lesson 2.1: Government Systems Deep-Dive | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/systems-lesson-2-1.html' OR path LIKE '%systems-lesson-2-1.html';


-- Update metadata for: Resource Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Resource Hub | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/resource-hub.html' OR path LIKE '%resource-hub.html';


-- Update metadata for: Week 3: Census & Population Trends | Y8 Statistics
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Week 3: Census & Population Trends | Y8 Statistics')
WHERE path = 'public/integrated-lessons/mathematics/lesson-3-census-population-trends.html' OR path LIKE '%lesson-3-census-population-trends.html';


-- Update metadata for: Unit 7 Lesson 3: AI Ethics in Practice | Te Kete A
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 7 Lesson 3: AI Ethics in Practice | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/unit-7-lesson-3.html' OR path LIKE '%unit-7-lesson-3.html';


-- Update metadata for: Unit 3 Lesson 3: Mathematics in Cultural Context |
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 3 Lesson 3: Mathematics in Cultural Context | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/mathematics/unit-3-lesson-3.html' OR path LIKE '%unit-3-lesson-3.html';


-- Update metadata for: Cognitive Biases | Critical Literacy Unit
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cognitive Biases | Critical Literacy Unit')
WHERE path = 'public/integrated-lessons/mathematics/cognitive-biases-comprehension-handout.html' OR path LIKE '%cognitive-biases-comprehension-handout.html';


-- Update metadata for: YouTube Resources | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'YouTube Resources | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/youtube.html' OR path LIKE '%youtube.html';


-- Update metadata for: Complete Curriculum | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Complete Curriculum | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/curriculum-index.html' OR path LIKE '%curriculum-index.html';


-- Update metadata for: Lesson 2: The Mystery of 'x'
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: The Mystery of ''x''')
WHERE path = 'public/integrated-lessons/mathematics/lesson-2-the-mystery-of-x.html' OR path LIKE '%lesson-2-the-mystery-of-x.html';


-- Update metadata for: Cultural Treasures | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Treasures | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/cultural-treasures.html' OR path LIKE '%cultural-treasures.html';


-- Update metadata for: Unit 4 Lesson 1: Understanding Economic Systems - 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 4 Lesson 1: Understanding Economic Systems - Who Wins and Who Loses? | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/mathematics/unit-4-lesson-1.html' OR path LIKE '%unit-4-lesson-1.html';


-- Update metadata for: Lesson 10: Your Data is a Taonga | Digital Kaitiak
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 10: Your Data is a Taonga | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/mathematics/lesson-10-data-as-taonga.html' OR path LIKE '%lesson-10-data-as-taonga.html';


-- Update metadata for: Te Kete Ako | Educational Resources Honoring Te Ao
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Educational Resources Honoring Te Ao Māori')
WHERE path = 'public/integrated-lessons/mathematics/index-backup-old-complex.html' OR path LIKE '%index-backup-old-complex.html';


-- Update metadata for: English/Literacy Progression Framework - Culturall
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'English/Literacy Progression Framework - Culturally Responsive Communication | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/mathematics/english-literacy-progression-framework.html' OR path LIKE '%english-literacy-progression-framework.html';


-- Update metadata for: Fluency & Suspense Combined Lesson | Writers Toolk
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Fluency & Suspense Combined Lesson | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/fluency-suspense-lesson-plan.html' OR path LIKE '%fluency-suspense-lesson-plan.html';


-- Update metadata for: The Writer's Toolkit: Rhetorical Devices
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit: Rhetorical Devices')
WHERE path = 'public/integrated-lessons/mathematics/writers-toolkit-rhetorical-devices-handout.html' OR path LIKE '%writers-toolkit-rhetorical-devices-handout.html';


-- Update metadata for: Teacher Dashboard | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Dashboard | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/teacher-dashboard.html' OR path LIKE '%teacher-dashboard.html';


-- Update metadata for: English Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'English Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/curriculum-english.html' OR path LIKE '%curriculum-english.html';


-- Update metadata for: Discover Orphans
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Discover Orphans')
WHERE path = 'public/integrated-lessons/mathematics/orphans.html' OR path LIKE '%orphans.html';


-- Update metadata for: Unit 1 Lesson 2: Mātauranga Māori - Traditional Kn
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 1 Lesson 2: Mātauranga Māori - Traditional Knowledge Systems | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/mathematics/unit-1-lesson-2.html' OR path LIKE '%unit-1-lesson-2.html';


-- Update metadata for: Whakairo Geometry | Mathematics & Science Toolkit 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Whakairo Geometry | Mathematics & Science Toolkit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/whakairo-geometry-lesson.html' OR path LIKE '%whakairo-geometry-lesson.html';


-- Update metadata for: Unit 6 Lesson 2: Innovation through Whakapapa | Te
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 6 Lesson 2: Innovation through Whakapapa | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/unit-6-lesson-2.html' OR path LIKE '%unit-6-lesson-2.html';


-- Update metadata for: Digital Pūrākau | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Pūrākau | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/digital-purakau.html' OR path LIKE '%digital-purakau.html';


-- Update metadata for: NZ Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'NZ Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/curriculum-alignment.html' OR path LIKE '%curriculum-alignment.html';


-- Update metadata for: Traditional Navigation & Modern GPS Integration - 
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Traditional Navigation & Modern GPS Integration - Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/traditional-navigation-and-modern-gps-integration.html' OR path LIKE '%traditional-navigation-and-modern-gps-integration.html';


-- Update metadata for: Social Sciences Progression Framework - Years 7-13
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Social Sciences Progression Framework - Years 7-13 | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/mathematics/social-sciences-progression-framework.html' OR path LIKE '%social-sciences-progression-framework.html';


-- Update metadata for: Lesson 6: Guardians of the Future
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6: Guardians of the Future')
WHERE path = 'public/integrated-lessons/mathematics/lesson-6-guardians-future.html' OR path LIKE '%lesson-6-guardians-future.html';


-- Update metadata for: Welcome to Te Kete Ako | Educational Resources for
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Welcome to Te Kete Ako | Educational Resources for New Zealand')
WHERE path = 'public/integrated-lessons/mathematics/welcome.html' OR path LIKE '%welcome.html';


-- Update metadata for: Lesson 6: Presentations & Peer Review | Guided Inq
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 6: Presentations & Peer Review | Guided Inquiry Unit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/lesson-6-presentations.html' OR path LIKE '%lesson-6-presentations.html';


-- Update metadata for: Te Ao Māori | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Ao Māori | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/te-ao-maori.html' OR path LIKE '%te-ao-maori.html';


-- Update metadata for: Week 5: Final Project & Presentation | Y8 Statisti
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Week 5: Final Project & Presentation | Y8 Statistics')
WHERE path = 'public/integrated-lessons/mathematics/lesson-5-final-project-presentation.html' OR path LIKE '%lesson-5-final-project-presentation.html';


-- Update metadata for: Unit 3 Lesson 1: Dual Knowledge Systems Foundation
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 3 Lesson 1: Dual Knowledge Systems Foundation | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/mathematics/unit-3-lesson-1.html' OR path LIKE '%unit-3-lesson-1.html';


-- Update metadata for: Lesson 4: Balancing Act
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: Balancing Act')
WHERE path = 'public/integrated-lessons/mathematics/lesson-4-balancing-act.html' OR path LIKE '%lesson-4-balancing-act.html';


-- Update metadata for: Te Kete Ako | World-Class Educational Resources Ho
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | World-Class Educational Resources Honoring Te Ao Māori')
WHERE path = 'public/integrated-lessons/mathematics/index-premium.html' OR path LIKE '%index-premium.html';


-- Update metadata for: Te Kete Ako - Comprehensive Site Map
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Comprehensive Site Map')
WHERE path = 'public/integrated-lessons/mathematics/sitemap-enhanced.html' OR path LIKE '%sitemap-enhanced.html';


-- Update metadata for: Algebraic Patterns: Finding Rules in Nature & Cult
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 1',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Algebraic Patterns: Finding Rules in Nature & Culture | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/algebraic-patterns-lesson.html' OR path LIKE '%algebraic-patterns-lesson.html';


-- Update metadata for: Unit 7 Lesson 1: AI Through Te Ao Māori Lens | Te 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 7 Lesson 1: AI Through Te Ao Māori Lens | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/unit-7-lesson-1.html' OR path LIKE '%unit-7-lesson-1.html';


-- Update metadata for: Lesson 1: Pattern Detectives
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1: Pattern Detectives')
WHERE path = 'public/integrated-lessons/mathematics/lesson-1-patterns-and-sequences.html' OR path LIKE '%lesson-1-patterns-and-sequences.html';


-- Update metadata for: Systems Lesson 1.1: What Makes a Society? | Te Ket
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Systems Lesson 1.1: What Makes a Society? | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/systems-lesson-1-1.html' OR path LIKE '%systems-lesson-1-1.html';


-- Update metadata for: Lesson Plan: Rhetorical Devices | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Rhetorical Devices | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/mathematics/rhetorical-devices-lesson-plan.html' OR path LIKE '%rhetorical-devices-lesson-plan.html';


-- Update metadata for: Unit 5 Lesson 4: Climate Justice Leadership - Indi
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 5 Lesson 4: Climate Justice Leadership - Indigenous Solutions for Global Challenges | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/unit-5-lesson-4.html' OR path LIKE '%unit-5-lesson-4.html';


-- Update metadata for: Social Sciences Curriculum Alignment | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Social Sciences Curriculum Alignment | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/curriculum-social-sciences.html' OR path LIKE '%curriculum-social-sciences.html';


-- Update metadata for: Te Kete Ako | Educational Resources Honoring Te Ao
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Educational Resources Honoring Te Ao Māori')
WHERE path = 'public/integrated-lessons/mathematics/index-simple.html' OR path LIKE '%index-simple.html';


-- Update metadata for: Climate Change Through Te Taiao Māori Lens - Te Ke
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Climate Change Through Te Taiao Māori Lens - Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/climate-change-through-te-taiao-māori-lens.html' OR path LIKE '%climate-change-through-te-taiao-māori-lens.html';


-- Update metadata for: My Kete | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'My Kete | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/my-kete.html' OR path LIKE '%my-kete.html';


-- Update metadata for: Site Map | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 7',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Site Map | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/site-map.html' OR path LIKE '%site-map.html';


-- Update metadata for: Educational Transformation | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Educational Transformation | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/educational-transformation-showcase.html' OR path LIKE '%educational-transformation-showcase.html';


-- Update metadata for: Lesson 8: The Art of the Upstander | Digital Kaiti
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 8: The Art of the Upstander | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/mathematics/lesson-8-art-of-the-upstander.html' OR path LIKE '%lesson-8-art-of-the-upstander.html';


-- Update metadata for: The Great Migration | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Great Migration | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/walker-lesson-1.2-the-great-migration.html' OR path LIKE '%walker-lesson-1.2-the-great-migration.html';


-- Update metadata for: Lesson 3: Building with Algebra
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Building with Algebra')
WHERE path = 'public/integrated-lessons/mathematics/lesson-3-building-with-algebra.html' OR path LIKE '%lesson-3-building-with-algebra.html';


-- Update metadata for: Te Kete Ako | Critical Thinking - Lesson 6: Digita
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Critical Thinking - Lesson 6: Digital Literacy & Online Safety')
WHERE path = 'public/integrated-lessons/mathematics/lesson-6.html' OR path LIKE '%lesson-6.html';


-- Update metadata for: Week 1: Introduction to Statistical Investigations
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Week 1: Introduction to Statistical Investigations | Y8 Statistics')
WHERE path = 'public/integrated-lessons/mathematics/lesson-1-introduction-statistical-investigations.html' OR path LIKE '%lesson-1-introduction-statistical-investigations.html';


-- Update metadata for: 🎓 Teacher AI Intelligence Hub | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), '🎓 Teacher AI Intelligence Hub | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/teacher-ai-intelligence-hub.html' OR path LIKE '%teacher-ai-intelligence-hub.html';


-- Update metadata for: Interactive Learning Demo | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Interactive Learning Demo | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/interactive-learning-demo.html' OR path LIKE '%interactive-learning-demo.html';


-- Update metadata for: Lesson 5: Restoration & Kaitiakitanga
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 5: Restoration & Kaitiakitanga')
WHERE path = 'public/integrated-lessons/mathematics/lesson-5-restoration-kaitiakitanga.html' OR path LIKE '%lesson-5-restoration-kaitiakitanga.html';


-- Update metadata for: Virtual Marae Training Protocol | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Virtual Marae Training Protocol | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/virtual-marae.html' OR path LIKE '%virtual-marae.html';


-- Update metadata for: Lesson 4: Ethics & Decision-Making
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 4: Ethics & Decision-Making')
WHERE path = 'public/integrated-lessons/mathematics/lesson-4-ethics-decision-making.html' OR path LIKE '%lesson-4-ethics-decision-making.html';


-- Update metadata for: Community Action Project Brief | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Community Action Project Brief | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/project-brief.html' OR path LIKE '%project-brief.html';


-- Update metadata for: Lesson Plans | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plans | Te Kete Ako')
WHERE path = 'public/integrated-lessons/mathematics/lessons.html' OR path LIKE '%lessons.html';


-- Update metadata for: Resource Discovery Hub - Te Kete Ako V2.5
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Resource Discovery Hub - Te Kete Ako V2.5')
WHERE path = 'public/integrated-lessons/mathematics/resource-discovery-hub.html' OR path LIKE '%resource-discovery-hub.html';


-- Update metadata for: Te Kete Ako | Educational Resources Honoring Te Ao
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Educational Resources Honoring Te Ao Māori')
WHERE path = 'public/integrated-lessons/mathematics/index-backup.html' OR path LIKE '%index-backup.html';


-- Update metadata for: Physics of Traditional Māori Instruments
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Physics of Traditional Māori Instruments')
WHERE path = 'public/integrated-lessons/mathematics/physics-of-traditional-māori-instruments.html' OR path LIKE '%physics-of-traditional-māori-instruments.html';


-- Update metadata for: A Forum for Justice: The Waitangi Tribunal | Te Ke
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'A Forum for Justice: The Waitangi Tribunal | Te Kete Ako')
WHERE path = 'public/integrated-lessons/social studies/walker-lesson-1.4-a-forum-for-justice.html' OR path LIKE '%walker-lesson-1.4-a-forum-for-justice.html';


-- Update metadata for: Te Kete Ako - Identifying Bias in News Reporting
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako - Identifying Bias in News Reporting')
WHERE path = 'public/integrated-lessons/social studies/lesson-2.html' OR path LIKE '%lesson-2.html';


-- Update metadata for: Te Kete Ako Dashboard | Your Teaching Resources
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako Dashboard | Your Teaching Resources')
WHERE path = 'public/integrated-lessons/social studies/dashboard.html' OR path LIKE '%dashboard.html';


-- Update metadata for: Te Kete Ako | Critical Thinking - Lesson 1: Unders
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Critical Thinking - Lesson 1: Understanding Media Messages')
WHERE path = 'public/integrated-lessons/social studies/lesson-1.html' OR path LIKE '%lesson-1.html';


-- Update metadata for: Lesson 2: The Aotearoa Wars | Unit 2: Decolonized 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 2: The Aotearoa Wars | Unit 2: Decolonized History | Te Kete Ako')
WHERE path = 'public/integrated-lessons/social studies/unit-2-lesson-2.html' OR path LIKE '%unit-2-lesson-2.html';


-- Update metadata for: Lesson 3: Logical Fallacies
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 3: Logical Fallacies')
WHERE path = 'public/integrated-lessons/social studies/lesson-3-logical-fallacies.html' OR path LIKE '%lesson-3-logical-fallacies.html';


-- Update metadata for: Teaching Tools & Platforms | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teaching Tools & Platforms | Te Kete Ako')
WHERE path = 'public/integrated-lessons/social studies/tools.html' OR path LIKE '%tools.html';


-- Update metadata for: Lesson 1.4: A Forum for Justice | Walker Unit | Te
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.4: A Forum for Justice | Walker Unit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/social studies/lesson-1-4-a-forum-for-justice.html' OR path LIKE '%lesson-1-4-a-forum-for-justice.html';


-- Update metadata for: Printable: Society Stations Handout
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Society Stations Handout')
WHERE path = 'public/integrated-lessons/social studies/lesson-1-1-society-stations.html' OR path LIKE '%lesson-1-1-society-stations.html';


-- Update metadata for: Unit 2: Decolonized History | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Unit 2: Decolonized History | Te Kete Ako')
WHERE path = 'public/integrated-lessons/social studies/unit-2-decolonized-history.html' OR path LIKE '%unit-2-decolonized-history.html';


-- Update metadata for: Society Design Collaboration Framework | Te Kete A
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Society Design Collaboration Framework | Te Kete Ako')
WHERE path = 'public/integrated-lessons/social studies/society-design-collaboration-framework.html' OR path LIKE '%society-design-collaboration-framework.html';


-- Update metadata for: Advanced Critical Thinking: Decision-Making Framew
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Advanced Critical Thinking: Decision-Making Frameworks | Te Kete Ako')
WHERE path = 'public/integrated-lessons/social studies/advanced-critical-thinking-decision-making.html' OR path LIKE '%advanced-critical-thinking-decision-making.html';


-- Update metadata for: Lesson 1.5: Reclaiming the Narrative | Walker Unit
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 1.5: Reclaiming the Narrative | Walker Unit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/lesson-1-5-reclaiming-the-narrative.html' OR path LIKE '%lesson-1-5-reclaiming-the-narrative.html';


-- Update metadata for: Offline - Te Kete Ako
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Offline - Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/offline.html' OR path LIKE '%offline.html';


-- Update metadata for: Digital Writing Tools | Writers Toolkit | Te Kete 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Writing Tools | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/digital-writing-tools.html' OR path LIKE '%digital-writing-tools.html';


-- Update metadata for: Te Kete Ako | Critical Thinking - Lesson 4: Logic 
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | Critical Thinking - Lesson 4: Logic & Reasoning')
WHERE path = 'public/integrated-lessons/english/lesson-4.html' OR path LIKE '%lesson-4.html';


-- Update metadata for: Printable: Tikanga Scenarios for Discussion
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Tikanga Scenarios for Discussion')
WHERE path = 'public/integrated-lessons/english/unit-1-lesson-2-tikanga-scenarios.html' OR path LIKE '%unit-1-lesson-2-tikanga-scenarios.html';


-- Update metadata for: Writers Toolkit Progress Tracker | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Writers Toolkit Progress Tracker | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/writers-toolkit-progress-tracker.html' OR path LIKE '%writers-toolkit-progress-tracker.html';


-- Update metadata for: Media Literacy: Analyzing Māori Representation
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Media Literacy: Analyzing Māori Representation')
WHERE path = 'public/integrated-lessons/english/media-literacy-analyzing-māori-representation.html' OR path LIKE '%media-literacy-analyzing-māori-representation.html';


-- Update metadata for: Cultural Integration Templates | Writers Toolkit |
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cultural Integration Templates | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/cultural-integration-templates.html' OR path LIKE '%cultural-integration-templates.html';


-- Update metadata for: Browse by Concept | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Browse by Concept | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/browse-by-concept.html' OR path LIKE '%browse-by-concept.html';


-- Update metadata for: Social Studies | Te Kete Ako
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Social Studies | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/social-studies.html' OR path LIKE '%social-studies.html';


-- Update metadata for: Walker Lesson 1.1 Assessment Rubric | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Walker Lesson 1.1 Assessment Rubric | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/walker-lesson-1-1-assessment-rubric.html' OR path LIKE '%walker-lesson-1-1-assessment-rubric.html';


-- Update metadata for: Lesson 7: Group Decision-Making
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 7: Group Decision-Making')
WHERE path = 'public/integrated-lessons/english/lesson-7-group-decision-making.html' OR path LIKE '%lesson-7-group-decision-making.html';


-- Update metadata for: Housing Affordability in Aotearoa: Critical Analys
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Housing Affordability in Aotearoa: Critical Analysis | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/housing-affordability-comprehension-handout.html' OR path LIKE '%housing-affordability-comprehension-handout.html';


-- Update metadata for: Ranginui Walker: A Life of Integrity - Student Han
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Ranginui Walker: A Life of Integrity - Student Handout | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/walker-lesson-1-1-student-handout.html' OR path LIKE '%walker-lesson-1-1-student-handout.html';


-- Update metadata for: Poetry Analysis Through Māori Literary Traditions
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Poetry Analysis Through Māori Literary Traditions')
WHERE path = 'public/integrated-lessons/english/poetry-analysis-through-māori-literary-traditions.html' OR path LIKE '%poetry-analysis-through-māori-literary-traditions.html';


-- Update metadata for: Printable: Decolonization Today
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Decolonization Today')
WHERE path = 'public/integrated-lessons/english/decolonization-today.html' OR path LIKE '%decolonization-today.html';


-- Update metadata for: Lesson 14: The Digital Korowai | Digital Kaitiakit
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson 14: The Digital Korowai | Digital Kaitiakitanga')
WHERE path = 'public/integrated-lessons/english/lesson-14-digital-korowai.html' OR path LIKE '%lesson-14-digital-korowai.html';


-- Update metadata for: Writers Toolkit Assessment Rubric | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Writers Toolkit Assessment Rubric | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/writers-toolkit-assessment-rubric.html' OR path LIKE '%writers-toolkit-assessment-rubric.html';


-- Update metadata for: Economic Justice: Analyzing Inequality | Te Kete A
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Economic Justice: Analyzing Inequality | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/economic-justice-deep-dive-comprehension.html' OR path LIKE '%economic-justice-deep-dive-comprehension.html';


-- Update metadata for: Printable: Te Tiriti Māori & English Texts Compari
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Te Tiriti Māori & English Texts Comparison')
WHERE path = 'public/integrated-lessons/english/treaty-two-texts.html' OR path LIKE '%treaty-two-texts.html';


-- Update metadata for: English | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'English | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/english.html' OR path LIKE '%english.html';


-- Update metadata for: Creative Writing Inspired by Whakataukī
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Creative Writing Inspired by Whakataukī')
WHERE path = 'public/integrated-lessons/english/creative-writing-inspired-by-whakataukī.html' OR path LIKE '%creative-writing-inspired-by-whakataukī.html';


-- Update metadata for: Cognitive Writing Strategies | Writers Toolkit | T
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Cognitive Writing Strategies | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/cognitive-writing-strategies.html' OR path LIKE '%cognitive-writing-strategies.html';


-- Update metadata for: Media Literacy: Critical Analysis Guide | Te Kete 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Media Literacy: Critical Analysis Guide | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/media-literacy-comprehension-handout.html' OR path LIKE '%media-literacy-comprehension-handout.html';


-- Update metadata for: Podcast Worksheet: Te Tiriti o Waitangi | Te Kete 
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Podcast Worksheet: Te Tiriti o Waitangi | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/worksheet-treaty-of-waitangi-podcast.html' OR path LIKE '%worksheet-treaty-of-waitangi-podcast.html';


-- Update metadata for: Lesson Plan: Building Suspense | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: Building Suspense | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/english/suspense-lesson-plan.html' OR path LIKE '%suspense-lesson-plan.html';


-- Update metadata for: Lesson Plan: The PEEL Method | Writer's Toolkit
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Plan: The PEEL Method | Writer''s Toolkit')
WHERE path = 'public/integrated-lessons/english/peel-lesson-plan.html' OR path LIKE '%peel-lesson-plan.html';


-- Update metadata for: Lesson Template: [Te Reo Name] - [English Name] | 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Lesson Template: [Te Reo Name] - [English Name] | Mangakōtukutuku College')
WHERE path = 'public/integrated-lessons/english/lesson-template.html' OR path LIKE '%lesson-template.html';


-- Update metadata for: Interactive Writing Games | Writers Toolkit | Te K
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Interactive Writing Games | Writers Toolkit | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/interactive-writing-games.html' OR path LIKE '%interactive-writing-games.html';


-- Update metadata for: Misleading Graphs & Data Literacy | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Misleading Graphs & Data Literacy | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/misleading-graphs-comprehension-handout.html' OR path LIKE '%misleading-graphs-comprehension-handout.html';


-- Update metadata for: Te Kete Ako | World's First AI-Enhanced Cultural E
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Kete Ako | World''s First AI-Enhanced Cultural Educational Platform')
WHERE path = 'public/integrated-lessons/english/index-new.html' OR path LIKE '%index-new.html';


-- Update metadata for: Search | Te Kete Ako
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 8',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Search | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/search.html' OR path LIKE '%search.html';


-- Update metadata for: Printable: Defending Tino Rangatiratanga Case Stud
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Printable: Defending Tino Rangatiratanga Case Studies')
WHERE path = 'public/integrated-lessons/english/maori-political-action.html' OR path LIKE '%maori-political-action.html';


-- Update metadata for: Digital Storytelling with Pūrākau Framework
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Storytelling with Pūrākau Framework')
WHERE path = 'public/integrated-lessons/english/digital-storytelling-with-pūrākau-framework.html' OR path LIKE '%digital-storytelling-with-pūrākau-framework.html';


-- Update metadata for: Argumentative Writing on Contemporary Māori Issues
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Argumentative Writing on Contemporary Māori Issues')
WHERE path = 'public/integrated-lessons/english/argumentative-writing-on-contemporary-māori-issues.html' OR path LIKE '%argumentative-writing-on-contemporary-māori-issues.html';


-- Update metadata for: Reclaiming the Narrative: Ka Whawhai Tonu Mātou | 
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Reclaiming the Narrative: Ka Whawhai Tonu Mātou | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/walker-lesson-1.5-reclaiming-the-narrative.html' OR path LIKE '%walker-lesson-1.5-reclaiming-the-narrative.html';


-- Update metadata for: Game Development with Cultural Themes
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Game Development with Cultural Themes')
WHERE path = 'public/integrated-lessons/english/game-development-with-cultural-themes.html' OR path LIKE '%game-development-with-cultural-themes.html';


-- Update metadata for: The Writer's Toolkit | Critical Literacy Unit
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'The Writer''s Toolkit | Critical Literacy Unit')
WHERE path = 'public/integrated-lessons/english/toolkit.html' OR path LIKE '%toolkit.html';


-- Update metadata for: AI Impact on Society: Critical Reading & Analysis 
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Impact on Society: Critical Reading & Analysis | Te Kete Ako')
WHERE path = 'public/integrated-lessons/english/ai-impact-comprehension-handout.html' OR path LIKE '%ai-impact-comprehension-handout.html';


-- Update metadata for: Teacher Quick-Start Guide: AI-Generated Resources 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 9',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Teacher Quick-Start Guide: AI-Generated Resources | Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/TEACHER-QUICK-START-GUIDE.html' OR path LIKE '%TEACHER-QUICK-START-GUIDE.html';


-- Update metadata for: Algebraic Thinking in Traditional Māori Games | Te
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Algebraic Thinking in Traditional Māori Games | Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/handouts/algebraic-thinking-in-traditional-māori-games.html' OR path LIKE '%algebraic-thinking-in-traditional-māori-games.html';


-- Update metadata for: Biotechnology Ethics Through Māori Worldview
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Biotechnology Ethics Through Māori Worldview')
WHERE path = 'public/generated-resources-alpha/handouts/biotechnology-ethics-through-māori-worldview.html' OR path LIKE '%biotechnology-ethics-through-māori-worldview.html';


-- Update metadata for: Leadership Development Through Cultural Values
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Leadership Development Through Cultural Values')
WHERE path = 'public/generated-resources-alpha/handouts/leadership-development-through-cultural-values.html' OR path LIKE '%leadership-development-through-cultural-values.html';


-- Update metadata for: Visual Arts Analysis with Māori Aesthetic Principl
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Visual Arts Analysis with Māori Aesthetic Principles')
WHERE path = 'public/generated-resources-alpha/handouts/visual-arts-analysis-with-cultural-context.html' OR path LIKE '%visual-arts-analysis-with-cultural-context.html';


-- Update metadata for: Cultural Safety Checklists for Classroom Discussio
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Cultural Safety Checklists for Classroom Discussions - Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/handouts/cultural-safety-checklists-for-classroom-discussions.html' OR path LIKE '%cultural-safety-checklists-for-classroom-discussions.html';


-- Update metadata for: Workplace Readiness with Cultural Competency
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Workplace Readiness with Cultural Competency')
WHERE path = 'public/generated-resources-alpha/handouts/workplace-readiness-with-cultural-competency.html' OR path LIKE '%workplace-readiness-with-cultural-competency.html';


-- Update metadata for: Digital Equity & Accessibility - Mobile Learning G
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Digital Equity & Accessibility - Mobile Learning Guide')
WHERE path = 'public/generated-resources-alpha/handouts/chromebook-optimized-mobile-learning-guide.html' OR path LIKE '%chromebook-optimized-mobile-learning-guide.html';


-- Update metadata for: Financial Literacy with Māori Economic Principles 
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Financial Literacy with Māori Economic Principles - Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/handouts/financial-literacy-with-māori-economic-principles.html' OR path LIKE '%financial-literacy-with-māori-economic-principles.html';


-- Update metadata for: Geometric Patterns in Māori Art and Architecture
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Geometric Patterns in Māori Art and Architecture')
WHERE path = 'public/generated-resources-alpha/handouts/geometric-patterns-in-māori-art-and-architecture.html' OR path LIKE '%geometric-patterns-in-māori-art-and-architecture.html';


-- Update metadata for: Data Visualization of Cultural Demographics
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Data Visualization of Cultural Demographics')
WHERE path = 'public/generated-resources-alpha/handouts/data-visualization-of-cultural-demographics.html' OR path LIKE '%data-visualization-of-cultural-demographics.html';


-- Update metadata for: Statistical Analysis of Treaty Settlement Data
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Statistical Analysis of Treaty Settlement Data')
WHERE path = 'public/generated-resources-alpha/handouts/statistical-analysis-of-treaty-settlement-data.html' OR path LIKE '%statistical-analysis-of-treaty-settlement-data.html';


-- Update metadata for: Coding Projects Inspired by Māori Patterns
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Coding Projects Inspired by Māori Patterns')
WHERE path = 'public/generated-resources-alpha/handouts/coding-projects-inspired-by-māori-patterns.html' OR path LIKE '%coding-projects-inspired-by-māori-patterns.html';


-- Update metadata for: Sustainable Energy Solutions from Traditional Know
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Sustainable Energy Solutions from Traditional Knowledge')
WHERE path = 'public/generated-resources-alpha/handouts/sustainable-energy-solutions-from-traditional-knowledge.html' OR path LIKE '%sustainable-energy-solutions-from-traditional-knowledge.html';


-- Update metadata for: Year 9 Starter Pack: Essential Skills for High Sch
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 9',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Year 9 Starter Pack: Essential Skills for High School Success - Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/handouts/year-9-starter-pack-essential-skills-for-high-school-success.html' OR path LIKE '%year-9-starter-pack-essential-skills-for-high-school-success.html';


-- Update metadata for: NCEA Level 1 Literacy & Numeracy Must-Knows - Te K
UPDATE resources 
SET 
    subject = 'English',
    level = 'Year 1',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'NCEA Level 1 Literacy & Numeracy Must-Knows - Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/handouts/ncea-level-1-literacy-and-numeracy-must-knows.html' OR path LIKE '%ncea-level-1-literacy-and-numeracy-must-knows.html';


-- Update metadata for: Probability and Chance in Māori Games
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Probability and Chance in Māori Games')
WHERE path = 'public/generated-resources-alpha/handouts/probability-and-chance-in-māori-games.html' OR path LIKE '%probability-and-chance-in-māori-games.html';


-- Update metadata for: Public Speaking with Cultural Confidence
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Public Speaking with Cultural Confidence')
WHERE path = 'public/generated-resources-alpha/handouts/public-speaking-with-cultural-confidence.html' OR path LIKE '%public-speaking-with-cultural-confidence.html';


-- Update metadata for: Food Security Through Traditional Knowledge System
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Food Security Through Traditional Knowledge Systems')
WHERE path = 'public/generated-resources-alpha/handouts/food-security-through-traditional-knowledge-systems.html' OR path LIKE '%food-security-through-traditional-knowledge-systems.html';


-- Update metadata for: Mathematical Modeling of Ecological Systems
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Mathematical Modeling of Ecological Systems')
WHERE path = 'public/generated-resources-alpha/handouts/mathematical-modeling-of-ecological-systems.html' OR path LIKE '%mathematical-modeling-of-ecological-systems.html';


-- Update metadata for: Calculus Applications in Environmental Modeling
UPDATE resources 
SET 
    subject = 'Mathematics',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Calculus Applications in Environmental Modeling')
WHERE path = 'public/generated-resources-alpha/handouts/calculus-applications-in-environmental-modeling.html' OR path LIKE '%calculus-applications-in-environmental-modeling.html';


-- Update metadata for: Chemistry of Traditional Māori Medicine | Te Kete 
UPDATE resources 
SET 
    subject = 'Science',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Chemistry of Traditional Māori Medicine | Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/handouts/chemistry-of-traditional-māori-medicine.html' OR path LIKE '%chemistry-of-traditional-māori-medicine.html';


-- Update metadata for: Information Literacy in the Digital Age
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Information Literacy in the Digital Age')
WHERE path = 'public/generated-resources-alpha/handouts/information-literacy-in-the-digital-age.html' OR path LIKE '%information-literacy-in-the-digital-age.html';


-- Update metadata for: Te Reo Maths Glossary (Key Terms in Māori & Englis
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Te Reo Maths Glossary (Key Terms in Māori & English) - Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/handouts/te-reo-maths-glossary-key-terms-in-māori-and-english.html' OR path LIKE '%te-reo-maths-glossary-key-terms-in-māori-and-english.html';


-- Update metadata for: Global Citizenship with Tangata Whenua Perspective
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Global Citizenship with Tangata Whenua Perspective')
WHERE path = 'public/generated-resources-alpha/handouts/global-citizenship-with-tangata-whenua-perspective.html' OR path LIKE '%global-citizenship-with-tangata-whenua-perspective.html';


-- Update metadata for: Social Media and Cultural Identity
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'handout',
    title = COALESCE(NULLIF(title, ''), 'Social Media and Cultural Identity')
WHERE path = 'public/generated-resources-alpha/handouts/social-media-and-cultural-identity.html' OR path LIKE '%social-media-and-cultural-identity.html';


-- Update metadata for: AI Ethics Through Māori Data Sovereignty
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics Through Māori Data Sovereignty')
WHERE path = 'public/generated-resources-alpha/lessons/ai-ethics-through-māori-data-sovereignty.html' OR path LIKE '%ai-ethics-through-māori-data-sovereignty.html';


-- Update metadata for: Media Literacy: Analyzing Māori Representation
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Media Literacy: Analyzing Māori Representation')
WHERE path = 'public/generated-resources-alpha/lessons/media-literacy-analyzing-māori-representation.html' OR path LIKE '%media-literacy-analyzing-māori-representation.html';


-- Update metadata for: Statistical Analysis of Sports Performance
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Statistical Analysis of Sports Performance')
WHERE path = 'public/generated-resources-alpha/lessons/statistical-analysis-of-sports-performance.html' OR path LIKE '%statistical-analysis-of-sports-performance.html';


-- Update metadata for: Career Pathways in STEM for Māori Students
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Career Pathways in STEM for Māori Students')
WHERE path = 'public/generated-resources-alpha/lessons/career-pathways-in-stem-for-māori-students.html' OR path LIKE '%career-pathways-in-stem-for-māori-students.html';


-- Update metadata for: Poetry Analysis Through Māori Literary Traditions
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Poetry Analysis Through Māori Literary Traditions')
WHERE path = 'public/generated-resources-alpha/lessons/poetry-analysis-through-māori-literary-traditions.html' OR path LIKE '%poetry-analysis-through-māori-literary-traditions.html';


-- Update metadata for: AI Ethics Through Māori Data Sovereignty | Te Kete
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'AI Ethics Through Māori Data Sovereignty | Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/lessons/ai-ethics-through-māori-data-sovereignty-FIXED.html' OR path LIKE '%ai-ethics-through-māori-data-sovereignty-FIXED.html';


-- Update metadata for: Narrative Writing Using Māori Story Structures
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Narrative Writing Using Māori Story Structures')
WHERE path = 'public/generated-resources-alpha/lessons/narrative-writing-using-māori-story-structures.html' OR path LIKE '%narrative-writing-using-māori-story-structures.html';


-- Update metadata for: Research Skills: Traditional and Digital Sources
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Research Skills: Traditional and Digital Sources')
WHERE path = 'public/generated-resources-alpha/lessons/research-skills-using-traditional-and-digital-sources.html' OR path LIKE '%research-skills-using-traditional-and-digital-sources.html';


-- Update metadata for: Creative Writing Inspired by Whakataukī
UPDATE resources 
SET 
    subject = 'English',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Creative Writing Inspired by Whakataukī')
WHERE path = 'public/generated-resources-alpha/lessons/creative-writing-inspired-by-whakataukī.html' OR path LIKE '%creative-writing-inspired-by-whakataukī.html';


-- Update metadata for: Debate Skills with Māori Oratory Traditions
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Debate Skills with Māori Oratory Traditions')
WHERE path = 'public/generated-resources-alpha/lessons/debate-skills-with-māori-oratory-traditions.html' OR path LIKE '%debate-skills-with-māori-oratory-traditions.html';


-- Update metadata for: Critical Analysis of Historical Documents | Te Ket
UPDATE resources 
SET 
    subject = 'Social Studies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Critical Analysis of Historical Documents | Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/lessons/critical-analysis-of-historical-documents.html' OR path LIKE '%critical-analysis-of-historical-documents.html';


-- Update metadata for: Traditional Navigation & Modern GPS Integration - 
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Traditional Navigation & Modern GPS Integration - Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/lessons/traditional-navigation-and-modern-gps-integration.html' OR path LIKE '%traditional-navigation-and-modern-gps-integration.html';


-- Update metadata for: Genetics and Whakapapa
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Genetics and Whakapapa')
WHERE path = 'public/generated-resources-alpha/lessons/genetics-and-whakapapa-scientific-and-cultural-perspectives.html' OR path LIKE '%genetics-and-whakapapa-scientific-and-cultural-perspectives.html';


-- Update metadata for: Renewable Energy and Māori Innovation
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Renewable Energy and Māori Innovation')
WHERE path = 'public/generated-resources-alpha/lessons/renewable-energy-and-māori-innovation.html' OR path LIKE '%renewable-energy-and-māori-innovation.html';


-- Update metadata for: Creative Problem Solving with Design Thinking
UPDATE resources 
SET 
    subject = 'Arts',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Creative Problem Solving with Design Thinking')
WHERE path = 'public/generated-resources-alpha/lessons/creative-problem-solving-with-design-thinking.html' OR path LIKE '%creative-problem-solving-with-design-thinking.html';


-- Update metadata for: Climate Change Through Te Taiao Māori Lens - Te Ke
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Climate Change Through Te Taiao Māori Lens - Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/lessons/climate-change-through-te-taiao-māori-lens.html' OR path LIKE '%climate-change-through-te-taiao-māori-lens.html';


-- Update metadata for: Digital Storytelling with Pūrākau Framework
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Digital Storytelling with Pūrākau Framework')
WHERE path = 'public/generated-resources-alpha/lessons/digital-storytelling-with-pūrākau-framework.html' OR path LIKE '%digital-storytelling-with-pūrākau-framework.html';


-- Update metadata for: Argumentative Writing on Contemporary Māori Issues
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'Year 10',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Argumentative Writing on Contemporary Māori Issues | Te Kete Ako')
WHERE path = 'public/generated-resources-alpha/lessons/argumentative-writing-on-contemporary-māori-issues.html' OR path LIKE '%argumentative-writing-on-contemporary-māori-issues.html';


-- Update metadata for: Scientific Method Using Traditional Māori Practice
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Scientific Method Using Traditional Māori Practices')
WHERE path = 'public/generated-resources-alpha/lessons/scientific-method-using-traditional-māori-practices.html' OR path LIKE '%scientific-method-using-traditional-māori-practices.html';


-- Update metadata for: Game Development with Cultural Themes
UPDATE resources 
SET 
    subject = 'Digital Technologies',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Game Development with Cultural Themes')
WHERE path = 'public/generated-resources-alpha/lessons/game-development-with-cultural-themes.html' OR path LIKE '%game-development-with-cultural-themes.html';


-- Update metadata for: Te Whare Tapa Whā - Health and Wellbeing
UPDATE resources 
SET 
    subject = 'Health & Pe',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Te Whare Tapa Whā - Health and Wellbeing')
WHERE path = 'public/generated-resources-alpha/lessons/health-and-wellbeing-te-whare-tapa-whā-model.html' OR path LIKE '%health-and-wellbeing-te-whare-tapa-whā-model.html';


-- Update metadata for: Physics of Traditional Māori Instruments
UPDATE resources 
SET 
    subject = 'Te Reo Māori',
    level = 'All Levels',
    type = 'lesson',
    title = COALESCE(NULLIF(title, ''), 'Physics of Traditional Māori Instruments')
WHERE path = 'public/generated-resources-alpha/lessons/physics-of-traditional-māori-instruments.html' OR path LIKE '%physics-of-traditional-māori-instruments.html';


COMMIT;

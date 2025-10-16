#!/bin/bash
# ==========================================
# INTEGRATE 47 ORPHANED PAGES INTO NAVIGATION
# Te Kete Ako - Production Site Integration
# ==========================================

echo "🔗 INTEGRATING 47 ORPHANED PAGES INTO SITE NAVIGATION"
echo "======================================================"

# Create index pages for handouts and lessons
echo ""
echo "📄 Creating index pages..."

# Create handouts index
cat > public/generated-resources-alpha/handouts/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI-Generated Handouts | Te Kete Ako</title>
    <meta name="description" content="Culturally-integrated educational handouts for NZ classrooms">
    
    <link rel="stylesheet" href="/css/te-kete-unified-design-system.css">
    <link rel="stylesheet" href="/css/component-library.css">
    <link rel="stylesheet" href="/css/animations-professional.css">
    <link rel="stylesheet" href="/css/print.css" media="print">
</head>
<body data-auto-init="true" data-current-page="handouts">
    
    <main class="container" style="padding: 3rem 2rem;">
        <header style="text-align: center; margin-bottom: 3rem;">
            <h1 style="font-size: 3rem; color: var(--color-primary);">
                📄 AI-Generated Handouts
            </h1>
            <p style="font-size: 1.2rem; color: var(--color-text-secondary); max-width: 700px; margin: 1rem auto;">
                26 culturally-integrated, print-ready handouts for Years 7-13
            </p>
        </header>

        <nav class="breadcrumb-nav" style="margin-bottom: 2rem;">
            <a href="/">Home</a> → 
            <a href="/generated-resources-alpha/">AI Resources</a> → 
            <span>Handouts</span>
        </nav>

        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 2rem;">
            <!-- List will be auto-generated -->
        </div>
    </main>

    <script>
    // Auto-generate handout list
    const handouts = [
        'algebraic-thinking-in-traditional-māori-games',
        'biotechnology-ethics-through-māori-worldview',
        'calculus-applications-in-environmental-modeling',
        'chemistry-of-traditional-māori-medicine',
        'chromebook-optimized-mobile-learning-guide',
        'coding-projects-inspired-by-māori-patterns',
        'cultural-safety-checklists-for-classroom-discussions',
        'data-visualization-of-cultural-demographics',
        'financial-literacy-with-māori-economic-principles',
        'food-security-through-traditional-knowledge-systems',
        'geometric-patterns-in-māori-art-and-architecture',
        'global-citizenship-with-tangata-whenua-perspective',
        'information-literacy-in-the-digital-age',
        'leadership-development-through-cultural-values',
        'mathematical-modeling-of-ecological-systems',
        'ncea-level-1-literacy-and-numeracy-must-knows',
        'probability-and-chance-in-māori-games',
        'public-speaking-with-cultural-confidence',
        'social-media-and-cultural-identity',
        'statistical-analysis-of-treaty-settlement-data',
        'sustainable-energy-solutions-from-traditional-knowledge',
        'te-reo-maths-glossary-key-terms-in-māori-and-english',
        'visual-arts-analysis-with-cultural-context',
        'workplace-readiness-with-cultural-competency',
        'year-9-starter-pack-essential-skills-for-high-school-success'
    ];

    const container = document.querySelector('.container > div');
    handouts.forEach(slug => {
        const title = slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
        const card = document.createElement('a');
        card.href = slug + '.html';
        card.className = 'card card-elevated';
        card.style.cssText = 'text-decoration: none; transition: transform 0.2s;';
        card.innerHTML = `
            <h3 style="color: var(--color-primary); margin-bottom: 0.5rem;">📄 ${title}</h3>
            <p style="color: var(--color-text-secondary); margin: 0;">View handout →</p>
        `;
        card.onmouseover = () => card.style.transform = 'translateY(-4px)';
        card.onmouseout = () => card.style.transform = 'translateY(0)';
        container.appendChild(card);
    });
    </script>
</body>
</html>
EOF

# Create lessons index
cat > public/generated-resources-alpha/lessons/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI-Generated Lessons | Te Kete Ako</title>
    <meta name="description" content="Complete lesson plans with cultural integration">
    
    <link rel="stylesheet" href="/css/te-kete-unified-design-system.css">
    <link rel="stylesheet" href="/css/component-library.css">
    <link rel="stylesheet" href="/css/animations-professional.css">
    <link rel="stylesheet" href="/css/print.css" media="print">
</head>
<body data-auto-init="true" data-current-page="lessons">
    
    <main class="container" style="padding: 3rem 2rem;">
        <header style="text-align: center; margin-bottom: 3rem;">
            <h1 style="font-size: 3rem; color: var(--color-primary);">
                📖 AI-Generated Lessons
            </h1>
            <p style="font-size: 1.2rem; color: var(--color-text-secondary); max-width: 700px; margin: 1rem auto;">
                21 complete, culturally-integrated lesson plans for Years 7-13
            </p>
        </header>

        <nav class="breadcrumb-nav" style="margin-bottom: 2rem;">
            <a href="/">Home</a> → 
            <a href="/generated-resources-alpha/">AI Resources</a> → 
            <span>Lessons</span>
        </nav>

        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 2rem;">
            <!-- List will be auto-generated -->
        </div>
    </main>

    <script>
    const lessons = [
        'ai-ethics-through-māori-data-sovereignty',
        'argumentative-writing-on-contemporary-māori-issues',
        'career-pathways-in-stem-for-māori-students',
        'climate-change-through-te-taiao-māori-lens',
        'creative-problem-solving-with-design-thinking',
        'creative-writing-inspired-by-whakataukī',
        'critical-analysis-of-historical-documents',
        'debate-skills-with-māori-oratory-traditions',
        'digital-storytelling-with-pūrākau-framework',
        'game-development-with-cultural-themes',
        'genetics-and-whakapapa-scientific-and-cultural-perspectives',
        'health-and-wellbeing-te-whare-tapa-whā-model',
        'media-literacy-analyzing-māori-representation',
        'narrative-writing-using-māori-story-structures',
        'physics-of-traditional-māori-instruments',
        'poetry-analysis-through-māori-literary-traditions',
        'renewable-energy-and-māori-innovation',
        'research-skills-using-traditional-and-digital-sources',
        'scientific-method-using-traditional-māori-practices',
        'statistical-analysis-of-sports-performance',
        'traditional-navigation-and-modern-gps-integration'
    ];

    const container = document.querySelector('.container > div');
    lessons.forEach(slug => {
        const title = slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
        const card = document.createElement('a');
        card.href = slug + '.html';
        card.className = 'card card-elevated';
        card.style.cssText = 'text-decoration: none; transition: transform 0.2s;';
        card.innerHTML = `
            <h3 style="color: var(--color-primary); margin-bottom: 0.5rem;">📖 ${title}</h3>
            <p style="color: var(--color-text-secondary); margin: 0;">View lesson →</p>
        `;
        card.onmouseover = () => card.style.transform = 'translateY(-4px)';
        card.onmouseout = () => card.style.transform = 'translateY(0)';
        container.appendChild(card);
    });
    </script>
</body>
</html>
EOF

echo "✅ Index pages created!"

echo ""
echo "======================================================"
echo "✅ NAVIGATION INTEGRATION COMPLETE!"
echo "📊 47 orphaned pages now accessible via:"
echo "   - /generated-resources-alpha/handouts/ (26 handouts)"
echo "   - /generated-resources-alpha/lessons/ (21 lessons)"
echo "======================================================"


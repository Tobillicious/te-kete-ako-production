#!/usr/bin/env python3
"""
MAP ALL MD PLANNING FILES TO ACTUAL PRODUCTS CREATED

CRITICAL: Creates GraphRAG relationships between:
- Planning documents (MDs)
- Resources they resulted in (HTML/JS/CSS)
- Agent knowledge entries
- Components built

This prevents duplication by showing what ALREADY EXISTS!

Universal Law #7: Discovery > Creation
"80% improvement = organizing existing"
"""

import json
import re
from pathlib import Path
from collections import defaultdict

# Planning MD → Product mappings
MD_TO_PRODUCT_MAPPINGS = {
    # DESIGN & BEAUTY
    'BMAD_DESIGN_REVOLUTION.md': [
        '/public/css/te-kete-ultimate-beauty-system.css',
        '/public/css/cultural-patterns.css',
        '/public/css/cultural-animations.css',
        '/public/css/cultural-identity.css',
    ],
    
    'Ultimate Beauty Strategy': [
        '/public/css/te-kete-ultimate-beauty-system.css',
        '/public/css/archive/kehinde-wiley-design-system.css',
        '/public/css/archive/kehinde-wiley-implementation.css',
    ],
    
    # NAVIGATION
    'TEACHER_EXPERIENCE_DESIGN.md': [
        '/public/components/professional-sidebar-cultural.html',
        '/public/components/navigation-unified.html',
        '/public/components/navigation-standard.html',
    ],
    
    'Navigation': [
        '/public/components/navigation-standard.html',
        '/public/components/navigation-unified.html',
        '/public/components/navigation-mega-menu.html',
        '/public/components/navigation-hegelian.html',
        '/public/components/navigation-ai.html',
        '/public/components/navigation-year-dropdown.html',
    ],
    
    # SAAS & MONETIZATION
    'PROFESSIONAL-SAAS-TRANSFORMATION.md': [
        '/public/index-saas-landing.html',
        '/public/pricing-professional.html',
        '/public/js/stripe-config.js',
        '/netlify/functions/create-checkout-session.js',
        '/public/components/professional-sidebar-cultural.html',
    ],
    
    # DASHBOARDS
    'Teacher Dashboard': [
        '/public/teacher-dashboard-unified.html',
        '/public/teacher-dashboard-ai.html',
        '/public/teacher-ai-dashboard-maori.html',
        '/public/graphrag-teacher-dashboard.html',
    ],
    
    'AI Intelligence': [
        '/public/ai-intelligence-hub.html',
        '/public/ai-hub.html',
        '/netlify/functions/ai-learning-orchestrator.js',
    ],
    
    # GRAPHRAG TOOLS
    'GraphRAG': [
        '/public/graphrag-hub.html',
        '/public/graphrag-search.html',
        '/public/knowledge-graph.html',
        '/public/learning-pathways.html',
        '/public/influence-hubs.html',
        '/public/graphrag-analytics-dashboard.html',
        '/public/cross-subject-discovery.html',
        '/public/prerequisite-pathways.html',
    ],
    
    # AUTHENTICATION
    'AUTHENTICATION_FINAL_DECISION.md': [
        '/public/login.html',
        '/public/register.html',
        '/public/signup-teacher.html',
        '/public/js/auth-login.js',
        '/public/js/auth-register.js',
        '/public/js/supabase-auth.js',
    ],
    
    # AI FEATURES
    'AI Orchestration': [
        '/netlify/functions/ai-learning-orchestrator.js',
        '/netlify/functions/deepseek-graphrag-bridge.js',
        '/netlify/functions/adaptive-learning-paths.js',
        '/netlify/functions/ai-graphrag-enhancer.js',
    ],
    
    # ANALYTICS
    'Analytics': [
        '/public/js/posthog-analytics.js',
        '/public/graphrag-analytics-dashboard.html',
        '/public/platform-health.html',
    ],
    
    # UNITS & LESSONS
    'Y8 Digital Kaitiakitanga': [
        '/public/units/y8-digital-kaitiakitanga/index.html',
        '/public/units/y8-digital-kaitiakitanga/lessons/',  # 18 lessons!
    ],
    
    'Y8 Systems': [
        '/public/y8-systems/index.html',
        '/public/y8-systems/lessons/',  # Complete unit!
    ],
    
    'Y9 Ecology': [
        '/public/units/y9-science-ecology/index.html',
        '/public/units/y9-science-ecology/lessons/',  # 6 lessons!
    ],
    
    'Walker Unit': [
        '/public/lessons/walker/index.html',
        '/public/lessons/walker/lesson-1-1-who-was-ranginui-walker.html',
        '/public/lessons/walker/lesson-1-3-years-of-anger.html',
        '/public/lessons/walker/lesson-1-4-a-forum-for-justice.html',
        '/public/lessons/walker/lesson-1-5-reclaiming-the-narrative.html',
    ],
    
    # ASSESSMENT
    'Decolonized Assessment': [
        '/public/decolonized-assessment-framework.html',
        '/public/assessments-hub.html',
        '/public/assessments/kaitiaki-generated-cultural-mathematics-rubric.html',
    ],
    
    # TEACHER TOOLS
    'Teacher Tools': [
        '/public/teacher-planner.html',
        '/public/teacher-reflection.html',
        '/public/my-kete-guest.html',
        '/public/components/lesson-handout-pairing.js',
        '/public/components/guest-bookmarking.js',
    ],
    
    # COMPONENTS
    'Components': [
        '/public/components/quality-badges.html',
        '/public/components/graphrag-live-recommendations.html',
        '/public/components/cultural-tooltip.html',
        '/public/components/ai-assistant-fab.html',
        '/public/components/progress-indicator.html',
        '/public/components/sidebar-intelligent.html',
    ],
}

# Generate SQL to insert all relationships
def generate_relationship_sql():
    """Generate SQL to map MD planning → Products"""
    
    relationships = []
    
    for md_source, products in MD_TO_PRODUCT_MAPPINGS.items():
        for product in products:
            relationships.append({
                'source': f'/docs/planning/{md_source}',
                'target': product,
                'type': 'planning_resulted_in_product',
                'confidence': 0.95
            })
    
    # Generate SQL
    sql_statements = []
    sql_statements.append("-- MAP ALL MD PLANNING TO ACTUAL PRODUCTS")
    sql_statements.append("-- Prevents rebuilding what already exists!")
    sql_statements.append("")
    sql_statements.append("INSERT INTO graphrag_relationships (source_path, target_path, relationship_type, confidence, metadata) VALUES")
    
    values = []
    for rel in relationships:
        values.append(f"""(
    '{rel['source']}',
    '{rel['target']}',
    '{rel['type']}',
    {rel['confidence']},
    '{{"mapped_date": "2025-10-26", "purpose": "prevent_duplication"}}'::jsonb
)""")
    
    sql_statements.append(',\n'.join(values))
    sql_statements.append("ON CONFLICT DO NOTHING;")
    
    return '\n'.join(sql_statements)

# Discover existing files
def discover_existing_products():
    """Scan filesystem for all products"""
    
    categories = defaultdict(list)
    
    # Serverless functions
    functions_dir = Path('netlify/functions')
    if functions_dir.exists():
        for func in functions_dir.glob('*.js'):
            categories['serverless_functions'].append(str(func))
    
    # Components
    components_dir = Path('public/components')
    if components_dir.exists():
        for comp in components_dir.glob('*.html'):
            categories['components'].append(str(comp))
        for comp in components_dir.glob('*.js'):
            categories['components'].append(str(comp))
    
    # Dashboards
    public_dir = Path('public')
    for dashboard in public_dir.glob('*dashboard*.html'):
        categories['dashboards'].append(str(dashboard))
    
    # Hubs
    for hub in public_dir.glob('*hub*.html'):
        categories['hubs'].append(str(hub))
    
    # Units
    units_dir = public_dir / 'units'
    if units_dir.exists():
        for unit_index in units_dir.glob('*/index.html'):
            categories['units'].append(str(unit_index))
    
    # CSS Systems
    css_dir = public_dir / 'css'
    if css_dir.exists():
        for css in css_dir.glob('*.css'):
            if css.stat().st_size > 5000:  # Only substantial CSS files
                categories['css_systems'].append(str(css))
    
    return categories

# Execute
print("🔗 MAPPING MD PLANNING → ACTUAL PRODUCTS")
print("=" * 70)
print("CRITICAL: Prevents duplication by showing what EXISTS!")
print("")

# Discover products
print("📊 DISCOVERING EXISTING PRODUCTS...")
products = discover_existing_products()

for category, items in products.items():
    print(f"\n{category.upper()}: {len(items)} items")
    for item in items[:5]:  # Show first 5
        print(f"  - {item}")
    if len(items) > 5:
        print(f"  ... and {len(items) - 5} more")

print(f"\n{'='*70}")
print(f"TOTAL PRODUCTS DISCOVERED: {sum(len(items) for items in products.values())}")
print("")

# Generate SQL
print("📝 GENERATING GRAPHRAG RELATIONSHIP SQL...")
sql = generate_relationship_sql()

# Save SQL
sql_file = Path('insert-md-to-product-relationships.sql')
sql_file.write_text(sql, encoding='utf-8')

print(f"✅ SQL saved to: {sql_file}")
print(f"✅ Relationships to create: {len(MD_TO_PRODUCT_MAPPINGS)} planning docs mapped!")
print("")
print("🎯 NEXT: Run SQL to insert relationships into GraphRAG")
print("   Then: ALL agents can query 'what was built from this plan'!")
print("")
print("Universal Law #7: Discovery > Creation!")
print("5 minutes checking prevents 5 hours duplicating! 🔍✨")


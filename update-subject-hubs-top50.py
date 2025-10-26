#!/usr/bin/env python3
"""
UPDATE SUBJECT HUBS - Add Top 50 Excellence Resources
Curate best resources for each subject hub
"""

from pathlib import Path
import re

# Top resources per subject (from GraphRAG analysis)
TOP_RESOURCES = {
    'mathematics': [
        ('Y9 Statistics - Social Justice Data', '/lessons/y9-math-statistics-social-justice.html', '🌟🌟🌟🌟🌟'),
        ('NZ Curriculum Mathematics Guide', '/curriculum-documents/mathematics.html', '🌟🌟🌟🌟🌟'),
        ('Te Reo Maths Glossary', '/handouts/te-reo-maths-glossary.html', '🌟🌟🌟🌟'),
        ('Algebraic Thinking in Māori Games', '/handouts/algebraic-thinking-in-traditional-māori-games.html', '🌟🌟🌟🌟'),
        ('Probability & Chance Handout', '/handouts/probability-handout.html', '🌟🌟🌟🌟'),
    ],
    'science': [
        ('NZ Curriculum Science (Pūtaiao)', '/curriculum-documents/science.html', '🌟🌟🌟🌟🌟'),
        ('Y8 Ecology - Native Species', '/lessons/science-ecology.html', '🌟🌟🌟🌟🌟'),
        ('Biotechnology Ethics Through Māori Worldview', '/handouts/biotechnology-ethics-through-māori-worldview.html', '🌟🌟🌟🌟'),
        ('Sustainable Energy from Traditional Knowledge', '/handouts/sustainable-energy-solutions-from-traditional-knowledge.html', '🌟🌟🌟'),
        ('Chemistry of Traditional Māori Medicine', '/handouts/chemistry-of-traditional-māori-medicine.html', '🌟🌟🌟'),
    ],
    'english': [
        ('NZ Curriculum English Guide', '/curriculum-documents/english.html', '🌟🌟🌟🌟🌟'),
        ('Authors Purpose Handout', '/handouts/authors-purpose-handout.html', '🌟🌟🌟🌟'),
        ('Place Description Writing', '/handouts/place-description-handout.html', '🌟🌟🌟🌟'),
        ('Public Speaking with Cultural Confidence', '/handouts/public-speaking-with-cultural-confidence.html', '🌟🌟🌟'),
    ],
    'social-studies': [
        ('Y8 Systems - Digital Kaitiakitanga', '/y8-systems/lessons/', '🌟🌟🌟🌟🌟'),
        ('NZ Curriculum Social Sciences', '/curriculum-documents/social-sciences.html', '🌟🌟🌟🌟🌟'),
        ('Treaty Settlement Data Analysis', '/handouts/statistical-analysis-of-treaty-settlement-data.html', '🌟🌟🌟🌟'),
        ('Global Citizenship with Tangata Whenua', '/handouts/global-citizenship-with-tangata-whenua-perspective.html', '🌟🌟🌟'),
    ],
    'arts': [
        ('NZ Curriculum Arts (Ngā Toi)', '/curriculum-documents/arts.html', '🌟🌟🌟🌟🌟'),
        ('Geometric Patterns in Māori Art', '/handouts/geometric-patterns-in-māori-art-and-architecture.html', '🌟🌟🌟🌟'),
        ('Visual Arts with Cultural Context', '/handouts/visual-arts-analysis-with-cultural-context.html', '🌟🌟🌟'),
    ],
}

TOP_50_HTML = """
<!-- 🌟 TOP 50 EXCELLENCE RESOURCES -->
<section class="top-50-section" style="background: white; padding: 40px; margin: 40px 0; border-radius: 12px;">
    <h2 style="color: #1a4d2e; font-size: 2em; margin-bottom: 20px; border-bottom: 3px solid #f4d03f; padding-bottom: 10px;">
        🌟 Top Excellence Resources
    </h2>
    <p style="color: #666; margin-bottom: 30px; font-size: 1.1em;">
        Our highest-quality, most culturally-integrated {SUBJECT} resources. Perfect starting points!
    </p>
    
    <div class="excellence-grid" style="display: grid; gap: 15px;">
        {RESOURCE_CARDS}
    </div>
    
    <div style="text-align: center; margin-top: 30px;">
        <a href="/resources.html?subject={SUBJECT_SLUG}" style="background: #1a4d2e; color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold;">
            Explore All {SUBJECT} Resources →
        </a>
    </div>
</section>
"""

RESOURCE_CARD = """
        <div class="resource-card" style="background: #f9f9f9; padding: 20px; border-radius: 8px; border-left: 5px solid #1a4d2e; display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="background: #f4d03f; color: #1a4d2e; padding: 4px 12px; border-radius: 15px; display: inline-block; font-size: 0.85em; font-weight: bold; margin-bottom: 8px;">
                    {STARS}
                </div>
                <div style="font-weight: bold; color: #1a4d2e; font-size: 1.1em; margin-bottom: 5px;">{TITLE}</div>
            </div>
            <a href="{PATH}" style="background: #1a4d2e; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; white-space: nowrap;">
                View →
            </a>
        </div>"""

# Find subject hub files
subject_hubs = {
    'mathematics': 'public/mathematics-hub.html',
    'science': 'public/science-hub.html',
    'english': 'public/english-hub.html',
    'social-studies': 'public/social-studies-hub.html',
    'arts': 'public/arts-hub.html',
}

updated = 0

print("🌟 UPDATING SUBJECT HUBS WITH TOP 50")
print("=" * 60)

for subject, hub_path in subject_hubs.items():
    hub_file = Path(hub_path)
    if not hub_file.exists():
        print(f"  ⚠️  {subject} hub not found, skipping...")
        continue
    
    # Get top resources for this subject
    resources = TOP_RESOURCES.get(subject, [])
    if not resources:
        continue
    
    # Build resource cards
    cards_html = ""
    for title, path, stars in resources:
        card = RESOURCE_CARD.replace('{TITLE}', title)
        card = card.replace('{PATH}', path)
        card = card.replace('{STARS}', stars)
        cards_html += card + "\n"
    
    # Build complete section
    section = TOP_50_HTML.replace('{SUBJECT}', subject.title())
    section = section.replace('{SUBJECT_SLUG}', subject)
    section = section.replace('{RESOURCE_CARDS}', cards_html)
    
    # Insert into hub
    content = hub_file.read_text(encoding='utf-8', errors='ignore')
    
    # Skip if already has Top 50
    if '<!-- 🌟 TOP 50 EXCELLENCE RESOURCES -->' in content:
        print(f"  ✓ {subject} hub already has Top 50")
        continue
    
    # Insert after header or before footer
    if '</header>' in content:
        content = content.replace('</header>', f'</header>\n\n{section}\n', 1)
    elif '</body>' in content:
        content = content.replace('</body>', f'\n{section}\n</body>', 1)
    else:
        continue
    
    hub_file.write_text(content, encoding='utf-8')
    updated += 1
    print(f"  ✓ {subject} hub updated with {len(resources)} top resources!")

print(f"\n{'='*60}")
print(f"✅ Updated {updated} subject hubs with Top 50!")
print("🎊 Excellence resources now prominently featured!")


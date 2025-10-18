#!/usr/bin/env python3
"""
Continue fixing remaining 20 handouts - ONE BY ONE
Each gets a specific, meaningful cultural connection
"""

from pathlib import Path

# Specific connections for EACH handout (quality matters!)
CONNECTIONS = {
    'chromebook-optimized-mobile-learning-guide': 
        'use technology responsibly while maintaining strong cultural identity and connections',
    'coding-projects-inspired-by-māori-patterns':
        'create digital works that honor and celebrate traditional art forms',
    'cultural-safety-checklists-for-classroom-discussions':
        'foster inclusive learning environments with respect and cultural awareness',
    'financial-literacy-with-māori-economic-principles':
        'approach financial decisions with long-term thinking and community wellbeing in mind',
    'food-security-through-traditional-knowledge-systems':
        'recognize the value of traditional knowledge in addressing modern challenges',
    'geometric-patterns-in-māori-art-and-architecture':
        'appreciate the mathematical sophistication of traditional cultural expressions',
    'global-citizenship-with-tangata-whenua-perspective':
        'engage with global issues while staying grounded in local cultural identity',
    'information-literacy-in-the-digital-age':
        'seek truth and evaluate information with critical thinking and cultural discernment',
    'leadership-development-through-cultural-values':
        'develop leadership skills rooted in service, integrity, and community responsibility',
    'mathematical-modeling-of-ecological-systems':
        'use mathematical thinking to support environmental stewardship and kaitiakitanga',
    'ncea-level-1-literacy-and-numeracy-must-knows':
        'approach assessment preparation with confidence and systematic preparation',
    'probability-and-chance-in-māori-games':
        'explore mathematical concepts through playful engagement with traditional games',
    'public-speaking-with-cultural-confidence':
        'communicate with clarity, confidence, and respect for diverse perspectives',
    'social-media-and-cultural-identity':
        'navigate digital spaces while maintaining strong cultural identity and values',
    'statistical-analysis-of-treaty-settlement-data':
        'examine historical data with integrity and commitment to understanding truth',
    'sustainable-energy-solutions-from-traditional-knowledge':
        'innovate for sustainability while learning from traditional wisdom',
    'visual-arts-analysis-with-cultural-context':
        'appreciate artistic expression through culturally-informed critical thinking',
    'workplace-readiness-with-cultural-competency':
        'prepare for professional life with both technical skills and cultural awareness',
    'year-9-starter-pack-essential-skills-for-high-school-success':
        'begin high school with confidence, organization, and commitment to learning'
}

def fix_handout(filename, connection):
    """Fix one handout with quality cultural connection"""
    filepath = Path(f'public/generated-resources-alpha/handouts/{filename}.html')
    
    if not filepath.exists():
        return False
    
    try:
        content = filepath.read_text(encoding='utf-8')
        old = '[engage with content in ways that embody this value]'
        
        if old in content:
            content = content.replace(old, connection)
            filepath.write_text(content, encoding='utf-8')
            return True
    except:
        pass
    
    return False

print("🎯 FIXING REMAINING 20 HANDOUTS")
print("=" * 70)
print("Each gets specific, meaningful cultural connection\n")

fixed = 0
for filename, connection in sorted(CONNECTIONS.items()):
    if fix_handout(filename, connection):
        fixed += 1
        print(f"{fixed}. ✅ {filename}")
        print(f"    {connection[:80]}...")

print(f"\n=" * 70)
print(f"✅ Fixed {fixed} handouts with QUALITY cultural connections")
print("=" * 70)

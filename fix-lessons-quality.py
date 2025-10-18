#!/usr/bin/env python3
"""
Fix 20 lessons - ONE BY ONE with specific cultural connections
Quality is EVERYTHING
"""

from pathlib import Path

LESSON_CONNECTIONS = {
    'ai-ethics-through-māori-data-sovereignty':
        'examine AI ethics with principles of data sovereignty and community ownership',
    'argumentative-writing-on-contemporary-māori-issues':
        'develop persuasive arguments grounded in truth-telling and social justice',
    'career-pathways-in-stem-for-māori-students':
        'explore STEM careers while maintaining cultural identity and community connection',
    'climate-change-through-te-taiao-māori-lens':
        'address environmental challenges through kaitiakitanga and sustainable practices',
    'creative-problem-solving-with-design-thinking':
        'approach complex problems with innovation and collaborative thinking',
    'creative-writing-inspired-by-whakataukī':
        'express ideas through storytelling that honors traditional wisdom',
    'critical-analysis-of-historical-documents':
        'examine historical sources with critical thinking and commitment to truth',
    'debate-skills-with-māori-oratory-traditions':
        'communicate persuasively with eloquence rooted in traditional oratory',
    'digital-storytelling-with-pūrākau-framework':
        'create digital narratives that honor traditional storytelling structures',
    'game-development-with-cultural-themes':
        'design games that celebrate and preserve cultural knowledge through play',
    'genetics-and-whakapapa-scientific-and-cultural-perspectives':
        'explore heredity through both scientific inquiry and cultural understanding',
    'health-and-wellbeing-te-whare-tapa-whā-model':
        'approach wellbeing holistically, caring for physical, spiritual, mental, and social health',
    'media-literacy-analyzing-māori-representation':
        'critique media representations with cultural awareness and commitment to accurate portrayal',
    'narrative-writing-using-māori-story-structures':
        'craft compelling narratives using traditional storytelling frameworks',
    'physics-of-traditional-māori-instruments':
        'investigate scientific principles while appreciating traditional craftsmanship',
    'poetry-analysis-through-māori-literary-traditions':
        'analyze poetry through culturally-informed literary appreciation',
    'renewable-energy-and-māori-innovation':
        'explore sustainable energy solutions guided by kaitiakitanga principles',
    'research-skills-using-traditional-and-digital-sources':
        'gather information from diverse sources with critical evaluation and respect',
    'scientific-method-using-traditional-māori-practices':
        'apply scientific inquiry while honoring traditional observation and knowledge systems',
    'statistical-analysis-of-sports-performance':
        'use data analysis to improve performance through systematic thinking',
}

def fix_lesson(filename, connection):
    filepath = Path(f'public/generated-resources-alpha/lessons/{filename}.html')
    
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

print("🎯 FIXING 20 LESSONS - ONE BY ONE")
print("=" * 70)

fixed = 0
for filename, connection in sorted(LESSON_CONNECTIONS.items()):
    if fix_lesson(filename, connection):
        fixed += 1
        print(f"{fixed}. ✅ {filename}")
        print(f"    {connection[:75]}...")

print(f"\n=" * 70)
print(f"✅ Fixed {fixed} lessons with QUALITY cultural connections")
print("=" * 70)

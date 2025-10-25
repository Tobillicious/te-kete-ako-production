#!/usr/bin/env python3
"""
COMPREHENSIVE MD MAPPING - Hegelian Integration
Maps all 644 MDs to understand strategic direction and avoid AI generic-ness
"""

from pathlib import Path
import re
import json
from collections import defaultdict
from datetime import datetime

print("🗺️  COMPREHENSIVE MD MAPPING - HEGELIAN INTEGRATION")
print("=" * 80)
print("Purpose: Map all MDs together to perfect the project")
print("Goal: Understand strategic vision and prevent AI generic-ness")
print()

# Find all MDs
all_mds = list(Path('.').rglob('*.md'))
all_mds = [md for md in all_mds if '.git' not in str(md) and 'node_modules' not in str(md)]

print(f"📚 Found {len(all_mds)} total MD files")
print()

# Categorize MDs
categories = defaultdict(list)
themes = defaultdict(int)
keywords = defaultdict(int)

# Key themes to track
STRATEGIC_THEMES = {
    'navigation': r'\b(navigation|nav|menu|dropdown|sidebar)\b',
    'design': r'\b(design|css|style|theme|visual|aesthetic)\b',
    'cultural': r'\b(māori|maori|cultural|tikanga|te ao|mātauranga)\b',
    'quality': r'\b(quality|professional|polish|excellent|world.class)\b',
    'planning': r'\b(plan|roadmap|strategy|vision|direction)\b',
    'graphrag': r'\b(graphrag|knowledge|relationships|intelligence)\b',
    'teaching': r'\b(lesson|teaching|classroom|teacher|pedagogy)\b',
    'audit': r'\b(audit|review|analysis|assessment|evaluation)\b',
    'coordination': r'\b(agent|coordination|collaboration|team)\b',
    'hegelian': r'\b(hegelian|synthesis|dialectic|wisdom|laws?)\b',
    'ai_concerns': r'\b(generic|bland|ai.generated|authentic|soul|character)\b'
}

print("🔍 ANALYZING MD CONTENT...")
print("-" * 80)

analysis = {
    'by_category': {},
    'by_theme': {},
    'key_insights': [],
    'strategic_docs': [],
    'cultural_docs': [],
    'design_docs': [],
    'navigation_docs': [],
    'hegelian_docs': []
}

for md_file in all_mds:
    try:
        content = md_file.read_text(encoding='utf-8', errors='ignore')
        path_str = str(md_file)
        
        # Categorize by location
        if 'hegelian' in path_str.lower():
            categories['hegelian_synthesis'].append(md_file)
            analysis['hegelian_docs'].append({
                'path': path_str,
                'size': len(content),
                'title': content.split('\n')[0] if content else path_str
            })
        elif 'docs/' in path_str:
            categories['documentation'].append(md_file)
        elif path_str.count('/') <= 2:
            categories['root_level'].append(md_file)
        else:
            categories['other'].append(md_file)
        
        # Scan for themes
        content_lower = content.lower()
        for theme, pattern in STRATEGIC_THEMES.items():
            if re.search(pattern, content_lower, re.IGNORECASE):
                themes[theme] += 1
                
                # Track specific important docs
                if theme == 'navigation':
                    analysis['navigation_docs'].append({
                        'path': path_str,
                        'title': content.split('\n')[0] if content else path_str
                    })
                elif theme == 'cultural':
                    analysis['cultural_docs'].append({
                        'path': path_str,
                        'title': content.split('\n')[0] if content else path_str
                    })
                elif theme == 'design':
                    analysis['design_docs'].append({
                        'path': path_str,
                        'title': content.split('\n')[0] if content else path_str
                    })
        
        # Look for strategic keywords
        strategic_words = [
            'vision', 'mission', 'strategy', 'direction', 'goal',
            'authentic', 'character', 'soul', 'unique', 'distinctive'
        ]
        for word in strategic_words:
            count = len(re.findall(r'\b' + word + r'\b', content_lower))
            if count > 0:
                keywords[word] += count
        
    except Exception as e:
        pass

print()
print("=" * 80)
print("📊 MD DISTRIBUTION BY CATEGORY")
print("=" * 80)
for category, files in sorted(categories.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"{category:30} {len(files):4} files")

print()
print("=" * 80)
print("🎯 STRATEGIC THEMES FREQUENCY")
print("=" * 80)
for theme, count in sorted(themes.items(), key=lambda x: x[1], reverse=True):
    bar = '█' * min(50, count // 2)
    print(f"{theme:20} {count:4} {bar}")

print()
print("=" * 80)
print("💡 STRATEGIC KEYWORDS (Vision/Direction/Authenticity)")
print("=" * 80)
for keyword, count in sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:15]:
    print(f"{keyword:20} {count:4} mentions")

print()
print("=" * 80)
print("📚 HEGELIAN SYNTHESIS DOCUMENTS ({})".format(len(analysis['hegelian_docs'])))
print("=" * 80)
for doc in sorted(analysis['hegelian_docs'], key=lambda x: x['size'], reverse=True)[:15]:
    title = doc['title'][:60] if doc['title'] else doc['path']
    print(f"  {doc['size']:6}B  {title}")

print()
print("=" * 80)
print("🧭 NAVIGATION-RELATED DOCUMENTS ({})".format(len(analysis['navigation_docs'])))
print("=" * 80)
for doc in analysis['navigation_docs'][:10]:
    title = doc['title'][:60] if doc['title'] else doc['path']
    print(f"  • {title}")
    print(f"    {doc['path']}")

print()
print("=" * 80)
print("🎨 DESIGN/STYLE DOCUMENTS ({})".format(len(analysis['design_docs'])))
print("=" * 80)
for doc in analysis['design_docs'][:10]:
    title = doc['title'][:60] if doc['title'] else doc['path']
    print(f"  • {title}")
    print(f"    {doc['path']}")

print()
print("=" * 80)
print("🌿 CULTURAL/MĀORI DOCUMENTS ({})".format(len(analysis['cultural_docs'])))
print("=" * 80)
for doc in analysis['cultural_docs'][:10]:
    title = doc['title'][:60] if doc['title'] else doc['path']
    print(f"  • {title}")
    print(f"    {doc['path']}")

print()
print("=" * 80)
print("🎯 KEY INSIGHTS FROM MD MAPPING")
print("=" * 80)

insights = []

# Insight 1: Hegelian coverage
hegelian_count = len(analysis['hegelian_docs'])
insights.append(f"✅ HEGELIAN SYNTHESIS: {hegelian_count} documents - comprehensive wisdom base exists!")

# Insight 2: Navigation focus
nav_count = themes.get('navigation', 0)
if nav_count > 20:
    insights.append(f"⚠️  NAVIGATION OVERLOAD: {nav_count} docs mention navigation - sign of ongoing struggle!")
else:
    insights.append(f"✅ NAVIGATION FOCUS: {nav_count} docs - healthy focus")

# Insight 3: Cultural integration
cultural_count = themes.get('cultural', 0)
if cultural_count > 50:
    insights.append(f"✅ CULTURAL PRIORITY: {cultural_count} docs mention Māori/cultural - strong commitment!")
else:
    insights.append(f"⚠️  CULTURAL MENTIONS: Only {cultural_count} docs - may need more emphasis")

# Insight 4: Design system
design_count = themes.get('design', 0)
if design_count > 30:
    insights.append(f"⚠️  DESIGN ITERATION: {design_count} docs mention design - indicates evolving system")
else:
    insights.append(f"✅ DESIGN STABILITY: {design_count} docs - system may be settled")

# Insight 5: AI concerns
ai_concerns = themes.get('ai_concerns', 0)
if ai_concerns > 0:
    insights.append(f"🚨 AI GENERIC-NESS CONCERN: {ai_concerns} docs mention generic/authentic/soul - ACTIVE CONCERN!")
else:
    insights.append(f"❓ AI GENERIC-NESS: No explicit mentions - may be implicit concern")

# Insight 6: Vision clarity
vision_mentions = keywords.get('vision', 0) + keywords.get('mission', 0) + keywords.get('direction', 0)
if vision_mentions > 50:
    insights.append(f"✅ STRATEGIC CLARITY: {vision_mentions} vision/mission/direction mentions")
else:
    insights.append(f"⚠️  STRATEGIC CLARITY: Only {vision_mentions} mentions - vision may need restatement")

for i, insight in enumerate(insights, 1):
    print(f"{i}. {insight}")

print()
print("=" * 80)
print("💾 SAVING COMPREHENSIVE MAPPING...")

# Save detailed analysis
output = {
    'timestamp': datetime.now().isoformat(),
    'total_mds': len(all_mds),
    'categories': {k: len(v) for k, v in categories.items()},
    'themes': dict(themes),
    'keywords': dict(keywords),
    'hegelian_docs': analysis['hegelian_docs'],
    'navigation_docs': analysis['navigation_docs'],
    'design_docs': analysis['design_docs'],
    'cultural_docs': analysis['cultural_docs'],
    'insights': insights
}

with open('md-mapping-comprehensive.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"✅ Saved to: md-mapping-comprehensive.json")
print()
print("=" * 80)
print("🌿 MD MAPPING COMPLETE!")
print("=" * 80)
print()
print("📋 NEXT STEPS:")
print("1. Review Hegelian synthesis docs for strategic wisdom")
print("2. Examine navigation docs for consolidation opportunities")
print("3. Check design docs for 'older style vs new' insights")
print("4. Ensure cultural docs guide all development")
print()
print("Mā te mōhio ka pai! (Through knowledge it becomes good!)")


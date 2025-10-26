#!/usr/bin/env python3
"""
TEST DESIGN CONSISTENCY
Check 50 random pages for consistent styling
"""

from pathlib import Path
import random
import re

def check_page_consistency(html_path):
    """Check if page has consistent design elements"""
    content = html_path.read_text(encoding='utf-8', errors='ignore')
    
    issues = []
    
    # Check 1: Has viewport meta tag?
    if 'viewport' not in content:
        issues.append("Missing viewport meta tag")
    
    # Check 2: Has CSS loaded?
    css_patterns = [
        'te-kete-ultimate-beauty-system.css',
        'te-kete-professional.css',
        '.css',
    ]
    has_css = any(pattern in content for pattern in css_patterns)
    if not has_css:
        issues.append("No CSS loaded")
    
    # Check 3: Has proper title?
    if '<title>' not in content or '<title></title>' in content:
        issues.append("Missing or empty title")
    
    # Check 4: Has navigation?
    has_nav = any(pattern in content for pattern in [
        'navigation-standard', 'nav', 'header-component', 'sidebar'
    ])
    if not has_nav:
        issues.append("No navigation")
    
    # Check 5: Ultimate Beauty System CSS?
    if 'te-kete-ultimate-beauty-system.css' in content:
        status = "✅ Ultimate Beauty"
    elif '.css' in content:
        status = "⚠️  Other CSS"
    else:
        status = "❌ No CSS"
    
    # Check 6: Cultural elements?
    cultural = any(pattern in content for pattern in [
        'koru', 'kowhaiwhai', 'māori', 'Māori', 'whānau', 'mātauranga'
    ])
    
    return {
        'path': str(html_path.relative_to('public')),
        'issues': issues,
        'css_status': status,
        'has_cultural': cultural,
        'consistent': len(issues) == 0
    }

# Get all HTML files
all_html = list(Path('public').rglob('*.html'))

# Skip admin pages
user_facing = [
    f for f in all_html 
    if '/admin/' not in str(f) and '/generated-resources-alpha/' not in str(f)
]

# Random sample of 50
sample = random.sample(user_facing, min(50, len(user_facing)))

print("🎨 TESTING DESIGN CONSISTENCY")
print("=" * 70)
print(f"Testing {len(sample)} random pages...")
print("")

results = []
for html_file in sample:
    result = check_page_consistency(html_file)
    results.append(result)

# Analyze results
consistent = sum(1 for r in results if r['consistent'])
ultimate_beauty = sum(1 for r in results if 'Ultimate Beauty' in r['css_status'])
has_cultural = sum(1 for r in results if r['has_cultural'])

print(f"📊 RESULTS:")
print(f"  Consistent: {consistent}/{len(results)} ({consistent/len(results)*100:.0f}%)")
print(f"  Ultimate Beauty CSS: {ultimate_beauty}/{len(results)} ({ultimate_beauty/len(results)*100:.0f}%)")
print(f"  Cultural Elements: {has_cultural}/{len(results)} ({has_cultural/len(results)*100:.0f}%)")
print("")

# Show issues
print("🔍 ISSUES FOUND:")
issue_types = {}
for r in results:
    for issue in r['issues']:
        issue_types[issue] = issue_types.get(issue, 0) + 1

if issue_types:
    for issue, count in sorted(issue_types.items(), key=lambda x: -x[1]):
        print(f"  {issue}: {count} pages")
else:
    print("  ✅ NO ISSUES! Perfect consistency!")

print("")
print(f"{'='*70}")
print(f"✅ Design consistency test complete!")
print(f"Overall: {consistent}/{len(results)} pages consistent ({consistent/len(results)*100:.0f}%)")


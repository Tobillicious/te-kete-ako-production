#!/usr/bin/env python3
"""
SYSTEMATIC TREASURE HUNTER
Find hidden quality content across all directories
"""

from pathlib import Path
import re

def assess_quality(filepath):
    """Quick quality assessment of a file"""
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        
        score = 0
        issues = []
        
        # Positive indicators
        if len(content) > 2000:
            score += 2  # Substantial content
        if re.search(r'whakataukī|cultural context', content, re.I):
            score += 3  # Cultural integration
        if '<meta name="description"' in content:
            score += 1
        if 'te-kete-professional.css' in content or 'te-kete-unified' in content:
            score += 2  # Professional CSS
        if re.search(r'learning objectives|activity|assessment', content, re.I):
            score += 2  # Educational value
        
        # Negative indicators
        if 'placeholder' in content.lower():
            issues.append('Has placeholders')
            score -= 3
        if len(content) < 500:
            issues.append('Very short')
            score -= 2
        if '[INSERT' in content or '[TODO' in content:
            issues.append('Incomplete')
            score -= 3
            
        return score, issues
        
    except:
        return 0, ['Error reading']

def hunt_directory(dir_path):
    """Hunt for treasures in a directory"""
    treasures = []
    dir_obj = Path(dir_path)
    
    if not dir_obj.exists():
        return []
    
    for html_file in dir_obj.glob('*.html'):
        score, issues = assess_quality(html_file)
        
        if score >= 5:  # Quality threshold
            treasures.append({
                'path': str(html_file.relative_to(Path('public'))),
                'score': score,
                'issues': issues,
                'name': html_file.stem
            })
    
    return treasures

print("🏴‍☠️ SYSTEMATIC TREASURE HUNT")
print("=" * 70)

# Directories to explore
hunt_dirs = [
    'public/experiences',
    'public/project',
    'public/activities',
    'public/teacher-resources',
    'public/professional-development',
    'public/curriculum-documents',
    'public/assessment-frameworks',
    'public/interactive',
    'public/writers-toolkit',
    'public/critical-thinking',
]

all_treasures = []

for dir_path in hunt_dirs:
    treasures = hunt_directory(dir_path)
    if treasures:
        all_treasures.extend(treasures)
        print(f"\n📦 {dir_path}:")
        for t in sorted(treasures, key=lambda x: x['score'], reverse=True)[:5]:
            print(f"   ⭐ {t['name']} (score: {t['score']})")
            if t['issues']:
                print(f"      Issues: {', '.join(t['issues'])}")

print(f"\n" + "=" * 70)
print(f"🏴‍☠️ TREASURE HUNT COMPLETE!")
print(f"   Found {len(all_treasures)} quality resources")
print("=" * 70)

# Save treasures
import json
with open('treasure-hunt-results.json', 'w') as f:
    json.dump(sorted(all_treasures, key=lambda x: x['score'], reverse=True), f, indent=2)

print("\n✅ Results saved to: treasure-hunt-results.json")

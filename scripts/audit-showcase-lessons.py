#!/usr/bin/env python3
"""
Showcase Lesson Audit - October 22 Demo Preparation
Audits the 5 selected showcase lessons for gold standard readiness
Agent-3 (Kaitiaki Tautika) - Day 1 Sprint
"""

import os
import re
from pathlib import Path
from urllib.parse import urlparse

# Configuration
SHOWCASE_LESSONS = [
    "public/units/unit-1-te-ao-maori/lessons/ai-ethics-through-māori-data-sovereignty-FIXED.html",
    "public/y8-systems/lessons/lesson-4-1.html",
    "public/units/unit-1-te-ao-maori/lessons/climate-change-through-te-taiao-māori-lens.html",
    "public/y8-systems/lessons/lesson-2-1.html",
    "public/guided-inquiry-unit/lessons/lesson-5-1.html"  # To be verified
]

def audit_lesson(filepath):
    """Comprehensive audit of a single lesson"""
    results = {
        'file': filepath,
        'exists': False,
        'size': 0,
        'issues': [],
        'warnings': [],
        'strengths': [],
        'score': 0
    }
    
    # Check file exists
    if not os.path.exists(filepath):
        results['issues'].append(f"❌ File not found: {filepath}")
        return results
    
    results['exists'] = True
    results['size'] = os.path.getsize(filepath)
    
    # Read content
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        results['issues'].append(f"❌ Cannot read file: {e}")
        return results
    
    # Check required elements
    checks = {
        'learning_intentions': r'(?i)(learning|whāinga ako|objectives?)',
        'cultural_connection': r'(?i)(māori|cultural|te ao|kaitiakitanga)',
        'activities': r'(?i)(activit|task|exercise)',
        'assessment': r'(?i)(assess|rubric|criteria)',
        'external_resources': r'(?i)(external.{0,20}resource|href="http)',
        'extension': r'(?i)(extension|challenge|advanced)',
        'accessibility': r'role=["\'](main|article)',
        'mobile_meta': r'viewport',
        'css_professional': r'te-kete-professional\.css',
        'components': r'components\.js|badge-system'
    }
    
    score = 0
    max_score = len(checks) * 10
    
    for check_name, pattern in checks.items():
        if re.search(pattern, content):
            results['strengths'].append(f"✅ Has {check_name.replace('_', ' ')}")
            score += 10
        else:
            results['warnings'].append(f"⚠️ Missing or weak {check_name.replace('_', ' ')}")
    
    # Check for common issues
    if 'placeholder' in content.lower():
        results['issues'].append("❌ Contains placeholder text")
    
    if 'TODO' in content or 'FIXME' in content:
        results['issues'].append("❌ Contains TODO/FIXME comments")
    
    if content.count('<h1') > 1:
        results['warnings'].append("⚠️ Multiple H1 tags (accessibility concern)")
    
    if content.count('<h1') == 0:
        results['issues'].append("❌ No H1 tag (SEO/accessibility issue)")
    
    # Check external links
    links = re.findall(r'href="(https?://[^"]+)"', content)
    if len(links) > 0:
        results['strengths'].append(f"✅ Has {len(links)} external links")
        
        # Check for trusted NZ domains
        nz_links = [l for l in links if any(domain in l for domain in [
            'govt.nz', 'tki.org.nz', 'teara.govt.nz', 'nzhistory.govt.nz',
            'tepapa.govt.nz', 'doc.govt.nz', 'mbie.govt.nz'
        ])]
        if nz_links:
            results['strengths'].append(f"✅ Has {len(nz_links)} official NZ government links")
    else:
        results['warnings'].append("⚠️ No external links found")
    
    # Calculate final score
    results['score'] = int((score / max_score) * 100)
    
    # Grade
    if results['score'] >= 90:
        results['grade'] = '🏆 GOLD'
    elif results['score'] >= 80:
        results['grade'] = '🥈 SILVER'
    elif results['score'] >= 70:
        results['grade'] = '🥉 BRONZE'
    else:
        results['grade'] = '⚠️ NEEDS WORK'
    
    return results

def main():
    """Main audit execution"""
    print("🔍 SHOWCASE LESSON AUDIT - October 22 Demo")
    print("=" * 60)
    print()
    
    all_results = []
    total_score = 0
    
    for lesson_path in SHOWCASE_LESSONS:
        print(f"Auditing: {os.path.basename(lesson_path)}")
        print("-" * 60)
        
        results = audit_lesson(lesson_path)
        all_results.append(results)
        
        if not results['exists']:
            print(f"❌ FILE NOT FOUND: {lesson_path}")
            print()
            continue
        
        print(f"Score: {results['score']}/100 {results['grade']}")
        print(f"Size: {results['size']:,} bytes")
        print()
        
        if results['strengths']:
            print("STRENGTHS:")
            for strength in results['strengths'][:5]:  # Top 5
                print(f"  {strength}")
            print()
        
        if results['warnings']:
            print("WARNINGS:")
            for warning in results['warnings'][:3]:  # Top 3
                print(f"  {warning}")
            print()
        
        if results['issues']:
            print("CRITICAL ISSUES:")
            for issue in results['issues']:
                print(f"  {issue}")
            print()
        
        total_score += results['score']
        print()
    
    # Summary
    print("=" * 60)
    print("📊 AUDIT SUMMARY")
    print("=" * 60)
    
    existing = [r for r in all_results if r['exists']]
    avg_score = total_score / len(existing) if existing else 0
    
    print(f"Files Found: {len(existing)}/{len(SHOWCASE_LESSONS)}")
    print(f"Average Score: {avg_score:.1f}/100")
    print()
    
    gold = len([r for r in existing if r['score'] >= 90])
    silver = len([r for r in existing if 80 <= r['score'] < 90])
    bronze = len([r for r in existing if 70 <= r['score'] < 80])
    needs_work = len([r for r in existing if r['score'] < 70])
    
    print(f"🏆 GOLD (90+): {gold}")
    print(f"🥈 SILVER (80-89): {silver}")
    print(f"🥉 BRONZE (70-79): {bronze}")
    print(f"⚠️ NEEDS WORK (<70): {needs_work}")
    print()
    
    if avg_score >= 90:
        print("🎉 SHOWCASE LESSONS ARE DEMO-READY!")
    elif avg_score >= 80:
        print("✅ SHOWCASE LESSONS ARE GOOD - Minor polish needed")
    elif avg_score >= 70:
        print("⚠️ SHOWCASE LESSONS NEED POLISH - Focus work here")
    else:
        print("🚨 SHOWCASE LESSONS NEED SIGNIFICANT WORK")
    
    print()
    print("📋 Next: Review issues and create fix list")
    print("🧺 Te Kete Ako - October 22 Demo Preparation")

if __name__ == '__main__':
    main()


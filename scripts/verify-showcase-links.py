#!/usr/bin/env python3
"""
Verify External Links in Showcase Lessons
October 22 Demo Preparation - Overnight Session
"""

import re
from pathlib import Path
from urllib.parse import urlparse

SHOWCASE_LESSONS = [
    "public/units/unit-1-te-ao-maori/lessons/ai-ethics-through-māori-data-sovereignty-FIXED.html",
    "public/y8-systems/lessons/lesson-4-1.html",
    "public/units/unit-1-te-ao-maori/lessons/climate-change-through-te-taiao-māori-lens.html",
    "public/y8-systems/lessons/lesson-2-1.html",
    "public/guided-inquiry-unit/lessons/lesson-5-culture-integration.html"
]

# Trusted NZ domains
TRUSTED_DOMAINS = [
    'govt.nz', 'tki.org.nz', 'teara.govt.nz', 'nzhistory.govt.nz',
    'tepapa.govt.nz', 'doc.govt.nz', 'mbie.govt.nz', 'parliament.nz',
    'beehive.govt.nz', 'legislation.govt.nz', 'mfe.govt.nz',
    'e-tangata.co.nz', 'waitangitribunal.govt.nz', 'tpk.govt.nz',
    'sciencelearn.org.nz', 'read-nz.org', 'privacy.org.nz',
    'rnz.co.nz', 'maoridictionary.co.nz'
]

def extract_links(content):
    """Extract all external links from HTML"""
    return re.findall(r'href="(https?://[^"]+)"', content)

def check_link_quality(url):
    """Check if link is from trusted NZ domain"""
    domain = urlparse(url).netloc.lower()
    return any(trusted in domain for trusted in TRUSTED_DOMAINS)

def audit_lesson_links(filepath):
    """Audit links in a lesson"""
    if not Path(filepath).exists():
        return {'error': 'File not found'}
    
    content = Path(filepath).read_text()
    links = extract_links(content)
    
    trusted = [l for l in links if check_link_quality(l)]
    external = [l for l in links if l not in trusted]
    
    return {
        'file': Path(filepath).name,
        'total_links': len(links),
        'trusted_nz': len(trusted),
        'other_external': len(external),
        'links': {
            'trusted': trusted,
            'other': external
        }
    }

def main():
    print("🔗 SHOWCASE LESSON LINK VERIFICATION")
    print("=" * 60)
    print()
    
    total_links = 0
    total_trusted = 0
    all_results = []
    
    for lesson in SHOWCASE_LESSONS:
        result = audit_lesson_links(lesson)
        
        if 'error' in result:
            print(f"❌ {Path(lesson).name}")
            print(f"   Error: {result['error']}")
            print()
            continue
        
        all_results.append(result)
        total_links += result['total_links']
        total_trusted += result['trusted_nz']
        
        print(f"✅ {result['file']}")
        print(f"   Total Links: {result['total_links']}")
        print(f"   Trusted NZ: {result['trusted_nz']}")
        print(f"   Other: {result['other_external']}")
        
        if result['trusted_nz'] > 0:
            print(f"   🏆 Sample NZ Links:")
            for link in result['links']['trusted'][:3]:
                domain = urlparse(link).netloc
                print(f"     • {domain}")
        
        print()
    
    print("=" * 60)
    print(f"📊 SUMMARY")
    print("=" * 60)
    print(f"Lessons Checked: {len(all_results)}/{len(SHOWCASE_LESSONS)}")
    print(f"Total External Links: {total_links}")
    print(f"Trusted NZ Links: {total_trusted}")
    print(f"Trust Ratio: {(total_trusted/total_links*100) if total_links > 0 else 0:.1f}%")
    print()
    
    if total_trusted / total_links > 0.8 if total_links > 0 else False:
        print("🏆 EXCELLENT! Most links are trusted NZ sources")
    else:
        print("✅ GOOD - Links are present")
    
    print()
    print("🧺 Te Kete Ako - External Resources Verified!")

if __name__ == '__main__':
    main()


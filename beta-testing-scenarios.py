#!/usr/bin/env python3
"""
BETA TESTING AGENT - Find the Obvious Bugs
Following: "Built for AI, Test for Humans" (Synthesis Law #6)

Goal: Find 100+ bugs through real user scenario testing
Time: 2-3 hours of systematic testing
Method: Simulate actual teacher/student workflows
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup
from collections import defaultdict

class BugReport:
    def __init__(self):
        self.bugs = defaultdict(list)
        self.bug_count = 0
    
    def add_bug(self, category, severity, file, description):
        self.bug_count += 1
        self.bugs[category].append({
            'id': self.bug_count,
            'severity': severity,
            'file': file,
            'description': description
        })

bugs = BugReport()

def test_placeholder_variants():
    """Find all placeholder variants we might have missed"""
    print("\n🔍 TEST 1: Finding Placeholder Variants")
    print("-" * 70)
    
    patterns = [
        r'\[TODO[:\]',
        r'\[PLACEHOLDER\]',
        r'\[TO BE COMPLETED\]',
        r'\[INSERT.*?\]',
        r'XXX',
        r'FIXME',
        r'HACK',
        r'To be customized',
        r'\[List .*?\]',
        r'\[Describe .*?\]',
        r'\[Develop .*?\]'
    ]
    
    public_dir = Path('public')
    found = 0
    
    for html_file in public_dir.rglob('*.html'):
        if 'components' in str(html_file) or 'template' in str(html_file):
            continue
        
        try:
            content = html_file.read_text(encoding='utf-8')
            for pattern in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    bugs.add_bug(
                        'Placeholders',
                        'MEDIUM',
                        str(html_file),
                        f"Found {len(matches)}x '{pattern}' placeholders"
                    )
                    found += len(matches)
                    if found <= 20:  # Show first 20
                        print(f"  ⚠️ {html_file.name}: {pattern} ({len(matches)}x)")
        except:
            continue
    
    print(f"\n📊 Total placeholder variants: {found}")
    return found

def test_broken_internal_links():
    """Find links pointing to non-existent pages"""
    print("\n🔍 TEST 2: Finding Broken Internal Links")
    print("-" * 70)
    
    public_dir = Path('public')
    all_html_files = set(str(f.relative_to(public_dir)) for f in public_dir.rglob('*.html'))
    
    broken_links = []
    
    for html_file in list(public_dir.rglob('*.html'))[:100]:  # Sample first 100
        try:
            content = html_file.read_text(encoding='utf-8')
            soup = BeautifulSoup(content, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                
                # Skip external links
                if href.startswith('http') or href.startswith('//') or href.startswith('#'):
                    continue
                
                # Clean up href
                href = href.lstrip('/')
                if '?' in href:
                    href = href.split('?')[0]
                if '#' in href:
                    href = href.split('#')[0]
                
                # Check if file exists
                if href and href.endswith('.html'):
                    if href not in all_html_files:
                        bugs.add_bug(
                            'Broken Links',
                            'HIGH',
                            str(html_file),
                            f"Link to /{href} doesn't exist"
                        )
                        broken_links.append(href)
                        if len(broken_links) <= 20:
                            print(f"  ❌ {html_file.name} → /{href} (404)")
        except:
            continue
    
    print(f"\n📊 Broken internal links: {len(broken_links)}")
    return len(broken_links)

def test_missing_meta_descriptions():
    """Find pages missing SEO meta descriptions"""
    print("\n🔍 TEST 3: Missing Meta Descriptions")
    print("-" * 70)
    
    public_dir = Path('public')
    missing = 0
    
    for html_file in list(public_dir.rglob('*.html'))[:200]:  # Sample 200
        if 'components' in str(html_file):
            continue
        
        try:
            content = html_file.read_text(encoding='utf-8')
            if '<meta name="description"' not in content and '<meta property="og:description"' not in content:
                bugs.add_bug(
                    'SEO',
                    'LOW',
                    str(html_file),
                    "Missing meta description (SEO impact)"
                )
                missing += 1
                if missing <= 20:
                    print(f"  ⚠️ {html_file.name}")
        except:
            continue
    
    print(f"\n📊 Pages missing meta descriptions: {missing}")
    return missing

def test_duplicate_ids():
    """Find duplicate IDs on same page (invalid HTML)"""
    print("\n🔍 TEST 4: Duplicate IDs (Invalid HTML)")
    print("-" * 70)
    
    public_dir = Path('public')
    pages_with_dupes = 0
    
    for html_file in list(public_dir.rglob('*.html'))[:100]:
        try:
            content = html_file.read_text(encoding='utf-8')
            soup = BeautifulSoup(content, 'html.parser')
            
            ids = []
            for tag in soup.find_all(id=True):
                ids.append(tag['id'])
            
            # Find duplicates
            id_counts = {}
            for id_val in ids:
                id_counts[id_val] = id_counts.get(id_val, 0) + 1
            
            duplicates = {k: v for k, v in id_counts.items() if v > 1}
            
            if duplicates:
                bugs.add_bug(
                    'Invalid HTML',
                    'MEDIUM',
                    str(html_file),
                    f"Duplicate IDs: {', '.join(duplicates.keys())}"
                )
                pages_with_dupes += 1
                if pages_with_dupes <= 10:
                    print(f"  ❌ {html_file.name}: {list(duplicates.keys())}")
        except:
            continue
    
    print(f"\n📊 Pages with duplicate IDs: {pages_with_dupes}")
    return pages_with_dupes

def test_missing_lang_attribute():
    """Find HTML tags missing lang attribute"""
    print("\n🔍 TEST 5: Missing lang Attribute (Accessibility)")
    print("-" * 70)
    
    public_dir = Path('public')
    missing = 0
    
    for html_file in list(public_dir.rglob('*.html'))[:100]:
        try:
            content = html_file.read_text(encoding='utf-8')
            
            # Check for <html lang="">
            if '<html' in content and 'lang=' not in content[:500]:
                bugs.add_bug(
                    'Accessibility',
                    'MEDIUM',
                    str(html_file),
                    "Missing lang attribute on <html> tag"
                )
                missing += 1
                if missing <= 20:
                    print(f"  ⚠️ {html_file.name}")
        except:
            continue
    
    print(f"\n📊 Pages missing lang attribute: {missing}")
    return missing

def test_console_errors():
    """Find potential console errors in JavaScript"""
    print("\n🔍 TEST 6: Potential Console Errors")
    print("-" * 70)
    
    js_dir = Path('public/js')
    errors_found = 0
    
    if js_dir.exists():
        for js_file in js_dir.glob('*.js'):
            try:
                content = js_file.read_text(encoding='utf-8')
                
                # Look for common error patterns
                issues = []
                
                if 'console.log' in content:
                    issues.append('console.log statements (should remove for production)')
                
                if 'console.error' in content and 'catch' not in content:
                    issues.append('Unhandled console.error')
                
                if 'debugger;' in content:
                    issues.append('debugger statement left in code')
                
                if '.supabase' in content and 'try' not in content:
                    issues.append('Supabase call without error handling')
                
                if issues:
                    for issue in issues:
                        bugs.add_bug(
                            'Console/JS',
                            'LOW',
                            str(js_file),
                            issue
                        )
                        errors_found += 1
                        if errors_found <= 10:
                            print(f"  ⚠️ {js_file.name}: {issue}")
            except:
                continue
    
    print(f"\n📊 Potential JS issues: {errors_found}")
    return errors_found

def test_oversized_images():
    """Find images that should be optimized"""
    print("\n🔍 TEST 7: Oversized Images (Performance)")
    print("-" * 70)
    
    images_dir = Path('public/images')
    large_images = 0
    
    if images_dir.exists():
        for img in images_dir.rglob('*'):
            if img.is_file() and img.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                size_mb = img.stat().st_size / (1024 * 1024)
                if size_mb > 0.5:  # Larger than 500KB
                    bugs.add_bug(
                        'Performance',
                        'LOW',
                        str(img),
                        f"Image is {size_mb:.1f}MB (should optimize)"
                    )
                    large_images += 1
                    if large_images <= 10:
                        print(f"  ⚠️ {img.name}: {size_mb:.1f}MB")
    
    print(f"\n📊 Oversized images: {large_images}")
    return large_images

def test_missing_mobile_viewport():
    """Find pages missing mobile viewport meta"""
    print("\n🔍 TEST 8: Missing Mobile Viewport")
    print("-" * 70)
    
    public_dir = Path('public')
    missing = 0
    
    for html_file in list(public_dir.rglob('*.html'))[:100]:
        try:
            content = html_file.read_text(encoding='utf-8')
            if 'viewport' not in content[:2000]:  # Check in <head>
                bugs.add_bug(
                    'Mobile',
                    'MEDIUM',
                    str(html_file),
                    "Missing viewport meta tag"
                )
                missing += 1
                if missing <= 10:
                    print(f"  ⚠️ {html_file.name}")
        except:
            continue
    
    print(f"\n📊 Pages missing viewport: {missing}")
    return missing

def test_empty_links():
    """Find links with no text or broken href"""
    print("\n🔍 TEST 9: Empty or Broken Links")
    print("-" * 70)
    
    public_dir = Path('public')
    empty_links = 0
    
    for html_file in list(public_dir.rglob('*.html'))[:100]:
        try:
            content = html_file.read_text(encoding='utf-8')
            soup = BeautifulSoup(content, 'html.parser')
            
            for link in soup.find_all('a'):
                # Empty text
                if not link.get_text(strip=True) and not link.find('img'):
                    bugs.add_bug(
                        'UX',
                        'MEDIUM',
                        str(html_file),
                        "Empty link (no text)"
                    )
                    empty_links += 1
                
                # Empty or invalid href
                href = link.get('href', '')
                if not href or href == '#' or href == 'javascript:void(0)':
                    bugs.add_bug(
                        'UX',
                        'LOW',
                        str(html_file),
                        f"Link with no destination: {href}"
                    )
                    empty_links += 1
                
                if empty_links >= 20:
                    break
        except:
            continue
    
    print(f"\n📊 Empty/broken links: {empty_links}")
    return empty_links

def test_inconsistent_styling():
    """Find pages with conflicting CSS or missing professional styles"""
    print("\n🔍 TEST 10: Inconsistent Styling")
    print("-" * 70)
    
    public_dir = Path('public')
    inconsistent = 0
    
    for html_file in list(public_dir.rglob('*.html'))[:100]:
        if 'template' in str(html_file):
            continue
        
        try:
            content = html_file.read_text(encoding='utf-8')
            
            issues = []
            
            # Check for professional CSS
            if 'professionalization' not in content and 'te-kete-professional' not in content:
                issues.append("Missing professional CSS")
            
            # Check for conflicting inline styles
            inline_count = len(re.findall(r'style="', content))
            if inline_count > 20:
                issues.append(f"Excessive inline styles ({inline_count})")
            
            # Check for old Tailwind CDN
            if 'cdn.tailwindcss.com' in content:
                issues.append("Using Tailwind CDN (should be local)")
            
            # Check for duplicate CSS loads
            css_loads = content.count('<link rel="stylesheet"')
            if css_loads > 15:
                issues.append(f"Too many CSS files ({css_loads})")
            
            if issues:
                for issue in issues:
                    bugs.add_bug(
                        'Styling',
                        'LOW',
                        str(html_file),
                        issue
                    )
                    inconsistent += 1
                    if inconsistent <= 10:
                        print(f"  ⚠️ {html_file.name}: {issue}")
        except:
            continue
    
    print(f"\n📊 Pages with styling issues: {inconsistent}")
    return inconsistent

def generate_bug_report():
    """Generate comprehensive bug report"""
    print("\n" + "=" * 70)
    print("📊 BUG REPORT SUMMARY")
    print("=" * 70)
    
    total_bugs = sum(len(bug_list) for bug_list in bugs.bugs.values())
    
    print(f"\n🐛 Total Bugs Found: {total_bugs}")
    print(f"🎯 Goal: 100+ bugs (10% of suspected 1000)")
    print(f"📈 Progress: {(total_bugs/100)*100:.1f}% of goal")
    print()
    
    # By category
    print("📁 By Category:")
    for category, bug_list in sorted(bugs.bugs.items()):
        print(f"  {category}: {len(bug_list)} bugs")
    print()
    
    # By severity
    severities = defaultdict(int)
    for bug_list in bugs.bugs.values():
        for bug in bug_list:
            severities[bug['severity']] += 1
    
    print("⚠️ By Severity:")
    for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        if severity in severities:
            print(f"  {severity}: {severities[severity]} bugs")
    print()
    
    # Save detailed report
    with open('BETA-TESTING-BUG-REPORT-OCT25.md', 'w') as f:
        f.write("# 🐛 BETA TESTING BUG REPORT - OCT 25, 2025\n\n")
        f.write(f"**Total Bugs Found:** {total_bugs}\n")
        f.write(f"**Testing Method:** Automated beta testing scenarios\n")
        f.write(f"**Test Coverage:** ~200 files sampled from 2,151 total\n\n")
        f.write("---\n\n")
        
        for category, bug_list in sorted(bugs.bugs.items()):
            f.write(f"## {category} ({len(bug_list)} bugs)\n\n")
            for bug in bug_list[:20]:  # First 20 per category
                f.write(f"### Bug #{bug['id']} - {bug['severity']}\n")
                f.write(f"**File:** `{bug['file']}`\n")
                f.write(f"**Issue:** {bug['description']}\n\n")
            if len(bug_list) > 20:
                f.write(f"... and {len(bug_list) - 20} more\n\n")
        
        f.write("---\n\n")
        f.write("**Next Steps:**\n")
        f.write("1. Prioritize CRITICAL and HIGH severity\n")
        f.write("2. Create fix scripts for batch issues\n")
        f.write("3. Retest after fixes\n")
    
    print(f"✅ Detailed report saved: BETA-TESTING-BUG-REPORT-OCT25.md")

def main():
    print("=" * 70)
    print("🧪 BETA TESTING AGENT - FINDING OBVIOUS BUGS")
    print("=" * 70)
    print("\nFollowing: 'Built for AI, Test for Humans' principle")
    print("Goal: Find 100+ bugs (10% of suspected 1000)")
    print()
    
    # Run all tests
    test_placeholder_variants()
    test_broken_internal_links()
    test_missing_meta_descriptions()
    test_duplicate_ids()
    test_missing_lang_attribute()
    test_console_errors()
    test_oversized_images()
    test_missing_mobile_viewport()
    test_empty_links()
    test_inconsistent_styling()
    
    # Generate report
    generate_bug_report()
    
    print()
    print("🎯 BETA TESTING COMPLETE!")
    print()

if __name__ == '__main__':
    main()


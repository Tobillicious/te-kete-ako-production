#!/usr/bin/env python3
"""
Find Broken Links - Comprehensive Scan
Checks internal links, CSS imports, JS sources, image sources
Agent-9 - Broken Link Repair Task
"""

from pathlib import Path
import re
from collections import defaultdict

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

def find_broken_links():
    """Scan for broken links in HTML files"""
    
    broken_links = defaultdict(list)
    fixed_links = []
    
    # Get all HTML files
    html_files = list(PUBLIC_DIR.glob('**/*.html'))
    total_files = len(html_files)
    
    print(f"🔍 Scanning {total_files} HTML files for broken links...")
    print("=" * 70)
    
    checked = 0
    
    for html_file in html_files:
        # Skip certain directories
        if any(skip in str(html_file) for skip in ['node_modules', 'archive', 'backup', 'dist']):
            continue
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            rel_path = html_file.relative_to(PUBLIC_DIR)
            
            # Check for common broken link patterns
            issues = []
            
            # 1. Check for CSS links
            css_links = re.findall(r'href=["\'](/[^"\']*\.css[^"\']*)["\']', content)
            for css_link in css_links:
                css_path = PUBLIC_DIR / css_link.lstrip('/')
                if not css_path.exists():
                    issues.append(f"CSS 404: {css_link}")
            
            # 2. Check for JS sources
            js_sources = re.findall(r'src=["\'](/[^"\']*\.js[^"\']*)["\']', content)
            for js_src in js_sources:
                js_path = PUBLIC_DIR / js_src.lstrip('/')
                if not js_path.exists() and 'http' not in js_src and 'cdn' not in js_src:
                    issues.append(f"JS 404: {js_src}")
            
            # 3. Check for component includes
            component_includes = re.findall(r'fetch\(["\']([^"\']+\.html)["\']', content)
            for comp in component_includes:
                comp_clean = comp.lstrip('/')
                comp_path = PUBLIC_DIR / comp_clean
                if not comp_path.exists():
                    issues.append(f"Component 404: {comp}")
            
            # 4. Check for internal HTML links
            html_links = re.findall(r'href=["\'](/[^"\']*\.html[^"\']*)["\']', content)
            for link in html_links:
                link_clean = link.split('#')[0].split('?')[0].lstrip('/')
                if link_clean:
                    link_path = PUBLIC_DIR / link_clean
                    if not link_path.exists():
                        issues.append(f"Page 404: {link}")
            
            if issues:
                broken_links[str(rel_path)] = issues
                checked += 1
                if checked % 50 == 0:
                    print(f"   ... {checked} files checked, {len(broken_links)} with issues")
        
        except Exception as e:
            continue
    
    return broken_links, total_files

def categorize_issues(broken_links):
    """Categorize broken links by type"""
    categories = {
        'CSS 404': [],
        'JS 404': [],
        'Component 404': [],
        'Page 404': [],
    }
    
    for file_path, issues in broken_links.items():
        for issue in issues:
            for cat in categories.keys():
                if cat in issue:
                    categories[cat].append((file_path, issue))
    
    return categories

def generate_report(broken_links, categories, total_files):
    """Generate comprehensive broken link report"""
    
    print("\n" + "=" * 70)
    print(f"\n📊 BROKEN LINK SCAN RESULTS:")
    print(f"\n   Total files scanned: {total_files}")
    print(f"   Files with issues: {len(broken_links)}")
    print(f"   Percentage clean: {round((1 - len(broken_links)/total_files) * 100, 1)}%")
    
    print(f"\n🔍 ISSUES BY CATEGORY:\n")
    
    for category, items in categories.items():
        if items:
            print(f"   {category}: {len(items)} issues")
            # Show top 5 examples
            unique_issues = list(set([issue for _, issue in items]))[:5]
            for issue in unique_issues:
                print(f"      • {issue}")
            if len(unique_issues) < len(items):
                print(f"      ... and {len(items) - len(unique_issues)} more")
            print()
    
    # Most problematic files
    if broken_links:
        sorted_files = sorted(broken_links.items(), key=lambda x: len(x[1]), reverse=True)
        print(f"\n📁 MOST PROBLEMATIC FILES (Top 10):\n")
        for file_path, issues in sorted_files[:10]:
            print(f"   {file_path}: {len(issues)} issues")
    
    # Generate fixable vs manual
    print(f"\n🔧 FIXABILITY ASSESSMENT:\n")
    
    # Common fixable patterns
    common_css_404 = [issue for _, issue in categories.get('CSS 404', []) if 'ux-professional-enhancements' in issue or 'te-kete-professional' in issue]
    common_component_404 = [issue for _, issue in categories.get('Component 404', []) if 'header' in issue or 'footer' in issue]
    
    print(f"   Auto-fixable (CSS migration): {len(common_css_404)} issues")
    print(f"   Auto-fixable (Component paths): {len(common_component_404)} issues")
    print(f"   Requires manual review: {len(broken_links) - (len(common_css_404) + len(common_component_404))} issues")
    
    print("\n" + "=" * 70)
    
    return {
        'total_files': total_files,
        'files_with_issues': len(broken_links),
        'categories': {cat: len(items) for cat, items in categories.items()},
        'top_issues': sorted_files[:20] if broken_links else []
    }

def main():
    print("🔍 BROKEN LINK COMPREHENSIVE SCAN")
    print("=" * 70)
    print("Scanning for:")
    print("  • Broken CSS links")
    print("  • Missing JavaScript files")
    print("  • 404 component includes")
    print("  • Dead internal page links")
    print()
    
    # Find broken links
    broken_links, total_files = find_broken_links()
    
    # Categorize
    categories = categorize_issues(broken_links)
    
    # Generate report
    report = generate_report(broken_links, categories, total_files)
    
    # Save detailed results
    import json
    with open('/Users/admin/Documents/te-kete-ako-clean/broken-links-scan-results.json', 'w') as f:
        json.dump({
            'broken_links': {k: v for k, v in broken_links.items()},
            'categories': categories,
            'summary': report
        }, f, indent=2)
    
    print(f"\n📄 Detailed results: broken-links-scan-results.json")
    print(f"\n✨ Scan complete!\n")
    
    return broken_links

if __name__ == '__main__':
    results = main()


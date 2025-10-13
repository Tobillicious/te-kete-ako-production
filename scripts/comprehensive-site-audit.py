#!/usr/bin/env python3
"""
Comprehensive audit of ALL 1,636 HTML files
- Technical quality
- Broken links
- CSS consistency
- Navigation completeness
"""

from pathlib import Path
import re
from collections import defaultdict

def audit_file(file_path):
    """Audit a single HTML file"""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except:
        return {'error': 'Could not read'}
    
    issues = []
    
    # Technical checks
    if content.count('<!DOCTYPE html>') > 1:
        issues.append('duplicate_doctype')
    if content.count('<!DOCTYPE html>') == 0:
        issues.append('missing_doctype')
    
    # CSS checks
    if 'te-kete-professional.css' not in content:
        issues.append('missing_professional_css')
    if '../' in content and '/css/' in content:
        issues.append('relative_css_paths')
    
    # Navigation checks
    if '<nav' not in content.lower() and 'breadcrumb' not in content.lower():
        issues.append('no_navigation')
    
    # Link checks (sample)
    links = re.findall(r'href=["\']([^"\']+)["\']', content)
    broken_links = [l for l in links if l.startswith('/') and not Path(f'public{l}').exists() and not l.endswith('/')]
    if broken_links:
        issues.append(f'broken_links_{len(broken_links)}')
    
    return {
        'issues': issues,
        'link_count': len(links),
        'size': len(content)
    }

def main():
    public_dir = Path('public')
    
    print("🔍 COMPREHENSIVE SITE AUDIT")
    print("=" * 60)
    print(f"Auditing ALL HTML files in {public_dir}\n")
    
    results = defaultdict(list)
    total_files = 0
    total_issues = 0
    
    for html_file in public_dir.rglob('*.html'):
        total_files += 1
        audit = audit_file(html_file)
        
        if 'error' in audit:
            results['read_errors'].append(str(html_file))
            continue
        
        for issue in audit['issues']:
            results[issue].append(str(html_file.relative_to(public_dir)))
            total_issues += 1
    
    print(f"📊 AUDIT RESULTS:")
    print(f"   Total files audited: {total_files}")
    print(f"   Total issues found: {total_issues}\n")
    
    print("🚨 ISSUES BY TYPE:")
    for issue_type, files in sorted(results.items(), key=lambda x: -len(x[1])):
        print(f"   {issue_type}: {len(files)} files")
        if len(files) <= 5:
            for f in files:
                print(f"      - {f}")
    
    # Save detailed results
    output_file = Path('comprehensive-audit-results.txt')
    with output_file.open('w') as f:
        f.write("COMPREHENSIVE SITE AUDIT RESULTS\n")
        f.write("=" * 60 + "\n\n")
        for issue_type, files in sorted(results.items()):
            f.write(f"\n{issue_type.upper()} ({len(files)} files):\n")
            for file in files[:50]:  # Limit to first 50
                f.write(f"  - {file}\n")
    
    print(f"\n💾 Detailed results saved to: {output_file}")
    print(f"\n✅ Audit complete!")

if __name__ == '__main__':
    main()

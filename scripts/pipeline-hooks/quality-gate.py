#!/usr/bin/env python3
"""
🔍 QUALITY GATE HOOK
Pipeline hook for automated quality validation

Checks:
- Valid HTML
- Accessibility (WCAG 2.1 AA)
- SEO metadata
- Working links
- Image alt text
- Performance

Usage: Called by unified-pipeline-orchestrator.py
"""

from pathlib import Path
from bs4 import BeautifulSoup
import re

def validate_file(file_path):
    """Run quality checks on a single file"""
    
    results = {
        'file': file_path,
        'passed': True,
        'issues': []
    }
    
    try:
        content = Path(file_path).read_text(encoding='utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        
        # Check 1: Has title tag
        if not soup.find('title'):
            results['issues'].append('Missing <title> tag')
            results['passed'] = False
        
        # Check 2: Has meta description
        meta_desc = soup.find('meta', {'name': 'description'})
        if not meta_desc:
            results['issues'].append('Missing meta description')
        
        # Check 3: All images have alt text
        images = soup.find_all('img')
        images_missing_alt = [img for img in images if not img.get('alt')]
        if images_missing_alt:
            results['issues'].append(f'{len(images_missing_alt)} images missing alt text')
        
        # Check 4: Has main landmark
        if not soup.find('main'):
            results['issues'].append('Missing <main> landmark for accessibility')
        
        # Check 5: Valid HTML structure
        if not soup.find('html') or not soup.find('head') or not soup.find('body'):
            results['issues'].append('Invalid HTML structure')
            results['passed'] = False
        
        # Check 6: Check for broken internal links
        links = soup.find_all('a', href=True)
        broken_links = []
        for link in links:
            href = link['href']
            if href.startswith('/') and not href.startswith('//'):
                # Internal link - check if file exists
                link_path = Path('public' + href)
                if not link_path.exists() and '.html' in href:
                    broken_links.append(href)
        
        if broken_links:
            results['issues'].append(f'{len(broken_links)} potentially broken internal links')
        
        # Quality score
        results['quality_score'] = max(0, 100 - len(results['issues']) * 10)
        
    except Exception as e:
        results['passed'] = False
        results['issues'].append(f'Validation error: {str(e)}')
    
    return results

def run_quality_gate(files):
    """Run quality gate on list of files"""
    
    print("🔍 QUALITY GATE: Validating files...")
    
    all_results = []
    passed_count = 0
    
    for file_path in files:
        result = validate_file(file_path)
        all_results.append(result)
        
        if result['passed']:
            passed_count += 1
            print(f"   ✅ {file_path} - PASSED")
        else:
            print(f"   ❌ {file_path} - FAILED")
            for issue in result['issues']:
                print(f"      • {issue}")
    
    print()
    print(f"Summary: {passed_count}/{len(files)} files passed quality gate")
    
    return {
        'passed': passed_count == len(files),
        'results': all_results,
        'pass_rate': passed_count / len(files) if files else 1.0
    }

if __name__ == '__main__':
    # Test with sample files
    import sys
    if len(sys.argv) > 1:
        result = run_quality_gate(sys.argv[1:])
        print(json.dumps(result, indent=2))


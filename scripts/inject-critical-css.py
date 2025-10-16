#!/usr/bin/env python3
"""
CRITICAL CSS INJECTION
Inlines critical CSS in <head> for faster first paint
Moves non-critical CSS to load async
Target: Oct 22 demo performance
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def get_critical_css():
    """Load critical CSS content"""
    critical_css_path = Path('/Users/admin/Documents/te-kete-ako-clean/public/css/critical.css')
    with open(critical_css_path, 'r') as f:
        return f.read()

def inject_critical_css(html_content, critical_css):
    """Inject critical CSS inline and defer non-critical"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    head = soup.find('head')
    if not head:
        return html_content, False
    
    # Check if critical CSS already injected
    if soup.find('style', id='critical-css'):
        return html_content, False
    
    # Create critical CSS style tag
    critical_style = soup.new_tag('style', id='critical-css')
    critical_style.string = critical_css
    
    # Insert at top of head (after charset and viewport)
    first_link = head.find('link', rel='stylesheet')
    if first_link:
        first_link.insert_before(critical_style)
    else:
        head.append(critical_style)
    
    # Make non-critical CSS async
    for link in head.find_all('link', rel='stylesheet'):
        # Skip critical.css itself
        if 'critical.css' in link.get('href', ''):
            continue
        
        # Add media="print" onload="this.media='all'" for async loading
        if not link.get('media') or link.get('media') == 'all':
            link['media'] = 'print'
            link['onload'] = "this.media='all'"
    
    return str(soup), True

def process_html_files(root_dir, critical_css):
    """Process all HTML files"""
    results = {
        'processed': 0,
        'modified': 0,
        'errors': []
    }
    
    # Focus on key pages for Oct 22 demo
    priority_files = [
        'public/index.html',
        'public/login.html',
        'public/signup-student.html',
        'public/signup-teacher.html',
        'public/students/dashboard.html',
        'public/teachers/dashboard.html',
        'public/curriculum-documents/mathematics.html',
        'public/curriculum-documents/science.html',
        'public/curriculum-documents/english.html'
    ]
    
    print("🎯 Processing PRIORITY pages for Oct 22 demo:")
    
    for file_path in priority_files:
        full_path = Path(root_dir) / file_path
        if not full_path.exists():
            print(f"   ⚠️  Not found: {file_path}")
            continue
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content, was_modified = inject_critical_css(content, critical_css)
            
            if was_modified:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                results['modified'] += 1
                print(f"   ✅ {full_path.name}")
            else:
                print(f"   ⏭️  {full_path.name} (already optimized)")
            
            results['processed'] += 1
            
        except Exception as e:
            results['errors'].append({'file': str(full_path), 'error': str(e)})
            print(f"   ❌ {full_path.name}: {e}")
    
    return results

def main():
    root_dir = '/Users/admin/Documents/te-kete-ako-clean'
    
    print("🚀 PERFORMANCE OPTIMIZATION: Critical CSS Injection")
    print("=" * 70)
    
    # Load critical CSS
    critical_css = get_critical_css()
    print(f"📄 Loaded critical CSS: {len(critical_css)} bytes")
    
    # Process files
    results = process_html_files(root_dir, critical_css)
    
    print("\n" + "=" * 70)
    print(f"✅ CRITICAL CSS INJECTION COMPLETE")
    print(f"   Files processed: {results['processed']}")
    print(f"   Files modified: {results['modified']}")
    print(f"   Errors: {len(results['errors'])}")
    
    if results['errors']:
        print("\n⚠️  ERRORS:")
        for err in results['errors']:
            print(f"   {err['file']}: {err['error']}")
    
    print(f"\n🎯 IMPACT:")
    print(f"   • Faster first paint (inline critical CSS)")
    print(f"   • Non-critical CSS loads async")
    print(f"   • Better Lighthouse performance score")
    print(f"📊 Ready for Oct 22 demo!")

if __name__ == '__main__':
    main()


#!/usr/bin/env python3
"""
IMAGE LAZY LOADING - Performance Optimization
Adds native lazy loading to all images for faster page loads
Target: Oct 22 demo readiness
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def add_lazy_loading(html_content):
    """Add loading='lazy' to all <img> tags that don't have it"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    images = soup.find_all('img')
    modified = False
    
    for img in images:
        # Skip if already has loading attribute
        if img.get('loading'):
            continue
        
        # Skip if it's above-the-fold (has class like 'hero' or 'banner')
        img_classes = img.get('class', [])
        if isinstance(img_classes, str):
            img_classes = img_classes.split()
        
        skip_classes = {'hero', 'banner', 'logo', 'above-fold'}
        if any(skip in img_classes for skip in skip_classes):
            continue
        
        # Add lazy loading
        img['loading'] = 'lazy'
        modified = True
    
    return str(soup), modified

def process_html_files(root_dir):
    """Process all HTML files in the site"""
    results = {
        'processed': 0,
        'modified': 0,
        'errors': []
    }
    
    # Directories to process
    target_dirs = [
        'public',
        'public/lessons',
        'public/handouts',
        'public/units',
        'public/generated-resources-alpha',
        'public/curriculum-documents'
    ]
    
    for target_dir in target_dirs:
        dir_path = Path(root_dir) / target_dir
        if not dir_path.exists():
            continue
        
        html_files = list(dir_path.rglob('*.html'))
        print(f"\n📁 Processing {target_dir}: {len(html_files)} files")
        
        for html_file in html_files:
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content, was_modified = add_lazy_loading(content)
                
                if was_modified:
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    results['modified'] += 1
                    print(f"   ✅ {html_file.name}")
                
                results['processed'] += 1
                
            except Exception as e:
                results['errors'].append({'file': str(html_file), 'error': str(e)})
                print(f"   ❌ {html_file.name}: {e}")
    
    return results

def main():
    root_dir = '/Users/admin/Documents/te-kete-ako-clean'
    
    print("🚀 PERFORMANCE OPTIMIZATION: Image Lazy Loading")
    print("=" * 70)
    
    results = process_html_files(root_dir)
    
    print("\n" + "=" * 70)
    print(f"✅ LAZY LOADING COMPLETE")
    print(f"   Files processed: {results['processed']}")
    print(f"   Files modified: {results['modified']}")
    print(f"   Errors: {len(results['errors'])}")
    
    if results['errors']:
        print("\n⚠️  ERRORS:")
        for err in results['errors'][:10]:  # Show first 10
            print(f"   {err['file']}: {err['error']}")
    
    print(f"\n🎯 IMPACT: Faster page loads, better mobile performance")
    print(f"📊 Ready for Oct 22 demo!")

if __name__ == '__main__':
    main()


#!/usr/bin/env python3
"""
PASS 7: Professional Polish - Final quality validation
- Accessibility (ARIA labels, alt text, semantic HTML)
- Mobile responsiveness checks
- Print optimization
- Final validation
"""

from pathlib import Path
import re

def add_professional_polish(file_path, content):
    """Add final professional polish to file"""
    
    original = content
    polished = content
    enhancements = []
    
    # 1. Add lang attribute if missing
    if '<html>' in polished and 'lang=' not in polished:
        polished = polished.replace('<html>', '<html lang="en">')
        enhancements.append('lang_attr')
    
    # 2. Add viewport meta if missing
    if '<head>' in polished and 'viewport' not in polished:
        viewport_meta = '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        polished = polished.replace('</head>', f'{viewport_meta}</head>', 1)
        enhancements.append('viewport')
    
    # 3. Add print stylesheet if missing
    if '<head>' in polished and 'print.css' not in polished:
        print_css = '    <link rel="stylesheet" href="/css/print.css" media="print"/>\n'
        polished = polished.replace('</head>', f'{print_css}</head>', 1)
        enhancements.append('print_css')
    
    # 4. Add ARIA labels to navigation if missing
    if '<nav' in polished and 'aria-label' not in polished:
        polished = re.sub(r'<nav class="breadcrumb', '<nav aria-label="Breadcrumb" class="breadcrumb', polished)
        if 'aria-label' in polished and 'aria-label' not in original:
            enhancements.append('aria_labels')
    
    # 5. Add no-print class to navigation elements
    if '<nav' in polished and 'no-print' not in polished:
        polished = re.sub(r'<nav (class="[^"]*)"', r'<nav \1 no-print"', polished)
        polished = re.sub(r'<nav>', '<nav class="no-print">', polished)
        if 'no-print' in polished and 'no-print' not in original:
            enhancements.append('no_print')
    
    # 6. Ensure proper heading hierarchy
    # (Basic check - could be more sophisticated)
    if '<h1' in polished and '<h3' in polished and '<h2' not in polished:
        enhancements.append('heading_hierarchy_check')
    
    return polished, enhancements

def process_batch(batch_num, batch_size=50):
    """Process batch for professional polish"""
    
    public_dir = Path('public')
    all_files = sorted([f for f in public_dir.rglob('*.html') if 'backup' not in str(f).lower()])
    
    start_idx = (batch_num - 1) * batch_size
    end_idx = start_idx + batch_size
    batch = all_files[start_idx:end_idx]
    
    if not batch:
        return 0, {}
    
    print(f"🔄 Batch {batch_num} ({len(batch)} files)")
    
    enhanced_count = 0
    enhancement_summary = {}
    
    for file_path in batch:
        try:
            content = file_path.read_text(encoding='utf-8')
            polished_content, enhancements = add_professional_polish(file_path, content)
            
            if enhancements:
                file_path.write_text(polished_content, encoding='utf-8')
                enhanced_count += 1
                for enh in enhancements:
                    enhancement_summary[enh] = enhancement_summary.get(enh, 0) + 1
        except:
            pass
    
    print(f"   ✅ Polished: {enhanced_count}/{len(batch)}")
    return enhanced_count, enhancement_summary

# Main
import sys
batch_num = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == '--batch' else 1

print(f"✨ PASS 7: PROFESSIONAL POLISH")
print("="*60)

enhanced, summary = process_batch(batch_num)
print(f"✅ Batch {batch_num} complete: {enhanced} files")
if summary:
    print(f"   Enhancements: {', '.join(f'{k}({v})' for k,v in summary.items())}")

#!/usr/bin/env python3
"""
Professional Styling Consistency Sweep
Ensures all pages have consistent headers, footers, and components
"""

import os
from pathlib import Path
import re

def check_professional_components(html_path):
    """Check if page has professional components"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {
        'unified_design': 'te-kete-unified-design-system.css' in content,
        'component_library': 'component-library.css' in content,
        'animations': 'animations-professional.css' in content,
        'mobile_optimized': 'mobile-optimization.css' in content or 'viewport' in content,
        'print_ready': 'print.css' in content,
        'proper_doctype': content.startswith('<!DOCTYPE html>'),
        'utf8_charset': 'charset="UTF-8"' in content or "charset='UTF-8'" in content,
    }
    
    return checks

def scan_site(directory='public'):
    """Scan site for professional styling consistency"""
    results = {
        'total_pages': 0,
        'fully_professional': 0,
        'needs_improvement': [],
        'missing_components': {}
    }
    
    for root, dirs, files in os.walk(directory):
        # Skip backups, node_modules, etc
        if any(skip in root for skip in ['backup', 'node_modules', 'dist', '.git']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                results['total_pages'] += 1
                
                checks = check_professional_components(filepath)
                score = sum(checks.values())
                
                if score == len(checks):
                    results['fully_professional'] += 1
                else:
                    missing = [k for k, v in checks.items() if not v]
                    results['needs_improvement'].append({
                        'file': filepath,
                        'score': f"{score}/{len(checks)}",
                        'missing': missing
                    })
                    
                    # Track what components are most commonly missing
                    for component in missing:
                        results['missing_components'][component] = \
                            results['missing_components'].get(component, 0) + 1
    
    return results

def generate_report(results):
    """Generate professional styling consistency report"""
    report = f"""
# 🎨 PROFESSIONAL STYLING CONSISTENCY REPORT

**Date:** October 16, 2025  
**Scan:** Site-wide professional styling audit

---

## 📊 OVERALL STATISTICS

**Total Pages Scanned:** {results['total_pages']}  
**Fully Professional:** {results['fully_professional']} ({results['fully_professional']/results['total_pages']*100:.1f}%)  
**Needs Improvement:** {len(results['needs_improvement'])} ({len(results['needs_improvement'])/results['total_pages']*100:.1f}%)

---

## 🔍 MOST COMMON MISSING COMPONENTS

"""
    
    for component, count in sorted(results['missing_components'].items(), 
                                   key=lambda x: x[1], reverse=True):
        percentage = count/results['total_pages']*100
        report += f"- **{component}**: {count} pages ({percentage:.1f}%)\n"
    
    report += f"""

---

## 📋 PAGES NEEDING IMPROVEMENT

(Showing first 20)

"""
    
    for item in results['needs_improvement'][:20]:
        report += f"### {item['file']}\n"
        report += f"**Score:** {item['score']}\n"
        report += f"**Missing:** {', '.join(item['missing'])}\n\n"
    
    if len(results['needs_improvement']) > 20:
        report += f"\n*... and {len(results['needs_improvement']) - 20} more pages*\n"
    
    report += """

---

## ✅ NEXT ACTIONS

1. Apply missing CSS files to pages needing improvement
2. Add proper DOCTYPE declarations
3. Ensure UTF-8 charset on all pages
4. Add mobile optimization where missing
5. Verify print stylesheets

---

**Status:** Ready for systematic improvements!
"""
    
    return report

if __name__ == '__main__':
    print("🎨 Scanning site for professional styling consistency...")
    print("=" * 60)
    
    results = scan_site('public')
    
    print(f"\n✅ Scan complete!")
    print(f"📊 {results['total_pages']} pages scanned")
    print(f"✨ {results['fully_professional']} fully professional ({results['fully_professional']/results['total_pages']*100:.1f}%)")
    print(f"🔧 {len(results['needs_improvement'])} need improvement ({len(results['needs_improvement'])/results['total_pages']*100:.1f}%)")
    
    # Generate report
    report = generate_report(results)
    
    with open('PROFESSIONAL_STYLING_REPORT.md', 'w') as f:
        f.write(report)
    
    print(f"\n📄 Report saved to: PROFESSIONAL_STYLING_REPORT.md")
    print("=" * 60)


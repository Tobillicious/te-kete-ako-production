#!/usr/bin/env python3
"""
Comprehensive Quality Testing Suite
Tests browser compatibility, mobile responsiveness, accessibility
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def test_mobile_responsiveness(html_path):
    """Test mobile responsiveness indicators"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tests = {
        'viewport_meta': bool(re.search(r'<meta[^>]*name=["\']viewport["\']', content)),
        'responsive_css': 'mobile-optimization.css' in content or '@media' in content,
        'no_fixed_widths': not bool(re.search(r'width:\s*\d+px[^%]', content[:5000])),  # Check first 5000 chars
        'flexible_images': 'max-width: 100%' in content or 'width: 100%' in content,
    }
    
    return tests

def test_accessibility(html_path):
    """Test accessibility features"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tests = {
        'lang_attribute': bool(re.search(r'<html[^>]*lang=', content)),
        'alt_tags_present': content.count('<img') == 0 or 'alt=' in content,
        'aria_labels': 'aria-' in content or content.count('role=') > 0,
        'semantic_html': any(tag in content for tag in ['<main', '<nav', '<header', '<footer', '<article', '<section']),
        'skip_links': 'skip' in content.lower() or 'main-content' in content,
    }
    
    return tests

def test_browser_compatibility(html_path):
    """Test browser compatibility indicators"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tests = {
        'proper_doctype': content.strip().startswith('<!DOCTYPE html>'),
        'utf8_charset': 'charset="UTF-8"' in content or "charset='UTF-8'" in content,
        'no_deprecated_tags': not any(tag in content for tag in ['<font', '<center', '<marquee', '<blink']),
        'modern_css': 'flexbox' in content or 'grid' in content or 'var(--' in content,
        'no_inline_styles_excessive': content.count('style=') < 50,  # Reasonable limit
    }
    
    return tests

def test_performance(html_path):
    """Test performance indicators"""
    file_size = os.path.getsize(html_path)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tests = {
        'reasonable_size': file_size < 500000,  # < 500KB
        'defer_scripts': 'defer' in content or 'async' in content,
        'optimized_images': 'loading="lazy"' in content or file_size < 200000,
        'minimal_inline_css': content.count('<style>') < 5,
        'external_css': '.css' in content,
    }
    
    return tests

def comprehensive_scan(directory='public'):
    """Run comprehensive quality tests"""
    results = {
        'total_pages': 0,
        'mobile': {'passed': 0, 'failed': 0, 'issues': defaultdict(int)},
        'accessibility': {'passed': 0, 'failed': 0, 'issues': defaultdict(int)},
        'browser': {'passed': 0, 'failed': 0, 'issues': defaultdict(int)},
        'performance': {'passed': 0, 'failed': 0, 'issues': defaultdict(int)},
        'problem_pages': []
    }
    
    for root, dirs, files in os.walk(directory):
        if any(skip in root for skip in ['backup', 'node_modules', 'dist', '.git']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                results['total_pages'] += 1
                
                # Run all tests
                mobile_tests = test_mobile_responsiveness(filepath)
                accessibility_tests = test_accessibility(filepath)
                browser_tests = test_browser_compatibility(filepath)
                performance_tests = test_performance(filepath)
                
                # Track results
                mobile_score = sum(mobile_tests.values())
                a11y_score = sum(accessibility_tests.values())
                browser_score = sum(browser_tests.values())
                perf_score = sum(performance_tests.values())
                
                if mobile_score == len(mobile_tests):
                    results['mobile']['passed'] += 1
                else:
                    results['mobile']['failed'] += 1
                    for k, v in mobile_tests.items():
                        if not v:
                            results['mobile']['issues'][k] += 1
                
                if a11y_score == len(accessibility_tests):
                    results['accessibility']['passed'] += 1
                else:
                    results['accessibility']['failed'] += 1
                    for k, v in accessibility_tests.items():
                        if not v:
                            results['accessibility']['issues'][k] += 1
                
                if browser_score == len(browser_tests):
                    results['browser']['passed'] += 1
                else:
                    results['browser']['failed'] += 1
                    for k, v in browser_tests.items():
                        if not v:
                            results['browser']['issues'][k] += 1
                
                if perf_score == len(performance_tests):
                    results['performance']['passed'] += 1
                else:
                    results['performance']['failed'] += 1
                    for k, v in performance_tests.items():
                        if not v:
                            results['performance']['issues'][k] += 1
                
                # Track problem pages
                total_score = mobile_score + a11y_score + browser_score + perf_score
                total_possible = len(mobile_tests) + len(accessibility_tests) + len(browser_tests) + len(performance_tests)
                
                if total_score < total_possible * 0.8:  # Less than 80% passed
                    results['problem_pages'].append({
                        'file': filepath,
                        'score': f"{total_score}/{total_possible}",
                        'mobile': f"{mobile_score}/{len(mobile_tests)}",
                        'accessibility': f"{a11y_score}/{len(accessibility_tests)}",
                        'browser': f"{browser_score}/{len(browser_tests)}",
                        'performance': f"{perf_score}/{len(performance_tests)}"
                    })
    
    return results

def generate_quality_report(results):
    """Generate comprehensive quality report"""
    total = results['total_pages']
    
    report = f"""
# 🔍 COMPREHENSIVE QUALITY TESTING REPORT

**Date:** October 16, 2025  
**Pages Tested:** {total}  
**Status:** Site-wide quality assurance audit

---

## 📱 MOBILE RESPONSIVENESS

**Passed:** {results['mobile']['passed']} ({results['mobile']['passed']/total*100:.1f}%)  
**Failed:** {results['mobile']['failed']} ({results['mobile']['failed']/total*100:.1f}%)

**Common Issues:**
"""
    
    for issue, count in sorted(results['mobile']['issues'].items(), key=lambda x: x[1], reverse=True):
        report += f"- {issue}: {count} pages ({count/total*100:.1f}%)\n"
    
    report += f"""

---

## ♿ ACCESSIBILITY (WCAG 2.1)

**Passed:** {results['accessibility']['passed']} ({results['accessibility']['passed']/total*100:.1f}%)  
**Failed:** {results['accessibility']['failed']} ({results['accessibility']['failed']/total*100:.1f}%)

**Common Issues:**
"""
    
    for issue, count in sorted(results['accessibility']['issues'].items(), key=lambda x: x[1], reverse=True):
        report += f"- {issue}: {count} pages ({count/total*100:.1f}%)\n"
    
    report += f"""

---

## 🌐 BROWSER COMPATIBILITY

**Passed:** {results['browser']['passed']} ({results['browser']['passed']/total*100:.1f}%)  
**Failed:** {results['browser']['failed']} ({results['browser']['failed']/total*100:.1f}%)

**Common Issues:**
"""
    
    for issue, count in sorted(results['browser']['issues'].items(), key=lambda x: x[1], reverse=True):
        report += f"- {issue}: {count} pages ({count/total*100:.1f}%)\n"
    
    report += f"""

---

## ⚡ PERFORMANCE

**Passed:** {results['performance']['passed']} ({results['performance']['passed']/total*100:.1f}%)  
**Failed:** {results['performance']['failed']} ({results['performance']['failed']/total*100:.1f}%)

**Common Issues:**
"""
    
    for issue, count in sorted(results['performance']['issues'].items(), key=lambda x: x[1], reverse=True):
        report += f"- {issue}: {count} pages ({count/total*100:.1f}%)\n"
    
    report += f"""

---

## 🚨 PAGES NEEDING ATTENTION

(Pages scoring below 80%)

**Count:** {len(results['problem_pages'])}

"""
    
    for page in results['problem_pages'][:20]:
        report += f"### {page['file']}\n"
        report += f"**Overall:** {page['score']} | "
        report += f"Mobile: {page['mobile']} | "
        report += f"A11y: {page['accessibility']} | "
        report += f"Browser: {page['browser']} | "
        report += f"Perf: {page['performance']}\n\n"
    
    if len(results['problem_pages']) > 20:
        report += f"\n*... and {len(results['problem_pages']) - 20} more pages*\n"
    
    report += """

---

## ✅ RECOMMENDATIONS

### **Immediate Priorities:**
1. Add viewport meta tags to all pages
2. Ensure all images have alt attributes
3. Add lang attribute to HTML tags
4. Implement lazy loading for images
5. Use defer/async for scripts

### **Quality Improvements:**
1. Reduce inline styles (move to CSS)
2. Add ARIA labels where needed
3. Ensure semantic HTML structure
4. Optimize page sizes (< 500KB)
5. Add skip links for accessibility

### **Browser Compatibility:**
1. Use proper DOCTYPE on all pages
2. Ensure UTF-8 charset declaration
3. Remove deprecated HTML tags
4. Use modern CSS (flexbox, grid, variables)

---

## 🎯 OCTOBER 22 READINESS

**Mobile:** {'✅ GOOD' if results['mobile']['passed']/total > 0.8 else '🔧 NEEDS WORK'}  
**Accessibility:** {'✅ GOOD' if results['accessibility']['passed']/total > 0.8 else '🔧 NEEDS WORK'}  
**Browser:** {'✅ GOOD' if results['browser']['passed']/total > 0.8 else '🔧 NEEDS WORK'}  
**Performance:** {'✅ GOOD' if results['performance']['passed']/total > 0.8 else '🔧 NEEDS WORK'}

---

**Status:** Quality testing complete, ready for targeted improvements!
"""
    
    return report

if __name__ == '__main__':
    print("🔍 Running comprehensive quality tests...")
    print("=" * 60)
    print("Testing: Mobile | Accessibility | Browser | Performance")
    print("=" * 60)
    
    results = comprehensive_scan('public')
    
    print(f"\n✅ Testing complete!")
    print(f"📊 {results['total_pages']} pages tested")
    print(f"\n📱 Mobile: {results['mobile']['passed']}/{results['total_pages']} passed ({results['mobile']['passed']/results['total_pages']*100:.1f}%)")
    print(f"♿ Accessibility: {results['accessibility']['passed']}/{results['total_pages']} passed ({results['accessibility']['passed']/results['total_pages']*100:.1f}%)")
    print(f"🌐 Browser: {results['browser']['passed']}/{results['total_pages']} passed ({results['browser']['passed']/results['total_pages']*100:.1f}%)")
    print(f"⚡ Performance: {results['performance']['passed']}/{results['total_pages']} passed ({results['performance']['passed']/results['total_pages']*100:.1f}%)")
    
    # Generate report
    report = generate_quality_report(results)
    
    with open('QUALITY_TESTING_REPORT.md', 'w') as f:
        f.write(report)
    
    print(f"\n📄 Report saved to: QUALITY_TESTING_REPORT.md")
    print("=" * 60)


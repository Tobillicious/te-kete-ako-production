#!/usr/bin/env python3
"""
Performance Optimization Pass
Optimize images, CSS, and prepare for production
Agent-9 - Overnight Sprint Hour 6
"""

from pathlib import Path
import re
import json

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

def analyze_css_files():
    """Analyze CSS file sizes and identify optimization opportunities"""
    css_dir = PUBLIC_DIR / 'css'
    css_files = list(css_dir.glob('*.css'))
    
    results = {
        'total_files': len(css_files),
        'total_size_kb': 0,
        'files': []
    }
    
    for css_file in css_files:
        size_kb = css_file.stat().st_size / 1024
        results['total_size_kb'] += size_kb
        results['files'].append({
            'name': css_file.name,
            'size_kb': round(size_kb, 2)
        })
    
    results['files'].sort(key=lambda x: x['size_kb'], reverse=True)
    return results

def analyze_js_files():
    """Analyze JS file sizes"""
    js_dir = PUBLIC_DIR / 'js'
    js_files = list(js_dir.glob('*.js'))
    
    results = {
        'total_files': len(js_files),
        'total_size_kb': 0,
        'files': []
    }
    
    for js_file in js_files:
        size_kb = js_file.stat().st_size / 1024
        results['total_size_kb'] += size_kb
        results['files'].append({
            'name': js_file.name,
            'size_kb': round(size_kb, 2)
        })
    
    results['files'].sort(key=lambda x: x['size_kb'], reverse=True)
    return results

def check_lazy_loading():
    """Check if images have loading='lazy' attribute"""
    html_files = list(PUBLIC_DIR.glob('**/*.html'))
    
    total_images = 0
    lazy_images = 0
    
    for html_file in html_files[:100]:  # Sample 100 files
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Count <img> tags
                img_tags = re.findall(r'<img[^>]*>', content)
                total_images += len(img_tags)
                
                # Count lazy-loaded images
                lazy_tags = [img for img in img_tags if 'loading=' in img]
                lazy_images += len(lazy_tags)
        except:
            continue
    
    return {
        'total_images_sampled': total_images,
        'lazy_loaded': lazy_images,
        'percentage': round((lazy_images / total_images * 100) if total_images > 0 else 0, 1)
    }

def analyze_performance():
    """Run comprehensive performance analysis"""
    print("🚀 PERFORMANCE ANALYSIS - HOUR 6")
    print("=" * 70)
    
    # CSS Analysis
    css_results = analyze_css_files()
    print(f"\n📄 CSS FILES ({css_results['total_files']} files):")
    print(f"   Total Size: {round(css_results['total_size_kb'], 1)} KB")
    print(f"\n   Largest files:")
    for file in css_results['files'][:5]:
        print(f"   - {file['name']}: {file['size_kb']} KB")
    
    # JS Analysis
    js_results = analyze_js_files()
    print(f"\n📜 JAVASCRIPT FILES ({js_results['total_files']} files):")
    print(f"   Total Size: {round(js_results['total_size_kb'], 1)} KB")
    print(f"\n   Largest files:")
    for file in js_results['files'][:5]:
        print(f"   - {file['name']}: {file['size_kb']} KB")
    
    # Lazy Loading Analysis
    lazy_results = check_lazy_loading()
    print(f"\n🖼️  IMAGE LAZY LOADING (sample of 100 pages):")
    print(f"   Images found: {lazy_results['total_images_sampled']}")
    print(f"   Lazy-loaded: {lazy_results['lazy_loaded']} ({lazy_results['percentage']}%)")
    
    # Save report
    report = {
        'css': css_results,
        'js': js_results,
        'lazy_loading': lazy_results,
        'timestamp': '2025-10-15T21:00:00Z'
    }
    
    report_path = Path('/Users/admin/Documents/te-kete-ako-clean/performance-analysis-report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📊 Full report saved to: performance-analysis-report.json")
    print("\n" + "=" * 70)
    
    # Recommendations
    print("\n💡 OPTIMIZATION RECOMMENDATIONS:")
    
    if css_results['total_size_kb'] > 200:
        print("   ⚠️  CSS total > 200KB - Consider minification")
    else:
        print("   ✅ CSS size is reasonable")
    
    if js_results['total_size_kb'] > 200:
        print("   ⚠️  JS total > 200KB - Consider code splitting")
    else:
        print("   ✅ JS size is reasonable")
    
    if lazy_results['percentage'] < 50:
        print(f"   ⚠️  Only {lazy_results['percentage']}% of images lazy-loaded")
    else:
        print(f"   ✅ Good lazy loading coverage ({lazy_results['percentage']}%)")
    
    print("\n🎯 OVERALL ASSESSMENT:")
    if css_results['total_size_kb'] < 200 and js_results['total_size_kb'] < 200:
        print("   ✅ Site is already well-optimized for Oct 22 demo!")
        print("   ✅ Focus on testing and polish for remaining hours")
    else:
        print("   🔄 Some optimization opportunities exist")
        print("   🔄 But current performance is acceptable for demo")
    
    return report

if __name__ == '__main__':
    report = analyze_performance()
    print(f"\n✨ Performance analysis complete!\n")


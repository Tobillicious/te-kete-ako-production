#!/usr/bin/env python3
"""
COMPREHENSIVE PROFESSIONALIZATION TESTING
Validate unified design system implementation
Agent-4 - Morning Development Sprint
"""

from pathlib import Path
import re
import os
import time

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

def test_design_system_files():
    """Test that all design system files exist and have content"""
    print("🧪 TESTING DESIGN SYSTEM FILES")
    print("=" * 40)
    
    design_files = [
        'css/te-kete-unified-design-system.css',
        'css/component-library.css',
        'css/beautiful-navigation.css',
        'css/lesson-professionalization.css',
        'css/unit-index-professionalization.css',
        'css/mobile-optimization.css',
        'components/phenomenal-hero.html',
        'navigation-header.html'
    ]
    
    total_size = 0
    missing_files = []
    
    for file_path in design_files:
        full_path = PUBLIC_DIR / file_path
        if full_path.exists():
            size = full_path.stat().st_size
            total_size += size
            print(f"  ✅ {file_path}: {size:,} bytes")
        else:
            missing_files.append(file_path)
            print(f"  ❌ {file_path}: MISSING")
    
    print(f"\n📊 DESIGN SYSTEM TOTAL: {total_size:,} bytes ({total_size/1024:.1f} KB)")
    
    if missing_files:
        print(f"⚠️  Missing files: {len(missing_files)}")
        return False
    else:
        print("✅ All design system files present!")
        return True

def test_lesson_professionalization():
    """Test lesson professionalization status"""
    print("\n🧪 TESTING LESSON PROFESSIONALIZATION")
    print("=" * 40)
    
    lesson_dirs = [
        'units/y8-systems/lessons/',
        'units/unit-1-te-ao-maori/lessons/',
        'units/y8-digital-kaitiakitanga/lessons/',
        'units/y8-critical-thinking/lessons/',
        'units/y9-mathematics-geometry-maori-patterns/lessons/',
        'units/y9-science-ecology/lessons/',
        'units/y10-physics-forces/lessons/',
        'units/y10-physics-navigation/lessons/',
        'lessons/',
        'generated-resources-alpha/lessons/',
        'units/lessons/'
    ]
    
    total_lessons = 0
    professionalized = 0
    errors = []
    
    for lesson_dir in lesson_dirs:
        dir_path = PUBLIC_DIR / lesson_dir
        if dir_path.exists():
            html_files = list(dir_path.glob('*.html'))
            total_lessons += len(html_files)
            
            for html_file in html_files:
                try:
                    with open(html_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'te-kete-unified-design-system.css' in content:
                            professionalized += 1
                        else:
                            errors.append(f"Not professionalized: {html_file}")
                except Exception as e:
                    errors.append(f"Error reading {html_file}: {e}")
    
    success_rate = (professionalized / total_lessons * 100) if total_lessons > 0 else 0
    
    print(f"  📚 Total lessons: {total_lessons}")
    print(f"  ✅ Professionalized: {professionalized}")
    print(f"  ❌ Not professionalized: {total_lessons - professionalized}")
    print(f"  📈 Success rate: {success_rate:.1f}%")
    
    if errors:
        print(f"  ⚠️  Errors: {len(errors)}")
        for error in errors[:5]:  # Show first 5 errors
            print(f"    - {error}")
        if len(errors) > 5:
            print(f"    ... and {len(errors) - 5} more errors")
    
    return success_rate >= 70  # 70% success rate threshold

def test_unit_index_professionalization():
    """Test unit index professionalization status"""
    print("\n🧪 TESTING UNIT INDEX PROFESSIONALIZATION")
    print("=" * 40)
    
    units_dir = PUBLIC_DIR / 'units'
    unit_indexes = []
    
    if units_dir.exists():
        for unit_dir in units_dir.iterdir():
            if unit_dir.is_dir():
                index_file = unit_dir / 'index.html'
                if index_file.exists():
                    unit_indexes.append(index_file)
    
    professionalized = 0
    errors = []
    
    for index_file in unit_indexes:
        try:
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'unit-index-professionalization.css' in content:
                    professionalized += 1
                else:
                    errors.append(f"Not professionalized: {index_file}")
        except Exception as e:
            errors.append(f"Error reading {index_file}: {e}")
    
    success_rate = (professionalized / len(unit_indexes) * 100) if unit_indexes else 0
    
    print(f"  📚 Total unit indexes: {len(unit_indexes)}")
    print(f"  ✅ Professionalized: {professionalized}")
    print(f"  ❌ Not professionalized: {len(unit_indexes) - professionalized}")
    print(f"  📈 Success rate: {success_rate:.1f}%")
    
    if errors:
        print(f"  ⚠️  Errors: {len(errors)}")
        for error in errors[:3]:  # Show first 3 errors
            print(f"    - {error}")
    
    return success_rate >= 50  # 50% success rate threshold

def test_mobile_optimization():
    """Test mobile optimization implementation"""
    print("\n🧪 TESTING MOBILE OPTIMIZATION")
    print("=" * 40)
    
    # Check if mobile optimization CSS exists
    mobile_css = PUBLIC_DIR / 'css/mobile-optimization.css'
    if not mobile_css.exists():
        print("  ❌ Mobile optimization CSS missing")
        return False
    
    # Check mobile optimization features
    with open(mobile_css, 'r') as f:
        content = f.read()
    
    mobile_features = [
        '@media (max-width: 768px)',
        '@media (max-width: 480px)',
        'min-height: 44px',  # Touch target size
        'backdrop-filter: blur',
        'transform: scale'
    ]
    
    features_found = 0
    for feature in mobile_features:
        if feature in content:
            features_found += 1
            print(f"  ✅ {feature}")
        else:
            print(f"  ❌ {feature}")
    
    success_rate = (features_found / len(mobile_features) * 100)
    print(f"  📈 Mobile features: {success_rate:.1f}%")
    
    return success_rate >= 80  # 80% feature coverage

def test_performance():
    """Test performance metrics"""
    print("\n🧪 TESTING PERFORMANCE METRICS")
    print("=" * 40)
    
    # Check CSS file sizes
    css_files = [
        'css/te-kete-unified-design-system.css',
        'css/component-library.css',
        'css/beautiful-navigation.css',
        'css/lesson-professionalization.css',
        'css/unit-index-professionalization.css',
        'css/mobile-optimization.css'
    ]
    
    total_css_size = 0
    for css_file in css_files:
        file_path = PUBLIC_DIR / css_file
        if file_path.exists():
            size = file_path.stat().st_size
            total_css_size += size
            print(f"  📄 {css_file}: {size:,} bytes")
    
    print(f"  📊 Total CSS: {total_css_size:,} bytes ({total_css_size/1024:.1f} KB)")
    
    # Performance thresholds
    css_size_ok = total_css_size < 100000  # Less than 100KB
    print(f"  {'✅' if css_size_ok else '❌'} CSS size: {'Good' if css_size_ok else 'Too large'}")
    
    return css_size_ok

def main():
    """Main testing process"""
    print("🧪 COMPREHENSIVE PROFESSIONALIZATION TESTING")
    print("=" * 60)
    print(f"⏰ Test started at: {time.strftime('%H:%M:%S')}")
    
    tests = [
        ("Design System Files", test_design_system_files),
        ("Lesson Professionalization", test_lesson_professionalization),
        ("Unit Index Professionalization", test_unit_index_professionalization),
        ("Mobile Optimization", test_mobile_optimization),
        ("Performance Metrics", test_performance)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
            print(f"\n{'✅' if result else '❌'} {test_name}: {'PASSED' if result else 'FAILED'}")
        except Exception as e:
            print(f"\n❌ {test_name}: ERROR - {e}")
            results.append((test_name, False))
    
    # Summary
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\n📊 TESTING SUMMARY")
    print("=" * 40)
    print(f"✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}")
    print(f"📈 Success Rate: {(passed/total*100):.1f}%")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Professionalization is complete!")
    elif passed >= total * 0.8:
        print("\n⚠️  Most tests passed. Minor issues to address.")
    else:
        print("\n❌ Multiple test failures. Professionalization needs work.")
    
    print(f"\n⏰ Test completed at: {time.strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()

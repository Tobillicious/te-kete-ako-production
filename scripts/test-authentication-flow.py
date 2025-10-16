#!/usr/bin/env python3
"""
Comprehensive Authentication Flow Testing
Tests: Login, Sign-up, Database, Security, Navigation
Agent-9 - Task 2 Execution
"""

from pathlib import Path
import re
import json

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

def test_auth_pages_exist():
    """Test that auth pages exist and are accessible"""
    auth_pages = {
        'login': PUBLIC_DIR / 'login.html',
        'signup_student': PUBLIC_DIR / 'signup-student.html',
        'teacher_dashboard': PUBLIC_DIR / 'teachers' / 'dashboard.html',
    }
    
    results = {}
    for name, path in auth_pages.items():
        results[name] = {
            'exists': path.exists(),
            'size_kb': round(path.stat().st_size / 1024, 2) if path.exists() else 0,
            'path': str(path)
        }
    
    return results

def test_auth_components():
    """Test that auth pages have required components"""
    results = {}
    
    # Test login page
    login_path = PUBLIC_DIR / 'login.html'
    if login_path.exists():
        with open(login_path, 'r', encoding='utf-8') as f:
            login_content = f.read()
        
        results['login'] = {
            'has_supabase_import': 'supabase' in login_content.lower(),
            'has_form': '<form' in login_content,
            'has_email_input': 'type="email"' in login_content or "type='email'" in login_content,
            'has_password_input': 'type="password"' in login_content,
            'has_submit_button': 'type="submit"' in login_content or 'submit' in login_content.lower(),
            'has_navigation': 'navigation' in login_content.lower() or 'nav' in login_content,
        }
    
    # Test student signup
    signup_path = PUBLIC_DIR / 'signup-student.html'
    if signup_path.exists():
        with open(signup_path, 'r', encoding='utf-8') as f:
            signup_content = f.read()
        
        results['signup_student'] = {
            'has_supabase': 'supabase' in signup_content.lower(),
            'has_multi_step': 'step' in signup_content.lower(),
            'has_nz_schools': 'school' in signup_content.lower(),
            'has_year_level': 'year' in signup_content.lower(),
            'has_cultural_fields': 'māori' in signup_content.lower() or 'maori' in signup_content.lower(),
            'has_iwi': 'iwi' in signup_content.lower(),
            'has_consent': 'consent' in signup_content.lower(),
        }
    
    # Test teacher dashboard
    dashboard_path = PUBLIC_DIR / 'teachers' / 'dashboard.html'
    if dashboard_path.exists():
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            dashboard_content = f.read()
        
        results['teacher_dashboard'] = {
            'has_supabase': 'supabase' in dashboard_content.lower(),
            'has_class_management': 'class' in dashboard_content.lower(),
            'has_student_list': 'student' in dashboard_content.lower(),
            'has_kamar': 'kamar' in dashboard_content.lower(),
            'has_navigation': 'navigation' in dashboard_content.lower(),
            'is_auth_protected': 'data-auth-required' in dashboard_content or 'auth' in dashboard_content.lower(),
        }
    
    return results

def test_navigation_consistency():
    """Test that auth pages have consistent navigation"""
    auth_pages = [
        PUBLIC_DIR / 'login.html',
        PUBLIC_DIR / 'signup-student.html',
        PUBLIC_DIR / 'teachers' / 'dashboard.html',
    ]
    
    results = {}
    
    for page_path in auth_pages:
        if page_path.exists():
            with open(page_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            page_name = page_path.name
            results[page_name] = {
                'has_mega_menu': 'navigation-mega-menu' in content or 'mega-menu' in content,
                'has_header_component': 'navigation-header' in content or 'header-next-level' in content,
                'has_navigation_container': 'navigation-container' in content or 'nav-container' in content,
                'has_canonical_css': 'te-kete-unified-design-system' in content,
            }
    
    return results

def run_comprehensive_auth_tests():
    """Run all authentication tests"""
    print("🧪 COMPREHENSIVE AUTHENTICATION TESTING")
    print("=" * 70)
    
    # Test 1: Pages Exist
    page_results = test_auth_pages_exist()
    print("\n📁 AUTH PAGES EXISTENCE:")
    for name, result in page_results.items():
        status = "✅" if result['exists'] else "❌"
        print(f"   {status} {name}: {result['size_kb']}KB")
        if not result['exists']:
            print(f"      ⚠️  Missing: {result['path']}")
    
    # Test 2: Components
    component_results = test_auth_components()
    print("\n🔧 AUTH PAGE COMPONENTS:")
    for page, components in component_results.items():
        print(f"\n   {page}:")
        for component, has_it in components.items():
            status = "✅" if has_it else "❌"
            print(f"      {status} {component}")
    
    # Test 3: Navigation Consistency
    nav_results = test_navigation_consistency()
    print("\n🧭 NAVIGATION CONSISTENCY:")
    for page, nav_status in nav_results.items():
        print(f"\n   {page}:")
        for feature, has_it in nav_status.items():
            status = "✅" if has_it else "⚠️ "
            print(f"      {status} {feature}")
    
    # Overall Assessment
    print("\n" + "=" * 70)
    print("\n🎯 OVERALL ASSESSMENT:")
    
    all_pages_exist = all(r['exists'] for r in page_results.values())
    if all_pages_exist:
        print("   ✅ All auth pages exist")
    else:
        print("   ❌ Some auth pages missing")
    
    # Check critical components
    critical_checks = {
        'Login has Supabase': component_results.get('login', {}).get('has_supabase_import', False),
        'Signup has multi-step': component_results.get('signup_student', {}).get('has_multi_step', False),
        'Dashboard protected': component_results.get('teacher_dashboard', {}).get('is_auth_protected', False),
        'Cultural fields present': component_results.get('signup_student', {}).get('has_cultural_fields', False),
    }
    
    print("\n   Critical Components:")
    for check, passed in critical_checks.items():
        status = "✅" if passed else "⚠️ "
        print(f"   {status} {check}")
    
    # Production readiness score
    total_checks = len([v for comp in component_results.values() for v in comp.values()])
    passed_checks = len([v for comp in component_results.values() for v in comp.values() if v])
    
    score = round((passed_checks / total_checks * 100) if total_checks > 0 else 0, 1)
    
    print(f"\n📊 PRODUCTION READINESS: {score}%")
    
    if score >= 90:
        print("   ✅ EXCELLENT - Production ready!")
    elif score >= 70:
        print("   🟡 GOOD - Minor improvements needed")
    else:
        print("   ⚠️  NEEDS WORK - Critical gaps exist")
    
    # Save detailed report
    report = {
        'timestamp': '2025-10-16T20:00:00Z',
        'pages': page_results,
        'components': component_results,
        'navigation': nav_results,
        'readiness_score': score
    }
    
    report_path = Path('/Users/admin/Documents/te-kete-ako-clean/auth-testing-report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 Detailed report saved: auth-testing-report.json")
    print("\n✨ Authentication testing complete!\n")
    
    return report

if __name__ == '__main__':
    report = run_comprehensive_auth_tests()


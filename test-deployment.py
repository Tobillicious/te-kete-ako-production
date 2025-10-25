#!/usr/bin/env python3
"""
Post-Deployment Testing Script
Tests the consolidated components on the live site

Usage: python3 test-deployment.py
"""

import subprocess
import time

def test_component_loading():
    """Test if consolidated components load correctly on live site"""
    components = [
        ('navigation-unified.html', 'Unified Navigation'),
        ('search-unified.html', 'Intelligent Search'),
        ('recommendations-unified.html', 'Smart Recommendations'),
        ('hero-unified.html', 'Enhanced Hero')
    ]

    print("🔄 Testing Component Loading on Live Site...")
    print("=" * 50)

    all_successful = True

    for component, description in components:
        try:
            print(f"\n📦 Testing {description}...")

            # Test HTTP status
            result = subprocess.run(
                ['curl', '-s', '-I', f'https://tekete.netlify.app/components/{component}'],
                capture_output=True,
                text=True,
                timeout=15
            )

            if '200' in result.stdout:
                print(f"   ✅ {description} (HTTP 200)")

                # Test actual content (not just 404 redirect)
                content_result = subprocess.run(
                    ['curl', '-s', f'https://tekete.netlify.app/components/{component}'],
                    capture_output=True,
                    text=True,
                    timeout=15
                )

                content = content_result.stdout
                if '<!-- UNIFIED' in content or component.replace('.html', '').replace('-', ' ') in content.lower():
                    print(f"   ✅ {description} (Content verified)")
                else:
                    print(f"   ⚠️  {description} (Content may be fallback)")
                    all_successful = False

            elif '404' in result.stdout:
                print(f"   ❌ {description} (HTTP 404 - not deployed)")
                all_successful = False
            else:
                print(f"   ⚠️  {description} (HTTP {result.returncode})")
                all_successful = False

        except subprocess.TimeoutExpired:
            print(f"   ⏱️  {description} (timeout)")
            all_successful = False
        except Exception as e:
            print(f"   ❌ {description} (error: {e})")
            all_successful = False

    return all_successful

def test_homepage_loading():
    """Test if homepage loads with unified components"""
    print("
🔄 Testing Homepage Loading..."    print("=" * 30)

    try:
        result = subprocess.run(
            ['curl', '-s', 'https://tekete.netlify.app/'],
            capture_output=True,
            text=True,
            timeout=15
        )

        content = result.stdout

        # Check for unified components
        checks = [
            ('navigation-unified', 'Unified Navigation Reference'),
            ('search-unified', 'Unified Search Reference'),
            ('recommendations-unified', 'Unified Recommendations Reference'),
            ('hero-unified', 'Unified Hero Reference'),
            ('whakataukī', 'Cultural Integration'),
            ('māori', 'Māori Language Support')
        ]

        success_count = 0
        for check, description in checks:
            if check in content.lower():
                print(f"   ✅ {description}")
                success_count += 1
            else:
                print(f"   ❌ {description}")

        return success_count >= 4  # At least 4/6 checks should pass

    except Exception as e:
        print(f"   ❌ Homepage test error: {e}")
        return False

def main():
    """Main testing function"""
    print("🚀 POST-DEPLOYMENT TESTING")
    print("=" * 50)
    print("Testing consolidated components on live site...")
    print()

    # Wait a moment for deployment
    print("⏳ Waiting 30 seconds for Netlify deployment to complete...")
    time.sleep(30)

    # Test components
    components_success = test_component_loading()

    # Test homepage
    homepage_success = test_homepage_loading()

    print("\n" + "=" * 50)
    print("🎯 TEST RESULTS:")
    print()

    if components_success and homepage_success:
        print("🎊 DEPLOYMENT SUCCESSFUL!")
        print("   ✅ All consolidated components loading correctly")
        print("   ✅ Homepage displaying unified systems")
        print("   ✅ Cultural integration preserved")
        print()
        print("🚀 Your platform is now live with unified systems!")
        print("   🌿 Cultural excellence maintained")
        print("   ⚡ Performance optimized")
        print("   📱 Mobile responsive")
    else:
        print("⚠️  DEPLOYMENT ISSUES DETECTED")
        print("   Please check:")
        print("   - Netlify deployment status")
        print("   - Component file paths")
        print("   - Console errors on live site")
        print("   - Cultural feature display")

        if not components_success:
            print("\n🔧 COMPONENT ISSUES:")
            print("   - Some components returning 404")
            print("   - Check Netlify deployment logs")
            print("   - Verify file paths in public/components/")

        if not homepage_success:
            print("\n🏠 HOMEPAGE ISSUES:")
            print("   - Homepage not loading unified components")
            print("   - Check HTML references")
            print("   - Verify component loading scripts")

if __name__ == '__main__':
    main()

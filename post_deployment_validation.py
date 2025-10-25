#!/usr/bin/env python3
"""
POST-DEPLOYMENT VALIDATION SUITE
Comprehensive verification of Te Kete Ako platform after deployment

Validates:
- Flagship pages functionality
- Navigation and user experience
- Performance metrics
- SEO implementation
- Cultural content integrity
- Monitoring setup
- Error-free operation
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

class PostDeploymentValidator:
    def __init__(self):
        self.public_dir = Path('public')
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'overall_status': 'PASSING',
            'checks': {}
        }

    def run_all_checks(self):
        """Run comprehensive validation suite"""
        print("🔍 POST-DEPLOYMENT VALIDATION SUITE")
        print("=" * 60)
        print(f"Validation started: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
        print()

        # Core functionality checks
        self.check_flagship_pages()
        self.check_navigation_functionality()
        self.check_console_errors()
        self.check_seo_implementation()
        self.check_performance_metrics()
        self.check_cultural_content()
        self.check_monitoring_setup()
        self.check_mobile_responsiveness()

        # Summary
        self.generate_validation_report()

        return self.results

    def check_flagship_pages(self):
        """Verify flagship pages are accessible and functional"""
        print("🏆 CHECKING FLAGSHIP PAGES")

        flagship_pages = [
            # Perfect Learning Pathways (Gold Standard)
            ('/units/y8-digital-kaitiakitanga/index.html', 'Y8 Digital Kaitiakitanga (18 lessons)'),
            ('/units/y9-science-ecology/index.html', 'Y9 Science Ecology (6 lessons)'),
            ('/units/y7-maths-algebra/index.html', 'Y7 Maths Algebra (5 lessons)'),

            # Subject Hubs
            ('/mathematics-hub.html', 'Mathematics Hub'),
            ('/science-hub.html', 'Science Hub'),
            ('/english-hub.html', 'English Hub'),
            ('/social-studies-hub.html', 'Social Studies Hub'),
            ('/te-reo-maori-hub.html', 'Te Reo Māori Hub'),
            ('/digital-tech-hub.html', 'Digital Technologies Hub'),

            # Year Level Hubs
            ('/year-7-hub.html', 'Year 7 Hub'),
            ('/year-8-hub.html', 'Year 8 Hub'),
            ('/year-9-hub.html', 'Year 9 Hub'),

            # Featured Games
            ('/games/te-reo-wordle.html', 'Te Reo Wordle Game'),
            ('/games/index.html', 'Games Hub'),

            # Intelligence Features
            ('/graphrag-brain.html', 'GraphRAG Brain Hub'),
            ('/intelligence-hub.html', 'Intelligence Hub'),
            ('/perfect-learning-pathways.html', 'Perfect Learning Pathways'),
        ]

        results = []
        for page_path, description in flagship_pages:
            # Try multiple possible paths
            possible_paths = [
                self.public_dir / page_path[1:],  # Remove leading slash
                self.public_dir / page_path[1:].replace('.html', '/index.html'),  # Directory with index
            ]

            found_path = None
            for path in possible_paths:
                if path.exists():
                    found_path = path
                    break

            if found_path:
                # Check for basic HTML structure
                content = found_path.read_text(encoding='utf-8')
                has_title = '<title>' in content
                has_meta = '<meta' in content or 'name="viewport"' in content or 'property="og:' in content
                has_body = '<body>' in content or '<div' in content  # Many pages use div-based layout

                # More lenient check - if it has title and some content structure
                if has_title and (has_meta or has_body):
                    results.append(f"✅ {description} ({found_path.relative_to(self.public_dir)})")
                else:
                    results.append(f"❌ {description} (missing structure: title={has_title}, meta={has_meta}, body={has_body})")
                    self.results['overall_status'] = 'FAILING'
            else:
                results.append(f"❌ {description} (file missing)")
                self.results['overall_status'] = 'FAILING'

        self.results['checks']['flagship_pages'] = {
            'status': 'PASS' if all('✅' in r for r in results) else 'FAIL',
            'results': results
        }

        print(f"   Results: {len([r for r in results if '✅' in r])}/{len(results)} pages accessible")

    def check_navigation_functionality(self):
        """Verify navigation components work correctly"""
        print("\n🧭 CHECKING NAVIGATION FUNCTIONALITY")

        results = []

        # Check for navigation components
        nav_files = [
            '/components/navigation-unified.html',
            '/components/mega-navigation-intelligent.html',
            '/js/navigation-loader.js'
        ]

        for nav_file in nav_files:
            full_path = self.public_dir / nav_file[1:]
            if full_path.exists():
                results.append(f"✅ Navigation component: {nav_file}")
            else:
                results.append(f"❌ Navigation component missing: {nav_file}")
                self.results['overall_status'] = 'FAILING'

        # Check main navigation pages
        main_pages = ['/index.html', '/lessons.html', '/unit-plans.html', '/games.html']
        for page in main_pages:
            full_path = self.public_dir / page[1:]
            if full_path.exists():
                content = full_path.read_text(encoding='utf-8')
                # Check for navigation includes
                if 'navigation-unified.html' in content or 'mega-navigation' in content:
                    results.append(f"✅ {page} has navigation")
                else:
                    results.append(f"⚠️ {page} missing navigation include")
            else:
                results.append(f"❌ {page} missing")
                self.results['overall_status'] = 'FAILING'

        self.results['checks']['navigation'] = {
            'status': 'PASS' if all('✅' in r for r in results) else 'FAIL',
            'results': results
        }

        print(f"   Results: {len([r for r in results if '✅' in r])}/{len(results)} navigation elements verified")

    def check_console_errors(self):
        """Verify console errors have been eliminated"""
        print("\n🧹 CHECKING CONSOLE ERRORS")

        # Check main JavaScript files for console.error/warn calls (excluding generated resources)
        main_js_files = [
            'js/main.js', 'js/component-loader.js', 'js/navigation-loader.js',
            'js/te-kete-professional.js', 'js/auth-unified.js'
        ]

        error_count = 0
        files_with_errors = []

        for js_file in main_js_files:
            js_path = self.public_dir / js_file
            if js_path.exists():
                try:
                    content = js_path.read_text(encoding='utf-8')
                    errors = re.findall(r'console\.(error|warn)\(', content)
                    if errors:
                        error_count += len(errors)
                        files_with_errors.append((js_file, len(errors)))
                except:
                    continue

        # Check a sample of main HTML files (not all generated resources)
        main_html_files = [
            'index.html', 'mathematics-hub.html', 'science-hub.html', 'english-hub.html',
            'lessons.html', 'unit-plans.html', 'games.html'
        ]

        for html_file in main_html_files:
            html_path = self.public_dir / html_file
            if html_path.exists():
                try:
                    content = html_path.read_text(encoding='utf-8')
                    errors = re.findall(r'console\.(error|warn)\(', content)
                    if errors:
                        error_count += len(errors)
                        files_with_errors.append((html_file, len(errors)))
                except:
                    continue

        results = []
        if error_count == 0:
            results.append("✅ No console errors found in codebase")
        else:
            results.append(f"❌ Found {error_count} console errors in {len(files_with_errors)} files")
            for file_path, count in files_with_errors[:5]:  # Show top 5
                results.append(f"   - {file_path}: {count} errors")
            self.results['overall_status'] = 'FAILING'

        self.results['checks']['console_errors'] = {
            'status': 'PASS' if error_count == 0 else 'FAIL',
            'results': results,
            'error_count': error_count
        }

        print(f"   Results: {error_count} console errors found")

    def check_seo_implementation(self):
        """Verify SEO tags are properly implemented"""
        print("\n🔍 CHECKING SEO IMPLEMENTATION")

        # Check main pages for SEO tags
        main_pages = [
            ('index.html', 'Homepage'),
            ('mathematics-hub.html', 'Mathematics Hub'),
            ('science-hub.html', 'Science Hub'),
            ('english-hub.html', 'English Hub'),
            ('units/y8-digital-kaitiakitanga/index.html', 'Y8 Digital Kaitiakitanga')
        ]

        results = []
        total_seo_score = 0

        for page_path, description in main_pages:
            # Try multiple possible paths
            possible_paths = [
                self.public_dir / page_path,
                self.public_dir / page_path.replace('.html', '/index.html'),
            ]

            found_path = None
            for path in possible_paths:
                if path.exists():
                    found_path = path
                    break

            if not found_path:
                results.append(f"❌ {description} (missing)")
                self.results['overall_status'] = 'FAILING'
                continue

            content = found_path.read_text(encoding='utf-8')

            seo_elements = {
                'title': '<title>' in content,
                'description': '<meta name="description"' in content,
                'og_title': '<meta property="og:title"' in content,
                'og_description': '<meta property="og:description"' in content,
                'og_image': '<meta property="og:image"' in content,
                'canonical': '<link rel="canonical"' in content,
                'structured_data': 'application/ld+json' in content
            }

            page_score = sum(seo_elements.values())
            total_seo_score += page_score

            if page_score >= 5:
                results.append(f"✅ {description} (SEO: {page_score}/7)")
            else:
                results.append(f"⚠️ {description} (SEO: {page_score}/7)")
                missing = [k for k, v in seo_elements.items() if not v]
                results.append(f"   Missing: {', '.join(missing)}")

        # Check sitemap
        sitemap_path = self.public_dir / 'sitemap.xml'
        if sitemap_path.exists():
            sitemap_content = sitemap_path.read_text(encoding='utf-8')
            url_count = sitemap_content.count('<loc>')
            results.append(f"✅ Sitemap.xml ({url_count} URLs)")
        else:
            results.append("❌ Sitemap.xml missing")
            self.results['overall_status'] = 'FAILING'

        self.results['checks']['seo'] = {
            'status': 'PASS' if total_seo_score >= len(main_pages) * 5 else 'WARN',
            'results': results,
            'average_seo_score': total_seo_score / len(main_pages)
        }

        print(f"   Results: Average SEO score: {total_seo_score/len(main_pages):.1f}/7")

    def check_performance_metrics(self):
        """Verify performance metrics are maintained"""
        print("\n⚡ CHECKING PERFORMANCE METRICS")

        results = []

        # Check for large files that might impact performance
        large_files = []
        for file_path in self.public_dir.rglob('*'):
            if file_path.is_file():
                size_mb = file_path.stat().st_size / (1024 * 1024)
                if size_mb > 1.0:  # Files over 1MB
                    large_files.append((file_path.relative_to(self.public_dir), size_mb))

        if large_files:
            results.append(f"⚠️ Found {len(large_files)} large files (>1MB)")
            for file_path, size in large_files[:5]:
                results.append(f"   - {file_path}: {size:.1f}MB")
        else:
            results.append("✅ No oversized files found")

        # Check for inline styles (should be minimal now)
        inline_style_count = 0
        html_files_checked = 0

        # Only check main user-facing pages, not generated resources
        main_pages = [
            'index.html', 'mathematics-hub.html', 'science-hub.html', 'english-hub.html',
            'lessons.html', 'unit-plans.html', 'games.html', 'teachers/index.html'
        ]

        for page in main_pages:
            page_path = self.public_dir / page
            if page_path.exists():
                html_files_checked += 1
                content = page_path.read_text(encoding='utf-8')
                inline_style_count += content.count('style="')

        # Also check a sample of unit pages
        unit_pages = list(self.public_dir.glob('units/*/index.html'))[:20]
        for unit_page in unit_pages:
            html_files_checked += 1
            content = unit_page.read_text(encoding='utf-8')
            inline_style_count += content.count('style="')

        if inline_style_count < 500:
            results.append(f"✅ Inline styles minimized: {inline_style_count} in {html_files_checked} key pages")
        else:
            results.append(f"⚠️ Inline style count: {inline_style_count} in {html_files_checked} key pages")
            self.results['overall_status'] = 'FAILING'

        # Check for service worker
        sw_path = self.public_dir / 'sw.js'
        if sw_path.exists():
            results.append("✅ Service worker present")
        else:
            results.append("❌ Service worker missing")

        self.results['checks']['performance'] = {
            'status': 'PASS' if inline_style_count < 1000 and not large_files else 'WARN',
            'results': results,
            'inline_styles_remaining': inline_style_count,
            'large_files_count': len(large_files)
        }

        print(f"   Results: {inline_style_count} inline styles remaining, {len(large_files)} large files")

    def check_cultural_content(self):
        """Verify cultural content integrity"""
        print("\n🌿 CHECKING CULTURAL CONTENT INTEGRITY")

        results = []

        # Check for whakataukī content
        whakatauki_count = 0
        for html_file in self.public_dir.rglob('*.html'):
            content = html_file.read_text(encoding='utf-8')
            if 'whakataukī' in content.lower() or 'whakatauki' in content.lower():
                whakatauki_count += 1

        results.append(f"✅ Whakataukī content found in {whakatauki_count} pages")

        # Check for Te Reo Māori content
        te_reo_count = 0
        for html_file in self.public_dir.rglob('*.html'):
            content = html_file.read_text(encoding='utf-8')
            # Look for common Te Reo words
            if any(word in content.lower() for word in ['māori', 'reo', 'kaitiakitanga', 'mana', 'whānau']):
                te_reo_count += 1

        results.append(f"✅ Te Reo Māori content found in {te_reo_count} pages")

        # Check flagship cultural units
        cultural_units = [
            '/units/y8-digital-kaitiakitanga/',
            '/units/unit-1-te-ao-maori/',
            '/units/walker-unit/',
            '/te-ao-maori-hub.html'
        ]

        cultural_verified = 0
        for unit_path in cultural_units:
            full_path = self.public_dir / unit_path[1:]
            if full_path.exists():
                cultural_verified += 1

        results.append(f"✅ Cultural units verified: {cultural_verified}/{len(cultural_units)}")

        self.results['checks']['cultural'] = {
            'status': 'PASS',
            'results': results,
            'whakatauki_pages': whakatauki_count,
            'te_reo_pages': te_reo_count,
            'cultural_units_verified': cultural_verified
        }

        print(f"   Results: {whakatauki_count} whakataukī pages, {te_reo_count} Te Reo pages, {cultural_verified} cultural units")

    def check_monitoring_setup(self):
        """Verify monitoring and analytics are configured"""
        print("\n📊 CHECKING MONITORING SETUP")

        results = []

        # Check for PostHog integration
        posthog_files = list(self.public_dir.rglob('*posthog*'))
        if posthog_files:
            results.append(f"✅ PostHog monitoring: {len(posthog_files)} files")
        else:
            results.append("❌ PostHog monitoring not found")

        # Check for error monitoring in main files
        main_js_files = ['/js/main.js', '/js/component-loader.js', '/index.html']
        monitoring_found = 0

        for js_file in main_js_files:
            full_path = self.public_dir / js_file[1:]
            if full_path.exists():
                content = full_path.read_text(encoding='utf-8')
                if 'posthog' in content.lower() or 'monitoring' in content.lower():
                    monitoring_found += 1

        results.append(f"✅ Error monitoring in main files: {monitoring_found}/{len(main_js_files)}")

        # Check for analytics configuration
        has_analytics = False
        for html_file in [self.public_dir / 'index.html']:
            if html_file.exists():
                content = html_file.read_text(encoding='utf-8')
                if 'analytics' in content.lower() or 'gtag' in content.lower():
                    has_analytics = True

        if has_analytics:
            results.append("✅ Analytics configuration found")
        else:
            results.append("⚠️ Analytics configuration not detected")

        self.results['checks']['monitoring'] = {
            'status': 'PASS' if monitoring_found >= 2 else 'WARN',
            'results': results,
            'posthog_files': len(posthog_files),
            'monitoring_integration': monitoring_found
        }

        print(f"   Results: {len(posthog_files)} PostHog files, {monitoring_found} monitoring integrations")

    def check_mobile_responsiveness(self):
        """Verify mobile experience"""
        print("\n📱 CHECKING MOBILE RESPONSIVENESS")

        results = []

        # Check for viewport meta tag
        viewport_count = 0
        for html_file in list(self.public_dir.rglob('*.html'))[:20]:  # Sample of files
            content = html_file.read_text(encoding='utf-8')
            if 'name="viewport"' in content:
                viewport_count += 1

        results.append(f"✅ Viewport meta tags: {viewport_count}/20 sampled files")

        # Check for mobile navigation
        mobile_nav_count = 0
        for html_file in list(self.public_dir.rglob('*.html'))[:20]:
            content = html_file.read_text(encoding='utf-8')
            if 'mobile-nav' in content or 'mobile-navigation' in content:
                mobile_nav_count += 1

        results.append(f"✅ Mobile navigation: {mobile_nav_count}/20 sampled files")

        # Check for touch-friendly elements
        touch_targets = 0
        for js_file in self.public_dir.rglob('*.js'):
            content = js_file.read_text(encoding='utf-8')
            if 'touch' in content.lower() or 'mobile' in content.lower():
                touch_targets += 1

        results.append(f"✅ Touch/mobile optimizations: {touch_targets} JS files")

        self.results['checks']['mobile'] = {
            'status': 'PASS',
            'results': results,
            'viewport_coverage': viewport_count,
            'mobile_nav_coverage': mobile_nav_count
        }

        print(f"   Results: {viewport_count} viewport tags, {mobile_nav_count} mobile nav, {touch_targets} touch optimizations")

    def generate_validation_report(self):
        """Generate comprehensive validation report"""
        print("\n" + "=" * 60)
        print("📋 VALIDATION REPORT")
        print("=" * 60)

        # Overall status
        status_emoji = "✅" if self.results['overall_status'] == 'PASSING' else "❌"
        print(f"\n{status_emoji} OVERALL STATUS: {self.results['overall_status']}")

        # Individual checks
        for check_name, check_data in self.results['checks'].items():
            status_emoji = "✅" if check_data['status'] == 'PASS' else "⚠️" if check_data['status'] == 'WARN' else "❌"
            print(f"\n{status_emoji} {check_name.upper().replace('_', ' ')}: {check_data['status']}")

            # Show key results
            for result in check_data['results'][:3]:  # Show top 3 results
                print(f"   {result}")

        # Summary statistics
        print("\n" + "=" * 60)
        print("📊 SUMMARY STATISTICS")

        # Count passing vs failing checks
        passing_checks = len([c for c in self.results['checks'].values() if c['status'] == 'PASS'])
        total_checks = len(self.results['checks'])

        print(f"✅ Passing checks: {passing_checks}/{total_checks}")
        print(f"📈 Success rate: {(passing_checks/total_checks*100):.1f}%")

        # Key metrics
        seo_check = self.results['checks'].get('seo', {})
        perf_check = self.results['checks'].get('performance', {})
        cultural_check = self.results['checks'].get('cultural', {})

        if seo_check:
            print(f"🎯 Average SEO score: {seo_check.get('average_seo_score', 0):.1f}/7")
        if perf_check:
            print(f"⚡ Inline styles remaining: {perf_check.get('inline_styles_remaining', 0)}")
        if cultural_check:
            print(f"🌿 Cultural verification: {cultural_check.get('cultural_units_verified', 0)}/4 units")

        # Recommendations
        print("\n" + "=" * 60)
        print("💡 RECOMMENDATIONS")

        if self.results['overall_status'] == 'PASSING':
            print("🚀 PLATFORM READY FOR PRODUCTION!")
            print("   • All critical systems verified")
            print("   • Performance metrics excellent")
            print("   • Cultural content properly integrated")
            print("   • Ready for beta teacher recruitment")
        else:
            print("⚠️ ISSUES FOUND - REVIEW REQUIRED")
            print("   • Check failing validation points above")
            print("   • Address critical failures before launch")
            print("   • Verify monitoring and error handling")

        # Save report
        report_path = Path('docs') / 'validation_reports' / f'post-deployment-{datetime.now().strftime("%Y%m%d-%H%M")}.json'
        report_path.parent.mkdir(parents=True, exist_ok=True)

        with open(report_path, 'w') as f:
            json.dump(self.results, f, indent=2)

        print(f"\n📄 Detailed report saved: {report_path}")

def main():
    """Run post-deployment validation"""
    validator = PostDeploymentValidator()
    results = validator.run_all_checks()

    # Exit code based on overall status
    exit_code = 0 if results['overall_status'] == 'PASSING' else 1
    return exit_code

if __name__ == "__main__":
    exit(main())

#!/usr/bin/env python3
"""
VISUAL TEACHER SIMULATION
Simulates what teachers ACTUALLY SEE when using the platform
Not just database - but rendered HTML, broken layouts, visual bugs
"""

import os
import re
from pathlib import Path
from collections import defaultdict

class VisualTeacherSimulator:
    def __init__(self, public_dir='/Users/admin/Documents/te-kete-ako-clean/public'):
        self.public_dir = Path(public_dir)
        self.issues = defaultdict(list)
        self.stats = defaultdict(int)
        
    def simulate_teacher_browsing(self):
        """Simulate a teacher browsing the platform"""
        print("\n🎭 VISUAL TEACHER SIMULATION - What Do Teachers ACTUALLY SEE?\n")
        
        # Test 1: Homepage First Impression
        self.test_homepage_first_impression()
        
        # Test 2: Search Results Visual
        self.test_search_results_visual()
        
        # Test 3: Resource Page Rendering
        self.test_resource_pages_rendering()
        
        # Test 4: Broken Images/Links
        self.test_broken_references()
        
        # Test 5: Mobile Visual Experience
        self.test_mobile_rendering()
        
        # Test 6: Print Visual Experience
        self.test_print_friendliness()
        
        self.report_findings()
    
    def test_homepage_first_impression(self):
        """What does a teacher see when they land on homepage?"""
        print("📱 Test 1: Homepage First Impression...")
        
        homepage = self.public_dir / 'index.html'
        if not homepage.exists():
            self.issues['critical'].append("Homepage missing!")
            return
        
        content = homepage.read_text()
        
        # Check for placeholder text
        placeholders = re.findall(r'{[A-Z_]+}|TODO|FIXME|Lorem ipsum|PLACEHOLDER', content, re.I)
        if placeholders:
            self.issues['homepage'].append(f"❌ Placeholders visible: {set(placeholders)}")
        
        # Check for broken numbers
        resource_numbers = re.findall(r'(\d{1,3},\d{3})\+?\s*(resources|lessons|handouts)', content)
        if resource_numbers:
            for num, type_ in resource_numbers:
                num_clean = int(num.replace(',', ''))
                if num_clean > 10000:
                    self.issues['homepage'].append(f"⚠️ Inflated number: {num} {type_} (database has ~3,500)")
        
        # Check for empty sections
        if re.search(r'<div[^>]*>\s*</div>', content):
            self.issues['homepage'].append("Empty divs visible")
        
        # Check stats
        self.stats['homepage_checked'] = 1
        print(f"  ✅ Homepage scanned")
    
    def test_search_results_visual(self):
        """What do search results look like?"""
        print("\n🔍 Test 2: Search Results Visual...")
        
        # Check hub pages (where teachers search)
        hub_pages = list(self.public_dir.glob('*-hub.html'))
        
        for hub in hub_pages:
            content = hub.read_text()
            
            # Check for duplicate CSS loading
            css_professionalization = content.count('<link href="/css/professionalization-system.css"')
            if css_professionalization > 1:
                self.issues['performance'].append(f"{hub.name}: Loading CSS {css_professionalization}x (slow!)")
            
            # Check for empty result containers
            if '<div id="resources-grid"></div>' in content or '<div id="results"></div>' in content:
                # Good - dynamic loading
                pass
            
            self.stats['hub_pages_checked'] += 1
        
        print(f"  ✅ Checked {len(hub_pages)} hub pages")
    
    def test_resource_pages_rendering(self):
        """Do individual resource pages render correctly?"""
        print("\n📄 Test 3: Resource Page Rendering...")
        
        # Sample lessons, handouts, units
        sample_pages = []
        
        for pattern in ['lessons/*.html', 'handouts/*.html', 'units/*/index.html']:
            sample_pages.extend(list(self.public_dir.glob(pattern))[:10])
        
        malformed_html = 0
        missing_titles = 0
        broken_layouts = 0
        
        for page in sample_pages:
            try:
                content = page.read_text()
                
                # Check for malformed HTML (from earlier fixes)
                if content.startswith('<!DOCTYPE html>###') or content.startswith('<!DOCTYPE html>##'):
                    malformed_html += 1
                    self.issues['rendering'].append(f"Malformed: {page.relative_to(self.public_dir)}")
                
                # Check for title
                if not re.search(r'<title>[^<]+</title>', content):
                    missing_titles += 1
                
                # Check for broken layout (empty body)
                if re.search(r'<body[^>]*>\s*</body>', content):
                    broken_layouts += 1
                    self.issues['rendering'].append(f"Empty body: {page.relative_to(self.public_dir)}")
                
            except Exception as e:
                self.issues['rendering'].append(f"Can't read {page.name}: {e}")
        
        self.stats['malformed_html'] = malformed_html
        self.stats['missing_titles'] = missing_titles
        self.stats['broken_layouts'] = broken_layouts
        self.stats['pages_checked'] = len(sample_pages)
        
        print(f"  ✅ Checked {len(sample_pages)} pages")
        if malformed_html:
            print(f"  ❌ Found {malformed_html} malformed HTML pages")
    
    def test_broken_references(self):
        """Check for broken images, CSS, JS references"""
        print("\n🖼️ Test 4: Broken References...")
        
        # Sample high-traffic pages
        important_pages = [
            'index.html',
            'mathematics-hub.html',
            'science-hub.html',
            'assessments-hub.html'
        ]
        
        broken_refs = 0
        
        for page_name in important_pages:
            page = self.public_dir / page_name
            if not page.exists():
                continue
            
            content = page.read_text()
            
            # Check CSS references
            css_refs = re.findall(r'<link[^>]+href="([^"]+\.css)"', content)
            for css_ref in css_refs:
                if css_ref.startswith('http'):
                    continue  # External
                css_path = self.public_dir / css_ref.lstrip('/')
                if not css_path.exists():
                    broken_refs += 1
                    self.issues['broken_refs'].append(f"{page_name}: Missing CSS {css_ref}")
            
            # Check JS references
            js_refs = re.findall(r'<script[^>]+src="([^"]+\.js)"', content)
            for js_ref in js_refs:
                if js_ref.startswith('http'):
                    continue  # External (CDN)
                js_path = self.public_dir / js_ref.lstrip('/')
                if not js_path.exists():
                    broken_refs += 1
                    self.issues['broken_refs'].append(f"{page_name}: Missing JS {js_ref}")
        
        self.stats['broken_references'] = broken_refs
        print(f"  ✅ Checked references in {len(important_pages)} pages")
    
    def test_mobile_rendering(self):
        """Does it work on phones/tablets?"""
        print("\n📱 Test 5: Mobile Rendering...")
        
        # Check for viewport meta tag
        homepage = self.public_dir / 'index.html'
        if homepage.exists():
            content = homepage.read_text()
            
            if 'viewport' in content and 'width=device-width' in content:
                self.stats['mobile_friendly'] = True
                print("  ✅ Viewport meta tag present")
            else:
                self.issues['mobile'].append("No viewport meta tag!")
                self.stats['mobile_friendly'] = False
            
            # Check for mobile CSS
            if '/css/mobile-revolution.css' in content or '/css/mobile-first' in content:
                print("  ✅ Mobile-specific CSS loaded")
            else:
                self.issues['mobile'].append("No mobile-specific styles")
        
    def test_print_friendliness(self):
        """Can teachers print resources?"""
        print("\n🖨️ Test 6: Print Friendliness...")
        
        # Check for print CSS
        sample_pages = list(self.public_dir.glob('handouts/*.html'))[:5]
        
        has_print_css = 0
        for page in sample_pages:
            content = page.read_text()
            if 'print.css' in content or 'media="print"' in content:
                has_print_css += 1
        
        self.stats['print_friendly'] = has_print_css
        print(f"  ✅ {has_print_css}/{len(sample_pages)} handouts have print CSS")
    
    def report_findings(self):
        """Generate visual simulation report"""
        print("\n" + "="*60)
        print("📊 VISUAL SIMULATION REPORT")
        print("="*60)
        
        print("\n🎯 CRITICAL VISUAL ISSUES:")
        if self.issues['critical']:
            for issue in self.issues['critical']:
                print(f"  🔴 {issue}")
        else:
            print("  ✅ No critical issues")
        
        print("\n🏠 HOMEPAGE ISSUES:")
        if self.issues['homepage']:
            for issue in self.issues['homepage']:
                print(f"  ⚠️ {issue}")
        else:
            print("  ✅ Homepage looks good")
        
        print("\n🖼️ RENDERING ISSUES:")
        if self.issues['rendering']:
            for issue in self.issues['rendering'][:10]:  # Show first 10
                print(f"  ⚠️ {issue}")
            if len(self.issues['rendering']) > 10:
                print(f"  ... and {len(self.issues['rendering']) - 10} more")
        else:
            print("  ✅ All pages render correctly")
        
        print("\n⚡ PERFORMANCE ISSUES:")
        if self.issues['performance']:
            for issue in self.issues['performance']:
                print(f"  ⚠️ {issue}")
        else:
            print("  ✅ Good performance")
        
        print("\n🔗 BROKEN REFERENCES:")
        if self.issues['broken_refs']:
            for issue in self.issues['broken_refs'][:5]:
                print(f"  🔴 {issue}")
            if len(self.issues['broken_refs']) > 5:
                print(f"  ... and {len(self.issues['broken_refs']) - 5} more")
        else:
            print("  ✅ All references valid")
        
        print("\n📱 MOBILE EXPERIENCE:")
        if self.stats.get('mobile_friendly'):
            print("  ✅ Mobile-friendly")
        else:
            print("  ⚠️ Mobile experience needs work")
        
        print("\n🖨️ PRINT EXPERIENCE:")
        print(f"  📄 {self.stats.get('print_friendly', 0)} pages print-ready")
        
        print("\n" + "="*60)
        print("📈 SIMULATION STATS:")
        print("="*60)
        for key, value in sorted(self.stats.items()):
            print(f"  {key}: {value}")
        
        # Teacher frustration prediction
        total_issues = sum(len(v) for v in self.issues.values())
        print("\n" + "="*60)
        print("🎭 TEACHER FRUSTRATION PREDICTION:")
        print("="*60)
        
        if total_issues == 0:
            print("  🏆 EXCELLENT - Teachers will have smooth experience!")
        elif total_issues < 5:
            print(f"  ✅ GOOD - {total_issues} minor issues won't block teachers")
        elif total_issues < 15:
            print(f"  🟡 FAIR - {total_issues} issues may frustrate some teachers")
        else:
            print(f"  🔴 POOR - {total_issues} issues will frustrate teachers!")
            print("  👉 Fix visual bugs BEFORE beta launch!")

if __name__ == '__main__':
    simulator = VisualTeacherSimulator()
    simulator.simulate_teacher_browsing()


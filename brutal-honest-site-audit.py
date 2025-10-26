#!/usr/bin/env python3
"""
BRUTAL HONEST SITE AUDIT
No optimism. No simulation. REAL problems.
Check ACTUAL files for ACTUAL issues.
"""

import os
import re
from pathlib import Path

class BrutalHonestAudit:
    def __init__(self):
        self.issues = []
        self.broken_count = 0
        self.placeholder_count = 0
        self.missing_css_count = 0
        self.broken_js_count = 0
        self.empty_pages = []
        self.duplicate_content = []
        
    def audit_html_files(self):
        """Check every HTML file for ACTUAL problems"""
        print("\n🔍 BRUTAL HONEST AUDIT - CHECKING REAL FILES...\n")
        
        html_files = list(Path('public').rglob('*.html'))
        print(f"📊 Scanning {len(html_files)} HTML files...\n")
        
        for filepath in html_files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Check for REAL problems
                self.check_broken_links(filepath, content)
                self.check_placeholders(filepath, content)
                self.check_missing_css(filepath, content)
                self.check_broken_js(filepath, content)
                self.check_empty_content(filepath, content)
                self.check_malformed_html(filepath, content)
                
            except Exception as e:
                self.issues.append({
                    'file': str(filepath),
                    'severity': 'HIGH',
                    'issue': f'Cannot read file: {e}'
                })
    
    def check_broken_links(self, filepath, content):
        """Find ACTUAL broken internal links"""
        # Find all href links
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
        
        for href in hrefs:
            # Skip external links
            if href.startswith('http') or href.startswith('#') or href.startswith('mailto'):
                continue
                
            # Skip valid paths
            if href.startswith('/') and not href.startswith('//'):
                # Check if file exists
                file_path = Path('public') / href.lstrip('/')
                
                # Remove query strings and anchors
                file_path = str(file_path).split('?')[0].split('#')[0]
                
                if not Path(file_path).exists() and not Path(file_path.rstrip('.html')).exists():
                    self.broken_count += 1
                    self.issues.append({
                        'file': str(filepath),
                        'severity': 'HIGH',
                        'issue': f'BROKEN LINK: {href} (file does not exist!)'
                    })
    
    def check_placeholders(self, filepath, content):
        """Find ACTUAL placeholders still in files"""
        placeholder_patterns = [
            r'\{[A-Z_]+\}',  # {PLACEHOLDER}
            r'TODO:',
            r'FIXME:',
            r'Lorem ipsum',
            r'placeholder',
            r'Coming soon',
            r'\[Your.*?\]',
            r'Example content',
        ]
        
        for pattern in placeholder_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                self.placeholder_count += len(matches)
                self.issues.append({
                    'file': str(filepath),
                    'severity': 'MEDIUM',
                    'issue': f'PLACEHOLDER FOUND: {len(matches)}x "{pattern}"'
                })
    
    def check_missing_css(self, filepath, content):
        """Check for CSS files that don't exist"""
        css_links = re.findall(r'<link[^>]*href=["\']([^"\']+\.css)["\']', content)
        
        for css_link in css_links:
            if css_link.startswith('/'):
                css_path = Path('public') / css_link.lstrip('/')
                if not css_path.exists():
                    self.missing_css_count += 1
                    self.issues.append({
                        'file': str(filepath),
                        'severity': 'HIGH',
                        'issue': f'MISSING CSS: {css_link} (404 error!)'
                    })
    
    def check_broken_js(self, filepath, content):
        """Check for JS files that don't exist"""
        js_links = re.findall(r'<script[^>]*src=["\']([^"\']+\.js)["\']', content)
        
        for js_link in js_links:
            if js_link.startswith('/'):
                js_path = Path('public') / js_link.lstrip('/')
                if not js_path.exists():
                    self.broken_js_count += 1
                    self.issues.append({
                        'file': str(filepath),
                        'severity': 'HIGH',
                        'issue': f'MISSING JS: {js_link} (404 error!)'
                    })
    
    def check_empty_content(self, filepath, content):
        """Find pages with almost no content"""
        # Remove HTML tags
        text_only = re.sub(r'<[^>]+>', '', content)
        text_only = text_only.strip()
        
        # If less than 200 characters of actual content
        if len(text_only) < 200:
            self.empty_pages.append(str(filepath))
            self.issues.append({
                'file': str(filepath),
                'severity': 'MEDIUM',
                'issue': f'EMPTY PAGE: Only {len(text_only)} chars of content!'
            })
    
    def check_malformed_html(self, filepath, content):
        """Check for ACTUAL HTML errors"""
        errors = []
        
        # Missing DOCTYPE
        if not content.strip().startswith('<!DOCTYPE'):
            errors.append('Missing DOCTYPE')
        
        # Missing <html>
        if '<html' not in content.lower():
            errors.append('Missing <html> tag')
        
        # Missing <head>
        if '<head' not in content.lower():
            errors.append('Missing <head> tag')
        
        # Missing <body>
        if '<body' not in content.lower():
            errors.append('Missing <body> tag')
        
        # Unclosed tags (basic check)
        open_divs = len(re.findall(r'<div[^>]*>', content))
        close_divs = len(re.findall(r'</div>', content))
        if abs(open_divs - close_divs) > 2:  # Allow small margin
            errors.append(f'Unclosed <div> tags: {open_divs} open, {close_divs} closed')
        
        if errors:
            self.issues.append({
                'file': str(filepath),
                'severity': 'HIGH',
                'issue': f'MALFORMED HTML: {", ".join(errors)}'
            })
    
    def print_results(self):
        """Print BRUTAL HONEST results"""
        print("\n" + "="*70)
        print("💀 BRUTAL HONEST AUDIT RESULTS")
        print("="*70 + "\n")
        
        # Count by severity
        high = [i for i in self.issues if i['severity'] == 'HIGH']
        medium = [i for i in self.issues if i['severity'] == 'MEDIUM']
        
        print(f"🔴 HIGH SEVERITY ISSUES: {len(high)}")
        print(f"🟡 MEDIUM SEVERITY ISSUES: {len(medium)}")
        print(f"📊 TOTAL ISSUES: {len(self.issues)}\n")
        
        # Summary stats
        print("="*70)
        print("📊 ISSUE BREAKDOWN:")
        print("="*70)
        print(f"🔗 Broken Links: {self.broken_count}")
        print(f"📝 Placeholders: {self.placeholder_count}")
        print(f"🎨 Missing CSS: {self.missing_css_count}")
        print(f"⚡ Missing JS: {self.broken_js_count}")
        print(f"📄 Empty Pages: {len(self.empty_pages)}")
        print()
        
        # Print HIGH severity first
        if high:
            print("="*70)
            print("🔴 HIGH SEVERITY (BREAKS SITE!):")
            print("="*70)
            for i, issue in enumerate(high[:20], 1):  # Top 20
                print(f"\n{i}. {Path(issue['file']).name}")
                print(f"   {issue['issue']}")
        
        # Print MEDIUM severity
        if medium:
            print("\n" + "="*70)
            print("🟡 MEDIUM SEVERITY (UX PROBLEMS):")
            print("="*70)
            for i, issue in enumerate(medium[:10], 1):  # Top 10
                print(f"\n{i}. {Path(issue['file']).name}")
                print(f"   {issue['issue']}")
        
        # THE TRUTH
        print("\n" + "="*70)
        print("💀 THE BRUTAL TRUTH:")
        print("="*70)
        
        if len(high) > 50:
            print(f"\n❌ SITE IS BROKEN: {len(high)} critical errors!")
            print("   Many pages will NOT load correctly.")
            print("   Users WILL see 404 errors.")
            print("   This needs IMMEDIATE fixing!")
        elif len(high) > 20:
            print(f"\n⚠️  SITE HAS ISSUES: {len(high)} critical errors.")
            print("   Some pages broken, but mostly functional.")
            print("   Needs fixing before beta launch!")
        elif len(high) > 0:
            print(f"\n🟡 SITE MOSTLY WORKS: {len(high)} critical errors.")
            print("   Minor issues, but functional overall.")
            print("   Polish needed.")
        else:
            print("\n✅ SITE IS CLEAN: No critical errors found!")
            print("   Ready for production!")
        
        if self.placeholder_count > 100:
            print(f"\n⚠️  {self.placeholder_count} PLACEHOLDERS = LOOKS UNFINISHED!")
        
        if len(self.empty_pages) > 50:
            print(f"\n⚠️  {len(self.empty_pages)} EMPTY PAGES = WASTELAND!")
        
        print("\n" + "="*70)
        print("💡 RECOMMENDATION:")
        print("="*70)
        
        if len(high) > 0:
            print("\n1. Fix HIGH severity issues FIRST (broken links, missing files)")
            print("2. Remove/fix placeholders (looks unprofessional)")
            print("3. Delete or fill empty pages")
            print("4. Test REAL user flows on REAL browser")
            print("5. Get HONEST user feedback")
        else:
            print("\nSite is technically solid! Focus on:")
            print("1. Content quality")
            print("2. User experience polish")
            print("3. Performance optimization")
        
        print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    auditor = BrutalHonestAudit()
    auditor.audit_html_files()
    auditor.print_results()


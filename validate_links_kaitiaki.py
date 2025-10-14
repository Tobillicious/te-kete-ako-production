#!/usr/bin/env python3
"""
KAITIAKI TŪHONO - Link Validation Script
Guardian of Connections - Systematic Link Healing

Validates all internal links across Te Kete Ako platform
Reports broken connections for healing
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json

class KaitiakiTuhono:
    """Guardian of Connections - Link Validator"""
    
    def __init__(self, root_dir="public"):
        self.root_dir = Path(root_dir)
        self.broken_links = []
        self.total_files = 0
        self.total_links = 0
        self.files_scanned = 0
        
    def find_all_html_files(self):
        """Find all HTML files in the site"""
        return list(self.root_dir.rglob("*.html"))
    
    def extract_links(self, file_path):
        """Extract all internal links from an HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all href links
            links = re.findall(r'href=["\']([^"\']+)["\']', content)
            
            # Filter for internal links only (start with / or relative)
            # Exclude: external (http://, https://,), protocol-relative (//), fragments (#), javascript:, mailto:
            internal_links = [
                link for link in links 
                if not link.startswith(('http://', 'https://', '//', 'mailto:', '#', 'javascript:'))
            ]
            
            return internal_links
        except Exception as e:
            print(f"⚠️  Error reading {file_path}: {e}")
            return []
    
    def resolve_link(self, source_file, link):
        """Resolve a link relative to source file"""
        source_dir = source_file.parent
        
        # Handle absolute paths (start with /) - these are relative to public/ (web root)
        if link.startswith('/'):
            # Absolute paths in HTML are relative to the web root (public/)
            target = self.root_dir / link.lstrip('/')
        else:
            # Handle relative paths
            target = source_dir / link
        
        # Normalize path
        try:
            target = target.resolve()
        except:
            return None
            
        return target
    
    def validate_file(self, file_path):
        """Validate all links in a single file"""
        links = self.extract_links(file_path)
        self.total_links += len(links)
        self.files_scanned += 1
        
        broken_in_file = []
        
        for link in links:
            # Skip query parameters and fragments for file existence check
            clean_link = link.split('?')[0].split('#')[0]
            
            if not clean_link:  # Just a fragment or query
                continue
                
            target = self.resolve_link(file_path, clean_link)
            
            if target and not target.exists():
                broken_in_file.append({
                    'source_file': str(file_path.relative_to(self.root_dir.parent)),
                    'broken_link': link,
                    'resolved_path': str(target) if target else 'Could not resolve',
                    'exists': False
                })
        
        return broken_in_file
    
    def validate_all(self):
        """Validate all HTML files in the site"""
        print("🔗 KAITIAKI TŪHONO - Beginning Systematic Validation")
        print("=" * 60)
        
        html_files = self.find_all_html_files()
        self.total_files = len(html_files)
        
        print(f"📊 Found {self.total_files} HTML files to validate")
        print(f"🎯 Scanning systematically...\n")
        
        # Validate each file
        for i, file_path in enumerate(html_files, 1):
            if i % 100 == 0:
                print(f"   Progress: {i}/{self.total_files} files ({i*100//self.total_files}%)")
            
            broken = self.validate_file(file_path)
            self.broken_links.extend(broken)
        
        print(f"\n✅ Validation Complete!")
        print(f"   Files scanned: {self.files_scanned}")
        print(f"   Links checked: {self.total_links}")
        print(f"   Broken links: {len(self.broken_links)}")
        
        return self.generate_report()
    
    def generate_report(self):
        """Generate comprehensive broken link report"""
        
        # Group broken links by source file
        by_file = defaultdict(list)
        for link in self.broken_links:
            by_file[link['source_file']].append(link)
        
        # Group by directory
        by_directory = defaultdict(int)
        for link in self.broken_links:
            directory = Path(link['source_file']).parent
            by_directory[str(directory)] += 1
        
        report = {
            'summary': {
                'total_files_scanned': self.files_scanned,
                'total_links_checked': self.total_links,
                'total_broken_links': len(self.broken_links),
                'files_with_broken_links': len(by_file),
                'percentage_broken': round((len(self.broken_links) / self.total_links * 100), 2) if self.total_links > 0 else 0
            },
            'by_file': dict(sorted(by_file.items(), key=lambda x: len(x[1]), reverse=True)),
            'by_directory': dict(sorted(by_directory.items(), key=lambda x: x[1], reverse=True)),
            'all_broken_links': self.broken_links
        }
        
        return report
    
    def print_summary(self, report):
        """Print human-readable summary"""
        print("\n" + "=" * 60)
        print("📋 VALIDATION SUMMARY")
        print("=" * 60)
        
        s = report['summary']
        print(f"\n✅ Files Scanned: {s['total_files_scanned']}")
        print(f"🔗 Links Checked: {s['total_links_checked']}")
        print(f"❌ Broken Links: {s['total_broken_links']} ({s['percentage_broken']}%)")
        print(f"📄 Files with Issues: {s['files_with_broken_links']}")
        
        if s['total_broken_links'] > 0:
            print(f"\n🎯 TOP 10 FILES WITH MOST BROKEN LINKS:")
            for file, links in list(report['by_file'].items())[:10]:
                print(f"   {len(links):3d} broken - {file}")
            
            print(f"\n🗂️  TOP DIRECTORIES WITH BROKEN LINKS:")
            for directory, count in list(report['by_directory'].items())[:10]:
                print(f"   {count:3d} broken - {directory}")
        else:
            print(f"\n🎉 NO BROKEN LINKS FOUND! All connections healthy! ✨")
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    # Initialize Guardian
    guardian = KaitiakiTuhono(root_dir="public")
    
    # Validate all links
    report = guardian.validate_all()
    
    # Print summary
    guardian.print_summary(report)
    
    # Save detailed report
    output_file = "KAITIAKI_BROKEN_LINKS_REPORT.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Detailed report saved: {output_file}")
    print("\n🔗 Kaitiaki Tūhono - Validation Complete")
    print("'Ko te tūhono te pūtake o te mātauranga'")
    print("Connection is the foundation of knowledge ✨\n")


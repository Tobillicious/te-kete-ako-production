#!/usr/bin/env python3
"""
Te Kete Ako Link Validation System
Quick check for broken internal links
"""

import os
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse
import json

class LinkChecker:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.broken_links = []
        self.valid_links = []
        
    def check_links(self):
        """Check all internal links in HTML files"""
        html_files = list(self.root_dir.rglob("*.html"))
        
        print(f"🔍 Checking links in {len(html_files)} HTML files...")
        
        for file_path in html_files:
            self.check_file_links(file_path)
        
        return {
            'total_files': len(html_files),
            'broken_links': len(self.broken_links),
            'valid_links': len(self.valid_links),
            'broken_details': self.broken_links
        }
    
    def check_file_links(self, file_path):
        """Check links in a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all href attributes
            href_pattern = r'href="([^"#]*(?:\.html)?[^"]*)"'
            matches = re.finditer(href_pattern, content)
            
            for match in matches:
                link = match.group(1)
                
                # Skip external links, mailto, tel, javascript
                if any(link.startswith(prefix) for prefix in ['http', 'mailto:', 'tel:', 'javascript:', '#']):
                    continue
                
                # Skip empty links
                if not link.strip():
                    continue
                
                # Resolve relative path
                if link.startswith('../'):
                    target_path = file_path.parent / link
                elif link.startswith('./'):
                    target_path = file_path.parent / link[2:]
                else:
                    target_path = file_path.parent / link
                
                try:
                    target_path = target_path.resolve()
                    
                    if target_path.exists():
                        self.valid_links.append({
                            'source': str(file_path.relative_to(self.root_dir)),
                            'link': link,
                            'target': str(target_path.relative_to(self.root_dir))
                        })
                    else:
                        self.broken_links.append({
                            'source_file': str(file_path.relative_to(self.root_dir)),
                            'broken_link': link,
                            'resolved_path': str(target_path),
                            'line': content[:match.start()].count('\n') + 1
                        })
                        
                except Exception as e:
                    self.broken_links.append({
                        'source_file': str(file_path.relative_to(self.root_dir)),
                        'broken_link': link,
                        'error': str(e),
                        'line': content[:match.start()].count('\n') + 1
                    })
                    
        except Exception as e:
            print(f"Error checking {file_path}: {e}")

def main():
    checker = LinkChecker("/Users/admin/Documents/te-kete-ako-clean")
    results = checker.check_links()
    
    print(f"\n📊 LINK CHECK RESULTS")
    print("=" * 30)
    print(f"✅ Valid links: {results['valid_links']}")
    print(f"❌ Broken links: {results['broken_links']}")
    print(f"📄 Files checked: {results['total_files']}")
    
    if results['broken_links'] > 0:
        print(f"\n🔗 BROKEN LINKS (showing first 10):")
        for link in results['broken_details'][:10]:
            print(f"   • {link['source_file']} → {link['broken_link']}")
    
    # Save results
    with open('link_check_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📄 Full results saved to link_check_results.json")
    return results

if __name__ == "__main__":
    main()
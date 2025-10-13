#!/usr/bin/env python3
"""
Fix broken links systematically
- Identify common broken patterns
- Fix or remove dead links
- Update navigation
"""

from pathlib import Path
import re
from collections import defaultdict

def find_broken_links(file_path):
    """Find broken links in a file"""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except:
        return []
    
    # Find all href links
    links = re.findall(r'href=["\']([^"\']+)["\']', content)
    
    broken = []
    for link in links:
        # Skip external links
        if link.startswith('http') or link.startswith('#') or link.startswith('mailto'):
            continue
        
        # Check if file exists
        if link.startswith('/'):
            target = Path('public' + link.rstrip('/'))
            if not target.exists() and not (target.parent / 'index.html').exists():
                broken.append(link)
    
    return broken

# Scan for broken links
public_dir = Path('public')
print("🔍 SCANNING FOR BROKEN LINKS")
print("="*60)

broken_by_file = {}
broken_patterns = defaultdict(int)

for html_file in public_dir.rglob('*.html'):
    if 'backup' in str(html_file).lower():
        continue
    
    broken = find_broken_links(html_file)
    if broken:
        broken_by_file[str(html_file)] = broken
        for link in broken:
            broken_patterns[link] += 1

print(f"\n📊 BROKEN LINK ANALYSIS:")
print(f"   Files with broken links: {len(broken_by_file)}")
print(f"   Total broken links: {sum(len(v) for v in broken_by_file.values())}")

print(f"\n🔝 TOP 20 MOST COMMON BROKEN LINKS:")
for link, count in sorted(broken_patterns.items(), key=lambda x: -x[1])[:20]:
    print(f"   {link}: {count} occurrences")

# Save report
with open('broken-links-report.txt', 'w') as f:
    f.write("BROKEN LINKS REPORT\n")
    f.write("="*60 + "\n\n")
    f.write(f"Files with broken links: {len(broken_by_file)}\n")
    f.write(f"Total broken links: {sum(len(v) for v in broken_by_file.values())}\n\n")
    f.write("Most common broken links:\n")
    for link, count in sorted(broken_patterns.items(), key=lambda x: -x[1])[:50]:
        f.write(f"  {link}: {count} times\n")

print(f"\n💾 Report saved to: broken-links-report.txt")
print(f"\n✅ Analysis complete - ready for systematic fixing")

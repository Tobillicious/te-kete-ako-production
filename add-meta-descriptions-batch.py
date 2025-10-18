#!/usr/bin/env python3
"""
Add Meta Descriptions to ALL Files Missing Them
Systematic, one by one
"""

from pathlib import Path
import re

print("📝 SYSTEMATIC META DESCRIPTION ADDITION")
print("=" * 70)

# Find all HTML files missing meta descriptions
missing_meta = []
for html_file in Path('public').rglob('*.html'):
    if any(x in str(html_file) for x in ['/archive/', '.master', '.bak', '.backup', 'node_modules']):
        continue
    
    try:
        content = html_file.read_text(encoding='utf-8', errors='ignore')
        if '<meta name="description"' not in content:
            missing_meta.append(html_file)
    except:
        pass

print(f"Found {len(missing_meta)} files missing meta descriptions")
print("Adding descriptions based on file content...\n")

added = 0
for i, filepath in enumerate(missing_meta[:50], 1):  # Process first 50
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        
        # Extract title for description
        title_match = re.search(r'<title>([^<|]+)', content, re.I)
        title = title_match.group(1).strip() if title_match else filepath.stem
        
        # Extract first paragraph for description
        p_match = re.search(r'<p[^>]*>([^<]+)</p>', content, re.I)
        first_p = p_match.group(1).strip()[:150] if p_match else f"{title} - Educational resource from Te Kete Ako"
        
        # Create meta description
        meta_desc = f'    <meta name="description" content="{first_p}">\n'
        
        # Insert after title
        if '<title>' in content and '<meta name="description"' not in content:
            content = re.sub(
                r'(<title>[^<]+</title>)',
                r'\1\n' + meta_desc,
                content,
                count=1
            )
            filepath.write_text(content, encoding='utf-8')
            added += 1
            
            if added % 10 == 0:
                print(f"   ✅ Added {added} meta descriptions...")
                
    except Exception as e:
        pass

print(f"\n✅ Added meta descriptions to {added} files")
print("=" * 70)

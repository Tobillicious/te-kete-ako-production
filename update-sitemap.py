#!/usr/bin/env python3
"""
Update Sitemap to Include Generated Resources Alpha Pages
Adds the 51 excellent pages from generated-resources-alpha to the sitemap for SEO

Issue: Generated resources are well-linked in navigation but missing from sitemap
This means search engines can't discover these high-quality resources
"""

import os
import re
from pathlib import Path
from datetime import datetime

def update_sitemap():
    """Add generated-resources-alpha pages to sitemap.xml"""

    # Read current sitemap
    with open('public/sitemap.xml', 'r', encoding='utf-8') as f:
        sitemap_content = f.read()

    # Get all HTML files in generated-resources-alpha
    alpha_dir = Path('public/generated-resources-alpha')
    alpha_files = list(alpha_dir.rglob('*.html'))

    print(f"🔍 Found {len(alpha_files)} pages in generated-resources-alpha")

    # Generate sitemap entries
    new_entries = []
    current_date = datetime.now().strftime('%Y-%m-%d')

    for file_path in alpha_files:
        # Get relative path from public directory
        rel_path = str(file_path.relative_to(Path('public')))

        # Convert to URL
        url = f'https://tekete.netlify.app/{rel_path}'

        # Determine priority based on content
        if 'index.html' in rel_path:
            priority = '0.9'
        elif 'handouts' in rel_path:
            priority = '0.8'
        elif 'lessons' in rel_path:
            priority = '0.8'
        else:
            priority = '0.7'

        entry = f'''  <url>
    <loc>{url}</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>'''

        new_entries.append(entry)

    # Find where to insert the new entries (before closing </urlset>)
    insert_pattern = r'(</urlset>)'

    if re.search(insert_pattern, sitemap_content):
        # Insert before closing </urlset>
        updated_sitemap = re.sub(insert_pattern, '\n'.join(new_entries) + r'\n\1', sitemap_content)

        # Write back to file
        with open('public/sitemap.xml', 'w', encoding='utf-8') as f:
            f.write(updated_sitemap)

        print(f"✅ Added {len(new_entries)} pages to sitemap")
        print("🚀 Generated resources now discoverable by search engines!")
        return True

    return False

def main():
    """Update sitemap with generated resources"""

    print("🔧 Updating sitemap.xml to include generated-resources-alpha pages...")

    if update_sitemap():
        print("✅ Sitemap updated successfully!")
        print("   - Added all 51 generated-resources-alpha pages")
        print("   - Pages now discoverable by search engines")
        print("   - Improved SEO for high-quality cultural resources")
    else:
        print("❌ Failed to update sitemap")

if __name__ == '__main__':
    main()

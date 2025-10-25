#!/usr/bin/env python3
"""
SEO Tags Automation Script for Te Kete Ako
Adds Open Graph, Twitter Cards, and canonical URLs to all HTML files

Based on audit findings: Missing SEO tags causing poor social sharing and discoverability
"""

import os
import re
from pathlib import Path

def add_seo_tags_to_file(file_path):
    """Add comprehensive SEO tags to a single HTML file"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract page title and description
    title_match = re.search(r'<title>([^<]+)</title>', content)
    desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']+)["\'][^>]*>', content)

    page_title = title_match.group(1) if title_match else "Te Kete Ako"
    page_description = desc_match.group(1) if desc_match else "World-class educational resources integrating mātauranga Māori with modern pedagogy"

    # Get relative path for URL construction
    rel_path = str(file_path.relative_to(Path('public')))
    if rel_path == 'index.html':
        page_url = 'https://tekete.netlify.app/'
    else:
        page_url = f'https://tekete.netlify.app/{rel_path.replace("index.html", "").rstrip("/")}'

    # SEO tags to add
    seo_tags = f'''<!-- SEO TAGS - Open Graph, Twitter Cards, Canonical URL -->
<!-- Open Graph / Facebook -->
<meta property="og:type" content="website"/>
<meta property="og:url" content="{page_url}"/>
<meta property="og:title" content="{page_title}"/>
<meta property="og:description" content="{page_description}"/>
<meta property="og:image" content="https://tekete.netlify.app/images/og-image.jpg"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:image:alt" content="Te Kete Ako - Educational Platform"/>
<meta property="og:site_name" content="Te Kete Ako"/>
<meta property="og:locale" content="en_NZ"/>

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:url" content="{page_url}"/>
<meta name="twitter:title" content="{page_title}"/>
<meta name="twitter:description" content="{page_description}"/>
<meta name="twitter:image" content="https://tekete.netlify.app/images/twitter-card.jpg"/>
<meta name="twitter:image:alt" content="Te Kete Ako - Educational Platform"/>
<meta name="twitter:site" content="@TeKeteAko"/>
<meta name="twitter:creator" content="@TeKeteAko"/>

<!-- Canonical URL -->
<link rel="canonical" href="{page_url}"/>

<!-- Additional SEO -->
<meta name="robots" content="index, follow"/>
<meta name="googlebot" content="index, follow"/>
<meta name="theme-color" content="#1a4d2e"/>

'''

    # Find where to insert the tags (after existing meta tags, before CSS)
    insert_pattern = r'(<meta[^>]*>[\s\n]*</head>)'

    if re.search(insert_pattern, content):
        # Insert before closing </head>
        content = re.sub(insert_pattern, seo_tags + r'\1', content)
    else:
        # Fallback: insert after title
        content = re.sub(r'(</title>)', r'\1\n' + seo_tags, content)

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    """Process all HTML files in the public directory"""

    public_dir = Path('public')
    html_files = list(public_dir.rglob('*.html'))

    print(f"🔍 Found {len(html_files)} HTML files to process")

    processed = 0
    skipped = 0

    for html_file in html_files:
        try:
            add_seo_tags_to_file(html_file)
            processed += 1
            print(f"✅ {html_file}")
        except Exception as e:
            skipped += 1
            print(f"❌ {html_file}: {e}")

    print("\n📊 Summary:")
    print(f"   ✅ Processed: {processed} files")
    print(f"   ❌ Skipped: {skipped} files")
    print(f"   📱 Total: {len(html_files)} files")
    print("\n🚀 SEO tags added to all pages!")
    print("   - Open Graph tags for Facebook sharing")
    print("   - Twitter Card tags for Twitter sharing")
    print("   - Canonical URLs for SEO")
    print("   - Robot directives for search engines")

if __name__ == '__main__':
    main()

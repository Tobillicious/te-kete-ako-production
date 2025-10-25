#!/usr/bin/env python3
"""
Add SEO Tags to Generated Resources Alpha Pages
Adds comprehensive SEO tags to the 51 excellent pages in generated-resources-alpha

Issue: These high-quality pages need proper SEO tags for maximum discoverability
"""

import os
import re
from pathlib import Path

def add_seo_to_alpha_file(file_path):
    """Add SEO tags to a single alpha resource file"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = False

    # Extract page title for SEO
    title_match = re.search(r'<title>([^<]+)</title>', content)
    page_title = title_match.group(1) if title_match else "Te Kete Ako Resource"

    # Get relative path for URL construction
    rel_path = str(file_path.relative_to(Path('public')))
    page_url = f'https://tekete.netlify.app/{rel_path}'

    # SEO tags to add
    seo_tags = f'''<!-- SEO TAGS - Open Graph, Twitter Cards, Canonical URL -->
<!-- Open Graph / Facebook -->
<meta property="og:type" content="article"/>
<meta property="og:url" content="{page_url}"/>
<meta property="og:title" content="{page_title}"/>
<meta property="og:description" content="High-quality educational resource integrating mātauranga Māori with contemporary learning. Part of Te Kete Ako's excellence collection."/>
<meta property="og:image" content="https://tekete.netlify.app/images/og-image.jpg"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:image:alt" content="Te Kete Ako - Educational Resource"/>
<meta property="og:site_name" content="Te Kete Ako"/>
<meta property="og:locale" content="en_NZ"/>

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:url" content="{page_url}"/>
<meta name="twitter:title" content="{page_title}"/>
<meta name="twitter:description" content="High-quality educational resource integrating mātauranga Māori with contemporary learning. Part of Te Kete Ako's excellence collection."/>
<meta name="twitter:image" content="https://tekete.netlify.app/images/twitter-card.jpg"/>
<meta name="twitter:image:alt" content="Te Kete Ako - Educational Resource"/>
<meta name="twitter:site" content="@TeKeteAko"/>
<meta name="twitter:creator" content="@TeKeteAko"/>

<!-- Canonical URL -->
<link rel="canonical" href="{page_url}"/>

<!-- Additional SEO -->
<meta name="robots" content="index, follow"/>
<meta name="googlebot" content="index, follow"/>

'''

    # Find where to insert the tags (after existing meta tags, before CSS)
    insert_pattern = r'(<meta[^>]*name=["\']theme-color["\'][^>]*>)'

    if re.search(insert_pattern, content):
        # Insert after theme-color meta
        content = re.sub(insert_pattern, r'\1\n' + seo_tags, content)
        changes_made = True

    # Write back if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    """Process all files in generated-resources-alpha directory"""

    alpha_dir = Path('public/generated-resources-alpha')
    alpha_files = list(alpha_dir.rglob('*.html'))

    print(f"🔍 Found {len(alpha_files)} pages in generated-resources-alpha")

    processed = 0
    fixed = 0

    for alpha_file in alpha_files:
        try:
            if add_seo_to_alpha_file(alpha_file):
                fixed += 1
                print(f"✅ Added SEO: {alpha_file}")
            processed += 1
        except Exception as e:
            print(f"❌ Error processing {alpha_file}: {e}")

    print("\n📊 Summary:")
    print(f"   📁 Processed: {processed} files")
    print(f"   ✅ Added SEO: {fixed} files")
    print("\n🚀 Alpha resources enhanced!")
    print("   - Added Open Graph tags for Facebook sharing")
    print("   - Added Twitter Card tags for Twitter sharing")
    print("   - Added canonical URLs for SEO")
    print("   - Enhanced discoverability of high-quality cultural resources")

if __name__ == '__main__':
    main()

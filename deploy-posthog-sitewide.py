#!/usr/bin/env python3
"""
📊 DEPLOY POSTHOG ANALYTICS SITEWIDE
Add PostHog tracking to all 1,828 pages
October 19, 2025 - Priority #5 Deployment
"""

import re
from pathlib import Path

print("📊 DEPLOYING POSTHOG ANALYTICS SITEWIDE")
print("=" * 70)

# Find all HTML files in public/
public_dir = Path('public')
html_files = list(public_dir.rglob('*.html'))

print(f"\n📊 Found {len(html_files)} HTML files in public/")

# POSTHOG ANALYTICS INJECTION
POSTHOG_SCRIPT = '''
<!-- 📊 ULTIMATE BEAUTY: PostHog Analytics (Privacy-First) -->
<script src="/js/posthog-analytics.js" defer></script>'''

# Track progress
files_updated = 0
files_skipped = 0
files_error = 0

def add_posthog(filepath):
    """Add PostHog analytics to a file if not present"""
    global files_updated, files_skipped, files_error
    
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Skip if already has PostHog
        if 'posthog-analytics.js' in content:
            files_skipped += 1
            return False
        
        # Skip component files
        if '/components/' in str(filepath):
            files_skipped += 1
            return False
        
        # Add PostHog script before </body>
        if '</body>' in content:
            content = content.replace(
                '</body>',
                POSTHOG_SCRIPT + '\n\n</body>'
            )
            filepath.write_text(content, encoding='utf-8')
            files_updated += 1
            return True
        else:
            files_skipped += 1
            return False
            
    except Exception as e:
        print(f"   ⚠️  Error: {filepath.name} - {e}")
        files_error += 1
        return False

# Process all files
print("\n🚀 ADDING POSTHOG TO ALL PAGES:\n")

for i, filepath in enumerate(html_files, 1):
    if add_posthog(filepath):
        if i % 100 == 0:
            print(f"   ✅ {i}/{len(html_files)}: {filepath.name}")

print("\n" + "=" * 70)
print("✅ POSTHOG ANALYTICS DEPLOYMENT COMPLETE")
print("=" * 70)
print(f"\n✅ Files updated: {files_updated}")
print(f"⏭️  Files skipped: {files_skipped}")
print(f"⚠️  Errors: {files_error}")
print(f"\n📊 PostHog now tracking on {files_updated} pages!")
print("\n🌿 Privacy-first analytics with kaitiakitanga! 🌿")


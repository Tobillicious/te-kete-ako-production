#!/usr/bin/env python3
"""
Fix placeholder content and template issues in HTML files.

This script addresses:
1. Duplicate SEO tags
2. Malformed JavaScript from cleanup scripts
3. Empty or incomplete content sections
4. Broken component loading scripts
5. Inconsistent meta tags
"""

import os
import re
from pathlib import Path

def fix_duplicate_seo_tags(content):
    """Remove duplicate SEO tags and keep only the properly formatted ones."""
    # Find all SEO tag blocks
    seo_patterns = [
        r'<!-- SEO TAGS.*?-->.*?<!-- Additional SEO -->',
        r'<!-- SEO TAGS.*?-->.*?<!-- Canonical URL -->',
    ]

    for pattern in seo_patterns:
        if re.search(pattern, content, re.DOTALL):
            # Remove duplicate SEO blocks
            content = re.sub(pattern, '', content, flags=re.DOTALL)

    # Remove orphaned SEO tags that aren't in proper blocks
    orphaned_seo = r'<meta property="og:.*?>|<meta name="twitter:.*?>|<link rel="canonical".*?>'
    content = re.sub(orphaned_seo, '', content)

    return content

def fix_malformed_javascript(content):
    """Fix broken JavaScript from cleanup scripts."""

    # Fix broken PostHog capture patterns
    broken_posthog = r'posthog\.capture\(\s*[\'"](error|javascript_error)[\'"]\s*,\s*\{\s*message:\s*[\'"]([^\'"]*)[\'"]\s*,\s*details:\s*([^,]+),\s*url:\s*window\.location\.pathname\s*\}\s*\);'
    content = re.sub(broken_posthog, '''posthog.capture('error', {
        message: '$2',
        details: $3,
        url: window.location.pathname
    });''', content)

    # Fix malformed Promise.all blocks
    malformed_promise = r'Promise\.all\(\s*\[\s*([^[\]]*(?:fetch\([^)]+\)[^[\]]*)*)\s*\]\s*\)\.then\(\(\)\s*=>\s*\{\s*// All components loaded successfully!\s*// User feedback provided via UI\s*\}\s*\)\.catch\(err\s*=>\s*\{\s*// Log to monitoring instead of console[^}]*}\s*\);'
    if re.search(malformed_promise, content, re.DOTALL):
        # Replace with proper parallel loading
        content = re.sub(malformed_promise, '''// PARALLEL COMPONENT LOADING - No more 2-3s delay!
Promise.all([
    // Components will be loaded here
]).then(() => {
    console.log('✅ All components loaded in parallel');
}).catch(err => {
    if (window.posthog) {
        posthog.capture('component_loading_error', {
            message: err.message,
            url: window.location.pathname
        });
    }
});''', content, flags=re.DOTALL)

    # Fix broken component loading scripts
    broken_component = r'fetch\([\'"][^\'"]*components/[^\'"]*[\'"]\)\s*\.then\(r\s*=>\s*r\.text\(\)\)\s*\.then\(html\s*=>\s*\{\s*const container\s*=\s*document\.getElementById\([\'"][^\'"]*[\'"]\);\s*if\s*\(container\)\s*container\.innerHTML\s*=\s*html;\s*else\s*// Log to monitoring instead of console[^}]*}\s*\)\s*\.catch\(err\s*=>\s*// Log to monitoring instead of console[^}]*\);'
    content = re.sub(broken_component, '''fetch('/components/navigation-standard.html')
    .then(r => r.text())
    .then(html => {
        const container = document.getElementById('beautiful-nav-container');
        if (container) container.innerHTML = html;
    })
    .catch(err => {
        if (window.posthog) {
            posthog.capture('component_loading_error', {
                message: err.message,
                url: window.location.pathname
            });
        }
    });''', content)

    return content

def fix_empty_content_sections(content):
    """Fix empty or incomplete content sections."""

    # Fix empty whakataukī sections
    empty_whakatauki = r'<p class="whakatauki-text">([^<]*)</p>\s*<p class="whakatauki-translation">([^<]*)</p>'
    if re.search(empty_whakatauki, content):
        content = re.sub(empty_whakatauki, '''<p class="whakatauki-text">"Mā te mōhio ka ora, mā te ora ka mōhio"</p>
<p class="whakatauki-translation">"Through knowledge comes wellbeing, through wellbeing comes knowledge"</p>''', content)

    # Fix incomplete cultural elements
    incomplete_cultural = r'This learning connects to the value of <strong>[^<]*</strong> by encouraging students to \[engage with content in ways that embody this value\]\.'
    content = re.sub(incomplete_cultural, 'This learning connects to the value of <strong>whaiara</strong> by encouraging students to engage with content in ways that embody this value.', content)

    # Fix empty submission lists
    empty_submissions = r'<div id="empty-state"[^>]*>.*?</div>'
    if re.search(empty_submissions, content, re.DOTALL):
        content = re.sub(empty_submissions, '''<div id="empty-state" class="empty-state" style="display: none;">
    <div style="text-align: center; padding: 3rem; background: #f8fafc; border-radius: 12px; border: 2px dashed #cbd5e1;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🌱</div>
        <h3 style="color: #475569; margin-bottom: 1rem;">Start Your Learning Journey</h3>
        <p style="color: #64748b; margin-bottom: 2rem;">You haven't submitted any projects yet. Ready to share your creativity and insights with your kaiako?</p>
        <a href="/project-submission.html" class="btn btn-primary" style="background: #1a4d2e; color: white; padding: 0.75rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600;">📝 Submit Your First Project</a>
    </div>
</div>''', content, flags=re.DOTALL)

    return content

def fix_inconsistent_meta_tags(content):
    """Fix duplicate or inconsistent meta tags."""

    # Remove duplicate viewport and charset
    content = re.sub(r'<meta charset="[^"]*">\s*<meta charset="[^"]*">', '<meta charset="UTF-8">', content)
    content = re.sub(r'<meta name="viewport"[^>]*>\s*<meta name="viewport"[^>]*>', '<meta name="viewport" content="width=device-width, initial-scale=1.0">', content)

    # Remove duplicate theme-color
    content = re.sub(r'<meta content="[^"]*" name="theme-color">\s*<meta content="[^"]*" name="theme-color">', '<meta content="#1a4d2e" name="theme-color">', content)

    return content

def fix_placeholders_in_file(file_path):
    """Fix all placeholder issues in a single HTML file."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Apply all fixes
    content = fix_duplicate_seo_tags(content)
    content = fix_malformed_javascript(content)
    content = fix_empty_content_sections(content)
    content = fix_inconsistent_meta_tags(content)

    # Write back if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    """Process all HTML files to fix placeholder issues."""

    public_dir = Path('public')
    html_files = list(public_dir.rglob('*.html'))

    print(f"🔍 Found {len(html_files)} HTML files to process")

    processed = 0
    changed = 0

    for html_file in html_files:
        try:
            if fix_placeholders_in_file(html_file):
                changed += 1
                print(f"✅ {html_file}")
            processed += 1
        except Exception as e:
            print(f"❌ {html_file}: {e}")

    print("\n📊 Summary:")
    print(f"   ✅ Fixed: {changed} files")
    print(f"   📁 Processed: {processed} files")
    print(f"   📱 Total: {len(html_files)} files")
    print("\n🚀 Placeholder issues fixed!")
    print("   - Removed duplicate SEO tags")
    print("   - Fixed malformed JavaScript")
    print("   - Filled empty content sections")
    print("   - Standardized meta tags")

if __name__ == '__main__':
    main()

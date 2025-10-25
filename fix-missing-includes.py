#!/usr/bin/env python3
"""
Fix Missing CSS/JS Includes - Comprehensive Include System
Adds all missing CSS and JS imports to HTML files across the site

Issue: 966+ missing includes found in audit - pages missing essential CSS/JS
Components missing: navigation, professional styling, component loader, search, etc.
"""

import os
import re
from pathlib import Path

def fix_missing_includes_in_file(file_path):
    """Add missing CSS/JS includes to a single HTML file"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = False

    # Check if this is already a properly structured page (has the unified system)
    has_professional_css = 'css/te-kete-professional.css' in content
    has_navigation_css = 'css/navigation-standard.css' in content
    has_component_loader = 'js/component-loader.js' in content
    has_enhanced_search = 'js/enhanced-search.js' in content

    # Only process files that need the full include system (most pages)
    needs_full_includes = not (has_professional_css and has_navigation_css and has_component_loader)

    if not needs_full_includes:
        return False

    # Essential includes to add (based on index.html structure)
    essential_includes = '''
<!-- UNIFIED DESIGN SYSTEM -->
<!-- PWA Manifest -->
<link href="/manifest.json" rel="manifest"/>
<meta content="#1a4d2e" name="theme-color"/>

<!-- CSS - UNIFIED PROFESSIONAL DESIGN SYSTEM (CONSOLIDATED) -->
<!-- ⭐ PROFESSIONAL SYSTEM FIRST - Core design tokens -->
<link rel="stylesheet" href="/css/professionalization-system.css">

<!-- ⭐ THEME SYSTEM (Tailwind + Ultimate Beauty) -->
<link rel="stylesheet" href="/css/te-kete-professional.css"/>
<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css"/>

<!-- ⭐ COMPONENT STYLES -->
<link rel="stylesheet" href="/css/main.css">
<link rel="stylesheet" href="/css/navigation-standard.css">
<link rel="stylesheet" href="/css/mobile-revolution.css">
<link rel="stylesheet" href="/css/mobile-first-classroom-tablets.css"/>

<!-- ⭐ PRINT STYLES (media="print" = only for printing) -->
<link rel="stylesheet" href="/css/print.css" media="print"/>
<link rel="stylesheet" href="/css/print-professional.css" media="print"/>

<!-- ⭐ TAILWIND (Loads second-to-last - utilities only, NO DUPLICATES) -->
<link rel="stylesheet" href="/css/tailwind.css">

<!-- ⭐ CASCADE FIX (Loads LAST - overrides conflicting variables) -->
<link rel="stylesheet" href="/css/cascade-fix.css">

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
    // Wait for Supabase CDN to load before initializing singleton
    window.addEventListener('DOMContentLoaded', () => {
        if (!window.supabase) {
            // Log to monitoring instead of console
            if (window.posthog) {
                posthog.capture('supabase_cdn_error', {
                    message: 'Supabase CDN failed to load',
                    url: window.location.pathname
                });
            }
        }
    });
</script>
<script src="/js/supabase-singleton.js"></script>
<!-- My Kete Database Integration - loads after singleton -->
<script src="/js/my-kete-database.js"></script>
<!-- Navigation Loader Singleton - loads after supabase setup -->
<script src="/js/navigation-loader.js"></script>
<!-- Component Loader - centralized async component management -->
<script src="/js/component-loader.js"></script>
<meta name="mobile-web-app-capable" content="yes"/>
<meta content="yes" name="apple-mobile-web-app-capable"/>
<meta content="black-translucent" name="apple-mobile-web-app-status-bar-style"/>
<meta content="Te Kete Ako" name="apple-mobile-web-app-title"/>
<link href="/icons/icon-192x192.png" rel="apple-touch-icon"/>
<!-- ENHANCED SEARCH -->
<script src="/js/enhanced-search.js" defer></script>
<!-- MOBILE PERFORMANCE OPTIMIZER -->
<script src="/js/mobile-performance-optimizer.js" defer></script>
<!-- TOUCH TARGET AUDITOR -->
<script src="/js/touch-target-auditor.js" defer></script>
<!-- 🎨 ULTIMATE CULTURAL GESTURES - Framer Motion System -->
<script src="/js/framer-cultural-gestures-ultimate.js" defer></script>
<!-- Service Worker Registration -->
<script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('/service-worker.js')
                    .then(registration => {
                        console.log('✅ PWA: Service Worker registered!', registration);
                    })
                    .catch(error => {
                        // Log to monitoring instead of console
                        if (window.posthog) {
                            posthog.capture('pwa_service_worker_error', {
                                message: 'Service Worker registration failed',
                                error: error.message,
                                url: window.location.pathname
                            });
                        }
                    });
            });
        }
</script>'''

    # Find where to insert the includes (after <head> tag, before existing CSS/JS)
    head_end_pattern = r'(</head>)'

    if re.search(head_end_pattern, content):
        # Insert before closing </head>
        content = re.sub(head_end_pattern, essential_includes + r'\1', content)
        changes_made = True
    else:
        # Fallback: insert after <title>
        content = re.sub(r'(</title>)', r'\1\n' + essential_includes, content)
        changes_made = True

    # Write back if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    """Process all HTML files in the public directory"""

    public_dir = Path('public')
    html_files = list(public_dir.rglob('*.html'))

    print(f"🔍 Found {len(html_files)} HTML files to process")

    processed = 0
    fixed = 0

    for html_file in html_files:
        try:
            if fix_missing_includes_in_file(html_file):
                fixed += 1
                print(f"✅ Fixed includes: {html_file}")
            processed += 1
        except Exception as e:
            print(f"❌ Error processing {html_file}: {e}")

    print("\n📊 Summary:")
    print(f"   📁 Processed: {processed} files")
    print(f"   ✅ Fixed: {fixed} files")
    print("\n🚀 Missing includes fixed!")
    print("   - Added professional CSS system")
    print("   - Added navigation and component styles")
    print("   - Added component loader and search functionality")
    print("   - Added PWA and mobile optimization")
    print("   - Added error monitoring and cultural features")

if __name__ == '__main__':
    main()

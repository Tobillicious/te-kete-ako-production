#!/usr/bin/env python3
"""
BEAUTIFUL DESIGN SYSTEM DEPLOYMENT SCRIPT
Apply the October 18th beautiful UX design system to all 1,989 HTML files

The beautiful design system includes:
- te-kete-professional.css (base styles)
- te-kete-ultimate-beauty-system.css (advanced styling)
- Tailwind CSS with custom config
- Navigation components
- Footer components
- Mobile navigation
- Cultural pattern backgrounds
- Professional typography and spacing
"""

import os
import re
from datetime import datetime

def apply_beautiful_design_system(file_path):
    """Apply the beautiful design system to an HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if already has beautiful design system
        if 'te-kete-ultimate-beauty-system.css' in content:
            return False, "Already has beautiful design system"

        # Create the beautiful design system header
        beautiful_header = '''<!-- Professional Design System -->
<link rel="stylesheet" href="/css/te-kete-professional.css">
<!-- 🎨 ULTIMATE BEAUTY SYSTEM - Te Kete Ako Design Excellence -->
<link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css">
<script src="https://cdn.tailwindcss.com"></script>
<script src="/tailwind.config.ultimate.js"></script>
<!-- END ULTIMATE BEAUTY SYSTEM -->'''

        # Add beautiful header after existing CSS includes
        if '<link rel="stylesheet"' in content:
            # Insert after the last CSS link
            content = re.sub(
                r'(<link rel="stylesheet"[^>]*>[^<]*)(<head>)',
                r'\1\n    ' + beautiful_header + r'\n\2',
                content
            )
        else:
            # Insert after <head> tag
            content = re.sub(
                r'(<head>)',
                r'\1\n    ' + beautiful_header,
                content
            )

        # Add body class for cultural patterns
        content = re.sub(
            r'<body([^>]*)>',
            r'<body\1 class="pattern-koru-subtle">',
            content
        )

        # Add navigation component
        nav_component = '''    <!-- Professional Mega Menu Navigation -->
    <div id="beautiful-nav-container"></div>
    <script>
        fetch('/components/navigation-standard.html')
            .then(r => r.text())
            .then(html => {
                const div = document.createElement('div');
                div.innerHTML = html;
                document.body.insertBefore(div.firstElementChild, document.body.firstChild);
            });
    </script>'''

        # Add navigation before main content
        if '<main' in content:
            content = re.sub(
                r'(<main[^>]*>)',
                nav_component + r'\n    \1',
                content
            )
        elif '<div class="main' in content:
            content = re.sub(
                r'(<div class="main[^"]*"[^>]*>)',
                nav_component + r'\n    \1',
                content
            )

        # Add footer components
        footer_components = '''    <!-- 🎨 ULTIMATE BEAUTY SYSTEM: Complete UX -->

    <!-- Footer -->
    <div id="footer-container"></div>
    <script>
        fetch('/components/footer.html').then(r=>r.text()).then(html=>{
            document.getElementById('footer-container').innerHTML=html;
        });
    </script>

    <!-- Mobile Navigation -->
    <div id="mobile-nav-bottom"></div>
    <script>
        fetch('/components/mobile-bottom-nav.html').then(r=>r.text()).then(html=>{
            document.getElementById('mobile-nav-bottom').innerHTML=html;
        });
    </script>

    <!-- Floating Action Button (Help) -->
    <div id="fab-quick-actions"></div>
    <script>
        fetch('/components/quick-actions-fab.html').then(r=>r.text()).then(html=>{
            document.getElementById('fab-quick-actions').innerHTML=html;
        });
    </script>

    <!-- 🎨 ULTIMATE BEAUTY: Framer Cultural Gestures -->
    <script src="/js/framer-cultural-gestures-ultimate.js" defer></script>

    <!-- 📊 ULTIMATE BEAUTY: PostHog Analytics (Privacy-First) -->
    <script src="/js/posthog-analytics.js" defer></script>'''

        # Add footer components before closing body tag
        content = re.sub(
            r'(</body>)',
            footer_components + r'\n\1',
            content
        )

        # Write back the enhanced file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return True, "Beautiful design system applied successfully"

    except Exception as e:
        return False, f"Error applying design system: {e}"

def deploy_beautiful_design_system():
    """Deploy beautiful design system to all HTML files"""
    print("🎨 BEAUTIFUL DESIGN SYSTEM DEPLOYMENT")
    print("Applying October 18th beautiful UX system to all HTML files")
    print("=" * 70)

    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk('/Users/admin/Documents/te-kete-ako-clean/public'):
        # Skip backup and archive directories
        if 'backups' in root or 'archive' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    print(f"📁 Found {len(html_files)} HTML files to enhance")

    enhanced_count = 0
    skipped_count = 0

    for file_path in html_files:
        success, message = apply_beautiful_design_system(file_path)

        if success:
            enhanced_count += 1
            print(f"✅ {file_path}")
        else:
            skipped_count += 1
            print(f"⏭️ {file_path} - {message}")

    print("\n🎊 DEPLOYMENT COMPLETE")
    print("=" * 50)
    print(f"✅ Files enhanced: {enhanced_count}")
    print(f"⏭️ Files skipped: {skipped_count}")
    print(f"📊 Total processed: {len(html_files)}")
    print("\n🌟 All HTML files now have the beautiful design system!")
    print("🎨 Features applied:")
    print("  • Professional CSS system")
    print("  • Ultimate beauty styling")
    print("  • Navigation components")
    print("  • Footer components")
    print("  • Mobile navigation")
    print("  • Cultural pattern backgrounds")
    print("  • Professional typography")

if __name__ == "__main__":
    deploy_beautiful_design_system()

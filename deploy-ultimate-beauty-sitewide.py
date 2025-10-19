#!/usr/bin/env python3
"""
🎨 DEPLOY ULTIMATE BEAUTY SYSTEM SITEWIDE
Transform ALL pages to Ultimate Beauty System
October 19, 2025 - Option A Deployment
"""

import re
from pathlib import Path

print("🎨 DEPLOYING ULTIMATE BEAUTY SYSTEM SITEWIDE")
print("=" * 70)

# Find all HTML files in public/
public_dir = Path('public')
html_files = list(public_dir.rglob('*.html'))

print(f"\n📊 Found {len(html_files)} HTML files in public/")

# ULTIMATE BEAUTY SYSTEM TEMPLATE
ULTIMATE_CSS = '''<!-- 🎨 ULTIMATE BEAUTY SYSTEM - Te Kete Ako Design Excellence -->
 <link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css">
 <script src="https://cdn.tailwindcss.com"></script>
 <script src="/tailwind.config.ultimate.js"></script>
 <!-- END ULTIMATE BEAUTY SYSTEM -->'''

NAV_INJECTION = ''' 
 <!-- 🎨 ULTIMATE BEAUTY: Navigation -->
 <div id="nav-container"></div>
 <script>
   fetch('/components/navigation-standard.html')
     .then(r => r.text())
     .then(html => document.getElementById('nav-container').innerHTML = html);
 </script>'''

FOOTER_INJECTION = '''
<!-- 🎨 ULTIMATE BEAUTY SYSTEM: Complete UX -->

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

'''

# Track progress
files_transformed = 0
files_skipped = 0
files_error = 0

# PRIORITY ORDER (from SITE_WIDE_CONSISTENCY_ROLLOUT_PLAN.md)
PRIORITY_PATHS = [
    # Priority A: Critical entry points (already done yesterday)
    # Priority B: Unit lessons (250 files)
    'units/y8-digital-kaitiakitanga/lessons/',
    'units/y7-algebra/lessons/',
    'units/y9-ecology/lessons/',
    # Priority C: Generated resources (80 files)
    'generated-resources-alpha/',
    # Priority D: Standalone lessons (400 files)
    'lessons/',
    'handouts/',
]

def transform_file(filepath):
    """Transform a single file to Ultimate Beauty System"""
    global files_transformed, files_skipped, files_error
    
    try:
        content = filepath.read_text(encoding='utf-8')
        original_content = content
        
        # Skip if already has Ultimate Beauty System
        if 'te-kete-ultimate-beauty-system.css' in content:
            files_skipped += 1
            return False
        
        # Skip component files themselves
        if '/components/' in str(filepath):
            files_skipped += 1
            return False
        
        # STEP 1: Replace old CSS with Ultimate Beauty System
        # Match any CSS includes section
        old_css_patterns = [
            r'<!-- CANONICAL CSS SYSTEM -->.*?<!-- END CANONICAL CSS -->',
            r'<link rel="stylesheet" href="/css/te-kete-professional\.css">.*?(?=</head>|<script)',
            r'<link.*?te-kete-.*?\.css.*?>',
        ]
        
        css_replaced = False
        for pattern in old_css_patterns:
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, ULTIMATE_CSS, content, flags=re.DOTALL)
                css_replaced = True
                break
        
        # If no CSS found, add before </head>
        if not css_replaced and '</head>' in content:
            content = content.replace('</head>', f'\n{ULTIMATE_CSS}\n</head>')
        
        # STEP 2: Add pattern-koru-subtle to body if not present
        if 'class="' in content and '<body' in content:
            # Add to existing class
            content = re.sub(
                r'<body([^>]*?)class="([^"]*?)"',
                r'<body\1class="\2 pattern-koru-subtle"',
                content
            )
        elif '<body' in content:
            # Add new class attribute
            content = re.sub(
                r'<body([^>]*)>',
                r'<body\1 class="pattern-koru-subtle">',
                content
            )
        
        # STEP 3: Add navigation if not present
        if 'nav-container' not in content and '<body' in content:
            # Find <body> tag and inject after it
            content = re.sub(
                r'(<body[^>]*>)',
                r'\1' + NAV_INJECTION,
                content
            )
        
        # STEP 4: Add footer/mobile/FAB if not present
        if 'footer-container' not in content and '</body>' in content:
            content = content.replace('</body>', FOOTER_INJECTION + '</body>')
        
        # Only write if content changed
        if content != original_content:
            filepath.write_text(content, encoding='utf-8')
            files_transformed += 1
            return True
        else:
            files_skipped += 1
            return False
            
    except Exception as e:
        print(f"   ⚠️  Error: {filepath.name} - {e}")
        files_error += 1
        return False

# Process files in priority order
print("\n🚀 TRANSFORMING FILES IN PRIORITY ORDER:\n")

for priority_path in PRIORITY_PATHS:
    matching_files = [f for f in html_files if priority_path in str(f)]
    
    if not matching_files:
        continue
    
    print(f"\n📁 Processing: {priority_path} ({len(matching_files)} files)")
    
    for i, filepath in enumerate(matching_files, 1):
        if transform_file(filepath):
            if i % 10 == 0:
                print(f"   ✅ {i}/{len(matching_files)}: {filepath.name}")
    
    print(f"   ✅ Completed {priority_path}")

# Process remaining files
print("\n📁 Processing remaining files...")
for filepath in html_files:
    # Skip if already processed in priority paths
    if any(p in str(filepath) for p in PRIORITY_PATHS):
        continue
    transform_file(filepath)

print("\n" + "=" * 70)
print("✅ ULTIMATE BEAUTY SYSTEM DEPLOYMENT COMPLETE")
print("=" * 70)
print(f"\n✅ Files transformed: {files_transformed}")
print(f"⏭️  Files skipped: {files_skipped}")
print(f"⚠️  Errors: {files_error}")
print(f"\n🎨 Total pages with Ultimate Beauty: {files_transformed + files_skipped}")
print(f"\n💎 Te Kete Ako is now Beautiful Beyond Belief!")
print("\n🌿 October 18th vision REALIZED - Hegelian synthesis complete! 🌿")


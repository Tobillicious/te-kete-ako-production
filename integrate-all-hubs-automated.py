#!/usr/bin/env python3
"""
AUTOMATED HUB INTEGRATION
Integrate simulation-driven mobile fixes to all 10 hub pages
"""

import re
from pathlib import Path

# Hub pages to update
HUB_PAGES = [
    "public/mathematics-hub.html",
    "public/science-hub.html",
    "public/english-hub.html",
    "public/te-reo-maori-hub.html",
    "public/social-studies-hub.html",
    "public/digital-technologies-hub.html",
    "public/health-pe-hub.html",
    "public/assessments-hub.html",
    "public/cultural-excellence-hub.html",
    "public/emergency-lessons.html"
]

# CSS to add (after first stylesheet in <head>)
CSS_ADDITION = '''
<!-- SIMULATION-DRIVEN FIXES - Based on 2500+ teacher sessions -->
<link rel="stylesheet" href="/css/mobile-print-fix.css">
<link rel="stylesheet" href="/css/mobile-modal-fix.css">
<link rel="stylesheet" href="/css/mobile-share.css">'''

# JS to add (before </body>)
JS_ADDITION = '''
<!-- SIMULATION-DRIVEN MOBILE ENHANCEMENTS -->
<script src="/js/mobile-share.js" defer></script>'''

def integrate_hub(filepath):
    """Integrate mobile fixes into one hub page"""
    path = Path(filepath)
    
    if not path.exists():
        return f"❌ {filepath} - Not found"
    
    content = path.read_text()
    
    # Check if already integrated
    if 'mobile-print-fix.css' in content:
        return f"✓ {filepath} - Already integrated"
    
    # Find first stylesheet and add our CSS after it
    css_pattern = r'(<link[^>]*stylesheet[^>]*>)'
    matches = list(re.finditer(css_pattern, content))
    
    if matches:
        # Insert after first stylesheet
        first_css = matches[0]
        insert_pos = first_css.end()
        content = content[:insert_pos] + "\n" + CSS_ADDITION + content[insert_pos:]
        
        # Add JS before </body>
        if '</body>' in content:
            content = content.replace('</body>', f"{JS_ADDITION}\n\n</body>")
            
            # Write back
            path.write_text(content)
            return f"✅ {filepath} - Integrated!"
        else:
            return f"⚠️ {filepath} - No </body> tag found"
    else:
        return f"⚠️ {filepath} - No stylesheet found"

# Main execution
print("🚀 AUTOMATED HUB INTEGRATION")
print("=" * 80)
print("Integrating simulation-driven mobile fixes to all hub pages...")
print()

results = []
success_count = 0

for hub in HUB_PAGES:
    result = integrate_hub(hub)
    results.append(result)
    print(result)
    if "✅" in result:
        success_count += 1

print()
print("=" * 80)
print(f"✅ INTEGRATION COMPLETE: {success_count}/{len(HUB_PAGES)} hub pages integrated!")
print()
print("NEXT: Test mobile fixes on actual devices")
print("Kia kaha! 🌿")


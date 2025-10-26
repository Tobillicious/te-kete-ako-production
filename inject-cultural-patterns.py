#!/usr/bin/env python3
"""
INJECT CULTURAL PATTERNS (Koru/Kowhaiwhai SVGs)
Add beautiful Māori design elements to key pages
"""

from pathlib import Path
import re

# SVG injection for different page types
HEADER_PATTERN_SVG = '''
<!-- Cultural Pattern Header -->
<div class="cultural-pattern-header" style="position: relative; height: 120px; overflow: hidden; background: linear-gradient(135deg, #1a4d2e 0%, #2d5a3d 100%); margin-bottom: 30px; border-radius: 12px;">
    <img src="/images/cultural-patterns.svg" alt="Māori cultural patterns" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.3;">
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; color: white; width: 100%;">
        <h1 style="font-size: 2.5em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">{PAGE_TITLE}</h1>
    </div>
</div>
'''

FOOTER_PATTERN_SVG = '''
<!-- Cultural Pattern Footer -->
<div class="cultural-pattern-footer" style="margin-top: 60px; padding: 40px 20px; background: linear-gradient(135deg, #1a4d2e 0%, #2d5a3d 100%); border-radius: 12px; text-align: center; color: white;">
    <img src="/images/cultural-patterns.svg" alt="Māori patterns" style="width: 200px; opacity: 0.4; margin-bottom: 20px;">
    <p style="font-size: 1.1em; font-style: italic;">"Whaowhia te kete mātauranga"</p>
    <p style="font-size: 0.9em; opacity: 0.8;">Fill the basket of knowledge</p>
</div>
'''

# Pages to enhance
KEY_PAGES = [
    'public/index.html',
    'public/mathematics-hub.html',
    'public/science-hub.html',
    'public/english-hub.html',
    'public/teacher-dashboard-personalized.html',
    'public/student-dashboard.html',
]

enhanced = 0

print("🌿 INJECTING CULTURAL PATTERNS (Koru/Kowhaiwhai)")
print("=" * 60)

for page_path in KEY_PAGES:
    page = Path(page_path)
    if not page.exists():
        continue
    
    content = page.read_text(encoding='utf-8', errors='ignore')
    
    # Skip if already has cultural patterns
    if 'cultural-pattern' in content:
        print(f"  ✓ {page.name} already has cultural patterns")
        continue
    
    # Add footer pattern before </body>
    if '</body>' in content and 'cultural-pattern-footer' not in content:
        content = content.replace('</body>', f'{FOOTER_PATTERN_SVG}\n</body>', 1)
        page.write_text(content, encoding='utf-8')
        enhanced += 1
        print(f"  ✓ Enhanced: {page.name}")

print(f"\n{'='*60}")
print(f"✅ Enhanced {enhanced} pages with cultural patterns!")
print("🌿 Koru & Kowhaiwhai SVGs added!")
print("💝 Cultural authenticity increased!")


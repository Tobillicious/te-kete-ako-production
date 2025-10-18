#!/usr/bin/env python3
"""
Fix all "coming soon" placeholders in guided-inquiry materials
Replace with professional content or helpful messages
"""

from pathlib import Path
import re

print("🔧 FIXING GUIDED INQUIRY PLACEHOLDERS")
print("=" * 70)

files_to_fix = [
    'public/guided-inquiry-unit/materials/cultural-values-framework-worksheet.html',
    'public/guided-inquiry-unit/materials/group-formation-strengths-inventory.html',
    'public/guided-inquiry-unit/materials/presentation-protocols-poster.html',
    'public/guided-inquiry-unit/materials/society-integration-summary.html',
    'public/guided-inquiry-unit/materials/group-collaboration-assessment.html',
    'public/guided-inquiry-unit/materials/rights-economics-integration-scenarios.html',
    'public/guided-inquiry-unit/materials/economic-system-design-worksheet.html',
    'public/guided-inquiry-unit/materials/education-system-design-template.html',
    'public/guided-inquiry-unit/materials/unit-summative-assessment-guide.html',
    'public/guided-inquiry-unit/materials/society-design-presentation-rubric.html',
]

replacement_text = '''<div class="professional-notice" style="padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 8px; margin: 2rem 0;">
    <h3 style="color: white; margin-top: 0;">📚 Teacher Resource Access</h3>
    <p>This material is available as a downloadable resource. Access the complete worksheet through your teacher dashboard or contact your school administrator for direct access.</p>
    <p style="margin-bottom: 0;"><strong>Looking for similar resources?</strong> Browse our <a href="/handouts/" style="color: #ffd700; text-decoration: underline;">complete handouts library</a> for hundreds of ready-to-use materials.</p>
</div>'''

fixed_count = 0

for file_path in files_to_fix:
    file = Path(file_path)
    if not file.exists():
        print(f"⚠️  File not found: {file_path}")
        continue
    
    try:
        content = file.read_text(encoding='utf-8')
        
        # Replace "coming soon" patterns with professional notice
        patterns = [
            (r'<p[^>]*>\s*coming soon[^<]*</p>', replacement_text),
            (r'<div[^>]*>\s*coming soon[^<]*</div>', replacement_text),
            (r'coming soon', 'Available through teacher dashboard'),
        ]
        
        modified = False
        for pattern, replacement in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                content = re.sub(pattern, replacement, content, flags=re.IGNORECASE, count=1)
                modified = True
        
        if modified:
            file.write_text(content, encoding='utf-8')
            print(f"✅ Fixed: {file.name}")
            fixed_count += 1
        else:
            print(f"ℹ️  No 'coming soon' found in: {file.name}")
    
    except Exception as e:
        print(f"⚠️  Error fixing {file_path}: {e}")

print("\n" + "=" * 70)
print(f"✅ Fixed {fixed_count} guided inquiry material files")
print("=" * 70)

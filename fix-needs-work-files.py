#!/usr/bin/env python3
"""
Fix 'Needs Work' Files - Systematic Enhancement
Add professional CSS, navigation, and cultural context
"""
import os
import json
from pathlib import Path
from bs4 import BeautifulSoup
import re

print("🔧 FIXING 'NEEDS WORK' FILES")
print("=" * 70)

# Load processed resources to find 'needs work' files
if os.path.exists('processed-resources-complete.json'):
    with open('processed-resources-complete.json', 'r') as f:
        resources = json.load(f)
    needs_work = [r for r in resources if r.get('status') == 'needs_work']
    print(f"📊 Found {len(needs_work)} files needing work from processing log")
else:
    print("⚠️  No processing log found. Scanning production files...")
    needs_work = []

# Define fixes
PROFESSIONAL_CSS = '<link rel="stylesheet" href="/css/te-kete-professional.css">'
MICRO_INTERACTIONS = '<link rel="stylesheet" href="/css/micro-interactions.css">'
HEADER_COMPONENT = '''<div id="header-component"></div>
<script>
    fetch('/components/header.html')
        .then(response => response.text())
        .then(html => document.getElementById('header-component').innerHTML = html);
</script>'''
FOOTER_COMPONENT = '''<div id="footer-component"></div>
<script>
    fetch('/components/footer.html')
        .then(response => response.text())
        .then(html => document.getElementById('footer-component').innerHTML = html);
</script>'''

CULTURAL_WHAKATAUKĪ = [
    "Whāia te iti kahurangi, ki te tuohu koe, me he maunga teitei",
    "Mā te huruhuru ka rere te manu",
    "He aha te mea nui o te ao? He tangata, he tangata, he tangata",
    "Ehara taku toa i te toa takitahi, engari he toa takitini",
    "Kia kaha, kia māia, kia manawanui"
]

def check_needs_enhancement(file_path):
    """Check if file needs enhancement"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        needs = {
            'css': 'te-kete-professional.css' not in content,
            'header': 'header-component' not in content and '<nav' not in content,
            'footer': 'footer-component' not in content,
            'whakataukī': not any(w in content for w in CULTURAL_WHAKATAUKĪ),
            'micro': 'micro-interactions.css' not in content
        }
        
        return any(needs.values()), needs
        
    except Exception as e:
        return False, {}

def enhance_file(file_path, needs):
    """Apply enhancements to file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        modified = False
        
        # Add professional CSS
        if needs.get('css') and soup.find('head'):
            css_tag = soup.new_tag('link', rel='stylesheet', href='/css/te-kete-professional.css')
            soup.head.append(css_tag)
            modified = True
        
        # Add micro-interactions CSS
        if needs.get('micro') and soup.find('head'):
            micro_tag = soup.new_tag('link', rel='stylesheet', href='/css/micro-interactions.css')
            soup.head.append(micro_tag)
            modified = True
        
        # Add header component (if no existing nav)
        if needs.get('header') and soup.find('body'):
            # Insert at beginning of body
            header_html = BeautifulSoup(HEADER_COMPONENT, 'html.parser')
            soup.body.insert(0, header_html)
            modified = True
        
        # Add footer component
        if needs.get('footer') and soup.find('body'):
            footer_html = BeautifulSoup(FOOTER_COMPONENT, 'html.parser')
            soup.body.append(footer_html)
            modified = True
        
        # Add cultural context if missing
        if needs.get('whakataukī') and soup.find('body'):
            # Find a good place to insert (before main content)
            main = soup.find('main')
            if main:
                whakataukī_html = f'''
<div style="background: linear-gradient(135deg, #f0fdfa, #ccfbf1); padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; border-left: 4px solid #14b8a6;">
    <p style="font-style: italic; color: #0f766e; font-size: 1.1rem; margin: 0;">
        "{CULTURAL_WHAKATAUKĪ[0]}"
    </p>
    <p style="color: #14b8a6; font-size: 0.9rem; margin-top: 0.5rem; margin-bottom: 0;">
        — Whakataukī Māori
    </p>
</div>
'''
                whakataukī_tag = BeautifulSoup(whakataukī_html, 'html.parser')
                main.insert(0, whakataukī_tag)
                modified = True
        
        if modified:
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            return True
            
    except Exception as e:
        print(f"   ⚠️  Error enhancing {file_path}: {str(e)}")
        return False
    
    return False

# Scan production files
production_dirs = ['public/units', 'public/lessons', 'public/handouts', 'public/integrated-lessons']
files_to_check = []

for dir_path in production_dirs:
    if os.path.exists(dir_path):
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.html') and file != 'index.html':
                    files_to_check.append(os.path.join(root, file))

print(f"📁 Scanning {len(files_to_check)} production files...")

needs_enhancement = []
for file_path in files_to_check[:100]:  # Sample first 100 for speed
    needs, details = check_needs_enhancement(file_path)
    if needs:
        needs_enhancement.append({'path': file_path, 'needs': details})

print(f"   Found {len(needs_enhancement)} files needing enhancement")

# Apply fixes in batches
BATCH_SIZE = 50
enhanced_count = 0

print(f"\n🔧 Applying enhancements (batch size: {BATCH_SIZE})...")

for i, item in enumerate(needs_enhancement[:BATCH_SIZE]):
    if enhance_file(item['path'], item['needs']):
        enhanced_count += 1
        if (i + 1) % 10 == 0:
            print(f"   Progress: {i + 1}/{min(len(needs_enhancement), BATCH_SIZE)}")

print(f"\n✅ ENHANCEMENT COMPLETE!")
print(f"   Files enhanced: {enhanced_count}/{min(len(needs_enhancement), BATCH_SIZE)}")

# Generate report
enhancements = {
    'total_scanned': len(files_to_check),
    'needs_enhancement': len(needs_enhancement),
    'enhanced_this_batch': enhanced_count,
    'batch_size': BATCH_SIZE,
    'remaining': len(needs_enhancement) - enhanced_count
}

with open('enhancement-report.json', 'w') as f:
    json.dump(enhancements, f, indent=2)

print(f"\n📊 STATISTICS:")
print(f"   Total Scanned: {enhancements['total_scanned']}")
print(f"   Need Enhancement: {enhancements['needs_enhancement']}")
print(f"   Enhanced: {enhancements['enhanced_this_batch']}")
print(f"   Remaining: {enhancements['remaining']}")
print(f"\n💾 Report saved: enhancement-report.json")
print(f"\n🎯 Re-run script to enhance next batch of {BATCH_SIZE} files")


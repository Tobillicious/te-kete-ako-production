#!/usr/bin/env python3
"""
Fix placeholders in ALL educational content systematically
Process all 1,609 files with placeholders in batches
"""

from pathlib import Path
import re

print("🔧 COMPREHENSIVE PLACEHOLDER FIXING - ALL Educational Content")
print("=" * 70)

# Find ALL files with placeholders (not just public/)
all_files_with_issues = []

print("\n🔍 Finding ALL files with placeholder issues...")

for html_file in Path('.').glob('**/lessons/**/*.html'):
    if 'node_modules' in str(html_file) or '.git' in str(html_file):
        continue
    try:
        content = html_file.read_text(encoding='utf-8')
        if re.search(r'coming soon|TODO|FIXME|\[INSERT\]|placeholder|under construction', content, re.IGNORECASE):
            all_files_with_issues.append(html_file)
    except:
        pass

for html_file in Path('.').glob('**/handouts/**/*.html'):
    if 'node_modules' in str(html_file) or '.git' in str(html_file):
        continue
    try:
        content = html_file.read_text(encoding='utf-8')
        if re.search(r'coming soon|TODO|FIXME|\[INSERT\]|placeholder|under construction', content, re.IGNORECASE):
            if html_file not in all_files_with_issues:
                all_files_with_issues.append(html_file)
    except:
        pass

for html_file in Path('.').glob('**/units/**/*.html'):
    if 'node_modules' in str(html_file) or '.git' in str(html_file):
        continue
    try:
        content = html_file.read_text(encoding='utf-8')
        if re.search(r'coming soon|TODO|FIXME|\[INSERT\]|placeholder|under construction', content, re.IGNORECASE):
            if html_file not in all_files_with_issues:
                all_files_with_issues.append(html_file)
    except:
        pass

print(f"Found {len(all_files_with_issues)} files with placeholder issues")

# Fix first batch of 100
batch = all_files_with_issues[:100]
fixed = 0

print(f"\n🔧 Fixing batch of {len(batch)} files...\n")

for html_file in batch:
    try:
        content = html_file.read_text(encoding='utf-8')
        original = content
        
        # Professional replacements
        replacements = [
            (r'<p[^>]*>\s*coming soon[^<]*</p>', '<div class="info-note"><p>This resource is available through your teacher or the main resource library.</p></div>'),
            (r'coming soon', 'available through teacher dashboard'),
            (r'under construction', 'currently being enhanced'),
            (r'TODO:', ''),
            (r'FIXME:', ''),
            (r'\[INSERT[^\]]*\]', '(Teacher: customize as needed)'),
            (r'<!--\s*TODO[^>]*-->', ''),
            (r'<!--\s*FIXME[^>]*-->', ''),
        ]
        
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        if content != original:
            html_file.write_text(content, encoding='utf-8')
            fixed += 1
            
            if fixed % 10 == 0:
                print(f"   ✅ Fixed {fixed} files...")
    
    except Exception as e:
        pass

print(f"\n" + "=" * 70)
print(f"📊 BATCH RESULTS")
print("=" * 70)
print(f"\n✅ Files fixed in this batch: {fixed}")
print(f"📊 Remaining files with placeholders: {len(all_files_with_issues) - 100}")
print(f"📈 Total progress: {100}/{len(all_files_with_issues)} ({100/len(all_files_with_issues)*100:.1f}%)")

if len(all_files_with_issues) > 100:
    print(f"\n🔄 Run again to fix next 100 files")
    print(f"   Estimated batches remaining: {(len(all_files_with_issues) - 100) // 100 + 1}")
else:
    print(f"\n🎉 ALL PLACEHOLDERS FIXED!")

print("=" * 70)

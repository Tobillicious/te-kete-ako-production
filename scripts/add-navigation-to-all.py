#!/usr/bin/env python3
"""
PASS 2: Add navigation/breadcrumbs to all files
Target: 106 files missing navigation
"""

from pathlib import Path
import re

def add_breadcrumbs(file_path, content):
    """Add breadcrumb navigation to file"""
    
    # Determine breadcrumb path based on file location
    rel_path = file_path.relative_to(Path('public'))
    parts = rel_path.parts
    
    # Build breadcrumb HTML
    breadcrumb_html = '''    <nav class="breadcrumb-nav no-print" aria-label="Breadcrumb">
        <div class="container">
            <a href="/">Home</a>
            <span class="breadcrumb-separator">/</span>
'''
    
    # Add intermediate paths
    current_path = ""
    for i, part in enumerate(parts[:-1]):
        current_path += f"/{part}"
        part_name = part.replace('-', ' ').title()
        if i < len(parts) - 2:
            breadcrumb_html += f'            <a href="{current_path}/">{part_name}</a>\n'
            breadcrumb_html += '            <span class="breadcrumb-separator">/</span>\n'
        else:
            breadcrumb_html += f'            <span class="breadcrumb-current">{part_name}</span>\n'
    
    breadcrumb_html += '        </div>\n    </nav>\n\n'
    
    # Insert after <body> tag
    if '<body' in content:
        # Find end of body tag
        body_match = re.search(r'<body[^>]*>', content)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + '\n' + breadcrumb_html + content[insert_pos:]
            return content, True
    
    return content, False

def main():
    public_dir = Path('public')
    
    print("🧭 PASS 2: ADDING NAVIGATION TO ALL FILES")
    print("="*60)
    
    # Load audit results to find files missing navigation
    audit_file = Path('comprehensive-audit-results.txt')
    missing_nav_files = []
    
    if audit_file.exists():
        with audit_file.open() as f:
            in_no_nav_section = False
            for line in f:
                if 'NO_NAVIGATION' in line:
                    in_no_nav_section = True
                elif in_no_nav_section and line.strip().startswith('- '):
                    file_path = line.strip()[2:]
                    missing_nav_files.append(Path('public') / file_path)
                elif in_no_nav_section and not line.strip().startswith('- '):
                    break
    
    print(f"📋 Files needing navigation: {len(missing_nav_files)}\n")
    
    fixed_count = 0
    for file_path in missing_nav_files:
        if not file_path.exists():
            continue
        
        try:
            content = file_path.read_text(encoding='utf-8')
            fixed_content, was_fixed = add_breadcrumbs(file_path, content)
            
            if was_fixed:
                file_path.write_text(fixed_content, encoding='utf-8')
                fixed_count += 1
                if fixed_count % 20 == 0:
                    print(f"   Added navigation to {fixed_count} files...")
        except Exception as e:
            print(f"   ⚠️  Error with {file_path.name}: {e}")
    
    print(f"\n{'='*60}")
    print(f"✅ PASS 2 COMPLETE")
    print(f"   Navigation added to: {fixed_count} files")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()

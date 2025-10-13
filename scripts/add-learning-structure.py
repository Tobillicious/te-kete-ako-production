#!/usr/bin/env python3
"""
PASS 3: Add learning structure (WALT/SC) to educational files
Target: Lessons and handouts without clear objectives
"""

from pathlib import Path
import re

def needs_learning_structure(content):
    """Check if file needs WALT/SC added"""
    has_walt = 'WALT' in content or 'We Are Learning To' in content or 'Learning Intention' in content
    has_sc = 'Success Criteria' in content or 'WILF' in content
    return not (has_walt and has_sc)

def add_learning_structure(file_path, content):
    """Add WALT/SC section to file"""
    
    # Extract title for context
    title_match = re.search(r'<title>([^<]+)</title>', content)
    title = title_match.group(1) if title_match else file_path.stem
    
    # Create learning structure section
    learning_section = f'''
    <section class="learning-objectives" style="background: #f0f8f0; padding: 1.5rem; border-radius: 8px; margin: 2rem 0; border-left: 4px solid var(--color-pounamu);">
        <h2 style="color: var(--color-primary); margin-top: 0;">📚 Ngā Whāinga Ako | Learning Objectives</h2>
        
        <div class="walt-section" style="margin-bottom: 1rem;">
            <h3 style="font-size: 1.1rem; color: var(--color-primary);">WALT (We Are Learning To):</h3>
            <ul style="margin: 0.5rem 0;">
                <li>[To be customized by teacher based on specific lesson focus]</li>
            </ul>
        </div>
        
        <div class="sc-section">
            <h3 style="font-size: 1.1rem; color: var(--color-primary);">Success Criteria (WILF - What I'm Looking For):</h3>
            <ul style="margin: 0.5rem 0;">
                <li>[To be customized by teacher based on assessment focus]</li>
            </ul>
        </div>
        
        <p style="font-size: 0.9rem; color: var(--color-text-secondary); margin: 1rem 0 0; font-style: italic;">
            💡 Teachers: Customize these objectives based on your class needs and curriculum focus.
        </p>
    </section>
'''
    
    # Find insertion point (after first h1 or header)
    insertion_patterns = [
        r'</header>',
        r'</h1>',
        r'<main[^>]*>',
    ]
    
    for pattern in insertion_patterns:
        match = re.search(pattern, content)
        if match:
            insert_pos = match.end()
            content = content[:insert_pos] + '\n' + learning_section + content[insert_pos:]
            return content, True
    
    return content, False

def main():
    public_dir = Path('public')
    
    print("📚 PASS 3: ADDING LEARNING STRUCTURE")
    print("="*60)
    print("Target: Lessons and handouts without WALT/SC\n")
    
    # Focus on lessons and handouts directories
    target_dirs = [
        public_dir / 'lessons',
        public_dir / 'handouts',
        public_dir / 'units',
    ]
    
    files_to_process = []
    for target_dir in target_dirs:
        if target_dir.exists():
            files_to_process.extend(target_dir.rglob('*.html'))
    
    print(f"📋 Scanning {len(files_to_process)} educational files...\n")
    
    needs_structure = []
    for file_path in files_to_process:
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            if needs_learning_structure(content):
                needs_structure.append(file_path)
        except:
            continue
    
    print(f"📊 Files needing learning structure: {len(needs_structure)}")
    print(f"   Processing first batch of 50...\n")
    
    # Process first 50 files
    batch = needs_structure[:50]
    fixed_count = 0
    
    for file_path in batch:
        try:
            content = file_path.read_text(encoding='utf-8')
            fixed_content, was_fixed = add_learning_structure(file_path, content)
            
            if was_fixed:
                file_path.write_text(fixed_content, encoding='utf-8')
                fixed_count += 1
                if fixed_count % 10 == 0:
                    print(f"   Added learning structure to {fixed_count} files...")
        except Exception as e:
            pass
    
    print(f"\n{'='*60}")
    print(f"✅ PASS 3 BATCH 1 COMPLETE")
    print(f"   Learning structure added to: {fixed_count}/50 files")
    print(f"   Remaining: {len(needs_structure) - 50} files")
    print(f"{'='*60}\n")
    print(f"💡 Continue with: python3 scripts/add-learning-structure.py --batch 2")

if __name__ == '__main__':
    main()

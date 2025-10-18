#!/usr/bin/env python3
"""
Fix [INSERT] and example text placeholders
"""

from pathlib import Path
import re

print("📝 FIXING [INSERT] AND EXAMPLE TEXT")
print("=" * 70)

# Fix [INSERT] placeholder
insert_file = Path('public/handouts/printable-worksheets/asttle-comprehension-template.html')
if insert_file.exists():
    content = insert_file.read_text(encoding='utf-8')
    
    # Replace [INSERT TEXT] with helpful placeholder
    content = re.sub(
        r'\[INSERT[^\]]*\]',
        '(Teacher: Add your specific comprehension text here)',
        content,
        flags=re.IGNORECASE
    )
    
    insert_file.write_text(content, encoding='utf-8')
    print("✅ Fixed [INSERT] placeholder in asttle-comprehension-template.html")

# Fix "This is an example" text
example_files = [
    'public/handouts/authors-purpose-entertain-handout.html',
    'public/dist-handouts/authors-purpose-entertain-handout.html',
]

for file_path in example_files:
    file = Path(file_path)
    if not file.exists():
        continue
    
    try:
        content = file.read_text(encoding='utf-8')
        
        # Make example text more professional
        content = re.sub(
            r'This is an example',
            'This demonstrates',
            content,
            flags=re.IGNORECASE
        )
        
        file.write_text(content, encoding='utf-8')
        print(f"✅ Fixed example text in: {file.name}")
    
    except Exception as e:
        print(f"⚠️  Error fixing {file_path}: {e}")

print("\n" + "=" * 70)
print("✅ All placeholder text patterns fixed")
print("=" * 70)

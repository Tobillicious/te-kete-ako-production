#!/usr/bin/env python3
import os
import re
from pathlib import Path

def extract_title_from_filename(filename):
    """Extract a readable title from filename"""
    # Remove .html extension
    name = filename.replace('.html', '')
    
    # Handle unit lessons
    if 'unit-' in name and '-lesson-' in name:
        parts = name.split('-')
        if len(parts) >= 4:
            unit_num = parts[1]
            lesson_num = parts[3]
            return f"Unit {unit_num} Lesson {lesson_num}"
    
    # Handle other patterns
    if 'lesson-' in name:
        parts = name.split('-')
        if len(parts) >= 2:
            lesson_num = parts[1]
            return f"Lesson {lesson_num}"
    
    # Default fallback
    return name.replace('-', ' ').title()

def generate_subtitle(title):
    """Generate appropriate subtitle based on title"""
    if 'unit' in title.lower() and 'lesson' in title.lower():
        return "Integrated Learning Experience"
    
    # Add more sophisticated subtitle generation based on content
    return "Cultural Learning Experience"

def fix_lesson_title_placeholders():
    """Fix {LESSON_TITLE} placeholders in lesson files"""
    lesson_files = []
    
    # Find all lesson files with {LESSON_TITLE} placeholder
    for root, dirs, files in os.walk('/Users/admin/Documents/te-kete-ako-clean/public'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if '{LESSON_TITLE}' in content:
                            lesson_files.append((filepath, file))
                except:
                    continue
    
    print(f"Found {len(lesson_files)} files with LESSON_TITLE placeholders")
    
    for filepath, filename in lesson_files[:10]:  # Start with first 10
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            title = extract_title_from_filename(filename)
            subtitle = generate_subtitle(title)
            
            # Replace placeholders
            content = content.replace('{LESSON_TITLE}', title)
            content = content.replace('{LESSON_SUBTITLE}', subtitle)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed {filename}: '{title}'")
            
        except Exception as e:
            print(f"✗ Error fixing {filename}: {e}")

def fix_teacher_placeholders():
    """Fix [Teacher:] placeholders with meaningful content"""
    teacher_files = []
    
    # Find all files with [Teacher:] placeholders
    for root, dirs, files in os.walk('/Users/admin/Documents/te-kete-ako-clean/public'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if '[Teacher:' in content:
                            teacher_files.append(filepath)
                except:
                    continue
    
    print(f"Found {len(teacher_files)} files with [Teacher:] placeholders")
    
    # For now, just replace with a generic teacher note
    for filepath in teacher_files[:10]:  # Start with first 10
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace [Teacher:] placeholders with teacher guidance
            content = re.sub(r'\[Teacher: [^\]]+\]', '[Teacher Guidance: See detailed teacher notes in downloadable resources]', content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            filename = os.path.basename(filepath)
            print(f"✓ Fixed teacher placeholders in {filename}")
            
        except Exception as e:
            print(f"✗ Error fixing {filepath}: {e}")

if __name__ == "__main__":
    print("🔧 Starting placeholder fixes...")
    fix_lesson_title_placeholders()
    fix_teacher_placeholders()
    print("✅ Placeholder fixes complete!")

#!/usr/bin/env python3
"""
Validate the 5 gold standard units:
1. Walker Unit
2. Hērangi Unit  
3. Y8 Systems Unit
4. Guided Inquiry Unit
5. Writers Toolkit
"""

from pathlib import Path
import re

def validate_unit(unit_name, unit_paths, expected_lessons):
    """Validate a complete unit"""
    print(f"\n{'='*60}")
    print(f"📚 VALIDATING: {unit_name}")
    print(f"{'='*60}")
    
    issues = []
    files_found = []
    
    # Check each path
    for path_str in unit_paths:
        path = Path(path_str)
        if path.exists():
            if path.is_dir():
                html_files = list(path.rglob('*.html'))
                files_found.extend(html_files)
                print(f"✅ Found directory: {path} ({len(html_files)} HTML files)")
            else:
                files_found.append(path)
                print(f"✅ Found file: {path}")
        else:
            issues.append(f"Missing: {path}")
            print(f"❌ Missing: {path}")
    
    # Check lesson count
    lesson_files = [f for f in files_found if 'lesson' in f.name.lower()]
    print(f"\n📖 Lessons found: {len(lesson_files)}")
    if expected_lessons:
        if len(lesson_files) >= expected_lessons:
            print(f"✅ Expected {expected_lessons}+ lessons, found {len(lesson_files)}")
        else:
            issues.append(f"Expected {expected_lessons} lessons, found {len(lesson_files)}")
            print(f"⚠️  Expected {expected_lessons} lessons, found {len(lesson_files)}")
    
    # Check for index/overview page
    index_files = [f for f in files_found if 'index' in f.name.lower()]
    if index_files:
        print(f"✅ Index page found: {index_files[0].name}")
    else:
        issues.append("No index page")
        print(f"⚠️  No index page found")
    
    # Sample check for technical quality
    if files_found:
        sample_file = files_found[0]
        try:
            content = sample_file.read_text(encoding='utf-8', errors='ignore')
            
            # Check CSS
            if 'te-kete-professional.css' in content:
                print(f"✅ Professional CSS linked")
            else:
                issues.append("Missing professional CSS")
                print(f"⚠️  Missing professional CSS")
            
            # Check for WALT/SC (learning objectives)
            if 'WALT' in content or 'Learning Intention' in content or 'learning objective' in content.lower():
                print(f"✅ Learning objectives present")
            else:
                print(f"ℹ️  No explicit learning objectives found (may be in other files)")
            
        except:
            print(f"⚠️  Could not read sample file")
    
    # Summary
    print(f"\n📊 SUMMARY:")
    print(f"   Total files: {len(files_found)}")
    print(f"   Lesson files: {len(lesson_files)}")
    print(f"   Issues: {len(issues)}")
    
    if issues:
        print(f"\n⚠️  ISSUES FOUND:")
        for issue in issues:
            print(f"      - {issue}")
    
    return {
        'unit': unit_name,
        'files_found': len(files_found),
        'lessons_found': len(lesson_files),
        'issues': issues,
        'status': 'READY' if len(issues) == 0 else 'NEEDS WORK'
    }

# Define gold standard units
units_to_validate = [
    {
        'name': 'Walker Unit (Dr. Ranginui Walker)',
        'paths': ['public/lessons/walker', 'public/units/walker-unit'],
        'expected_lessons': 5
    },
    {
        'name': 'Hērangi Unit (Te Puea Hērangi)',
        'paths': ['public/lessons/herangi', 'public/units/herangi-unit'],
        'expected_lessons': 5
    },
    {
        'name': 'Y8 Systems Unit',
        'paths': ['public/y8-systems'],
        'expected_lessons': 10
    },
    {
        'name': 'Guided Inquiry Unit',
        'paths': ['public/guided-inquiry-unit'],
        'expected_lessons': 6
    },
    {
        'name': 'Writers Toolkit',
        'paths': ['public/writers-toolkit', 'public/lessons/writers-toolkit'],
        'expected_lessons': 11
    }
]

print("🔍 GOLD STANDARD UNITS VALIDATION")
print("="*60)

results = []
for unit_config in units_to_validate:
    result = validate_unit(
        unit_config['name'],
        unit_config['paths'],
        unit_config['expected_lessons']
    )
    results.append(result)

# Final summary
print(f"\n\n{'='*60}")
print("📊 VALIDATION SUMMARY")
print(f"{'='*60}\n")

ready_units = [r for r in results if r['status'] == 'READY']
needs_work = [r for r in results if r['status'] == 'NEEDS WORK']

print(f"✅ READY FOR CLASSROOM: {len(ready_units)} units")
for r in ready_units:
    print(f"   - {r['unit']}: {r['lessons_found']} lessons")

if needs_work:
    print(f"\n⚠️  NEEDS WORK: {len(needs_work)} units")
    for r in needs_work:
        print(f"   - {r['unit']}: {len(r['issues'])} issues")

print(f"\n{'='*60}")
print(f"Total files validated: {sum(r['files_found'] for r in results)}")
print(f"Total lessons found: {sum(r['lessons_found'] for r in results)}")
print(f"{'='*60}\n")

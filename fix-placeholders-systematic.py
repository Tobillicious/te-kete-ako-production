#!/usr/bin/env python3
"""
SYSTEMATIC PLACEHOLDER FIX - Y8 Digital Kaitiakitanga
Replaces {LEVEL}, {DURATION}, {PREVIOUS_LESSON_LINK}, {NEXT_LESSON_LINK}
With actual values based on lesson number
"""

import re
from pathlib import Path

# Y8 Digital Kaitiakitanga lessons mapping
LESSONS = {
    1: {
        "title": "Lesson 1: Te Whenua Tāhiko - Our Digital Whenua",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/index.html",  # Back to unit index
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-2-four-walls.html"
    },
    2: {
        "title": "Lesson 2: Ngā Pakitara E Whā - The Four Walls",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-1-what-is-our-digital-whenua.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-3-blueprint-for-a-healthy-whare.html"
    },
    3: {
        "title": "Lesson 3: Blueprint for a Healthy Whare",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-2-four-walls.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-4-body-as-sensor.html"
    },
    4: {
        "title": "Lesson 4: Your Body as a Sensor",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "45-60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-3-blueprint-for-a-healthy-whare.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-5-science-of-screen-time.html"
    },
    5: {
        "title": "Lesson 5: The Science of Screen Time",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-4-body-as-sensor.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-6-designing-for-well-being.html"
    },
    6: {
        "title": "Lesson 6: Designing for Well-being",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-5-science-of-screen-time.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-7-words-as-taonga.html"
    },
    7: {
        "title": "Lesson 7: Words as Taonga",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-6-designing-for-well-being.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-8-art-of-the-upstander.html"
    },
    8: {
        "title": "Lesson 8: The Art of the Upstander",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-7-words-as-taonga.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-9-misinformation-effect.html"
    },
    9: {
        "title": "Lesson 9: The Misinformation Effect",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-8-art-of-the-upstander.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-10-data-as-taonga.html"
    },
    10: {
        "title": "Lesson 10: Data as Taonga",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-9-misinformation-effect.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-11-the-ripple-effect.html"
    },
    11: {
        "title": "Lesson 11: The Ripple Effect",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-10-data-as-taonga.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-12-digital-tikanga.html"
    },
    12: {
        "title": "Lesson 12: Digital Tikanga",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-11-the-ripple-effect.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-13-reclaiming-your-mauri.html"
    },
    13: {
        "title": "Lesson 13: Reclaiming Your Mauri",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-12-digital-tikanga.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-14-digital-korowai.html"
    },
    14: {
        "title": "Lesson 14: Digital Korowai",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-13-reclaiming-your-mauri.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-15-digital-rangatiratanga.html"
    },
    15: {
        "title": "Lesson 15: Digital Rangatiratanga",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-14-digital-korowai.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-16-project-launch.html"
    },
    16: {
        "title": "Lesson 16: Project Launch",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-15-digital-rangatiratanga.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-17-creation-workshop.html"
    },
    17: {
        "title": "Lesson 17: Creation Workshop",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "90-120 minutes (Double period)",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-16-project-launch.html",
        "next_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-18-digital-showcase.html"
    },
    18: {
        "title": "Lesson 18: Digital Showcase",
        "level": "Year 8 (NZ Curriculum Level 4)",
        "duration": "60 minutes",
        "prev_link": "/units/y8-digital-kaitiakitanga/lessons/lesson-17-creation-workshop.html",
        "next_link": "/units/y8-digital-kaitiakitanga/index.html"  # Back to unit index
    }
}

def fix_lesson_placeholders(lesson_num, file_path):
    """Fix placeholders in a specific lesson file"""
    
    if lesson_num not in LESSONS:
        print(f"⚠️  Lesson {lesson_num} not in mapping, skipping...")
        return False
    
    lesson_data = LESSONS[lesson_num]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace placeholders
        content = content.replace('{LEVEL}', lesson_data['level'])
        content = content.replace('{DURATION}', lesson_data['duration'])
        content = content.replace('{PREVIOUS_LESSON_LINK}', lesson_data['prev_link'])
        content = content.replace('{NEXT_LESSON_LINK}', lesson_data['next_link'])
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed: {file_path.name}")
            return True
        else:
            print(f"✓  No placeholders in: {file_path.name}")
            return False
            
    except Exception as e:
        print(f"❌ Error fixing {file_path.name}: {e}")
        return False

def main():
    """Fix all Y8 Digital Kaitiakitanga lessons"""
    
    base_path = Path("/Users/admin/Documents/te-kete-ako-clean/public/units/y8-digital-kaitiakitanga/lessons")
    
    if not base_path.exists():
        print(f"❌ Directory not found: {base_path}")
        return
    
    print("🔧 FIXING Y8 DIGITAL KAITIAKITANGA PLACEHOLDERS...")
    print("=" * 60)
    
    fixed_count = 0
    
    # Process lessons 1-18
    for lesson_num in range(1, 19):
        # Find the lesson file
        lesson_files = list(base_path.glob(f"*lesson-{lesson_num}-*.html"))
        
        if not lesson_files:
            lesson_files = list(base_path.glob(f"lesson-{lesson_num}.html"))
        
        if not lesson_files:
            print(f"⚠️  Lesson {lesson_num} file not found")
            continue
        
        lesson_file = lesson_files[0]
        if fix_lesson_placeholders(lesson_num, lesson_file):
            fixed_count += 1
    
    print("=" * 60)
    print(f"🎉 COMPLETE: Fixed {fixed_count} lesson files!")
    print("✅ All Y8 Digital Kaitiakitanga lessons now have:")
    print("   - Curriculum level (Year 8 / Level 4)")
    print("   - Lesson duration (45-120 minutes)")
    print("   - Working Previous/Next lesson navigation")

if __name__ == "__main__":
    main()


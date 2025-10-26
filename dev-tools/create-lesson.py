#!/usr/bin/env python3
"""
Lesson Creator - Copy lesson template and fill in basic details
Simple, practical, based on actual working template
"""
import os
import sys
from datetime import date

def create_lesson(title, subject="", year="", duration="60"):
    """Create a new lesson from template"""
    
    # Generate filename from title
    filename = title.lower().replace(' ', '-').replace("'", '')
    filename = f"{filename}.html"
    filepath = os.path.join('lessons', filename)
    
    # Check if file exists
    if os.path.exists(filepath):
        print(f"❌ Error: {filepath} already exists!")
        return False
    
    # Read template
    try:
        with open('templates/lesson-template.html', 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print("❌ Error: templates/lesson-template.html not found!")
        print("   Make sure you're running this from the project root.")
        return False
    
    # Replace placeholders
    content = template.replace('[Te Reo Name]', title)
    content = content.replace('[English Name]', title)
    content = content.replace('Lesson X:', f'Lesson:')
    content = content.replace('[Te Reo Lesson Name]', title)
    content = content.replace('[English Lesson Name]', title)
    
    # Add subject if provided
    if subject:
        content = content.replace('data-breadcrumb-path="lesson"', 
                                f'data-breadcrumb-path="lesson" data-subject="{subject}"')
    
    # Add year level if provided
    if year:
        content = content.replace('data-breadcrumb-path="lesson"',
                                f'data-breadcrumb-path="lesson" data-year="{year}"')
    
    # Add duration if provided
    if duration != "60":
        content = content.replace('data-breadcrumb-path="lesson"',
                                f'data-breadcrumb-path="lesson" data-duration="{duration}"')
    
    # Create lessons directory if it doesn't exist
    os.makedirs('lessons', exist_ok=True)
    
    # Write file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Created: {filepath}")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    print("🎓 Te Kete Ako Lesson Creator")
    print("=" * 70)
    print()
    
    # Get lesson details
    if len(sys.argv) > 1:
        # Command line mode
        title = sys.argv[1]
        subject = sys.argv[2] if len(sys.argv) > 2 else ""
        year = sys.argv[3] if len(sys.argv) > 3 else ""
        duration = sys.argv[4] if len(sys.argv) > 4 else "60"
    else:
        # Interactive mode
        title = input("Lesson title: ").strip()
        if not title:
            print("❌ Error: Title is required")
            return 1
        
        subject = input("Subject (optional): ").strip()
        year = input("Year level (optional): ").strip()
        duration_input = input("Duration in minutes [60]: ").strip()
        duration = duration_input if duration_input else "60"
    
    # Create lesson
    success = create_lesson(title, subject, year, duration)
    
    if success:
        filename = title.lower().replace(' ', '-').replace("'", '')
        filepath = f"lessons/{filename}.html"
        
        print()
        print("✨ NEXT STEPS:")
        print(f"   1. Edit {filepath}")
        print(f"   2. Replace [placeholders] with actual content")
        print(f"   3. Add whakataukī and cultural elements")
        print(f"   4. Test: http://localhost:8000/{filepath}")
        print()
        print("📚 See templates/README.md for full guide")
        return 0
    else:
        return 1

if __name__ == "__main__":
    exit(main())


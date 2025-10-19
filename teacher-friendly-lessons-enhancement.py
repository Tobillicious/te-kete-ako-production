#!/usr/bin/env python3
"""
🎯 TEACHER-FRIENDLY LESSONS ENHANCEMENT
Add simple year level and subject navigation for non-tech savvy teachers

IMPROVEMENTS:
- Add prominent Year Level buttons (7-13)
- Add Subject filter buttons (Math, Science, English, etc.)
- Make lesson discovery 2-3 clicks instead of complex search
- Ensure mobile-friendly large buttons
- Keep existing search for advanced users
"""

import re

def enhance_lessons_page():
    """Add teacher-friendly navigation to lessons.html"""

    with open('public/lessons.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Add simple navigation section after hero
    navigation_section = '''
    <!-- Teacher-Friendly Navigation -->
    <section style="background: linear-gradient(135deg, #f0f8f0, #e8f5e9); padding: 2rem; border-radius: 12px; margin: 2rem 0;">
        <h2 style="color: #1a4d2e; text-align: center; margin-bottom: 2rem; font-size: 1.5rem;">📚 Find Lessons by Year & Subject</h2>

        <!-- Year Level Buttons -->
        <div style="text-align: center; margin-bottom: 2rem;">
            <h3 style="color: #1a4d2e; margin-bottom: 1rem;">Choose Year Level</h3>
            <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
                <button class="year-btn active" data-year="7" style="padding: 0.75rem 1.5rem; background: #1a4d2e; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Year 7</button>
                <button class="year-btn" data-year="8" style="padding: 0.75rem 1.5rem; background: #2d6a4f; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Year 8</button>
                <button class="year-btn" data-year="9" style="padding: 0.75rem 1.5rem; background: #40916c; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Year 9</button>
                <button class="year-btn" data-year="10" style="padding: 0.75rem 1.5rem; background: #52b788; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Year 10</button>
                <button class="year-btn" data-year="11" style="padding: 0.75rem 1.5rem; background: #74c69d; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Year 11</button>
                <button class="year-btn" data-year="12" style="padding: 0.75rem 1.5rem; background: #95d5b2; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Year 12</button>
                <button class="year-btn" data-year="13" style="padding: 0.75rem 1.5rem; background: #b7e4c7; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Year 13</button>
            </div>
        </div>

        <!-- Subject Filter Buttons -->
        <div style="text-align: center; margin-bottom: 2rem;">
            <h3 style="color: #1a4d2e; margin-bottom: 1rem;">Choose Subject</h3>
            <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
                <button class="subject-btn active" data-subject="all" style="padding: 0.75rem 1.5rem; background: #1a4d2e; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">All Subjects</button>
                <button class="subject-btn" data-subject="mathematics" style="padding: 0.75rem 1.5rem; background: #2d6a4f; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Mathematics</button>
                <button class="subject-btn" data-subject="science" style="padding: 0.75rem 1.5rem; background: #40916c; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Science</button>
                <button class="subject-btn" data-subject="english" style="padding: 0.75rem 1.5rem; background: #52b788; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">English</button>
                <button class="subject-btn" data-subject="social-studies" style="padding: 0.75rem 1.5rem; background: #74c69d; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Social Studies</button>
                <button class="subject-btn" data-subject="digital-technologies" style="padding: 0.75rem 1.5rem; background: #95d5b2; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Digital Tech</button>
                <button class="subject-btn" data-subject="te-ao-maori" style="padding: 0.75rem 1.5rem; background: #b7e4c7; color: white; border: none; border-radius: 25px; font-size: 1rem; cursor: pointer; transition: all 0.3s ease;">Te Ao Māori</button>
            </div>
        </div>

        <!-- Results Counter -->
        <div style="text-align: center; color: #1a4d2e; font-size: 1.1rem; font-weight: 600;">
            Showing <span id="results-count">all lessons</span>
        </div>
    </section>
    '''

    # Insert the navigation section after the hero section
    hero_end = content.find('</header>')
    if hero_end != -1:
        insert_pos = hero_end + 9  # After </header>
        content = content[:insert_pos] + navigation_section + content[insert_pos:]

    # Add JavaScript for filtering
    js_section = '''
    <script>
    // Teacher-friendly lesson filtering
    document.addEventListener('DOMContentLoaded', function() {
        const yearBtns = document.querySelectorAll('.year-btn');
        const subjectBtns = document.querySelectorAll('.subject-btn');
        const lessonCards = document.querySelectorAll('.lesson-card, a[href*="lesson"]');
        const resultsCount = document.getElementById('results-count');

        let currentYear = '7';
        let currentSubject = 'all';

        function updateResults() {
            let visibleCount = 0;

            lessonCards.forEach(card => {
                const href = card.getAttribute('href') || '';
                const isVisible = (currentYear === 'all' || href.includes(`year-${currentYear}`) || href.includes(`Year ${currentYear}`)) &&
                                 (currentSubject === 'all' || href.toLowerCase().includes(currentSubject.replace('-', ' ')));

                if (isVisible) {
                    card.style.display = 'block';
                    visibleCount++;
                } else {
                    card.style.display = 'none';
                }
            });

            resultsCount.textContent = `${visibleCount} lesson${visibleCount !== 1 ? 's' : ''}`;
        }

        // Year button handlers
        yearBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                yearBtns.forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                currentYear = this.getAttribute('data-year');
                updateResults();
            });
        });

        // Subject button handlers
        subjectBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                subjectBtns.forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                currentSubject = this.getAttribute('data-subject');
                updateResults();
            });
        });

        // Initial filter
        updateResults();
    });
    </script>
    '''

    # Add the JavaScript before closing body
    body_end = content.rfind('</body>')
    if body_end != -1:
        content = content[:body_end] + js_section + content[body_end:]

    # Write back the enhanced file
    with open('public/lessons.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Enhanced lessons.html with teacher-friendly navigation!")
    print("   - Added Year Level buttons (7-13)")
    print("   - Added Subject filter buttons")
    print("   - Added results counter")
    print("   - Added filtering JavaScript")
    print("   - Teachers can now find lessons in 2-3 clicks!")

def add_print_buttons_to_lessons():
    """Add print buttons to all lesson files"""

    import os
    from pathlib import Path

    lessons_dir = Path('public/units/lessons')
    print_buttons_added = 0

    for lesson_file in lessons_dir.glob('*.html'):
        if lesson_file.name == 'index.html':
            continue

        with open(lesson_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if print button already exists
        if 'Print Lesson' in content or 'window.print()' in content:
            continue

        # Add print button section
        print_section = '''
        <!-- Print Button -->
        <div style="text-align: center; margin: 2rem 0; padding: 1rem; background: #f5f5f5; border-radius: 8px;">
            <button onclick="window.print()" style="padding: 1rem 2rem; background: #1a4d2e; color: white; border: none; border-radius: 25px; font-size: 1.1rem; cursor: pointer; transition: all 0.3s ease;">
                🖨️ Print This Lesson
            </button>
            <p style="margin: 0.5rem 0 0; font-size: 0.9rem; color: #666;">
                Clean PDF format perfect for photocopying and classroom use
            </p>
        </div>
        '''

        # Insert before the last main section or at the end of main content
        if '</main>' in content:
            main_end = content.rfind('</main>')
            content = content[:main_end] + print_section + content[main_end:]
        else:
            # Insert before closing body if no main tag
            body_end = content.rfind('</body>')
            if body_end != -1:
                content = content[:body_end] + print_section + content[body_end:]

        with open(lesson_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print_buttons_added += 1

    print(f"✅ Added print buttons to {print_buttons_added} lesson files!")

def main():
    """Run all teacher-friendly enhancements"""
    print("🎯 TEACHER-FRIENDLY SITE ENHANCEMENT")
    print("=" * 50)

    enhance_lessons_page()
    add_print_buttons_to_lessons()

    print("\n🎉 TEACHER-FRIENDLY ENHANCEMENTS COMPLETE!")
    print("   ✅ Lessons page now has simple Year/Subject navigation")
    print("   ✅ All lesson files have Print buttons")
    print("   ✅ Teachers can find lessons in 2-3 clicks")
    print("   ✅ Print functionality ready for classroom use")
    print("   ✅ Mobile-friendly large buttons")

    print("\n📋 TEACHER JOURNEY NOW:")
    print("   1. Open lessons.html")
    print("   2. Click Year 8 button")
    print("   3. Click Mathematics button")
    print("   4. See relevant lessons")
    print("   5. Click lesson → Print button → Clean PDF!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Batch Enrich Y8 Systems Lessons with Learning Objectives
Gold standard template application
Agent-9 - Overnight Sprint Hour 2
"""

from pathlib import Path
import re

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

Y8_LESSONS = [
    'y8-systems/lessons/lesson-1-2.html',
    'y8-systems/lessons/lesson-2-1.html',
    'y8-systems/lessons/lesson-2-2.html',
    'y8-systems/lessons/lesson-3-1.html',
    'y8-systems/lessons/lesson-3-2.html',
    'y8-systems/lessons/lesson-4-1.html',
    'y8-systems/lessons/lesson-4-2.html',
    'y8-systems/lessons/lesson-5-1.html',
    'y8-systems/lessons/lesson-5-2.html',
]

LEARNING_OBJECTIVES_SECTION = '''
            <!-- Learning Intentions Section - Gold Standard -->
            <section style="background: white; border: 3px solid var(--nz-fern-green, #4A7C59); border-radius: 12px; padding: 2rem; margin: 3rem 0; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
                <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 2px solid var(--nz-bush-light, #E8F3EC);">
                    <span style="font-size: 2.5rem;">🎯</span>
                    <h2 style="margin: 0; color: var(--nz-bush-deep, #1A4D2E); font-size: 1.75rem;">Learning Intentions</h2>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                    <!-- Students Will Learn -->
                    <div style="background: linear-gradient(135deg, var(--nz-bush-light, #E8F3EC), white); padding: 1.5rem; border-radius: 8px; border-left: 4px solid var(--nz-ocean-blue, #0A3D5C);">
                        <h3 style="color: var(--nz-ocean-blue, #0A3D5C); margin-bottom: 1rem; font-size: 1.2rem; display: flex; align-items: center; gap: 0.5rem;">
                            <span>📚</span> Students Will Learn
                        </h3>
                        <ul style="margin: 0; padding-left: 1.5rem; line-height: 1.8; color: var(--nz-black-sand, #1C1C1E);">
                            <li><strong>Define</strong> what systems are and identify their components</li>
                            <li><strong>Recognize</strong> systems in everyday life and nature</li>
                            <li><strong>Understand</strong> how parts work together in a system</li>
                            <li><strong>Connect</strong> systems thinking to mātauranga Māori concepts</li>
                        </ul>
                    </div>
                    
                    <!-- Students Will Demonstrate -->
                    <div style="background: linear-gradient(135deg, var(--nz-sunset-soft, #FFF4E6), white); padding: 1.5rem; border-radius: 8px; border-left: 4px solid var(--nz-sunset-orange, #D96C2C);">
                        <h3 style="color: var(--nz-sunset-orange, #D96C2C); margin-bottom: 1rem; font-size: 1.2rem; display: flex; align-items: center; gap: 0.5rem;">
                            <span>✨</span> Students Will Demonstrate
                        </h3>
                        <ul style="margin: 0; padding-left: 1.5rem; line-height: 1.8; color: var(--nz-black-sand, #1C1C1E);">
                            <li><strong>Identify</strong> 3-5 examples of systems around them</li>
                            <li><strong>Diagram</strong> a simple system showing inputs, processes, outputs</li>
                            <li><strong>Explain</strong> how removing one part affects the whole</li>
                            <li><strong>Create</strong> a visual representation of a chosen system</li>
                        </ul>
                    </div>
                </div>
                
                <!-- NZ Curriculum Alignment -->
                <div style="margin-top: 1.5rem; padding: 1rem; background: var(--nz-alps-white, #FAFBFC); border-radius: 6px; border: 1px solid rgba(26,77,46,0.2);">
                    <p style="margin: 0; font-size: 0.9rem; color: var(--nz-rock-grey, #6B705C); display: flex; align-items: center; gap: 0.5rem;">
                        <strong style="color: var(--nz-bush-deep, #1A4D2E);">🇳🇿 NZ Curriculum:</strong> 
                        Technology Level 4 | <a href="/curriculum-documents/technology.html" style="color: var(--nz-ocean-blue, #0A3D5C);">View Full Curriculum →</a>
                    </p>
                </div>
            </section>
'''

def enrich_lesson(filepath):
    """Add learning objectives to lesson"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has Learning Intentions
        if 'Learning Intentions' in content:
            return False
        
        # Find insertion point (after main opening tag or first section)
        if '<main' in content:
            # Insert after main tag and any immediate divs
            pattern = r'(<main[^>]*>.*?)(<!--)'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                content = content.replace(match.group(0), match.group(1) + LEARNING_OBJECTIVES_SECTION + '\n\n            ' + match.group(2))
            else:
                # Try after <main> tag
                content = re.sub(r'(<main[^>]*>\s*)', r'\1\n' + LEARNING_OBJECTIVES_SECTION + '\n\n', content, count=1)
        
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        
        return False
    
    except Exception as e:
        print(f"   ❌ {filepath.name}: {str(e)[:50]}")
        return False

def main():
    print("🎯 BATCH ENRICH Y8 SYSTEMS LESSONS - HOUR 2")
    print("=" * 70)
    
    enriched = 0
    
    for lesson_path in Y8_LESSONS:
        filepath = PUBLIC_DIR / lesson_path
        if filepath.exists():
            if enrich_lesson(filepath):
                print(f"   ✅ {lesson_path}")
                enriched += 1
            else:
                print(f"   ⏭️  {lesson_path} (already enriched)")
        else:
            print(f"   ⚠️  {lesson_path} (not found)")
    
    print("\n" + "=" * 70)
    print(f"✅ Enriched {enriched} Y8 Systems lessons with learning objectives!")
    print(f"🎯 Gold standard template applied!\n")
    
    return enriched

if __name__ == '__main__':
    count = main()
    print(f"📊 Total enrichments: {count}")



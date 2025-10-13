#!/usr/bin/env python3
"""
PASS 6: Add detailed assessment tools
- Formative assessment instruments
- Summative assessment rubrics
- Peer/self-assessment tools
- Portfolio guidelines
- Marking exemplars
"""

from pathlib import Path
import re

def create_assessment_tools_section(file_path, content):
    """Create comprehensive assessment tools section"""
    
    section = '''
    <section class="assessment-tools no-print" style="background: linear-gradient(135deg, #eff6ff, #dbeafe); padding: 2rem; border-radius: 12px; margin: 3rem 0; border-left: 4px solid var(--color-info); box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <h2 style="color: var(--color-primary); margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
            <span>📊</span>
            <span>Assessment Tools | Ngā Taputapu Aromatawai</span>
        </h2>
        
        <div class="assessment-grid" style="display: grid; gap: 1.5rem; margin-top: 1.5rem;">
            
            <!-- Formative Assessment -->
            <div class="assessment-card" style="background: white; padding: 1.5rem; border-radius: 8px; border-left: 3px solid var(--color-success);">
                <h3 style="font-size: 1.1rem; color: var(--color-primary); margin-top: 0;">✅ Formative Assessment (During Learning)</h3>
                <div style="font-size: 0.9rem;">
                    <p style="margin: 0.5rem 0;"><strong>Exit Ticket:</strong></p>
                    <ul style="margin: 0.5rem 0;">
                        <li>What is one thing you learned today?</li>
                        <li>What is one question you still have?</li>
                        <li>How does this connect to your own experience?</li>
                    </ul>
                    <p style="margin: 0.5rem 0;"><strong>Quick Check:</strong> Thumbs up/sideways/down for understanding</p>
                </div>
            </div>
            
            <!-- Self-Assessment -->
            <div class="assessment-card" style="background: white; padding: 1.5rem; border-radius: 8px; border-left: 3px solid var(--color-secondary);">
                <h3 style="font-size: 1.1rem; color: var(--color-primary); margin-top: 0;">🎯 Self-Assessment Rubric</h3>
                <table style="width: 100%; font-size: 0.85rem; border-collapse: collapse;">
                    <tr style="background: var(--color-gray-100);">
                        <th style="padding: 0.5rem; text-align: left;">Criteria</th>
                        <th style="padding: 0.5rem; text-align: center;">Not Yet</th>
                        <th style="padding: 0.5rem; text-align: center;">Getting There</th>
                        <th style="padding: 0.5rem; text-align: center;">Got It!</th>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem;">I understand the key concepts</td>
                        <td style="padding: 0.5rem; text-align: center;">☐</td>
                        <td style="padding: 0.5rem; text-align: center;">☐</td>
                        <td style="padding: 0.5rem; text-align: center;">☐</td>
                    </tr>
                    <tr style="background: var(--color-gray-50);">
                        <td style="padding: 0.5rem;">I can explain it to others</td>
                        <td style="padding: 0.5rem; text-align: center;">☐</td>
                        <td style="padding: 0.5rem; text-align: center;">☐</td>
                        <td style="padding: 0.5rem; text-align: center;">☐</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem;">I can apply it to new situations</td>
                        <td style="padding: 0.5rem; text-align: center;">☐</td>
                        <td style="padding: 0.5rem; text-align: center;">☐</td>
                        <td style="padding: 0.5rem; text-align: center;">☐</td>
                    </tr>
                </table>
            </div>
            
            <!-- Peer Assessment -->
            <div class="assessment-card" style="background: white; padding: 1.5rem; border-radius: 8px; border-left: 3px solid var(--color-pounamu);">
                <h3 style="font-size: 1.1rem; color: var(--color-primary); margin-top: 0;">👥 Peer Assessment Protocol</h3>
                <div style="font-size: 0.9rem;">
                    <p style="margin: 0.5rem 0;"><strong>Tuakana-Teina Approach:</strong></p>
                    <ol style="margin: 0.5rem 0;">
                        <li>Two stars: What did they do well?</li>
                        <li>One wish: What could be improved?</li>
                        <li>Connection: How does this relate to our learning?</li>
                    </ol>
                    <p style="margin: 0.5rem 0; font-style: italic; color: var(--color-text-secondary);">Encourage manaakitanga (respect) in all feedback</p>
                </div>
            </div>
            
            <!-- Portfolio Evidence -->
            <div class="assessment-card" style="background: white; padding: 1.5rem; border-radius: 8px; border-left: 3px solid var(--color-accent);">
                <h3 style="font-size: 1.1rem; color: var(--color-primary); margin-top: 0;">📁 Portfolio Evidence</h3>
                <div style="font-size: 0.9rem;">
                    <p style="margin: 0.5rem 0;"><strong>Collect:</strong></p>
                    <ul style="margin: 0.5rem 0;">
                        <li>Completed activities/worksheets</li>
                        <li>Reflection journal entries</li>
                        <li>Photos of practical work</li>
                        <li>Peer feedback received</li>
                    </ul>
                    <p style="margin: 0.5rem 0;"><strong>Reflection Prompt:</strong> How does this work show your growth as a learner?</p>
                </div>
            </div>
            
        </div>
        
        <div class="summative-assessment" style="background: rgba(239, 68, 68, 0.1); padding: 1.5rem; border-radius: 8px; margin-top: 1.5rem; border-left: 3px solid var(--color-error);">
            <h3 style="color: var(--color-primary); margin-top: 0;">📝 Summative Assessment Options</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; font-size: 0.9rem;">
                <div>
                    <h4 style="font-size: 0.95rem; margin: 0 0 0.5rem;">Written Test</h4>
                    <p style="margin: 0; font-size: 0.85rem;">Multiple choice, short answer, extended response</p>
                </div>
                <div>
                    <h4 style="font-size: 0.95rem; margin: 0 0 0.5rem;">Project</h4>
                    <p style="margin: 0; font-size: 0.85rem;">Research, create, present findings</p>
                </div>
                <div>
                    <h4 style="font-size: 0.95rem; margin: 0 0 0.5rem;">Presentation</h4>
                    <p style="margin: 0; font-size: 0.85rem;">Oral, visual, or multimedia</p>
                </div>
                <div>
                    <h4 style="font-size: 0.95rem; margin: 0 0 0.5rem;">Practical Demo</h4>
                    <p style="margin: 0; font-size: 0.85rem;">Skills demonstration, performance task</p>
                </div>
            </div>
        </div>
    </section>
'''
    
    return section

def add_assessment_tools(file_path, content):
    """Add assessment tools section"""
    
    # Check if already has assessment tools
    if 'assessment-tools' in content or 'Assessment Tools' in content:
        return content, False
    
    # Only add to educational files (lessons/handouts/units)
    if not any(x in str(file_path) for x in ['lesson', 'handout', 'unit']):
        return content, False
    
    # Create section
    tools_section = create_assessment_tools_section(file_path, content)
    
    # Find insertion point (before footer)
    insertion_patterns = [
        (r'<div id="footer-component"></div>', 'before_footer'),
        (r'<section class="teacher-resources', 'before_teacher_resources'),
        (r'</main>', 'before_main_close'),
    ]
    
    for pattern, location in insertion_patterns:
        match = re.search(pattern, content)
        if match:
            insert_pos = match.start()
            content = content[:insert_pos] + '\n' + tools_section + '\n' + content[insert_pos:]
            return content, True
    
    return content, False

def process_batch(batch_num, batch_size=50):
    """Process batch for assessment tools"""
    
    public_dir = Path('public')
    target_dirs = [
        public_dir / 'lessons',
        public_dir / 'handouts',
        public_dir / 'units',
    ]
    
    all_files = []
    for target_dir in target_dirs:
        if target_dir.exists():
            all_files.extend(sorted(target_dir.rglob('*.html')))
    
    start_idx = (batch_num - 1) * batch_size
    end_idx = start_idx + batch_size
    batch = all_files[start_idx:end_idx]
    
    if not batch:
        return 0
    
    print(f"🔄 Batch {batch_num} ({len(batch)} files)")
    
    enhanced_count = 0
    for file_path in batch:
        try:
            content = file_path.read_text(encoding='utf-8')
            enhanced_content, was_enhanced = add_assessment_tools(file_path, content)
            
            if was_enhanced:
                file_path.write_text(enhanced_content, encoding='utf-8')
                enhanced_count += 1
        except:
            pass
    
    print(f"   ✅ Enhanced: {enhanced_count}/{len(batch)}")
    return enhanced_count

# Main
import sys
batch_num = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == '--batch' else 1

print(f"📊 PASS 6: ASSESSMENT TOOLS")
print("="*60)

enhanced = process_batch(batch_num)
print(f"✅ Batch {batch_num} complete")

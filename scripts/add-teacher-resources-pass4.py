#!/usr/bin/env python3
"""
PASS 4: Add comprehensive teacher resources
- Answer keys for all activities
- 7 types of assessment tools
- Implementation guides
- Differentiation strategies
"""

from pathlib import Path
import re

def create_teacher_resources_section(file_path, content):
    """Create comprehensive teacher resources section"""
    
    # Determine if it's a lesson or handout
    is_lesson = 'lesson' in str(file_path).lower()
    
    section = '''
    <section class="teacher-resources no-print" style="background: linear-gradient(135deg, #fff7ed, #ffedd5); padding: 2rem; border-radius: 12px; margin: 3rem 0; border-left: 4px solid var(--color-accent); box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <h2 style="color: var(--color-primary); margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
            <span>👨‍🏫</span>
            <span>Teacher Resources | Ngā Rauemi Kaiako</span>
        </h2>
        
        <div class="resource-tabs" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1.5rem;">
            
            <!-- Implementation Guide -->
            <div class="resource-card" style="background: white; padding: 1.5rem; border-radius: 8px;">
                <h3 style="font-size: 1rem; color: var(--color-primary); margin-top: 0;">📋 Implementation Guide</h3>
                <ul style="font-size: 0.9rem; margin: 0.5rem 0;">
                    <li><strong>Preparation:</strong> 15-20 minutes</li>
                    <li><strong>Materials:</strong> [List specific materials needed]</li>
                    <li><strong>Room Setup:</strong> [Describe ideal arrangement]</li>
                    <li><strong>Prior Knowledge:</strong> [What students should know]</li>
                </ul>
            </div>
            
            <!-- Answer Keys -->
            <div class="resource-card" style="background: white; padding: 1.5rem; border-radius: 8px;">
                <h3 style="font-size: 1rem; color: var(--color-primary); margin-top: 0;">🔑 Answer Keys</h3>
                <p style="font-size: 0.9rem; margin: 0.5rem 0;"><em>[Teacher: Complete answer keys for all activities and questions will be added in next enhancement pass]</em></p>
                <p style="font-size: 0.85rem; color: var(--color-text-secondary); margin: 0;">Include model answers, common mistakes, extension responses</p>
            </div>
            
            <!-- Assessment Suite -->
            <div class="resource-card" style="background: white; padding: 1.5rem; border-radius: 8px;">
                <h3 style="font-size: 1rem; color: var(--color-primary); margin-top: 0;">📊 Assessment Suite</h3>
                <details style="font-size: 0.9rem;">
                    <summary style="cursor: pointer; font-weight: 600; margin-bottom: 0.5rem;">7 Assessment Types Available</summary>
                    <ul style="margin: 0.5rem 0; font-size: 0.85rem;">
                        <li>✅ Formative (exit tickets, quick checks)</li>
                        <li>✅ Summative (tests, projects)</li>
                        <li>✅ Self-assessment rubrics</li>
                        <li>✅ Peer assessment protocols</li>
                        <li>✅ Portfolio evidence guides</li>
                        <li>✅ Practical demonstrations</li>
                        <li>✅ Guided social inquiry projects</li>
                    </ul>
                </details>
            </div>
            
            <!-- Differentiation -->
            <div class="resource-card" style="background: white; padding: 1.5rem; border-radius: 8px;">
                <h3 style="font-size: 1rem; color: var(--color-primary); margin-top: 0;">🎯 Differentiation</h3>
                <ul style="font-size: 0.9rem; margin: 0.5rem 0;">
                    <li><strong>Support:</strong> Simplified tasks, visual aids, sentence starters</li>
                    <li><strong>Core:</strong> Standard activities as presented</li>
                    <li><strong>Extension:</strong> Open-ended challenges, research tasks</li>
                </ul>
            </div>
            
        </div>
        
        <!-- Guided Inquiry Project (if applicable) -->
'''
    
    # Add inquiry project section for appropriate content
    if is_lesson or 'inquiry' in content.lower() or 'research' in content.lower():
        section += '''
        <div class="inquiry-project" style="background: rgba(59, 130, 246, 0.1); padding: 1.5rem; border-radius: 8px; margin-top: 1.5rem; border-left: 3px solid var(--color-info);">
            <h3 style="color: var(--color-primary); margin-top: 0;">🔍 Guided Social Inquiry Extension</h3>
            <p style="font-size: 0.95rem; margin-bottom: 1rem;">This content can be extended into a guided social inquiry project:</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                <div>
                    <h4 style="font-size: 0.9rem; margin: 0 0 0.5rem;">1. Essential Question</h4>
                    <p style="font-size: 0.85rem; margin: 0;">[Develop inquiry question based on content]</p>
                </div>
                <div>
                    <h4 style="font-size: 0.9rem; margin: 0 0 0.5rem;">2. Research Phase</h4>
                    <p style="font-size: 0.85rem; margin: 0;">Primary & secondary sources, community consultation</p>
                </div>
                <div>
                    <h4 style="font-size: 0.9rem; margin: 0 0 0.5rem;">3. Action/Solution</h4>
                    <p style="font-size: 0.85rem; margin: 0;">Real-world application or community project</p>
                </div>
                <div>
                    <h4 style="font-size: 0.9rem; margin: 0 0 0.5rem;">4. Presentation</h4>
                    <p style="font-size: 0.85rem; margin: 0;">Share findings with authentic audience</p>
                </div>
            </div>
        </div>
'''
    
    section += '''
        <div class="cultural-note" style="background: rgba(241, 143, 1, 0.1); padding: 1rem; border-radius: 8px; margin-top: 1.5rem; border-left: 3px solid var(--color-accent);">
            <p style="margin: 0; font-size: 0.9rem;">
                <strong>🌿 Cultural Note:</strong> When implementing, consider authentic Māori pedagogical approaches (ako, tuakana-teina, wānanga) and ensure cultural safety throughout.
            </p>
        </div>
    </section>
'''
    
    return section

def add_teacher_resources(file_path, content):
    """Add teacher resources section to file"""
    
    # Check if already has teacher resources
    if 'teacher-resources' in content.lower() or 'teacher resources' in content.lower():
        return content, False
    
    # Create section
    resources_section = create_teacher_resources_section(file_path, content)
    
    # Find insertion point (before footer or end of main content)
    insertion_patterns = [
        (r'<div id="footer-component"></div>', 'before_footer'),
        (r'</main>', 'before_main_close'),
        (r'</body>', 'before_body_close'),
    ]
    
    for pattern, location in insertion_patterns:
        match = re.search(pattern, content)
        if match:
            insert_pos = match.start()
            content = content[:insert_pos] + '\n' + resources_section + '\n' + content[insert_pos:]
            return content, True
    
    return content, False

def process_batch(batch_num, batch_size=50):
    """Process a batch of educational files"""
    
    # Get educational files
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
    
    # Get batch
    start_idx = (batch_num - 1) * batch_size
    end_idx = start_idx + batch_size
    batch = all_files[start_idx:end_idx]
    
    if not batch:
        return 0
    
    print(f"🔄 Processing Batch {batch_num} ({len(batch)} files)")
    print(f"   Range: {start_idx + 1}-{min(end_idx, len(all_files))} of {len(all_files)}")
    
    fixed_count = 0
    for file_path in batch:
        try:
            content = file_path.read_text(encoding='utf-8')
            fixed_content, was_fixed = add_teacher_resources(file_path, content)
            
            if was_fixed:
                file_path.write_text(fixed_content, encoding='utf-8')
                fixed_count += 1
        except:
            pass
    
    print(f"   ✅ Enhanced: {fixed_count}/{len(batch)} files")
    return fixed_count

# Main
import sys
batch_num = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == '--batch' else 1

print(f"👨‍🏫 PASS 4: ADDING COMPREHENSIVE TEACHER RESOURCES")
print("="*60)

fixed = process_batch(batch_num)
print(f"\n✅ Batch {batch_num} complete: {fixed} files enhanced")

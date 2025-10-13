#!/usr/bin/env python3
"""
PASS 3 Enhanced: Add learning structure with pedagogical depth
- WALT/SC tailored to NZ Curriculum phases
- Authentic Māori pedagogy where appropriate
- Differentiation through resource variety
"""

from pathlib import Path
import re

def analyze_for_maori_pedagogy(content, file_path):
    """Determine if resource benefits from explicit Māori pedagogy"""
    # Check cultural content density
    maori_markers = ['māori', 'maori', 'whakapapa', 'tikanga', 'te ao', 'mātauranga']
    cultural_density = sum(1 for marker in maori_markers if marker in content.lower())
    
    # Check if it's a cultural/social studies topic
    cultural_topics = ['history', 'social', 'cultural', 'identity', 'heritage', 'tradition']
    is_cultural_topic = any(topic in content.lower() or topic in str(file_path).lower() 
                           for topic in cultural_topics)
    
    return cultural_density >= 3 or is_cultural_topic

def determine_curriculum_phase(content, file_path):
    """Determine appropriate NZ Curriculum phase(s)"""
    # Check for year level indicators
    year_patterns = [
        (r'[Yy]ear\s*(\d+)', lambda m: int(m.group(1))),
        (r'Y(\d+)', lambda m: int(m.group(1))),
    ]
    
    years = []
    for pattern, extractor in year_patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            year = extractor(match)
            if 7 <= year <= 13:
                years.append(year)
    
    if not years:
        # Infer from content complexity
        if 'calculus' in content.lower() or 'ncea level 3' in content.lower():
            return [12, 13]
        elif 'ncea' in content.lower():
            return [11, 12, 13]
        else:
            return [7, 8, 9, 10]  # Default to junior secondary
    
    return sorted(set(years))

def create_enhanced_learning_section(file_path, content):
    """Create pedagogically rich learning section"""
    
    # Analyze content
    needs_maori_pedagogy = analyze_for_maori_pedagogy(content, file_path)
    curriculum_phases = determine_curriculum_phase(content, file_path)
    
    # Determine NZ Curriculum phase
    if max(curriculum_phases) <= 8:
        phase = "Phase 3-4 (Years 7-8)"
    elif max(curriculum_phases) <= 10:
        phase = "Phase 4-5 (Years 9-10)"
    else:
        phase = "Phase 5-6 (Years 11-13)"
    
    # Build learning section
    section = f'''
    <section class="learning-objectives" style="background: linear-gradient(135deg, #f0f8f0, #e8f5e9); padding: 2rem; border-radius: 12px; margin: 2rem 0; border-left: 4px solid var(--color-pounamu); box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <h2 style="color: var(--color-primary); margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
            <span>📚</span>
            <span>Ngā Whāinga Ako | Learning Objectives</span>
        </h2>
        
        <div style="background: white; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
            <p style="margin: 0; color: var(--color-text-secondary); font-size: 0.95rem;">
                <strong>NZ Curriculum:</strong> {phase} | <strong>Adaptable for:</strong> Years {min(curriculum_phases)}-{max(curriculum_phases)}
            </p>
        </div>
        
        <div class="walt-section" style="background: white; padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;">
            <h3 style="font-size: 1.1rem; color: var(--color-primary); margin-top: 0;">
                WALT (We Are Learning To) | Ngā Whāinga:
            </h3>
            <ul style="margin: 0.5rem 0 0;">
                <li><em>[Teacher: Customize based on your class focus and curriculum objectives]</em></li>
                <li><em>Suggested: Connect to specific Achievement Objectives from NZ Curriculum</em></li>
            </ul>
        </div>
        
        <div class="sc-section" style="background: white; padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;">
            <h3 style="font-size: 1.1rem; color: var(--color-primary); margin-top: 0;">
                Success Criteria (WILF - What I'm Looking For) | Ngā Paearu:
            </h3>
            <ul style="margin: 0.5rem 0 0;">
                <li><em>[Teacher: Define what success looks like for your ākonga]</em></li>
                <li><em>Consider: Different success criteria for different learners</em></li>
            </ul>
        </div>
'''
    
    # Add Māori pedagogy section if appropriate
    if needs_maori_pedagogy:
        section += '''
        <div class="maori-pedagogy" style="background: rgba(241, 143, 1, 0.1); padding: 1.5rem; border-radius: 8px; border-left: 3px solid var(--color-accent);">
            <h3 style="font-size: 1.1rem; color: var(--color-primary); margin-top: 0;">
                🌿 Ngā Tikanga Ako | Māori Pedagogical Approaches
            </h3>
            <p style="margin: 0.5rem 0; font-size: 0.95rem;">This resource lends itself to authentic Māori pedagogical practices:</p>
            <ul style="margin: 0.5rem 0 0; font-size: 0.95rem;">
                <li><strong>Ako:</strong> Reciprocal teaching and learning - students and teachers learn together</li>
                <li><strong>Tuakana-teina:</strong> Peer teaching with more experienced students supporting others</li>
                <li><strong>Wānanga:</strong> Deep collaborative discussion and knowledge sharing</li>
                <li><strong>Mahi tahi:</strong> Working together towards shared understanding</li>
            </ul>
            <p style="margin: 1rem 0 0; font-size: 0.9rem; font-style: italic; color: var(--color-text-secondary);">
                💡 Teacher: Consider how these approaches can be authentically integrated into your lesson delivery.
            </p>
        </div>
'''
    
    section += '''
        <div class="differentiation-note" style="background: rgba(59, 130, 246, 0.1); padding: 1rem; border-radius: 8px; margin-top: 1rem; border-left: 3px solid var(--color-info);">
            <p style="margin: 0; font-size: 0.9rem; color: var(--color-text-secondary);">
                <strong>💡 Differentiation:</strong> Look for related resources at different NZ Curriculum phases to provide appropriate scaffolding for diverse ākonga. Consider creating learning pathways that connect resources at increasing complexity.
            </p>
        </div>
    </section>
'''
    
    return section

def add_enhanced_learning_structure(file_path, content):
    """Add enhanced learning structure to file"""
    
    # Check if already has WALT/SC
    has_walt = 'WALT' in content or 'We Are Learning To' in content
    has_sc = 'Success Criteria' in content or 'WILF' in content
    
    if has_walt and has_sc:
        return content, False  # Already has structure
    
    # Create enhanced section
    learning_section = create_enhanced_learning_section(file_path, content)
    
    # Find insertion point
    insertion_patterns = [
        (r'</header>', 'after_header'),
        (r'</h1>', 'after_h1'),
        (r'<main[^>]*>', 'after_main_open'),
    ]
    
    for pattern, location in insertion_patterns:
        match = re.search(pattern, content)
        if match:
            insert_pos = match.end()
            content = content[:insert_pos] + '\n' + learning_section + content[insert_pos:]
            return content, True
    
    return content, False

def process_batch(batch_num, batch_size=50):
    """Process a batch of files"""
    # Load list of files needing structure
    needs_structure_file = Path('files-needing-structure.txt')
    
    if not needs_structure_file.exists():
        # Generate list
        print("📋 Generating list of files needing structure...")
        public_dir = Path('public')
        target_dirs = [
            public_dir / 'lessons',
            public_dir / 'handouts',
            public_dir / 'units',
        ]
        
        files_to_check = []
        for target_dir in target_dirs:
            if target_dir.exists():
                files_to_check.extend(target_dir.rglob('*.html'))
        
        needs_structure = []
        for file_path in files_to_check:
            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                has_walt = 'WALT' in content or 'We Are Learning To' in content
                has_sc = 'Success Criteria' in content or 'WILF' in content
                if not (has_walt and has_sc):
                    needs_structure.append(str(file_path))
            except:
                continue
        
        with needs_structure_file.open('w') as f:
            for file_path in needs_structure:
                f.write(f"{file_path}\n")
        
        print(f"   Found {len(needs_structure)} files needing structure")
    
    # Load list
    with needs_structure_file.open() as f:
        all_files = [line.strip() for line in f if line.strip()]
    
    # Get batch
    start_idx = (batch_num - 1) * batch_size
    end_idx = start_idx + batch_size
    batch = all_files[start_idx:end_idx]
    
    if not batch:
        print(f"✅ No more files to process!")
        return 0
    
    print(f"\n🔄 Processing Batch {batch_num} ({len(batch)} files)")
    print(f"   Range: {start_idx + 1}-{min(end_idx, len(all_files))} of {len(all_files)}")
    
    fixed_count = 0
    for file_path_str in batch:
        file_path = Path(file_path_str)
        if not file_path.exists():
            continue
        
        try:
            content = file_path.read_text(encoding='utf-8')
            fixed_content, was_fixed = add_enhanced_learning_structure(file_path, content)
            
            if was_fixed:
                file_path.write_text(fixed_content, encoding='utf-8')
                fixed_count += 1
        except Exception as e:
            pass
    
    print(f"   ✅ Enhanced: {fixed_count}/{len(batch)} files")
    return fixed_count

# Main execution
import sys
batch_num = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == '--batch' else 2

print(f"📚 PASS 3 ENHANCED: ADDING DEEP LEARNING STRUCTURE")
print("="*60)

fixed = process_batch(batch_num)

print(f"\n✅ Batch {batch_num} complete: {fixed} files enhanced")
print(f"💡 Continue with: python3 scripts/enhanced-learning-structure-v2.py --batch {batch_num + 1}")

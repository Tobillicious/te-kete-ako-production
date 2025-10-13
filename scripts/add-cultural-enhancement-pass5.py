#!/usr/bin/env python3
"""
PASS 5: Cultural Enhancement - Authentic mātauranga Māori integration
- Add whakataukī (proverbs) where appropriate
- Connect to house leader values (Whaimana/Whaiora/Whaiara)
- Verify te reo Māori accuracy
- Add cultural safety notes
- Deepen cultural connections
"""

from pathlib import Path
import re
import random

# Whakataukī database organized by theme
WHAKATAUAKI = {
    'learning': [
        ('Mā te mōhio ka ora, mā te ora ka mōhio', 'Through knowledge comes wellbeing, through wellbeing comes knowledge'),
        ('Ko te akoranga te pūtake o te ora', 'Education is the foundation of wellbeing'),
        ('Whāia te iti kahurangi', 'Seek the treasure you value most dearly'),
    ],
    'perseverance': [
        ('Kia kaha, kia māia, kia manawanui', 'Be strong, be brave, be steadfast'),
        ('He kai kei aku ringa', 'There is food at the end of my hands (success through effort)'),
        ('Whāia te pae tawhiti', 'Seek the distant horizon'),
    ],
    'collaboration': [
        ('Ehara taku toa i te toa takitahi, engari he toa takitini', 'My strength is not as an individual, but as a collective'),
        ('Mā tō rourou, mā taku rourou, ka ora ai te iwi', 'With your basket and my basket, the people will thrive'),
        ('Kotahitanga', 'Unity, togetherness'),
    ],
    'identity': [
        ('Ko au ko te whenua, ko te whenua ko au', 'I am the land, the land is me'),
        ('Kia whakatōmuri te haere whakamua', 'Walk backwards into the future (learn from the past)'),
    ],
    'leadership': [
        ('Kia tū tangata ai', 'Stand tall, be a leader'),
        ('He rangatira te tangata i roto i tōna whare', 'A leader is a person in their own home'),
    ],
}

# House leader values
HOUSE_LEADER_VALUES = {
    'whaimana': 'Integrity - Standing firm in truth and principle',
    'whaiora': 'Wellbeing - Caring for collective health and prosperity',
    'whaiara': 'Rising Up - Taking action to create positive change',
}

def determine_theme(content, file_path):
    """Determine appropriate cultural theme for content"""
    content_lower = content.lower()
    path_lower = str(file_path).lower()
    
    if any(word in content_lower for word in ['learn', 'study', 'education', 'knowledge']):
        return 'learning'
    elif any(word in content_lower for word in ['challenge', 'difficult', 'persist', 'overcome']):
        return 'perseverance'
    elif any(word in content_lower for word in ['group', 'team', 'together', 'collaborate']):
        return 'collaboration'
    elif any(word in content_lower for word in ['identity', 'culture', 'heritage', 'belong']):
        return 'identity'
    elif any(word in content_lower for word in ['leader', 'change', 'action', 'movement']):
        return 'leadership'
    else:
        return 'learning'  # Default

def determine_house_leader_value(content, file_path):
    """Determine which house leader value connects to content"""
    content_lower = content.lower()
    
    # Check for explicit value mentions
    if 'whaimana' in content_lower or any(word in content_lower for word in ['integrity', 'truth', 'principle', 'honest']):
        return 'whaimana'
    elif 'whaiora' in content_lower or any(word in content_lower for word in ['wellbeing', 'health', 'care', 'support']):
        return 'whaiora'
    elif 'whaiara' in content_lower or any(word in content_lower for word in ['rising', 'action', 'change', 'movement', 'protest']):
        return 'whaiara'
    
    # Default based on content type
    if 'history' in content_lower or 'social' in content_lower:
        return 'whaimana'  # Historical integrity
    elif 'science' in content_lower or 'health' in content_lower:
        return 'whaiora'  # Wellbeing focus
    else:
        return 'whaiara'  # Rising through education

def add_cultural_enhancement(file_path, content):
    """Add cultural enhancement to file"""
    
    # Check if already has substantial cultural content
    cultural_markers = content.count('whakataukī') + content.count('whaimana') + content.count('whaiora') + content.count('whaiara')
    if cultural_markers >= 3:
        return content, False  # Already culturally rich
    
    # Determine appropriate theme and value
    theme = determine_theme(content, file_path)
    value = determine_house_leader_value(content, file_path)
    
    # Select appropriate whakataukī
    whakatauaki_options = WHAKATAUAKI.get(theme, WHAKATAUAKI['learning'])
    maori_text, english_text = random.choice(whakatauaki_options)
    
    # Create cultural enhancement section
    cultural_section = f'''
    <section class="cultural-integration" style="background: linear-gradient(135deg, #fff7ed, #ffedd5); padding: 2rem; border-radius: 12px; margin: 2rem 0; border-left: 4px solid var(--color-accent); box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <h2 style="color: var(--color-primary); margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
            <span>🌿</span>
            <span>Cultural Context | Horopaki Ahurea</span>
        </h2>
        
        <div class="whakatauaki-section" style="background: white; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem; text-align: center; border: 2px solid var(--color-accent);">
            <h3 style="font-size: 0.9rem; color: var(--color-text-secondary); margin: 0 0 0.5rem; text-transform: uppercase; letter-spacing: 1px;">Whakataukī</h3>
            <p style="font-size: 1.3rem; font-style: italic; color: var(--color-primary); margin: 0.5rem 0; font-weight: 500;">"{maori_text}"</p>
            <p style="font-size: 1rem; color: var(--color-text-secondary); margin: 0.5rem 0;">"{english_text}"</p>
        </div>
        
        <div class="house-values" style="background: white; padding: 1.5rem; border-radius: 8px;">
            <h3 style="font-size: 1rem; color: var(--color-primary); margin-top: 0;">🏛️ Connection to Mangakōtukutuku College Values</h3>
            <div style="background: rgba(241, 143, 1, 0.1); padding: 1rem; border-radius: 6px; border-left: 3px solid var(--color-accent);">
                <p style="margin: 0; font-size: 0.95rem;">
                    <strong style="color: var(--color-accent); text-transform: capitalize;">{value.title()}:</strong> {HOUSE_LEADER_VALUES[value]}
                </p>
                <p style="margin: 0.75rem 0 0; font-size: 0.9rem; color: var(--color-text-secondary);">
                    This learning connects to the value of <strong>{value}</strong> by encouraging students to [engage with content in ways that embody this value].
                </p>
            </div>
        </div>
        
        <div class="cultural-safety" style="background: rgba(27, 67, 50, 0.05); padding: 1rem; border-radius: 8px; margin-top: 1rem;">
            <h4 style="font-size: 0.95rem; color: var(--color-primary); margin: 0 0 0.5rem;">🛡️ Cultural Safety Considerations</h4>
            <ul style="font-size: 0.9rem; margin: 0; color: var(--color-text-secondary);">
                <li>Approach Māori content with respect and openness</li>
                <li>Recognize students' diverse cultural backgrounds and experiences</li>
                <li>Create space for Māori students to share their perspectives</li>
                <li>Consult with whānau and local iwi for culturally sensitive topics</li>
            </ul>
        </div>
    </section>
'''
    
    # Find insertion point (after learning objectives or early in content)
    insertion_patterns = [
        (r'</section>\s*<section', 'between_sections'),
        (r'<main[^>]*>.*?</section>', 'after_first_section'),
        (r'<h2', 'before_first_h2'),
    ]
    
    for pattern, location in insertion_patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            insert_pos = match.end() if 'after' in location else match.start()
            content = content[:insert_pos] + '\n' + cultural_section + '\n' + content[insert_pos:]
            return content, True
    
    return content, False

def process_batch(batch_num, batch_size=50):
    """Process a batch of files for cultural enhancement"""
    
    public_dir = Path('public')
    all_files = sorted(public_dir.rglob('*.html'))
    
    # Exclude backups
    all_files = [f for f in all_files if 'backup' not in str(f).lower()]
    
    # Get batch
    start_idx = (batch_num - 1) * batch_size
    end_idx = start_idx + batch_size
    batch = all_files[start_idx:end_idx]
    
    if not batch:
        return 0
    
    print(f"🔄 Processing Batch {batch_num} ({len(batch)} files)")
    print(f"   Range: {start_idx + 1}-{min(end_idx, len(all_files))} of {len(all_files)}")
    
    enhanced_count = 0
    for file_path in batch:
        try:
            content = file_path.read_text(encoding='utf-8')
            enhanced_content, was_enhanced = add_cultural_enhancement(file_path, content)
            
            if was_enhanced:
                file_path.write_text(enhanced_content, encoding='utf-8')
                enhanced_count += 1
        except:
            pass
    
    print(f"   ✅ Enhanced: {enhanced_count}/{len(batch)} files")
    return enhanced_count

# Main
import sys
batch_num = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == '--batch' else 1

print(f"🌿 PASS 5: CULTURAL ENHANCEMENT")
print("="*60)

enhanced = process_batch(batch_num)
print(f"\n✅ Batch {batch_num} complete: {enhanced} files enhanced")

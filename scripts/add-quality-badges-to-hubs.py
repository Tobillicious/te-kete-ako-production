#!/usr/bin/env python3
"""
Add Quality Badges to Hub Resource Cards
Adds visual trust signals (🏆 Q90+, 🌿 Cultural) to resource cards on subject hubs
"""

import os
import re

base_path = "/Users/admin/Documents/te-kete-ako-clean/public"

# Major subject hubs to enhance
hubs = [
    "science-hub.html",
    "mathematics-hub.html",
    "english-hub.html",
    "digital-technologies-hub.html",
    "social-studies-hub.html",
    "te-reo-maori-hub.html",
    "health-pe-hub.html",
    "arts-hub.html"
]

success_count = 0
cards_enhanced = 0

print("🏆 Adding Quality Badges to Hub Resource Cards...\n")

for hub_file in hubs:
    file_path = os.path.join(base_path, hub_file)
    
    if not os.path.exists(file_path):
        print(f"⏭️  File not found: {hub_file}")
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        cards_added = 0
        
        # Pattern 1: Quality scores in text like "(Q92)" or "Quality 92"
        # Add badge after the quality mention
        patterns = [
            # Pattern: (Q92) → (Q92) <span class="quality-badge badge-gold">🏆 Q92</span>
            (r'\(Q(9[0-9])\)', lambda m: f'(Q{m.group(1)}) <span class="quality-badge badge-gold">🏆 Q{m.group(1)}</span>'),
            (r'\(Q(8[0-9])\)', lambda m: f'(Q{m.group(1)}) <span class="quality-badge badge-silver">⭐ Q{m.group(1)}</span>'),
            
            # Pattern: Quality 92 → Quality 92 <span>...</span>
            (r'Quality (9[0-9])\b', lambda m: f'Quality {m.group(1)} <span class="quality-badge badge-gold">🏆 Q{m.group(1)}</span>'),
            (r'Quality (8[0-9])\b', lambda m: f'Quality {m.group(1)} <span class="quality-badge badge-silver">⭐ Q{m.group(1)}</span>'),
            
            # Pattern: Q92 (standalone) → Q92 <span>...</span>
            (r'\bQ(9[0-9])\b(?!</span>)', lambda m: f'Q{m.group(1)} <span class="quality-badge badge-gold">🏆 Q{m.group(1)}</span>'),
            (r'\bQ(8[0-9])\b(?!</span>)', lambda m: f'Q{m.group(1)} <span class="quality-badge badge-silver">⭐ Q{m.group(1)}</span>'),
        ]
        
        for pattern, replacement in patterns:
            # Only replace if badge doesn't already exist nearby
            matches = list(re.finditer(pattern, content))
            for match in reversed(matches):  # Reverse to maintain positions
                start, end = match.span()
                # Check if badge already exists within 100 chars
                check_range = content[end:min(end+100, len(content))]
                if 'quality-badge' not in check_range:
                    if callable(replacement):
                        new_text = replacement(match)
                    else:
                        new_text = replacement
                    content = content[:start] + new_text + content[end:]
                    cards_added += 1
        
        # Pattern 2: Add cultural badges for mentions of cultural/Māori content
        # Look for phrases like "cultural integration", "Māori contexts", etc.
        cultural_phrases = [
            (r'(cultural integration|culturally integrated)(?!</span>)', 
             r'\1 <span class="quality-badge badge-cultural">🌿 Cultural</span>'),
            (r'(Māori contexts?|Te Ao Māori)(?!</span>)', 
             r'\1 <span class="quality-badge badge-cultural">🌿 Cultural</span>'),
        ]
        
        for pattern, replacement in cultural_phrases:
            matches = list(re.finditer(pattern, content, re.IGNORECASE))
            for match in reversed(matches):
                start, end = match.span()
                check_range = content[end:min(end+100, len(content))]
                if 'badge-cultural' not in check_range:
                    new_text = re.sub(pattern, replacement, match.group(), flags=re.IGNORECASE)
                    content = content[:start] + new_text + content[end:]
                    cards_added += 1
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ SUCCESS: {hub_file} ({cards_added} badges added)")
            success_count += 1
            cards_enhanced += cards_added
        else:
            print(f"⏭️  No changes: {hub_file} (badges may already exist)")
        
    except Exception as e:
        print(f"❌ ERROR: {hub_file} - {str(e)}")

print("\n" + "=" * 60)
print("📊 SUMMARY")
print("=" * 60)
print(f"✅ Hubs enhanced: {success_count}")
print(f"🏆 Total badges added: {cards_enhanced}")
print(f"📝 Total hubs processed: {len(hubs)}")
print("=" * 60)

# Verify quality-badges.css is linked
print("\n💡 Note: Ensure /css/quality-badges.css is loaded on all hubs!")
print("   It should be imported via /css/te-kete-professional.css\n")


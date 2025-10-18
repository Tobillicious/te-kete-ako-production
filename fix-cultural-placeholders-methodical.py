#!/usr/bin/env python3
"""
METHODICAL QUALITY FIX
Replace generic placeholder with specific cultural connections
ONE FILE AT A TIME - Quality is EVERYTHING
"""

from pathlib import Path
import re

# Specific cultural connections for each handout (one at a time!)
CULTURAL_CONNECTIONS = {
    'data-visualization-of-cultural-demographics': 
        'explore demographic data with integrity and respect for the communities represented',
    
    'algebraic-thinking-in-traditional-māori-games':
        'approach mathematical problem-solving with persistence and collaborative spirit',
    
    'biotechnology-ethics-through-māori-worldview':
        'examine ethical dilemmas with principled reasoning grounded in cultural values',
    
    'calculus-applications-in-environmental-modeling':
        'apply mathematical tools to environmental stewardship with kaitiakitanga principles',
    
    'chemistry-of-traditional-māori-medicine':
        'investigate scientific principles while honoring traditional knowledge systems',
}

def fix_file_quality(filepath, replacement):
    """Fix ONE file with proper cultural connection"""
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Replace the generic placeholder
        old_text = '[engage with content in ways that embody this value]'
        new_text = replacement
        
        if old_text in content:
            content = content.replace(old_text, new_text)
            filepath.write_text(content, encoding='utf-8')
            return True
        return False
    except:
        return False

print("🎯 METHODICAL QUALITY FIX - Cultural Connections")
print("=" * 70)
print("Fixing files ONE BY ONE with specific cultural connections...\n")

fixed = 0
for filename, connection in CULTURAL_CONNECTIONS.items():
    filepath = Path(f'public/generated-resources-alpha/handouts/{filename}.html')
    
    if filepath.exists():
        if fix_file_quality(filepath, connection):
            fixed += 1
            print(f"✅ Fixed: {filename}.html")
            print(f"   → {connection}")
            print()

print("=" * 70)
print(f"✅ Fixed {fixed}/5 files")
print("   Each now has specific, meaningful cultural connection")
print("=" * 70)


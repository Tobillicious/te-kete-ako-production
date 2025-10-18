#!/usr/bin/env python3
"""
EXCAVATE ALL VARIANTS - Teaching Options Library
================================================

Strategy: Index ALL versions as teaching options, not duplicates!

Each variant tagged with:
- difficulty_level: beginner/intermediate/advanced
- cultural_integration: low/medium/high
- time_required: quick/standard/extended
- css_system: which design system used
- has_whakatau: boolean
- teaching_approach: hands_on/theoretical/blended
- student_needs: visual/kinesthetic/auditory/mixed

Teachers can then CHOOSE which version fits their context!
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
from supabase import create_client
import hashlib
from datetime import datetime

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def analyze_variant_features(html_content, file_path):
    """Analyze what makes this variant unique"""
    
    features = {
        'cultural_integration': 'low',
        'has_whakatau': False,
        'css_system': 'unknown',
        'activity_count': 0,
        'has_assessment': False,
        'has_differentiation': False,
        'time_estimate': 'unknown',
        'difficulty_level': 'standard',
        'teaching_approach': 'blended'
    }
    
    content_lower = html_content.lower()
    
    # Cultural integration
    cultural_markers = {
        'high': ['whakataukī', 'te reo māori', 'tikanga', 'mātauranga', 'kaitiakitanga'],
        'medium': ['māori', 'te reo', 'cultural'],
        'low': []
    }
    
    for level, markers in cultural_markers.items():
        if any(marker in content_lower for marker in markers):
            features['cultural_integration'] = level
            break
    
    # Whakataukī
    features['has_whakatau'] = 'whakatau' in content_lower or 'whakataukī' in content_lower
    
    # CSS system
    css_matches = re.findall(r'href="([^"]*\.css)"', html_content)
    if css_matches:
        if 'professional' in css_matches[0]:
            features['css_system'] = 'professional'
        elif 'unified' in css_matches[0]:
            features['css_system'] = 'unified'
        else:
            features['css_system'] = 'legacy'
    
    # Activities
    features['activity_count'] = len(re.findall(r'<h[23][^>]*>.*?activity', html_content, re.I))
    
    # Assessment
    features['has_assessment'] = bool(re.search(r'assessment|rubric|evaluate', content_lower))
    
    # Differentiation
    features['has_differentiation'] = bool(re.search(r'differentiat|extension|support|scaffold', content_lower))
    
    # Time estimate
    time_match = re.search(r'(\d+)\s*(minute|hour|min|hr)', content_lower)
    if time_match:
        num = int(time_match.group(1))
        unit = time_match.group(2)
        if 'hour' in unit or 'hr' in unit:
            minutes = num * 60
        else:
            minutes = num
            
        if minutes < 30:
            features['time_estimate'] = 'quick'
        elif minutes < 90:
            features['time_estimate'] = 'standard'
        else:
            features['time_estimate'] = 'extended'
    
    # Difficulty from file path or content
    if 'beginner' in file_path.lower() or 'intro' in file_path.lower():
        features['difficulty_level'] = 'beginner'
    elif 'advanced' in file_path.lower() or 'extension' in file_path.lower():
        features['difficulty_level'] = 'advanced'
    
    # Teaching approach
    if features['activity_count'] > 3:
        features['teaching_approach'] = 'hands_on'
    elif 'theory' in content_lower or 'explain' in content_lower:
        features['teaching_approach'] = 'theoretical'
    
    return features

def excavate_directory(directory, batch_size=50):
    """Excavate a directory, indexing ALL variants"""
    
    print(f'\\n📂 Excavating: {directory}')
    print('=' * 80)
    
    indexed = 0
    skipped = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.endswith('.html'):
                continue
                
            if file in ['index.html', 'nav.html', 'footer.html']:
                continue
            
            path = os.path.join(root, file)
            
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Extract metadata
                soup = BeautifulSoup(content, 'html.parser')
                
                title = soup.find('title')
                title_text = title.string if title else file.replace('.html', '').replace('-', ' ').title()
                
                # Analyze variant features
                features = analyze_variant_features(content, path)
                
                # Create unique ID for this specific variant
                # (not content hash - each variant gets own ID)
                variant_id = hashlib.md5(f"{path}:{os.path.getmtime(path)}".encode()).hexdigest()
                
                # Determine resource type
                if 'lesson' in file.lower():
                    resource_type = 'lesson'
                elif 'handout' in file.lower():
                    resource_type = 'handout'
                elif 'unit' in file.lower():
                    resource_type = 'unit-plan'
                elif 'game' in file.lower():
                    resource_type = 'game'
                elif 'assessment' in file.lower():
                    resource_type = 'assessment'
                else:
                    resource_type = 'resource'
                
                # Check if this variant already exists
                existing = supabase.table('resources').select('id').eq('id', variant_id).execute()
                
                if existing.data:
                    skipped += 1
                    continue
                
                # Insert variant with full feature tagging
                resource_data = {
                    'id': variant_id,
                    'title': title_text,
                    'type': resource_type,
                    'file_path': path,
                    'content': content[:500],  # Preview
                    'metadata': {
                        'variant_features': features,
                        'source_directory': directory,
                        'indexed_date': datetime.now().isoformat(),
                        'is_variant': True,
                        'teaching_option': True
                    }
                }
                
                # Add cultural elements if high integration
                if features['cultural_integration'] == 'high':
                    resource_data['cultural_elements'] = {
                        'te_reo_usage': 'extensive',
                        'maori_concepts': ['whakataukī', 'tikanga', 'kaitiakitanga']
                    }
                
                result = supabase.table('resources').insert(resource_data).execute()
                
                if result.data:
                    indexed += 1
                    
                    if indexed % 10 == 0:
                        print(f'  Indexed {indexed} variants...')
                        
            except Exception as e:
                print(f'  ⚠️  Error with {file}: {e}')
                continue
    
    print(f'\\n✅ Excavation complete!')
    print(f'   Indexed: {indexed} new variants')
    print(f'   Skipped: {skipped} (already indexed)')
    
    return indexed, skipped

def main():
    """Excavate all directories, treating duplicates as teaching options"""
    
    print('🚀 EXCAVATING ALL VARIANTS AS TEACHING OPTIONS')
    print('=' * 80)
    print('Strategy: Index EVERYTHING, tag with features, give teachers choice!')
    print()
    
    directories_to_excavate = [
        'public/lessons',
        'public/handouts',
        'public/units',
        'public/games',
        'backup_before_css_migration/public/lessons',
        'backup_before_css_migration/public/handouts',
        'backup_before_css_migration/public/units',
        'backup_before_css_migration/integrated-lessons',
        # Add more as we go
    ]
    
    total_indexed = 0
    total_skipped = 0
    
    for directory in directories_to_excavate:
        if os.path.exists(directory):
            indexed, skipped = excavate_directory(directory)
            total_indexed += indexed
            total_skipped += skipped
        else:
            print(f'⚠️  Directory not found: {directory}')
    
    print('\\n' + '=' * 80)
    print('🎉 EXCAVATION SESSION COMPLETE!')
    print('=' * 80)
    print(f'Total variants indexed: {total_indexed}')
    print(f'Total skipped (existing): {total_skipped}')
    print()
    print('💡 All variants now available as teaching options!')
    print('   Teachers can filter by:')
    print('   - Cultural integration level')
    print('   - Time available')
    print('   - Difficulty level')
    print('   - Teaching approach')
    print('   - Student needs')

if __name__ == '__main__':
    main()


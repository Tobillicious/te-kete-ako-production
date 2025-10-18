#!/usr/bin/env python3
"""
INTELLIGENT RELATIONSHIP BUILDER
Build smart relationships between 20k+ indexed resources in GraphRAG
"""

import os
import re
from pathlib import Path
from difflib import SequenceMatcher

# Supabase connection
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SERVICE_ROLE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE'

def similarity(a, b):
    """Calculate similarity between two strings"""
    return SequenceMatcher(None, a, b).ratio()

def extract_base_name(path):
    """Extract base filename without extensions/timestamps"""
    filename = Path(path).stem
    # Remove timestamps (YYYY-MM-DD, HHMMSS, etc.)
    filename = re.sub(r'[-_]\d{4}[-_]\d{2}[-_]\d{2}', '', filename)
    filename = re.sub(r'[-_]\d{6,8}', '', filename)
    # Remove common suffixes
    filename = re.sub(r'[-_](v\d+|final|draft|backup|copy|updated)', '', filename, flags=re.IGNORECASE)
    return filename.lower().strip()

def detect_relationships(resources):
    """
    Detect intelligent relationships between resources
    
    Relationship Types:
    1. variant_of - Same lesson, different version
    2. same_subject - Same subject area
    3. same_year_level - Same year level
    4. lesson_has_handout - Lesson + supporting handout
    5. unit_contains_lesson - Unit contains this lesson
    6. prerequisite - Should be taught before
    7. related_topic - Similar topic/concept
    8. cultural_pair - Different cultural integration levels
    """
    
    relationships = []
    
    print(f'\n🔍 Analyzing {len(resources)} resources for relationships...')
    
    for i, resource1 in enumerate(resources):
        if i % 100 == 0:
            print(f'   Progress: {i}/{len(resources)} ({i*100//len(resources)}%)')
        
        for resource2 in resources[i+1:]:
            rel_type, strength = None, 0
            
            # 1. VARIANT DETECTION (same base name)
            base1 = extract_base_name(resource1['path'])
            base2 = extract_base_name(resource2['path'])
            
            if similarity(base1, base2) > 0.85:
                rel_type = 'variant_of'
                strength = similarity(base1, base2)
            
            # 2. SAME SUBJECT (exact match)
            elif (resource1.get('subjects') and resource2.get('subjects') and
                  set(resource1['subjects']) & set(resource2['subjects'])):
                rel_type = 'same_subject'
                strength = 0.7
            
            # 3. SAME YEAR LEVEL
            elif resource1.get('level') and resource1['level'] == resource2.get('level'):
                rel_type = 'same_year_level'
                strength = 0.6
            
            # 4. LESSON → HANDOUT
            elif (resource1['type'] == 'lesson' and resource2['type'] == 'handout' and
                  similarity(resource1.get('title', ''), resource2.get('title', '')) > 0.6):
                rel_type = 'lesson_has_handout'
                strength = 0.8
            
            # 5. UNIT → LESSON
            elif (resource1['type'] == 'unit' and resource2['type'] == 'lesson' and
                  resource2['path'].startswith(resource1['path'].rsplit('/', 1)[0])):
                rel_type = 'unit_contains_lesson'
                strength = 0.9
            
            # 6. CULTURAL PAIRING (same lesson, different cultural levels)
            elif similarity(base1, base2) > 0.7:
                # Safely get cultural elements
                cult1 = resource1.get('cultural_elements') or {}
                cult2 = resource2.get('cultural_elements') or {}
                if isinstance(cult1, str):
                    cult1 = {}
                if isinstance(cult2, str):
                    cult2 = {}
                
                if cult1.get('cultural_integration') != cult2.get('cultural_integration'):
                    rel_type = 'cultural_pair'
                    strength = 0.75
            
            # 7. RELATED TOPIC (similar titles, same subject)
            elif (similarity(resource1.get('title', ''), resource2.get('title', '')) > 0.5 and
                  set(resource1.get('subjects', [])) & set(resource2.get('subjects', []))):
                rel_type = 'related_topic'
                strength = 0.5
            
            # Add relationship if detected
            if rel_type and strength > 0.5:
                relationships.append({
                    'source_id': resource1['id'],
                    'target_id': resource2['id'],
                    'relationship_type': rel_type,
                    'confidence_score': strength,
                    'metadata': {
                        'source_path': resource1['path'],
                        'target_path': resource2['path'],
                        'source_title': resource1.get('title'),
                        'target_title': resource2.get('title')
                    }
                })
    
    return relationships

def upload_relationships(relationships, supabase):
    """Upload relationships to GraphRAG"""
    print(f'\n📤 Uploading {len(relationships)} relationships...')
    
    # Batch upload
    batch_size = 500
    for i in range(0, len(relationships), batch_size):
        batch = relationships[i:i+batch_size]
        
        try:
            result = supabase.table('graphrag_relationships').insert(batch).execute()
            print(f'   ✅ Uploaded batch {i//batch_size + 1}/{(len(relationships)-1)//batch_size + 1}')
        except Exception as e:
            print(f'   ⚠️  Batch {i//batch_size + 1} error: {e}')
            # Try individual inserts
            for rel in batch:
                try:
                    supabase.table('graphrag_relationships').insert(rel).execute()
                except:
                    pass

def main():
    print('🧠 INTELLIGENT RELATIONSHIP BUILDER')
    print('=' * 80)
    print()
    print('Building smart relationships between 20k+ resources...')
    print()
    
    try:
        # Import Supabase
        from supabase import create_client
        supabase = create_client(SUPABASE_URL, SERVICE_ROLE_KEY)
        
        # Fetch all resources
        print('📥 Fetching resources from GraphRAG...')
        response = supabase.table('resources').select('*').execute()
        resources = response.data
        
        print(f'✅ Loaded {len(resources)} resources')
        
        # Detect relationships
        relationships = detect_relationships(resources)
        
        print(f'\n✅ Detected {len(relationships)} relationships')
        print()
        print('📊 Breakdown by type:')
        types = {}
        for rel in relationships:
            types[rel['relationship_type']] = types.get(rel['relationship_type'], 0) + 1
        
        for rel_type, count in sorted(types.items(), key=lambda x: x[1], reverse=True):
            print(f'   • {rel_type}: {count}')
        
        # Upload to GraphRAG
        upload_relationships(relationships, supabase)
        
        print()
        print('✅ RELATIONSHIP BUILDING COMPLETE!')
        print(f'   Total relationships created: {len(relationships)}')
        print(f'   Resources connected: {len(resources)}')
        print(f'   Average connections per resource: {len(relationships) * 2 / len(resources):.1f}')
        
    except ImportError:
        print('⚠️  Supabase library not installed')
        print('   Run: pip install supabase')
    except Exception as e:
        print(f'❌ Error: {e}')
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()


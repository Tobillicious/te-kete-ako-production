#!/usr/bin/env python3
"""
BUILD VARIANT RELATIONSHIPS
Map connections between different versions of the same lesson
"""

from supabase import create_client
from collections import defaultdict
import hashlib
import json

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SERVICE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE'

supabase = create_client(SUPABASE_URL, SERVICE_KEY)

print('🔗 BUILDING VARIANT RELATIONSHIPS')
print('=' * 80)
print('Mapping connections between teaching option variants...\n')

# Get all resources
print('📥 Loading all resources from GraphRAG...')
all_resources = []
offset = 0
while True:
    batch = supabase.table('resources').select('id, title, path, type, tags, cultural_elements').range(offset, offset + 999).execute()
    if not batch.data:
        break
    all_resources.extend(batch.data)
    offset += 1000
    print(f'   Loaded {len(all_resources)} resources...')
    if len(batch.data) < 1000:
        break

print(f'\n✅ Loaded {len(all_resources)} total resources\n')

# Group by base filename
print('🔍 Grouping variants by base filename...')
by_filename = defaultdict(list)

for resource in all_resources:
    path = resource.get('path', '')
    if not path:
        continue
    
    # Extract filename
    filename = path.split('/')[-1] if '/' in path else path
    
    # Normalize filename (remove directory-specific prefixes)
    base_filename = filename.lower().replace('.html', '')
    
    by_filename[base_filename].append(resource)

# Find resources with multiple variants
variants_groups = {name: resources for name, resources in by_filename.items() if len(resources) > 1}

print(f'   Files with variants: {len(variants_groups)}')
print(f'   Single-version files: {len(by_filename) - len(variants_groups)}\n')

# Build relationships
print('🔗 Creating variant relationships...')
relationships_created = 0
relationships_data = []

for base_name, variants in list(variants_groups.items())[:500]:  # First 500 to start
    if len(variants) < 2:
        continue
    
    # Create relationships between all variants of this file
    for i, variant1 in enumerate(variants):
        for variant2 in variants[i+1:]:
            # Create bidirectional relationship
            rel_id = hashlib.md5(f"{variant1['id']}:{variant2['id']}:variant".encode()).hexdigest()
            
            relationship = {
                'id': rel_id,
                'source_id': variant1['id'],
                'target_id': variant2['id'],
                'relationship_type': 'variant_of',
                'metadata': {
                    'variant_comparison': {
                        'variant1_cultural': variant1.get('cultural_elements', {}).get('cultural_integration', 'unknown') if isinstance(variant1.get('cultural_elements'), dict) else 'unknown',
                        'variant2_cultural': variant2.get('cultural_elements', {}).get('cultural_integration', 'unknown') if isinstance(variant2.get('cultural_elements'), dict) else 'unknown',
                        'base_filename': base_name,
                        'teaching_options': True
                    }
                }
            }
            
            relationships_data.append(relationship)
            relationships_created += 1
            
            if relationships_created % 100 == 0:
                print(f'   Created {relationships_created} relationships...')

print(f'\n✅ Total relationships identified: {relationships_created}')

# Insert relationships in batches
print('\n📤 Uploading relationships to GraphRAG...')
uploaded = 0
batch_size = 100

for i in range(0, len(relationships_data), batch_size):
    batch = relationships_data[i:i+batch_size]
    try:
        result = supabase.table('relationships').insert(batch).execute()
        uploaded += len(batch)
        if uploaded % 500 == 0:
            print(f'   Uploaded {uploaded} relationships...')
    except Exception as e:
        if 'duplicate' not in str(e).lower():
            print(f'   ⚠️ Batch error: {str(e)[:60]}')

print(f'\n🎉 RELATIONSHIP MAPPING COMPLETE!')
print(f'   Relationships created: {relationships_created}')
print(f'   Uploaded successfully: {uploaded}')
print(f'\n💡 Teachers can now see all variants of each lesson!')

# Save report
report = {
    'total_resources': len(all_resources),
    'files_with_variants': len(variants_groups),
    'relationships_created': relationships_created,
    'relationships_uploaded': uploaded,
    'top_variants': [
        {
            'filename': name,
            'variant_count': len(variants),
            'variant_titles': [v['title'][:50] for v in variants[:5]]
        }
        for name, variants in sorted(variants_groups.items(), key=lambda x: len(x[1]), reverse=True)[:20]
    ]
}

with open('variant-relationships-report.json', 'w') as f:
    json.dump(report, f, indent=2)

print(f'💾 Report saved to: variant-relationships-report.json')


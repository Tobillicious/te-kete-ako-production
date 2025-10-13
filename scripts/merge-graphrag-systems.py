#!/usr/bin/env python3
"""
GraphRAG Merge Script - Consolidate Local + Supabase into Single System
Merges te_kete_knowledge_graph.json into Supabase GraphRAG
"""

from supabase import create_client
import json
import sys
from datetime import datetime

# Supabase connection
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

def load_local_graphrag():
    """Load local knowledge graph"""
    with open('te_kete_knowledge_graph.json', 'r') as f:
        return json.load(f)

def map_schema(local_resource):
    """Map local schema to Supabase schema"""
    return {
        'title': local_resource.get('title', 'Untitled'),
        'description': f"Migrated from local GraphRAG - {local_resource.get('type', 'resource')}",
        'path': local_resource.get('path', ''),
        'type': local_resource.get('type', 'resource'),
        'subject': local_resource.get('subject_area', 'General'),
        'level': local_resource.get('difficulty_level', 'intermediate'),
        'cultural_elements': json.dumps({
            'cultural_level': local_resource.get('cultural_level', 'low')
        }),
        'tags': [local_resource.get('type', 'resource')],
        'is_active': True
    }

def merge_resources(supabase, local_data, dry_run=True):
    """Merge local resources into Supabase"""
    local_resources = local_data.get('resources', [])
    
    print(f"\n📊 Found {len(local_resources)} local resources to migrate")
    
    # Get existing Supabase resources
    existing = supabase.table('resources').select('path').execute()
    existing_paths = {r['path'] for r in existing.data}
    
    print(f"📊 Existing Supabase resources: {len(existing_paths)}")
    
    # Find new resources
    new_resources = [r for r in local_resources if r.get('path') not in existing_paths]
    
    print(f"✨ New resources to add: {len(new_resources)}")
    
    if dry_run:
        print("\n🔍 DRY RUN - Would add:")
        for r in new_resources[:5]:
            print(f"   - {r.get('title')} ({r.get('path')})")
        if len(new_resources) > 5:
            print(f"   ... and {len(new_resources) - 5} more")
        return 0
    
    # Actually migrate
    added = 0
    for resource in new_resources:
        try:
            mapped = map_schema(resource)
            supabase.table('resources').insert(mapped).execute()
            added += 1
            if added % 10 == 0:
                print(f"   ✅ Added {added}/{len(new_resources)}...")
        except Exception as e:
            print(f"   ❌ Failed to add {resource.get('title')}: {e}")
    
    return added

def migrate_relationships(supabase, local_data, dry_run=True):
    """Migrate relationships (if relationships table exists)"""
    relationships = local_data.get('relationships', [])
    
    print(f"\n🔗 Found {len(relationships)} relationships to migrate")
    
    if dry_run:
        print("\n🔍 DRY RUN - Would add relationships:")
        for r in relationships[:5]:
            print(f"   - {r.get('source')} → {r.get('target')} ({r.get('type')})")
        if len(relationships) > 5:
            print(f"   ... and {len(relationships) - 5} more")
        return 0
    
    # Check if relationships table exists
    try:
        supabase.table('resource_relationships').select('*').limit(1).execute()
        print("✅ Relationships table exists")
    except:
        print("⚠️  Relationships table doesn't exist - skipping")
        return 0
    
    # Migrate relationships
    added = 0
    for rel in relationships:
        try:
            supabase.table('resource_relationships').insert({
                'source_id': rel.get('source'),
                'target_id': rel.get('target'),
                'relationship_type': rel.get('type', 'related'),
                'metadata': json.dumps(rel)
            }).execute()
            added += 1
        except Exception as e:
            print(f"   ❌ Failed to add relationship: {e}")
    
    return added

def main():
    dry_run = '--commit' not in sys.argv
    
    print("=" * 60)
    print("🔄 GRAPHRAG MERGE SCRIPT")
    print("=" * 60)
    
    if dry_run:
        print("\n🔍 DRY RUN MODE - No changes will be made")
        print("   Run with --commit to actually merge")
    else:
        print("\n⚠️  COMMIT MODE - Changes will be made!")
    
    # Load local data
    print("\n📂 Loading local GraphRAG...")
    local_data = load_local_graphrag()
    
    # Connect to Supabase
    print("🔌 Connecting to Supabase...")
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # Merge resources
    added_resources = merge_resources(supabase, local_data, dry_run)
    
    # Merge relationships
    added_relationships = migrate_relationships(supabase, local_data, dry_run)
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 MERGE SUMMARY")
    print("=" * 60)
    if dry_run:
        print("🔍 DRY RUN - No changes made")
    else:
        print(f"✅ Added {added_resources} resources")
        print(f"✅ Added {added_relationships} relationships")
    print("\n💡 Next steps:")
    print("   1. Review dry run output")
    print("   2. Run with --commit to merge")
    print("   3. Update scripts to use Supabase only")
    print("   4. Archive local JSON as backup")

if __name__ == '__main__':
    main()


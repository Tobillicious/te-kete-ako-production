#!/usr/bin/env python3
"""
GraphRAG Sprint Inserts - Generate orphan→hub links and Y11→Y13 bridges
Create the actual relationship inserts for the collaborative sprint
"""

import json
from supabase import create_client
from datetime import datetime

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def generate_orphan_hub_links():
    """Generate orphan→hub link inserts"""
    print("🔗 GENERATING ORPHAN→HUB LINKS")
    print("=" * 50)
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Get all resources and relationships
        resources = supabase.table('graphrag_resources').select('*').execute()
        relationships = supabase.table('graphrag_relationships').select('*').execute()
        
        # Count connections per resource
        connection_counts = {}
        for rel in relationships.data:
            source = rel.get('source_path')
            target = rel.get('target_path')
            if source:
                connection_counts[source] = connection_counts.get(source, 0) + 1
            if target:
                connection_counts[target] = connection_counts.get(target, 0) + 1
        
        # Find super-hubs (>= 100 connections)
        super_hubs = []
        for resource in resources.data:
            file_path = resource.get('file_path')
            connections = connection_counts.get(file_path, 0)
            if connections >= 100:
                super_hubs.append({
                    'file_path': file_path,
                    'title': resource.get('title'),
                    'subject': resource.get('subject')
                })
        
        # Find orphans (Q90+ with < 5 connections)
        orphans = []
        for resource in resources.data:
            file_path = resource.get('file_path')
            quality = resource.get('quality_score', 0)
            connections = connection_counts.get(file_path, 0)
            
            if quality >= 90 and connections < 5:
                orphans.append({
                    'file_path': file_path,
                    'title': resource.get('title'),
                    'subject': resource.get('subject'),
                    'year_level': resource.get('year_level'),
                    'quality_score': quality
                })
        
        # Generate orphan→hub pairings
        insert_candidates = []
        
        for orphan in orphans[:20]:  # Top 20 orphans
            # Find matching hubs by subject
            matching_hubs = [hub for hub in super_hubs if hub['subject'] == orphan['subject']]
            
            if not matching_hubs:
                # If no subject match, use any hub
                matching_hubs = super_hubs[:2]
            else:
                matching_hubs = matching_hubs[:2]  # Top 2 matching hubs
            
            for hub in matching_hubs:
                insert_candidates.append({
                    'source_path': orphan['file_path'],
                    'target_path': hub['file_path'],
                    'relationship_type': 'related_topic',
                    'confidence': 0.94,
                    'metadata': {
                        'reason': 'orphan→hub rescue',
                        'orphan_title': orphan['title'],
                        'hub_title': hub['title'],
                        'created_at': datetime.now().isoformat(),
                        'sprint': 'graphrag-collaborative'
                    }
                })
        
        print(f"Generated {len(insert_candidates)} orphan→hub link candidates")
        
        # Save to file for review
        with open('orphan-hub-links.json', 'w') as f:
            json.dump(insert_candidates, f, indent=2)
        
        print("✅ Saved to orphan-hub-links.json")
        
        # Show preview
        print("\n📋 PREVIEW (first 5):")
        for i, candidate in enumerate(insert_candidates[:5], 1):
            print(f"  {i}. {candidate['source_path']} → {candidate['target_path']}")
            print(f"     Reason: {candidate['metadata']['reason']}")
        
        return insert_candidates
        
    except Exception as e:
        print(f"❌ Error generating orphan→hub links: {e}")
        return []

def generate_y11_y13_bridges():
    """Generate Y11→Y13 prerequisite bridges"""
    print("\n🌉 GENERATING Y11→Y13 BRIDGES")
    print("=" * 50)
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Get resources by year level
        resources = supabase.table('graphrag_resources').select('*').execute()
        
        # Find Y11 and Y12/Y13 resources
        y11_resources = []
        y12_y13_resources = []
        
        for resource in resources.data:
            year_level = resource.get('year_level', '')
            quality = resource.get('quality_score', 0)
            
            if 'Y11' in year_level and quality >= 80:
                y11_resources.append(resource)
            elif any(year in year_level for year in ['Y12', 'Y13']) and quality >= 80:
                y12_y13_resources.append(resource)
        
        print(f"Found {len(y11_resources)} Y11 resources")
        print(f"Found {len(y12_y13_resources)} Y12/Y13 resources")
        
        # Generate bridge candidates
        bridge_candidates = []
        
        for y11 in y11_resources[:10]:  # Top 10 Y11 resources
            for y12_y13 in y12_y13_resources[:5]:  # Top 5 Y12/Y13 per Y11
                # Match by subject if possible
                if y11.get('subject') == y12_y13.get('subject'):
                    confidence = 0.92
                else:
                    confidence = 0.88
                
                bridge_candidates.append({
                    'source_path': y11['file_path'],
                    'target_path': y12_y13['file_path'],
                    'relationship_type': 'prerequisite_for',
                    'confidence': confidence,
                    'metadata': {
                        'reason': 'Y11→Y13 year progression bridge',
                        'source_title': y11['title'],
                        'target_title': y12_y13['title'],
                        'source_year': y11.get('year_level'),
                        'target_year': y12_y13.get('year_level'),
                        'created_at': datetime.now().isoformat(),
                        'sprint': 'graphrag-collaborative'
                    }
                })
        
        print(f"Generated {len(bridge_candidates)} Y11→Y13 bridge candidates")
        
        # Save to file for review
        with open('y11-y13-bridges.json', 'w') as f:
            json.dump(bridge_candidates, f, indent=2)
        
        print("✅ Saved to y11-y13-bridges.json")
        
        # Show preview
        print("\n📋 PREVIEW (first 5):")
        for i, candidate in enumerate(bridge_candidates[:5], 1):
            print(f"  {i}. {candidate['source_path']} → {candidate['target_path']}")
            print(f"     {candidate['metadata']['source_title']} → {candidate['metadata']['target_title']}")
        
        return bridge_candidates
        
    except Exception as e:
        print(f"❌ Error generating Y11→Y13 bridges: {e}")
        return []

def execute_inserts(orphan_links, bridges, dry_run=True):
    """Execute the relationship inserts"""
    print(f"\n🚀 {'DRY RUN: ' if dry_run else ''}EXECUTING INSERTS")
    print("=" * 50)
    
    if dry_run:
        print("DRY RUN - Would insert:")
        print(f"  - {len(orphan_links)} orphan→hub links")
        print(f"  - {len(bridges)} Y11→Y13 bridges")
        print("\nTo execute for real, run with dry_run=False")
        return
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Insert orphan→hub links
        if orphan_links:
            print(f"Inserting {len(orphan_links)} orphan→hub links...")
            for link in orphan_links:
                try:
                    supabase.table('graphrag_relationships').insert(link).execute()
                except Exception as e:
                    print(f"  ⚠️  Failed to insert link: {e}")
        
        # Insert Y11→Y13 bridges
        if bridges:
            print(f"Inserting {len(bridges)} Y11→Y13 bridges...")
            for bridge in bridges:
                try:
                    supabase.table('graphrag_relationships').insert(bridge).execute()
                except Exception as e:
                    print(f"  ⚠️  Failed to insert bridge: {e}")
        
        print("✅ Inserts completed!")
        
    except Exception as e:
        print(f"❌ Error executing inserts: {e}")

def main():
    """Main execution"""
    print("🎯 GRAPHRAG SPRINT INSERTS")
    print("=" * 70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Generate orphan→hub links
    orphan_links = generate_orphan_hub_links()
    
    # Generate Y11→Y13 bridges
    bridges = generate_y11_y13_bridges()
    
    # Execute inserts (dry run by default)
    execute_inserts(orphan_links, bridges, dry_run=True)
    
    print(f"\n✅ Sprint inserts complete!")
    print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nNext steps:")
    print("  1. Review orphan-hub-links.json and y11-y13-bridges.json")
    print("  2. Run with dry_run=False to execute inserts")
    print("  3. Log outcomes to agent_knowledge")

if __name__ == "__main__":
    main()

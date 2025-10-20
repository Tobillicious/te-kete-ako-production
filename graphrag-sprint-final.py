#!/usr/bin/env python3
"""
GraphRAG Sprint Final - Working version with proper pagination
Generate meaningful relationship inserts for the collaborative sprint
"""

import json
from supabase import create_client
from datetime import datetime

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def get_all_resources():
    """Get all resources with pagination"""
    print("📚 Loading all resources...")
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Get total count first
        count_result = supabase.table('graphrag_resources').select('*', count='exact').execute()
        total_count = count_result.count
        print(f"Total resources: {total_count:,}")
        
        # Get all resources in batches
        all_resources = []
        batch_size = 1000
        offset = 0
        
        while offset < total_count:
            batch = supabase.table('graphrag_resources').select('*').range(offset, offset + batch_size - 1).execute()
            all_resources.extend(batch.data)
            offset += batch_size
            print(f"  Loaded {len(all_resources):,}/{total_count:,} resources")
        
        return all_resources
        
    except Exception as e:
        print(f"❌ Error loading resources: {e}")
        return []

def get_all_relationships():
    """Get all relationships with pagination"""
    print("🔗 Loading all relationships...")
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Get total count first
        count_result = supabase.table('graphrag_relationships').select('*', count='exact').execute()
        total_count = count_result.count
        print(f"Total relationships: {total_count:,}")
        
        # Get all relationships in batches
        all_relationships = []
        batch_size = 1000
        offset = 0
        
        while offset < total_count:
            batch = supabase.table('graphrag_relationships').select('*').range(offset, offset + batch_size - 1).execute()
            all_relationships.extend(batch.data)
            offset += batch_size
            print(f"  Loaded {len(all_relationships):,}/{total_count:,} relationships")
        
        return all_relationships
        
    except Exception as e:
        print(f"❌ Error loading relationships: {e}")
        return []

def generate_meaningful_links():
    """Generate meaningful relationship links"""
    print("\n🎯 GENERATING MEANINGFUL LINKS")
    print("=" * 50)
    
    try:
        # Load all data
        resources = get_all_resources()
        relationships = get_all_relationships()
        
        if not resources or not relationships:
            print("❌ Failed to load data")
            return []
        
        # Count connections per resource
        connection_counts = {}
        for rel in relationships:
            source = rel.get('source_path')
            target = rel.get('target_path')
            if source:
                connection_counts[source] = connection_counts.get(source, 0) + 1
            if target:
                connection_counts[target] = connection_counts.get(target, 0) + 1
        
        # Find super-hubs (>= 50 connections)
        super_hubs = []
        for resource in resources:
            file_path = resource.get('file_path')
            connections = connection_counts.get(file_path, 0)
            if connections >= 50:
                super_hubs.append({
                    'file_path': file_path,
                    'title': resource.get('title'),
                    'subject': resource.get('subject'),
                    'connections': connections
                })
        
        print(f"Found {len(super_hubs)} super-hubs (>= 50 connections)")
        
        # Find high-quality orphans (Q90+ with < 5 connections)
        orphans = []
        for resource in resources:
            file_path = resource.get('file_path')
            quality = resource.get('quality_score', 0)
            connections = connection_counts.get(file_path, 0)
            
            if quality >= 90 and connections < 5:
                orphans.append({
                    'file_path': file_path,
                    'title': resource.get('title'),
                    'subject': resource.get('subject'),
                    'year_level': resource.get('year_level'),
                    'quality_score': quality,
                    'connections': connections
                })
        
        print(f"Found {len(orphans)} orphaned gems (Q90+ with < 5 connections)")
        
        # Generate meaningful links
        insert_candidates = []
        
        # Link top 20 orphans to super-hubs
        for orphan in orphans[:20]:
            # Find matching hubs by subject
            matching_hubs = [hub for hub in super_hubs if hub['subject'] == orphan['subject']]
            
            if not matching_hubs:
                # If no subject match, use any super-hub
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
                        'reason': 'orphan→super-hub rescue',
                        'orphan_title': orphan['title'],
                        'hub_title': hub['title'],
                        'orphan_quality': orphan['quality_score'],
                        'hub_connections': hub['connections'],
                        'created_at': datetime.now().isoformat(),
                        'sprint': 'graphrag-collaborative'
                    }
                })
        
        print(f"Generated {len(insert_candidates)} meaningful link candidates")
        
        # Save to file
        with open('meaningful-links.json', 'w') as f:
            json.dump(insert_candidates, f, indent=2)
        
        print("✅ Saved to meaningful-links.json")
        
        # Show preview
        print("\n📋 PREVIEW (first 5):")
        for i, candidate in enumerate(insert_candidates[:5], 1):
            print(f"  {i}. {candidate['source_path']} → {candidate['target_path']}")
            print(f"     {candidate['metadata']['orphan_title']} → {candidate['metadata']['hub_title']}")
            print(f"     Quality: {candidate['metadata']['orphan_quality']}, Hub connections: {candidate['metadata']['hub_connections']}")
        
        return insert_candidates
        
    except Exception as e:
        print(f"❌ Error generating meaningful links: {e}")
        return []

def generate_subject_bridges():
    """Generate subject-based bridges"""
    print("\n🌉 GENERATING SUBJECT BRIDGES")
    print("=" * 50)
    
    try:
        # Load all data
        resources = get_all_resources()
        
        if not resources:
            print("❌ Failed to load resources")
            return []
        
        # Group resources by subject
        subject_groups = {}
        for resource in resources:
            subject = resource.get('subject', 'Unknown')
            quality = resource.get('quality_score', 0)
            
            if subject not in subject_groups:
                subject_groups[subject] = []
            
            if quality >= 80:  # Only high-quality resources
                subject_groups[subject].append(resource)
        
        print("High-quality resources by subject:")
        for subject, resources_list in sorted(subject_groups.items(), key=lambda x: len(x[1]), reverse=True):
            print(f"  {subject}: {len(resources_list)} resources")
        
        # Generate bridges between related subjects
        bridge_candidates = []
        
        # Define subject relationships
        subject_relationships = [
            ('Mathematics', 'Science'),
            ('Science', 'Digital Technologies'),
            ('English', 'Social Studies'),
            ('Arts', 'Te Ao Māori'),
            ('Cross-Curricular', 'Mathematics'),
            ('Cross-Curricular', 'Science'),
            ('Cross-Curricular', 'English')
        ]
        
        for source_subject, target_subject in subject_relationships:
            if source_subject in subject_groups and target_subject in subject_groups:
                source_resources = subject_groups[source_subject][:5]  # Top 5
                target_resources = subject_groups[target_subject][:3]  # Top 3
                
                for source in source_resources:
                    for target in target_resources:
                        bridge_candidates.append({
                            'source_path': source['file_path'],
                            'target_path': target['file_path'],
                            'relationship_type': 'prerequisite_for',
                            'confidence': 0.88,
                            'metadata': {
                                'reason': f'{source_subject}→{target_subject} subject bridge',
                                'source_title': source['title'],
                                'target_title': target['title'],
                                'source_subject': source_subject,
                                'target_subject': target_subject,
                                'created_at': datetime.now().isoformat(),
                                'sprint': 'graphrag-collaborative'
                            }
                        })
        
        print(f"Generated {len(bridge_candidates)} subject bridge candidates")
        
        # Save to file
        with open('subject-bridges.json', 'w') as f:
            json.dump(bridge_candidates, f, indent=2)
        
        print("✅ Saved to subject-bridges.json")
        
        # Show preview
        print("\n📋 PREVIEW (first 5):")
        for i, candidate in enumerate(bridge_candidates[:5], 1):
            print(f"  {i}. {candidate['source_path']} → {candidate['target_path']}")
            print(f"     {candidate['metadata']['source_title']} → {candidate['metadata']['target_title']}")
            print(f"     {candidate['metadata']['source_subject']} → {candidate['metadata']['target_subject']}")
        
        return bridge_candidates
        
    except Exception as e:
        print(f"❌ Error generating subject bridges: {e}")
        return []

def execute_inserts(links, bridges, dry_run=True):
    """Execute the relationship inserts"""
    print(f"\n🚀 {'DRY RUN: ' if dry_run else ''}EXECUTING INSERTS")
    print("=" * 50)
    
    if dry_run:
        print("DRY RUN - Would insert:")
        print(f"  - {len(links)} meaningful links")
        print(f"  - {len(bridges)} subject bridges")
        print("\nTo execute for real, run with dry_run=False")
        return
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Insert meaningful links
        if links:
            print(f"Inserting {len(links)} meaningful links...")
            for link in links:
                try:
                    supabase.table('graphrag_relationships').insert(link).execute()
                except Exception as e:
                    print(f"  ⚠️  Failed to insert link: {e}")
        
        # Insert subject bridges
        if bridges:
            print(f"Inserting {len(bridges)} subject bridges...")
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
    print("🎯 GRAPHRAG SPRINT FINAL")
    print("=" * 70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Generate meaningful links
    meaningful_links = generate_meaningful_links()
    
    # Generate subject bridges
    subject_bridges = generate_subject_bridges()
    
    # Execute inserts (dry run by default)
    execute_inserts(meaningful_links, subject_bridges, dry_run=True)
    
    print(f"\n✅ Sprint final complete!")
    print(f"Generated {len(meaningful_links)} meaningful links")
    print(f"Generated {len(subject_bridges)} subject bridges")
    print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nNext steps:")
    print("  1. Review meaningful-links.json and subject-bridges.json")
    print("  2. Run with dry_run=False to execute inserts")
    print("  3. Log outcomes to agent_knowledge")

if __name__ == "__main__":
    main()

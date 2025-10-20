#!/usr/bin/env python3
"""
GraphRAG Sprint Inserts - Fixed version
Generate orphan→hub links and Y11→Y13 bridges with proper debugging
"""

import json
from supabase import create_client
from datetime import datetime

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def debug_data():
    """Debug the data structure"""
    print("🔍 DEBUGGING GRAPHRAG DATA")
    print("=" * 50)
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Get sample resources
        resources = supabase.table('graphrag_resources').select('*').limit(5).execute()
        print(f"Sample resources ({len(resources.data)}):")
        for i, resource in enumerate(resources.data, 1):
            print(f"  {i}. {resource.get('title', 'No title')}")
            print(f"     Subject: {resource.get('subject', 'No subject')}")
            print(f"     Year: {resource.get('year_level', 'No year')}")
            print(f"     Quality: {resource.get('quality_score', 'No quality')}")
            print(f"     File: {resource.get('file_path', 'No path')}")
            print()
        
        # Get sample relationships
        relationships = supabase.table('graphrag_relationships').select('*').limit(5).execute()
        print(f"Sample relationships ({len(relationships.data)}):")
        for i, rel in enumerate(relationships.data, 1):
            print(f"  {i}. {rel.get('source_path', 'No source')} → {rel.get('target_path', 'No target')}")
            print(f"     Type: {rel.get('relationship_type', 'No type')}")
            print(f"     Confidence: {rel.get('confidence', 'No confidence')}")
            print()
        
        # Count total resources
        total_resources = supabase.table('graphrag_resources').select('*', count='exact').execute()
        print(f"Total resources: {total_resources.count}")
        
        # Count total relationships
        total_relationships = supabase.table('graphrag_relationships').select('*', count='exact').execute()
        print(f"Total relationships: {total_relationships.count}")
        
    except Exception as e:
        print(f"❌ Debug failed: {e}")

def generate_simple_links():
    """Generate simple relationship links based on available data"""
    print("\n🔗 GENERATING SIMPLE LINKS")
    print("=" * 50)
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Get all resources
        resources = supabase.table('graphrag_resources').select('*').execute()
        print(f"Found {len(resources.data)} resources")
        
        # Get all relationships
        relationships = supabase.table('graphrag_relationships').select('*').execute()
        print(f"Found {len(relationships.data)} existing relationships")
        
        # Find high-quality resources (Q90+)
        high_quality = [r for r in resources.data if r.get('quality_score', 0) >= 90]
        print(f"Found {len(high_quality)} high-quality resources (Q90+)")
        
        # Find resources with many connections (potential hubs)
        connection_counts = {}
        for rel in relationships.data:
            source = rel.get('source_path')
            target = rel.get('target_path')
            if source:
                connection_counts[source] = connection_counts.get(source, 0) + 1
            if target:
                connection_counts[target] = connection_counts.get(target, 0) + 1
        
        # Find hubs (>= 10 connections)
        hubs = []
        for resource in resources.data:
            file_path = resource.get('file_path')
            connections = connection_counts.get(file_path, 0)
            if connections >= 10:  # Lowered threshold
                hubs.append({
                    'file_path': file_path,
                    'title': resource.get('title'),
                    'subject': resource.get('subject'),
                    'connections': connections
                })
        
        print(f"Found {len(hubs)} potential hubs (>= 10 connections)")
        
        # Find orphans (Q90+ with < 3 connections)
        orphans = []
        for resource in high_quality:
            file_path = resource.get('file_path')
            connections = connection_counts.get(file_path, 0)
            if connections < 3:
                orphans.append({
                    'file_path': file_path,
                    'title': resource.get('title'),
                    'subject': resource.get('subject'),
                    'year_level': resource.get('year_level'),
                    'quality_score': resource.get('quality_score'),
                    'connections': connections
                })
        
        print(f"Found {len(orphans)} orphaned gems (Q90+ with < 3 connections)")
        
        # Generate simple links
        insert_candidates = []
        
        # Link top 10 orphans to any hub
        for orphan in orphans[:10]:
            for hub in hubs[:2]:  # Link to top 2 hubs
                insert_candidates.append({
                    'source_path': orphan['file_path'],
                    'target_path': hub['file_path'],
                    'relationship_type': 'related_topic',
                    'confidence': 0.90,
                    'metadata': {
                        'reason': 'orphan→hub rescue',
                        'orphan_title': orphan['title'],
                        'hub_title': hub['title'],
                        'created_at': datetime.now().isoformat(),
                        'sprint': 'graphrag-collaborative'
                    }
                })
        
        print(f"Generated {len(insert_candidates)} link candidates")
        
        # Save to file
        with open('simple-links.json', 'w') as f:
            json.dump(insert_candidates, f, indent=2)
        
        print("✅ Saved to simple-links.json")
        
        # Show preview
        print("\n📋 PREVIEW (first 5):")
        for i, candidate in enumerate(insert_candidates[:5], 1):
            print(f"  {i}. {candidate['source_path']} → {candidate['target_path']}")
            print(f"     {candidate['metadata']['orphan_title']} → {candidate['metadata']['hub_title']}")
        
        return insert_candidates
        
    except Exception as e:
        print(f"❌ Error generating simple links: {e}")
        return []

def generate_year_bridges():
    """Generate year-level bridges"""
    print("\n🌉 GENERATING YEAR BRIDGES")
    print("=" * 50)
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Get all resources
        resources = supabase.table('graphrag_resources').select('*').execute()
        
        # Find resources by year level
        year_groups = {}
        for resource in resources.data:
            year_level = resource.get('year_level', '')
            if year_level:
                if year_level not in year_groups:
                    year_groups[year_level] = []
                year_groups[year_level].append(resource)
        
        print("Resources by year level:")
        for year, resources_list in sorted(year_groups.items()):
            print(f"  {year}: {len(resources_list)} resources")
        
        # Generate bridges between consecutive years
        bridge_candidates = []
        
        # Find Y11, Y12, Y13 resources
        y11_resources = []
        y12_resources = []
        y13_resources = []
        
        for resource in resources.data:
            year_level = resource.get('year_level', '')
            quality = resource.get('quality_score', 0)
            
            if 'Y11' in year_level and quality >= 80:
                y11_resources.append(resource)
            elif 'Y12' in year_level and quality >= 80:
                y12_resources.append(resource)
            elif 'Y13' in year_level and quality >= 80:
                y13_resources.append(resource)
        
        print(f"Y11 resources: {len(y11_resources)}")
        print(f"Y12 resources: {len(y12_resources)}")
        print(f"Y13 resources: {len(y13_resources)}")
        
        # Create Y11→Y12 bridges
        for y11 in y11_resources[:5]:
            for y12 in y12_resources[:3]:
                bridge_candidates.append({
                    'source_path': y11['file_path'],
                    'target_path': y12['file_path'],
                    'relationship_type': 'prerequisite_for',
                    'confidence': 0.88,
                    'metadata': {
                        'reason': 'Y11→Y12 year progression',
                        'source_title': y11['title'],
                        'target_title': y12['title'],
                        'created_at': datetime.now().isoformat(),
                        'sprint': 'graphrag-collaborative'
                    }
                })
        
        # Create Y12→Y13 bridges
        for y12 in y12_resources[:5]:
            for y13 in y13_resources[:3]:
                bridge_candidates.append({
                    'source_path': y12['file_path'],
                    'target_path': y13['file_path'],
                    'relationship_type': 'prerequisite_for',
                    'confidence': 0.88,
                    'metadata': {
                        'reason': 'Y12→Y13 year progression',
                        'source_title': y12['title'],
                        'target_title': y13['title'],
                        'created_at': datetime.now().isoformat(),
                        'sprint': 'graphrag-collaborative'
                    }
                })
        
        print(f"Generated {len(bridge_candidates)} year bridge candidates")
        
        # Save to file
        with open('year-bridges.json', 'w') as f:
            json.dump(bridge_candidates, f, indent=2)
        
        print("✅ Saved to year-bridges.json")
        
        # Show preview
        print("\n📋 PREVIEW (first 5):")
        for i, candidate in enumerate(bridge_candidates[:5], 1):
            print(f"  {i}. {candidate['source_path']} → {candidate['target_path']}")
            print(f"     {candidate['metadata']['source_title']} → {candidate['metadata']['target_title']}")
        
        return bridge_candidates
        
    except Exception as e:
        print(f"❌ Error generating year bridges: {e}")
        return []

def main():
    """Main execution"""
    print("🎯 GRAPHRAG SPRINT INSERTS (FIXED)")
    print("=" * 70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Debug data first
    debug_data()
    
    # Generate simple links
    simple_links = generate_simple_links()
    
    # Generate year bridges
    year_bridges = generate_year_bridges()
    
    print(f"\n✅ Sprint inserts complete!")
    print(f"Generated {len(simple_links)} simple links")
    print(f"Generated {len(year_bridges)} year bridges")
    print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()

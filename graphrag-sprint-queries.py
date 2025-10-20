#!/usr/bin/env python3
"""
GraphRAG Sprint Queries - Super-hubs, Orphans, Year Bridges
Execute the GraphRAG intelligence queries for the collaborative sprint
"""

import json
from supabase import create_client
from datetime import datetime

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def run_sprint_queries():
    """Run all GraphRAG sprint queries"""
    print("🚀 GRAPHRAG SPRINT QUERIES")
    print("=" * 70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("✅ Connected to Supabase GraphRAG")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return
    
    # 1. SUPER-HUBS (>= 100 connections)
    print("\n🔗 SUPER-HUBS (>= 100 connections)")
    print("-" * 50)
    try:
        # Get all resources with relationship counts
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
        
        # Find super-hubs
        super_hubs = []
        for resource in resources.data:
            file_path = resource.get('file_path')
            connections = connection_counts.get(file_path, 0)
            if connections >= 100:
                super_hubs.append({
                    'file_path': file_path,
                    'title': resource.get('title'),
                    'subject': resource.get('subject'),
                    'quality_score': resource.get('quality_score'),
                    'connections': connections
                })
        
        super_hubs.sort(key=lambda x: x['connections'], reverse=True)
        print(f"Found {len(super_hubs)} super-hubs:")
        for i, hub in enumerate(super_hubs[:20], 1):
            print(f"  {i:2d}. {hub['title'][:60]}... ({hub['connections']} connections)")
            print(f"      Subject: {hub['subject']}, Quality: {hub['quality_score']}")
        
    except Exception as e:
        print(f"⚠️  Super-hubs query failed: {e}")
    
    # 2. ORPHANED GEMS (Q90+ with < 5 connections)
    print("\n💎 ORPHANED GEMS (Q90+ with < 5 connections)")
    print("-" * 50)
    try:
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
                    'quality_score': quality,
                    'connections': connections
                })
        
        orphans.sort(key=lambda x: (x['quality_score'], -x['connections']), reverse=True)
        print(f"Found {len(orphans)} orphaned gems:")
        for i, orphan in enumerate(orphans[:20], 1):
            print(f"  {i:2d}. {orphan['title'][:60]}... (Q{orphan['quality_score']}, {orphan['connections']} connections)")
            print(f"      Subject: {orphan['subject']}, Year: {orphan['year_level']}")
        
    except Exception as e:
        print(f"⚠️  Orphans query failed: {e}")
    
    # 3. YEAR BRIDGE COVERAGE
    print("\n🌉 YEAR BRIDGE COVERAGE")
    print("-" * 50)
    try:
        # Analyze prerequisite relationships by year level
        year_bridges = {}
        for rel in relationships.data:
            if rel.get('relationship_type') == 'prerequisite_for':
                source_year = rel.get('source_year_level')
                target_year = rel.get('target_year_level')
                if source_year and target_year and source_year != target_year:
                    bridge = f"{source_year}→{target_year}"
                    year_bridges[bridge] = year_bridges.get(bridge, 0) + 1
        
        print("Prerequisite bridges by year level:")
        for bridge, count in sorted(year_bridges.items(), key=lambda x: x[1]):
            print(f"  {bridge}: {count} bridges")
        
        # Identify weak bridges
        weak_bridges = [bridge for bridge, count in year_bridges.items() if count < 10]
        if weak_bridges:
            print(f"\n⚠️  Weak bridges (< 10 connections): {', '.join(weak_bridges)}")
        
    except Exception as e:
        print(f"⚠️  Year bridges query failed: {e}")
    
    # 4. UNDERUTILIZED RELATIONSHIP TYPES
    print("\n🔧 UNDERUTILIZED RELATIONSHIP TYPES")
    print("-" * 50)
    try:
        type_counts = {}
        for rel in relationships.data:
            rel_type = rel.get('relationship_type', 'unknown')
            type_counts[rel_type] = type_counts.get(rel_type, 0) + 1
        
        underutilized = [(t, c) for t, c in type_counts.items() if c < 10]
        underutilized.sort(key=lambda x: x[1])
        
        print(f"Found {len(underutilized)} underutilized types:")
        for rel_type, count in underutilized[:15]:
            print(f"  {rel_type}: {count} uses")
        
    except Exception as e:
        print(f"⚠️  Relationship types query failed: {e}")
    
    # 5. CULTURAL INTEGRATION BY SUBJECT
    print("\n🌿 CULTURAL INTEGRATION BY SUBJECT")
    print("-" * 50)
    try:
        subject_stats = {}
        for resource in resources.data:
            subject = resource.get('subject', 'Unknown')
            cultural = resource.get('cultural_context', False)
            
            if subject not in subject_stats:
                subject_stats[subject] = {'total': 0, 'cultural': 0}
            
            subject_stats[subject]['total'] += 1
            if cultural:
                subject_stats[subject]['cultural'] += 1
        
        print("Cultural integration by subject:")
        for subject, stats in sorted(subject_stats.items(), 
                                    key=lambda x: x[1]['cultural']/x[1]['total'] if x[1]['total'] > 0 else 0, 
                                    reverse=True):
            total = stats['total']
            cultural = stats['cultural']
            percentage = (cultural / total * 100) if total > 0 else 0
            print(f"  {subject}: {cultural}/{total} ({percentage:.1f}%)")
        
    except Exception as e:
        print(f"⚠️  Cultural integration query failed: {e}")
    
    # 6. SUMMARY AND RECOMMENDATIONS
    print("\n📊 SPRINT SUMMARY & RECOMMENDATIONS")
    print("=" * 70)
    
    try:
        total_resources = len(resources.data)
        total_relationships = len(relationships.data)
        
        print(f"Platform Stats:")
        print(f"  Total Resources: {total_resources:,}")
        print(f"  Total Relationships: {total_relationships:,}")
        print(f"  Super-hubs: {len(super_hubs)}")
        print(f"  Orphaned gems: {len(orphans)}")
        
        print(f"\n🎯 HIGH-IMPACT ACTIONS:")
        print(f"  1. Link {min(20, len(orphans))} orphans to super-hubs")
        print(f"  2. Build Y11→Y13 prerequisite bridges")
        print(f"  3. Scale {len(underutilized)} underutilized relationship types")
        print(f"  4. Cultural enrichment for weak subjects")
        
    except Exception as e:
        print(f"⚠️  Summary failed: {e}")
    
    print(f"\n✅ Sprint queries complete!")
    print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    run_sprint_queries()

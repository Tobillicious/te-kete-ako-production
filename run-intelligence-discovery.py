#!/usr/bin/env python3
"""
INTELLIGENCE DISCOVERY EXECUTION
Run the intelligence tools we built to discover platform insights
"""

import sys
import os
import json
from datetime import datetime
from supabase import create_client

# Add scripts directory to path
sys.path.append('/Users/admin/Documents/te-kete-ako-clean/scripts')

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def main():
    print("🚀 INTELLIGENCE DISCOVERY EXECUTION")
    print("=" * 70)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Bypassing terminal hanging issue...")
    print()
    
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # ================================================================
    # DISCOVERY 1: PLATFORM STATE ANALYSIS
    # ================================================================
    
    print("📊 DISCOVERY 1: PLATFORM STATE ANALYSIS")
    print("-" * 50)
    
    try:
        # Query platform stats
        resources_response = supabase.table('graphrag_resources').select('*', count='exact').execute()
        total_resources = resources_response.count if hasattr(resources_response, 'count') else len(resources_response.data)
        
        relationships_response = supabase.table('graphrag_relationships').select('*', count='exact').execute()
        total_relationships = relationships_response.count if hasattr(relationships_response, 'count') else len(relationships_response.data)
        
        # Cultural integration analysis
        cultural_response = supabase.table('graphrag_resources')\
            .select('cultural_context')\
            .eq('cultural_context', True)\
            .execute()
        cultural_count = len(cultural_response.data) if cultural_response.data else 0
        
        # Quality analysis
        quality_response = supabase.table('graphrag_resources')\
            .select('quality_score')\
            .gte('quality_score', 90)\
            .execute()
        excellence_count = len(quality_response.data) if quality_response.data else 0
        
        platform_stats = {
            'total_resources': total_resources,
            'total_relationships': total_relationships,
            'cultural_integration': cultural_count,
            'excellence_resources': excellence_count,
            'cultural_percentage': round((cultural_count / total_resources * 100), 2) if total_resources > 0 else 0,
            'excellence_percentage': round((excellence_count / total_resources * 100), 2) if total_resources > 0 else 0,
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"✅ Total Resources: {total_resources:,}")
        print(f"✅ Total Relationships: {total_relationships:,}")
        print(f"✅ Cultural Integration: {cultural_count:,} ({platform_stats['cultural_percentage']}%)")
        print(f"✅ Excellence Resources: {excellence_count:,} ({platform_stats['excellence_percentage']}%)")
        
        # Save platform stats
        with open('/Users/admin/Documents/te-kete-ako-clean/platform-discovery-stats.json', 'w') as f:
            json.dump(platform_stats, f, indent=2)
        
        print("✅ Platform stats saved: platform-discovery-stats.json")
        
    except Exception as e:
        print(f"❌ Error in platform analysis: {e}")
    
    print()
    
    # ================================================================
    # DISCOVERY 2: ORPHANED EXCELLENCE ANALYSIS
    # ================================================================
    
    print("💎 DISCOVERY 2: ORPHANED EXCELLENCE ANALYSIS")
    print("-" * 50)
    
    try:
        # Find high-quality resources
        excellence_resources = supabase.table('graphrag_resources')\
            .select('file_path, title, quality_score')\
            .gte('quality_score', 90)\
            .execute()
        
        orphans = []
        for resource in excellence_resources.data:
            # Check connection count
            connections = supabase.table('graphrag_relationships')\
                .select('id')\
                .or_(f'source_path.eq.{resource["file_path"]},target_path.eq.{resource["file_path"]}')\
                .execute()
            
            connection_count = len(connections.data) if connections.data else 0
            
            if connection_count < 5:  # Consider orphaned if <5 connections
                orphans.append({
                    'file_path': resource['file_path'],
                    'title': resource['title'],
                    'quality_score': resource['quality_score'],
                    'connection_count': connection_count
                })
        
        orphan_analysis = {
            'total_excellence': len(excellence_resources.data),
            'orphans_found': len(orphans),
            'orphan_percentage': round((len(orphans) / len(excellence_resources.data) * 100), 2) if excellence_resources.data else 0,
            'orphans': orphans,
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"✅ Excellence Resources: {len(excellence_resources.data):,}")
        print(f"✅ Orphans Found: {len(orphans):,} ({orphan_analysis['orphan_percentage']}%)")
        
        if orphans:
            print("🔍 Top 5 Orphans:")
            for i, orphan in enumerate(orphans[:5]):
                print(f"   {i+1}. {orphan['title']} (Q{orphan['quality_score']}, {orphan['connection_count']} connections)")
        
        # Save orphan analysis
        with open('/Users/admin/Documents/te-kete-ako-clean/orphan-discovery-analysis.json', 'w') as f:
            json.dump(orphan_analysis, f, indent=2)
        
        print("✅ Orphan analysis saved: orphan-discovery-analysis.json")
        
    except Exception as e:
        print(f"❌ Error in orphan analysis: {e}")
    
    print()
    
    # ================================================================
    # DISCOVERY 3: RELATIONSHIP TYPE ANALYSIS
    # ================================================================
    
    print("⛏️  DISCOVERY 3: RELATIONSHIP TYPE ANALYSIS")
    print("-" * 50)
    
    try:
        # Get all relationship types and their usage
        relationships = supabase.table('graphrag_relationships')\
            .select('relationship_type')\
            .execute()
        
        type_counts = {}
        for rel in relationships.data:
            rel_type = rel['relationship_type']
            type_counts[rel_type] = type_counts.get(rel_type, 0) + 1
        
        # Sort by usage
        sorted_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
        
        # Find underutilized types (used <50 times)
        underutilized = [(t, c) for t, c in sorted_types if c < 50]
        
        relationship_analysis = {
            'total_relationship_types': len(type_counts),
            'total_relationships': len(relationships.data),
            'underutilized_types': len(underutilized),
            'top_10_types': sorted_types[:10],
            'underutilized_list': underutilized,
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"✅ Total Relationship Types: {len(type_counts)}")
        print(f"✅ Total Relationships: {len(relationships.data):,}")
        print(f"✅ Underutilized Types: {len(underutilized)}")
        
        print("🔍 Top 10 Relationship Types:")
        for i, (rel_type, count) in enumerate(sorted_types[:10]):
            print(f"   {i+1}. {rel_type}: {count:,} uses")
        
        if underutilized:
            print("🔍 Underutilized Types (<50 uses):")
            for rel_type, count in underutilized[:10]:
                print(f"   - {rel_type}: {count} uses")
        
        # Save relationship analysis
        with open('/Users/admin/Documents/te-kete-ako-clean/relationship-discovery-analysis.json', 'w') as f:
            json.dump(relationship_analysis, f, indent=2)
        
        print("✅ Relationship analysis saved: relationship-discovery-analysis.json")
        
    except Exception as e:
        print(f"❌ Error in relationship analysis: {e}")
    
    print()
    
    # ================================================================
    # DISCOVERY 4: CULTURAL INTEGRATION ANALYSIS
    # ================================================================
    
    print("🌿 DISCOVERY 4: CULTURAL INTEGRATION ANALYSIS")
    print("-" * 50)
    
    try:
        # Analyze cultural integration by subject
        subjects = ['Mathematics', 'Science', 'English', 'Social Studies', 'Digital Technologies', 'History']
        cultural_by_subject = {}
        
        for subject in subjects:
            # Get resources for this subject
            subject_resources = supabase.table('graphrag_resources')\
                .select('cultural_context')\
                .ilike('subject', f'%{subject}%')\
                .execute()
            
            if subject_resources.data:
                total_subject = len(subject_resources.data)
                cultural_subject = len([r for r in subject_resources.data if r.get('cultural_context')])
                cultural_percentage = round((cultural_subject / total_subject * 100), 2)
                
                cultural_by_subject[subject] = {
                    'total_resources': total_subject,
                    'cultural_resources': cultural_subject,
                    'cultural_percentage': cultural_percentage
                }
        
        cultural_analysis = {
            'by_subject': cultural_by_subject,
            'overall_cultural': platform_stats.get('cultural_percentage', 0),
            'timestamp': datetime.now().isoformat()
        }
        
        print("🌿 Cultural Integration by Subject:")
        for subject, data in cultural_by_subject.items():
            print(f"   {subject}: {data['cultural_percentage']}% ({data['cultural_resources']}/{data['total_resources']})")
        
        # Save cultural analysis
        with open('/Users/admin/Documents/te-kete-ako-clean/cultural-discovery-analysis.json', 'w') as f:
            json.dump(cultural_analysis, f, indent=2)
        
        print("✅ Cultural analysis saved: cultural-discovery-analysis.json")
        
    except Exception as e:
        print(f"❌ Error in cultural analysis: {e}")
    
    print()
    
    # ================================================================
    # SUMMARY
    # ================================================================
    
    print("🎉 INTELLIGENCE DISCOVERY COMPLETE!")
    print("=" * 70)
    print("Files generated:")
    print("- platform-discovery-stats.json")
    print("- orphan-discovery-analysis.json") 
    print("- relationship-discovery-analysis.json")
    print("- cultural-discovery-analysis.json")
    print()
    print("Next steps:")
    print("1. Review generated files for insights")
    print("2. Plan next evolution based on discoveries")
    print("3. Execute intelligence tools based on findings")
    print()

if __name__ == "__main__":
    main()

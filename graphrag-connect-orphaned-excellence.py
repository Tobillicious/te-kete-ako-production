#!/usr/bin/env python3
"""
🌟 GraphRAG Orphaned Excellence Connector
Finds high-quality, low-connection resources and builds intelligent relationships

Priority: Connect Q90+ resources with <10 connections
Method: Semantic analysis, cultural threading, subject matching
"""

import os
import sys
from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def init_supabase():
    """Initialize Supabase client"""
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def find_orphaned_excellence(supabase: Client, min_quality=90, max_connections=10):
    """Find high-quality resources with few connections"""
    print(f"🔍 Finding resources with Q{min_quality}+ and <{max_connections} connections...")
    
    # Get all high-quality resources
    response = supabase.table('graphrag_resources')\
        .select('file_path, title, resource_type, subject, year_level, quality_score, cultural_context, has_whakataukī, has_te_reo')\
        .gte('quality_score', min_quality)\
        .execute()
    
    high_quality = response.data
    print(f"   Found {len(high_quality)} high-quality resources")
    
    # Count connections for each
    orphaned = []
    for resource in high_quality:
        path = resource['file_path']
        
        # Count relationships
        rel_response = supabase.table('graphrag_relationships')\
            .select('id', count='exact')\
            .or_(f'source_path.eq.{path},target_path.eq.{path}')\
            .execute()
        
        connection_count = rel_response.count or 0
        
        if connection_count < max_connections:
            resource['connection_count'] = connection_count
            orphaned.append(resource)
    
    print(f"   ⭐ Found {len(orphaned)} orphaned excellence resources!")
    return orphaned

def analyze_resource_for_connections(resource):
    """Analyze a resource to determine what it should connect to"""
    connections_to_build = []
    path = resource['file_path']
    
    # 1. CSS files should connect to pages that use them
    if resource['resource_type'] == 'Stylesheet':
        if 'cultural-pattern' in path:
            connections_to_build.append({
                'type': 'pattern',
                'targets': ['pages with cultural elements', 'lessons with Te Ao Māori'],
                'relationship_type': 'styles_cultural_content'
            })
        elif 'te-kete-professional' in path or 'ultimate-beauty' in path:
            connections_to_build.append({
                'type': 'global',
                'targets': ['all pages', 'design system components'],
                'relationship_type': 'global_stylesheet'
            })
    
    # 2. JavaScript files should connect to pages that use them
    if resource['resource_type'] == 'JavaScript' or '.js' in path:
        filename = path.split('/')[-1]
        if 'intelligence' in filename or 'graphrag' in filename or 'ai' in filename:
            connections_to_build.append({
                'type': 'intelligence',
                'targets': ['interactive pages', 'dashboard pages', 'search interfaces'],
                'relationship_type': 'powers_intelligence'
            })
        elif 'cultural' in filename:
            connections_to_build.append({
                'type': 'cultural',
                'targets': ['cultural content pages', 'lessons with Te Ao Māori'],
                'relationship_type': 'enhances_cultural_experience'
            })
    
    # 3. Tool/Dashboard pages should connect to related content
    if resource['resource_type'] in ['Tool', 'Dashboard', 'Feature Hub']:
        if 'teacher' in path.lower():
            connections_to_build.append({
                'type': 'professional',
                'targets': ['teacher resources', 'professional development', 'planning tools'],
                'relationship_type': 'supports_professional_practice'
            })
    
    # 4. Cultural resources should connect to curriculum
    if resource.get('cultural_context') or resource.get('has_whakataukī'):
        subject = resource.get('subject', 'General')
        connections_to_build.append({
            'type': 'cultural_curriculum',
            'targets': [f'{subject} lessons', 'cross-curricular units', 'cultural competence resources'],
            'relationship_type': 'cultural_enhancement'
        })
    
    return connections_to_build

def build_smart_connections(supabase: Client, orphaned_resource, dry_run=True):
    """Build intelligent connections for an orphaned resource"""
    analysis = analyze_resource_for_connections(orphaned_resource)
    relationships_created = []
    
    for connection_type in analysis:
        print(f"\n   Building {connection_type['type']} connections for: {orphaned_resource['title']}")
        
        # Find target resources based on analysis
        targets = find_target_resources(supabase, connection_type, orphaned_resource)
        
        for target in targets[:5]:  # Limit to 5 connections per type
            relationship = {
                'source_path': orphaned_resource['file_path'],
                'target_path': target['file_path'],
                'relationship_type': connection_type['relationship_type'],
                'confidence': 0.85,  # High confidence for manually analyzed connections
                'metadata': {
                    'created_by': 'orphaned_excellence_connector',
                    'analysis_type': connection_type['type'],
                    'source_quality': orphaned_resource['quality_score'],
                    'target_quality': target.get('quality_score', 0)
                }
            }
            
            if not dry_run:
                # Insert into database
                supabase.table('graphrag_relationships').insert(relationship).execute()
                print(f"      ✅ Connected to: {target['title']}")
            else:
                print(f"      🔗 Would connect to: {target['title']}")
            
            relationships_created.append(relationship)
    
    return relationships_created

def find_target_resources(supabase: Client, connection_type, source_resource):
    """Find target resources for a given connection type"""
    targets = []
    
    # Different query strategies based on connection type
    if connection_type['type'] == 'cultural':
        # Find cultural content in the same or related subjects
        response = supabase.table('graphrag_resources')\
            .select('file_path, title, resource_type, quality_score')\
            .eq('cultural_context', True)\
            .neq('file_path', source_resource['file_path'])\
            .limit(10)\
            .execute()
        targets = response.data
    
    elif connection_type['type'] == 'intelligence':
        # Find interactive and dashboard pages
        response = supabase.table('graphrag_resources')\
            .select('file_path, title, resource_type, quality_score')\
            .in_('resource_type', ['Interactive', 'Dashboard', 'Tool', 'Page'])\
            .neq('file_path', source_resource['file_path'])\
            .limit(10)\
            .execute()
        targets = response.data
    
    elif connection_type['type'] == 'professional':
        # Find teacher-related resources
        response = supabase.table('graphrag_resources')\
            .select('file_path, title, resource_type, quality_score')\
            .or_('file_path.ilike.%teacher%,file_path.ilike.%professional%')\
            .neq('file_path', source_resource['file_path'])\
            .limit(10)\
            .execute()
        targets = response.data
    
    elif connection_type['type'] == 'pattern' or connection_type['type'] == 'global':
        # Find high-quality pages
        response = supabase.table('graphrag_resources')\
            .select('file_path, title, resource_type, quality_score')\
            .in_('resource_type', ['Page', 'Lesson', 'Unit-Plan'])\
            .gte('quality_score', 85)\
            .neq('file_path', source_resource['file_path'])\
            .limit(15)\
            .execute()
        targets = response.data
    
    return targets

def main():
    """Main execution"""
    print("🌟 GraphRAG Orphaned Excellence Connector")
    print("=" * 70)
    
    # Check for dry-run flag
    dry_run = '--dry-run' in sys.argv or len(sys.argv) == 1
    
    if dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
        print("   Run with --execute to actually create relationships\n")
    else:
        print("⚡ EXECUTE MODE - Will create relationships in database\n")
    
    # Initialize
    supabase = init_supabase()
    
    # Find orphaned excellence
    orphaned = find_orphaned_excellence(supabase, min_quality=95, max_connections=5)
    
    if not orphaned:
        print("\n✅ No orphaned excellence found! All high-quality resources are well-connected.")
        return
    
    # Analyze and show top candidates
    print(f"\n📊 TOP ORPHANED EXCELLENCE CANDIDATES:\n")
    for i, resource in enumerate(orphaned[:10], 1):
        print(f"{i}. {resource['title']}")
        print(f"   Quality: {resource['quality_score']} | Connections: {resource['connection_count']}")
        print(f"   Path: {resource['file_path']}")
        print()
    
    # Build connections for top 5
    print("\n🔧 BUILDING CONNECTIONS FOR TOP 5...\n")
    total_created = 0
    
    for resource in orphaned[:5]:
        print(f"━" * 70)
        print(f"🎯 {resource['title']}")
        relationships = build_smart_connections(supabase, resource, dry_run=dry_run)
        total_created += len(relationships)
    
    print(f"\n" + "=" * 70)
    if dry_run:
        print(f"✅ ANALYSIS COMPLETE")
        print(f"   Would create {total_created} new relationships")
        print(f"\n   Run with --execute to apply changes")
    else:
        print(f"✅ SUCCESS!")
        print(f"   Created {total_created} new high-quality relationships")
        print(f"   GraphRAG is now more connected! 🎉")

if __name__ == "__main__":
    main()


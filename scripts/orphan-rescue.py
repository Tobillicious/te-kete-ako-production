#!/usr/bin/env python3
"""
💎 ORPHAN RESCUE - Connect high-quality isolated resources

Finds Q90+ resources with <5 connections and suggests/creates relationships
to integrate them into learning pathways

Usage: python3 scripts/orphan-rescue.py [--dry-run] [--auto]
"""

import sys
import json
from datetime import datetime
from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def initialize_supabase() -> Client:
    """Initialize Supabase client"""
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def find_orphaned_gems(supabase: Client, min_quality: int = 90, max_connections: int = 5) -> list:
    """Find high-quality resources with few connections"""
    print(f"💎 Finding orphaned gems (Q{min_quality}+ with ≤{max_connections} connections)...\n")
    
    try:
        # Get high-quality resources
        high_quality = supabase.table('graphrag_resources')\
            .select('*')\
            .gte('quality_score', min_quality)\
            .execute()
        
        if not high_quality.data:
            print("⚠️  No high-quality resources found")
            return []
        
        print(f"   Found {len(high_quality.data)} Q{min_quality}+ resources")
        
        # Get all relationships
        relationships = supabase.table('graphrag_relationships')\
            .select('source_path, target_path')\
            .execute()
        
        # Count connections per resource
        connection_counts = {}
        for rel in relationships.data:
            source = rel.get('source_path')
            target = rel.get('target_path')
            
            if source:
                connection_counts[source] = connection_counts.get(source, 0) + 1
            if target:
                connection_counts[target] = connection_counts.get(target, 0) + 1
        
        # Find orphans
        orphans = []
        for resource in high_quality.data:
            path = resource.get('file_path')
            connections = connection_counts.get(path, 0)
            
            if connections <= max_connections:
                resource['connections'] = connections
                orphans.append(resource)
        
        orphans.sort(key=lambda x: (x.get('quality_score', 0), -x.get('connections', 0)), reverse=True)
        
        print(f"   ✅ Found {len(orphans)} orphaned gems!\n")
        return orphans
    
    except Exception as e:
        print(f"❌ Error finding orphans: {e}")
        return []

def find_similar_resources(supabase: Client, orphan: dict, limit: int = 10) -> list:
    """Find resources similar to the orphan (same subject, nearby year level)"""
    try:
        subject = orphan.get('subject')
        year_level = orphan.get('year_level')
        
        query = supabase.table('graphrag_resources').select('*')
        
        # Match subject
        if subject:
            query = query.eq('subject', subject)
        
        # Get resources
        result = query.limit(100).execute()
        
        if not result.data:
            return []
        
        # Score by similarity
        similar = []
        for resource in result.data:
            # Don't match self
            if resource['file_path'] == orphan['file_path']:
                continue
            
            score = 0.0
            
            # Subject match (already filtered)
            if resource.get('subject') == subject:
                score += 0.4
            
            # Year level proximity
            if year_level and resource.get('year_level'):
                try:
                    year_diff = abs(int(year_level) - int(resource['year_level']))
                    if year_diff == 0:
                        score += 0.3
                    elif year_diff == 1:
                        score += 0.2
                    elif year_diff == 2:
                        score += 0.1
                except:
                    pass
            
            # Cultural match
            if orphan.get('cultural_context') and resource.get('cultural_context'):
                score += 0.2
            
            # Quality match
            if resource.get('quality_score', 0) >= 85:
                score += 0.1
            
            if score > 0.3:
                resource['similarity_score'] = score
                similar.append(resource)
        
        similar.sort(key=lambda x: x['similarity_score'], reverse=True)
        return similar[:limit]
    
    except Exception as e:
        print(f"⚠️  Error finding similar resources: {e}")
        return []

def suggest_relationships(supabase: Client, orphan: dict, similar: list) -> list:
    """Suggest relationship types based on resource characteristics"""
    suggestions = []
    
    orphan_type = orphan.get('resource_type', 'unknown')
    orphan_year = orphan.get('year_level')
    
    for similar_res in similar:
        similar_type = similar_res.get('resource_type', 'unknown')
        similar_year = similar_res.get('year_level')
        
        # Determine relationship type
        rel_type = 'related_content'
        confidence = similar_res['similarity_score']
        reasoning = f"Similar {orphan.get('subject')} content"
        
        # Prerequisite relationship
        if orphan_year and similar_year:
            try:
                if int(similar_year) > int(orphan_year):
                    rel_type = 'prerequisite_for'
                    confidence += 0.05
                    reasoning = f"Y{orphan_year} prerequisite for Y{similar_year} content"
                elif int(similar_year) < int(orphan_year):
                    rel_type = 'prerequisite_for'
                    confidence += 0.05
                    reasoning = f"Y{similar_year} prerequisite for Y{orphan_year} content"
                    # Swap direction
                    orphan, similar_res = similar_res, orphan
            except:
                pass
        
        # Cultural wisdom thread
        if orphan.get('cultural_context') and similar_res.get('cultural_context'):
            rel_type = 'shared_cultural_wisdom'
            confidence += 0.05
            reasoning = f"Shared cultural context in {orphan.get('subject')}"
        
        # Support relationship
        if orphan_type == 'handout' and similar_type == 'lesson':
            rel_type = 'supports_learning_in'
            confidence += 0.05
            reasoning = f"Handout supports {similar_res.get('title', 'lesson')}"
        elif orphan_type == 'lesson' and similar_type == 'handout':
            rel_type = 'lesson_has_handout'
            confidence += 0.05
            reasoning = f"Lesson enhanced by handout"
        
        suggestions.append({
            'source_path': orphan['file_path'],
            'source_title': orphan.get('title', 'Unknown'),
            'target_path': similar_res['file_path'],
            'target_title': similar_res.get('title', 'Unknown'),
            'relationship_type': rel_type,
            'confidence': round(min(confidence, 0.95), 3),
            'reasoning': reasoning
        })
    
    return suggestions

def display_rescue_opportunities(orphans: list, supabase: Client, limit: int = 5):
    """Display rescue opportunities for orphaned resources"""
    print("=" * 70)
    print("🚨 ORPHAN RESCUE OPPORTUNITIES")
    print("=" * 70 + "\n")
    
    for i, orphan in enumerate(orphans[:limit], 1):
        print(f"{i}. {orphan.get('title', 'Unknown')}")
        print(f"   Quality: {orphan.get('quality_score', '?')}/100")
        print(f"   Connections: {orphan.get('connections', 0)}")
        print(f"   Subject: {orphan.get('subject', 'Unknown')}")
        print(f"   Year: {orphan.get('year_level', 'Unknown')}")
        print(f"   Path: {orphan.get('file_path', '')}")
        
        # Find similar resources
        similar = find_similar_resources(supabase, orphan, limit=5)
        
        if similar:
            print(f"\n   💡 Suggested connections:")
            suggestions = suggest_relationships(supabase, orphan, similar)
            
            for j, suggestion in enumerate(suggestions[:3], 1):
                print(f"      {j}. {suggestion['relationship_type']} → {suggestion['target_title'][:50]}")
                print(f"         Confidence: {suggestion['confidence']:.2f}")
                print(f"         Reasoning: {suggestion['reasoning']}")
        else:
            print(f"\n   ⚠️  No similar resources found for automatic rescue")
        
        print()
    
    if len(orphans) > limit:
        print(f"... and {len(orphans) - limit} more orphaned gems\n")

def rescue_orphans(supabase: Client, orphans: list, auto: bool = False, dry_run: bool = False) -> int:
    """Create rescue relationships for orphaned resources"""
    if dry_run:
        print("🔍 DRY RUN: Showing rescue plan without creating relationships\n")
    
    rescued = 0
    total_connections = 0
    
    for orphan in orphans:
        print(f"\n🔗 Rescuing: {orphan.get('title', 'Unknown')}...")
        
        # Find similar resources
        similar = find_similar_resources(supabase, orphan, limit=5)
        
        if not similar:
            print(f"   ⚠️  No rescue candidates found")
            continue
        
        # Get relationship suggestions
        suggestions = suggest_relationships(supabase, orphan, similar)
        
        if not suggestions:
            print(f"   ⚠️  No relationships could be suggested")
            continue
        
        # Create relationships
        for suggestion in suggestions[:3]:  # Top 3 suggestions
            if dry_run:
                print(f"   Would create: {suggestion['relationship_type']}")
                print(f"      → {suggestion['target_title'][:50]}")
                print(f"      Confidence: {suggestion['confidence']:.2f}")
                total_connections += 1
            else:
                try:
                    supabase.table('graphrag_relationships').insert({
                        'source_path': suggestion['source_path'],
                        'target_path': suggestion['target_path'],
                        'relationship_type': suggestion['relationship_type'],
                        'confidence': suggestion['confidence'],
                        'reasoning': suggestion['reasoning'],
                        'created_at': datetime.now().isoformat()
                    }).execute()
                    
                    print(f"   ✅ Created: {suggestion['relationship_type']}")
                    print(f"      → {suggestion['target_title'][:50]}")
                    total_connections += 1
                
                except Exception as e:
                    print(f"   ⚠️  Error creating relationship: {e}")
        
        if not dry_run and total_connections > 0:
            rescued += 1
    
    return rescued, total_connections

def main():
    """Main execution"""
    print("\n" + "="*70)
    print("💎 ORPHAN RESCUE")
    print("   Connect high-quality isolated resources to learning pathways")
    print("="*70 + "\n")
    
    # Parse arguments
    dry_run = '--dry-run' in sys.argv
    auto = '--auto' in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN MODE: No changes will be made\n")
    
    supabase = initialize_supabase()
    
    # Find orphaned gems
    orphans = find_orphaned_gems(supabase)
    
    if not orphans:
        print("✅ No orphaned gems found! All high-quality resources are well-connected.\n")
        return 0
    
    # Display opportunities
    display_rescue_opportunities(orphans, supabase, limit=10)
    
    # Rescue orphans
    if auto or not dry_run:
        print("=" * 70)
        print("🚀 STARTING RESCUE OPERATIONS")
        print("=" * 70)
        
        rescued, total_connections = rescue_orphans(supabase, orphans, auto, dry_run)
        
        print("\n" + "=" * 70)
        print("📊 RESCUE SUMMARY")
        print("=" * 70)
        print(f"Orphans found: {len(orphans)}")
        print(f"Orphans rescued: {rescued}")
        print(f"Connections created: {total_connections}")
        print(f"Average connections per orphan: {total_connections / rescued if rescued > 0 else 0:.1f}")
        print("=" * 70 + "\n")
        
        if dry_run:
            print("💡 Run without --dry-run to actually create relationships\n")
        else:
            print("🎊 Orphan rescue complete!")
            print("💎 High-quality resources are now discoverable!\n")
    else:
        print("\n💡 Run with --auto flag to create rescue relationships\n")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())


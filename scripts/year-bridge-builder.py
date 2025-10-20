#!/usr/bin/env python3
"""
🌉 YEAR BRIDGE BUILDER
Build prerequisite connections between year levels for clear progressions

Critical gaps: Y7→Y8, Y9→Y10, Y11→Y12, Y12→Y13
Goal: Enable students to follow learning progressions through school

Usage: python3 scripts/year-bridge-builder.py [--dry-run] [--bridge Y11-Y12]
"""

import sys
import json
from datetime import datetime
from collections import defaultdict
from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

# Critical year bridges to build
CRITICAL_BRIDGES = [
    ('7', '8', 'Y7→Y8 Foundation'),
    ('8', '9', 'Y8→Y9 Development'),
    ('9', '10', 'Y9→Y10 Application'),
    ('10', '11', 'Y10→Y11 NCEA Level 1 Prep'),
    ('11', '12', 'Y11→Y12 NCEA L1→L2'),
    ('12', '13', 'Y12→Y13 NCEA L2→L3')
]

# Pedagogical progression frameworks
PROGRESSION_FRAMEWORKS = {
    'Science': {
        'concepts': ['observation', 'investigation', 'analysis', 'synthesis', 'critique'],
        'keywords': ['scientific method', 'hypothesis', 'experiment', 'data', 'conclusion']
    },
    'Mathematics': {
        'concepts': ['computation', 'problem solving', 'reasoning', 'proof', 'application'],
        'keywords': ['calculate', 'solve', 'prove', 'apply', 'model']
    },
    'English': {
        'concepts': ['comprehension', 'analysis', 'interpretation', 'evaluation', 'creation'],
        'keywords': ['read', 'analyze', 'interpret', 'evaluate', 'write']
    },
    'Social Studies': {
        'concepts': ['understanding', 'analysis', 'critique', 'synthesis', 'action'],
        'keywords': ['history', 'society', 'culture', 'change', 'impact']
    },
    'Digital Technologies': {
        'concepts': ['understanding', 'application', 'design', 'development', 'evaluation'],
        'keywords': ['digital', 'technology', 'code', 'design', 'create']
    }
}

def initialize_supabase() -> Client:
    """Initialize Supabase client"""
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def analyze_year_bridges(supabase: Client) -> dict:
    """Analyze current state of year-level bridges"""
    print("🔍 Analyzing year-level prerequisite bridges...\n")
    
    try:
        # Get all prerequisite relationships
        prerequisites = supabase.table('graphrag_relationships')\
            .select('*')\
            .eq('relationship_type', 'prerequisite_for')\
            .execute()
        
        if not prerequisites.data:
            print("⚠️  No prerequisite relationships found")
            return {}
        
        # Get resources to map paths to year levels
        resources = supabase.table('graphrag_resources')\
            .select('file_path, year_level, subject')\
            .execute()
        
        path_to_year = {}
        path_to_subject = {}
        for res in resources.data:
            if res.get('file_path'):
                path_to_year[res['file_path']] = res.get('year_level')
                path_to_subject[res['file_path']] = res.get('subject')
        
        # Count bridges
        bridge_counts = defaultdict(int)
        bridge_subjects = defaultdict(lambda: defaultdict(int))
        
        for rel in prerequisites.data:
            source_year = path_to_year.get(rel['source_path'])
            target_year = path_to_year.get(rel['target_path'])
            subject = path_to_subject.get(rel['source_path'])
            
            if source_year and target_year and source_year != target_year:
                bridge = f"Y{source_year}→Y{target_year}"
                bridge_counts[bridge] += 1
                if subject:
                    bridge_subjects[bridge][subject] += 1
        
        # Display results
        print("📊 Current Year Bridge Status:")
        print("-" * 70)
        
        for source, target, description in CRITICAL_BRIDGES:
            bridge_key = f"Y{source}→Y{target}"
            count = bridge_counts.get(bridge_key, 0)
            status = "✅" if count >= 10 else "⚠️" if count >= 5 else "🔴"
            
            print(f"{status} {bridge_key}: {count} bridges - {description}")
            
            if count > 0 and bridge_key in bridge_subjects:
                subjects = bridge_subjects[bridge_key]
                top_subjects = sorted(subjects.items(), key=lambda x: x[1], reverse=True)[:3]
                print(f"   Top subjects: {', '.join([f'{subj} ({cnt})' for subj, cnt in top_subjects])}")
        
        print()
        return dict(bridge_counts)
    
    except Exception as e:
        print(f"❌ Error analyzing bridges: {e}")
        return {}

def find_bridge_candidates(supabase: Client, source_year: str, target_year: str) -> list:
    """Find candidate resource pairs for a year bridge"""
    print(f"\n🔎 Finding candidates for Y{source_year}→Y{target_year} bridge...")
    
    try:
        # Get resources for source year
        source_resources = supabase.table('graphrag_resources')\
            .select('*')\
            .eq('year_level', source_year)\
            .gte('quality_score', 80)\
            .execute()
        
        # Get resources for target year
        target_resources = supabase.table('graphrag_resources')\
            .select('*')\
            .eq('year_level', target_year)\
            .gte('quality_score', 80)\
            .execute()
        
        if not source_resources.data or not target_resources.data:
            print(f"   ⚠️  Insufficient resources (source: {len(source_resources.data)}, target: {len(target_resources.data)})")
            return []
        
        print(f"   Found {len(source_resources.data)} Y{source_year} resources")
        print(f"   Found {len(target_resources.data)} Y{target_year} resources")
        
        # Group by subject
        candidates = []
        
        for source_res in source_resources.data:
            subject = source_res.get('subject')
            if not subject:
                continue
            
            # Find target resources in same subject
            matching_targets = [r for r in target_resources.data if r.get('subject') == subject]
            
            for target_res in matching_targets:
                # Calculate match confidence
                confidence = calculate_bridge_confidence(source_res, target_res, source_year, target_year)
                
                if confidence >= 0.80:
                    candidates.append({
                        'source': source_res,
                        'target': target_res,
                        'confidence': confidence,
                        'subject': subject
                    })
        
        candidates.sort(key=lambda x: x['confidence'], reverse=True)
        print(f"   ✅ Found {len(candidates)} high-confidence bridge opportunities")
        
        return candidates
    
    except Exception as e:
        print(f"❌ Error finding candidates: {e}")
        return []

def calculate_bridge_confidence(source: dict, target: dict, source_year: str, target_year: str) -> float:
    """Calculate confidence for a year bridge relationship"""
    confidence = 0.70  # Base confidence for same subject, adjacent years
    
    subject = source.get('subject')
    
    # Year adjacency bonus
    try:
        year_diff = abs(int(target_year) - int(source_year))
        if year_diff == 1:
            confidence += 0.10  # Adjacent years
        elif year_diff == 2:
            confidence += 0.05  # Near years
    except:
        pass
    
    # Quality bonus
    source_quality = source.get('quality_score', 0)
    target_quality = target.get('quality_score', 0)
    if source_quality >= 90 and target_quality >= 90:
        confidence += 0.08
    elif source_quality >= 85 and target_quality >= 85:
        confidence += 0.05
    
    # Cultural alignment bonus
    if source.get('cultural_context') and target.get('cultural_context'):
        confidence += 0.05
    
    # Content similarity (basic check)
    source_title = (source.get('title', '') + ' ' + source.get('description', '')).lower()
    target_title = (target.get('title', '') + ' ' + target.get('description', '')).lower()
    
    # Check for progression keywords
    if subject in PROGRESSION_FRAMEWORKS:
        keywords = PROGRESSION_FRAMEWORKS[subject]['keywords']
        source_keywords = sum(1 for kw in keywords if kw in source_title)
        target_keywords = sum(1 for kw in keywords if kw in target_title)
        
        if source_keywords > 0 and target_keywords > 0:
            confidence += 0.05
    
    # NCEA progression (Y10→Y11, Y11→Y12, Y12→Y13)
    try:
        source_yr = int(source_year)
        target_yr = int(target_year)
        if (source_yr == 10 and target_yr == 11) or \
           (source_yr == 11 and target_yr == 12) or \
           (source_yr == 12 and target_yr == 13):
            confidence += 0.08  # NCEA progression bonus
    except:
        pass
    
    return min(confidence, 0.98)  # Cap at 0.98

def build_bridges(supabase: Client, source_year: str, target_year: str, candidates: list, dry_run: bool = False) -> int:
    """Build prerequisite bridges between year levels"""
    if dry_run:
        print(f"\n🔍 DRY RUN: Would create {len(candidates)} bridges")
        for i, candidate in enumerate(candidates[:5], 1):
            print(f"\n{i}. {candidate['subject']}")
            print(f"   Y{source_year}: {candidate['source'].get('title', 'Unknown')}")
            print(f"   Y{target_year}: {candidate['target'].get('title', 'Unknown')}")
            print(f"   Confidence: {candidate['confidence']:.2f}")
        if len(candidates) > 5:
            print(f"\n   ... and {len(candidates) - 5} more")
        return 0
    
    print(f"\n🌉 Building Y{source_year}→Y{target_year} bridges...")
    
    created = 0
    
    for candidate in candidates[:20]:  # Limit to top 20 per bridge
        try:
            reasoning = f"Year {source_year} prerequisite for Year {target_year} - {candidate['subject']} progression (confidence: {candidate['confidence']:.2f})"
            
            supabase.table('graphrag_relationships').insert({
                'source_path': candidate['source']['file_path'],
                'target_path': candidate['target']['file_path'],
                'relationship_type': 'prerequisite_for',
                'confidence': candidate['confidence'],
                'reasoning': reasoning,
                'created_at': datetime.now().isoformat()
            }).execute()
            
            created += 1
            if created % 5 == 0:
                print(f"   ✅ {created} bridges created...")
        
        except Exception as e:
            print(f"   ⚠️  Error creating bridge: {e}")
    
    print(f"   ✅ Created {created} bridges!")
    return created

def main():
    """Main execution"""
    print("\n" + "="*70)
    print("🌉 YEAR BRIDGE BUILDER")
    print("   Build prerequisite connections between year levels")
    print("="*70 + "\n")
    
    # Parse arguments
    dry_run = '--dry-run' in sys.argv
    specific_bridge = None
    
    for i, arg in enumerate(sys.argv):
        if arg == '--bridge' and i + 1 < len(sys.argv):
            bridge_arg = sys.argv[i + 1]
            if '-' in bridge_arg:
                parts = bridge_arg.split('-')
                if len(parts) == 2:
                    specific_bridge = (parts[0].replace('Y', ''), parts[1].replace('Y', ''))
    
    if dry_run:
        print("🔍 DRY RUN MODE: No changes will be made\n")
    
    supabase = initialize_supabase()
    
    # Analyze current state
    current_bridges = analyze_year_bridges(supabase)
    
    # Determine which bridges to build
    bridges_to_build = []
    
    if specific_bridge:
        bridges_to_build = [specific_bridge + (f"Y{specific_bridge[0]}→Y{specific_bridge[1]}",)]
        print(f"\n🎯 Building specific bridge: Y{specific_bridge[0]}→Y{specific_bridge[1]}\n")
    else:
        # Build all critical bridges
        for source, target, description in CRITICAL_BRIDGES:
            bridge_key = f"Y{source}→Y{target}"
            current_count = current_bridges.get(bridge_key, 0)
            
            # Prioritize bridges with fewest connections
            if current_count < 10:
                bridges_to_build.append((source, target, description))
        
        print(f"\n🎯 Building {len(bridges_to_build)} priority bridges\n")
    
    # Build bridges
    total_created = 0
    
    for source, target, description in bridges_to_build:
        print("=" * 70)
        print(f"Building: {description} (Y{source}→Y{target})")
        print("=" * 70)
        
        # Find candidates
        candidates = find_bridge_candidates(supabase, source, target)
        
        if not candidates:
            print(f"⚠️  No candidates found for Y{source}→Y{target}")
            continue
        
        # Build bridges
        created = build_bridges(supabase, source, target, candidates, dry_run)
        total_created += created
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 BRIDGE BUILDING SUMMARY")
    print("=" * 70)
    print(f"Bridges attempted: {len(bridges_to_build)}")
    print(f"Connections created: {total_created}")
    print(f"Average per bridge: {total_created / len(bridges_to_build) if bridges_to_build else 0:.1f}")
    print("=" * 70 + "\n")
    
    if dry_run:
        print("💡 Run without --dry-run to actually create bridges\n")
    else:
        print("🎊 Bridge building complete!")
        print("🌉 Students can now follow clear year-level progressions!\n")
        print("💡 Run analysis again to see new bridge counts:\n")
        print("   python3 scripts/year-bridge-builder.py --dry-run\n")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())


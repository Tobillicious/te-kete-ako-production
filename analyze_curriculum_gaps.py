#!/usr/bin/env python3
"""
Curriculum Gap Analysis - Analyze what's missing from 2007 NZC
"""

import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client
from collections import defaultdict
# import pandas as pd  # Not needed

# Load environment variables
load_dotenv()

def connect_to_supabase():
    """Connect to Supabase database"""
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_service_key = os.getenv('SUPABASE_SERVICE_KEY')
    
    if not supabase_url:
        supabase_url = 'https://nlgldaqtubrlcqddppbq.supabase.co'
    
    if not supabase_service_key:
        # Try anon key from mcp-server/.env
        anon_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
        supabase_service_key = anon_key
    
    return create_client(supabase_url, supabase_service_key)

def analyze_curriculum_data(client: Client):
    """Analyze current curriculum data in the database"""
    print("📊 CURRICULUM DATABASE ANALYSIS")
    print("=" * 50)
    
    # Get overall counts by version
    result = client.table('curriculum_statements').select('curriculum_version', count='exact').execute()
    total_statements = result.count if hasattr(result, 'count') else 0
    
    print(f"Total curriculum statements in database: {total_statements}")
    
    # Get breakdown by curriculum version
    version_query = client.table('curriculum_statements').select('curriculum_version').execute()
    version_counts = defaultdict(int)
    
    for statement in version_query.data:
        version_counts[statement['curriculum_version']] += 1
    
    print("\n📚 BY CURRICULUM VERSION:")
    for version, count in version_counts.items():
        print(f"  {version}: {count} statements")
    
    # Analyze by learning area for each version
    print("\n📖 BY LEARNING AREA:")
    
    for version in version_counts.keys():
        print(f"\n{version.upper()}:")
        
        area_query = client.table('curriculum_statements').select('learning_area').eq('curriculum_version', version).execute()
        area_counts = defaultdict(int)
        
        for statement in area_query.data:
            area_counts[statement['learning_area']] += 1
        
        for area, count in sorted(area_counts.items()):
            print(f"  {area}: {count} statements")
    
    # Check for 2007 NZC specific structure
    print("\n🔍 2007 NZC ANALYSIS:")
    nzc_2007_query = client.table('curriculum_statements').select('*').eq('curriculum_version', '2007_nzc').execute()
    
    if nzc_2007_query.data:
        print(f"Found {len(nzc_2007_query.data)} 2007 NZC statements")
        
        # Analyze level distribution
        level_counts = defaultdict(int)
        area_level_counts = defaultdict(lambda: defaultdict(int))
        
        for statement in nzc_2007_query.data:
            level = statement.get('level')
            area = statement.get('learning_area')
            
            if level:
                level_counts[level] += 1
                area_level_counts[area][level] += 1
        
        print("  By Level:")
        for level in sorted(level_counts.keys()):
            print(f"    Level {level}: {level_counts[level]} statements")
        
        print("  By Learning Area and Level:")
        for area, levels in sorted(area_level_counts.items()):
            print(f"    {area}:")
            for level in sorted(levels.keys()):
                print(f"      Level {level}: {levels[level]} statements")
    else:
        print("❌ NO 2007 NZC statements found in database!")
    
    # Analyze English specifically (mentioned in onboarding notes)
    print("\n📝 ENGLISH CURRICULUM ANALYSIS:")
    english_query = client.table('curriculum_statements').select('*').ilike('learning_area', '%english%').execute()
    
    english_by_version = defaultdict(int)
    english_by_phase_level = defaultdict(lambda: defaultdict(int))
    
    for statement in english_query.data:
        version = statement['curriculum_version']
        english_by_version[version] += 1
        
        if version == '2007_nzc' and statement.get('level'):
            english_by_phase_level['2007_levels'][statement['level']] += 1
        elif 'temataiaho' in version or 'draft' in version:
            phase = statement.get('phase', 'Unknown')
            english_by_phase_level[version][phase] += 1
    
    for version, count in english_by_version.items():
        print(f"  {version}: {count} statements")
    
    print("  Phase/Level breakdown:")
    for version_type, phases in english_by_phase_level.items():
        print(f"    {version_type}:")
        for phase, count in sorted(phases.items()):
            print(f"      {phase}: {count} statements")
    
    return {
        'total_statements': total_statements,
        'version_counts': dict(version_counts),
        'has_2007_nzc': len(nzc_2007_query.data) > 0 if 'nzc_2007_query' in locals() else False,
        'english_analysis': dict(english_by_version)
    }

def identify_gaps(analysis_results):
    """Identify specific gaps based on expected 2007 NZC structure"""
    print("\n🚨 GAP ANALYSIS:")
    print("=" * 50)
    
    # Expected 2007 NZC structure
    expected_learning_areas = [
        'English', 'Mathematics and Statistics', 'Science', 'Social Sciences',
        'The Arts', 'Health and Physical Education', 'Technology', 'Learning Languages'
    ]
    
    expected_levels = [1, 2, 3, 4, 5, 6, 7, 8]
    
    print("Expected 2007 NZC structure:")
    print(f"  Learning Areas: {len(expected_learning_areas)}")
    print(f"  Levels: {len(expected_levels)}")
    print(f"  Expected total combinations: {len(expected_learning_areas) * len(expected_levels)} = {len(expected_learning_areas) * len(expected_levels)}")
    
    # Based on typical NZC structure, estimate statements per area/level
    estimated_statements_per_combo = 12  # Conservative estimate
    estimated_total_2007_statements = len(expected_learning_areas) * len(expected_levels) * estimated_statements_per_combo
    
    print(f"  Estimated total 2007 NZC statements: {estimated_total_2007_statements}")
    
    current_2007_count = analysis_results['version_counts'].get('2007_nzc', 0)
    gap = estimated_total_2007_statements - current_2007_count
    
    print(f"\n📊 CURRENT STATUS:")
    print(f"  Current 2007 NZC statements: {current_2007_count}")
    print(f"  Estimated missing: {gap}")
    print(f"  Coverage: {(current_2007_count / estimated_total_2007_statements) * 100:.1f}%")
    
    # Critical gaps
    print(f"\n⚠️  CRITICAL GAPS:")
    if current_2007_count == 0:
        print("  🔴 NO 2007 NZC curriculum found at all!")
        print("  🔴 Missing ALL learning areas and levels")
    elif current_2007_count < 100:
        print("  🟡 Minimal 2007 NZC coverage - major gaps likely")
    
    # English Phase 3 issue (from onboarding notes)
    english_count = analysis_results['english_analysis'].get('temataiaho_2025', 0) + analysis_results['english_analysis'].get('draft_2025', 0)
    if english_count < 20:
        print(f"  🔴 English curriculum severely lacking: only {english_count} statements")
    
    return {
        'estimated_missing_2007': gap,
        'coverage_percentage': (current_2007_count / estimated_total_2007_statements) * 100,
        'critical_gaps': current_2007_count < 100
    }

def recommend_sources():
    """Recommend official sources for 2007 NZC objectives"""
    print("\n📚 RECOMMENDED OFFICIAL SOURCES:")
    print("=" * 50)
    
    sources = [
        {
            'name': 'New Zealand Curriculum Online',
            'url': 'https://nzcurriculum.tki.org.nz/',
            'description': 'Official TKI curriculum documents',
            'priority': 1,
            'content': 'Complete learning area achievement objectives'
        },
        {
            'name': 'Education.govt.nz - Curriculum',
            'url': 'https://www.education.govt.nz/our-work/changes-in-education/curriculum-and-assessment-changes/',
            'description': 'Ministry of Education curriculum resources',
            'priority': 2,
            'content': 'Official curriculum documents and updates'
        },
        {
            'name': 'TKI - Learning Areas',
            'url': 'https://nzcurriculum.tki.org.nz/The-New-Zealand-Curriculum/Learning-areas',
            'description': 'Detailed learning area pages with objectives',
            'priority': 1,
            'content': 'Achievement objectives by level and strand'
        },
        {
            'name': 'NZQA - Achievement Standards',
            'url': 'https://www.nzqa.govt.nz/ncea/assessment/search.do',
            'description': 'NCEA achievement standards linked to curriculum',
            'priority': 3,
            'content': 'Senior secondary curriculum objectives'
        }
    ]
    
    for i, source in enumerate(sources, 1):
        print(f"{i}. {source['name']}")
        print(f"   URL: {source['url']}")
        print(f"   Priority: {source['priority']}/3")
        print(f"   Content: {source['content']}")
        print()
    
    return sources

def recommend_extraction_approach():
    """Recommend the best approach for extracting missing data"""
    print("\n🛠️  RECOMMENDED EXTRACTION APPROACH:")
    print("=" * 50)
    
    approach = {
        'phase_1': {
            'name': 'Automated Web Scraping',
            'description': 'Use existing scraper scripts to extract from TKI',
            'tools': ['scripts/curriculum-scraper/scraper_advanced.py'],
            'target_sites': ['https://nzcurriculum.tki.org.nz/'],
            'estimated_time': '2-4 hours',
            'confidence': 'High'
        },
        'phase_2': {
            'name': 'Manual Document Processing',
            'description': 'Process official PDF documents where scraping fails',
            'tools': ['PDF extraction tools', 'Manual entry'],
            'target_sources': ['Official MoE curriculum PDFs'],
            'estimated_time': '8-16 hours',
            'confidence': 'Medium'
        },
        'phase_3': {
            'name': 'Data Validation & Quality Check',
            'description': 'Verify extracted data against official sources',
            'tools': ['Database queries', 'Cross-referencing'],
            'estimated_time': '2-4 hours',
            'confidence': 'High'
        }
    }
    
    for phase, details in approach.items():
        print(f"{phase.upper()}: {details['name']}")
        print(f"  Description: {details['description']}")
        print(f"  Tools: {', '.join(details['tools'])}")
        print(f"  Estimated time: {details['estimated_time']}")
        print(f"  Success confidence: {details['confidence']}")
        print()
    
    print("🎯 IMMEDIATE NEXT STEPS:")
    print("1. Test database connection and current scraper scripts")
    print("2. Identify specific 2007 NZC pages on TKI website")
    print("3. Adapt existing scraper for 2007 NZC structure")
    print("4. Run extraction for highest-priority learning areas first")
    print("5. Validate and upload to curriculum_statements table")
    
    return approach

def main():
    """Main analysis function"""
    try:
        # Connect to database
        client = connect_to_supabase()
        print("✅ Connected to Supabase database")
        
        # Analyze current data
        analysis_results = analyze_curriculum_data(client)
        
        # Identify gaps
        gap_analysis = identify_gaps(analysis_results)
        
        # Recommend sources
        sources = recommend_sources()
        
        # Recommend approach
        approach = recommend_extraction_approach()
        
        # Save results
        results = {
            'analysis': analysis_results,
            'gaps': gap_analysis,
            'sources': sources,
            'approach': approach,
            'timestamp': '2025-10-31'
        }
        
        with open('curriculum_gap_analysis.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n💾 Analysis saved to: curriculum_gap_analysis.json")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Check your database connection and environment variables.")

if __name__ == "__main__":
    main()
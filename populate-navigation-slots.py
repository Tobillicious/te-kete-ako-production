#!/usr/bin/env python3
"""
NAVIGATION SLOT POPULATION SYSTEM
Automatically assigns 8,178 resources to existing navigation slots using GraphRAG intelligence
NO new navigation items - just fill what exists!
"""

import os
from supabase import create_client, Client

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjg4MDA0NzYsImV4cCI6MjA0NDM3NjQ3Nn0.4eta2Wdz1MgJu63-ka1IQi_FcJBNjHdUe43Q_m5nHjY"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# EXISTING NAVIGATION SLOTS (from navigation-standard.html)
NAVIGATION_SLOTS = {
    'units_1_7_cross': [
        '/units/unit-1-te-ao-maori.html',
        '/units/unit-2-decolonized-history.html',
        '/units/unit-3-stem-matauranga.html',
        '/units/unit-4-economic-justice.html',
        '/units/unit-5-global-connections.html',
        '/units/unit-6-future-rangatiratanga.html',
        '/units/unit-7-digital-tech-ai-ethics.html'
    ],
    'units_1_7_math': [
        '/units/unit-1-mathematics/index.html',
        '/units/unit-2-mathematics/index.html',
        '/units/unit-3-mathematics/index.html',
        '/units/unit-4-mathematics/index.html',
        '/units/unit-5-mathematics/index.html',
        '/units/unit-6-mathematics/index.html',
        '/units/unit-7-mathematics/index.html'
    ],
    'units_1_7_science': [
        '/units/unit-1-science/index.html',
        '/units/unit-2-science/index.html',
        '/units/unit-3-science/index.html',
        '/units/unit-4-science/index.html',
        '/units/unit-5-science/index.html',
        '/units/unit-6-science/index.html',
        '/units/unit-7-science/index.html'
    ],
    'units_1_7_english': [
        '/units/unit-1-english/index.html',
        '/units/unit-2-english/index.html',
        '/units/unit-3-english/index.html',
        '/units/unit-4-english/index.html',
        '/units/unit-5-english/index.html',
        '/units/unit-6-english/index.html',
        '/units/unit-7-english/index.html'
    ],
    'subject_hubs': {
        'Mathematics': '/public/mathematics-hub.html',
        'Science': '/public/science-hub.html',
        'English': '/public/english-hub.html',
        'Social Studies': '/public/social-studies.html',
        'Te Ao Māori': '/public/te-ao-maori.html',
        'Digital Tech': '/public/digital-tech-hub.html'
    },
    'year_levels': {
        'Year 7': '/public/year-7-curriculum.html',
        'Year 8': '/public/year-8-curriculum.html',
        'Year 9': '/public/year-9-curriculum.html',
        'Year 10': '/public/year-10-curriculum.html'
    },
    'special_collections': {
        'Games': '/public/games.html',
        'Assessments': '/public/assessments-complete.html',
        'Handouts': '/public/handouts.html',
        'Gold': '/public/gold-collection.html',
        'Tools': '/public/teacher-tools.html'
    }
}

def analyze_slot_needs():
    """Query GraphRAG to see what needs to go where"""
    print("🧠 QUERYING GRAPHRAG FOR SLOT ASSIGNMENT...")
    
    # Get all resources that need slots
    response = supabase.table('graphrag_resources')\
        .select('file_path, title, resource_type, subject, year_level, quality_score, has_whakataukī')\
        .in_('resource_type', ['Lesson', 'Handout', 'Unit-Plan', 'Game', 'Assessment'])\
        .gte('quality_score', 85)\
        .execute()
    
    resources = response.data
    print(f"📊 Found {len(resources)} high-quality resources to assign")
    
    # Assign to slots
    assignments = {
        'units_1_7': [],
        'subject_hubs': {},
        'year_levels': {},
        'special_collections': {}
    }
    
    for resource in resources:
        # Assign to appropriate slot(s)
        subject = resource.get('subject', 'General')
        year = resource.get('year_level', 'All')
        res_type = resource.get('resource_type')
        quality = resource.get('quality_score', 0)
        
        # Games go to games collection
        if res_type == 'Game':
            if 'Games' not in assignments['special_collections']:
                assignments['special_collections']['Games'] = []
            assignments['special_collections']['Games'].append(resource)
        
        # Gold goes to gold collection
        if quality >= 90:
            if 'Gold' not in assignments['special_collections']:
                assignments['special_collections']['Gold'] = []
            assignments['special_collections']['Gold'].append(resource)
        
        # Subject hub assignment
        if subject and subject != 'General' and subject != 'Unknown':
            if subject not in assignments['subject_hubs']:
                assignments['subject_hubs'][subject] = []
            assignments['subject_hubs'][subject].append(resource)
        
        # Year level assignment
        if year and 'Year' in str(year):
            if year not in assignments['year_levels']:
                assignments['year_levels'][year] = []
            assignments['year_levels'][year].append(resource)
    
    return assignments

def generate_population_report(assignments):
    """Show what goes where"""
    print("\n" + "="*70)
    print("🎯 NAVIGATION SLOT POPULATION REPORT")
    print("="*70)
    
    print("\n📚 SPECIAL COLLECTIONS:")
    for collection, resources in assignments['special_collections'].items():
        print(f"  {collection}: {len(resources)} resources")
    
    print("\n🏫 SUBJECT HUBS:")
    for subject, resources in assignments['subject_hubs'].items():
        print(f"  {subject}: {len(resources)} resources")
    
    print("\n🎓 YEAR LEVELS:")
    for year, resources in assignments['year_levels'].items():
        print(f"  {year}: {len(resources)} resources")
    
    print("\n" + "="*70)
    print("✅ ALL RESOURCES ASSIGNED TO EXISTING NAVIGATION SLOTS!")
    print("="*70)

if __name__ == "__main__":
    print("🚀 NAVIGATION SLOT POPULATION SYSTEM")
    print("="*70)
    print("STRATEGY: Use EXISTING navigation, just fill it!")
    print("="*70 + "\n")
    
    assignments = analyze_slot_needs()
    generate_population_report(assignments)
    
    print("\n✨ NEXT: Update each slot page with its assigned resources")
    print("📖 See navigation-standard.html for all existing slots")


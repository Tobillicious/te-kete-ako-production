#!/usr/bin/env python3

"""
Quick GraphRAG Test Script
Tests connection to Supabase and shows sample queries
"""

from supabase import create_client
import json
from datetime import datetime

# Supabase connection (from .env / MCP config)
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def test_graphrag():
    print("\n🧠 Testing Supabase GraphRAG Connection")
    print("=" * 60)
    
    # Connect
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        print(f"✅ Connected to {SUPABASE_URL}")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return
    
    print()
    
    # Test 1: Count all resources
    try:
        result = supabase.table('resources').select('*', count='exact').limit(1).execute()
        print(f"📊 Total Resources: {result.count}")
    except Exception as e:
        print(f"⚠️  Could not count resources: {e}")
    
    # Test 2: Get sample resources
    try:
        result = supabase.table('resources').select('id, title, type, cultural_level').limit(5).execute()
        print(f"\n📚 Sample Resources (first 5):")
        for r in result.data:
            cultural = r.get('cultural_level', 'unknown')
            print(f"  - [{r['type']}] {r['title']} (cultural: {cultural})")
    except Exception as e:
        print(f"⚠️  Could not fetch resources: {e}")
    
    # Test 3: Find high cultural content
    try:
        result = supabase.table('resources').select('*', count='exact').eq('cultural_level', 'high').execute()
        print(f"\n🌿 High Cultural Value Resources: {result.count}")
        if result.data:
            print("   Examples:")
            for r in result.data[:3]:
                print(f"   - {r['title']}")
    except Exception as e:
        print(f"⚠️  Could not query cultural level: {e}")
    
    # Test 4: Resources by type
    try:
        types = ['handout', 'lesson', 'unit', 'activity']
        print(f"\n📋 Resources by Type:")
        for t in types:
            result = supabase.table('resources').select('*', count='exact').eq('type', t).execute()
            print(f"   - {t}: {result.count}")
    except Exception as e:
        print(f"⚠️  Could not query by type: {e}")
    
    # Test 5: Sample concepts
    try:
        result = supabase.table('resource_concepts').select('concept_name, concept_type').limit(10).execute()
        if result.data:
            print(f"\n🔗 Sample Māori Concepts:")
            concepts = list(set(r['concept_name'] for r in result.data))
            for c in concepts[:5]:
                print(f"   - {c}")
    except Exception as e:
        print(f"⚠️  Could not fetch concepts: {e}")
    
    print("\n" + "=" * 60)
    print("✅ GraphRAG test complete!")
    print()
    print("Example queries you can run:")
    print("  - Find all handouts: supabase.table('resources').select('*').eq('type', 'handout').execute()")
    print("  - High cultural: supabase.table('resources').select('*').eq('cultural_level', 'high').execute()")
    print("  - By concept: supabase.table('resource_concepts').select('*, resources(*)').eq('concept_name', 'haka').execute()")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_graphrag()


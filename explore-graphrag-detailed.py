#!/usr/bin/env python3
"""
Comprehensive GraphRAG Exploration
Show everything in the knowledge graph
"""

from supabase import create_client

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🧠 COMPREHENSIVE GRAPHRAG EXPLORATION")
print("=" * 70)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get all tables in the database
print("\n📊 GRAPHRAG DATABASE STRUCTURE:")
print("-" * 70)

# Check resources table
try:
    result = supabase.table('resources').select('*', count='exact').limit(1).execute()
    total = result.count if hasattr(result, 'count') else 'Unknown'
    print(f"\n✅ 'resources' table: {total} total entries")
    
    # Sample a few resources to see structure
    sample = supabase.table('resources').select('*').limit(3).execute()
    if sample.data:
        print(f"\n   Sample resource structure:")
        for key in sample.data[0].keys():
            print(f"   - {key}")
    
except Exception as e:
    print(f"   ⚠️  Error: {e}")

# Check for other GraphRAG tables
other_tables = [
    'knowledge_nodes',
    'knowledge_edges', 
    'episodic_memory',
    'procedural_workflows',
    'agent_jobs',
    'artifact_catalog',
    'quality_assessments',
    'learning_outcomes'
]

print(f"\n📋 Checking for additional GraphRAG tables:")
for table in other_tables:
    try:
        result = supabase.table(table).select('*', count='exact').limit(1).execute()
        count = result.count if hasattr(result, 'count') else len(result.data) if result.data else 0
        if count > 0:
            print(f"   ✅ '{table}': {count} entries")
        else:
            print(f"   ⚠️  '{table}': exists but empty")
    except Exception as e:
        print(f"   ❌ '{table}': not found")

print("\n" + "=" * 70)

#!/usr/bin/env python3
"""List all accessible Supabase tables"""

from supabase import create_client

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("📊 CHECKING SUPABASE TABLES...")
print("=" * 60)

tables_to_check = [
    'resources',
    'relationships', 
    'graphrag_resources',
    'graphrag_relationships',
    'communities',
    'resource_concepts',
    'resource_embeddings',
    'multi_ai_coordination_log',
    'agent_knowledge',
    'agent_coordination',
    'profiles'
]

accessible = []
not_accessible = []

for table in tables_to_check:
    try:
        result = supabase.table(table).select('id', count='exact').limit(1).execute()
        accessible.append((table, result.count))
        print(f"✅ {table:30} ({result.count} total rows)")
    except Exception as e:
        not_accessible.append((table, str(e)[:50]))
        print(f"❌ {table:30} NOT ACCESSIBLE")

print("\n" + "=" * 60)
print(f"📊 SUMMARY: {len(accessible)}/{len(tables_to_check)} tables accessible")
print("=" * 60)


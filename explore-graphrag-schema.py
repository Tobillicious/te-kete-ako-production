#!/usr/bin/env python3

"""
Explore actual GraphRAG schema
"""

from supabase import create_client
import json

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("\n🔍 Exploring GraphRAG Schema")
print("=" * 60)

# Get sample resource to see structure
result = supabase.table('resources').select('*').limit(1).execute()
if result.data:
    print("\n📋 Resource Structure:")
    resource = result.data[0]
    for key, value in resource.items():
        value_preview = str(value)[:50] if value else "null"
        print(f"  - {key}: {value_preview}")

# Get stats
print("\n📊 Resource Statistics:")
result = supabase.table('resources').select('*', count='exact').limit(1).execute()
print(f"  Total: {result.count}")

# Count by type
types_result = supabase.table('resources').select('type').execute()
if types_result.data:
    types = {}
    for r in types_result.data:
        t = r.get('type', 'unknown')
        types[t] = types.get(t, 0) + 1
    print(f"\n  By Type:")
    for t, count in sorted(types.items(), key=lambda x: -x[1]):
        print(f"    - {t}: {count}")

# Sample resources
print(f"\n📚 Sample Resources:")
result = supabase.table('resources').select('*').limit(5).execute()
for r in result.data:
    title = r.get('title', 'Untitled')[:50]
    rtype = r.get('type', 'unknown')
    print(f"  - [{rtype}] {title}")

print("\n" + "=" * 60 + "\n")


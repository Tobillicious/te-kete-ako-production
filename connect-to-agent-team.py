#!/usr/bin/env python3
"""
CONNECT TO AGENT TEAM - MCP/Supabase Coordination
See what other agents are doing on the 90k document organization
"""

from supabase import create_client
import json
from datetime import datetime

# Supabase GraphRAG connection
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🤝 CONNECTING TO AGENT TEAM VIA MCP/SUPABASE")
print("=" * 60)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# 1. Check total resources in GraphRAG
print("\n📊 GRAPHRAG STATUS:")
result = supabase.table('resources').select('*', count='exact').limit(1).execute()
print(f"   Total resources indexed: {result.count}")

# 2. Check resource types
print("\n📁 RESOURCE BREAKDOWN:")
types_result = supabase.table('resources').select('type').execute()
if types_result.data:
    from collections import Counter
    types = Counter([r.get('type', 'unknown') for r in types_result.data])
    for rtype, count in types.most_common():
        print(f"   {rtype}: {count}")

# 3. Check for agent_coordination table
print("\n🤝 CHECKING AGENT COORDINATION:")
try:
    agents = supabase.table('agent_coordination').select('*').execute()
    if agents.data:
        print(f"   Active agents: {len(agents.data)}")
        for agent in agents.data:
            print(f"   - {agent.get('agent_name')}: {agent.get('status')}")
    else:
        print("   No agents currently registered in coordination table")
except Exception as e:
    print(f"   agent_coordination table: Not found or error ({e})")

# 4. Check for agent_knowledge table
print("\n🧠 CHECKING AGENT KNOWLEDGE:")
try:
    knowledge = supabase.table('agent_knowledge').select('*', count='exact').limit(5).execute()
    print(f"   Knowledge entries: {knowledge.count}")
    if knowledge.data:
        print(f"   Recent knowledge:")
        for k in knowledge.data[:3]:
            print(f"   - {k.get('title', 'Untitled')[:60]}")
except Exception as e:
    print(f"   agent_knowledge table: Not found or error ({e})")

# 5. Check what tables exist
print("\n📊 AVAILABLE TABLES:")
tables_to_check = ['resources', 'agent_coordination', 'agent_knowledge', 'site_structure', 'content_hierarchy']
for table in tables_to_check:
    try:
        result = supabase.table(table).select('*', count='exact').limit(1).execute()
        print(f"   ✅ {table}: {result.count} records")
    except:
        print(f"   ❌ {table}: Not found")

# 6. Get schema info
print("\n🔍 GETTING SCHEMA INFO:")
try:
    # Try to get one resource to see structure
    sample = supabase.table('resources').select('*').limit(1).execute()
    if sample.data:
        resource = sample.data[0]
        print(f"   Resource fields:")
        for key in resource.keys():
            print(f"   - {key}")
except Exception as e:
    print(f"   Error: {e}")

# 7. Search for "unit" resources to see organization
print("\n🔍 SAMPLE: Units in GraphRAG:")
units = supabase.table('resources').select('title, type, path').ilike('title', '%unit%').limit(10).execute()
for unit in units.data:
    print(f"   - {unit.get('title', 'Untitled')[:50]} ({unit.get('type', '?')})")

# 8. Check if today's work is in there
print("\n🔍 CHECKING TODAY'S WORK:")
todays_units = ['unit-1-te-ao-maori', 'unit-2-decolonized', 'y8-statistics']
for unit_name in todays_units:
    result = supabase.table('resources').select('title').ilike('path', f'%{unit_name}%').limit(1).execute()
    if result.data:
        print(f"   ✅ {unit_name}: Already in GraphRAG")
    else:
        print(f"   ❌ {unit_name}: Not yet indexed")

print("\n" + "=" * 60)
print("\n✅ CONNECTION COMPLETE")
print("\n📖 Next Steps:")
print("   1. If 90k documents in GraphRAG, query them to understand organization")
print("   2. Register current agent work in coordination table")
print("   3. Query what other agents are working on")
print("   4. Use GraphRAG data instead of guessing file counts")
print("   5. Coordinate systematically with team")


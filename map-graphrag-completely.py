#!/usr/bin/env python3
"""
MAP THE GRAPHRAG COMPLETELY
Understand what's ALREADY in the knowledge graph before continuing
"""

from supabase import create_client
import json

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🗺️  MAPPING GRAPHRAG COMPLETELY")
print("=" * 70)
print("Understanding what's ALREADY in the knowledge graph...")
print()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get all tables
print("📊 CHECKING GRAPHRAG TABLES:")
print("-" * 70)

# 1. Check resources table
try:
    resources = supabase.table('resources').select('*').execute()
    print(f"✅ resources table: {len(resources.data)} entries")
    
    if resources.data:
        # Analyze what's in there
        types = {}
        for r in resources.data:
            rtype = r.get('type', 'unknown')
            types[rtype] = types.get(rtype, 0) + 1
        
        print("   Types breakdown:")
        for rtype, count in sorted(types.items(), key=lambda x: x[1], reverse=True):
            print(f"     - {rtype}: {count}")
except Exception as e:
    print(f"⚠️  resources table error: {e}")

print()

# 2. Check agent_coordination table
try:
    coordination = supabase.table('agent_coordination').select('*').execute()
    print(f"✅ agent_coordination table: {len(coordination.data)} entries")
    
    if coordination.data:
        # Recent activity
        recent = sorted(coordination.data, key=lambda x: x.get('created_at', ''), reverse=True)[:5]
        print("   Recent activity:")
        for entry in recent:
            agent = entry.get('agent_name', 'unknown')
            task = entry.get('task_claimed', '')[:60]
            print(f"     - {agent}: {task}...")
except Exception as e:
    print(f"⚠️  agent_coordination table error: {e}")

print()

# 3. Check agent_knowledge table
try:
    knowledge = supabase.table('agent_knowledge').select('*').execute()
    print(f"✅ agent_knowledge table: {len(knowledge.data)} entries")
    
    if knowledge.data:
        # Categories
        categories = {}
        for k in knowledge.data:
            cat = k.get('category', 'unknown')
            categories[cat] = categories.get(cat, 0) + 1
        
        print("   Categories:")
        for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"     - {cat}: {count}")
except Exception as e:
    print(f"⚠️  agent_knowledge table error: {e}")

print()
print("=" * 70)
print("🎯 GRAPHRAG MAP COMPLETE")
print("=" * 70)
print()
print("Now I can see what's already documented!")
print("This prevents duplicate work and shows gaps.")


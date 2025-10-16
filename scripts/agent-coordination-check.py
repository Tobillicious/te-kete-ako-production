#!/usr/bin/env python3
"""
MANDATORY AGENT COORDINATION CHECK
Run BEFORE starting any work!
Queries MCP GraphRAG to see what others are doing
"""

import os
from supabase import create_client, Client

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

print("=" * 70)
print("🤝 AGENT COORDINATION CHECK - MANDATORY PRE-WORK")
print("=" * 70)
print()

# Query current agent work
print("📊 CHECKING WHAT OTHER AGENTS ARE DOING...")
print()

response = supabase.table('agent_coordination')\
    .select('*')\
    .in_('status', ['planning', 'in_progress'])\
    .order('updated_at', desc=True)\
    .limit(10)\
    .execute()

if response.data:
    print("🚨 OTHER AGENTS CURRENTLY WORKING:")
    print()
    for agent in response.data:
        print(f"   Agent: {agent['agent_name']}")
        print(f"   Task:  {agent['task_claimed']}")
        print(f"   Status: {agent['status']}")
        if agent.get('files_modified'):
            print(f"   Files: {', '.join(agent['files_modified'][:5])}")
        print(f"   Started: {agent['started_at']}")
        print()
    
    print("⚠️  COORDINATION REQUIRED!")
    print("   → Read their work before proceeding")
    print("   → Build on their work, don't duplicate")
    print("   → Coordinate in ACTIVE_QUESTIONS.md")
    print()
else:
    print("✅ NO OTHER AGENTS CURRENTLY WORKING")
    print("   You can proceed with your task!")
    print()

# Query recent completions
print("📚 RECENT AGENT COMPLETIONS (Last 24 hours):")
print()

from datetime import datetime, timedelta
yesterday = (datetime.now() - timedelta(days=1)).isoformat()

completed = supabase.table('agent_coordination')\
    .select('agent_name, task_claimed, completed_at, key_decisions')\
    .eq('status', 'completed')\
    .gte('completed_at', yesterday)\
    .order('completed_at', desc=True)\
    .limit(5)\
    .execute()

if completed.data:
    for work in completed.data:
        print(f"   ✅ {work['agent_name']}: {work['task_claimed']}")
        if work.get('key_decisions'):
            for key, val in work['key_decisions'].items():
                print(f"      → {key}: {val}")
        print()
else:
    print("   (No completions logged yet - start logging!)")
    print()

# GraphRAG stats
print("📊 GRAPHRAG STATUS:")
print()

stats = supabase.table('resources').select('count', count='exact').execute()
print(f"   Total Resources: {stats.count}")

print()
print("=" * 70)
print("🎯 READY TO START? Remember to LOG YOUR WORK!")
print()
print("   1. Claim task in agent_coordination table")
print("   2. Update ACTIVE_QUESTIONS.md")
print("   3. Do the work")
print("   4. Update progress every 30 mins")
print("   5. Mark complete when done")
print("=" * 70)


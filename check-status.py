#!/usr/bin/env python3
from supabase import create_client

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Quick write test
try:
    result = supabase.table('agent_knowledge').insert({
        'source_type': 'test',
        'source_name': 'Test Oct 20',
        'doc_type': 'test'
    }).execute()
    supabase.table('agent_knowledge').delete().eq('source_name', 'Test Oct 20').execute()
    print("✅ WORKING - All agents can write to GraphRAG!")
except Exception as e:
    if 'row-level security' in str(e).lower():
        print("❌ STILL BLOCKED - Need to run fix in Supabase Dashboard")
        print("   Go to: https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/sql")
        print("   Run: COMPLETE-MULTI-AGENT-FIX.sql")
    else:
        print(f"⚠️  Error: {str(e)[:100]}")


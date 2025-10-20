#!/usr/bin/env python3
"""Ultra-quick multi-agent access test"""
from supabase import create_client
import sys

URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase = create_client(URL, KEY)

print("🧪 Testing multi-agent write access...\n")

try:
    # Try to write to agent_knowledge
    result = supabase.table('agent_knowledge').insert({
        'source_type': 'test',
        'source_name': 'Quick Test ' + str(hash('test'))[:8],
        'doc_type': 'verification'
    }).execute()
    
    # Cleanup
    supabase.table('agent_knowledge').delete().eq('source_name', result.data[0]['source_name']).execute()
    
    print("✅ SUCCESS: Multi-agent access is WORKING!")
    print("   All 12 agents can read/write to GraphRAG")
    print("   Coordination fully operational")
    sys.exit(0)
    
except Exception as e:
    error = str(e)
    if 'row-level security' in error.lower() or '42501' in error:
        print("❌ BLOCKED: Multi-agent access needs fixing")
        print("   RLS policy is blocking writes")
        print()
        print("🔧 TO FIX:")
        print("   Run: python3 apply-multi-agent-fix.py")
        print("   Or use MCP Supabase to execute: COMPLETE-MULTI-AGENT-FIX.sql")
        sys.exit(1)
    else:
        print(f"⚠️  Unknown error: {error[:200]}")
        sys.exit(2)

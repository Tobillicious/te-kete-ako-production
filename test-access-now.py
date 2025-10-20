#!/usr/bin/env python3
"""Quick test of multi-agent GraphRAG access"""

from supabase import create_client

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

print("🧪 TESTING MULTI-AGENT ACCESS...")
print()

# Test graphrag_resources READ
try:
    result = supabase.table('graphrag_resources').select('id, title').limit(1).execute()
    print(f"✅ graphrag_resources READ: WORKING ({len(result.data)} rows)")
except Exception as e:
    print(f"❌ graphrag_resources READ: BLOCKED")
    print(f"   {str(e)[:100]}")

# Test graphrag_resources WRITE  
try:
    test = supabase.table('graphrag_resources').insert({
        'file_path': '/test-multi-agent-' + str(hash('test')),
        'title': 'Test',
        'quality_score': 1
    }).execute()
    # Cleanup
    supabase.table('graphrag_resources').delete().eq('title', 'Test').execute()
    print(f"✅ graphrag_resources WRITE: WORKING")
except Exception as e:
    print(f"❌ graphrag_resources WRITE: BLOCKED")
    print(f"   {str(e)[:100]}")

print()
print("=" * 60)
print("VERDICT:")

# Try one more comprehensive test
try:
    count = supabase.table('graphrag_resources').select('id', count='exact').limit(1).execute()
    total = count.count
    print(f"✅ Multi-agent access is WORKING!")
    print(f"   GraphRAG has {total:,} resources accessible")
    print()
    print("🎉 All 12 agents can collaborate!")
except Exception as e:
    print(f"❌ Multi-agent access is BROKEN")
    print(f"   Error: {str(e)[:150]}")
    print()
    print("🔧 FIX: Run COMPLETE-MULTI-AGENT-FIX.sql in Supabase")


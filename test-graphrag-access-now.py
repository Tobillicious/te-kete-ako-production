#!/usr/bin/env python3
"""
Quick GraphRAG Access Test
Tests if we can currently read from GraphRAG tables
"""

from supabase import create_client
import sys

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

print("🧪 TESTING GRAPHRAG ACCESS...")
print("=" * 60)

try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # Test 1: Read resources
    print("\n📖 Test 1: Reading resources table...")
    result = supabase.table('resources').select('id, title').limit(5).execute()
    print(f"✅ SUCCESS: Found {len(result.data)} resources")
    if result.data:
        print(f"   Sample: {result.data[0].get('title', 'N/A')[:50]}")
    
    # Test 2: Read relationships
    print("\n🔗 Test 2: Reading relationships table...")
    result = supabase.table('relationships').select('id, relationship_type').limit(5).execute()
    print(f"✅ SUCCESS: Found {len(result.data)} relationships")
    
    # Test 3: Read coordination log
    print("\n📋 Test 3: Reading multi_ai_coordination_log...")
    result = supabase.table('multi_ai_coordination_log').select('id').limit(5).execute()
    print(f"✅ SUCCESS: Found {len(result.data)} coordination entries")
    
    # Test 4: Count high-quality resources
    print("\n💎 Test 4: Counting high-quality resources (Q90+)...")
    result = supabase.table('resources').select('id', count='exact').gte('quality_score', 90).execute()
    print(f"✅ SUCCESS: {result.count} high-quality resources")
    
    print("\n" + "=" * 60)
    print("🎉 GRAPHRAG IS FULLY ACCESSIBLE!")
    print("   All agents can read and collaborate")
    print("=" * 60)
    sys.exit(0)
    
except Exception as e:
    error_msg = str(e).lower()
    
    print("\n" + "=" * 60)
    if 'row-level security' in error_msg or 'policy' in error_msg:
        print("❌ GRAPHRAG ACCESS BLOCKED BY RLS POLICIES")
        print("\n🔧 FIX REQUIRED:")
        print("   1. Open: https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/sql")
        print("   2. Run: supabase/migrations/20251020_restore_multi_agent_access.sql")
        print("   3. See: APPLY_MULTI_AGENT_FIX_NOW.md for instructions")
    elif 'not found' in error_msg or 'does not exist' in error_msg:
        print("❌ TABLE NOT FOUND")
        print("   Check table names or database schema")
    else:
        print(f"❌ ERROR: {str(e)[:150]}")
    
    print("=" * 60)
    sys.exit(1)

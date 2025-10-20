#!/usr/bin/env python3
"""
Execute Multi-Agent Access Fix
Direct approach using Supabase Python client
"""

from supabase import create_client, Client
import sys

# Supabase credentials (using anon key - same as other scripts)
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def test_access(supabase: Client) -> dict:
    """Test current access to key tables"""
    print("\n" + "="*70)
    print("🧪 TESTING CURRENT ACCESS LEVELS")
    print("="*70 + "\n")
    
    results = {}
    
    # Test resources table
    try:
        result = supabase.table('resources').select('id', count='exact').limit(1).execute()
        results['resources'] = f"✅ SUCCESS ({result.count} total)"
        print(f"✅ resources table: Accessible ({result.count} records)")
    except Exception as e:
        results['resources'] = f"❌ BLOCKED: {str(e)[:80]}"
        print(f"❌ resources table: {str(e)[:80]}")
    
    # Test agent_knowledge table
    try:
        result = supabase.table('agent_knowledge').select('id', count='exact').limit(1).execute()
        results['agent_knowledge'] = f"✅ SUCCESS ({result.count} total)"
        print(f"✅ agent_knowledge table: Accessible ({result.count} records)")
    except Exception as e:
        results['agent_knowledge'] = f"❌ BLOCKED: {str(e)[:80]}"
        print(f"❌ agent_knowledge table: {str(e)[:80]}")
    
    # Test relationships table
    try:
        result = supabase.table('relationships').select('id', count='exact').limit(1).execute()
        results['relationships'] = f"✅ SUCCESS ({result.count} total)"
        print(f"✅ relationships table: Accessible ({result.count} records)")
    except Exception as e:
        results['relationships'] = f"❌ BLOCKED: {str(e)[:80]}"
        print(f"❌ relationships table: {str(e)[:80]}")
    
    # Test multi_ai_coordination_log table
    try:
        result = supabase.table('multi_ai_coordination_log').select('id', count='exact').limit(1).execute()
        results['coordination_log'] = f"✅ SUCCESS ({result.count} total)"
        print(f"✅ coordination log: Accessible ({result.count} records)")
    except Exception as e:
        results['coordination_log'] = f"❌ BLOCKED: {str(e)[:80]}"
        print(f"❌ coordination log: {str(e)[:80]}")
    
    return results

def main():
    print("="*70)
    print("🔓 MULTI-AGENT ACCESS DIAGNOSIS & FIX")
    print("="*70)
    print()
    print("Purpose: Diagnose and fix agent access to GraphRAG/MCP tables")
    print()
    
    # Connect to Supabase
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("✅ Connected to Supabase")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return 1
    
    # Test current access
    before_results = test_access(supabase)
    
    # Count failures
    failures = sum(1 for v in before_results.values() if v.startswith('❌'))
    
    print("\n" + "="*70)
    print("📊 DIAGNOSIS SUMMARY")
    print("="*70 + "\n")
    
    if failures == 0:
        print("🎉 ALL TABLES ACCESSIBLE!")
        print("✅ No fix needed - all agents can already access GraphRAG/MCP")
        print()
        print("If you're still experiencing issues, check:")
        print("  1. Network connectivity")
        print("  2. API key validity")
        print("  3. Table-level RLS policies in Supabase Dashboard")
        return 0
    else:
        print(f"⚠️  PROBLEM CONFIRMED: {failures}/4 tables blocked")
        print()
        print("🔧 FIX REQUIRED:")
        print("   1. Open Supabase Dashboard SQL Editor")
        print("   2. Execute: supabase/migrations/20251020_restore_multi_agent_access.sql")
        print()
        print("📖 See APPLY_MULTI_AGENT_FIX_NOW.md for detailed instructions")
        print()
        print("Note: RLS policy changes require service_role key or Dashboard access.")
        print("      Anon key cannot modify policies (security feature).")
        return 1

if __name__ == "__main__":
    sys.exit(main())


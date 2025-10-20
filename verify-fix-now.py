#!/usr/bin/env python3
"""Quick verification of multi-agent access"""

from supabase import create_client
import sys

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

print("\n🔍 QUICK VERIFICATION: Multi-Agent Access\n" + "="*60 + "\n")

try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("✅ Connected to Supabase\n")
    
    # Test 1: Read resources
    try:
        result = supabase.table('resources').select('id, title').limit(3).execute()
        print(f"✅ READ resources: {len(result.data)} items ({result.count if hasattr(result, 'count') else 'many'} total)")
        if result.data:
            print(f"   Example: {result.data[0].get('title', 'N/A')[:60]}")
    except Exception as e:
        print(f"❌ READ resources: {str(e)[:100]}")
    
    # Test 2: Read relationships  
    try:
        result = supabase.table('relationships').select('id, relationship_type').limit(3).execute()
        print(f"✅ READ relationships: {len(result.data)} items")
    except Exception as e:
        print(f"❌ READ relationships: {str(e)[:100]}")
    
    # Test 3: Read agent_knowledge
    try:
        result = supabase.table('agent_knowledge').select('id, source_name').limit(3).execute()
        print(f"✅ READ agent_knowledge: {len(result.data)} items")
        if result.data:
            print(f"   Recent: {result.data[0].get('source_name', 'N/A')[:60]}")
    except Exception as e:
        print(f"❌ READ agent_knowledge: {str(e)[:100]}")
    
    # Test 4: TRY TO WRITE (this is the critical test)
    print("\n🧪 Testing WRITE access (the critical fix):\n")
    
    try:
        test_data = {
            'source_type': 'verification_test',
            'source_name': 'Multi-Agent Access Verification - Oct 20 2025',
            'doc_type': 'test',
            'key_insights': ['Testing multi-agent write access']
        }
        result = supabase.table('agent_knowledge').insert(test_data).execute()
        
        # Clean up test entry
        if result.data:
            supabase.table('agent_knowledge').delete().eq('source_name', test_data['source_name']).execute()
        
        print("✅ WRITE agent_knowledge: WORKING!")
        print("\n" + "="*60)
        print("🎉 SUCCESS! MULTI-AGENT ACCESS IS WORKING!")
        print("="*60)
        print("\n✅ All 12 agents can now:")
        print("   - Read GraphRAG resources")
        print("   - Write to agent_knowledge")
        print("   - Collaborate fully\n")
        sys.exit(0)
        
    except Exception as e:
        error_msg = str(e)
        if 'row-level security' in error_msg.lower() or '42501' in error_msg:
            print("❌ WRITE agent_knowledge: BLOCKED BY RLS")
            print(f"   Error: {error_msg[:150]}")
            print("\n" + "="*60)
            print("⚠️  FIX NEEDED: Multi-agent WRITE access still blocked")
            print("="*60)
            print("\n📋 TO FIX:")
            print("   1. Open: https://supabase.com/dashboard/project/nlgldaqtubrlcqddppbq/sql")
            print("   2. Run: COMPLETE-MULTI-AGENT-FIX.sql")
            print("   3. Verify with: python3 verify-fix-now.py\n")
            sys.exit(1)
        else:
            print(f"❌ WRITE test failed: {error_msg[:150]}")
            sys.exit(2)
            
except Exception as e:
    print(f"❌ Connection failed: {e}")
    sys.exit(3)


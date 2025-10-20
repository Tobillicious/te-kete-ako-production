#!/usr/bin/env python3
"""
Test Multi-Agent GraphRAG Access
Verifies that all agents can read and write to GraphRAG tables
"""

from supabase import create_client
import sys

# Supabase credentials
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def test_multi_agent_access():
    """Test GraphRAG access for multi-agent collaboration"""
    
    print("=" * 70)
    print("🔍 TESTING MULTI-AGENT GRAPHRAG ACCESS")
    print("=" * 70)
    print()
    
    supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    
    results = {
        'read_access': {},
        'write_access': {},
        'overall_status': 'UNKNOWN'
    }
    
    # Test tables
    tables = [
        'graphrag_resources',
        'graphrag_relationships', 
        'agent_knowledge',
        'agent_coordination'
    ]
    
    # Test READ access
    print("📖 Testing READ Access:")
    print("-" * 70)
    for table in tables:
        try:
            result = supabase.table(table).select('id').limit(1).execute()
            results['read_access'][table] = True
            print(f"✅ {table:30} READ: WORKING")
        except Exception as e:
            results['read_access'][table] = False
            print(f"❌ {table:30} READ: BLOCKED")
            print(f"   Error: {str(e)[:100]}")
    
    print()
    
    # Test WRITE access
    print("✍️  Testing WRITE Access:")
    print("-" * 70)
    for table in tables:
        try:
            # Prepare test data based on table
            if table == 'graphrag_resources':
                test_data = {
                    'file_path': '/test-multi-agent-access',
                    'title': 'Multi-Agent Access Test',
                    'quality_score': 1
                }
                cleanup_field = 'file_path'
                cleanup_value = '/test-multi-agent-access'
            elif table == 'graphrag_relationships':
                test_data = {
                    'source_path': '/test-source',
                    'target_path': '/test-target',
                    'relationship_type': 'test',
                    'confidence_score': 0.5
                }
                cleanup_field = 'source_path'
                cleanup_value = '/test-source'
            elif table == 'agent_knowledge':
                test_data = {
                    'source_type': 'test',
                    'source_name': 'Multi-Agent Access Test',
                    'doc_type': 'test'
                }
                cleanup_field = 'source_name'
                cleanup_value = 'Multi-Agent Access Test'
            elif table == 'agent_coordination':
                test_data = {
                    'agent_name': 'test-agent',
                    'task_claimed': 'Testing multi-agent access',
                    'status': 'testing'
                }
                cleanup_field = 'agent_name'
                cleanup_value = 'test-agent'
            else:
                continue
            
            # Try insert
            result = supabase.table(table).insert(test_data).execute()
            
            # Clean up
            supabase.table(table).delete().eq(cleanup_field, cleanup_value).execute()
            
            results['write_access'][table] = True
            print(f"✅ {table:30} WRITE: WORKING")
            
        except Exception as e:
            results['write_access'][table] = False
            error_msg = str(e)
            
            if 'row-level security' in error_msg.lower():
                print(f"❌ {table:30} WRITE: BLOCKED BY RLS")
            elif 'permission denied' in error_msg.lower():
                print(f"❌ {table:30} WRITE: PERMISSION DENIED")
            else:
                print(f"❌ {table:30} WRITE: BLOCKED")
            
            # Show first 100 chars of error
            if 'message' in error_msg:
                print(f"   Error: {error_msg[:150]}")
    
    print()
    print("=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    
    # Calculate status
    read_working = sum(results['read_access'].values())
    write_working = sum(results['write_access'].values())
    total_tests = len(tables)
    
    print(f"READ Access:  {read_working}/{total_tests} tables working")
    print(f"WRITE Access: {write_working}/{total_tests} tables working")
    print()
    
    if read_working == total_tests and write_working == total_tests:
        results['overall_status'] = 'FULLY OPERATIONAL'
        print("🎉 STATUS: ✅ MULTI-AGENT ACCESS FULLY OPERATIONAL")
        print("   All agents can READ and WRITE to GraphRAG")
        return 0
    elif read_working == total_tests:
        results['overall_status'] = 'READ-ONLY'
        print("⚠️  STATUS: ⚠️  MULTI-AGENT ACCESS READ-ONLY")
        print("   Agents can READ but cannot WRITE to GraphRAG")
        print()
        print("🔧 FIX: Run URGENT-MULTI-AGENT-GRAPHRAG-FIX.sql in Supabase")
        return 1
    else:
        results['overall_status'] = 'BROKEN'
        print("❌ STATUS: ❌ MULTI-AGENT ACCESS BROKEN")
        print("   Agents cannot access GraphRAG properly")
        print()
        print("🔧 FIX: Check API keys and run URGENT-MULTI-AGENT-GRAPHRAG-FIX.sql")
        return 2

if __name__ == "__main__":
    sys.exit(test_multi_agent_access())


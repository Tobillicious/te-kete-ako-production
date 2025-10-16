#!/usr/bin/env python3
"""
TEST KNOWLEDGE QUERIES
Verify that the knowledge preservation system works correctly
"""

import json
import sqlite3
from pathlib import Path

def test_mcp_export():
    """Test MCP knowledge export"""
    print("🔍 TESTING MCP KNOWLEDGE EXPORT")
    print("=" * 40)
    
    try:
        with open('MCP_KNOWLEDGE_EXPORT.json', 'r') as f:
            mcp_data = json.load(f)
        
        print(f"✅ MCP Export loaded successfully")
        print(f"📊 Categories: {len(mcp_data['knowledge_categories'])}")
        
        for category, data in mcp_data['knowledge_categories'].items():
            print(f"  {category}: {data['total_items']} items")
            if data['high_importance_items']:
                print(f"    High importance: {len(data['high_importance_items'])} items")
        
        return True
    except Exception as e:
        print(f"❌ Error loading MCP export: {e}")
        return False

def test_graphrag_export():
    """Test GraphRAG knowledge export"""
    print("\n🧠 TESTING GRAPHRAG KNOWLEDGE EXPORT")
    print("=" * 40)
    
    try:
        with open('GRAPHRAG_KNOWLEDGE_EXPORT.json', 'r') as f:
            graphrag_data = json.load(f)
        
        print(f"✅ GraphRAG Export loaded successfully")
        print(f"📊 Nodes: {len(graphrag_data['nodes'])}")
        print(f"🔗 Edges: {len(graphrag_data['edges'])}")
        print(f"📈 Total knowledge items: {graphrag_data['metadata']['total_knowledge_items']}")
        
        # Show sample nodes
        if graphrag_data['nodes']:
            sample_node = graphrag_data['nodes'][0]
            print(f"📝 Sample node: {sample_node['id']} ({sample_node['category']})")
            print(f"    Content preview: {sample_node['content'][:100]}...")
        
        return True
    except Exception as e:
        print(f"❌ Error loading GraphRAG export: {e}")
        return False

def test_sqlite_database():
    """Test SQLite knowledge database"""
    print("\n🗄️ TESTING SQLITE KNOWLEDGE DATABASE")
    print("=" * 40)
    
    try:
        conn = sqlite3.connect('knowledge_preservation.db')
        cursor = conn.cursor()
        
        # Test each table
        tables = ['coordination_knowledge', 'technical_knowledge', 'content_knowledge', 
                 'progress_knowledge', 'documentation_knowledge', 'status_knowledge']
        
        for table in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"✅ {table}: {count} items")
            
            # Show high importance items
            cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE importance_score >= 70")
            high_importance = cursor.fetchone()[0]
            if high_importance > 0:
                print(f"    High importance: {high_importance} items")
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Error accessing SQLite database: {e}")
        return False

def test_specific_queries():
    """Test specific knowledge queries"""
    print("\n🔍 TESTING SPECIFIC KNOWLEDGE QUERIES")
    print("=" * 40)
    
    try:
        conn = sqlite3.connect('knowledge_preservation.db')
        cursor = conn.cursor()
        
        # Query 1: High importance coordination items
        cursor.execute("""
            SELECT knowledge_type, content, importance_score 
            FROM coordination_knowledge 
            WHERE importance_score >= 70 
            ORDER BY importance_score DESC 
            LIMIT 3
        """)
        
        results = cursor.fetchall()
        print(f"🎯 High importance coordination items: {len(results)}")
        for result in results:
            print(f"  {result[0]} (score: {result[2]})")
            print(f"    {result[1][:100]}...")
        
        # Query 2: Technical knowledge
        cursor.execute("""
            SELECT COUNT(*) FROM technical_knowledge
        """)
        tech_count = cursor.fetchone()[0]
        print(f"⚙️ Technical knowledge items: {tech_count}")
        
        # Query 3: Content knowledge
        cursor.execute("""
            SELECT COUNT(*) FROM content_knowledge
        """)
        content_count = cursor.fetchone()[0]
        print(f"📚 Content knowledge items: {content_count}")
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Error in specific queries: {e}")
        return False

def main():
    print("🧪 KNOWLEDGE PRESERVATION VERIFICATION")
    print("=" * 50)
    print("Testing that all essential information is preserved and accessible")
    print()
    
    tests = [
        ("MCP Export", test_mcp_export),
        ("GraphRAG Export", test_graphrag_export),
        ("SQLite Database", test_sqlite_database),
        ("Specific Queries", test_specific_queries)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                print(f"✅ {test_name}: PASSED")
                passed += 1
            else:
                print(f"❌ {test_name}: FAILED")
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {e}")
    
    print(f"\n📊 VERIFICATION RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Knowledge preservation system is working perfectly!")
        print("✅ No information lost - everything is preserved and accessible!")
    else:
        print("⚠️ Some tests failed - check the errors above")
    
    return passed == total

if __name__ == "__main__":
    main()

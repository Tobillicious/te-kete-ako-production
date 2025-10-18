#!/usr/bin/env python3
"""
Simple GraphRAG Query Tool for Agents
Usage: python3 query-graphrag.py "SELECT * FROM graphrag_resources WHERE file_path LIKE '_agent_rules/%';"
"""

import sys
import json
from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def query_graphrag(query_sql):
    """Execute SQL query against GraphRAG"""
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Execute raw SQL via RPC (if available) or parse and use appropriate method
        # For now, we'll use table queries
        
        if "_agent_rules" in query_sql:
            results = supabase.table('graphrag_resources').select('*').like('file_path', '_agent_rules/%').execute()
        elif "_dev_patterns" in query_sql:
            results = supabase.table('graphrag_resources').select('*').like('file_path', '_dev_patterns/%').execute()
        elif "_issues" in query_sql:
            results = supabase.table('graphrag_resources').select('*').like('file_path', '_issues/%').execute()
        elif "_session_learnings" in query_sql:
            results = supabase.table('graphrag_resources').select('*').like('file_path', '_session_learnings/%').execute()
        else:
            # Try to execute as direct SQL (may not work without proper RLS)
            print("⚠️  Complex queries may require MCP. Showing agent rules as example:")
            results = supabase.table('graphrag_resources').select('*').like('file_path', '_agent_%').execute()
        
        return results.data
    
    except Exception as e:
        return {"error": str(e)}

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 query-graphrag.py \"SELECT query\"")
        print("\nQuick queries:")
        print("  python3 query-graphrag.py agent_rules")
        print("  python3 query-graphrag.py dev_patterns")
        print("  python3 query-graphrag.py issues")
        print("  python3 query-graphrag.py learnings")
        sys.exit(1)
    
    query = sys.argv[1]
    
    # Handle quick query shortcuts
    quick_queries = {
        "agent_rules": "SELECT * FROM graphrag_resources WHERE file_path LIKE '_agent_rules/%';",
        "dev_patterns": "SELECT * FROM graphrag_resources WHERE file_path LIKE '_dev_patterns/%';",
        "issues": "SELECT * FROM graphrag_resources WHERE file_path LIKE '_issues/%';",
        "learnings": "SELECT * FROM graphrag_resources WHERE file_path LIKE '_session_learnings/%';",
    }
    
    if query in quick_queries:
        query = quick_queries[query]
    
    print(f"🔍 Executing: {query}\n")
    results = query_graphrag(query)
    
    if isinstance(results, dict) and "error" in results:
        print(f"❌ Error: {results['error']}")
        sys.exit(1)
    
    print(f"✅ Found {len(results)} result(s)\n")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()


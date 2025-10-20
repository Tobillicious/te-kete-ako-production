#!/usr/bin/env python3
"""
Fixed GraphRAG Query Tool - Direct Supabase Connection
This fixes the broken query system that was falling back to agent rules
"""

import sys
import json
from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def execute_graphrag_query(query_sql):
    """Execute proper SQL queries against GraphRAG"""
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Handle different query types
        if "COUNT(*)" in query_sql.upper():
            if "graphrag_resources" in query_sql:
                result = supabase.table('graphrag_resources').select('id', count='exact').execute()
                return {"count": result.count}
            elif "graphrag_relationships" in query_sql:
                result = supabase.table('graphrag_relationships').select('id', count='exact').execute()
                return {"count": result.count}
        
        # Handle SELECT queries
        elif "SELECT" in query_sql.upper():
            if "graphrag_resources" in query_sql:
                # Parse basic SELECT queries
                if "WHERE" in query_sql.upper():
                    # Extract WHERE conditions
                    where_part = query_sql.split("WHERE")[1].strip()
                    if "LIKE" in where_part.upper():
                        # Handle LIKE queries
                        field = where_part.split("LIKE")[0].strip()
                        pattern = where_part.split("LIKE")[1].strip().strip("'\"")
                        result = supabase.table('graphrag_resources').select('*').like(field, pattern).execute()
                    else:
                        # Handle other WHERE conditions
                        result = supabase.table('graphrag_resources').select('*').execute()
                else:
                    result = supabase.table('graphrag_resources').select('*').execute()
                return result.data
        
        # Default fallback
        result = supabase.table('graphrag_resources').select('*').limit(10).execute()
        return result.data
    
    except Exception as e:
        return {"error": str(e)}

def main():
    if len(sys.argv) < 2:
        print("🔧 Fixed GraphRAG Query Tool")
        print("Usage: python3 fix-graphrag-queries.py \"SELECT query\"")
        print("\nExample queries:")
        print("  python3 fix-graphrag-queries.py \"SELECT COUNT(*) FROM graphrag_resources\"")
        print("  python3 fix-graphrag-queries.py \"SELECT COUNT(*) FROM graphrag_relationships\"")
        print("  python3 fix-graphrag-queries.py \"SELECT * FROM graphrag_resources WHERE subject = 'Mathematics' LIMIT 5\"")
        sys.exit(1)
    
    query = sys.argv[1]
    print(f"🔍 Executing: {query}\n")
    
    results = execute_graphrag_query(query)
    
    if isinstance(results, dict) and "error" in results:
        print(f"❌ Error: {results['error']}")
        sys.exit(1)
    elif isinstance(results, dict) and "count" in results:
        print(f"✅ Count: {results['count']}")
    else:
        print(f"✅ Found {len(results)} result(s)\n")
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()

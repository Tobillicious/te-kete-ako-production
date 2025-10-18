#!/usr/bin/env python3
"""
Query GraphRAG Knowledge Base on Supabase
Access 90k+ documents from other agents
"""

import os
import json
from supabase import create_client, Client

# Supabase connection from repo config
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

def query_agent_knowledge():
    """Query what other agents have discovered"""
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        print("🔍 QUERYING GRAPHRAG KNOWLEDGE BASE")
        print("=" * 70)
        print("")
        
        # Query recent agent work
        print("📊 Recent Agent Discoveries:\n")
        response = supabase.table('agent_knowledge').select('*').limit(20).execute()
        
        if response.data:
            for item in response.data:
                print(f"Agent: {item.get('agent_name', 'Unknown')}")
                print(f"Task: {item.get('task_claimed', 'N/A')}")
                print(f"Category: {item.get('category', 'N/A')}")
                if 'key_insights' in item:
                    print(f"Insights: {item['key_insights'][:200]}...")
                print("")
        
        # Query agent coordination
        print("\n🤝 Agent Coordination Status:\n")
        coord_response = supabase.table('agent_coordination').select('*').order('created_at', desc=True).limit(10).execute()
        
        if coord_response.data:
            for item in coord_response.data:
                print(f"Agent: {item.get('agent_name', 'Unknown')}")
                print(f"Status: {item.get('status', 'N/A')}")
                print(f"Task: {item.get('task_claimed', 'N/A')}")
                print("")
        
        # Count total knowledge
        print("\n📚 Knowledge Base Stats:\n")
        count_response = supabase.table('agent_knowledge').select('*', count='exact').execute()
        print(f"Total Documents: {count_response.count if hasattr(count_response, 'count') else 'Unknown'}")
        
    except Exception as e:
        print(f"⚠️ Error connecting to Supabase: {e}")
        print("\nTrying alternate method...")
        
        # Try reading local cache
        cache_files = [
            'GRAPH_RAG_ENTRIES.json',
            'GRAPHRAG_INSIGHTS.md',
            'MCP_KNOWLEDGE_EXPORT.json'
        ]
        
        for cache_file in cache_files:
            if os.path.exists(cache_file):
                print(f"\n✅ Found local cache: {cache_file}")
                with open(cache_file, 'r') as f:
                    try:
                        data = json.load(f)
                        print(f"   Entries: {len(data) if isinstance(data, list) else 'Multiple'}")
                    except:
                        print(f"   (Markdown file)")

if __name__ == "__main__":
    query_agent_knowledge()


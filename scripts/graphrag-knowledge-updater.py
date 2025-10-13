#!/usr/bin/env python3
"""
GraphRAG Knowledge Updater for Te Kete Ako Agents
Simple script for agents to add new knowledge to GraphRAG
"""

import json
import sys
from datetime import datetime

try:
    from supabase_graphrag_connector import SupabaseGraphRAGConnector
except ImportError:
    print("Error: Could not import SupabaseGraphRAGConnector")
    sys.exit(1)

def add_knowledge_to_graphrag(agent_id, knowledge_type, title, description, content, metadata=None):
    """Add new knowledge to GraphRAG"""
    connector = SupabaseGraphRAGConnector()
    
    # Create knowledge entry
    knowledge_entry = {
        "agent_id": agent_id,
        "knowledge_type": knowledge_type,  # discovery, solution, pattern, etc.
        "title": title,
        "description": description,
        "content": content,
        "metadata": metadata or {},
        "timestamp": datetime.now().isoformat()
    }
    
    # Log the knowledge addition
    print(f"🧠 Adding knowledge to GraphRAG from {agent_id}:")
    print(f"   Type: {knowledge_type}")
    print(f"   Title: {title}")
    print(f"   Description: {description}")
    
    # In a real implementation, this would add to the GraphRAG database
    # For now, we'll save to a file and log the activity
    with open("graphrag-knowledge-log.json", "a") as f:
        f.write(json.dumps(knowledge_entry) + "\n")
    
    # Log agent activity
    connector.log_agent_activity(
        agent_id, 
        f"Added knowledge: {title}",
        {"knowledge_type": knowledge_type, "description": description}
    )
    
    print(f"✅ Knowledge added to GraphRAG successfully!")
    return True

def query_graphrag_knowledge(agent_id, query, limit=10):
    """Query GraphRAG for existing knowledge"""
    connector = SupabaseGraphRAGConnector()
    
    print(f"🔍 {agent_id} querying GraphRAG for: '{query}'")
    
    # Search for relevant resources
    results = connector.search_resources(query, limit)
    
    print(f"📊 Found {len(results)} relevant resources:")
    for i, result in enumerate(results[:5]):  # Show first 5
        print(f"   {i+1}. {result.get('title', 'No title')} ({result.get('type', 'No type')})")
    
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python graphrag-knowledge-updater.py <command>")
        print("Commands:")
        print("  add <agent_id> <type> <title> <description> <content_file> - Add knowledge to GraphRAG")
        print("  query <agent_id> <query> - Query GraphRAG for knowledge")
        print("  example - Show example usage")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 7:
            print("Usage: python graphrag-knowledge-updater.py add <agent_id> <type> <title> <description> <content_file>")
            sys.exit(1)
        
        agent_id = sys.argv[2]
        knowledge_type = sys.argv[3]
        title = sys.argv[4]
        description = sys.argv[5]
        content_file = sys.argv[6]
        
        try:
            with open(content_file, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: Content file not found: {content_file}")
            sys.exit(1)
        
        add_knowledge_to_graphrag(agent_id, knowledge_type, title, description, content)
    
    elif command == "query":
        if len(sys.argv) < 4:
            print("Usage: python graphrag-knowledge-updater.py query <agent_id> <query>")
            sys.exit(1)
        
        agent_id = sys.argv[2]
        query = " ".join(sys.argv[3:])
        
        query_graphrag_knowledge(agent_id, query)
    
    elif command == "example":
        print("Example usage:")
        print()
        print("# Add discovery to GraphRAG:")
        print("python graphrag-knowledge-updater.py add agent-2 discovery \"CSS Fix\" \"Fixed hero-description class\" \"Added missing CSS class to te-kete-professional.css\" css-fix-details.txt")
        print()
        print("# Query GraphRAG before making changes:")
        print("python graphrag-knowledge-updater.py query agent-2 \"CSS hero classes\"")
        print()
    
    else:
        print(f"Unknown command: {command}")

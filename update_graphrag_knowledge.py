#!/usr/bin/env python3
"""
Update GraphRAG with Development Discoveries
Integrates session learning into the persistent knowledge base.
"""

import json
import sys
from neo4j_loader_official import Neo4jKnowledgeLoader

def update_development_knowledge():
    """Update GraphRAG with our development discoveries."""
    print("🧠 Updating GraphRAG with development discoveries...")
    
    # Neo4j connection details (from neo4j_loader_official.py)
    uri = "neo4j+s://cd5763ca.databases.neo4j.io"
    username = "neo4j"
    password = "te0kutquDw1nIft0mcrvxOn_TEEtybBzM9IYf_IQa88"
    
    loader = None
    try:
        # Initialize loader
        loader = Neo4jKnowledgeLoader(uri, username, password)
        
        # Test connection
        if not loader.test_connection():
            print("❌ Failed to connect to Neo4j")
            return False
        
        # Load our development discoveries
        loader.load_development_discoveries('development_knowledge_updates.json')
        
        # Test that our knowledge was added
        print("\n🔍 Verifying knowledge integration...")
        with loader.driver.session() as session:
            # Check development sessions
            result = session.run("MATCH (s:DevelopmentSession) RETURN count(s) as sessions")
            session_count = result.single()['sessions']
            print(f"📅 Development sessions: {session_count}")
            
            # Check knowledge discoveries
            result = session.run("MATCH (k:Knowledge) RETURN count(k) as discoveries")
            discovery_count = result.single()['discoveries']
            print(f"🔍 Knowledge discoveries: {discovery_count}")
            
            # Show recent discoveries
            result = session.run("""
                MATCH (k:Knowledge) 
                WHERE k.session_date = '2025-07-30'
                RETURN k.title as title, k.status as status, k.priority as priority
                ORDER BY k.priority DESC
            """)
            
            print("\n📋 Today's discoveries added to GraphRAG:")
            for record in result:
                status = record.get('status', 'unknown')
                title = record.get('title', 'Unknown')
                priority = record.get('priority', 'unknown')
                status_emoji = "✅" if status == 'resolved' else "⚠️" if status == 'identified' else "🔄"
                print(f"  {status_emoji} {title} ({priority} priority)")
        
        print("\n🎉 GraphRAG knowledge base successfully updated!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating GraphRAG: {e}")
        return False
        
    finally:
        if loader:
            loader.close()

if __name__ == "__main__":
    success = update_development_knowledge()
    sys.exit(0 if success else 1)
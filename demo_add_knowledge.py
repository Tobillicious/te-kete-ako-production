#!/usr/bin/env python3
"""
Demo: How to Add Knowledge to GraphRAG System
Shows how agents can contribute their discoveries to the collective intelligence
"""

from supabase import create_client
import json
from datetime import datetime

# Supabase connection
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def add_agent_knowledge():
    """Demonstrate how to add agent discoveries to the knowledge base"""
    
    print("🧠 DEMO: Adding Knowledge to GraphRAG System")
    print("=" * 60)
    
    # Example: Add a new discovery
    discovery = {
        "source_type": "discovery",
        "source_name": "GraphRAG Demo - Supabase Integration Success",
        "doc_type": "technical_discovery",
        "key_insights": [
            "Supabase GraphRAG system is fully operational with 17,507 resources",
            "Agent Intelligence Amplifier provides 50x intelligence multiplier",
            "199 high cultural integration resources ready for featuring",
            "Orphaned gems identified: 19 excellence resources need connections"
        ],
        "technical_details": {
            "platform_stats": {
                "total_resources": 17507,
                "total_relationships": 239866,
                "cultural_integration": "36.7%",
                "excellence_tier": "57.6%"
            },
            "tools_available": [
                "query_graphrag.py - Basic queries",
                "agent-intelligence-amplifier.py - 50x intelligence",
                "supabase_graphrag_connector.py - Advanced operations"
            ]
        },
        "agents_involved": ["demo-agent"],
        "created_at": datetime.now().isoformat()
    }
    
    try:
        # Add to agent_knowledge table
        result = supabase.table('agent_knowledge').insert(discovery).execute()
        
        if result.data:
            print("✅ Successfully added discovery to agent_knowledge!")
            print(f"   Discovery ID: {result.data[0].get('id', 'unknown')}")
            print(f"   Title: {discovery['source_name']}")
            print(f"   Key Insights: {len(discovery['key_insights'])} insights")
        else:
            print("❌ Failed to add discovery")
            
    except Exception as e:
        print(f"❌ Error adding knowledge: {e}")

def add_resource_relationship():
    """Demonstrate how to add relationships between resources"""
    
    print("\n🔗 DEMO: Adding Resource Relationships")
    print("=" * 60)
    
    # Example: Connect two resources
    relationship = {
        "source_path": "/public/units/y8-digital-kaitiakitanga/lessons/lesson-1-digital-whare.html",
        "target_path": "/public/units/y8-digital-kaitiakitanga/handouts/blueprint-for-my-digital-whare.html",
        "relationship_type": "lesson_uses_handout",
        "confidence": 0.95,
        "reasoning": "Lesson 1 introduces digital whare concept, handout provides practical template",
        "created_at": datetime.now().isoformat()
    }
    
    try:
        # Add to graphrag_relationships table
        result = supabase.table('graphrag_relationships').insert(relationship).execute()
        
        if result.data:
            print("✅ Successfully added relationship!")
            print(f"   Source: {relationship['source_path']}")
            print(f"   Target: {relationship['target_path']}")
            print(f"   Type: {relationship['relationship_type']}")
            print(f"   Confidence: {relationship['confidence']}")
        else:
            print("❌ Failed to add relationship")
            
    except Exception as e:
        print(f"❌ Error adding relationship: {e}")

def query_recent_knowledge():
    """Show how to query recent agent discoveries"""
    
    print("\n🔍 DEMO: Querying Recent Agent Knowledge")
    print("=" * 60)
    
    try:
        # Get recent discoveries
        result = supabase.table('agent_knowledge')\
            .select('source_name, key_insights, created_at')\
            .order('created_at', desc=True)\
            .limit(5)\
            .execute()
        
        if result.data:
            print("📚 Recent Agent Discoveries:")
            for i, discovery in enumerate(result.data, 1):
                name = discovery.get('source_name', 'Unknown')[:50]
                insights = discovery.get('key_insights', [])
                created = discovery.get('created_at', 'Unknown')
                print(f"\n{i}. {name}")
                if insights:
                    print(f"   💡 {insights[0][:80]}...")
                print(f"   📅 {created[:10]}")
        else:
            print("ℹ️  No recent discoveries found")
            
    except Exception as e:
        print(f"❌ Error querying knowledge: {e}")

def main():
    """Run the demonstration"""
    
    print("🚀 GRAPHRAG KNOWLEDGE ADDITION DEMO")
    print("=" * 60)
    print("This demo shows how agents can contribute to the collective intelligence")
    print()
    
    # Test connection first
    try:
        test_result = supabase.table('agent_knowledge').select('*', count='exact').limit(1).execute()
        print(f"✅ Connected to GraphRAG! {test_result.count} knowledge entries")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return
    
    # Run demonstrations
    add_agent_knowledge()
    add_resource_relationship()
    query_recent_knowledge()
    
    print("\n" + "=" * 60)
    print("🎯 KEY TAKEAWAYS:")
    print("1. Use agent_knowledge table to share discoveries")
    print("2. Use graphrag_relationships to connect resources")
    print("3. Query recent knowledge to avoid duplicate work")
    print("4. Always include technical_details for future agents")
    print("5. Use descriptive source_name for discoverability")
    print("\n🌿 Kia kaha! Build the collective intelligence!")

if __name__ == '__main__':
    main()

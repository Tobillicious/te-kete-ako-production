#!/usr/bin/env python3
"""
Test the GraphRAG Phase 1 implementation
"""

import requests
import json
from supabase import create_client, Client

# Configuration
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

def test_direct_sql_function():
    """Test the match_resources SQL function directly"""
    print("🧪 Testing match_resources SQL function...")
    
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # Create a simple test embedding (384 dimensions of zeros)
    test_embedding = [0.0] * 384
    test_embedding[0] = 1.0  # Add some variation
    
    try:
        result = supabase.rpc('match_resources', {
            'query_embedding': test_embedding,
            'match_threshold': 0.0,  # Very low threshold for testing
            'match_count': 5
        }).execute()
        
        if result.data:
            print(f"✅ SQL function works! Found {len(result.data)} resources")
            for resource in result.data[:3]:
                print(f"   - {resource['title']} (similarity: {resource['similarity']:.3f})")
        else:
            print("⚠️ SQL function returned no results")
            
    except Exception as e:
        print(f"❌ SQL function test failed: {e}")

def test_embedding_count():
    """Check how many embeddings we have"""
    print("\n📊 Checking embedding count...")
    
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    try:
        # Count embeddings
        result = supabase.table('resource_embeddings').select('id', count='exact').execute()
        print(f"✅ Total embeddings: {result.count}")
        
        # Count resources
        result = supabase.table('resources').select('id', count='exact').execute()
        print(f"✅ Total resources: {result.count}")
        
    except Exception as e:
        print(f"❌ Count check failed: {e}")

def simulate_semantic_search():
    """Simulate what the Edge Function would do"""
    print("\n🔍 Simulating semantic search...")
    
    # These are test queries a user might make
    test_queries = [
        "Māori culture and traditions",
        "writing skills and essays", 
        "systems thinking social studies",
        "Treaty of Waitangi history",
        "interactive games for learning"
    ]
    
    from sentence_transformers import SentenceTransformer
    
    try:
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        for query in test_queries:
            print(f"\n🔍 Query: '{query}'")
            
            # Generate embedding
            embedding = model.encode(query).tolist()
            
            # Search
            result = supabase.rpc('match_resources', {
                'query_embedding': embedding,
                'match_threshold': 0.3,
                'match_count': 3
            }).execute()
            
            if result.data:
                print(f"   Found {len(result.data)} matches:")
                for resource in result.data:
                    similarity_pct = round(resource['similarity'] * 100)
                    print(f"   • {resource['title']} ({similarity_pct}% match)")
            else:
                print("   No matches found")
                
    except Exception as e:
        print(f"❌ Semantic search simulation failed: {e}")

if __name__ == "__main__":
    print("🌟 Te Kete Ako - GraphRAG Phase 1 Testing")
    print("=" * 50)
    
    test_embedding_count()
    test_direct_sql_function() 
    simulate_semantic_search()
    
    print("\n" + "=" * 50)
    print("🎉 Testing complete! If all tests passed, GraphRAG Phase 1 is working!")
    print("Next steps:")
    print("1. Deploy the Edge Function to Supabase")
    print("2. Create the frontend search interface")
    print("3. Move to GraphRAG Phase 2 (Knowledge Graph)")
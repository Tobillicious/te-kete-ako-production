#!/usr/bin/env python3
"""
Quick GraphRAG connection test
"""
import os
import requests
import json

# Use the same credentials that worked before
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def test_graphrag_connection():
    """Test basic GraphRAG connection and query recent knowledge"""
    headers = {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f'Bearer {SUPABASE_ANON_KEY}',
        'Content-Type': 'application/json'
    }
    
    # Test simple query for recent game improvements
    query = "recent game improvements October 2025 categories patterns validation"
    
    try:
        # Basic connection test
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/documents?select=*&limit=5",
            headers=headers
        )
        
        if response.status_code == 200:
            docs = response.json()
            print(f"✅ GraphRAG Connection: SUCCESS")
            print(f"📊 Documents found: {len(docs)}")
            
            # Look for recent content
            recent_found = False
            for doc in docs:
                content = doc.get('content', '').lower()
                if any(term in content for term in ['game', 'categories', 'patterns', 'october']):
                    recent_found = True
                    print(f"🎮 Found recent game content: {doc.get('title', 'Untitled')[:50]}...")
                    
            if not recent_found:
                print("⚠️  No recent game improvements found in GraphRAG")
                
            return True
        else:
            print(f"❌ GraphRAG Connection: FAILED ({response.status_code})")
            return False
            
    except Exception as e:
        print(f"❌ GraphRAG Connection: ERROR - {e}")
        return False

if __name__ == "__main__":
    print("🔍 Testing GraphRAG Connection...\n")
    test_graphrag_connection()
#!/usr/bin/env python3
"""
INSERT SYNTHESIZED KNOWLEDGE INTO GRAPHRAG
===========================================

Reads knowledge-synthesis-output.json and inserts into Supabase GraphRAG
"""

import json
import os
from supabase import create_client, Client

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

INPUT_FILE = "/Users/admin/Documents/te-kete-ako-clean/knowledge-synthesis-output.json"

def insert_to_graphrag(data):
    """Insert synthesized knowledge entries into GraphRAG"""
    
    if not SUPABASE_KEY:
        print("❌ SUPABASE_KEY not set! Use: export SUPABASE_KEY='your-key'")
        print("   (Get from Supabase Dashboard > Settings > API)")
        return
    
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    print("📤 Inserting knowledge into GraphRAG...")
    print()
    
    insertions = data['graphrag_insertions']
    success_count = 0
    error_count = 0
    
    for i, entry in enumerate(insertions, 1):
        try:
            # Prepare entry for Supabase
            resource = {
                'title': entry['title'],
                'description': entry['description'],
                'path': entry['path'],
                'type': entry['type'],
                'tags': entry['tags'],
                'author': entry.get('author', 'knowledge-synthesis-system')
            }
            
            # Insert
            result = supabase.table('resources').insert(resource).execute()
            
            print(f"✅ [{i}/{len(insertions)}] {entry['title']}")
            success_count += 1
            
        except Exception as e:
            print(f"❌ [{i}/{len(insertions)}] Error: {str(e)[:100]}")
            error_count += 1
    
    print()
    print("=" * 60)
    print(f"✅ Successfully inserted: {success_count}")
    print(f"❌ Errors: {error_count}")
    print("=" * 60)

def main():
    print("🧠 KNOWLEDGE → GRAPHRAG INSERTION")
    print("=" * 60)
    print()
    
    # Load synthesized knowledge
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"📂 Loaded: {INPUT_FILE}")
    print(f"📊 Entries: {len(data['graphrag_insertions'])}")
    print()
    
    # Insert
    insert_to_graphrag(data)
    
    print()
    print("✅ Knowledge now searchable in GraphRAG!")
    print()
    print("Query examples:")
    print("  SELECT * FROM resources WHERE 'archived-knowledge' = ANY(tags);")
    print("  SELECT * FROM resources WHERE type = 'knowledge-synthesis';")
    print("  SELECT * FROM resources WHERE author LIKE 'agent-%';")

if __name__ == "__main__":
    main()


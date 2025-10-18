#!/usr/bin/env python3
"""
🔍 COMPLETE KNOWLEDGE SEARCH
Search across ALL 6,850+ indexed educational resources
"""

import sqlite3
import sys
from pathlib import Path

def search_knowledge(query, limit=20):
    """Search the complete knowledge base"""
    db_path = Path(__file__).parent / 'te-kete-complete-knowledge.db'
    
    if not db_path.exists():
        print("❌ Knowledge base not found! Run build script first.")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # FTS5 search
    cursor.execute('''
    SELECT r.filepath, r.title, r.category, r.word_count,
           snippet(resources_fts, 1, '→ ', ' ←', '...', 50) as snippet
    FROM resources_fts 
    JOIN resources r ON resources_fts.rowid = r.id
    WHERE resources_fts MATCH ?
    ORDER BY rank
    LIMIT ?
    ''', (query, limit))
    
    results = cursor.fetchall()
    
    print(f"\n🔍 Search: '{query}'")
    print("=" * 80)
    print(f"Found {len(results)} results:\n")
    
    for i, (path, title, category, wc, snippet) in enumerate(results, 1):
        print(f"{i}. [{category.upper()}] {title}")
        print(f"   📄 {path}")
        print(f"   📝 {wc:,d} words")
        print(f"   💬 {snippet}")
        print()
    
    # Statistics
    cursor.execute('SELECT COUNT(*), SUM(word_count) FROM resources')
    total, words = cursor.fetchone()
    print(f"💾 Database: {total:,d} resources, {words:,d} total words indexed")
    
    conn.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 search-complete-knowledge.py 'search query'")
        print("\nExamples:")
        print("  python3 search-complete-knowledge.py 'fractions'")
        print("  python3 search-complete-knowledge.py 'te ao māori'")
        print("  python3 search-complete-knowledge.py 'assessment rubric'")
        sys.exit(1)
    
    query = ' '.join(sys.argv[1:])
    search_knowledge(query)


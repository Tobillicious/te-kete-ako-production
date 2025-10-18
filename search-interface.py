#!/usr/bin/env python3
"""
LOCAL SEARCH INTERFACE
Query the complete codebase via command line
"""

import sqlite3
import sys

def search_codebase(query, limit=20):
    """Search the local index"""
    conn = sqlite3.connect("te-kete-local-index.db")
    cursor = conn.cursor()
    
    print(f"🔍 Searching for: '{query}'")
    print("=" * 70)
    
    # Search using FTS5
    cursor.execute('''
        SELECT path, title, type, subject, description
        FROM search_index
        WHERE search_index MATCH ?
        ORDER BY rank
        LIMIT ?
    ''', (query, limit))
    
    results = cursor.fetchall()
    
    if not results:
        print("❌ No results found")
        conn.close()
        return
    
    print(f"✅ Found {len(results)} results:\n")
    
    for i, (path, title, res_type, subject, desc) in enumerate(results, 1):
        print(f"{i}. {title}")
        print(f"   Type: {res_type} | Subject: {subject}")
        print(f"   Path: {path}")
        if desc:
            print(f"   {desc[:100]}...")
        print()
    
    conn.close()

def get_unit_contents(unit_path):
    """Get all lessons in a unit"""
    conn = sqlite3.connect("te-kete-local-index.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT target_path FROM relationships
        WHERE source_path = ? AND relationship_type = 'unit_contains_lesson'
    ''', (unit_path,))
    
    lessons = cursor.fetchall()
    conn.close()
    return [l[0] for l in lessons]

def show_stats():
    """Show database statistics"""
    conn = sqlite3.connect("te-kete-local-index.db")
    cursor = conn.cursor()
    
    print("📊 LOCAL SEARCH ENGINE STATISTICS")
    print("=" * 70)
    
    cursor.execute("SELECT COUNT(*) FROM resources")
    total = cursor.fetchone()[0]
    print(f"\n✅ Total resources: {total}")
    
    cursor.execute("SELECT type, COUNT(*) FROM resources GROUP BY type ORDER BY COUNT(*) DESC")
    print(f"\n📚 By Type:")
    for type_name, count in cursor.fetchall():
        print(f"   {type_name}: {count}")
    
    cursor.execute("SELECT subject, COUNT(*) FROM resources GROUP BY subject ORDER BY COUNT(*) DESC")
    print(f"\n📊 By Subject:")
    for subject, count in cursor.fetchall():
        print(f"   {subject}: {count}")
    
    cursor.execute("SELECT COUNT(*) FROM relationships")
    rels = cursor.fetchone()[0]
    print(f"\n🔗 Relationships mapped: {rels}")
    
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 search-interface.py stats              # Show statistics")
        print("  python3 search-interface.py <query>            # Search content")
        print()
        print("Examples:")
        print("  python3 search-interface.py stats")
        print("  python3 search-interface.py 'algebra patterns'")
        print("  python3 search-interface.py 'cultural identity'")
        sys.exit(1)
    
    if sys.argv[1] == 'stats':
        show_stats()
    else:
        query = ' '.join(sys.argv[1:])
        search_codebase(query)


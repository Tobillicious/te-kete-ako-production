#!/usr/bin/env python3
"""
LOCAL SEARCH ENGINE - No External Dependencies
Complete local search and relationship mapping
"""

import json
import sqlite3
from pathlib import Path
import re
from datetime import datetime

class LocalSearchEngine:
    def __init__(self):
        self.db_path = "te-kete-local-index.db"
        self.conn = sqlite3.connect(self.db_path)
        self.setup_database()
        
    def setup_database(self):
        """Create local SQLite database for all content"""
        print("🗄️  CREATING LOCAL DATABASE")
        print("=" * 70)
        
        cursor = self.conn.cursor()
        
        # Resources table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT UNIQUE NOT NULL,
                title TEXT,
                description TEXT,
                content_preview TEXT,
                type TEXT,
                subject TEXT,
                year_level TEXT,
                cultural_elements TEXT,
                file_size INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Relationships table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS relationships (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_path TEXT,
                target_path TEXT,
                relationship_type TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Search index (FTS5 for full-text search)
        cursor.execute('''
            CREATE VIRTUAL TABLE IF NOT EXISTS search_index 
            USING fts5(
                path, 
                title, 
                description, 
                content_preview,
                type,
                subject
            )
        ''')
        
        self.conn.commit()
        print("✅ Local database created")
        
    def index_all_files(self):
        """Index all educational content"""
        print("\n📊 INDEXING ALL EDUCATIONAL CONTENT")
        print("=" * 70)
        
        exclude = ['node_modules', '.git', '.backup', '.master', '.bak', 
                   '/archive/', '/backups/', '/dist/', 'temp-restore']
        
        cursor = self.conn.cursor()
        indexed = 0
        
        # Index HTML files
        for html_file in Path('public').rglob('*.html'):
            path_str = str(html_file)
            if any(ex in path_str for ex in exclude):
                continue
                
            try:
                content = html_file.read_text(encoding='utf-8', errors='ignore')
                
                # Extract metadata
                title = self._extract_title(content) or html_file.name
                description = self._extract_description(content) or ""
                content_preview = content[:1000]
                
                # Categorize
                res_type = self._determine_type(path_str)
                subject = self._determine_subject(path_str)
                year_level = self._extract_year_level(path_str)
                cultural = self._extract_cultural_elements(content)
                
                # Insert into database
                cursor.execute('''
                    INSERT OR REPLACE INTO resources 
                    (path, title, description, content_preview, type, subject, year_level, cultural_elements, file_size)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    path_str,
                    title[:500],
                    description[:1000],
                    content_preview,
                    res_type,
                    subject,
                    year_level,
                    ','.join(cultural),
                    len(content)
                ))
                
                # Add to search index
                cursor.execute('''
                    INSERT OR REPLACE INTO search_index 
                    (path, title, description, content_preview, type, subject)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (path_str, title, description, content_preview, res_type, subject))
                
                indexed += 1
                
                if indexed % 100 == 0:
                    print(f"   ✅ Indexed {indexed} files...")
                    self.conn.commit()
                    
            except Exception as e:
                pass
        
        self.conn.commit()
        print(f"\n✅ Indexed {indexed} educational files")
        return indexed
    
    def map_relationships(self):
        """Map relationships between files"""
        print("\n🔗 MAPPING RELATIONSHIPS")
        print("=" * 70)
        
        cursor = self.conn.cursor()
        relationships = 0
        
        # Get all resources
        cursor.execute("SELECT path FROM resources")
        all_paths = [row[0] for row in cursor.fetchall()]
        
        # Map unit → lesson relationships
        units = [p for p in all_paths if '/units/' in p and 'index.html' in p]
        lessons = [p for p in all_paths if '/lessons/' in p or 'lesson-' in p.lower()]
        
        for unit_path in units:
            unit_dir = str(Path(unit_path).parent)
            
            for lesson_path in lessons:
                if unit_dir in lesson_path:
                    cursor.execute('''
                        INSERT OR IGNORE INTO relationships 
                        (source_path, target_path, relationship_type)
                        VALUES (?, ?, ?)
                    ''', (unit_path, lesson_path, 'unit_contains_lesson'))
                    relationships += 1
        
        self.conn.commit()
        print(f"✅ Mapped {relationships} relationships")
        return relationships
    
    def _extract_title(self, content):
        """Extract title from HTML"""
        match = re.search(r'<title>([^<]+)</title>', content, re.I)
        if match:
            return match.group(1).strip()
        match = re.search(r'<h1[^>]*>([^<]+)</h1>', content, re.I)
        if match:
            return re.sub(r'<[^>]+>', '', match.group(1)).strip()
        return None
    
    def _extract_description(self, content):
        """Extract description"""
        match = re.search(r'<meta name="description" content="([^"]+)"', content, re.I)
        if match:
            return match.group(1).strip()
        return None
    
    def _determine_type(self, path):
        """Determine content type"""
        path_lower = path.lower()
        if '/units/' in path_lower and 'index.html' in path_lower:
            return 'unit'
        elif '/lessons/' in path_lower or 'lesson-' in path_lower:
            return 'lesson'
        elif '/handouts/' in path_lower or 'handout' in path_lower:
            return 'handout'
        elif '/games/' in path_lower:
            return 'game'
        elif '/tools/' in path_lower:
            return 'tool'
        return 'resource'
    
    def _determine_subject(self, path):
        """Determine subject"""
        path_lower = path.lower()
        if any(x in path_lower for x in ['math', 'algebra', 'geometry', 'statistics']):
            return 'mathematics'
        elif any(x in path_lower for x in ['science', 'physics', 'chemistry', 'ecology']):
            return 'science'
        elif any(x in path_lower for x in ['english', 'literacy', 'writing']):
            return 'english'
        elif any(x in path_lower for x in ['social', 'history', 'walker', 'herangi']):
            return 'social-studies'
        elif any(x in path_lower for x in ['māori', 'maori', 'te-reo']):
            return 'te-reo-maori'
        return 'general'
    
    def _extract_year_level(self, path):
        """Extract year level"""
        match = re.search(r'y(\d+)', path.lower())
        if match:
            return f"Year {match.group(1)}"
        return None
    
    def _extract_cultural_elements(self, content):
        """Extract cultural elements"""
        elements = []
        if re.search(r'whakataukī|whakatauaki', content, re.I):
            elements.append('whakataukī')
        if re.search(r'tikanga', content, re.I):
            elements.append('tikanga')
        if re.search(r'whakapapa', content, re.I):
            elements.append('whakapapa')
        if re.search(r'kaitiakitanga', content, re.I):
            elements.append('kaitiakitanga')
        return elements
    
    def search(self, query, limit=20):
        """Search the local index"""
        cursor = self.conn.cursor()
        
        # FTS5 search
        cursor.execute('''
            SELECT path, title, type, subject, description
            FROM search_index
            WHERE search_index MATCH ?
            ORDER BY rank
            LIMIT ?
        ''', (query, limit))
        
        results = []
        for row in cursor.fetchall():
            results.append({
                'path': row[0],
                'title': row[1],
                'type': row[2],
                'subject': row[3],
                'description': row[4]
            })
        
        return results
    
    def get_stats(self):
        """Get database statistics"""
        cursor = self.conn.cursor()
        
        cursor.execute("SELECT type, COUNT(*) FROM resources GROUP BY type")
        type_counts = dict(cursor.fetchall())
        
        cursor.execute("SELECT subject, COUNT(*) FROM resources GROUP BY subject")
        subject_counts = dict(cursor.fetchall())
        
        cursor.execute("SELECT COUNT(*) FROM resources")
        total = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM relationships")
        relationships = cursor.fetchone()[0]
        
        return {
            'total_resources': total,
            'by_type': type_counts,
            'by_subject': subject_counts,
            'relationships': relationships
        }
    
    def close(self):
        """Close database connection"""
        self.conn.close()

def build_local_search():
    """Build complete local search system"""
    engine = LocalSearchEngine()
    
    # Index everything
    indexed = engine.index_all_files()
    
    # Map relationships
    relationships = engine.map_relationships()
    
    # Get stats
    stats = engine.get_stats()
    
    print("\n" + "=" * 70)
    print("📊 LOCAL SEARCH ENGINE STATS")
    print("=" * 70)
    print(f"\n✅ Total indexed: {stats['total_resources']}")
    print(f"✅ Relationships: {stats['relationships']}")
    
    print(f"\n📚 By Type:")
    for type_name, count in sorted(stats['by_type'].items(), key=lambda x: x[1], reverse=True):
        print(f"   {type_name}: {count}")
    
    print(f"\n📊 By Subject:")
    for subject, count in sorted(stats['by_subject'].items(), key=lambda x: x[1], reverse=True):
        print(f"   {subject}: {count}")
    
    print("\n" + "=" * 70)
    print("✅ LOCAL SEARCH ENGINE READY!")
    print("=" * 70)
    print(f"\n📍 Database: te-kete-local-index.db")
    print("🔍 Use engine.search('query') to search all content")
    print("🔗 All relationships mapped locally")
    
    # Test search
    print("\n🧪 Testing search...")
    results = engine.search("whakapapa cultural")
    print(f"   Found {len(results)} results for 'whakapapa cultural'")
    if results:
        print(f"   Example: {results[0]['title']}")
    
    engine.close()
    return stats

if __name__ == "__main__":
    stats = build_local_search()
    print("\n🎯 Local search engine fully operational!")


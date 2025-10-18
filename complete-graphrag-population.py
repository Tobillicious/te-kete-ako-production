#!/usr/bin/env python3
"""
COMPLETE GRAPHRAG POPULATION
Scan all 11,786 files and populate GraphRAG for full searchability
"""

from pathlib import Path
import json
from collections import defaultdict
from supabase import create_client
import hashlib

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

class CompleteGraphRAGPopulator:
    def __init__(self):
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.stats = defaultdict(int)
        self.files_to_index = []
        
    def scan_all_files(self):
        """Scan entire codebase"""
        print("🔍 SCANNING ALL 11,786 FILES")
        print("=" * 70)
        
        exclude_patterns = ['node_modules', '.git', '.DS_Store', '__pycache__']
        
        for file_path in Path('.').rglob('*'):
            if file_path.is_file():
                # Skip excluded
                if any(pattern in str(file_path) for pattern in exclude_patterns):
                    continue
                    
                self.stats['total_files'] += 1
                
                # Categorize by extension
                suffix = file_path.suffix or 'no_extension'
                self.stats[f'ext_{suffix}'] += 1
                
                # Categorize educational content
                path_str = str(file_path)
                if self._is_educational_content(path_str, suffix):
                    self.files_to_index.append({
                        'path': path_str,
                        'type': self._determine_type(path_str, suffix),
                        'category': self._determine_category(path_str),
                        'file': file_path
                    })
                    self.stats['indexable'] += 1
        
        print(f"✅ Scanned {self.stats['total_files']} files")
        print(f"✅ Found {self.stats['indexable']} indexable educational files")
        
    def _is_educational_content(self, path, suffix):
        """Check if file is educational content worth indexing"""
        if suffix not in ['.html', '.md', '.json']:
            return False
        
        # Educational directories
        edu_paths = ['/public/', '/units/', '/lessons/', '/handouts/', '/games/', 
                     '/tools/', '/curriculum', '/teachers/', '/students/']
        
        # Exclude patterns
        exclude = ['.backup', '.master', '.bak', 'node_modules', '/archive/', '/dist/']
        
        if any(ex in path for ex in exclude):
            return False
            
        return any(edu in path for edu in edu_paths)
    
    def _determine_type(self, path, suffix):
        """Determine content type"""
        path_lower = path.lower()
        if '/lessons/' in path_lower or 'lesson-' in path_lower:
            return 'lesson'
        elif '/handouts/' in path_lower or 'handout' in path_lower:
            return 'handout'
        elif '/units/' in path_lower and 'index.html' in path_lower:
            return 'unit'
        elif '/games/' in path_lower:
            return 'game'
        elif '/tools/' in path_lower:
            return 'tool'
        elif '/curriculum' in path_lower:
            return 'curriculum'
        return 'resource'
    
    def _determine_category(self, path):
        """Determine subject category"""
        path_lower = path.lower()
        if any(x in path_lower for x in ['maths', 'mathematics', 'algebra', 'geometry']):
            return 'mathematics'
        elif any(x in path_lower for x in ['science', 'biology', 'chemistry', 'physics']):
            return 'science'
        elif any(x in path_lower for x in ['english', 'literacy', 'writing', 'reading']):
            return 'english'
        elif any(x in path_lower for x in ['social', 'history', 'civics', 'walker', 'herangi']):
            return 'social-studies'
        elif any(x in path_lower for x in ['te-reo', 'maori', 'māori', 'cultural']):
            return 'te-reo-maori'
        elif any(x in path_lower for x in ['digital', 'technology', 'coding']):
            return 'technology'
        return 'general'
    
    def populate_graphrag(self, batch_size=100):
        """Populate GraphRAG in batches"""
        print(f"\n📊 POPULATING GRAPHRAG")
        print("=" * 70)
        
        indexed = 0
        errors = 0
        
        for i in range(0, len(self.files_to_index), batch_size):
            batch = self.files_to_index[i:i+batch_size]
            
            for item in batch:
                try:
                    file_path = item['file']
                    
                    # Read content
                    if file_path.suffix == '.html':
                        content = file_path.read_text(encoding='utf-8', errors='ignore')
                        title = self._extract_title(content)
                        description = self._extract_description(content)
                    elif file_path.suffix == '.md':
                        content = file_path.read_text(encoding='utf-8', errors='ignore')
                        title = content.split('\n')[0].replace('#', '').strip()[:100]
                        description = content[:500]
                    else:
                        continue
                    
                    # Create resource object
                    resource = {
                        'title': title or file_path.name,
                        'description': description or f"{item['type']} resource",
                        'path': item['path'],
                        'type': item['type'],
                        'subject': item['category'],
                        'content_hash': hashlib.md5(content.encode()).hexdigest()
                    }
                    
                    # Insert or update in GraphRAG
                    result = self.supabase.table('resources').upsert(
                        resource,
                        on_conflict='path'
                    ).execute()
                    
                    indexed += 1
                    
                except Exception as e:
                    errors += 1
                    if errors < 5:  # Show first few errors
                        print(f"   ⚠️  Error: {str(e)[:100]}")
            
            # Progress update
            if (i + batch_size) % 500 == 0:
                print(f"   📊 Progress: {indexed}/{len(self.files_to_index)} files indexed...")
        
        print(f"\n✅ Indexed {indexed} files")
        print(f"⚠️  Errors: {errors}")
        
        return indexed, errors
    
    def _extract_title(self, html_content):
        """Extract title from HTML"""
        import re
        match = re.search(r'<title>([^<]+)</title>', html_content, re.I)
        if match:
            return match.group(1).strip()[:200]
        match = re.search(r'<h1[^>]*>([^<]+)</h1>', html_content, re.I)
        if match:
            return match.group(1).strip()[:200]
        return None
    
    def _extract_description(self, html_content):
        """Extract description from HTML"""
        import re
        match = re.search(r'<meta name="description" content="([^"]+)"', html_content, re.I)
        if match:
            return match.group(1).strip()[:500]
        # Get first paragraph
        match = re.search(r'<p[^>]*>([^<]+)</p>', html_content, re.I)
        if match:
            return match.group(1).strip()[:500]
        return None
    
    def print_summary(self):
        """Print comprehensive summary"""
        print("\n" + "=" * 70)
        print("📊 COMPLETE CODEBASE SUMMARY")
        print("=" * 70)
        
        print(f"\nTotal files: {self.stats['total_files']}")
        print(f"Indexable educational content: {self.stats['indexable']}")
        
        print("\nTop file types:")
        ext_stats = [(k.replace('ext_', ''), v) for k, v in self.stats.items() if k.startswith('ext_')]
        for ext, count in sorted(ext_stats, key=lambda x: x[1], reverse=True)[:15]:
            print(f"   {ext}: {count}")
    
    def run_complete_population(self):
        """Run complete scan and population"""
        self.scan_all_files()
        self.print_summary()
        
        # Save stats before populating
        with open('complete-codebase-stats.json', 'w') as f:
            json.dump(dict(self.stats), f, indent=2)
        
        print(f"\n🚀 Ready to populate GraphRAG with {len(self.files_to_index)} files")
        print("   (This will take a few minutes...)")
        
        indexed, errors = self.populate_graphrag()
        
        print("\n✅ GRAPHRAG POPULATION COMPLETE!")
        print(f"   Indexed: {indexed} files")
        print(f"   Errors: {errors}")
        
        return indexed, errors

if __name__ == "__main__":
    populator = CompleteGraphRAGPopulator()
    populator.run_complete_population()

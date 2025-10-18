#!/usr/bin/env python3
"""
INDEX EVERYTHING TO GRAPHRAG
Index all 80K+ files including backups, integrated-lessons, archives
Complete knowledge graph of entire platform
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path('/Users/admin/Documents/te-kete-ako-clean')

class ComprehensiveFullIndexer:
    def __init__(self):
        self.stats = {
            'total_scanned': 0,
            'indexed': 0,
            'skipped': 0,
            'errors': 0,
            'relationships': 0,
            'by_type': {}
        }
        self.records = []
        
    def should_index(self, filepath):
        """Determine if file should be indexed"""
        # Skip these directories
        skip_dirs = ['node_modules', '.git', '__pycache__', '.venv']
        
        for skip in skip_dirs:
            if skip in str(filepath):
                return False
        
        # Only index these file types
        return filepath.suffix in ['.html', '.json', '.md']
    
    def extract_metadata(self, filepath):
        """Extract metadata from any file"""
        try:
            content = filepath.read_text(encoding='utf-8', errors='ignore')
            
            metadata = {
                'filepath': str(filepath.relative_to(PROJECT_ROOT)),
                'filename': filepath.name,
                'file_type': filepath.suffix[1:],
                'directory': str(filepath.parent.relative_to(PROJECT_ROOT)),
                'size_bytes': filepath.stat().st_size,
                'modified': datetime.fromtimestamp(filepath.stat().st_mtime).isoformat(),
                'is_public': 'public/' in str(filepath),
                'is_backup': 'backup' in str(filepath).lower() or 'archive' in str(filepath).lower()
            }
            
            # Extract from HTML
            if filepath.suffix == '.html':
                # Title
                title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
                metadata['title'] = title_match.group(1).strip() if title_match else filepath.stem
                
                # Meta description
                desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', content, re.IGNORECASE)
                metadata['description'] = desc_match.group(1)[:500] if desc_match else ''
                
                # Year level
                year_match = re.search(r'Year\s*(\d+)|Y(\d+)|year-(\d+)', content, re.IGNORECASE)
                if year_match:
                    metadata['year_level'] = year_match.group(1) or year_match.group(2) or year_match.group(3)
                
                # Subjects
                subjects = []
                content_lower = content.lower()
                if any(word in content_lower for word in ['mathematics', 'math', 'algebra', 'geometry', 'statistics']):
                    subjects.append('Mathematics')
                if any(word in content_lower for word in ['science', 'physics', 'chemistry', 'biology', 'ecology']):
                    subjects.append('Science')
                if any(word in content_lower for word in ['english', 'literacy', 'writing', 'reading']):
                    subjects.append('English')
                if any(word in content_lower for word in ['social studies', 'history', 'geography', 'civics']):
                    subjects.append('Social Studies')
                if any(word in content_lower for word in ['te reo', 'māori language', 'maori language']):
                    subjects.append('Te Reo Māori')
                metadata['subjects'] = subjects
                
                # Cultural elements
                metadata['has_whakatauaki'] = 'whakataukī' in content_lower or 'whakatauaki' in content_lower
                metadata['has_te_reo'] = 'māori' in content_lower or 'maori' in content_lower
                metadata['has_cultural_context'] = 'cultural context' in content_lower or 'te ao māori' in content_lower
                
                # Resource type from path
                path_str = str(filepath).lower()
                if '/lessons/' in path_str or 'lesson-' in path_str:
                    metadata['resource_type'] = 'lesson'
                elif '/handouts/' in path_str or 'handout' in path_str:
                    metadata['resource_type'] = 'handout'
                elif '/units/' in path_str or 'unit-' in path_str:
                    metadata['resource_type'] = 'unit'
                elif '/games/' in path_str or 'game' in path_str:
                    metadata['resource_type'] = 'game'
                elif '/assessment' in path_str:
                    metadata['resource_type'] = 'assessment'
                else:
                    metadata['resource_type'] = 'page'
                
                # Count links
                links = re.findall(r'href=["\'](/[^"\']+)["\']', content)
                metadata['outbound_links'] = len([l for l in links if not l.startswith('http')])
                self.stats['relationships'] += metadata['outbound_links']
            
            # Extract from JSON
            elif filepath.suffix == '.json':
                try:
                    data = json.loads(content)
                    metadata['title'] = data.get('title', data.get('name', filepath.stem))
                    metadata['description'] = str(data.get('description', ''))[:500]
                    metadata['json_keys'] = list(data.keys())[:20]  # First 20 keys
                except:
                    metadata['title'] = filepath.stem
            
            # Extract from Markdown
            elif filepath.suffix == '.md':
                lines = content.split('\n')[:50]  # First 50 lines
                first_heading = next((line for line in lines if line.startswith('#')), None)
                metadata['title'] = first_heading.lstrip('#').strip() if first_heading else filepath.stem
                # Extract first paragraph as description
                paragraphs = [l.strip() for l in lines if l.strip() and not l.startswith('#') and not l.startswith('```')]
                metadata['description'] = paragraphs[0][:500] if paragraphs else ''
            
            # Track by type
            file_type = metadata['file_type']
            self.stats['by_type'][file_type] = self.stats['by_type'].get(file_type, 0) + 1
            
            return metadata
            
        except Exception as e:
            return None
    
    def index_all(self):
        """Index ALL files in project"""
        print('\n🚀 COMPREHENSIVE FULL PROJECT INDEXING')
        print('=' * 70)
        print(f'Scanning entire project: {PROJECT_ROOT}')
        print('This will take a few minutes...\n')
        
        # Scan all files
        for filepath in PROJECT_ROOT.rglob('*'):
            if not filepath.is_file():
                continue
            
            self.stats['total_scanned'] += 1
            
            if not self.should_index(filepath):
                self.stats['skipped'] += 1
                continue
            
            # Extract metadata
            metadata = self.extract_metadata(filepath)
            if metadata:
                self.records.append(metadata)
                self.stats['indexed'] += 1
                
                # Progress indicator
                if self.stats['indexed'] % 500 == 0:
                    print(f'  📊 Indexed {self.stats["indexed"]:,} files...')
            else:
                self.stats['errors'] += 1
        
        # Save complete index
        print(f'\n💾 Saving index of {len(self.records):,} records...')
        
        # Save in chunks (JSON files can't be too large)
        chunk_size = 5000
        for i in range(0, len(self.records), chunk_size):
            chunk = self.records[i:i+chunk_size]
            output_file = f'graphrag-full-index-part{i//chunk_size + 1}.json'
            with open(output_file, 'w') as f:
                json.dump({
                    'part': i//chunk_size + 1,
                    'timestamp': datetime.now().isoformat(),
                    'records': chunk
                }, f, indent=2)
            print(f'  ✅ Saved {output_file} ({len(chunk):,} records)')
        
        # Summary stats
        stats_file = 'graphrag-full-index-stats.json'
        with open(stats_file, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'stats': self.stats,
                'total_records': len(self.records)
            }, f, indent=2)
        
        # Print summary
        print('\n' + '=' * 70)
        print('📊 COMPLETE PROJECT INDEX\n')
        print(f'Total files scanned: {self.stats["total_scanned"]:,}')
        print(f'✅ Successfully indexed: {self.stats["indexed"]:,}')
        print(f'⏭️  Skipped (node_modules, .git, etc): {self.stats["skipped"]:,}')
        print(f'❌ Errors: {self.stats["errors"]:,}')
        print(f'🔗 Relationships mapped: {self.stats["relationships"]:,}')
        
        print(f'\n📁 Files by Type:')
        for file_type, count in sorted(self.stats['by_type'].items(), key=lambda x: x[1], reverse=True):
            print(f'  - {file_type}: {count:,}')
        
        print(f'\n📄 Output: graphrag-full-index-part*.json')
        print(f'📊 Stats: {stats_file}')
        print('\n✅ COMPLETE PROJECT INDEXED!')
        print('=' * 70 + '\n')
        
        return self.records

if __name__ == '__main__':
    indexer = ComprehensiveFullIndexer()
    records = indexer.index_all()
    
    print(f'🎉 Ready to upload {len(records):,} records to GraphRAG!\n')


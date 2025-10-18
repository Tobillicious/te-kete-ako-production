#!/usr/bin/env python3
"""
GRAPHRAG MASS INDEXER - Index EVERYTHING!
Systematically adds all content to GraphRAG with intelligent categorization
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import json

class GraphRAGMassIndexer:
    def __init__(self):
        self.base_path = Path('/Users/admin/Documents/te-kete-ako-clean/public')
        self.indexed = []
        self.relationships = []
        
    def extract_metadata(self, html_path):
        """Extract rich metadata from HTML file"""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
            
            # Extract key information
            title = soup.find('title')
            title = title.text if title else html_path.stem
            
            # Detect cultural elements
            has_te_reo = bool(re.search(r'\b(kia ora|māori|whānau|kaitiakitanga|whakapapa|tikanga|mātauranga)\b', content, re.I))
            has_whakataukī = bool(re.search(r'(whakataukī|"[^"]{20,100}".*translation)', content, re.I))
            cultural_context = has_te_reo or has_whakataukī
            
            # Detect subject
            subject = self.detect_subject(content, html_path)
            year_level = self.detect_year_level(content, html_path)
            resource_type = self.detect_resource_type(html_path)
            
            # Quality heuristics
            quality_score = self.calculate_quality(soup, cultural_context)
            
            return {
                'file_path': str(html_path.relative_to(html_path.parents[4])),
                'title': title[:200],
                'resource_type': resource_type,
                'subject': subject,
                'year_level': year_level,
                'quality_score': quality_score,
                'cultural_context': cultural_context,
                'has_whakataukī': has_whakataukī,
                'has_te_reo': has_te_reo,
                'metadata': {
                    'auto_indexed': True,
                    'word_count': len(content.split()),
                    'has_images': bool(soup.find('img')),
                    'has_interactive': bool(soup.find('script'))
                }
            }
        except Exception as e:
            print(f"Error processing {html_path}: {e}")
            return None
    
    def detect_subject(self, content, path):
        """Intelligently detect subject from content and path"""
        path_str = str(path).lower()
        content_lower = content.lower()
        
        # Path-based detection
        if 'math' in path_str or 'algebra' in path_str or 'geometry' in path_str:
            return 'Mathematics'
        if 'science' in path_str or 'ecology' in path_str or 'physics' in path_str:
            return 'Science'
        if 'english' in path_str or 'writing' in path_str or 'writers' in path_str:
            return 'English'
        if 'digital' in path_str or 'technology' in path_str:
            return 'Technology'
        if 'social' in path_str or 'history' in path_str:
            return 'Social Studies'
        if 'arts' in path_str or 'visual' in path_str:
            return 'Arts'
        if 'te-reo' in path_str or 'māori' in path_str:
            return 'Te Reo Māori'
        
        # Content-based detection
        if any(word in content_lower for word in ['algebra', 'equation', 'geometry', 'calculus']):
            return 'Mathematics'
        if any(word in content_lower for word in ['ecosystem', 'biology', 'chemistry', 'physics']):
            return 'Science'
        if any(word in content_lower for word in ['narrative', 'poetry', 'writing', 'grammar']):
            return 'English'
        
        return 'Cross-Curricular'
    
    def detect_year_level(self, content, path):
        """Detect year level from path and content"""
        path_str = str(path).lower()
        
        # Check path for year indicators
        year_match = re.search(r'y(\d+)', path_str)
        if year_match:
            return f'Year {year_match.group(1)}'
        
        # Check for year level in content
        for year in range(7, 14):
            if f'year {year}' in content.lower():
                return f'Year {year}'
        
        # Check for senior/junior indicators
        if 'senior' in path_str or any(y in path_str for y in ['y11', 'y12', 'y13']):
            return 'Years 11-13'
        if 'junior' in path_str or any(y in path_str for y in ['y7', 'y8', 'y9']):
            return 'Years 7-9'
        
        return 'Years 7-13'
    
    def detect_resource_type(self, path):
        """Detect resource type from path"""
        path_str = str(path).lower()
        
        if '/lessons/' in path_str or 'lesson-plan' in path_str:
            return 'lesson'
        if '/handouts/' in path_str or 'handout' in path_str:
            return 'handout'
        if '/games/' in path_str or 'game' in path_str or 'wordle' in path_str or 'wordsearch' in path_str:
            return 'interactive_game'
        if '/assessments/' in path_str or 'rubric' in path_str or 'assessment' in path_str:
            return 'assessment'
        if '/units/' in path_str and 'index.html' in path_str:
            return 'unit'
        if 'hub' in path_str:
            return 'hub_page'
        if '/components/' in path_str:
            return 'component'
        if 'activity' in path_str or 'practice' in path_str:
            return 'activity'
        
        return 'resource'
    
    def calculate_quality(self, soup, cultural_context):
        """Calculate quality score based on content analysis"""
        score = 70  # Base
        
        # Has structured content
        if soup.find(['h1', 'h2', 'h3']):
            score += 5
        
        # Has navigation
        if soup.find('nav'):
            score += 3
        
        # Has cultural content
        if cultural_context:
            score += 10
        
        # Has interactive elements
        if soup.find('script'):
            score += 5
        
        # Has good typography (professional CSS)
        if soup.find('link', href=re.compile(r'te-kete-professional|transformative')):
            score += 7
        
        return min(score, 100)
    
    def scan_directory(self, directory, limit=1000):
        """Scan directory for HTML files"""
        html_files = list(Path(directory).rglob('*.html'))
        print(f"Found {len(html_files)} HTML files in {directory}")
        
        for html_file in html_files[:limit]:
            metadata = self.extract_metadata(html_file)
            if metadata:
                self.indexed.append(metadata)
        
        return len(self.indexed)
    
    def generate_sql(self):
        """Generate SQL for all indexed resources"""
        sql_statements = []
        
        for resource in self.indexed:
            sql = f"""
INSERT INTO graphrag_resources (file_path, resource_type, title, subject, year_level, quality_score, cultural_context, has_whakataukī, has_te_reo, metadata)
VALUES (
  '{resource['file_path']}',
  '{resource['resource_type']}',
  $${resource['title']}$$,
  '{resource['subject']}',
  '{resource['year_level']}',
  {resource['quality_score']},
  {str(resource['cultural_context']).lower()},
  {str(resource['has_whakataukī']).lower()},
  {str(resource['has_te_reo']).lower()},
  '{json.dumps(resource['metadata'])}'::jsonb
) ON CONFLICT (file_path) DO UPDATE SET quality_score = EXCLUDED.quality_score;"""
            sql_statements.append(sql)
        
        return '\n'.join(sql_statements)
    
    def save_batch_sql(self, filename='graphrag-mass-index.sql', batch_size=50):
        """Save SQL in batches for execution"""
        with open(filename, 'w') as f:
            f.write("-- GRAPHRAG MASS INDEX - Auto-generated\n")
            f.write(f"-- Total resources: {len(self.indexed)}\n\n")
            
            for i in range(0, len(self.indexed), batch_size):
                batch = self.indexed[i:i+batch_size]
                f.write(f"-- Batch {i//batch_size + 1}\n")
                for resource in batch:
                    f.write(f"INSERT INTO graphrag_resources (file_path, resource_type, title, subject, year_level, quality_score, cultural_context, has_whakataukī, has_te_reo, metadata) VALUES ('{resource['file_path']}', '{resource['resource_type']}', $${resource['title']}$$, '{resource['subject']}', '{resource['year_level']}', {resource['quality_score']}, {str(resource['cultural_context']).lower()}, {str(resource['has_whakataukī']).lower()}, {str(resource['has_te_reo']).lower()}, '{json.dumps(resource['metadata'])}'::jsonb) ON CONFLICT (file_path) DO UPDATE SET quality_score = EXCLUDED.quality_score;\n")
                f.write("\n")
        
        print(f"✅ Saved {len(self.indexed)} resources to {filename}")


if __name__ == '__main__':
    print("🧠 GRAPHRAG MASS INDEXER")
    print("=" * 60)
    
    indexer = GraphRAGMassIndexer()
    
    # Scan key directories
    directories = [
        '/Users/admin/Documents/te-kete-ako-clean/public/handouts',
        '/Users/admin/Documents/te-kete-ako-clean/public/lessons',
        '/Users/admin/Documents/te-kete-ako-clean/public/units',
    ]
    
    for directory in directories:
        if os.path.exists(directory):
            count = indexer.scan_directory(directory, limit=500)
            print(f"✅ Scanned {directory}: {count} files")
    
    # Generate SQL
    indexer.save_batch_sql()
    
    print("\n📊 INDEXING COMPLETE")
    print(f"Total resources: {len(indexer.indexed)}")
    print(f"SQL file: graphrag-mass-index.sql")
    print("\n🎯 Ready to import to GraphRAG!")


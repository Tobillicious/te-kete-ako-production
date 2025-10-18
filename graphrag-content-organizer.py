#!/usr/bin/env python3
"""
GraphRAG Content Organizer
Scans all content and uses GraphRAG to intelligently cluster resources into units
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
import sqlite3

# GraphRAG database connection
GRAPHRAG_DB = "knowledge_preservation.db"
PUBLIC_DIR = Path("public")

class ContentOrganizer:
    def __init__(self):
        self.conn = sqlite3.connect(GRAPHRAG_DB)
        self.content_inventory = defaultdict(list)
        
    def scan_all_content(self):
        """Scan all HTML files and categorize them"""
        print("🔍 Scanning all content files...")
        
        for html_file in PUBLIC_DIR.rglob("*.html"):
            if self.should_process(html_file):
                metadata = self.extract_metadata(html_file)
                if metadata:
                    self.content_inventory[metadata['type']].append(metadata)
        
        print(f"\n📊 Content Inventory:")
        for content_type, items in self.content_inventory.items():
            print(f"   {content_type}: {len(items)} files")
    
    def should_process(self, file_path):
        """Filter out system files"""
        exclude_patterns = [
            'node_modules', 'dist', 'backup', 'archive', 
            'components', 'templates', '.hub'
        ]
        return not any(pattern in str(file_path) for pattern in exclude_patterns)
    
    def extract_metadata(self, file_path):
        """Extract metadata from HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine content type
            content_type = self.classify_content(file_path, content)
            
            # Extract key information
            title = self.extract_title(content)
            subject = self.extract_subject(content, file_path)
            year_level = self.extract_year_level(content, file_path)
            cultural_elements = self.has_cultural_context(content)
            
            return {
                'path': str(file_path),
                'type': content_type,
                'title': title,
                'subject': subject,
                'year_level': year_level,
                'has_cultural': cultural_elements,
                'has_whakatauaki': 'whakataukī' in content.lower() or 'whakatauaki' in content.lower(),
                'size': len(content)
            }
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")
            return None
    
    def classify_content(self, file_path, content):
        """Classify content type"""
        path_str = str(file_path).lower()
        
        if 'lesson' in path_str:
            return 'lesson'
        elif 'handout' in path_str:
            return 'handout'
        elif 'unit' in path_str and 'index' in path_str:
            return 'unit-overview'
        elif 'assessment' in path_str or 'rubric' in path_str:
            return 'assessment'
        elif 'game' in path_str:
            return 'game'
        elif 'tool' in path_str or 'generator' in path_str:
            return 'tool'
        elif 'index.html' in path_str:
            return 'index-page'
        else:
            return 'other'
    
    def extract_title(self, content):
        """Extract title from HTML"""
        match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        if match:
            return match.group(1).replace('| Te Kete Ako', '').strip()
        
        match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE)
        if match:
            return re.sub(r'<[^>]+>', '', match.group(1)).strip()
        
        return "Untitled"
    
    def extract_subject(self, content, file_path):
        """Extract subject area"""
        path_str = str(file_path).lower()
        
        subject_keywords = {
            'social studies': ['social', 'history', 'geography', 'civics', 'society'],
            'english': ['english', 'literacy', 'writing', 'reading', 'writer'],
            'mathematics': ['maths', 'math', 'algebra', 'geometry', 'statistics'],
            'science': ['science', 'biology', 'physics', 'chemistry', 'ecology'],
            'technology': ['technology', 'digital', 'coding', 'computer', 'ai'],
            'te reo': ['te-reo', 'reo', 'māori-language'],
            'arts': ['arts', 'visual', 'music', 'drama'],
            'health-pe': ['health', 'pe', 'wellbeing', 'whare-tapa']
        }
        
        for subject, keywords in subject_keywords.items():
            if any(keyword in path_str for keyword in keywords):
                return subject
        
        return 'cross-curricular'
    
    def extract_year_level(self, content, file_path):
        """Extract year level"""
        path_str = str(file_path)
        
        # Check file path for year indicators
        year_match = re.search(r'[yY](\d{1,2})', path_str)
        if year_match:
            year = int(year_match.group(1))
            if 7 <= year <= 13:
                return year
        
        # Check content for year level mentions
        year_match = re.search(r'Year (\d{1,2})', content)
        if year_match:
            year = int(year_match.group(1))
            if 7 <= year <= 13:
                return year
        
        return None
    
    def has_cultural_context(self, content):
        """Check for cultural integration"""
        cultural_markers = [
            'cultural context',
            'te ao māori',
            'mātauranga',
            'tikanga',
            'kaitiakitanga',
            'whānau',
            'iwi'
        ]
        
        content_lower = content.lower()
        return any(marker in content_lower for marker in cultural_markers)
    
    def cluster_into_units(self):
        """Use GraphRAG to suggest unit clustering"""
        print("\n🤖 Using GraphRAG to suggest unit organization...")
        
        cursor = self.conn.cursor()
        
        # Get existing units from GraphRAG
        cursor.execute("""
            SELECT DISTINCT 
                metadata->>'subject_area' as subject,
                metadata->>'year_level' as year_level,
                COUNT(*) as resource_count
            FROM agent_knowledge
            WHERE category = 'lessons'
                AND metadata->>'subject_area' IS NOT NULL
            GROUP BY subject, year_level
            ORDER BY subject, year_level
        """)
        
        existing_clusters = cursor.fetchall()
        
        print("\n📦 Suggested Unit Structure:")
        for subject, year_level, count in existing_clusters:
            if subject and year_level:
                print(f"   {subject} - Year {year_level}: {count} resources")
        
        return existing_clusters
    
    def generate_migration_plan(self):
        """Generate specific file migration recommendations"""
        print("\n📋 Generating migration plan...")
        
        migration_plan = {
            'gold_standard_units': [],
            'good_units': [],
            'needs_organization': [],
            'orphaned_content': []
        }
        
        # Classify units by quality
        for content_type, items in self.content_inventory.items():
            if content_type == 'unit-overview':
                for item in items:
                    if 'y8-systems' in item['path']:
                        migration_plan['gold_standard_units'].append(item)
                    elif 'guided-inquiry' in item['path'] or 'walker' in item['path']:
                        migration_plan['gold_standard_units'].append(item)
                    else:
                        migration_plan['needs_organization'].append(item)
            
            elif content_type in ['lesson', 'handout'] and items:
                # Check if lesson belongs to a unit
                for item in items:
                    if not self.has_parent_unit(item['path']):
                        migration_plan['orphaned_content'].append(item)
        
        print(f"\n🌟 Gold Standard Units: {len(migration_plan['gold_standard_units'])}")
        print(f"📚 Units Needing Organization: {len(migration_plan['needs_organization'])}")
        print(f"🏝️ Orphaned Content: {len(migration_plan['orphaned_content'])}")
        
        return migration_plan
    
    def has_parent_unit(self, file_path):
        """Check if content belongs to a unit"""
        unit_dirs = [
            'y8-systems', 'guided-inquiry', 'walker-unit',
            'writers-toolkit', 'critical-thinking',
            'generated-resources-alpha'
        ]
        return any(unit_dir in file_path for unit_dir in unit_dirs)
    
    def export_organization_report(self, migration_plan):
        """Export detailed report"""
        report = {
            'scan_date': str(Path.cwd()),
            'total_files': sum(len(items) for items in self.content_inventory.values()),
            'content_by_type': {k: len(v) for k, v in self.content_inventory.items()},
            'migration_plan': migration_plan,
            'suggested_units': self.generate_unit_suggestions()
        }
        
        with open('graphrag-organization-report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print("\n✅ Report exported to: graphrag-organization-report.json")
    
    def generate_unit_suggestions(self):
        """Suggest new unit creation based on content clusters"""
        suggestions = []
        
        # Group by subject + year level
        clusters = defaultdict(lambda: defaultdict(list))
        
        for item in self.content_inventory['lesson']:
            if item['subject'] and item['year_level']:
                key = f"{item['subject']}-Y{item['year_level']}"
                clusters[item['subject']][item['year_level']].append(item)
        
        for subject, year_levels in clusters.items():
            for year, lessons in year_levels.items():
                if len(lessons) >= 3:  # Minimum 3 lessons for a unit
                    suggestions.append({
                        'subject': subject,
                        'year_level': year,
                        'lesson_count': len(lessons),
                        'suggested_unit_code': f"Y{year}-{subject[:2].upper()}-01",
                        'lessons': [l['title'] for l in lessons[:5]]  # First 5
                    })
        
        return suggestions

def main():
    print("🏗️ GraphRAG Content Organizer")
    print("=" * 50)
    
    organizer = ContentOrganizer()
    
    # Step 1: Scan all content
    organizer.scan_all_content()
    
    # Step 2: Use GraphRAG for clustering
    organizer.cluster_into_units()
    
    # Step 3: Generate migration plan
    migration_plan = organizer.generate_migration_plan()
    
    # Step 4: Export report
    organizer.export_organization_report(migration_plan)
    
    print("\n✨ Organization analysis complete!")
    print("\n📖 Next Steps:")
    print("   1. Review graphrag-organization-report.json")
    print("   2. Prioritize gold standard units for migration")
    print("   3. Use GraphRAG to map relationships")
    print("   4. Begin systematic reorganization")

if __name__ == "__main__":
    main()


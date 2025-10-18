#!/usr/bin/env python3
"""
GRAPHRAG-GUIDED EXCAVATION
Use knowledge graph to guide systematic goldmine discovery
Query → Find Gaps → Review → Update → Repeat
"""

from supabase import create_client
from pathlib import Path
import json
import re

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

class GraphRAGGuidedExcavator:
    def __init__(self):
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.graphrag_paths = set()
        self.public_files = []
        self.gaps = []
        self.reviewed = []
        
    def load_graphrag_map(self):
        """Load what's already in GraphRAG"""
        print("\n📥 LOADING GRAPHRAG MAP...")
        print("-" * 70)
        
        resources = self.supabase.table('resources').select('path').execute()
        
        # Normalize paths
        for r in resources.data:
            path = r['path'].replace('/public/', '').replace('public/', '')
            self.graphrag_paths.add(path)
        
        print(f"✅ GraphRAG contains: {len(self.graphrag_paths)} unique paths")
    
    def find_gaps_by_category(self, category):
        """Find missing files in a specific category"""
        print(f"\n🔍 FINDING GAPS: {category}")
        print("-" * 70)
        
        # Search patterns for categories
        patterns = {
            'experiences': 'experiences/*.html',
            'professional_dev': 'professional-development/*.html',
            'assessments': 'assessments/*.html',
            'components': 'components/*.html',
            'templates': 'templates/*.html',
            'curriculum_docs': 'curriculum-documents/*.html',
            'tools': 'tools/*.html'
        }
        
        if category not in patterns:
            print(f"⚠️  Unknown category: {category}")
            return []
        
        # Find files in this category
        category_files = list(Path('public').glob(patterns[category]))
        
        # Check which are missing from GraphRAG
        missing = []
        for file_path in category_files:
            rel_path = str(file_path.relative_to('public'))
            if rel_path not in self.graphrag_paths:
                missing.append(rel_path)
        
        print(f"📂 Total files in {category}: {len(category_files)}")
        print(f"✅ In GraphRAG: {len(category_files) - len(missing)}")
        print(f"❌ Missing: {len(missing)}")
        
        if missing:
            print(f"\n📝 Missing files:")
            for m in missing[:10]:
                print(f"  - {m}")
            if len(missing) > 10:
                print(f"  ... and {len(missing) - 10} more")
        
        return missing
    
    def review_and_add(self, file_path, priority='normal'):
        """Review a file and add to GraphRAG"""
        full_path = Path('public') / file_path
        
        if not full_path.exists():
            return False
        
        try:
            content = full_path.read_text(encoding='utf-8', errors='ignore')
            
            # Extract metadata
            title_match = re.search(r'<title>(.*?)</title>', content)
            title = title_match.group(1).replace(' | Te Kete Ako', '').strip() if title_match else full_path.stem
            
            desc_match = re.search(r'<meta name="description" content="(.*?)"', content)
            description = desc_match.group(1) if desc_match else ''
            
            # Determine type
            rtype = self.determine_type(file_path, content)
            
            # Check cultural integration
            cultural_level = self.check_cultural_integration(content)
            
            # Determine subject
            subject = self.determine_subject(file_path, content)
            
            # Create resource
            resource = {
                'title': title[:200],  # Limit length
                'path': file_path,
                'type': rtype,
                'subject': subject,
                'level': self.determine_level(content),
                'description': description[:500] if description else title,
                'featured': priority == 'high',
                'cultural_elements': {'integration_level': cultural_level},
                'tags': self.extract_tags(file_path, content)[:10]
            }
            
            # Add to GraphRAG
            self.supabase.table('resources').insert(resource).execute()
            
            self.reviewed.append({
                'path': file_path,
                'title': title,
                'type': rtype,
                'added': True
            })
            
            return True
            
        except Exception as e:
            print(f"    ⚠️  Error: {str(e)[:60]}...")
            return False
    
    def determine_type(self, path, content):
        """Smart type determination"""
        if 'lesson' in path.lower():
            return 'lesson'
        elif 'handout' in path.lower():
            return 'handout'
        elif 'component' in path.lower():
            return 'component'
        elif 'template' in path.lower():
            return 'template'
        elif 'assessment' in path.lower() or 'rubric' in path.lower():
            return 'assessment'
        elif 'experience' in path.lower() or 'interactive' in path.lower():
            return 'interactive'
        elif 'professional-development' in path.lower():
            return 'professional_development'
        elif 'tool' in path.lower() or 'generator' in path.lower():
            return 'tool'
        else:
            return 'resource'
    
    def check_cultural_integration(self, content):
        """Check cultural integration level"""
        content_lower = content.lower()
        
        has_whakatau = 'whakataukī' in content_lower or 'whakatauaki' in content_lower
        has_tikanga = 'tikanga' in content_lower
        has_cultural_context = 'cultural context' in content_lower or 'horopaki' in content_lower
        
        if has_whakatau and has_tikanga and has_cultural_context:
            return 'essential'
        elif has_whakatau or (has_tikanga and has_cultural_context):
            return 'high'
        elif has_tikanga or has_cultural_context:
            return 'medium'
        else:
            return 'low'
    
    def determine_subject(self, path, content):
        """Determine subject area"""
        path_lower = path.lower()
        content_lower = content.lower()
        
        if 'mathematics' in path_lower or 'math' in path_lower:
            return 'Mathematics'
        elif 'science' in path_lower:
            return 'Science'
        elif 'english' in path_lower:
            return 'English'
        elif 'te reo' in path_lower or 'maori' in path_lower:
            return 'Te Reo Māori'
        elif 'social' in path_lower:
            return 'Social Studies'
        elif 'health' in path_lower:
            return 'Health & PE'
        elif 'technology' in path_lower or 'tech' in path_lower:
            return 'Technology'
        elif 'arts' in path_lower:
            return 'The Arts'
        else:
            return 'Cross-Curricular'
    
    def determine_level(self, content):
        """Determine year level"""
        content_lower = content.lower()
        
        for year in range(7, 14):
            if f'year {year}' in content_lower or f'y{year}' in content_lower:
                return f'Year {year}'
        
        for level in range(1, 9):
            if f'level {level}' in content_lower or f'nzc l{level}' in content_lower:
                return f'Level {level}'
        
        return 'All Levels'
    
    def extract_tags(self, path, content):
        """Extract relevant tags"""
        tags = []
        content_lower = content.lower()
        
        # From path
        if 'cultural' in path.lower():
            tags.append('cultural')
        if 'māori' in path.lower() or 'maori' in path.lower():
            tags.append('māori')
        
        # From content
        if 'whakataukī' in content_lower:
            tags.append('whakataukī')
        if 'tikanga' in content_lower:
            tags.append('tikanga')
        if 'gold' in path.lower() or 'professional' in path.lower():
            tags.append('high-quality')
        
        return tags
    
    def excavate_category(self, category, priority='normal'):
        """Excavate a complete category"""
        print(f"\n💎 EXCAVATING: {category.upper()}")
        print("=" * 70)
        
        # Find gaps
        missing = self.find_gaps_by_category(category)
        
        if not missing:
            print("✅ Category already complete in GraphRAG!")
            return
        
        # Review and add
        print(f"\n📝 REVIEWING AND ADDING {len(missing)} FILES...")
        print("-" * 70)
        
        added = 0
        for file_path in missing[:20]:  # Limit per batch
            print(f"  Processing: {file_path}")
            if self.review_and_add(file_path, priority):
                added += 1
        
        print(f"\n✅ Added {added}/{min(len(missing), 20)} files to GraphRAG")
        
        return added
    
    def run(self, categories=None):
        """Run guided excavation"""
        print("\n" + "🗺️ " * 35)
        print("GRAPHRAG-GUIDED GOLDMINE EXCAVATION")
        print("🗺️ " * 35)
        
        # Load current GraphRAG state
        self.load_graphrag_map()
        
        # Default categories in priority order
        if not categories:
            categories = [
                ('experiences', 'high'),
                ('professional_dev', 'high'),
                ('curriculum_docs', 'high'),
                ('assessments', 'high'),
                ('tools', 'medium'),
                ('components', 'medium'),
                ('templates', 'medium')
            ]
        
        # Excavate each category
        total_added = 0
        for category, priority in categories:
            added = self.excavate_category(category, priority)
            if added:
                total_added += added
        
        # Summary
        print("\n" + "=" * 70)
        print("🎉 EXCAVATION SESSION COMPLETE")
        print("=" * 70)
        print(f"📊 Files added to GraphRAG: {total_added}")
        print(f"📝 Files reviewed: {len(self.reviewed)}")
        print()
        print("💡 GraphRAG is now more complete!")
        print("   Other agents can discover these treasures through queries")
        
        # Save session report
        with open('graphrag-excavation-session.json', 'w') as f:
            json.dump({
                'reviewed': self.reviewed,
                'total_added': total_added
            }, f, indent=2)

if __name__ == '__main__':
    excavator = GraphRAGGuidedExcavator()
    excavator.run()


#!/usr/bin/env python3
"""
GraphRAG Relationship Mapper
Maps relationships between lessons, handouts, units, and resources
"""

from supabase import create_client
from pathlib import Path
from collections import defaultdict
import json
import re

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

class RelationshipMapper:
    def __init__(self):
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.resources = []
        self.relationships = defaultdict(list)
        
    def load_resources(self):
        """Load all resources from GraphRAG"""
        print("📥 Loading resources from GraphRAG...")
        result = self.supabase.table('resources').select('*').execute()
        self.resources = result.data
        print(f"   Loaded {len(self.resources)} resources")
    
    def map_unit_to_lessons(self):
        """Map which lessons belong to which units"""
        print("\n🔗 Mapping Units → Lessons...")
        
        units = [r for r in self.resources if r.get('type') == 'unit']
        lessons = [r for r in self.resources if r.get('type') == 'lesson']
        
        unit_lesson_map = defaultdict(list)
        
        for lesson in lessons:
            lesson_path = lesson.get('path', '')
            lesson_title = lesson.get('title', 'Untitled')
            
            # Find parent unit by path analysis
            for unit in units:
                unit_path = unit.get('path', '')
                if unit_path and unit_path in lesson_path:
                    unit_lesson_map[unit.get('title')].append(lesson_title)
        
        print(f"\n   Found {len(unit_lesson_map)} units with linked lessons:")
        for unit, lessons in sorted(unit_lesson_map.items())[:10]:
            print(f"   📦 {unit}: {len(lessons)} lessons")
        
        self.relationships['unit_lessons'] = dict(unit_lesson_map)
        return unit_lesson_map
    
    def map_lesson_to_handouts(self):
        """Map which handouts support which lessons"""
        print("\n🔗 Mapping Lessons → Handouts...")
        
        lessons = [r for r in self.resources if r.get('type') == 'lesson']
        handouts = [r for r in self.resources if r.get('type') == 'handout']
        
        lesson_handout_map = defaultdict(list)
        
        # Match by shared keywords and themes
        for lesson in lessons:
            lesson_title = lesson.get('title', '').lower()
            lesson_path = lesson.get('path', '').lower()
            
            # Extract key terms
            lesson_terms = self.extract_key_terms(lesson_title + ' ' + lesson_path)
            
            for handout in handouts:
                handout_title = handout.get('title', '').lower()
                handout_path = handout.get('path', '').lower()
                handout_terms = self.extract_key_terms(handout_title + ' ' + handout_path)
                
                # Check for term overlap
                common_terms = lesson_terms & handout_terms
                if len(common_terms) >= 2:  # At least 2 shared terms
                    lesson_handout_map[lesson.get('title')].append({
                        'handout': handout.get('title'),
                        'shared_terms': list(common_terms)
                    })
        
        print(f"\n   Mapped {len(lesson_handout_map)} lessons to handouts")
        print(f"   Sample connections:")
        for lesson, handouts in list(lesson_handout_map.items())[:3]:
            print(f"   📖 {lesson}")
            for h in handouts[:2]:
                print(f"      → {h['handout']} (terms: {', '.join(h['shared_terms'][:3])})")
        
        self.relationships['lesson_handouts'] = dict(lesson_handout_map)
        return lesson_handout_map
    
    def find_prerequisites(self):
        """Identify prerequisite relationships"""
        print("\n🔗 Finding Prerequisites...")
        
        lessons = [r for r in self.resources if r.get('type') == 'lesson']
        prerequisites = defaultdict(list)
        
        # Look for sequential patterns
        for lesson in lessons:
            path = lesson.get('path', '')
            title = lesson.get('title', '')
            
            # Check for lesson numbers
            lesson_num = self.extract_lesson_number(path + ' ' + title)
            if lesson_num and lesson_num > 1:
                # Look for previous lesson
                for other in lessons:
                    other_path = other.get('path', '')
                    other_num = self.extract_lesson_number(other_path + ' ' + other.get('title', ''))
                    
                    if other_num == lesson_num - 1:
                        # Same unit/directory structure
                        if Path(path).parent == Path(other_path).parent:
                            prerequisites[title].append(other.get('title'))
        
        print(f"\n   Found {len(prerequisites)} lessons with prerequisites")
        for lesson, prereqs in list(prerequisites.items())[:5]:
            print(f"   📖 {lesson}")
            for p in prereqs:
                print(f"      ← Requires: {p}")
        
        self.relationships['prerequisites'] = dict(prerequisites)
        return prerequisites
    
    def find_related_by_culture(self):
        """Find resources related by Māori concepts"""
        print("\n🔗 Finding Cultural Connections...")
        
        concept_resources = defaultdict(list)
        
        for resource in self.resources:
            cultural_elements = resource.get('cultural_elements', {})
            if isinstance(cultural_elements, dict):
                concepts = cultural_elements.get('maori_concepts', [])
                if isinstance(concepts, list):
                    for concept in concepts:
                        concept_resources[concept].append({
                            'title': resource.get('title'),
                            'type': resource.get('type')
                        })
        
        # Find resources that share concepts
        print(f"\n   Found {len(concept_resources)} Māori concepts connecting resources:")
        for concept, resources in sorted(concept_resources.items(), key=lambda x: -len(x[1]))[:5]:
            print(f"   🌿 {concept}: {len(resources)} resources")
            for r in resources[:2]:
                print(f"      - [{r['type']}] {r['title'][:50]}")
        
        self.relationships['cultural_connections'] = dict(concept_resources)
        return concept_resources
    
    def extract_key_terms(self, text):
        """Extract key terms from text"""
        # Remove common words
        stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        
        # Extract words
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Filter and return
        return set(w for w in words if len(w) > 3 and w not in stopwords)
    
    def extract_lesson_number(self, text):
        """Extract lesson number from text"""
        # Look for patterns like "lesson 1", "lesson-1", "l1", etc.
        patterns = [
            r'lesson[\s-]*(\d+)',
            r'l[\s-]*(\d+)',
            r'unit[\s-]*(\d+)[\s-]*lesson[\s-]*(\d+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text.lower())
            if match:
                # Get last group (lesson number)
                return int(match.groups()[-1])
        return None
    
    def generate_report(self):
        """Generate comprehensive relationship report"""
        report = {
            'total_resources': len(self.resources),
            'relationships': {
                'unit_to_lessons': len(self.relationships.get('unit_lessons', {})),
                'lesson_to_handouts': len(self.relationships.get('lesson_handouts', {})),
                'prerequisites': len(self.relationships.get('prerequisites', {})),
                'cultural_connections': len(self.relationships.get('cultural_connections', {}))
            },
            'details': self.relationships
        }
        
        with open('graphrag-relationships.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n✅ Relationship map saved to: graphrag-relationships.json")
        
        # Summary
        print(f"\n📊 Relationship Summary:")
        print(f"   Units with lessons: {report['relationships']['unit_to_lessons']}")
        print(f"   Lessons with handouts: {report['relationships']['lesson_to_handouts']}")
        print(f"   Prerequisite chains: {report['relationships']['prerequisites']}")
        print(f"   Cultural connections: {report['relationships']['cultural_connections']}")

def main():
    print("🗺️ GraphRAG Relationship Mapper")
    print("=" * 60)
    
    mapper = RelationshipMapper()
    mapper.load_resources()
    mapper.map_unit_to_lessons()
    mapper.map_lesson_to_handouts()
    mapper.find_prerequisites()
    mapper.find_related_by_culture()
    mapper.generate_report()
    
    print("\n✨ Relationship mapping complete!")
    print("\n📖 Next Steps:")
    print("   1. Review graphrag-relationships.json")
    print("   2. Use relationships to improve navigation")
    print("   3. Create learning pathway suggestions")
    print("   4. Link handouts to appropriate lessons")

if __name__ == "__main__":
    main()


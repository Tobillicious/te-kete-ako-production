#!/usr/bin/env python3
"""
GRAPHRAG QUALITY EXCAVATION
One by one: Find → Review → Verify → Test → Catalog → Document

Quality is EVERYTHING - no batch processing, individual attention to each file
"""

from supabase import create_client
from pathlib import Path
import json
import re
from datetime import datetime

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

class QualityExcavator:
    def __init__(self):
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.graphrag_paths = set()
        self.reviewed = []
        self.session_start = datetime.now()
        
    def load_graphrag_paths(self):
        """Get current GraphRAG state"""
        resources = self.supabase.table('resources').select('path').execute()
        self.graphrag_paths = {self.normalize_path(r['path']) for r in resources.data}
        
    def normalize_path(self, path):
        return path.replace('/public/', '').replace('public/', '')
    
    def find_next_gap(self, directory=None):
        """Find the next file not in GraphRAG"""
        if directory:
            search_path = Path('public') / directory
            files = list(search_path.glob('*.html')) if search_path.exists() else []
        else:
            # Find globally
            files = list(Path('public').rglob('*.html'))
            files = [f for f in files if not any(x in str(f) for x in ['backup', 'node_modules', '.git'])]
        
        for file_path in sorted(files):
            rel_path = str(file_path.relative_to('public'))
            if self.normalize_path(rel_path) not in self.graphrag_paths:
                return rel_path
        
        return None
    
    def deep_review(self, file_path):
        """Deep quality review of a single file"""
        full_path = Path('public') / file_path
        
        print(f"\n{'=' * 70}")
        print(f"📄 REVIEWING: {file_path}")
        print(f"{'=' * 70}")
        
        if not full_path.exists():
            print("❌ File not found!")
            return None
        
        # Read file
        try:
            content = full_path.read_text(encoding='utf-8', errors='ignore')
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            return None
        
        # File stats
        lines = content.split('\n')
        size_kb = len(content) / 1024
        
        print(f"\n📊 FILE STATS:")
        print(f"   Lines: {len(lines)}")
        print(f"   Size: {size_kb:.1f} KB")
        print(f"   Words: ~{len(content.split())}")
        
        # Extract metadata
        review = {
            'path': file_path,
            'lines': len(lines),
            'size_kb': size_kb,
            'checks': {}
        }
        
        # Title check
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).replace(' | Te Kete Ako', '').strip()
            review['title'] = title[:200]
            review['checks']['has_title'] = True
            print(f"   ✅ Title: {title[:60]}{'...' if len(title) > 60 else ''}")
        else:
            review['title'] = full_path.stem
            review['checks']['has_title'] = False
            print(f"   ⚠️  No title found, using filename")
        
        # Description check
        desc_match = re.search(r'<meta name="description" content="(.*?)"', content, re.IGNORECASE)
        if desc_match:
            description = desc_match.group(1)
            review['description'] = description[:500]
            review['checks']['has_description'] = True
            print(f"   ✅ Description: {description[:60]}{'...' if len(description) > 60 else ''}")
        else:
            review['description'] = review['title']
            review['checks']['has_description'] = False
            print(f"   ⚠️  No meta description")
        
        # HTML5 structure check
        review['checks']['has_html5'] = '<html' in content.lower()
        review['checks']['has_head'] = '<head' in content.lower()
        review['checks']['has_body'] = '<body' in content.lower()
        
        # Navigation check
        review['checks']['has_nav'] = '<nav' in content.lower() or 'navigation' in content.lower()
        
        # CSS check
        review['checks']['has_css'] = '<link' in content or '<style' in content.lower()
        
        # Cultural integration check
        cultural_markers = {
            'whakataukī': content.count('whakataukī') + content.count('whakatauaki'),
            'tikanga': content.count('tikanga') + content.count('Tikanga'),
            'māori': content.count('Māori') + content.count('māori') + content.count('Maori'),
            'te_reo': content.count('te reo') + content.count('Te Reo'),
            'cultural_context': content.count('cultural context') + content.count('horopaki')
        }
        
        review['cultural_markers'] = cultural_markers
        total_cultural = sum(cultural_markers.values())
        
        if total_cultural >= 5:
            cultural_level = 'essential'
        elif total_cultural >= 3:
            cultural_level = 'high'
        elif total_cultural >= 1:
            cultural_level = 'medium'
        else:
            cultural_level = 'low'
        
        review['cultural_level'] = cultural_level
        
        print(f"\n🌿 CULTURAL INTEGRATION: {cultural_level.upper()}")
        for marker, count in cultural_markers.items():
            if count > 0:
                print(f"   {marker}: {count}")
        
        # Content type determination
        path_lower = file_path.lower()
        if 'lesson' in path_lower:
            rtype = 'lesson'
        elif 'handout' in path_lower:
            rtype = 'handout'
        elif 'game' in path_lower:
            rtype = 'game'
        elif 'assessment' in path_lower or 'rubric' in path_lower:
            rtype = 'assessment'
        elif 'unit' in path_lower:
            rtype = 'unit-plan'
        elif 'activity' in path_lower:
            rtype = 'activity'
        else:
            rtype = 'interactive'
        
        review['type'] = rtype
        
        # Subject determination
        subjects_map = {
            'math': 'Mathematics', 'science': 'Science', 'english': 'English',
            'te reo': 'Te Reo Māori', 'maori': 'Te Reo Māori', 'social': 'Social Studies',
            'health': 'Health & PE', 'technology': 'Technology', 'arts': 'The Arts'
        }
        
        subject = 'Cross-Curricular'
        for key, value in subjects_map.items():
            if key in path_lower:
                subject = value
                break
        
        review['subject'] = subject
        
        # Quality score (0-100)
        quality_score = 0
        if review['checks']['has_title']:
            quality_score += 15
        if review['checks']['has_description']:
            quality_score += 15
        if review['checks']['has_html5']:
            quality_score += 10
        if review['checks']['has_nav']:
            quality_score += 10
        if review['checks']['has_css']:
            quality_score += 10
        if total_cultural > 0:
            quality_score += min(total_cultural * 5, 30)  # Up to 30 points for cultural
        if size_kb > 5:  # Substantial content
            quality_score += 10
        
        review['quality_score'] = quality_score
        
        print(f"\n⭐ QUALITY SCORE: {quality_score}/100")
        
        # Quality assessment
        if quality_score >= 80:
            quality_rating = "GOLD STANDARD ⭐⭐⭐⭐⭐"
        elif quality_score >= 60:
            quality_rating = "HIGH QUALITY ⭐⭐⭐⭐"
        elif quality_score >= 40:
            quality_rating = "GOOD ⭐⭐⭐"
        else:
            quality_rating = "NEEDS IMPROVEMENT ⚠️"
        
        review['quality_rating'] = quality_rating
        print(f"   {quality_rating}")
        
        print(f"\n📋 SUMMARY:")
        print(f"   Type: {rtype}")
        print(f"   Subject: {subject}")
        print(f"   Cultural Level: {cultural_level}")
        
        return review
    
    def add_to_graphrag(self, review, featured=False):
        """Add reviewed file to GraphRAG"""
        
        resource = {
            'title': review['title'],
            'path': review['path'],
            'type': review['type'],
            'subject': review['subject'],
            'level': 'All Levels',
            'description': review['description'],
            'featured': featured or review['quality_score'] >= 80,
            'cultural_elements': {
                'integration_level': review['cultural_level'],
                'markers': review['cultural_markers']
            }
        }
        
        try:
            self.supabase.table('resources').insert(resource).execute()
            print(f"\n✅ ADDED TO GRAPHRAG")
            self.graphrag_paths.add(self.normalize_path(review['path']))
            return True
        except Exception as e:
            print(f"\n⚠️  GraphRAG Error: {str(e)[:80]}...")
            return False
    
    def excavate_one_by_one(self, directory=None, count=10):
        """Excavate files one by one with full review"""
        
        print("\n" + "🗺️ " * 35)
        print("QUALITY-FIRST GRAPHRAG EXCAVATION")
        print("One by one: Review → Verify → Catalog → Document")
        print("🗺️ " * 35)
        print()
        
        # Load current state
        self.load_graphrag_paths()
        
        print(f"📊 Current GraphRAG: {len(self.graphrag_paths)} resources")
        print(f"🎯 Target: Review {count} files systematically")
        
        if directory:
            print(f"📂 Focus: {directory}")
        else:
            print(f"📂 Searching: Entire public/ directory")
        
        # Review files one by one
        reviewed_count = 0
        added_count = 0
        
        for i in range(count):
            # Find next gap
            next_file = self.find_next_gap(directory)
            
            if not next_file:
                print(f"\n🎉 No more gaps found in {directory or 'public/'}!")
                break
            
            # Deep review
            review = self.deep_review(next_file)
            
            if review:
                # Add to GraphRAG
                if self.add_to_graphrag(review):
                    added_count += 1
                    self.reviewed.append(review)
                
                reviewed_count += 1
                
                # Progress
                print(f"\n📈 Progress: {reviewed_count}/{count} reviewed, {added_count} added")
                
                # Brief pause for readability
                if reviewed_count < count:
                    input("\n⏸️  Press ENTER to continue to next file...")
        
        # Session summary
        print("\n" + "=" * 70)
        print("📊 SESSION SUMMARY")
        print("=" * 70)
        print(f"Files reviewed: {reviewed_count}")
        print(f"Added to GraphRAG: {added_count}")
        print(f"Success rate: {(added_count/reviewed_count*100) if reviewed_count > 0 else 0:.1f}%")
        
        # Quality breakdown
        if self.reviewed:
            avg_quality = sum(r['quality_score'] for r in self.reviewed) / len(self.reviewed)
            gold_count = sum(1 for r in self.reviewed if r['quality_score'] >= 80)
            
            print(f"\nAverage quality score: {avg_quality:.1f}/100")
            print(f"Gold standard files: {gold_count}/{len(self.reviewed)} ({gold_count/len(self.reviewed)*100:.1f}%)")
        
        # Save session log
        session_log = {
            'date': self.session_start.isoformat(),
            'reviewed_count': reviewed_count,
            'added_count': added_count,
            'directory': directory,
            'files': self.reviewed
        }
        
        log_file = f"quality-excavation-{self.session_start.strftime('%Y%m%d-%H%M%S')}.json"
        with open(log_file, 'w') as f:
            json.dump(session_log, f, indent=2)
        
        print(f"\n💾 Session log saved: {log_file}")
        print("\n🎯 Quality-first approach complete!")

if __name__ == '__main__':
    excavator = QualityExcavator()
    
    # Start with components directory (high value, small count)
    excavator.excavate_one_by_one(directory='components', count=10)


#!/usr/bin/env python3
"""
Analyze Te Kete Ako content using existing Supabase GraphRAG
This works with the REAL GraphRAG system
"""

from supabase import create_client
import os
from pathlib import Path
from collections import defaultdict, Counter
import json

# Supabase GraphRAG connection
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

PUBLIC_DIR = Path("public")

class ContentAnalyzer:
    def __init__(self):
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.local_files = set()
        self.graphrag_resources = []
        
    def scan_local_files(self):
        """Scan actual filesystem for HTML files"""
        print("🔍 Scanning local filesystem...")
        
        for html_file in PUBLIC_DIR.rglob("*.html"):
            if self.should_process(html_file):
                rel_path = str(html_file.relative_to(PUBLIC_DIR))
                self.local_files.add(rel_path)
        
        print(f"   Found {len(self.local_files)} HTML files locally")
    
    def should_process(self, file_path):
        """Filter out system files"""
        exclude = ['node_modules', 'dist', 'backup', 'archive', 'components', 'templates', '.hub']
        return not any(pattern in str(file_path) for pattern in exclude)
    
    def get_graphrag_resources(self):
        """Get all resources from Supabase GraphRAG"""
        print("📊 Querying Supabase GraphRAG...")
        
        try:
            result = self.supabase.table('resources').select('*').execute()
            self.graphrag_resources = result.data
            print(f"   Found {len(self.graphrag_resources)} resources in GraphRAG")
            return True
        except Exception as e:
            print(f"   ❌ Error accessing GraphRAG: {e}")
            return False
    
    def analyze_coverage(self):
        """Compare local files vs GraphRAG coverage"""
        print("\n📈 Analyzing GraphRAG Coverage...")
        
        graphrag_paths = set()
        for resource in self.graphrag_resources:
            path = resource.get('path', '')
            if path:
                graphrag_paths.add(path)
        
        in_graphrag = self.local_files & graphrag_paths
        not_in_graphrag = self.local_files - graphrag_paths
        
        coverage = (len(in_graphrag) / len(self.local_files) * 100) if self.local_files else 0
        
        print(f"\n   ✅ In GraphRAG: {len(in_graphrag)} files ({coverage:.1f}%)")
        print(f"   ❌ Not in GraphRAG: {len(not_in_graphrag)} files")
        
        return not_in_graphrag
    
    def analyze_by_type(self):
        """Analyze resources by type"""
        print("\n📁 Resources by Type:")
        
        type_counts = Counter([r.get('type', 'unknown') for r in self.graphrag_resources])
        
        for res_type, count in type_counts.most_common():
            print(f"   {res_type}: {count}")
    
    def analyze_cultural_integration(self):
        """Analyze cultural integration levels"""
        print("\n🌿 Cultural Integration Analysis:")
        
        cultural_levels = []
        for r in self.graphrag_resources:
            cultural_elements = r.get('cultural_elements', {})
            if isinstance(cultural_elements, dict):
                level = cultural_elements.get('cultural_integration')
                if level:
                    cultural_levels.append(level)
        
        if cultural_levels:
            level_counts = Counter(cultural_levels)
            for level, count in level_counts.most_common():
                print(f"   {level}: {count} resources")
        else:
            print("   No cultural integration data found")
    
    def find_unit_clusters(self):
        """Find potential unit groupings from GraphRAG"""
        print("\n🎯 Potential Unit Clusters:")
        
        # Group by subject and year level if available
        clusters = defaultdict(list)
        
        for resource in self.graphrag_resources:
            # Try to extract subject and year from metadata
            metadata = resource.get('metadata', {})
            path = resource.get('path', '')
            
            # Look for year level patterns
            year = None
            for y in range(7, 14):
                if f'y{y}' in path.lower() or f'year-{y}' in path.lower():
                    year = y
                    break
            
            # Look for subject patterns
            subject = 'unknown'
            if 'math' in path.lower(): subject = 'mathematics'
            elif 'science' in path.lower(): subject = 'science'
            elif 'english' in path.lower() or 'literacy' in path.lower(): subject = 'english'
            elif 'social' in path.lower(): subject = 'social-studies'
            elif 'digital' in path.lower() or 'tech' in path.lower(): subject = 'technology'
            
            if year:
                key = f"Y{year}-{subject}"
                clusters[key].append(resource)
        
        # Show clusters with 3+ resources (potential units)
        potential_units = {k: v for k, v in clusters.items() if len(v) >= 3}
        
        if potential_units:
            print(f"\n   Found {len(potential_units)} potential unit clusters:\n")
            for cluster_name, resources in sorted(potential_units.items(), key=lambda x: -len(x[1]))[:15]:
                print(f"   📦 {cluster_name}: {len(resources)} resources")
                # Show first 3 resources in cluster
                for resource in resources[:3]:
                    title = resource.get('title', 'Untitled')[:50]
                    res_type = resource.get('type', '?')
                    print(f"      - [{res_type}] {title}")
                if len(resources) > 3:
                    print(f"      ... and {len(resources) - 3} more")
                print()
        else:
            print("   No clear clusters found (need 3+ resources per cluster)")
    
    def find_orphaned_lessons(self):
        """Find lessons not part of any unit"""
        print("\n🏝️ Orphaned Lessons (Not in Units):")
        
        # Lessons that don't have a parent unit in their path
        orphaned = []
        for resource in self.graphrag_resources:
            if resource.get('type') == 'lesson':
                path = resource.get('path', '')
                # Check if path contains unit directory pattern
                if not any(unit_dir in path for unit_dir in [
                    '/units/', '/y8-systems/', '/guided-inquiry/', 
                    '/writers-toolkit/', '/critical-thinking/'
                ]):
                    orphaned.append(resource)
        
        print(f"   Found {len(orphaned)} orphaned lessons")
        
        # Show first 10
        for resource in orphaned[:10]:
            title = resource.get('title', 'Untitled')[:60]
            path = resource.get('path', 'no path')[:50]
            print(f"   - {title}")
            print(f"     Path: {path}")
        
        if len(orphaned) > 10:
            print(f"\n   ... and {len(orphaned) - 10} more orphaned lessons")
    
    def generate_report(self):
        """Generate comprehensive report"""
        report = {
            'scan_date': str(Path.cwd()),
            'local_files': len(self.local_files),
            'graphrag_resources': len(self.graphrag_resources),
            'analysis': {
                'types': dict(Counter([r.get('type') for r in self.graphrag_resources])),
                'cultural_levels': {},
                'potential_units': {}
            }
        }
        
        # Add cultural levels
        for r in self.graphrag_resources:
            cultural_elements = r.get('cultural_elements', {})
            if isinstance(cultural_elements, dict):
                level = cultural_elements.get('cultural_integration')
                if level:
                    report['analysis']['cultural_levels'][level] = \
                        report['analysis']['cultural_levels'].get(level, 0) + 1
        
        with open('graphrag-content-analysis.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n✅ Report saved to: graphrag-content-analysis.json")

def main():
    print("🏗️ Te Kete Ako Content Analysis (Using Real GraphRAG)")
    print("=" * 60)
    
    analyzer = ContentAnalyzer()
    
    # Step 1: Scan local files
    analyzer.scan_local_files()
    
    # Step 2: Get GraphRAG data
    if not analyzer.get_graphrag_resources():
        print("\n❌ Cannot access GraphRAG. Check Supabase connection.")
        return
    
    # Step 3: Analyze
    analyzer.analyze_coverage()
    analyzer.analyze_by_type()
    analyzer.analyze_cultural_integration()
    analyzer.find_unit_clusters()
    analyzer.find_orphaned_lessons()
    
    # Step 4: Generate report
    analyzer.generate_report()
    
    print("\n✨ Analysis complete!")
    print("\n📖 Next Steps:")
    print("   1. Review graphrag-content-analysis.json")
    print("   2. Use cluster suggestions to create new units")
    print("   3. Update orphaned lessons into appropriate units")
    print("   4. Ensure all content is in GraphRAG")

if __name__ == "__main__":
    main()


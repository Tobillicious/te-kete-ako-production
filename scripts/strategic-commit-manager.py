#!/usr/bin/env python3
"""
STRATEGIC COMMIT MANAGER
Organizes 683 uncommitted changes into logical, atomic commits
"""

import subprocess
import json
import re
from datetime import datetime

class StrategicCommitManager:
    def __init__(self):
        self.changes = []
        self.commit_batches = []
        
    def analyze_changes(self):
        """Analyze all uncommitted changes"""
        print("🔍 ANALYZING 683 UNCOMMITTED CHANGES")
        print("=" * 50)
        
        # Get all uncommitted files
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        
        if result.returncode != 0:
            print("Error getting git status")
            return False
            
        lines = result.stdout.strip().split('\n')
        self.changes = [line for line in lines if line.strip()]
        
        print(f"📊 Total changes: {len(self.changes)}")
        
        # Categorize changes
        categories = {
            'html_files': [],
            'css_files': [],
            'js_files': [],
            'documentation': [],
            'scripts': [],
            'other': []
        }
        
        for change in self.changes:
            status = change[:2]
            filepath = change[3:]
            
            if filepath.endswith('.html'):
                categories['html_files'].append((status, filepath))
            elif filepath.endswith('.css'):
                categories['css_files'].append((status, filepath))
            elif filepath.endswith('.js'):
                categories['js_files'].append((status, filepath))
            elif filepath.endswith('.md'):
                categories['documentation'].append((status, filepath))
            elif filepath.startswith('scripts/'):
                categories['scripts'].append((status, filepath))
            else:
                categories['other'].append((status, filepath))
        
        # Print analysis
        for category, files in categories.items():
            if files:
                print(f"  {category}: {len(files)} files")
        
        return categories
    
    def create_commit_batches(self, categories):
        """Create logical commit batches"""
        print("\n🎯 CREATING STRATEGIC COMMIT BATCHES")
        print("=" * 50)
        
        batches = []
        
        # Batch 1: Core HTML pages (main site)
        main_html = [f for status, f in categories['html_files'] 
                    if not any(x in f for x in ['handouts/', 'lessons/', 'units/', 'integrated-'])]
        if main_html:
            batches.append({
                'name': 'Core HTML Pages',
                'files': main_html,
                'message': 'feat: update core HTML pages with unified navigation'
            })
        
        # Batch 2: Unit pages
        unit_html = [f for status, f in categories['html_files'] 
                    if 'units/' in f]
        if unit_html:
            batches.append({
                'name': 'Unit Pages',
                'files': unit_html,
                'message': 'feat: update unit pages with unified navigation'
            })
        
        # Batch 3: Lesson pages
        lesson_html = [f for status, f in categories['html_files'] 
                      if 'lessons/' in f]
        if lesson_html:
            batches.append({
                'name': 'Lesson Pages',
                'files': lesson_html,
                'message': 'feat: update lesson pages with unified navigation'
            })
        
        # Batch 4: Handout pages
        handout_html = [f for status, f in categories['html_files'] 
                       if 'handouts/' in f]
        if handout_html:
            batches.append({
                'name': 'Handout Pages',
                'files': handout_html,
                'message': 'feat: update handout pages with unified navigation'
            })
        
        # Batch 5: CSS files
        if categories['css_files']:
            batches.append({
                'name': 'CSS Files',
                'files': [f for status, f in categories['css_files']],
                'message': 'feat: update CSS files with unified styling'
            })
        
        # Batch 6: JavaScript files
        if categories['js_files']:
            batches.append({
                'name': 'JavaScript Files',
                'files': [f for status, f in categories['js_files']],
                'message': 'feat: update JavaScript files with unified functionality'
            })
        
        # Batch 7: Documentation
        if categories['documentation']:
            batches.append({
                'name': 'Documentation',
                'files': [f for status, f in categories['documentation']],
                'message': 'docs: update documentation with team coordination protocols'
            })
        
        # Batch 8: Scripts
        if categories['scripts']:
            batches.append({
                'name': 'Scripts',
                'files': [f for status, f in categories['scripts']],
                'message': 'feat: add automation scripts for team coordination'
            })
        
        # Batch 9: Other files
        if categories['other']:
            batches.append({
                'name': 'Other Files',
                'files': [f for status, f in categories['other']],
                'message': 'chore: update remaining files with unified approach'
            })
        
        self.commit_batches = batches
        
        print(f"📦 Created {len(batches)} strategic commit batches:")
        for i, batch in enumerate(batches, 1):
            print(f"  {i}. {batch['name']}: {len(batch['files'])} files")
        
        return batches
    
    def execute_commits(self, dry_run=True):
        """Execute the commit batches"""
        if dry_run:
            print("\n🔍 DRY RUN - COMMIT PLAN:")
            print("=" * 50)
            for i, batch in enumerate(self.commit_batches, 1):
                print(f"\nBatch {i}: {batch['name']}")
                print(f"  Files: {len(batch['files'])}")
                print(f"  Message: {batch['message']}")
                if len(batch['files']) <= 10:
                    for file in batch['files']:
                        print(f"    - {file}")
                else:
                    print(f"    - {batch['files'][0]} ... and {len(batch['files'])-1} more")
        else:
            print("\n🚀 EXECUTING COMMITS:")
            print("=" * 50)
            for i, batch in enumerate(self.commit_batches, 1):
                print(f"\n📦 Batch {i}: {batch['name']}")
                
                # Stage files
                for file in batch['files']:
                    subprocess.run(['git', 'add', file], check=True)
                
                # Commit
                subprocess.run(['git', 'commit', '-m', batch['message']], check=True)
                print(f"  ✅ Committed {len(batch['files'])} files")
    
    def generate_report(self):
        """Generate strategic commit report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_changes': len(self.changes),
            'commit_batches': len(self.commit_batches),
            'batches': []
        }
        
        for batch in self.commit_batches:
            report['batches'].append({
                'name': batch['name'],
                'file_count': len(batch['files']),
                'message': batch['message']
            })
        
        with open('strategic-commit-report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📊 Report saved to: strategic-commit-report.json")
        return report

def main():
    manager = StrategicCommitManager()
    
    # Analyze changes
    categories = manager.analyze_changes()
    if not categories:
        return
    
    # Create commit batches
    batches = manager.create_commit_batches(categories)
    if not batches:
        return
    
    # Generate report
    report = manager.generate_report()
    
    # Show dry run
    manager.execute_commits(dry_run=True)
    
    print(f"\n✅ STRATEGIC COMMIT PLAN READY!")
    print(f"📊 {len(batches)} batches to commit {len(manager.changes)} files")
    print(f"🎯 Ready for execution with --execute flag")

if __name__ == "__main__":
    main()

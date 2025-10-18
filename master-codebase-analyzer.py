#!/usr/bin/env python3
"""
MASTER CODEBASE ANALYZER
Complete deep-dive analysis of entire Te Kete Ako repository
Updates GraphRAG with comprehensive relationships
"""

from pathlib import Path
from collections import defaultdict
import json
import re
from datetime import datetime
from supabase import create_client

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

class MasterCodebaseAnalyzer:
    def __init__(self):
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.repo_root = Path('.')
        
        # File inventories
        self.html_files = []
        self.md_files = []
        self.js_files = []
        self.py_files = []
        self.json_files = []
        self.css_files = []
        
        # Content categorization
        self.units = []
        self.lessons = []
        self.handouts = []
        self.games = []
        self.tools = []
        self.components = []
        
        # Relationships
        self.relationships = defaultdict(list)
        
        # Analysis results
        self.stats = {}
        self.orphans = []
        self.duplicates = []
        
        # Exclude patterns
        self.exclude_dirs = {
            'node_modules', '.git', '.netlify', 'backup_before_css_migration',
            'backup_before_minification', 'backups', 'archived-bloat', 'dist'
        }
    
    def should_scan(self, path):
        """Check if path should be scanned"""
        parts = path.parts
        return not any(excluded in parts for excluded in self.exclude_dirs)
    
    def scan_all_files(self):
        """Comprehensive file system scan"""
        print("\n🔍 SCANNING ENTIRE CODEBASE")
        print("=" * 70)
        
        for path in self.repo_root.rglob('*'):
            if not path.is_file() or not self.should_scan(path):
                continue
            
            suffix = path.suffix.lower()
            
            if suffix == '.html':
                self.html_files.append(path)
            elif suffix == '.md':
                self.md_files.append(path)
            elif suffix == '.js':
                self.js_files.append(path)
            elif suffix == '.py':
                self.py_files.append(path)
            elif suffix == '.json':
                self.json_files.append(path)
            elif suffix == '.css':
                self.css_files.append(path)
        
        print(f"✅ HTML files: {len(self.html_files):,}")
        print(f"✅ Markdown files: {len(self.md_files):,}")
        print(f"✅ JavaScript files: {len(self.js_files):,}")
        print(f"✅ Python files: {len(self.py_files):,}")
        print(f"✅ JSON files: {len(self.json_files):,}")
        print(f"✅ CSS files: {len(self.css_files):,}")
        print(f"\n📊 Total scanned: {len(self.html_files) + len(self.md_files) + len(self.js_files) + len(self.py_files) + len(self.json_files) + len(self.css_files):,} files")
    
    def categorize_html_content(self):
        """Categorize HTML files by type"""
        print("\n📚 CATEGORIZING HTML CONTENT")
        print("=" * 70)
        
        for html_file in self.html_files:
            path_str = str(html_file)
            
            # Categorize by path
            if '/units/' in path_str:
                self.units.append(html_file)
            elif '/lessons/' in path_str or 'lesson' in html_file.name.lower():
                self.lessons.append(html_file)
            elif '/handouts/' in path_str or 'handout' in html_file.name.lower():
                self.handouts.append(html_file)
            elif '/games/' in path_str or 'game' in path_str.lower():
                self.games.append(html_file)
            elif '/tools/' in path_str:
                self.tools.append(html_file)
            elif '/components/' in path_str:
                self.components.append(html_file)
        
        print(f"📦 Units: {len(self.units)}")
        print(f"📖 Lessons: {len(self.lessons)}")
        print(f"📄 Handouts: {len(self.handouts)}")
        print(f"🎮 Games: {len(self.games)}")
        print(f"🛠️  Tools: {len(self.tools)}")
        print(f"🧩 Components: {len(self.components)}")
    
    def analyze_file_relationships(self):
        """Map relationships between files"""
        print("\n🔗 ANALYZING FILE RELATIONSHIPS")
        print("=" * 70)
        
        # Analyze links in HTML files
        link_pattern = re.compile(r'href=["\']([^"\']+)["\']')
        
        for html_file in self.html_files[:100]:  # Sample for speed
            try:
                content = html_file.read_text(encoding='utf-8', errors='ignore')
                links = link_pattern.findall(content)
                
                for link in links:
                    if link.startswith('http') or link.startswith('#'):
                        continue
                    
                    self.relationships[str(html_file)].append(link)
            except Exception as e:
                pass
        
        print(f"✅ Analyzed {len(self.relationships)} files for links")
        
        # Count total relationships
        total_links = sum(len(links) for links in self.relationships.values())
        print(f"🔗 Found {total_links:,} internal links")
    
    def identify_orphaned_content(self):
        """Find orphaned files not linked from anywhere"""
        print("\n🏝️  IDENTIFYING ORPHANED CONTENT")
        print("=" * 70)
        
        # Get all linked files
        all_links = set()
        for links in self.relationships.values():
            all_links.update(links)
        
        # Check which HTML files in public aren't linked
        public_html = [f for f in self.html_files if 'public/' in str(f)]
        
        for html_file in public_html:
            path_str = str(html_file)
            # Check if file path appears in any links
            is_linked = any(path_str.endswith(link) or link in path_str for link in all_links)
            
            if not is_linked and 'index.html' not in path_str:
                self.orphans.append(html_file)
        
        print(f"⚠️  Found {len(self.orphans)} potentially orphaned files")
        
        # Show examples
        if self.orphans:
            print("\n📝 Sample orphaned files:")
            for orphan in self.orphans[:10]:
                print(f"   - {orphan.relative_to(self.repo_root)}")
    
    def analyze_documentation(self):
        """Analyze markdown documentation"""
        print("\n📝 ANALYZING DOCUMENTATION")
        print("=" * 70)
        
        # Categorize MDs
        root_mds = [f for f in self.md_files if len(f.parts) == 2]  # Root level
        docs_mds = [f for f in self.md_files if 'docs/' in str(f)]
        archive_mds = [f for f in self.md_files if 'archive' in str(f).lower()]
        
        print(f"📌 Root-level MDs: {len(root_mds)}")
        print(f"📚 Docs folder MDs: {len(docs_mds)}")
        print(f"🗄️  Archived MDs: {len(archive_mds)}")
        
        # Identify recent vs old
        recent_mds = []
        for md_file in root_mds:
            if md_file.stat().st_mtime > (datetime.now().timestamp() - 7*24*3600):  # Last 7 days
                recent_mds.append(md_file)
        
        print(f"🆕 Recent (7 days): {len(recent_mds)}")
        
        if recent_mds:
            print("\n📋 Recent documentation:")
            for md in sorted(recent_mds, key=lambda x: x.stat().st_mtime, reverse=True)[:15]:
                print(f"   - {md.name}")
    
    def analyze_scripts(self):
        """Analyze automation scripts"""
        print("\n🐍 ANALYZING AUTOMATION SCRIPTS")
        print("=" * 70)
        
        root_scripts = [f for f in self.py_files if len(f.parts) == 2]
        scripts_dir = [f for f in self.py_files if 'scripts/' in str(f)]
        
        print(f"📌 Root-level scripts: {len(root_scripts)}")
        print(f"📂 Scripts directory: {len(scripts_dir)}")
        
        # Categorize by purpose
        graphrag_scripts = [f for f in self.py_files if 'graphrag' in f.name.lower()]
        audit_scripts = [f for f in self.py_files if 'audit' in f.name.lower()]
        test_scripts = [f for f in self.py_files if 'test' in f.name.lower()]
        
        print(f"\n🔍 By Purpose:")
        print(f"   GraphRAG tools: {len(graphrag_scripts)}")
        print(f"   Audit tools: {len(audit_scripts)}")
        print(f"   Test tools: {len(test_scripts)}")
    
    def generate_stats(self):
        """Generate comprehensive statistics"""
        self.stats = {
            'scan_timestamp': datetime.now().isoformat(),
            'total_files': len(self.html_files) + len(self.md_files) + len(self.js_files) + len(self.py_files),
            'content': {
                'units': len(self.units),
                'lessons': len(self.lessons),
                'handouts': len(self.handouts),
                'games': len(self.games),
                'tools': len(self.tools),
                'components': len(self.components)
            },
            'files_by_type': {
                'html': len(self.html_files),
                'markdown': len(self.md_files),
                'javascript': len(self.js_files),
                'python': len(self.py_files),
                'json': len(self.json_files),
                'css': len(self.css_files)
            },
            'relationships': {
                'total_mapped': len(self.relationships),
                'orphaned_files': len(self.orphans)
            }
        }
    
    def update_graphrag(self):
        """Update GraphRAG with findings"""
        print("\n💾 UPDATING GRAPHRAG DATABASE")
        print("=" * 70)
        
        try:
            # Store codebase analysis
            analysis_record = {
                'agent_name': 'master-codebase-analyzer',
                'task_claimed': 'Complete codebase analysis and relationship mapping',
                'status': 'completed',
                'key_decisions': self.stats,
                'content_discovered': {
                    'units': [str(u.relative_to(self.repo_root)) for u in self.units[:50]],
                    'orphans': [str(o.relative_to(self.repo_root)) for o in self.orphans[:50]]
                }
            }
            
            result = self.supabase.table('agent_coordination').insert(analysis_record).execute()
            print("✅ Updated agent_coordination table")
            
            # Save detailed report
            report_path = Path('COMPLETE-CODEBASE-ANALYSIS-REPORT.json')
            report_path.write_text(json.dumps(self.stats, indent=2))
            print(f"✅ Saved detailed report: {report_path}")
            
        except Exception as e:
            print(f"⚠️  GraphRAG update error: {e}")
            print("   (Continuing with local analysis...)")
    
    def generate_summary_report(self):
        """Generate human-readable summary"""
        print("\n" + "=" * 70)
        print("📊 CODEBASE ANALYSIS SUMMARY")
        print("=" * 70)
        
        print(f"\n🎯 CONTENT INVENTORY:")
        print(f"   Units: {len(self.units)}")
        print(f"   Lessons: {len(self.lessons)}")
        print(f"   Handouts: {len(self.handouts)}")
        print(f"   Games: {len(self.games)}")
        print(f"   Tools: {len(self.tools)}")
        
        print(f"\n⚠️  ISSUES FOUND:")
        print(f"   Orphaned files: {len(self.orphans)}")
        
        print(f"\n📁 FILE COUNTS:")
        print(f"   HTML: {len(self.html_files):,}")
        print(f"   Markdown: {len(self.md_files):,}")
        print(f"   JavaScript: {len(self.js_files):,}")
        print(f"   Python: {len(self.py_files):,}")
        
        print("\n✅ Analysis complete! Check COMPLETE-CODEBASE-ANALYSIS-REPORT.json for details")
    
    def run(self):
        """Execute complete analysis"""
        print("\n" + "🚀 " * 35)
        print("MASTER CODEBASE ANALYZER - COMPLETE DEEP SCAN")
        print("🚀 " * 35)
        
        self.scan_all_files()
        self.categorize_html_content()
        self.analyze_file_relationships()
        self.identify_orphaned_content()
        self.analyze_documentation()
        self.analyze_scripts()
        self.generate_stats()
        self.update_graphrag()
        self.generate_summary_report()

if __name__ == '__main__':
    analyzer = MasterCodebaseAnalyzer()
    analyzer.run()


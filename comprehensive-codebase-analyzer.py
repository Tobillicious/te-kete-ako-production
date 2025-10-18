#!/usr/bin/env python3
"""
COMPREHENSIVE CODEBASE ANALYZER
Analyzes EVERYTHING and updates GraphRAG with full relationship map
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
import hashlib

class ComprehensiveAnalyzer:
    def __init__(self):
        self.files_analyzed = 0
        self.relationships = defaultdict(list)
        self.file_inventory = {}
        self.content_index = {}
        self.dependency_graph = defaultdict(set)
        self.cultural_content = defaultdict(list)
        self.maori_terms = defaultdict(int)
        
    def analyze_entire_codebase(self):
        """Scan every accessible file"""
        print("🔍 COMPREHENSIVE CODEBASE ANALYSIS")
        print("=" * 70)
        
        root = Path("/Users/admin/Documents/te-kete-ako-clean")
        
        # Directories to analyze
        targets = [
            root / "public",
            root / "src",
            root / "scripts",
            root / "supabase",
            root / "components",
        ]
        
        for target in targets:
            if target.exists():
                self.scan_directory(target)
        
        print(f"\n✅ Analyzed {self.files_analyzed} files")
        
    def scan_directory(self, directory):
        """Recursively scan directory"""
        for item in directory.rglob("*"):
            # Skip unwanted directories
            if any(skip in str(item) for skip in ['node_modules', '.git', 'backup', 'archive']):
                continue
                
            if item.is_file():
                self.analyze_file(item)
    
    def analyze_file(self, filepath):
        """Deep analysis of single file"""
        try:
            self.files_analyzed += 1
            
            # File metadata
            rel_path = str(filepath.relative_to(Path("/Users/admin/Documents/te-kete-ako-clean")))
            file_type = filepath.suffix
            file_size = filepath.stat().st_size
            
            self.file_inventory[rel_path] = {
                "type": file_type,
                "size": file_size,
                "path": str(filepath)
            }
            
            # Analyze text files
            if file_type in ['.html', '.js', '.css', '.md', '.json', '.py', '.sql']:
                try:
                    content = filepath.read_text(encoding='utf-8', errors='ignore')
                    self.analyze_content(rel_path, content, file_type)
                except:
                    pass
                    
        except Exception as e:
            pass
    
    def analyze_content(self, filepath, content, file_type):
        """Analyze file content for relationships"""
        
        # Find links/imports/references
        if file_type == '.html':
            self.find_html_relationships(filepath, content)
            self.find_cultural_content(filepath, content)
        elif file_type == '.js':
            self.find_js_relationships(filepath, content)
        elif file_type == '.css':
            self.find_css_relationships(filepath, content)
        elif file_type == '.py':
            self.find_python_relationships(filepath, content)
        
        # Index searchable content
        if len(content) < 500000:  # Skip huge files
            self.content_index[filepath] = {
                "hash": hashlib.md5(content.encode()).hexdigest()[:16],
                "lines": content.count('\n'),
                "chars": len(content)
            }
    
    def find_html_relationships(self, filepath, content):
        """Extract HTML relationships"""
        # Links
        links = re.findall(r'href=["\'](.*?)["\']', content)
        for link in links:
            if link and not link.startswith('http') and not link.startswith('#'):
                self.relationships[filepath].append({
                    "type": "links_to",
                    "target": link,
                    "context": "html_href"
                })
        
        # Scripts
        scripts = re.findall(r'src=["\'](.*?\.js)["\']', content)
        for script in scripts:
            self.dependency_graph[filepath].add(script)
            self.relationships[filepath].append({
                "type": "requires_script",
                "target": script
            })
        
        # CSS
        stylesheets = re.findall(r'href=["\'](.*?\.css)["\']', content)
        for css in stylesheets:
            self.dependency_graph[filepath].add(css)
            self.relationships[filepath].append({
                "type": "requires_css",
                "target": css
            })
    
    def find_js_relationships(self, filepath, content):
        """Extract JavaScript relationships"""
        # Imports
        imports = re.findall(r'import.*?["\'](.+?)["\']', content)
        for imp in imports:
            self.dependency_graph[filepath].add(imp)
        
        # Fetch calls
        fetches = re.findall(r'fetch\(["\'](.+?)["\']', content)
        for fetch in fetches:
            self.relationships[filepath].append({
                "type": "fetches",
                "target": fetch
            })
    
    def find_css_relationships(self, filepath, content):
        """Extract CSS relationships"""
        # URL references
        urls = re.findall(r'url\(["\']?(.+?)["\']?\)', content)
        for url in urls:
            if not url.startswith('data:'):
                self.relationships[filepath].append({
                    "type": "references",
                    "target": url
                })
    
    def find_python_relationships(self, filepath, content):
        """Extract Python relationships"""
        # Imports
        imports = re.findall(r'(?:from|import)\s+([a-zA-Z_][a-zA-Z0-9_\.]*)', content)
        for imp in imports:
            self.dependency_graph[filepath].add(imp)
    
    def find_cultural_content(self, filepath, content):
        """Find Māori cultural content"""
        # Common Māori terms
        maori_terms = [
            'whakapapa', 'tikanga', 'mana', 'tapu', 'noa', 'wairua', 
            'mauri', 'whenua', 'tangata whenua', 'mātauranga', 
            'kaitiakitanga', 'manaakitanga', 'whanaungatanga',
            'tino rangatiratanga', 'te tiriti', 'te ao māori',
            'whakataukī', 'karakia', 'hongi', 'pōwhiri'
        ]
        
        content_lower = content.lower()
        for term in maori_terms:
            if term in content_lower:
                self.maori_terms[term] += 1
                self.cultural_content[term].append(filepath)
    
    def generate_relationship_map(self):
        """Generate comprehensive relationship map"""
        print("\n📊 RELATIONSHIP ANALYSIS")
        print("=" * 70)
        
        print(f"\n🔗 Total Relationships: {sum(len(v) for v in self.relationships.values())}")
        print(f"🌐 Files with dependencies: {len(self.dependency_graph)}")
        print(f"🌿 Cultural content files: {len(set(f for files in self.cultural_content.values() for f in files))}")
        
        # Top linked files
        link_counts = defaultdict(int)
        for source, rels in self.relationships.items():
            for rel in rels:
                if rel['type'] == 'links_to':
                    link_counts[rel['target']] += 1
        
        print("\n🔗 Most Linked Resources (Top 10):")
        for target, count in sorted(link_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"   {count:3d}x → {target}")
        
        # Cultural content
        print("\n🌿 Māori Cultural Content Distribution:")
        for term, count in sorted(self.maori_terms.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"   {term:25s} → {count:3d} files")
    
    def export_to_graphrag_format(self):
        """Export to GraphRAG-compatible format"""
        graphrag_data = {
            "metadata": {
                "total_files": self.files_analyzed,
                "file_types": {},
                "total_relationships": sum(len(v) for v in self.relationships.values()),
                "cultural_terms_found": len(self.maori_terms)
            },
            "files": self.file_inventory,
            "relationships": {k: v for k, v in self.relationships.items()},
            "dependencies": {k: list(v) for k, v in self.dependency_graph.items()},
            "cultural_index": {k: v for k, v in self.cultural_content.items()},
            "cultural_term_frequency": dict(self.maori_terms)
        }
        
        # Count file types
        for file_info in self.file_inventory.values():
            ftype = file_info['type']
            graphrag_data["metadata"]["file_types"][ftype] = \
                graphrag_data["metadata"]["file_types"].get(ftype, 0) + 1
        
        with open('comprehensive-codebase-analysis.json', 'w') as f:
            json.dump(graphrag_data, f, indent=2)
        
        print(f"\n✅ Exported to: comprehensive-codebase-analysis.json")
        
        return graphrag_data
    
    def generate_statistics(self):
        """Generate comprehensive statistics"""
        print("\n📈 CODEBASE STATISTICS")
        print("=" * 70)
        
        # File type breakdown
        types = defaultdict(int)
        total_size = 0
        for info in self.file_inventory.values():
            types[info['type']] += 1
            total_size += info['size']
        
        print(f"\n📁 File Type Distribution:")
        for ftype, count in sorted(types.items(), key=lambda x: x[1], reverse=True):
            print(f"   {ftype:10s} → {count:4d} files")
        
        print(f"\n💾 Total Size: {total_size / 1024 / 1024:.1f} MB")
        print(f"📊 Average File Size: {total_size / self.files_analyzed / 1024:.1f} KB")

def main():
    analyzer = ComprehensiveAnalyzer()
    analyzer.analyze_entire_codebase()
    analyzer.generate_relationship_map()
    analyzer.generate_statistics()
    graphrag_data = analyzer.export_to_graphrag_format()
    
    print("\n" + "=" * 70)
    print("✨ COMPREHENSIVE ANALYSIS COMPLETE!")
    print("=" * 70)
    print("\n📊 Summary:")
    print(f"   Files Analyzed: {analyzer.files_analyzed}")
    print(f"   Relationships: {sum(len(v) for v in analyzer.relationships.values())}")
    print(f"   Cultural Files: {len(set(f for files in analyzer.cultural_content.values() for f in files))}")
    print(f"   Māori Terms: {len(analyzer.maori_terms)}")
    print("\n🎯 Next: Use comprehensive-codebase-analysis.json for GraphRAG updates")

if __name__ == "__main__":
    main()

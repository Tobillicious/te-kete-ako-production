#!/usr/bin/env python3
"""
🎯 INTELLIGENT KNOWLEDGE CONSOLIDATION ENGINE
Reduces 3286 MD files to intelligent, searchable knowledge clusters
"""

import os
import json
import re
from datetime import datetime
from collections import defaultdict, Counter
import hashlib

class KnowledgeConsolidationEngine:
    def __init__(self):
        self.root_dir = "/Users/admin/Documents/te-kete-ako-clean"
        self.md_files = []
        self.knowledge_clusters = defaultdict(list)
        self.treasures_found = []

    def discover_md_files(self):
        """Find all MD files, focusing on root level"""
        print("🔍 Discovering MD files...")

        for file in os.listdir(self.root_dir):
            if file.endswith('.md') and not file.startswith('node_modules'):
                filepath = os.path.join(self.root_dir, file)
                self.md_files.append(filepath)

        print(f"📊 Found {len(self.md_files)} root-level MD files")
        return self.md_files

    def analyze_content_patterns(self):
        """Analyze content to find treasures and patterns"""
        print("💎 Hunting for knowledge treasures...")

        content_patterns = {
            'architecture': r'architecture|design|system|technical|implementation',
            'priorities': r'priority|urgent|critical|deadline|milestone',
            'coordination': r'coordination|workflow|agent|collaboration|parallel',
            'cultural': r'cultural|māori|reo|tikanga|kaupapa|whānau',
            'educational': r'lesson|unit|curriculum|learning|student|teacher',
            'progress': r'progress|status|complete|achieve|deliverable'
        }

        for filepath in self.md_files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    filename = os.path.basename(filepath)

                    # Categorize by content patterns
                    for category, pattern in content_patterns.items():
                        if re.search(pattern, content):
                            self.knowledge_clusters[category].append({
                                'file': filename,
                                'path': filepath,
                                'size': len(content),
                                'category': category
                            })

                    # Look for high-value insights
                    if re.search(r'insight|lesson.learned|discovery|breakthrough', content):
                        self.treasures_found.append({
                            'file': filename,
                            'type': 'insight',
                            'value': 'High-value learning discovered'
                        })

            except Exception as e:
                print(f"Error processing {filepath}: {e}")

        print(f"🎯 Found {len(self.treasures_found)} high-value insights")

    def create_knowledge_clusters(self):
        """Create intelligent knowledge clusters"""
        print("🧠 Creating knowledge clusters...")

        clusters = {}

        for category, files in self.knowledge_clusters.items():
            if len(files) < 3:  # Skip small clusters
                continue

            # Group files by similarity
            cluster_content = []
            for file_info in files:
                try:
                    with open(file_info['path'], 'r', encoding='utf-8') as f:
                        content = f.read()
                        cluster_content.append({
                            'title': file_info['file'],
                            'content': content[:1000],  # First 1000 chars for clustering
                            'size': file_info['size']
                        })
                except:
                    continue

            clusters[category] = {
                'file_count': len(files),
                'total_size': sum(f['size'] for f in files),
                'files': [f['file'] for f in files],
                'sample_content': cluster_content[:3]  # Keep samples for reference
            }

        return clusters

    def generate_consolidation_report(self):
        """Generate strategic consolidation recommendations"""
        clusters = self.create_knowledge_clusters()

        report = {
            'timestamp': datetime.now().isoformat(),
            'total_files': len(self.md_files),
            'clusters': clusters,
            'treasures': self.treasures_found,
            'recommendations': self.generate_recommendations(clusters)
        }

        # Save report
        with open(f"{self.root_dir}/knowledge-consolidation-report.json", 'w') as f:
            json.dump(report, f, indent=2)

        return report

    def generate_recommendations(self, clusters):
        """Generate intelligent consolidation recommendations"""
        recommendations = []

        # Priority-based consolidation
        priority_order = ['architecture', 'priorities', 'coordination', 'cultural', 'educational']

        for category in priority_order:
            if category in clusters:
                cluster = clusters[category]
                recommendations.append({
                    'action': 'consolidate',
                    'category': category,
                    'file_count': cluster['file_count'],
                    'priority': 'high' if cluster['file_count'] > 10 else 'medium',
                    'strategy': 'merge_similar_content' if cluster['file_count'] > 5 else 'create_summary'
                })

        # Archive recommendations
        recommendations.append({
            'action': 'archive',
            'target': 'node_modules README files',
            'reason': 'Dependency documentation - not project knowledge',
            'count': 2564
        })

        return recommendations

# Run the consolidation engine
if __name__ == "__main__":
    engine = KnowledgeConsolidationEngine()
    engine.discover_md_files()
    engine.analyze_content_patterns()
    report = engine.generate_consolidation_report()

    print("✅ Knowledge consolidation analysis complete!")
    print(f"📋 Generated report with {len(report['recommendations'])} recommendations")

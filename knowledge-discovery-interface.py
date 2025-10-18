#!/usr/bin/env python3
"""
🔍 KNOWLEDGE DISCOVERY INTERFACE
Makes finding relevant information effortless for agents
"""

import os
import json
import re
from collections import defaultdict
from datetime import datetime

class KnowledgeDiscoveryInterface:
    def __init__(self):
        self.root_dir = "/Users/admin/Documents/te-kete-ako-clean"
        self.knowledge_cache = {}
        self.search_index = {}

    def build_search_index(self):
        """Build a fast search index of all valuable content"""
        print("🏗️ Building knowledge search index...")

        # Index root-level MD files (the important ones)
        for file in os.listdir(self.root_dir):
            if file.endswith('.md') and not file.startswith('node_modules'):
                filepath = os.path.join(self.root_dir, file)
                self._index_file(filepath)

        # Index archived content for historical knowledge
        archive_dirs = [
            'archive/documentation-history',
            'docs/archive'
        ]

        for archive_dir in archive_dirs:
            archive_path = os.path.join(self.root_dir, archive_dir)
            if os.path.exists(archive_path):
                for root, dirs, files in os.walk(archive_path):
                    for file in files:
                        if file.endswith('.md'):
                            filepath = os.path.join(root, file)
                            self._index_file(filepath, is_archived=True)

        print(f"📚 Indexed {len(self.search_index)} knowledge chunks")

    def _index_file(self, filepath, is_archived=False):
        """Index a file for fast searching"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split into searchable chunks
            chunks = self._split_into_chunks(content)

            for i, chunk in enumerate(chunks):
                chunk_id = f"{os.path.basename(filepath)}_chunk_{i}"

                # Extract key information
                self.search_index[chunk_id] = {
                    'filepath': filepath,
                    'chunk': chunk,
                    'is_archived': is_archived,
                    'size': len(chunk),
                    'keywords': self._extract_keywords(chunk),
                    'category': self._categorize_content(chunk)
                }

        except Exception as e:
            print(f"Error indexing {filepath}: {e}")

    def _split_into_chunks(self, content, chunk_size=1000):
        """Split content into searchable chunks"""
        chunks = []
        words = content.split()

        for i in range(0, len(words), chunk_size // 6):  # Approximate chunks
            chunk_words = words[i:i + chunk_size // 6]
            chunks.append(' '.join(chunk_words))

        return chunks[:5]  # Limit to first 5 chunks per file

    def _extract_keywords(self, text):
        """Extract important keywords from text"""
        # Remove common stop words and extract meaningful terms
        stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        words = re.findall(r'\b\w{4,}\b', text.lower())  # Words 4+ chars

        # Count frequency and return top keywords
        word_count = defaultdict(int)
        for word in words:
            if word not in stop_words:
                word_count[word] += 1

        return [word for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]]

    def _categorize_content(self, text):
        """Categorize content type"""
        text_lower = text.lower()

        if re.search(r'architecture|design|system|technical', text_lower):
            return 'architecture'
        elif re.search(r'priority|urgent|critical|deadline', text_lower):
            return 'priorities'
        elif re.search(r'coordination|workflow|agent|parallel', text_lower):
            return 'coordination'
        elif re.search(r'cultural|māori|reo|tikanga', text_lower):
            return 'cultural'
        elif re.search(r'lesson|unit|curriculum|learning', text_lower):
            return 'educational'
        elif re.search(r'progress|status|complete|achieve', text_lower):
            return 'progress'
        else:
            return 'general'

    def search_knowledge(self, query, limit=10, category=None):
        """Search for relevant knowledge"""
        query_lower = query.lower()
        results = []

        for chunk_id, chunk_data in self.search_index.items():
            # Filter by category if specified
            if category and chunk_data['category'] != category:
                continue

            # Calculate relevance score
            relevance = self._calculate_relevance(query_lower, chunk_data)

            if relevance > 0.1:  # Minimum relevance threshold
                results.append({
                    'chunk_id': chunk_id,
                    'filepath': chunk_data['filepath'],
                    'category': chunk_data['category'],
                    'is_archived': chunk_data['is_archived'],
                    'relevance_score': relevance,
                    'keywords': chunk_data['keywords'][:5],  # Top 5 keywords
                    'preview': chunk_data['chunk'][:200] + '...'  # Preview text
                })

        # Sort by relevance and return top results
        return sorted(results, key=lambda x: x['relevance_score'], reverse=True)[:limit]

    def _calculate_relevance(self, query, chunk_data):
        """Calculate relevance score for a chunk"""
        relevance = 0.0
        chunk_text = chunk_data['chunk'].lower()

        # Direct query match
        if query in chunk_text:
            relevance += 0.6

        # Keyword matches
        for keyword in chunk_data['keywords']:
            if keyword in query or query in keyword:
                relevance += 0.2

        # Category relevance (bonus for matching categories)
        query_words = set(query.split())
        for word in query_words:
            if word in chunk_data['category']:
                relevance += 0.1

        return min(relevance, 1.0)

    def get_knowledge_clusters(self):
        """Get overview of knowledge clusters"""
        clusters = defaultdict(list)

        for chunk_id, chunk_data in self.search_index.items():
            category = chunk_data['category']
            clusters[category].append({
                'file': os.path.basename(chunk_data['filepath']),
                'is_archived': chunk_data['is_archived'],
                'keyword_count': len(chunk_data['keywords'])
            })

        # Summarize clusters
        cluster_summary = {}
        for category, files in clusters.items():
            cluster_summary[category] = {
                'file_count': len(files),
                'archived_files': sum(1 for f in files if f['is_archived']),
                'active_files': sum(1 for f in files if not f['is_archived']),
                'total_keywords': sum(f['keyword_count'] for f in files)
            }

        return cluster_summary

    def generate_discovery_report(self):
        """Generate a report of discovered knowledge"""
        clusters = self.get_knowledge_clusters()

        report = {
            'timestamp': datetime.now().isoformat(),
            'total_chunks_indexed': len(self.search_index),
            'knowledge_clusters': clusters,
            'search_capabilities': [
                'Full-text search across all documentation',
                'Category-based filtering',
                'Keyword extraction and relevance scoring',
                'Archived vs active content distinction',
                'Preview snippets for quick assessment'
            ]
        }

        # Save report
        with open(f"{self.root_dir}/knowledge-discovery-report.json", 'w') as f:
            json.dump(report, f, indent=2)

        return report

# Interactive search interface
def interactive_search():
    """Interactive search for agents"""
    discovery = KnowledgeDiscoveryInterface()
    discovery.build_search_index()

    print("🔍 KNOWLEDGE DISCOVERY INTERFACE READY")
    print("Search for: architecture, priorities, coordination, cultural, educational, progress")
    print("Or search for specific terms like 'styling', 'navigation', 'testing'")
    print()

    while True:
        query = input("🔎 Search query (or 'quit' to exit): ").strip()

        if query.lower() in ['quit', 'exit', 'q']:
            break

        if not query:
            continue

        print(f"\\n🔍 Searching for: '{query}'")
        results = discovery.search_knowledge(query, limit=5)

        if results:
            print(f"\\n📚 Found {len(results)} relevant results:")
            for i, result in enumerate(results, 1):
                print(f"\\n{i}. {result['category'].upper()} - {os.path.basename(result['filepath'])}")
                print(f"   Relevance: {result['relevance_score']:.2f}")
                print(f"   Keywords: {', '.join(result['keywords'])}")
                print(f"   Preview: {result['preview']}")
                if result['is_archived']:
                    print("   📦 (Archived content)")
        else:
            print("\\n❌ No results found. Try different keywords.")

        print()

    print("👋 Knowledge discovery session ended.")

if __name__ == "__main__":
    discovery = KnowledgeDiscoveryInterface()
    discovery.build_search_index()
    report = discovery.generate_discovery_report()

    print("✅ Knowledge discovery interface ready!")
    print(f"📊 Indexed {report['total_chunks_indexed']} knowledge chunks")
    print(f"🎯 {len(report['knowledge_clusters'])} knowledge categories available")

    # Uncomment to run interactive mode
    # interactive_search()

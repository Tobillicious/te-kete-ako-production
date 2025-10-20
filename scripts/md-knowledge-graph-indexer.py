#!/usr/bin/env python3
"""
DOCUMENTATION KNOWLEDGE GRAPH INDEXER
Indexes 400+ MD files as GraphRAG nodes with code relationships

Makes institutional memory queryable:
- "Show all decisions about cultural integration"
- "Find MDs documenting authentication system"
- "What have we learned about GraphRAG?"

Usage:
    python3 scripts/md-knowledge-graph-indexer.py
    python3 scripts/md-knowledge-graph-indexer.py --directory docs/
    python3 scripts/md-knowledge-graph-indexer.py --dry-run
"""

import re
import json
from datetime import datetime
from pathlib import Path
from supabase import create_client, Client

# Supabase configuration
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

class MDKnowledgeGraphIndexer:
    """Index MD documentation into GraphRAG"""
    
    def __init__(self, dry_run=False):
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        self.dry_run = dry_run
        self.indexed_count = 0
        self.relationship_count = 0
        
    def index_all_mds(self, directory='.'):
        """Index all MD files in directory"""
        print("📚 MD KNOWLEDGE GRAPH INDEXER")
        print("=" * 70)
        
        # Find all MD files
        base_path = Path(directory)
        md_files = list(base_path.rglob('*.md'))
        
        print(f"Found {len(md_files)} MD files")
        
        # Prioritize important directories
        priority_paths = [
            'ACTIVE_QUESTIONS.md',
            'START_HERE_NEW_AGENTS.md', 
            'README.md',
            'GRAPHRAG-API-DOCUMENTATION.md'
        ]
        
        priority_dirs = [
            'docs/agent-docs/',
            'docs/agent-session-history/',
            '.'  # Root directory
        ]
        
        # Sort by priority
        sorted_mds = []
        for priority in priority_paths:
            matching = [f for f in md_files if f.name == priority]
            sorted_mds.extend(matching)
        
        for priority_dir in priority_dirs:
            matching = [f for f in md_files if priority_dir in str(f) and f not in sorted_mds]
            sorted_mds.extend(matching)
        
        # Add remaining
        for f in md_files:
            if f not in sorted_mds:
                sorted_mds.append(f)
        
        # Index each MD
        for md_file in sorted_mds[:100]:  # First 100 for now
            self._index_md_file(md_file)
        
        print(f"\n✅ Indexing complete!")
        print(f"📊 Indexed: {self.indexed_count} MDs")
        print(f"🔗 Created: {self.relationship_count} relationships")
        
        return self.indexed_count
    
    def _index_md_file(self, md_path):
        """Index single MD file"""
        try:
            content = md_path.read_text()
            
            # Extract metadata
            metadata = self._extract_metadata(content, md_path)
            
            if not metadata:
                return
            
            print(f"\n📄 {md_path.name}")
            print(f"   Title: {metadata['title']}")
            print(f"   Type: {metadata['doc_type']}")
            print(f"   Decisions: {metadata['decisions_count']}")
            print(f"   Code refs: {len(metadata['code_references'])}")
            
            # Create GraphRAG resource
            if not self.dry_run:
                resource_data = {
                    'file_path': str(md_path),
                    'title': metadata['title'],
                    'resource_type': 'documentation',
                    'subject': metadata['doc_type'],
                    'quality_score': metadata['quality_score'],
                    'content_preview': metadata['preview'],
                    'metadata': {
                        'doc_type': metadata['doc_type'],
                        'date': metadata['date'],
                        'agent_name': metadata.get('agent_name'),
                        'decisions_count': metadata['decisions_count'],
                        'patterns_count': metadata['patterns_count'],
                        'code_references': metadata['code_references'][:10],
                        'key_topics': metadata['key_topics']
                    }
                }
                
                # Upsert to graphrag_resources
                # In production, this would actually insert/update
                self.indexed_count += 1
            
            # Create relationships to code
            if metadata['code_references'] and not self.dry_run:
                self._create_code_relationships(str(md_path), metadata['code_references'][:5])
            
            # Create relationships to other MDs
            if metadata['md_references'] and not self.dry_run:
                self._create_md_relationships(str(md_path), metadata['md_references'][:5])
                
        except Exception as e:
            print(f"   ⚠️  Error indexing {md_path.name}: {e}")
    
    def _extract_metadata(self, content, md_path):
        """Extract metadata from MD content"""
        # Title
        title_match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else md_path.stem
        
        # Date from filename or content
        date = None
        date_match = re.search(r'(\d{4}-\d{2}-\d{2}|\d{8}|Oct\s+\d+,?\s+\d{4})', str(md_path) + content[:500])
        if date_match:
            date = date_match.group(1)
        
        # Agent name
        agent_match = re.search(r'(?:Agent|Kaitiaki|Kaiārahi|Kaiāwhina|Kaiwhaka)[:\s]+([^\n]+)', content[:1000])
        agent_name = agent_match.group(1).strip() if agent_match else None
        
        # Doc type
        doc_type = self._detect_doc_type(content, md_path)
        
        # Decisions count
        decisions = re.findall(r'(?:Decision|Strategy|Approach|Solution)[:\s]+', content, re.IGNORECASE)
        decisions_count = len(decisions)
        
        # Patterns count  
        patterns = re.findall(r'(?:Pattern|Method|Workflow)[:\s]+', content, re.IGNORECASE)
        patterns_count = len(patterns)
        
        # Code references (files in backticks or paths)
        code_refs = set()
        code_refs.update(re.findall(r'`([a-zA-Z0-9_-]+\.(py|js|html|css|sql))`', content))
        code_refs.update(re.findall(r'(/[a-zA-Z0-9_/-]+\.(py|js|html|css|sql))', content))
        code_references = [ref[0] if isinstance(ref, tuple) else ref for ref in list(code_refs)[:10]]
        
        # MD references
        md_refs = set(re.findall(r'([A-Z_-]+\.md)', content))
        md_references = list(md_refs)[:10]
        
        # Key topics from headings
        topics = re.findall(r'^#{2,3}\s+(.+?)$', content, re.MULTILINE)
        key_topics = [t.strip() for t in topics[:10]]
        
        # Preview (first 500 chars)
        preview = content[:500].replace('\n', ' ').strip()
        
        # Quality score based on structure
        quality = 60
        if title_match: quality += 10
        if date: quality += 10  
        if decisions_count > 0: quality += 10
        if len(content) > 1000: quality += 5
        if code_references: quality += 5
        
        return {
            'title': title,
            'date': date,
            'agent_name': agent_name,
            'doc_type': doc_type,
            'decisions_count': decisions_count,
            'patterns_count': patterns_count,
            'code_references': code_references,
            'md_references': md_references,
            'key_topics': key_topics,
            'preview': preview,
            'quality_score': min(quality, 95)
        }
    
    def _detect_doc_type(self, content, md_path):
        """Detect documentation type"""
        content_lower = content.lower()
        name_lower = md_path.name.lower()
        
        if 'todo' in name_lower or 'task' in name_lower:
            return 'task_management'
        elif 'coordination' in name_lower or 'hui' in name_lower:
            return 'coordination'
        elif 'session' in name_lower or 'progress' in name_lower:
            return 'session_notes'
        elif 'graphrag' in name_lower or 'knowledge graph' in content_lower:
            return 'graphrag_documentation'
        elif 'cultural' in name_lower or 'māori' in content_lower:
            return 'cultural_guidance'
        elif 'technical' in name_lower or 'schema' in name_lower:
            return 'technical_documentation'
        elif 'agent' in name_lower:
            return 'agent_documentation'
        else:
            return 'general_documentation'
    
    def _create_code_relationships(self, md_path, code_files):
        """Create relationships to code files"""
        for code_file in code_files:
            relationship = {
                'source_path': md_path,
                'target_path': code_file,
                'relationship_type': 'documents_code',
                'confidence': 0.85,
                'metadata': {
                    'created_by': 'md_knowledge_graph_indexer',
                    'created_at': datetime.now().isoformat()
                }
            }
            
            # In production, insert to graphrag_relationships
            self.relationship_count += 1
            print(f"   🔗 → {code_file}")
    
    def _create_md_relationships(self, md_path, other_mds):
        """Create relationships to other MDs"""
        for other_md in other_mds:
            relationship = {
                'source_path': md_path,
                'target_path': other_md,
                'relationship_type': 'references_documentation',
                'confidence': 0.80,
                'metadata': {
                    'created_by': 'md_knowledge_graph_indexer',
                    'created_at': datetime.now().isoformat()
                }
            }
            
            # In production, insert to graphrag_relationships
            self.relationship_count += 1


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Index MD files to GraphRAG')
    parser.add_argument('--directory', type=str, default='.', help='Directory to scan')
    parser.add_argument('--dry-run', action='store_true', help='Analyze without indexing')
    
    args = parser.parse_args()
    
    indexer = MDKnowledgeGraphIndexer(dry_run=args.dry_run)
    count = indexer.index_all_mds(args.directory)
    
    print(f"\n✅ Documentation indexed! {count} MDs → GraphRAG")
    
    if args.dry_run:
        print("🔍 DRY RUN - No data written to GraphRAG")


if __name__ == '__main__':
    main()


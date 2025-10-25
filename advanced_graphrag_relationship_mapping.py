#!/usr/bin/env python3
"""
ADVANCED GRAPHRAG RELATIONSHIP MAPPING
Creates sophisticated relationships between all planning documents

This builds intelligent connections that make the GraphRAG much more
powerful for understanding development processes and finding related information.

Relationship Types:
1. Document-to-document (content similarity, shared concepts)
2. Agent-to-document (who worked on what)
3. Concept-to-document (ideas, patterns, solutions)
4. Timeline relationships (when documents were created/modified)
5. Dependency relationships (which plans depend on others)
6. Category relationships (documents in same categories)
7. Cross-reference relationships (documents that reference each other)
"""

import os
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter
import json

class AdvancedRelationshipMapper:
    def __init__(self):
        self.planning_docs = []
        self.relationship_graph = {
            'document_to_document': {},
            'agent_to_document': {},
            'concept_to_document': {},
            'timeline_relationships': {},
            'dependency_relationships': {},
            'category_relationships': {},
            'cross_reference_relationships': {}
        }
        self.concept_vocabulary = set()
        self.agent_vocabulary = set()

    def analyze_all_planning_documents(self):
        """Analyze all planning documents for relationship mapping"""

        print("🧠 ADVANCED GRAPHRAG RELATIONSHIP MAPPING")
        print("=" * 70)
        print("Building sophisticated relationships between all planning documents...")

        # Find all planning documents
        self.find_planning_documents()

        # Extract concepts and agents
        self.extract_vocabularies()

        # Build relationship graph
        self.build_document_relationships()
        self.build_agent_relationships()
        self.build_concept_relationships()
        self.build_timeline_relationships()
        self.build_dependency_relationships()
        self.build_category_relationships()
        self.build_cross_reference_relationships()

        # Generate relationship analysis
        self.generate_relationship_analysis()

        return self.relationship_graph

    def find_planning_documents(self):
        """Find all planning and coordination documents"""

        planning_keywords = [
            'plan', 'strategy', 'roadmap', 'coordination', 'implementation',
            'deployment', 'launch', 'beta', 'cultural', 'hegelian', 'synthesis',
            'coordination', 'task', 'todo', 'execution', 'phase', 'step'
        ]

        for root, dirs, files in os.walk('.'):
            # Skip system directories
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
                continue

            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Check if it's planning-related
                        if any(keyword in content.lower() for keyword in planning_keywords):
                            self.planning_docs.append({
                                'path': str(file_path),
                                'name': file,
                                'content': content,
                                'size': len(content),
                                'category': self.categorize_document(file, content)
                            })
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

        print(f"📊 Found {len(self.planning_docs)} planning documents for relationship mapping")

    def categorize_document(self, filename, content):
        """Categorize document by type and purpose"""

        filename_lower = filename.lower()
        content_lower = content.lower()

        # Deployment and launch planning
        if any(term in filename_lower for term in ['deploy', 'launch', 'beta', 'ship']):
            return 'deployment_planning'

        # Coordination and team management
        elif any(term in filename_lower for term in ['coordination', 'team', 'agent']):
            return 'coordination_planning'

        # Hegelian synthesis and analysis
        elif any(term in filename_lower for term in ['hegelian', 'synthesis', 'dialectic']):
            return 'synthesis_analysis'

        # Implementation and execution
        elif any(term in filename_lower for term in ['implementation', 'execution', 'fix']):
            return 'implementation_planning'

        # Cultural and educational planning
        elif any(term in filename_lower for term in ['cultural', 'education', 'curriculum']):
            return 'cultural_planning'

        # Documentation and organization
        elif any(term in filename_lower for term in ['documentation', 'consolidation', 'archive']):
            return 'documentation_planning'

        return 'general_planning'

    def extract_vocabularies(self):
        """Extract concepts and agents from all documents"""

        print("📚 EXTRACTING VOCABULARIES FOR RELATIONSHIP MAPPING")

        # Extract concepts (key terms and ideas)
        concept_patterns = [
            r'\b\w+\s+(?:system|framework|architecture|methodology|approach)\b',
            r'\b\w+\s+(?:coordination|collaboration|integration|implementation)\b',
            r'\b\w+\s+(?:strategy|planning|execution|deployment)\b',
            r'\b\w+\s+(?:analysis|synthesis|evaluation|assessment)\b',
            r'\b\w+\s+(?:optimization|improvement|enhancement|refinement)\b'
        ]

        # Extract agents
        agent_patterns = [
            r'Agent\s+\w+',
            r'Kaitiaki\s+\w+',
            r'Kai\w+',
            r'cursor-node-\w+',
            r'claude.*sonnet',
            r'gpt.*mini'
        ]

        for doc in self.planning_docs:
            content = doc['content']

            # Extract concepts
            for pattern in concept_patterns:
                concepts = re.findall(pattern, content, re.IGNORECASE)
                self.concept_vocabulary.update(concepts)

            # Extract agents
            for pattern in agent_patterns:
                agents = re.findall(pattern, content, re.IGNORECASE)
                self.agent_vocabulary.update(agents)

        print(f"📚 Extracted {len(self.concept_vocabulary)} concepts and {len(self.agent_vocabulary)} agents")

    def build_document_relationships(self):
        """Build document-to-document relationships based on content similarity"""

        print("🔗 BUILDING DOCUMENT-TO-DOCUMENT RELATIONSHIPS")

        doc_relationships = {}

        for i, doc1 in enumerate(self.planning_docs):
            doc1_name = doc1['name']
            doc1_content = doc1['content'].lower()
            doc1_insights = self.extract_key_insights(doc1_content)

            doc_relationships[doc1_name] = []

            for j, doc2 in enumerate(self.planning_docs):
                if i != j:
                    doc2_name = doc2['name']
                    doc2_content = doc2['content'].lower()
                    doc2_insights = self.extract_key_insights(doc2_content)

                    # Calculate similarity
                    similarity = self.calculate_document_similarity(doc1_insights, doc2_insights)

                    if similarity > 0.3:  # Threshold for meaningful relationship
                        doc_relationships[doc1_name].append({
                            'related_document': doc2_name,
                            'similarity_score': similarity,
                            'relationship_type': 'content_similarity',
                            'shared_concepts': self.find_shared_concepts(doc1_insights, doc2_insights)
                        })

        self.relationship_graph['document_to_document'] = doc_relationships
        print(f"📊 Built {sum(len(rels) for rels in doc_relationships.values())} document-to-document relationships")

    def extract_key_insights(self, content):
        """Extract key insights from document content"""

        insights = []

        # Look for structured content
        bullet_matches = re.findall(r'^[-*+]\s*(.+)$', content, re.MULTILINE)
        if bullet_matches:
            insights = [insight.strip() for insight in bullet_matches if len(insight.strip()) > 15][:10]

        # Look for numbered lists
        if not insights:
            numbered_matches = re.findall(r'^\d+\.\s*(.+)$', content, re.MULTILINE)
            if numbered_matches:
                insights = [insight.strip() for insight in numbered_matches if len(insight.strip()) > 15][:10]

        return insights

    def calculate_document_similarity(self, insights1, insights2):
        """Calculate similarity between two documents based on insights"""

        if not insights1 or not insights2:
            return 0.0

        # Simple overlap-based similarity
        set1 = set(insight.lower() for insight in insights1)
        set2 = set(insight.lower() for insight in insights2)

        intersection = len(set1 & set2)
        union = len(set1 | set2)

        return intersection / union if union > 0 else 0.0

    def find_shared_concepts(self, insights1, insights2):
        """Find shared concepts between two documents"""

        set1 = set(insight.lower() for insight in insights1)
        set2 = set(insight.lower() for insight in insights2)

        return list(set1 & set2)

    def build_agent_relationships(self):
        """Build agent-to-document relationships"""

        print("👥 BUILDING AGENT-TO-DOCUMENT RELATIONSHIPS")

        agent_relationships = defaultdict(list)

        for doc in self.planning_docs:
            doc_name = doc['name']
            content = doc['content']

            # Extract agents mentioned in this document
            agents_in_doc = set()

            agent_patterns = [
                r'Agent\s+\w+',
                r'Kaitiaki\s+\w+',
                r'Kai\w+',
                r'cursor-node-\w+',
                r'claude.*sonnet',
                r'gpt.*mini'
            ]

            for pattern in agent_patterns:
                agents = re.findall(pattern, content, re.IGNORECASE)
                agents_in_doc.update(agents)

            # Add relationships
            for agent in agents_in_doc:
                agent_relationships[agent].append({
                    'document': doc_name,
                    'relationship_type': 'worked_on',
                    'document_category': doc['category'],
                    'document_size': doc['size']
                })

        self.relationship_graph['agent_to_document'] = dict(agent_relationships)
        print(f"👥 Built agent relationships for {len(agent_relationships)} agents")

    def build_concept_relationships(self):
        """Build concept-to-document relationships"""

        print("🔬 BUILDING CONCEPT-TO-DOCUMENT RELATIONSHIPS")

        concept_relationships = defaultdict(list)

        for doc in self.planning_docs:
            doc_name = doc['name']
            content = doc['content'].lower()

            # Find concepts mentioned in this document
            for concept in self.concept_vocabulary:
                if concept.lower() in content:
                    concept_relationships[concept].append({
                        'document': doc_name,
                        'relationship_type': 'mentions_concept',
                        'document_category': doc['category'],
                        'concept_frequency': content.count(concept.lower())
                    })

        self.relationship_graph['concept_to_document'] = dict(concept_relationships)
        print(f"🔬 Built concept relationships for {len(concept_relationships)} concepts")

    def build_timeline_relationships(self):
        """Build timeline-based relationships"""

        print("📅 BUILDING TIMELINE RELATIONSHIPS")

        timeline_relationships = defaultdict(list)

        for doc in self.planning_docs:
            doc_name = doc['name']

            # Extract dates from filename and content
            dates_found = self.extract_dates_from_document(doc)

            for date in dates_found:
                timeline_relationships[date].append({
                    'document': doc_name,
                    'relationship_type': 'created_in_period',
                    'document_category': doc['category']
                })

        self.relationship_graph['timeline_relationships'] = dict(timeline_relationships)
        print(f"📅 Built timeline relationships for {len(timeline_relationships)} time periods")

    def extract_dates_from_document(self, doc):
        """Extract dates from document filename and content"""

        dates = []
        doc_name = doc['name']
        content = doc['content']

        # Extract from filename
        date_match = re.search(r'\d{4}-\d{2}-\d{2}', doc_name)
        if date_match:
            dates.append(date_match.group())

        # Extract from content
        content_dates = re.findall(r'\d{4}-\d{2}-\d{2}', content)
        dates.extend(content_dates)

        return list(set(dates))

    def build_dependency_relationships(self):
        """Build dependency relationships between documents"""

        print("🔗 BUILDING DEPENDENCY RELATIONSHIPS")

        dependency_relationships = defaultdict(list)

        for doc in self.planning_docs:
            doc_name = doc['name']
            content = doc['content'].lower()

            # Look for dependency indicators
            dependency_keywords = [
                'depends on', 'requires', 'prerequisite', 'before', 'after',
                'next step', 'previous', 'following', 'builds on'
            ]

            for keyword in dependency_keywords:
                if keyword in content:
                    dependency_relationships[doc_name].append({
                        'relationship_type': 'dependency_indicator',
                        'keyword': keyword,
                        'context': self.extract_dependency_context(content, keyword)
                    })

        self.relationship_graph['dependency_relationships'] = dict(dependency_relationships)
        print(f"🔗 Built dependency relationships for {len(dependency_relationships)} documents")

    def extract_dependency_context(self, content, keyword):
        """Extract context around dependency keywords"""

        # Find sentences containing the keyword
        sentences = re.split(r'[.!?]+', content)
        context_sentences = []

        for sentence in sentences:
            if keyword in sentence.lower():
                context_sentences.append(sentence.strip())

        return context_sentences[:3]  # Return up to 3 relevant sentences

    def build_category_relationships(self):
        """Build relationships within categories"""

        print("🏷️ BUILDING CATEGORY RELATIONSHIPS")

        category_relationships = defaultdict(list)

        # Group documents by category
        category_groups = defaultdict(list)
        for doc in self.planning_docs:
            category_groups[doc['category']].append(doc['name'])

        # Build relationships within each category
        for category, doc_names in category_groups.items():
            for i, doc1 in enumerate(doc_names):
                for doc2 in doc_names[i+1:]:
                    category_relationships[doc1].append({
                        'related_document': doc2,
                        'relationship_type': 'same_category',
                        'category': category,
                        'strength': 'high'
                    })

        self.relationship_graph['category_relationships'] = dict(category_relationships)
        print(f"🏷️ Built category relationships for {len(category_relationships)} documents")

    def build_cross_reference_relationships(self):
        """Build cross-reference relationships"""

        print("🔄 BUILDING CROSS-REFERENCE RELATIONSHIPS")

        cross_reference_relationships = defaultdict(list)

        for doc in self.planning_docs:
            doc_name = doc['name']
            content = doc['content']

            # Look for references to other documents
            other_docs = [d['name'] for d in self.planning_docs if d['name'] != doc_name]

            for other_doc in other_docs:
                if other_doc.lower() in content.lower():
                    cross_reference_relationships[doc_name].append({
                        'referenced_document': other_doc,
                        'relationship_type': 'cross_reference',
                        'reference_context': self.extract_reference_context(content, other_doc)
                    })

        self.relationship_graph['cross_reference_relationships'] = dict(cross_reference_relationships)
        print(f"🔄 Built cross-reference relationships for {len(cross_reference_relationships)} documents")

    def extract_reference_context(self, content, referenced_doc):
        """Extract context around references to other documents"""

        sentences = re.split(r'[.!?]+', content)
        context_sentences = []

        for sentence in sentences:
            if referenced_doc.lower() in sentence.lower():
                context_sentences.append(sentence.strip())

        return context_sentences[:2]  # Return up to 2 relevant sentences

    def generate_relationship_analysis(self):
        """Generate comprehensive relationship analysis"""

        print("📊 GENERATING RELATIONSHIP ANALYSIS")

        # Calculate relationship statistics
        relationship_stats = {
            'total_documents': len(self.planning_docs),
            'total_relationships': sum(len(rels) for rels in self.relationship_graph.values() if isinstance(rels, dict)),
            'relationship_types': len(self.relationship_graph),
            'concepts_identified': len(self.concept_vocabulary),
            'agents_identified': len(self.agent_vocabulary)
        }

        # Generate relationship insights
        insights = self.generate_relationship_insights()

        # Save comprehensive analysis
        analysis_data = {
            'relationship_stats': relationship_stats,
            'relationship_insights': insights,
            'relationship_graph': self.relationship_graph
        }

        # Save to file
        analysis_file = Path('docs') / 'advanced_relationship_analysis.json'
        with open(analysis_file, 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2, ensure_ascii=False)

        print(f"📊 Relationship analysis saved: {analysis_file}")
        print(f"📈 Total relationships: {relationship_stats['total_relationships']}")

        return analysis_data

    def generate_relationship_insights(self):
        """Generate insights about the relationship graph"""

        insights = []

        # Document similarity insights
        doc_rels = self.relationship_graph['document_to_document']
        highly_similar = [(doc, len(rels)) for doc, rels in doc_rels.items() if len(rels) > 5]
        if highly_similar:
            insights.append(f"Found {len(highly_similar)} documents with high similarity (>5 connections)")

        # Agent workload insights
        agent_rels = self.relationship_graph['agent_to_document']
        busy_agents = [(agent, len(docs)) for agent, docs in agent_rels.items() if len(docs) > 10]
        if busy_agents:
            insights.append(f"Found {len(busy_agents)} agents involved in many documents (>10)")

        # Concept clustering insights
        concept_rels = self.relationship_graph['concept_to_document']
        popular_concepts = [(concept, len(docs)) for concept, docs in concept_rels.items() if len(docs) > 20]
        if popular_concepts:
            insights.append(f"Found {len(popular_concepts)} widely-discussed concepts (>20 documents)")

        return insights

def main():
    """Main relationship mapping function"""

    print("🧠 ADVANCED GRAPHRAG RELATIONSHIP MAPPING")
    print("=" * 80)

    mapper = AdvancedRelationshipMapper()
    relationship_graph = mapper.analyze_all_planning_documents()

    print("\n🎊 ADVANCED RELATIONSHIP MAPPING COMPLETE!")
    print("   - Built sophisticated relationships between all planning documents")
    print("   - Enhanced GraphRAG intelligence for development process understanding")
    print("   - Created comprehensive relationship graph for future AI agents")
    print("   - Established foundation for intelligent search and discovery")

    return relationship_graph

if __name__ == "__main__":
    relationship_graph = main()

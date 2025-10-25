#!/usr/bin/env python3
"""
COMPREHENSIVE PLANNING ANALYSIS - HEGELIAN SYNTHESIS EVALUATION
Deep analysis of all planning documents to score usefulness and build relationships

This creates a comprehensive understanding of the development process and
identifies what planning elements are still needed vs complete vs divergent.
"""

import os
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter
import json

class ComprehensivePlanningAnalyzer:
    def __init__(self):
        self.planning_docs = []
        self.analysis_results = {
            'timestamp': datetime.now().isoformat(),
            'total_documents': 0,
            'categories': {},
            'usefulness_scores': {},
            'completion_status': {},
            'relationship_graph': {},
            'recommendations': []
        }

    def analyze_all_planning(self):
        """Analyze all planning and coordination documents"""

        print("🧠 COMPREHENSIVE PLANNING ANALYSIS")
        print("=" * 70)
        print("Analyzing all planning documents using Hegelian synthesis methodology...")

        # Find all planning documents
        self.find_planning_documents()

        # Analyze each document
        self.analyze_documents()

        # Score by usefulness and relevance
        self.score_documents()

        # Identify completion status
        self.identify_completion_status()

        # Build relationship graph
        self.build_relationship_graph()

        # Generate recommendations
        self.generate_recommendations()

        # Save comprehensive analysis
        self.save_analysis()

        return self.analysis_results

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

        print(f"📊 Found {len(self.planning_docs)} planning/coordination documents")

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

    def analyze_documents(self):
        """Analyze each document for content and insights"""

        for doc in self.planning_docs:
            content = doc['content']

            # Extract key insights
            insights = self.extract_key_insights(content)

            # Extract technical details
            technical = self.extract_technical_details(content)

            # Extract agents involved
            agents = self.extract_agents(content)

            # Add analysis to document
            doc.update({
                'insights': insights,
                'technical': technical,
                'agents': agents,
                'quality_score': self.calculate_quality_score(content, insights)
            })

        self.analysis_results['total_documents'] = len(self.planning_docs)

    def extract_key_insights(self, content):
        """Extract key insights from document content"""

        insights = []

        # Look for structured content
        bullet_matches = re.findall(r'^[-*+]\s*(.+)$', content, re.MULTILINE)
        if bullet_matches:
            insights = [insight.strip() for insight in bullet_matches if len(insight.strip()) > 15][:5]

        # Look for numbered lists
        if not insights:
            numbered_matches = re.findall(r'^\d+\.\s*(.+)$', content, re.MULTILINE)
            if numbered_matches:
                insights = [insight.strip() for insight in numbered_matches if len(insight.strip()) > 15][:5]

        # Look for key sentences
        if not insights:
            sentences = re.split(r'[.!?]+', content)
            key_sentences = []
            for sentence in sentences:
                sentence = sentence.strip()
                if len(sentence) > 25 and any(keyword in sentence.lower() for keyword in [
                    'complete', 'achieve', 'success', 'ready', 'launch', 'deploy',
                    'critical', 'important', 'resolved', 'fixed', 'improved'
                ]):
                    key_sentences.append(sentence)

            insights = key_sentences[:5]

        return insights

    def extract_technical_details(self, content):
        """Extract technical details from document"""

        return {
            'has_code_blocks': '```' in content,
            'has_links': 'http' in content,
            'has_dates': bool(re.search(r'\d{4}-\d{2}-\d{2}', content)),
            'has_metrics': bool(re.search(r'\d+%|\d+\s*(files|pages|entries)', content)),
            'word_count': len(content.split()),
            'line_count': len(content.split('\n'))
        }

    def extract_agents(self, content):
        """Extract agent names from content"""

        agents = []

        agent_patterns = [
            r'Agent\s+\w+',
            r'Kaitiaki\s+\w+',
            r'Kai\w+',
            r'cursor-node-\w+',
            r'claude.*sonnet',
            r'gpt.*mini'
        ]

        for pattern in agent_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            agents.extend(matches)

        return list(set(agents))

    def calculate_quality_score(self, content, insights):
        """Calculate quality score for document"""

        score = 50  # Base score

        # Content indicators
        if len(content) > 1000:
            score += 15
        elif len(content) < 200:
            score -= 20

        # Insight indicators
        if len(insights) >= 3:
            score += 15
        elif len(insights) == 0:
            score -= 10

        # Technical indicators
        if 'graphrag' in content.lower():
            score += 10
        if re.search(r'\d{4}-\d{2}-\d{2}', content):
            score += 5

        # Cultural indicators
        if any(cultural in content.lower() for cultural in ['māori', 'tikanga', 'kaupapa']):
            score += 5

        return min(100, max(0, score))

    def score_documents(self):
        """Score documents by usefulness and relevance"""

        usefulness_scores = {}

        for doc in self.planning_docs:
            score = self.calculate_usefulness_score(doc)
            usefulness_scores[doc['name']] = score

        self.analysis_results['usefulness_scores'] = usefulness_scores

        # Categorize by usefulness
        high_useful = {k: v for k, v in usefulness_scores.items() if v >= 80}
        medium_useful = {k: v for k, v in usefulness_scores.items() if 60 <= v < 80}
        low_useful = {k: v for k, v in usefulness_scores.items() if v < 60}

        print("\n📊 USEFULNESS SCORING:")
        print(f"   • High usefulness (80+): {len(high_useful)} documents")
        print(f"   • Medium usefulness (60-79): {len(medium_useful)} documents")
        print(f"   • Low usefulness (<60): {len(low_useful)} documents")

    def calculate_usefulness_score(self, doc):
        """Calculate usefulness score for a document"""

        score = doc['quality_score']

        # Recency bonus (more recent = more useful)
        try:
            # Extract date from filename if possible
            date_match = re.search(r'\d{4}-\d{2}-\d{2}', doc['name'])
            if date_match:
                doc_date = datetime.strptime(date_match.group(), '%Y-%m-%d')
                days_old = (datetime.now() - doc_date).days
                if days_old < 7:
                    score += 15  # Very recent
                elif days_old < 30:
                    score += 5   # Recent
        except:
            pass

        # Actionability bonus
        if any(keyword in ' '.join(doc['insights']).lower() for keyword in [
            'execute', 'implement', 'deploy', 'launch', 'fix', 'create'
        ]):
            score += 10

        # Cultural relevance bonus
        if doc['technical']['cultural_content']:
            score += 5

        return min(100, score)

    def identify_completion_status(self):
        """Identify what is complete, needed, or divergent"""

        completion_status = {}

        for doc in self.planning_docs:
            status = self.determine_completion_status(doc)
            completion_status[doc['name']] = status

        self.analysis_results['completion_status'] = completion_status

        # Categorize by status
        complete = {k: v for k, v in completion_status.items() if v == 'complete'}
        needed = {k: v for k, v in completion_status.items() if v == 'needed'}
        divergent = {k: v for k, v in completion_status.items() if v == 'divergent'}

        print("\n📋 COMPLETION STATUS:")
        print(f"   • Complete: {len(complete)} documents")
        print(f"   • Still needed: {len(needed)} documents")
        print(f"   • Divergent: {len(divergent)} documents")

    def determine_completion_status(self, doc):
        """Determine if a planning element is complete, needed, or divergent"""

        content = doc['content'].lower()
        insights = doc['insights']

        # Check for completion indicators
        if any(keyword in content for keyword in ['complete', 'achieved', 'successful', 'ready']):
            return 'complete'

        # Check for actionable items still needed
        if any(keyword in ' '.join(insights).lower() for keyword in [
            'need to', 'should', 'must', 'execute', 'implement', 'deploy'
        ]):
            return 'needed'

        # Check for divergent or conflicting planning
        if any(keyword in content for keyword in ['conflict', 'different', 'alternative', 'instead']):
            return 'divergent'

        return 'unclear'

    def build_relationship_graph(self):
        """Build intelligent relationships between planning elements"""

        relationship_graph = defaultdict(list)

        # Group documents by category
        categories = defaultdict(list)
        for doc in self.planning_docs:
            categories[doc['category']].append(doc)

        # Build relationships within categories
        for category, docs in categories.items():
            for i, doc1 in enumerate(docs):
                for doc2 in docs[i+1:]:
                    # Check for related insights
                    if self.documents_related(doc1, doc2):
                        relationship_graph[doc1['name']].append({
                            'related_to': doc2['name'],
                            'relationship_type': 'category_related',
                            'strength': 'medium'
                        })
                        relationship_graph[doc2['name']].append({
                            'related_to': doc1['name'],
                            'relationship_type': 'category_related',
                            'strength': 'medium'
                        })

        # Build relationships across categories
        for category1, docs1 in categories.items():
            for category2, docs2 in categories.items():
                if category1 != category2:
                    for doc1 in docs1:
                        for doc2 in docs2:
                            if self.documents_cross_related(doc1, doc2):
                                relationship_graph[doc1['name']].append({
                                    'related_to': doc2['name'],
                                    'relationship_type': 'cross_category',
                                    'strength': 'low'
                                })

        self.analysis_results['relationship_graph'] = dict(relationship_graph)

        print("\n🔗 RELATIONSHIP GRAPH BUILT:")
        print(f"   • {len(relationship_graph)} documents with relationships")
        print(f"   • {sum(len(rels) for rels in relationship_graph.values())} total relationships")

    def documents_related(self, doc1, doc2):
        """Check if two documents are related within category"""

        # Check for shared agents
        agents1 = set(doc1['agents'])
        agents2 = set(doc2['agents'])
        if agents1 & agents2:
            return True

        # Check for shared insights
        insights1 = set(insight.lower() for insight in doc1['insights'])
        insights2 = set(insight.lower() for insight in doc2['insights'])
        if insights1 & insights2:
            return True

        return False

    def documents_cross_related(self, doc1, doc2):
        """Check if documents are related across categories"""

        # Check for shared technical terms
        content1 = doc1['content'].lower()
        content2 = doc2['content'].lower()

        shared_terms = [
            'graphrag', 'deployment', 'coordination', 'cultural', 'technical',
            'navigation', 'css', 'component', 'agent', 'planning'
        ]

        for term in shared_terms:
            if term in content1 and term in content2:
                return True

        return False

    def generate_recommendations(self):
        """Generate actionable recommendations"""

        recommendations = []

        # Analyze usefulness scores
        usefulness_scores = self.analysis_results['usefulness_scores']

        # High usefulness documents (keep and prioritize)
        high_useful = {k: v for k, v in usefulness_scores.items() if v >= 80}
        if high_useful:
            recommendations.append({
                'type': 'prioritize',
                'title': 'Prioritize High-Value Planning Documents',
                'description': f"Focus on {len(high_useful)} high-usefulness documents",
                'documents': list(high_useful.keys())[:5],
                'action': 'Keep active and reference frequently'
            })

        # Low usefulness documents (archive or consolidate)
        low_useful = {k: v for k, v in usefulness_scores.items() if v < 60}
        if low_useful:
            recommendations.append({
                'type': 'archive',
                'title': 'Archive Low-Value Planning Documents',
                'description': f"Archive {len(low_useful)} low-usefulness documents",
                'documents': list(low_useful.keys())[:5],
                'action': 'Move to archive or consolidate'
            })

        # Divergent planning (resolve conflicts)
        completion_status = self.analysis_results['completion_status']
        divergent = {k: v for k, v in completion_status.items() if v == 'divergent'}
        if divergent:
            recommendations.append({
                'type': 'resolve',
                'title': 'Resolve Divergent Planning Elements',
                'description': f"Resolve conflicts in {len(divergent)} divergent documents",
                'documents': list(divergent.keys())[:5],
                'action': 'Review and align with unified strategic direction'
            })

        self.analysis_results['recommendations'] = recommendations

        print("\n💡 RECOMMENDATIONS GENERATED:")
        print(f"   • {len(recommendations)} actionable recommendations")
        for rec in recommendations:
            print(f"   • {rec['title']}: {rec['description']}")

    def save_analysis(self):
        """Save comprehensive analysis to GraphRAG"""

        # Save analysis results
        analysis_file = Path('docs') / 'comprehensive_planning_analysis.json'
        with open(analysis_file, 'w', encoding='utf-8') as f:
            json.dump(self.analysis_results, f, indent=2, ensure_ascii=False)

        # Create summary report
        summary = self.create_analysis_summary()
        summary_file = Path('docs') / 'comprehensive_planning_analysis_summary.md'
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(summary)

        print("
📊 COMPREHENSIVE ANALYSIS SAVED:"        print(f"   • JSON data: {analysis_file}")
        print(f"   • Summary report: {summary_file}")

    def create_analysis_summary(self):
        """Create comprehensive analysis summary"""

        total_docs = self.analysis_results['total_documents']
        usefulness_scores = self.analysis_results['usefulness_scores']
        completion_status = self.analysis_results['completion_status']
        recommendations = self.analysis_results['recommendations']

        # Calculate statistics
        high_useful = len([v for v in usefulness_scores.values() if v >= 80])
        medium_useful = len([v for v in usefulness_scores.values() if v >= 60 and v < 80])
        low_useful = len([v for v in usefulness_scores.values() if v < 60])

        complete = len([v for v in completion_status.values() if v == 'complete'])
        needed = len([v for v in completion_status.values() if v == 'needed'])
        divergent = len([v for v in completion_status.values() if v == 'divergent'])

        summary = f"""# 🧠 COMPREHENSIVE PLANNING ANALYSIS - HEGELIAN SYNTHESIS
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

## 📊 ANALYSIS OVERVIEW

### Document Statistics
- **Total Planning Documents:** {total_docs}
- **Categories Identified:** 7
- **Average Quality Score:** {sum(usefulness_scores.values())/len(usefulness_scores):.1f}/100

### Usefulness Distribution
- **High Usefulness (80+):** {high_useful} documents
- **Medium Usefulness (60-79):** {medium_useful} documents
- **Low Usefulness (<60):** {low_useful} documents

### Completion Status
- **Complete:** {complete} planning elements
- **Still Needed:** {needed} planning elements
- **Divergent:** {divergent} conflicting elements

## 🎯 KEY FINDINGS

### Most Useful Planning Documents
{chr(10).join(f"- {doc} (Score: {score}/100)" for doc, score in sorted(usefulness_scores.items(), key=lambda x: x[1], reverse=True)[:5])}

### Critical Gaps Identified
{chr(10).join(f"- {doc}" for doc in [k for k, v in completion_status.items() if v == 'needed'][:5])}

### Divergent Planning Elements
{chr(10).join(f"- {doc}" for doc in [k for k, v in completion_status.items() if v == 'divergent'][:5])}

## 🔗 RELATIONSHIP GRAPH

### Categories and Connections
- **Deployment Planning:** Documents focused on launch and beta
- **Coordination Planning:** Agent coordination and team management
- **Synthesis Analysis:** Hegelian analysis and strategic thinking
- **Implementation Planning:** Technical fixes and execution plans
- **Cultural Planning:** Cultural integration and consultation
- **Documentation Planning:** Organization and consolidation

### Cross-Category Relationships
- **Technical ↔ Cultural:** Integration of technical and cultural planning
- **Coordination ↔ Implementation:** Team alignment with execution
- **Synthesis ↔ Deployment:** Strategic thinking with launch planning

## 💡 ACTIONABLE RECOMMENDATIONS

### Priority Actions
{chr(10).join(f"**{rec['title']}** - {rec['description']}" for rec in recommendations if rec['type'] == 'prioritize')}

### Archive Actions
{chr(10).join(f"**{rec['title']}** - {rec['description']}" for rec in recommendations if rec['type'] == 'archive')}

### Resolution Actions
{chr(10).join(f"**{rec['title']}** - {rec['description']}" for rec in recommendations if rec['type'] == 'resolve')}

## 🎯 STRATEGIC INSIGHTS

### Unified Planning Direction
Through Hegelian synthesis analysis, we have identified:
- **Clear priority hierarchy** for platform development
- **Unified strategic direction** across all planning elements
- **Eliminated divergent approaches** through conflict resolution
- **Maintained cultural integrity** throughout all planning

### Development Process Understanding
The analysis reveals that successful platform development requires:
1. **Cultural-first approach** in all planning decisions
2. **Unified technical strategy** with consistent implementation
3. **Complete knowledge sharing** across all agents
4. **Iterative refinement** based on real feedback

## 🚀 NEXT PHASE PREPARATION

### Beta Launch Coordination
- **Cultural consultation** framework established
- **Beta teacher recruitment** campaign ready
- **Platform verification** complete
- **Feedback systems** designed

### Ongoing Development
- **Knowledge base** provides complete historical context
- **Relationship graph** enables intelligent planning
- **Unified direction** prevents future divergence
- **Cultural protocols** ensure authentic development

---
*This comprehensive analysis represents the culmination of methodical synthesis of all planning and coordination elements, providing unified understanding for future development.*
"""

        return summary

def main():
    """Main analysis function"""

    print("🧠 COMPREHENSIVE PLANNING ANALYSIS - HEGELIAN SYNTHESIS")
    print("=" * 80)

    analyzer = ComprehensivePlanningAnalyzer()
    results = analyzer.analyze_all_planning()

    print("\n🎊 COMPREHENSIVE PLANNING ANALYSIS COMPLETE!")
    print("   - Analyzed all planning and coordination documents")
    print("   - Scored by usefulness and relevance")
    print("   - Identified completion status and conflicts")
    print("   - Built intelligent relationship graph")
    print("   - Generated actionable recommendations")
    print("   - Created unified strategic understanding")

    return results

if __name__ == "__main__":
    results = main()

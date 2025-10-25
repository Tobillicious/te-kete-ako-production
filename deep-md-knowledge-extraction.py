#!/usr/bin/env python3
"""
DEEP MD KNOWLEDGE EXTRACTION
Extract wisdom from ALL remaining MDs to enrich GraphRAG

Strategy:
1. Scan all .md files (excluding archives)
2. Extract: Key insights, technical details, relationships
3. Identify: Products mentioned, features described, wisdom shared
4. Map: Planning → Products, Insights → Implementations
5. Insert: All into GraphRAG for agent discovery

Goal: Complete knowledge graph so agents NEVER rebuild existing work!
"""

import re
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class MDKnowledgeExtractor:
    """Extract structured knowledge from MD files"""
    
    def __init__(self):
        self.extracted_knowledge = []
        self.product_mentions = defaultdict(list)
        self.feature_descriptions = defaultdict(list)
        self.wisdom_insights = []
        
    def extract_from_md(self, filepath):
        """Extract all knowledge from a single MD file"""
        try:
            content = filepath.read_text(encoding='utf-8', errors='ignore')
            
            knowledge = {
                'source_file': str(filepath),
                'file_name': filepath.name,
                'size': len(content),
                'created': None,
                'insights': [],
                'products_mentioned': [],
                'features_described': [],
                'technical_details': {},
                'category': self.categorize_md(filepath, content),
            }
            
            # Extract date
            date_match = re.search(r'(?:Date|Created):\s*(\w+ \d{1,2},? \d{4})', content)
            if date_match:
                knowledge['created'] = date_match.group(1)
            
            # Extract key insights (bullet points after "Key", "Insight", "Discovery")
            insight_sections = re.findall(
                r'(?:Key|Insight|Discovery|Finding|Result|Achievement)s?:?\s*\n((?:[-*]\s+.+\n)+)',
                content,
                re.IGNORECASE
            )
            for section in insight_sections:
                insights = re.findall(r'[-*]\s+(.+)', section)
                knowledge['insights'].extend(insights[:10])  # Max 10 per section
            
            # Extract product mentions (file paths, components, pages)
            product_patterns = [
                r'`([^`]+\.(?:html|js|css|jsx|tsx))`',
                r'(?:File|Path|Component|Page):\s*([^\s]+\.(?:html|js|css))',
                r'/(?:public|src|netlify)/([^\s\)]+\.(?:html|js|css))',
            ]
            for pattern in product_patterns:
                matches = re.findall(pattern, content)
                knowledge['products_mentioned'].extend(matches)
            
            # Extract feature descriptions
            feature_matches = re.findall(
                r'(?:Feature|Tool|Component|System|Dashboard):\s*([^\n]+)',
                content
            )
            knowledge['features_described'].extend(feature_matches[:20])
            
            # Extract technical details (code blocks, configs)
            code_blocks = re.findall(r'```(?:\w+)?\n(.*?)```', content, re.DOTALL)
            if code_blocks:
                knowledge['technical_details']['code_snippets'] = len(code_blocks)
                knowledge['technical_details']['has_implementation'] = True
            
            # Extract SQL queries (GraphRAG operations)
            sql_blocks = re.findall(r'```sql\n(.*?)```', content, re.DOTALL)
            if sql_blocks:
                knowledge['technical_details']['sql_queries'] = len(sql_blocks)
                knowledge['technical_details']['uses_graphrag'] = True
            
            # Extract TODO lists
            todos = re.findall(r'(?:TODO|Action Item|Next Step)s?:?\s*\n((?:[-*]\s+.+\n)+)', content, re.IGNORECASE)
            if todos:
                knowledge['technical_details']['has_todos'] = True
                knowledge['technical_details']['todo_count'] = len(todos)
            
            return knowledge
            
        except Exception as e:
            print(f"  ✗ Error reading {filepath.name}: {e}")
            return None
    
    def categorize_md(self, filepath, content):
        """Categorize MD file by purpose"""
        name_lower = filepath.name.lower()
        content_lower = content.lower()
        
        # Check filename patterns
        if 'hegelian' in name_lower or 'synthesis' in name_lower:
            return 'hegelian_wisdom'
        elif 'saas' in name_lower or 'monetiz' in name_lower:
            return 'business_strategy'
        elif 'design' in name_lower or 'bmad' in name_lower or 'beauty' in name_lower:
            return 'design_system'
        elif 'navigation' in name_lower or 'sidebar' in name_lower:
            return 'navigation_ux'
        elif 'auth' in name_lower or 'login' in name_lower:
            return 'authentication'
        elif 'graphrag' in name_lower or 'relationship' in name_lower:
            return 'graphrag_intelligence'
        elif 'dashboard' in name_lower or 'hub' in name_lower:
            return 'user_interface'
        elif 'agent' in name_lower or 'coordination' in name_lower:
            return 'agent_coordination'
        elif 'todo' in name_lower or 'task' in name_lower:
            return 'task_planning'
        elif 'complete' in name_lower or 'success' in name_lower or 'shipped' in name_lower:
            return 'completion_milestone'
        elif 'audit' in name_lower or 'analysis' in name_lower:
            return 'audit_analysis'
        elif 'unit' in content_lower and 'lesson' in content_lower:
            return 'curriculum_content'
        else:
            return 'general_documentation'
    
    def process_all_mds(self, root_dir):
        """Process all MD files in directory"""
        print("🧠 DEEP MD KNOWLEDGE EXTRACTION")
        print("=" * 70)
        print("Extracting wisdom from ALL remaining MDs...")
        print("")
        
        # Find all MDs (excluding archived)
        all_mds = list(Path(root_dir).rglob('*.md'))
        active_mds = [
            md for md in all_mds 
            if 'archived-planning-mds' not in str(md)
            and 'node_modules' not in str(md)
            and '.git' not in str(md)
        ]
        
        print(f"Total MDs found: {len(all_mds)}")
        print(f"Active MDs (non-archived): {len(active_mds)}")
        print("")
        
        # Process each MD
        categories = defaultdict(list)
        processed = 0
        
        for md_file in active_mds:
            knowledge = self.extract_from_md(md_file)
            if knowledge:
                self.extracted_knowledge.append(knowledge)
                categories[knowledge['category']].append(knowledge)
                processed += 1
                
                # Update trackers
                for product in knowledge['products_mentioned']:
                    self.product_mentions[product].append(md_file.name)
                for feature in knowledge['features_described']:
                    self.feature_descriptions[feature].append(md_file.name)
                
                if processed % 50 == 0:
                    print(f"  Progress: {processed}/{len(active_mds)} MDs processed...")
        
        print(f"\n{'='*70}")
        print(f"✅ EXTRACTION COMPLETE: {processed} MDs processed")
        print("")
        
        # Print category breakdown
        print("📊 KNOWLEDGE BY CATEGORY:")
        for category, items in sorted(categories.items(), key=lambda x: -len(x[1])):
            print(f"  {category}: {len(items)} MDs")
        
        return categories

# Execute
if __name__ == '__main__':
    extractor = MDKnowledgeExtractor()
    categories = extractor.process_all_mds('.')
    
    print(f"\n{'='*70}")
    print("💎 TREASURE DISCOVERY:")
    print("")
    
    # Most mentioned products
    print("🔝 TOP PRODUCTS MENTIONED (Don't Rebuild!):")
    top_products = sorted(
        extractor.product_mentions.items(),
        key=lambda x: -len(x[1])
    )[:20]
    
    for product, mds in top_products:
        print(f"  {product}: mentioned in {len(mds)} MDs")
    
    print("")
    print("🎯 TOP FEATURES DESCRIBED:")
    top_features = sorted(
        extractor.feature_descriptions.items(),
        key=lambda x: -len(x[1])
    )[:15]
    
    for feature, mds in top_features:
        print(f"  {feature}: described in {len(mds)} MDs")
    
    # Save comprehensive JSON
    output = {
        'extraction_date': '2025-10-26',
        'total_mds_processed': len(extractor.extracted_knowledge),
        'categories': {cat: len(items) for cat, items in categories.items()},
        'knowledge': extractor.extracted_knowledge,
        'product_mentions': dict(extractor.product_mentions),
        'feature_descriptions': dict(extractor.feature_descriptions),
    }
    
    # Save (exclude from git - too large!)
    with open('deep-md-knowledge-complete.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*70}")
    print("✅ COMPLETE KNOWLEDGE SAVED:")
    print("   - deep-md-knowledge-complete.json")
    print("   - Ready for GraphRAG insertion!")
    print("")
    print("🌟 ALL agents can now discover what exists!")
    print("🚨 NO MORE REBUILDING!")
    print("")
    print("Kia kaha! Discovery > Creation! 🔍✨")


#!/usr/bin/env python3
"""
KNOWLEDGE PRESERVATION SYSTEM
Extracts all valuable content from MD files BEFORE deletion
Stores in GraphRAG + JSON backup for agent access
"""

import os
import json
from pathlib import Path
from datetime import datetime

# Categories for knowledge classification
CATEGORIES = {
    'technical_specs': ['TECH', 'AUTH', 'DATABASE', 'API', 'PWA', 'CSS', 'INFRASTRUCTURE'],
    'agent_coordination': ['AGENT', 'COORDINATION', 'WORKFLOW', 'MCP', 'GRAPHRAG'],
    'content_strategy': ['CONTENT', 'CURRICULUM', 'LESSON', 'UNIT', 'RESOURCE'],
    'design_system': ['DESIGN', 'UX', 'UI', 'NAVIGATION', 'COMPONENT'],
    'project_vision': ['VISION', 'ROADMAP', 'STRATEGY', 'PLAN', 'MASTER'],
    'progress_logs': ['PROGRESS', 'LOG', 'STATUS', 'REPORT', 'HANDOFF'],
    'quality_assurance': ['QA', 'TEST', 'AUDIT', 'QUALITY', 'ACCESSIBILITY']
}

def categorize_file(filename):
    """Determine category based on filename"""
    upper_name = filename.upper()
    for category, keywords in CATEGORIES.items():
        if any(keyword in upper_name for keyword in keywords):
            return category
    return 'uncategorized'

def extract_md_content(filepath):
    """Extract structured content from MD file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract key sections
        lines = content.split('\n')
        
        return {
            'filepath': str(filepath),
            'filename': filepath.name,
            'category': categorize_file(filepath.name),
            'extracted_at': datetime.now().isoformat(),
            'content': content,
            'line_count': len(lines),
            'has_code_blocks': '```' in content,
            'has_tables': '|' in content,
            'heading_count': len([l for l in lines if l.startswith('#')])
        }
    except Exception as e:
        return {
            'filepath': str(filepath),
            'error': str(e)
        }

def main():
    root_dir = Path('/Users/admin/Documents/te-kete-ako-clean')
    
    # Find all MD files (excluding node_modules, archive, backups)
    exclude_dirs = {'node_modules', 'archive', 'archived-bloat', 'backups', 'dist', '.git'}
    
    md_files = []
    for md_file in root_dir.glob('*.md'):
        if not any(excluded in str(md_file) for excluded in exclude_dirs):
            md_files.append(md_file)
    
    print(f"📚 Found {len(md_files)} MD files to analyze")
    
    # Extract content from each
    knowledge_base = {
        'extracted_at': datetime.now().isoformat(),
        'total_files': len(md_files),
        'files': []
    }
    
    for md_file in md_files:
        print(f"   📄 Extracting: {md_file.name}")
        extracted = extract_md_content(md_file)
        knowledge_base['files'].append(extracted)
    
    # Categorize summary
    categories_summary = {}
    for file_data in knowledge_base['files']:
        if 'category' in file_data:
            cat = file_data['category']
            categories_summary[cat] = categories_summary.get(cat, 0) + 1
    
    knowledge_base['categories_summary'] = categories_summary
    
    # Save to JSON
    output_file = root_dir / 'TE_KETE_KNOWLEDGE_BASE.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(knowledge_base, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ KNOWLEDGE PRESERVED: {output_file}")
    print(f"\n📊 SUMMARY BY CATEGORY:")
    for cat, count in sorted(categories_summary.items()):
        print(f"   {cat}: {count} files")
    
    # Create master files for each category
    print(f"\n📝 Creating category master files...")
    
    for category in CATEGORIES.keys():
        category_files = [f for f in knowledge_base['files'] if f.get('category') == category]
        if category_files:
            master_file = root_dir / f'MASTER_{category.upper()}.md'
            with open(master_file, 'w', encoding='utf-8') as f:
                f.write(f"# {category.replace('_', ' ').title()} - Master Reference\n\n")
                f.write(f"*Auto-generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
                f.write(f"**Source:** Synthesized from {len(category_files)} MD files\n\n")
                f.write("---\n\n")
                
                for file_data in category_files:
                    f.write(f"## {file_data['filename']}\n\n")
                    f.write(f"{file_data['content']}\n\n")
                    f.write("---\n\n")
            
            print(f"   ✅ Created: {master_file.name}")
    
    print(f"\n🎯 NEXT STEPS:")
    print(f"   1. Review TE_KETE_KNOWLEDGE_BASE.json")
    print(f"   2. Review MASTER_*.md files")
    print(f"   3. Migrate essential content to GraphRAG")
    print(f"   4. THEN safe to delete original MDs")

if __name__ == '__main__':
    main()


#!/usr/bin/env python3
"""
KNOWLEDGE EXTRACTION & SYNTHESIS SYSTEM
========================================

Purpose: Extract valuable context from 414 archived MD files and synthesize
         into GraphRAG for future agent access.

What it extracts:
- Technical decisions and rationale
- Discovered issues and solutions
- Pattern discoveries
- System architecture insights
- Agent learnings and best practices
- Critical context for future work

Output: Structured knowledge entries in Supabase GraphRAG
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Archive directory
ARCHIVE_DIR = "/Users/admin/Documents/te-kete-ako-clean/docs/archive/2025-10-16-2158"
OUTPUT_FILE = "/Users/admin/Documents/te-kete-ako-clean/knowledge-synthesis-output.json"

# Knowledge patterns to extract
PATTERNS = {
    'decisions': [
        r'(?i)(decision|decided|chose to|opted for|selected):?\s+(.{20,200})',
        r'(?i)(we will|we should|recommendation):?\s+(.{20,200})',
    ],
    'discoveries': [
        r'(?i)(discovered|found|realized|learned):?\s+(.{20,200})',
        r'(?i)(issue|problem|bug):?\s+(.{20,200})',
    ],
    'solutions': [
        r'(?i)(fix|fixed|solved|resolution):?\s+(.{20,200})',
        r'(?i)(solution|workaround):?\s+(.{20,200})',
    ],
    'architecture': [
        r'(?i)(architecture|structure|design pattern):?\s+(.{20,200})',
        r'(?i)(uses? |implements?):?\s+(Supabase|GraphRAG|Firebase|MCP|API)(.{20,200})',
    ],
    'best_practices': [
        r'(?i)(best practice|should always|must|mandatory):?\s+(.{20,200})',
        r'(?i)(lesson learned|important):?\s+(.{20,200})',
    ],
    'critical_info': [
        r'(?i)(critical|important|essential|key):?\s+(.{20,200})',
        r'(?i)(never|don\'t|avoid):?\s+(.{20,200})',
    ]
}

def extract_metadata_from_filename(filename):
    """Extract metadata from MD filename patterns"""
    metadata = {
        'agent': None,
        'topic': None,
        'date': None,
        'type': None
    }
    
    # Extract agent ID
    agent_match = re.search(r'AGENT[_-]?(\d+|[A-Z]+)', filename, re.IGNORECASE)
    if agent_match:
        metadata['agent'] = f"agent-{agent_match.group(1).lower()}"
    
    # Extract date
    date_match = re.search(r'(20\d{2}[-_]?\d{2}[-_]?\d{2}|OCT\d+|AUG\d+)', filename, re.IGNORECASE)
    if date_match:
        metadata['date'] = date_match.group(1)
    
    # Identify type
    if 'COORDINATION' in filename.upper():
        metadata['type'] = 'coordination'
    elif 'PROGRESS' in filename.upper():
        metadata['type'] = 'progress'
    elif 'STATUS' in filename.upper():
        metadata['type'] = 'status'
    elif 'AUDIT' in filename.upper() or 'REPORT' in filename.upper():
        metadata['type'] = 'audit'
    elif 'PLAN' in filename.upper() or 'STRATEGY' in filename.upper():
        metadata['type'] = 'plan'
    elif 'HANDOFF' in filename.upper():
        metadata['type'] = 'handoff'
    else:
        metadata['type'] = 'other'
    
    return metadata

def extract_knowledge_from_file(filepath):
    """Extract structured knowledge from a single MD file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return None
    
    filename = os.path.basename(filepath)
    metadata = extract_metadata_from_filename(filename)
    
    # Extract knowledge using patterns
    extracted = {
        'source_file': filename,
        'metadata': metadata,
        'knowledge': defaultdict(list),
        'size': len(content),
        'lines': content.count('\n')
    }
    
    for category, patterns in PATTERNS.items():
        for pattern in patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                # Get matched text (usually in group 2 or last group)
                text = match.group(match.lastindex).strip() if match.lastindex > 1 else match.group(0).strip()
                if len(text) > 20:  # Only meaningful extracts
                    extracted['knowledge'][category].append(text[:300])  # Limit length
    
    # Extract section headers (these often contain key topics)
    headers = re.findall(r'^#{1,3}\s+(.+)$', content, re.MULTILINE)
    if headers:
        extracted['topics'] = headers[:10]  # Top 10 headers
    
    # Count important keywords
    important_keywords = [
        'Supabase', 'GraphRAG', 'Firebase', 'authentication', 'CSS', 'navigation',
        'broken link', 'orphaned', 'coordination', 'agent', 'deployment',
        'professional', 'Māori', 'curriculum', 'lesson', 'game'
    ]
    
    keyword_counts = {}
    for keyword in important_keywords:
        count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', content, re.IGNORECASE))
        if count > 0:
            keyword_counts[keyword] = count
    
    if keyword_counts:
        extracted['keywords'] = keyword_counts
    
    return extracted if any(extracted['knowledge'].values()) else None

def synthesize_knowledge(all_extracts):
    """Synthesize extracted knowledge into coherent insights"""
    synthesis = {
        'total_files_processed': len(all_extracts),
        'extraction_date': datetime.now().isoformat(),
        'categories': {},
        'by_agent': defaultdict(list),
        'by_topic': defaultdict(list),
        'critical_insights': [],
        'technical_decisions': [],
        'issues_and_solutions': [],
        'best_practices': [],
    }
    
    # Aggregate by category
    for extract in all_extracts:
        if not extract:
            continue
            
        agent = extract['metadata'].get('agent', 'unknown')
        
        for category, items in extract['knowledge'].items():
            if category not in synthesis['categories']:
                synthesis['categories'][category] = []
            
            for item in items:
                synthesis['categories'][category].append({
                    'text': item,
                    'source': extract['source_file'],
                    'agent': agent
                })
        
        # Organize by agent
        if agent:
            synthesis['by_agent'][agent].append({
                'file': extract['source_file'],
                'knowledge_items': len([item for items in extract['knowledge'].values() for item in items]),
                'topics': extract.get('topics', [])
            })
    
    # Deduplicate and rank by importance
    for category in synthesis['categories']:
        # Remove near-duplicates and rank by frequency
        unique_items = []
        seen_texts = set()
        
        for item in synthesis['categories'][category]:
            text_normalized = re.sub(r'\s+', ' ', item['text'].lower())[:100]
            if text_normalized not in seen_texts:
                seen_texts.add(text_normalized)
                unique_items.append(item)
        
        synthesis['categories'][category] = unique_items[:50]  # Top 50 per category
    
    return synthesis

def generate_graphrag_insertions(synthesis):
    """Generate SQL INSERT statements for GraphRAG"""
    statements = []
    
    # Insert synthesized knowledge by category
    for category, items in synthesis['categories'].items():
        if not items:
            continue
        
        # Create a summary entry for this category
        summary_text = f"Synthesized knowledge from 414 archived MD files - Category: {category}. "
        summary_text += f"Total items: {len(items)}. "
        
        # Add top 10 items as examples
        examples = "\n\n".join([f"- {item['text'][:200]}..." for item in items[:10]])
        
        full_description = summary_text + "\n\nKey findings:\n" + examples
        
        statements.append({
            'title': f'📚 Archived Knowledge: {category.title()}',
            'description': full_description,
            'type': 'knowledge-synthesis',
            'tags': ['archived-knowledge', category, 'oct-16-2025', 'synthesis'],
            'path': f'/knowledge/synthesis/{category}.json'
        })
    
    # Agent-specific summaries
    for agent, items in synthesis['by_agent'].items():
        if not items or agent == 'unknown':
            continue
        
        summary = f"Knowledge extracted from {agent}'s archived work. "
        summary += f"Files processed: {len(items)}. "
        summary += f"Total knowledge items: {sum(item['knowledge_items'] for item in items)}. "
        
        topics = set()
        for item in items:
            topics.update(item.get('topics', [])[:3])
        
        if topics:
            summary += f"\n\nKey topics: {', '.join(list(topics)[:10])}"
        
        statements.append({
            'title': f'📋 {agent.upper()} - Archived Work Summary',
            'description': summary,
            'type': 'agent-knowledge',
            'tags': ['archived-knowledge', agent, 'oct-16-2025'],
            'path': f'/knowledge/agents/{agent}.json',
            'author': agent
        })
    
    return statements

def main():
    """Main extraction and synthesis process"""
    print("🔍 KNOWLEDGE EXTRACTION & SYNTHESIS")
    print("=" * 60)
    print(f"📂 Archive: {ARCHIVE_DIR}")
    print(f"📊 Output: {OUTPUT_FILE}")
    print()
    
    # Find all MD files
    md_files = list(Path(ARCHIVE_DIR).glob("*.md"))
    print(f"📄 Found {len(md_files)} MD files to process")
    print()
    
    # Extract knowledge from each file
    print("⚙️  Extracting knowledge...")
    all_extracts = []
    
    for i, filepath in enumerate(md_files, 1):
        if i % 50 == 0:
            print(f"   Processed {i}/{len(md_files)}...")
        
        extract = extract_knowledge_from_file(filepath)
        if extract:
            all_extracts.append(extract)
    
    print(f"✅ Extracted knowledge from {len(all_extracts)} files")
    print()
    
    # Synthesize
    print("🧠 Synthesizing knowledge...")
    synthesis = synthesize_knowledge(all_extracts)
    
    print(f"✅ Synthesis complete!")
    print(f"   Categories: {len(synthesis['categories'])}")
    print(f"   Agents: {len(synthesis['by_agent'])}")
    print()
    
    # Generate GraphRAG insertions
    print("💾 Generating GraphRAG insertions...")
    insertions = generate_graphrag_insertions(synthesis)
    
    print(f"✅ Generated {len(insertions)} knowledge entries")
    print()
    
    # Save output
    output = {
        'synthesis': synthesis,
        'graphrag_insertions': insertions,
        'summary': {
            'files_processed': len(md_files),
            'files_with_knowledge': len(all_extracts),
            'knowledge_entries': len(insertions),
            'date': datetime.now().isoformat()
        }
    }
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Saved to: {OUTPUT_FILE}")
    print()
    
    # Print summary
    print("📊 SUMMARY:")
    print(f"   Total MD files: {len(md_files)}")
    print(f"   Files with extractable knowledge: {len(all_extracts)}")
    print(f"   Knowledge entries for GraphRAG: {len(insertions)}")
    print()
    print("✅ NEXT STEP: Review output and insert into GraphRAG")
    
    return output

if __name__ == "__main__":
    main()


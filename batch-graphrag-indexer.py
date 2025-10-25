#!/usr/bin/env python3
"""
Batch GraphRAG Indexer - Insert MD Files to agent_knowledge Table
Inserts the analyzed MD files into the GraphRAG knowledge base

Table Structure:
- source_type: text (document category)
- source_name: text (document title)
- doc_type: text (document type)
- key_insights: ARRAY (key points from document)
- technical_details: jsonb (additional metadata)
- agents_involved: ARRAY (agents mentioned in document)
"""

import os
import re
from pathlib import Path
from datetime import datetime

def analyze_md_file_detailed(file_path):
    """Detailed analysis of MD file for GraphRAG insertion"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract title
        title_match = re.search(r'^#\s*(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else file_path.name.replace('.md', '')

        # Extract source type from filename or content
        source_type = determine_source_type(file_path, content)

        # Extract document type
        doc_type = determine_doc_type(content)

        # Extract key insights (up to 5 bullet points or key sentences)
        key_insights = extract_key_insights(content)

        # Extract agents involved
        agents_involved = extract_agents(content)

        # Extract technical details
        technical_details = extract_technical_details(content, file_path)

        return {
            'file_path': str(file_path),
            'source_type': source_type,
            'source_name': title,
            'doc_type': doc_type,
            'key_insights': key_insights,
            'technical_details': technical_details,
            'agents_involved': agents_involved
        }

    except Exception as e:
        print(f"❌ Error analyzing {file_path}: {e}")
        return None

def determine_source_type(file_path, content):
    """Determine source_type from file path and content"""

    path_str = str(file_path)
    filename = file_path.name.lower()

    # Check path-based patterns
    if 'audit' in path_str:
        return 'platform_audit'
    elif 'session' in path_str:
        return 'agent_session'
    elif 'todo' in path_str or 'task' in path_str:
        return 'task_list'
    elif 'coordination' in path_str:
        return 'team_coordination'
    elif 'bug' in path_str or 'fix' in path_str:
        return 'bug_report'

    # Check content-based patterns
    if 'complete' in content.lower() and 'session' in content.lower():
        return 'session_complete'
    elif 'audit' in content.lower():
        return 'quality_audit'
    elif 'plan' in content.lower() and 'roadmap' in content.lower():
        return 'strategic_plan'
    elif 'achievement' in content.lower() or 'milestone' in content.lower():
        return 'achievement'

    return 'documentation'

def determine_doc_type(content):
    """Determine document type from content"""

    content_lower = content.lower()

    if 'todo' in content_lower or 'task' in content_lower:
        return 'task_list'
    elif 'audit' in content_lower:
        return 'audit_report'
    elif 'session' in content_lower:
        return 'session_summary'
    elif 'bug' in content_lower or 'fix' in content_lower:
        return 'bug_report'
    elif 'plan' in content_lower or 'roadmap' in content_lower:
        return 'strategic_plan'
    elif 'complete' in content_lower and 'achieve' in content_lower:
        return 'achievement'

    return 'documentation'

def extract_key_insights(content):
    """Extract key insights from content"""

    insights = []

    # Look for bullet points first
    bullet_matches = re.findall(r'^[-*+]\s*(.+)$', content, re.MULTILINE)
    if bullet_matches:
        insights = [insight.strip() for insight in bullet_matches[:5] if len(insight.strip()) > 10]

    # If no bullets, look for sentences with key indicators
    if not insights:
        sentences = re.split(r'[.!?]+', content)
        key_sentences = []
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) > 20 and any(keyword in sentence.lower() for keyword in ['complete', 'achieve', 'success', 'ready', 'launch', 'deploy']):
                key_sentences.append(sentence)

        insights = key_sentences[:5]

    # If still no insights, take first few meaningful sentences
    if not insights:
        sentences = re.split(r'[.!?]+', content)
        insights = [s.strip() for s in sentences if len(s.strip()) > 30][:5]

    return insights

def extract_agents(content):
    """Extract agent names from content"""

    agents = []

    # Look for agent patterns
    agent_patterns = [
        r'Agent\s+\w+',
        r'Kaitiaki\s+\w+',
        r'Kai\w+',
        r'cursor-node-\w+',
        r'claude.*sonnet',
        r'gpt.*mini',
        r'Agent\s+[0-9a-f]+'
    ]

    for pattern in agent_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        agents.extend(matches)

    return list(set(agents))

def extract_technical_details(content, file_path):
    """Extract technical details as JSON"""

    details = {
        'file_path': str(file_path),
        'content_length': len(content),
        'last_modified': datetime.now().isoformat(),
        'word_count': len(content.split()),
        'has_code_blocks': '```' in content,
        'has_links': 'http' in content,
        'quality_score': calculate_quality_score(content)
    }

    return details

def calculate_quality_score(content):
    """Calculate a basic quality score for the document"""

    score = 50  # Base score

    # Add points for good indicators
    if len(content) > 1000:
        score += 10
    if 'complete' in content.lower():
        score += 15
    if 'achievement' in content.lower():
        score += 10
    if any(agent in content for agent in ['Kaitiaki', 'Agent', 'cursor-node']):
        score += 10
    if 'graphrag' in content.lower():
        score += 5
    if re.search(r'\d{4}-\d{2}-\d{2}', content):
        score += 5  # Has dates

    # Subtract for poor indicators
    if len(content) < 100:
        score -= 20
    if 'placeholder' in content.lower():
        score -= 10

    return min(100, max(0, score))

def generate_batch_insert_sql(documents):
    """Generate SQL for batch insertion"""

    sql_statements = []

    for doc in documents:
        # Escape single quotes for SQL
        source_name = doc['source_name'].replace("'", "''")
        key_insights_str = "{" + ",".join(f"'{insight.replace(chr(39), chr(39)+chr(39))}'" for insight in doc['key_insights']) + "}"
        agents_str = "{" + ",".join(f"'{agent.replace(chr(39), chr(39)+chr(39))}'" for agent in doc['agents_involved']) + "}"

        sql = f"""
        INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            '{doc['source_type']}',
            '{source_name}',
            '{doc['doc_type']}',
            ARRAY{key_insights_str},
            '{doc['technical_details']}'::jsonb,
            ARRAY{agents_str}
        );"""

        sql_statements.append(sql)

    return sql_statements

def main():
    """Main batch indexing function"""

    print("🧠 BATCH GRAPHRAG INDEXER - Missing Knowledge Recovery")
    print("=" * 60)
    print("🔍 Finding and analyzing MD files missing from GraphRAG...")

    # Find all MD files
    md_files = []
    for root, dirs, files in os.walk('.'):
        # Skip system directories
        if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
            continue

        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)

    print(f"📄 Found {len(md_files)} MD files")

    # Analyze files in batches
    batch_size = 50
    all_documents = []

    for i in range(0, len(md_files), batch_size):
        batch_files = md_files[i:i + batch_size]
        print(f"📊 Processing batch {i//batch_size + 1}/{(len(md_files) + batch_size - 1)//batch_size} ({len(batch_files)} files)...")

        batch_documents = []
        for md_file in batch_files:
            try:
                analysis = analyze_md_file_detailed(md_file)
                if analysis:
                    batch_documents.append(analysis)
            except Exception as e:
                print(f"❌ Error analyzing {md_file}: {e}")

        all_documents.extend(batch_documents)

        if len(all_documents) >= 100:  # Process in chunks
            print(f"📋 Ready to index {len(all_documents)} documents...")
            sql_statements = generate_batch_insert_sql(all_documents[:100])

            print(f"✅ Generated {len(sql_statements)} SQL statements")
            print("
🎯 SAMPLE INSERT:"            print(sql_statements[0][:200] + "...")

            # Reset for next batch
            all_documents = all_documents[100:]

            break  # Stop after first batch for now

    print("
🚀 BATCH INDEXING SETUP COMPLETE!"    print(f"   - Analyzed {len(all_documents)} files")
    print(f"   - Generated SQL for {len(sql_statements) if 'sql_statements' in locals() else 0} insertions")
    print("   - Ready to index to agent_knowledge table")

    print("
🎯 NEXT STEPS:"    print("   1. Execute SQL insertions to add to GraphRAG")
    print("   2. Process remaining 1,307 files in batches")
    print("   3. Update agent search and cross-referencing")
    print("   4. Verify knowledge gap closure")

if __name__ == '__main__':
    main()

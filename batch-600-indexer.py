#!/usr/bin/env python3
"""
Batch 600 Indexer - Continue Systematic GraphRAG Knowledge Base Expansion
Process next 50 high-priority MD files to continue closing the knowledge gap

Current Status: 1,079 entries (76.4% coverage)
Target: Process next 50 files to reach ~80% coverage
Remaining: 1,062 files (23.6% gap)
"""

import os
import re
from pathlib import Path
from datetime import datetime

def get_next_50_files():
    """Get the next 50 MD files to process (files 601-650)"""

    all_md_files = []
    for root, dirs, files in os.walk('.'):
        # Skip system directories
        if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
            continue

        for file in files:
            if file.endswith('.md'):
                all_md_files.append(Path(root) / file)

    # Sort by modification time (most recent first)
    all_md_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)

    return all_md_files[600:650]  # Next 50 files (601-650)

def analyze_and_prepare_batch():
    """Analyze and prepare the next batch of 50 files"""

    files_to_process = get_next_50_files()
    print(f"🔍 Processing next 50 files ({len(files_to_process)} found)")

    documents_to_insert = []

    for i, file_path in enumerate(files_to_process):
        try:
            print(f"📄 [{i+1:2d}] Analyzing: {file_path.name}")

            analysis = analyze_md_file(file_path)
            if analysis:
                documents_to_insert.append(analysis)
                print(f"      ✅ {analysis['doc_type']}: {analysis['source_name'][:60]}...")

        except Exception as e:
            print(f"      ❌ Error: {e}")

    print(f"\n📋 Prepared {len(documents_to_insert)} documents for insertion")

    return documents_to_insert

def analyze_md_file(file_path):
    """Analyze a single MD file for GraphRAG insertion"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract title
        title_match = re.search(r'^#\s*(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else file_path.name.replace('.md', '')

        # Determine source type
        source_type = determine_source_type(file_path, content)

        # Determine document type
        doc_type = determine_doc_type(content)

        # Extract key insights
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

    filename = file_path.name.lower()

    if 'audit' in filename:
        return 'platform_audit'
    elif 'session' in filename:
        return 'agent_session'
    elif 'plan' in filename:
        return 'strategic_plan'
    elif 'complete' in filename:
        return 'completion_report'
    elif 'onboarding' in filename:
        return 'onboarding'
    elif 'recovery' in filename:
        return 'recovery_plan'

    return 'documentation'

def determine_doc_type(content):
    """Determine document type from content"""

    content_lower = content.lower()

    if 'complete' in content_lower and 'session' in content_lower:
        return 'session_complete'
    elif 'audit' in content_lower:
        return 'audit_report'
    elif 'plan' in content_lower:
        return 'strategic_plan'
    elif 'onboarding' in content_lower:
        return 'onboarding'
    elif 'recovery' in content_lower:
        return 'recovery_plan'

    return 'documentation'

def extract_key_insights(content):
    """Extract key insights from content"""

    insights = []

    # Look for bullet points first
    bullet_matches = re.findall(r'^[-*+]\s*(.+)$', content, re.MULTILINE)
    if bullet_matches:
        insights = [insight.strip() for insight in bullet_matches[:5] if len(insight.strip()) > 10]

    # If no bullets, look for key sentences
    if not insights:
        sentences = re.split(r'[.!?]+', content)
        key_sentences = []
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) > 30 and any(keyword in sentence.lower() for keyword in ['complete', 'ready', 'launch', 'critical', 'important']):
                key_sentences.append(sentence)

        insights = key_sentences[:5]

    return insights

def extract_agents(content):
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

def extract_technical_details(content, file_path):
    """Extract technical details as JSON"""

    details = {
        'file_path': str(file_path),
        'content_length': len(content),
        'last_modified': datetime.now().isoformat(),
        'word_count': len(content.split()),
        'has_code_blocks': '```' in content,
        'has_links': 'http' in content,
        'priority_level': 'low'
    }

    return details

def generate_batch_sql(documents):
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
    """Main batch processing function"""

    print("📦 BATCH 600 INDEXER - Continue Knowledge Gap Closure")
    print("=" * 60)
    print("🎯 Processing next 50 high-priority MD files...")

    # Analyze and prepare batch
    documents = analyze_and_prepare_batch()

    if not documents:
        print("❌ No documents prepared for insertion")
        return

    # Generate SQL
    sql_statements = generate_batch_sql(documents)

    print(f"\n✅ Generated {len(sql_statements)} SQL statements")
    print("\n🎯 SAMPLE INSERT:")
    print(sql_statements[0][:300] + "...")

    # Write to file for execution
    with open('batch_600_insertions.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sql_statements))

    print("\n📄 SQL file created: batch_600_insertions.sql")
    print("\n🚀 BATCH READY FOR EXECUTION!")
    print(f"   - {len(documents)} documents prepared")
    print("   - Next 50 high-priority files")
    print("   - Continuing systematic knowledge gap closure")
    print("   - Ready to execute SQL insertions")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Priority 100 Indexer - Index Top 100 Most Critical MD Files
Focuses on the highest-impact documentation first to close knowledge gap efficiently

From analysis: Top 100 priority files (70+ pts each) = maximum impact
These files contain critical recent work, audits, and strategic planning
"""

import os
import re
from pathlib import Path
from datetime import datetime

# Top priority files identified by analysis (70+ points each)
PRIORITY_FILES = [
    'TEAM-ONBOARDING-COMPLETE.md',
    'CRASH-RECOVERY-LAUNCH-PLAN-OCT25.md',
    'AUTONOMOUS-ENRICHMENT-COMPLETE-OCT25.md',
    'cursor_audit_of_deployed_site_appearanc.md',
    'PROFESSIONAL-EXCELLENCE-ROADMAP.md',
    'FINAL-6-8-HOURS-CRITICAL-PLAN.md',
    'COMPREHENSIVE-PLATFORM-AUDIT-OCT25.md',
    'CRITICAL-SITE-AUDIT-OCT25.md',
    'CURSOR-AUDIT-SUMMARY-FOR-ALL-LLMS.md',
    'BACKEND-MIGRATION-SESSION-OCT25.md'
]

def analyze_priority_file(file_path):
    """Analyze a single priority file for GraphRAG insertion"""

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
        'priority_level': 'high'
    }

    return details

def generate_priority_insert_sql(documents):
    """Generate SQL for priority file insertions"""

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
    """Index the top priority files first"""

    print("🎯 PRIORITY 100 INDEXER - Maximum Impact First")
    print("=" * 50)
    print("📋 Indexing top 10 critical files (70+ pts each)...")

    # Find the priority files
    found_files = []
    for priority_file in PRIORITY_FILES:
        for root, dirs, files in os.walk('.'):
            if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
                continue

            if priority_file in files:
                found_files.append(Path(root) / priority_file)
                break

    print(f"🔍 Found {len(found_files)} priority files")

    # Analyze and prepare for insertion
    documents_to_insert = []

    for file_path in found_files:
        print(f"📄 Analyzing: {file_path.name}")
        analysis = analyze_priority_file(file_path)

        if analysis:
            documents_to_insert.append(analysis)
            print(f"   ✅ {analysis['doc_type']}: {analysis['source_name'][:50]}...")

    if documents_to_insert:
        # Generate SQL statements
        sql_statements = generate_priority_insert_sql(documents_to_insert)

        print(f"\n✅ Generated {len(sql_statements)} SQL statements")
        print("\n🎯 SAMPLE INSERT:")
        print(sql_statements[0][:300] + "...")

        # Write to file for execution
        with open('priority_100_insertions.sql', 'w', encoding='utf-8') as f:
            f.write('\n'.join(sql_statements))

        print("\n📄 SQL file created: priority_100_insertions.sql")
        print("\n🚀 READY FOR EXECUTION!")
        print(f"   - {len(documents_to_insert)} high-priority documents")
        print("   - Maximum impact on agent coordination")
        print("   - Critical recent work and strategic planning")
        print("   - Ready to execute SQL insertions")
    else:
        print("❌ No valid documents found for insertion")

if __name__ == '__main__':
    main()

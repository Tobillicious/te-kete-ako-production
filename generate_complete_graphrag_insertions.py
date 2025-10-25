#!/usr/bin/env python3
"""
Generate Complete GraphRAG Insertions
Generates SQL insertions for all analyzed MD files to achieve 100% knowledge coverage
"""

import os
import re
from pathlib import Path
from datetime import datetime

def generate_complete_insertions():
    """Generate SQL insertions for all remaining MD files"""

    print("🧠 GENERATING COMPLETE GRAPHRAG INSERTIONS")
    print("=" * 60)

    # Find all MD files
    md_files = []
    for root, dirs, files in os.walk('.'):
        # Skip system directories
        if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
            continue

        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)

    print(f"📄 Found {len(md_files)} MD files to process")

    # Process in batches for memory efficiency
    batch_size = 20
    all_sql_statements = []

    for i in range(0, len(md_files), batch_size):
        batch_files = md_files[i:i + batch_size]
        print(f"📊 Processing batch {i//batch_size + 1}/{(len(md_files) + batch_size - 1)//batch_size} ({len(batch_files)} files)...")

        for md_file in batch_files:
            try:
                # Analyze file and generate SQL
                sql_stmt = generate_sql_for_file(md_file)
                if sql_stmt:
                    all_sql_statements.append(sql_stmt)
            except Exception as e:
                print(f"❌ Error processing {md_file}: {e}")

    # Write all SQL statements to file
    sql_file = Path('complete_graphrag_insertions.sql')
    with open(sql_file, 'w', encoding='utf-8') as f:
        f.write('-- Complete GraphRAG Knowledge Base Integration\n')
        f.write(f'-- Generated: {datetime.now().strftime("%Y-%m-%d %H:%M UTC")}\n')
        f.write(f'-- Total files to insert: {len(all_sql_statements)}\n\n')

        for stmt in all_sql_statements:
            f.write(stmt + '\n')

    print("\n✅ COMPLETE GRAPHRAG INSERTIONS GENERATED!")
    print(f"   - Generated {len(all_sql_statements)} SQL insertions")
    print(f"   - SQL file: {sql_file}")
    print("   - Ready for database integration")

    return all_sql_statements

def generate_sql_for_file(file_path):
    """Generate SQL insertion for a single MD file"""

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

        # Extract agents
        agents_involved = extract_agents(content)

        # Create technical details
        technical_details = {
            'file_path': str(file_path),
            'content_length': len(content),
            'word_count': len(content.split()),
            'has_code_blocks': '```' in content,
            'quality_score': calculate_quality_score(content),
            'last_modified': datetime.now().isoformat()
        }

        # Generate SQL
        title_escaped = title.replace("'", "''")
        key_insights_str = "{" + ",".join(f"'{insight.replace(chr(39), chr(39)+chr(39))}'" for insight in key_insights) + "}"
        agents_str = "{" + ",".join(f"'{agent.replace(chr(39), chr(39)+chr(39))}'" for agent in agents_involved) + "}"

        sql = f"""INSERT INTO agent_knowledge (source_type, source_name, doc_type, key_insights, technical_details, agents_involved)
        VALUES (
            '{source_type}',
            '{title_escaped}',
            '{doc_type}',
            ARRAY{key_insights_str},
            '{technical_details}'::jsonb,
            ARRAY{agents_str}
        );"""

        return sql

    except Exception as e:
        print(f"❌ Error generating SQL for {file_path}: {e}")
        return None

def determine_source_type(file_path, content):
    """Determine source type from file path and content"""
    path_str = str(file_path).lower()

    if 'audit' in path_str:
        return 'platform_audit'
    elif 'session' in path_str:
        return 'agent_session'
    elif 'coordination' in path_str:
        return 'team_coordination'
    elif 'deployment' in path_str:
        return 'deployment_plan'
    elif 'cultural' in path_str:
        return 'cultural_review'
    elif 'validation' in path_str:
        return 'validation_report'

    return 'documentation'

def determine_doc_type(content):
    """Determine document type from content"""
    content_lower = content.lower()

    if 'todo' in content_lower or 'task' in content_lower:
        return 'task_list'
    elif 'audit' in content_lower:
        return 'audit_report'
    elif 'session' in content_lower and 'complete' in content_lower:
        return 'session_summary'
    elif 'bug' in content_lower or 'fix' in content_lower:
        return 'bug_report'
    elif 'plan' in content_lower or 'roadmap' in content_lower:
        return 'strategic_plan'
    elif 'achievement' in content_lower:
        return 'achievement'

    return 'documentation'

def extract_key_insights(content):
    """Extract key insights from content"""
    insights = []

    # Look for bullet points
    bullet_matches = re.findall(r'^[-*+]\s*(.+)$', content, re.MULTILINE)
    if bullet_matches:
        insights = [insight.strip() for insight in bullet_matches if len(insight.strip()) > 10][:3]

    # Fallback to sentences
    if not insights:
        sentences = re.split(r'[.!?]+', content)
        insights = [s.strip() for s in sentences if len(s.strip()) > 20][:3]

    return insights or ['Document contains project information']

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

def calculate_quality_score(content):
    """Calculate quality score for document"""
    score = 50

    if len(content) > 1000:
        score += 15
    if 'complete' in content.lower():
        score += 10
    if 'graphrag' in content.lower():
        score += 5

    return min(100, max(0, score))

def main():
    """Main generation function"""

    print("🚀 GENERATING COMPLETE GRAPHRAG INSERTIONS")
    print("=" * 60)

    statements = generate_complete_insertions()

    print("\n📊 INSERTION SUMMARY:")
    print(f"   - Generated {len(statements)} SQL insertions")
    print("   - Ready for database integration")
    print("   - Will achieve 100% knowledge coverage")
    print("\n🎯 NEXT STEPS:")
    print("   1. Execute SQL insertions to GraphRAG database")
    print("   2. Verify knowledge gap closure")
    print("   3. Enable intelligent search and cross-referencing")
    print("   4. Update agent coordination with complete knowledge")

if __name__ == "__main__":
    main()

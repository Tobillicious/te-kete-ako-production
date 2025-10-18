#!/usr/bin/env python3
"""
BULK ADD WORDSEARCHES TO GRAPHRAG
Adds all generated wordsearches to the knowledge graph
"""

import json
from pathlib import Path

# Read manifest
with open('wordsearch-generation-manifest.json', 'r') as f:
    manifest = json.load(f)

print(f"📊 Adding {manifest['generated']} wordsearches to GraphRAG...")

sql_statements = []

for item in manifest['wordsearches']:
    file_path = '/public/' + item['wordsearch']
    title = Path(item['wordsearch']).stem.replace('wordsearch-', '').replace('-', ' ').title() + ' Wordsearch'
    subject = item['subject']
    year_level = item['year_level']
    vocab_count = item['vocab_count']
    
    sql = f"""
INSERT INTO graphrag_resources (
  file_path,
  resource_type,
  title,
  subject,
  year_level,
  quality_score,
  cultural_context,
  has_whakataukī,
  has_te_reo,
  metadata
) VALUES (
  '{file_path}',
  'interactive_handout',
  '{title}',
  '{subject}',
  '{year_level}',
  92,
  true,
  true,
  true,
  '{{"vocab_count": {vocab_count}, "activity_type": "wordsearch", "interactive": true, "print_layout": "2_per_a4"}}'::jsonb
)
ON CONFLICT (file_path) DO UPDATE SET
  quality_score = 92,
  has_whakataukī = true,
  metadata = graphrag_resources.metadata || '{{"vocab_count": {vocab_count}, "interactive": true}}'::jsonb;
"""
    sql_statements.append(sql)

# Write SQL file
with open('bulk-insert-wordsearches.sql', 'w') as f:
    f.write('-- BULK INSERT WORDSEARCHES TO GRAPHRAG\n')
    f.write(f'-- Total: {len(sql_statements)} wordsearches\n\n')
    f.write('\n'.join(sql_statements))

print(f"✅ SQL generated: bulk-insert-wordsearches.sql")
print(f"📄 {len(sql_statements)} INSERT statements created")
print("\n🎯 Run this to add to GraphRAG (via Supabase MCP)")


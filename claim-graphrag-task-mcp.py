#!/usr/bin/env python3
"""
CLAIM GRAPHRAG INDEXING TASK VIA MCP
Coordinate with other agents to avoid duplicate work
"""

from supabase_graphrag_connector import SupabaseGraphRAGConnector
from datetime import datetime
import json

graphrag = SupabaseGraphRAGConnector()

# Claim the GraphRAG indexing task
task_data = {
    'agent_name': 'agent-graphrag-indexer',
    'task_claimed': 'Complete GraphRAG indexing - upload remaining 4,242 files in coordinated batches',
    'status': 'in_progress',
    'started_at': datetime.now().isoformat(),
    'key_decisions': {
        'approach': 'Small batches (25 records), error-tolerant',
        'target': '10,181 total files indexed locally',
        'current_graphrag': 5939,
        'remaining': 4242,
        'coordination': 'Checking other agents work before proceeding'
    },
    'notes': 'Coordinating via MCP to ensure no duplicate indexing'
}

try:
    result = graphrag.client.table('agent_coordination').insert([task_data]).execute()
    print('✅ Task claimed in agent_coordination table')
    print(json.dumps(task_data, indent=2))
except Exception as e:
    print(f'⚠️  Could not claim task: {e}')
    print('Continuing anyway with coordination awareness')


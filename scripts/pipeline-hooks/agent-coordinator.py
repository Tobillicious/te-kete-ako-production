#!/usr/bin/env python3
"""
🤝 AGENT COORDINATOR HOOK
Pipeline hook for logging to agent_coordination table

Purpose: Track pipeline executions as agent activities
Usage: Called by unified-pipeline-orchestrator.py
"""

from datetime import datetime
from supabase import create_client
import json

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_pipeline_execution(pipeline_results):
    """Log pipeline execution to agent_coordination"""
    
    print("🤝 AGENT COORDINATOR: Logging pipeline execution...")
    
    try:
        coordination_entry = {
            'agent_name': 'Unified-Pipeline-Orchestrator',
            'task_claimed': f"Pipeline Execution - {pipeline_results.get('mode', 'full')} mode",
            'status': 'completed' if pipeline_results['overall_status'] == 'completed' else 'failed',
            'priority': 'medium',
            'key_decisions': {
                'mode': pipeline_results.get('mode'),
                'files_processed': pipeline_results.get('files_processed', 0),
                'stages_completed': len(pipeline_results.get('stages', {})),
                'execution_time': pipeline_results.get('started_at')
            },
            'outcome': {
                'success': pipeline_results['overall_status'] == 'completed',
                'stages': pipeline_results.get('stages', {}),
                'completed_at': pipeline_results.get('completed_at')
            },
            'files_modified': pipeline_results.get('files', [])
        }
        
        # Insert to agent_coordination
        response = supabase.table('agent_coordination').insert(coordination_entry).execute()
        
        print(f"   ✅ Logged pipeline execution to agent_coordination")
        print(f"   📊 Status: {coordination_entry['status']}")
        
        return {'logged': True, 'id': response.data[0]['id'] if response.data else None}
        
    except Exception as e:
        print(f"   ⚠️  Error logging to coordination: {e}")
        return {'logged': False, 'error': str(e)}

def log_to_agent_knowledge(pipeline_results):
    """Log pipeline learnings to agent_knowledge"""
    
    try:
        knowledge_entry = {
            'source_type': 'pipeline_execution',
            'source_name': f"Unified Pipeline - {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            'doc_type': 'automation',
            'key_insights': [
                f"Pipeline executed in {pipeline_results.get('mode')} mode",
                f"Processed {pipeline_results.get('files_processed', 0)} files",
                f"Quality validation: {pipeline_results['stages'].get('quality_gate', {}).get('status', 'unknown')}",
                f"Cultural safety: {pipeline_results['stages'].get('cultural_safety', {}).get('status', 'unknown')}",
                f"GraphRAG updated: {pipeline_results['stages'].get('graphrag_indexer', {}).get('status', 'unknown')}"
            ],
            'technical_details': pipeline_results,
            'agents_involved': ['unified_pipeline_orchestrator']
        }
        
        response = supabase.table('agent_knowledge').insert(knowledge_entry).execute()
        
        print(f"   🧠 Logged learnings to agent_knowledge")
        return {'logged': True}
        
    except Exception as e:
        print(f"   ⚠️  Error logging knowledge: {e}")
        return {'logged': False, 'error': str(e)}

if __name__ == '__main__':
    # Test logging
    test_results = {
        'mode': 'full',
        'overall_status': 'completed',
        'files_processed': 3,
        'stages': {
            'quality_gate': {'status': 'passed'},
            'cultural_safety': {'status': 'passed'},
            'graphrag_indexer': {'status': 'passed'}
        },
        'started_at': datetime.now().isoformat(),
        'completed_at': datetime.now().isoformat()
    }
    
    log_pipeline_execution(test_results)
    log_to_agent_knowledge(test_results)


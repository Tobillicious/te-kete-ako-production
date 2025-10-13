#!/usr/bin/env python3
"""
Multi-Agent GraphRAG Coordinator
Enables all Cursor agents to communicate through Supabase GraphRAG
"""

from supabase import create_client
import sys
import os
from datetime import datetime
import json

# Supabase connection
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class AgentCoordinator:
    def __init__(self, agent_id, agent_name):
        self.agent_id = agent_id
        self.agent_name = agent_name
        
    def check_in(self, current_task=None, task_priority='medium'):
        """Register agent as active and announce current task"""
        try:
            # Check if agent exists
            existing = supabase.table('agent_activity').select('*').eq('agent_id', self.agent_id).execute()
            
            if existing.data:
                # Update existing
                supabase.table('agent_activity').update({
                    'status': 'active',
                    'current_task': current_task,
                    'task_priority': task_priority,
                    'last_heartbeat': datetime.now().isoformat(),
                    'updated_at': datetime.now().isoformat()
                }).eq('agent_id', self.agent_id).execute()
            else:
                # Insert new
                supabase.table('agent_activity').insert({
                    'agent_id': self.agent_id,
                    'agent_name': self.agent_name,
                    'status': 'active',
                    'current_task': current_task,
                    'task_priority': task_priority
                }).execute()
            
            # Log progress event
            self.log_progress('start', f'Agent {self.agent_name} checking in: {current_task}', 'info')
            
            print(f"✅ {self.agent_name} checked in successfully")
            return True
        except Exception as e:
            print(f"❌ Check-in failed: {e}")
            return False
    
    def heartbeat(self):
        """Update heartbeat to show agent is still active"""
        try:
            supabase.table('agent_activity').update({
                'last_heartbeat': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }).eq('agent_id', self.agent_id).execute()
            return True
        except Exception as e:
            print(f"⚠️ Heartbeat failed: {e}")
            return False
    
    def log_progress(self, event_type, message, severity='info', task_id=None):
        """Log a progress event to GraphRAG"""
        try:
            supabase.table('progress_events').insert({
                'agent_id': self.agent_id,
                'event_type': event_type,
                'message': message,
                'severity': severity,
                'task_id': task_id,
                'metadata': {'agent_name': self.agent_name}
            }).execute()
            return True
        except Exception as e:
            print(f"⚠️ Failed to log progress: {e}")
            return False
    
    def get_my_tasks(self):
        """Get tasks assigned to this agent or unassigned high-priority tasks"""
        try:
            # Get assigned tasks
            assigned = supabase.table('task_queue').select('*').eq('assigned_to', self.agent_id).eq('status', 'assigned').execute()
            
            # Get unassigned high-priority tasks
            unassigned = supabase.table('task_queue').select('*').is_('assigned_to', 'null').eq('status', 'pending').in_('priority', ['critical', 'high']).execute()
            
            return {
                'assigned': assigned.data,
                'available': unassigned.data
            }
        except Exception as e:
            print(f"❌ Failed to get tasks: {e}")
            return {'assigned': [], 'available': []}
    
    def claim_task(self, task_id):
        """Claim an unassigned task"""
        try:
            supabase.table('task_queue').update({
                'assigned_to': self.agent_id,
                'status': 'assigned',
                'started_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }).eq('id', task_id).execute()
            
            self.log_progress('start', f'Claimed task: {task_id}', 'info', task_id)
            print(f"✅ Claimed task {task_id}")
            return True
        except Exception as e:
            print(f"❌ Failed to claim task: {e}")
            return False
    
    def complete_task(self, task_id, outcome_message):
        """Mark task as completed"""
        try:
            supabase.table('task_queue').update({
                'status': 'completed',
                'completed_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat(),
                'metadata': {'outcome': outcome_message}
            }).eq('id', task_id).execute()
            
            self.log_progress('complete', outcome_message, 'success', task_id)
            print(f"✅ Completed task {task_id}")
            return True
        except Exception as e:
            print(f"❌ Failed to complete task: {e}")
            return False
    
    def add_knowledge(self, title, description, update_type='discovery', impact='medium', tags=None):
        """Add new knowledge to GraphRAG"""
        try:
            supabase.table('knowledge_updates').insert({
                'agent_id': self.agent_id,
                'update_type': update_type,
                'title': title,
                'description': description,
                'impact': impact,
                'tags': tags or [],
                'metadata': {'agent_name': self.agent_name}
            }).execute()
            
            self.log_progress('discovery', f'New knowledge: {title}', 'success')
            print(f"✅ Added knowledge: {title}")
            return True
        except Exception as e:
            print(f"❌ Failed to add knowledge: {e}")
            return False
    
    def ask_coordination(self, title, description, priority='medium', target_agents=None):
        """Ask other agents for coordination/input"""
        try:
            result = supabase.table('agent_coordination').insert({
                'coordination_type': 'question',
                'priority': priority,
                'title': title,
                'description': description,
                'initiating_agent_id': self.agent_id,
                'target_agents': target_agents,
                'status': 'open',
                'metadata': {'agent_name': self.agent_name}
            }).execute()
            
            coord_id = result.data[0]['id'] if result.data else None
            self.log_progress('question', f'Asked coordination: {title}', 'info')
            print(f"✅ Posted coordination question: {title}")
            return coord_id
        except Exception as e:
            print(f"❌ Failed to post coordination: {e}")
            return None
    
    def respond_to_coordination(self, coordination_id, response_text, response_type='comment'):
        """Respond to a coordination item"""
        try:
            supabase.table('agent_responses').insert({
                'coordination_id': coordination_id,
                'agent_id': self.agent_id,
                'agent_name': self.agent_name,
                'response_text': response_text,
                'response_type': response_type
            }).execute()
            
            print(f"✅ Responded to coordination {coordination_id}")
            return True
        except Exception as e:
            print(f"❌ Failed to respond: {e}")
            return False
    
    def get_open_coordination(self):
        """Get open coordination items"""
        try:
            result = supabase.table('agent_coordination').select('*').eq('status', 'open').order('priority', desc=False).order('created_at', desc=True).execute()
            return result.data
        except Exception as e:
            print(f"❌ Failed to get coordination: {e}")
            return []
    
    def get_recent_activity(self, limit=20):
        """Get recent activity from all agents"""
        try:
            result = supabase.table('progress_events').select('*').order('created_at', desc=True).limit(limit).execute()
            return result.data
        except Exception as e:
            print(f"❌ Failed to get activity: {e}")
            return []
    
    def check_out(self):
        """Mark agent as offline"""
        try:
            supabase.table('agent_activity').update({
                'status': 'offline',
                'updated_at': datetime.now().isoformat()
            }).eq('agent_id', self.agent_id).execute()
            
            self.log_progress('complete', f'Agent {self.agent_name} signing off', 'info')
            print(f"✅ {self.agent_name} checked out")
            return True
        except Exception as e:
            print(f"❌ Check-out failed: {e}")
            return False


# ============================================
# COMMAND LINE INTERFACE
# ============================================

def cmd_status():
    """Show current agent activity and coordination status"""
    print("🔍 Current Agent Status\n")
    
    try:
        # Active agents
        agents = supabase.table('agent_activity').select('*').eq('status', 'active').execute()
        print(f"👥 Active Agents: {len(agents.data)}")
        for agent in agents.data:
            task = agent.get('current_task', 'No task')
            print(f"  • {agent['agent_name']} ({agent['agent_id']}): {task}")
        
        print()
        
        # Open coordination
        coordination = supabase.table('agent_coordination').select('*').eq('status', 'open').execute()
        print(f"🤝 Open Coordination Items: {len(coordination.data)}")
        for item in coordination.data[:5]:
            print(f"  • [{item['priority'].upper()}] {item['title']}")
            print(f"    By: {item['initiating_agent_id']}")
        
        print()
        
        # Pending tasks
        tasks = supabase.table('task_queue').select('*').in_('status', ['pending', 'assigned']).execute()
        print(f"📋 Pending/Assigned Tasks: {len(tasks.data)}")
        for task in tasks.data[:5]:
            assigned = task.get('assigned_to', 'unassigned')
            print(f"  • [{task['priority'].upper()}] {task['task_name']}")
            print(f"    Status: {task['status']} | Assigned: {assigned}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

def cmd_tasks():
    """List all available tasks"""
    print("📋 Available Tasks\n")
    
    try:
        tasks = supabase.table('task_queue').select('*').order('priority', desc=False).execute()
        
        for task in tasks.data:
            status_icon = {'pending': '⏳', 'assigned': '👷', 'in_progress': '🔄', 'completed': '✅', 'blocked': '🚫'}
            icon = status_icon.get(task['status'], '❓')
            
            print(f"{icon} [{task['priority'].upper()}] {task['task_name']}")
            print(f"   Status: {task['status']}")
            if task.get('assigned_to'):
                print(f"   Assigned to: {task['assigned_to']}")
            print(f"   Description: {task['task_description'][:100]}...")
            print()
    
    except Exception as e:
        print(f"❌ Error: {e}")

def cmd_activity(limit=10):
    """Show recent activity"""
    print(f"📊 Recent Activity (last {limit} events)\n")
    
    try:
        events = supabase.table('progress_events').select('*').order('created_at', desc=True).limit(limit).execute()
        
        for event in events.data:
            severity_icon = {'critical': '🔴', 'error': '❌', 'warning': '⚠️', 'info': 'ℹ️', 'success': '✅'}
            icon = severity_icon.get(event['severity'], 'ℹ️')
            
            timestamp = event['created_at'][:19]  # Just date and time
            print(f"{icon} [{timestamp}] {event['agent_id']}: {event['message']}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

def cmd_coordination():
    """Show open coordination items"""
    print("🤝 Open Coordination Items\n")
    
    try:
        items = supabase.table('agent_coordination').select('*').eq('status', 'open').order('priority', desc=False).execute()
        
        for item in items.data:
            print(f"[{item['priority'].upper()}] {item['title']}")
            print(f"  Type: {item['coordination_type']}")
            print(f"  By: {item['initiating_agent_id']}")
            print(f"  Description: {item['description'][:150]}...")
            print(f"  ID: {item['id']}")
            print()
    
    except Exception as e:
        print(f"❌ Error: {e}")

def cmd_help():
    """Show help"""
    print("""
🤝 Multi-Agent GraphRAG Coordinator

Usage: python3 agent_graphrag_coordinator.py [command]

Commands:
  status       Show current agent activity and system status
  tasks        List all available tasks
  activity     Show recent activity from all agents
  coordination Show open coordination items
  help         Show this help

Examples:
  python3 agent_graphrag_coordinator.py status
  python3 agent_graphrag_coordinator.py tasks
  python3 agent_graphrag_coordinator.py activity
  python3 agent_graphrag_coordinator.py coordination

Python API Usage:
  from agent_graphrag_coordinator import AgentCoordinator
  
  agent = AgentCoordinator('agent-123', 'Agent 1')
  agent.check_in('Working on styling')
  agent.log_progress('update', 'Found CSS issue')
  agent.add_knowledge('CSS Loading Bug', 'CSS fails to load due to path issue')
  agent.check_out()
""")

def main():
    if len(sys.argv) < 2:
        cmd_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'status':
        cmd_status()
    elif command == 'tasks':
        cmd_tasks()
    elif command == 'activity':
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        cmd_activity(limit)
    elif command == 'coordination':
        cmd_coordination()
    elif command == 'help':
        cmd_help()
    else:
        print(f"Unknown command: {command}")
        cmd_help()

if __name__ == '__main__':
    main()


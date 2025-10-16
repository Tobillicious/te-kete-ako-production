#!/usr/bin/env python3
"""
AGENT COLLABORATION HUB
Prevents divergence through continuous coordination
MCP + GraphRAG + Real-time sync
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

try:
    from supabase_graphrag_connector import SupabaseGraphRAGConnector
except ImportError:
    print("⚠️  GraphRAG connector not found, limited functionality")
    SupabaseGraphRAGConnector = None

class AgentCollaborationHub:
    """
    Prevents agent divergence through mandatory coordination
    """
    
    def __init__(self):
        self.state_file = Path('AGENT_COLLABORATION_STATE.json')
        self.coordination_file = Path('ACTIVE_COORDINATION.md')
        self.active_agents = {}
        self.task_claims = {}
        
        # Initialize GraphRAG if available
        if SupabaseGraphRAGConnector:
            try:
                self.graphrag = SupabaseGraphRAGConnector()
                print("✅ GraphRAG connected")
            except:
                self.graphrag = None
                print("⚠️  GraphRAG connection failed")
        else:
            self.graphrag = None
        
        # Load existing state
        self.load_state()
    
    def register_agent(self, agent_id, capabilities):
        """Register agent with collaboration hub"""
        self.active_agents[agent_id] = {
            'capabilities': capabilities,
            'current_task': None,
            'last_check_in': datetime.now().isoformat(),
            'status': 'idle',
            'tasks_completed': 0
        }
        self.save_state()
        
        print(f"✅ {agent_id} registered with hub")
        print(f"   Capabilities: {', '.join(capabilities)}")
        
        # Update coordination doc
        self.update_coordination_doc()
        
        return True
    
    def claim_task(self, agent_id, task_description, task_files=[]):
        """
        Agent claims a task - PREVENTS CONFLICTS!
        Returns: {'approved': bool, 'conflicts': [agent_ids]}
        """
        print(f"\n🎯 {agent_id} wants to claim: {task_description}")
        
        # Check for conflicts with other active agents
        conflicts = []
        for other_id, other_data in self.active_agents.items():
            if other_id != agent_id and other_data['current_task']:
                # Check for file conflicts
                if task_files:
                    other_task = self.task_claims.get(other_id, {})
                    other_files = other_task.get('files', [])
                    overlap = set(task_files) & set(other_files)
                    if overlap:
                        conflicts.append({
                            'agent': other_id,
                            'reason': f'File conflict: {overlap}',
                            'task': other_data['current_task']
                        })
                
                # Check for topic overlap
                if self.tasks_overlap(task_description, other_data['current_task']):
                    conflicts.append({
                        'agent': other_id,
                        'reason': 'Topic overlap',
                        'task': other_data['current_task']
                    })
        
        if conflicts:
            print(f"⚠️  CONFLICTS DETECTED with {len(conflicts)} agent(s):")
            for conflict in conflicts:
                print(f"   - {conflict['agent']}: {conflict['reason']}")
                print(f"     Their task: {conflict['task']}")
            print(f"\n🤝 MUST coordinate before proceeding!")
            return {'approved': False, 'conflicts': conflicts}
        
        # No conflicts - approve task claim
        self.active_agents[agent_id]['current_task'] = task_description
        self.active_agents[agent_id]['status'] = 'working'
        self.active_agents[agent_id]['task_started'] = datetime.now().isoformat()
        
        self.task_claims[agent_id] = {
            'description': task_description,
            'files': task_files,
            'started': datetime.now().isoformat()
        }
        
        self.save_state()
        self.update_coordination_doc()
        
        print(f"✅ APPROVED: {agent_id} can proceed with task")
        return {'approved': True, 'conflicts': []}
    
    def check_in(self, agent_id, progress_update):
        """Agent reports progress - MANDATORY every 30 mins"""
        if agent_id not in self.active_agents:
            print(f"⚠️  {agent_id} not registered! Register first.")
            return False
        
        self.active_agents[agent_id]['last_check_in'] = datetime.now().isoformat()
        self.active_agents[agent_id]['latest_progress'] = progress_update
        
        self.save_state()
        
        # Log to GraphRAG if available
        if self.graphrag:
            try:
                # GraphRAG logging would go here
                pass
            except:
                pass
        
        print(f"✅ {agent_id} checked in: {progress_update[:60]}...")
        
        # Update coordination doc
        self.update_coordination_doc()
        
        return True
    
    def complete_task(self, agent_id, completion_summary):
        """Agent completes task"""
        if agent_id not in self.active_agents:
            return False
        
        # Log completion
        self.active_agents[agent_id]['current_task'] = None
        self.active_agents[agent_id]['status'] = 'idle'
        self.active_agents[agent_id]['tasks_completed'] += 1
        self.active_agents[agent_id]['last_completion'] = {
            'summary': completion_summary,
            'time': datetime.now().isoformat()
        }
        
        # Clear task claim
        if agent_id in self.task_claims:
            del self.task_claims[agent_id]
        
        self.save_state()
        self.update_coordination_doc()
        
        print(f"🎉 {agent_id} completed task!")
        print(f"   Summary: {completion_summary[:80]}...")
        
        # Broadcast to team
        self.broadcast_completion(agent_id, completion_summary)
        
        return True
    
    def coordinator_check(self, coordinator_id='agent-4'):
        """Coordinator runs this every 30 minutes"""
        print(f"\n{'='*70}")
        print(f"🔄 COORDINATOR CHECK - {datetime.now().strftime('%H:%M:%S')}")
        print(f"{'='*70}")
        
        total = len(self.active_agents)
        working = sum(1 for a in self.active_agents.values() if a['status'] == 'working')
        idle = total - working
        
        print(f"\n📊 TEAM STATUS: {working} working | {idle} idle | {total} total\n")
        
        # Check each agent
        issues = []
        for agent_id, data in self.active_agents.items():
            last_check = datetime.fromisoformat(data['last_check_in'])
            minutes_since = (datetime.now() - last_check).seconds / 60
            
            status_emoji = "✅" if minutes_since < 30 else "⚠️"
            task_display = data['current_task'][:50] if data['current_task'] else 'idle'
            
            print(f"{status_emoji} {agent_id:15} {data['status']:10} {task_display}")
            
            if minutes_since > 30 and data['status'] == 'working':
                issues.append(f"{agent_id} - No check-in for {minutes_since:.0f} mins")
                print(f"   ⚠️  MISSING CHECK-IN for {minutes_since:.0f} minutes!")
        
        if issues:
            print(f"\n🚨 ISSUES DETECTED:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print(f"\n✅ All agents responding normally")
        
        # Update coordination doc
        self.update_coordination_doc()
        
        print(f"\n{'='*70}\n")
        
        return issues
    
    def tasks_overlap(self, task1, task2):
        """Check if two task descriptions overlap"""
        if not task1 or not task2:
            return False
        
        task1_words = set(task1.lower().split())
        task2_words = set(task2.lower().split())
        
        # Remove common words
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
        task1_words -= common_words
        task2_words -= common_words
        
        # Check overlap
        overlap = task1_words & task2_words
        
        # If more than 30% overlap, consider it a conflict
        if len(overlap) > 0:
            overlap_pct = len(overlap) / max(len(task1_words), len(task2_words))
            return overlap_pct > 0.3
        
        return False
    
    def get_team_status(self):
        """Get current status of all agents"""
        return {
            'total_agents': len(self.active_agents),
            'working': sum(1 for a in self.active_agents.values() if a['status'] == 'working'),
            'idle': sum(1 for a in self.active_agents.values() if a['status'] == 'idle'),
            'agents': self.active_agents,
            'last_updated': datetime.now().isoformat()
        }
    
    def update_coordination_doc(self):
        """Update ACTIVE_COORDINATION.md with current team status"""
        status = self.get_team_status()
        
        content = f"""# 🤝 ACTIVE COORDINATION - LIVE STATUS

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC  
**Coordinator:** agent-4 (Kaitiaki Tūhono)  
**Team Status:** {status['working']} working | {status['idle']} idle | {status['total_agents']} total

---

## 🔄 CURRENT AGENT ACTIVITIES

"""
        
        for agent_id, data in sorted(self.active_agents.items()):
            status_emoji = "🟢" if data['status'] == 'working' else "⚪"
            content += f"### {status_emoji} {agent_id}\n"
            content += f"**Status:** {data['status']}\n"
            content += f"**Current Task:** {data['current_task'] or 'None'}\n"
            content += f"**Last Check-In:** {data['last_check_in']}\n"
            content += f"**Tasks Completed:** {data['tasks_completed']}\n\n"
        
        content += """
---

## 📋 HOW TO USE THIS SYSTEM

**Before Starting Task:**
```python
python3 scripts/agent-collaboration-hub.py claim <agent-id> "<task description>"
```

**Every 30 Minutes:**
```python
python3 scripts/agent-collaboration-hub.py checkin <agent-id> "<progress update>"
```

**When Task Complete:**
```python
python3 scripts/agent-collaboration-hub.py complete <agent-id> "<completion summary>"
```

---

**This file is AUTO-UPDATED by the coordination hub!**
"""
        
        with open(self.coordination_file, 'w') as f:
            f.write(content)
    
    def broadcast_completion(self, agent_id, summary):
        """Broadcast completion to all agents"""
        print(f"\n📢 BROADCASTING to all agents:")
        print(f"   {agent_id} completed: {summary[:60]}...")
    
    def save_state(self):
        """Save current state"""
        with open(self.state_file, 'w') as f:
            json.dump({
                'agents': self.active_agents,
                'tasks': self.task_claims,
                'last_updated': datetime.now().isoformat()
            }, f, indent=2)
    
    def load_state(self):
        """Load existing state"""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r') as f:
                    data = json.load(f)
                    self.active_agents = data.get('agents', {})
                    self.task_claims = data.get('tasks', {})
                    print(f"✅ Loaded state: {len(self.active_agents)} agents")
            except:
                pass

# CLI Interface
def main():
    hub = AgentCollaborationHub()
    
    if len(sys.argv) < 2:
        print("AGENT COLLABORATION HUB")
        print("=" * 50)
        print("\nUsage:")
        print("  register   <agent-id> <capability1,capability2,...>")
        print("  claim      <agent-id> <task description>")
        print("  checkin    <agent-id> <progress update>")
        print("  complete   <agent-id> <completion summary>")
        print("  status     - Show all agent status")
        print("  coordinate - Run coordinator check (for coordinator agent)")
        return
    
    command = sys.argv[1]
    
    if command == 'register' and len(sys.argv) >= 4:
        agent_id = sys.argv[2]
        capabilities = sys.argv[3].split(',')
        hub.register_agent(agent_id, capabilities)
    
    elif command == 'claim' and len(sys.argv) >= 4:
        agent_id = sys.argv[2]
        task = ' '.join(sys.argv[3:])
        result = hub.claim_task(agent_id, task)
        
        if not result['approved']:
            print(f"\n🚨 TASK BLOCKED - Must coordinate first!")
            sys.exit(1)
    
    elif command == 'checkin' and len(sys.argv) >= 4:
        agent_id = sys.argv[2]
        progress = ' '.join(sys.argv[3:])
        hub.check_in(agent_id, progress)
    
    elif command == 'complete' and len(sys.argv) >= 4:
        agent_id = sys.argv[2]
        summary = ' '.join(sys.argv[3:])
        hub.complete_task(agent_id, summary)
    
    elif command == 'status':
        status = hub.get_team_status()
        print(f"\n📊 TEAM STATUS")
        print(f"="*50)
        print(f"Total Agents: {status['total_agents']}")
        print(f"Working: {status['working']}")
        print(f"Idle: {status['idle']}")
        print(f"\nAgents:")
        for agent_id, data in status['agents'].items():
            print(f"  {agent_id}: {data['status']} - {data['current_task'] or 'idle'}")
    
    elif command == 'coordinate':
        hub.coordinator_check()
    
    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()


#!/usr/bin/env python3
"""
UNIFIED AGENT COORDINATOR - PREVENT DIVERGENCE
Simple tool to enforce agent coordination via MCP & GraphRAG
Usage: python3 agent-coordinator.py [command] [args]
"""

import sys
import json
from datetime import datetime
from pathlib import Path

# Coordination state file
STATE_FILE = Path('/Users/admin/Documents/te-kete-ako-clean/.agent-coordination-state.json')

def load_state():
    """Load current coordination state"""
    if STATE_FILE.exists():
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {'agents': {}, 'tasks': {}, 'last_sync': None}

def save_state(state):
    """Save coordination state"""
    state['last_sync'] = datetime.now().isoformat()
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def check_in(agent_id):
    """Agent check-in"""
    state = load_state()
    
    print(f"\n🤝 AGENT {agent_id} CHECK-IN")
    print("=" * 70)
    
    # Show recent activity
    print(f"\n📊 RECENT AGENT ACTIVITY (Last 6 hours):\n")
    
    active_agents = {k: v for k, v in state['agents'].items() 
                     if v.get('status') == 'active'}
    
    if active_agents:
        for agent, info in active_agents.items():
            print(f"   🟢 {agent}: {info.get('current_task', 'Unknown')}")
            print(f"      Last update: {info.get('last_update', 'Unknown')}")
    else:
        print("   No other agents currently active")
    
    # Show claimed tasks
    print(f"\n📋 CLAIMED TASKS:\n")
    
    active_tasks = {k: v for k, v in state['tasks'].items() 
                   if v.get('status') == 'in-progress'}
    
    if active_tasks:
        for task, info in active_tasks.items():
            print(f"   🔒 {task}")
            print(f"      Owner: {info.get('owner', 'Unknown')}")
            print(f"      Started: {info.get('started', 'Unknown')}")
    else:
        print("   No tasks currently claimed")
    
    # Update state
    state['agents'][agent_id] = {
        'status': 'active',
        'last_update': datetime.now().isoformat(),
        'current_task': None
    }
    
    save_state(state)
    
    print(f"\n✅ {agent_id} checked in successfully!")
    print(f"\n💡 Next: Claim a task with: --claim \"Task description\"")
    print("=" * 70 + "\n")

def claim_task(agent_id, task_description):
    """Claim a task"""
    state = load_state()
    
    # Check for conflicts
    for task_id, task_info in state['tasks'].items():
        if task_info.get('status') == 'in-progress':
            # Simple conflict detection (keyword match)
            if any(word in task_description.lower() for word in task_info.get('description', '').lower().split()[:5]):
                print(f"\n⚠️  POTENTIAL CONFLICT DETECTED!")
                print(f"   Task: {task_id}")
                print(f"   Owner: {task_info.get('owner')}")
                print(f"   Description: {task_info.get('description')}")
                print(f"\n   Coordinate with {task_info.get('owner')} before proceeding!\n")
                return
    
    # Claim task
    task_id = f"{agent_id}-{datetime.now().strftime('%Y%m%d-%H%M')}"
    
    state['tasks'][task_id] = {
        'description': task_description,
        'owner': agent_id,
        'status': 'in-progress',
        'started': datetime.now().isoformat(),
        'updates': []
    }
    
    state['agents'][agent_id]['current_task'] = task_id
    
    save_state(state)
    
    print(f"\n✅ TASK CLAIMED: {task_id}")
    print(f"   Agent: {agent_id}")
    print(f"   Description: {task_description}")
    print(f"\n💡 Update progress every 30 mins with: --update \"What I did\"")
    print("=" * 70 + "\n")

def update_progress(agent_id, progress_description):
    """Update task progress"""
    state = load_state()
    
    # Find agent's current task
    current_task_id = state['agents'].get(agent_id, {}).get('current_task')
    
    if not current_task_id:
        print(f"\n⚠️  No active task for {agent_id}!")
        print(f"   Claim a task first with: --claim \"Task description\"\n")
        return
    
    # Update task
    if current_task_id in state['tasks']:
        state['tasks'][current_task_id]['updates'].append({
            'timestamp': datetime.now().isoformat(),
            'progress': progress_description
        })
        state['tasks'][current_task_id]['last_update'] = datetime.now().isoformat()
    
    # Update agent
    state['agents'][agent_id]['last_update'] = datetime.now().isoformat()
    
    save_state(state)
    
    print(f"\n✅ PROGRESS UPDATED")
    print(f"   Task: {current_task_id}")
    print(f"   Progress: {progress_description}")
    print(f"\n💡 Continue working, update again in 30 mins!")
    print("=" * 70 + "\n")

def complete_task(agent_id):
    """Mark task as complete"""
    state = load_state()
    
    current_task_id = state['agents'].get(agent_id, {}).get('current_task')
    
    if current_task_id and current_task_id in state['tasks']:
        state['tasks'][current_task_id]['status'] = 'completed'
        state['tasks'][current_task_id]['completed'] = datetime.now().isoformat()
        state['agents'][agent_id]['current_task'] = None
        
        save_state(state)
        
        print(f"\n🎉 TASK COMPLETED: {current_task_id}")
        print(f"\n💡 Next: Check in for new task or sign off")
        print("=" * 70 + "\n")
    else:
        print(f"\n⚠️  No active task to complete for {agent_id}\n")

def check_conflicts():
    """Check for agent conflicts"""
    state = load_state()
    
    print(f"\n🔍 CONFLICT DETECTION")
    print("=" * 70)
    
    active_tasks = {k: v for k, v in state['tasks'].items() 
                   if v.get('status') == 'in-progress'}
    
    if not active_tasks:
        print(f"\n✅ No active tasks - no conflicts possible\n")
        return
    
    print(f"\n📋 ACTIVE TASKS ({len(active_tasks)}):\n")
    
    for task_id, task_info in active_tasks.items():
        print(f"   🔒 {task_id}")
        print(f"      Owner: {task_info.get('owner')}")
        print(f"      Task: {task_info.get('description')}")
        print(f"      Started: {task_info.get('started')}")
        print()
    
    # Simple conflict detection
    tasks_list = list(active_tasks.values())
    if len(tasks_list) > 1:
        print(f"⚠️  MULTIPLE AGENTS WORKING - Check for overlaps!")
        print(f"   Coordinate if working on related areas!\n")
    else:
        print(f"✅ Only one active task - low conflict risk\n")
    
    print("=" * 70 + "\n")

def show_status():
    """Show current coordination status"""
    state = load_state()
    
    print(f"\n📊 AGENT COORDINATION STATUS")
    print("=" * 70)
    
    print(f"\n👥 ACTIVE AGENTS:\n")
    active = {k: v for k, v in state['agents'].items() if v.get('status') == 'active'}
    
    if active:
        for agent, info in active.items():
            task = info.get('current_task', 'No task')
            print(f"   🟢 {agent}")
            print(f"      Task: {task}")
            print(f"      Last update: {info.get('last_update', 'Unknown')}")
    else:
        print("   No agents currently active")
    
    print(f"\n📋 ALL TASKS:\n")
    for task_id, task_info in state['tasks'].items():
        status_icon = "✅" if task_info['status'] == 'completed' else "🔄"
        print(f"   {status_icon} {task_id}")
        print(f"      {task_info.get('description', 'No description')}")
        print(f"      Owner: {task_info.get('owner')}")
        print(f"      Status: {task_info['status']}")
    
    print(f"\n🕐 Last Sync: {state.get('last_sync', 'Never')}")
    print("=" * 70 + "\n")

def main():
    if len(sys.argv) < 2:
        print("""
🤖 UNIFIED AGENT COORDINATOR - USAGE:

MANDATORY COMMANDS:
  --check-in AGENT_ID              Check in before starting work
  --claim AGENT_ID "Task desc"     Claim a task
  --update AGENT_ID "Progress"     Update progress (every 30 mins!)
  --complete AGENT_ID              Mark task complete

HELPFUL COMMANDS:
  --status                         Show all agent status
  --conflicts                      Check for conflicts
  
EXAMPLE WORKFLOW:
  1. python3 agent-coordinator.py --check-in agent-9
  2. python3 agent-coordinator.py --claim agent-9 "Fix broken links"
  3. (Work for 30 mins)
  4. python3 agent-coordinator.py --update agent-9 "Fixed 100 CSS links"
  5. (Work for 30 mins)
  6. python3 agent-coordinator.py --update agent-9 "Fixed 200 more links"
  7. python3 agent-coordinator.py --complete agent-9

REMEMBER: This prevents divergence! Use it EVERY session!
        """)
        return
    
    command = sys.argv[1]
    
    if command == '--check-in' and len(sys.argv) >= 3:
        check_in(sys.argv[2])
    elif command == '--claim' and len(sys.argv) >= 4:
        claim_task(sys.argv[2], sys.argv[3])
    elif command == '--update' and len(sys.argv) >= 4:
        update_progress(sys.argv[2], sys.argv[3])
    elif command == '--complete' and len(sys.argv) >= 3:
        complete_task(sys.argv[2])
    elif command == '--status':
        show_status()
    elif command == '--conflicts':
        check_conflicts()
    else:
        print("❌ Invalid command. Run without args for help.")

if __name__ == '__main__':
    main()


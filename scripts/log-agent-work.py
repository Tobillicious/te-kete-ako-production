#!/usr/bin/env python3
"""
Log Agent Work to MCP GraphRAG
MANDATORY: Use this to claim tasks and update progress
"""

import sys
import json
from datetime import datetime
from supabase import create_client, Client

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def claim_task(agent_name, task_description):
    """Claim a new task"""
    print(f"📝 Claiming task for {agent_name}...")
    
    response = supabase.table('agent_coordination').insert({
        'agent_name': agent_name,
        'task_claimed': task_description,
        'status': 'planning',
        'files_modified': [],
        'key_decisions': {}
    }).execute()
    
    print(f"✅ Task claimed! ID: {response.data[0]['id']}")
    print(f"   Remember to update progress every 30 mins!")
    return response.data[0]['id']

def update_progress(agent_name, files=None, decisions=None, status='in_progress'):
    """Update work progress"""
    print(f"🔄 Updating progress for {agent_name}...")
    
    update_data = {
        'status': status,
        'updated_at': datetime.now().isoformat()
    }
    
    if files:
        update_data['files_modified'] = files
    
    if decisions:
        update_data['key_decisions'] = decisions
    
    response = supabase.table('agent_coordination')\
        .update(update_data)\
        .eq('agent_name', agent_name)\
        .in_('status', ['planning', 'in_progress'])\
        .execute()
    
    print(f"✅ Progress updated!")
    if files:
        print(f"   Files modified: {len(files)}")
    return response

def mark_complete(agent_name, files, decisions, handoff=None):
    """Mark task complete"""
    print(f"🎉 Marking complete for {agent_name}...")
    
    update_data = {
        'status': 'completed',
        'completed_at': datetime.now().isoformat(),
        'files_modified': files,
        'key_decisions': decisions,
        'updated_at': datetime.now().isoformat()
    }
    
    if handoff:
        update_data['next_agent_handoff'] = handoff
    
    response = supabase.table('agent_coordination')\
        .update(update_data)\
        .eq('agent_name', agent_name)\
        .eq('status', 'in_progress')\
        .execute()
    
    print(f"✅ Task marked complete!")
    if handoff:
        print(f"   Handoff: {handoff}")
    return response

def show_menu():
    """Interactive menu"""
    print("\n" + "=" * 70)
    print("AGENT COORDINATION - WHAT DO YOU WANT TO DO?")
    print("=" * 70)
    print()
    print("1. Check what other agents are doing")
    print("2. Claim a new task")
    print("3. Update my progress")
    print("4. Mark my task complete")
    print("5. Exit")
    print()
    choice = input("Choice (1-5): ").strip()
    return choice

def main():
    """Main interactive loop"""
    
    if len(sys.argv) > 1:
        agent_name = sys.argv[1]
    else:
        agent_name = input("Enter your agent name (e.g., Agent-4, Kaitiaki-Aronui): ").strip()
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            # Check coordination
            os.system('python3 scripts/agent-coordination-check.py')
        
        elif choice == '2':
            # Claim task
            task = input("Task description: ").strip()
            claim_task(agent_name, task)
        
        elif choice == '3':
            # Update progress
            files_input = input("Files modified (comma-separated, or press Enter): ").strip()
            files = [f.strip() for f in files_input.split(',')] if files_input else None
            
            decisions_input = input("Key decisions (JSON, or press Enter): ").strip()
            decisions = json.loads(decisions_input) if decisions_input else None
            
            update_progress(agent_name, files, decisions)
        
        elif choice == '4':
            # Mark complete
            files_input = input("All files modified (comma-separated): ").strip()
            files = [f.strip() for f in files_input.split(',')]
            
            decisions_input = input("Key decisions (JSON): ").strip()
            decisions = json.loads(decisions_input) if decisions_input else {}
            
            handoff = input("Handoff to next agent (or press Enter): ").strip()
            handoff = handoff if handoff else None
            
            mark_complete(agent_name, files, decisions, handoff)
        
        elif choice == '5':
            print("\n👋 Goodbye! Remember to coordinate!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()


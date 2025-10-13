#!/usr/bin/env python3
"""
Enhanced Progress Tracking System for Te Kete Ako
Monitors agent tasks, provides status updates, and identifies blockers
"""

import json
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class ProgressTracker:
    def __init__(self):
        self.progress_file = "agent-progress-tracking.json"
        self.log_file = "progress-log.md"
        self.current_work_plan = "current-work-plan.json"
        
    def load_progress_data(self) -> Dict:
        """Load existing progress data or create new structure"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        
        # Default structure
        return {
            "last_updated": datetime.now().isoformat(),
            "agents": {},
            "tasks": {},
            "milestones": {
                "phase_1": {
                    "name": "Phase 1: Immediate Integration",
                    "target_date": (datetime.now() + timedelta(days=7)).isoformat(),
                    "status": "completed",
                    "completion_date": datetime.now().isoformat()
                },
                "phase_2": {
                    "name": "Phase 2: Priority Integration",
                    "target_date": (datetime.now() + timedelta(days=21)).isoformat(),
                    "status": "in_progress",
                    "completion_date": None
                },
                "phase_3": {
                    "name": "Phase 3: Standard Integration",
                    "target_date": (datetime.now() + timedelta(days=42)).isoformat(),
                    "status": "pending",
                    "completion_date": None
                },
                "phase_4": {
                    "name": "Phase 4: Bulk Integration",
                    "target_date": (datetime.now() + timedelta(days=70)).isoformat(),
                    "status": "pending",
                    "completion_date": None
                }
            }
        }
    
    def load_work_plan(self) -> Dict:
        """Load the current work plan"""
        if os.path.exists(self.current_work_plan):
            with open(self.current_work_plan, 'r') as f:
                return json.load(f)
        return {"assignments": []}
    
    def update_agent_status(self, agent_id: str, task_id: int, status: str, notes: str = ""):
        """Update an agent's status on a specific task"""
        progress_data = self.load_progress_data()
        work_plan = self.load_work_plan()
        
        # Initialize agent if not exists
        if agent_id not in progress_data["agents"]:
            progress_data["agents"][agent_id] = {
                "name": f"Agent-{agent_id.split('-')[1]}",
                "last_checkin": None,
                "current_tasks": {},
                "completed_tasks": [],
                "total_completed": 0
            }
        
        # Get task details from work plan
        task_details = {}
        for assignment in work_plan.get("assignments", []):
            if assignment.get("issue", {}).get("description") and assignment.get("status") != "completed":
                # This is a simplified approach - in a real system we'd match by task_id
                task_details = {
                    "description": assignment.get("issue", {}).get("description", "Unknown task"),
                    "type": assignment.get("issue", {}).get("type", "unknown"),
                    "priority": assignment.get("issue", {}).get("priority", "medium")
                }
                break
        
        # Update agent status
        agent_data = progress_data["agents"][agent_id]
        agent_data["last_checkin"] = datetime.now().isoformat()
        
        if status == "completed":
            if task_id not in agent_data["completed_tasks"]:
                agent_data["completed_tasks"].append(task_id)
                agent_data["total_completed"] += 1
            
            # Remove from current tasks if present
            if task_id in agent_data["current_tasks"]:
                del agent_data["current_tasks"][task_id]
        else:
            agent_data["current_tasks"][task_id] = {
                "status": status,
                "notes": notes,
                "updated": datetime.now().isoformat(),
                **task_details
            }
        
        # Save updated progress
        progress_data["last_updated"] = datetime.now().isoformat()
        with open(self.progress_file, 'w') as f:
            json.dump(progress_data, f, indent=2)
        
        # Also update the markdown log
        self.update_markdown_log(agent_id, task_details.get("description", "Unknown task"), status, notes)
        
        return True
    
    def update_markdown_log(self, agent_id: str, task_name: str, status: str, notes: str = ""):
        """Update the markdown progress log"""
        timestamp = datetime.now().strftime("%H:%M")
        status_emoji = {
            "in_progress": "🔄",
            "completed": "✅",
            "blocked": "🚫",
            "pending": "⏳"
        }.get(status, "📝")
        
        log_entry = f"[{timestamp}] {agent_id}: {status_emoji} {task_name} - {notes}"
        
        with open(self.log_file, 'a') as f:
            f.write(f"{log_entry}\n")
    
    def generate_status_report(self) -> str:
        """Generate a comprehensive status report"""
        progress_data = self.load_progress_data()
        work_plan = self.load_work_plan()
        
        report = f"""# Te Kete Ako Progress Status Report
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Mission Overview
Transforming Te Kete Ako into New Zealand's most comprehensive educational platform with 6,699+ teaching resources.

## Phase Progress
"""
        
        for phase_id, phase_data in progress_data["milestones"].items():
            status_emoji = {
                "completed": "✅",
                "in_progress": "🔄",
                "pending": "⏳"
            }.get(phase_data["status"], "❓")
            
            report += f"### {phase_data['name']} {status_emoji}\n"
            report += f"- **Status:** {phase_data['status'].title()}\n"
            report += f"- **Target Date:** {phase_data['target_date'][:10]}\n"
            
            if phase_data["completion_date"]:
                report += f"- **Completed:** {phase_data['completion_date'][:10]}\n"
            
            report += "\n"
        
        report += "## Agent Status\n\n"
        
        for agent_id, agent_data in progress_data["agents"].items():
            last_checkin = agent_data.get("last_checkin", "Never")
            if last_checkin != "Never":
                last_checkin = datetime.fromisoformat(last_checkin).strftime("%Y-%m-%d %H:%M")
            
            report += f"### {agent_data['name']}\n"
            report += f"- **Last Check-in:** {last_checkin}\n"
            report += f"- **Tasks Completed:** {agent_data['total_completed']}\n"
            report += f"- **Current Tasks:** {len(agent_data['current_tasks'])}\n"
            
            if agent_data["current_tasks"]:
                report += "- **Active Work:**\n"
                for task_id, task_data in agent_data["current_tasks"].items():
                    report += f"  - {task_data.get('description', 'Unknown task')} ({task_data['status']})\n"
            
            report += "\n"
        
        # Calculate overall progress
        total_tasks = len(work_plan.get("assignments", []))
        completed_tasks = sum(1 for a in work_plan.get("assignments", []) if a.get("status") == "completed")
        
        if total_tasks > 0:
            progress_percent = (completed_tasks / total_tasks) * 100
            report += f"## Overall Progress\n\n"
            report += f"- **Tasks Completed:** {completed_tasks}/{total_tasks} ({progress_percent:.1f}%)\n"
            report += f"- **Active Agents:** {len(progress_data['agents'])}\n"
            report += f"- **Content Integrated:** 1,113+ files\n"
        
        report += "\n---\n"
        report += "*Every task brings us closer to our goal of creating New Zealand's most comprehensive educational platform.*"
        
        return report
    
    def check_for_blockers(self) -> List[Dict]:
        """Identify potential blockers in the workflow"""
        progress_data = self.load_progress_data()
        blockers = []
        
        # Check for agents who haven't checked in recently
        now = datetime.now()
        for agent_id, agent_data in progress_data["agents"].items():
            last_checkin = agent_data.get("last_checkin")
            if last_checkin:
                last_checkin_time = datetime.fromisoformat(last_checkin)
                if now - last_checkin_time > timedelta(days=1):
                    blockers.append({
                        "type": "agent_inactive",
                        "agent": agent_id,
                        "message": f"{agent_data['name']} hasn't checked in for over 24 hours",
                        "severity": "medium"
                    })
        
        # Check for tasks stuck in same status too long
        for agent_id, agent_data in progress_data["agents"].items():
            for task_id, task_data in agent_data.get("current_tasks", {}).items():
                updated = task_data.get("updated")
                if updated:
                    updated_time = datetime.fromisoformat(updated)
                    if now - updated_time > timedelta(days=3):
                        blockers.append({
                            "type": "task_stalled",
                            "agent": agent_id,
                            "task": task_data.get("description", "Unknown task"),
                            "message": f"Task '{task_data.get('description')}' has been {task_data['status']} for over 3 days",
                            "severity": "high"
                        })
        
        return blockers
    
    def save_status_report(self):
        """Save the status report to a file"""
        report = self.generate_status_report()
        
        with open("progress-status-report.md", 'w') as f:
            f.write(report)
        
        print("✅ Status report saved to progress-status-report.md")
        
        # Check for blockers
        blockers = self.check_for_blockers()
        if blockers:
            print("\n⚠️  Blockers Identified:")
            for blocker in blockers:
                print(f"  - {blocker['message']} (Severity: {blocker['severity']})")
        
        return report

if __name__ == "__main__":
    tracker = ProgressTracker()
    
    if len(sys.argv) < 2:
        print("Usage: python progress-tracker.py <command>")
        print("Commands:")
        print("  report - Generate status report")
        print("  update <agent_id> <task_id> <status> [notes] - Update agent task status")
        print("  blockers - Check for workflow blockers")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "report":
        tracker.save_status_report()
        
    elif command == "update":
        if len(sys.argv) < 5:
            print("Usage: python progress-tracker.py update <agent_id> <task_id> <status> [notes]")
            sys.exit(1)
        
        agent_id = sys.argv[2]
        task_id = int(sys.argv[3])
        status = sys.argv[4]
        notes = sys.argv[5] if len(sys.argv) > 5 else ""
        
        tracker.update_agent_status(agent_id, task_id, status, notes)
        print(f"✅ Updated {agent_id} task {task_id} status to {status}")
        
    elif command == "blockers":
        blockers = tracker.check_for_blockers()
        if blockers:
            print("Blockers identified:")
            for blocker in blockers:
                print(f"  - {blocker['message']} (Severity: {blocker['severity']})")
        else:
            print("No blockers identified.")
    
    else:
        print(f"Unknown command: {command}")

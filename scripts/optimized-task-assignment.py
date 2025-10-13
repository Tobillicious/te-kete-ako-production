#!/usr/bin/env python3
"""
Optimized Task Assignment System for Te Kete Ako
Streamlined for fewer agents with focus on high-impact tasks
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Tuple, Optional

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from supabase_graphrag_connector import SupabaseGraphRAGConnector
except ImportError:
    print("Error: Could not import SupabaseGraphRAGConnector")
    sys.exit(1)

class OptimizedTaskAssigner:
    def __init__(self):
        self.graphrag = SupabaseGraphRAGConnector()
        
        # Streamlined agent capabilities for fewer agents
        self.agent_capabilities = {
            "agent-2": ["styling", "css", "design-system", "accessibility"],
            "agent-4": ["navigation", "links", "structure", "orphaned-pages"],
            "agent-6": ["content", "cultural-enhancement", "integration", "resource-management"],
            "agent-7": ["cultural", "maori-knowledge", "authenticity", "validation"],
            "agent-10": ["coordination", "mcp", "communication", "documentation"],
            "agent-11": ["qa", "testing", "browser-testing", "performance"]
        }
        
        # High-impact task templates
        self.task_templates = {
            "css-fix": {
                "capabilities": ["styling", "css"],
                "priority": "critical",
                "impact": "high",
                "description": "Fix CSS styling issues",
                "agents": ["agent-2"],
                "estimated_time": "30 minutes"
            },
            "orphan-integration": {
                "capabilities": ["orphaned-pages", "navigation"],
                "priority": "critical",
                "impact": "high",
                "description": "Integrate orphaned pages into navigation",
                "agents": ["agent-4", "agent-6"],
                "estimated_time": "2 hours"
            },
            "content-enhancement": {
                "capabilities": ["content", "cultural-enhancement"],
                "priority": "high",
                "impact": "medium",
                "description": "Enhance content with cultural context",
                "agents": ["agent-6", "agent-7"],
                "estimated_time": "1 hour"
            },
            "cultural-validation": {
                "capabilities": ["cultural", "maori-knowledge"],
                "priority": "high",
                "impact": "high",
                "description": "Validate cultural authenticity of content",
                "agents": ["agent-7"],
                "estimated_time": "45 minutes"
            },
            "qa-testing": {
                "capabilities": ["qa", "testing", "browser-testing"],
                "priority": "medium",
                "impact": "medium",
                "description": "Test functionality and browser compatibility",
                "agents": ["agent-11"],
                "estimated_time": "1 hour"
            }
        }
    
    def detect_critical_issues(self) -> List[Dict]:
        """Detect only critical issues that need immediate attention"""
        issues = []
        
        # Check for missing CSS classes (we know this is critical)
        issues.append({
            "type": "css-fix",
            "description": "Missing hero-description and hero-actions CSS classes",
            "location": "public/css/te-kete-professional.css",
            "priority": "critical",
            "impact": "high",
            "capabilities": ["styling", "css"],
            "user_visible": True
        })
        
        # Check for orphaned pages (high impact)
        issues.append({
            "type": "orphan-integration",
            "description": "45+ orphaned pages in generated-resources-alpha directory",
            "location": "public/generated-resources-alpha/",
            "priority": "critical",
            "impact": "high",
            "capabilities": ["orphaned-pages", "navigation"],
            "user_visible": True
        })
        
        return issues
    
    def prioritize_by_impact(self, issues: List[Dict]) -> List[Dict]:
        """Prioritize tasks by user impact and agent efficiency"""
        # Sort by priority first, then by impact
        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        impact_order = {"high": 0, "medium": 1, "low": 2}
        
        def sort_key(issue):
            return (
                priority_order.get(issue.get("priority", "low"), 3),
                impact_order.get(issue.get("impact", "low"), 3),
                issue.get("user_visible", False)  # User-visible issues first
            )
        
        return sorted(issues, key=sort_key)
    
    def assign_optimally(self, issues: List[Dict]) -> List[Dict]:
        """Assign tasks to optimize agent efficiency and minimize conflicts"""
        assignments = []
        
        for issue in issues:
            # Find best-matching agent (first match for simplicity)
            best_agent = None
            for agent_id, capabilities in self.agent_capabilities.items():
                if any(cap in capabilities for cap in issue.get("capabilities", [])):
                    best_agent = agent_id
                    break
            
            # Create assignment
            assignment = {
                "issue": issue,
                "assigned_to": best_agent,
                "status": "assigned" if best_agent else "unassigned",
                "created_at": datetime.now().isoformat()
            }
            
            assignments.append(assignment)
        
        return assignments
    
    def generate_optimized_plan(self) -> Dict:
        """Generate an optimized work plan for fewer agents"""
        # Detect critical issues only
        issues = self.detect_critical_issues()
        
        # Prioritize by impact
        prioritized = self.prioritize_by_impact(issues)
        
        # Assign optimally
        assignments = self.assign_optimally(prioritized)
        
        # Create work plan
        work_plan = {
            "generated_at": datetime.now().isoformat(),
            "strategy": "optimized-for-fewer-agents",
            "total_issues": len(issues),
            "total_assignments": len(assignments),
            "assignments": assignments,
            "agent_focus": {
                agent_id: next((
                    a["issue"]["type"] for a in assignments 
                    if a["assigned_to"] == agent_id
                ), "idle") 
                for agent_id in self.agent_capabilities.keys()
            }
        }
        
        return work_plan
    
    def save_work_plan(self, work_plan: Dict, filename: str = "optimized-work-plan.json"):
        """Save optimized work plan to file"""
        with open(filename, 'w') as f:
            json.dump(work_plan, f, indent=2)
        print(f"Optimized work plan saved to {filename}")
    
    def get_next_task(self, agent_id: str) -> Optional[Dict]:
        """Get the next task for a specific agent"""
        try:
            with open("optimized-work-plan.json", 'r') as f:
                work_plan = json.load(f)
            
            for assignment in work_plan["assignments"]:
                if assignment["assigned_to"] == agent_id and assignment["status"] == "assigned":
                    return assignment
            
            return None
        except FileNotFoundError:
            print("No optimized work plan found. Run 'generate' first.")
            return None
    
    def complete_task(self, agent_id: str, task_type: str) -> bool:
        """Mark a task as completed by an agent"""
        try:
            with open("optimized-work-plan.json", 'r') as f:
                work_plan = json.load(f)
            
            for assignment in work_plan["assignments"]:
                if (assignment["assigned_to"] == agent_id and 
                    assignment["issue"]["type"] == task_type and 
                    assignment["status"] == "assigned"):
                    
                    assignment["status"] = "completed"
                    assignment["completed_at"] = datetime.now().isoformat()
                    
                    # Save updated work plan
                    with open("optimized-work-plan.json", 'w') as f:
                        json.dump(work_plan, f, indent=2)
                    
                    print(f"Task {task_type} marked as completed by {agent_id}")
                    return True
            
            print(f"No active task {task_type} found for {agent_id}")
            return False
        except Exception as e:
            print(f"Error completing task: {e}")
            return False

if __name__ == "__main__":
    assigner = OptimizedTaskAssigner()
    
    if len(sys.argv) < 2:
        print("Usage: python optimized-task-assignment.py <command>")
        print("Commands:")
        print("  generate - Generate optimized work plan")
        print("  next <agent_id> - Get next task for agent")
        print("  complete <agent_id> <task_type> - Mark task as complete")
        print("  status - Show current work plan status")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "generate":
        work_plan = assigner.generate_optimized_plan()
        assigner.save_work_plan(work_plan)
        print(f"Generated optimized work plan with {work_plan['total_assignments']} tasks")
        
        # Show agent focus
        print("\nAgent Focus:")
        for agent_id, focus in work_plan["agent_focus"].items():
            print(f"  {agent_id}: {focus}")
        
    elif command == "next":
        if len(sys.argv) < 3:
            print("Usage: python optimized-task-assignment.py next <agent_id>")
            sys.exit(1)
        
        agent_id = sys.argv[2]
        task = assigner.get_next_task(agent_id)
        
        if task:
            issue = task["issue"]
            print(f"Next task for {agent_id}:")
            print(f"  Type: {issue['type']}")
            print(f"  Description: {issue['description']}")
            print(f"  Location: {issue['location']}")
            print(f"  Priority: {issue['priority']}")
            print(f"  Impact: {issue['impact']}")
        else:
            print(f"No tasks available for {agent_id}")
        
    elif command == "complete":
        if len(sys.argv) < 4:
            print("Usage: python optimized-task-assignment.py complete <agent_id> <task_type>")
            sys.exit(1)
        
        agent_id = sys.argv[2]
        task_type = sys.argv[3]
        assigner.complete_task(agent_id, task_type)
        
    elif command == "status":
        try:
            with open("optimized-work-plan.json", 'r') as f:
                work_plan = json.load(f)
            
            print(f"Optimized Work Plan Status ({work_plan['generated_at']})")
            print(f"Strategy: {work_plan['strategy']}")
            print(f"Total tasks: {work_plan['total_assignments']}")
            
            print("\nAgent Focus:")
            for agent_id, focus in work_plan["agent_focus"].items():
                print(f"  {agent_id}: {focus}")
            
            print("\nTask Status:")
            for assignment in work_plan["assignments"]:
                issue = assignment["issue"]
                status = assignment["status"]
                assigned = assignment.get("assigned_to", "Unassigned")
                
                print(f"  [{status.upper()}] {issue['description']} (Assigned: {assigned})")
        except FileNotFoundError:
            print("No optimized work plan found. Run 'generate' first.")
    
    else:
        print(f"Unknown command: {command}")

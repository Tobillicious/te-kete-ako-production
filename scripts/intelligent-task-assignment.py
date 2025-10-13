#!/usr/bin/env python3
"""
Intelligent Task Assignment System for Te Kete Ako
Automatically identifies tasks, matches to agent capabilities, and prioritizes work
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

class IntelligentTaskAssigner:
    def __init__(self):
        self.graphrag = SupabaseGraphRAGConnector()
        self.work_plan_file = "current-work-plan.json"
        self.completed_tasks_file = "completed-tasks.json"
        
        # Load completed tasks if file exists
        self.completed_tasks = []
        if os.path.exists(self.completed_tasks_file):
            try:
                with open(self.completed_tasks_file, 'r') as f:
                    self.completed_tasks = json.load(f)
            except Exception as e:
                print(f"Error loading completed tasks: {e}")
        
        self.agent_capabilities = {
            "agent-1": ["file-discovery", "categorization", "inventory"],
            "agent-2": ["styling", "css", "design-system"],
            "agent-3": ["content", "cultural-enhancement", "education"],
            "agent-4": ["navigation", "links", "structure"],
            "agent-5": ["qa", "testing", "validation"],
            "agent-6": ["orphaned-pages", "integration", "resource-management"],
            "agent-7": ["cultural", "maori-knowledge", "authenticity"],
            "agent-8": ["performance", "optimization", "speed"],
            "agent-9": ["accessibility", "wcag", "testing"],
            "agent-10": ["coordination", "mcp", "communication"],
            "agent-11": ["browser-testing", "devtools", "diagnosis"],
            "agent-12": ["documentation", "progress-tracking", "knowledge-base"]
        }
        
        # Task templates with required capabilities
        self.task_templates = {
            "css-fix": {
                "capabilities": ["styling", "css"],
                "priority": "high",
                "description": "Fix CSS styling issues",
                "agents": ["agent-2"]
            },
            "orphan-integration": {
                "capabilities": ["orphaned-pages", "navigation"],
                "priority": "high",
                "description": "Integrate orphaned pages into navigation",
                "agents": ["agent-4", "agent-6"]
            },
            "content-enhancement": {
                "capabilities": ["content", "cultural-enhancement"],
                "priority": "medium",
                "description": "Enhance content with cultural context",
                "agents": ["agent-3", "agent-7"]
            },
            "navigation-fix": {
                "capabilities": ["navigation", "links"],
                "priority": "medium",
                "description": "Fix navigation issues",
                "agents": ["agent-4"]
            },
            "link-fix": {
                "capabilities": ["navigation", "links"],
                "priority": "high",
                "description": "Fix broken links",
                "agents": ["agent-4", "agent-6"]
            },
            "accessibility-fix": {
                "capabilities": ["accessibility", "wcag"],
                "priority": "medium",
                "description": "Fix accessibility issues",
                "agents": ["agent-9"]
            },
            "qa-testing": {
                "capabilities": ["qa", "testing", "browser-testing"],
                "priority": "medium",
                "description": "Test functionality and browser compatibility",
                "agents": ["agent-5", "agent-11"]
            },
            "performance-optimization": {
                "capabilities": ["performance", "optimization"],
                "priority": "low",
                "description": "Optimize site performance",
                "agents": ["agent-8"]
            },
            "auth-cleanup": {
                "capabilities": ["coordination", "mcp", "communication"],
                "priority": "high",
                "description": "Clean up authentication system conflicts",
                "agents": ["agent-10"]
            },
            "validation-pipeline": {
                "capabilities": ["qa", "testing", "validation"],
                "priority": "high",
                "description": "Create validation pipeline for unstaged changes",
                "agents": ["agent-5", "agent-11"]
            },
            "deployment-workflow": {
                "capabilities": ["coordination", "documentation", "knowledge-base"],
                "priority": "high",
                "description": "Create deployment workflow with testing",
                "agents": ["agent-10", "agent-12"]
            },
            "lesson-integration": {
                "capabilities": ["content", "integration", "resource-management"],
                "priority": "critical",
                "description": "Integrate 2,752 discovered lessons into the site",
                "agents": ["agent-6"]
            },
            "handout-integration": {
                "capabilities": ["orphaned-pages", "navigation", "integration"],
                "priority": "critical",
                "description": "Integrate 2,257 discovered handouts into the site",
                "agents": ["agent-4"]
            },
            "cultural-validation": {
                "capabilities": ["cultural", "maori-knowledge", "authenticity"],
                "priority": "high",
                "description": "Validate cultural authenticity of 1,223 high cultural value resources",
                "agents": ["agent-7"]
            },
            "quality-checks": {
                "capabilities": ["qa", "testing", "browser-testing"],
                "priority": "medium",
                "description": "Set up automated quality checks",
                "agents": ["agent-5", "agent-9", "agent-11"]
            },
            "lessons-integration": {
                "capabilities": ["orphaned-pages", "navigation"],
                "priority": "high",
                "description": "Integrate 2,750 high-quality lessons into site navigation",
                "agents": ["agent-6"]
            },
            "handouts-integration": {
                "capabilities": ["orphaned-pages", "navigation"],
                "priority": "high",
                "description": "Integrate 2,256 high-quality handouts into site navigation",
                "agents": ["agent-4"]
            },
            "cultural-content-integration": {
                "capabilities": ["content", "cultural-enhancement"],
                "priority": "high",
                "description": "Integrate 1,223 high cultural value resources",
                "agents": ["agent-7"]
            },
            "batch-lessons-integration": {
                "capabilities": ["orphaned-pages", "navigation", "resource-management"],
                "priority": "critical",
                "description": "Batch integrate 2,750 lessons into unit structures with proper navigation",
                "agents": ["agent-6", "agent-4"]
            },
            "batch-handouts-integration": {
                "capabilities": ["orphaned-pages", "navigation", "resource-management"],
                "priority": "critical",
                "description": "Batch integrate 2,256 handouts and connect to relevant lessons",
                "agents": ["agent-4", "agent-6"]
            },
            "content-navigation-system": {
                "capabilities": ["navigation", "links", "structure"],
                "priority": "critical",
                "description": "Create comprehensive navigation system for 5,793 content items",
                "agents": ["agent-4", "agent-10"]
            },
            "content-filtering-system": {
                "capabilities": ["content", "cultural-enhancement", "coordination"],
                "priority": "high",
                "description": "Implement filtering and search for content by subject, year level, and cultural relevance",
                "agents": ["agent-3", "agent-7", "agent-10"]
            }
        }
    
    def detect_issues(self) -> List[Dict]:
        """Scan the codebase to detect issues needing attention"""
        issues = []
        
        # Check for missing CSS classes
        css_issues = self._detect_css_issues()
        issues.extend(css_issues)
        
        # Check for orphaned pages
        orphan_issues = self._detect_orphaned_pages()
        issues.extend(orphan_issues)
        
        # Check for broken links
        link_issues = self._detect_broken_links()
        issues.extend(link_issues)
        
        # Check for accessibility issues
        a11y_issues = self._detect_accessibility_issues()
        issues.extend(a11y_issues)
        
        # Check for authentication conflicts
        auth_issues = self._detect_auth_conflicts()
        issues.extend(auth_issues)
        
        # Check for validation pipeline needs
        validation_issues = self._detect_validation_needs()
        issues.extend(validation_issues)
        
        # Check for content integration needs
        content_integration_issues = self._detect_content_integration_needs()
        issues.extend(content_integration_issues)
        
        return issues
    
    def _detect_css_issues(self) -> List[Dict]:
        """Detect CSS styling issues"""
        issues = []
        
        # Check for missing hero classes (we know this is an issue)
        issues.append({
            "type": "css-fix",
            "description": "Missing hero-description and hero-actions CSS classes",
            "location": "public/css/te-kete-professional.css",
            "priority": "high",
            "capabilities": ["styling", "css"]
        })
        
        return issues
    
    def _detect_orphaned_pages(self) -> List[Dict]:
        """Detect orphaned pages that need integration"""
        issues = []
        
        # We know there are 45+ orphaned pages in generated-resources-alpha
        issues.append({
            "type": "orphan-integration",
            "description": "45+ orphaned pages in generated-resources-alpha directory",
            "location": "public/generated-resources-alpha/",
            "priority": "high",
            "capabilities": ["orphaned-pages", "navigation"]
        })
        
        return issues
    
    def _detect_broken_links(self) -> List[Dict]:
        """Detect broken links"""
        issues = []
        
        # Check for broken navigation links
        issues.append({
            "type": "broken-links",
            "description": "Check for broken navigation links across the site",
            "location": "public/",
            "priority": "medium",
            "capabilities": ["navigation", "qa"]
        })
        
        return issues
    
    def _detect_auth_conflicts(self) -> List[Dict]:
        """Detect authentication system conflicts and role-based experience needs"""
        issues = []
        
        # Check for multiple authentication systems
        issues.append({
            "type": "auth-cleanup",
            "description": "Implement role-based authentication system (teacher vs student views)",
            "location": "authentication system",
            "priority": "high",
            "capabilities": ["coordination", "mcp", "communication"]
        })
        
        return issues
    
    def _detect_validation_needs(self) -> List[Dict]:
        """Detect validation pipeline and workflow needs"""
        issues = []
        
        # Check for validation pipeline
        issues.append({
            "type": "validation-pipeline",
            "description": "Create validation pipeline for unstaged changes",
            "location": "workflow system",
            "priority": "high",
            "capabilities": ["qa", "testing", "validation"]
        })
        
        # Check for deployment workflow
        issues.append({
            "type": "deployment-workflow",
            "description": "Create deployment workflow with testing",
            "location": "deployment system",
            "priority": "high",
            "capabilities": ["coordination", "documentation", "knowledge-base"]
        })
        
        # Check for quality checks
        issues.append({
            "type": "quality-checks",
            "description": "Set up automated quality checks",
            "location": "quality system",
            "priority": "medium",
            "capabilities": ["qa", "testing", "browser-testing"]
        })
        
        return issues
    
    def _detect_accessibility_issues(self) -> List[Dict]:
        """Detect accessibility issues"""
        issues = []
        
        # This would be implemented with actual accessibility checking
        # For now, return empty list
        return issues
    
    def _detect_performance_issues(self) -> List[Dict]:
        """Detect performance issues"""
        issues = []
        
        # Check for unoptimized images
        issues.append({
            "type": "performance-optimization",
            "description": "Optimize images for better loading performance",
            "location": "public/",
            "priority": "low",
            "capabilities": ["performance", "optimization"]
        })
        
        return issues
    
    def _detect_content_integration_needs(self) -> List[Dict]:
        """Detect content that needs integration"""
        issues = []
        
        # Check if content discovery results exist
        if os.path.exists("content-discovery-results.json"):
            with open("content-discovery-results.json", 'r') as f:
                discovery_results = json.load(f)
            
            # Add lesson integration task
            lessons_count = len([item for item in discovery_results if item.get("type") == "lessons"])
            if lessons_count > 0:
                issues.append({
                    "type": "lesson-integration",
                    "description": f"Integrate {lessons_count} discovered lessons into the site",
                    "location": "content-discovery-results.json",
                    "priority": "critical",
                    "capabilities": ["content", "integration", "resource-management"]
                })
            
            # Add handout integration task
            handouts_count = len([item for item in discovery_results if item.get("type") == "handouts"])
            if handouts_count > 0:
                issues.append({
                    "type": "handout-integration",
                    "description": f"Integrate {handouts_count} discovered handouts into the site",
                    "location": "content-discovery-results.json",
                    "priority": "critical",
                    "capabilities": ["orphaned-pages", "navigation", "integration"]
                })
            
            # Add cultural validation task
            high_cultural_count = len([item for item in discovery_results if item.get("cultural_level") == "high"])
            if high_cultural_count > 0:
                issues.append({
                    "type": "cultural-validation",
                    "description": f"Validate cultural authenticity of {high_cultural_count} high cultural value resources",
                    "location": "content-discovery-results.json",
                    "priority": "high",
                    "capabilities": ["cultural", "maori-knowledge", "authenticity"]
                })
        
        return issues
    
    def assign_tasks(self, issues: List[Dict]) -> List[Dict]:
        """Assign issues to appropriate agents"""
        assignments = []
        
        for issue in issues:
            # Find agents with required capabilities
            capable_agents = []
            for agent_id, capabilities in self.agent_capabilities.items():
                if any(cap in capabilities for cap in issue.get("capabilities", [])):
                    capable_agents.append(agent_id)
            
            # Create assignment
            assignment = {
                "issue": issue,
                "capable_agents": capable_agents,
                "assigned_to": None,
                "status": "unassigned",
                "created_at": datetime.now().isoformat()
            }
            
            assignments.append(assignment)
        
        return assignments
    
    def prioritize_tasks(self, assignments: List[Dict]) -> List[Dict]:
        """Prioritize tasks based on impact and dependencies"""
        # Sort by priority (high, medium, low)
        priority_order = {"high": 0, "medium": 1, "low": 2}
        
        def sort_key(assignment):
            issue = assignment["issue"]
            return priority_order.get(issue.get("priority", "low"), 3)
        
        return sorted(assignments, key=sort_key)
    
    def generate_work_plan(self) -> Dict:
        """Generate a complete work plan"""
        # Detect issues
        issues = self.detect_issues()
        
        # Filter out already completed tasks
        filtered_issues = self.filter_completed_tasks(issues)
        
        # Assign tasks
        assignments = self.assign_tasks(filtered_issues)
        
        # Prioritize tasks
        prioritized = self.prioritize_tasks(assignments)
        
        # Create work plan
        work_plan = {
            "generated_at": datetime.now().isoformat(),
            "total_issues": len(issues),
            "completed_tasks": len(issues) - len(filtered_issues),
            "total_assignments": len(prioritized),
            "assignments": prioritized
        }
        
        return work_plan
    
    def save_work_plan(self, work_plan: Dict, filename: str = None):
        """Save work plan to file"""
        if filename is None:
            filename = self.work_plan_file
            
        with open(filename, 'w') as f:
            json.dump(work_plan, f, indent=2)
        print(f"Work plan saved to {filename}")
    
    def is_task_completed(self, task_type: str, location: str) -> bool:
        """Check if a task has already been completed"""
        for completed_task in self.completed_tasks:
            if (completed_task.get("type") == task_type and 
                completed_task.get("location") == location):
                return True
        return False
    
    def mark_task_completed(self, task_type: str, location: str, agent_id: str, validation_score: float):
        """Mark a task as completed"""
        completed_task = {
            "type": task_type,
            "location": location,
            "completed_by": agent_id,
            "completed_at": datetime.now().isoformat(),
            "validation_score": validation_score
        }
        
        self.completed_tasks.append(completed_task)
        
        # Save to file
        with open(self.completed_tasks_file, 'w') as f:
            json.dump(self.completed_tasks, f, indent=2)
        
        print(f"Task marked as completed: {task_type} at {location}")
    
    def filter_completed_tasks(self, issues: List[Dict]) -> List[Dict]:
        """Filter out issues that have already been completed"""
        filtered_issues = []
        
        for issue in issues:
            if not self.is_task_completed(issue.get("type"), issue.get("location")):
                filtered_issues.append(issue)
            else:
                print(f"Skipping completed task: {issue.get('description')}")
        
        return filtered_issues
    
    def claim_task(self, agent_id: str, task_index: int) -> bool:
        """Allow an agent to claim a specific task"""
        try:
            with open(self.work_plan_file, 'r') as f:
                work_plan = json.load(f)
            
            if 0 <= task_index < len(work_plan["assignments"]):
                assignment = work_plan["assignments"][task_index]
                
                # Check if agent is capable
                if agent_id in assignment["capable_agents"]:
                    assignment["assigned_to"] = agent_id
                    assignment["status"] = "assigned"
                    assignment["claimed_at"] = datetime.now().isoformat()
                    
                    # Save updated work plan
                    with open(self.work_plan_file, 'w') as f:
                        json.dump(work_plan, f, indent=2)
                    
                    print(f"Task {task_index} claimed by {agent_id}")
                    return True
                else:
                    print(f"Agent {agent_id} not capable for task {task_index}")
                    return False
            else:
                print(f"Invalid task index: {task_index}")
                return False
        except Exception as e:
            print(f"Error claiming task: {e}")
            return False

if __name__ == "__main__":
    assigner = IntelligentTaskAssigner()
    
    if len(sys.argv) < 2:
        print("Usage: python intelligent-task-assignment.py <command>")
        print("Commands:")
        print("  generate - Generate work plan")
        print("  claim <agent_id> <task_index> - Claim a task")
        print("  complete <task_type> <location> <agent_id> <validation_score> - Mark task as completed")
        print("  status - Show current work plan status")
        print("  completed - Show completed tasks")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "generate":
        work_plan = assigner.generate_work_plan()
        assigner.save_work_plan(work_plan)
        print(f"Generated work plan with {work_plan['total_assignments']} tasks")
        if work_plan.get('completed_tasks', 0) > 0:
            print(f"Skipped {work_plan['completed_tasks']} already completed tasks")
        
    elif command == "claim":
        if len(sys.argv) < 4:
            print("Usage: python intelligent-task-assignment.py claim <agent_id> <task_index>")
            sys.exit(1)
        
        agent_id = sys.argv[2]
        task_index = int(sys.argv[3])
        assigner.claim_task(agent_id, task_index)
        
    elif command == "complete":
        if len(sys.argv) < 6:
            print("Usage: python intelligent-task-assignment.py complete <task_type> <location> <agent_id> <validation_score>")
            sys.exit(1)
        
        task_type = sys.argv[2]
        location = sys.argv[3]
        agent_id = sys.argv[4]
        validation_score = float(sys.argv[5])
        
        assigner.mark_task_completed(task_type, location, agent_id, validation_score)
        
    elif command == "status":
        try:
            with open(assigner.work_plan_file, 'r') as f:
                work_plan = json.load(f)
            
            print(f"Work Plan Status ({work_plan['generated_at']})")
            print(f"Total issues: {work_plan['total_issues']}")
            if work_plan.get('completed_tasks'):
                print(f"Completed tasks: {work_plan['completed_tasks']}")
            print(f"Active tasks: {work_plan['total_assignments']}")
            
            for i, assignment in enumerate(work_plan["assignments"]):
                issue = assignment["issue"]
                status = assignment["status"]
                assigned = assignment.get("assigned_to", "Unassigned")
                
                print(f"{i}. [{status.upper()}] {issue['description']} (Assigned: {assigned})")
        except FileNotFoundError:
            print("No work plan found. Run 'generate' first.")
    
    elif command == "completed":
        if len(assigner.completed_tasks) == 0:
            print("No completed tasks found.")
        else:
            print(f"Completed Tasks ({len(assigner.completed_tasks)} total):")
            for i, task in enumerate(assigner.completed_tasks):
                print(f"{i}. {task['type']} at {task['location']} - Score: {task['validation_score']}/100 by {task['completed_by']} at {task['completed_at']}")
    
    else:
        print(f"Unknown command: {command}")

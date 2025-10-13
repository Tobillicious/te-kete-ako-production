#!/usr/bin/env python3
"""
Content Prioritization System for Te Kete Ako
Analyzes discovered content to determine integration priorities based on
quality, cultural value, curriculum alignment, and user impact.
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class ContentPrioritizer:
    def __init__(self):
        self.discovery_file = "content-discovery-results.json"
        self.prioritized_content = []
        self.integration_phases = {
            "phase_1": {
                "name": "Immediate Integration (Week 1)",
                "description": "High-quality, high-cultural-value content",
                "max_items": 100,
                "criteria": {
                    "min_quality_score": 80,
                    "cultural_level": ["high"],
                    "content_types": ["lessons", "handouts", "units"]
                }
            },
            "phase_2": {
                "name": "Priority Integration (Week 2-3)",
                "description": "Quality content with good curriculum alignment",
                "max_items": 300,
                "criteria": {
                    "min_quality_score": 70,
                    "cultural_level": ["high", "medium"],
                    "content_types": ["lessons", "handouts", "units", "assessments"]
                }
            },
            "phase_3": {
                "name": "Standard Integration (Week 4-6)",
                "description": "All remaining quality content",
                "max_items": 1000,
                "criteria": {
                    "min_quality_score": 60,
                    "cultural_level": ["high", "medium", "low"],
                    "content_types": ["lessons", "handouts", "units", "assessments", "games"]
                }
            },
            "phase_4": {
                "name": "Bulk Integration (Week 7-10)",
                "description": "All remaining content",
                "max_items": 5000,
                "criteria": {
                    "min_quality_score": 0,
                    "cultural_level": ["high", "medium", "low", "none"],
                    "content_types": ["lessons", "handouts", "units", "assessments", "games", "resources"]
                }
            }
        }
    
    def load_discovered_content(self) -> List[Dict]:
        """Load the discovered content from the content discovery results"""
        if not os.path.exists(self.discovery_file):
            print(f"Error: Discovery file {self.discovery_file} not found.")
            print("Run 'python3 scripts/content-treasure-hunter.py discover' first.")
            sys.exit(1)
        
        with open(self.discovery_file, 'r') as f:
            return json.load(f)
    
    def calculate_priority_score(self, content_item: Dict) -> int:
        """Calculate a priority score for content based on multiple factors"""
        score = 0
        
        # Base quality score (40% weight)
        quality_score = content_item.get('quality_score', 0)
        score += quality_score * 0.4
        
        # Cultural value (30% weight)
        cultural_level = content_item.get('cultural_level', 'none')
        cultural_scores = {
            'high': 100,
            'medium': 70,
            'low': 40,
            'none': 0
        }
        score += cultural_scores.get(cultural_level, 0) * 0.3
        
        # Content type importance (20% weight)
        content_type = content_item.get('type', 'other')
        type_scores = {
            'lessons': 100,
            'handouts': 90,
            'units': 95,
            'assessments': 80,
            'games': 70,
            'resources': 60,
            'other': 30
        }
        score += type_scores.get(content_type, 30) * 0.2
        
        # File size indicator (10% weight) - larger files often have more content
        file_size = content_item.get('file_size', 0)
        if file_size > 50000:  # Large files
            size_score = 100
        elif file_size > 20000:  # Medium files
            size_score = 80
        elif file_size > 5000:  # Small files
            size_score = 60
        else:  # Very small files
            size_score = 30
        score += size_score * 0.1
        
        return int(score)
    
    def meets_criteria(self, content_item: Dict, criteria: Dict) -> bool:
        """Check if content item meets the specified criteria"""
        # Check quality score
        if content_item.get('quality_score', 0) < criteria.get('min_quality_score', 0):
            return False
        
        # Check cultural level
        cultural_levels = criteria.get('cultural_level', [])
        if cultural_levels and content_item.get('cultural_level', 'none') not in cultural_levels:
            return False
        
        # Check content types
        content_types = criteria.get('content_types', [])
        if content_types and content_item.get('type', 'other') not in content_types:
            return False
        
        return True
    
    def prioritize_content(self) -> Dict:
        """Prioritize content into integration phases"""
        discovered_content = self.load_discovered_content()
        
        # Calculate priority scores for all content
        for item in discovered_content:
            item['priority_score'] = self.calculate_priority_score(item)
        
        # Sort by priority score (descending)
        discovered_content.sort(key=lambda x: x['priority_score'], reverse=True)
        
        # Assign to phases
        phase_assignments = {}
        used_items = set()
        
        for phase_id, phase_config in self.integration_phases.items():
            phase_items = []
            
            for item in discovered_content:
                if item['path'] in used_items:
                    continue
                
                if self.meets_criteria(item, phase_config['criteria']):
                    phase_items.append(item)
                    used_items.add(item['path'])
                    
                    # Stop if we've reached the max for this phase
                    if len(phase_items) >= phase_config['max_items']:
                        break
            
            phase_assignments[phase_id] = {
                'config': phase_config,
                'items': phase_items,
                'count': len(phase_items)
            }
        
        # Create summary
        total_assigned = sum(phase['count'] for phase in phase_assignments.values())
        unassigned = [item for item in discovered_content if item['path'] not in used_items]
        
        result = {
            'total_discovered': len(discovered_content),
            'total_assigned': total_assigned,
            'total_unassigned': len(unassigned),
            'phases': phase_assignments,
            'unassigned': unassigned[:100],  # Keep first 100 unassigned for reference
            'generated_at': datetime.now().isoformat()
        }
        
        return result
    
    def save_prioritization(self, prioritization: Dict):
        """Save the prioritization results to files"""
        # Save full prioritization
        with open('content-prioritization.json', 'w') as f:
            json.dump(prioritization, f, indent=2)
        
        # Save phase-specific files
        for phase_id, phase_data in prioritization['phases'].items():
            phase_config = phase_data['config']
            phase_items = phase_data['items']
            
            filename = f"integration-{phase_id.replace('_', '-')}.json"
            with open(filename, 'w') as f:
                json.dump({
                    'phase': phase_id,
                    'name': phase_config['name'],
                    'description': phase_config['description'],
                    'items': phase_items,
                    'count': len(phase_items)
                }, f, indent=2)
        
        # Create a summary report
        self.create_summary_report(prioritization)
    
    def create_summary_report(self, prioritization: Dict):
        """Create a human-readable summary report"""
        report = f"""# Content Prioritization Report
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary
- **Total Discovered:** {prioritization['total_discovered']} files
- **Total Assigned:** {prioritization['total_assigned']} files
- **Total Unassigned:** {prioritization['total_unassigned']} files

## Integration Phases

"""
        
        for phase_id, phase_data in prioritization['phases'].items():
            phase_config = phase_data['config']
            phase_items = phase_data['items']
            
            report += f"""### {phase_config['name']}
- **Description:** {phase_config['description']}
- **Items to Integrate:** {len(phase_items)}
- **Criteria:**
  - Minimum Quality Score: {phase_config['criteria'].get('min_quality_score', 0)}
  - Cultural Levels: {', '.join(phase_config['criteria'].get('cultural_level', []))}
  - Content Types: {', '.join(phase_config['criteria'].get('content_types', []))}

**Top 5 Items:**
"""
            
            for i, item in enumerate(phase_items[:5]):
                report += f"{i+1}. **{item['title']}** (Score: {item['priority_score']})\n"
                report += f"   - Path: {item['path']}\n"
                report += f"   - Type: {item.get('type', 'unknown')}\n"
                report += f"   - Cultural Level: {item.get('cultural_level', 'unknown')}\n"
                report += f"   - Quality Score: {item.get('quality_score', 0)}\n\n"
            
            report += "\n"
        
        # Save the report
        with open('content-prioritization-report.md', 'w') as f:
            f.write(report)
    
    def generate_integration_tasks(self) -> List[Dict]:
        """Generate specific integration tasks based on prioritization"""
        if not os.path.exists('content-prioritization.json'):
            print("Error: Prioritization file not found. Run prioritize first.")
            return []
        
        with open('content-prioritization.json', 'r') as f:
            prioritization = json.load(f)
        
        tasks = []
        
        # Create tasks for Phase 1 (Immediate Integration)
        phase_1_items = prioritization['phases']['phase_1']['items']
        if phase_1_items:
            tasks.append({
                'task_id': 'phase-1-integration',
                'title': 'Phase 1: Immediate Integration',
                'description': f'Integrate {len(phase_1_items)} high-priority content items',
                'agent': 'agent-6',  # Orphaned pages specialist
                'priority': 'critical',
                'estimated_hours': 8,
                'items': phase_1_items[:20],  # Limit to first 20 for manageable task
                'phase': 'phase_1'
            })
        
        # Create tasks for Phase 2 (Priority Integration)
        phase_2_items = prioritization['phases']['phase_2']['items']
        if phase_2_items:
            tasks.append({
                'task_id': 'phase-2-integration',
                'title': 'Phase 2: Priority Integration',
                'description': f'Integrate {len(phase_2_items)} priority content items',
                'agent': 'agent-4',  # Navigation specialist
                'priority': 'high',
                'estimated_hours': 16,
                'items': phase_2_items[:30],  # Limit to first 30
                'phase': 'phase_2'
            })
        
        # Create cultural validation task for high cultural value items
        high_cultural_items = [
            item for item in prioritization['phases']['phase_1']['items'] + 
                      prioritization['phases']['phase_2']['items']
            if item.get('cultural_level') == 'high'
        ]
        
        if high_cultural_items:
            tasks.append({
                'task_id': 'cultural-validation',
                'title': 'Cultural Validation of High-Value Content',
                'description': f'Validate cultural authenticity of {len(high_cultural_items)} high cultural value items',
                'agent': 'agent-7',  # Cultural specialist
                'priority': 'critical',
                'estimated_hours': 12,
                'items': high_cultural_items[:25],  # Limit to first 25
                'phase': 'validation'
            })
        
        return tasks
    
    def save_integration_tasks(self, tasks: List[Dict]):
        """Save integration tasks to file"""
        with open('content-integration-tasks.json', 'w') as f:
            json.dump(tasks, f, indent=2)
        
        print(f"Generated {len(tasks)} integration tasks")
        for task in tasks:
            print(f"  - {task['title']}: {task['description']} (Agent: {task['agent']})")

if __name__ == "__main__":
    prioritizer = ContentPrioritizer()
    
    if len(sys.argv) < 2:
        print("Usage: python content-prioritizer.py <command>")
        print("Commands:")
        print("  prioritize - Analyze and prioritize content")
        print("  tasks - Generate integration tasks")
        print("  full - Run complete prioritization and task generation")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "prioritize":
        print("🎯 Prioritizing content...")
        prioritization = prioritizer.prioritize_content()
        prioritizer.save_prioritization(prioritization)
        print(f"✅ Prioritization complete!")
        print(f"   Total discovered: {prioritization['total_discovered']}")
        print(f"   Total assigned: {prioritization['total_assigned']}")
        print(f"   Total unassigned: {prioritization['total_unassigned']}")
        
    elif command == "tasks":
        print("📋 Generating integration tasks...")
        tasks = prioritizer.generate_integration_tasks()
        prioritizer.save_integration_tasks(tasks)
        
    elif command == "full":
        print("🚀 Running complete prioritization...")
        prioritization = prioritizer.prioritize_content()
        prioritizer.save_prioritization(prioritization)
        print(f"✅ Prioritization complete!")
        
        print("📋 Generating integration tasks...")
        tasks = prioritizer.generate_integration_tasks()
        prioritizer.save_integration_tasks(tasks)
        print("✅ Task generation complete!")
        
    else:
        print(f"Unknown command: {command}")

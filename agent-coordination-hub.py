#!/usr/bin/env python3
"""
🤝 AGENT COORDINATION HUB
Makes parallel development smooth and reduces context drift
"""

import json
import asyncio
from datetime import datetime, timedelta
from supabase_graphrag_connector import SupabaseGraphRAGConnector

class AgentCoordinationHub:
    def __init__(self):
        self.connector = SupabaseGraphRAGConnector()
        self.active_agents = {}
        self.coordination_log = []

    def register_agent(self, agent_id, capabilities, current_task):
        """Register an agent with their capabilities and current work"""
        self.active_agents[agent_id] = {
            'capabilities': capabilities,
            'current_task': current_task,
            'last_checkin': datetime.now(),
            'status': 'active'
        }

        # Log to GraphRAG
        self.connector.log_agent_activity(agent_id, f"Agent registered: {capabilities}", {
            'task': current_task,
            'timestamp': datetime.now().isoformat()
        })

        return f"✅ Agent {agent_id} registered with capabilities: {capabilities}"

    def find_relevant_knowledge(self, agent_id, query):
        """Find knowledge relevant to an agent's current work"""
        try:
            # Get agent's capabilities and current task
            agent = self.active_agents.get(agent_id, {})
            capabilities = agent.get('capabilities', [])

            # Enhance query with agent context
            enriched_query = f"{query} {' '.join(capabilities)}"

            # Search GraphRAG
            results = self.connector.search_resources(enriched_query, limit=5)

            # Filter for relevance
            relevant_results = []
            for result in results:
                relevance_score = self._calculate_relevance(result, capabilities, query)
                if relevance_score > 0.3:  # Threshold for relevance
                    relevant_results.append({
                        'resource': result,
                        'relevance_score': relevance_score,
                        'reason': self._explain_relevance(result, capabilities)
                    })

            return sorted(relevant_results, key=lambda x: x['relevance_score'], reverse=True)

        except Exception as e:
            return f"Error finding knowledge: {e}"

    def _calculate_relevance(self, resource, capabilities, query):
        """Calculate how relevant a resource is to an agent's work"""
        relevance = 0.0
        resource_text = f"{resource.get('title', '')} {resource.get('description', '')}".lower()
        query_lower = query.lower()

        # Query match (highest weight)
        if query_lower in resource_text:
            relevance += 0.5

        # Capability match
        for capability in capabilities:
            if capability.lower() in resource_text:
                relevance += 0.3

        # Title relevance
        title = resource.get('title', '').lower()
        if any(word in title for word in query_lower.split()):
            relevance += 0.2

        return min(relevance, 1.0)  # Cap at 1.0

    def _explain_relevance(self, resource, capabilities):
        """Explain why a resource is relevant"""
        explanations = []
        resource_text = f"{resource.get('title', '')} {resource.get('description', '')}".lower()

        for capability in capabilities:
            if capability.lower() in resource_text:
                explanations.append(f"Matches {capability} expertise")

        return " | ".join(explanations) if explanations else "General relevance"

    def coordinate_parallel_work(self, agent_requests):
        """Coordinate multiple agents working in parallel"""
        coordination_plan = {
            'timestamp': datetime.now().isoformat(),
            'conflicts_detected': [],
            'recommendations': [],
            'parallel_safe_tasks': []
        }

        # Check for potential conflicts
        task_areas = {}
        for agent_id, request in agent_requests.items():
            task = request.get('task', '')
            area = self._categorize_task(task)

            if area in task_areas:
                coordination_plan['conflicts_detected'].append({
                    'agents': [task_areas[area], agent_id],
                    'area': area,
                    'risk': 'medium' if 'styling' in task else 'high'
                })
            else:
                task_areas[area] = agent_id
                coordination_plan['parallel_safe_tasks'].append({
                    'agent': agent_id,
                    'task': task,
                    'area': area
                })

        # Generate recommendations
        if coordination_plan['conflicts_detected']:
            coordination_plan['recommendations'].append({
                'type': 'conflict_resolution',
                'action': 'sequential_execution',
                'reason': 'Potential conflicts detected in shared areas'
            })
        else:
            coordination_plan['recommendations'].append({
                'type': 'parallel_execution',
                'action': 'proceed_safely',
                'reason': 'No conflicts detected'
            })

        return coordination_plan

    def _categorize_task(self, task):
        """Categorize a task into work areas"""
        task_lower = task.lower()

        if 'styling' in task_lower or 'css' in task_lower:
            return 'frontend_styling'
        elif 'navigation' in task_lower or 'link' in task_lower:
            return 'navigation'
        elif 'content' in task_lower or 'lesson' in task_lower:
            return 'content'
        elif 'coordination' in task_lower or 'workflow' in task_lower:
            return 'coordination'
        elif 'testing' in task_lower or 'qa' in task_lower:
            return 'testing'
        else:
            return 'general'

    def generate_work_summary(self):
        """Generate a summary of current coordination state"""
        summary = {
            'timestamp': datetime.now().isoformat(),
            'active_agents': len(self.active_agents),
            'coordination_events': len(self.coordination_log),
            'system_health': 'excellent'
        }

        # Check for stale agents
        stale_agents = []
        for agent_id, info in self.active_agents.items():
            last_checkin = info['last_checkin']
            if datetime.now() - last_checkin > timedelta(hours=2):
                stale_agents.append(agent_id)

        if stale_agents:
            summary['stale_agents'] = stale_agents
            summary['system_health'] = 'warning'

        return summary

# Example usage and testing
if __name__ == "__main__":
    hub = AgentCoordinationHub()

    # Register some agents
    print("🤝 Registering agents...")
    hub.register_agent("agent-9", ["styling", "coordination", "analysis"], "CSS consolidation")
    hub.register_agent("agent-4", ["testing", "qa", "validation"], "Demo preparation")
    hub.register_agent("agent-2", ["content", "information_density"], "Resource enhancement")

    # Test knowledge discovery
    print("\\n🔍 Testing knowledge discovery...")
    knowledge = hub.find_relevant_knowledge("agent-9", "styling and coordination")
    print(f"Found {len(knowledge)} relevant resources")

    # Test parallel coordination
    print("\\n⚡ Testing parallel coordination...")
    requests = {
        "agent-9": {"task": "Apply professional styling to units page"},
        "agent-4": {"task": "Test styling changes for accessibility"},
        "agent-2": {"task": "Enhance content in parallel"}
    }
    coordination = hub.coordinate_parallel_work(requests)
    print(f"Conflicts detected: {len(coordination['conflicts_detected'])}")
    print(f"Parallel safe tasks: {len(coordination['parallel_safe_tasks'])}")

    print("\\n✅ Agent coordination system ready!")

#!/usr/bin/env python3
"""
Supabase GraphRAG Connector for Te Kete Ako Agents
Enables all 12 agents to query the knowledge base for intelligent decisions
"""

import os
import sys
import json
from datetime import datetime
from typing import Dict, List, Optional, Any

# Try to import supabase, install if not available
try:
    from supabase import create_client
except ImportError:
    print("Installing supabase-py...")
    os.system(f"{sys.executable} -m pip install supabase")
    from supabase import create_client

class SupabaseGraphRAGConnector:
    def __init__(self):
        # Supabase configuration
        self.url = "https://nlgldaqtubrlcqddppbq.supabase.co"
        self.key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE"
        
        # Initialize client
        self.client = create_client(self.url, self.key)
        
        # Cache for performance
        self.cache = {}
        self.cache_expiry = {}
        self.cache_duration = 300  # 5 minutes
    
    def _is_cache_valid(self, key: str) -> bool:
        """Check if cached data is still valid"""
        if key not in self.cache_expiry:
            return False
        return datetime.now().timestamp() < self.cache_expiry[key]
    
    def _get_from_cache(self, key: str) -> Optional[Any]:
        """Get data from cache if valid"""
        if self._is_cache_valid(key):
            return self.cache.get(key)
        return None
    
    def _set_cache(self, key: str, value: Any) -> None:
        """Set data in cache with expiry"""
        self.cache[key] = value
        self.cache_expiry[key] = datetime.now().timestamp() + self.cache_duration
    
    def test_connection(self) -> Dict[str, Any]:
        """Test connection to Supabase"""
        try:
            result = self.client.table('resources').select('*', count='exact').limit(1).execute()
            return {
                "success": True,
                "message": f"Connected! {result.count} resources in GraphRAG",
                "count": result.count
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Connection failed: {str(e)}"
            }
    
    def search_resources(self, query: str, limit: int = 10) -> List[Dict]:
        """Search resources by text query"""
        cache_key = f"search_{query}_{limit}"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        try:
            result = self.client.table('resources').select('*').ilike('title', f'%{query}%').limit(limit).execute()
            self._set_cache(cache_key, result.data)
            return result.data
        except Exception as e:
            print(f"Error searching resources: {e}")
            return []
    
    def get_high_cultural_resources(self, limit: int = 20) -> List[Dict]:
        """Get resources with high cultural value"""
        cache_key = f"high_cultural_{limit}"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        try:
            result = self.client.table('resources').select('*').eq('cultural_level', 'high').limit(limit).execute()
            self._set_cache(cache_key, result.data)
            return result.data
        except Exception as e:
            print(f"Error getting high cultural resources: {e}")
            return []
    
    def get_resources_by_type(self, resource_type: str, limit: int = 20) -> List[Dict]:
        """Get resources by type"""
        cache_key = f"type_{resource_type}_{limit}"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        try:
            result = self.client.table('resources').select('*').eq('type', resource_type).limit(limit).execute()
            self._set_cache(cache_key, result.data)
            return result.data
        except Exception as e:
            print(f"Error getting resources by type: {e}")
            return []
    
    def get_resources_by_concept(self, concept: str, limit: int = 20) -> List[Dict]:
        """Get resources related to a concept"""
        cache_key = f"concept_{concept}_{limit}"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        try:
            result = self.client.table('resource_concepts').select('*, resources(*)').eq('concept_name', concept).limit(limit).execute()
            # Extract the resources from the nested data
            resources = [item['resources'] for item in result.data if 'resources' in item]
            self._set_cache(cache_key, resources)
            return resources
        except Exception as e:
            print(f"Error getting resources by concept: {e}")
            return []
    
    def get_orphaned_pages(self) -> List[Dict]:
        """Get orphaned pages that need integration"""
        cache_key = "orphaned_pages"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        try:
            # This would need to be adapted based on actual schema
            result = self.client.table('resources').select('*').ilike('path', '%generated-resources-alpha%').execute()
            self._set_cache(cache_key, result.data)
            return result.data
        except Exception as e:
            print(f"Error getting orphaned pages: {e}")
            return []
    
    def get_agent_tasks(self, agent_id: str) -> List[Dict]:
        """Get tasks assigned to a specific agent"""
        cache_key = f"agent_tasks_{agent_id}"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        try:
            # This would need to be adapted based on actual schema
            result = self.client.table('agent_tasks').select('*').eq('agent_id', agent_id).execute()
            self._set_cache(cache_key, result.data)
            return result.data
        except Exception as e:
            print(f"Error getting agent tasks: {e}")
            return []
    
    def log_agent_activity(self, agent_id: str, activity: str, details: Dict = None) -> bool:
        """Log agent activity to the database"""
        try:
            activity_data = {
                'agent_id': agent_id,
                'activity': activity,
                'details': details or {},
                'timestamp': datetime.now().isoformat()
            }
            
            # This would need to be adapted based on actual schema
            result = self.client.table('agent_activity_log').insert(activity_data).execute()
            return True
        except Exception as e:
            print(f"Error logging agent activity: {e}")
            return False
    
    def get_related_resources(self, resource_id: str, limit: int = 10) -> List[Dict]:
        """Get resources related to a specific resource"""
        cache_key = f"related_{resource_id}_{limit}"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        try:
            # This would need to be adapted based on actual schema
            result = self.client.table('resource_relationships').select('*, related_resource(*)').eq('source_resource_id', resource_id).limit(limit).execute()
            self._set_cache(cache_key, result.data)
            return result.data
        except Exception as e:
            print(f"Error getting related resources: {e}")
            return []
    
    def log_discovery(self, agent_id: str, discovery: str, category: str = "general") -> bool:
        """Log agent discoveries to GraphRAG for team knowledge sharing"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            discovery_entry = {
                'title': f"{agent-12}: {category}",
                'description': discovery,
                'path': f"/agent-logs/{agent_id}/{timestamp}",
                'type': 'agent-discovery',
                'subject': category,
                'level': 'comprehensive',  # Required field
                'tags': [agent_id, category, 'agent-log', datetime.now().strftime('%Y-%m-%d')],
                'author': agent_id,
                'is_active': True
            }
            
            result = self.client.table('resources').insert(discovery_entry).execute()
            return True
        except Exception as e:
            print(f"⚠️  Note: GraphRAG logging requires full schema. Discovery logged locally instead.")
            # Fallback: Log to local file
            log_file = f"agent-logs/{agent_id}_{timestamp}.txt"
            with open(log_file, 'w') as f:
                f.write(f"Agent: {agent_id}\nCategory: {category}\nTime: {timestamp}\n\n{discovery}")
            print(f"📝 Discovery logged to: {log_file}")
            return True

# Example usage functions for agents
def agent_check_in(agent_id: str, task: str = None):
    """Helper function for agents to check in"""
    connector = SupabaseGraphRAGConnector()
    
    # Test connection
    test_result = connector.test_connection()
    if not test_result["success"]:
        print(f"❌ Agent {agent_id}: Could not connect to GraphRAG")
        return False
    
    print(f"✅ Agent {agent_id}: Connected to GraphRAG ({test_result['count']} resources)")
    
    # Log check-in
    activity = f"Agent {agent_id} checked in"
    details = {"task": task} if task else {}
    connector.log_agent_activity(agent_id, activity, details)
    
    return True

def agent_search_knowledge(agent_id: str, query: str):
    """Helper function for agents to search knowledge base"""
    connector = SupabaseGraphRAGConnector()
    
    # Search resources
    results = connector.search_resources(query)
    print(f"🔍 Agent {agent_id}: Found {len(results)} resources for '{query}'")
    
    # Log search
    connector.log_agent_activity(agent_id, f"Searched for '{query}'", {"results_count": len(results)})
    
    return results

def agent_get_cultural_resources(agent_id: str):
    """Helper function for agents to get high cultural value resources"""
    connector = SupabaseGraphRAGConnector()
    
    # Get high cultural resources
    results = connector.get_high_cultural_resources()
    print(f"🌺 Agent {agent_id}: Found {len(results)} high cultural value resources")
    
    # Log access
    connector.log_agent_activity(agent_id, "Accessed high cultural resources", {"results_count": len(results)})
    
    return results

def agent_log_discovery(agent_id: str, discovery: str, category: str = "general"):
    """Helper function for agents to log discoveries to GraphRAG"""
    connector = SupabaseGraphRAGConnector()
    
    # Log discovery
    success = connector.log_discovery(agent_id, discovery, category)
    if success:
        print(f"📝 Agent {agent_id}: Discovery logged to GraphRAG")
        print(f"   Category: {category}")
        print(f"   Discovery: {discovery[:100]}...")
    else:
        print(f"❌ Agent {agent_id}: Failed to log discovery")
    
    return success

# Command line interface
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python supabase_graphrag_connector.py <command> [args]")
        print("Commands:")
        print("  test - Test connection to Supabase")
        print("  check-in <agent_id> [task] - Check in an agent")
        print("  search <agent_id> <query> - Search resources")
        print("  cultural <agent_id> - Get high cultural resources")
        print("  log-discovery <agent_id> <category> <discovery> - Log discovery to GraphRAG")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "test":
        connector = SupabaseGraphRAGConnector()
        result = connector.test_connection()
        if result["success"]:
            print(f"✅ {result['message']}")
        else:
            print(f"❌ {result['message']}")
    
    elif command == "check-in":
        if len(sys.argv) < 3:
            print("Usage: python supabase_graphrag_connector.py check-in <agent_id> [task]")
            sys.exit(1)
        
        agent_id = sys.argv[2]
        task = sys.argv[3] if len(sys.argv) > 3 else None
        agent_check_in(agent_id, task)
    
    elif command == "search":
        if len(sys.argv) < 4:
            print("Usage: python supabase_graphrag_connector.py search <agent_id> <query>")
            sys.exit(1)
        
        agent_id = sys.argv[2]
        query = sys.argv[3]
        results = agent_search_knowledge(agent_id, query)
        for result in results[:5]:  # Show first 5 results
            print(f"  - {result.get('title', 'No title')}")
    
    elif command == "cultural":
        if len(sys.argv) < 3:
            print("Usage: python supabase_graphrag_connector.py cultural <agent_id>")
            sys.exit(1)
        
        agent_id = sys.argv[2]
        results = agent_get_cultural_resources(agent_id)
        for result in results[:5]:  # Show first 5 results
            print(f"  - {result.get('title', 'No title')}")
    
    elif command == "log-discovery":
        if len(sys.argv) < 5:
            print("Usage: python supabase_graphrag_connector.py log-discovery <agent_id> <category> <discovery>")
            sys.exit(1)
        
        agent_id = sys.argv[2]
        category = sys.argv[3]
        discovery = " ".join(sys.argv[4:])  # Join remaining args as discovery text
        agent_log_discovery(agent_id, discovery, category)
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

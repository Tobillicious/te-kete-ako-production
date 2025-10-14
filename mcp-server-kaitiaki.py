#!/usr/bin/env python3
"""
MCP Server for Kaitiaki Aronui - Proper Model Context Protocol Implementation
Enables Cursor agents to coordinate via MCP + GraphRAG
"""

import sys
import json
from datetime import datetime
from typing import Dict, List, Optional

# Use the existing Supabase connector
try:
    from supabase_graphrag_connector import SupabaseGraphRAGConnector
except ImportError:
    print("Error: supabase_graphrag_connector not found", file=sys.stderr)
    sys.exit(1)

class KaitiakiMCPServer:
    """MCP Server for Te Kete Ako 12-Agent Coordination"""
    
    def __init__(self):
        self.connector = SupabaseGraphRAGConnector()
        self.agents = {}
        self.session_id = datetime.now().isoformat()
        
    def handle_initialize(self, params: dict) -> dict:
        """Handle MCP initialize request"""
        return {
            "protocolVersion": "1.0",
            "serverInfo": {
                "name": "kaitiaki-aronui-mcp",
                "version": "1.0.0"
            },
            "capabilities": {
                "tools": {
                    "list_agents": {
                        "description": "List all active agents and their status"
                    },
                    "check_in": {
                        "description": "Register agent with MCP server"
                    },
                    "query_graphrag": {
                        "description": "Query GraphRAG knowledge base"
                    },
                    "update_knowledge": {
                        "description": "Add new knowledge to GraphRAG"
                    },
                    "get_assignments": {
                        "description": "Get current work assignments"
                    }
                }
            }
        }
    
    def handle_list_tools(self, params: dict) -> dict:
        """List available tools"""
        return {
            "tools": [
                {
                    "name": "list_agents",
                    "description": "Get status of all 12 agents",
                    "inputSchema": {
                        "type": "object",
                        "properties": {}
                    }
                },
                {
                    "name": "check_in",
                    "description": "Check in as an agent",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "agent_id": {"type": "string"},
                            "status": {"type": "string"},
                            "current_work": {"type": "string"}
                        },
                        "required": ["agent_id"]
                    }
                },
                {
                    "name": "query_graphrag",
                    "description": "Search GraphRAG knowledge base",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string"},
                            "limit": {"type": "number"}
                        },
                        "required": ["query"]
                    }
                },
                {
                    "name": "update_knowledge",
                    "description": "Add knowledge to GraphRAG",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "agent_id": {"type": "string"},
                            "title": {"type": "string"},
                            "content": {"type": "string"}
                        },
                        "required": ["agent_id", "title", "content"]
                    }
                }
            ]
        }
    
    def handle_call_tool(self, params: dict) -> dict:
        """Handle tool calls"""
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        
        if tool_name == "list_agents":
            return self._list_agents()
        elif tool_name == "check_in":
            return self._check_in(arguments)
        elif tool_name == "query_graphrag":
            return self._query_graphrag(arguments)
        elif tool_name == "update_knowledge":
            return self._update_knowledge(arguments)
        else:
            return {"error": f"Unknown tool: {tool_name}"}
    
    def _list_agents(self) -> dict:
        """List all agents"""
        return {
            "content": [{
                "type": "text",
                "text": json.dumps({
                    "total": 12,
                    "active": len(self.agents),
                    "agents": self.agents,
                    "session": self.session_id
                }, indent=2)
            }]
        }
    
    def _check_in(self, args: dict) -> dict:
        """Check in an agent"""
        agent_id = args.get("agent_id")
        status = args.get("status", "online")
        current_work = args.get("current_work", "")
        
        self.agents[agent_id] = {
            "id": agent_id,
            "status": status,
            "current_work": current_work,
            "last_seen": datetime.now().isoformat()
        }
        
        return {
            "content": [{
                "type": "text",
                "text": f"✅ {agent_id} checked in. {len(self.agents)}/12 agents active."
            }]
        }
    
    def _query_graphrag(self, args: dict) -> dict:
        """Query GraphRAG"""
        query = args.get("query")
        limit = args.get("limit", 10)
        
        results = self.connector.search_resources(query, limit)
        
        return {
            "content": [{
                "type": "text",
                "text": json.dumps({
                    "query": query,
                    "results_count": len(results),
                    "results": results[:5]  # First 5 results
                }, indent=2)
            }]
        }
    
    def _update_knowledge(self, args: dict) -> dict:
        """Update GraphRAG with new knowledge"""
        agent_id = args.get("agent_id")
        title = args.get("title")
        content = args.get("content")
        
        # Log to GraphRAG connector
        success = self.connector.log_agent_activity(
            agent_id,
            f"Added knowledge: {title}",
            {"content": content}
        )
        
        return {
            "content": [{
                "type": "text",
                "text": f"✅ Knowledge '{title}' added by {agent_id}" if success else "❌ Failed to add knowledge"
            }]
        }
    
    def run(self):
        """Run MCP server with stdio transport"""
        for line in sys.stdin:
            try:
                request = json.loads(line)
                method = request.get("method")
                params = request.get("params", {})
                request_id = request.get("id")
                
                # Handle different MCP methods
                if method == "initialize":
                    result = self.handle_initialize(params)
                elif method == "tools/list":
                    result = self.handle_list_tools(params)
                elif method == "tools/call":
                    result = self.handle_call_tool(params)
                else:
                    result = {"error": f"Unknown method: {method}"}
                
                # Send response
                response = {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "result": result
                }
                print(json.dumps(response), flush=True)
                
            except Exception as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": request.get("id") if isinstance(request, dict) else None,
                    "error": {
                        "code": -32603,
                        "message": str(e)
                    }
                }
                print(json.dumps(error_response), flush=True)

if __name__ == "__main__":
    server = KaitiakiMCPServer()
    server.run()


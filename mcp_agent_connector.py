#!/usr/bin/env python3
"""
MCP Agent Connector for Te Kete Ako
Enables all 12 agents to connect to Supabase GraphRAG for real-time collaboration

Usage: python mcp_agent_connector.py [agent-id]
"""

import os
import sys
import re
from datetime import datetime
from supabase import create_client

# Configuration
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class MCPAgentConnector:
    def __init__(self, agent_id=None):
        self.agent_id = agent_id or f"Agent-{hash(datetime.now()) % 12 + 1}"
        self.status = 'active'
        self.last_update = datetime.now().isoformat()
    
    def check_in(self, task="Collaborating via MCP"):
        """Check in to the coordination system"""
        try:
            # Update progress-log.md
            timestamp = datetime.now().strftime("%H:%M")
            log_entry = f"[{timestamp}] {self.agent_id}: ✅ Connected via MCP - {task}\n"
            
            with open("progress-log.md", "a") as f:
                f.write(log_entry)
            
            # Update AGENT_MCP_COORDINATION.md
            self.update_agent_status(task)
            
            print(f"✅ {self.agent_id} checked in successfully")
            return True
        except Exception as error:
            print(f"❌ Failed to check in: {str(error)}")
            return False
    
    def update_agent_status(self, task):
        """Update agent status in coordination file"""
        try:
            with open("AGENT_MCP_COORDINATION.md", "r") as f:
                content = f.read()
            
            # Find the agent status table and update this agent's status
            timestamp = datetime.now().strftime("%H:%M")
            agent_line = f"| {self.agent_id} | 🟢 Active | {task} | {timestamp} |"
            
            # Check if agent already exists in table
            if f"| {self.agent_id} |" in content:
                # Update existing line
                pattern = re.compile(rf"\| {re.escape(self.agent_id)} \|[^\n]*")
                content = pattern.sub(agent_line, content)
            else:
                # Add new line before the closing table
                table_end = content.find("| Agent 12 | 🟡 Pending | Awaiting task | - |")
                if table_end != -1:
                    content = content[:table_end] + agent_line + "\n" + content[table_end:]
            
            with open("AGENT_MCP_COORDINATION.md", "w") as f:
                f.write(content)
        except Exception as error:
            print(f"Failed to update agent status: {str(error)}")
    
    def query_resources(self, topic, limit=10):
        """Query GraphRAG for resources"""
        try:
            result = supabase.table('resources').select('*').ilike('title', f'%{topic}%').limit(limit).execute()
            
            data = result.data
            print(f"📚 Found {len(data)} resources on \"{topic}\":")
            for i, resource in enumerate(data):
                print(f"  {i+1}. {resource['title']} ({resource.get('type', 'unknown')})")
            
            return data
        except Exception as error:
            print(f"❌ Query failed: {str(error)}")
            return []
    
    def find_high_cultural_content(self, limit=10):
        """Find high cultural content"""
        try:
            result = supabase.table('resources').select('*').eq('cultural_level', 'high').limit(limit).execute()
            
            data = result.data
            print(f"🌱 Found {len(data)} high cultural resources:")
            for i, resource in enumerate(data):
                print(f"  {i+1}. {resource['title']} ({resource.get('type', 'unknown')})")
            
            return data
        except Exception as error:
            print(f"❌ Query failed: {str(error)}")
            return []
    
    def check_resource_exists(self, title):
        """Check if resource exists before creating"""
        try:
            result = supabase.table('resources').select('*').eq('title', title).limit(1).execute()
            return len(result.data) > 0
        except Exception as error:
            print(f"❌ Check failed: {str(error)}")
            return False
    
    def post_question(self, question):
        """Post a question to ACTIVE_QUESTIONS.md"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"\n### {self.agent_id} asks ({timestamp}):\n{question}\n\n"
            
            with open("ACTIVE_QUESTIONS.md", "a") as f:
                f.write(entry)
            
            print("🤔 Question posted to ACTIVE_QUESTIONS.md")
        except Exception as error:
            print(f"❌ Failed to post question: {str(error)}")
    
    def get_team_updates(self):
        """Get latest updates from team"""
        try:
            with open("progress-log.md", "r") as f:
                lines = f.readlines()
            
            # Get last 20 lines
            recent_lines = lines[-20:]
            print("📋 Recent team updates:")
            for line in recent_lines:
                if line.strip():
                    print(f"  {line.strip()}")
            
            return recent_lines
        except Exception as error:
            print(f"❌ Failed to get updates: {str(error)}")
            return []
    
    def start_collaboration(self, task):
        """Start collaboration session"""
        print(f"🚀 Starting MCP collaboration for {self.agent_id}")
        
        # Check in
        self.check_in(task)
        
        # Get team updates
        self.get_team_updates()
        
        # Example query to GraphRAG
        print(f"\n🧠 Example GraphRAG query for \"{self.agent_id}\":")
        self.query_resources('māori', 3)
        
        print(f"\n✅ {self.agent_id} is now connected and ready to collaborate!")
        print(f"\n📖 Available methods:")
        print(f"  - connector.query_resources(topic)")
        print(f"  - connector.find_high_cultural_content()")
        print(f"  - connector.check_resource_exists(title)")
        print(f"  - connector.post_question(question)")
        print(f"  - connector.get_team_updates()")
        print(f"  - connector.check_in(task)")

# Auto-run if called directly
if __name__ == "__main__":
    agent_id = sys.argv[1] if len(sys.argv) > 1 else None
    connector = MCPAgentConnector(agent_id)
    connector.start_collaboration("MCP connection established")

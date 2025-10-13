#!/usr/bin/env node

/**
 * ================================================================
 * AGENT SUPABASE GRAPHRAG CONNECTION - TE KETE AKO
 * ================================================================
 * 
 * Unified connection script for all 12 agents to access the
 * Supabase GraphRAG knowledge base for intelligent decision making
 * 
 * Usage: node agent-graphrag-connection.js [agent_id] [query]
 * 
 * ================================================================
 */

const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

// Configuration
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

class AgentGraphRAGConnection {
    constructor(agentId) {
        this.agentId = agentId || `agent-${Math.floor(Math.random() * 12) + 1}`;
        this.supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
        this.connectionTime = new Date().toISOString();
        
        console.log(`🔗 Agent ${this.agentId} connecting to Supabase GraphRAG...`);
    }
    
    async testConnection() {
        try {
            const { count, error } = await this.supabase
                .from('resources')
                .select('*', { count: 'exact', head: true });
                
            if (error) throw error;
            
            console.log(`✅ Connected! Found ${count} resources in GraphRAG`);
            return { success: true, count };
        } catch (error) {
            console.error(`❌ Connection failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
    
    async searchResources(query, options = {}) {
        const {
            limit = 10,
            culturalLevel = null,
            resourceType = null,
            concept = null
        } = options;
        
        try {
            let supabaseQuery = this.supabase
                .from('resources')
                .select('*')
                .ilike('title', `%${query}%`)
                .limit(limit);
                
            if (culturalLevel) {
                supabaseQuery = supabaseQuery.eq('cultural_level', culturalLevel);
            }
            
            if (resourceType) {
                supabaseQuery = supabaseQuery.eq('type', resourceType);
            }
            
            const { data, error } = await supabaseQuery;
            
            if (error) throw error;
            
            console.log(`🔍 Found ${data.length} resources matching "${query}"`);
            return { success: true, data };
        } catch (error) {
            console.error(`❌ Search failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
    
    async findByConcept(conceptName, limit = 10) {
        try {
            const { data, error } = await this.supabase
                .from('resource_concepts')
                .select('*, resources(*)')
                .eq('concept_name', conceptName)
                .limit(limit);
                
            if (error) throw error;
            
            console.log(`🧠 Found ${data.length} resources for concept "${conceptName}"`);
            return { success: true, data };
        } catch (error) {
            console.error(`❌ Concept search failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
    
    async getHighCulturalResources(limit = 20) {
        try {
            const { data, error } = await this.supabase
                .from('resources')
                .select('*')
                .eq('cultural_level', 'high')
                .limit(limit);
                
            if (error) throw error;
            
            console.log(`🌱 Found ${data.length} high cultural value resources`);
            return { success: true, data };
        } catch (error) {
            console.error(`❌ High cultural search failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
    
    async logAgentActivity(activity, details = {}) {
        try {
            const logEntry = {
                agent_id: this.agentId,
                activity,
                details,
                timestamp: new Date().toISOString()
            };
            
            // In a real implementation, you might have an agent_activity table
            // For now, we'll log to a local file
            const logFile = path.join(__dirname, 'agent-activity.log');
            const logLine = JSON.stringify(logEntry) + '\n';
            fs.appendFileSync(logFile, logLine);
            
            console.log(`📝 Activity logged: ${activity}`);
            return { success: true };
        } catch (error) {
            console.error(`❌ Activity logging failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
    
    async registerWithMCP() {
        try {
            const response = await fetch('http://localhost:3001/register-agent', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    agentId: this.agentId,
                    capabilities: ['graphrag-query', 'resource-search', 'cultural-analysis'],
                    timestamp: this.connectionTime
                })
            });
            
            if (!response.ok) {
                throw new Error(`MCP registration failed: ${response.statusText}`);
            }
            
            const result = await response.json();
            console.log(`🤝 Registered with MCP: ${result.message}`);
            return { success: true, data: result };
        } catch (error) {
            console.error(`❌ MCP registration failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
    
    async getCollaborationStatus() {
        try {
            const response = await fetch('http://localhost:3001/status');
            
            if (!response.ok) {
                throw new Error(`Failed to get status: ${response.statusText}`);
            }
            
            const status = await response.json();
            console.log(`📊 Collaboration status: ${status.agents} agents active`);
            return { success: true, data: status };
        } catch (error) {
            console.error(`❌ Status check failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
}

// Command line interface
async function main() {
    const args = process.argv.slice(2);
    const agentId = args[0];
    const command = args[1];
    const query = args.slice(2).join(' ');
    
    const agent = new AgentGraphRAGConnection(agentId);
    
    // Test connection first
    const connectionTest = await agent.testConnection();
    if (!connectionTest.success) {
        process.exit(1);
    }
    
    // Register with MCP
    await agent.registerWithMCP();
    
    // Execute command
    switch (command) {
        case 'search':
            if (!query) {
                console.error('Please provide a search query');
                process.exit(1);
            }
            await agent.searchResources(query);
            break;
            
        case 'concept':
            if (!query) {
                console.error('Please provide a concept name');
                process.exit(1);
            }
            await agent.findByConcept(query);
            break;
            
        case 'high-cultural':
            await agent.getHighCulturalResources();
            break;
            
        case 'status':
            await agent.getCollaborationStatus();
            break;
            
        case 'log':
            if (!query) {
                console.error('Please provide an activity to log');
                process.exit(1);
            }
            await agent.logAgentActivity(query);
            break;
            
        default:
            console.log(`
Available commands:
  search [query]     - Search resources by title
  concept [name]     - Find resources by concept
  high-cultural      - Get high cultural value resources
  status             - Check collaboration status
  log [activity]     - Log agent activity
  
Examples:
  node agent-graphrag-connection.js agent-1 search haka
  node agent-graphrag-connection.js agent-2 concept mātauranga
  node agent-graphrag-connection.js agent-3 high-cultural
            `);
    }
}

// Export for use as module
module.exports = AgentGraphRAGConnection;

// Run if called directly
if (require.main === module) {
    main().catch(console.error);
}

#!/usr/bin/env node

/**
 * MCP Agent Connector for Te Kete Ako
 * Enables all 12 agents to connect to Supabase GraphRAG for real-time collaboration
 * 
 * Usage: node mcp-agent-connector.js [agent-id]
 */

const fs = require('fs');
const path = require('path');
const { createClient } = require('@supabase/supabase-js');

// Configuration from .env file
const supabaseUrl = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

// Initialize Supabase client
const supabase = createClient(supabaseUrl, supabaseKey);

// Agent ID from command line argument or default
const agentId = process.argv[2] || `Agent-${Math.floor(Math.random() * 12) + 1}`;

// Main connector class
class MCPAgentConnector {
    constructor(agentId) {
        this.agentId = agentId;
        this.status = 'active';
        this.lastUpdate = new Date().toISOString();
    }

    // Check in to the coordination system
    async checkIn(task = 'Collaborating via MCP') {
        try {
            // Update progress-log.md
            const logEntry = `[${new Date().toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit' })}] ${this.agentId}: ✅ Connected via MCP - ${task}\n`;
            fs.appendFileSync(path.join(__dirname, 'progress-log.md'), logEntry);

            // Update AGENT_MCP_COORDINATION.md
            await this.updateAgentStatus(task);

            console.log(`✅ ${this.agentId} checked in successfully`);
            return true;
        } catch (error) {
            console.error(`❌ Failed to check in: ${error.message}`);
            return false;
        }
    }

    // Update agent status in coordination file
    async updateAgentStatus(task) {
        try {
            const coordFile = path.join(__dirname, 'AGENT_MCP_COORDINATION.md');
            let content = fs.readFileSync(coordFile, 'utf8');
            
            // Find the agent status table and update this agent's status
            const agentLine = `| ${this.agentId} | 🟢 Active | ${task} | ${new Date().toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit' })} |`;
            
            // Check if agent already exists in table
            if (content.includes(`| ${this.agentId} |`)) {
                // Update existing line
                const regex = new RegExp(`\\| ${this.agentId.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')} \\|[^\\n]*`, 'g');
                content = content.replace(regex, agentLine);
            } else {
                // Add new line before the closing table
                const tableEnd = content.indexOf('| Agent 12 | 🟡 Pending | Awaiting task | - |');
                if (tableEnd !== -1) {
                    content = content.substring(0, tableEnd) + agentLine + '\n' + content.substring(tableEnd);
                }
            }
            
            fs.writeFileSync(coordFile, content);
        } catch (error) {
            console.error(`Failed to update agent status: ${error.message}`);
        }
    }

    // Query GraphRAG for resources
    async queryResources(topic, limit = 10) {
        try {
            const { data, error } = await supabase
                .from('resources')
                .select('*')
                .ilike('title', `%${topic}%`)
                .limit(limit);

            if (error) throw error;
            
            console.log(`📚 Found ${data.length} resources on "${topic}":`);
            data.forEach((resource, i) => {
                console.log(`  ${i+1}. ${resource.title} (${resource.type || 'unknown'})`);
            });
            
            return data;
        } catch (error) {
            console.error(`❌ Query failed: ${error.message}`);
            return [];
        }
    }

    // Find high cultural content
    async findHighCulturalContent(limit = 10) {
        try {
            const { data, error } = await supabase
                .from('resources')
                .select('*')
                .eq('cultural_level', 'high')
                .limit(limit);

            if (error) throw error;
            
            console.log(`🌱 Found ${data.length} high cultural resources:`);
            data.forEach((resource, i) => {
                console.log(`  ${i+1}. ${resource.title} (${resource.type || 'unknown'})`);
            });
            
            return data;
        } catch (error) {
            console.error(`❌ Query failed: ${error.message}`);
            return [];
        }
    }

    // Check if resource exists before creating
    async checkResourceExists(title) {
        try {
            const { data, error } = await supabase
                .from('resources')
                .select('*')
                .eq('title', title)
                .limit(1);

            if (error) throw error;
            
            return data.length > 0;
        } catch (error) {
            console.error(`❌ Check failed: ${error.message}`);
            return false;
        }
    }

    // Post a question to ACTIVE_QUESTIONS.md
    postQuestion(question) {
        try {
            const questionFile = path.join(__dirname, 'ACTIVE_QUESTIONS.md');
            const timestamp = new Date().toLocaleString();
            const entry = `\n### ${this.agentId} asks (${timestamp}):\n${question}\n\n`;
            
            fs.appendFileSync(questionFile, entry);
            console.log(`🤔 Question posted to ACTIVE_QUESTIONS.md`);
        } catch (error) {
            console.error(`❌ Failed to post question: ${error.message}`);
        }
    }

    // Get latest updates from team
    getTeamUpdates() {
        try {
            const logFile = path.join(__dirname, 'progress-log.md');
            const content = fs.readFileSync(logFile, 'utf8');
            const lines = content.split('\n');
            
            // Get last 20 lines
            const recentLines = lines.slice(-20);
            console.log(`📋 Recent team updates:`);
            recentLines.forEach(line => {
                if (line.trim()) console.log(`  ${line}`);
            });
            
            return recentLines;
        } catch (error) {
            console.error(`❌ Failed to get updates: ${error.message}`);
            return [];
        }
    }

    // Start collaboration session
    async startCollaboration(task) {
        console.log(`🚀 Starting MCP collaboration for ${this.agentId}`);
        
        // Check in
        await this.checkIn(task);
        
        // Get team updates
        this.getTeamUpdates();
        
        // Example query to GraphRAG
        console.log(`\n🧠 Example GraphRAG query for "${this.agentId}":`);
        await this.queryResources('māori', 3);
        
        console.log(`\n✅ ${this.agentId} is now connected and ready to collaborate!`);
        console.log(`\n📖 Available methods:`);
        console.log(`  - connector.queryResources(topic)`);
        console.log(`  - connector.findHighCulturalContent()`);
        console.log(`  - connector.checkResourceExists(title)`);
        console.log(`  - connector.postQuestion(question)`);
        console.log(`  - connector.getTeamUpdates()`);
        console.log(`  - connector.checkIn(task)`);
    }
}

// Auto-run if called directly
if (require.main === module) {
    const connector = new MCPAgentConnector(agentId);
    connector.startCollaboration('MCP connection established');
}

module.exports = MCPAgentConnector;

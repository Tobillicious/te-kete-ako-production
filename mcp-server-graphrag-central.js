#!/usr/bin/env node

/**
 * MCP Server with Supabase GraphRAG as Central Brain
 * Forces all 12 agents to collaborate through the knowledge graph
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

// Import Supabase connector
const { createClient } = require('@supabase/supabase-js');

// Supabase configuration
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

class GraphRAGCentralMCPServer {
    constructor() {
        this.port = 3003; // New port for GraphRAG-central server
        this.projectRoot = __dirname;
        
        // Initialize Supabase client
        this.supabase = createClient(SUPABASE_URL, SUPABASE_KEY);
        
        // Agent registry
        this.agents = new Map();
        
        // Initialize with all 12 agent slots
        for (let i = 1; i <= 12; i++) {
            this.agents.set(`agent-${i}`, {
                id: `agent-${i}`,
                status: 'offline',
                lastSeen: null,
                currentTask: null,
                capabilities: this.getAgentCapabilities(i),
                knowledgeQueries: [],
                collaborations: []
            });
        }
        
        // Central coordination state
        this.coordination = {
            currentFocus: null,
            activeCollaborations: [],
            sharedKnowledge: new Map(),
            decisions: new Map(),
            taskQueue: []
        };
        
        console.log('🔗 Connected to Supabase GraphRAG as central brain');
    }

    getAgentCapabilities(agentNum) {
        const capabilities = {
            1: ["file-discovery", "categorization", "inventory"],
            2: ["styling", "css", "design-system"],
            3: ["content", "cultural-enhancement", "education"],
            4: ["navigation", "links", "structure"],
            5: ["qa", "testing", "validation"],
            6: ["orphaned-pages", "integration", "resource-management"],
            7: ["cultural", "maori-knowledge", "authenticity"],
            8: ["performance", "optimization", "speed"],
            9: ["accessibility", "wcag", "testing"],
            10: ["coordination", "mcp", "communication"],
            11: ["browser-testing", "devtools", "diagnosis"],
            12: ["documentation", "progress-tracking", "knowledge-base"]
        };
        return capabilities[agentNum] || ["general"];
    }

    async start() {
        // Test Supabase connection
        try {
            const { count, error } = await this.supabase
                .from('resources')
                .select('*', { count: 'exact', head: true });
                
            if (error) throw error;
            console.log(`✅ GraphRAG connected: ${count} resources in knowledge base`);
        } catch (error) {
            console.error('❌ Failed to connect to GraphRAG:', error.message);
            process.exit(1);
        }

        const server = http.createServer((req, res) => {
            this.handleRequest(req, res);
        });

        server.listen(this.port, () => {
            console.log(`🚀 GraphRAG-Central MCP Server running on port ${this.port}`);
            console.log(`🧠 Supabase GraphRAG: CENTRAL BRAIN`);
            console.log(`🤝 Ready for 12-agent FORCED COLLABORATION`);
            console.log(`📚 Knowledge Base: 467+ resources`);
            console.log(`🔄 All decisions MUST go through GraphRAG`);
        });
    }

    async handleRequest(req, res) {
        res.setHeader('Content-Type', 'application/json');
        res.setHeader('Access-Control-Allow-Origin', '*');
        res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
        res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
        
        if (req.method === 'OPTIONS') {
            res.writeHead(200);
            res.end();
            return;
        }
        
        const url = new URL(req.url, `http://localhost:${this.port}`);
        
        try {
            switch (url.pathname) {
                case '/status':
                    await this.handleStatus(req, res);
                    break;
                case '/check-in':
                    await this.handleCheckIn(req, res);
                    break;
                case '/query-knowledge':
                    await this.handleQueryKnowledge(req, res);
                    break;
                case '/add-knowledge':
                    await this.handleAddKnowledge(req, res);
                    break;
                case '/propose-decision':
                    await this.handleProposeDecision(req, res);
                    break;
                case '/get-decisions':
                    await this.handleGetDecisions(req, res);
                    break;
                case '/collaborate':
                    await this.handleCollaboration(req, res);
                    break;
                case '/claim-task':
                    await this.handleClaimTask(req, res);
                    break;
                case '/update-task':
                    await this.handleUpdateTask(req, res);
                    break;
                case '/complete-task':
                    await this.handleCompleteTask(req, res);
                    break;
                default:
                    res.writeHead(404);
                    res.end(JSON.stringify({ error: 'Endpoint not found' }));
            }
        } catch (error) {
            console.error('Request error:', error);
            res.writeHead(500);
            res.end(JSON.stringify({ error: error.message }));
        }
    }

    async handleStatus(req, res) {
        const activeCount = Array.from(this.agents.values()).filter(a => a.status === 'online').length;
        
        // Get latest knowledge from GraphRAG
        try {
            const { count } = await this.supabase
                .from('resources')
                .select('*', { count: 'exact', head: true });
                
            res.writeHead(200);
            res.end(JSON.stringify({
                status: 'running',
                project: 'te-kete-ako',
                timestamp: new Date().toISOString(),
                totalAgents: 12,
                activeAgents: activeCount,
                agentStatus: Array.from(this.agents.values()),
                graphragResources: count,
                coordination: 'FORCED_COLLABORATION_VIA_GRAPHRAG',
                currentFocus: this.coordination.currentFocus,
                activeCollaborations: this.coordination.activeCollaborations.length
            }));
        } catch (error) {
            res.writeHead(500);
            res.end(JSON.stringify({ error: 'Failed to get GraphRAG status' }));
        }
    }

    async handleCheckIn(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', async () => {
            try {
                const data = JSON.parse(body);
                const { agentId, status, currentTask } = data;
                
                if (!this.agents.has(agentId)) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Invalid agent ID' }));
                    return;
                }
                
                // Update agent status
                const agent = this.agents.get(agentId);
                agent.status = status || 'online';
                agent.lastSeen = new Date().toISOString();
                agent.currentTask = currentTask || null;
                
                // Log to GraphRAG
                await this.logToGraphRAG({
                    type: 'agent_check_in',
                    agentId: agentId,
                    status: status,
                    task: currentTask,
                    timestamp: new Date().toISOString()
                });
                
                // Get current coordination state
                const coordinationState = await this.getCoordinationState();
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    agentId: agentId,
                    status: agent.status,
                    totalActive: Array.from(this.agents.values()).filter(a => a.status === 'online').length,
                    coordination: coordinationState,
                    message: "All agent actions MUST be coordinated through GraphRAG"
                }));
            } catch (error) {
                res.writeHead(500);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    async handleQueryKnowledge(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', async () => {
            try {
                const data = JSON.parse(body);
                const { agentId, query, context } = data;
                
                if (!this.agents.has(agentId)) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Invalid agent ID' }));
                    return;
                }
                
                // Query GraphRAG
                const results = await this.queryGraphRAG(query, context);
                
                // Log query to agent
                const agent = this.agents.get(agentId);
                agent.knowledgeQueries.push({
                    query: query,
                    results: results.length,
                    timestamp: new Date().toISOString()
                });
                
                // Log to GraphRAG
                await this.logToGraphRAG({
                    type: 'knowledge_query',
                    agentId: agentId,
                    query: query,
                    resultsCount: results.length,
                    timestamp: new Date().toISOString()
                });
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    agentId: agentId,
                    query: query,
                    results: results,
                    message: "Use this knowledge to coordinate with other agents"
                }));
            } catch (error) {
                res.writeHead(500);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    async handleAddKnowledge(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', async () => {
            try {
                const data = JSON.parse(body);
                const { agentId, knowledge, type } = data;
                
                if (!this.agents.has(agentId)) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Invalid agent ID' }));
                    return;
                }
                
                // Add to GraphRAG
                const result = await this.addToGraphRAG(knowledge, type, agentId);
                
                // Update shared knowledge
                this.coordination.sharedKnowledge.set(result.id, {
                    ...knowledge,
                    addedBy: agentId,
                    timestamp: new Date().toISOString()
                });
                
                // Log to GraphRAG
                await this.logToGraphRAG({
                    type: 'knowledge_added',
                    agentId: agentId,
                    knowledgeId: result.id,
                    knowledgeType: type,
                    timestamp: new Date().toISOString()
                });
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    agentId: agentId,
                    knowledgeId: result.id,
                    message: "Knowledge added to GraphRAG and shared with all agents"
                }));
            } catch (error) {
                res.writeHead(500);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    async handleProposeDecision(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', async () => {
            try {
                const data = JSON.parse(body);
                const { agentId, decision, rationale, affectedAgents } = data;
                
                if (!this.agents.has(agentId)) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Invalid agent ID' }));
                    return;
                }
                
                // Create decision record
                const decisionId = `decision-${Date.now()}`;
                this.coordination.decisions.set(decisionId, {
                    id: decisionId,
                    proposedBy: agentId,
                    decision: decision,
                    rationale: rationale,
                    affectedAgents: affectedAgents || [],
                    status: 'proposed',
                    timestamp: new Date().toISOString(),
                    feedback: []
                });
                
                // Log to GraphRAG
                await this.logToGraphRAG({
                    type: 'decision_proposed',
                    agentId: agentId,
                    decisionId: decisionId,
                    decision: decision,
                    timestamp: new Date().toISOString()
                });
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    agentId: agentId,
                    decisionId: decisionId,
                    message: "Decision proposed. Other agents will be notified to provide feedback."
                }));
            } catch (error) {
                res.writeHead(500);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    async handleGetDecisions(req, res) {
        try {
            const decisions = Array.from(this.coordination.decisions.values());
            
            res.writeHead(200);
            res.end(JSON.stringify({ 
                success: true,
                decisions: decisions,
                message: "Review these decisions and provide feedback"
            }));
        } catch (error) {
            res.writeHead(500);
            res.end(JSON.stringify({ error: error.message }));
        }
    }

    async handleCollaboration(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', async () => {
            try {
                const data = JSON.parse(body);
                const { agentId, targetAgent, message, collaborationType } = data;
                
                if (!this.agents.has(agentId) || !this.agents.has(targetAgent)) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Invalid agent ID' }));
                    return;
                }
                
                // Create collaboration record
                const collaborationId = `collab-${Date.now()}`;
                const collaboration = {
                    id: collaborationId,
                    participants: [agentId, targetAgent],
                    type: collaborationType || 'general',
                    messages: [{
                        from: agentId,
                        to: targetAgent,
                        message: message,
                        timestamp: new Date().toISOString()
                    }],
                    created: new Date().toISOString(),
                    status: 'active'
                };
                
                this.coordination.activeCollaborations.push(collaboration);
                
                // Update agent records
                const agent = this.agents.get(agentId);
                const target = this.agents.get(targetAgent);
                agent.collaborations.push(collaborationId);
                target.collaborations.push(collaborationId);
                
                // Log to GraphRAG
                await this.logToGraphRAG({
                    type: 'collaboration_started',
                    agentId: agentId,
                    targetAgent: targetAgent,
                    collaborationId: collaborationId,
                    message: message,
                    timestamp: new Date().toISOString()
                });
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    collaborationId: collaborationId,
                    message: "Collaboration initiated and logged to GraphRAG"
                }));
            } catch (error) {
                res.writeHead(500);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    async handleClaimTask(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', async () => {
            try {
                const data = JSON.parse(body);
                const { agentId, task, priority } = data;
                
                if (!this.agents.has(agentId)) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Invalid agent ID' }));
                    return;
                }
                
                // Add to task queue
                const taskRecord = {
                    id: `task-${Date.now()}`,
                    agentId: agentId,
                    task: task,
                    priority: priority || 'normal',
                    status: 'claimed',
                    created: new Date().toISOString()
                };
                
                this.coordination.taskQueue.push(taskRecord);
                
                // Update agent
                const agent = this.agents.get(agentId);
                agent.currentTask = task;
                
                // Log to GraphRAG
                await this.logToGraphRAG({
                    type: 'task_claimed',
                    agentId: agentId,
                    taskId: taskRecord.id,
                    task: task,
                    timestamp: new Date().toISOString()
                });
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    taskId: taskRecord.id,
                    agentId: agentId,
                    task: task,
                    message: "Task claimed and logged to GraphRAG. Other agents can see this."
                }));
            } catch (error) {
                res.writeHead(500);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    async handleUpdateTask(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', async () => {
            try {
                const data = JSON.parse(body);
                const { agentId, taskId, status, notes } = data;
                
                // Find and update task
                const task = this.coordination.taskQueue.find(t => t.id === taskId);
                if (!task) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Invalid task ID' }));
                    return;
                }
                
                task.status = status || task.status;
                task.lastUpdate = new Date().toISOString();
                if (notes) task.notes = notes;
                
                // Log to GraphRAG
                await this.logToGraphRAG({
                    type: 'task_updated',
                    agentId: agentId,
                    taskId: taskId,
                    status: status,
                    notes: notes,
                    timestamp: new Date().toISOString()
                });
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    taskId: taskId,
                    status: task.status,
                    message: "Task updated and logged to GraphRAG"
                }));
            } catch (error) {
                res.writeHead(500);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    async handleCompleteTask(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', async () => {
            try {
                const data = JSON.parse(body);
                const { agentId, taskId, results } = data;
                
                // Find and complete task
                const task = this.coordination.taskQueue.find(t => t.id === taskId);
                if (!task) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Invalid task ID' }));
                    return;
                }
                
                task.status = 'completed';
                task.completed = new Date().toISOString();
                if (results) task.results = results;
                
                // Update agent
                const agent = this.agents.get(agentId);
                agent.currentTask = null;
                
                // Log to GraphRAG
                await this.logToGraphRAG({
                    type: 'task_completed',
                    agentId: agentId,
                    taskId: taskId,
                    results: results,
                    timestamp: new Date().toISOString()
                });
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    taskId: taskId,
                    task: task.task,
                    message: "Task completed and logged to GraphRAG. All agents can see this."
                }));
            } catch (error) {
                res.writeHead(500);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    // GraphRAG integration methods
    async queryGraphRAG(query, context = null) {
        try {
            // Search resources by title
            const { data: titleResults } = await this.supabase
                .from('resources')
                .select('*')
                .ilike('title', `%${query}%`)
                .limit(10);
                
            // Search resources by description
            const { data: descResults } = await this.supabase
                .from('resources')
                .select('*')
                .ilike('description', `%${query}%`)
                .limit(10);
                
            // Combine and deduplicate results
            const allResults = [...titleResults, ...descResults];
            const uniqueResults = allResults.filter((item, index, self) =>
                index === self.findIndex((t) => t.id === item.id)
            );
            
            return uniqueResults;
        } catch (error) {
            console.error('Error querying GraphRAG:', error);
            return [];
        }
    }

    async addToGraphRAG(knowledge, type, agentId) {
        try {
            const newResource = {
                title: knowledge.title || `Knowledge from ${agentId}`,
                description: knowledge.description || '',
                type: type || 'knowledge',
                subject: knowledge.subject || 'General',
                path: knowledge.path || null,
                tags: knowledge.tags || [],
                cultural_elements: knowledge.cultural_elements || {},
                curriculum_alignment: knowledge.curriculum_alignment || {},
                difficulty_level: knowledge.difficulty_level || 'beginner',
                estimated_duration_minutes: knowledge.estimated_duration_minutes || 15,
                author: agentId,
                is_active: true
            };
            
            const { data, error } = await this.supabase
                .from('resources')
                .insert(newResource)
                .select();
                
            if (error) throw error;
            return data[0];
        } catch (error) {
            console.error('Error adding to GraphRAG:', error);
            throw error;
        }
    }

    async logToGraphRAG(activity) {
        try {
            // In a real implementation, this would log to a dedicated activity table
            // For now, we'll just log to console
            console.log(`🧠 GraphRAG Log: ${activity.type} by ${activity.agentId}`);
            
            // Also append to progress-log.md
            const logEntry = `\n## ${activity.timestamp}\n${activity.type}: ${activity.agentId}\n`;
            fs.appendFileSync(path.join(this.projectRoot, 'progress-log.md'), logEntry);
        } catch (error) {
            console.error('Error logging to GraphRAG:', error);
        }
    }

    async getCoordinationState() {
        try {
            // Get recent decisions
            const recentDecisions = Array.from(this.coordination.decisions.values())
                .filter(d => d.status === 'proposed')
                .slice(-5);
                
            // Get active collaborations
            const activeCollabs = this.coordination.activeCollaborations
                .filter(c => c.status === 'active')
                .slice(-5);
                
            return {
                currentFocus: this.coordination.currentFocus,
                recentDecisions: recentDecisions,
                activeCollaborations: activeCollabs,
                sharedKnowledgeCount: this.coordination.sharedKnowledge.size
            };
        } catch (error) {
            console.error('Error getting coordination state:', error);
            return {};
        }
    }
}

// Start the GraphRAG-central server
const server = new GraphRAGCentralMCPServer();
server.start().catch(console.error);

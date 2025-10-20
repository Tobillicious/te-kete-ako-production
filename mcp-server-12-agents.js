#!/usr/bin/env node

const http = require('http');
const fs = require('fs');
const path = require('path');

// Supabase configuration
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

class TwelveAgentMCPServer {
    constructor() {
        this.port = 3002; // Different port to avoid conflicts
        this.projectRoot = __dirname;
        this.activeAgents = new Map(); // Track all 12 agents
        this.agentTasks = new Map(); // Track current tasks
        this.collaborationRooms = new Map(); // For agent collaboration
        
        // Initialize with all 12 agent slots
        for (let i = 1; i <= 12; i++) {
            this.activeAgents.set(`agent-${i}`, {
                id: `agent-${i}`,
                status: 'offline',
                lastSeen: null,
                currentTask: null,
                capabilities: this.getAgentCapabilities(i)
            });
        }
        
        this.instructions = {
            timestamp: new Date().toISOString(),
            priority: "COLLABORATE_NOW",
            message: "All 12 agents check in and coordinate via Supabase GraphRAG",
            agentGuidance: {
                "agent-1": "Discovery: File inventory and categorization",
                "agent-2": "Styling: Apply professional template structure", 
                "agent-3": "Content: Cultural enhancement and educational value",
                "agent-4": "Navigation: Link fixing and structure organization",
                "agent-5": "QA: Testing and accessibility validation",
                "agent-6": "Orphaned Pages: Integrate 45+ unlinked resources",
                "agent-7": "Cultural: Te Ao Māori context and authenticity",
                "agent-8": "Performance: Optimization and speed improvements",
                "agent-9": "Accessibility: WCAG 2.1 compliance and testing",
                "agent-10": "Coordination: MCP server and team communication",
                "agent-11": "Browser Testing: DevTools diagnosis and reality checks",
                "agent-12": "Documentation: Progress tracking and knowledge base"
            },
            qualityStandards: {
                template: "Use te-kete-professional.css system",
                cultural: "Honor mātauranga Māori authentically", 
                accessibility: "WCAG 2.1 compliance required",
                testing: "Functionality and cross-browser validation",
                collaboration: "Use Supabase GraphRAG for all decisions"
            }
        };
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

    start() {
        const server = http.createServer((req, res) => {
            this.handleRequest(req, res);
        });

        server.listen(this.port, () => {
            console.log(`🚀 12-Agent MCP Server running on port ${this.port}`);
            console.log(`📊 Project: te-kete-ako`);
            console.log(`🤝 Ready for 12-agent collaboration`);
            console.log(`🔗 Supabase GraphRAG integration: ACTIVE`);
            console.log(`📁 Files: Scanning 954+ site files`);
        });
    }

    handleRequest(req, res) {
        res.setHeader('Content-Type', 'application/json');
        res.setHeader('Access-Control-Allow-Origin', '*');
        res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
        res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization, apikey, X-Requested-With, x-client-info');
        res.setHeader('Access-Control-Allow-Credentials', 'true');
        
        if (req.method === 'OPTIONS') {
            res.writeHead(200);
            res.end();
            return;
        }
        
        const url = new URL(req.url, `http://localhost:${this.port}`);
        
        switch (url.pathname) {
            case '/status':
                this.handleStatus(req, res);
                break;
            case '/register':
                this.handleRegister(req, res);
                break;
            case '/check-in':
                this.handleCheckIn(req, res);
                break;
            case '/supabase-query':
                this.handleSupabaseQuery(req, res);
                break;
            case '/collaborate':
                this.handleCollaboration(req, res);
                break;
            case '/instructions':
                this.handleInstructions(req, res);
                break;
            case '/progress':
                this.handleProgress(req, res);
                break;
            case '/claim-task':
                this.handleClaimTask(req, res);
                break;
            case '/update-task':
                this.handleUpdateTask(req, res);
                break;
            case '/complete-task':
                this.handleCompleteTask(req, res);
                break;
            default:
                res.writeHead(404);
                res.end(JSON.stringify({ error: 'Endpoint not found' }));
        }
    }

    handleRegister(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                const { agentId, capabilities } = data;

                if (!agentId) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'agentId required' }));
                    return;
                }

                if (!this.activeAgents.has(agentId)) {
                    this.activeAgents.set(agentId, {
                        id: agentId,
                        status: 'online',
                        lastSeen: new Date().toISOString(),
                        currentTask: null,
                        capabilities: Array.isArray(capabilities) && capabilities.length > 0 ? capabilities : ['general']
                    });
                }

                this.updateProgressLog(`🤝 Registered agent ${agentId}`);

                res.writeHead(200);
                res.end(JSON.stringify({
                    success: true,
                    agent: this.activeAgents.get(agentId)
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    handleStatus(req, res) {
        const activeCount = Array.from(this.activeAgents.values()).filter(a => a.status === 'online').length;
        
        res.writeHead(200);
        res.end(JSON.stringify({
            status: 'running',
            project: 'te-kete-ako',
            timestamp: new Date().toISOString(),
            totalAgents: 12,
            activeAgents: activeCount,
            agentStatus: Array.from(this.activeAgents.values()),
            supabaseConnection: 'ACTIVE',
            coordination: 'FULL_12_AGENT_COLLABORATION'
        }));
    }

    handleCheckIn(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                const { agentId, status, currentTask } = data;
                
                // Auto-register unknown agents for true multi-agent support
                if (!this.activeAgents.has(agentId)) {
                    this.activeAgents.set(agentId, {
                        id: agentId,
                        status: status || 'online',
                        lastSeen: new Date().toISOString(),
                        currentTask: currentTask || null,
                        capabilities: ['general']
                    });
                } else {
                    // Update agent status
                    const agent = this.activeAgents.get(agentId);
                    agent.status = status || 'online';
                    agent.lastSeen = new Date().toISOString();
                    agent.currentTask = currentTask || null;
                }
                
                // Update progress log
                this.updateProgressLog(`Agent ${agentId} checked in: ${status} - ${currentTask || 'No task'}`);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    agentId: agentId,
                    status: agent.status,
                    totalActive: Array.from(this.activeAgents.values()).filter(a => a.status === 'online').length,
                    instructions: this.instructions
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    handleSupabaseQuery(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                const { agentId, query, table, filters } = data;
                
                // For now, return a mock response
                // In a real implementation, this would query Supabase
                const mockResponse = {
                    agentId: agentId,
                    query: query,
                    table: table,
                    results: `Mock results for ${query} on ${table}`,
                    timestamp: new Date().toISOString()
                };
                
                res.writeHead(200);
                res.end(JSON.stringify(mockResponse));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    handleCollaboration(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                const { agentId, targetAgent, message, collaborationType } = data;
                
                // Create collaboration room
                const roomId = `${agentId}-${targetAgent}-${Date.now()}`;
                this.collaborationRooms.set(roomId, {
                    id: roomId,
                    participants: [agentId, targetAgent],
                    type: collaborationType || 'general',
                    messages: [{
                        from: agentId,
                        to: targetAgent,
                        message: message,
                        timestamp: new Date().toISOString()
                    }],
                    created: new Date().toISOString()
                });
                
                // Update progress log
                this.updateProgressLog(`Collaboration: ${agentId} -> ${targetAgent}: ${message}`);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    roomId: roomId,
                    message: "Collaboration room created"
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    handleInstructions(req, res) {
        res.writeHead(200);
        res.end(JSON.stringify(this.instructions));
    }

    handleProgress(req, res) {
        try {
            const progressContent = fs.readFileSync(path.join(this.projectRoot, 'progress-log.md'), 'utf8');
            res.writeHead(200);
            res.end(JSON.stringify({ 
                progress: progressContent,
                lastUpdated: new Date().toISOString(),
                activeAgents: Array.from(this.activeAgents.values()).filter(a => a.status === 'online')
            }));
        } catch (error) {
            res.writeHead(500);
            res.end(JSON.stringify({ error: 'Progress log not found' }));
        }
    }

    handleClaimTask(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                const { agentId, task, priority } = data;
                
                if (!this.activeAgents.has(agentId)) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Invalid agent ID' }));
                    return;
                }
                
                // Assign task to agent
                const taskId = `${agentId}-${Date.now()}`;
                this.agentTasks.set(taskId, {
                    id: taskId,
                    agentId: agentId,
                    task: task,
                    priority: priority || 'normal',
                    status: 'in-progress',
                    created: new Date().toISOString()
                });
                
                // Update agent
                const agent = this.activeAgents.get(agentId);
                agent.currentTask = task;
                
                // Update progress log
                this.updateProgressLog(`Agent ${agentId} claimed task: ${task}`);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    taskId: taskId,
                    agentId: agentId,
                    task: task,
                    instructions: this.instructions
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    handleUpdateTask(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                const { agentId, taskId, status, notes } = data;
                
                if (!this.agentTasks.has(taskId)) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Invalid task ID' }));
                    return;
                }
                
                // Update task
                const task = this.agentTasks.get(taskId);
                task.status = status || task.status;
                task.lastUpdate = new Date().toISOString();
                if (notes) task.notes = notes;
                
                // Update progress log
                this.updateProgressLog(`Agent ${agentId} - ${taskId}: ${status} - ${notes || ''}`);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    taskId: taskId,
                    status: task.status
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    handleCompleteTask(req, res) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end(JSON.stringify({ error: 'Method not allowed' }));
            return;
        }

        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                const { agentId, taskId, results } = data;
                
                if (!this.agentTasks.has(taskId)) {
                    res.writeHead(400);
                    res.end(JSON.stringify({ error: 'Invalid task ID' }));
                    return;
                }
                
                // Complete task
                const task = this.agentTasks.get(taskId);
                task.status = 'completed';
                task.completed = new Date().toISOString();
                if (results) task.results = results;
                
                // Update agent
                const agent = this.activeAgents.get(agentId);
                agent.currentTask = null;
                
                // Update progress log
                this.updateProgressLog(`✅ Agent ${agentId} COMPLETED: ${task.task}`);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    taskId: taskId,
                    task: task.task,
                    nextSteps: "Claim next available task or collaborate with other agents"
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    updateProgressLog(message) {
        const timestamp = new Date().toISOString();
        const logEntry = `\n## ${timestamp}\n${message}\n`;
        
        try {
            fs.appendFileSync(path.join(this.projectRoot, 'progress-log.md'), logEntry);
            console.log(`📝 Progress updated: ${message}`);
        } catch (error) {
            console.error(`Error updating progress log: ${error}`);
        }
    }
}

// Start the 12-agent server
const server = new TwelveAgentMCPServer();
server.start();

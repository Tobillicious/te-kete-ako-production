#!/usr/bin/env node

const http = require('http');
const fs = require('fs');
const path = require('path');

// Supabase configuration
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

class SupabaseMCPServer {
    constructor() {
        this.port = 3001;
        this.projectRoot = __dirname;
        this.activeAgents = new Map(); // Track active agents
        this.agentTasks = new Map(); // Track current tasks
        this.collaborationRooms = new Map(); // Track collaboration rooms
        
        // Initialize with 12 agent slots
        for (let i = 1; i <= 12; i++) {
            this.activeAgents.set(`agent-${i}`, {
                id: `agent-${i}`,
                status: 'available',
                lastSeen: null,
                currentTask: null,
                skills: this.getAgentSkills(i)
            });
        }
    }

    getAgentSkills(agentId) {
        const skills = {
            'agent-1': ['discovery', 'content-analysis', 'cultural-research'],
            'agent-2': ['styling', 'css', 'design-systems', 'ui/ux'],
            'agent-3': ['content-enhancement', 'cultural-integration', 'educational-value'],
            'agent-4': ['navigation', 'linking', 'structure', 'organization'],
            'agent-5': ['qa', 'testing', 'accessibility', 'validation'],
            'agent-6': ['performance', 'optimization', 'speed', 'efficiency'],
            'agent-7': ['cultural-authenticity', 'mātauranga-māori', 'te-reo'],
            'agent-8': ['curriculum-alignment', 'educational-standards', 'assessment'],
            'agent-9': ['integration', 'coordination', 'system-thinking'],
            'agent-10': ['orphaned-pages', 'content-recovery', 'linking'],
            'agent-11': ['data-analysis', 'metrics', 'insights'],
            'agent-12': ['deployment', 'automation', 'ci-cd']
        };
        
        return skills[agentId] || ['general'];
    }

    start() {
        const server = http.createServer((req, res) => {
            this.handleRequest(req, res);
        });

        server.listen(this.port, () => {
            console.log(`🚀 Supabase MCP Server running on port ${this.port}`);
            console.log(`📊 Project: te-kete-ako`);
            console.log(`🧠 Connected to Supabase GraphRAG`);
            console.log(`🤝 Ready for 12-agent collaboration`);
            console.log(`📁 954+ files ready for transformation`);
        });
    }

    async handleRequest(req, res) {
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
            case '/heartbeat':
                this.handleHeartbeat(req, res);
                break;
            case '/supabase-query':
                this.handleSupabaseQuery(req, res);
                break;
            case '/collaborate':
                this.handleCollaborate(req, res);
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
            case '/find-collaborators':
                this.handleFindCollaborators(req, res);
                break;
            case '/progress':
                this.handleProgress(req, res);
                break;
            default:
                res.writeHead(404);
                res.end(JSON.stringify({ error: 'Endpoint not found' }));
        }
    }

    handleStatus(req, res) {
        const activeCount = Array.from(this.activeAgents.values()).filter(a => a.status === 'active').length;
        
        res.writeHead(200);
        res.end(JSON.stringify({
            status: 'running',
            project: 'te-kete-ako',
            timestamp: new Date().toISOString(),
            agents: {
                total: 12,
                active: activeCount,
                available: 12 - activeCount
            },
            supabase: 'connected',
            coordination: 'active'
        }));
    }

    async handleRegister(req, res) {
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
                const { agentId, agentType, capabilities } = data;
                
                // Dynamically register unknown agents to support many concurrent agents
                if (!this.activeAgents.has(agentId)) {
                    this.activeAgents.set(agentId, {
                        id: agentId,
                        status: 'active',
                        lastSeen: new Date().toISOString(),
                        type: agentType,
                        capabilities: capabilities || [],
                        skills: capabilities || []
                    });
                } else {
                    const agent = this.activeAgents.get(agentId);
                    agent.status = 'active';
                    agent.lastSeen = new Date().toISOString();
                    agent.type = agentType;
                    agent.capabilities = capabilities;
                }
                
                console.log(`🤖 Agent ${agentId} registered (${agentType})`);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    agentId: agentId,
                    status: 'registered',
                    totalAgents: this.activeAgents.size
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    async handleHeartbeat(req, res) {
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
                const { agentId } = data;
                
                if (this.activeAgents.has(agentId)) {
                    const agent = this.activeAgents.get(agentId);
                    agent.lastSeen = new Date().toISOString();
                }
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    timestamp: new Date().toISOString()
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    async handleSupabaseQuery(req, res) {
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
                const { agentId, query, table, filters } = data;
                
                // Make request to Supabase
                const supabaseUrl = `${SUPABASE_URL}/rest/v1/${table}`;
                const url = new URL(supabaseUrl);
                
                // Add filters as query parameters
                if (filters) {
                    Object.entries(filters).forEach(([key, value]) => {
                        url.searchParams.set(key, value);
                    });
                }
                
                const response = await fetch(url, {
                    method: 'GET',
                    headers: {
                        'apikey': SUPABASE_KEY,
                        'Authorization': `Bearer ${SUPABASE_KEY}`,
                        'Content-Type': 'application/json'
                    }
                });
                
                const result = await response.json();
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    data: result,
                    count: result.length
                }));
            } catch (error) {
                console.error('Supabase query error:', error);
                res.writeHead(500);
                res.end(JSON.stringify({ error: 'Supabase query failed' }));
            }
        });
    }

    async handleCollaborate(req, res) {
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
                const { agentId, task, requiredSkills, message } = data;
                
                // Create collaboration room
                const roomId = `room-${Date.now()}`;
                this.collaborationRooms.set(roomId, {
                    id: roomId,
                    createdBy: agentId,
                    task: task,
                    requiredSkills: requiredSkills || [],
                    message: message,
                    participants: [agentId],
                    createdAt: new Date().toISOString()
                });
                
                // Find agents with required skills
                const availableAgents = Array.from(this.activeAgents.values())
                    .filter(a => a.status === 'active' && a.id !== agentId)
                    .filter(a => requiredSkills.some(skill => a.skills.includes(skill)))
                    .map(a => ({
                        id: a.id,
                        skills: a.skills
                    }));
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    roomId: roomId,
                    availableAgents: availableAgents,
                    message: 'Collaboration room created'
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
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

        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                const { agentId, task, priority } = data;
                
                // Update agent status
                const agent = this.activeAgents.get(agentId);
                if (agent) {
                    agent.currentTask = task;
                    agent.taskPriority = priority || 'medium';
                }
                
                // Track task
                const taskId = `task-${Date.now()}`;
                this.agentTasks.set(taskId, {
                    id: taskId,
                    agentId: agentId,
                    task: task,
                    priority: priority || 'medium',
                    status: 'in-progress',
                    createdAt: new Date().toISOString()
                });
                
                // Update progress log
                this.updateProgressLog(`Agent ${agentId} claimed task: ${task}`);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    taskId: taskId,
                    message: 'Task claimed successfully'
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
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

        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                const { agentId, taskId, status, notes } = data;
                
                // Update task
                if (this.agentTasks.has(taskId)) {
                    const task = this.agentTasks.get(taskId);
                    task.status = status;
                    task.notes = notes;
                    task.updatedAt = new Date().toISOString();
                }
                
                // Update progress log
                this.updateProgressLog(`Agent ${agentId} - ${taskId}: ${status} - ${notes || ''}`);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    message: 'Task updated successfully'
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
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

        req.on('end', () => {
            try {
                const data = JSON.parse(body);
                const { agentId, taskId, result } = data;
                
                // Update task
                if (this.agentTasks.has(taskId)) {
                    const task = this.agentTasks.get(taskId);
                    task.status = 'completed';
                    task.result = result;
                    task.completedAt = new Date().toISOString();
                }
                
                // Update agent status
                const agent = this.activeAgents.get(agentId);
                if (agent) {
                    agent.currentTask = null;
                }
                
                // Update progress log
                this.updateProgressLog(`✅ Agent ${agentId} COMPLETED: ${taskId} - ${result || ''}`);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    message: 'Task completed successfully',
                    nextSteps: "Claim next available task or collaborate with other agents"
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    async handleFindCollaborators(req, res) {
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
                const { agentId, requiredSkills, excludeSelf } = data;
                
                // Find agents with required skills
                let availableAgents = Array.from(this.activeAgents.values())
                    .filter(a => a.status === 'active');
                
                if (excludeSelf) {
                    availableAgents = availableAgents.filter(a => a.id !== agentId);
                }
                
                if (requiredSkills && requiredSkills.length > 0) {
                    availableAgents = availableAgents.filter(a => 
                        requiredSkills.some(skill => a.skills.includes(skill))
                    );
                }
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    collaborators: availableAgents.map(a => ({
                        id: a.id,
                        skills: a.skills,
                        currentTask: a.currentTask
                    }))
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    async handleProgress(req, res) {
        try {
            const progressContent = fs.readFileSync(path.join(this.projectRoot, 'progress-log.md'), 'utf8');
            
            // Get active tasks
            const activeTasks = Array.from(this.agentTasks.values())
                .filter(t => t.status === 'in-progress');
            
            // Get active agents
            const activeAgents = Array.from(this.activeAgents.values())
                .filter(a => a.status === 'active');
            
            res.writeHead(200);
            res.end(JSON.stringify({ 
                progress: progressContent,
                activeTasks: activeTasks,
                activeAgents: activeAgents,
                lastUpdated: new Date().toISOString()
            }));
        } catch (error) {
            res.writeHead(500);
            res.end(JSON.stringify({ error: 'Progress log not found' }));
        }
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

// Start the Supabase MCP server
const server = new SupabaseMCPServer();
server.start();

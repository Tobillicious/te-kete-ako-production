#!/usr/bin/env node

/**
 * ================================================================
 * MCP SERVER WITH SUPABASE GRAPHRAG INTEGRATION
 * ================================================================
 * 
 * Enables real-time collaboration between all 12 Te Kete Ako agents
 * through Supabase GraphRAG knowledge base
 * 
 * Features:
 * - Agent coordination and task assignment
 * - Knowledge base queries and updates
 * - Progress tracking and communication
 * - Resource discovery and linking
 * 
 * ================================================================
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const { createClient } = require('@supabase/supabase-js');

class SupabaseGraphRAGMCPServer {
    constructor() {
        this.port = 3001;
        this.projectRoot = __dirname;
        this.agents = new Map(); // Track active agents
        this.tasks = new Map(); // Track assigned tasks
        this.knowledgeCache = new Map(); // Cache frequent queries
        
        // Supabase configuration
        this.supabaseUrl = 'https://nlgldaqtubrlcqddppbq.supabase.co';
        this.supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';
        
        // Initialize Supabase client
        this.supabase = createClient(this.supabaseUrl, this.supabaseKey);
        
        // Agent coordination instructions
        this.instructions = {
            timestamp: new Date().toISOString(),
            priority: "COLLABORATE_VIA_GRAPHRAG",
            message: "All agents coordinate through Supabase GraphRAG knowledge base",
            agentGuidance: {
                agent1: "Cultural content specialist - Query GraphRAG for high cultural value resources",
                agent2: "Frontend styling - Use GraphRAG to find design patterns and components",
                agent3: "Content enhancement - Query GraphRAG for related concepts and resources",
                agent4: "Navigation specialist - Use GraphRAG to find related content for linking",
                agent5: "QA specialist - Query GraphRAG for quality standards and test cases",
                agent6: "Backend integration - Use GraphRAG for API and database schemas",
                agent7: "Mātauranga Māori expert - Query GraphRAG for cultural context and authenticity",
                agent8: "Accessibility specialist - Use GraphRAG for accessibility patterns and guidelines",
                agent9: "Performance optimizer - Query GraphRAG for optimization techniques",
                agent10: "Orphaned pages specialist - Use GraphRAG to find related content for integration",
                agent11: "Mobile responsiveness - Use GraphRAG for mobile patterns and components",
                agent12: "Content curator - Use GraphRAG to identify and organize high-value content"
            },
            collaborationProtocol: {
                checkIn: "Post status to progress-log.md",
                queryKnowledge: "Use GraphRAG before making decisions",
                shareFindings: "Update knowledge base with discoveries",
                coordinateTasks: "Assign and track tasks through MCP",
                resolveConflicts: "Use GraphRAG to find authoritative answers"
            }
        };
    }

    async start() {
        // Test Supabase connection
        try {
            const { count, error } = await this.supabase
                .from('resources')
                .select('*', { count: 'exact', head: true });
                
            if (error) {
                console.error('❌ Supabase connection failed:', error.message);
                process.exit(1);
            }
            
            console.log(`✅ Connected to Supabase GraphRAG: ${count} resources`);
        } catch (error) {
            console.error('❌ Failed to initialize Supabase:', error.message);
            process.exit(1);
        }

        const server = http.createServer((req, res) => {
            this.handleRequest(req, res);
        });

        server.listen(this.port, () => {
            console.log(`🚀 Supabase GraphRAG MCP Server running on port ${this.port}`);
            console.log(`📊 Project: te-kete-ako`);
            console.log(`🧠 Knowledge Base: Connected to Supabase GraphRAG`);
            console.log(`🤝 Ready for 12-agent collaboration`);
            console.log(`📋 Instructions: Available at /instructions`);
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
        const path = url.pathname;
        
        try {
            if (path === '/status') {
                await this.handleStatus(req, res);
            } else if (path === '/instructions') {
                this.handleInstructions(req, res);
            } else if (path === '/agent/checkin') {
                await this.handleAgentCheckin(req, res);
            } else if (path === '/agent/status') {
                await this.handleAgentStatus(req, res);
            } else if (path === '/graphrag/query') {
                await this.handleGraphRAGQuery(req, res);
            } else if (path === '/graphrag/resources') {
                await this.handleGraphRAGResources(req, res);
            } else if (path === '/tasks/assign') {
                await this.handleTaskAssign(req, res);
            } else if (path === '/tasks/update') {
                await this.handleTaskUpdate(req, res);
            } else if (path === '/collaboration/progress') {
                await this.handleCollaborationProgress(req, res);
            } else {
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
        const activeAgents = Array.from(this.agents.values());
        const activeTasks = Array.from(this.tasks.values());
        
        res.writeHead(200);
        res.end(JSON.stringify({
            status: 'running',
            project: 'te-kete-ako',
            supabase: 'connected',
            agents: {
                total: 12,
                active: activeAgents.length,
                list: activeAgents
            },
            tasks: {
                total: activeTasks.length,
                pending: activeTasks.filter(t => t.status === 'pending').length,
                inProgress: activeTasks.filter(t => t.status === 'in_progress').length,
                completed: activeTasks.filter(t => t.status === 'completed').length
            },
            timestamp: new Date().toISOString()
        }));
    }

    handleInstructions(req, res) {
        res.writeHead(200);
        res.end(JSON.stringify(this.instructions));
    }

    async handleAgentCheckin(req, res) {
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', async () => {
            try {
                const data = JSON.parse(body);
                const agentId = data.agentId;
                const agentInfo = {
                    id: agentId,
                    name: data.name || agentId,
                    specialty: data.specialty || 'general',
                    status: data.status || 'active',
                    lastSeen: new Date().toISOString(),
                    currentTask: data.currentTask || null
                };
                
                this.agents.set(agentId, agentInfo);
                
                // Log to progress-log.md
                const logEntry = `[${new Date().toLocaleTimeString()}] Agent ${agentId}: Checked in - ${agentInfo.specialty}\n`;
                fs.appendFileSync(path.join(this.projectRoot, 'progress-log.md'), logEntry);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true, 
                    message: 'Agent checked in',
                    agent: agentInfo
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    async handleAgentStatus(req, res) {
        const agents = Array.from(this.agents.values());
        res.writeHead(200);
        res.end(JSON.stringify({ agents }));
    }

    async handleGraphRAGQuery(req, res) {
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', async () => {
            try {
                const { query, type = 'resources', limit = 10 } = JSON.parse(body);
                
                // Check cache first
                const cacheKey = `${type}:${query}:${limit}`;
                if (this.knowledgeCache.has(cacheKey)) {
                    const cached = this.knowledgeCache.get(cacheKey);
                    if (Date.now() - cached.timestamp < 60000) { // 1 minute cache
                        res.writeHead(200);
                        res.end(JSON.stringify({ 
                            ...cached.data,
                            cached: true
                        }));
                        return;
                    }
                }
                
                let result;
                
                if (type === 'resources') {
                    // Search resources by title or content
                    result = await this.supabase
                        .from('resources')
                        .select('*')
                        .or(`title.ilike.%${query}%,content.ilike.%${query}%`)
                        .limit(limit);
                } else if (type === 'concepts') {
                    // Search by concept
                    result = await this.supabase
                        .from('resource_concepts')
                        .select('*, resources(*)')
                        .ilike('concept_name', `%${query}%`)
                        .limit(limit);
                } else if (type === 'cultural') {
                    // Search high cultural value content
                    result = await this.supabase
                        .from('resources')
                        .select('*')
                        .eq('cultural_level', 'high')
                        .or(`title.ilike.%${query}%,content.ilike.%${query}%`)
                        .limit(limit);
                }
                
                // Cache the result
                this.knowledgeCache.set(cacheKey, {
                    data: result,
                    timestamp: Date.now()
                });
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    ...result,
                    cached: false
                }));
            } catch (error) {
                res.writeHead(500);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    async handleGraphRAGResources(req, res) {
        try {
            const { type, limit = 20 } = new URL(req.url, `http://localhost:${this.port}`);
            
            let result;
            
            if (type === 'high_cultural') {
                result = await this.supabase
                    .from('resources')
                    .select('*')
                    .eq('cultural_level', 'high')
                    .limit(limit);
            } else if (type === 'recent') {
                result = await this.supabase
                    .from('resources')
                    .select('*')
                    .order('created_at', { ascending: false })
                    .limit(limit);
            } else {
                // Default: all resources
                result = await this.supabase
                    .from('resources')
                    .select('*')
                    .limit(limit);
            }
            
            res.writeHead(200);
            res.end(JSON.stringify(result));
        } catch (error) {
            res.writeHead(500);
            res.end(JSON.stringify({ error: error.message }));
        }
    }

    async handleTaskAssign(req, res) {
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', async () => {
            try {
                const taskData = JSON.parse(body);
                const taskId = `task_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
                
                const task = {
                    id: taskId,
                    title: taskData.title,
                    description: taskData.description,
                    assignedTo: taskData.assignedTo || null,
                    status: 'pending',
                    priority: taskData.priority || 'medium',
                    createdAt: new Date().toISOString(),
                    dependencies: taskData.dependencies || []
                };
                
                this.tasks.set(taskId, task);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true, 
                    task: task
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    async handleTaskUpdate(req, res) {
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', async () => {
            try {
                const { taskId, updates } = JSON.parse(body);
                
                if (!this.tasks.has(taskId)) {
                    res.writeHead(404);
                    res.end(JSON.stringify({ error: 'Task not found' }));
                    return;
                }
                
                const task = this.tasks.get(taskId);
                Object.assign(task, updates, {
                    updatedAt: new Date().toISOString()
                });
                
                this.tasks.set(taskId, task);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true, 
                    task: task
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: error.message }));
            }
        });
    }

    async handleCollaborationProgress(req, res) {
        try {
            // Read progress-log.md
            const progressLogPath = path.join(this.projectRoot, 'progress-log.md');
            const progressLog = fs.existsSync(progressLogPath) 
                ? fs.readFileSync(progressLogPath, 'utf8')
                : '';
            
            // Get recent entries (last 50 lines)
            const lines = progressLog.split('\n');
            const recentEntries = lines.slice(-50);
            
            // Get active agents and tasks
            const activeAgents = Array.from(this.agents.values());
            const activeTasks = Array.from(this.tasks.values());
            
            res.writeHead(200);
            res.end(JSON.stringify({
                progressLog: recentEntries,
                agents: activeAgents,
                tasks: activeTasks,
                timestamp: new Date().toISOString()
            }));
        } catch (error) {
            res.writeHead(500);
            res.end(JSON.stringify({ error: error.message }));
        }
    }
}

// Start the server
const server = new SupabaseGraphRAGMCPServer();
server.start().catch(console.error);

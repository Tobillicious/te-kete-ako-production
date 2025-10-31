#!/usr/bin/env node
/**
 * Te Kete Ako - Custom MCP Server for Agent Coordination
 * Enables real-time bidirectional communication between agents
 * Port: 5000
 */

const http = require('http');
const { createClient } = require('@supabase/supabase-js');
require('dotenv').config();

// Initialize Supabase
const supabase = createClient(
    process.env.SUPABASE_URL || 'https://nlgldaqtubrlcqddppbq.supabase.co',
    process.env.SUPABASE_SERVICE_KEY || process.env.SUPABASE_ANON_KEY
);

// Agent coordination state
const activeAgents = new Map();
const messageQueue = [];

// MCP Server Implementation
class MCPServer {
    constructor(port = 3002) {
        this.port = port;
        this.server = null;
    }

    async start() {
        this.server = http.createServer(async (req, res) => {
            // Enable CORS
            res.setHeader('Access-Control-Allow-Origin', '*');
            res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
            res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
            res.setHeader('Content-Type', 'application/json');

            if (req.method === 'OPTIONS') {
                res.writeHead(200);
                res.end();
                return;
            }

            const url = new URL(req.url, `http://localhost:${this.port}`);
            const path = url.pathname;

            try {
                // Route handlers
                if (path === '/health') {
                    await this.handleHealth(req, res);
                } else if (path === '/agents/register') {
                    await this.handleRegister(req, res);
                } else if (path === '/agents/active') {
                    await this.handleActiveAgents(req, res);
                } else if (path === '/messages/send') {
                    await this.handleSendMessage(req, res);
                } else if (path === '/messages/receive') {
                    await this.handleReceiveMessages(req, res);
                } else if (path === '/graphrag/query') {
                    await this.handleGraphRAGQuery(req, res);
                } else if (path === '/graphrag/update') {
                    await this.handleGraphRAGUpdate(req, res);
                } else if (path === '/coordination/status') {
                    await this.handleCoordinationStatus(req, res);
                } else {
                    res.writeHead(404);
                    res.end(JSON.stringify({ error: 'Not Found' }));
                }
            } catch (error) {
                console.error('Error handling request:', error);
                res.writeHead(500);
                res.end(JSON.stringify({ error: error.message }));
            }
        });

        this.server.listen(this.port, () => {
            console.log('🎉 Te Kete Ako MCP Server Started!');
            console.log(`📡 Listening on http://localhost:${this.port}`);
            console.log('✅ Ready for agent coordination');
            console.log('');
            console.log('Available endpoints:');
            console.log('  GET  /health - Server health check');
            console.log('  POST /agents/register - Register agent');
            console.log('  GET  /agents/active - List active agents');
            console.log('  POST /messages/send - Send message to agent(s)');
            console.log('  GET  /messages/receive?agent=NAME - Receive messages');
            console.log('  POST /graphrag/query - Query GraphRAG');
            console.log('  POST /graphrag/update - Update GraphRAG');
            console.log('  GET  /coordination/status - Current coordination state');
        });
    }

    // Health check endpoint
    async handleHealth(req, res) {
        const health = {
            status: 'healthy',
            timestamp: new Date().toISOString(),
            uptime: process.uptime(),
            activeAgents: activeAgents.size,
            pendingMessages: messageQueue.length,
            supabase: 'connected'
        };

        // Test Supabase connection
        try {
            const { data, error } = await supabase
                .from('graphrag_resources')
                .select('id')
                .limit(1);
            
            if (error) health.supabase = 'error: ' + error.message;
        } catch (err) {
            health.supabase = 'disconnected';
        }

        res.writeHead(200);
        res.end(JSON.stringify(health, null, 2));
    }

    // Register agent
    async handleRegister(req, res) {
        const body = await this.readBody(req);
        const { agentName, agentType, capabilities } = JSON.parse(body);

        const agentInfo = {
            name: agentName,
            type: agentType,
            capabilities: capabilities || [],
            registeredAt: new Date().toISOString(),
            lastSeen: new Date().toISOString()
        };

        activeAgents.set(agentName, agentInfo);

        console.log(`✅ Agent registered: ${agentName} (${agentType})`);

        // Log to Supabase
        await supabase.from('graphrag_resources').insert({
            file_path: `/coordination/agent-activity/${agentName}-${Date.now()}`,
            resource_type: 'agent_activity',
            title: `${agentName} Connected`,
            metadata: {
                event: 'agent_registered',
                agent: agentName,
                type: agentType,
                capabilities,
                timestamp: new Date().toISOString()
            },
            subject: 'Platform Infrastructure',
            year_level: 'All',
            quality_score: 100,
            archive_status: 'active'
        });

        res.writeHead(200);
        res.end(JSON.stringify({ success: true, agent: agentInfo }));
    }

    // Get active agents
    async handleActiveAgents(req, res) {
        const agents = Array.from(activeAgents.values());
        res.writeHead(200);
        res.end(JSON.stringify({ agents, count: agents.length }));
    }

    // Send message to agent(s)
    async handleSendMessage(req, res) {
        const body = await this.readBody(req);
        const { from, to, message, priority, metadata } = JSON.parse(body);

        const msg = {
            id: Date.now(),
            from,
            to, // Can be array or single agent name
            message,
            priority: priority || 'normal',
            metadata: metadata || {},
            timestamp: new Date().toISOString(),
            read: false
        };

        messageQueue.push(msg);

        // Also persist to Supabase for durability
        await supabase.from('graphrag_resources').insert({
            file_path: `/coordination/messages/${from}-to-${to}-${msg.id}`,
            resource_type: 'agent_message',
            title: `${from} → ${to}`,
            metadata: {
                from,
                to,
                message,
                priority,
                ...metadata,
                message_id: msg.id,
                timestamp: msg.timestamp
            },
            subject: 'Platform Infrastructure',
            year_level: 'All',
            quality_score: 100,
            archive_status: 'active'
        });

        console.log(`📨 Message from ${from} to ${to}: ${message.substring(0, 60)}...`);

        res.writeHead(200);
        res.end(JSON.stringify({ success: true, messageId: msg.id }));
    }

    // Receive messages for an agent
    async handleReceiveMessages(req, res) {
        const url = new URL(req.url, `http://localhost:${this.port}`);
        const agentName = url.searchParams.get('agent');
        const since = url.searchParams.get('since'); // Timestamp

        if (!agentName) {
            res.writeHead(400);
            res.end(JSON.stringify({ error: 'agent parameter required' }));
            return;
        }

        // Get messages from queue
        const messages = messageQueue.filter(msg => {
            const isForMe = msg.to === agentName || (Array.isArray(msg.to) && msg.to.includes(agentName));
            const isNew = !since || new Date(msg.timestamp) > new Date(since);
            return isForMe && isNew;
        });

        // Mark as read
        messages.forEach(msg => msg.read = true);

        res.writeHead(200);
        res.end(JSON.stringify({ messages, count: messages.length }));
    }

    // Query GraphRAG
    async handleGraphRAGQuery(req, res) {
        const body = await this.readBody(req);
        const { query, limit } = JSON.parse(body);

        const { data, error } = await supabase
            .from('graphrag_resources')
            .select('*')
            .ilike('title', `%${query}%`)
            .limit(limit || 10);

        if (error) {
            res.writeHead(500);
            res.end(JSON.stringify({ error: error.message }));
            return;
        }

        res.writeHead(200);
        res.end(JSON.stringify({ results: data, count: data.length }));
    }

    // Update GraphRAG
    async handleGraphRAGUpdate(req, res) {
        const body = await this.readBody(req);
        const { resource, relationships } = JSON.parse(body);

        const results = {};

        // Insert resource
        if (resource) {
            const { data, error } = await supabase
                .from('graphrag_resources')
                .insert(resource)
                .select()
                .single();
            
            if (error) {
                res.writeHead(500);
                res.end(JSON.stringify({ error: error.message }));
                return;
            }
            results.resource = data;
        }

        // Insert relationships
        if (relationships && relationships.length > 0) {
            const { data, error } = await supabase
                .from('graphrag_relationships')
                .insert(relationships)
                .select();
            
            if (error) {
                console.error('Relationship insert error:', error);
            } else {
                results.relationships = data;
            }
        }

        res.writeHead(200);
        res.end(JSON.stringify({ success: true, results }));
    }

    // Get coordination status
    async handleCoordinationStatus(req, res) {
        const status = {
            timestamp: new Date().toISOString(),
            activeAgents: Array.from(activeAgents.values()),
            pendingMessages: messageQueue.filter(m => !m.read).length,
            totalMessages: messageQueue.length,
            server: 'running',
            uptime: process.uptime()
        };

        // Get recent coordination messages from Supabase
        const { data } = await supabase
            .from('graphrag_resources')
            .select('title, metadata, created_at')
            .eq('resource_type', 'agent_coordination')
            .order('created_at', { ascending: false })
            .limit(5);

        status.recentCoordination = data || [];

        res.writeHead(200);
        res.end(JSON.stringify(status, null, 2));
    }

    // Helper to read request body
    readBody(req) {
        return new Promise((resolve, reject) => {
            let body = '';
            req.on('data', chunk => body += chunk.toString());
            req.on('end', () => resolve(body));
            req.on('error', reject);
        });
    }
}

// Start server
const server = new MCPServer(3002);
server.start();

// Graceful shutdown
process.on('SIGINT', () => {
    console.log('\n🛑 Shutting down MCP server...');
    process.exit(0);
});

process.on('SIGTERM', () => {
    console.log('\n🛑 Shutting down MCP server...');
    process.exit(0);
});


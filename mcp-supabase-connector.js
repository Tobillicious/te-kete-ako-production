#!/usr/bin/env node

/**
 * ================================================================
 * UNIFIED SUPABASE GRAPHRAG CONNECTOR FOR TE KETE AKO AGENTS
 * ================================================================
 * 
 * Provides a unified interface for all 12 agents to access the
 * Supabase GraphRAG knowledge base through the MCP server
 * 
 * Usage: node mcp-supabase-connector.js
 * 
 * ================================================================
 */

const { createClient } = require('@supabase/supabase-js');
const http = require('http');
const fs = require('fs');
const path = require('path');

class SupabaseGraphRAGConnector {
    constructor() {
        // Supabase configuration
        this.supabaseUrl = 'https://nlgldaqtubrlcqddppbq.supabase.co';
        this.supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';
        
        // Initialize Supabase client
        this.supabase = createClient(this.supabaseUrl, this.supabaseKey);
        
        // MCP server port
        this.port = 3002;
        
        // Agent registry
        this.agents = new Map();
        
        // Cache for frequent queries
        this.cache = new Map();
        this.cacheTimeout = 5 * 60 * 1000; // 5 minutes
    }
    
    start() {
        const server = http.createServer((req, res) => {
            this.handleRequest(req, res);
        });
        
        server.listen(this.port, () => {
            console.log(`🔗 Supabase GraphRAG Connector running on port ${this.port}`);
            console.log(`📊 Connected to: ${this.supabaseUrl}`);
            console.log(`🤝 Ready for all 12 agents to access GraphRAG knowledge base`);
        });
    }
    
    handleRequest(req, res) {
        res.setHeader('Content-Type', 'application/json');
        res.setHeader('Access-Control-Allow-Origin', '*');
        res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
        res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Agent-ID');
        
        if (req.method === 'OPTIONS') {
            res.writeHead(200);
            res.end();
            return;
        }
        
        const url = new URL(req.url, `http://localhost:${this.port}`);
        const agentId = req.headers['agent-id'] || 'unknown';
        
        // Register agent if provided
        if (agentId !== 'unknown') {
            this.registerAgent(agentId);
        }
        
        if (req.method === 'GET' && url.pathname === '/status') {
            this.handleStatus(req, res);
        } else if (req.method === 'GET' && url.pathname === '/resources') {
            this.handleResources(req, res, url);
        } else if (req.method === 'GET' && url.pathname === '/concepts') {
            this.handleConcepts(req, res, url);
        } else if (req.method === 'GET' && url.pathname === '/agents') {
            this.handleAgents(req, res);
        } else if (req.method === 'POST' && url.pathname === '/query') {
            this.handleQuery(req, res);
        } else {
            res.writeHead(404);
            res.end(JSON.stringify({ error: 'Endpoint not found' }));
        }
    }
    
    async handleStatus(req, res) {
        try {
            // Test Supabase connection
            const { count, error } = await this.supabase
                .from('resources')
                .select('*', { count: 'exact', head: true });
            
            if (error) throw error;
            
            res.writeHead(200);
            res.end(JSON.stringify({
                status: 'connected',
                supabase: this.supabaseUrl,
                resources: count,
                agents: Array.from(this.agents.keys()),
                timestamp: new Date().toISOString()
            }));
        } catch (error) {
            res.writeHead(500);
            res.end(JSON.stringify({
                status: 'error',
                message: error.message
            }));
        }
    }
    
    async handleResources(req, res, url) {
        try {
            const limit = parseInt(url.searchParams.get('limit')) || 20;
            const offset = parseInt(url.searchParams.get('offset')) || 0;
            const cultural = url.searchParams.get('cultural');
            const type = url.searchParams.get('type');
            const search = url.searchParams.get('search');
            
            let query = this.supabase
                .from('resources')
                .select('*')
                .range(offset, offset + limit - 1);
            
            if (cultural) {
                query = query.eq('cultural_level', cultural);
            }
            
            if (type) {
                query = query.eq('type', type);
            }
            
            if (search) {
                query = query.ilike('title', `%${search}%`);
            }
            
            const { data, error } = await query;
            
            if (error) throw error;
            
            res.writeHead(200);
            res.end(JSON.stringify({
                resources: data,
                count: data.length,
                offset,
                limit
            }));
        } catch (error) {
            res.writeHead(500);
            res.end(JSON.stringify({
                error: error.message
            }));
        }
    }
    
    async handleConcepts(req, res, url) {
        try {
            const concept = url.searchParams.get('name');
            
            if (!concept) {
                // Get all concepts
                const { data, error } = await this.supabase
                    .from('resource_concepts')
                    .select('concept_name')
                    .limit(100);
                
                if (error) throw error;
                
                const concepts = [...new Set(data.map(item => item.concept_name))];
                
                res.writeHead(200);
                res.end(JSON.stringify({ concepts }));
                return;
            }
            
            // Get resources for specific concept
            const { data, error } = await this.supabase
                .from('resource_concepts')
                .select('*, resources(*)')
                .eq('concept_name', concept);
            
            if (error) throw error;
            
            res.writeHead(200);
            res.end(JSON.stringify({
                concept,
                resources: data.map(item => item.resources).filter(Boolean)
            }));
        } catch (error) {
            res.writeHead(500);
            res.end(JSON.stringify({
                error: error.message
            }));
        }
    }
    
    handleAgents(req, res) {
        res.writeHead(200);
        res.end(JSON.stringify({
            agents: Array.from(this.agents.entries()).map(([id, info]) => ({
                id,
                ...info
            })),
            count: this.agents.size
        }));
    }
    
    async handleQuery(req, res) {
        try {
            let body = '';
            req.on('data', chunk => {
                body += chunk.toString();
            });
            
            req.on('end', async () => {
                const { query, type } = JSON.parse(body);
                
                // Check cache first
                const cacheKey = `${type}:${query}`;
                if (this.cache.has(cacheKey)) {
                    const cached = this.cache.get(cacheKey);
                    if (Date.now() - cached.timestamp < this.cacheTimeout) {
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
                    const { data, error } = await this.supabase
                        .from('resources')
                        .select('*')
                        .ilike('title', `%${query}%`)
                        .limit(20);
                    
                    if (error) throw error;
                    result = { resources: data };
                } else if (type === 'concepts') {
                    const { data, error } = await this.supabase
                        .from('resource_concepts')
                        .select('*, resources(*)')
                        .ilike('concept_name', `%${query}%`)
                        .limit(20);
                    
                    if (error) throw error;
                    result = { 
                        concept: query,
                        resources: data.map(item => item.resources).filter(Boolean)
                    };
                } else {
                    // Default search across both
                    const [resourcesResult, conceptsResult] = await Promise.all([
                        this.supabase
                            .from('resources')
                            .select('*')
                            .ilike('title', `%${query}%`)
                            .limit(10),
                        this.supabase
                            .from('resource_concepts')
                            .select('*, resources(*)')
                            .ilike('concept_name', `%${query}%`)
                            .limit(10)
                    ]);
                    
                    result = {
                        resources: resourcesResult.data,
                        concepts: conceptsResult.data.map(item => item.resources).filter(Boolean)
                    };
                }
                
                // Cache result
                this.cache.set(cacheKey, {
                    data: result,
                    timestamp: Date.now()
                });
                
                res.writeHead(200);
                res.end(JSON.stringify(result));
            });
        } catch (error) {
            res.writeHead(500);
            res.end(JSON.stringify({
                error: error.message
            }));
        }
    }
    
    registerAgent(agentId) {
        if (!this.agents.has(agentId)) {
            console.log(`🤝 Agent ${agentId} connected to GraphRAG`);
        }
        
        this.agents.set(agentId, {
            id: agentId,
            lastSeen: new Date().toISOString(),
            requests: (this.agents.get(agentId)?.requests || 0) + 1
        });
    }
}

// Start the connector
const connector = new SupabaseGraphRAGConnector();
connector.start();

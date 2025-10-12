#!/usr/bin/env node

const http = require('http');
const fs = require('fs');
const path = require('path');

class EnhancedMCPServer {
    constructor() {
        this.port = 3001;
        this.projectRoot = __dirname;
        this.instructions = {
            timestamp: new Date().toISOString(),
            priority: "START_MISSION",
            message: "All agents check in and claim first available page",
            agentGuidance: {
                agent1: "Focus on file discovery and categorization",
                agent2: "Apply professional styling to first page",
                agent3: "Enhance cultural content on completed styling",
                agent4: "Fix navigation and links after content enhancement",
                agent5: "QA test completed pages before marking done"
            },
            qualityStandards: {
                template: "Use te-kete-professional.css system",
                cultural: "Honor mātauranga Māori authentically",
                accessibility: "WCAG 2.1 compliance required",
                testing: "Functionality and cross-browser validation"
            }
        };
    }

    start() {
        const server = http.createServer((req, res) => {
            this.handleRequest(req, res);
        });

        server.listen(this.port, () => {
            console.log(`🚀 Enhanced MCP Server running on port ${this.port}`);
            console.log(`📊 Project: te-kete-ako`);
            console.log(`📁 Files: Scanning 954+ site files`);
            console.log(`🤝 Ready for collaborative agent coordination`);
        });
    }

    handleRequest(req, res) {
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
        
        switch (url.pathname) {
            case '/status':
                this.handleStatus(req, res);
                break;
            case '/files':
                this.listFiles(req, res);
                break;
            case '/instructions':
                this.handleInstructions(req, res);
                break;
            case '/progress':
                this.handleProgress(req, res);
                break;
            case '/claim-page':
                this.handleClaimPage(req, res);
                break;
            case '/update-progress':
                this.handleUpdateProgress(req, res);
                break;
            case '/complete-page':
                this.handleCompletePage(req, res);
                break;
            default:
                res.writeHead(404);
                res.end(JSON.stringify({ error: 'Endpoint not found' }));
        }
    }

    handleStatus(req, res) {
        res.writeHead(200);
        res.end(JSON.stringify({
            status: 'running',
            project: 'te-kete-ako',
            timestamp: new Date().toISOString(),
            agents: 5,
            files: '954+',
            coordination: 'active'
        }));
    }

    handleFiles(req, res) {
        const publicDir = path.join(this.projectRoot, 'public');
        const files = this.scanDirectory(publicDir, 'public');
        
        res.writeHead(200);
        res.end(JSON.stringify({ 
            files: files,
            total: files.length,
            categories: this.categorizeFiles(files)
        }));
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
                lastUpdated: new Date().toISOString()
            }));
        } catch (error) {
            res.writeHead(500);
            res.end(JSON.stringify({ error: 'Progress log not found' }));
        }
    }

    handleClaimPage(req, res) {
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
                const { agent, page } = data;
                
                // Update progress log with page claim
                this.updateProgressLog(`Agent ${agent} claimed page: ${page}`);
                
                // Update instructions for coordination
                this.instructions.timestamp = new Date().toISOString();
                this.instructions.message = `Agent ${agent} working on ${page}`;
                this.instructions.currentWork = { agent, page, status: 'in-progress' };
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    claimed: page,
                    agent: agent,
                    instructions: this.instructions
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    handleUpdateProgress(req, res) {
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
                const { agent, page, status, notes } = data;
                
                // Update progress log
                this.updateProgressLog(`Agent ${agent} - ${page}: ${status} - ${notes || ''}`);
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    updated: true
                }));
            } catch (error) {
                res.writeHead(400);
                res.end(JSON.stringify({ error: 'Invalid request data' }));
            }
        });
    }

    handleCompletePage(req, res) {
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
                const { agent, page } = data;
                
                // Update progress log
                this.updateProgressLog(`✅ Agent ${agent} COMPLETED: ${page}`);
                
                // Update instructions for next steps
                this.instructions.timestamp = new Date().toISOString();
                this.instructions.message = `Page ${page} completed by Agent ${agent}`;
                this.instructions.completedWork = { agent, page, timestamp: new Date().toISOString() };
                
                res.writeHead(200);
                res.end(JSON.stringify({ 
                    success: true,
                    completed: page,
                    agent: agent,
                    nextSteps: "Claim next available page or assist other agents"
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

    scanDirectory(dir, prefix) {
        const files = [];
        
        try {
            const items = fs.readdirSync(dir);
            
            for (const item of items) {
                const fullPath = path.join(dir, item);
                const relativePath = path.join(prefix, item);
                const stat = fs.statSync(fullPath);
                
                if (stat.isDirectory()) {
                    files.push(...this.scanDirectory(fullPath, relativePath));
                } else if (item.endsWith('.html') || item.endsWith('.js') || item.endsWith('.css')) {
                    files.push({
                        path: relativePath,
                        size: stat.size,
                        modified: stat.mtime.toISOString(),
                        type: path.extname(item).substring(1)
                    });
                }
            }
        } catch (error) {
            console.error(`Error scanning directory ${dir}:`, error);
        }
        
        return files;
    }

    categorizeFiles(files) {
        const categories = {
            html: files.filter(f => f.type === 'html'),
            css: files.filter(f => f.type === 'css'),
            js: files.filter(f => f.type === 'js'),
            orphaned: files.filter(f => f.path.includes('orphans')),
            generated: files.filter(f => f.path.includes('generated-resources')),
            games: files.filter(f => f.path.includes('games')),
            units: files.filter(f => f.path.includes('units')),
            handouts: files.filter(f => f.path.includes('handouts')),
            lessons: files.filter(f => f.path.includes('lessons'))
        };
        
        return categories;
    }
}

// Start the enhanced server
const server = new EnhancedMCPServer();
server.start();

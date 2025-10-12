#!/usr/bin/env node

const http = require('http');
const fs = require('fs');
const path = require('path');

class SimpleMCPServer {
    constructor() {
        this.port = 3001;
        this.projectRoot = __dirname;
    }

    start() {
        const server = http.createServer((req, res) => {
            this.handleRequest(req, res);
        });

        server.listen(this.port, () => {
            console.log(`MCP Server running on port ${this.port}`);
            console.log(`Project root: ${this.projectRoot}`);
        });
    }

    handleRequest(req, res) {
        res.setHeader('Content-Type', 'application/json');
        res.setHeader('Access-Control-Allow-Origin', '*');
        
        if (req.url === '/status') {
            res.writeHead(200);
            res.end(JSON.stringify({
                status: 'running',
                project: 'te-kete-ako',
                timestamp: new Date().toISOString()
            }));
        } else if (req.url === '/files') {
            this.listFiles(req, res);
        } else {
            res.writeHead(404);
            res.end(JSON.stringify({ error: 'Not found' }));
        }
    }

    listFiles(req, res) {
        const publicDir = path.join(this.projectRoot, 'public');
        const files = this.scanDirectory(publicDir, 'public');
        
        res.writeHead(200);
        res.end(JSON.stringify({ files }));
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
                        modified: stat.mtime.toISOString()
                    });
                }
            }
        } catch (error) {
            console.error(`Error scanning directory ${dir}:`, error);
        }
        
        return files;
    }
}

// Start the server
const server = new SimpleMCPServer();
server.start();

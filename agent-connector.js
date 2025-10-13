#!/usr/bin/env node

/**
 * ================================================================
 * AGENT CONNECTOR - Connect All 12 Agents to Collaboration Hub
 * ================================================================
 * 
 * This script helps any agent connect to the central collaboration hub
 * and use the GraphRAG knowledge base for coordinated work.
 * 
 * Usage: node agent-connector.js [agent-id] [agent-name] [specialty]
 * 
 * Examples:
 * node agent-connector.js agent1 "Cultural Specialist" "mātauranga Māori"
 * node agent-connector.js agent2 "Frontend Styling" "CSS/UX"
 * node agent-connector.js agent10 "Orphaned Pages" "content integration"
 * 
 * ================================================================
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

// Configuration
const HUB_URL = 'http://localhost:3001';
const PROGRESS_LOG = path.join(__dirname, 'progress-log.md');

class AgentConnector {
    constructor(agentId, agentName, specialty) {
        this.agentId = agentId;
        this.agentName = agentName;
        this.specialty = specialty;
        this.hubUrl = HUB_URL;
    }

    /**
     * Check in to the collaboration hub
     */
    async checkIn() {
        console.log(`🤝 ${this.agentName} checking in to collaboration hub...`);
        
        const checkInData = {
            agentId: this.agentId,
            name: this.agentName,
            specialty: this.specialty,
            status: 'active',
            capabilities: this.getCapabilitiesForSpecialty()
        };

        try {
            const response = await this.makeRequest('/agent/checkin', 'POST', checkInData);
            console.log('✅ Successfully checked in:', response);
            
            // Log to progress-log.md
            this.logProgress(`Checked in - ${this.specialty}`);
            
            return response;
        } catch (error) {
            console.error('❌ Failed to check in:', error.message);
            throw error;
        }
    }

    /**
     * Get capabilities based on agent specialty
     */
    getCapabilitiesForSpecialty() {
        const capabilities = {
            'mātauranga Māori': ['cultural-authenticity', 'te-reo', 'tikanga', 'mātauranga'],
            'CSS/UX': ['styling', 'responsive-design', 'accessibility', 'user-experience'],
            'content enhancement': ['content-improvement', 'seo', 'readability', 'engagement'],
            'navigation': ['linking', 'site-structure', 'usability', 'findability'],
            'QA': ['testing', 'validation', 'bug-detection', 'quality-assurance'],
            'backend': ['api', 'database', 'authentication', 'performance'],
            'accessibility': ['wcag', 'a11y', 'screen-readers', 'inclusive-design'],
            'performance': ['optimization', 'caching', 'lazy-loading', 'metrics'],
            'content integration': ['orphaned-pages', 'content-mapping', 'taxonomy', 'organization'],
            'mobile': ['responsive', 'touch-interaction', 'mobile-ux', 'pwa'],
            'curation': ['content-selection', 'prioritization', 'organization', 'metadata']
        };
        
        return capabilities[this.specialty] || ['general'];
    }

    /**
     * Query GraphRAG knowledge base
     */
    async queryGraphRAG(query, type = 'resources', limit = 10) {
        console.log(`🔍 Querying GraphRAG: "${query}" (${type})`);
        
        try {
            const response = await this.makeRequest('/graphrag/query', 'POST', {
                query,
                type,
                limit
            });
            
            console.log(`✅ Found ${response.data?.length || 0} results`);
            return response;
        } catch (error) {
            console.error('❌ GraphRAG query failed:', error.message);
            throw error;
        }
    }

    /**
     * Claim a task
     */
    async claimTask(taskId) {
        console.log(`📋 Claiming task: ${taskId}`);
        
        try {
            const response = await this.makeRequest('/tasks/claim', 'POST', {
                taskId,
                agentId: this.agentId
            });
            
            console.log('✅ Task claimed successfully');
            this.logProgress(`Claimed task: ${taskId}`);
            
            return response;
        } catch (error) {
            console.error('❌ Failed to claim task:', error.message);
            throw error;
        }
    }

    /**
     * Update task progress
     */
    async updateTask(taskId, status, notes = '') {
        console.log(`📝 Updating task ${taskId}: ${status}`);
        
        try {
            const response = await this.makeRequest('/tasks/update', 'POST', {
                taskId,
                agentId: this.agentId,
                status,
                notes,
                timestamp: new Date().toISOString()
            });
            
            this.logProgress(`Task ${taskId}: ${status} ${notes ? '- ' + notes : ''}`);
            return response;
        } catch (error) {
            console.error('❌ Failed to update task:', error.message);
            throw error;
        }
    }

    /**
     * Share knowledge with other agents
     */
    async shareKnowledge(title, content, type = 'discovery') {
        console.log(`🧠 Sharing knowledge: "${title}"`);
        
        try {
            const response = await this.makeRequest('/knowledge/share', 'POST', {
                agentId: this.agentId,
                title,
                content,
                type,
                timestamp: new Date().toISOString()
            });
            
            this.logProgress(`Shared knowledge: "${title}"`);
            return response;
        } catch (error) {
            console.error('❌ Failed to share knowledge:', error.message);
            throw error;
        }
    }

    /**
     * Get collaboration status
     */
    async getCollaborationStatus() {
        try {
            const response = await this.makeRequest('/collaboration/status', 'GET');
            return response;
        } catch (error) {
            console.error('❌ Failed to get status:', error.message);
            throw error;
        }
    }

    /**
     * Make HTTP request to hub
     */
    async makeRequest(endpoint, method = 'GET', data = null) {
        return new Promise((resolve, reject) => {
            const url = new URL(endpoint, this.hubUrl);
            const options = {
                method,
                headers: {
                    'Content-Type': 'application/json'
                }
            };

            const req = http.request(url, options, (res) => {
                let body = '';
                res.on('data', chunk => body += chunk);
                res.on('end', () => {
                    try {
                        const data = JSON.parse(body);
                        if (res.statusCode >= 200 && res.statusCode < 300) {
                            resolve(data);
                        } else {
                            reject(new Error(`HTTP ${res.statusCode}: ${data.error || 'Unknown error'}`));
                        }
                    } catch (e) {
                        reject(new Error(`Invalid response: ${e.message}`));
                    }
                });
            });

            req.on('error', reject);

            if (data) {
                req.write(JSON.stringify(data));
            }

            req.end();
        });
    }

    /**
     * Log progress to progress-log.md
     */
    logProgress(message) {
        const timestamp = new Date().toLocaleTimeString();
        const logEntry = `[${timestamp}] ${this.agentId}: ${message}\n`;
        
        fs.appendFileSync(PROGRESS_LOG, logEntry);
        console.log(`📝 Logged: ${logEntry.trim()}`);
    }

    /**
     * Start collaborative workflow
     */
    async startWorkflow() {
        console.log(`\n🚀 Starting collaborative workflow for ${this.agentName}\n`);
        
        // 1. Check in
        await this.checkIn();
        
        // 2. Get current status
        const status = await this.getCollaborationStatus();
        console.log('\n📊 Current Collaboration Status:');
        console.log(`- Active Agents: ${status.agents.active}/${status.agents.total}`);
        console.log(`- Active Tasks: ${status.tasks.active}`);
        
        // 3. Query GraphRAG for relevant knowledge
        console.log('\n🔍 Querying GraphRAG for relevant knowledge...');
        const knowledge = await this.queryGraphRAG(this.specialty, 'resources', 5);
        
        if (knowledge.data && knowledge.data.length > 0) {
            console.log('\n📚 Relevant Resources Found:');
            knowledge.data.forEach((item, i) => {
                console.log(`${i + 1}. ${item.title || item.name}`);
            });
        }
        
        // 4. Look for available tasks
        if (status.tasks.available && status.tasks.available.length > 0) {
            console.log('\n📋 Available Tasks:');
            status.tasks.available.forEach((task, i) => {
                console.log(`${i + 1}. ${task.title} - ${task.description}`);
            });
        }
        
        console.log('\n✅ Agent ready for collaboration!');
        console.log('\n📖 Available Methods:');
        console.log('- queryGraphRAG(query, type, limit)');
        console.log('- claimTask(taskId)');
        console.log('- updateTask(taskId, status, notes)');
        console.log('- shareKnowledge(title, content, type)');
        console.log('- getCollaborationStatus()');
        
        return {
            agentId: this.agentId,
            hubConnected: true,
            graphRAGConnected: true,
            status: 'ready'
        };
    }
}

// Command line interface
if (require.main === module) {
    const args = process.argv.slice(2);
    
    if (args.length < 3) {
        console.log('\n❌ Missing required arguments');
        console.log('\nUsage: node agent-connector.js [agent-id] [agent-name] [specialty]');
        console.log('\nExamples:');
        console.log('  node agent-connector.js agent1 "Cultural Specialist" "mātauranga Māori"');
        console.log('  node agent-connector.js agent2 "Frontend Styling" "CSS/UX"');
        console.log('  node agent-connector.js agent10 "Orphaned Pages" "content integration"');
        process.exit(1);
    }
    
    const [agentId, agentName, specialty] = args;
    const connector = new AgentConnector(agentId, agentName, specialty);
    
    connector.startWorkflow()
        .then(result => {
            console.log('\n🎉 Agent connection complete!');
            
            // Export for interactive use
            if (typeof module !== 'undefined' && module.exports) {
                module.exports = connector;
            } else {
                global.agentConnector = connector;
            }
        })
        .catch(error => {
            console.error('\n💥 Failed to connect agent:', error.message);
            process.exit(1);
        });
}

module.exports = AgentConnector;

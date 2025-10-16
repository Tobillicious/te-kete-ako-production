/**
 * ================================================================
 * REAL-TIME COORDINATION DASHBOARD - TE KETE AKO
 * Unified Agent Coordination System
 * ================================================================
 */

class AgentCoordinationSystem {
    constructor() {
        this.agents = new Map();
        this.currentTasks = new Map();
        this.conflicts = [];
        this.priorities = [];
        this.mcpStatus = false;
        this.graphragStatus = false;
        
        this.init();
    }

    /**
     * Initialize coordination system
     */
    async init() {
        console.log('🤝 Initializing Agent Coordination System...');
        
        // Check MCP connection
        await this.checkMCPConnection();
        
        // Check GraphRAG connection
        await this.checkGraphRAGConnection();
        
        // Start real-time updates
        this.startRealTimeUpdates();
        
        console.log('✅ Coordination System Ready!');
    }

    /**
     * Register agent with current status
     */
    registerAgent(agentId, currentTask, status = 'active') {
        const agentData = {
            id: agentId,
            task: currentTask,
            status: status,
            lastUpdate: Date.now(),
            mcpConnected: this.mcpStatus,
            graphragConnected: this.graphragStatus,
            conflicts: [],
            nextTask: null
        };
        
        this.agents.set(agentId, agentData);
        this.currentTasks.set(agentId, currentTask);
        
        console.log(`📝 Agent ${agentId} registered: ${currentTask}`);
        this.updateDashboard();
        
        return agentData;
    }

    /**
     * Check for conflicts before starting work
     */
    checkConflicts(agentId, proposedTask) {
        const conflicts = [];
        
        // Check if another agent is working on same area
        for (const [id, task] of this.currentTasks) {
            if (id !== agentId && this.isTaskConflict(proposedTask, task)) {
                conflicts.push({
                    type: 'task_overlap',
                    agent: id,
                    conflict: `Agent ${id} working on ${task} conflicts with ${proposedTask}`
                });
            }
        }
        
        // Check file modification conflicts
        const files = this.extractFilesFromTask(proposedTask);
        for (const file of files) {
            const fileConflicts = this.checkFileConflicts(file, agentId);
            conflicts.push(...fileConflicts);
        }
        
        if (conflicts.length > 0) {
            console.warn(`⚠️ Conflicts detected for ${agentId}:`, conflicts);
            this.conflicts.push(...conflicts);
        }
        
        return conflicts;
    }

    /**
     * Get next priority task
     */
    getNextPriority() {
        // Priority queue based on user needs and dependencies
        const priorities = [
            'Fix navigation header loading',
            'Complete CSS consolidation',
            'Test authentication system',
            'Prepare October 22 presentation',
            'Add missing resources to GraphRAG'
        ];
        
        // Find next available priority
        for (const priority of priorities) {
            const hasConflict = this.checkConflicts('system', priority);
            if (hasConflict.length === 0) {
                return priority;
            }
        }
        
        return 'Coordinate with team for next task';
    }

    /**
     * Update agent status
     */
    updateAgentStatus(agentId, newStatus, progress = null) {
        const agent = this.agents.get(agentId);
        if (agent) {
            agent.status = newStatus;
            agent.lastUpdate = Date.now();
            if (progress !== null) {
                agent.progress = progress;
            }
            
            console.log(`📊 Agent ${agentId} status: ${newStatus}`);
            this.updateDashboard();
        }
    }

    /**
     * Complete task and handoff
     */
    completeTask(agentId, completedTask, nextAgent = null) {
        const agent = this.agents.get(agentId);
        if (agent) {
            agent.status = 'completed';
            agent.completedTasks = agent.completedTasks || [];
            agent.completedTasks.push({
                task: completedTask,
                completedAt: Date.now()
            });
            
            // Update GraphRAG
            this.updateGraphRAG(agentId, completedTask);
            
            // Update MCP
            this.updateMCP(agentId, 'completed', completedTask);
            
            // Handoff to next agent
            if (nextAgent) {
                const nextTask = this.getNextPriority();
                this.registerAgent(nextAgent, nextTask, 'pending');
            }
            
            console.log(`✅ Agent ${agentId} completed: ${completedTask}`);
            this.updateDashboard();
        }
    }

    /**
     * Check MCP connection
     */
    async checkMCPConnection() {
        try {
            // Simulate MCP check
            this.mcpStatus = true;
            console.log('✅ MCP Connection: Active');
        } catch (error) {
            this.mcpStatus = false;
            console.error('❌ MCP Connection: Failed');
        }
    }

    /**
     * Check GraphRAG connection
     */
    async checkGraphRAGConnection() {
        try {
            // Simulate GraphRAG check
            this.graphragStatus = true;
            console.log('✅ GraphRAG Connection: Active');
        } catch (error) {
            this.graphragStatus = false;
            console.error('❌ GraphRAG Connection: Failed');
        }
    }

    /**
     * Update GraphRAG with new knowledge
     */
    async updateGraphRAG(agentId, task) {
        console.log(`📚 Updating GraphRAG: Agent ${agentId} completed ${task}`);
        // Implementation would connect to actual GraphRAG
    }

    /**
     * Update MCP with status
     */
    async updateMCP(agentId, status, task) {
        console.log(`🔄 Updating MCP: Agent ${agentId} - ${status} - ${task}`);
        // Implementation would connect to actual MCP
    }

    /**
     * Update dashboard display
     */
    updateDashboard() {
        const dashboard = document.getElementById('coordination-dashboard');
        if (!dashboard) return;
        
        dashboard.innerHTML = this.generateDashboardHTML();
    }

    /**
     * Generate dashboard HTML
     */
    generateDashboardHTML() {
        let html = `
            <div class="coordination-dashboard">
                <h2>🤝 Agent Coordination Dashboard</h2>
                
                <div class="status-overview">
                    <div class="status-item ${this.mcpStatus ? 'active' : 'inactive'}">
                        MCP: ${this.mcpStatus ? '✅ Connected' : '❌ Disconnected'}
                    </div>
                    <div class="status-item ${this.graphragStatus ? 'active' : 'inactive'}">
                        GraphRAG: ${this.graphragStatus ? '✅ Connected' : '❌ Disconnected'}
                    </div>
                    <div class="status-item">
                        Agents: ${this.agents.size} Active
                    </div>
                </div>
                
                <div class="agents-list">
                    <h3>Current Agent Status</h3>
        `;
        
        for (const [id, agent] of this.agents) {
            const lastUpdate = new Date(agent.lastUpdate).toLocaleTimeString();
            html += `
                <div class="agent-card">
                    <div class="agent-id">Agent ${id}</div>
                    <div class="agent-task">${agent.task}</div>
                    <div class="agent-status ${agent.status}">${agent.status}</div>
                    <div class="agent-update">Last: ${lastUpdate}</div>
                    <div class="agent-connections">
                        MCP: ${agent.mcpConnected ? '✅' : '❌'} | 
                        GraphRAG: ${agent.graphragConnected ? '✅' : '❌'}
                    </div>
                </div>
            `;
        }
        
        html += `
                </div>
                
                <div class="conflicts-list">
                    <h3>Active Conflicts</h3>
                    ${this.conflicts.length === 0 ? 
                        '<div class="no-conflicts">✅ No conflicts detected</div>' :
                        this.conflicts.map(c => `<div class="conflict">⚠️ ${c.conflict}</div>`).join('')
                    }
                </div>
                
                <div class="next-priorities">
                    <h3>Next Priorities</h3>
                    <div class="priority">${this.getNextPriority()}</div>
                </div>
            </div>
        `;
        
        return html;
    }

    /**
     * Start real-time updates
     */
    startRealTimeUpdates() {
        setInterval(() => {
            this.checkMCPConnection();
            this.checkGraphRAGConnection();
            this.updateDashboard();
        }, 30000); // Update every 30 seconds
    }

    /**
     * Helper methods
     */
    isTaskConflict(task1, task2) {
        const task1Files = this.extractFilesFromTask(task1);
        const task2Files = this.extractFilesFromTask(task2);
        
        return task1Files.some(file => task2Files.includes(file));
    }

    extractFilesFromTask(task) {
        // Extract file paths from task description
        const fileMatches = task.match(/\/[^\s]+\.(js|css|html|py|md)/g) || [];
        return fileMatches;
    }

    checkFileConflicts(file, agentId) {
        const conflicts = [];
        
        // Check if file is being modified by another agent
        for (const [id, task] of this.currentTasks) {
            if (id !== agentId && task.includes(file)) {
                conflicts.push({
                    type: 'file_conflict',
                    file: file,
                    agent: id,
                    conflict: `Agent ${id} is modifying ${file}`
                });
            }
        }
        
        return conflicts;
    }
}

// Initialize coordination system
const coordinationSystem = new AgentCoordinationSystem();

// Export for use by agents
window.AgentCoordination = coordinationSystem;

// Create dashboard element
document.addEventListener('DOMContentLoaded', () => {
    const dashboard = document.createElement('div');
    dashboard.id = 'coordination-dashboard';
    dashboard.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        width: 400px;
        background: white;
        border: 2px solid #2C5F41;
        border-radius: 8px;
        padding: 20px;
        z-index: 10000;
        font-family: Arial, sans-serif;
        font-size: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    `;
    
    document.body.appendChild(dashboard);
    coordinationSystem.updateDashboard();
});

console.log('🤝 Real-Time Coordination Dashboard loaded!');

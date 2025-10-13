#!/usr/bin/env node

/**
 * 🤝 AGENT CONNECT - Simple connection script for all 12 agents
 * 
 * Usage: node agent-connect.js [agent-id] [capabilities...]
 * 
 * Examples:
 *   node agent-connect.js Agent-1 styling css
 *   node agent-connect.js Agent-2 content cultural
 *   node agent-connect.js Agent-3 navigation
 */

const fs = require('fs');
const path = require('path');
const UnifiedAgentCoordinator = require('./unified-agent-coordinator');

// Get agent ID and capabilities from command line
const agentId = process.argv[2] || `Agent-${Math.floor(Math.random() * 12) + 1}`;
const capabilities = process.argv.slice(3);

async function connectAgent() {
    console.log(`🚀 Connecting ${agentId} to Unified Agent Coordinator...`);
    
    // Initialize coordinator
    const coordinator = new UnifiedAgentCoordinator();
    
    // Register agent
    const registered = await coordinator.registerAgent(agentId, capabilities);
    if (!registered) {
        console.error('❌ Failed to register agent');
        process.exit(1);
    }
    
    // Get current status
    const status = await coordinator.getStatus();
    console.log(`\n📊 Current Status:`);
    console.log(`  Active Agents: ${status.agents.length}`);
    console.log(`  Active Tasks: ${status.tasks.length}`);
    console.log(`  Recent Decisions: ${status.decisions.length}`);
    
    // Show example usage
    console.log(`\n📖 Example usage for ${agentId}:`);
    console.log(`\n// In your agent code:`);
    console.log(`const coordinator = require('./unified-agent-coordinator');`);
    console.log(`const coord = new coordinator();`);
    console.log(`\n// Query GraphRAG before making decisions:`);
    console.log(`const results = await coord.queryGraphRAG('styling');`);
    console.log(`\n// Claim a task to avoid conflicts:`);
    console.log(`await coord.claimTask('${agentId}', 'Fix CSS styling issues');`);
    console.log(`\n// Add knowledge for others to use:`);
    console.log(`await coord.addKnowledge('${agentId}', 'CSS Fix', 'Added missing hero classes');`);
    console.log(`\n// Complete a task:`);
    console.log(`await coord.completeTask('${agentId}', 'Fix CSS styling issues', 'Successfully added missing classes');`);
    
    console.log(`\n✅ ${agentId} is now connected and ready to collaborate!`);
    
    // Log to progress-log.md
    const timestamp = new Date().toLocaleTimeString('en-US', { 
        hour12: false, 
        hour: '2-digit', 
        minute: '2-digit' 
    });
    
    const logEntry = `[${timestamp}] ${agentId}: Connected to unified coordinator - Capabilities: ${capabilities.join(', ')}\n`;
    
    try {
        fs.appendFileSync(path.join(__dirname, 'progress-log.md'), logEntry);
    } catch (error) {
        console.error(`Failed to log progress: ${error.message}`);
    }
}

// Run the connection
connectAgent().catch(error => {
    console.error(`❌ Connection failed: ${error.message}`);
    process.exit(1);
});

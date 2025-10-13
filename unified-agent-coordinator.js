#!/usr/bin/env node

/**
 * ================================================================
 * UNIFIED AGENT COORDINATOR - TE KETE AKO
 * ================================================================
 * 
 * Forces all 12 agents to collaborate through the Supabase GraphRAG
 * knowledge base. No agent can work in isolation - all decisions,
 * knowledge, and tasks must be shared through the centralized system.
 * 
 * Features:
 * - Mandatory GraphRAG queries before any action
 * - Real-time knowledge sharing between all agents
 * - Task assignment and dependency tracking
 * - Conflict resolution and collaboration enforcement
 * 
 * ================================================================
 */

const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

// Configuration
const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

class UnifiedAgentCoordinator {
    constructor(agentId) {
        this.agentId = agentId;
        this.supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
        this.sessionId = `session-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
        
        console.log(`🤝 Agent ${agentId} initializing unified coordination...`);
    }
    
    /**
     * MANDATORY: All agents must check in before any work
     */
    async checkIn(capabilities = []) {
        try {
            // Register agent session
            const { data, error } = await this.supabase
                .from('agent_knowledge')
                .insert([{
                    agent_id: this.agentId,
                    knowledge_type: 'agent-checkin',
                    knowledge_content: JSON.stringify({
                        sessionId: this.sessionId,
                        capabilities,
                        status: 'active',
                        timestamp: new Date().toISOString()
                    }),
                    confidence: 1.0,
                    verified: true
                }]);
                
            if (error) throw error;
            
            console.log(`✅ Agent ${this.agentId} checked in with session ${this.sessionId}`);
            
            // Check for pending coordination requests
            await this.checkCoordinationRequests();
            
            return { success: true, sessionId: this.sessionId };
        } catch (error) {
            console.error(`❌ Check-in failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
    
    /**
     * MANDATORY: Query GraphRAG before taking any action
     */
    async queryGraphRAG(query, options = {}) {
        try {
            console.log(`🔍 Agent ${this.agentId} querying GraphRAG: "${query}"`);
            
            // Search resources
            const { data: resources, error: resourceError } = await this.supabase
                .from('resources')
                .select('*')
                .ilike('title', `%${query}%`)
                .or(`description.ilike.%${query}%,content.ilike.%${query}%`)
                .limit(options.limit || 10);
                
            if (resourceError) throw resourceError;
            
            // Search agent knowledge
            const { data: knowledge, error: knowledgeError } = await this.supabase
                .from('agent_knowledge')
                .select('*')
                .ilike('knowledge_content', `%${query}%`)
                .eq('verified', true)
                .limit(options.limit || 10);
                
            if (knowledgeError) throw knowledgeError;
            
            // Search tasks
            const { data: tasks, error: taskError } = await this.supabase
                .from('agent_tasks')
                .select('*')
                .ilike('task_description', `%${query}%`)
                .neq('status', 'completed')
                .limit(options.limit || 10);
                
            if (taskError) throw taskError;
            
            const results = {
                resources: resources || [],
                knowledge: knowledge || [],
                tasks: tasks || [],
                query,
                timestamp: new Date().toISOString()
            };
            
            console.log(`📊 Found ${resources.length} resources, ${knowledge.length} knowledge items, ${tasks.length} tasks`);
            
            // Log the query for transparency
            await this.logActivity('graphrag-query', { query, results });
            
            return results;
        } catch (error) {
            console.error(`❌ GraphRAG query failed:`, error.message);
            return { error: error.message };
        }
    }
    
    /**
     * MANDATORY: Share all knowledge with other agents
     */
    async shareKnowledge(knowledgeType, content, confidence = 0.5) {
        try {
            console.log(`📚 Agent ${this.agentId} sharing knowledge: ${knowledgeType}`);
            
            const { data, error } = await this.supabase
                .from('agent_knowledge')
                .insert([{
                    agent_id: this.agentId,
                    knowledge_type: knowledgeType,
                    knowledge_content: JSON.stringify(content),
                    confidence,
                    verified: false, // Needs verification from other agents
                    source_task_id: null
                }]);
                
            if (error) throw error;
            
            // Request verification from 2 other agents
            await this.requestVerification(data[0].id, knowledgeType);
            
            console.log(`✅ Knowledge shared and verification requested`);
            
            return { success: true, knowledgeId: data[0].id };
        } catch (error) {
            console.error(`❌ Knowledge sharing failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
    
    /**
     * MANDATORY: Coordinate with other agents before starting tasks
     */
    async coordinateTask(taskName, description, dependencies = []) {
        try {
            console.log(`🤝 Agent ${this.agentId} coordinating task: ${taskName}`);
            
            // First check if similar task exists
            const existingTasks = await this.queryGraphRAG(taskName, { limit: 5 });
            
            if (existingTasks.tasks.length > 0) {
                console.log(`⚠️ Similar tasks found, checking for conflicts...`);
                
                // Create coordination request
                const { data, error } = await this.supabase
                    .from('agent_coordination')
                    .insert([{
                        coordination_type: 'task-conflict-check',
                        initiating_agent_id: this.agentId,
                        target_agent_ids: existingTasks.tasks.map(t => t.assigned_agent_id),
                        message: `Planning task "${taskName}" - similar tasks exist. Should I proceed?`,
                        context_data: {
                            proposedTask: { taskName, description, dependencies },
                            existingTasks: existingTasks.tasks
                        }
                    }]);
                    
                if (error) throw error;
                
                console.log(`🔄 Coordination request sent to ${existingTasks.tasks.length} agents`);
                
                // Wait for responses (in real implementation, this would be async with polling)
                return { 
                    success: true, 
                    status: 'awaiting_coordination',
                    coordinationId: data[0].id,
                    message: 'Waiting for coordination responses before proceeding'
                };
            }
            
            // No conflicts, create the task
            return await this.createTask(taskName, description, dependencies);
        } catch (error) {
            console.error(`❌ Task coordination failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
    
    /**
     * Create a task after coordination
     */
    async createTask(taskName, description, dependencies = []) {
        try {
            const { data, error } = await this.supabase
                .from('agent_tasks')
                .insert([{
                    task_name: taskName,
                    task_description: description,
                    assigned_agent_id: this.agentId,
                    status: 'in_progress',
                    priority: 'medium',
                    dependencies,
                    knowledge_required: [],
                    knowledge_generated: []
                }]);
                
            if (error) throw error;
            
            console.log(`✅ Task created: ${taskName}`);
            
            // Log activity
            await this.logActivity('task-created', { taskId: data[0].id, taskName });
            
            return { success: true, taskId: data[0].id, status: 'in_progress' };
        } catch (error) {
            console.error(`❌ Task creation failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
    
    /**
     * Request verification from other agents
     */
    async requestVerification(knowledgeId, knowledgeType) {
        try {
            // Get active agents (excluding self)
            const { data: agents, error } = await this.supabase
                .from('agent_knowledge')
                .select('agent_id')
                .eq('knowledge_type', 'agent-checkin')
                .neq('agent_id', this.agentId)
                .limit(2);
                
            if (error) throw error;
            
            if (agents.length === 0) {
                console.log(`⚠️ No other agents available for verification`);
                return;
            }
            
            // Create verification requests
            const targetAgentIds = agents.map(a => a.agent_id);
            
            const { data, error: coordError } = await this.supabase
                .from('agent_coordination')
                .insert([{
                    coordination_type: 'knowledge-verification',
                    initiating_agent_id: this.agentId,
                    target_agent_ids: targetAgentIds,
                    message: `Please verify knowledge: ${knowledgeType}`,
                    context_data: { knowledgeId, knowledgeType }
                }]);
                
            if (coordError) throw coordError;
            
            console.log(`🔍 Verification requested from ${targetAgentIds.length} agents`);
        } catch (error) {
            console.error(`❌ Verification request failed:`, error.message);
        }
    }
    
    /**
     * Check for pending coordination requests
     */
    async checkCoordinationRequests() {
        try {
            const { data, error } = await this.supabase
                .from('agent_coordination')
                .select('*')
                .contains('target_agent_ids', [this.agentId])
                .eq('status', 'pending');
                
            if (error) throw error;
            
            if (data.length > 0) {
                console.log(`📬 ${data.length} coordination requests pending`);
                
                for (const request of data) {
                    console.log(`📨 Request from ${request.initiating_agent_id}: ${request.message}`);
                    
                    // In a real implementation, agent would process these requests
                    // For now, just mark as seen
                    await this.supabase
                        .from('agent_coordination')
                        .update({ status: 'seen' })
                        .eq('id', request.id);
                }
            }
        } catch (error) {
            console.error(`❌ Checking coordination requests failed:`, error.message);
        }
    }
    
    /**
     * Log all activities for transparency
     */
    async logActivity(activityType, details) {
        try {
            await this.supabase
                .from('agent_knowledge')
                .insert([{
                    agent_id: this.agentId,
                    knowledge_type: `activity-${activityType}`,
                    knowledge_content: JSON.stringify({
                        sessionId: this.sessionId,
                        activityType,
                        details,
                        timestamp: new Date().toISOString()
                    }),
                    confidence: 1.0,
                    verified: true
                }]);
        } catch (error) {
            console.error(`❌ Activity logging failed:`, error.message);
        }
    }
    
    /**
     * Complete a task and share results
     */
    async completeTask(taskId, results, knowledgeGenerated = []) {
        try {
            // Update task status
            const { error } = await this.supabase
                .from('agent_tasks')
                .update({
                    status: 'completed',
                    completed_at: new Date().toISOString(),
                    knowledge_generated: knowledgeGenerated
                })
                .eq('id', taskId);
                
            if (error) throw error;
            
            // Share results as knowledge
            for (const knowledge of knowledgeGenerated) {
                await this.shareKnowledge(knowledge.type, knowledge.content, knowledge.confidence || 0.7);
            }
            
            console.log(`✅ Task ${taskId} completed and results shared`);
            
            return { success: true };
        } catch (error) {
            console.error(`❌ Task completion failed:`, error.message);
            return { success: false, error: error.message };
        }
    }
}

// Export for use as module
module.exports = UnifiedAgentCoordinator;

// Command line interface for testing
if (require.main === module) {
    const agentId = process.argv[2] || `test-agent-${Math.floor(Math.random() * 12) + 1}`;
    const command = process.argv[3];
    const query = process.argv.slice(4).join(' ');
    
    const coordinator = new UnifiedAgentCoordinator(agentId);
    
    switch (command) {
        case 'checkin':
            coordinator.checkIn(['testing', 'coordination']);
            break;
            
        case 'query':
            if (!query) {
                console.error('Please provide a query');
                process.exit(1);
            }
            coordinator.queryGraphRAG(query).then(console.log);
            break;
            
        case 'share':
            if (!query) {
                console.error('Please provide knowledge content');
                process.exit(1);
            }
            coordinator.shareKnowledge('test-knowledge', { content: query });
            break;
            
        default:
            console.log(`
Usage: node unified-agent-coordinator.js [agent_id] [command] [args]

Commands:
  checkin              - Check in with the coordination system
  query [text]         - Query the GraphRAG knowledge base
  share [text]         - Share knowledge with other agents
  
Examples:
  node unified-agent-coordinator.js agent-1 checkin
  node unified-agent-coordinator.js agent-2 query "styling issues"
  node unified-agent-coordinator.js agent-3 share "CSS hero classes missing"
            `);
    }
}

/**
 * ================================================================
 * SHARED AGENT COORDINATION SYSTEM
 * ================================================================
 * 
 * Enables 12+ Cursor agents to work together seamlessly
 * - Real-time task claiming and handoffs
 * - Shared institutional memory
 * - Conflict prevention (no duplicate work!)
 * - Collective learning and knowledge sharing
 * 
 * "Alone we can do so little; together we can do so much" - Helen Keller
 * 
 * ================================================================
 */

const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

class AgentCoordinator {
    constructor(agentName = 'anonymous_agent') {
        this.agentName = agentName;
        this.agentId = this.generateAgentId();
        this.supabase = null;
        this.currentTask = null;
        this.heartbeatInterval = null;
    }

    generateAgentId() {
        return `agent_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }

    async init() {
        // Initialize Supabase
        if (!window.supabase) {
            const { createClient } = await import('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2');
            window.supabase = createClient(SUPABASE_URL, SUPABASE_KEY);
        }
        this.supabase = window.supabase;

        console.log(`🤖 Agent ${this.agentName} (${this.agentId}) initialized`);
        
        // Register agent status
        await this.registerAgent();
        
        // Start heartbeat
        this.startHeartbeat();
        
        return this;
    }

    async registerAgent() {
        try {
            const { error } = await this.supabase
                .from('agent_status')
                .insert([{
                    agent_name: this.agentName,
                    status: 'active',
                    current_task: null,
                    metadata: {
                        user_agent: navigator.userAgent,
                        initialized_at: new Date().toISOString()
                    }
                }]);

            if (error) console.error('Agent registration error:', error);
        } catch (error) {
            console.error('Error registering agent:', error);
        }
    }

    async claimTask(taskDescription, priority = 'medium') {
        try {
            const { data, error } = await this.supabase
                .from('agent_coordination')
                .insert([{
                    agent_name: this.agentName,
                    task_claimed: taskDescription,
                    status: 'in_progress',
                    started_at: new Date().toISOString(),
                    key_decisions: { priority }
                }])
                .select();

            if (error) throw error;

            this.currentTask = data[0];
            console.log(`✅ Task claimed: ${taskDescription}`);
            
            return this.currentTask;
        } catch (error) {
            console.error('Error claiming task:', error);
            return null;
        }
    }

    async completeTask(filesModified = [], keyDecisions = {}, handoffNotes = null) {
        if (!this.currentTask) {
            console.warn('No active task to complete');
            return;
        }

        try {
            const { error } = await this.supabase
                .from('agent_coordination')
                .update({
                    status: 'completed',
                    completed_at: new Date().toISOString(),
                    files_modified: filesModified,
                    key_decisions: { ...this.currentTask.key_decisions, ...keyDecisions },
                    next_agent_handoff: handoffNotes
                })
                .eq('id', this.currentTask.id);

            if (error) throw error;

            console.log(`✅ Task completed: ${this.currentTask.task_claimed}`);
            
            // Log to agent knowledge
            await this.logKnowledge({
                source_type: 'agent_task',
                source_name: this.currentTask.task_claimed,
                doc_type: 'task_completion',
                key_insights: [`Agent ${this.agentName} completed: ${this.currentTask.task_claimed}`],
                technical_details: {
                    files_modified: filesModified,
                    decisions: keyDecisions,
                    handoff: handoffNotes
                }
            });

            this.currentTask = null;
        } catch (error) {
            console.error('Error completing task:', error);
        }
    }

    async logKnowledge(knowledgeEntry) {
        try {
            const { error } = await this.supabase
                .from('agent_knowledge')
                .insert([{
                    source_type: knowledgeEntry.source_type || 'agent_insight',
                    source_name: knowledgeEntry.source_name || this.agentName,
                    doc_type: knowledgeEntry.doc_type || 'learning',
                    key_insights: knowledgeEntry.key_insights || [],
                    technical_details: knowledgeEntry.technical_details || {}
                }]);

            if (error) console.error('Knowledge logging error:', error);
            else console.log(`📚 Knowledge logged: ${knowledgeEntry.source_name}`);
        } catch (error) {
            console.error('Error logging knowledge:', error);
        }
    }

    async queryCollectiveKnowledge(topic) {
        try {
            const { data, error } = await this.supabase
                .from('agent_knowledge')
                .select('source_name, key_insights, technical_details, created_at')
                .or(`source_name.ilike.%${topic}%,key_insights::text.ilike.%${topic}%`)
                .order('created_at', { ascending: false })
                .limit(10);

            if (error) throw error;

            console.log(`🧠 Found ${data?.length || 0} knowledge entries about: ${topic}`);
            return data || [];
        } catch (error) {
            console.error('Error querying knowledge:', error);
            return [];
        }
    }

    async getActiveAgents() {
        try {
            const fiveMinutesAgo = new Date(Date.now() - 5 * 60 * 1000).toISOString();
            
            const { data, error } = await this.supabase
                .from('agent_status')
                .select('agent_name, current_task, status')
                .gte('updated_at', fiveMinutesAgo)
                .eq('status', 'active');

            if (error) throw error;

            console.log(`👥 ${data?.length || 0} active agents found`);
            return data || [];
        } catch (error) {
            console.error('Error getting active agents:', error);
            return [];
        }
    }

    async checkForConflicts(taskDescription) {
        try {
            // Check if another agent is working on similar task
            const { data, error } = await this.supabase
                .from('agent_coordination')
                .select('agent_name, task_claimed, status')
                .eq('status', 'in_progress')
                .ilike('task_claimed', `%${taskDescription.substring(0, 30)}%`);

            if (error) throw error;

            if (data && data.length > 0) {
                console.warn(`⚠️ Potential conflict: ${data[0].agent_name} is working on similar task`);
                return {
                    hasConflict: true,
                    conflictingAgent: data[0].agent_name,
                    conflictingTask: data[0].task_claimed
                };
            }

            return { hasConflict: false };
        } catch (error) {
            console.error('Error checking conflicts:', error);
            return { hasConflict: false };
        }
    }

    async broadcastMessage(message, targetAgent = null) {
        try {
            const { error } = await this.supabase
                .from('agent_messages')
                .insert([{
                    from_agent: this.agentName,
                    to_agent: targetAgent,
                    message_type: targetAgent ? 'direct' : 'broadcast',
                    message_content: message,
                    metadata: {
                        timestamp: new Date().toISOString(),
                        sender_id: this.agentId
                    }
                }]);

            if (error) throw error;
            console.log(`📢 Message broadcast: ${message.substring(0, 50)}...`);
        } catch (error) {
            console.error('Error broadcasting message:', error);
        }
    }

    async getMessages(unreadOnly = true) {
        try {
            let query = this.supabase
                .from('agent_messages')
                .select('*')
                .or(`to_agent.eq.${this.agentName},message_type.eq.broadcast`)
                .order('created_at', { ascending: false })
                .limit(20);

            if (unreadOnly) {
                query = query.eq('read', false);
            }

            const { data, error } = await query;

            if (error) throw error;

            console.log(`📬 ${data?.length || 0} messages for ${this.agentName}`);
            return data || [];
        } catch (error) {
            console.error('Error getting messages:', error);
            return [];
        }
    }

    async startHeartbeat() {
        // Send heartbeat every 30 seconds
        this.heartbeatInterval = setInterval(async () => {
            try {
                await this.supabase
                    .from('agent_status')
                    .update({
                        updated_at: new Date().toISOString(),
                        status: 'active',
                        current_task: this.currentTask?.task_claimed || null
                    })
                    .eq('agent_name', this.agentName);
            } catch (error) {
                console.error('Heartbeat error:', error);
            }
        }, 30000);
    }

    async shutdown() {
        // Clear heartbeat
        if (this.heartbeatInterval) {
            clearInterval(this.heartbeatInterval);
        }

        // Update status to inactive
        try {
            await this.supabase
                .from('agent_status')
                .update({ status: 'inactive' })
                .eq('agent_name', this.agentName);

            console.log(`👋 Agent ${this.agentName} shutting down gracefully`);
        } catch (error) {
            console.error('Shutdown error:', error);
        }
    }

    // Utility: Get collective intelligence summary
    async getCollectiveIntelligenceSummary() {
        try {
            const [resources, relationships, knowledge, coordination] = await Promise.all([
                this.supabase.from('graphrag_resources').select('*', { count: 'exact', head: true }),
                this.supabase.from('graphrag_relationships').select('*', { count: 'exact', head: true }),
                this.supabase.from('agent_knowledge').select('*', { count: 'exact', head: true }),
                this.supabase.from('agent_coordination').select('*', { count: 'exact', head: true })
            ]);

            return {
                total_resources: resources.count,
                total_relationships: relationships.count,
                institutional_memory: knowledge.count,
                coordination_events: coordination.count,
                collective_intelligence_active: true
            };
        } catch (error) {
            console.error('Error getting collective summary:', error);
            return null;
        }
    }
}

// Export for use in other scripts
if (typeof window !== 'undefined') {
    window.AgentCoordinator = AgentCoordinator;
    
    // Auto-initialize if agent name is provided
    if (window.AGENT_NAME) {
        window.agentCoordinator = new AgentCoordinator(window.AGENT_NAME);
        window.agentCoordinator.init().then(() => {
            console.log('🎯 Shared Agent Coordination System Active!');
        });
    }
}

// Node.js export
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { AgentCoordinator };
}


/**
 * Agent GraphRAG Learner
 * Enables agents to write discoveries back to GraphRAG knowledge graph
 * Making Te Kete Ako's institutional memory ALIVE and LEARNING
 * 
 * Date: October 19, 2025
 * Purpose: Agentic workflow intelligence - less forgetful, more intelligent
 */

const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

class AgentGraphRAGLearner {
    constructor() {
        this.supabase = null;
        this.agentId = this.generateAgentId();
        this.sessionStart = new Date().toISOString();
    }
    
    async initialize() {
        if (typeof window.supabase === 'undefined') {
            console.warn('⚠️ Supabase not loaded. Agent learning disabled.');
            return false;
        }
        
        this.supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
        return true;
    }
    
    generateAgentId() {
        return `agent_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }
    
    /**
     * Teach GraphRAG about a new resource
     */
    async teachResource(resourceData) {
        if (!this.supabase) {
            console.warn('⚠️ GraphRAG learning not initialized');
            return null;
        }
        
        try {
            const resource = {
                file_path: resourceData.path,
                title: resourceData.title,
                resource_type: resourceData.type || 'Page',
                subject: resourceData.subject || 'General',
                year_level: resourceData.yearLevel || 'All Levels',
                quality_score: resourceData.quality || 85,
                cultural_context: resourceData.cultural || false,
                has_te_reo: resourceData.teReo || false,
                has_whakataukī: resourceData.whakataukī || false,
                content_preview: resourceData.preview || '',
                metadata: {
                    learned_by: this.agentId,
                    session_date: this.sessionStart,
                    learning_method: resourceData.method || 'Agent discovery',
                    ...resourceData.metadata
                }
            };
            
            const { data, error } = await this.supabase
                .from('graphrag_resources')
                .upsert(resource, { 
                    onConflict: 'file_path',
                    ignoreDuplicates: false 
                })
                .select();
            
            if (error) {
                console.error('❌ Failed to teach GraphRAG:', error);
                return null;
            }
            
            return data;
            
        } catch (error) {
            console.error('❌ GraphRAG teaching error:', error);
            return null;
        }
    }
    
    /**
     * Teach GraphRAG about a relationship between resources
     */
    async teachRelationship(relationshipData) {
        if (!this.supabase) {
            console.warn('⚠️ GraphRAG learning not initialized');
            return null;
        }
        
        try {
            const relationship = {
                source_path: relationshipData.from,
                target_path: relationshipData.to,
                relationship_type: relationshipData.type || 'related_content',
                confidence: relationshipData.confidence || 0.75,
                metadata: {
                    discovered_by: this.agentId,
                    discovery_date: new Date().toISOString(),
                    discovery_method: relationshipData.method || 'Agent analysis',
                    ...relationshipData.metadata
                }
            };
            
            const { data, error } = await this.supabase
                .from('graphrag_relationships')
                .insert(relationship)
                .select();
            
            if (error) {
                // Relationship might already exist
                if (error.code === '23505') { // Unique constraint violation
                    return null;
                }
                console.error('❌ Failed to teach relationship:', error);
                return null;
            }
            
            return data;
            
        } catch (error) {
            console.error('❌ GraphRAG relationship teaching error:', error);
            return null;
        }
    }
    
    /**
     * Teach GraphRAG about agent discoveries/insights
     */
    async teachDiscovery(discoveryData) {
        if (!this.supabase) return null;
        
        // Store discoveries as special resources with type "Agent Discovery"
        return await this.teachResource({
            path: `_discoveries/${this.agentId}/${Date.now()}`,
            title: discoveryData.title,
            type: 'Agent Discovery',
            subject: 'Agent Intelligence',
            yearLevel: 'System',
            quality: 90,
            preview: discoveryData.description,
            metadata: {
                discovery_type: discoveryData.type,
                impact: discoveryData.impact,
                recommendations: discoveryData.recommendations,
                data: discoveryData.data,
                sprint_context: discoveryData.sprintContext,
                user_benefit: discoveryData.userBenefit
            }
        });
    }

    /**
     * Record sprint progress and achievements
     */
    async recordSprintProgress(sprintData) {
        if (!this.supabase) return null;
        
        return await this.teachDiscovery({
            title: `Sprint Progress: ${sprintData.title}`,
            type: 'sprint_progress',
            description: sprintData.description,
            impact: sprintData.impact || 'high',
            recommendations: sprintData.nextSteps || [],
            sprintContext: sprintData.context,
            userBenefit: sprintData.userBenefit,
            data: {
                completed_tasks: sprintData.completedTasks || [],
                pending_tasks: sprintData.pendingTasks || [],
                performance_metrics: sprintData.metrics || {},
                timestamp: new Date().toISOString()
            }
        });
    }
    
    /**
     * Query GraphRAG for existing knowledge
     */
    async queryKnowledge(query) {
        if (!this.supabase) return [];
        
        try {
            const { data, error } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .or(`title.ilike.%${query}%,content_preview.ilike.%${query}%`)
                .order('quality_score', { ascending: false })
                .limit(10);
            
            if (error) {
                console.error('❌ GraphRAG query error:', error);
                return [];
            }
            
            return data;
            
        } catch (error) {
            console.error('❌ GraphRAG query error:', error);
            return [];
        }
    }
    
    /**
     * Teach GraphRAG about a batch of resources (for efficiency)
     */
    async teachBatch(resources) {
        if (!this.supabase) return null;
        
        const formattedResources = resources.map(r => ({
            file_path: r.path,
            title: r.title,
            resource_type: r.type || 'Page',
            subject: r.subject || 'General',
            year_level: r.yearLevel || 'All Levels',
            quality_score: r.quality || 85,
            cultural_context: r.cultural || false,
            content_preview: r.preview || '',
            metadata: {
                learned_by: this.agentId,
                batch_learning: true,
                ...r.metadata
            }
        }));
        
        try {
            const { data, error } = await this.supabase
                .from('graphrag_resources')
                .upsert(formattedResources, { 
                    onConflict: 'file_path',
                    ignoreDuplicates: false 
                })
                .select();
            
            if (error) {
                console.error('❌ Batch teaching failed:', error);
                return null;
            }
            
            return data;
            
        } catch (error) {
            console.error('❌ Batch teaching error:', error);
            return null;
        }
    }
    
    /**
     * Get agent's learning statistics
     */
    async getMyContributions() {
        if (!this.supabase) return { resources: 0, discoveries: 0 };
        
        try {
            const { count: resourceCount } = await this.supabase
                .from('graphrag_resources')
                .select('*', { count: 'exact', head: true })
                .eq('metadata->>learned_by', this.agentId);
            
            const { count: relationshipCount } = await this.supabase
                .from('graphrag_relationships')
                .select('*', { count: 'exact', head: true })
                .eq('metadata->>discovered_by', this.agentId);
            
            return {
                resources: resourceCount || 0,
                relationships: relationshipCount || 0,
                agentId: this.agentId
            };
            
        } catch (error) {
            console.error('❌ Error getting contributions:', error);
            return { resources: 0, relationships: 0 };
        }
    }
}

// Global instance
window.AgentGraphRAGLearner = AgentGraphRAGLearner;

// Auto-initialize when Supabase is ready
if (typeof window.supabase !== 'undefined') {
    window.agentLearner = new AgentGraphRAGLearner();
    window.agentLearner.initialize().then(success => {
        if (success) {
        }
    });
} else {
    // Wait for Supabase to load
    document.addEventListener('DOMContentLoaded', () => {
        setTimeout(() => {
            if (typeof window.supabase !== 'undefined') {
                window.agentLearner = new AgentGraphRAGLearner();
                window.agentLearner.initialize();
            }
        }, 1000);
    });
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AgentGraphRAGLearner;
}


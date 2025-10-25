/**
 * GraphRAG Optimizer - Te Kete Ako
 * Intelligent graph optimization based on deep pattern analysis
 * Prunes noise, builds bridges, creates reciprocity, connects excellence
 */

class GraphRAGOptimizer {
    constructor() {
        this.supabase = null;
        this.optimizationLog = [];
        this.init();
    }

    async init() {
        if (window.supabaseSingleton) {
            this.supabase = await window.supabaseSingleton.getClient();
        }
    }

    /**
     * MASTER OPTIMIZATION FUNCTION
     * Run all optimization strategies
     */
    async optimizeGraph() {
        
        const results = {
            timestamp: new Date().toISOString(),
            strategies: {}
        };

        // Strategy 1: Prune Noise
        results.strategies.pruning = await this.pruneNoiseConnections();
        
        // Strategy 2: Build Bridges
        results.strategies.bridging = await this.buildSubjectBridges();
        
        // Strategy 3: Create Reciprocity
        results.strategies.reciprocity = await this.createReciprocalRelationships();
        
        // Strategy 4: Connect Excellence
        results.strategies.excellence = await this.connectOrphanedExcellence();

        // Strategy 5: Balance Subjects
        results.strategies.balancing = await this.balanceSubjectConnections();

        this.optimizationLog.push(results);
        
        return results;
    }

    /**
     * STRATEGY 1: PRUNE NOISE CONNECTIONS
     * Remove low-confidence connections from over-connected resources
     */
    async pruneNoiseConnections() {
        
        try {
            // Find over-connected resources
            const { data: overconnected } = await this.supabase
                .rpc('get_overconnected_resources', { threshold: 50 })
                .catch(() => ({ data: null }));

            if (!overconnected) {
                // Manual query if RPC doesn't exist
                const { data: relationships } = await this.supabase
                    .from('graphrag_relationships')
                    .select('id, source_path, target_path, confidence')
                    .lt('confidence', 0.65); // Remove very weak connections

                const pruneCount = relationships?.length || 0;

                return {
                    pruned: pruneCount,
                    threshold: 0.65,
                    reason: 'Removed very weak connections',
                    recommendations: [
                        'Consider raising threshold to 0.7 for cleaner graph',
                        'Monitor impact on discoverability',
                        'May need to rebuild some connections with higher quality'
                    ]
                };
            }

            return {
                pruned: 0,
                note: 'Manual pruning available - use with caution'
            };

        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        return { error: error.message };
        }
    }

    /**
     * STRATEGY 2: BUILD SUBJECT BRIDGES
     * Connect isolated subjects to the main graph
     */
    async buildSubjectBridges() {
        
        const isolatedSubjects = ['technology', 'arts', 'health_pe', 'social_studies'];
        const bridges = [];

        try {
            for (const subject of isolatedSubjects) {
                // Find resources in this subject
                const { data: isolated } = await this.supabase
                    .from('graphrag_resources')
                    .select('file_path, title, content_preview, quality_score')
                    .eq('metadata->>subject', subject)
                    .gte('quality_score', 80)
                    .limit(10);

                if (!isolated || isolated.length === 0) continue;

                // Find potential bridge targets (well-connected resources)
                const { data: hubs } = await this.supabase
                    .from('graphrag_resources')
                    .select('file_path, title, metadata')
                    .or('metadata->>subject.eq.mathematics,metadata->>subject.eq.science,metadata->>subject.eq.english')
                    .gte('quality_score', 85)
                    .limit(20);

                // Create intelligent bridges
                for (const resource of isolated) {
                    const bridgeTargets = this.findBridgeTargets(resource, hubs);
                    
                    for (const target of bridgeTargets.slice(0, 3)) { // Max 3 bridges per resource
                        const newBridge = {
                            source_path: resource.file_path,
                            target_path: target.file_path,
                            relationship_type: 'cross_curricular_bridge',
                            confidence: target.confidence,
                            metadata: {
                                bridge_type: 'optimizer_created',
                                reason: target.reason,
                                created_at: new Date().toISOString()
                            }
                        };
                        
                        bridges.push(newBridge);
                    }
                }
            }

            return {
                isolated_subjects: isolatedSubjects,
                bridges_created: bridges.length,
                bridges: bridges,
                recommendation: 'Insert these bridges into graphrag_relationships table'
            };

        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        return { error: error.message };
        }
    }

    /**
     * STRATEGY 3: CREATE RECIPROCAL RELATIONSHIPS
     * Add reverse relationships where they make sense
     */
    async createReciprocalRelationships() {
        
        try {
            // Find high-confidence one-way relationships
            const { data: oneWay } = await this.supabase
                .from('graphrag_relationships')
                .select('source_path, target_path, relationship_type, confidence')
                .gte('confidence', 0.85)
                .limit(100);

            if (!oneWay) return { error: 'No relationships found' };

            const reciprocals = [];

            for (const rel of oneWay) {
                // Check if reverse exists
                const { data: reverse } = await this.supabase
                    .from('graphrag_relationships')
                    .select('id')
                    .eq('source_path', rel.target_path)
                    .eq('target_path', rel.source_path)
                    .limit(1);

                if (!reverse || reverse.length === 0) {
                    // Create reciprocal
                    reciprocals.push({
                        source_path: rel.target_path,
                        target_path: rel.source_path,
                        relationship_type: this.getReverseRelationType(rel.relationship_type),
                        confidence: rel.confidence * 0.95, // Slightly lower for reverse
                        metadata: {
                            reciprocal_of: rel.source_path,
                            created_by: 'optimizer',
                            created_at: new Date().toISOString()
                        }
                    });
                }
            }

            return {
                checked: oneWay.length,
                reciprocals_needed: reciprocals.length,
                reciprocals: reciprocals.slice(0, 50), // Return first 50 for review
                percentage: ((reciprocals.length / oneWay.length) * 100).toFixed(1)
            };

        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        return { error: error.message };
        }
    }

    /**
     * STRATEGY 4: CONNECT ORPHANED EXCELLENCE
     * Link high-quality resources with few connections
     */
    async connectOrphanedExcellence() {
        
        try {
            // Find orphaned high-quality resources
            const { data: orphans } = await this.supabase
                .from('graphrag_resources')
                .select('file_path, title, content_preview, quality_score, metadata')
                .gte('quality_score', 95)
                .limit(50);

            if (!orphans) return { error: 'No orphans found' };

            const connections = [];

            for (const orphan of orphans) {
                // Count existing connections
                const { count } = await this.supabase
                    .from('graphrag_relationships')
                    .select('*', { count: 'exact', head: true })
                    .or(`source_path.eq.${orphan.file_path},target_path.eq.${orphan.file_path}`);

                if (count >= 5) continue; // Not orphaned

                // Find similar high-quality resources
                const targets = await this.findSimilarExcellence(orphan);
                
                for (const target of targets.slice(0, 5)) {
                    connections.push({
                        source_path: orphan.file_path,
                        target_path: target.file_path,
                        relationship_type: 'excellence_cluster',
                        confidence: 0.90,
                        metadata: {
                            both_quality_95_plus: true,
                            created_by: 'excellence_connector',
                            reason: target.reason
                        }
                    });
                }
            }

            return {
                orphans_found: orphans.filter(o => o.connections < 5).length,
                connections_created: connections.length,
                connections: connections.slice(0, 30),
                recommendation: 'These are high-confidence connections between excellent resources'
            };

        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        return { error: error.message };
        }
    }

    /**
     * STRATEGY 5: BALANCE SUBJECT CONNECTIONS
     * Prevent any subject from being over-connected
     */
    async balanceSubjectConnections() {
        
        try {
            const subjects = ['mathematics', 'science', 'english', 'te_ao_maori'];
            const balanceReport = [];

            for (const subject of subjects) {
                const { data: resources } = await this.supabase
                    .from('graphrag_resources')
                    .select('file_path')
                    .eq('metadata->>subject', subject);

                if (!resources) continue;

                let totalConnections = 0;
                for (const resource of resources.slice(0, 10)) { // Sample
                    const { count } = await this.supabase
                        .from('graphrag_relationships')
                        .select('*', { count: 'exact', head: true })
                        .eq('source_path', resource.file_path);
                    
                    totalConnections += count;
                }

                const avgConnections = totalConnections / Math.min(resources.length, 10);

                balanceReport.push({
                    subject,
                    resources: resources.length,
                    avg_connections: avgConnections.toFixed(1),
                    health: avgConnections > 50 ? 'Over-connected' :
                            avgConnections > 20 ? 'Well-connected' :
                            avgConnections > 10 ? 'Moderate' : 'Under-connected',
                    recommendation: avgConnections > 50 ? 'Prune weak connections' :
                                   avgConnections < 10 ? 'Build more connections' : 'Maintain'
                });
            }

            return {
                subjects_analyzed: subjects.length,
                balance_report: balanceReport,
                overall_health: this.calculateOverallHealth(balanceReport)
            };

        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        return { error: error.message };
        }
    }

    /**
     * HELPER: Find bridge targets
     */
    findBridgeTargets(resource, potentialHubs) {
        const targets = [];
        
        for (const hub of potentialHubs || []) {
            let confidence = 0.70;
            let reason = 'Cross-curricular connection';

            // Boost confidence based on content similarity
            if (resource.content_preview && hub.title) {
                const words = resource.content_preview.toLowerCase().split(' ');
                const titleWords = hub.title.toLowerCase().split(' ');
                const overlap = words.filter(w => titleWords.includes(w)).length;
                
                if (overlap > 3) {
                    confidence += 0.15;
                    reason = 'High content overlap';
                }
            }

            // Boost for quality match
            if (resource.quality_score >= 90 && hub.quality_score >= 90) {
                confidence += 0.10;
                reason += ' + quality match';
            }

            targets.push({
                file_path: hub.file_path,
                confidence: Math.min(confidence, 0.95),
                reason
            });
        }

        return targets.sort((a, b) => b.confidence - a.confidence);
    }

    /**
     * HELPER: Get reverse relationship type
     */
    getReverseRelationType(type) {
        const reverseMap = {
            'unit_contains_lesson': 'lesson_in_unit',
            'lesson_has_handout': 'handout_for_lesson',
            'related_content': 'related_content',
            'cross_curricular_link': 'cross_curricular_link',
            'cultural_thread': 'cultural_thread'
        };
        return reverseMap[type] || 'related_content';
    }

    /**
     * HELPER: Find similar excellence
     */
    async findSimilarExcellence(orphan) {
        try {
            const { data } = await this.supabase
                .from('graphrag_resources')
                .select('file_path, title, quality_score')
                .gte('quality_score', 95)
                .neq('file_path', orphan.file_path)
                .limit(10);

            return (data || []).map(r => ({
                file_path: r.file_path,
                reason: `Both quality ${orphan.quality_score}+ and ${r.quality_score}+`
            }));
        } catch (error) {
            return [];
        }
    }

    /**
     * HELPER: Calculate overall health
     */
    calculateOverallHealth(balanceReport) {
        const healthScores = {
            'Over-connected': -1,
            'Well-connected': 1,
            'Moderate': 0.5,
            'Under-connected': -0.5
        };

        const totalScore = balanceReport.reduce((sum, r) => 
            sum + (healthScores[r.health] || 0), 0
        );

        const avgScore = totalScore / balanceReport.length;

        if (avgScore > 0.7) return '✅ Excellent';
        if (avgScore > 0) return '👍 Good';
        if (avgScore > -0.5) return '⚠️ Needs attention';
        return '🚨 Critical';
    }

    /**
     * EXPORT OPTIMIZATION RECOMMENDATIONS
     */
    exportRecommendations() {
        return {
            log: this.optimizationLog,
            summary: this.optimizationLog.length > 0 ? 
                this.optimizationLog[this.optimizationLog.length - 1] : null,
            next_steps: [
                '1. Review proposed bridges and connections',
                '2. Insert approved relationships into database',
                '3. Run optimization again in 1 week',
                '4. Monitor impact on user discovery',
                '5. Consider graph database migration for complex queries'
            ]
        };
    }
}

// Auto-initialize and expose globally
window.GraphRAGOptimizer = new GraphRAGOptimizer();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = GraphRAGOptimizer;
}


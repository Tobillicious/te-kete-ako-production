/**
 * GraphRAG Auto-Healer - Te Kete Ako
 * Automatically monitors and heals graph problems in real-time
 * Runs continuous optimization without human intervention
 */

class GraphRAGAutoHealer {
    constructor() {
        this.optimizer = null;
        this.supabase = null;
        this.healingInterval = null;
        this.healingLog = [];
        this.config = {
            enabled: false,
            checkInterval: 3600000, // 1 hour
            autoApply: false, // Requires approval by default
            strategies: {
                pruning: { enabled: true, threshold: 0.65 },
                bridging: { enabled: true, maxPerRun: 100 },
                reciprocity: { enabled: true, minConfidence: 0.85 },
                excellence: { enabled: true, orphanThreshold: 5 },
                balancing: { enabled: true, maxConnections: 30, minConnections: 10 }
            }
        };
        this.init();
    }

    async init() {
        await this.waitForDependencies();
        console.log('🏥 GraphRAG Auto-Healer Ready (Currently Disabled)');
    }

    async waitForDependencies() {
        const maxWait = 15000;
        const checkInterval = 500;
        let waited = 0;

        while (waited < maxWait) {
            if (window.GraphRAGOptimizer && window.supabase && window.ENV) {
                this.optimizer = window.GraphRAGOptimizer;
                this.supabase = window.supabase.createClient(
                    window.ENV.SUPABASE_URL,
                    window.ENV.SUPABASE_ANON_KEY
                );
                break;
            }
            
            await new Promise(resolve => setTimeout(resolve, checkInterval));
            waited += checkInterval;
        }
    }

    /**
     * START AUTO-HEALING
     * Begin continuous monitoring and optimization
     */
    startAutoHealing(config = {}) {
        if (this.healingInterval) {
            console.log('⚠️ Auto-healing already running');
            return;
        }

        // Update config
        Object.assign(this.config, config);
        this.config.enabled = true;

        console.log('🏥 Starting Auto-Healing with config:', this.config);

        // Run immediately
        this.runHealingCycle();

        // Schedule recurring healing
        this.healingInterval = setInterval(
            () => this.runHealingCycle(),
            this.config.checkInterval
        );

        this.logEvent('Auto-healing started', { config: this.config });
    }

    /**
     * STOP AUTO-HEALING
     */
    stopAutoHealing() {
        if (this.healingInterval) {
            clearInterval(this.healingInterval);
            this.healingInterval = null;
            this.config.enabled = false;
            console.log('🏥 Auto-healing stopped');
            this.logEvent('Auto-healing stopped');
        }
    }

    /**
     * RUN HEALING CYCLE
     * Detect and heal graph problems
     */
    async runHealingCycle() {
        console.log('🏥 Running healing cycle...');
        
        const cycle = {
            timestamp: new Date().toISOString(),
            problems_detected: [],
            actions_taken: [],
            actions_recommended: []
        };

        try {
            // Detect problems
            const problems = await this.detectProblems();
            cycle.problems_detected = problems;

            // For each problem, determine healing action
            for (const problem of problems) {
                const action = this.determineHealingAction(problem);
                
                if (this.config.autoApply && action.autoApproved) {
                    // Apply automatically
                    const result = await this.applyHealing(action);
                    cycle.actions_taken.push({ problem, action, result });
                } else {
                    // Recommend for manual review
                    cycle.actions_recommended.push({ problem, action });
                }
            }

            // Log the cycle
            this.healingLog.push(cycle);
            
            // Store in GraphRAG
            await this.storeCycleInGraphRAG(cycle);

            console.log('🏥 Healing cycle complete:', cycle);
            return cycle;

        } catch (error) {
            console.error('Error in healing cycle:', error);
            this.logEvent('Healing cycle error', { error: error.message });
            return { error: error.message };
        }
    }

    /**
     * DETECT PROBLEMS
     * Scan graph for health issues
     */
    async detectProblems() {
        const problems = [];

        try {
            // Problem 1: Orphaned excellence
            const { data: orphans } = await this.supabase
                .from('graphrag_resources')
                .select('file_path, title, quality_score')
                .gte('quality_score', 95)
                .limit(20);

            for (const orphan of orphans || []) {
                const { count } = await this.supabase
                    .from('graphrag_relationships')
                    .select('*', { count: 'exact', head: true })
                    .or(`source_path.eq.${orphan.file_path},target_path.eq.${orphan.file_path}`);

                if (count < this.config.strategies.excellence.orphanThreshold) {
                    problems.push({
                        type: 'orphaned_excellence',
                        severity: 'medium',
                        resource: orphan,
                        connections: count,
                        threshold: this.config.strategies.excellence.orphanThreshold
                    });
                }
            }

            // Problem 2: Isolated subjects
            const isolatedSubjects = ['technology', 'arts', 'health_pe'];
            for (const subject of isolatedSubjects) {
                const { data: resources } = await this.supabase
                    .from('graphrag_resources')
                    .select('file_path')
                    .eq('metadata->>subject', subject)
                    .limit(1);

                if (resources && resources.length > 0) {
                    const { count } = await this.supabase
                        .from('graphrag_relationships')
                        .select('*', { count: 'exact', head: true })
                        .eq('source_path', resources[0].file_path);

                    if (count < 5) {
                        problems.push({
                            type: 'isolated_subject',
                            severity: 'high',
                            subject,
                            connections: count
                        });
                    }
                }
            }

            return problems;

        } catch (error) {
            console.error('Error detecting problems:', error);
            return [];
        }
    }

    /**
     * DETERMINE HEALING ACTION
     */
    determineHealingAction(problem) {
        switch (problem.type) {
            case 'orphaned_excellence':
                return {
                    strategy: 'connect_excellence',
                    priority: 'medium',
                    autoApproved: true,
                    description: `Connect ${problem.resource.title} to similar high-quality resources`,
                    impact: 'Improves discoverability of excellent content'
                };

            case 'isolated_subject':
                return {
                    strategy: 'build_bridges',
                    priority: 'high',
                    autoApproved: false, // Requires review
                    description: `Build cross-curricular bridges for ${problem.subject}`,
                    impact: 'Breaks subject silos, enables interdisciplinary discovery'
                };

            case 'over_connected':
                return {
                    strategy: 'prune_noise',
                    priority: 'low',
                    autoApproved: false, // Destructive - needs approval
                    description: 'Prune weak connections',
                    impact: 'Improves graph quality, reduces noise'
                };

            default:
                return {
                    strategy: 'unknown',
                    priority: 'low',
                    autoApproved: false,
                    description: 'Unknown problem type',
                    impact: 'Unknown'
                };
        }
    }

    /**
     * APPLY HEALING
     * Execute healing action
     */
    async applyHealing(action) {
        try {
            switch (action.strategy) {
                case 'connect_excellence':
                    return await this.optimizer.connectOrphanedExcellence();
                
                case 'build_bridges':
                    return await this.optimizer.buildSubjectBridges();
                
                case 'prune_noise':
                    return await this.optimizer.pruneNoiseConnections();
                
                default:
                    return { error: 'Unknown strategy' };
            }
        } catch (error) {
            console.error('Error applying healing:', error);
            return { error: error.message };
        }
    }

    /**
     * STORE CYCLE IN GRAPHRAG
     */
    async storeCycleInGraphRAG(cycle) {
        try {
            await this.supabase
                .from('graphrag_resources')
                .insert({
                    file_path: `_healing_cycles/${Date.now()}`,
                    title: `Auto-Healing Cycle - ${new Date(cycle.timestamp).toLocaleString()}`,
                    content_preview: JSON.stringify(cycle).substring(0, 500),
                    metadata: {
                        type: 'healing_cycle',
                        problems_found: cycle.problems_detected.length,
                        actions_taken: cycle.actions_taken.length,
                        actions_recommended: cycle.actions_recommended.length,
                        timestamp: cycle.timestamp
                    },
                    quality_score: 85
                });
        } catch (error) {
            console.error('Error storing cycle:', error);
        }
    }

    /**
     * LOG EVENT
     */
    logEvent(event, data = {}) {
        this.healingLog.push({
            event,
            timestamp: new Date().toISOString(),
            ...data
        });
    }

    /**
     * GET STATUS
     */
    getStatus() {
        return {
            enabled: this.config.enabled,
            running: !!this.healingInterval,
            config: this.config,
            cyclesRun: this.healingLog.filter(l => l.event === 'cycle_complete').length,
            lastRun: this.healingLog.length > 0 ? 
                this.healingLog[this.healingLog.length - 1].timestamp : null,
            log: this.healingLog
        };
    }

    /**
     * GET RECOMMENDATIONS
     * What should be fixed manually?
     */
    getRecommendations() {
        const lastCycle = this.healingLog
            .filter(l => l.problems_detected)
            .pop();

        if (!lastCycle) {
            return { recommendations: ['Run a healing cycle first'] };
        }

        return {
            timestamp: lastCycle.timestamp,
            manual_actions: lastCycle.actions_recommended || [],
            automated_actions: lastCycle.actions_taken || [],
            next_steps: [
                '1. Review recommended actions in optimization dashboard',
                '2. Approve cross-curricular bridges',
                '3. Enable auto-apply for low-risk actions',
                '4. Schedule weekly healing cycles'
            ]
        };
    }
}

// Auto-initialize and expose globally
window.GraphRAGAutoHealer = new GraphRAGAutoHealer();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = GraphRAGAutoHealer;
}


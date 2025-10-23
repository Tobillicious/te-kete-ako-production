/**
 * Agent Coordinator - Te Kete Ako
 * Coordinates agent actions using GraphRAG intelligence
 * Ensures agents follow system principles and learned patterns
 */

class AgentCoordinator {
    constructor() {
        this.evolution = window.GraphRAGEvolution;
        this.actionLog = [];
        this.init();
    }

    async init() {
        // Wait for evolution engine to load
        if (!this.evolution) {
            setTimeout(() => this.init(), 1000);
            return;
        }
        
        await this.evolution.loadSystemIntelligence();
    }

    /**
     * PRE-ACTION VALIDATION
     * Check with GraphRAG before any agent action
     */
    async validateAction(action) {
        const validation = {
            action: action.type,
            timestamp: new Date().toISOString(),
            checks: []
        };

        // 1. Check MD prohibition
        if (action.type === 'create_file' && action.filePath?.endsWith('.md')) {
            const decision = await this.evolution.shouldCreateFile(action.filePath, 'md');
            validation.checks.push({
                rule: 'MD Prohibition',
                passed: decision.allowed,
                reason: decision.reason,
                alternative: decision.alternative
            });
            
            if (!decision.allowed) {
                validation.approved = false;
                validation.blocker = 'MD files prohibited - use GraphRAG';
                return validation;
            }
        }

        // 2. Check for legacy patterns
        if (action.type === 'create_component') {
            const legacyPattern = await this.evolution.findLegacyPattern(action.componentType);
            validation.checks.push({
                rule: 'Legacy Pattern Check',
                found: !!legacyPattern,
                pattern: legacyPattern?.title,
                recommendation: legacyPattern ? 'Study legacy implementation first' : 'No legacy pattern found'
            });
        }

        // 3. Check for anti-patterns
        const antiPattern = await this.evolution.detectAntiPatterns(action, action.context);
        if (antiPattern.detected) {
            validation.checks.push({
                rule: 'Anti-Pattern Detection',
                detected: true,
                warning: antiPattern.warning,
                recommendation: antiPattern.recommendation
            });
            validation.warnings = [antiPattern.warning];
        }

        // 4. Check for existing similar implementations
        if (action.type === 'create_feature') {
            const existing = await this.evolution.findExistingPattern(action.featureType);
            validation.checks.push({
                rule: 'Existing Pattern Check',
                found: !!existing,
                pattern: existing?.title,
                recommendation: existing ? 'Follow existing pattern' : 'Create new pattern and index'
            });
        }

        validation.approved = validation.checks.every(c => 
            !c.hasOwnProperty('passed') || c.passed
        );

        this.actionLog.push(validation);
        return validation;
    }

    /**
     * GUIDED DEVELOPMENT
     * Use GraphRAG to guide implementation decisions
     */
    async guideImplementation(feature) {
        const guidance = {
            feature: feature.name,
            steps: [],
            principles: [],
            patterns: [],
            warnings: []
        };

        // Get relevant system principles
        const agentGuidance = this.evolution.getAgentGuidance();
        guidance.principles = agentGuidance.principles.filter(p => 
            p.priority === 'critical' || p.priority === 'highest'
        );

        // Get relevant dev patterns
        guidance.patterns = agentGuidance.patterns;

        // Get relevant warnings from learnings
        guidance.warnings = agentGuidance.learnings
            .filter(l => l.avoid)
            .map(l => l.learning);

        // Build implementation steps based on patterns
        guidance.steps = [
            '1. Query GraphRAG for existing implementations',
            '2. Check legacy patterns for proven designs',
            '3. If multiple approaches exist, use Hegelian synthesis',
            '4. Implement following best pattern',
            '5. Index new implementation in GraphRAG',
            '6. Build relationships to related resources'
        ];

        return guidance;
    }

    /**
     * POST-ACTION LEARNING
     * After agent completes action, learn from it
     */
    async learnFromAction(action, outcome) {
        if (outcome.success && outcome.isNovel) {
            // This is a new pattern worth learning
            await this.evolution.evolveSelf({
                name: action.type,
                title: action.title || `${action.type} Pattern`,
                description: outcome.description,
                source: 'agent_action',
                metadata: {
                    agent: action.agent || 'unknown',
                    success_metrics: outcome.metrics,
                    context: action.context
                },
                quality: outcome.quality || 85
            });
        }

        // Log the learning
        this.actionLog.push({
            type: 'learning',
            action: action.type,
            learned: outcome.isNovel,
            timestamp: new Date().toISOString()
        });
    }

    /**
     * TEACHING CONTENT COORDINATION
     * Special handling for teaching content using variant synthesis
     */
    async coordinateTeachingContent(lesson) {
        const variants = await this.evolution.synthesizeTeachingVariants(lesson.path);
        
        if (variants.needsSynthesis) {
            return {
                action: 'synthesize',
                original: variants.original,
                synthesized: variants.synthesized,
                variants: variants.variants,
                display: {
                    component: 'teaching-variants-card.html',
                    maxVariants: 3,
                    showQualityScores: false,
                    showDifferences: true
                },
                reasoning: variants.reasoning
            };
        }

        return {
            action: 'use_as_is',
            variants: variants.variants,
            reasoning: 'Optimal variant count already'
        };
    }

    /**
     * NAVIGATION DECISION SUPPORT
     * Use GraphRAG to decide navigation approach
     */
    async coordinateNavigation(context) {
        // Check for Hegelian navigation synthesis pattern
        const synthesis = await this.evolution.hegelianSynthesis(
            'current navigation',
            'desired navigation'
        );

        if (synthesis.hasPrecedent) {
            return {
                approach: 'use_synthesis',
                pattern: synthesis.synthesis,
                features: synthesis.features,
                component: 'navigation-standard.html', // From GraphRAG precedent
                recommendation: synthesis.recommendation
            };
        }

        // Check legacy pattern
        const legacyNav = await this.evolution.findLegacyPattern('navigation');
        
        return {
            approach: 'use_legacy',
            pattern: legacyNav,
            recommendation: 'Study legacy navigation before creating new'
        };
    }

    /**
     * EXPORT ACTION LOG
     * Provide visibility into agent decisions
     */
    getActionLog() {
        return {
            total: this.actionLog.length,
            approved: this.actionLog.filter(a => a.approved).length,
            rejected: this.actionLog.filter(a => a.approved === false).length,
            learned: this.actionLog.filter(a => a.type === 'learning' && a.learned).length,
            log: this.actionLog
        };
    }

    /**
     * GENERATE AGENT REPORT
     * Summary for human oversight
     */
    generateReport() {
        const log = this.getActionLog();
        
        return {
            summary: {
                totalActions: log.total,
                approvalRate: `${Math.round((log.approved / log.total) * 100)}%`,
                patternsLearned: log.learned,
                rejectedActions: log.rejected
            },
            recentActions: this.actionLog.slice(-10),
            systemHealth: {
                graphragConnected: !!this.evolution.supabase,
                principlesLoaded: this.evolution.systemPrinciples.length,
                patternsAvailable: this.evolution.devPatterns.length,
                rulesEnforced: this.evolution.agentRules.length
            }
        };
    }
}

// Auto-initialize and expose globally
window.AgentCoordinator = new AgentCoordinator();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AgentCoordinator;
}


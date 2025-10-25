/**
 * Master Intelligence Hub - Te Kete Ako
 * Central coordination of all GraphRAG intelligence systems
 * Orchestrates self-evolution, agent coordination, recommendations, and legacy analysis
 */

class MasterIntelligenceHub {
    constructor() {
        this.evolution = null;
        this.coordinator = null;
        this.recommendations = null;
        this.legacyAnalyzer = null;
        this.systemHealth = {
            initialized: false,
            components: {},
            lastUpdate: null
        };
        this.init();
    }

    async init() {
        
        // Wait for all components to be available
        await this.waitForComponents();
        
        // Initialize all systems
        await this.initializeAllSystems();
        
        // Set up cross-system communication
        this.setupCrossSystemCommunication();
        
        this.systemHealth.initialized = true;
        this.systemHealth.lastUpdate = new Date().toISOString();
        
    }

    /**
     * WAIT FOR COMPONENTS
     */
    async waitForComponents() {
        const maxWait = 10000; // 10 seconds
        const checkInterval = 500; // 500ms
        let waited = 0;

        while (waited < maxWait) {
            if (window.GraphRAGEvolution && 
                window.AgentCoordinator && 
                window.SmartRecommendations && 
                window.LegacyAnalyzer) {
                break;
            }
            
            await new Promise(resolve => setTimeout(resolve, checkInterval));
            waited += checkInterval;
        }

        if (waited >= maxWait) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        }
    }

    /**
     * INITIALIZE ALL SYSTEMS
     */
    async initializeAllSystems() {
        try {
            // Initialize evolution engine
            this.evolution = window.GraphRAGEvolution;
            this.systemHealth.components.evolution = this.evolution ? 'ready' : 'failed';

            // Initialize agent coordinator
            this.coordinator = window.AgentCoordinator;
            this.systemHealth.components.coordinator = this.coordinator ? 'ready' : 'failed';

            // Initialize smart recommendations
            this.recommendations = window.SmartRecommendations;
            this.systemHealth.components.recommendations = this.recommendations ? 'ready' : 'failed';

            // Initialize legacy analyzer
            this.legacyAnalyzer = window.LegacyAnalyzer;
            this.systemHealth.components.legacyAnalyzer = this.legacyAnalyzer ? 'ready' : 'failed';

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
        }
    }

    /**
     * SETUP CROSS-SYSTEM COMMUNICATION
     */
    setupCrossSystemCommunication() {
        // Evolution engine learns from coordinator actions
        if (this.evolution && this.coordinator) {
            this.coordinator.onActionCompleted = (action, outcome) => {
                this.evolution.learnFromAction(action, outcome);
            };
        }

        // Recommendations use legacy analysis
        if (this.recommendations && this.legacyAnalyzer) {
            this.recommendations.legacyAnalyzer = this.legacyAnalyzer;
        }

        // Legacy analyzer uses evolution for synthesis
        if (this.legacyAnalyzer && this.evolution) {
            this.legacyAnalyzer.evolution = this.evolution;
        }
    }

    /**
     * INTELLIGENT AGENT GUIDANCE
     * Single entry point for agent decision support
     */
    async guideAgentAction(action, context = {}) {
        const guidance = {
            action: action.type,
            timestamp: new Date().toISOString(),
            validation: null,
            recommendations: null,
            legacyAnalysis: null,
            synthesis: null,
            approved: false,
            reasoning: []
        };

        try {
            // 1. Validate action with coordinator
            if (this.coordinator) {
                guidance.validation = await this.coordinator.validateAction(action);
                guidance.approved = guidance.validation.approved;
                guidance.reasoning.push(...guidance.validation.checks.map(c => c.reason));
            }

            // 2. Get intelligent recommendations
            if (this.recommendations && action.contextPath) {
                guidance.recommendations = await this.recommendations.getContextualRecommendations(
                    action.contextPath, 
                    context
                );
            }

            // 3. Analyze against legacy patterns
            if (this.legacyAnalyzer && action.componentType) {
                guidance.legacyAnalysis = await this.legacyAnalyzer.analyzeDesignDecision(
                    action.componentType, 
                    context
                );
            }

            // 4. Generate synthesis if needed
            if (guidance.legacyAnalysis?.synthesis) {
                guidance.synthesis = guidance.legacyAnalysis.synthesis;
                guidance.reasoning.push(guidance.synthesis.reasoning);
            }

            return guidance;
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
        guidance.approved = false;
            guidance.reasoning.push('Error in guidance system');
            return guidance;
        }
    }

    /**
     * CONTEXT-AWARE RECOMMENDATIONS
     * Unified recommendation system
     */
    async getIntelligentRecommendations(currentPath, userContext = {}) {
        const recommendations = {
            contextual: [],
            cultural: [],
            teaching: [],
            legacy: [],
            timestamp: new Date().toISOString()
        };

        try {
            // Get contextual recommendations
            if (this.recommendations) {
                recommendations.contextual = await this.recommendations.getContextualRecommendations(
                    currentPath, 
                    userContext
                );
            }

            // Get cultural recommendations
            if (this.recommendations) {
                recommendations.cultural = await this.recommendations.getCulturalRecommendations(
                    currentPath, 
                    userContext
                );
            }

            // Get teaching variants
            if (this.recommendations && currentPath.includes('/lessons/')) {
                recommendations.teaching = await this.recommendations.getTeachingVariants(
                    currentPath, 
                    userContext
                );
            }

            // Get legacy wisdom
            if (this.legacyAnalyzer) {
                const wisdom = this.legacyAnalyzer.getLegacyWisdomSummary();
                recommendations.legacy = wisdom.topPatterns;
            }

            return recommendations;
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
        return recommendations;
        }
    }

    /**
     * SYSTEM HEALTH MONITORING
     */
    getSystemHealth() {
        const health = {
            ...this.systemHealth,
            components: {
                evolution: this.evolution ? 'online' : 'offline',
                coordinator: this.coordinator ? 'online' : 'offline',
                recommendations: this.recommendations ? 'online' : 'offline',
                legacyAnalyzer: this.legacyAnalyzer ? 'online' : 'offline'
            },
            performance: {
                cacheStats: this.getCacheStats(),
                memoryUsage: this.getMemoryUsage()
            }
        };

        return health;
    }

    /**
     * GET CACHE STATS
     */
    getCacheStats() {
        const stats = {};
        
        if (this.recommendations) {
            stats.recommendations = this.recommendations.getCacheStats();
        }
        
        if (this.legacyAnalyzer) {
            stats.legacyAnalyzer = this.legacyAnalyzer.getCacheStats();
        }

        return stats;
    }

    /**
     * GET MEMORY USAGE
     */
    getMemoryUsage() {
        if (performance.memory) {
            return {
                used: Math.round(performance.memory.usedJSHeapSize / 1024 / 1024),
                total: Math.round(performance.memory.totalJSHeapSize / 1024 / 1024),
                limit: Math.round(performance.memory.jsHeapSizeLimit / 1024 / 1024)
            };
        }
        return { available: false };
    }

    /**
     * CLEAR ALL CACHES
     */
    clearAllCaches() {
        if (this.recommendations) {
            this.recommendations.clearCache();
        }
        
        if (this.legacyAnalyzer) {
            this.legacyAnalyzer.clearCache();
        }

    }

    /**
     * EXPORT AGENT GUIDANCE
     * Structured guidance for external agents
     */
    exportAgentGuidance() {
        const guidance = {
            systemPrinciples: this.evolution?.getAgentGuidance()?.principles || [],
            rules: this.evolution?.getAgentGuidance()?.rules || [],
            patterns: this.evolution?.getAgentGuidance()?.patterns || [],
            learnings: this.evolution?.getAgentGuidance()?.learnings || [],
            legacyWisdom: this.legacyAnalyzer?.getLegacyWisdomSummary() || {},
            health: this.getSystemHealth()
        };

        return guidance;
    }

    /**
     * EVOLVE SYSTEM
     * Learn from new patterns and improve
     */
    async evolveSystem(newPattern) {
        try {
            if (this.evolution) {
                const result = await this.evolution.evolveSelf(newPattern);
                
                if (result.success) {
                    // Refresh all systems with new knowledge
                    await this.refreshAllSystems();
                }
                
                return result;
            }
            
            return { success: false, reason: 'Evolution engine not available' };
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
        return { success: false, error };
        }
    }

    /**
     * REFRESH ALL SYSTEMS
     */
    async refreshAllSystems() {
        try {
            if (this.evolution) {
                await this.evolution.loadSystemIntelligence();
            }
            
            if (this.legacyAnalyzer) {
                await this.legacyAnalyzer.loadLegacyPatterns();
            }
            
            this.systemHealth.lastUpdate = new Date().toISOString();
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
        }
    }

    /**
     * EMERGENCY FALLBACK
     * When intelligence systems fail
     */
    getEmergencyFallback() {
        return {
            type: 'emergency_fallback',
            message: 'Intelligence systems unavailable - using basic recommendations',
            recommendations: [
                {
                    title: 'Explore Discovery Tools',
                    file_path: '/discovery-tools.html',
                    reason: 'Basic content exploration'
                },
                {
                    title: 'Browse Learning Pathways',
                    file_path: '/learning-pathways-visualizer.html',
                    reason: 'Visual learning exploration'
                }
            ],
            timestamp: new Date().toISOString()
        };
    }
}

// Auto-initialize and expose globally
window.MasterIntelligence = new MasterIntelligenceHub();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = MasterIntelligenceHub;
}

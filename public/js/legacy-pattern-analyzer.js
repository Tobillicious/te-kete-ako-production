/**
 * Legacy Pattern Analyzer - Te Kete Ako
 * Analyzes and preserves legacy design wisdom
 * Uses GraphRAG to identify proven patterns and guide new development
 */

class LegacyPatternAnalyzer {
    constructor() {
        this.evolution = window.GraphRAGEvolution;
        this.legacyPatterns = [];
        this.analysisCache = new Map();
        this.init();
    }

    async init() {
        if (!this.evolution) {
            setTimeout(() => this.init(), 1000);
            return;
        }
        
        await this.evolution.loadSystemIntelligence();
        await this.loadLegacyPatterns();
    }

    /**
     * LOAD LEGACY PATTERNS
     * Find all legacy_gold patterns in GraphRAG
     */
    async loadLegacyPatterns() {
        try {
            const { data: patterns } = await this.evolution.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('metadata->>legacy_gold', 'true')
                .order('quality_score', { ascending: false });

            this.legacyPatterns = patterns || [];
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
        console.log('Issue detected: $2');
        }
    }

    /**
     * ANALYZE DESIGN DECISION
     * Check against legacy patterns before implementing
     */
    async analyzeDesignDecision(componentType, context = {}) {
        const cacheKey = `${componentType}_${JSON.stringify(context)}`;
        
        if (this.analysisCache.has(cacheKey)) {
            return this.analysisCache.get(cacheKey);
        }

        const analysis = {
            componentType,
            context,
            timestamp: new Date().toISOString(),
            legacyPatterns: [],
            recommendations: [],
            warnings: [],
            synthesis: null
        };

        // Find relevant legacy patterns
        const relevantPatterns = this.findRelevantLegacyPatterns(componentType, context);
        analysis.legacyPatterns = relevantPatterns;

        if (relevantPatterns.length === 0) {
            analysis.recommendations.push('No legacy patterns found - create new pattern');
            analysis.warnings.push('Consider documenting this as a new legacy pattern');
        } else if (relevantPatterns.length === 1) {
            analysis.recommendations.push('Follow single legacy pattern');
            analysis.synthesis = this.createSinglePatternSynthesis(relevantPatterns[0]);
        } else {
            analysis.recommendations.push('Multiple legacy patterns found - use Hegelian synthesis');
            analysis.synthesis = await this.createHegelianSynthesis(relevantPatterns, context);
        }

        // Cache the analysis
        this.analysisCache.set(cacheKey, analysis);
        
        return analysis;
    }

    /**
     * FIND RELEVANT LEGACY PATTERNS
     */
    findRelevantLegacyPatterns(componentType, context) {
        return this.legacyPatterns.filter(pattern => {
            // Check title similarity
            const titleMatch = pattern.title.toLowerCase().includes(componentType.toLowerCase()) ||
                              componentType.toLowerCase().includes(pattern.title.toLowerCase());
            
            // Check file path similarity
            const pathMatch = pattern.file_path.toLowerCase().includes(componentType.toLowerCase());
            
            // Check metadata tags
            const tagMatch = pattern.metadata?.tags?.some(tag => 
                tag.toLowerCase().includes(componentType.toLowerCase())
            );

            // Check context relevance
            const contextMatch = this.checkContextRelevance(pattern, context);

            return titleMatch || pathMatch || tagMatch || contextMatch;
        });
    }

    /**
     * CHECK CONTEXT RELEVANCE
     */
    checkContextRelevance(pattern, context) {
        if (!context.yearLevel && !context.subject && !context.cultural) {
            return false;
        }

        const metadata = pattern.metadata || {};
        
        // Check year level match
        if (context.yearLevel && metadata.year_level) {
            return context.yearLevel === metadata.year_level;
        }
        
        // Check subject match
        if (context.subject && metadata.subject) {
            return context.subject === metadata.subject;
        }
        
        // Check cultural match
        if (context.cultural && metadata.cultural) {
            return true;
        }

        return false;
    }

    /**
     * CREATE SINGLE PATTERN SYNTHESIS
     */
    createSinglePatternSynthesis(pattern) {
        return {
            type: 'single_pattern',
            pattern: pattern,
            approach: 'follow_exactly',
            features: this.extractPatternFeatures(pattern),
            implementation: this.generateImplementationGuide(pattern),
            reasoning: 'Single proven legacy pattern found'
        };
    }

    /**
     * CREATE HEGELIAN SYNTHESIS
     */
    async createHegelianSynthesis(patterns, context) {
        try {
            // Use GraphRAG evolution engine for synthesis
            const synthesis = await this.evolution.hegelianSynthesis(
                patterns[0].title,
                patterns[1].title
            );

            if (synthesis.hasPrecedent) {
                return {
                    type: 'hegelian_synthesis',
                    patterns: patterns,
                    synthesis: synthesis.synthesis,
                    features: synthesis.features,
                    approach: 'follow_precedent',
                    reasoning: synthesis.recommendation
                };
            }

            // Create new synthesis
            return {
                type: 'new_synthesis',
                patterns: patterns,
                approach: 'create_synthesis',
                features: this.mergePatternFeatures(patterns),
                implementation: this.generateSynthesisImplementation(patterns),
                reasoning: 'Create new synthesis from multiple patterns'
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
        console.log('Issue detected: $2');
            return {
                type: 'fallback',
                patterns: patterns,
                approach: 'use_highest_quality',
                reasoning: 'Synthesis failed - use highest quality pattern'
            };
        }
    }

    /**
     * EXTRACT PATTERN FEATURES
     */
    extractPatternFeatures(pattern) {
        const features = [];
        
        if (pattern.metadata?.responsive) features.push('Responsive Design');
        if (pattern.metadata?.cultural) features.push('Cultural Integration');
        if (pattern.metadata?.accessibility) features.push('Accessibility');
        if (pattern.metadata?.performance) features.push('Performance Optimized');
        if (pattern.metadata?.teaching_variants) features.push('Teaching Variants');
        
        return features;
    }

    /**
     * MERGE PATTERN FEATURES
     */
    mergePatternFeatures(patterns) {
        const allFeatures = patterns.flatMap(p => this.extractPatternFeatures(p));
        return [...new Set(allFeatures)]; // Remove duplicates
    }

    /**
     * GENERATE IMPLEMENTATION GUIDE
     */
    generateImplementationGuide(pattern) {
        return {
            steps: [
                '1. Study the legacy pattern implementation',
                '2. Understand the design principles used',
                '3. Adapt to current context while preserving core wisdom',
                '4. Test with target audience',
                '5. Document as new legacy pattern if successful'
            ],
            keyPrinciples: this.extractKeyPrinciples(pattern),
            commonPitfalls: this.identifyCommonPitfalls(pattern),
            qualityChecks: this.generateQualityChecks(pattern)
        };
    }

    /**
     * GENERATE SYNTHESIS IMPLEMENTATION
     */
    generateSynthesisImplementation(patterns) {
        return {
            steps: [
                '1. Analyze all legacy patterns',
                '2. Identify common successful elements',
                '3. Extract unique valuable features from each',
                '4. Create unified implementation',
                '5. Test synthesis approach',
                '6. Document as new synthesis pattern'
            ],
            synthesisApproach: 'Take best features from each pattern',
            conflictResolution: 'Prioritize user experience and cultural integration',
            testingStrategy: 'A/B test against individual patterns'
        };
    }

    /**
     * EXTRACT KEY PRINCIPLES
     */
    extractKeyPrinciples(pattern) {
        const principles = [];
        
        if (pattern.metadata?.legacy_gold) {
            principles.push('Proven in production');
        }
        
        if (pattern.quality_score >= 95) {
            principles.push('High quality implementation');
        }
        
        if (pattern.metadata?.cultural) {
            principles.push('Cultural sensitivity');
        }
        
        if (pattern.metadata?.teaching_variants) {
            principles.push('Pedagogical flexibility');
        }

        return principles;
    }

    /**
     * IDENTIFY COMMON PITFALLS
     */
    identifyCommonPitfalls(pattern) {
        const pitfalls = [];
        
        if (pattern.metadata?.legacy_gold && !pattern.metadata?.modernized) {
            pitfalls.push('May need modernization for current standards');
        }
        
        if (pattern.metadata?.specific_context) {
            pitfalls.push('Context-specific - may not generalize');
        }
        
        if (pattern.quality_score < 90) {
            pitfalls.push('Quality concerns - review implementation');
        }

        return pitfalls;
    }

    /**
     * GENERATE QUALITY CHECKS
     */
    generateQualityChecks(pattern) {
        return [
            'Responsive design across devices',
            'Cultural appropriateness',
            'Accessibility compliance',
            'Performance optimization',
            'User experience testing',
            'Code maintainability'
        ];
    }

    /**
     * PRESERVE NEW PATTERN
     * When a new pattern is successfully created
     */
    async preserveNewPattern(patternData) {
        try {
            const { data, error } = await this.evolution.supabase
                .from('graphrag_resources')
                .insert({
                    file_path: `_legacy_patterns/${patternData.name}`,
                    title: patternData.title,
                    content_preview: patternData.description,
                    metadata: {
                        type: 'legacy_pattern',
                        legacy_gold: true,
                        created_date: new Date().toISOString(),
                        creator: patternData.creator || 'system',
                        ...patternData.metadata
                    },
                    quality_score: patternData.quality || 90
                })
                .select();

            if (!error) {
                // Refresh local cache
                await this.loadLegacyPatterns();
                return { success: true, data };
            }

            return { success: false, error };
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
        console.log('Issue detected: $2');
            return { success: false, error };
        }
    }

    /**
     * GET LEGACY WISDOM SUMMARY
     */
    getLegacyWisdomSummary() {
        const summary = {
            totalPatterns: this.legacyPatterns.length,
            highQuality: this.legacyPatterns.filter(p => p.quality_score >= 95).length,
            cultural: this.legacyPatterns.filter(p => p.metadata?.cultural).length,
            teaching: this.legacyPatterns.filter(p => p.metadata?.teaching_variants).length,
            responsive: this.legacyPatterns.filter(p => p.metadata?.responsive).length,
            topPatterns: this.legacyPatterns
                .sort((a, b) => b.quality_score - a.quality_score)
                .slice(0, 5)
                .map(p => ({
                    title: p.title,
                    quality: p.quality_score,
                    features: this.extractPatternFeatures(p)
                }))
        };

        return summary;
    }

    /**
     * CLEAR ANALYSIS CACHE
     */
    clearCache() {
        this.analysisCache.clear();
    }

    /**
     * GET CACHE STATS
     */
    getCacheStats() {
        return {
            analysisCache: this.analysisCache.size,
            legacyPatterns: this.legacyPatterns.length
        };
    }
}

// Auto-initialize and expose globally
window.LegacyAnalyzer = new LegacyPatternAnalyzer();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LegacyPatternAnalyzer;
}

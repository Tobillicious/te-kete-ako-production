/**
 * Smart Recommendation Engine - Te Kete Ako
 * Uses GraphRAG intelligence for context-aware recommendations
 * Leverages system principles, teaching variants, and cultural patterns
 */

class SmartRecommendationEngine {
    constructor() {
        this.evolution = window.GraphRAGEvolution;
        this.coordinator = window.AgentCoordinator;
        this.recommendationCache = new Map();
        this.init();
    }

    async init() {
        if (!this.evolution) {
            setTimeout(() => this.init(), 1000);
            return;
        }
        
        await this.evolution.loadSystemIntelligence();
    }

    /**
     * CONTEXT-AWARE RECOMMENDATIONS
     * Use GraphRAG relationships + system intelligence
     */
    async getContextualRecommendations(currentPath, userContext = {}) {
        const cacheKey = `${currentPath}_${JSON.stringify(userContext)}`;
        
        if (this.recommendationCache.has(cacheKey)) {
            return this.recommendationCache.get(cacheKey);
        }

        try {
            // Get base recommendations from GraphRAG relationships
            const { data: relationships } = await this.evolution.supabase
                .from('graphrag_relationships')
                .select('target_path, relationship_type, confidence, metadata')
                .eq('source_path', currentPath)
                .gte('confidence', 0.6)
                .order('confidence', { ascending: false })
                .limit(20);

            if (!relationships || relationships.length === 0) {
                return this.getFallbackRecommendations(userContext);
            }

            // Enhance with system intelligence
            const enhanced = await this.enhanceRecommendations(relationships, userContext);
            
            // Apply intelligent filtering and ranking
            const ranked = this.rankRecommendations(enhanced, userContext);
            
            // Cache for performance
            this.recommendationCache.set(cacheKey, ranked);
            
            return ranked;
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
            return this.getFallbackRecommendations(userContext);
        }
    }

    /**
     * ENHANCE RECOMMENDATIONS WITH INTELLIGENCE
     */
    async enhanceRecommendations(relationships, userContext) {
        const enhanced = await Promise.all(
            relationships.map(async (rel) => {
                const { data: resource } = await this.evolution.supabase
                    .from('graphrag_resources')
                    .select('*')
                    .eq('file_path', rel.target_path)
                    .single();

                if (!resource) return null;

                const enhancement = {
                    ...resource,
                    relationship: rel.relationship_type,
                    confidence: rel.confidence,
                    priority: 'medium',
                    reasons: []
                };

                // Apply system intelligence enhancements
                await this.applySystemIntelligence(enhancement, userContext);
                await this.applyCulturalIntelligence(enhancement, userContext);
                await this.applyTeachingIntelligence(enhancement, userContext);
                await this.applyLegacyIntelligence(enhancement, userContext);

                return enhancement;
            })
        );

        return enhanced.filter(e => e !== null);
    }

    /**
     * APPLY SYSTEM INTELLIGENCE
     */
    async applySystemIntelligence(enhancement, userContext) {
        // Check if resource follows system principles
        const principles = this.evolution.systemPrinciples;
        
        for (const principle of principles) {
            if (this.matchesPrinciple(enhancement, principle)) {
                enhancement.priority = 'high';
                enhancement.reasons.push(`Follows principle: ${principle.title}`);
            }
        }

        // Check for anti-patterns
        const antiPatterns = this.evolution.sessionLearnings.filter(l => 
            l.title.includes('anti-pattern') || l.title.includes('bloat')
        );

        for (const pattern of antiPatterns) {
            if (this.matchesAntiPattern(enhancement, pattern)) {
                enhancement.priority = 'low';
                enhancement.reasons.push(`⚠️ Anti-pattern: ${pattern.title}`);
            }
        }
    }

    /**
     * APPLY CULTURAL INTELLIGENCE
     */
    async applyCulturalIntelligence(enhancement, userContext) {
        if (userContext.culturalFocus && enhancement.metadata?.cultural) {
            enhancement.priority = 'high';
            enhancement.reasons.push('Cultural integration focus');
        }

        if (enhancement.metadata?.te_ao_maori) {
            enhancement.priority = 'high';
            enhancement.reasons.push('Te Ao Māori content');
        }

        if (enhancement.metadata?.whakatauki) {
            enhancement.reasons.push('Contains Whakataukī (Māori proverb)');
        }
    }

    /**
     * APPLY TEACHING INTELLIGENCE
     */
    async applyTeachingIntelligence(enhancement, userContext) {
        if (enhancement.metadata?.teaching_variants) {
            enhancement.reasons.push('Multiple teaching approaches available');
        }

        if (enhancement.metadata?.year_level) {
            const yearMatch = userContext.yearLevel === enhancement.metadata.year_level;
            if (yearMatch) {
                enhancement.priority = 'high';
                enhancement.reasons.push(`Perfect year level match: ${enhancement.metadata.year_level}`);
            }
        }

        if (enhancement.metadata?.subject) {
            const subjectMatch = userContext.subject === enhancement.metadata.subject;
            if (subjectMatch) {
                enhancement.priority = 'high';
                enhancement.reasons.push(`Subject match: ${enhancement.metadata.subject}`);
            }
        }
    }

    /**
     * APPLY LEGACY INTELLIGENCE
     */
    async applyLegacyIntelligence(enhancement, userContext) {
        if (enhancement.metadata?.legacy_gold) {
            enhancement.priority = 'high';
            enhancement.reasons.push('Proven legacy design');
        }

        if (enhancement.quality_score >= 95) {
            enhancement.reasons.push('High quality score');
        }
    }

    /**
     * RANK RECOMMENDATIONS INTELLIGENTLY
     */
    rankRecommendations(enhanced, userContext) {
        return enhanced
            .sort((a, b) => {
                // Priority scoring
                const priorityScore = { high: 3, medium: 2, low: 1 };
                const aPriority = priorityScore[a.priority] || 2;
                const bPriority = priorityScore[b.priority] || 2;
                
                if (aPriority !== bPriority) {
                    return bPriority - aPriority;
                }
                
                // Then by confidence
                return b.confidence - a.confidence;
            })
            .slice(0, 8); // Top 8 recommendations
    }

    /**
     * TEACHING VARIANT RECOMMENDATIONS
     * Special handling for lesson content
     */
    async getTeachingVariants(lessonPath, userContext = {}) {
        try {
            const variants = await this.evolution.synthesizeTeachingVariants(lessonPath);
            
            if (variants.needsSynthesis) {
                return {
                    type: 'teaching_variants',
                    display: 'variants_card',
                    variants: variants.variants,
                    reasoning: variants.reasoning,
                    maxDisplay: 3,
                    showDifferences: true
                };
            }

            return {
                type: 'single_variant',
                variant: variants.variants[0],
                reasoning: 'Optimal single variant'
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
            return { type: 'error', message: 'Unable to load teaching variants' };
        }
    }

    /**
     * CULTURAL CONTEXT RECOMMENDATIONS
     * Enhance with Te Ao Māori context
     */
    async getCulturalRecommendations(currentPath, culturalContext = {}) {
        try {
            const { data: cultural } = await this.evolution.supabase
                .from('graphrag_resources')
                .select('*')
                .or('metadata->>cultural.eq.true,metadata->>te_ao_maori.eq.true,metadata->>whakatauki.eq.true')
                .gte('quality_score', 80)
                .order('quality_score', { ascending: false })
                .limit(5);

            return cultural?.map(c => ({
                ...c,
                type: 'cultural',
                culturalElements: this.extractCulturalElements(c),
                display: 'cultural_card'
            })) || [];
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
            return [];
        }
    }

    /**
     * EXTRACT CULTURAL ELEMENTS
     */
    extractCulturalElements(resource) {
        const elements = [];
        
        if (resource.metadata?.te_ao_maori) elements.push('Te Ao Māori');
        if (resource.metadata?.whakatauki) elements.push('Whakataukī');
        if (resource.metadata?.cultural) elements.push('Cultural Integration');
        if (resource.metadata?.maori_language) elements.push('Te Reo Māori');
        
        return elements;
    }

    /**
     * FALLBACK RECOMMENDATIONS
     * When GraphRAG relationships are sparse
     */
    getFallbackRecommendations(userContext) {
        return [
            {
                title: 'Explore Discovery Tools',
                file_path: '/discovery-tools.html',
                type: 'fallback',
                priority: 'medium',
                reasons: ['Discovery tools for content exploration']
            },
            {
                title: 'Browse Learning Pathways',
                file_path: '/learning-pathways-visualizer.html',
                type: 'fallback',
                priority: 'medium',
                reasons: ['Visual learning pathway exploration']
            }
        ];
    }

    /**
     * UTILITY METHODS
     */
    matchesPrinciple(resource, principle) {
        // Simple matching - could be enhanced with NLP
        return resource.title.toLowerCase().includes(principle.title.toLowerCase()) ||
               resource.content_preview?.toLowerCase().includes(principle.title.toLowerCase());
    }

    matchesAntiPattern(resource, pattern) {
        return resource.title.toLowerCase().includes(pattern.title.toLowerCase()) ||
               resource.content_preview?.toLowerCase().includes(pattern.title.toLowerCase());
    }

    /**
     * CLEAR CACHE
     */
    clearCache() {
        this.recommendationCache.clear();
    }

    /**
     * GET CACHE STATS
     */
    getCacheStats() {
        return {
            size: this.recommendationCache.size,
            keys: Array.from(this.recommendationCache.keys())
        };
    }
}

// Auto-initialize and expose globally
window.SmartRecommendations = new SmartRecommendationEngine();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SmartRecommendationEngine;
}

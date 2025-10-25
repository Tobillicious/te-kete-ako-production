/**
 * GraphRAG Self-Evolution Engine - Te Kete Ako
 * Uses GraphRAG intelligence to evolve itself and guide agent development
 * Queries system principles, dev patterns, and session learnings for decisions
 */

class GraphRAGSelfEvolutionEngine {
    constructor() {
        this.supabase = null;
        this.systemPrinciples = [];
        this.devPatterns = [];
        this.agentRules = [];
        this.sessionLearnings = [];
        this.init();
    }

    async init() {
        await this.initializeSupabase();
        await this.loadSystemIntelligence();
    }

    async initializeSupabase() {
        if (window.supabaseSingleton) {
            this.supabase = await window.supabaseSingleton.getClient();
        }
    }

    /**
     * Load all system intelligence from GraphRAG
     */
    async loadSystemIntelligence() {
        try {
            // Load system principles
            const { data: principles } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('metadata->>type', 'system_principle')
                .gte('quality_score', 95);
            
            this.systemPrinciples = principles || [];

            // Load dev patterns
            const { data: patterns } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .ilike('file_path', '%_dev_patterns%');
            
            this.devPatterns = patterns || [];

            // Load agent rules
            const { data: rules } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .ilike('file_path', '%_agent_rules%');
            
            this.agentRules = rules || [];

            // Load session learnings
            const { data: learnings } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .ilike('file_path', '%_session_learnings%');
            
            this.sessionLearnings = learnings || [];

            console.log('📊 GraphRAG Engine Loaded:', {
                principles: this.systemPrinciples.length,
                patterns: this.devPatterns.length,
                rules: this.agentRules.length,
                learnings: this.sessionLearnings.length
            });
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
     * INTELLIGENT DECISION ENGINE
     * Query GraphRAG before making any development decision
     */
    async shouldCreateFile(filePath, fileType) {
        // Check MD prohibition rule
        if (filePath.endsWith('.md')) {
            const mdRule = this.agentRules.find(r => r.file_path.includes('md_prohibition'));
            if (mdRule) {
                return {
                    allowed: false,
                    reason: 'MD Prohibition: GraphRAG is source of truth. Use GraphRAG instead.',
                    alternative: 'Store knowledge in graphrag_resources table'
                };
            }
        }

        // Check for existing patterns
        const existingPattern = await this.findExistingPattern(fileType);
        if (existingPattern) {
            return {
                allowed: true,
                reason: 'Pattern exists - follow existing implementation',
                pattern: existingPattern
            };
        }

        return { allowed: true, reason: 'No conflicts found' };
    }

    /**
     * LEGACY INTELLIGENCE
     * Query legacy patterns before creating new components
     */
    async findLegacyPattern(componentType) {
        try {
            const { data } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('metadata->>legacy_gold', 'true')
                .ilike('title', `%${componentType}%`)
                .order('quality_score', { ascending: false })
                .limit(1);

            return data?.[0] || null;
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
            return null;
        }
    }

    /**
     * HEGELIAN SYNTHESIS DECISION
     * Use dialectical approach for design decisions
     */
    async hegelianSynthesis(thesis, antithesis) {
        // Query GraphRAG for similar synthesis patterns
        try {
            const { data } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('metadata->>type', 'design_synthesis_pattern')
                .or(`title.ilike.%${thesis}%,title.ilike.%${antithesis}%`);

            if (data && data.length > 0) {
                return {
                    hasPrecedent: true,
                    synthesis: data[0].metadata.synthesis_approach,
                    features: data[0].metadata.features,
                    recommendation: 'Follow proven synthesis pattern'
                };
            }

            return {
                hasPrecedent: false,
                recommendation: 'Create new synthesis and index in GraphRAG'
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
            return { hasPrecedent: false };
        }
    }

    /**
     * TEACHING VARIANT SYNTHESIS
     * Intelligently synthesize teaching content variants
     */
    async synthesizeTeachingVariants(lessonPath) {
        try {
            // Find all variants of this lesson
            const lessonName = lessonPath.split('/').pop().replace('.html', '');
            
            const { data: variants } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .ilike('file_path', `%${lessonName}%`)
                .eq('metadata->>type', 'lesson')
                .gte('quality_score', 75)
                .order('quality_score', { ascending: false });

            if (!variants || variants.length <= 3) {
                return { needsSynthesis: false, variants };
            }

            // Apply intelligent synthesis: top 3 by quality + diversity
            const synthesized = this.selectDiverseVariants(variants, 3);

            return {
                needsSynthesis: true,
                original: variants.length,
                synthesized: synthesized.length,
                variants: synthesized,
                reasoning: 'Teaching Variants System: Offer 2-3 distinct pedagogical choices'
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
            return { needsSynthesis: false };
        }
    }

    /**
     * Select diverse variants based on metadata differences
     */
    selectDiverseVariants(variants, maxCount = 3) {
        if (variants.length <= maxCount) return variants;

        const selected = [variants[0]]; // Always include highest quality
        
        for (let i = 1; i < variants.length && selected.length < maxCount; i++) {
            const candidate = variants[i];
            const isDiverse = selected.every(v => 
                this.calculateDiversity(v.metadata, candidate.metadata) > 0.3
            );
            
            if (isDiverse) {
                selected.push(candidate);
            }
        }

        return selected;
    }

    /**
     * Calculate diversity score between two metadata objects
     */
    calculateDiversity(meta1, meta2) {
        const keys = new Set([...Object.keys(meta1 || {}), ...Object.keys(meta2 || {})]);
        let differences = 0;
        
        for (const key of keys) {
            if (meta1?.[key] !== meta2?.[key]) {
                differences++;
            }
        }
        
        return differences / keys.size;
    }

    /**
     * INTELLIGENT RECOMMENDATION ENGINE
     * Use GraphRAG relationships + system intelligence for recommendations
     */
    async getIntelligentRecommendations(currentPath, userContext = {}) {
        try {
            // Get base recommendations from relationships
            const { data: relationships } = await this.supabase
                .from('graphrag_relationships')
                .select('target_path, relationship_type, confidence, metadata')
                .eq('source_path', currentPath)
                .gte('confidence', 0.7)
                .order('confidence', { ascending: false })
                .limit(10);

            if (!relationships) return [];

            // Enhance with system intelligence
            const enhanced = await Promise.all(
                relationships.map(async (rel) => {
                    const { data: resource } = await this.supabase
                        .from('graphrag_resources')
                        .select('*')
                        .eq('file_path', rel.target_path)
                        .single();

                    if (!resource) return null;

                    // Apply intelligent filtering
                    if (resource.metadata?.legacy_gold && !userContext.preferLegacy) {
                        resource.priority = 'high';
                        resource.reason = 'Proven legacy design';
                    }

                    if (resource.metadata?.cultural && userContext.culturalFocus) {
                        resource.priority = 'high';
                        resource.reason = 'Cultural integration';
                    }

                    if (resource.metadata?.teaching_variants) {
                        resource.priority = 'medium';
                        resource.reason = 'Pedagogical choice available';
                    }

                    return {
                        ...resource,
                        relationship: rel.relationship_type,
                        confidence: rel.confidence
                    };
                })
            );

            return enhanced.filter(e => e !== null);
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
     * ANTI-PATTERN DETECTION
     * Check session learnings for known anti-patterns
     */
    async detectAntiPatterns(action, context) {
        const antiPatterns = this.sessionLearnings.filter(l => 
            l.title.includes('anti-pattern') || l.title.includes('bloat')
        );

        for (const pattern of antiPatterns) {
            if (action.type === 'homepage_modification' && pattern.file_path.includes('homepage_bloat')) {
                return {
                    detected: true,
                    pattern: pattern.title,
                    warning: 'Homepage bloat anti-pattern detected',
                    recommendation: pattern.content_preview
                };
            }
        }

        return { detected: false };
    }

    /**
     * CONTINUOUS EVOLUTION
     * GraphRAG learns from new patterns and stores them
     */
    async evolveSelf(newPattern) {
        try {
            // Determine if this is a new pattern worth storing
            const isNovel = await this.isNovelPattern(newPattern);
            
            if (isNovel) {
                const { data, error } = await this.supabase
                    .from('graphrag_resources')
                    .insert({
                        file_path: `_learned_patterns/${newPattern.name}`,
                        title: newPattern.title,
                        content_preview: newPattern.description,
                        metadata: {
                            type: 'learned_pattern',
                            date: new Date().toISOString(),
                            learned_from: newPattern.source,
                            ...newPattern.metadata
                        },
                        quality_score: newPattern.quality || 85
                    })
                    .select();

                if (!error) {
                    return { success: true, data };
                }
            }

            return { success: false, reason: 'Pattern already exists' };
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
     * Check if pattern is novel
     */
    async isNovelPattern(newPattern) {
        try {
            const { data } = await this.supabase
                .from('graphrag_resources')
                .select('id')
                .ilike('title', `%${newPattern.title}%`)
                .limit(1);

            return !data || data.length === 0;
        } catch (error) {
            return true; // If check fails, assume novel
        }
    }

    /**
     * Find existing pattern by type
     */
    async findExistingPattern(type) {
        try {
            const { data } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .ilike('file_path', `%_dev_patterns%${type}%`)
                .order('quality_score', { ascending: false })
                .limit(1);

            return data?.[0] || null;
        } catch (error) {
            return null;
        }
    }

    /**
     * EXPORT AGENT GUIDANCE
     * Provide structured guidance for agent development
     */
    getAgentGuidance() {
        return {
            principles: this.systemPrinciples.map(p => ({
                principle: p.title,
                priority: p.metadata?.priority,
                action: p.metadata?.action
            })),
            rules: this.agentRules.map(r => ({
                rule: r.title,
                enforcement: 'strict'
            })),
            patterns: this.devPatterns.map(p => ({
                pattern: p.title,
                usage: 'recommended'
            })),
            learnings: this.sessionLearnings.map(l => ({
                learning: l.title,
                avoid: true
            }))
        };
    }
}

// Auto-initialize and expose globally for agent use
window.GraphRAGEvolution = new GraphRAGSelfEvolutionEngine();

// Export for agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = GraphRAGSelfEvolutionEngine;
}


/**
 * GraphRAG Recommendation Engine
 * Uses relationship data to suggest related resources
 */

(function() {
    // Prevent duplicate declarations
    if (typeof window.GraphRAGRecommendations !== 'undefined') {
        return;
    }

    const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
    const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

    class GraphRAGRecommendations {
    constructor() {
        this.supabase = window.supabase ? window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY) : null;
        this.cache = new Map();
    }

    /**
     * Get recommendations for a specific resource
     * @param {string} resourcePath - File path of the resource
     * @param {Object} options - Recommendation options
     * @returns {Promise<Array>} - Recommended resources
     */
    async getRecommendations(resourcePath, options = {}) {
        const {
            maxResults = 10,
            relationshipTypes = ['prerequisite', 'related', 'variant', 'requires'],
            minQualityScore = 70,
            culturalContext = null,
            yearLevel = null
        } = options;

        // Check cache first
        const cacheKey = `${resourcePath}_${JSON.stringify(options)}`;
        if (this.cache.has(cacheKey)) {
            return this.cache.get(cacheKey);
        }

        try {
            // 1. Get direct relationships
            const { data: relationships, error: relError } = await this.supabase
                .from('graphrag_relationships')
                .select('*')
                .or(`source_path.eq.${resourcePath},target_path.eq.${resourcePath}`)
                .in('relationship_type', relationshipTypes);

            if (relError) throw relError;

            // 2. Extract related resource paths
            const relatedPaths = new Set();
            relationships.forEach(rel => {
                if (rel.source_path === resourcePath) {
                    relatedPaths.add(rel.target_path);
                } else {
                    relatedPaths.add(rel.source_path);
                }
            });

            // 3. Fetch related resources with metadata
            if (relatedPaths.size === 0) {
                return [];
            }

            let query = this.supabase
                .from('graphrag_resources')
                .select('*')
                .in('file_path', Array.from(relatedPaths))
                .gte('quality_score', minQualityScore)
                .order('quality_score', { ascending: false })
                .limit(maxResults);

            // Filter by cultural context if specified
            if (culturalContext) {
                query = query.eq('cultural_context', culturalContext);
            }

            // Filter by year level if specified
            if (yearLevel) {
                query = query.eq('year_level', yearLevel);
            }

            const { data: resources, error: resError } = await query;

            if (resError) throw resError;

            // 4. Enrich with relationship context
            const enrichedResources = resources.map(resource => {
                const relContext = relationships.find(rel => 
                    rel.source_path === resource.file_path || rel.target_path === resource.file_path
                );
                
                return {
                    ...resource,
                    relationship_type: relContext ? relContext.relationship_type : 'related',
                    relationship_metadata: relContext ? relContext.metadata : null,
                    relevance_score: this.calculateRelevanceScore(resource, relContext)
                };
            });

            // 5. Sort by relevance
            enrichedResources.sort((a, b) => b.relevance_score - a.relevance_score);

            // Cache results
            this.cache.set(cacheKey, enrichedResources);

            return enrichedResources;

        } catch (error) {
            console.error('Error getting recommendations:', error);
            return [];
        }
    }

    /**
     * Calculate relevance score for a resource
     */
    calculateRelevanceScore(resource, relationship) {
        let score = resource.quality_score || 50;

        // Boost based on relationship type
        const relationshipBoosts = {
            'prerequisite': 20,
            'requires': 15,
            'related': 10,
            'variant': 8,
            'similar': 5
        };

        if (relationship && relationshipBoosts[relationship.relationship_type]) {
            score += relationshipBoosts[relationship.relationship_type];
        }

        // Boost cultural resources
        if (resource.has_whakataukī) score += 5;
        if (resource.cultural_context) score += 5;
        if (resource.has_te_reo) score += 3;

        return Math.min(score, 100);
    }

    /**
     * Get "Similar Resources" based on multiple factors
     */
    async getSimilarResources(resourcePath, maxResults = 6) {
        try {
            // Get the source resource
            const { data: source, error: sourceError } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('file_path', resourcePath)
                .single();

            if (sourceError || !source) {
                console.error('Source resource not found');
                return [];
            }

            // Find resources with similar attributes
            let query = this.supabase
                .from('graphrag_resources')
                .select('*')
                .neq('file_path', resourcePath) // Exclude self
                .gte('quality_score', 70);

            // Match by subject
            if (source.subject) {
                query = query.eq('subject', source.subject);
            }

            // Match by year level (within ±1 level)
            if (source.year_level) {
                query = query.or(`year_level.eq.${source.year_level},year_level.eq.${parseInt(source.year_level) + 1},year_level.eq.${parseInt(source.year_level) - 1}`);
            }

            const { data: similar, error: simError } = await query.limit(maxResults * 2);

            if (simError) throw simError;

            // Calculate similarity scores
            const scored = similar.map(res => ({
                ...res,
                similarity_score: this.calculateSimilarityScore(source, res)
            }));

            // Sort and limit
            scored.sort((a, b) => b.similarity_score - a.similarity_score);
            return scored.slice(0, maxResults);

        } catch (error) {
            console.error('Error getting similar resources:', error);
            return [];
        }
    }

    /**
     * Calculate similarity score between two resources
     */
    calculateSimilarityScore(source, target) {
        let score = 0;

        // Exact subject match
        if (source.subject === target.subject) score += 30;

        // Exact year level match
        if (source.year_level === target.year_level) score += 20;

        // Resource type match
        if (source.resource_type === target.resource_type) score += 15;

        // Cultural attributes match
        if (source.has_whakataukī && target.has_whakataukī) score += 10;
        if (source.cultural_context && target.cultural_context) score += 10;

        // Quality score proximity
        const qualityDiff = Math.abs((source.quality_score || 50) - (target.quality_score || 50));
        score += Math.max(0, 15 - qualityDiff / 5);

        return score;
    }

    /**
     * Get learning pathway (prerequisite chain)
     */
    async getLearningPathway(resourcePath) {
        try {
            const pathway = [];
            const visited = new Set();
            
            // Recursive function to build prerequisite chain
            const buildChain = async (path, depth = 0) => {
                if (depth > 10 || visited.has(path)) return; // Prevent infinite loops
                visited.add(path);

                // Get prerequisite relationships
                const { data: prereqs } = await this.supabase
                    .from('graphrag_relationships')
                    .select('*, source:graphrag_resources!graphrag_relationships_source_path_fkey(*)')
                    .eq('target_path', path)
                    .eq('relationship_type', 'prerequisite');

                if (prereqs && prereqs.length > 0) {
                    for (const prereq of prereqs) {
                        await buildChain(prereq.source_path, depth + 1);
                    }
                }

                // Get the resource details
                const { data: resource } = await this.supabase
                    .from('graphrag_resources')
                    .select('*')
                    .eq('file_path', path)
                    .single();

                if (resource) {
                    pathway.push({
                        ...resource,
                        depth
                    });
                }
            };

            await buildChain(resourcePath);

            // Sort by depth (prerequisites first)
            pathway.sort((a, b) => b.depth - a.depth);

            return pathway;

        } catch (error) {
            console.error('Error building learning pathway:', error);
            return [];
        }
    }

    /**
     * Clear recommendation cache
     */
    clearCache() {
        this.cache.clear();
    }

    // Export to global scope
    window.GraphRAGRecommendations = GraphRAGRecommendations;

    // Initialize global instance
    window.graphRAGRecommendations = new GraphRAGRecommendations();

    // Export for module systems
    if (typeof module !== 'undefined' && module.exports) {
        module.exports = GraphRAGRecommendations;
    }
})();

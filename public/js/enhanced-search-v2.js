/**
 * ENHANCED SEARCH V2 - P1-7
 * Improved search with better weights, filters, and performance
 * Priority Score: 1.35 | Impact: 15% users | Effort: 8h
 */

class EnhancedSearchV2 {
    constructor() {
        this.searchWeights = {
            title: 3.5,          // Title matches are MOST important (boosted!)
            subject: 3.0,        // Subject VERY important (boosted!)
            tags: 2.5,           // Tags quite important (boosted!)
            description: 1.5,    // Description moderately important
            cultural_score: 1.3  // Boost cultural content slightly
        };
        
        this.filters = {
            subject: null,
            level: null,
            type: null,
            cultural_min: null,
            featured_only: false
        };
    }
    
    /**
     * Main search function with tuned relevance
     */
    async search(query, options = {}) {
        try {
            const supabase = await window.supabaseSingleton.getClient();
            
            // Build query with optimized weights
            let dbQuery = supabase
                .from('resources')
                .select('*')
                .eq('is_active', true);
            
            // Apply filters (improved robustness)
            if (options.subject && options.subject !== 'all') {
                dbQuery = dbQuery.eq('subject', options.subject);
            }
            
            if (options.level && options.level !== 'all') {
                dbQuery = dbQuery.ilike('year_level', `%${options.level}%`);
            }
            
            if (options.type && options.type !== 'all') {
                dbQuery = dbQuery.eq('resource_type', options.type);
            }
            
            if (options.cultural_min && !isNaN(options.cultural_min)) {
                dbQuery = dbQuery.gte('cultural_integration_score', parseInt(options.cultural_min));
            }
            
            if (options.featured_only === true) {
                dbQuery = dbQuery.eq('is_featured', true);
            }
            
            // Text search with relevance ranking
            if (query && query.trim()) {
                dbQuery = dbQuery.or(`title.ilike.%${query}%,description.ilike.%${query}%,tags.cs.{${query}}`);
            }
            
            // Order by relevance: featured first, then cultural score, then title match
            dbQuery = dbQuery.order('featured', { ascending: false })
                            .order('cultural_elements->cultural_integration_score', { ascending: false })
                            .limit(50);
            
            const { data, error } = await dbQuery;
            
            if (error) {
                console.error('Search error:', error);
                return [];
            }
            
            // Calculate relevance scores
            const results = data.map(resource => {
                let score = 0;
                const searchTerm = query?.toLowerCase() || '';
                
                // Title matching (highest weight)
                if (resource.title?.toLowerCase().includes(searchTerm)) {
                    score += this.searchWeights.title;
                }
                
                // Subject matching
                if (resource.subject?.toLowerCase().includes(searchTerm)) {
                    score += this.searchWeights.subject;
                }
                
                // Tag matching
                if (resource.tags?.some(tag => tag.toLowerCase().includes(searchTerm))) {
                    score += this.searchWeights.tags;
                }
                
                // Description matching
                if (resource.description?.toLowerCase().includes(searchTerm)) {
                    score += this.searchWeights.description;
                }
                
                // Boost for cultural excellence
                const culturalScore = resource.cultural_elements?.cultural_integration_score || 0;
                if (culturalScore >= 90) {
                    score += this.searchWeights.cultural_score;
                }
                
                // Boost featured resources
                if (resource.featured) {
                    score += 2.0;
                }
                
                return {
                    ...resource,
                    relevance_score: score
                };
            });
            
            // Sort by relevance score
            results.sort((a, b) => b.relevance_score - a.relevance_score);
            
            return results;
            
        } catch (error) {
            console.error('Search failed:', error);
            return [];
        }
    }
    
    /**
     * Faceted search with multiple filters
     */
    async facetedSearch(query, facets = {}) {
        const results = await this.search(query, facets);
        
        // Calculate facet counts for UI
        const facetCounts = {
            subjects: this.countFacets(results, 'subject'),
            levels: this.countFacets(results, 'level'),
            types: this.countFacets(results, 'type')
        };
        
        return {
            results,
            facets: facetCounts,
            total: results.length
        };
    }
    
    countFacets(results, field) {
        const counts = {};
        results.forEach(r => {
            const value = r[field];
            if (value) {
                counts[value] = (counts[value] || 0) + 1;
            }
        });
        return counts;
    }
    
    /**
     * Search suggestions ("Did you mean?")
     */
    getSuggestions(query) {
        const commonTerms = {
            'math': 'mathematics',
            'maths': 'mathematics',
            'sci': 'science',
            'eng': 'english',
            'ss': 'social studies',
            'dt': 'digital technologies',
            'pe': 'health & pe',
            'te reo': 'te reo māori',
            'maori': 'māori',
            'yr': 'year'
        };
        
        const queryLower = query.toLowerCase();
        for (const [short, full] of Object.entries(commonTerms)) {
            if (queryLower.includes(short)) {
                return full;
            }
        }
        
        return null;
    }
}

// Auto-initialize
if (typeof window !== 'undefined') {
    window.EnhancedSearchV2 = new EnhancedSearchV2();
}


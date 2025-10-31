/**
 * Curriculum V3 API
 * JavaScript interface for querying NZ Curriculum statements from Supabase
 */

const CurriculumAPI = {
    
    /**
     * Get all available learning areas for a curriculum version
     */
    async getLearningAreas(version = 'temataiaho_2025') {
        try {
            const { data, error } = await supabase
                .from('curriculum_statements')
                .select('learning_area')
                .eq('curriculum_version', version)
                .is('archived_at', null)
                .order('learning_area');
            
            if (error) throw error;
            
            // Return unique learning areas
            const unique = [...new Set(data.map(d => d.learning_area))];
            return unique;
        } catch (err) {
            console.error('Error fetching learning areas:', err);
            return [];
        }
    },
    
    /**
     * Get phases for a learning area (Te Mātaiaho 2025)
     */
    async getPhases(learningArea, version = 'temataiaho_2025') {
        try {
            const { data, error } = await supabase
                .from('curriculum_statements')
                .select('phase, year_levels')
                .eq('curriculum_version', version)
                .eq('learning_area', learningArea)
                .not('phase', 'is', null)
                .order('phase');
            
            if (error) throw error;
            
            // Deduplicate and format
            const phasesMap = {};
            data.forEach(item => {
                if (item.phase && !phasesMap[item.phase]) {
                    phasesMap[item.phase] = {
                        phase: item.phase,
                        years: item.year_levels || []
                    };
                }
            });
            
            return Object.values(phasesMap);
        } catch (err) {
            console.error('Error fetching phases:', err);
            return [];
        }
    },
    
    /**
     * Get strands for a learning area and phase
     */
    async getStrands(learningArea, phase, version = 'temataiaho_2025') {
        try {
            const { data, error } = await supabase
                .from('curriculum_statements')
                .select('strand')
                .eq('curriculum_version', version)
                .eq('learning_area', learningArea)
                .eq('phase', phase)
                .not('strand', 'is', null)
                .order('strand');
            
            if (error) throw error;
            
            // Return unique strands
            const unique = [...new Set(data.map(d => d.strand).filter(s => s))];
            return unique;
        } catch (err) {
            console.error('Error fetching strands:', err);
            return [];
        }
    },
    
    /**
     * Get curriculum statements with filters
     */
    async getStatements(filters = {}) {
        try {
            let query = supabase
                .from('curriculum_statements')
                .select('*')
                .is('archived_at', null);
            
            // Apply filters
            if (filters.version) query = query.eq('curriculum_version', filters.version);
            if (filters.learningArea) query = query.eq('learning_area', filters.learningArea);
            if (filters.phase) query = query.eq('phase', filters.phase);
            if (filters.level) query = query.eq('level', filters.level);
            if (filters.strand) query = query.eq('strand', filters.strand);
            if (filters.element) query = query.eq('element', filters.element);
            
            query = query.order('id');
            
            const { data, error } = await query;
            
            if (error) throw error;
            return data || [];
        } catch (err) {
            console.error('Error fetching statements:', err);
            return [];
        }
    },
    
    /**
     * Get statement count for filters
     */
    async getCount(filters = {}) {
        try {
            let query = supabase
                .from('curriculum_statements')
                .select('id', { count: 'exact', head: true })
                .is('archived_at', null);
            
            if (filters.version) query = query.eq('curriculum_version', filters.version);
            if (filters.learningArea) query = query.eq('learning_area', filters.learningArea);
            if (filters.phase) query = query.eq('phase', filters.phase);
            if (filters.strand) query = query.eq('strand', filters.strand);
            
            const { count, error } = await query;
            
            if (error) throw error;
            return count || 0;
        } catch (err) {
            console.error('Error counting statements:', err);
            return 0;
        }
    },
    
    /**
     * Search curriculum statements (full-text)
     */
    async search(searchTerm, limit = 50) {
        try {
            const { data, error } = await supabase
                .rpc('search_curriculum_statements', {
                    search_query: searchTerm,
                    limit_count: limit
                });
            
            if (error) throw error;
            return data || [];
        } catch (err) {
            console.error('Error searching:', err);
            // Fallback to basic text search
            return this.basicSearch(searchTerm, limit);
        }
    },
    
    /**
     * Fallback search using LIKE
     */
    async basicSearch(searchTerm, limit = 50) {
        try {
            const { data, error } = await supabase
                .from('curriculum_statements')
                .select('*')
                .or(`statement_text.ilike.%${searchTerm}%,learning_area.ilike.%${searchTerm}%,strand.ilike.%${searchTerm}%`)
                .is('archived_at', null)
                .limit(limit);
            
            if (error) throw error;
            return data || [];
        } catch (err) {
            console.error('Error in basic search:', err);
            return [];
        }
    },
    
    /**
     * Get navigation structure (cached)
     */
    async getNavigation() {
        try {
            // Try materialized view first
            const { data, error } = await supabase
                .from('curriculum_navigation')
                .select('*')
                .order('curriculum_version, learning_area, phase, level');
            
            if (error) {
                // Fallback to function
                return this.getNavigationFallback();
            }
            
            return data || [];
        } catch (err) {
            console.error('Error fetching navigation:', err);
            return this.getNavigationFallback();
        }
    },
    
    /**
     * Fallback navigation query
     */
    async getNavigationFallback() {
        try {
            const { data, error } = await supabase
                .from('curriculum_statements')
                .select('curriculum_version, learning_area, phase, level, strand, element')
                .is('archived_at', null);
            
            if (error) throw error;
            
            // Group by version/area/phase
            const nav = {};
            data.forEach(item => {
                const key = `${item.curriculum_version}|${item.learning_area}|${item.phase || item.level}`;
                if (!nav[key]) {
                    nav[key] = {
                        curriculum_version: item.curriculum_version,
                        learning_area: item.learning_area,
                        phase: item.phase,
                        level: item.level,
                        strands: new Set(),
                        elements: new Set(),
                        count: 0
                    };
                }
                if (item.strand) nav[key].strands.add(item.strand);
                if (item.element) nav[key].elements.add(item.element);
                nav[key].count++;
            });
            
            // Convert sets to arrays
            return Object.values(nav).map(item => ({
                ...item,
                strands: Array.from(item.strands),
                elements: Array.from(item.elements)
            }));
        } catch (err) {
            console.error('Error in navigation fallback:', err);
            return [];
        }
    },
    
    /**
     * Get database stats
     */
    async getStats() {
        try {
            const { data, error } = await supabase
                .from('curriculum_statements')
                .select('curriculum_version, learning_area, phase, element', { count: 'exact' })
                .is('archived_at', null);
            
            if (error) throw error;
            
            // Calculate stats
            const stats = {
                total: data.length,
                byVersion: {},
                bySubject: {},
                byPhase: {},
                byElement: {}
            };
            
            data.forEach(item => {
                // By version
                stats.byVersion[item.curriculum_version] = (stats.byVersion[item.curriculum_version] || 0) + 1;
                
                // By subject
                stats.bySubject[item.learning_area] = (stats.bySubject[item.learning_area] || 0) + 1;
                
                // By phase
                if (item.phase) {
                    stats.byPhase[item.phase] = (stats.byPhase[item.phase] || 0) + 1;
                }
                
                // By element
                if (item.element) {
                    stats.byElement[item.element] = (stats.byElement[item.element] || 0) + 1;
                }
            });
            
            return stats;
        } catch (err) {
            console.error('Error fetching stats:', err);
            return null;
        }
    }
};

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CurriculumAPI;
}


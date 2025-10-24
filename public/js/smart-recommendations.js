/**
 * Smart Recommendations Engine
 * Uses GraphRAG + AI to provide intelligent content suggestions
 */

class SmartRecommendations {
    constructor() {
        this.supabase = null;
        this.currentPage = null;
        this.initialized = false;
    }

    async init() {
        if (this.initialized) return;

        const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
        const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

        if (window.supabaseSingleton) {
            this.supabase = await window.supabaseSingleton.getClient();
        }
        this.currentPage = window.location.pathname;
        this.initialized = true;
    }

    /**
     * Get smart recommendations for current page
     */
    async getRecommendations(limit = 6) {
        await this.init();

        try {
            // Get current page from GraphRAG
            const { data: current } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('file_path', this.currentPage.replace('/public/', ''))
                .single();

            if (!current) {
                // Fallback: get popular high-quality resources
                return this.getPopularResources(limit);
            }

            // Get related via relationships - ENHANCED WITH FULL GRAPHRAG POWER
            const { data: relationships } = await this.supabase
                .from('graphrag_relationships')
                .select('target_path, relationship_type, confidence, metadata')
                .eq('source_path', current.file_path)
                .in('relationship_type', [
                    'prerequisite',           // Next steps in learning
                    'related_content',        // Related resources (30,217 total!)
                    'has_handout',           // Supplementary materials
                    'shared_cultural_element', // Cultural connections (5,021 total!)
                    'same_subject',          // Same subject resources (46,752!)
                    'unit_contains_lesson',  // Part of same unit
                    'complementary_tool'     // Works well with this
                ])
                .gte('confidence', 0.70)     // Only high-confidence recommendations
                .order('confidence', { ascending: false })
                .limit(limit * 3);

            if (!relationships || relationships.length === 0) {
                return this.getSimilarResources(current, limit);
            }

            // Fetch related resources with smart prioritization
            const paths = relationships.map(r => r.target_path);
            const { data: related } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .in('file_path', paths)
                .limit(limit * 2);

            if (!related) return [];

            // Smart scoring: prioritize by relationship type + confidence
            const scored = related.map(resource => {
                const rel = relationships.find(r => r.target_path === resource.file_path);
                let score = (rel?.confidence || 0.5) * 100;
                
                // Boost scores based on relationship type
                if (rel?.relationship_type === 'prerequisite') score += 20; // Next steps are highest priority!
                if (rel?.relationship_type === 'shared_cultural_element') score += 15; // Cultural connections valued
                if (rel?.relationship_type === 'has_handout') score += 10; // Practical materials
                if (rel?.relationship_type === 'unit_contains_lesson') score += 12; // Related lessons in unit
                
                // Boost quality resources
                if (resource.quality_score) score += resource.quality_score * 0.2;
                if (resource.has_whakataukī) score += 5;
                
                return { ...resource, _recommendationScore: score, _relationshipType: rel?.relationship_type };
            });

            // Sort by score and return top N
            return scored.sort((a, b) => b._recommendationScore - a._recommendationScore).slice(0, limit);

        } catch (error) {
            console.error('Error getting recommendations:', error);
            return this.getPopularResources(limit);
        }
    }

    /**
     * Get similar resources based on metadata
     */
    async getSimilarResources(source, limit = 6) {
        const { data } = await this.supabase
            .from('graphrag_resources')
            .select('*')
            .eq('subject', source.subject)
            .eq('year_level', source.year_level)
            .neq('file_path', source.file_path)
            .gte('quality_score', 80)
            .limit(limit);

        return data || [];
    }

    /**
     * Get popular high-quality resources as fallback
     */
    async getPopularResources(limit = 6) {
        const { data } = await this.supabase
            .from('graphrag_resources')
            .select('*')
            .gte('quality_score', 90)
            .order('quality_score', { ascending: false })
            .limit(limit);

        return data || [];
    }

    /**
     * Render recommendations widget
     */
    async renderWidget(containerId) {
        const recommendations = await this.getRecommendations(6);

        if (recommendations.length === 0) return;

        const container = document.getElementById(containerId);
        if (!container) return;

        let html = `
            <div style="background: linear-gradient(135deg, #f3f4f6, #e5e7eb); border-radius: 16px; padding: 2rem; margin: 2rem 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                <h3 style="margin-top: 0; color: #1f2937; display: flex; align-items: center; gap: 0.5rem;">
                    <span>🧠</span>
                    <span>Smart Recommendations</span>
                    <span style="background: linear-gradient(135deg, #a855f7, #ec4899); color: white; font-size: 0.75rem; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 700;">AI</span>
                </h3>
                <p style="color: #6b7280; margin-bottom: 1.5rem;">Powered by 163,995 relationships across 56 connection types • GraphRAG Intelligence</p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
        `;

        recommendations.forEach(rec => {
            // Get relationship type badge
            let relationshipBadge = '';
            const relType = rec._relationshipType;
            if (relType === 'prerequisite') relationshipBadge = '<span style="background: #3b82f6; color: white; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 600;">📚 Next Step</span>';
            else if (relType === 'shared_cultural_element') relationshipBadge = '<span style="background: #10b981; color: white; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 600;">🌿 Cultural Link</span>';
            else if (relType === 'has_handout') relationshipBadge = '<span style="background: #f59e0b; color: white; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 600;">📄 Handout</span>';
            else if (relType === 'unit_contains_lesson') relationshipBadge = '<span style="background: #8b5cf6; color: white; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 600;">📖 Same Unit</span>';
            
            const matchScore = Math.round(rec._recommendationScore || 0);
            
            html += `
                <a href="${rec.file_path}" style="text-decoration: none; display: block; background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #a855f7; transition: all 0.3s ease; box-shadow: 0 2px 8px rgba(0,0,0,0.05);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 24px rgba(168, 85, 247, 0.3)'" onmouseout="this.style.transform=''; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.05)'">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
                        <h4 style="margin: 0; color: #1f2937; font-size: 1rem; flex: 1;">${rec.title || 'Resource'}</h4>
                        <span style="background: linear-gradient(135deg, #a855f7, #ec4899); color: white; font-size: 0.7rem; padding: 0.25rem 0.5rem; border-radius: 8px; font-weight: 700; white-space: nowrap; margin-left: 0.5rem;">${matchScore}% match</span>
                    </div>
                    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; font-size: 0.75rem;">
                        ${relationshipBadge}
                        ${rec.quality_score ? `<span style="background: #fef3c7; color: #78350f; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 600;">⭐ ${rec.quality_score}</span>` : ''}
                        ${rec.has_whakataukī ? `<span style="background: #d1fae5; color: #065f46; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 600;">🌿 Te Reo</span>` : ''}
                    </div>
                </a>
            `;
        });

        html += `
                </div>
                <p style="margin-top: 1.5rem; font-size: 0.875rem; color: #6b7280; text-align: center;">
                    <a href="/graphrag-brain.html" style="color: #a855f7; font-weight: 600;">🧠 Explore more with the GraphRAG Brain →</a>
                </p>
            </div>
        `;

        container.innerHTML = html;
    }

    /**
     * Get predictive suggestions based on user behavior
     */
    async getPredictiveSuggestions(userProfile) {
        await this.init();

        const { yearLevel, subjects, recentViews } = userProfile;
        
        // Build smart query based on user profile
        let query = this.supabase
            .from('graphrag_resources')
            .select('*')
            .gte('quality_score', 85);

        if (yearLevel) {
            query = query.ilike('year_level', `%Year ${yearLevel}%`);
        }

        if (subjects && subjects.length > 0) {
            const subjectFilter = subjects.map(s => `subject.ilike.%${s}%`).join(',');
            query = query.or(subjectFilter);
        }

        const { data } = await query.limit(10);
        return data || [];
    }

    /**
     * Track user interaction for smarter future recommendations
     */
    async trackInteraction(resourcePath, interactionType = 'view') {
        // Could log to Supabase for ML-powered recommendations later
    }
}

// Initialize global instance
window.SmartRecommendations = new SmartRecommendations();

// Auto-initialize on DOMContentLoaded
window.addEventListener('DOMContentLoaded', async () => {
    // Auto-render if container exists
    const container = document.getElementById('smart-recommendations');
    if (container) {
        await window.SmartRecommendations.renderWidget('smart-recommendations');
    }
});

// Export for modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SmartRecommendations;
}


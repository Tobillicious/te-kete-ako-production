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

        this.supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
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

            // Get related via relationships
            const { data: relationships } = await this.supabase
                .from('graphrag_relationships')
                .select('target_path, relationship_type')
                .eq('source_path', current.file_path)
                .in('relationship_type', ['prerequisite', 'related_content', 'has_handout'])
                .limit(limit * 2);

            if (!relationships || relationships.length === 0) {
                return this.getSimilarResources(current, limit);
            }

            // Fetch related resources
            const paths = relationships.map(r => r.target_path);
            const { data: related } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .in('file_path', paths)
                .gte('quality_score', 75)
                .limit(limit);

            return related || [];

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
                <p style="color: #6b7280; margin-bottom: 1.5rem;">Based on GraphRAG intelligence and your current resource</p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
        `;

        recommendations.forEach(rec => {
            html += `
                <a href="${rec.file_path}" style="text-decoration: none; display: block; background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #a855f7; transition: all 0.3s ease; box-shadow: 0 2px 8px rgba(0,0,0,0.05);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 24px rgba(168, 85, 247, 0.3)'" onmouseout="this.style.transform=''; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.05)'">
                    <h4 style="margin: 0 0 0.5rem 0; color: #1f2937; font-size: 1rem;">${rec.title || 'Resource'}</h4>
                    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; font-size: 0.75rem;">
                        ${rec.quality_score ? `<span style="background: #fef3c7; color: #78350f; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 600;">⭐ ${rec.quality_score}</span>` : ''}
                        ${rec.has_whakataukī ? `<span style="background: #d1fae5; color: #065f46; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 600;">🌿</span>` : ''}
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
        console.log(`📊 Tracked: ${interactionType} on ${resourcePath}`);
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


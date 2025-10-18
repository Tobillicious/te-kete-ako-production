/**
 * GRAPHRAG-POWERED RECOMMENDATIONS
 * Use 5,324 relationships to show related resources
 */

const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

class GraphRAGRecommendations {
    constructor() {
        this.headers = {
            'apikey': SUPABASE_ANON_KEY,
            'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
            'Content-Type': 'application/json'
        };
    }
    
    /**
     * Get related resources using GraphRAG relationships
     */
    async getRelatedResources(resourcePath, limit = 6) {
        try {
            // Get relationships for this resource
            const relResponse = await fetch(
                `${SUPABASE_URL}/rest/v1/graphrag_relationships?source_path=eq.${encodeURIComponent(resourcePath)}&limit=${limit}`,
                { headers: this.headers }
            );
            
            if (!relResponse.ok) return [];
            
            const relationships = await relResponse.json();
            
            // Get the target resources
            const targetPaths = relationships.map(r => r.target_path);
            if (targetPaths.length === 0) return [];
            
            // Fetch resource details
            const resourcesResponse = await fetch(
                `${SUPABASE_URL}/rest/v1/resources?path=in.(${targetPaths.map(p => `"${p}"`).join(',')})`,
                { headers: this.headers }
            );
            
            if (!resourcesResponse.ok) return [];
            
            const resources = await resourcesResponse.json();
            
            // Combine with relationship metadata
            return resources.map(resource => {
                const rel = relationships.find(r => r.target_path === resource.path);
                return {
                    ...resource,
                    relationship_type: rel?.relationship_type,
                    confidence: rel?.confidence
                };
            });
            
        } catch (error) {
            console.error('GraphRAG recommendations error:', error);
            return [];
        }
    }
    
    /**
     * Get recommendations by type
     */
    async getRecommendationsByType(resourcePath, relationshipType = 'same_subject', limit = 4) {
        try {
            const relResponse = await fetch(
                `${SUPABASE_URL}/rest/v1/graphrag_relationships?source_path=eq.${encodeURIComponent(resourcePath)}&relationship_type=eq.${relationshipType}&limit=${limit}`,
                { headers: this.headers }
            );
            
            if (!relResponse.ok) return [];
            
            const relationships = await relResponse.json();
            const targetPaths = relationships.map(r => r.target_path);
            
            if (targetPaths.length === 0) return [];
            
            const resourcesResponse = await fetch(
                `${SUPABASE_URL}/rest/v1/resources?path=in.(${targetPaths.map(p => `"${p}"`).join(',')})`,
                { headers: this.headers }
            );
            
            return resourcesResponse.ok ? await resourcesResponse.json() : [];
            
        } catch (error) {
            console.error('Type-specific recommendations error:', error);
            return [];
        }
    }
    
    /**
     * Render recommendations widget
     */
    async renderRecommendationsWidget(resourcePath, containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;
        
        container.innerHTML = '<div class="loading">Loading recommendations...</div>';
        
        const related = await this.getRelatedResources(resourcePath, 6);
        
        if (related.length === 0) {
            container.innerHTML = '<p style="color: #666;">No related resources yet - check back soon!</p>';
            return;
        }
        
        let html = `
            <div style="background: linear-gradient(135deg, #f0fdfa, #ccfbf1); padding: 2rem; border-radius: 12px; margin: 2rem 0;">
                <h3 style="color: #0f766e; margin-bottom: 1.5rem; font-size: 1.5rem;">
                    🧠 AI-Recommended Related Resources
                </h3>
                <div style="display: grid; gap: 1rem;">
        `;
        
        related.forEach(resource => {
            const relationshipLabel = this.getRelationshipLabel(resource.relationship_type);
            
            html += `
                <a href="${resource.path}" style="
                    display: flex;
                    gap: 1rem;
                    padding: 1rem;
                    background: white;
                    border-radius: 8px;
                    text-decoration: none;
                    color: inherit;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    transition: all 0.2s;
                    border-left: 3px solid #14b8a6;
                " onmouseover="this.style.transform='translateX(4px)'; this.style.boxShadow='0 4px 12px rgba(20,184,166,0.2)'"
                   onmouseout="this.style.transform=''; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)'">
                    <div style="font-size: 2rem;">${this.getTypeIcon(resource.type)}</div>
                    <div style="flex: 1;">
                        <div style="font-weight: 600; color: #0f766e; margin-bottom: 0.25rem;">
                            ${resource.title}
                        </div>
                        <div style="font-size: 0.85rem; color: #64748b;">
                            ${relationshipLabel} • ${resource.type} • ${resource.subject}
                        </div>
                    </div>
                    <div style="color: #14b8a6; font-size: 1.5rem;">→</div>
                </a>
            `;
        });
        
        html += `
                </div>
                <div style="text-align: center; margin-top: 1.5rem; font-size: 0.9rem; color: #0f766e;">
                    Powered by ${related.length} connections from 5,324 GraphRAG relationships
                </div>
            </div>
        `;
        
        container.innerHTML = html;
    }
    
    getRelationshipLabel(type) {
        const labels = {
            'same_subject': 'Same Subject',
            'same_year_level': 'Same Year Level',
            'lesson_has_handout': 'Related Handout',
            'unit_contains_lesson': 'Part of Unit',
            'has_interactive_game': 'Interactive Version',
            'prerequisite': 'Builds On',
            'lesson_sequence': 'Next in Sequence',
            'has_assessment': 'Assessment Available',
            'related_content': 'Related'
        };
        return labels[type] || 'Related';
    }
    
    getTypeIcon(type) {
        const icons = {
            'lesson': '📖',
            'handout': '📄',
            'game': '🎮',
            'unit-plan': '📚',
            'assessment': '📊',
            'interactive': '💻',
            'activity': '🎯'
        };
        return icons[type] || '📄';
    }
}

// Initialize globally
window.graphragRecommendations = new GraphRAGRecommendations();

// Auto-render if element exists
document.addEventListener('DOMContentLoaded', () => {
    const widget = document.getElementById('graphrag-recommendations');
    if (widget && widget.dataset.resourcePath) {
        window.graphragRecommendations.renderRecommendationsWidget(
            widget.dataset.resourcePath,
            'graphrag-recommendations'
        );
    }
});


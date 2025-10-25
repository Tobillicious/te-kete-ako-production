/**
 * ENHANCED GRAPHRAG SEARCH
 * Intelligent search using 8,037 resources + 5,324 relationships
 */

const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

class EnhancedGraphRAGSearch {
    constructor() {
        this.headers = {
            'apikey': SUPABASE_ANON_KEY,
            'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
            'Content-Type': 'application/json'
        };
        this.filters = {
            subject: 'all',
            yearLevel: 'all',
            type: 'all',
            cultural: false
        };
    }
    
    /**
     * Search with filters and GraphRAG intelligence
     */
    async search(query, filters = {}) {
        this.filters = {...this.filters, ...filters};
        
        try {
            // Build query
            let url = `${SUPABASE_URL}/rest/v1/resources?select=*`;
            
            // Text search
            if (query) {
                url += `&or=(title.ilike.*${encodeURIComponent(query)}*,description.ilike.*${encodeURIComponent(query)}*)`;
            }
            
            // Subject filter
            if (this.filters.subject && this.filters.subject !== 'all') {
                url += `&subject=ilike.*${this.filters.subject}*`;
            }
            
            // Type filter
            if (this.filters.type && this.filters.type !== 'all') {
                url += `&type=eq.${this.filters.type}`;
            }
            
            // Year level filter
            if (this.filters.yearLevel && this.filters.yearLevel !== 'all') {
                url += `&level=ilike.*${this.filters.yearLevel}*`;
            }
            
            url += '&limit=50';
            
            const response = await fetch(url, { headers: this.headers });
            if (!response.ok) return [];
            
            let results = await response.json();
            
            // Enhance with GraphRAG data
            results = await this.enhanceWithGraphRAG(results);
            
            // Sort by relevance
            results = this.rankResults(results, query);
            
            return results;
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        return [];
        }
    }
    
    /**
     * Enhance results with GraphRAG relationship data
     */
    async enhanceWithGraphRAG(results) {
        const enhanced = [];
        
        for (const resource of results) {
            // Get relationship count for this resource
            try {
                const relResponse = await fetch(
                    `${SUPABASE_URL}/rest/v1/graphrag_relationships?source_path=eq.${encodeURIComponent(resource.path)}&select=count`,
                    { headers: {...this.headers, 'Prefer': 'count=exact'} }
                );
                
                const relationshipCount = relResponse.ok ? 
                    parseInt(relResponse.headers.get('Content-Range')?.split('/')[1] || '0') : 0;
                
                enhanced.push({
                    ...resource,
                    graphrag: {
                        relationship_count: relationshipCount,
                        is_connected: relationshipCount > 0,
                        connectivity_score: Math.min(relationshipCount / 10, 1) // 0-1 score
                    }
                });
            } catch {
                enhanced.push(resource);
            }
        }
        
        return enhanced;
    }
    
    /**
     * Rank results by relevance + GraphRAG connectivity
     */
    rankResults(results, query) {
        return results.sort((a, b) => {
            // Prioritize exact title matches
            const aExact = a.title.toLowerCase().includes(query?.toLowerCase() || '') ? 10 : 0;
            const bExact = b.title.toLowerCase().includes(query?.toLowerCase() || '') ? 10 : 0;
            
            // Add GraphRAG connectivity bonus
            const aGraphRAG = (a.graphrag?.connectivity_score || 0) * 5;
            const bGraphRAG = (b.graphrag?.connectivity_score || 0) * 5;
            
            // Featured resources bonus
            const aFeatured = a.featured ? 3 : 0;
            const bFeatured = b.featured ? 3 : 0;
            
            const aScore = aExact + aGraphRAG + aFeatured;
            const bScore = bExact + bGraphRAG + bFeatured;
            
            return bScore - aScore;
        });
    }
    
    /**
     * Get autocomplete suggestions
     */
    async getAutocomplete(query, limit = 8) {
        if (!query || query.length < 2) return [];
        
        try {
            const response = await fetch(
                `${SUPABASE_URL}/rest/v1/resources?select=title,path,type,subject&title=ilike.*${encodeURIComponent(query)}*&limit=${limit}`,
                { headers: this.headers }
            );
            
            return response.ok ? await response.json() : [];
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        return [];
        }
    }
    
    /**
     * Render search results with GraphRAG intelligence
     */
    renderResults(results, containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;
        
        if (results.length === 0) {
            container.innerHTML = `
                <div style="text-align: center; padding: 4rem; color: #666;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🔍</div>
                    <p style="font-size: 1.2rem;">No resources found. Try different search terms!</p>
                </div>
            `;
            return;
        }
        
        let html = `
            <div style="margin-bottom: 1.5rem; color: #666;">
                Found <strong>${results.length}</strong> resources${results.length === 50 ? ' (showing first 50)' : ''}
            </div>
            <div style="display: grid; gap: 1.5rem;">
        `;
        
        results.forEach(resource => {
            const relationshipBadge = resource.graphrag?.is_connected ? 
                `<span class="ai-recommended-badge" title="${resource.graphrag.relationship_count} connections">🧠 AI Connected</span>` : '';
            
            html += `
                <div class="search-result-card" style="
                    background: white;
                    padding: 1.5rem;
                    border-radius: 12px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    transition: all 0.2s;
                    border-left: 4px solid ${this.getSubjectColor(resource.subject)};
                " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.15)'"
                   onmouseout="this.style.transform=''; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)'">
                    <div style="display: flex; gap: 1rem; align-items: start;">
                        <div style="font-size: 2.5rem;">${this.getTypeIcon(resource.type)}</div>
                        <div style="flex: 1;">
                            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.3rem;">
                                <a href="${resource.path}" style="color: #1a4d2e; text-decoration: none;">
                                    ${resource.title}
                                </a>
                            </h3>
                            <p style="color: #666; font-size: 0.95rem; margin-bottom: 0.75rem; line-height: 1.5;">
                                ${(resource.description || '').substring(0, 150)}${resource.description?.length > 150 ? '...' : ''}
                            </p>
                            <div class="badge-container">
                                <span class="subject-badge ${resource.subject.toLowerCase().replace(' ', '-')}">${resource.subject}</span>
                                <span class="year-badge">${resource.level}</span>
                                <span class="type-badge">${resource.type}</span>
                                ${relationshipBadge}
                            </div>
                        </div>
                    </div>
                </div>
            `;
        });
        
        html += '</div>';
        container.innerHTML = html;
    }
    
    getSubjectColor(subject) {
        const colors = {
            'Mathematics': '#7c3aed',
            'Science': '#059669',
            'English': '#dc2626',
            'Social Studies': '#ea580c',
            'Te Reo Māori': '#0f766e',
            'Arts': '#be185d',
            'Technology': '#1e40af'
        };
        
        for (const [key, color] of Object.entries(colors)) {
            if (subject.includes(key)) return color;
        }
        return '#1a4d2e';
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
window.enhancedSearch = new EnhancedGraphRAGSearch();


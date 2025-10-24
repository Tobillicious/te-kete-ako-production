/**
 * GraphRAG Real-Time Connection Counter
 * 
 * Replaces fake/hardcoded connection badges with REAL counts from Supabase
 * 
 * Usage:
 * <script src="/js/graphrag-connection-counter.js"></script>
 * <div class="connection-badge" data-resource-path="/public/some-lesson.html">Loading...</div>
 */

const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

class GraphRAGConnectionCounter {
    constructor() {
        this.supabase = null;
        this.cache = new Map();
        this.init();
    }

    async init() {
        // Temporarily disabled to stop console spam during debugging
        console.log('🔇 GraphRAG Connection Counter temporarily disabled for debugging');
        return;
        
        // Initialize Supabase client
        if (window.supabase && window.supabase.createClient) {
            this.supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
            
            // Auto-update all connection badges on page
            this.updateAllBadges();
        } else {
            console.warn('⚠️ Supabase not loaded yet, retrying...');
            setTimeout(() => this.init(), 500);
        }
    }

    /**
     * Get REAL connection count for a resource
     */
    async getConnections(resourcePath) {
        // Check cache first
        if (this.cache.has(resourcePath)) {
            return this.cache.get(resourcePath);
        }

        try {
            // Query actual relationships from GraphRAG
            const { data, error } = await this.supabase
                .from('graphrag_relationships')
                .select('relationship_type, confidence')
                .or(`source_path.eq.${resourcePath},target_path.eq.${resourcePath}`);

            if (error) {
                console.error('GraphRAG query error:', error);
                return null;
            }

            // Count by relationship type
            const byType = {};
            data.forEach(rel => {
                const type = rel.relationship_type || 'unknown';
                byType[type] = (byType[type] || 0) + 1;
            });

            const result = {
                total: data.length,
                byType: byType,
                avgConfidence: data.length > 0 
                    ? data.reduce((sum, r) => sum + (r.confidence || 0), 0) / data.length 
                    : 0
            };

            // Cache for 5 minutes
            this.cache.set(resourcePath, result);
            setTimeout(() => this.cache.delete(resourcePath), 5 * 60 * 1000);

            return result;
        } catch (error) {
            console.error('Connection count error:', error);
            return null;
        }
    }

    /**
     * Update a single badge element
     */
    async updateBadge(element) {
        const resourcePath = element.dataset.resourcePath;
        if (!resourcePath) {
            console.warn('No data-resource-path on element:', element);
            return;
        }

        // Show loading state
        element.innerHTML = '<span style="opacity: 0.6;">⏳ Loading...</span>';

        const connections = await this.getConnections(resourcePath);
        
        if (!connections) {
            element.innerHTML = '❌ Error';
            return;
        }

        // Update badge with REAL count
        if (element.dataset.showBreakdown === 'true') {
            element.innerHTML = this.renderDetailedBadge(connections);
        } else {
            element.innerHTML = this.renderSimpleBadge(connections);
        }
    }

    /**
     * Simple badge: just show total
     */
    renderSimpleBadge(connections) {
        if (connections.total === 0) {
            return `<span style="color: #dc2626;">⚠️ 0 connections (orphaned)</span>`;
        }

        const color = connections.total > 50 ? '#dc2626' : 
                     connections.total > 20 ? '#f59e0b' : 
                     connections.total > 10 ? '#10b981' : '#6b7280';

        return `<span style="color: ${color}; font-weight: 700;">🔗 ${connections.total} connections</span>`;
    }

    /**
     * Detailed badge: show breakdown by type
     */
    renderDetailedBadge(connections) {
        if (connections.total === 0) {
            return `<div style="padding: 1rem; background: #fee2e2; border-left: 4px solid #dc2626; border-radius: 8px;">
                <strong style="color: #991b1b;">⚠️ Orphaned Resource</strong>
                <p style="color: #7f1d1d; font-size: 0.9rem; margin-top: 0.5rem;">
                    This high-quality resource has no connections. Consider linking it to relevant hubs!
                </p>
            </div>`;
        }

        // Sort types by count
        const sorted = Object.entries(connections.byType)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5); // Top 5

        const breakdown = sorted.map(([type, count]) => {
            const emoji = this.getEmojiForType(type);
            return `<div style="display: flex; justify-content: space-between; margin: 0.25rem 0;">
                <span>${emoji} ${this.formatTypeName(type)}</span>
                <strong>${count}</strong>
            </div>`;
        }).join('');

        return `<div style="padding: 1rem; background: #f0fdf4; border-left: 4px solid #10b981; border-radius: 8px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                <strong style="color: #065f46;">🔗 ${connections.total} Total Connections</strong>
                <span style="background: #dcfce7; color: #166534; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem;">
                    ${Math.round(connections.avgConfidence * 100)}% avg confidence
                </span>
            </div>
            <div style="font-size: 0.9rem; color: #047857;">
                ${breakdown}
            </div>
        </div>`;
    }

    /**
     * Get emoji for relationship type
     */
    getEmojiForType(type) {
        const emojiMap = {
            'same_subject': '📚',
            'related_content': '🔗',
            'prerequisite': '📖',
            'shared_cultural_element': '🌿',
            'cross_curricular_link': '🌉',
            'same_year_level': '👥',
            'unit_contains_lesson': '📦',
            'cultural_thread': '🧵'
        };
        return emojiMap[type] || '•';
    }

    /**
     * Format type name for display
     */
    formatTypeName(type) {
        return type
            .split('_')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ');
    }

    /**
     * Update all badges on page
     */
    async updateAllBadges() {
        const badges = document.querySelectorAll('[data-resource-path]');

        // Update in batches to avoid overwhelming the API
        const batchSize = 5;
        for (let i = 0; i < badges.length; i += batchSize) {
            const batch = Array.from(badges).slice(i, i + batchSize);
            await Promise.all(batch.map(badge => this.updateBadge(badge)));
            
            // Small delay between batches
            if (i + batchSize < badges.length) {
                await new Promise(resolve => setTimeout(resolve, 100));
            }
        }

    }

    /**
     * Public API: Get connections for a specific resource
     */
    async getResourceConnections(resourcePath) {
        return await this.getConnections(resourcePath);
    }
}

GraphRAGConnectionCounter.prototype.injectBadgesIfMissing = function(){
    try {
        var selectors = [
            'a[href^="/generated-resources-alpha/"]',
            'a[href^="/units/"]',
            'a[href^="/handouts/"]',
            'a[href^="/integrated-lessons/"]'
        ];
        var links = [];
        selectors.forEach(function(sel){ links = links.concat(Array.from(document.querySelectorAll(sel))); });
        links.forEach(function(a){
            if (!a.querySelector('.connection-badge')) {
                var href = a.getAttribute('href') || '';
                if (!href) return;
                // Normalize to /public path if not already absolute
                var publicPath = href.indexOf('/public/') === 0 ? href : ('/public' + (href.startsWith('/') ? href : ('/' + href)));
                a.style.position = a.style.position || 'relative';
                var b = document.createElement('div');
                b.className = 'connection-badge';
                b.setAttribute('data-resource-path', publicPath);
                b.setAttribute('style','position:absolute; top:-12px; right:12px; background:#e0f2fe; color:#075985; padding:0.35rem 0.75rem; border-radius:18px; font-weight:800; font-size:0.75rem;');
                b.textContent = '🔄 Loading...';
                a.insertBefore(b, a.firstChild);
            }
        });
    } catch (e) { console.warn('Badge auto-inject failed', e); }
};

// Hook into init to inject before updating
const _origInit = GraphRAGConnectionCounter.prototype.init;
GraphRAGConnectionCounter.prototype.init = async function(){
    if (window.supabaseSingleton) {
        this.supabase = await window.supabaseSingleton.getClient();
        // New: inject missing badges
        this.injectBadgesIfMissing();
        // Then update
        this.updateAllBadges();
    } else {
        console.warn('⚠️ Supabase not loaded yet, retrying...');
        setTimeout(() => this.init(), 500);
    }
};

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.graphragCounter = new GraphRAGConnectionCounter();
    });
} else {
    window.graphragCounter = new GraphRAGConnectionCounter();
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = GraphRAGConnectionCounter;
}

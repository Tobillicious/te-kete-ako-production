/**
 * Sidebar GraphRAG Connector - Te Kete Ako
 * Connects intelligent sidebar to GraphRAG for real-time recommendations
 * Phase 2 of Sitewide Excellence
 */

class SidebarGraphRAGConnector {
    constructor() {
        this.supabase = null;
        this.currentPath = window.location.pathname;
        this.init();
    }

    async init() {
        await this.initializeSupabase();
        this.loadSidebarIfNeeded();
    }

    async initializeSupabase() {
        if (window.supabaseSingleton) {
            this.supabase = await window.supabaseSingleton.getClient();
        }
    }

    loadSidebarIfNeeded() {
        // Check if we're on a lesson, unit, or handout page
        const isContentPage = 
            this.currentPath.includes('/lessons/') ||
            this.currentPath.includes('/units/') ||
            this.currentPath.includes('/handouts/') ||
            this.currentPath.includes('/integrated-lessons/');

        if (isContentPage && !document.querySelector('.left-sidebar')) {
            this.injectSidebar();
        }
    }

    async injectSidebar() {
        try {
            // Fetch the intelligent sidebar component
            const response = await fetch('/components/sidebar-intelligent.html');
            const html = await response.text();

            // Find or create sidebar container
            let container = document.getElementById('sidebar-container');
            if (!container) {
                container = document.createElement('div');
                container.id = 'sidebar-container';
                
                // Insert after header/navigation
                const mainContent = document.querySelector('main') || document.querySelector('.content');
                if (mainContent) {
                    mainContent.insertAdjacentElement('beforebegin', container);
                }
            }

            container.innerHTML = html;

            // Initialize GraphRAG connections
            await this.connectToGraphRAG();
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        }
    }

    async connectToGraphRAG() {
        if (!this.supabase) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        return;
        }

        try {
            // Get current resource from GraphRAG
            const { data: currentResource } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('file_path', this.currentPath.replace(/^\//, 'public/'))
                .single();

            if (currentResource) {
                // Get related resources via relationships
                const { data: relationships } = await this.supabase
                    .from('graphrag_relationships')
                    .select(`
                        target_path,
                        relationship_type,
                        confidence
                    `)
                    .eq('source_path', currentResource.file_path)
                    .gte('confidence', 0.7)
                    .order('confidence', { ascending: false })
                    .limit(5);

                if (relationships && relationships.length > 0) {
                    await this.displayGraphRAGResources(relationships);
                }
            }
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        }
    }

    async displayGraphRAGResources(relationships) {
        const container = document.getElementById('sidebar-related-resources');
        if (!container) return;

        try {
            // Fetch resource details for each relationship
            const resourcePromises = relationships.map(async (rel) => {
                const { data } = await this.supabase
                    .from('graphrag_resources')
                    .select('title, file_path, metadata')
                    .eq('file_path', rel.target_path)
                    .single();
                
                return data ? {
                    title: data.title,
                    url: this.convertFilePathToURL(data.file_path),
                    type: data.metadata?.type || 'resource',
                    icon: this.getIconForType(data.metadata?.type)
                } : null;
            });

            const resources = (await Promise.all(resourcePromises)).filter(r => r !== null);

            if (resources.length > 0) {
                container.innerHTML = resources.map(r => 
                    `<li><a href="${r.url}">${r.icon} ${r.title}</a></li>`
                ).join('');
            }
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        }
    }

    convertFilePathToURL(filePath) {
        // Convert "public/units/y8-critical-thinking/lesson-1.html" 
        // to "/units/y8-critical-thinking/lesson-1.html"
        return '/' + filePath.replace(/^public\//, '');
    }

    getIconForType(type) {
        const icons = {
            'lesson': '📖',
            'unit': '📚',
            'handout': '📄',
            'game': '🎮',
            'assessment': '📝',
            'tool': '🔧',
            'component': '🧩'
        };
        return icons[type] || '📌';
    }
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        new SidebarGraphRAGConnector();
    });
} else {
    new SidebarGraphRAGConnector();
}


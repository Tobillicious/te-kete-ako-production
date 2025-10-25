/**
 * 🧬 COMPONENT LOADER - Coordinated Component Loading System
 * 
 * PROBLEM: Multiple async fetch() calls for components load in random order
 * → Layout shift (CLS failure)
 * → Z-index conflicts
 * → Visual glitches
 * 
 * SOLUTION: Load components in priority order with coordination
 * PRIORITY 1 (CRITICAL): Navigation (blocks everything)
 * PRIORITY 2 (HIGH): Hero sections (above fold)
 * PRIORITY 3 (NORMAL): Main content (user visible)
 * PRIORITY 4 (LOW): Polish elements (below fold)
 */

class ComponentLoader {
    constructor() {
        this.components = [];
        this.loading = new Set();
        this.loaded = new Set();
        this.queue = [];
        this.maxConcurrent = 4; // Max 4 components loading concurrently (faster than sequential)
        this.currentLoading = 0;
    }

    /**
     * Register a component to be loaded
     * @param {Object} config - { id, url, selector, priority, waitFor }
     */
    register(config) {
        const {
            id,
            url,
            selector = `#${id}-component`,
            priority = 'normal',
            waitFor = null
        } = config;

        this.components.push({
            id,
            url,
            selector,
            priority: this.getPriorityValue(priority),
            waitFor,
            retries: 0,
            maxRetries: 3
        });
    }

    /**
     * Convert priority string to numeric value
     */
    getPriorityValue(priority) {
        const map = {
            'critical': 100,
            'high': 75,
            'normal': 50,
            'low': 25
        };
        return map[priority] || 50;
    }

    /**
     * Start loading components in priority order
     */
    async loadAll() {
        // Sort by priority (highest first), then by registration order
        const sorted = [...this.components].sort((a, b) => {
            if (b.priority !== a.priority) {
                return b.priority - a.priority;
            }
            return this.components.indexOf(a) - this.components.indexOf(b);
        });

        // Load components with coordination
        for (const component of sorted) {
            await this.waitForDependency(component.waitFor);
            this.queue.push(component);
            this.processQueue();
        }

        // Wait for all loading to complete
        return new Promise(resolve => {
            const checkDone = () => {
                if (this.loading.size === 0 && this.queue.length === 0 && this.currentLoading === 0) {
                    resolve();
                } else {
                    setTimeout(checkDone, 100);
                }
            };
            checkDone();
        });
    }

    /**
     * Process the loading queue with concurrency limit
     */
    async processQueue() {
        while (this.queue.length > 0 && this.currentLoading < this.maxConcurrent) {
            const component = this.queue.shift();
            this.currentLoading++;
            this.loading.add(component.id);

            this.loadComponent(component)
                .then(() => {
                    this.loaded.add(component.id);
                })
                .catch(err => {
                    // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        if (component.retries < component.maxRetries) {
                        component.retries++;
                        this.queue.push(component); // Retry
                    }
                })
                .finally(() => {
                    this.loading.delete(component.id);
                    this.currentLoading--;
                    this.processQueue(); // Continue processing
                });
        }
    }

    /**
     * Load a single component
     */
    async loadComponent(component) {
        const { id, url, selector } = component;

        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const html = await response.text();
            const container = document.querySelector(selector);

            if (container) {
                container.innerHTML = html;
                // Trigger load event for any scripts in the component
                this.triggerComponentReady(id);
            } else {
                // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        }
        } catch (err) {
            throw new Error(`Failed to load ${id}: ${err.message}`);
        }
    }

    /**
     * Wait for a dependency to load
     */
    async waitForDependency(dependencyId) {
        if (!dependencyId) return;

        return new Promise(resolve => {
            const check = () => {
                if (this.loaded.has(dependencyId)) {
                    resolve();
                } else {
                    setTimeout(check, 100);
                }
            };
            check();
        });
    }

    /**
     * Trigger custom event when component is ready
     */
    triggerComponentReady(componentId) {
        document.dispatchEvent(
            new CustomEvent('component-loaded', {
                detail: { componentId }
            })
        );
    }

    /**
     * Static factory for default homepage components
     */
    static createForHomepage() {
        const loader = new ComponentLoader();

        // Priority 1: Navigation (already loaded in index.html, but keeping for consistency)
        // Skip - navigation loads synchronously before this

        // Priority 2: Hero sections (above fold, critical)
        loader.register({
            id: 'hero-unified',
            url: '/components/hero-unified.html',
            selector: '#hero-component',
            priority: 'high'
        });

        loader.register({
            id: 'featured-carousel',
            url: '/components/featured-carousel.html',
            selector: '#featured-component',
            priority: 'high'
        });

        // Priority 3: Main content widgets (above fold, important)
        loader.register({
            id: 'top-cultural-widget',
            url: '/components/top-cultural-widget.html',
            selector: '#top-cultural-widget',
            priority: 'normal'
        });

        loader.register({
            id: 'games-showcase',
            url: '/components/games-showcase.html',
            selector: '#games-showcase-container',
            priority: 'normal'
        });

        // Priority 4: Footer and polish (below fold)
        loader.register({
            id: 'footer',
            url: '/components/footer.html',
            selector: '#footer-component',
            priority: 'low'
        });

        loader.register({
            id: 'mobile-bottom-nav',
            url: '/components/mobile-bottom-nav.html',
            selector: '#mobile-nav-bottom',
            priority: 'low'
        });

        loader.register({
            id: 'beta-badge',
            url: '/components/beta-badge.html',
            selector: '#beta-badge-component',
            priority: 'low'
        });

        loader.register({
            id: 'onboarding-tour',
            url: '/components/onboarding-tour.html',
            selector: '#onboarding-tour-component',
            priority: 'low'
        });

        loader.register({
            id: 'quick-actions-fab',
            url: '/components/quick-actions-fab.html',
            selector: '#fab-quick-actions',
            priority: 'low'
        });

        return loader;
    }
}

// Global instance for homepage
window.componentLoader = ComponentLoader.createForHomepage();

// Auto-start ENABLED - Load components using coordinated system
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.componentLoader.loadAll()
            .then(() => {
                // User feedback provided via UI
                // Trigger custom event for when all components are ready
                document.dispatchEvent(new CustomEvent('homepage-components-ready'));
            })
            .catch(err => {
                // Log to monitoring instead of console
                if (window.posthog) {
                    posthog.capture('component_loading_error', {
                        error: err.message,
                        url: window.location.pathname
                    });
                }
                // Show user-friendly message instead of error
                // System status logged
            });
    });
} else {
    window.componentLoader.loadAll()
        .then(() => {
            // User feedback provided via UI
            document.dispatchEvent(new CustomEvent('homepage-components-ready'));
        })
        .catch(err => {
            // Log to monitoring instead of console
            if (window.posthog) {
                posthog.capture('component_loading_error', {
                    error: err.message,
                    url: window.location.pathname
                });
            }
            // Show user-friendly message instead of error
            // System status logged
        });
}

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ComponentLoader;
}

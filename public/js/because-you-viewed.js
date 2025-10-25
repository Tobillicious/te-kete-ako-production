/**
 * BECAUSE YOU VIEWED - Personalized Recommendation System
 * Tracks user's viewing history and recommends related resources via GraphRAG
 * Privacy-first: All data stored in localStorage, never sent to server
 */

(function() {
    'use strict';

    // Prevent duplicate initialization
    if (window.BecauseYouViewed) {
        return;
    }

    class BecauseYouViewed {
        constructor() {
            this.storageKey = 'te-kete-viewing-history';
            this.maxHistory = 10; // Keep last 10 viewed resources
            this.supabaseUrl = 'https://nlgldaqtubrlcqddppbq.supabase.co';
            this.supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';
            this.supabase = null;
        }

        /**
         * Initialize the system
         */
        async init() {
            try {
                // Track current page view
                this.trackCurrentPage();

                // Load Supabase if not already loaded
                if (typeof window.supabase === 'undefined' || !window.supabase.from) {
                    const supabaseModule = await import('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2');
                    if (window.supabaseSingleton) {
                        this.supabase = await window.supabaseSingleton.getClient();
                    }
                } else {
                    this.supabase = window.supabase;
                }

                // Show recommendations if user has history
                const history = this.getHistory();
                if (history.length >= 2) { // Need at least 2 viewed pages
                    await this.showRecommendations();
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

        /**
         * Track current page in viewing history
         */
        trackCurrentPage() {
            const currentPath = window.location.pathname;
            
            // Only track lesson, handout, and unit pages
            if (!this.isTrackablePage(currentPath)) {
                return;
            }

            const history = this.getHistory();
            
            // Don't add if it's already the most recent
            if (history.length > 0 && history[0].path === currentPath) {
                return;
            }

            // Create history entry
            const entry = {
                path: currentPath,
                timestamp: new Date().toISOString(),
                title: document.title || 'Untitled'
            };

            // Add to front of array
            history.unshift(entry);

            // Keep only last N entries
            const trimmed = history.slice(0, this.maxHistory);

            // Save to localStorage
            localStorage.setItem(this.storageKey, JSON.stringify(trimmed));
        }

        /**
         * Get viewing history from localStorage
         */
        getHistory() {
            try {
                const stored = localStorage.getItem(this.storageKey);
                return stored ? JSON.parse(stored) : [];
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
         * Check if page should be tracked
         */
        isTrackablePage(path) {
            const trackable = [
                '/lessons/',
                '/handouts/',
                '/dist-handouts/',
                '/units/',
                '/generated-resources-alpha/',
                '/integrated-lessons/'
            ];
            return trackable.some(pattern => path.includes(pattern));
        }

        /**
         * Show recommendations based on viewing history
         */
        async showRecommendations() {
            try {
                const history = this.getHistory();
                if (history.length < 2) return;

                // Get GraphRAG relationships for recent pages
                const recentPaths = history.slice(0, 5).map(h => h.path);
                
                const { data: relationships, error: relError } = await this.supabase
                    .from('graphrag_relationships')
                    .select('target_path, relationship_type, confidence, source_path')
                    .in('source_path', recentPaths)
                    .gte('confidence', 0.6) // High confidence only
                    .order('confidence', { ascending: false })
                    .limit(20);

                if (relError || !relationships || relationships.length === 0) {
                    return;
                }

                // Get unique target paths (exclude already viewed)
                const viewedPaths = history.map(h => h.path);
                const targetPaths = [...new Set(relationships.map(r => r.target_path))]
                    .filter(path => !viewedPaths.includes(path));

                if (targetPaths.length === 0) return;

                // Fetch resource details
                const { data: resources, error: resError } = await this.supabase
                    .from('graphrag_resources')
                    .select('file_path, title, resource_type, subject, year_level, quality_score, cultural_context')
                    .in('file_path', targetPaths)
                    .gte('quality_score', 85)
                    .order('quality_score', { ascending: false })
                    .limit(4);

                if (resError || !resources || resources.length === 0) {
                    return;
                }

                // Display recommendations
                this.displayRecommendationBanner(resources);

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

        /**
         * Display recommendation banner
         */
        displayRecommendationBanner(resources) {
            // Check if banner already exists
            if (document.getElementById('because-you-viewed-banner')) {
                return;
            }

            const banner = document.createElement('div');
            banner.id = 'because-you-viewed-banner';
            banner.style.cssText = `
                position: fixed;
                bottom: 20px;
                right: 20px;
                max-width: 400px;
                background: linear-gradient(135deg, #7c3aed 0%, #6366f1 100%);
                color: white;
                padding: 1.5rem;
                border-radius: 16px;
                box-shadow: 0 8px 32px rgba(124, 58, 237, 0.4);
                z-index: 9999;
                animation: slideInFromRight 0.5s ease-out;
            `;

            banner.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                    <h4 style="margin: 0; font-size: 1.1rem; font-weight: 700;">
                        💡 Because You Viewed...
                    </h4>
                    <button onclick="document.getElementById('because-you-viewed-banner').remove()" 
                        style="background: rgba(255,255,255,0.2); border: none; color: white; width: 24px; height: 24px; border-radius: 50%; cursor: pointer; font-size: 1.2rem; line-height: 1;">
                        ×
                    </button>
                </div>
                <p style="margin: 0 0 1rem 0; font-size: 0.85rem; opacity: 0.9;">
                    Based on your recent views, you might enjoy:
                </p>
                <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                    ${resources.slice(0, 3).map(r => `
                        <a href="${r.file_path}" 
                            style="background: rgba(255,255,255,0.15); padding: 0.75rem; border-radius: 8px; text-decoration: none; color: white; display: block; border-left: 3px solid rgba(255,255,255,0.4); transition: all 0.2s;"
                            onmouseover="this.style.background='rgba(255,255,255,0.25)'"
                            onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                            <div style="font-weight: 600; margin-bottom: 0.25rem; font-size: 0.9rem;">
                                ${r.title}
                            </div>
                            <div style="font-size: 0.75rem; opacity: 0.8;">
                                ${r.subject} • ${r.resource_type} • ⭐ ${r.quality_score}
                            </div>
                        </a>
                    `).join('')}
                </div>
                <button onclick="document.getElementById('because-you-viewed-banner').remove()" 
                    style="margin-top: 1rem; width: 100%; background: rgba(255,255,255,0.2); color: white; border: 1px solid rgba(255,255,255,0.3); padding: 0.5rem; border-radius: 8px; cursor: pointer; font-weight: 600; font-size: 0.85rem;">
                    Dismiss
                </button>
            `;

            // Add animation keyframes
            const style = document.createElement('style');
            style.textContent = `
                @keyframes slideInFromRight {
                    from {
                        transform: translateX(120%);
                        opacity: 0;
                    }
                    to {
                        transform: translateX(0);
                        opacity: 1;
                    }
                }
                @media (max-width: 768px) {
                    #because-you-viewed-banner {
                        bottom: 80px !important;
                        left: 10px !important;
                        right: 10px !important;
                        max-width: none !important;
                    }
                }
            `;
            document.head.appendChild(style);

            // Add to page
            document.body.appendChild(banner);

            // Auto-dismiss after 30 seconds
            setTimeout(() => {
                if (banner.parentNode) {
                    banner.style.animation = 'slideOutToRight 0.5s ease-out';
                    setTimeout(() => banner.remove(), 500);
                }
            }, 30000);
        }

        /**
         * Clear viewing history (for privacy)
         */
        clearHistory() {
            localStorage.removeItem(this.storageKey);
        }
    }

    // Initialize on DOM ready
    window.BecauseYouViewed = BecauseYouViewed;
    
    // Auto-init
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', async () => {
            const tracker = new BecauseYouViewed();
            await tracker.init();
        });
    } else {
        (async () => {
            const tracker = new BecauseYouViewed();
            await tracker.init();
        })();
    }

})();


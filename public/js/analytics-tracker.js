/**
 * Analytics Tracker for Te Kete Ako
 * Tracks component usage, GraphRAG recommendations, and user engagement
 * Created: October 21, 2025
 */

(function() {
    'use strict';

    // Initialize Supabase client (reuse existing if available)
    const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
    const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';

    // Generate or retrieve session ID
    const SESSION_ID = sessionStorage.getItem('tk_session_id') || generateSessionId();
    sessionStorage.setItem('tk_session_id', SESSION_ID);

    function generateSessionId() {
        return 'sess_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }

    // Get current resource path
    const CURRENT_PATH = window.location.pathname;

    // Analytics tracking object
    window.TeKeteAnalytics = {
        sessionId: SESSION_ID,
        supabase: null,

        async init() {
            try {
                // Initialize Supabase if not already done
                if (!window.supabase || !window.supabase.from) {
                    const { createClient } = await import('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2');
                    window.supabase = createClient(SUPABASE_URL, SUPABASE_KEY);
                }
                this.supabase = window.supabase;
                
                // Track page view
                this.trackPageView();
                
                // Set up component tracking
                this.setupComponentTracking();
                
            } catch (error) {
                // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        }
        },

        async trackEvent(eventData) {
            if (!this.supabase) return;

            try {
                const { error } = await this.supabase
                    .from('component_analytics')
                    .insert([{
                        session_id: this.sessionId,
                        resource_path: CURRENT_PATH,
                        user_agent: navigator.userAgent,
                        timestamp: new Date().toISOString(),
                        ...eventData
                    }]);

                if (error) {
                    // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        }
            } catch (error) {
                // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        }
        },

        trackPageView() {
            this.trackEvent({
                component_type: 'page_view',
                user_action: 'view',
                metadata: {
                    title: document.title,
                    referrer: document.referrer,
                    viewport: `${window.innerWidth}x${window.innerHeight}`
                }
            });
        },

        setupComponentTracking() {
            // Track Similar Resources component
            this.trackSimilarResources();
            
            // Track Most Connected component
            this.trackMostConnected();
            
            // Track Quality Badge interactions
            this.trackQualityBadges();
        },

        trackSimilarResources() {
            // Wait for component to load
            setTimeout(() => {
                const container = document.getElementById('similar-resources');
                if (!container) return;

                // Track component view
                this.trackEvent({
                    component_type: 'similar_resources',
                    user_action: 'component_loaded',
                    metadata: {
                        resource_count: container.querySelectorAll('.similar-resource-card').length
                    }
                });

                // Track clicks on recommendations
                container.querySelectorAll('.similar-resource-card').forEach((card, index) => {
                    card.addEventListener('click', (e) => {
                        const href = card.getAttribute('href');
                        const title = card.querySelector('.resource-title')?.textContent;
                        
                        this.trackEvent({
                            component_type: 'similar_resources',
                            user_action: 'click',
                            clicked_resource_path: href,
                            metadata: {
                                position: index + 1,
                                title: title,
                                total_recommendations: container.querySelectorAll('.similar-resource-card').length
                            }
                        });
                    });

                    // Track hovers (interest without click)
                    let hoverTimeout;
                    card.addEventListener('mouseenter', () => {
                        hoverTimeout = setTimeout(() => {
                            const href = card.getAttribute('href');
                            this.trackEvent({
                                component_type: 'similar_resources',
                                user_action: 'hover_sustained',
                                clicked_resource_path: href,
                                metadata: {
                                    position: index + 1,
                                    duration: '2s'
                                }
                            });
                        }, 2000); // Track if user hovers for 2+ seconds
                    });

                    card.addEventListener('mouseleave', () => {
                        clearTimeout(hoverTimeout);
                    });
                });
            }, 3000); // Wait 3s for component to fully load
        },

        trackMostConnected() {
            setTimeout(() => {
                const container = document.getElementById('most-connected');
                if (!container) return;

                this.trackEvent({
                    component_type: 'most_connected',
                    user_action: 'component_loaded',
                    metadata: {
                        resource_count: container.querySelectorAll('.connected-resource-card').length
                    }
                });

                // Track clicks
                container.querySelectorAll('.connected-resource-card').forEach((card, index) => {
                    card.addEventListener('click', (e) => {
                        const href = card.getAttribute('href');
                        const connectionCount = card.querySelector('.connection-count-badge')?.textContent;
                        
                        this.trackEvent({
                            component_type: 'most_connected',
                            user_action: 'click',
                            clicked_resource_path: href,
                            metadata: {
                                position: index + 1,
                                connection_count: connectionCount
                            }
                        });
                    });
                });
            }, 2000);
        },

        trackQualityBadges() {
            // Track clicks on quality badges (if they're clickable)
            document.querySelectorAll('.quality-badge').forEach((badge) => {
                badge.addEventListener('click', (e) => {
                    this.trackEvent({
                        component_type: 'quality_badge',
                        user_action: 'click',
                        metadata: {
                            badge_text: badge.textContent,
                            badge_type: Array.from(badge.classList).find(c => c.startsWith('badge-'))
                        }
                    });
                });
            });
        },

        // Public method for manual tracking
        track(componentType, action, metadata = {}) {
            this.trackEvent({
                component_type: componentType,
                user_action: action,
                metadata: metadata
            });
        }
    };

    // Auto-initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            window.TeKeteAnalytics.init();
        });
    } else {
        window.TeKeteAnalytics.init();
    }

    // Track session end
    window.addEventListener('beforeunload', () => {
        // Calculate session duration
        const sessionStart = parseInt(SESSION_ID.split('_')[1]);
        const sessionDuration = Date.now() - sessionStart;
        
        // Send final event (beacon for reliability)
        if (navigator.sendBeacon && window.TeKeteAnalytics.supabase) {
            window.TeKeteAnalytics.trackEvent({
                component_type: 'session',
                user_action: 'end',
                metadata: {
                    duration_ms: sessionDuration,
                    duration_minutes: Math.round(sessionDuration / 60000)
                }
            });
        }
    });

})();


/**
 * 🎨 TE KETE AKO POSTHOG ANALYTICS SYSTEM
 * User Behavior Tracking × Cultural Privacy Respect
 * 
 * HEGELIAN SYNTHESIS:
 * THESIS: Silicon Valley data-driven insights
 * ANTITHESIS: Māori data sovereignty & privacy
 * SYNTHESIS: Ethical analytics with kaitiakitanga
 * 
 * Features:
 * - Page view tracking
 * - User journey mapping
 * - Resource engagement metrics
 * - Cultural content interaction tracking
 * - Privacy-first approach (respects Do Not Track)
 * - GDPR/NZ Privacy Act compliant
 */

// PostHog Configuration
// TODO: Replace with actual PostHog project API key when available
const POSTHOG_CONFIG = {
    apiKey: 'phc_YOUR_PROJECT_API_KEY_HERE', // Replace with real key from posthog.com
    apiHost: 'https://app.posthog.com',
    enabled: true, // Set to false to disable tracking
    respectDoNotTrack: true, // Honor user privacy preferences
    capturePageview: true,
    capturePageLeave: true,
};

class TeKeteAnalytics {
    constructor() {
        this.initialized = false;
        this.posthog = null;
        this.consentGiven = this.checkConsent();
        
        
        if (this.shouldInitialize()) {
            this.init();
        } else {
        }
    }
    
    checkConsent() {
        // Check for Do Not Track
        if (navigator.doNotTrack === '1' || navigator.doNotTrack === 'yes') {
            return false;
        }
        
        // Check for explicit consent
        const consent = localStorage.getItem('tka-analytics-consent');
        if (consent === 'denied') return false;
        if (consent === 'granted') return true;
        
        // Default: granted (with option to opt-out via settings)
        return true;
    }
    
    shouldInitialize() {
        return (
            POSTHOG_CONFIG.enabled &&
            this.consentGiven &&
            POSTHOG_CONFIG.apiKey !== 'phc_YOUR_PROJECT_API_KEY_HERE'
        );
    }
    
    init() {
        // Load PostHog library
        !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
        
        posthog.init(POSTHOG_CONFIG.apiKey, {
            api_host: POSTHOG_CONFIG.apiHost,
            autocapture: true,
            capture_pageview: POSTHOG_CONFIG.capturePageview,
            capture_pageleave: POSTHOG_CONFIG.capturePageLeave,
            persistence: 'localStorage',
            
            // Privacy settings
            respect_dnt: POSTHOG_CONFIG.respectDoNotTrack,
            opt_out_capturing_by_default: false,
            
            // Performance
            loaded: (posthog) => {
                this.posthog = posthog;
                this.initialized = true;
                this.trackInitialPageView();
            }
        });
    }
    
    trackInitialPageView() {
        if (!this.initialized) return;
        
        // Track page metadata
        const pageData = {
            page_title: document.title,
            page_url: window.location.href,
            page_path: window.location.pathname,
            referrer: document.referrer,
            
            // Te Kete specific metadata
            subject: this.detectSubject(),
            year_level: this.detectYearLevel(),
            resource_type: this.detectResourceType(),
            has_cultural_content: this.detectCulturalContent(),
        };
        
        this.posthog.capture('$pageview', pageData);
    }
    
    detectSubject() {
        const path = window.location.pathname.toLowerCase();
        if (path.includes('mathematics') || path.includes('math')) return 'Mathematics';
        if (path.includes('science')) return 'Science';
        if (path.includes('english')) return 'English';
        if (path.includes('social-studies')) return 'Social Studies';
        if (path.includes('digital') || path.includes('technology')) return 'Digital Technologies';
        if (path.includes('te-ao-maori') || path.includes('te-reo')) return 'Te Ao Māori';
        if (path.includes('health') || path.includes('pe')) return 'Health & PE';
        if (path.includes('arts')) return 'Arts';
        return 'General';
    }
    
    detectYearLevel() {
        const path = window.location.pathname;
        const yearMatch = path.match(/y(\d+)|year[- ](\d+)/i);
        if (yearMatch) {
            const year = yearMatch[1] || yearMatch[2];
            return `Year ${year}`;
        }
        return 'Multiple';
    }
    
    detectResourceType() {
        const path = window.location.pathname.toLowerCase();
        if (path.includes('/lessons/')) return 'Lesson';
        if (path.includes('/handouts/')) return 'Handout';
        if (path.includes('/units/')) return 'Unit';
        if (path.includes('/games/')) return 'Game';
        if (path.includes('/assessments/')) return 'Assessment';
        if (path.includes('hub')) return 'Hub';
        return 'Page';
    }
    
    detectCulturalContent() {
        const bodyText = document.body.textContent.toLowerCase();
        const culturalKeywords = ['whakataukī', 'māori', 'kaitiakitanga', 'te reo', 'tikanga', 'whakapapa'];
        return culturalKeywords.some(keyword => bodyText.includes(keyword));
    }
    
    // Public tracking methods
    trackResourceView(resourceId, resourceTitle, subject) {
        if (!this.initialized) return;
        
        this.posthog.capture('resource_viewed', {
            resource_id: resourceId,
            resource_title: resourceTitle,
            subject: subject,
            timestamp: new Date().toISOString()
        });
    }
    
    trackResourceDownload(resourceId, resourceTitle, format) {
        if (!this.initialized) return;
        
        this.posthog.capture('resource_downloaded', {
            resource_id: resourceId,
            resource_title: resourceTitle,
            format: format,
            timestamp: new Date().toISOString()
        });
    }
    
    trackSearch(query, resultsCount) {
        if (!this.initialized) return;
        
        this.posthog.capture('search_performed', {
            query: query,
            results_count: resultsCount,
            timestamp: new Date().toISOString()
        });
    }
    
    trackUserJourney(fromPage, toPage, action) {
        if (!this.initialized) return;
        
        this.posthog.capture('user_journey', {
            from: fromPage,
            to: toPage,
            action: action,
            timestamp: new Date().toISOString()
        });
    }
    
    trackCulturalEngagement(culturalElement, interaction) {
        if (!this.initialized) return;
        
        this.posthog.capture('cultural_engagement', {
            element_type: culturalElement, // 'whakataukī', 'te_reo', 'cultural_pattern'
            interaction: interaction, // 'viewed', 'clicked', 'expanded'
            timestamp: new Date().toISOString()
        });
    }
    
    identifyUser(userId, properties) {
        if (!this.initialized) return;
        
        this.posthog.identify(userId, {
            ...properties,
            platform: 'Te Kete Ako',
            version: '2025.10'
        });
    }
}

// Initialize analytics system
let teKeteAnalytics;
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        teKeteAnalytics = new TeKeteAnalytics();
        window.teKeteAnalytics = teKeteAnalytics;
    });
} else {
    teKeteAnalytics = new TeKeteAnalytics();
    window.teKeteAnalytics = teKeteAnalytics;
}

// Export for global access
window.TeKeteAnalytics = TeKeteAnalytics;

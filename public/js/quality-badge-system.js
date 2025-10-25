/**
 * QUALITY BADGE SYSTEM - P0 Critical Fix
 * Automatically adds quality badges to all resources
 * Based on GraphRAG quality scores
 * Priority Score: 2.00 | Impact: 20% users
 */

class QualityBadgeSystem {
    constructor() {
        this.initialized = false;
    }
    
    /**
     * Get quality badge HTML for a given quality score
     */
    getBadgeHTML(qualityScore, culturalIntegration = null) {
        if (!qualityScore || qualityScore < 0) {
            return '';
        }
        
        let badgeClass, badgeText, tooltip;
        
        // Determine badge level
        if (qualityScore >= 95) {
            badgeClass = 'quality-exceptional';
            badgeText = 'Exceptional';
            tooltip = `Quality Score: ${qualityScore}/100 - Exceptional standard`;
        } else if (qualityScore >= 90) {
            badgeClass = 'quality-excellent';
            badgeText = 'Excellent';
            tooltip = `Quality Score: ${qualityScore}/100 - Excellent standard`;
        } else if (qualityScore >= 85) {
            badgeClass = 'quality-very-good';
            badgeText = 'Very Good';
            tooltip = `Quality Score: ${qualityScore}/100 - Very good quality`;
        } else if (qualityScore >= 80) {
            badgeClass = 'quality-good';
            badgeText = 'Good';
            tooltip = `Quality Score: ${qualityScore}/100 - Good quality`;
        } else if (qualityScore >= 75) {
            badgeClass = 'quality-satisfactory';
            badgeText = 'Satisfactory';
            tooltip = `Quality Score: ${qualityScore}/100 - Satisfactory`;
        } else {
            return ''; // Don't show badges for <75
        }
        
        let html = `<span class="quality-badge ${badgeClass}" data-tooltip="${tooltip}">${badgeText}</span>`;
        
        // Add cultural badge if high integration
        if (culturalIntegration && culturalIntegration >= 80) {
            html += `<span class="cultural-badge" data-tooltip="Cultural Integration: ${culturalIntegration}%">Cultural</span>`;
        }
        
        return html;
    }
    
    /**
     * Add quality badges to all resource cards on current page
     */
    async addBadgesToPage() {
        console.log('🌟 Adding quality badges to resources...');
        
        // Find all resource cards/links
        const resourceElements = document.querySelectorAll('[data-quality-score]');
        
        let badgesAdded = 0;
        
        resourceElements.forEach(element => {
            const qualityScore = parseFloat(element.dataset.qualityScore);
            const culturalScore = parseFloat(element.dataset.culturalScore);
            
            if (qualityScore) {
                const badgeHTML = this.getBadgeHTML(qualityScore, culturalScore);
                
                if (badgeHTML) {
                    // Find or create badge container
                    let badgeContainer = element.querySelector('.badge-container');
                    
                    if (!badgeContainer) {
                        badgeContainer = document.createElement('div');
                        badgeContainer.className = 'badge-container';
                        
                        // Insert after title or at end of card
                        const title = element.querySelector('h3, h4, .resource-title');
                        if (title) {
                            title.insertAdjacentElement('afterend', badgeContainer);
                        } else {
                            element.appendChild(badgeContainer);
                        }
                    }
                    
                    badgeContainer.innerHTML = badgeHTML;
                    badgesAdded++;
                }
            }
        });
        
        console.log(`✅ Added ${badgesAdded} quality badges`);
        this.initialized = true;
    }
    
    /**
     * Initialize badge system on page load
     */
    init() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.addBadgesToPage());
        } else {
            this.addBadgesToPage();
        }
    }
}

// Auto-initialize
if (typeof window !== 'undefined') {
    window.QualityBadgeSystem = new QualityBadgeSystem();
    window.QualityBadgeSystem.init();
}


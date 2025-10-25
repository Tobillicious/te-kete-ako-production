/**
 * Intelligence Integration - Te Kete Ako
 * Integrates all intelligence systems into existing pages
 * Auto-loads and connects GraphRAG intelligence to user experience
 */

class IntelligenceIntegration {
    constructor() {
        this.masterIntelligence = null;
        this.integrationPoints = new Map();
        this.init();
    }

    async init() {
        // Wait for master intelligence to be ready
        await this.waitForMasterIntelligence();
        
        // Auto-detect integration points
        this.detectIntegrationPoints();
        
        // Connect intelligence to existing elements
        this.connectIntelligenceToElements();
        
    }

    /**
     * WAIT FOR MASTER INTELLIGENCE
     */
    async waitForMasterIntelligence() {
        const maxWait = 15000; // 15 seconds
        const checkInterval = 500;
        let waited = 0;

        while (waited < maxWait) {
            if (window.MasterIntelligence && window.MasterIntelligence.systemHealth.initialized) {
                this.masterIntelligence = window.MasterIntelligence;
                break;
            }
            
            await new Promise(resolve => setTimeout(resolve, checkInterval));
            waited += checkInterval;
        }

        if (waited >= maxWait) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        console.log('Issue detected: $2');
        }
    }

    /**
     * DETECT INTEGRATION POINTS
     */
    detectIntegrationPoints() {
        // Detect sidebar integration points
        const sidebars = document.querySelectorAll('[data-intelligent-sidebar]');
        sidebars.forEach(sidebar => {
            this.integrationPoints.set(sidebar, 'intelligent_sidebar');
        });

        // Detect recommendation areas
        const recAreas = document.querySelectorAll('[data-recommendations]');
        recAreas.forEach(area => {
            this.integrationPoints.set(area, 'recommendations');
        });

        // Detect teaching content
        const lessons = document.querySelectorAll('[data-lesson-content]');
        lessons.forEach(lesson => {
            this.integrationPoints.set(lesson, 'teaching_variants');
        });

        // Detect cultural content
        const cultural = document.querySelectorAll('[data-cultural-content]');
        cultural.forEach(element => {
            this.integrationPoints.set(element, 'cultural_intelligence');
        });

    }

    /**
     * CONNECT INTELLIGENCE TO ELEMENTS
     */
    connectIntelligenceToElements() {
        this.integrationPoints.forEach((type, element) => {
            switch (type) {
                case 'intelligent_sidebar':
                    this.connectIntelligentSidebar(element);
                    break;
                case 'recommendations':
                    this.connectRecommendations(element);
                    break;
                case 'teaching_variants':
                    this.connectTeachingVariants(element);
                    break;
                case 'cultural_intelligence':
                    this.connectCulturalIntelligence(element);
                    break;
            }
        });
    }

    /**
     * CONNECT INTELLIGENT SIDEBAR
     */
    async connectIntelligentSidebar(sidebar) {
        if (!this.masterIntelligence) return;

        try {
            const currentPath = window.location.pathname;
            const userContext = this.extractUserContext();

            // Get intelligent recommendations
            const recommendations = await this.masterIntelligence.getIntelligentRecommendations(
                currentPath, 
                userContext
            );

            // Update sidebar with recommendations
            this.updateSidebarWithRecommendations(sidebar, recommendations);
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
        console.log('Issue detected: $2');
        }
    }

    /**
     * CONNECT RECOMMENDATIONS
     */
    async connectRecommendations(element) {
        if (!this.masterIntelligence) return;

        try {
            const currentPath = window.location.pathname;
            const userContext = this.extractUserContext();

            const recommendations = await this.masterIntelligence.getIntelligentRecommendations(
                currentPath, 
                userContext
            );

            this.renderRecommendations(element, recommendations);
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
        console.log('Issue detected: $2');
        }
    }

    /**
     * CONNECT TEACHING VARIANTS
     */
    async connectTeachingVariants(element) {
        if (!this.masterIntelligence) return;

        try {
            const currentPath = window.location.pathname;
            const userContext = this.extractUserContext();

            const recommendations = await this.masterIntelligence.getIntelligentRecommendations(
                currentPath, 
                userContext
            );

            if (recommendations.teaching) {
                this.renderTeachingVariants(element, recommendations.teaching);
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
        console.log('Issue detected: $2');
        }
    }

    /**
     * CONNECT CULTURAL INTELLIGENCE
     */
    async connectCulturalIntelligence(element) {
        if (!this.masterIntelligence) return;

        try {
            const currentPath = window.location.pathname;
            const userContext = { ...this.extractUserContext(), cultural: true };

            const recommendations = await this.masterIntelligence.getIntelligentRecommendations(
                currentPath, 
                userContext
            );

            if (recommendations.cultural) {
                this.renderCulturalIntelligence(element, recommendations.cultural);
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
        console.log('Issue detected: $2');
        }
    }

    /**
     * EXTRACT USER CONTEXT
     */
    extractUserContext() {
        const context = {};

        // Extract from data attributes
        const contextElement = document.querySelector('[data-user-context]');
        if (contextElement) {
            try {
                const contextData = JSON.parse(contextElement.dataset.userContext);
                Object.assign(context, contextData);
            } catch (e) {
                // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        console.log('Issue detected: $2');
            }
        }

        // Extract from URL
        const path = window.location.pathname;
        if (path.includes('/units/')) {
            context.yearLevel = this.extractYearLevel(path);
            context.subject = this.extractSubject(path);
        }

        // Extract from page metadata
        const metaYear = document.querySelector('meta[name="year-level"]');
        if (metaYear) context.yearLevel = metaYear.content;

        const metaSubject = document.querySelector('meta[name="subject"]');
        if (metaSubject) context.subject = metaSubject.content;

        return context;
    }

    /**
     * EXTRACT YEAR LEVEL FROM PATH
     */
    extractYearLevel(path) {
        const yearMatch = path.match(/y(\d+)/);
        return yearMatch ? `Year ${yearMatch[1]}` : null;
    }

    /**
     * EXTRACT SUBJECT FROM PATH
     */
    extractSubject(path) {
        if (path.includes('math')) return 'Mathematics';
        if (path.includes('science')) return 'Science';
        if (path.includes('english')) return 'English';
        if (path.includes('maori')) return 'Te Ao Māori';
        return null;
    }

    /**
     * UPDATE SIDEBAR WITH RECOMMENDATIONS
     */
    updateSidebarWithRecommendations(sidebar, recommendations) {
        // Find or create recommendations section
        let recSection = sidebar.querySelector('[data-recommendations-section]');
        if (!recSection) {
            recSection = document.createElement('div');
            recSection.setAttribute('data-recommendations-section', 'true');
            sidebar.appendChild(recSection);
        }

        // Render contextual recommendations
        if (recommendations.contextual && recommendations.contextual.length > 0) {
            this.renderRecommendationList(recSection, recommendations.contextual, 'Related Resources');
        }

        // Render cultural recommendations
        if (recommendations.cultural && recommendations.cultural.length > 0) {
            this.renderRecommendationList(recSection, recommendations.cultural, 'Cultural Resources');
        }

        // Render teaching variants
        if (recommendations.teaching) {
            this.renderTeachingVariants(recSection, recommendations.teaching);
        }
    }

    /**
     * RENDER RECOMMENDATIONS
     */
    renderRecommendations(element, recommendations) {
        element.innerHTML = '';

        if (recommendations.contextual && recommendations.contextual.length > 0) {
            this.renderRecommendationList(element, recommendations.contextual, 'Recommended Resources');
        }

        if (recommendations.cultural && recommendations.cultural.length > 0) {
            this.renderRecommendationList(element, recommendations.cultural, 'Cultural Resources');
        }
    }

    /**
     * RENDER RECOMMENDATION LIST
     */
    renderRecommendationList(container, recommendations, title) {
        const section = document.createElement('div');
        section.className = 'recommendations-section';
        
        const titleEl = document.createElement('h3');
        titleEl.textContent = title;
        titleEl.className = 'recommendations-title';
        section.appendChild(titleEl);

        const list = document.createElement('ul');
        list.className = 'recommendations-list';

        recommendations.slice(0, 5).forEach(rec => {
            const item = document.createElement('li');
            item.className = 'recommendation-item';
            
            const link = document.createElement('a');
            link.href = rec.file_path;
            link.textContent = rec.title;
            link.className = 'recommendation-link';
            
            if (rec.reasons && rec.reasons.length > 0) {
                const reason = document.createElement('span');
                reason.textContent = ` (${rec.reasons[0]})`;
                reason.className = 'recommendation-reason';
                link.appendChild(reason);
            }
            
            item.appendChild(link);
            list.appendChild(item);
        });

        section.appendChild(list);
        container.appendChild(section);
    }

    /**
     * RENDER TEACHING VARIANTS
     */
    renderTeachingVariants(container, teachingData) {
        if (teachingData.type !== 'teaching_variants') return;

        const section = document.createElement('div');
        section.className = 'teaching-variants-section';
        
        const title = document.createElement('h3');
        title.textContent = 'Teaching Approaches';
        title.className = 'variants-title';
        section.appendChild(title);

        const variants = document.createElement('div');
        variants.className = 'variants-grid';

        teachingData.variants.forEach((variant, index) => {
            const variantCard = document.createElement('div');
            variantCard.className = 'variant-card';
            
            const variantTitle = document.createElement('h4');
            variantTitle.textContent = `Approach ${index + 1}`;
            variantCard.appendChild(variantTitle);

            const variantLink = document.createElement('a');
            variantLink.href = variant.file_path;
            variantLink.textContent = variant.title;
            variantLink.className = 'variant-link';
            variantCard.appendChild(variantLink);

            variants.appendChild(variantCard);
        });

        section.appendChild(variants);
        container.appendChild(section);
    }

    /**
     * RENDER CULTURAL INTELLIGENCE
     */
    renderCulturalIntelligence(element, culturalData) {
        element.innerHTML = '';

        culturalData.forEach(cultural => {
            const card = document.createElement('div');
            card.className = 'cultural-card';
            
            const title = document.createElement('h3');
            title.textContent = cultural.title;
            card.appendChild(title);

            const link = document.createElement('a');
            link.href = cultural.file_path;
            link.textContent = 'Explore Cultural Resource';
            link.className = 'cultural-link';
            card.appendChild(link);

            if (cultural.culturalElements && cultural.culturalElements.length > 0) {
                const elements = document.createElement('div');
                elements.className = 'cultural-elements';
                elements.textContent = `Elements: ${cultural.culturalElements.join(', ')}`;
                card.appendChild(elements);
            }

            element.appendChild(card);
        });
    }
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.IntelligenceIntegration = new IntelligenceIntegration();
    });
} else {
    window.IntelligenceIntegration = new IntelligenceIntegration();
}

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = IntelligenceIntegration;
}

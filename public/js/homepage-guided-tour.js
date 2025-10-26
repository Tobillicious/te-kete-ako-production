// Homepage Guided Tour
// Created: October 26, 2025
// Purpose: Help low-tech teachers navigate the platform (SIMULATION-DRIVEN!)

class HomepageTour {
    constructor() {
        this.currentStep = 0;
        this.steps = [
            {
                element: 'a[href="/teachers/index.html"]',
                title: '🧑‍🏫 Start Here if You're a Teacher',
                description: 'Click this big button to see all teaching resources, lesson plans, and professional tools.',
                position: 'bottom'
            },
            {
                element: 'a[href="/emergency-lessons.html"]',
                title: '🚨 Need a Lesson RIGHT NOW?',
                description: 'Emergency Lessons are ready to print in under 2 minutes. Perfect for substitute teachers!',
                position: 'bottom'
            },
            {
                element: 'a[href="/top-10-starter-pack.html"]',
                title: '⭐ Best Place to Start',
                description: 'Our hand-picked Top 10 lessons are the easiest way to get started. All gold-standard quality!',
                position: 'top'
            },
            {
                element: 'a[href="/pricing.html"]',
                title: '💰 14-Day Free Trial',
                description: '$15/month gets you 3,500+ resources, KAMAR integration, AI tools, and more. Try free for 14 days!',
                position: 'top'
            }
        ];
    }
    
    init() {
        // Check if user has seen tour before
        const tourCompleted = localStorage.getItem('homepage_tour_completed');
        
        // Only show to first-time visitors
        if (!tourCompleted && this.isHomepage()) {
            setTimeout(() => this.startTour(), 2000); // 2 second delay
        }
    }
    
    isHomepage() {
        return window.location.pathname === '/' || window.location.pathname === '/index.html';
    }
    
    startTour() {
        // Create overlay
        this.overlay = document.createElement('div');
        this.overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.7);
            z-index: 9998;
            display: flex;
            align-items: center;
            justify-content: center;
        `;
        
        // Create welcome modal
        this.overlay.innerHTML = `
            <div style="
                background: white;
                padding: 3rem;
                border-radius: 20px;
                max-width: 500px;
                text-align: center;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            ">
                <div style="font-size: 4rem; margin-bottom: 1rem;">🌿</div>
                <h2 style="color: #2F4F2F; margin: 0 0 1rem;">Kia ora! Welcome to Te Kete Ako!</h2>
                <p style="color: #666; margin: 0 0 2rem; font-size: 1.1rem;">
                    Would you like a quick 60-second tour to help you get started?
                </p>
                <div style="display: flex; gap: 1rem;">
                    <button onclick="window.homepageTour.skipTour()" style="
                        flex: 1;
                        padding: 1rem;
                        background: #8B7D6B;
                        color: white;
                        border: none;
                        border-radius: 8px;
                        font-weight: 600;
                        cursor: pointer;
                    ">
                        No Thanks
                    </button>
                    <button onclick="window.homepageTour.showStep(0)" style="
                        flex: 1;
                        padding: 1rem;
                        background: #8B4513;
                        color: white;
                        border: none;
                        border-radius: 8px;
                        font-weight: 600;
                        cursor: pointer;
                    ">
                        Yes, Show Me! →
                    </button>
                </div>
            </div>
        `;
        
        document.body.appendChild(this.overlay);
    }
    
    showStep(stepIndex) {
        if (stepIndex >= this.steps.length) {
            this.completeTour();
            return;
        }
        
        this.currentStep = stepIndex;
        const step = this.steps[stepIndex];
        
        // Find target element
        const targetElement = document.querySelector(step.element);
        
        if (!targetElement) {
            // Skip to next if element not found
            this.showStep(stepIndex + 1);
            return;
        }
        
        // Remove old tooltip if exists
        const oldTooltip = document.getElementById('tour-tooltip');
        if (oldTooltip) oldTooltip.remove();
        
        // Highlight target element
        targetElement.style.position = 'relative';
        targetElement.style.zIndex = '9999';
        targetElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
        
        // Create tooltip
        const tooltip = document.createElement('div');
        tooltip.id = 'tour-tooltip';
        tooltip.style.cssText = `
            position: absolute;
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
            max-width: 300px;
            z-index: 10000;
            ${step.position === 'bottom' ? 'top: calc(100% + 1rem);' : 'bottom: calc(100% + 1rem);'}
            left: 50%;
            transform: translateX(-50%);
        `;
        
        tooltip.innerHTML = `
            <h3 style="color: #2F4F2F; margin: 0 0 0.5rem; font-size: 1.1rem;">
                ${step.title}
            </h3>
            <p style="color: #666; margin: 0 0 1rem; font-size: 0.9rem;">
                ${step.description}
            </p>
            <div style="display: flex; gap: 0.5rem; justify-content: space-between; align-items: center;">
                <span style="color: #999; font-size: 0.875rem;">
                    ${stepIndex + 1} of ${this.steps.length}
                </span>
                <div style="display: flex; gap: 0.5rem;">
                    <button onclick="window.homepageTour.skipTour()" style="
                        padding: 0.5rem 1rem;
                        background: #e5e7eb;
                        border: none;
                        border-radius: 6px;
                        cursor: pointer;
                        font-size: 0.875rem;
                    ">
                        Skip
                    </button>
                    <button onclick="window.homepageTour.showStep(${stepIndex + 1})" style="
                        padding: 0.5rem 1rem;
                        background: #8B4513;
                        color: white;
                        border: none;
                        border-radius: 6px;
                        cursor: pointer;
                        font-weight: 600;
                        font-size: 0.875rem;
                    ">
                        ${stepIndex === this.steps.length - 1 ? 'Finish!' : 'Next →'}
                    </button>
                </div>
            </div>
        `;
        
        targetElement.appendChild(tooltip);
    }
    
    skipTour() {
        this.completeTour();
    }
    
    completeTour() {
        // Remove overlay
        if (this.overlay) {
            this.overlay.remove();
        }
        
        // Remove tooltip
        const tooltip = document.getElementById('tour-tooltip');
        if (tooltip) tooltip.remove();
        
        // Mark as completed
        localStorage.setItem('homepage_tour_completed', 'true');
        
        console.log('✅ Homepage tour completed!');
    }
}

// Initialize global instance
if (typeof window !== 'undefined') {
    window.homepageTour = new HomepageTour();
    
    // Auto-init on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            window.homepageTour.init();
        });
    } else {
        window.homepageTour.init();
    }
}


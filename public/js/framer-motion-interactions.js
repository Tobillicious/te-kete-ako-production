/**
 * Framer Motion Micro-Interactions - Te Kete Ako
 * Delightful animations and micro-interactions
 * Phase 2 of Tech Stack Evolution
 */

class TeKeteAnimations {
    constructor() {
        this.motion = null;
        this.init();
    }

    async init() {
        await this.loadFramerMotion();
        this.setupPageTransitions();
        this.setupCardAnimations();
        this.setupButtonInteractions();
        this.setupScrollAnimations();
        this.setupCulturalAnimations();
    }

    async loadFramerMotion() {
        if (window.motion) {
            this.motion = window.motion;
            return;
        }

        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = 'https://unpkg.com/framer-motion@11/dist/framer-motion.js';
            script.onload = () => {
                this.motion = window.motion;
                resolve();
            };
            script.onerror = reject;
            document.head.appendChild(script);
        });
    }

    setupPageTransitions() {
        // Smooth page transitions
        this.motion?.motion('body', {
            initial: { opacity: 0 },
            animate: { opacity: 1 },
            transition: { duration: 0.5, ease: 'easeOut' }
        });

        // Header animation
        this.motion?.motion('header', {
            initial: { y: -100, opacity: 0 },
            animate: { y: 0, opacity: 1 },
            transition: { duration: 0.6, ease: 'easeOut' }
        });
    }

    setupCardAnimations() {
        // Lesson cards
        document.querySelectorAll('.lesson-card, .unit-card, .resource-card').forEach((card, index) => {
            this.motion?.motion(card, {
                initial: { y: 50, opacity: 0 },
                animate: { y: 0, opacity: 1 },
                transition: { 
                    duration: 0.5, 
                    delay: index * 0.1,
                    ease: 'easeOut'
                },
                whileHover: {
                    y: -5,
                    scale: 1.02,
                    transition: { duration: 0.2 }
                }
            });
        });

        // Statistics cards
        document.querySelectorAll('.stat-card, .insight-card').forEach((card, index) => {
            this.motion?.motion(card, {
                initial: { scale: 0.8, opacity: 0 },
                animate: { scale: 1, opacity: 1 },
                transition: { 
                    duration: 0.4, 
                    delay: index * 0.1,
                    ease: 'backOut'
                },
                whileHover: {
                    scale: 1.05,
                    transition: { duration: 0.2 }
                }
            });
        });
    }

    setupButtonInteractions() {
        // Primary buttons
        document.querySelectorAll('.btn-primary, .subscribe-btn').forEach(button => {
            this.motion?.motion(button, {
                whileHover: {
                    scale: 1.05,
                    boxShadow: '0 8px 25px rgba(0,0,0,0.15)',
                    transition: { duration: 0.2 }
                },
                whileTap: {
                    scale: 0.95,
                    transition: { duration: 0.1 }
                }
            });
        });

        // Navigation links
        document.querySelectorAll('.nav-link').forEach(link => {
            this.motion?.motion(link, {
                whileHover: {
                    y: -2,
                    transition: { duration: 0.2 }
                }
            });
        });

        // Search button
        const searchBtn = document.querySelector('.search-trigger-btn');
        if (searchBtn) {
            this.motion?.motion(searchBtn, {
                whileHover: {
                    scale: 1.1,
                    rotate: 5,
                    transition: { duration: 0.2 }
                },
                whileTap: {
                    scale: 0.9,
                    transition: { duration: 0.1 }
                }
            });
        }
    }

    setupScrollAnimations() {
        // Intersection Observer for scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateOnScroll(entry.target);
                }
            });
        }, observerOptions);

        // Observe elements for scroll animations
        document.querySelectorAll('.hero-section, .feature-section, .stats-section').forEach(section => {
            observer.observe(section);
        });
    }

    animateOnScroll(element) {
        this.motion?.motion(element, {
            initial: { y: 100, opacity: 0 },
            animate: { y: 0, opacity: 1 },
            transition: { duration: 0.6, ease: 'easeOut' }
        });
    }

    setupCulturalAnimations() {
        // Whakataukī animations
        document.querySelectorAll('.whakatauki, .cultural-opening').forEach(element => {
            this.motion?.motion(element, {
                initial: { scale: 0.9, opacity: 0 },
                animate: { scale: 1, opacity: 1 },
                transition: { 
                    duration: 0.8, 
                    ease: 'easeOut',
                    delay: 0.2
                }
            });
        });

        // Māori pattern animations
        document.querySelectorAll('.maori-pattern, .kowhaiwhai').forEach(pattern => {
            this.motion?.motion(pattern, {
                animate: {
                    rotate: [0, 360],
                    scale: [1, 1.1, 1]
                },
                transition: {
                    duration: 20,
                    repeat: Infinity,
                    ease: 'linear'
                }
            });
        });

        // Cultural elements fade in
        document.querySelectorAll('.cultural-note, .te-kete-header').forEach(element => {
            this.motion?.motion(element, {
                initial: { opacity: 0, y: 20 },
                animate: { opacity: 1, y: 0 },
                transition: { 
                    duration: 0.5,
                    delay: 0.3
                }
            });
        });
    }

    // Teaching Variants Animations
    animateTeachingVariants() {
        document.querySelectorAll('.variant-card').forEach((card, index) => {
            this.motion?.motion(card, {
                initial: { x: -50, opacity: 0 },
                animate: { x: 0, opacity: 1 },
                transition: { 
                    duration: 0.4, 
                    delay: index * 0.1,
                    ease: 'easeOut'
                },
                whileHover: {
                    x: 10,
                    scale: 1.05,
                    transition: { duration: 0.2 }
                }
            });
        });
    }

    // GraphRAG Search Animations
    animateSearchResults() {
        const results = document.querySelectorAll('.search-result, .unit-result');
        results.forEach((result, index) => {
            this.motion?.motion(result, {
                initial: { y: 30, opacity: 0 },
                animate: { y: 0, opacity: 1 },
                transition: { 
                    duration: 0.3, 
                    delay: index * 0.05,
                    ease: 'easeOut'
                }
            });
        });
    }

    // Loading Animations
    animateLoading() {
        const loadingElements = document.querySelectorAll('.loading-spinner, .spinner');
        loadingElements.forEach(spinner => {
            this.motion?.motion(spinner, {
                animate: {
                    rotate: 360
                },
                transition: {
                    duration: 1,
                    repeat: Infinity,
                    ease: 'linear'
                }
            });
        });
    }

    // Success/Error Animations
    animateNotification(type, message) {
        const notification = document.createElement('div');
        notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
            type === 'success' ? 'bg-green-500 text-white' : 'bg-red-500 text-white'
        }`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        this.motion?.motion(notification, {
            initial: { x: 300, opacity: 0 },
            animate: { x: 0, opacity: 1 },
            exit: { x: 300, opacity: 0 },
            transition: { duration: 0.3 }
        });
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            this.motion?.motion(notification, {
                animate: { x: 300, opacity: 0 },
                transition: { duration: 0.3 },
                onComplete: () => notification.remove()
            });
        }, 5000);
    }

    // Year Level Dropdown Animations
    animateYearDropdown() {
        const dropdown = document.querySelector('.dropdown');
        if (dropdown) {
            this.motion?.motion(dropdown, {
                initial: { y: -20, opacity: 0 },
                animate: { y: 0, opacity: 1 },
                exit: { y: -20, opacity: 0 },
                transition: { duration: 0.2 }
            });
        }
    }

    // Sidebar Animations
    animateSidebar() {
        const sidebar = document.querySelector('.left-sidebar');
        if (sidebar) {
            this.motion?.motion(sidebar, {
                initial: { x: -300, opacity: 0 },
                animate: { x: 0, opacity: 1 },
                transition: { duration: 0.4, ease: 'easeOut' }
            });
        }
    }

    // Print Button Animation
    animatePrintButton() {
        const printBtn = document.querySelector('button[onclick="window.print()"]');
        if (printBtn) {
            this.motion?.motion(printBtn, {
                whileHover: {
                    scale: 1.05,
                    backgroundColor: '#047857',
                    transition: { duration: 0.2 }
                },
                whileTap: {
                    scale: 0.95,
                    transition: { duration: 0.1 }
                }
            });
        }
    }

    // Counter Animations
    animateCounters() {
        document.querySelectorAll('.stat-counter, .metric-value').forEach(counter => {
            const target = parseInt(counter.getAttribute('data-target') || counter.textContent);
            this.motion?.motion(counter, {
                animate: { 
                    scale: [1, 1.1, 1],
                    color: ['#059669', '#10b981', '#059669']
                },
                transition: { 
                    duration: 0.5,
                    delay: 0.2
                }
            });
        });
    }

    // Cultural Integration Animations
    animateCulturalElements() {
        // Whakataukī fade in
        document.querySelectorAll('.proverb, .translation, .context').forEach((element, index) => {
            this.motion?.motion(element, {
                initial: { opacity: 0, y: 20 },
                animate: { opacity: 1, y: 0 },
                transition: { 
                    duration: 0.5,
                    delay: index * 0.2
                }
            });
        });

        // Māori patterns rotation
        document.querySelectorAll('.maori-pattern').forEach(pattern => {
            this.motion?.motion(pattern, {
                animate: {
                    rotate: [0, 360]
                },
                transition: {
                    duration: 30,
                    repeat: Infinity,
                    ease: 'linear'
                }
            });
        });
    }
}

// Initialize animations when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => new TeKeteAnimations());
} else {
    new TeKeteAnimations();
}

// Export for global access
window.TeKeteAnimations = TeKeteAnimations;

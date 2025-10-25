/* =================================================================
   TE KETE AKO PROFESSIONAL JAVASCRIPT V1.0
   "Clean • Fast • Accessible • Maintainable"
   Core functionality for educational platform
   ================================================================= */

(function() {
    'use strict';

    // =================================================================
    // CONFIGURATION
    // =================================================================
    const CONFIG = {
        breakpoints: {
            mobile: 480,
            tablet: 768,
            desktop: 1024
        },
        animations: {
            duration: 250,
            easing: 'ease-in-out'
        },
        selectors: {
            nav: '.main-nav',
            cards: '.card',
            buttons: '.btn',
            forms: 'form',
            links: 'a[href^="#"]'
        }
    };

    // =================================================================
    // UTILITY FUNCTIONS
    // =================================================================
    const Utils = {
        // Debounce function for performance
        debounce(func, wait) {
            let timeout;
            return function executedFunction(...args) {
                const later = () => {
                    clearTimeout(timeout);
                    func(...args);
                };
                clearTimeout(timeout);
                timeout = setTimeout(later, wait);
            };
        },

        // Throttle function for scroll events
        throttle(func, limit) {
            let inThrottle;
            return function() {
                const args = arguments;
                const context = this;
                if (!inThrottle) {
                    func.apply(context, args);
                    inThrottle = true;
                    setTimeout(() => inThrottle = false, limit);
                }
            };
        },

        // Check if element is in viewport
        isInViewport(element) {
            const rect = element.getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        },

        // Get current breakpoint
        getCurrentBreakpoint() {
            const width = window.innerWidth;
            if (width < CONFIG.breakpoints.mobile) return 'mobile';
            if (width < CONFIG.breakpoints.tablet) return 'tablet';
            return 'desktop';
        },

        // Smooth scroll to element
        scrollToElement(element, offset = 0) {
            const targetPosition = element.offsetTop - offset;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    };

    // =================================================================
    // NAVIGATION SYSTEM
    // =================================================================
    const Navigation = {
        init() {
            this.setupMobileMenu();
            this.setupSmoothScrolling();
            this.setupKeyboardNavigation();
            this.setupActiveStates();
        },

        setupMobileMenu() {
            const nav = document.querySelector(CONFIG.selectors.nav);
            if (!nav) return;

            // Create mobile menu toggle if it doesn't exist
            if (!document.querySelector('.mobile-menu-toggle')) {
                const toggle = document.createElement('button');
                toggle.className = 'mobile-menu-toggle';
                toggle.innerHTML = '☰';
                toggle.setAttribute('aria-label', 'Toggle navigation menu');
                toggle.setAttribute('aria-expanded', 'false');
                
                nav.parentNode.insertBefore(toggle, nav);
                
                toggle.addEventListener('click', () => {
                    const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
                    toggle.setAttribute('aria-expanded', !isExpanded);
                    nav.classList.toggle('mobile-open');
                });
            }
        },

        setupSmoothScrolling() {
            const links = document.querySelectorAll(CONFIG.selectors.links);
            links.forEach(link => {
                link.addEventListener('click', (e) => {
                    const href = link.getAttribute('href');
                    if (href.startsWith('#')) {
                        e.preventDefault();
                        const target = document.querySelector(href);
                        if (target) {
                            Utils.scrollToElement(target, 80);
                        }
                    }
                });
            });
        },

        setupKeyboardNavigation() {
            const navLinks = document.querySelectorAll(`${CONFIG.selectors.nav} a`);
            navLinks.forEach((link, index) => {
                link.addEventListener('keydown', (e) => {
                    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
                        e.preventDefault();
                        const nextLink = navLinks[index + 1] || navLinks[0];
                        nextLink.focus();
                    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
                        e.preventDefault();
                        const prevLink = navLinks[index - 1] || navLinks[navLinks.length - 1];
                        prevLink.focus();
                    }
                });
            });
        },

        setupActiveStates() {
            const currentPage = document.body.getAttribute('data-current-page');
            if (currentPage) {
                const activeLink = document.querySelector(`${CONFIG.selectors.nav} a[href*="${currentPage}"]`);
                if (activeLink) {
                    activeLink.setAttribute('aria-current', 'page');
                    activeLink.classList.add('active');
                }
            }
        }
    };

    // =================================================================
    // INTERACTION ENHANCEMENTS
    // =================================================================
    const Interactions = {
        init() {
            this.setupCardHoverEffects();
            this.setupButtonStates();
            this.setupFormEnhancements();
        },

        setupCardHoverEffects() {
            const cards = document.querySelectorAll(CONFIG.selectors.cards);
            cards.forEach(card => {
                card.addEventListener('mouseenter', () => {
                    card.style.transform = 'translateY(-2px)';
                    card.style.boxShadow = '0 10px 25px rgba(0, 0, 0, 0.1)';
                });

                card.addEventListener('mouseleave', () => {
                    card.style.transform = 'translateY(0)';
                    card.style.boxShadow = '';
                });
            });
        },

        setupButtonStates() {
            const buttons = document.querySelectorAll(CONFIG.selectors.buttons);
            buttons.forEach(button => {
                // Add loading state
                button.addEventListener('click', (e) => {
                    if (button.type === 'submit' || button.classList.contains('btn-primary')) {
                        button.classList.add('loading');
                        button.disabled = true;
                        
                        // Re-enable after a delay (for demo purposes)
                        setTimeout(() => {
                            button.classList.remove('loading');
                            button.disabled = false;
                        }, 2000);
                    }
                });
            });
        },

        setupFormEnhancements() {
            const forms = document.querySelectorAll(CONFIG.selectors.forms);
            forms.forEach(form => {
                // Real-time validation
                const inputs = form.querySelectorAll('input, textarea, select');
                inputs.forEach(input => {
                    input.addEventListener('blur', () => this.validateField(input));
                    input.addEventListener('input', Utils.debounce(() => this.validateField(input), 300));
                });

                // Form submission
                form.addEventListener('submit', (e) => {
                    if (!this.validateForm(form)) {
                        e.preventDefault();
                    }
                });
            });
        },

        validateField(field) {
            const value = field.value.trim();
            const type = field.type;
            let isValid = true;
            let message = '';

            // Required field validation
            if (field.required && !value) {
                isValid = false;
                message = 'This field is required';
            }

            // Email validation
            if (type === 'email' && value) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(value)) {
                    isValid = false;
                    message = 'Please enter a valid email address';
                }
            }

            // Update field state
            field.classList.toggle('error', !isValid);
            field.classList.toggle('valid', isValid && value);
            
            // Show/hide error message
            let errorElement = field.parentNode.querySelector('.error-message');
            if (!isValid) {
                if (!errorElement) {
                    errorElement = document.createElement('span');
                    errorElement.className = 'error-message';
                    field.parentNode.appendChild(errorElement);
                }
                errorElement.textContent = message;
            } else if (errorElement) {
                errorElement.remove();
            }

            return isValid;
        },

        validateForm(form) {
            const inputs = form.querySelectorAll('input, textarea, select');
            let isValid = true;

            inputs.forEach(input => {
                if (!this.validateField(input)) {
                    isValid = false;
                }
            });

            return isValid;
        }
    };

    // =================================================================
    // ACCESSIBILITY ENHANCEMENTS
    // =================================================================
    const Accessibility = {
        init() {
            this.setupFocusManagement();
            this.setupAriaLabels();
            this.setupReducedMotion();
            this.setupHighContrast();
        },

        setupFocusManagement() {
            // Skip to content link
            const skipLink = document.createElement('a');
            skipLink.href = '#main-content';
            skipLink.textContent = 'Skip to main content';
            skipLink.className = 'skip-link sr-only';
            document.body.insertBefore(skipLink, document.body.firstChild);

            // Focus visible polyfill for older browsers
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Tab') {
                    document.body.classList.add('keyboard-navigation');
                }
            });

            document.addEventListener('mousedown', () => {
                document.body.classList.remove('keyboard-navigation');
            });
        },

        setupAriaLabels() {
            // Add aria-labels to interactive elements without text
            const iconButtons = document.querySelectorAll('button:not([aria-label]):empty');
            iconButtons.forEach(button => {
                const icon = button.textContent || button.innerHTML;
                if (icon.length <= 2) {
                    button.setAttribute('aria-label', 'Button');
                }
            });
        },

        setupReducedMotion() {
            // Respect user's motion preferences
            const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
            if (mediaQuery.matches) {
                document.documentElement.style.setProperty('--transition-fast', '0ms');
                document.documentElement.style.setProperty('--transition-normal', '0ms');
                document.documentElement.style.setProperty('--transition-slow', '0ms');
            }
        },

        setupHighContrast() {
            // Detect high contrast mode
            const mediaQuery = window.matchMedia('(prefers-contrast: high)');
            if (mediaQuery.matches) {
                document.body.classList.add('high-contrast');
            }
        }
    };

    // =================================================================
    // PERFORMANCE MONITORING
    // =================================================================
    const Performance = {
        init() {
            this.setupLazyLoading();
            this.monitorCoreWebVitals();
        },

        setupLazyLoading() {
            if ('IntersectionObserver' in window) {
                const images = document.querySelectorAll('img[data-src]');
                const imageObserver = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            const img = entry.target;
                            img.src = img.dataset.src;
                            img.removeAttribute('data-src');
                            imageObserver.unobserve(img);
                        }
                    });
                });

                images.forEach(img => imageObserver.observe(img));
            }
        },

        monitorCoreWebVitals() {
            // Basic performance monitoring
            window.addEventListener('load', () => {
                const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
                
                // Log any performance issues
                if (loadTime > 3000) {
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
            });
        }
    };

    // =================================================================
    // CULTURAL INTEGRATION
    // =================================================================
    const CulturalIntegration = {
        init() {
            this.setupTeReoDisplay();
            this.setupCulturalElements();
        },

        setupTeReoDisplay() {
            // Toggle Te Reo Māori display
            const toggleButton = document.querySelector('.te-reo-toggle');
            if (toggleButton) {
                toggleButton.addEventListener('click', () => {
                    document.body.classList.toggle('show-te-reo');
                    const isShowing = document.body.classList.contains('show-te-reo');
                    toggleButton.textContent = isShowing ? 'Hide Te Reo' : 'Show Te Reo';
                });
            }
        },

        setupCulturalElements() {
            // Add cultural context to educational content
            const culturalElements = document.querySelectorAll('[data-cultural-context]');
            culturalElements.forEach(element => {
                const context = element.getAttribute('data-cultural-context');
                element.setAttribute('title', `Cultural context: ${context}`);
            });
        }
    };

    // =================================================================
    // ERROR HANDLING
    // =================================================================
    const ErrorHandling = {
        init() {
            window.addEventListener('error', this.handleError.bind(this));
            window.addEventListener('unhandledrejection', this.handlePromiseRejection.bind(this));
        },

        handleError(event) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        // In production, you might want to send this to an error tracking service
        },

        handlePromiseRejection(event) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        event.preventDefault();
        }
    };

    // =================================================================
    // BADGE SYSTEM LOADER (CSP-safe)
    // =================================================================
    function loadBadgeSystemCspSafe() {
        if (document.documentElement.getAttribute('data-badge-system-loaded') === '1') return;
        fetch('/components/badge-system.html')
            .then(r => r.text())
            .then(html => {
                const wrapper = document.createElement('div');
                wrapper.innerHTML = html;
                const styleEl = wrapper.querySelector('style');
                const scriptEl = wrapper.querySelector('script');
                
                // Add style if exists and not already loaded
                if (styleEl && !document.head.querySelector('style[data-badge-system="1"]')) {
                    styleEl.setAttribute('data-badge-system', '1');
                    document.head.appendChild(styleEl);
                }
                
                // Add script with proper error handling
                if (scriptEl && scriptEl.textContent && !document.body.querySelector('script[data-badge-system="1"]')) {
                    try {
                        const scriptContent = scriptEl.textContent.trim();
                        // Validate script has content before creating element
                        if (scriptContent && scriptContent.length > 10) {
                            const s = document.createElement('script');
                            s.textContent = scriptContent;
                            s.setAttribute('data-badge-system', '1');
                            document.body.appendChild(s);
                        }
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
        }
                }
                document.documentElement.setAttribute('data-badge-system-loaded', '1');
            })
            .catch(e => {
                // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        });
    }

    // =================================================================
    // INITIALIZATION
    // =================================================================
    function init() {
        // Initialize all modules
        Navigation.init();
        Interactions.init();
        Accessibility.init();
        Performance.init();
        CulturalIntegration.init();
        ErrorHandling.init();
        loadBadgeSystemCspSafe();

        // Mark as initialized
        document.body.classList.add('js-initialized');
        
        // Dispatch custom event
        document.dispatchEvent(new CustomEvent('teKeteAkoReady', {
            detail: {
                version: '1.0.0',
                timestamp: Date.now()
            }
        }));

    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Expose utilities for external use
    window.TeKeteAko = {
        Utils,
        Navigation,
        Interactions,
        Accessibility,
        Performance,
        CulturalIntegration
    };

})();

/**
 * Professional UX Enhancements for Te Kete Ako
 * Adds smooth animations, lazy loading, and modern interactions
 */

// Smooth scroll to anchors
document.addEventListener('DOMContentLoaded', () => {
    // Add smooth scrolling for all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId !== '#' && targetId !== '#!') {
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    e.preventDefault();
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Lazy load images
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });

    // Add entrance animations to cards
    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 100); // Stagger animations
                cardObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.card, .lesson-card, .unit-card, .value-card, .resource-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        cardObserver.observe(card);
    });

    // Back to top button
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '↑';
    backToTop.className = 'back-to-top no-print';
    backToTop.style.cssText = `
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: var(--color-primary, #2C5F41);
        color: white;
        border: none;
        font-size: 1.5rem;
        cursor: pointer;
        opacity: 0;
        transform: translateY(100px);
        transition: all 0.3s ease;
        z-index: 1000;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    `;
    backToTop.setAttribute('aria-label', 'Back to top');
    document.body.appendChild(backToTop);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
            backToTop.style.opacity = '1';
            backToTop.style.transform = 'translateY(0)';
        } else {
            backToTop.style.opacity = '0';
            backToTop.style.transform = 'translateY(100px)';
        }
    });

    backToTop.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Add hover effect to external links
    document.querySelectorAll('a[target="_blank"]').forEach(link => {
        if (!link.querySelector('.external-icon')) {
            const icon = document.createElement('span');
            icon.className = 'external-icon';
            icon.innerHTML = ' ↗';
            icon.style.cssText = 'font-size: 0.8em; opacity: 0.7;';
            link.appendChild(icon);
        }
    });

    // Loading state for buttons
    document.querySelectorAll('[data-loading]').forEach(button => {
        button.addEventListener('click', function() {
            if (!this.classList.contains('loading')) {
                this.classList.add('loading');
                this.dataset.originalText = this.innerHTML;
                // Remove loading class after action completes (example: 2 seconds)
                setTimeout(() => {
                    this.classList.remove('loading');
                    this.innerHTML = this.dataset.originalText;
                }, 2000);
            }
        });
    });

    // Form enhancements
    document.querySelectorAll('input, textarea, select').forEach(field => {
        // Add floating labels effect
        field.addEventListener('focus', function() {
            this.parentElement?.classList.add('focused');
        });

        field.addEventListener('blur', function() {
            if (!this.value) {
                this.parentElement?.classList.remove('focused');
            }
        });

        // Add validation feedback
        field.addEventListener('invalid', function(e) {
            e.preventDefault();
            this.classList.add('error');
            const errorMsg = this.dataset.errorMessage || 'Please fill out this field';
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.textContent = errorMsg;
            errorDiv.style.cssText = 'color: #d32f2f; font-size: 0.875rem; margin-top: 0.25rem;';
            
            // Remove existing error message
            const existingError = this.parentElement?.querySelector('.error-message');
            if (existingError) existingError.remove();
            
            this.parentElement?.appendChild(errorDiv);
        });

        field.addEventListener('input', function() {
            this.classList.remove('error');
            const errorMsg = this.parentElement?.querySelector('.error-message');
            if (errorMsg) errorMsg.remove();
        });
    });

    // Add keyboard navigation enhancements
    document.addEventListener('keydown', (e) => {
        // Escape key closes modals/overlays
        if (e.key === 'Escape') {
            document.querySelectorAll('.modal, .overlay, .mobile-nav-overlay').forEach(el => {
                if (el.style.display !== 'none') {
                    el.style.display = 'none';
                    el.classList.remove('active');
                }
            });
        }
    });

    // Console message for developers
    console.log('%c🧺 Te Kete Ako', 'font-size: 2rem; font-weight: bold; color: #2C5F41;');
    console.log('%cProfessional UX enhancements loaded ✨', 'font-size: 1rem; color: #666;');
    console.log('%cMātauranga Māori meets modern web development', 'font-size: 0.9rem; color: #999; font-style: italic;');
});

// Add page load animation
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
    
    // Fade in body
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    requestAnimationFrame(() => {
        document.body.style.opacity = '1';
    });
});

// Performance monitoring (non-intrusive)
if ('performance' in window) {
    window.addEventListener('load', () => {
        const perfData = performance.getEntriesByType('navigation')[0];
        if (perfData) {
            const loadTime = perfData.loadEventEnd - perfData.loadEventStart;
            console.log(`⚡ Page loaded in ${loadTime.toFixed(0)}ms`);
        }
    });
}

// Export for use in other scripts
window.TeKeteAko = window.TeKeteAko || {};
window.TeKeteAko.ux = {
    version: '1.0.0',
    initialized: true,
    enableSmoothScroll: true,
    enableLazyLoad: true,
    enableAnimations: true
};


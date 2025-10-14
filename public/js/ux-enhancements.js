/**
 * UX ENHANCEMENTS - Te Kete Ako Professional Polish
 * Smooth animations, scroll effects, interactive elements
 */

(function() {
    'use strict';

    // =================================================================
    // SMOOTH SCROLL TO ANCHORS
    // =================================================================
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const href = this.getAttribute('href');
            if (href === '#') return;
            
                    e.preventDefault();
                    const target = document.querySelector(href);
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                }
            });
        });

    // =================================================================
    // STICKY HEADER ON SCROLL
    // =================================================================
    const header = document.querySelector('.site-header');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            header?.classList.add('scrolled');
        } else {
            header?.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });

    // =================================================================
    // FADE IN ON SCROLL OBSERVER
    // =================================================================
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                }
            });
        }, observerOptions);

    // Observe all elements with fade-in-scroll class
    document.querySelectorAll('.fade-in-scroll').forEach(el => {
            observer.observe(el);
    });

    // Auto-add fade-in to major sections
    document.querySelectorAll('section').forEach((section, index) => {
        if (index > 0) { // Skip hero
            section.classList.add('fade-in-scroll');
            observer.observe(section);
        }
    });

    // =================================================================
    // BACK TO TOP BUTTON
    // =================================================================
    const backToTop = document.createElement('div');
    backToTop.className = 'back-to-top';
    backToTop.innerHTML = '↑';
    backToTop.setAttribute('aria-label', 'Back to top');
    backToTop.setAttribute('role', 'button');
    backToTop.setAttribute('tabindex', '0');
    document.body.appendChild(backToTop);

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });

    backToTop.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // =================================================================
    // SCROLL PROGRESS INDICATOR
    // =================================================================
    const scrollProgress = document.createElement('div');
    scrollProgress.className = 'scroll-progress';
    document.body.appendChild(scrollProgress);

    window.addEventListener('scroll', () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        scrollProgress.style.width = scrolled + '%';
    });

    // =================================================================
    // CARD HOVER EFFECTS - Consistent Across Site
    // =================================================================
    document.querySelectorAll('.featured-card, .value-card, .resource-card, .lesson-card, .unit-card, .content-card').forEach(card => {
        card.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
        
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-8px)';
            this.style.boxShadow = '0 20px 40px rgba(0, 0, 0, 0.15)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
            this.style.boxShadow = '';
        });
    });

    // =================================================================
    // BUTTON RIPPLE EFFECT
    // =================================================================
    document.querySelectorAll('.btn, .print-button').forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            Object.assign(ripple.style, {
                position: 'absolute',
                borderRadius: '50%',
                background: 'rgba(255, 255, 255, 0.6)',
                transform: 'scale(0)',
                animation: 'ripple 0.6s ease-out',
                pointerEvents: 'none'
            });
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            
            setTimeout(() => ripple.remove(), 600);
        });
    });

    // Add ripple animation
    const style = document.createElement('style');
    style.textContent = `
            @keyframes ripple {
                to {
                    transform: scale(2);
                    opacity: 0;
                }
            }
    `;
    document.head.appendChild(style);

    // =================================================================
    // TOAST NOTIFICATION SYSTEM
    // =================================================================
    window.showToast = function(message, type = 'success', duration = 3000) {
        let container = document.querySelector('.toast-container');
        if (!container) {
            container = document.createElement('div');
            container.className = 'toast-container';
            document.body.appendChild(container);
        }

        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.textContent = message;
        container.appendChild(toast);

        setTimeout(() => {
            toast.style.animation = 'slideOutRight 0.4s ease';
            setTimeout(() => toast.remove(), 400);
        }, duration);
    };

    // =================================================================
    // LOADING OVERLAY HELPER
    // =================================================================
    window.showLoading = function() {
        let overlay = document.querySelector('.loading-overlay');
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.className = 'loading-overlay';
            overlay.innerHTML = `
                <div class="loading-content">
                    <div class="loading-spinner"></div>
                    <p style="color: var(--color-primary); font-weight: 600;">Loading...</p>
                </div>
            `;
            document.body.appendChild(overlay);
        }
        overlay.classList.add('active');
    };

    window.hideLoading = function() {
        const overlay = document.querySelector('.loading-overlay');
        if (overlay) {
            overlay.classList.remove('active');
        }
    };

    // =================================================================
    // FILTER PILLS INTERACTION
    // =================================================================
    document.querySelectorAll('.filter-pill').forEach(pill => {
        pill.addEventListener('click', function() {
            // Toggle active state
            this.classList.toggle('active');
            
            // Trigger filter update (implement filtering logic as needed)
            const activeFilters = Array.from(document.querySelectorAll('.filter-pill.active'))
                .map(p => p.dataset.filter);
            
            console.log('Active filters:', activeFilters);
            // Implement filtering logic here based on your needs
        });
    });

    // =================================================================
    // LAZY LOADING IMAGES
    // =================================================================
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('loading');
                img.classList.add('loaded');
                imageObserver.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        img.classList.add('loading');
        imageObserver.observe(img);
    });

    // =================================================================
    // KEYBOARD NAVIGATION IMPROVEMENTS
    // =================================================================
    document.addEventListener('keydown', (e) => {
        // ESC to close modals/overlays
        if (e.key === 'Escape') {
            document.querySelectorAll('.modal, .overlay').forEach(el => {
                el.classList.remove('active');
            });
        }
    });

    // =================================================================
    // CONSOLE WELCOME MESSAGE
    // =================================================================
    console.log('%c🧺 Te Kete Ako - Kia ora!', 'font-size: 20px; font-weight: bold; color: #4a6e2a;');
    console.log('%cProfessional Educational Platform', 'font-size: 14px; color: #666;');
    console.log('%c1,414 resources • 132% GraphRAG coverage • Coordinated by 12 AI agents', 'font-size: 12px; color: #999;');
    console.log('%cBuilt with manaakitanga 🌿', 'font-size: 12px; color: #7a6b1f; font-style: italic;');

    // =================================================================
    // PERFORMANCE MONITORING (Optional)
    // =================================================================
    if (window.performance && window.performance.timing) {
        window.addEventListener('load', () => {
            setTimeout(() => {
                const perfData = window.performance.timing;
                const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
                console.log(`⚡ Page loaded in ${pageLoadTime}ms`);
            }, 0);
        });
    }

})();

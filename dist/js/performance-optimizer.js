/**
 * PERFORMANCE OPTIMIZER - Te Kete Ako
 * Mobile-first performance enhancements
 */

class PerformanceOptimizer {
    constructor() {
        this.init();
    }

    init() {
        this.setupLazyLoading();
        this.optimizeImages();
        this.setupIntersectionObserver();
        this.deferNonCriticalCSS();
        this.preloadCriticalResources();
        
        console.log('🚀 Performance Optimizer initialized');
    }

    setupLazyLoading() {
        // Lazy load images
        const images = document.querySelectorAll('img[data-src]');
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        images.forEach(img => {
            imageObserver.observe(img);
        });

        // Lazy load background images
        const bgImages = document.querySelectorAll('[data-bg]');
        const bgObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const element = entry.target;
                    element.style.backgroundImage = `url('${element.dataset.bg}')`;
                    element.classList.add('loaded');
                    bgObserver.unobserve(element);
                }
            });
        });

        bgImages.forEach(el => {
            bgObserver.observe(el);
        });
    }

    optimizeImages() {
        // Convert existing images to lazy loading
        const existingImages = document.querySelectorAll('img:not([data-src]):not([data-critical])');
        existingImages.forEach(img => {
            if (img.src && !img.classList.contains('critical-image')) {
                // Skip images that are already visible or critical
                const rect = img.getBoundingClientRect();
                const isInViewport = rect.top < window.innerHeight && rect.bottom > 0;
                
                if (!isInViewport && !img.src.includes('data:image')) {
                    // Add loading placeholder
                    const placeholder = this.createImagePlaceholder(img.naturalWidth || 200, img.naturalHeight || 120);
                    img.dataset.src = img.src;
                    img.src = placeholder;
                    img.classList.add('lazy');
                    img.loading = 'lazy';
                }
            }
        });
    }

    createImagePlaceholder(width = 200, height = 120) {
        // Create SVG placeholder with cultural pattern
        return `data:image/svg+xml;base64,${btoa(`
            <svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="${width}" height="${height}" fill="#f3f4f6"/>
                <defs>
                    <pattern id="koru" patternUnits="userSpaceOnUse" width="20" height="20">
                        <path d="M10,10 Q15,5 20,10 Q15,15 10,10" fill="none" stroke="rgba(0,176,185,0.2)" stroke-width="1"/>
                    </pattern>
                </defs>
                <rect width="${width}" height="${height}" fill="url(#koru)"/>
                <text x="${width/2}" y="${height/2}" font-family="Arial" font-size="14" fill="#9ca3af" text-anchor="middle" dy="0.3em">Loading...</text>
            </svg>
        `)}`;
    }

    setupIntersectionObserver() {
        // Fade in animations for elements as they come into view
        const animateElements = document.querySelectorAll('.animate-on-scroll, .cultural-card, .feature-card');
        const animationObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                    animationObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '50px 0px'
        });

        animateElements.forEach(el => {
            animationObserver.observe(el);
        });
    }

    deferNonCriticalCSS() {
        // Defer non-critical CSS loading
        const nonCriticalCSS = [
            'css/lesson-plan.css',
            'css/youtube-library.css',
            'css/digital-purakau.css'
        ];

        nonCriticalCSS.forEach(cssFile => {
            this.loadCSSAsync(cssFile);
        });
    }

    loadCSSAsync(href) {
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = href;
        link.media = 'print';
        link.onload = function() {
            this.media = 'all';
        };
        document.head.appendChild(link);
    }

    preloadCriticalResources() {
        // Preload critical fonts
        const criticalFonts = [
            'https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap',
            'https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap'
        ];

        criticalFonts.forEach(font => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.href = font;
            link.as = 'style';
            link.crossOrigin = 'anonymous';
            document.head.appendChild(link);
        });
    }

    // Mobile performance optimizations
    optimizeForMobile() {
        // Reduce animations on low-end devices
        if (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 4) {
            document.documentElement.classList.add('reduce-motion');
        }

        // Optimize touch interactions
        document.addEventListener('touchstart', function() {}, { passive: true });
        document.addEventListener('touchmove', function() {}, { passive: true });

        // Prevent 300ms click delay on older mobile browsers
        if ('ontouchstart' in window) {
            document.body.style.touchAction = 'manipulation';
        }
    }

    // Monitor performance
    monitorPerformance() {
        if ('performance' in window) {
            window.addEventListener('load', () => {
                setTimeout(() => {
                    const perfData = performance.getEntriesByType('navigation')[0];
                    const loadTime = perfData.loadEventEnd - perfData.fetchStart;
                    
                    console.log(`📊 Page load time: ${Math.round(loadTime)}ms`);
                    
                    // Send performance data (only in development)
                    if (window.ENV && window.ENV.IS_DEVELOPMENT) {
                        console.log('📈 Performance metrics:', {
                            loadTime: Math.round(loadTime),
                            domContentLoaded: Math.round(perfData.domContentLoadedEventEnd - perfData.fetchStart),
                            firstPaint: performance.getEntriesByType('paint')[0]?.startTime || 0
                        });
                    }
                }, 0);
            });
        }
    }
}

// Initialize performance optimizer when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const perfOptimizer = new PerformanceOptimizer();
    perfOptimizer.optimizeForMobile();
    perfOptimizer.monitorPerformance();
});

// Add lazy loading CSS
const lazyCSS = document.createElement('style');
lazyCSS.textContent = `
    .lazy {
        opacity: 0.6;
        transition: opacity 0.3s;
    }
    
    .lazy.loaded {
        opacity: 1;
    }
    
    .animate-on-scroll {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    
    .animate-on-scroll.animate-in {
        opacity: 1;
        transform: translateY(0);
    }
    
    @media (prefers-reduced-motion: reduce), .reduce-motion {
        .animate-on-scroll,
        .lazy {
            transition: none !important;
            transform: none !important;
            animation: none !important;
        }
    }
    
    /* Mobile performance optimizations */
    @media (max-width: 768px) {
        * {
            -webkit-tap-highlight-color: transparent;
        }
        
        .hero-cultural-pattern,
        .background-pattern {
            display: none; /* Remove complex patterns on mobile */
        }
        
        .shadow-strong {
            box-shadow: var(--shadow-light) !important; /* Lighter shadows */
        }
    }
`;
document.head.appendChild(lazyCSS);

console.log('⚡ Performance optimization loaded');
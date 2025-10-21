/**
 * TE KETE AKO - MOBILE PERFORMANCE OPTIMIZER
 * Optimized for classroom tablet usage and slow internet connections
 * Mangakōtukutuku College Enhancement
 */

class MobilePerformanceOptimizer {
    constructor() {
        this.connection = null;
        this.isSlowConnection = false;
        this.touchDevice = false;
        this.observer = null;
        
        this.init();
    }
    
    init() {
        this.detectConnection();
        this.detectTouchDevice();
        this.optimizeForDevice();
        this.setupLazyLoading();
        this.setupResourceHints();
        this.setupConnectionObserver();
        this.setupPerformanceMonitoring();
    }
    
    /**
     * Detect network connection speed
     */
    detectConnection() {
        // Check for Network Information API support
        this.connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
        
        if (this.connection) {
            // Detect slow connections
            const slowConnections = ['slow-2g', '2g', '3g'];
            this.isSlowConnection = slowConnections.includes(this.connection.effectiveType) || 
                                   this.connection.downlink < 1.5;
            
            // Apply optimizations for slow connections
            if (this.isSlowConnection) {
                this.enableSlowConnectionMode();
            }
            
            // Listen for connection changes
            this.connection.addEventListener('change', () => {
                this.detectConnection();
            });
        } else {
            // Fallback: detect slow connections through timing
            this.detectSlowConnectionFallback();
        }
    }
    
    /**
     * Fallback method to detect slow connections
     */
    detectSlowConnectionFallback() {
        const startTime = Date.now();
        const imageTest = new Image();
        
        imageTest.onload = () => {
            const duration = Date.now() - startTime;
            // If test image takes more than 1 second, assume slow connection
            if (duration > 1000) {
                this.isSlowConnection = true;
                this.enableSlowConnectionMode();
            }
        };
        
        imageTest.onerror = () => {
            this.isSlowConnection = true;
            this.enableSlowConnectionMode();
        };
        
        // Small test image (1x1 pixel)
        imageTest.src = 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7';
    }
    
    /**
     * Detect touch device capabilities
     */
    detectTouchDevice() {
        this.touchDevice = ('ontouchstart' in window) || 
                          (navigator.maxTouchPoints > 0) || 
                          (navigator.msMaxTouchPoints > 0);
                          
        if (this.touchDevice) {
            document.body.classList.add('touch-device');
            this.optimizeForTouch();
        }
    }
    
    /**
     * Enable optimizations for slow connections
     */
    enableSlowConnectionMode() {
        document.body.classList.add('slow-connection');
        
        // Disable non-essential animations
        this.disableAnimations();
        
        // Reduce image quality
        this.optimizeImages();
        
        // Defer non-critical resources
        this.deferNonCriticalResources();
        
        // Show connection indicator
        this.showConnectionIndicator('slow');
        
        console.log('🐌 Slow connection detected - performance mode enabled');
    }
    
    /**
     * Optimize for touch devices
     */
    optimizeForTouch() {
        // Increase touch target sizes
        this.enhanceTouchTargets();
        
        // Add touch feedback
        this.addTouchFeedback();
        
        // Optimize scrolling
        this.optimizeScrolling();
        
        console.log('👆 Touch device detected - touch optimizations enabled');
    }
    
    /**
     * Setup lazy loading for images and videos
     */
    setupLazyLoading() {
        // Native lazy loading support
        if ('loading' in HTMLImageElement.prototype) {
            const images = document.querySelectorAll('img[data-src]');
            images.forEach(img => {
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                img.setAttribute('loading', 'lazy');
            });
        } else {
            // Intersection Observer fallback
            this.setupIntersectionObserver();
        }
        
        // Lazy load videos
        this.setupVideoLazyLoading();
    }
    
    /**
     * Setup Intersection Observer for lazy loading
     */
    setupIntersectionObserver() {
        if ('IntersectionObserver' in window) {
            this.observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const element = entry.target;
                        
                        if (element.dataset.src) {
                            element.src = element.dataset.src;
                            element.removeAttribute('data-src');
                        }
                        
                        if (element.dataset.srcset) {
                            element.srcset = element.dataset.srcset;
                            element.removeAttribute('data-srcset');
                        }
                        
                        this.observer.unobserve(element);
                    }
                });
            }, {
                rootMargin: '50px 0px',
                threshold: 0.01
            });
            
            // Observe images and videos
            const lazyElements = document.querySelectorAll('img[data-src], video[data-src]');
            lazyElements.forEach(element => {
                this.observer.observe(element);
            });
        }
    }
    
    /**
     * Setup video lazy loading
     */
    setupVideoLazyLoading() {
        const videos = document.querySelectorAll('video[data-src]');
        
        videos.forEach(video => {
            // Only load videos on fast connections or when user interacts
            if (!this.isSlowConnection || video.hasAttribute('data-autoload')) {
                this.loadVideo(video);
            } else {
                // Show play button overlay for manual loading
                this.addVideoLoadTrigger(video);
            }
        });
    }
    
    /**
     * Load video element
     */
    loadVideo(video) {
        if (video.dataset.src) {
            video.src = video.dataset.src;
            video.removeAttribute('data-src');
        }
        
        // Load poster image
        if (video.dataset.poster) {
            video.poster = video.dataset.poster;
            video.removeAttribute('data-poster');
        }
    }
    
    /**
     * Add manual video load trigger
     */
    addVideoLoadTrigger(video) {
        const overlay = document.createElement('div');
        overlay.className = 'video-load-overlay';
        overlay.innerHTML = `
            <button class="video-load-btn" aria-label="Load video">
                <span class="play-icon">▶️</span>
                <span class="load-text">Tap to load video</span>
            </button>
        `;
        
        overlay.addEventListener('click', () => {
            this.loadVideo(video);
            overlay.remove();
            video.play();
        });
        
        video.parentNode.insertBefore(overlay, video.nextSibling);
    }
    
    /**
     * Setup resource hints for better loading
     */
    setupResourceHints() {
        // Preconnect to important domains
        const domains = [
            'fonts.googleapis.com',
            'fonts.gstatic.com',
            'cdn.jsdelivr.net'
        ];
        
        domains.forEach(domain => {
            const link = document.createElement('link');
            link.rel = 'preconnect';
            link.href = `https://${domain}`;
            link.crossOrigin = 'anonymous';
            document.head.appendChild(link);
        });
        
        // DNS prefetch for external resources
        this.prefetchDNS();
    }
    
    /**
     * Prefetch DNS for external resources
     */
    prefetchDNS() {
        const externalLinks = document.querySelectorAll('a[href^="http"]');
        const domains = new Set();
        
        externalLinks.forEach(link => {
            try {
                const url = new URL(link.href);
                domains.add(url.hostname);
            } catch (e) {
                // Invalid URL, skip
            }
        });
        
        domains.forEach(domain => {
            const link = document.createElement('link');
            link.rel = 'dns-prefetch';
            link.href = `//${domain}`;
            document.head.appendChild(link);
        });
    }
    
    /**
     * Disable non-essential animations on slow connections
     */
    disableAnimations() {
        const style = document.createElement('style');
        style.textContent = `
            .slow-connection * {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
            
            .slow-connection .cultural-pattern,
            .slow-connection .koru-pattern {
                display: none !important;
            }
            
            .slow-connection .complex-animation {
                display: none !important;
            }
        `;
        document.head.appendChild(style);
    }
    
    /**
     * Optimize images for slow connections
     */
    optimizeImages() {
        const images = document.querySelectorAll('img');
        
        images.forEach(img => {
            // Add loading placeholder
            if (!img.complete && !img.src.includes('data:')) {
                img.classList.add('loading-skeleton');
                
                img.onload = () => {
                    img.classList.remove('loading-skeleton');
                };
            }
            
            // Defer offscreen images
            if (this.isElementBelowFold(img)) {
                const placeholder = this.createImagePlaceholder(img);
                img.parentNode.replaceChild(placeholder, img);
            }
        });
    }
    
    /**
     * Check if element is below the fold
     */
    isElementBelowFold(element) {
        const rect = element.getBoundingClientRect();
        return rect.top > window.innerHeight;
    }
    
    /**
     * Create image placeholder
     */
    createImagePlaceholder(img) {
        const placeholder = document.createElement('div');
        placeholder.className = 'image-placeholder';
        placeholder.style.cssText = `
            width: ${img.width || 200}px;
            height: ${img.height || 150}px;
            background: #f0f0f0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            color: #666;
            border-radius: 8px;
            cursor: pointer;
        `;
        placeholder.innerHTML = `
            <span>📷 Tap to load image</span>
        `;
        
        placeholder.addEventListener('click', () => {
            placeholder.parentNode.replaceChild(img, placeholder);
        });
        
        return placeholder;
    }
    
    /**
     * Defer non-critical resources
     */
    deferNonCriticalResources() {
        // Defer non-critical stylesheets
        const nonCriticalCSS = document.querySelectorAll('link[rel="stylesheet"][data-defer]');
        nonCriticalCSS.forEach(link => {
            link.media = 'print';
            link.onload = () => {
                link.media = 'all';
            };
        });
        
        // Defer non-critical scripts
        const nonCriticalJS = document.querySelectorAll('script[data-defer]');
        nonCriticalJS.forEach(script => {
            script.defer = true;
        });
    }
    
    /**
     * Enhance touch targets for better usability
     */
    enhanceTouchTargets() {
        const interactive = document.querySelectorAll('button, a, input, select, textarea');
        
        interactive.forEach(element => {
            const rect = element.getBoundingClientRect();
            
            // Ensure minimum touch target size (48x48px)
            if (rect.width < 48 || rect.height < 48) {
                element.style.minWidth = '48px';
                element.style.minHeight = '48px';
                element.style.display = 'inline-flex';
                element.style.alignItems = 'center';
                element.style.justifyContent = 'center';
            }
            
            // Add touch target indicator class
            element.classList.add('touch-target');
        });
    }
    
    /**
     * Add touch feedback to interactive elements
     */
    addTouchFeedback() {
        const touchTargets = document.querySelectorAll('.touch-target');
        
        touchTargets.forEach(target => {
            target.addEventListener('touchstart', () => {
                target.classList.add('touch-active');
            });
            
            target.addEventListener('touchend', () => {
                setTimeout(() => {
                    target.classList.remove('touch-active');
                }, 150);
            });
        });
        
        // Add CSS for touch feedback
        const style = document.createElement('style');
        style.textContent = `
            .touch-target {
                transition: transform 0.1s ease, opacity 0.1s ease;
            }
            
            .touch-target.touch-active {
                transform: scale(0.98);
                opacity: 0.8;
            }
        `;
        document.head.appendChild(style);
    }
    
    /**
     * Optimize scrolling performance
     */
    optimizeScrolling() {
        // Enable hardware acceleration for scrolling elements
        const scrollElements = document.querySelectorAll('.scroll-container, .mobile-nav-items');
        
        scrollElements.forEach(element => {
            element.style.transform = 'translateZ(0)';
            element.style.willChange = 'transform';
        });
        
        // Throttle scroll events
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            if (scrollTimeout) {
                cancelAnimationFrame(scrollTimeout);
            }
            
            scrollTimeout = requestAnimationFrame(() => {
                this.handleScroll();
            });
        }, { passive: true });
    }
    
    /**
     * Handle scroll events efficiently
     */
    handleScroll() {
        // Hide/show mobile navigation on scroll (if needed)
        const mobileNav = document.querySelector('.mobile-bottom-nav');
        
        if (mobileNav && this.lastScrollY !== undefined) {
            const scrollingDown = window.scrollY > this.lastScrollY;
            
            if (scrollingDown && window.scrollY > 100) {
                mobileNav.style.transform = 'translateY(100%)';
            } else {
                mobileNav.style.transform = 'translateY(0)';
            }
        }
        
        this.lastScrollY = window.scrollY;
    }
    
    /**
     * Setup connection observer
     */
    setupConnectionObserver() {
        if (this.connection) {
            this.connection.addEventListener('change', () => {
                this.handleConnectionChange();
            });
        }
    }
    
    /**
     * Handle connection changes
     */
    handleConnectionChange() {
        const wasSlowConnection = this.isSlowConnection;
        this.detectConnection();
        
        if (this.isSlowConnection && !wasSlowConnection) {
            this.showConnectionIndicator('slow');
            this.enableSlowConnectionMode();
        } else if (!this.isSlowConnection && wasSlowConnection) {
            this.showConnectionIndicator('fast');
            this.disableSlowConnectionMode();
        }
    }
    
    /**
     * Disable slow connection mode
     */
    disableSlowConnectionMode() {
        document.body.classList.remove('slow-connection');
        
        // Re-enable animations
        const slowStyles = document.querySelector('style[data-slow-connection]');
        if (slowStyles) {
            slowStyles.remove();
        }
        
        console.log('🚀 Fast connection restored - full features enabled');
    }
    
    /**
     * Show connection indicator
     */
    showConnectionIndicator(type) {
        // Remove existing indicator
        const existing = document.querySelector('.connection-indicator');
        if (existing) {
            existing.remove();
        }
        
        const indicator = document.createElement('div');
        indicator.className = 'connection-indicator';
        indicator.innerHTML = type === 'slow' ? 
            '🐌 Slow connection detected - optimized mode' : 
            '🚀 Connection improved - full features restored';
        
        indicator.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'slow' ? '#f59e0b' : '#10b981'};
            color: white;
            padding: 12px 16px;
            border-radius: 8px;
            font-size: 14px;
            z-index: 10000;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            animation: slideInFromRight 0.3s ease;
        `;
        
        document.body.appendChild(indicator);
        
        // Remove after 5 seconds
        setTimeout(() => {
            if (indicator.parentNode) {
                indicator.style.animation = 'slideOutToRight 0.3s ease';
                setTimeout(() => {
                    indicator.remove();
                }, 300);
            }
        }, 5000);
    }
    
    /**
     * Setup performance monitoring
     */
    setupPerformanceMonitoring() {
        // Monitor Critical Web Vitals
        this.monitorWebVitals();
        
        // Monitor memory usage
        this.monitorMemoryUsage();
        
        // Monitor loading performance
        this.monitorLoadingPerformance();
    }
    
    /**
     * Monitor Web Vitals
     */
    monitorWebVitals() {
        // First Contentful Paint
        this.observePerformanceEntry('paint', (entries) => {
            entries.forEach(entry => {
                if (entry.name === 'first-contentful-paint') {
                    console.log(`🎨 First Contentful Paint: ${entry.startTime}ms`);
                    
                    if (entry.startTime > 3000) {
                        this.showPerformanceWarning('Slow initial loading detected');
                    }
                }
            });
        });
        
        // Largest Contentful Paint
        this.observePerformanceEntry('largest-contentful-paint', (entries) => {
            const lastEntry = entries[entries.length - 1];
            console.log(`🖼️ Largest Contentful Paint: ${lastEntry.startTime}ms`);
            
            if (lastEntry.startTime > 4000) {
                this.showPerformanceWarning('Content loading slowly');
            }
        });
    }
    
    /**
     * Observe performance entries
     */
    observePerformanceEntry(type, callback) {
        if ('PerformanceObserver' in window) {
            try {
                const observer = new PerformanceObserver((list) => {
                    callback(list.getEntries());
                });
                observer.observe({ entryTypes: [type] });
            } catch (e) {
                // Performance observation not supported
            }
        }
    }
    
    /**
     * Monitor memory usage
     */
    monitorMemoryUsage() {
        if ('memory' in performance) {
            setInterval(() => {
                const memory = performance.memory;
                const used = memory.usedJSHeapSize / 1048576; // Convert to MB
                const limit = memory.jsHeapSizeLimit / 1048576;
                
                if (used / limit > 0.8) {
                    this.showPerformanceWarning('High memory usage detected');
                    this.optimizeMemoryUsage();
                }
            }, 30000); // Check every 30 seconds
        }
    }
    
    /**
     * Monitor loading performance
     */
    monitorLoadingPerformance() {
        window.addEventListener('load', () => {
            const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
            console.log(`⏱️ Page load time: ${loadTime}ms`);
            
            if (loadTime > 5000) {
                this.showPerformanceWarning('Page loaded slowly');
            }
        });
    }
    
    /**
     * Optimize memory usage
     */
    optimizeMemoryUsage() {
        // Remove inactive event listeners
        this.cleanupEventListeners();
        
        // Clear image caches
        this.clearImageCaches();
        
        // Garbage collect if possible
        if (window.gc) {
            window.gc();
        }
    }
    
    /**
     * Show performance warning
     */
    showPerformanceWarning(message) {
        console.warn(`⚠️ Performance: ${message}`);
        
        // Show user-friendly notification if performance is severely impacted
        if (this.isSlowConnection) {
            this.showConnectionIndicator('slow');
        }
    }
    
    /**
     * Cleanup event listeners
     */
    cleanupEventListeners() {
        // Remove touch event listeners from elements no longer in view
        const touchElements = document.querySelectorAll('.touch-target');
        
        touchElements.forEach(element => {
            if (!this.isElementVisible(element)) {
                // Clone element to remove all event listeners
                const newElement = element.cloneNode(true);
                element.parentNode.replaceChild(newElement, element);
            }
        });
    }
    
    /**
     * Check if element is visible
     */
    isElementVisible(element) {
        const rect = element.getBoundingClientRect();
        return rect.top < window.innerHeight && rect.bottom > 0;
    }
    
    /**
     * Clear image caches
     */
    clearImageCaches() {
        const images = document.querySelectorAll('img');
        
        images.forEach(img => {
            if (!this.isElementVisible(img) && img.src.startsWith('blob:')) {
                // Revoke blob URLs to free memory
                URL.revokeObjectURL(img.src);
            }
        });
    }
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.mobileOptimizer = new MobilePerformanceOptimizer();
    });
} else {
    window.mobileOptimizer = new MobilePerformanceOptimizer();
}

// Add animation keyframes for connection indicator
const animationStyles = document.createElement('style');
animationStyles.textContent = `
    @keyframes slideInFromRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutToRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    .video-load-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.8);
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
        cursor: pointer;
    }
    
    .video-load-btn {
        background: white;
        border: none;
        border-radius: 8px;
        padding: 16px 24px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.2s ease;
    }
    
    .video-load-btn:hover {
        transform: scale(1.05);
    }
    
    .play-icon {
        font-size: 24px;
    }
    
    .image-placeholder {
        transition: opacity 0.3s ease;
    }
    
    .image-placeholder:hover {
        opacity: 0.8;
    }
`;

document.head.appendChild(animationStyles);
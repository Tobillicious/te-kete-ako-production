/**
 * LAZY LOAD IMAGES - P2-18 Performance
 * Improves page load by lazy loading images
 * Target: <2 seconds page load
 */

class LazyImageLoader {
    constructor() {
        this.init();
    }
    
    init() {
        // Use Intersection Observer for modern browsers
        if ('IntersectionObserver' in window) {
            this.observerLazyLoad();
        } else {
            // Fallback: load all images immediately
            this.loadAllImages();
        }
    }
    
    observerLazyLoad() {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    this.loadImage(img);
                    observer.unobserve(img);
                }
            });
        }, {
            rootMargin: '50px' // Start loading 50px before image enters viewport
        });
        
        // Observe all images with data-src attribute
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
    
    loadImage(img) {
        const src = img.dataset.src;
        if (src) {
            img.src = src;
            img.removeAttribute('data-src');
            img.classList.add('loaded');
        }
    }
    
    loadAllImages() {
        document.querySelectorAll('img[data-src]').forEach(img => {
            this.loadImage(img);
        });
    }
}

// Auto-initialize
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', () => {
        new LazyImageLoader();
    });
}


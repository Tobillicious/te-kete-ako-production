/**
 * COUNTER ANIMATION - Hero Stats
 * Animates numbers on page load for impact
 */

function animateCounter(element, target, duration = 2000, suffix = '') {
    const start = 0;
    const increment = target / (duration / 16); // 60fps
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current).toLocaleString() + suffix;
    }, 16);
}

function initCounters() {
    const counters = document.querySelectorAll('[data-counter]');
    
    // Use Intersection Observer for scroll-triggered animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.dataset.animated) {
                const target = parseInt(entry.target.dataset.counter);
                const suffix = entry.target.dataset.suffix || '';
                const duration = parseInt(entry.target.dataset.duration) || 2000;
                
                animateCounter(entry.target, target, duration, suffix);
                entry.target.dataset.animated = 'true';
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => observer.observe(counter));
}

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCounters);
} else {
    initCounters();
}


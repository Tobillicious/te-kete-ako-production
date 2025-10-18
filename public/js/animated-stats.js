/**
 * ✨ ANIMATED STATISTICS
 * Numbers count up on page load - wow factor!
 */

function animateValue(element, start, end, duration) {
    const range = end - start;
    const increment = range / (duration / 16); // 60fps
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        if ((increment > 0 && current >= end) || (increment < 0 && current <= end)) {
            current = end;
            clearInterval(timer);
        }
        
        // Format number with commas
        element.textContent = Math.floor(current).toLocaleString();
    }, 16);
}

// Intersection Observer to trigger animation when visible
const observeStats = () => {
    const stats = document.querySelectorAll('[data-animate-value]');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.dataset.animated) {
                const targetValue = parseInt(entry.target.dataset.animateValue);
                animateValue(entry.target, 0, targetValue, 2000);
                entry.target.dataset.animated = 'true';
            }
        });
    }, { threshold: 0.5 });
    
    stats.forEach(stat => observer.observe(stat));
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', observeStats);

// Export
window.animateStats = observeStats;


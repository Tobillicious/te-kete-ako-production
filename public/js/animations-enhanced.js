/**
 * ENHANCED ANIMATIONS
 * Professional scroll animations, transitions, and micro-interactions
 */

class EnhancedAnimations {
  constructor() {
    this.observeElements();
    this.initializeCounters();
    this.setupHoverEffects();
  }

  /**
   * Intersection Observer for scroll animations
   */
  observeElements() {
    const options = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animated');
          
          // Trigger counter animations
          if (entry.target.classList.contains('stat-counter')) {
            this.animateCounter(entry.target);
          }
        }
      });
    }, options);

    // Observe all elements with animation classes
    document.querySelectorAll('.fade-in, .slide-up, .stat-counter, .resource-card').forEach(el => {
      observer.observe(el);
    });
  }

  /**
   * Animate number counters
   */
  animateCounter(element) {
    const target = parseInt(element.getAttribute('data-target') || element.textContent.replace(/,/g, ''));
    const duration = 2000;
    const steps = 60;
    const increment = target / steps;
    const stepTime = duration / steps;
    let current = 0;

    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        element.textContent = target.toLocaleString();
        clearInterval(timer);
      } else {
        element.textContent = Math.floor(current).toLocaleString();
      }
    }, stepTime);
  }

  /**
   * Initialize all counters
   */
  initializeCounters() {
    document.querySelectorAll('.stat-counter').forEach(el => {
      const target = parseInt(el.getAttribute('data-target'));
      if (target) {
        el.textContent = '0';
      }
    });
  }

  /**
   * Setup enhanced hover effects
   */
  setupHoverEffects() {
    // Card elevation on hover
    document.querySelectorAll('.resource-card, .stat-card, .unit-node').forEach(card => {
      card.addEventListener('mouseenter', function() {
        this.style.transition = 'all 0.3s cubic-bezier(0.4, 0.0, 0.2, 1)';
      });
    });

    // Button ripple effects
    document.querySelectorAll('button, .btn').forEach(button => {
      button.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        
        this.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
      });
    });
  }

  /**
   * Smooth scroll to element
   */
  static scrollTo(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
      element.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  }

  /**
   * Parallax effect for hero sections
   */
  static initParallax() {
    const hero = document.querySelector('.hero-enhanced, .pathway-hero, .whakatauki-hero');
    if (!hero) return;

    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      hero.style.transform = `translateY(${scrolled * 0.5}px)`;
    });
  }

  /**
   * Stagger animation for lists
   */
  static staggerElements(selector, delay = 100) {
    document.querySelectorAll(selector).forEach((el, index) => {
      el.style.animationDelay = `${index * delay}ms`;
    });
  }
}

// Auto-initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  new EnhancedAnimations();
  
  // Initialize parallax if not reduced motion
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    EnhancedAnimations.initParallax();
  }
  
  // Stagger card animations
  EnhancedAnimations.staggerElements('.resource-card', 50);
});

// Export for use in other scripts
window.EnhancedAnimations = EnhancedAnimations;


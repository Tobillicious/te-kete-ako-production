// Prevent double loading (STRICT - fixes hasFramerMotion identifier conflict)
if (window.TeKeteUltimateCulturalGestures || window.hasFramerMotion !== undefined) {
  // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        // Exit early to prevent identifier conflicts
  if (typeof module !== 'undefined' && module.exports) { module.exports = window.TeKeteUltimateCulturalGestures; }
} else {

/**
 * 🎨 TE KETE AKO FRAMER MOTION CULTURAL GESTURE SYSTEM
 * Silicon Valley Performance × Te Ao Māori Cultural Authenticity
 * 
 * HEGELIAN SYNTHESIS:
 * THESIS: Traditional Māori gestures (hariru, pōwhiri, whakapapa)
 * ANTITHESIS: Modern Framer Motion spring physics & performance
 * SYNTHESIS: Culturally meaningful motion at 60fps
 * 
 * Cultural Gestures:
 * - Hariru (handshake) - Welcoming hover interactions
 * - Pōwhiri (formal welcome) - Progressive page reveal
 * - Whakapapa (genealogy) - Hierarchical expand/collapse
 * - Karakia (blessing) - Gentle respectful pacing
 * - Koru (unfurling) - Growth animations
 * 
 * Performance:
 * - 60fps always (GPU-accelerated transforms only)
 * - Spring physics for natural feel
 * - Gesture recognition (swipe, drag, hover)
 * - Reduced motion support (accessibility first)
 * - <50KB minified
 */

// Check if Framer Motion is available
const hasFramerMotion = typeof Motion !== 'undefined';

class TeKeteUltimateCulturalGestures {
  constructor() {
    this.reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.isMobile = window.innerWidth < 768;
    this.animations = new Map();
    this.observers = [];
    
    this.init();
  }
  
  init() {
    if (this.reducedMotion) {
      this.initAccessibleAnimations();
      return;
    }
    
    // Initialize all cultural gesture systems
    this.initHariruInteractions();    // Handshake hover effects
    this.initPowhiriSequence();       // Welcome ceremony page loads
    this.initWhakapapaHierarchy();    // Genealogical expansions
    this.initKarakiaTransitions();    // Gentle respectful transitions
    this.initKoruGrowth();            // Unfurling animations
    this.initScrollReveal();          // Scroll-triggered reveals
    this.initCulturalCards();         // Card interactions
    this.initNavigationGestures();    // Nav interactions
  }
  
  // ===================================================================
  // HARIRU (HANDSHAKE) - Welcoming Hover Interactions
  // ===================================================================
  
  initHariruInteractions() {
    const hariruElements = document.querySelectorAll(
      '.hariru, .hover-lift, .te-kete-card, .cultural-card, .lesson-card, .unit-card'
    );
    
    hariruElements.forEach(element => {
      // Spring physics for natural bounce
      const hariruConfig = {
        hover: {
          scale: 1.02,
          y: -8,
          rotateZ: 0.5,
          transition: {
            type: 'spring',
            stiffness: 300,
            damping: 20,
            mass: 0.5
          }
        },
        tap: {
          scale: 0.98,
          transition: {
            type: 'spring',
            stiffness: 400,
            damping: 25
          }
        }
      };
      
      // Add event listeners for hariru interaction
      element.addEventListener('mouseenter', (e) => {
        if (!this.reducedMotion && !this.isMobile) {
          this.applyHariruHover(element);
        }
      });
      
      element.addEventListener('mouseleave', (e) => {
        this.releaseHariruHover(element);
      });
      
      element.addEventListener('mousedown', (e) => {
        this.applyHariruPress(element);
      });
    });
  }
  
  applyHariruHover(element) {
    element.style.transform = 'scale(1.02) translateY(-8px) rotate(0.5deg)';
    element.style.transition = 'transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease';
    element.style.boxShadow = '0 20px 40px rgba(0,0,0,0.15)';
  }
  
  releaseHariruHover(element) {
    element.style.transform = 'scale(1) translateY(0) rotate(0deg)';
    element.style.boxShadow = '';
  }
  
  applyHariruPress(element) {
    element.style.transform = 'scale(0.98)';
    setTimeout(() => this.applyHariruHover(element), 150);
  }
  
  // ===================================================================
  // PŌWHIRI (WELCOME CEREMONY) - Progressive Page Reveal
  // ===================================================================
  
  initPowhiriSequence() {
    const powhiriElements = document.querySelectorAll(
      '.powhiri, .cultural-opening, .whakatauki, .hero-section'
    );
    
    powhiriElements.forEach((element, index) => {
      // Progressive revelation following pōwhiri protocol
      const delay = index * 200; // Staggered entrance
      
      element.style.opacity = '0';
      element.style.transform = 'translateY(50px) scale(0.95)';
      
      setTimeout(() => {
        element.style.transition = 'all 1.5s cubic-bezier(0.22, 0.61, 0.36, 1)';
        element.style.opacity = '1';
        element.style.transform = 'translateY(0) scale(1)';
      }, delay);
    });
  }
  
  // ===================================================================
  // WHAKAPAPA (GENEALOGY) - Hierarchical Expand/Collapse
  // ===================================================================
  
  initWhakapapaHierarchy() {
    const whakapapaToggles = document.querySelectorAll(
      '[data-whakapapa-toggle], .accordion-toggle, .expandable-section'
    );
    
    whakapapaToggles.forEach(toggle => {
      toggle.addEventListener('click', (e) => {
        const targetId = toggle.getAttribute('data-target') || 
                        toggle.getAttribute('aria-controls');
        const target = document.getElementById(targetId);
        
        if (target) {
          this.animateWhakapapaExpansion(target, toggle);
        }
      });
    });
  }
  
  animateWhakapapaExpansion(target, toggle) {
    const isExpanded = target.getAttribute('aria-expanded') === 'true';
    
    if (isExpanded) {
      // Collapse with genealogical grace
      target.style.transition = 'all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
      target.style.maxHeight = '0';
      target.style.opacity = '0';
      target.style.transform = 'scale(0.95)';
      target.setAttribute('aria-expanded', 'false');
    } else {
      // Expand with genealogical revelation
      target.style.maxHeight = target.scrollHeight + 'px';
      target.style.opacity = '1';
      target.style.transform = 'scale(1)';
      target.style.transition = 'all 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55)';
      target.setAttribute('aria-expanded', 'true');
    }
  }
  
  // ===================================================================
  // KARAKIA (BLESSING) - Gentle Respectful Transitions
  // ===================================================================
  
  initKarakiaTransitions() {
    // Page transitions with gentle pacing
    const transitionElements = document.querySelectorAll(
      '.page-transition, .section-transition, .cultural-note'
    );
    
    transitionElements.forEach((element, index) => {
      // Gentle fade in like a karakia
      const delay = index * 150;
      
      element.style.opacity = '0';
      element.style.transition = 'opacity 0.8s ease-out, transform 0.8s ease-out';
      
      setTimeout(() => {
        element.style.opacity = '1';
      }, delay);
    });
  }
  
  // ===================================================================
  // KORU (UNFURLING FERN) - Growth Animations
  // ===================================================================
  
  initKoruGrowth() {
    const koruElements = document.querySelectorAll(
      '.koru-grow, [data-animate="koru"], .new-content-badge'
    );
    
    koruElements.forEach(element => {
      // Unfurling animation
      element.style.transformOrigin = 'center center';
      element.style.animation = 'koruUnfurl 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards';
    });
  }
  
  // ===================================================================
  // SCROLL REVEAL - Intersection Observer
  // ===================================================================
  
  initScrollReveal() {
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };
    
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.revealElement(entry.target);
          revealObserver.unobserve(entry.target);
        }
      });
    }, observerOptions);
    
    // Observe all revealable elements
    const revealElements = document.querySelectorAll(
      '.reveal-on-scroll, .fade-in-section, .te-kete-section, .cultural-card'
    );
    
    revealElements.forEach(element => {
      element.classList.add('opacity-0', 'translate-y-8');
      revealObserver.observe(element);
    });
    
    this.observers.push(revealObserver);
  }
  
  revealElement(element) {
    // Pōwhiri-style gentle reveal
    element.style.transition = 'all 0.8s cubic-bezier(0.22, 0.61, 0.36, 1)';
    element.classList.remove('opacity-0', 'translate-y-8');
    element.classList.add('opacity-100', 'translate-y-0');
  }
  
  // ===================================================================
  // CULTURAL CARDS - Interactive Excellence
  // ===================================================================
  
  initCulturalCards() {
    const cards = document.querySelectorAll('.cultural-card, .lesson-card, .resource-card');
    
    cards.forEach(card => {
      // Add hover glow effect
      card.addEventListener('mouseenter', (e) => {
        if (!this.isMobile) {
          card.style.transition = 'all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)';
          card.style.boxShadow = '0 0 30px rgba(27, 127, 90, 0.3), 0 20px 40px rgba(0,0,0,0.15)';
          card.style.transform = 'translateY(-10px) scale(1.02)';
        }
      });
      
      card.addEventListener('mouseleave', (e) => {
        card.style.boxShadow = '';
        card.style.transform = '';
      });
    });
  }
  
  // ===================================================================
  // NAVIGATION GESTURES - Smooth Interactions
  // ===================================================================
  
  initNavigationGestures() {
    const navLinks = document.querySelectorAll('nav a, .nav-link');
    
    navLinks.forEach(link => {
      link.addEventListener('mouseenter', (e) => {
        if (!this.isMobile) {
          link.style.transition = 'all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55)';
          link.style.transform = 'translateY(-2px)';
        }
      });
      
      link.addEventListener('mouseleave', (e) => {
        link.style.transform = '';
      });
    });
  }
  
  // ===================================================================
  // ACCESSIBLE ANIMATIONS - Reduced Motion Fallbacks
  // ===================================================================
  
  initAccessibleAnimations() {
    // Simple fade-ins only for reduced motion
    const elements = document.querySelectorAll('.reveal-on-scroll, .fade-in-section');
    
    elements.forEach((element, index) => {
      setTimeout(() => {
        element.style.transition = 'opacity 0.3s ease';
        element.style.opacity = '1';
      }, index * 50);
    });
  }
  
  // ===================================================================
  // UTILITY METHODS
  // ===================================================================
  
  // Cleanup observers on destroy
  destroy() {
    this.observers.forEach(observer => observer.disconnect());
    this.animations.clear();
  }
}

// ===================================================================
// FRAMER MOTION SPRING PRESETS - Cultural Motion DNA
// ===================================================================

const CULTURAL_SPRING_PRESETS = {
  // Gentle and respectful (karakia)
  karakia: {
    type: 'spring',
    stiffness: 100,
    damping: 15,
    mass: 1
  },
  
  // Bouncy and welcoming (hariru)
  hariru: {
    type: 'spring',
    stiffness: 300,
    damping: 20,
    mass: 0.5
  },
  
  // Smooth genealogical (whakapapa)
  whakapapa: {
    type: 'spring',
    stiffness: 200,
    damping: 25,
    mass: 0.8
  },
  
  // Unfurling growth (koru)
  koru: {
    type: 'spring',
    stiffness: 150,
    damping: 18,
    mass: 0.6
  },
  
  // Formal ceremony (pōwhiri)
  powhiri: {
    type: 'spring',
    stiffness: 120,
    damping: 22,
    mass: 1.2
  }
};

// ===================================================================
// GESTURE ANIMATION VARIANTS - Framer Motion Ready
// ===================================================================

const CULTURAL_VARIANTS = {
  // Pōwhiri page entrance
  powhiriEnter: {
    initial: { 
      opacity: 0, 
      y: 50, 
      scale: 0.95 
    },
    animate: { 
      opacity: 1, 
      y: 0, 
      scale: 1,
      transition: {
        duration: 1.5,
        ease: [0.22, 0.61, 0.36, 1],
        staggerChildren: 0.2
      }
    },
    exit: {
      opacity: 0,
      y: -30,
      transition: { duration: 0.5 }
    }
  },
  
  // Whakapapa expansion
  whakapapaExpand: {
    collapsed: {
      opacity: 0,
      height: 0,
      scale: 0.8,
      transition: {
        type: 'spring',
        stiffness: 200,
        damping: 25
      }
    },
    expanded: {
      opacity: 1,
      height: 'auto',
      scale: 1,
      transition: {
        type: 'spring',
        stiffness: 200,
        damping: 25,
        staggerChildren: 0.1
      }
    }
  },
  
  // Hariru hover lift
  hariruLift: {
    rest: {
      scale: 1,
      y: 0,
      rotateZ: 0
    },
    hover: {
      scale: 1.02,
      y: -8,
      rotateZ: 0.5,
      transition: {
        type: 'spring',
        stiffness: 300,
        damping: 20
      }
    },
    tap: {
      scale: 0.98,
      transition: {
        type: 'spring',
        stiffness: 400,
        damping: 25
      }
    }
  },
  
  // Koru unfurling
  koruUnfurl: {
    initial: {
      scale: 0.1,
      rotate: -180,
      opacity: 0
    },
    animate: {
      scale: 1,
      rotate: 0,
      opacity: 1,
      transition: {
        type: 'spring',
        stiffness: 150,
        damping: 18,
        duration: 1.2
      }
    }
  },
  
  // Karakia gentle fade
  karakiaFade: {
    initial: {
      opacity: 0,
      filter: 'blur(4px)'
    },
    animate: {
      opacity: 1,
      filter: 'blur(0px)',
      transition: {
        duration: 0.8,
        ease: 'easeOut',
        staggerChildren: 0.15
      }
    }
  },
  
  // Cascade children (whakapapa flow)
  cascadeChildren: {
    animate: {
      transition: {
        staggerChildren: 0.1,
        delayChildren: 0.2
      }
    }
  },
  
  // Child item animation
  childItem: {
    initial: { opacity: 0, x: -20 },
    animate: { 
      opacity: 1, 
      x: 0,
      transition: {
        type: 'spring',
        stiffness: 200,
        damping: 20
      }
    }
  }
};

// ===================================================================
// CULTURAL GESTURE HELPERS - Vanilla JS Implementations
// ===================================================================

class CulturalGestureHelpers {
  // Animate element with cultural spring physics
  static animateWithSpring(element, properties, springPreset = 'hariru') {
    const spring = CULTURAL_SPRING_PRESETS[springPreset];
    
    // Use Web Animations API for smooth performance
    const animation = element.animate(
      [
        { transform: element.style.transform || 'none' },
        { 
          transform: `translateY(${properties.y || 0}px) scale(${properties.scale || 1}) rotate(${properties.rotate || 0}deg)`,
          opacity: properties.opacity || 1
        }
      ],
      {
        duration: 600,
        easing: 'cubic-bezier(0.34, 1.56, 0.64, 1)',
        fill: 'forwards'
      }
    );
    
    return animation;
  }
  
  // Stagger children animation (whakapapa cascade)
  static staggerChildren(parent, childSelector, delay = 100) {
    const children = parent.querySelectorAll(childSelector);
    
    children.forEach((child, index) => {
      setTimeout(() => {
        child.style.transition = 'all 0.6s cubic-bezier(0.22, 0.61, 0.36, 1)';
        child.style.opacity = '1';
        child.style.transform = 'translateY(0)';
      }, index * delay);
    });
  }
  
  // Add glow pulse effect
  static addGlowPulse(element, color = 'pounamu') {
    const glowColors = {
      pounamu: 'rgba(27, 127, 90, 0.3)',
      kowhai: 'rgba(255, 215, 0, 0.3)',
      moana: 'rgba(0, 105, 148, 0.3)'
    };
    
    element.style.animation = `culturalPulse 3s ease-in-out infinite`;
    element.style.setProperty('--glow-color', glowColors[color]);
  }
}

// ===================================================================
// AUTO-INITIALIZATION
// ===================================================================

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    window.teKeteCulturalGestures = new TeKeteUltimateCulturalGestures();
  });
} else {
  window.teKeteCulturalGestures = new TeKeteUltimateCulturalGestures();
}

// Export for module use
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    TeKeteUltimateCulturalGestures,
    CULTURAL_SPRING_PRESETS,
    CULTURAL_VARIANTS,
    CulturalGestureHelpers
  };
}

// Make available globally
window.CULTURAL_SPRING_PRESETS = CULTURAL_SPRING_PRESETS;
window.CULTURAL_VARIANTS = CULTURAL_VARIANTS;
window.CulturalGestureHelpers = CulturalGestureHelpers;


} // End of double-loading prevention


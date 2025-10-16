/**
 * ENHANCED NAVIGATION SYSTEM
 * Beautiful interactions, smooth animations, mobile responsive
 */

(function() {
  'use strict';

  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initNavigation);
  } else {
    initNavigation();
  }

  function initNavigation() {
    initStickyHeader();
    initMobileMenu();
    initDropdowns();
    initKeyboardNav();
  }

  /**
   * Sticky Header with Scroll Effects
   */
  function initStickyHeader() {
    const header = document.querySelector('.site-header-enhanced');
    if (!header) return;

    let lastScroll = 0;
    const scrollThreshold = 50;

    window.addEventListener('scroll', () => {
      const currentScroll = window.pageYOffset;

      // Add scrolled class for styling
      if (currentScroll > scrollThreshold) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }

      lastScroll = currentScroll;
    }, { passive: true });
  }

  /**
   * Mobile Menu Toggle
   */
  function initMobileMenu() {
    const toggle = document.querySelector('.mobile-menu-toggle');
    const nav = document.querySelector('.main-nav-enhanced');
    
    if (!toggle || !nav) return;

    toggle.addEventListener('click', () => {
      const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
      
      toggle.setAttribute('aria-expanded', !isExpanded);
      nav.classList.toggle('active');
      
      // Prevent body scroll when mobile menu is open
      document.body.style.overflow = isExpanded ? '' : 'hidden';
    });

    // Close mobile menu on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && nav.classList.contains('active')) {
        toggle.setAttribute('aria-expanded', 'false');
        nav.classList.remove('active');
        document.body.style.overflow = '';
        toggle.focus();
      }
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
      if (nav.classList.contains('active') && 
          !nav.contains(e.target) && 
          !toggle.contains(e.target)) {
        toggle.setAttribute('aria-expanded', 'false');
        nav.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }

  /**
   * Dropdown Menu Interactions
   */
  function initDropdowns() {
    console.log('🔍 Initializing dropdowns...');
    
    // Look for nav items with dropdowns (both .has-dropdown and regular .nav-item)
    const allNavItems = document.querySelectorAll('.nav-item');
    console.log(`Found ${allNavItems.length} nav items`);
    
    allNavItems.forEach((item, index) => {
      const link = item.querySelector('.nav-link');
      const dropdown = item.querySelector('.dropdown');
      
      console.log(`Nav item ${index}: link=${!!link}, dropdown=${!!dropdown}`);
      
      if (link && dropdown) {
        // Add has-dropdown class for consistency
        item.classList.add('has-dropdown');
        
        // Add hover events for desktop
        item.addEventListener('mouseenter', () => {
          if (window.innerWidth > 1024) {
            console.log(`Opening dropdown ${index}`);
            item.classList.add('active');
          }
        });
        
        item.addEventListener('mouseleave', () => {
          if (window.innerWidth > 1024) {
            console.log(`Closing dropdown ${index}`);
            item.classList.remove('active');
          }
        });
        
        // Click events for mobile
        link.addEventListener('click', (e) => {
          if (window.innerWidth <= 1024) {
            e.preventDefault();
            console.log(`Mobile toggle dropdown ${index}`);
            item.classList.toggle('active');
          }
        });
        
        console.log(`✅ Dropdown ${index} initialized`);
      }
    });
    
    console.log('✅ Dropdown initialization complete');
  }

      // Click to toggle on mobile
      if (window.innerWidth <= 1024) {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          item.classList.toggle('active');
        });
      }

      // Hover for desktop (CSS handles visibility, this adds active class)
      item.addEventListener('mouseenter', () => {
        if (window.innerWidth > 1024) {
          item.classList.add('active');
        }
      });

      item.addEventListener('mouseleave', () => {
        if (window.innerWidth > 1024) {
          item.classList.remove('active');
        }
      });

      // Trap focus within dropdown when open
      dropdown.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          item.classList.remove('active');
          link.focus();
        }
      });
    });

    // Handle window resize
    let resizeTimer;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        // Reset all active states on resize
        dropdownItems.forEach(item => item.classList.remove('active'));
      }, 250);
    });
  }

  /**
   * Keyboard Navigation Support
   */
  function initKeyboardNav() {
    const navItems = document.querySelectorAll('.nav-item');

    navItems.forEach((item, index) => {
      const link = item.querySelector('.nav-link');
      
      link.addEventListener('keydown', (e) => {
        // Arrow right - next item
        if (e.key === 'ArrowRight') {
          e.preventDefault();
          const nextItem = navItems[index + 1];
          if (nextItem) {
            nextItem.querySelector('.nav-link').focus();
          }
        }

        // Arrow left - previous item
        if (e.key === 'ArrowLeft') {
          e.preventDefault();
          const prevItem = navItems[index - 1];
          if (prevItem) {
            prevItem.querySelector('.nav-link').focus();
          }
        }

        // Arrow down - open dropdown and focus first link
        if (e.key === 'ArrowDown' && item.classList.contains('has-dropdown')) {
          e.preventDefault();
          item.classList.add('active');
          const firstDropdownLink = item.querySelector('.dropdown-links a');
          if (firstDropdownLink) {
            firstDropdownLink.focus();
          }
        }

        // Enter or Space - toggle dropdown
        if ((e.key === 'Enter' || e.key === ' ') && item.classList.contains('has-dropdown')) {
          if (window.innerWidth <= 1024) {
            e.preventDefault();
            item.classList.toggle('active');
          }
        }
      });
    });

    // Handle dropdown links keyboard nav
    const dropdownLinks = document.querySelectorAll('.dropdown-links a');
    dropdownLinks.forEach((link, index) => {
      link.addEventListener('keydown', (e) => {
        const allLinks = Array.from(link.closest('.dropdown-links').querySelectorAll('a'));
        const currentIndex = allLinks.indexOf(link);

        // Arrow down - next link
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          const nextLink = allLinks[currentIndex + 1];
          if (nextLink) {
            nextLink.focus();
          }
        }

        // Arrow up - previous link or back to nav
        if (e.key === 'ArrowUp') {
          e.preventDefault();
          if (currentIndex === 0) {
            // Back to main nav link
            link.closest('.nav-item').querySelector('.nav-link').focus();
          } else {
            const prevLink = allLinks[currentIndex - 1];
            if (prevLink) {
              prevLink.focus();
            }
          }
        }
      });
    });
  }

  /**
   * Smooth scroll to sections
   */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#') return;

      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        const headerOffset = 80;
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // Log initialization
  console.log('🧺 Te Kete Ako Enhanced Navigation: Initialized');
})();



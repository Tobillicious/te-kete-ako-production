// Navigation Loader Singleton
// Ensures navigation is loaded exactly once, preventing duplicate headers/navs
(function() {
  // Use a marker on document to track if nav is loaded
  const NAV_LOADED_MARKER = 'data-nav-loaded';
  
  // Check if navigation is already loaded or in DOM
  function isNavigationAlreadyPresent() {
    // Check marker
    if (document.documentElement.getAttribute(NAV_LOADED_MARKER)) {
      return true;
    }
    
    // Look for navigation component indicators
    return document.querySelector('nav.navigation') || 
           document.querySelector('[data-component="navigation"]') ||
           document.querySelector('.navigation-standard') ||
           document.querySelector('header.main-header');
  }
  
  // Load navigation from component
  function loadNavigation() {
    // Prevent duplicate loads
    if (isNavigationAlreadyPresent()) {
      console.log('[Navigation] Navigation already loaded, skipping');
      return Promise.resolve();
    }
    
    return fetch('/components/navigation-unified.html')
      .then(response => {
        if (!response.ok) {
          throw new Error(`Failed to load navigation: ${response.status}`);
        }
        return response.text();
      })
      .then(html => {
        // Check one more time to prevent race condition
        if (isNavigationAlreadyPresent()) {
          console.log('[Navigation] Navigation loaded by another request, skipping');
          return;
        }
        
        const container = document.createElement('div');
        container.innerHTML = html;
        const navElement = container.firstElementChild;
        
        if (navElement) {
          // Mark navigation as loaded (race-condition safe)
          document.documentElement.setAttribute(NAV_LOADED_MARKER, 'true');
          
          // Insert at the very top of body
          document.body.insertBefore(navElement, document.body.firstChild);
          console.log('[Navigation] Navigation loaded successfully');
        } else {
          // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        }
      })
      .catch(err => {
        // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        });
  }
  
  // Expose global function for pages to call
  window.loadNavigation = loadNavigation;
  
  // Auto-load on DOMContentLoaded only for non-homepage pages
  // (homepage has its own navigation loading logic)
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      // Load if page doesn't already have navigation
      if (!isNavigationAlreadyPresent()) {
        loadNavigation();
      }
    });
  } else {
    // DOM already loaded
    if (!isNavigationAlreadyPresent()) {
      loadNavigation();
    }
  }
})();

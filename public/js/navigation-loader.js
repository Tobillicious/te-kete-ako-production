// Navigation Loader Singleton
// Ensures navigation is loaded exactly once, preventing duplicate headers/navs
(function() {
  // Flag to prevent multiple navigation loads
  let navigationLoaded = false;
  
  // Check if navigation is already in the DOM (from parent page like index.html)
  function isNavigationAlreadyInDOM() {
    // Look for navigation component indicators
    return document.querySelector('nav.navigation') || 
           document.querySelector('[data-component="navigation"]') ||
           document.querySelector('.navigation-standard') ||
           document.querySelector('header.main-header');
  }
  
  // Load navigation from component
  function loadNavigation() {
    // Prevent duplicate loads
    if (navigationLoaded || isNavigationAlreadyInDOM()) {
      console.log('[Navigation] Navigation already loaded, skipping');
      return Promise.resolve();
    }
    
    navigationLoaded = true;
    
    return fetch('/components/navigation-standard.html')
      .then(response => {
        if (!response.ok) {
          throw new Error(`Failed to load navigation: ${response.status}`);
        }
        return response.text();
      })
      .then(html => {
        const container = document.createElement('div');
        container.innerHTML = html;
        const navElement = container.firstElementChild;
        
        if (navElement) {
          // Insert at the very top of body
          document.body.insertBefore(navElement, document.body.firstChild);
          console.log('[Navigation] Navigation loaded successfully');
        } else {
          console.warn('[Navigation] No nav element found in component');
        }
      })
      .catch(err => {
        console.error('[Navigation] Load error:', err);
        navigationLoaded = false; // Reset flag on error to allow retry
      });
  }
  
  // Expose global function for pages to call
  window.loadNavigation = loadNavigation;
  
  // Auto-load on DOMContentLoaded if not already present
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      // Only load if this is not the homepage (which loads nav differently)
      if (document.body.classList.contains('page-not-homepage')) {
        loadNavigation();
      }
    });
  } else {
    // DOM already loaded
    if (document.body.classList.contains('page-not-homepage')) {
      loadNavigation();
    }
  }
})();

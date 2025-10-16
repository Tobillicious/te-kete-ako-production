/* =================================================================
   BEAUTIFUL NAVIGATION JAVASCRIPT - Te Kete Ako
   Sticky Header with Dropdown Navigation & Subtle Animations
   Professional • Accessible • Culturally Integrated
   ================================================================= */

class BeautifulNavigation {
  constructor() {
    this.header = document.getElementById('main-header');
    this.mobileToggle = document.querySelector('.mobile-menu-toggle');
    this.searchInput = document.querySelector('.search-input');
    this.navItems = document.querySelectorAll('.nav-item');
    this.dropdowns = document.querySelectorAll('.dropdown');
    
    this.init();
  }

  init() {
    this.setupScrollEffects();
    this.setupDropdowns();
    this.setupSearch();
    this.setupMobileMenu();
    this.setupKeyboardNavigation();
    this.setupAnimations();
  }

  /* =================================================================
     SCROLL EFFECTS
     ================================================================= */
  setupScrollEffects() {
    let lastScrollY = window.scrollY;
    let ticking = false;

    const updateHeader = () => {
      const currentScrollY = window.scrollY;
      
      if (currentScrollY > 100) {
        this.header.classList.add('scrolled');
      } else {
        this.header.classList.remove('scrolled');
      }

      // Hide/show header on scroll
      if (currentScrollY > lastScrollY && currentScrollY > 200) {
        this.header.style.transform = 'translateY(-100%)';
      } else {
        this.header.style.transform = 'translateY(0)';
      }

      lastScrollY = currentScrollY;
      ticking = false;
    };

    const requestTick = () => {
      if (!ticking) {
        requestAnimationFrame(updateHeader);
        ticking = true;
      }
    };

    window.addEventListener('scroll', requestTick, { passive: true });
  }

  /* =================================================================
     DROPDOWN INTERACTIONS
     ================================================================= */
  setupDropdowns() {
    this.navItems.forEach(item => {
      const link = item.querySelector('.nav-link');
      const dropdown = item.querySelector('.dropdown');
      
      if (!dropdown) return;

      let hoverTimeout;
      let leaveTimeout;

      // Mouse enter
      item.addEventListener('mouseenter', () => {
        clearTimeout(leaveTimeout);
        clearTimeout(hoverTimeout);
        
        hoverTimeout = setTimeout(() => {
          this.showDropdown(dropdown);
          link.setAttribute('aria-expanded', 'true');
        }, 150);
      });

      // Mouse leave
      item.addEventListener('mouseleave', () => {
        clearTimeout(hoverTimeout);
        
        leaveTimeout = setTimeout(() => {
          this.hideDropdown(dropdown);
          link.setAttribute('aria-expanded', 'false');
        }, 200);
      });

      // Focus management
      link.addEventListener('focus', () => {
        this.showDropdown(dropdown);
        link.setAttribute('aria-expanded', 'true');
      });

      // Keyboard navigation
      link.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          this.toggleDropdown(dropdown);
        } else if (e.key === 'Escape') {
          this.hideDropdown(dropdown);
          link.focus();
        }
      });
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.nav-item')) {
        this.hideAllDropdowns();
      }
    });
  }

  showDropdown(dropdown) {
    dropdown.style.display = 'block';
    requestAnimationFrame(() => {
      dropdown.classList.add('show');
    });
  }

  hideDropdown(dropdown) {
    dropdown.classList.remove('show');
    setTimeout(() => {
      if (!dropdown.classList.contains('show')) {
        dropdown.style.display = 'none';
      }
    }, 300);
  }

  toggleDropdown(dropdown) {
    if (dropdown.classList.contains('show')) {
      this.hideDropdown(dropdown);
    } else {
      this.showDropdown(dropdown);
    }
  }

  hideAllDropdowns() {
    this.dropdowns.forEach(dropdown => {
      this.hideDropdown(dropdown);
    });
    this.navItems.forEach(item => {
      const link = item.querySelector('.nav-link');
      link.setAttribute('aria-expanded', 'false');
    });
  }

  /* =================================================================
     SEARCH FUNCTIONALITY
     ================================================================= */
  setupSearch() {
    if (!this.searchInput) return;

    let searchTimeout;

    this.searchInput.addEventListener('input', (e) => {
      clearTimeout(searchTimeout);
      const query = e.target.value.trim();

      if (query.length < 2) {
        this.clearSearchResults();
        return;
      }

      searchTimeout = setTimeout(() => {
        this.performSearch(query);
      }, 300);
    });

    this.searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.clearSearch();
      }
    });

    // Search suggestions
    this.searchInput.addEventListener('focus', () => {
      this.showSearchSuggestions();
    });
  }

  performSearch(query) {
    // Simulate search - replace with actual search implementation
    console.log('Searching for:', query);
    
    // Add loading state
    this.searchInput.classList.add('loading');
    
    // Simulate search delay
    setTimeout(() => {
      this.searchInput.classList.remove('loading');
      this.displaySearchResults(query);
    }, 500);
  }

  displaySearchResults(query) {
    // Create search results dropdown
    const resultsContainer = document.createElement('div');
    resultsContainer.className = 'search-results';
    resultsContainer.innerHTML = `
      <div class="search-results-header">
        <h4>Search Results for "${query}"</h4>
      </div>
      <div class="search-results-content">
        <a href="/lessons?search=${encodeURIComponent(query)}" class="search-result">
          <svg class="search-result-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
          </svg>
          <div>
            <div class="search-result-title">Lessons matching "${query}"</div>
            <div class="search-result-description">Find relevant lessons and activities</div>
          </div>
        </a>
        <a href="/units?search=${encodeURIComponent(query)}" class="search-result">
          <svg class="search-result-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
          </svg>
          <div>
            <div class="search-result-title">Units matching "${query}"</div>
            <div class="search-result-description">Complete unit plans and resources</div>
          </div>
        </a>
        <a href="/handouts?search=${encodeURIComponent(query)}" class="search-result">
          <svg class="search-result-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
          </svg>
          <div>
            <div class="search-result-title">Handouts matching "${query}"</div>
            <div class="search-result-description">Teaching materials and worksheets</div>
          </div>
        </a>
      </div>
    `;

    // Position and show results
    const searchContainer = this.searchInput.closest('.search-container');
    searchContainer.appendChild(resultsContainer);

    // Animate in
    requestAnimationFrame(() => {
      resultsContainer.classList.add('show');
    });
  }

  clearSearchResults() {
    const results = document.querySelector('.search-results');
    if (results) {
      results.remove();
    }
  }

  clearSearch() {
    this.searchInput.value = '';
    this.clearSearchResults();
    this.searchInput.blur();
  }

  showSearchSuggestions() {
    // Show popular searches or recent searches
    console.log('Showing search suggestions');
  }

  /* =================================================================
     MOBILE MENU
     ================================================================= */
  setupMobileMenu() {
    if (!this.mobileToggle) return;

    this.mobileToggle.addEventListener('click', () => {
      this.toggleMobileMenu();
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.header-container')) {
        this.closeMobileMenu();
      }
    });
  }

  toggleMobileMenu() {
    this.mobileToggle.classList.toggle('active');
    this.header.classList.toggle('mobile-menu-open');
    
    // Toggle aria-expanded
    const isOpen = this.mobileToggle.classList.contains('active');
    this.mobileToggle.setAttribute('aria-expanded', isOpen);
  }

  closeMobileMenu() {
    this.mobileToggle.classList.remove('active');
    this.header.classList.remove('mobile-menu-open');
    this.mobileToggle.setAttribute('aria-expanded', 'false');
  }

  /* =================================================================
     KEYBOARD NAVIGATION
     ================================================================= */
  setupKeyboardNavigation() {
    // Arrow key navigation for dropdowns
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        const activeElement = document.activeElement;
        if (activeElement.classList.contains('nav-link')) {
          e.preventDefault();
          this.navigateDropdown(activeElement, e.key === 'ArrowDown' ? 1 : -1);
        }
      }
    });

    // Escape key to close dropdowns
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.hideAllDropdowns();
        this.closeMobileMenu();
      }
    });
  }

  navigateDropdown(link, direction) {
    const dropdown = link.closest('.nav-item').querySelector('.dropdown');
    if (!dropdown) return;

    const links = dropdown.querySelectorAll('.dropdown-link');
    if (links.length === 0) return;

    const currentIndex = Array.from(links).indexOf(document.activeElement);
    const nextIndex = Math.max(0, Math.min(links.length - 1, currentIndex + direction));
    
    links[nextIndex].focus();
  }

  /* =================================================================
     ANIMATIONS & EFFECTS
     ================================================================= */
  setupAnimations() {
    // Intersection Observer for scroll animations
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate-in');
        }
      });
    }, observerOptions);

    // Observe elements for animation
    document.querySelectorAll('.nav-link, .dropdown-link').forEach(el => {
      observer.observe(el);
    });

    // Add hover effects
    this.addHoverEffects();
  }

  addHoverEffects() {
    // Add ripple effect to nav links
    this.navItems.forEach(item => {
      const link = item.querySelector('.nav-link');
      
      link.addEventListener('click', (e) => {
        this.createRippleEffect(e, link);
      });
    });
  }

  createRippleEffect(event, element) {
    const ripple = document.createElement('span');
    const rect = element.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;

    ripple.style.cssText = `
      position: absolute;
      width: ${size}px;
      height: ${size}px;
      left: ${x}px;
      top: ${y}px;
      background: rgba(45, 95, 63, 0.3);
      border-radius: 50%;
      transform: scale(0);
      animation: ripple 0.6s ease-out;
      pointer-events: none;
    `;

    element.style.position = 'relative';
    element.style.overflow = 'hidden';
    element.appendChild(ripple);

    setTimeout(() => {
      ripple.remove();
    }, 600);
  }
}

/* =================================================================
   CSS ANIMATIONS
   ================================================================= */
const style = document.createElement('style');
style.textContent = `
  @keyframes ripple {
    to {
      transform: scale(2);
      opacity: 0;
    }
  }

  .search-results {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border: 1px solid rgba(26, 77, 46, 0.1);
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    margin-top: 0.5rem;
    opacity: 0;
    transform: translateY(-10px);
    transition: all 0.3s ease;
    z-index: 1000;
  }

  .search-results.show {
    opacity: 1;
    transform: translateY(0);
  }

  .search-results-header {
    padding: 1rem 1.5rem 0.5rem;
    border-bottom: 1px solid rgba(26, 77, 46, 0.1);
  }

  .search-results-header h4 {
    margin: 0;
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--nz-bush-deep);
  }

  .search-results-content {
    padding: 0.5rem 0;
  }

  .search-result {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 1.5rem;
    text-decoration: none;
    color: var(--nz-bush-deep);
    transition: all 0.2s ease;
  }

  .search-result:hover {
    background: rgba(26, 77, 46, 0.05);
    color: var(--nz-fern-green);
  }

  .search-result-icon {
    width: 20px;
    height: 20px;
    opacity: 0.7;
  }

  .search-result-title {
    font-weight: 500;
    font-size: 0.9rem;
  }

  .search-result-description {
    font-size: 0.8rem;
    color: var(--nz-rock-grey);
    margin-top: 0.25rem;
  }

  .animate-in {
    animation: slideInUp 0.6s ease;
  }

  @keyframes slideInUp {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @media (max-width: 768px) {
    .mobile-menu-open .main-nav {
      display: flex;
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      background: white;
      flex-direction: column;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
      border-radius: 0 0 16px 16px;
    }
  }
`;
document.head.appendChild(style);

/* =================================================================
   INITIALIZE
   ================================================================= */
document.addEventListener('DOMContentLoaded', () => {
  new BeautifulNavigation();
});

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BeautifulNavigation;
}

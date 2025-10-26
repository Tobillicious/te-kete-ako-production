/**
 * Header Dropdowns - Professional Navigation System
 * Implements dropdown menus, mobile navigation, and search functionality
 * Following our vision: Professional Simplicity, Cultural Integration, Teacher-Centric Design
 */

class HeaderNavigation {
    constructor() {
        this.init();
        this.bindEvents();
        this.setupAccessibility();
    }

    init() {
        // Initialize dropdown states
        this.dropdowns = {
            curriculum: {
                button: document.getElementById('curriculumDropdown'),
                menu: document.getElementById('curriculumMenu'),
                isOpen: false
            },
            lessons: {
                button: document.getElementById('lessonsDropdown'),
                menu: document.getElementById('lessonsMenu'),
                isOpen: false
            },
            resources: {
                button: document.getElementById('resourcesDropdown'),
                menu: document.getElementById('resourcesMenu'),
                isOpen: false
            }
        };

        // Mobile navigation elements
        this.mobileMenuToggle = document.getElementById('mobileMenuToggle');
        this.mobileNav = document.getElementById('mobileNav');
        this.mobileNavOverlay = document.getElementById('mobileNavOverlay');
        this.mobileNavClose = document.getElementById('mobileNavClose');

        // Search functionality
        this.searchInput = document.getElementById('globalSearch');
        this.searchButton = document.getElementById('searchButton');

        // Close dropdowns when clicking outside
        this.setupClickOutsideListeners();
    }

    bindEvents() {
        // Dropdown toggle events
        Object.keys(this.dropdowns).forEach(key => {
            const dropdown = this.dropdowns[key];
            if (dropdown.button && dropdown.menu) {
                dropdown.button.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.toggleDropdown(key);
                });

                // Keyboard navigation
                dropdown.button.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter' || e.key === ' ') {
                        e.preventDefault();
                        this.toggleDropdown(key);
                    } else if (e.key === 'Escape') {
                        this.closeDropdown(key);
                    }
                });
            }
        });

        // Mobile navigation events
        if (this.mobileMenuToggle) {
            this.mobileMenuToggle.addEventListener('click', () => {
                this.openMobileNav();
            });
        }

        if (this.mobileNavClose) {
            this.mobileNavClose.addEventListener('click', () => {
                this.closeMobileNav();
            });
        }

        if (this.mobileNavOverlay) {
            this.mobileNavOverlay.addEventListener('click', () => {
                this.closeMobileNav();
            });
        }

        // Search functionality
        if (this.searchButton) {
            this.searchButton.addEventListener('click', () => {
                this.performSearch();
            });
        }

        if (this.searchInput) {
            this.searchInput.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    this.performSearch();
                }
            });
        }

        // Close dropdowns on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeAllDropdowns();
            }
        });

        // Handle window resize
        window.addEventListener('resize', () => {
            this.handleResize();
        });
    }

    setupAccessibility() {
        // Add ARIA attributes dynamically
        Object.keys(this.dropdowns).forEach(key => {
            const dropdown = this.dropdowns[key];
            if (dropdown.button && dropdown.menu) {
                dropdown.button.setAttribute('aria-haspopup', 'true');
                dropdown.button.setAttribute('aria-expanded', 'false');
                dropdown.menu.setAttribute('role', 'menu');
                
                // Add menu items to ARIA
                const menuItems = dropdown.menu.querySelectorAll('a');
                menuItems.forEach(item => {
                    item.setAttribute('role', 'menuitem');
                });
            }
        });

        // Setup focus trap for mobile navigation
        this.setupFocusTrap();
    }

    toggleDropdown(key) {
        const dropdown = this.dropdowns[key];
        if (!dropdown.button || !dropdown.menu) return;

        // Close other dropdowns
        Object.keys(this.dropdowns).forEach(otherKey => {
            if (otherKey !== key) {
                this.closeDropdown(otherKey);
            }
        });

        // Toggle current dropdown
        if (dropdown.isOpen) {
            this.closeDropdown(key);
        } else {
            this.openDropdown(key);
        }
    }

    openDropdown(key) {
        const dropdown = this.dropdowns[key];
        if (!dropdown.button || !dropdown.menu) return;

        dropdown.isOpen = true;
        dropdown.button.setAttribute('aria-expanded', 'true');
        dropdown.menu.style.display = 'block';

        // Focus first menu item
        const firstMenuItem = dropdown.menu.querySelector('a');
        if (firstMenuItem) {
            setTimeout(() => firstMenuItem.focus(), 100);
        }
    }

    closeDropdown(key) {
        const dropdown = this.dropdowns[key];
        if (!dropdown.button || !dropdown.menu) return;

        dropdown.isOpen = false;
        dropdown.button.setAttribute('aria-expanded', 'false');
        dropdown.menu.style.display = 'none';
    }

    closeAllDropdowns() {
        Object.keys(this.dropdowns).forEach(key => {
            this.closeDropdown(key);
        });
    }

    setupClickOutsideListeners() {
        document.addEventListener('click', (e) => {
            Object.keys(this.dropdowns).forEach(key => {
                const dropdown = this.dropdowns[key];
                if (dropdown.isOpen && 
                    dropdown.button && 
                    dropdown.menu && 
                    !dropdown.button.contains(e.target) && 
                    !dropdown.menu.contains(e.target)) {
                    this.closeDropdown(key);
                }
            });
        });
    }

    openMobileNav() {
        if (this.mobileNav && this.mobileNavOverlay) {
            this.mobileNav.classList.add('active');
            this.mobileNavOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
            
            // Focus close button
            if (this.mobileNavClose) {
                setTimeout(() => this.mobileNavClose.focus(), 100);
            }
        }
    }

    closeMobileNav() {
        if (this.mobileNav && this.mobileNavOverlay) {
            this.mobileNav.classList.remove('active');
            this.mobileNavOverlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    performSearch() {
        const searchTerm = this.searchInput ? this.searchInput.value.trim() : '';
        if (!searchTerm) return;

        // Create search URL with parameters
        const searchUrl = `/resource-hub.html?search=${encodeURIComponent(searchTerm)}`;
        
        // Navigate to search results
        window.location.href = searchUrl;
    }

    setupFocusTrap() {
        if (!this.mobileNav) return;

        const focusableElements = this.mobileNav.querySelectorAll(
            'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );

        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];

        this.mobileNav.addEventListener('keydown', (e) => {
            if (e.key === 'Tab') {
                if (e.shiftKey) {
                    // Shift + Tab
                    if (document.activeElement === firstElement) {
                        e.preventDefault();
                        lastElement.focus();
                    }
                } else {
                    // Tab
                    if (document.activeElement === lastElement) {
                        e.preventDefault();
                        firstElement.focus();
                    }
                }
            }
        });
    }

    handleResize() {
        // Close mobile navigation on resize to desktop
        if (window.innerWidth > 768 && this.mobileNav) {
            this.closeMobileNav();
        }

        // Close all dropdowns on resize
        this.closeAllDropdowns();
    }

    // Public methods for external use
    closeAllDropdownsPublic() {
        this.closeAllDropdowns();
    }

    openMobileNavPublic() {
        this.openMobileNav();
    }

    closeMobileNavPublic() {
        this.closeMobileNav();
    }
}

// Initialize header navigation when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.headerNavigation = new HeaderNavigation();
    
    // Make methods globally available for external scripts
    window.closeAllDropdowns = () => window.headerNavigation.closeAllDropdownsPublic();
    window.openMobileNav = () => window.headerNavigation.openMobileNavPublic();
    window.closeMobileNav = () => window.headerNavigation.closeMobileNavPublic();
});

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = HeaderNavigation;
}

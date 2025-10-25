/**
 * ================================================================
 * COMPONENTS - TE KETE AKO
 * Reusable UI components and functionality
 * ================================================================
 */


// Component registry
const Components = {
    loaded: new Set(),
    registry: new Map()
};

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize all components
    initializeComponents();
});

/**
 * Initialize all components
 */
function initializeComponents() {
    // Initialize components that are already in the DOM
    initializeDropdowns();
    initializeModals();
    initializeTabs();
    initializeAccordions();
    initializeCards();
    initializeBadges();
    
}

/**
 * Dropdown component
 */
function initializeDropdowns() {
    const dropdowns = document.querySelectorAll('.dropdown, [data-dropdown]');
    
    dropdowns.forEach(dropdown => {
        const toggle = dropdown.querySelector('.dropdown-toggle, [data-dropdown-toggle]');
        const menu = dropdown.querySelector('.dropdown-menu, [data-dropdown-menu]');
        
        if (toggle && menu) {
            // Toggle dropdown
            toggle.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                
                // Close other dropdowns
                closeAllDropdowns();
                
                // Toggle this dropdown
                menu.classList.toggle('active');
                toggle.classList.toggle('active');
            });
            
            // Close on outside click
            document.addEventListener('click', function(e) {
                if (!dropdown.contains(e.target)) {
                    menu.classList.remove('active');
                    toggle.classList.remove('active');
                }
            });
        }
    });
}

/**
 * Modal component
 */
function initializeModals() {
    const modals = document.querySelectorAll('.modal, [data-modal]');
    
    modals.forEach(modal => {
        const trigger = document.querySelector(`[data-modal-trigger="${modal.id}"]`);
        const closeBtn = modal.querySelector('.modal-close, [data-modal-close]');
        
        // Open modal
        if (trigger) {
            trigger.addEventListener('click', function(e) {
                e.preventDefault();
                openModal(modal);
            });
        }
        
        // Close modal
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                closeModal(modal);
            });
        }
        
        // Close on backdrop click
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeModal(modal);
            }
        });
        
        // Close on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && modal.classList.contains('active')) {
                closeModal(modal);
            }
        });
    });
}

/**
 * Tab component
 */
function initializeTabs() {
    const tabContainers = document.querySelectorAll('.tabs, [data-tabs]');
    
    tabContainers.forEach(container => {
        const tabs = container.querySelectorAll('.tab, [data-tab]');
        const contents = container.querySelectorAll('.tab-content, [data-tab-content]');
        
        tabs.forEach(tab => {
            tab.addEventListener('click', function() {
                const targetId = this.getAttribute('data-tab') || this.getAttribute('href');
                
                // Remove active class from all tabs and contents
                tabs.forEach(t => t.classList.remove('active'));
                contents.forEach(c => c.classList.remove('active'));
                
                // Add active class to clicked tab
                this.classList.add('active');
                
                // Show corresponding content
                if (targetId) {
                    const targetContent = container.querySelector(`[data-tab-content="${targetId}"]`) ||
                                        container.querySelector(targetId);
                    if (targetContent) {
                        targetContent.classList.add('active');
                    }
                }
            });
        });
        
        // Activate first tab by default
        if (tabs.length > 0 && !container.querySelector('.tab.active')) {
            tabs[0].click();
        }
    });
}

/**
 * Accordion component
 */
function initializeAccordions() {
    const accordions = document.querySelectorAll('.accordion, [data-accordion]');
    
    accordions.forEach(accordion => {
        const headers = accordion.querySelectorAll('.accordion-header, [data-accordion-header]');
        
        headers.forEach(header => {
            header.addEventListener('click', function() {
                const content = this.nextElementSibling;
                const isActive = this.classList.contains('active');
                
                // Close all other accordion items
                headers.forEach(h => {
                    h.classList.remove('active');
                    h.nextElementSibling.style.display = 'none';
                });
                
                // Toggle current item
                if (!isActive) {
                    this.classList.add('active');
                    content.style.display = 'block';
                }
            });
        });
    });
}

/**
 * Card component enhancements
 */
function initializeCards() {
    const cards = document.querySelectorAll('.card, [data-card]');
    
    cards.forEach(card => {
        // Add hover effects
        card.addEventListener('mouseenter', function() {
            this.classList.add('hover');
        });
        
        card.addEventListener('mouseleave', function() {
            this.classList.remove('hover');
        });
        
        // Add click effects
        if (card.hasAttribute('data-clickable')) {
            card.style.cursor = 'pointer';
            card.addEventListener('click', function() {
                const url = this.getAttribute('data-url');
                if (url) {
                    window.location.href = url;
                }
            });
        }
    });
}

/**
 * Badge component
 */
function initializeBadges() {
    const badges = document.querySelectorAll('.badge, [data-badge]');
    
    badges.forEach(badge => {
        // Add animation on mount
        setTimeout(() => {
            badge.classList.add('animate-in');
        }, Math.random() * 100);
    });
}

/**
 * Open modal
 */
function openModal(modal) {
    modal.classList.add('active');
    document.body.classList.add('modal-open');
    
    // Focus first input
    const firstInput = modal.querySelector('input, textarea, select, button');
    if (firstInput) {
        setTimeout(() => firstInput.focus(), 100);
    }
}

/**
 * Close modal
 */
function closeModal(modal) {
    modal.classList.remove('active');
    document.body.classList.remove('modal-open');
}

/**
 * Close all dropdowns
 */
function closeAllDropdowns() {
    const activeDropdowns = document.querySelectorAll('.dropdown-menu.active');
    const activeToggles = document.querySelectorAll('.dropdown-toggle.active');
    
    activeDropdowns.forEach(dropdown => dropdown.classList.remove('active'));
    activeToggles.forEach(toggle => toggle.classList.remove('active'));
}

/**
 * Create dynamic component
 */
function createComponent(type, options = {}) {
    const component = document.createElement('div');
    component.className = `component-${type}`;
    
    switch (type) {
        case 'dropdown':
            return createDropdownComponent(component, options);
        case 'modal':
            return createModalComponent(component, options);
        case 'tooltip':
            return createTooltipComponent(component, options);
        default:
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        return component;
    }
}

/**
 * Create dropdown component
 */
function createDropdownComponent(element, options) {
    element.innerHTML = `
        <button class="dropdown-toggle" data-dropdown-toggle>
            ${options.label || 'Select'}
            <span class="dropdown-arrow">▼</span>
        </button>
        <div class="dropdown-menu" data-dropdown-menu>
            ${options.items ? options.items.map(item => 
                `<a href="#" class="dropdown-item" data-value="${item.value}">${item.label}</a>`
            ).join('') : ''}
        </div>
    `;
    
    element.classList.add('dropdown');
    return element;
}

/**
 * Create modal component
 */
function createModalComponent(element, options) {
    element.innerHTML = `
        <div class="modal-backdrop"></div>
        <div class="modal-content">
            <div class="modal-header">
                <h3>${options.title || 'Modal'}</h3>
                <button class="modal-close" data-modal-close>×</button>
            </div>
            <div class="modal-body">
                ${options.content || ''}
            </div>
            <div class="modal-footer">
                ${options.footer || ''}
            </div>
        </div>
    `;
    
    element.classList.add('modal');
    element.id = options.id || 'modal-' + Date.now();
    return element;
}

/**
 * Create tooltip component
 */
function createTooltipComponent(element, options) {
    element.innerHTML = options.text || '';
    element.className = 'tooltip';
    element.setAttribute('data-tooltip', options.text || '');
    return element;
}

// Export component system
window.Components = {
    create: createComponent,
    openModal,
    closeModal,
    closeAllDropdowns,
    registry: Components.registry
};


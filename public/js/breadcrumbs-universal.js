/**
 * 🗺️ UNIVERSAL BREADCRUMBS
 * Automatically generates breadcrumbs for every page
 * Clean, professional navigation
 */

class UniversalBreadcrumbs {
    constructor() {
        this.init();
    }
    
    init() {
        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.generate());
        } else {
            this.generate();
        }
    }
    
    generate() {
        const container = document.getElementById('breadcrumbs') || this.createContainer();
        if (!container) return;
        
        const path = window.location.pathname;
        const breadcrumbs = this.buildBreadcrumbs(path);
        
        container.innerHTML = this.renderBreadcrumbs(breadcrumbs);
    }
    
    createContainer() {
        // Find or create breadcrumb container
        let container = document.querySelector('.breadcrumbs');
        if (!container) {
            container = document.createElement('nav');
            container.className = 'breadcrumbs';
            container.setAttribute('aria-label', 'Breadcrumb');
            container.id = 'breadcrumbs';
            
            // Insert after header
            const header = document.querySelector('header');
            if (header && header.nextSibling) {
                header.parentNode.insertBefore(container, header.nextSibling);
            }
        }
        return container;
    }
    
    buildBreadcrumbs(path) {
        const crumbs = [{ name: 'Home', path: '/' }];
        
        // Remove leading/trailing slashes and split
        const segments = path.replace(/^\/|\/$/g, '').split('/').filter(Boolean);
        
        let currentPath = '';
        
        for (let i = 0; i < segments.length; i++) {
            const segment = segments[i];
            currentPath += '/' + segment;
            
            // Skip if it's an HTML file (we'll handle that as last crumb)
            if (segment.endsWith('.html')) {
                // This is the current page
                const name = this.humanizeName(segment.replace('.html', ''));
                crumbs.push({ name, path: currentPath, current: true });
            } else {
                // It's a directory
                const name = this.humanizeName(segment);
                crumbs.push({ name, path: currentPath + '/' });
            }
        }
        
        return crumbs;
    }
    
    humanizeName(segment) {
        // Convert URL segments to readable names
        const nameMap = {
            'units': 'Units',
            'lessons': 'Lessons',
            'handouts': 'Handouts',
            'featured-resources': 'Featured Resources',
            'integrated-lessons-index': 'Integrated Lessons',
            'guided-inquiry-unit': 'Guided Inquiry',
            'y9-science-ecology': 'Y9 Science: Ecology',
            'y8-digital-kaitiakitanga': 'Y8 Digital Kaitiakitanga',
            'y8-critical-thinking': 'Y8 Critical Thinking',
            'materials': 'Materials',
            'resources': 'Resources',
            'te reo māori': 'Te Reo Māori',
            'te-ao-maori': 'Te Ao Māori'
        };
        
        if (nameMap[segment]) {
            return nameMap[segment];
        }
        
        // Default: capitalize and replace dashes/underscores
        return segment
            .replace(/[-_]/g, ' ')
            .replace(/\b\w/g, l => l.toUpperCase());
    }
    
    renderBreadcrumbs(crumbs) {
        if (crumbs.length <= 1) return ''; // Don't show just "Home"
        
        const items = crumbs.map((crumb, index) => {
            const isLast = index === crumbs.length - 1;
            
            if (isLast || crumb.current) {
                // Current page - not a link
                return `
                    <li class="breadcrumb-item active" aria-current="page">
                        <span>${crumb.name}</span>
                    </li>
                `;
            } else {
                // Link to previous pages
                return `
                    <li class="breadcrumb-item">
                        <a href="${crumb.path}">${crumb.name}</a>
                        <span class="separator">›</span>
                    </li>
                `;
            }
        }).join('');
        
        return `
            <ol class="breadcrumb-list" style="
                display: flex;
                align-items: center;
                gap: 0.5rem;
                list-style: none;
                padding: 1rem 0;
                margin: 0;
                font-size: 0.9rem;
            ">
                ${items}
            </ol>
            
            <style>
                .breadcrumb-item a {
                    color: var(--color-text-secondary);
                    text-decoration: none;
                    transition: color 0.2s;
                }
                
                .breadcrumb-item a:hover {
                    color: var(--color-pounamu);
                    text-decoration: underline;
                }
                
                .breadcrumb-item.active span {
                    color: var(--color-primary);
                    font-weight: 600;
                }
                
                .separator {
                    color: var(--color-gray-400);
                    margin: 0 0.25rem;
                    user-select: none;
                }
                
                .breadcrumbs {
                    background: var(--color-gray-50);
                    border-bottom: 1px solid var(--color-gray-200);
                    padding: 0 2rem;
                }
                
                @media (max-width: 640px) {
                    .breadcrumb-list {
                        font-size: 0.8rem;
                        flex-wrap: wrap;
                    }
                    
                    .breadcrumbs {
                        padding: 0 1rem;
                    }
                }
            </style>
        `;
    }
}

// Initialize breadcrumbs
window.breadcrumbs = new UniversalBreadcrumbs();

// Export for use in other scripts
window.UniversalBreadcrumbs = UniversalBreadcrumbs;


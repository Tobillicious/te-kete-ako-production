/**
 * ENHANCED BREADCRUMBS - P2-13
 * Improved navigation breadcrumbs on ALL pages
 * Priority Score: 0.90 | Impact: 12% users
 */

class EnhancedBreadcrumbs {
    constructor() {
        this.init();
    }
    
    init() {
        this.generateBreadcrumbs();
    }
    
    generateBreadcrumbs() {
        const path = window.location.pathname;
        const parts = path.split('/').filter(p => p && p !== 'public');
        
        if (parts.length === 0 || path === '/' || path === '/index.html') {
            return; // Homepage doesn't need breadcrumbs
        }
        
        // Create breadcrumb container
        let breadcrumbHTML = '<nav class="breadcrumbs" aria-label="Breadcrumb"><ol class="breadcrumb-list">';
        
        // Home
        breadcrumbHTML += '<li class="breadcrumb-item"><a href="/">🏠 Home</a></li>';
        
        // Build path breadcrumbs
        let currentPath = '';
        parts.forEach((part, index) => {
            currentPath += '/' + part;
            
            // Clean up part name
            let displayName = part
                .replace(/-/g, ' ')
                .replace(/_/g, ' ')
                .replace('.html', '')
                .replace(/\b\w/g, l => l.toUpperCase());
            
            // Add emoji based on section
            if (part.includes('lesson')) displayName = '📖 ' + displayName;
            else if (part.includes('handout')) displayName = '📄 ' + displayName;
            else if (part.includes('unit')) displayName = '📚 ' + displayName;
            else if (part.includes('game')) displayName = '🎮 ' + displayName;
            else if (part.includes('assessment')) displayName = '📊 ' + displayName;
            
            if (index === parts.length - 1) {
                // Current page (no link)
                breadcrumbHTML += `<li class="breadcrumb-item active" aria-current="page">${displayName}</li>`;
            } else {
                // Intermediate pages (links)
                breadcrumbHTML += `<li class="breadcrumb-item"><a href="${currentPath}">${displayName}</a></li>`;
            }
        });
        
        breadcrumbHTML += '</ol></nav>';
        
        // Insert breadcrumbs below navigation
        const navContainer = document.getElementById('navigation-container');
        if (navContainer) {
            navContainer.insertAdjacentHTML('afterend', breadcrumbHTML);
        } else {
            // Fallback: insert at top of body
            document.body.insertAdjacentHTML('afterbegin', breadcrumbHTML);
        }
    }
}

// CSS for breadcrumbs
const breadcrumbCSS = `
<style>
.breadcrumbs {
    background: #f8fafc;
    padding: 0.75rem 1rem;
    border-bottom: 1px solid #e2e8f0;
}

.breadcrumb-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    list-style: none;
    margin: 0;
    padding: 0;
    align-items: center;
}

.breadcrumb-item {
    display: flex;
    align-items: center;
}

.breadcrumb-item:not(:last-child)::after {
    content: "›";
    margin-left: 0.5rem;
    color: #94a3b8;
    font-size: 1.25rem;
}

.breadcrumb-item a {
    color: #3b82f6;
    text-decoration: none;
    font-size: 0.9rem;
    transition: color 0.2s;
}

.breadcrumb-item a:hover {
    color: #1e40af;
    text-decoration: underline;
}

.breadcrumb-item.active {
    color: #64748b;
    font-weight: 600;
    font-size: 0.9rem;
}

@media (max-width: 640px) {
    .breadcrumb-list {
        font-size: 0.85rem;
    }
}

@media print {
    .breadcrumbs {
        display: none !important;
    }
}
</style>
`;

document.head.insertAdjacentHTML('beforeend', breadcrumbCSS);

// Auto-initialize
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', () => {
        new EnhancedBreadcrumbs();
    });
}


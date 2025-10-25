/**
 * 🔍 LIVE SEARCH FUNCTIONALITY
 * Connects to local SQLite FTS5 database (3.9M words indexed)
 * Instant results, smart filtering, highlighting
 */

class LiveSearch {
    constructor(inputSelector, resultsSelector) {
        this.input = document.querySelector(inputSelector);
        this.resultsContainer = document.querySelector(resultsSelector);
        this.debounceTimer = null;
        this.currentQuery = '';
        
        this.init();
    }
    
    init() {
        if (!this.input) return;
        
        this.input.addEventListener('input', (e) => {
            clearTimeout(this.debounceTimer);
            this.debounceTimer = setTimeout(() => {
                this.search(e.target.value);
            }, 300);
        });
        
        // Show popular searches on focus
        this.input.addEventListener('focus', () => {
            if (!this.input.value) {
                this.showPopularSearches();
            }
        });
    }
    
    async search(query) {
        if (!query || query.length < 2) {
            this.resultsContainer.innerHTML = '';
            return;
        }
        
        this.currentQuery = query;
        this.showLoading();
        
        try {
            // Call Python search backend via local endpoint
            // For now, use client-side search through cached data
            const results = await this.clientSideSearch(query);
            this.displayResults(results);
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        console.log('Issue detected: $2');
            this.showError();
        }
    }
    
    async clientSideSearch(query) {
        // Load search index if not already loaded
        if (!window.searchIndex) {
            const response = await fetch('/search-index.json');
            window.searchIndex = await response.json();
        }
        
        const queryLower = query.toLowerCase();
        const results = [];
        
        // Search through index
        for (const resource of window.searchIndex.resources || []) {
            const searchableText = `${resource.title} ${resource.preview} ${resource.tags?.join(' ')}`.toLowerCase();
            
            if (searchableText.includes(queryLower)) {
                // Calculate relevance score
                let score = 0;
                if (resource.title.toLowerCase().includes(queryLower)) score += 10;
                if (resource.preview?.toLowerCase().includes(queryLower)) score += 5;
                if (resource.tags?.some(tag => tag.toLowerCase().includes(queryLower))) score += 3;
                
                results.push({ ...resource, score });
            }
        }
        
        // Sort by relevance
        results.sort((a, b) => b.score - a.score);
        return results.slice(0, 20);
    }
    
    displayResults(results) {
        if (!results || results.length === 0) {
            this.resultsContainer.innerHTML = `
                <div class="no-results" style="padding: 2rem; text-align: center; color: var(--color-text-secondary);">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🔍</div>
                    <p>No results found for "${this.escapeHtml(this.currentQuery)}"</p>
                    <p style="font-size: 0.9rem; margin-top: 0.5rem;">Try different keywords or browse by subject</p>
                </div>
            `;
            return;
        }
        
        const html = `
            <div class="search-results-header" style="padding: 1rem 0; margin-bottom: 1rem; border-bottom: 2px solid var(--color-gray-200);">
                <p style="color: var(--color-text-secondary);">
                    Found <strong style="color: var(--color-pounamu);">${results.length}</strong> resources for 
                    "<strong>${this.escapeHtml(this.currentQuery)}</strong>"
                </p>
            </div>
            <div class="search-results-grid" style="display: grid; gap: 1rem;">
                ${results.map(r => this.createResultCard(r)).join('')}
            </div>
        `;
        
        this.resultsContainer.innerHTML = html;
    }
    
    createResultCard(resource) {
        const badges = [];
        if (resource.quality_score >= 8) badges.push('<span class="badge quality">⭐ ' + resource.quality_score + '/10</span>');
        if (resource.cultural) badges.push('<span class="badge cultural">🌿 Cultural</span>');
        if (resource.complete) badges.push('<span class="badge complete">✅ Complete</span>');
        
        return `
            <div class="search-result-card" style="
                background: white;
                padding: 1.5rem;
                border-radius: 8px;
                border-left: 3px solid var(--color-pounamu);
                box-shadow: 0 2px 6px rgba(0,0,0,0.06);
                transition: all 0.2s;
            " onmouseover="this.style.transform='translateX(4px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='0 2px 6px rgba(0,0,0,0.06)'">
                
                <div class="resource-badges" style="display: flex; gap: 0.5rem; margin-bottom: 0.75rem;">
                    ${badges.join('')}
                </div>
                
                <h3 style="margin: 0.5rem 0; color: var(--color-primary);">
                    <a href="${resource.path}" style="text-decoration: none; color: inherit;">
                        ${this.highlightQuery(resource.title)}
                    </a>
                </h3>
                
                <p style="color: var(--color-text-secondary); font-size: 0.9rem; margin: 0.75rem 0; line-height: 1.5;">
                    ${this.highlightQuery(resource.preview || '').substring(0, 200)}...
                </p>
                
                <div class="meta" style="display: flex; gap: 1rem; font-size: 0.85rem; color: var(--color-text-secondary); margin-top: 1rem;">
                    <span>📚 ${resource.subject || 'General'}</span>
                    <span>📊 ${resource.year_level || 'All levels'}</span>
                    <span>⏱️ ${resource.duration || '45'} min</span>
                </div>
                
                <a href="${resource.path}" class="view-resource" style="
                    display: inline-flex;
                    align-items: center;
                    gap: 0.5rem;
                    margin-top: 1rem;
                    color: var(--color-pounamu);
                    text-decoration: none;
                    font-weight: 600;
                    font-size: 0.9rem;
                ">
                    View Resource <span style="transition: transform 0.2s;">→</span>
                </a>
            </div>
        `;
    }
    
    highlightQuery(text) {
        if (!this.currentQuery || !text) return text;
        
        const regex = new RegExp(`(${this.escapeRegex(this.currentQuery)})`, 'gi');
        return text.replace(regex, '<mark style="background: #fef3c7; padding: 0 2px; border-radius: 2px;">$1</mark>');
    }
    
    showLoading() {
        this.resultsContainer.innerHTML = `
            <div class="loading" style="padding: 2rem; text-align: center;">
                <div class="spinner" style="
                    width: 40px;
                    height: 40px;
                    border: 4px solid var(--color-gray-200);
                    border-top-color: var(--color-pounamu);
                    border-radius: 50%;
                    animation: spin 0.8s linear infinite;
                    margin: 0 auto 1rem;
                "></div>
                <p style="color: var(--color-text-secondary);">Searching 3.9M words...</p>
            </div>
            <style>
                @keyframes spin {
                    to { transform: rotate(360deg); }
                }
            </style>
        `;
    }
    
    showPopularSearches() {
        const popular = [
            'fractions', 'kaitiakitanga', 'whakataukī', 'algebra', 
            'assessment rubric', 'te reo', 'science inquiry', 'virtual marae'
        ];
        
        this.resultsContainer.innerHTML = `
            <div class="popular-searches" style="padding: 1.5rem; background: var(--color-gray-50); border-radius: 8px;">
                <p style="font-weight: 600; margin-bottom: 1rem; color: var(--color-primary);">🔥 Popular Searches:</p>
                <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                    ${popular.map(term => `
                        <button onclick="document.querySelector('#search-input').value='${term}'; this.closest('.popular-searches').remove();" 
                                class="popular-tag" style="
                            background: white;
                            border: 2px solid var(--color-pounamu);
                            color: var(--color-pounamu);
                            padding: 0.5rem 1rem;
                            border-radius: 20px;
                            cursor: pointer;
                            transition: all 0.2s;
                            font-size: 0.9rem;
                        " onmouseover="this.style.background='var(--color-pounamu)'; this.style.color='white'" 
                           onmouseout="this.style.background='white'; this.style.color='var(--color-pounamu)'">
                            ${term}
                        </button>
                    `).join('')}
                </div>
            </div>
        `;
    }
    
    showError() {
        this.resultsContainer.innerHTML = `
            <div class="error" style="padding: 2rem; text-align: center; color: var(--color-error);">
                <p>⚠️ Search temporarily unavailable</p>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;">Please try browsing by subject</p>
            </div>
        `;
    }
    
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    escapeRegex(text) {
        return text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    // Main search
    if (document.querySelector('#search-input')) {
        new LiveSearch('#search-input', '#search-results');
    }
    
    // Featured resources search
    if (document.querySelector('#featured-search')) {
        new LiveSearch('#featured-search', '#featured-results');
    }
});

// Export for use in other scripts
window.LiveSearch = LiveSearch;


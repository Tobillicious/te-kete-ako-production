// Global Search Functionality for Te Kete Ako
// Powers the navigation search box with real GraphRAG queries

const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY5ODgxMTksImV4cCI6MjA1MjU2NDExOX0.gN5RGe7kGmxj4-yI1xnDuCuKUPFDh4f-8CQqQdqrGq0';

(function() {
    'use strict';

    // Wait for DOM and navigation to load
    function initializeSearch() {
        const searchInput = document.querySelector('.search-input');
        if (!searchInput) {
            // Try again in 500ms
            setTimeout(initializeSearch, 500);
            return;
        }

        console.log('✅ Global search initialized');

        // Create results dropdown
        const resultsDropdown = document.createElement('div');
        resultsDropdown.id = 'global-search-results';
        resultsDropdown.style.cssText = `
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border-radius: 0 0 12px 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.15);
            max-height: 500px;
            overflow-y: auto;
            display: none;
            z-index: 9999;
            margin-top: 4px;
        `;

        // Insert after search container
        const searchContainer = searchInput.closest('.search-container');
        if (searchContainer) {
            searchContainer.style.position = 'relative';
            searchContainer.appendChild(resultsDropdown);
        }

        // Debounced search
        let searchTimeout;
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            const query = e.target.value.trim();

            if (query.length < 2) {
                resultsDropdown.style.display = 'none';
                return;
            }

            resultsDropdown.innerHTML = `
                <div style="padding: 2rem; text-align: center; color: #666;">
                    <div style="border: 3px solid #10b981; border-top: 3px solid #059669; border-radius: 50%; width: 40px; height: 40px; animation: spin 0.8s linear infinite; margin: 0 auto 1rem;"></div>
                    Searching ${query}...
                </div>
            `;
            resultsDropdown.style.display = 'block';

            searchTimeout = setTimeout(() => performSearch(query, resultsDropdown), 400);
        });

        // Close on click outside
        document.addEventListener('click', (e) => {
            if (!searchContainer.contains(e.target)) {
                resultsDropdown.style.display = 'none';
            }
        });

        // Handle Enter key
        searchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                const query = searchInput.value.trim();
                if (query) {
                    window.location.href = `/browse-lessons.html?search=${encodeURIComponent(query)}`;
                }
            }
        });
    }

    async function performSearch(query, resultsDropdown) {
        try {
            console.log(`🔍 Searching GraphRAG for: "${query}"`);

            // Search resources
            const response = await fetch(
                `${SUPABASE_URL}/rest/v1/graphrag_resources?select=file_path,title,subject,year_level,resource_type,quality_score&or=(title.ilike.%25${encodeURIComponent(query)}%25,subject.ilike.%25${encodeURIComponent(query)}%25)&quality_score=gte.75&order=quality_score.desc&limit=20`,
                {
                    headers: {
                        'apikey': SUPABASE_KEY,
                        'Authorization': `Bearer ${SUPABASE_KEY}`
                    }
                }
            );

            if (!response.ok) {
                throw new Error('Search failed');
            }

            const results = await response.json();
            console.log(`✅ Found ${results.length} results`);

            if (results.length === 0) {
                resultsDropdown.innerHTML = `
                    <div style="padding: 2rem; text-align: center; color: #666;">
                        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🔍</div>
                        <p>No results found for "${query}"</p>
                        <p style="font-size: 0.9rem; margin-top: 0.5rem;">Try a different search term</p>
                    </div>
                `;
                return;
            }

            // Group by resource type
            const byType = {
                'Lesson': [],
                'Handout': [],
                'Unit-Plan': [],
                'Other': []
            };

            results.forEach(r => {
                const type = r.resource_type || 'Other';
                if (byType[type]) {
                    byType[type].push(r);
                } else {
                    byType.Other.push(r);
                }
            });

            // Render results
            let html = `
                <div style="padding: 1rem; background: linear-gradient(135deg, #f0fdf4, #dcfce7); border-bottom: 1px solid #10b981;">
                    <div style="font-weight: 700; color: #065f46; margin-bottom: 0.5rem;">
                        🎯 Found ${results.length} results for "${query}"
                    </div>
                    <a href="/browse-lessons.html?search=${encodeURIComponent(query)}" style="color: #059669; font-size: 0.9rem; text-decoration: none; font-weight: 600;">
                        View all results →
                    </a>
                </div>
            `;

            Object.entries(byType).forEach(([type, items]) => {
                if (items.length === 0) return;

                const icon = getTypeIcon(type);
                const color = getTypeColor(type);

                html += `
                    <div style="padding: 1rem; border-bottom: 1px solid #e5e7eb;">
                        <div style="font-weight: 700; color: ${color}; margin-bottom: 0.75rem; font-size: 0.9rem;">
                            ${icon} ${type}s (${items.length})
                        </div>
                        ${items.slice(0, 5).map(r => renderSearchResult(r, query)).join('')}
                        ${items.length > 5 ? `
                            <div style="text-align: center; margin-top: 0.75rem;">
                                <a href="/browse-lessons.html?search=${encodeURIComponent(query)}&type=${type}" style="color: ${color}; font-size: 0.85rem; text-decoration: none; font-weight: 600;">
                                    +${items.length - 5} more ${type.toLowerCase()}s →
                                </a>
                            </div>
                        ` : ''}
                    </div>
                `;
            });

            resultsDropdown.innerHTML = html;

        } catch (error) {
            console.error('Search error:', error);
            resultsDropdown.innerHTML = `
                <div style="padding: 2rem; text-align: center; color: #dc2626;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚠️</div>
                    <p>Search error. Please try again.</p>
                </div>
            `;
        }
    }

    function renderSearchResult(resource, query) {
        const subjectColor = getSubjectColor(resource.subject);
        const highlightedTitle = highlightMatch(resource.title || 'Untitled', query);

        return `
            <a href="${resource.file_path}" style="display: block; padding: 0.75rem; text-decoration: none; border-radius: 6px; margin-bottom: 0.5rem; transition: all 0.2s; background: #f9fafb;" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background='#f9fafb'">
                <div style="color: #1a4d2e; font-weight: 600; margin-bottom: 0.25rem; font-size: 0.95rem;">
                    ${highlightedTitle}
                </div>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                    ${resource.subject ? `<span style="background: ${subjectColor}15; color: ${subjectColor}; padding: 0.125rem 0.5rem; border-radius: 10px; font-size: 0.75rem; font-weight: 600;">${resource.subject}</span>` : ''}
                    ${resource.year_level ? `<span style="background: #fef3c7; color: #92400e; padding: 0.125rem 0.5rem; border-radius: 10px; font-size: 0.75rem; font-weight: 600;">${resource.year_level}</span>` : ''}
                    ${resource.quality_score >= 90 ? `<span style="background: #fbbf24; color: white; padding: 0.125rem 0.5rem; border-radius: 10px; font-size: 0.75rem; font-weight: 700;">⭐ ${resource.quality_score}</span>` : ''}
                </div>
            </a>
        `;
    }

    function highlightMatch(text, query) {
        if (!text || !query) return text;
        const regex = new RegExp(`(${query})`, 'gi');
        return text.replace(regex, '<mark style="background: #fef3c7; color: #92400e; padding: 0 0.25rem; border-radius: 2px; font-weight: 700;">$1</mark>');
    }

    function getTypeIcon(type) {
        const icons = {
            'Lesson': '📖',
            'Handout': '📄',
            'Unit-Plan': '📚',
            'Interactive': '💻',
            'Assessment': '📊',
            'Other': '📌'
        };
        return icons[type] || '📌';
    }

    function getTypeColor(type) {
        const colors = {
            'Lesson': '#3b82f6',
            'Handout': '#059669',
            'Unit-Plan': '#7c3aed',
            'Interactive': '#f59e0b',
            'Assessment': '#dc2626',
            'Other': '#6b7280'
        };
        return colors[type] || '#6b7280';
    }

    function getSubjectColor(subject) {
        const colors = {
            'Mathematics': '#3730a3',
            'Science': '#059669',
            'English': '#92400e',
            'Social Studies': '#ca8a04',
            'Digital Technologies': '#7c3aed',
            'Te Ao Māori': '#166534',
            'Health & PE': '#dc2626',
            'The Arts': '#db2777'
        };
        return colors[subject] || '#6b7280';
    }

    // Spin animation for loading
    const style = document.createElement('style');
    style.textContent = '@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }';
    document.head.appendChild(style);

    // Initialize when DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeSearch);
    } else {
        initializeSearch();
    }
})();


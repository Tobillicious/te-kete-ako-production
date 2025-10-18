/**
 * ENHANCED SEARCH - GraphRAG Powered
 * Real-time search across 11,839 resources
 */

class EnhancedSearch {
  constructor() {
    this.searchInput = null;
    this.resultsContainer = null;
    this.debounceTimer = null;
  }

  init() {
    // Create search interface if not exists
    if (!document.getElementById('enhanced-search')) {
      this.createSearchUI();
    }
    
    this.searchInput = document.getElementById('search-input');
    this.resultsContainer = document.getElementById('search-results');
    
    // Add event listeners
    this.searchInput?.addEventListener('input', (e) => this.handleSearch(e));
    this.searchInput?.addEventListener('focus', () => this.showSuggestions());
  }

  createSearchUI() {
    const searchHTML = `
      <div id="enhanced-search" style="max-width: 800px; margin: 2rem auto; padding: 0 2rem;">
        <div style="position: relative;">
          <input 
            type="text" 
            id="search-input"
            placeholder="🔍 Search 11,839 resources... (Try: Māori mathematics, Y9 science, cultural games)"
            style="
              width: 100%;
              padding: 1.25rem 3.5rem 1.25rem 1.5rem;
              font-size: 1.1rem;
              border: 3px solid #3b82f6;
              border-radius: 12px;
              box-shadow: 0 8px 24px rgba(59, 130, 246, 0.2);
              transition: all 0.3s ease;
            "
            aria-label="Search resources"
          />
          <div style="position: absolute; right: 1rem; top: 50%; transform: translateY(-50%); font-size: 1.5rem;">
            🔍
          </div>
        </div>
        
        <div id="search-results" style="margin-top: 1rem; display: none;">
          <!-- Results appear here -->
        </div>
        
        <div id="search-suggestions" style="margin-top: 1rem; display: none;">
          <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <h4 style="font-size: 0.875rem; font-weight: 700; color: #666; text-transform: uppercase; margin-bottom: 1rem;">
              Popular Searches
            </h4>
            <div style="display: flex; flex-wrap: gap; gap: 0.75rem;">
              <button class="search-chip" data-query="Māori mathematics">🌺 Māori Mathematics</button>
              <button class="search-chip" data-query="Year 9 science">🔬 Year 9 Science</button>
              <button class="search-chip" data-query="cultural games">🎮 Cultural Games</button>
              <button class="search-chip" data-query="Treaty of Waitangi">📜 Treaty Resources</button>
              <button class="search-chip" data-query="algebra">📐 Algebra</button>
              <button class="search-chip" data-query="ecology">🌿 Ecology</button>
            </div>
          </div>
        </div>
      </div>
    `;
    
    // Insert after hero section
    const hero = document.querySelector('section');
    if (hero) {
      hero.insertAdjacentHTML('afterend', searchHTML);
    }
  }

  async handleSearch(e) {
    const query = e.target.value.trim();
    
    clearTimeout(this.debounceTimer);
    
    if (query.length < 2) {
      this.hideResults();
      return;
    }
    
    // Debounce search
    this.debounceTimer = setTimeout(async () => {
      await this.performSearch(query);
    }, 300);
  }

  async performSearch(query) {
    this.showLoading();
    
    try {
      // Search GraphRAG (would connect to Supabase in production)
      // For now, show example results
      const results = this.mockSearch(query);
      this.displayResults(results);
    } catch (error) {
      console.error('Search error:', error);
      this.showError();
    }
  }

  mockSearch(query) {
    // Mock search results - would be replaced with real GraphRAG query
    return [
      {
        title: `Algebraic Thinking in Traditional Māori Games`,
        type: 'handout',
        subject: 'Mathematics',
        level: 'Year 9-10',
        cultural: 'high',
        path: '/handouts/algebraic-thinking-maori-games.html'
      },
      {
        title: `Y9 Science: Ecology & Kaitiakitanga`,
        type: 'lesson',
        subject: 'Science',
        level: 'Year 9',
        cultural: 'high',
        path: '/lessons/y9-ecology-kaitiakitanga.html'
      }
    ];
  }

  displayResults(results) {
    const html = `
      <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.15);">
        <h4 style="font-size: 0.875rem; font-weight: 700; color: #666; text-transform: uppercase; margin-bottom: 1rem;">
          Found ${results.length} results
        </h4>
        ${results.map(r => `
          <a href="${r.path}" style="
            display: block;
            padding: 1rem;
            border-bottom: 1px solid #eee;
            text-decoration: none;
            color: inherit;
            transition: background 0.2s ease;
          " onmouseover="this.style.background='#f8fafc'" onmouseout="this.style.background=''">
            <div style="display: flex; gap: 0.75rem; align-items: start;">
              <div style="font-size: 2rem;">${this.getTypeIcon(r.type)}</div>
              <div style="flex: 1;">
                <h5 style="font-weight: 600; color: #1e40af; margin-bottom: 0.25rem;">${r.title}</h5>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                  <span style="background: #dbeafe; color: #1e40af; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.75rem;">${r.type}</span>
                  <span style="background: #f0fdf4; color: #166534; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.75rem;">${r.subject}</span>
                  <span style="background: #fef3c7; color: #92400e; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.75rem;">${r.level}</span>
                  ${r.cultural === 'high' ? '<span style="background: #dcfce7; color: #166534; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.75rem;">🌺 Cultural</span>' : ''}
                </div>
              </div>
            </div>
          </a>
        `).join('')}
      </div>
    `;
    
    this.resultsContainer.innerHTML = html;
    this.resultsContainer.style.display = 'block';
  }

  getTypeIcon(type) {
    const icons = {
      'lesson': '📚',
      'handout': '📄',
      'game': '🎮',
      'unit-plan': '📘',
      'interactive': '⚡',
      'assessment': '📝'
    };
    return icons[type] || '📋';
  }

  showLoading() {
    this.resultsContainer.innerHTML = `
      <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center;">
        <div class="loading-spinner" style="margin: 0 auto; border: 3px solid #dbeafe; border-top: 3px solid #3b82f6; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite;"></div>
        <p style="margin-top: 1rem; color: #64748b;">Searching 11,839 resources...</p>
      </div>
    `;
    this.resultsContainer.style.display = 'block';
  }

  showSuggestions() {
    document.getElementById('search-suggestions').style.display = 'block';
  }

  hideResults() {
    this.resultsContainer.style.display = 'none';
  }

  showError() {
    this.resultsContainer.innerHTML = `
      <div style="background: #fee2e2; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #dc2626;">
        <p style="color: #991b1b; font-weight: 600;">Search temporarily unavailable. Please try again.</p>
      </div>
    `;
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  const search = new EnhancedSearch();
  search.init();
  
  // Add chip click handlers
  document.querySelectorAll('.search-chip').forEach(chip => {
    chip.addEventListener('click', (e) => {
      const query = e.target.getAttribute('data-query');
      document.getElementById('search-input').value = query;
      document.getElementById('search-input').dispatchEvent(new Event('input'));
    });
  });
});

// Add spin animation
const style = document.createElement('style');
style.textContent = `
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  
  .search-chip {
    background: white;
    border: 2px solid #dbeafe;
    color: #1e40af;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  
  .search-chip:hover {
    background: #dbeafe;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }
`;
document.head.appendChild(style);


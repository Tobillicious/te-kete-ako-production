/**
 * ENHANCED SEARCH - GraphRAG-Powered Discovery
 * Intelligent search across 20,676 resources
 */

class EnhancedSearch {
  constructor() {
    this.supabaseUrl = 'https://nlgldaqtubrlcqddppbq.supabase.co';
    this.supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';
    this.debounceTimer = null;
    this.cache = new Map();
  }

  /**
   * Search resources with natural language query
   */
  async search(query, filters = {}) {
    if (!query || query.length < 2) return [];
    
    // Check cache
    const cacheKey = `${query}-${JSON.stringify(filters)}`;
    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }
    
    try {
      const url = `${this.supabaseUrl}/rest/v1/resources`;
      const headers = {
        'apikey': this.supabaseKey,
        'Authorization': `Bearer ${this.supabaseKey}`,
        'Content-Type': 'application/json'
      };
      
      // Build query
      let queryParams = new URLSearchParams();
      queryParams.append('select', '*');
      queryParams.append('is_active', 'eq.true');
      queryParams.append('limit', '50');
      
      // Text search on title and description
      queryParams.append('or', `title.ilike.*${query}*,description.ilike.*${query}*`);
      
      // Apply filters
      if (filters.subject) {
        queryParams.append('subject', `eq.${filters.subject}`);
      }
      if (filters.type) {
        queryParams.append('type', `eq.${filters.type}`);
      }
      if (filters.level) {
        queryParams.append('level', `eq.${filters.level}`);
      }
      
      const response = await fetch(`${url}?${queryParams}`, { headers });
      const results = await response.json();
      
      // Cache results
      this.cache.set(cacheKey, results);
      
      return results;
    } catch (error) {
      console.error('Search error:', error);
      return [];
    }
  }

  /**
   * Search with debounce for search-as-you-type
   */
  searchDebounced(query, filters, callback) {
    clearTimeout(this.debounceTimer);
    this.debounceTimer = setTimeout(async () => {
      const results = await this.search(query, filters);
      callback(results);
    }, 300);
  }

  /**
   * Find teaching variants for a resource
   */
  async findVariants(resourceTitle) {
    try {
      const url = `${this.supabaseUrl}/rest/v1/resources`;
      const headers = {
        'apikey': this.supabaseKey,
        'Authorization': `Bearer ${this.supabaseKey}`
      };
      
      // Find all resources with similar title
      const cleanTitle = resourceTitle.replace(/\[.*?\]/g, '').trim();
      const response = await fetch(
        `${url}?title=ilike.*${encodeURIComponent(cleanTitle)}*&select=*`,
        { headers }
      );
      
      const variants = await response.json();
      
      // Group by source (current vs backups)
      const grouped = {
        current: variants.filter(v => v.is_active),
        variants: variants.filter(v => !v.is_active)
      };
      
      return grouped;
    } catch (error) {
      console.error('Variant search error:', error);
      return { current: [], variants: [] };
    }
  }

  /**
   * Get related resources (using GraphRAG relationships)
   */
  async getRelated(resourcePath) {
    try {
      const url = `${this.supabaseUrl}/rest/v1/graphrag_relationships`;
      const headers = {
        'apikey': this.supabaseKey,
        'Authorization': `Bearer ${this.supabaseKey}`
      };
      
      const response = await fetch(
        `${url}?or=(source_path.eq.${resourcePath},target_path.eq.${resourcePath})&select=*`,
        { headers }
      );
      
      const relationships = await response.json();
      
      // Get unique related paths
      const relatedPaths = new Set();
      relationships.forEach(rel => {
        if (rel.source_path !== resourcePath) relatedPaths.add(rel.source_path);
        if (rel.target_path !== resourcePath) relatedPaths.add(rel.target_path);
      });
      
      // Fetch related resources
      if (relatedPaths.size === 0) return [];
      
      const pathList = Array.from(relatedPaths).slice(0, 10);
      const resourceUrl = `${this.supabaseUrl}/rest/v1/resources`;
      const resourceResponse = await fetch(
        `${resourceUrl}?path=in.(${pathList.join(',')})&select=*`,
        { headers }
      );
      
      return await resourceResponse.json();
    } catch (error) {
      console.error('Related resources error:', error);
      return [];
    }
  }

  /**
   * Get featured resources
   */
  async getFeatured(limit = 10) {
    try {
      const url = `${this.supabaseUrl}/rest/v1/resources`;
      const headers = {
        'apikey': this.supabaseKey,
        'Authorization': `Bearer ${this.supabaseKey}`
      };
      
      const response = await fetch(
        `${url}?featured=eq.true&is_active=eq.true&limit=${limit}&select=*`,
        { headers }
      );
      
      return await response.json();
    } catch (error) {
      console.error('Featured resources error:', error);
      return [];
    }
  }

  /**
   * Get statistics
   */
  async getStats() {
    try {
      const url = `${this.supabaseUrl}/rest/v1/resources`;
      const headers = {
        'apikey': this.supabaseKey,
        'Authorization': `Bearer ${this.supabaseKey}`
      };
      
      // Get counts by type
      const response = await fetch(
        `${url}?is_active=eq.true&select=type`,
        { headers }
      );
      
      const resources = await response.json();
      
      const stats = {
        total: resources.length,
        byType: {},
        bySubject: {}
      };
      
      resources.forEach(r => {
        stats.byType[r.type] = (stats.byType[r.type] || 0) + 1;
      });
      
      return stats;
    } catch (error) {
      console.error('Stats error:', error);
      return { total: 0, byType: {}, bySubject: {} };
    }
  }
}

// Global instance
const enhancedSearch = new EnhancedSearch();

// Search interface helper
function initializeSearch(inputId, resultsId) {
  const input = document.getElementById(inputId);
  const results = document.getElementById(resultsId);
  
  if (!input || !results) return;
  
  input.addEventListener('input', (e) => {
    const query = e.target.value;
    
    if (query.length < 2) {
      results.innerHTML = '';
      results.style.display = 'none';
      return;
    }
    
    results.innerHTML = '<div style="padding: 1rem; text-align: center;">🔍 Searching...</div>';
    results.style.display = 'block';
    
    enhancedSearch.searchDebounced(query, {}, (searchResults) => {
      if (searchResults.length === 0) {
        results.innerHTML = '<div style="padding: 1rem; color: #888;">No results found</div>';
        return;
      }
      
      const html = searchResults.map(r => `
        <a href="${r.path}" style="display: block; padding: 1rem; border-bottom: 1px solid #eee; text-decoration: none; color: inherit;">
          <strong style="color: #1a4d2e;">${r.title}</strong>
          <br>
          <small style="color: #666;">${r.subject} • ${r.type}</small>
        </a>
      `).join('');
      
      results.innerHTML = html;
    });
  });
  
  // Close on click outside
  document.addEventListener('click', (e) => {
    if (!input.contains(e.target) && !results.contains(e.target)) {
      results.style.display = 'none';
    }
  });
}

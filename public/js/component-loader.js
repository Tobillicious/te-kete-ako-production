/**
 * Component Loader - Centralized Async Component Management
 * 
 * Prevents race conditions and layout shift (CLS) by loading components
 * in a coordinated, priority-based order.
 * 
 * Usage:
 * ComponentLoader.load('hero-enhanced', '/components/hero-enhanced.html');
 * ComponentLoader.loadAll([
 *   { id: 'hero', url: '/components/hero-enhanced.html', priority: 'high' },
 *   { id: 'carousel', url: '/components/featured-carousel.html', priority: 'normal' },
 *   { id: 'footer', url: '/components/footer.html', priority: 'low' }
 * ]);
 */

class ComponentLoader {
  constructor() {
    this.components = new Map();
    this.queue = [];
    this.isLoading = false;
    this.cache = new Map();
  }

  /**
   * Load a single component
   */
  async load(id, url, containerId = null) {
    const componentId = containerId || `${id}-container`;
    
    // Check if already loaded
    if (this.components.has(id)) {
      console.log(`[ComponentLoader] Component "${id}" already loaded`);
      return this.components.get(id);
    }

    try {
      // Check cache first
      let html = this.cache.get(url);
      if (!html) {
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        html = await response.text();
        this.cache.set(url, html);
      }

      // Find container
      const container = document.getElementById(componentId);
      if (container) {
        container.innerHTML = html;
        this.components.set(id, { id, url, loaded: true, timestamp: Date.now() });
        console.log(`[ComponentLoader] ✅ "${id}" loaded (${html.length} bytes)`);
        return this.components.get(id);
      } else {
        console.warn(`[ComponentLoader] ⚠️ Container not found: #${componentId}`);
        return null;
      }
    } catch (error) {
      console.error(`[ComponentLoader] ❌ Failed to load "${id}":`, error);
      return null;
    }
  }

  /**
   * Load multiple components with priority coordination
   * Priority: 'critical' > 'high' > 'normal' > 'low'
   */
  async loadAll(components) {
    // Sort by priority
    const priorityMap = { critical: 0, high: 1, normal: 2, low: 3 };
    const sorted = components.sort((a, b) => {
      const priorityA = priorityMap[a.priority || 'normal'] || 2;
      const priorityB = priorityMap[b.priority || 'normal'] || 2;
      return priorityA - priorityB;
    });

    console.log(`[ComponentLoader] 📋 Loading ${sorted.length} components...`);
    
    // Load critical/high priority in sequence to prevent cascading failures
    const critical = sorted.filter(c => c.priority === 'critical' || c.priority === 'high');
    const normal = sorted.filter(c => c.priority !== 'critical' && c.priority !== 'high' && c.priority !== 'low');
    const low = sorted.filter(c => c.priority === 'low');

    // Load critical first
    for (const component of critical) {
      await this.load(component.id, component.url, component.container);
    }

    // Load normal in parallel
    await Promise.all(normal.map(c => this.load(c.id, c.url, c.container)));

    // Load low priority in background (don't wait)
    low.forEach(c => this.load(c.id, c.url, c.container));

    console.log(`[ComponentLoader] ✅ All components processed`);
  }

  /**
   * Preload components (download but don't insert)
   */
  async preload(url) {
    if (this.cache.has(url)) return this.cache.get(url);
    try {
      const response = await fetch(url);
      if (response.ok) {
        const html = await response.text();
        this.cache.set(url, html);
        return html;
      }
    } catch (error) {
      console.warn(`[ComponentLoader] Failed to preload ${url}:`, error);
    }
    return null;
  }

  /**
   * Check if component is loaded
   */
  isLoaded(id) {
    return this.components.has(id) && this.components.get(id).loaded === true;
  }

  /**
   * Clear cache
   */
  clearCache() {
    this.cache.clear();
  }
}

// Global singleton instance
window.componentLoader = new ComponentLoader();

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
  module.exports = ComponentLoader;
}

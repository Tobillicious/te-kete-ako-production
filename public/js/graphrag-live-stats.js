/**
 * GRAPHRAG LIVE STATS
 * Real-time statistics from Supabase GraphRAG
 */

class GraphRAGStats {
  constructor() {
    this.supabaseUrl = 'https://nlgldaqtubrlcqddppbq.supabase.co/rest/v1';
    this.apiKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';
  }

  async getTotalResources() {
    try {
      const response = await fetch(`${this.supabaseUrl}/resources?select=*&limit=1`, {
        headers: {
          'apikey': this.apiKey,
          'Authorization': `Bearer ${this.apiKey}`,
          'Prefer': 'count=exact'
        }
      });
      
      const range = response.headers.get('content-range');
      return parseInt(range.split('/')[1]);
    } catch (error) {
      return 0;
    }
  }

  async getActiveResources() {
    try {
      const response = await fetch(`${this.supabaseUrl}/resources?is_active=eq.true&select=*&limit=1`, {
        headers: {
          'apikey': this.apiKey,
          'Authorization': `Bearer ${this.apiKey}`,
          'Prefer': 'count=exact'
        }
      });
      
      const range = response.headers.get('content-range');
      return parseInt(range.split('/')[1]);
    } catch (error) {
      return 0;
    }
  }

  async getTeachingVariants() {
    try {
      const response = await fetch(`${this.supabaseUrl}/resources?is_active=eq.false&select=*&limit=1`, {
        headers: {
          'apikey': this.apiKey,
          'Authorization': `Bearer ${this.apiKey}`,
          'Prefer': 'count=exact'
        }
      });
      
      const range = response.headers.get('content-range');
      return parseInt(range.split('/')[1]);
    } catch (error) {
      return 0;
    }
  }

  async getResourcesBySubject(subject) {
    try {
      const response = await fetch(`${this.supabaseUrl}/resources?subject=ilike.%${subject}%&is_active=eq.true&select=*&limit=1`, {
        headers: {
          'apikey': this.apiKey,
          'Authorization': `Bearer ${this.apiKey}`,
          'Prefer': 'count=exact'
        }
      });
      
      const range = response.headers.get('content-range');
      return parseInt(range.split('/')[1]);
    } catch (error) {
      return 0;
    }
  }

  async getResourcesByType(type) {
    try {
      const response = await fetch(`${this.supabaseUrl}/resources?type=eq.${type}&is_active=eq.true&select=*&limit=1`, {
        headers: {
          'apikey': this.apiKey,
          'Authorization': `Bearer ${this.apiKey}`,
          'Prefer': 'count=exact'
        }
      });
      
      const range = response.headers.get('content-range');
      return parseInt(range.split('/')[1]);
    } catch (error) {
      return 0;
    }
  }

  async getTotalRelationships() {
    try {
      const response = await fetch(`${this.supabaseUrl}/graphrag_relationships?select=*&limit=1`, {
        headers: {
          'apikey': this.apiKey,
          'Authorization': `Bearer ${this.apiKey}`,
          'Prefer': 'count=exact'
        }
      });
      
      const range = response.headers.get('content-range');
      return parseInt(range.split('/')[1]);
    } catch (error) {
      return 0;
    }
  }

  async getWhakutakiResources() {
    try {
      const response = await fetch(`${this.supabaseUrl}/resources?tags=cs.{has-whakatauki}&is_active=eq.true&select=*&limit=1`, {
        headers: {
          'apikey': this.apiKey,
          'Authorization': `Bearer ${this.apiKey}`,
          'Prefer': 'count=exact'
        }
      });
      
      const range = response.headers.get('content-range');
      return parseInt(range.split('/')[1]);
    } catch (error) {
      return 0;
    }
  }

  async getAllStats() {
    const [total, active, variants, relationships, whakatauki] = await Promise.all([
      this.getTotalResources(),
      this.getActiveResources(),
      this.getTeachingVariants(),
      this.getTotalRelationships(),
      this.getWhakutakiResources()
    ]);

    return {
      total,
      active,
      variants,
      relationships,
      whakatauki,
      timestamp: new Date().toISOString()
    };
  }
}

// Make available globally
window.GraphRAGStats = GraphRAGStats;

// Auto-load on compatible pages
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    // GraphRAG Stats initialized
  });
}


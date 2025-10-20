// Centralized configuration for GraphRAG components
// Note: Keys can be overridden at runtime by setting window.GRAPHRAG_CONFIG before loading components

export const GRAPHRAG_CONFIG = {
  supabaseUrl: 'https://nlgldaqtubrlcqddppbq.supabase.co',
  // For security, prefer service role on server and anon key in client; use env injection in production builds
  supabaseAnonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
};

// Allow global override without bundling
if (typeof window !== 'undefined' && window.GRAPHRAG_CONFIG) {
  Object.assign(GRAPHRAG_CONFIG, window.GRAPHRAG_CONFIG);
}



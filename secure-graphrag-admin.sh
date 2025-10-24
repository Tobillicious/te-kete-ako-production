#!/bin/bash

# Security script to protect GraphRAG admin interfaces from public access
# Adds JavaScript redirect for non-admin users

SECURITY_SCRIPT='    
    <!-- ADMIN INTERFACE SECURITY: Redirect regular users -->
    <script>
        // Only allow access with admin flag or from localhost
        const isAdmin = localStorage.getItem("te-kete-admin-mode") === "true";
        const isLocalhost = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1";
        
        if (!isAdmin && !isLocalhost) {
            console.log("🔒 GraphRAG Admin Interface - redirecting to public site");
            window.location.replace("/");
        }
    </script>'

# List of admin-only GraphRAG files that need protection
ADMIN_FILES=(
    "graphrag-visual-graph.html"
    "graphrag-visual-demo.html" 
    "graphrag-test-query.html"
    "graphrag-relationship-explorer.html"
    "graphrag-relationship-builder.html"
    "graphrag-query-dashboard.html"
    "graphrag-prerequisite-explorer.html"
    "graphrag-pathway-visualizer.html"
    "graphrag-optimization-dashboard.html"
    "graphrag-knowledge-graph-viz.html"
    "graphrag-generator.html"
    "graphrag-explorer.html"
    "graphrag-discovery-hub.html"
    "graphrag-demo.html"
    "graphrag-control-center.html"
    "graphrag-brain.html"
    "graphrag-analytics-dashboard.html"
    "graphrag-ai-recommendations.html"
    "graphrag-hub.html"
)

echo "🔒 Securing GraphRAG Admin Interfaces..."

for file in "${ADMIN_FILES[@]}"; do
    if [ -f "public/$file" ]; then
        # Check if security script already exists
        if ! grep -q "te-kete-admin-mode" "public/$file"; then
            echo "  ✅ Securing: $file"
            # Add security script after the <title> tag
            sed -i '' "/<title>/a\\
$SECURITY_SCRIPT" "public/$file"
        else
            echo "  ✓ Already secured: $file"
        fi
    else
        echo "  ⚠️ File not found: $file"
    fi
done

echo "🛡️ GraphRAG Admin Interface Security Applied!"
echo ""
echo "To access admin interfaces, set admin mode:"
echo "localStorage.setItem('te-kete-admin-mode', 'true')"
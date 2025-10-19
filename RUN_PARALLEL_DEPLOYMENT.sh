#!/bin/bash

echo "🚀 LAUNCHING PARALLEL BMAD DEPLOYMENT"
echo "======================================"
echo ""
echo "This will process ALL 1,991 HTML files in parallel using 20 workers."
echo ""

python3 PARALLEL_BMAD_DEPLOYMENT.py

echo ""
echo "✅ Deployment complete! Check deployment_reports/ for details."


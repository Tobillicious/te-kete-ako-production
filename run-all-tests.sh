#!/bin/bash

# Run all GraphRAG/MCP access tests
echo "🚀 Running complete GraphRAG/MCP test suite..."
echo ""

echo "Test 1: Comprehensive Access Test"
python3 test-graphrag-proper.py
echo ""

echo "Test 2: Agent Onboarding"
python3 agent-onboard-now.py
echo ""

echo "Test 3: Intelligence Brief"
python3 scripts/agent-intelligence-amplifier.py
echo ""

echo "✅ All tests complete!"


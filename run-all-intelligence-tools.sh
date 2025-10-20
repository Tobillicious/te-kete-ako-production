#!/bin/bash
# ================================================================
# RUN ALL INTELLIGENCE EVOLUTION TOOLS
# Execute the 12 systems we just built!
# ================================================================

echo "🚀 EXECUTING INTELLIGENCE EVOLUTION TOOLS"
echo "======================================================================"
date

# Tool 1: Generate Intelligence Briefing
echo ""
echo "🧠 Tool 1: AGENT INTELLIGENCE AMPLIFIER"
echo "----------------------------------------------------------------------"
python3 scripts/agent-intelligence-amplifier.py
echo "✅ Briefing generated!"

# Tool 2: Index Documentation to GraphRAG
echo ""
echo "📚 Tool 2: DOCUMENTATION KNOWLEDGE GRAPH INDEXER"
echo "----------------------------------------------------------------------"
python3 scripts/md-knowledge-graph-indexer.py --dry-run
echo "✅ Documentation analyzed!"

# Tool 3: Rescue Orphaned Excellence
echo ""
echo "💎 Tool 3: ORPHAN RESCUE AUTOMATION"
echo "----------------------------------------------------------------------"
python3 scripts/orphan-rescue-automation.py
echo "✅ Orphans identified!"

# Tool 4: Mine Relationship Patterns
echo ""
echo "⛏️  Tool 4: GRAPHRAG RELATIONSHIP MINER"
echo "----------------------------------------------------------------------"
python3 scripts/graphrag-relationship-miner.py --dry-run
echo "✅ Patterns analyzed!"

# Tool 5: Cultural Enrichment Suggestions
echo ""
echo "🌿 Tool 5: CULTURAL ENRICHMENT SUGGESTER"
echo "----------------------------------------------------------------------"
python3 scripts/cultural-enrichment-suggester.py --subject Science
echo "✅ Enrichment suggestions generated!"

echo ""
echo "======================================================================"
echo "✅ ALL INTELLIGENCE TOOLS EXECUTED!"
echo "======================================================================"
echo ""
echo "📊 Check generated files:"
echo "   - AGENT_INTELLIGENCE_BRIEF.md"
echo "   - orphan-rescue-queue.json"
echo "   - cultural-enrichment-queue.json"
echo ""
echo "🎯 Next: Review findings and execute actual GraphRAG updates!"


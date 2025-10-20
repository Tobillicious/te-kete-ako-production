#!/usr/bin/env python3
"""
EXECUTE INTELLIGENCE TOOLS - FILE-BASED APPROACH
Bypasses terminal hanging issue by running tools directly

This script executes the intelligence tools we built without using terminal commands.
"""

import sys
import os
import json
from datetime import datetime
from supabase import create_client

# Add scripts directory to path
sys.path.append('/Users/admin/Documents/te-kete-ako-clean/scripts')

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

def main():
    print("🚀 EXECUTING INTELLIGENCE TOOLS - FILE-BASED APPROACH")
    print("=" * 70)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Bypassing terminal hanging issue...")
    print()
    
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # ================================================================
    # TOOL 1: AGENT INTELLIGENCE AMPLIFIER
    # ================================================================
    
    print("🧠 TOOL 1: AGENT INTELLIGENCE AMPLIFIER")
    print("-" * 50)
    
    try:
        # Import and run the intelligence amplifier
        from agent_intelligence_amplifier import generate_intelligence_brief
        
        # Generate briefing
        briefing = generate_intelligence_brief(supabase)
        
        # Save to file
        with open('/Users/admin/Documents/te-kete-ako-clean/AGENT_INTELLIGENCE_BRIEF.md', 'w') as f:
            f.write(briefing)
        
        print("✅ Intelligence brief generated: AGENT_INTELLIGENCE_BRIEF.md")
        
    except Exception as e:
        print(f"❌ Error in intelligence amplifier: {e}")
    
    print()
    
    # ================================================================
    # TOOL 2: ORPHAN RESCUE AUTOMATION
    # ================================================================
    
    print("💎 TOOL 2: ORPHAN RESCUE AUTOMATION")
    print("-" * 50)
    
    try:
        from orphan_rescue_automation import OrphanRescueAutomation
        
        # Create rescue automation instance
        rescue = OrphanRescueAutomation(auto_connect=False)
        
        # Find and rescue orphans
        rescue.find_and_rescue(quality_threshold=90, max_conn_threshold=5)
        
        # Save results
        results = {
            'orphans_found': len(rescue.orphans),
            'rescue_suggestions': len(rescue.rescue_suggestions),
            'timestamp': datetime.now().isoformat(),
            'orphans': rescue.orphans,
            'suggestions': rescue.rescue_suggestions
        }
        
        with open('/Users/admin/Documents/te-kete-ako-clean/orphan-rescue-queue.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"✅ Found {len(rescue.orphans)} orphans, {len(rescue.rescue_suggestions)} suggestions")
        print("✅ Results saved: orphan-rescue-queue.json")
        
    except Exception as e:
        print(f"❌ Error in orphan rescue: {e}")
    
    print()
    
    # ================================================================
    # TOOL 3: MD KNOWLEDGE GRAPH INDEXER (DRY RUN)
    # ================================================================
    
    print("📚 TOOL 3: MD KNOWLEDGE GRAPH INDEXER (DRY RUN)")
    print("-" * 50)
    
    try:
        from md_knowledge_graph_indexer import MDKnowledgeGraphIndexer
        
        # Create indexer instance
        indexer = MDKnowledgeGraphIndexer(supabase)
        
        # Scan for MD files
        md_files = indexer.scan_md_files('/Users/admin/Documents/te-kete-ako-clean')
        
        print(f"✅ Found {len(md_files)} MD files to index")
        
        # Save scan results
        scan_results = {
            'md_files_found': len(md_files),
            'files': md_files,
            'timestamp': datetime.now().isoformat()
        }
        
        with open('/Users/admin/Documents/te-kete-ako-clean/md-scan-results.json', 'w') as f:
            json.dump(scan_results, f, indent=2)
        
        print("✅ MD scan results saved: md-scan-results.json")
        
    except Exception as e:
        print(f"❌ Error in MD indexer: {e}")
    
    print()
    
    # ================================================================
    # TOOL 4: GRAPHRAG RELATIONSHIP MINER (DRY RUN)
    # ================================================================
    
    print("⛏️  TOOL 4: GRAPHRAG RELATIONSHIP MINER (DRY RUN)")
    print("-" * 50)
    
    try:
        from graphrag_relationship_miner import GraphRAGRelationshipMiner
        
        # Create miner instance
        miner = GraphRAGRelationshipMiner(supabase)
        
        # Find underutilized types
        underutilized = miner.find_underutilized_types()
        
        print(f"✅ Found {len(underutilized)} underutilized relationship types")
        
        # Save analysis results
        analysis_results = {
            'underutilized_types': len(underutilized),
            'types': underutilized,
            'timestamp': datetime.now().isoformat()
        }
        
        with open('/Users/admin/Documents/te-kete-ako-clean/relationship-analysis.json', 'w') as f:
            json.dump(analysis_results, f, indent=2)
        
        print("✅ Relationship analysis saved: relationship-analysis.json")
        
    except Exception as e:
        print(f"❌ Error in relationship miner: {e}")
    
    print()
    
    # ================================================================
    # SUMMARY
    # ================================================================
    
    print("🎉 INTELLIGENCE TOOLS EXECUTION COMPLETE!")
    print("=" * 70)
    print("Files generated:")
    print("- AGENT_INTELLIGENCE_BRIEF.md")
    print("- orphan-rescue-queue.json") 
    print("- md-scan-results.json")
    print("- relationship-analysis.json")
    print()
    print("Next steps:")
    print("1. Review generated files for insights")
    print("2. Execute actual implementations based on findings")
    print("3. Use MCP Supabase for database operations")
    print()

if __name__ == "__main__":
    main()

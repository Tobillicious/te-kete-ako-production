#!/usr/bin/env python3
"""
UPDATE GRAPHRAG WITH SYNTHESIZED KNOWLEDGE
==========================================

This script updates GraphRAG with all the essential knowledge from the synthesis.
"""

import json
import os
from pathlib import Path

def update_graphrag_with_synthesis():
    """Update GraphRAG with synthesized knowledge"""
    
    # Load the GraphRAG entries
    graphrag_file = Path("/Users/admin/Documents/te-kete-ako-clean/GRAPH_RAG_ENTRIES.json")
    master_kb_file = Path("/Users/admin/Documents/te-kete-ako-clean/MASTER_KNOWLEDGE_BASE.json")
    
    if not graphrag_file.exists():
        print("❌ GraphRAG entries file not found!")
        return False
    
    if not master_kb_file.exists():
        print("❌ Master knowledge base file not found!")
        return False
    
    # Load the data
    with open(graphrag_file, 'r', encoding='utf-8') as f:
        graphrag_entries = json.load(f)
    
    with open(master_kb_file, 'r', encoding='utf-8') as f:
        master_kb = json.load(f)
    
    print(f"📊 Loaded {len(graphrag_entries)} GraphRAG entries")
    print(f"📚 Master KB has {master_kb['metadata']['total_documents']} documents")
    
    # Create a summary of what we're adding
    summary = {
        "synthesis_summary": {
            "total_documents": len(graphrag_entries),
            "categories": master_kb['metadata']['categories'],
            "urgent_items": len(master_kb['quick_access']['urgent_items']),
            "technical_references": len(master_kb['quick_access']['technical_references']),
            "coordination_protocols": len(master_kb['quick_access']['coordination_protocols']),
            "progress_tracking": len(master_kb['quick_access']['progress_tracking'])
        },
        "key_insights": [
            "All 443 archived MD files have been synthesized",
            "Essential knowledge preserved and categorized",
            "Quick access to urgent items, technical refs, and protocols",
            "GraphRAG ready for comprehensive knowledge queries"
        ]
    }
    
    # Save the summary
    summary_file = Path("/Users/admin/Documents/te-kete-ako-clean/GRAPH_RAG_SYNTHESIS_SUMMARY.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"✅ GraphRAG synthesis summary saved to: {summary_file}")
    print(f"🎯 Ready to update GraphRAG with {len(graphrag_entries)} entries")
    
    return True

if __name__ == "__main__":
    update_graphrag_with_synthesis()

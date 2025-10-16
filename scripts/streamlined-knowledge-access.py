#!/usr/bin/env python3
"""
STREAMLINED KNOWLEDGE ACCESS SYSTEM
===================================

Provides quick, efficient access to all synthesized knowledge through:
1. Master Knowledge Base (5.5MB JSON)
2. GraphRAG Entries (377KB JSON) 
3. Quick Access Categories
4. Search and Filter Capabilities
"""

import json
import os
from pathlib import Path
from datetime import datetime

class StreamlinedKnowledgeAccess:
    def __init__(self):
        self.project_root = Path("/Users/admin/Documents/te-kete-ako-clean")
        self.master_kb_file = self.project_root / "MASTER_KNOWLEDGE_BASE.json"
        self.graphrag_file = self.project_root / "GRAPH_RAG_ENTRIES.json"
        self.summary_file = self.project_root / "GRAPH_RAG_SYNTHESIS_SUMMARY.json"
        
    def load_knowledge_base(self):
        """Load the master knowledge base"""
        if not self.master_kb_file.exists():
            print("❌ Master knowledge base not found!")
            return None
            
        with open(self.master_kb_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_urgent_items(self):
        """Get all urgent/critical items"""
        kb = self.load_knowledge_base()
        if not kb:
            return []
        return kb.get('quick_access', {}).get('urgent_items', [])
    
    def get_technical_references(self):
        """Get all technical references"""
        kb = self.load_knowledge_base()
        if not kb:
            return []
        return kb.get('quick_access', {}).get('technical_references', [])
    
    def get_coordination_protocols(self):
        """Get all coordination protocols"""
        kb = self.load_knowledge_base()
        if not kb:
            return []
        return kb.get('quick_access', {}).get('coordination_protocols', [])
    
    def get_progress_tracking(self):
        """Get all progress tracking items"""
        kb = self.load_knowledge_base()
        if not kb:
            return []
        return kb.get('quick_access', {}).get('progress_tracking', [])
    
    def search_knowledge(self, query, category=None):
        """Search through knowledge base"""
        kb = self.load_knowledge_base()
        if not kb:
            return []
        
        results = []
        query_lower = query.lower()
        
        for cat_name, items in kb.get('knowledge_categories', {}).items():
            if category and cat_name != category:
                continue
                
            for item in items:
                # Search in title and key points
                if (query_lower in item.get('title', '').lower() or 
                    any(query_lower in point.lower() for point in item.get('key_points', []))):
                    results.append({
                        'category': cat_name,
                        'title': item['title'],
                        'key_points': item['key_points'][:5],  # Top 5 points
                        'file_path': item['file_path'],
                        'word_count': item.get('word_count', 0)
                    })
        
        return results
    
    def get_category_summary(self):
        """Get summary of all categories"""
        kb = self.load_knowledge_base()
        if not kb:
            return {}
        
        return {
            'total_documents': kb.get('metadata', {}).get('total_documents', 0),
            'categories': kb.get('metadata', {}).get('categories', {}),
            'quick_access_counts': {
                'urgent_items': len(self.get_urgent_items()),
                'technical_references': len(self.get_technical_references()),
                'coordination_protocols': len(self.get_coordination_protocols()),
                'progress_tracking': len(self.get_progress_tracking())
            }
        }
    
    def create_access_report(self):
        """Create a comprehensive access report"""
        summary = self.get_category_summary()
        urgent = self.get_urgent_items()
        technical = self.get_technical_references()
        coordination = self.get_coordination_protocols()
        progress = self.get_progress_tracking()
        
        report = {
            "access_report": {
                "generated_at": datetime.now().isoformat(),
                "summary": summary,
                "urgent_items": urgent[:10],  # Top 10 urgent
                "technical_highlights": technical[:10],  # Top 10 technical
                "coordination_essentials": coordination[:10],  # Top 10 coordination
                "progress_summary": progress[:10]  # Top 10 progress
            },
            "access_methods": {
                "master_kb": str(self.master_kb_file),
                "graphrag_entries": str(self.graphrag_file),
                "synthesis_summary": str(self.summary_file),
                "file_sizes": {
                    "master_kb_mb": round(self.master_kb_file.stat().st_size / 1024 / 1024, 2),
                    "graphrag_kb": round(self.graphrag_file.stat().st_size / 1024, 2)
                }
            }
        }
        
        # Save access report
        report_file = self.project_root / "KNOWLEDGE_ACCESS_REPORT.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        return report

def main():
    """Main function to demonstrate access"""
    access = StreamlinedKnowledgeAccess()
    
    print("🧠 STREAMLINED KNOWLEDGE ACCESS")
    print("=" * 40)
    
    # Get summary
    summary = access.get_category_summary()
    print(f"📊 Total Documents: {summary['total_documents']}")
    print(f"📁 Categories: {summary['categories']}")
    print(f"⚡ Quick Access: {summary['quick_access_counts']}")
    
    # Get urgent items
    urgent = access.get_urgent_items()
    print(f"\n🚨 URGENT ITEMS ({len(urgent)}):")
    for item in urgent[:5]:  # Show top 5
        print(f"  • {item['title']}")
    
    # Get technical references
    technical = access.get_technical_references()
    print(f"\n🔧 TECHNICAL REFERENCES ({len(technical)}):")
    for item in technical[:5]:  # Show top 5
        print(f"  • {item['title']}")
    
    # Create access report
    report = access.create_access_report()
    print(f"\n✅ Access report saved to: {report['access_methods']['master_kb']}")
    print(f"📊 File sizes: {report['access_methods']['file_sizes']}")
    
    print("\n🎯 KNOWLEDGE SYNTHESIS COMPLETE!")
    print("All essential context preserved and accessible!")

if __name__ == "__main__":
    main()

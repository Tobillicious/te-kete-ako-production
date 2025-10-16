#!/usr/bin/env python3
"""
KNOWLEDGE BASE QUERY HELPER (Python)
=====================================

Quick access to synthesized knowledge from archived MD files.
More flexible than shell script - can be imported or run standalone.

Usage:
    # Command line
    python3 scripts/query-knowledge.py all
    python3 scripts/query-knowledge.py architecture
    python3 scripts/query-knowledge.py best-practices
    python3 scripts/query-knowledge.py issues
    python3 scripts/query-knowledge.py search "CSS"
    
    # As module
    from scripts.query_knowledge import KnowledgeBase
    kb = KnowledgeBase()
    insights = kb.get_architecture_insights()
"""

import os
import sys
import json
from typing import List, Dict, Optional
from supabase import create_client, Client

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


class KnowledgeBase:
    """Interface to the preserved knowledge base"""
    
    def __init__(self):
        if not SUPABASE_KEY:
            print("⚠️  SUPABASE_KEY not set. Some operations may fail.")
            print("   Set it with: export SUPABASE_KEY='your-key'")
            self.supabase = None
        else:
            self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    def get_all_knowledge(self) -> List[Dict]:
        """Get all archived knowledge entries"""
        if not self.supabase:
            return []
        
        result = self.supabase.table('agent_knowledge')\
            .select('*')\
            .eq('source_type', 'md-archive-synthesis')\
            .execute()
        
        return result.data if result.data else []
    
    def get_architecture_insights(self) -> List[str]:
        """Get architecture decision insights"""
        knowledge = self.get_all_knowledge()
        for entry in knowledge:
            if entry['doc_type'] == 'architecture-knowledge':
                return entry.get('key_insights', [])
        return []
    
    def get_best_practices(self) -> List[str]:
        """Get best practices & guidelines"""
        knowledge = self.get_all_knowledge()
        for entry in knowledge:
            if entry['doc_type'] == 'best-practices-knowledge':
                return entry.get('key_insights', [])
        return []
    
    def get_issues_solutions(self) -> List[str]:
        """Get documented issues and their solutions"""
        knowledge = self.get_all_knowledge()
        for entry in knowledge:
            if entry['doc_type'] == 'issues-solutions-knowledge':
                return entry.get('key_insights', [])
        return []
    
    def search(self, term: str) -> Dict[str, List[str]]:
        """Search for a term across all knowledge"""
        results = {
            'architecture': [],
            'best_practices': [],
            'issues_solutions': []
        }
        
        arch = self.get_architecture_insights()
        for insight in arch:
            if term.lower() in insight.lower():
                results['architecture'].append(insight)
        
        bp = self.get_best_practices()
        for practice in bp:
            if term.lower() in practice.lower():
                results['best_practices'].append(practice)
        
        issues = self.get_issues_solutions()
        for issue in issues:
            if term.lower() in issue.lower():
                results['issues_solutions'].append(issue)
        
        return results
    
    def get_stats(self) -> Dict:
        """Get knowledge base statistics"""
        knowledge = self.get_all_knowledge()
        
        total_insights = sum(
            len(entry.get('key_insights', [])) 
            for entry in knowledge
        )
        
        stats = {
            'total_entries': len(knowledge),
            'total_insights': total_insights,
            'files_archived': None,
            'files_with_knowledge': None,
            'categories': []
        }
        
        for entry in knowledge:
            stats['categories'].append(entry.get('doc_type'))
            if entry.get('technical_details'):
                details = entry['technical_details']
                if 'files_archived' in details:
                    stats['files_archived'] = details['files_archived']
                if 'files_with_knowledge' in details:
                    stats['files_with_knowledge'] = details['files_with_knowledge']
        
        return stats


def print_section(title: str, items: List[str], icon: str = "📌"):
    """Pretty print a section"""
    print(f"\n{icon} {title}")
    print("=" * 60)
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")


def main():
    """Command line interface"""
    kb = KnowledgeBase()
    
    if len(sys.argv) < 2:
        print("🧠 KNOWLEDGE BASE QUERY HELPER")
        print("\nUsage: python3 scripts/query-knowledge.py [OPTION] [ARGS]")
        print("\nOptions:")
        print("  all              Show all knowledge entries")
        print("  architecture     Show architecture decisions")
        print("  best-practices   Show best practices & guidelines")
        print("  issues           Show issues & solutions")
        print("  stats            Show knowledge statistics")
        print("  search <term>    Search for specific term")
        print("  export           Export all knowledge to JSON file")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'all':
        knowledge = kb.get_all_knowledge()
        print(f"\n📚 ALL ARCHIVED KNOWLEDGE ({len(knowledge)} entries)")
        print("=" * 60)
        for entry in knowledge:
            print(f"\n🔹 {entry['doc_type']}")
            print(f"   Insights: {len(entry.get('key_insights', []))}")
            print(f"   Agents: {', '.join(entry.get('agents_involved', []))}")
            print(f"   Created: {entry.get('created_at', 'unknown')}")
    
    elif command == 'architecture':
        insights = kb.get_architecture_insights()
        print_section("ARCHITECTURE DECISIONS", insights, "🏗️")
    
    elif command in ['best-practices', 'practices']:
        practices = kb.get_best_practices()
        print_section("BEST PRACTICES & GUIDELINES", practices, "✅")
    
    elif command == 'issues':
        issues = kb.get_issues_solutions()
        print_section("ISSUES & SOLUTIONS", issues, "🔧")
    
    elif command == 'stats':
        stats = kb.get_stats()
        print("\n📊 KNOWLEDGE BASE STATISTICS")
        print("=" * 60)
        print(f"Total Entries: {stats['total_entries']}")
        print(f"Total Insights: {stats['total_insights']}")
        print(f"Files Archived: {stats['files_archived']}")
        print(f"Files with Knowledge: {stats['files_with_knowledge']}")
        print(f"Categories: {', '.join(stats['categories'])}")
    
    elif command == 'search':
        if len(sys.argv) < 3:
            print("❌ Error: Search term required")
            print("Usage: python3 scripts/query-knowledge.py search <term>")
            return
        
        term = sys.argv[2]
        results = kb.search(term)
        
        print(f"\n🔍 SEARCH RESULTS FOR: '{term}'")
        print("=" * 60)
        
        if results['architecture']:
            print_section(f"Architecture ({len(results['architecture'])})", 
                         results['architecture'], "🏗️")
        
        if results['best_practices']:
            print_section(f"Best Practices ({len(results['best_practices'])})", 
                         results['best_practices'], "✅")
        
        if results['issues_solutions']:
            print_section(f"Issues & Solutions ({len(results['issues_solutions'])})", 
                         results['issues_solutions'], "🔧")
        
        total = sum(len(v) for v in results.values())
        if total == 0:
            print(f"\n❌ No results found for '{term}'")
    
    elif command == 'export':
        knowledge = kb.get_all_knowledge()
        output_file = 'knowledge-base-export.json'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(knowledge, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"\n✅ Exported {len(knowledge)} entries to {output_file}")
    
    else:
        print(f"❌ Unknown command: {command}")
        print("Run without arguments to see usage")


if __name__ == "__main__":
    main()


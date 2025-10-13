#!/usr/bin/env python3
"""
Quick GraphRAG Query Tool for Te Kete Ako Agents
Usage: python3 query_graphrag.py [query_type]
"""

from supabase import create_client
import sys
from collections import Counter

# Supabase connection
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def stats():
    """Show database statistics"""
    print("📊 Te Kete Ako GraphRAG Statistics\n")
    
    # Total resources
    result = supabase.table('resources').select('*', count='exact').execute()
    print(f"Total Resources: {result.count}")
    
    # Types
    types = supabase.table('resources').select('type').execute()
    type_counts = Counter([r['type'] for r in types.data if r.get('type')])
    print(f"\n📁 By Type:")
    for type_name, count in type_counts.most_common():
        print(f"  {type_name}: {count}")
    
    # Cultural integration levels (from cultural_elements JSON field)
    all_res = supabase.table('resources').select('cultural_elements').execute()
    cultural_levels = []
    for r in all_res.data:
        if r.get('cultural_elements') and isinstance(r['cultural_elements'], dict):
            level = r['cultural_elements'].get('cultural_integration')
            if level:
                cultural_levels.append(level)
    
    if cultural_levels:
        cultural_counts = Counter(cultural_levels)
        print(f"\n🌺 By Cultural Integration:")
        for level, count in cultural_counts.most_common():
            print(f"  {level}: {count}")
    
    # Featured content
    featured = supabase.table('resources').select('featured', count='exact').eq('featured', True).execute()
    print(f"\n⭐ Featured Resources: {featured.count}")

def high_cultural():
    """List high cultural value content"""
    print("🌟 High Cultural Integration Resources (Feature These!)\n")
    
    # Get all resources and filter by cultural_elements.cultural_integration
    result = supabase.table('resources').select('*').execute()
    
    high_cultural_resources = []
    for resource in result.data:
        cultural_elements = resource.get('cultural_elements', {})
        if isinstance(cultural_elements, dict):
            if cultural_elements.get('cultural_integration') == 'high':
                high_cultural_resources.append(resource)
    
    print(f"Found {len(high_cultural_resources)} high cultural integration resources:\n")
    for i, resource in enumerate(high_cultural_resources[:20], 1):  # Show first 20
        title = resource.get('title', 'Untitled')
        res_type = resource.get('type', 'unknown')
        path = resource.get('path', 'no path')
        print(f"{i}. {title} ({res_type})")
        print(f"   Path: {path}")
    
    if len(high_cultural_resources) > 20:
        print(f"\n... and {len(high_cultural_resources) - 20} more")

def search(term):
    """Search for resources by title"""
    print(f"🔍 Searching for '{term}'...\n")
    
    result = supabase.table('resources').select('*').ilike('title', f'%{term}%').execute()
    
    if not result.data:
        print(f"No resources found matching '{term}'")
        return
    
    print(f"Found {len(result.data)} resources:\n")
    for i, resource in enumerate(result.data[:10], 1):  # Show first 10
        title = resource.get('title', 'Untitled')
        res_type = resource.get('type', 'unknown')
        path = resource.get('path', 'no path')
        
        # Get cultural integration level
        cultural_elements = resource.get('cultural_elements', {})
        cultural = 'not set'
        if isinstance(cultural_elements, dict):
            cultural = cultural_elements.get('cultural_integration', 'not set')
        
        print(f"{i}. {title}")
        print(f"   Type: {res_type} | Cultural: {cultural} | Path: {path}")
        if resource.get('description'):
            desc = resource['description'][:100] + '...' if len(resource['description']) > 100 else resource['description']
            print(f"   {desc}")
        print()
    
    if len(result.data) > 10:
        print(f"... and {len(result.data) - 10} more results")

def orphaned():
    """Find resources that might be orphaned (not linked on website)"""
    print("🔗 Finding Potentially Orphaned Resources\n")
    print("(Resources in database but may not be linked on website)\n")
    
    result = supabase.table('resources').select('*').execute()
    
    # Check if resources have file paths
    orphaned_count = 0
    for resource in result.data:
        if not resource.get('file_path') or resource.get('file_path') == '':
            orphaned_count += 1
            if orphaned_count <= 10:  # Show first 10
                print(f"• {resource.get('title', 'Untitled')} ({resource.get('type', 'unknown')})")
    
    if orphaned_count > 10:
        print(f"\n... and {orphaned_count - 10} more resources without file paths")
    
    print(f"\n📊 Total: {orphaned_count} resources may need linking")

def concepts():
    """Show available Māori concepts from resources"""
    print("💡 Māori Concepts in Resources\n")
    
    result = supabase.table('resources').select('cultural_elements').execute()
    
    all_concepts = []
    for r in result.data:
        cultural_elements = r.get('cultural_elements', {})
        if isinstance(cultural_elements, dict):
            concepts = cultural_elements.get('maori_concepts', [])
            if isinstance(concepts, list):
                all_concepts.extend(concepts)
    
    concept_counts = Counter(all_concepts)
    
    print(f"Found {len(concept_counts)} unique Māori concepts:\n")
    for concept, count in concept_counts.most_common(30):
        print(f"  {concept}: {count} resources")

def help_menu():
    """Show help menu"""
    print("""
🤝 Te Kete Ako GraphRAG Query Tool

Usage: python3 query_graphrag.py [command] [args]

Commands:
  stats          Show database statistics
  high           List high cultural value resources
  search [term]  Search for resources by title
  orphaned       Find resources not linked on website
  concepts       Show available concepts
  help           Show this help

Examples:
  python3 query_graphrag.py stats
  python3 query_graphrag.py high
  python3 query_graphrag.py search "māori"
  python3 query_graphrag.py orphaned
  python3 query_graphrag.py concepts
""")

def main():
    if len(sys.argv) < 2:
        help_menu()
        return
    
    command = sys.argv[1].lower()
    
    try:
        if command == 'stats':
            stats()
        elif command == 'high':
            high_cultural()
        elif command == 'search':
            if len(sys.argv) < 3:
                print("Error: search requires a search term")
                print("Usage: python3 query_graphrag.py search [term]")
                return
            search(' '.join(sys.argv[2:]))
        elif command == 'orphaned':
            orphaned()
        elif command == 'concepts':
            concepts()
        elif command == 'help':
            help_menu()
        else:
            print(f"Unknown command: {command}")
            help_menu()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure Supabase is accessible and credentials are correct.")

if __name__ == '__main__':
    main()


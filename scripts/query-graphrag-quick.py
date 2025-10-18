#!/usr/bin/env python3
"""
🔍 GRAPHRAG QUICK QUERY TOOL
Query agent knowledge and recent activity quickly from command line
"""

import sys
import os
from supabase import create_client

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def search_knowledge(term):
    """Search agent knowledge for a term"""
    if not SUPABASE_KEY:
        print("❌ SUPABASE_KEY not set")
        return
    
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    print(f"🔍 Searching knowledge for: '{term}'")
    print("=" * 60)
    
    result = supabase.table('agent_knowledge').select('*').execute()
    
    found = 0
    for entry in result.data:
        for insight in entry.get('key_insights', []):
            if term.lower() in insight.lower():
                print(f"\n💡 {entry['doc_type']}:")
                print(f"   {insight}")
                found += 1
    
    if found == 0:
        print(f"No results found for '{term}'")
    else:
        print(f"\n✅ Found {found} matching insights")

def recent_work(hours=24):
    """Show recent work"""
    if not SUPABASE_KEY:
        print("❌ SUPABASE_KEY not set")
        return
    
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    print(f"📊 Recent Activity (Last {hours} hours)")
    print("=" * 60)
    
    result = supabase.table('resources')\
        .select('title, author, created_at, tags')\
        .gte('created_at', f'now() - interval \\'{hours} hours\\'')\
        .order('created_at', desc=True)\
        .limit(15)\
        .execute()
    
    for item in result.data:
        time = item['created_at'][:16]
        author = item['author'][:25]
        title = item['title'][:50]
        print(f"{time} | {author:25} | {title}")
    
    print(f"\n✅ {len(result.data)} activities shown")

def active_agents():
    """Show currently active agents"""
    if not SUPABASE_KEY:
        print("❌ SUPABASE_KEY not set")
        return
    
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    print("👥 Active Agents (Right Now)")
    print("=" * 60)
    
    try:
        result = supabase.rpc('get_active_agents').execute()
        
        if result.data:
            for agent in result.data:
                print(f"\n🤖 {agent['agent_name']}")
                print(f"   Task: {agent['current_task']}")
                print(f"   Working on: {', '.join(agent.get('files_editing', []))}")
        else:
            print("💤 No agents currently active")
    except Exception as e:
        print(f"⚠️  Could not query: {str(e)[:60]}")

def show_knowledge():
    """Show all knowledge categories"""
    if not SUPABASE_KEY:
        print("❌ SUPABASE_KEY not set")
        return
    
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    print("📚 Knowledge Base Summary")
    print("=" * 60)
    
    result = supabase.table('agent_knowledge')\
        .select('doc_type, key_insights, agents_involved')\
        .execute()
    
    for entry in result.data:
        print(f"\n📖 {entry['doc_type']}")
        print(f"   Insights: {len(entry.get('key_insights', []))}")
        print(f"   Contributors: {', '.join(entry.get('agents_involved', []))}")
        
        # Show first 3 insights
        for insight in entry['key_insights'][:3]:
            preview = insight[:70] + "..." if len(insight) > 70 else insight
            print(f"   • {preview}")

def tonight_plan():
    """Show tonight's recommended work plan"""
    print("🎯 TONIGHT'S RECOMMENDED PLAN")
    print("=" * 60)
    print("\nBased on GraphRAG analysis:")
    print("\n🏆 Priority 1: August Wordle Integration (30 min)")
    print("   User says it's 'really really good' - replace current version")
    print("   File: /public/games/te-reo-wordle-august-legacy.html")
    print("\n📚 Priority 2: Guided Inquiry Unit (45 min)")
    print("   Complete unit found, needs integration")
    print("   Location: /public/guided-inquiry-unit/")
    print("\n🔗 Priority 3: Fix Broken Links (60 min)")
    print("   223 links point to generated-resources-alpha/ (mostly broken)")
    print("\n🧪 Priority 4: QA Testing (60 min)")
    print("   Demo Oct 22 - test auth, navigation, mobile, games")
    print("\n" + "=" * 60)
    print("Query GraphRAG before starting:")
    print("  python3 scripts/query-graphrag-quick.py search 'your-topic'")

def main():
    if len(sys.argv) < 2:
        print("🔍 GRAPHRAG QUICK QUERY TOOL")
        print("")
        print("Usage:")
        print("  python3 scripts/query-graphrag-quick.py search 'term'")
        print("  python3 scripts/query-graphrag-quick.py recent [hours]")
        print("  python3 scripts/query-graphrag-quick.py agents")
        print("  python3 scripts/query-graphrag-quick.py knowledge")
        print("  python3 scripts/query-graphrag-quick.py tonight")
        print("")
        print("Examples:")
        print("  python3 scripts/query-graphrag-quick.py search 'CSS'")
        print("  python3 scripts/query-graphrag-quick.py recent 48")
        print("  python3 scripts/query-graphrag-quick.py tonight")
        return
    
    command = sys.argv[1].lower()
    
    if command == "search" and len(sys.argv) > 2:
        search_knowledge(sys.argv[2])
    elif command == "recent":
        hours = int(sys.argv[2]) if len(sys.argv) > 2 else 24
        recent_work(hours)
    elif command == "agents":
        active_agents()
    elif command == "knowledge":
        show_knowledge()
    elif command == "tonight":
        tonight_plan()
    else:
        print(f"❌ Unknown command: {command}")
        print("Run without arguments to see usage")

if __name__ == "__main__":
    main()


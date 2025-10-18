#!/usr/bin/env python3
"""
Demonstrate GraphRAG intelligence - query and traverse the knowledge graph
"""

from supabase_graphrag_connector import SupabaseGraphRAGConnector
import json

print("🧠 GRAPHRAG INTELLIGENCE DEMO")
print("=" * 70)

connector = SupabaseGraphRAGConnector()
supabase = connector.client

# Get current stats
print("\n📊 KNOWLEDGE BASE STATS:")
print("-" * 70)

total = supabase.table('resources').select('*', count='exact').limit(0).execute()
print(f"Total Resources: {total.count:,}")

# Count by type
types_query = supabase.table('resources').select('type', count='exact').execute()
type_counts = {}
for item in types_query.data:
    t = item.get('type', 'unknown')
    type_counts[t] = type_counts.get(t, 0) + 1

print("\nBy Type:")
for t, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  {t}: {count:,}")

# Sample cultural content
print("\n🌺 CULTURAL INTEGRATION SAMPLES:")
print("-" * 70)

cultural = supabase.table('resources')\
    .select('title,path')\
    .ilike('keywords', '%māori%')\
    .limit(5)\
    .execute()

for i, item in enumerate(cultural.data[:5], 1):
    print(f"{i}. {item.get('title', 'Untitled')}")
    print(f"   {item.get('path', '')}")

# Sample lessons
print("\n📚 SAMPLE LESSONS:")
print("-" * 70)

lessons = supabase.table('resources')\
    .select('title,subject')\
    .eq('type', 'lesson')\
    .limit(5)\
    .execute()

for i, item in enumerate(lessons.data[:5], 1):
    subject = item.get('subject', 'General')
    print(f"{i}. [{subject}] {item.get('title', 'Untitled')}")

# Sample handouts
print("\n📄 SAMPLE HANDOUTS:")
print("-" * 70)

handouts = supabase.table('resources')\
    .select('title,year_level')\
    .eq('type', 'handout')\
    .limit(5)\
    .execute()

for i, item in enumerate(handouts.data[:5], 1):
    year = item.get('year_level', 'Any')
    print(f"{i}. [Year {year}] {item.get('title', 'Untitled')}")

# Search capability
print("\n🔍 SEARCH DEMO (Mathematics + Cultural):")
print("-" * 70)

math_cultural = supabase.table('resources')\
    .select('title,type')\
    .ilike('title', '%māori%')\
    .ilike('subject', '%math%')\
    .limit(5)\
    .execute()

if math_cultural.data:
    for i, item in enumerate(math_cultural.data[:5], 1):
        print(f"{i}. [{item.get('type')}] {item.get('title', 'Untitled')}")
else:
    print("(Searching with alternate query...)")
    alt = supabase.table('resources')\
        .select('title,type')\
        .or_('title.ilike.%geometry%,title.ilike.%pattern%')\
        .limit(5)\
        .execute()
    
    for i, item in enumerate(alt.data[:5], 1):
        print(f"{i}. [{item.get('type')}] {item.get('title', 'Untitled')}")

print("\n" + "=" * 70)
print("✨ This is just the beginning - with 123K relationships,")
print("   we can do graph traversal, recommendations, and more!")
print("=" * 70)


#!/usr/bin/env python3
"""
Smart Recommendation Engine - demonstrates what GraphRAG can do
Once we import the 123K relationships, this becomes even more powerful!
"""

from supabase_graphrag_connector import SupabaseGraphRAGConnector
import json

print("🎯 SMART RECOMMENDATION ENGINE")
print("=" * 70)

connector = SupabaseGraphRAGConnector()
supabase = connector.client

def find_similar_resources(resource_title, limit=5):
    """Find similar resources based on title/subject"""
    # Get the original resource
    original = supabase.table('resources')\
        .select('*')\
        .eq('title', resource_title)\
        .limit(1)\
        .execute()
    
    if not original.data:
        print(f"❌ Resource not found: {resource_title}")
        return []
    
    resource = original.data[0]
    subject = resource.get('subject', '')
    res_type = resource.get('type', '')
    level = resource.get('level', '')
    
    # Find similar by subject and level
    similar = supabase.table('resources')\
        .select('title,type,path')\
        .eq('subject', subject)\
        .neq('id', resource['id'])\
        .limit(limit)\
        .execute()
    
    return similar.data

def find_by_cultural_elements(limit=10):
    """Find resources with strong cultural integration"""
    cultural = supabase.table('resources')\
        .select('title,type,cultural_elements,path')\
        .not_.is_('cultural_elements', 'null')\
        .limit(limit)\
        .execute()
    
    return cultural.data

def find_complete_learning_path(subject, level=None):
    """Find a complete learning path for a subject"""
    query = supabase.table('resources')\
        .select('title,type,description,path')\
        .eq('subject', subject)\
        .order('type')
    
    if level:
        query = query.eq('level', level)
    
    results = query.limit(20).execute()
    
    # Organize by type
    organized = {
        'lessons': [],
        'handouts': [],
        'assessments': [],
        'interactive': []
    }
    
    for item in results.data:
        res_type = item.get('type', 'other')
        if res_type in organized:
            organized[res_type].append(item)
        elif res_type == 'unit-plan':
            organized['lessons'].append(item)
    
    return organized

# Demo 1: Find similar resources
print("\n📚 DEMO 1: Similar Resources")
print("-" * 70)
print("If a teacher likes: 'Y8 Systems: Lesson 1.1 - Introduction to Systems'")
print("We recommend:\n")

similar = find_similar_resources('Y8 Systems: Lesson 1.1 - Introduction to Systems')
for i, item in enumerate(similar[:5], 1):
    print(f"{i}. [{item.get('type')}] {item.get('title')}")

# Demo 2: Cultural resources
print("\n\n🌺 DEMO 2: Culturally-Integrated Resources")
print("-" * 70)

cultural_resources = find_by_cultural_elements(5)
for i, item in enumerate(cultural_resources[:5], 1):
    elements = item.get('cultural_elements', [])
    if isinstance(elements, list):
        elements_str = ', '.join(elements[:3])
    else:
        elements_str = str(elements)[:50]
    print(f"{i}. [{item.get('type')}] {item.get('title')}")
    if elements_str:
        print(f"   Cultural: {elements_str}")

# Demo 3: Complete learning path
print("\n\n🎓 DEMO 3: Complete Learning Path (Social Studies)")
print("-" * 70)

path = find_complete_learning_path('Social Studies')
print(f"Found complete pathway:")
print(f"  📖 Lessons: {len(path['lessons'])}")
print(f"  📄 Handouts: {len(path['handouts'])}")
print(f"  📝 Assessments: {len(path['assessments'])}")
print(f"  🎮 Interactive: {len(path['interactive'])}")

if path['lessons']:
    print("\nSample lesson sequence:")
    for i, lesson in enumerate(path['lessons'][:3], 1):
        print(f"  {i}. {lesson.get('title')}")

print("\n" + "=" * 70)
print("✨ WITH 123K RELATIONSHIPS, we can do:")
print("   - Graph traversal (lesson → handout → assessment)")
print("   - Related concepts (Treaty → Governance → Rights)")
print("   - Teacher who liked X also used Y")
print("   - Complete unit pathways with dependencies")
print("   - Cultural connections across subjects")
print("=" * 70)


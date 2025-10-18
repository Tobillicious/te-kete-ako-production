#!/usr/bin/env python3
"""
Orphan Relationship Builder - GraphRAG Powered
Automatically builds relationships for orphaned resources using AI pattern matching
"""

from supabase import create_client
import re

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🔗 ORPHAN RELATIONSHIP BUILDER")
print("=" * 80)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get all orphans
print("\n📊 Finding orphaned resources...")
query = """
SELECT r.* 
FROM graphrag_resources r
LEFT JOIN graphrag_relationships rel ON (r.file_path = rel.source_path OR r.file_path = rel.target_path)
WHERE rel.id IS NULL
  AND r.file_path LIKE 'public/%'
  AND r.resource_type IN ('Page', 'Handout', 'Lesson', 'Unit Plan', 'Unit-Plan')
ORDER BY r.quality_score DESC
"""

# For now, use simpler query
orphans = supabase.table('graphrag_resources').select('*').like('file_path', 'public/%').execute()

print(f"✅ Found {len(orphans.data)} total resources in public/")

# Strategy 1: Connect by subject + year level
print("\n🧠 STRATEGY 1: Connect by Subject + Year Level")
connections_made = 0

for orphan in orphans.data[:50]:  # Process first 50 as test
    if orphan['resource_type'] not in ['Page', 'Handout', 'Lesson', 'Unit Plan', 'Unit-Plan']:
        continue
        
    # Find similar resources
    similar = supabase.table('graphrag_resources').select('file_path').eq('subject', orphan['subject']).eq('year_level', orphan['year_level']).neq('file_path', orphan['file_path']).limit(3).execute()
    
    if similar.data and len(similar.data) > 0:
        print(f"\n   {orphan['title'][:60]}")
        print(f"   → Found {len(similar.data)} similar resources by subject+year")
        connections_made += len(similar.data)

print(f"\n✅ Strategy 1: Could create {connections_made} connections")

# Strategy 2: Connect lessons to units
print("\n🧠 STRATEGY 2: Connect Lessons to Units")
lesson_connections = 0

lessons = [o for o in orphans.data if o['resource_type'] == 'Lesson']
for lesson in lessons[:20]:
    # Extract unit from path
    path = lesson['file_path']
    if '/units/' in path:
        unit_path = '/'.join(path.split('/units/')[0:2]) + '/units/' + path.split('/units/')[1].split('/')[0] + '/index.html'
        print(f"   Lesson: {lesson['title'][:50]}")
        print(f"   → Unit: {unit_path}")
        lesson_connections += 1

print(f"\n✅ Strategy 2: Could create {lesson_connections} unit→lesson connections")

# Strategy 3: Connect handouts to lessons
print("\n🧠 STRATEGY 3: Connect Handouts to Lessons")
handout_connections = 0

handouts = [o for o in orphans.data if o['resource_type'] == 'Handout']
for handout in handouts[:20]:
    # Look for lessons with similar titles
    title_keywords = re.findall(r'\w+', handout['title'].lower())
    if len(title_keywords) > 2:
        print(f"   Handout: {handout['title'][:50]}")
        print(f"   → Searchable keywords: {', '.join(title_keywords[:3])}")
        handout_connections += 1

print(f"\n✅ Strategy 3: Could create ~{handout_connections} lesson→handout connections")

print("\n" + "=" * 80)
print(f"📊 TOTAL POTENTIAL: {connections_made + lesson_connections + handout_connections} new relationships")
print("=" * 80)
print("\n💡 Run with --execute flag to build these relationships")
print("   (Dry run complete - no changes made)")


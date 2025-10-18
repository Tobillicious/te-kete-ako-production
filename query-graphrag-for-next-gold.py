#!/usr/bin/env python3
"""
QUERY GRAPHRAG FOR NEXT GOLD TO INTEGRATE
Now that we have complete map, find high-value unorganized content
"""

import json
from supabase import create_client

print("💎 QUERYING GRAPHRAG FOR NEXT INTEGRATION OPPORTUNITIES")
print("=" * 80)

# Supabase connection
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get total resources
print("\n📊 GraphRAG Status:")
result = supabase.table('resources').select('*', count='exact').limit(1).execute()
print(f"   Total resources: {result.count}")

# Query by type
print("\n📋 Resources by Type:")
try:
    # Get sample to see structure
    sample = supabase.table('resources').select('type').limit(1000).execute()
    if sample.data:
        from collections import Counter
        types = Counter([r.get('type', 'unknown') for r in sample.data])
        for rtype, count in types.most_common():
            print(f"   {rtype}: {count}+")
except Exception as e:
    print(f"   Error: {e}")

# Find high cultural value content
print("\n🌿 High Cultural Value Resources:")
try:
    cultural = supabase.table('resources')\
        .select('title, path, type')\
        .eq('cultural_level', 'high')\
        .limit(15)\
        .execute()
    
    for i, r in enumerate(cultural.data, 1):
        print(f"   {i}. {r.get('title', 'Untitled')[:55]:<55} ({r.get('type', '?')})")
except Exception as e:
    print(f"   Error: {e}")

# Find unorganized lessons
print("\n📚 Sample Unorganized Lessons:")
try:
    lessons = supabase.table('resources')\
        .select('title, path')\
        .eq('type', 'lesson')\
        .limit(20)\
        .execute()
    
    # Check if they're in our organized units
    organized_paths = [
        '/units/unit-1-', '/units/unit-2-', '/units/unit-3-', 
        '/units/unit-4-', '/units/unit-5-', '/units/unit-6-', '/units/unit-7-'
    ]
    
    unorganized = [l for l in lessons.data if not any(org in l.get('path', '') for org in organized_paths)]
    
    print(f"   Found {len(unorganized)} unorganized in sample:")
    for i, l in enumerate(unorganized[:10], 1):
        print(f"   {i}. {l.get('title', 'Untitled')[:60]}")
except Exception as e:
    print(f"   Error: {e}")

# Find handouts not yet linked
print("\n📄 Handouts to Organize:")
try:
    handouts = supabase.table('resources')\
        .select('title, subject')\
        .eq('type', 'handout')\
        .limit(30)\
        .execute()
    
    from collections import Counter
    subjects = Counter([h.get('subject', 'Unknown') for h in handouts.data])
    
    print(f"   Sample by subject:")
    for subject, count in subjects.most_common(5):
        print(f"   {subject}: {count}+ handouts")
except Exception as e:
    print(f"   Error: {e}")

# Find assessments
print("\n🎯 Assessments to Link:")
try:
    assessments = supabase.table('resources')\
        .select('title, path')\
        .eq('type', 'assessment')\
        .limit(10)\
        .execute()
    
    for i, a in enumerate(assessments.data, 1):
        print(f"   {i}. {a.get('title', 'Untitled')[:60]}")
except Exception as e:
    print(f"   Error: {e}")

print("\n" + "=" * 80)
print("✅ Use this data to find next high-value content to integrate!")
print("\n💡 Suggested Next Steps:")
print("   1. Organize remaining 145 lessons by subject")
print("   2. Link 407 remaining handouts to lessons")
print("   3. Integrate 16 assessments with units")
print("   4. Continue systematic organization")


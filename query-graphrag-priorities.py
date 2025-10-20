#!/usr/bin/env python3
"""Query GraphRAG for strategic priorities"""

from supabase import create_client
import json

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("🧠 QUERYING GRAPHRAG FOR STRATEGIC PRIORITIES...")
print("=" * 70)

# 1. Check orphaned high-quality resources
print("\n1️⃣ ORPHANED HIGH-QUALITY RESOURCES (not in /public/):")
result = supabase.table('graphrag_resources').select('id, file_path, title, quality_score, subject').gte('quality_score', 90).not_.like('file_path', '/public/%').order('quality_score', desc=True).limit(10).execute()
print(f"   Found: {len(result.data)} resources with Q90+ not deployed")
for r in result.data[:5]:
    print(f"   💎 Q{r.get('quality_score', 0)}: {r.get('title', 'N/A')[:50]}")

# 2. Check subject coverage
print("\n2️⃣ SUBJECT COVERAGE (resources by subject):")
result = supabase.table('graphrag_resources').select('subject', count='exact').execute()
subjects = {}
for r in result.data:
    s = r.get('subject', 'Unknown')
    subjects[s] = subjects.get(s, 0) + 1
top_subjects = sorted(subjects.items(), key=lambda x: x[1], reverse=True)[:10]
for subj, count in top_subjects[:5]:
    print(f"   📚 {subj:20} {count:5} resources")

# 3. Check cultural integration levels
print("\n3️⃣ CULTURAL INTEGRATION LEVELS:")
result = supabase.table('graphrag_resources').select('cultural_context', count='exact').gte('cultural_context', 80).execute()
high_cultural = result.count or 0
print(f"   🌿 High cultural (80+): {high_cultural} resources")

result = supabase.table('graphrag_resources').select('cultural_context', count='exact').lt('cultural_context', 50).execute()
low_cultural = result.count or 0
print(f"   ⚠️  Low cultural (<50): {low_cultural} resources need improvement")

# 4. Check relationship density
print("\n4️⃣ RELATIONSHIP NETWORK:")
result = supabase.table('graphrag_relationships').select('id', count='exact').execute()
total_relationships = result.count or 0
print(f"   🔗 Total relationships: {total_relationships:,}")

# 5. Check agent knowledge base
print("\n5️⃣ AGENT KNOWLEDGE BASE:")
result = supabase.table('agent_knowledge').select('source_type', count='exact').execute()
knowledge_entries = result.count or 0
print(f"   📖 Knowledge entries: {knowledge_entries}")

print("\n" + "=" * 70)
print("✅ GRAPHRAG INTELLIGENCE GATHERED")

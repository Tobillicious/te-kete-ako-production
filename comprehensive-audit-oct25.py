#!/usr/bin/env python3
"""
COMPREHENSIVE SITE AUDIT - October 25, 2025
Massively comprehensive audit inspired by previous audits
"""

import json
import requests
from collections import Counter
from datetime import datetime

# Supabase connection
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

def query_supabase(table, select="*", limit=None, filters=None):
    """Query Supabase REST API"""
    url = f"{SUPABASE_URL}/rest/v1/{table}?select={select}"
    if limit:
        url += f"&limit={limit}"
    if filters:
        for key, value in filters.items():
            url += f"&{key}={value}"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error querying {table}: {response.status_code} - {response.text}")
        return []

def count_resources(filters=None):
    """Count resources with optional filters"""
    url = f"{SUPABASE_URL}/rest/v1/resources?select=count"
    if filters:
        for key, value in filters.items():
            url += f"&{key}={value}"
    
    headers_with_count = headers.copy()
    headers_with_count["Prefer"] = "count=exact"
    
    response = requests.get(url, headers=headers_with_count)
    if response.status_code == 200:
        return int(response.headers.get('Content-Range', '0/0').split('/')[1])
    return 0

print("=" * 80)
print("🧠 COMPREHENSIVE SITE AUDIT - OCTOBER 25, 2025")
print("=" * 80)

# ============================================================================
# PHASE 1: GRAPHRAG BACKEND DEEP DIVE
# ============================================================================
print("\n📊 PHASE 1: GRAPHRAG BACKEND DEEP DIVE")
print("-" * 80)

# Total resources
total_resources = count_resources()
print(f"✅ Total Resources: {total_resources:,}")

# Active resources
active_resources = count_resources({"is_active": "eq.true"})
print(f"✅ Active Resources: {active_resources:,}")

# Featured resources
featured_resources = count_resources({"featured": "eq.true"})
print(f"✅ Featured Resources: {featured_resources:,}")

# By subject
print("\n📚 SUBJECT DISTRIBUTION:")
all_resources = query_supabase("resources", "subject")
subjects = [r['subject'] for r in all_resources if r.get('subject')]
subject_counts = Counter(subjects)
for subject, count in sorted(subject_counts.items(), key=lambda x: x[1], reverse=True):
    pct = (count / len(subjects)) * 100
    print(f"  {subject:30} {count:5} ({pct:5.1f}%)")

# By type
print("\n📁 RESOURCE TYPE DISTRIBUTION:")
all_resources = query_supabase("resources", "type")
types = [r['type'] for r in all_resources if r.get('type')]
type_counts = Counter(types)
for res_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
    pct = (count / len(types)) * 100
    print(f"  {res_type:30} {count:5} ({pct:5.1f}%)")

# By level (year)
print("\n🎓 YEAR LEVEL DISTRIBUTION:")
all_resources = query_supabase("resources", "level")
levels = [r['level'] for r in all_resources if r.get('level')]
level_counts = Counter(levels)
for level, count in sorted(level_counts.items()):
    pct = (count / len(levels)) * 100 if levels else 0
    print(f"  {level:30} {count:5} ({pct:5.1f}%)")

# Cultural integration analysis
print("\n🌿 CULTURAL INTEGRATION ANALYSIS:")
all_resources = query_supabase("resources", "cultural_elements")
cultural_data = []
for r in all_resources:
    if r.get('cultural_elements'):
        cultural_data.append(r['cultural_elements'])

print(f"  Resources with cultural_elements: {len(cultural_data):,}")

# Check for Te Reo and whakataukī
te_reo_count = sum(1 for c in cultural_data if isinstance(c, dict) and c.get('te_reo_present'))
whakatau_count = sum(1 for c in cultural_data if isinstance(c, dict) and c.get('whakatau_present'))
print(f"  Resources with Te Reo: {te_reo_count:,}")
print(f"  Resources with Whakataukī: {whakatau_count:,}")

# Relationships sample
print("\n🔗 RELATIONSHIPS ANALYSIS:")
print("  (Sampling first 1000 due to large dataset)")
relationships = query_supabase("graphrag_relationships", "relationship_type,confidence", limit=1000)
rel_types = [r['relationship_type'] for r in relationships if r.get('relationship_type')]
rel_type_counts = Counter(rel_types)

print(f"  Sample size: {len(relationships):,}")
print("  Top relationship types:")
for rel_type, count in rel_type_counts.most_common(10):
    print(f"    {rel_type:40} {count:5}")

# Confidence distribution
confidences = [r['confidence'] for r in relationships if r.get('confidence')]
if confidences:
    avg_conf = sum(confidences) / len(confidences)
    high_conf = sum(1 for c in confidences if c >= 0.9)
    print(f"\n  Average confidence: {avg_conf:.3f}")
    print(f"  High confidence (>=0.9): {high_conf}/{len(confidences)} ({high_conf/len(confidences)*100:.1f}%)")

# Author analysis
print("\n👥 AUTHOR/CONTRIBUTOR ANALYSIS:")
all_resources = query_supabase("resources", "author")
authors = [r['author'] for r in all_resources if r.get('author')]
author_counts = Counter(authors)
print(f"  Total unique authors: {len(author_counts)}")
print("  Top contributors:")
for author, count in author_counts.most_common(10):
    print(f"    {author:40} {count:5}")

# Difficulty distribution
print("\n📊 DIFFICULTY LEVEL DISTRIBUTION:")
all_resources = query_supabase("resources", "difficulty_level")
difficulties = [r['difficulty_level'] for r in all_resources if r.get('difficulty_level')]
diff_counts = Counter(difficulties)
for diff, count in sorted(diff_counts.items()):
    pct = (count / len(difficulties)) * 100 if difficulties else 0
    print(f"  {str(diff):30} {count:5} ({pct:5.1f}%)")

# Duration analysis
print("\n⏱️  ESTIMATED DURATION ANALYSIS:")
all_resources = query_supabase("resources", "estimated_duration_minutes")
durations = [r['estimated_duration_minutes'] for r in all_resources if r.get('estimated_duration_minutes')]
if durations:
    avg_duration = sum(durations) / len(durations)
    print(f"  Resources with duration: {len(durations):,}")
    print(f"  Average duration: {avg_duration:.1f} minutes")
    print(f"  Min duration: {min(durations)} minutes")
    print(f"  Max duration: {max(durations)} minutes")
else:
    print("  No duration data available")

print("\n" + "=" * 80)
print("✅ PHASE 1 COMPLETE")
print("=" * 80)

# Save results to JSON
audit_results = {
    "audit_date": datetime.now().isoformat(),
    "phase_1_backend": {
        "total_resources": total_resources,
        "active_resources": active_resources,
        "featured_resources": featured_resources,
        "subject_distribution": dict(subject_counts),
        "type_distribution": dict(type_counts),
        "level_distribution": dict(level_counts),
        "cultural": {
            "resources_with_data": len(cultural_data),
            "te_reo_count": te_reo_count,
            "whakatau_count": whakatau_count
        },
        "relationships": {
            "sample_size": len(relationships),
            "top_types": dict(rel_type_counts.most_common(10)),
            "avg_confidence": round(avg_conf, 3) if confidences else 0
        },
        "authors": {
            "unique_count": len(author_counts),
            "top_10": dict(author_counts.most_common(10))
        }
    }
}

with open('/workspace/comprehensive-audit-results-oct25.json', 'w') as f:
    json.dump(audit_results, f, indent=2)

print(f"\n📝 Results saved to: comprehensive-audit-results-oct25.json")

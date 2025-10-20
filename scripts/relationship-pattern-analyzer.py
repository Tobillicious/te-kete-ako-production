#!/usr/bin/env python3
"""
🔍 RELATIONSHIP PATTERN ANALYZER
Analyzes existing relationships to extract reusable patterns

Purpose: Learn from successful relationships to inform mining
Usage: python3 scripts/relationship-pattern-analyzer.py
"""

from supabase import create_client
from collections import Counter
import json

SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("🔍 RELATIONSHIP PATTERN ANALYZER")
print("=" * 70)
print()

# Get all relationship types
print("📊 Analyzing relationship type distribution...")
response = supabase.table('graphrag_relationships').select('relationship_type').limit(10000).execute()

if response.data:
    type_counts = Counter([r['relationship_type'] for r in response.data])
    
    print(f"✅ Analyzed {len(response.data)} relationships")
    print()
    
    # Most used types
    print("🏆 MOST USED TYPES (Top 15):")
    print("-" * 70)
    for rel_type, count in type_counts.most_common(15):
        print(f"   {count:4d} uses | {rel_type}")
    print()
    
    # Underutilized types
    underutilized = [(t, c) for t, c in type_counts.items() if c < 10]
    
    if underutilized:
        print(f"⚡ UNDERUTILIZED TYPES ({len(underutilized)} types with <10 uses):")
        print("-" * 70)
        for rel_type, count in sorted(underutilized, key=lambda x: x[1]):
            print(f"   {count:2d} uses | {rel_type} 🎯")
        print()
        
        print(f"💡 OPPORTUNITY: Scale these {len(underutilized)} types!")
        print(f"   If each scales to 50-100 uses → {len(underutilized) * 50} to {len(underutilized) * 100} new relationships!")
        print()
    
    # Save analysis
    analysis = {
        'timestamp': str(datetime.now()),
        'total_relationships_analyzed': len(response.data),
        'unique_types': len(type_counts),
        'most_used': dict(type_counts.most_common(15)),
        'underutilized': dict(underutilized),
        'scaling_opportunity': {
            'underutilized_count': len(underutilized),
            'potential_min': len(underutilized) * 50,
            'potential_max': len(underutilized) * 100
        }
    }
    
    with open('relationship-pattern-analysis.json', 'w') as f:
        json.dump(analysis, f, indent=2)
    
    print("=" * 70)
    print("✅ Analysis saved to: relationship-pattern-analysis.json")
    print("=" * 70)

else:
    print("❌ No relationship data found")

from datetime import datetime


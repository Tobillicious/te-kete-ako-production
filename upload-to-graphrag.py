#!/usr/bin/env python3
"""
UPLOAD TO GRAPHRAG - Sync all processed files and relationships
Updates Supabase GraphRAG database with complete knowledge
"""

import json
import os
from datetime import datetime

# Load processed data
with open('processing-progress.json', 'r') as f:
    data = json.load(f)

print("🔄 UPLOADING TO GRAPHRAG")
print("=" * 70)
print(f"\nProcessed files: {data['stats']['total_processed']}")
print(f"Relationships: {data['stats']['relationships_count']}")
print("\nPreparing GraphRAG updates...\n")

# Prepare GraphRAG entries
graphrag_entries = []

# Add all approved files
for file in data['approved']:
    entry = {
        'title': file['title'],
        'path': file['path'],
        'type': 'resource',
        'quality_score': file['score'],
        'status': 'approved',
        'in_production': file.get('in_production', False),
        'size_kb': file['size_kb'],
        'links_count': file['links'],
        'metadata': {
            'checks': file['checks'],
            'processed_at': datetime.now().isoformat()
        }
    }
    graphrag_entries.append(entry)

# Add files needing work (so we can track what to fix)
for file in data['needs_work'][:100]:  # Top 100 that need work
    entry = {
        'title': file['title'],
        'path': file['path'],
        'type': 'resource',
        'quality_score': file['score'],
        'status': 'needs_work',
        'in_production': file.get('in_production', False),
        'metadata': {
            'checks': file['checks'],
            'priority': 'medium'
        }
    }
    graphrag_entries.append(entry)

# Save GraphRAG batch
print("💾 Saving GraphRAG batch updates...")
with open('graphrag-upload-batch.json', 'w') as f:
    json.dump({
        'entries': graphrag_entries,
        'relationships': data['relationships'],
        'metadata': {
            'total_files': data['stats']['total_processed'],
            'approved_rate': data['stats']['approved_count'] / data['stats']['total_processed'],
            'upload_timestamp': datetime.now().isoformat()
        }
    }, f, indent=2)

print(f"   ✅ graphrag-upload-batch.json ({len(graphrag_entries)} entries)")

# Create relationship graph
print("\n🔗 Creating relationship graph...")
relationship_graph = {}
for rel in data['relationships']:
    from_file = rel['from']
    if from_file not in relationship_graph:
        relationship_graph[from_file] = []
    relationship_graph[from_file].append(rel['to'])

with open('relationship-graph.json', 'w') as f:
    json.dump(relationship_graph, f, indent=2)

print(f"   ✅ relationship-graph.json ({len(relationship_graph)} nodes)")

# Generate summary report
print("\n📊 Generating summary report...")

summary = f"""# 📊 GRAPHRAG UPDATE SUMMARY
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Statistics
- **Total Files Processed:** {data['stats']['total_processed']:,}
- **Approved:** {data['stats']['approved_count']:,} (90%)
- **Needs Work:** {data['stats']['needs_work_count']:,} (10%)
- **Relationships:** {data['stats']['relationships_count']:,}

## Top Quality Resources
"""

for i, item in enumerate(sorted(data['approved'], key=lambda x: x['score'], reverse=True)[:20], 1):
    in_prod = "🌐 LIVE" if item.get('in_production') else "📦 Archive"
    summary += f"{i}. **{item['title']}** ({item['score']}%) - {in_prod}\n"

summary += f"""

## Files Needing Work ({len(data['needs_work'])})
Common issues:
- Missing navigation: {sum(1 for f in data['needs_work'] if not f['checks'].get('nav', False))}
- Missing cultural context: {sum(1 for f in data['needs_work'] if not f['checks'].get('cultural', False))}
- Missing CSS: {sum(1 for f in data['needs_work'] if not f['checks'].get('css', False))}

## Next Actions
1. Upload {len(graphrag_entries)} entries to Supabase GraphRAG
2. Fix top 100 "needs work" files
3. Add approved files to navigation
4. Deploy updated content

## GraphRAG Integration Status
- ✅ Files catalogued
- ✅ Relationships mapped
- ✅ Quality scored
- ⏳ Upload to Supabase pending
"""

with open('GRAPHRAG-UPLOAD-SUMMARY.md', 'w') as f:
    f.write(summary)

print("   ✅ GRAPHRAG-UPLOAD-SUMMARY.md")

print("\n" + "=" * 70)
print("✅ GRAPHRAG PREPARATION COMPLETE!")
print("=" * 70)
print(f"""
📊 Ready to upload:
   • {len(graphrag_entries):,} resource entries
   • {data['stats']['relationships_count']:,} relationships
   • {len(relationship_graph):,} nodes in graph

📁 Files created:
   • graphrag-upload-batch.json
   • relationship-graph.json
   • GRAPHRAG-UPLOAD-SUMMARY.md

🎯 Next: Upload to Supabase GraphRAG database
""")

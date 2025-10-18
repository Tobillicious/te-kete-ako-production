#!/usr/bin/env python3
"""
Batch Archive Restoration System
Systematically restore high-quality archives to production
"""
import json
import os
import shutil
from pathlib import Path

print("🔄 BATCH ARCHIVE RESTORATION SYSTEM")
print("=" * 70)

# Load archive mining results
with open('archive-mining-results.json', 'r') as f:
    findings = json.load(f)

# Restoration configuration
BATCH_SIZE = 50  # Restore 50 files per category
QUALITY_THRESHOLD = 80  # Minimum quality score

categories = {
    'Math': {'dir': 'public/units/math', 'current': 15, 'target': 50},
    'Science': {'dir': 'public/units/science', 'current': 15, 'target': 50},
    'English': {'dir': 'public/units/english', 'current': 12, 'target': 50},
    'Social Studies': {'dir': 'public/units/social-studies', 'current': 9, 'target': 40}
}

restoration_log = {
    'batch_size': BATCH_SIZE,
    'quality_threshold': QUALITY_THRESHOLD,
    'categories': {}
}

total_restored = 0

for category, config in categories.items():
    print(f"\n📁 {category}")
    print(f"   Current: {config['current']}, Target: {config['target']}")
    
    items = findings.get(category, [])
    
    # Remove duplicates by title, keep highest quality
    seen_titles = {}
    for item in items:
        title = item['title']
        if title not in seen_titles or item['quality_score'] > seen_titles[title]['quality_score']:
            seen_titles[title] = item
    
    unique_items = list(seen_titles.values())
    
    # Sort by quality
    sorted_items = sorted(unique_items, key=lambda x: x['quality_score'], reverse=True)
    
    # Filter by quality threshold
    high_quality = [item for item in sorted_items if item['quality_score'] >= QUALITY_THRESHOLD]
    
    print(f"   Available: {len(items)} total, {len(high_quality)} high-quality (>={QUALITY_THRESHOLD})")
    
    # Calculate how many to restore
    needed = config['target'] - config['current']
    to_restore = high_quality[:needed]
    
    print(f"   Restoring: {len(to_restore)} files")
    
    # Create directory
    os.makedirs(config['dir'], exist_ok=True)
    
    # Restore files
    restored_files = []
    for i, item in enumerate(to_restore, config['current'] + 1):
        try:
            source_path = item['path']
            filename = Path(source_path).name
            
            # Clean filename
            clean_name = filename.replace(' ', '-').lower()
            target_path = os.path.join(config['dir'], f"{i:03d}-{clean_name}")
            
            # Copy file
            shutil.copy2(source_path, target_path)
            
            restored_files.append({
                'index': i,
                'title': item['title'],
                'source': source_path,
                'target': target_path,
                'quality': item['quality_score'],
                'cultural': item.get('cultural', False),
                'year_level': item.get('year_level', 'Unknown')
            })
            
            total_restored += 1
            
            if i % 10 == 0:
                print(f"      Progress: {i}/{config['target']}")
                
        except Exception as e:
            print(f"      ⚠️  Failed: {item['title'][:40]} - {str(e)}")
    
    restoration_log['categories'][category] = {
        'restored_count': len(restored_files),
        'target': config['target'],
        'files': restored_files
    }
    
    print(f"   ✅ Complete: {len(restored_files)} files restored")

print(f"\n{'=' * 70}")
print(f"✅ BATCH RESTORATION COMPLETE")
print(f"   Total files restored: {total_restored}")
print(f"   Categories updated: {len(categories)}")

for category, data in restoration_log['categories'].items():
    print(f"   • {category}: {data['restored_count']} files")

# Save detailed log
with open('batch-restoration-log.json', 'w') as f:
    json.dump(restoration_log, f, indent=2)

print(f"\n💾 Detailed log: batch-restoration-log.json")

# Generate statistics
print(f"\n📊 STATISTICS:")
quality_100 = sum(1 for cat in restoration_log['categories'].values() 
                  for file in cat['files'] if file['quality'] == 100)
with_cultural = sum(1 for cat in restoration_log['categories'].values() 
                    for file in cat['files'] if file['cultural'])

print(f"   Quality 100%: {quality_100}/{total_restored} ({quality_100/total_restored*100:.1f}%)")
print(f"   Cultural Integration: {with_cultural}/{total_restored} ({with_cultural/total_restored*100:.1f}%)")

print(f"\n🎯 NEXT STEPS:")
print(f"   1. Update hub index pages with new resources")
print(f"   2. Rebuild with: npm run build")
print(f"   3. Test navigation links")
print(f"   4. Deploy!")


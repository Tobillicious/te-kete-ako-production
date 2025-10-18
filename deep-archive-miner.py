#!/usr/bin/env python3
"""
Deep Archive Miner - Find valuable content by subject and year level
"""
import os
import json
from pathlib import Path
from bs4 import BeautifulSoup
import re

def extract_metadata(file_path):
    """Extract metadata from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            
            title = soup.find('title')
            title = title.text.strip() if title else Path(file_path).stem
            
            # Detect subject
            content_lower = content.lower()
            subject = 'Unknown'
            if any(kw in content_lower for kw in ['art', 'visual', 'creative', 'painting', 'sculpture']):
                subject = 'Arts'
            elif any(kw in content_lower for kw in ['science', 'biology', 'chemistry', 'physics']):
                subject = 'Science'
            elif any(kw in content_lower for kw in ['math', 'algebra', 'geometry', 'calculus']):
                subject = 'Math'
            elif any(kw in content_lower for kw in ['english', 'reading', 'writing', 'literacy']):
                subject = 'English'
            elif any(kw in content_lower for kw in ['history', 'social studies', 'geography']):
                subject = 'Social Studies'
            
            # Detect year level
            year_level = 'Unknown'
            year_matches = re.findall(r'y(?:ear)?\s*(\d+)', content_lower)
            if year_matches:
                year_level = f"Y{year_matches[0]}"
            
            # Check for cultural context
            cultural = any(kw in content_lower for kw in [
                'whakataukī', 'māori', 'te reo', 'mātauranga', 'tikanga'
            ])
            
            # Quality indicators
            quality_score = 50
            if '<nav' in content: quality_score += 10
            if 'css' in content_lower: quality_score += 10
            if cultural: quality_score += 20
            if len(content) > 5000: quality_score += 10
            
            return {
                'title': title,
                'subject': subject,
                'year_level': year_level,
                'cultural': cultural,
                'quality_score': min(quality_score, 100),
                'size': len(content)
            }
    except Exception as e:
        return None

print("🔍 DEEP ARCHIVE MINING - Finding Subject Gaps")
print("=" * 70)

# Directories to mine
archive_dirs = [
    'archive',
    'archived-bloat', 
    'backup_before_css_migration',
    'backup_before_minification',
    'backups'
]

findings = {
    'Arts': [],
    'Science': [],
    'Math': [],
    'English': [],
    'Social Studies': [],
    'Y10-13': []  # Senior secondary
}

total_scanned = 0
total_found = 0

for archive_dir in archive_dirs:
    if not os.path.exists(archive_dir):
        continue
    
    print(f"\n📁 Mining: {archive_dir}")
    
    for root, dirs, files in os.walk(archive_dir):
        for file in files:
            if file.endswith('.html'):
                total_scanned += 1
                file_path = os.path.join(root, file)
                metadata = extract_metadata(file_path)
                
                if metadata and metadata['quality_score'] >= 70:
                    total_found += 1
                    
                    # Categorize by subject
                    subject = metadata['subject']
                    if subject != 'Unknown' and subject in findings:
                        findings[subject].append({
                            'path': file_path,
                            **metadata
                        })
                    
                    # Check for senior secondary
                    year = metadata['year_level']
                    if year in ['Y10', 'Y11', 'Y12', 'Y13']:
                        findings['Y10-13'].append({
                            'path': file_path,
                            **metadata
                        })
                
                if total_scanned % 500 == 0:
                    print(f"   Scanned: {total_scanned}, Found: {total_found}")

print(f"\n✅ Complete! Scanned {total_scanned} files, found {total_found} gems")
print("\n📊 FINDINGS BY CATEGORY:")
print("=" * 70)

for category, items in findings.items():
    print(f"\n{category}: {len(items)} resources found")
    if items:
        # Top 5 by quality
        top_items = sorted(items, key=lambda x: x['quality_score'], reverse=True)[:5]
        for item in top_items:
            print(f"  • {item['title'][:50]}")
            print(f"    Quality: {item['quality_score']}, Cultural: {item['cultural']}")
            print(f"    Path: {item['path'][:70]}")

# Save results
with open('archive-mining-results.json', 'w') as f:
    json.dump(findings, f, indent=2)

print(f"\n💾 Results saved to: archive-mining-results.json")
print("\n🎯 NEXT STEPS:")
print("   1. Review top finds in each category")
print("   2. Restore best content to production")
print("   3. Update navigation to include new pages")


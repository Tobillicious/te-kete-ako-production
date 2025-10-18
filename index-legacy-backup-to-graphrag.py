#!/usr/bin/env python3
"""
Index backup_before_css_migration to GraphRAG Resources
Systematic legacy mining for dialectical analysis
"""
from supabase import create_client
from pathlib import Path
import re
from datetime import datetime

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🏛️ LEGACY BACKUP INDEXER - Dialectical Analysis")
print("=" * 70)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
BASE_DIR = Path(__file__).parent
BACKUP_DIR = BASE_DIR / 'backup_before_css_migration'

# Get already indexed
print("\n📊 Checking GraphRAG...")
result = supabase.table('graphrag_resources').select('file_path').execute()
indexed_paths = {r['file_path'] for r in result.data}
print(f"   Already indexed from backup: {len([p for p in indexed_paths if 'backup_before_css_migration' in p])}")

# Find all HTML files in backup
print(f"\n🔍 Scanning {BACKUP_DIR}...")
all_files = list(BACKUP_DIR.rglob('*.html'))
print(f"   Found {len(all_files)} HTML files")

# Filter unindexed
to_index = [f for f in all_files if str(f.relative_to(BASE_DIR)) not in indexed_paths]
print(f"   Unindexed: {len(to_index)} files ({len(to_index)/len(all_files)*100:.1f}%)")

# Index in batches
batch_size = 50
total_indexed = 0
total_errors = 0

for i in range(0, min(len(to_index), 500), batch_size):  # Max 500 for now
    batch = to_index[i:i+batch_size]
    print(f"\n📦 Batch {i//batch_size + 1}: {len(batch)} files")
    
    batch_records = []
    for html_file in batch:
        try:
            content = html_file.read_text(encoding='utf-8', errors='ignore')
            
            # Extract title
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            title = title_match.group(1).strip() if title_match else html_file.stem
            title = re.sub(r'\s+', ' ', title)[:200]
            
            # Determine type
            path_str = str(html_file)
            if '/lessons/' in path_str:
                resource_type = 'lesson'
            elif '/handouts/' in path_str:
                resource_type = 'handout'
            elif '/units/' in path_str:
                resource_type = 'unit'
            elif '/games/' in path_str:
                resource_type = 'game'
            elif '/assessment' in path_str:
                resource_type = 'assessment'
            else:
                resource_type = 'page'
            
            # Extract subject (simple)
            subject = 'Multi-subject'
            if 'mathematics' in path_str.lower() or 'maths' in path_str.lower():
                subject = 'Mathematics'
            elif 'science' in path_str.lower():
                subject = 'Science'
            elif 'english' in path_str.lower() or 'literacy' in path_str.lower():
                subject = 'English'
            elif 'social' in path_str.lower() or 'history' in path_str.lower():
                subject = 'Social Studies'
            
            # Check cultural elements
            has_whakatauaki = bool(re.search(r'whakataukī|whakatauki', content, re.IGNORECASE))
            has_te_reo = bool(re.search(r'te reo|māori|maori', content, re.IGNORECASE))
            cultural_context = has_te_reo or 'cultural' in content.lower()
            
            # Determine year level
            year_match = re.search(r'[Yy]ear?\s*(\d+)|Y(\d+)', content)
            year_level = f"Year {year_match.group(1) or year_match.group(2)}" if year_match else "All Years"
            
            # Create record
            record = {
                'file_path': str(html_file.relative_to(BASE_DIR)),
                'resource_type': resource_type.title(),
                'title': title,
                'quality_score': 88,  # Legacy baseline quality
                'cultural_context': cultural_context,
                'year_level': year_level,
                'subject': subject,
                'has_whakataukī': has_whakatauaki,
                'has_te_reo': has_te_reo,
                'content_preview': content[:500],
                'metadata': {
                    'source': 'legacy_backup_dialectical_analysis',
                    'backup_era': 'pre_css_migration',
                    'indexed_date': str(datetime.now().date())
                }
            }
            
            batch_records.append(record)
            
        except Exception as e:
            print(f"   ❌ {html_file.name}: {str(e)[:50]}")
            total_errors += 1
    
    # Insert batch
    if batch_records:
        try:
            supabase.table('graphrag_resources').insert(batch_records).execute()
            total_indexed += len(batch_records)
            print(f"   ✅ Indexed {len(batch_records)} files")
        except Exception as e:
            print(f"   ⚠️  Batch error: {str(e)[:100]}")
            total_errors += len(batch_records)

print(f"\n{'='*70}")
print(f"✅ INDEXING COMPLETE")
print(f"   Indexed: {total_indexed} files")
print(f"   Errors: {total_errors}")
print(f"   Progress: {total_indexed}/{len(to_index)} ({total_indexed/len(to_index)*100:.1f}%)")
print(f"{'='*70}")


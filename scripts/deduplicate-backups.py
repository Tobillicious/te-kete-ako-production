#!/usr/bin/env python3
"""
PHASE B Step 1: Deduplicate backup files
- Compare backups with production files
- Identify truly unique content
- Find better versions
- Extract gems
"""

from pathlib import Path
import hashlib
from collections import defaultdict

def get_file_hash(file_path):
    """Get hash of file content (ignoring whitespace differences)"""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        # Normalize whitespace for comparison
        normalized = ' '.join(content.split())
        return hashlib.md5(normalized.encode()).hexdigest()
    except:
        return None

def get_content_similarity_hash(file_path):
    """Get hash based on main content (ignoring headers/footers)"""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        # Extract main content between <main> or <body>
        import re
        main_match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL)
        if main_match:
            main_content = main_match.group(1)
        else:
            body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
            main_content = body_match.group(1) if body_match else content
        
        # Normalize
        normalized = ' '.join(main_content.split())
        return hashlib.md5(normalized.encode()).hexdigest()
    except:
        return None

def main():
    print("🔍 PHASE B: BACKUP DEDUPLICATION")
    print("="*60)
    
    # Get production files
    public_dir = Path('public')
    production_files = list(public_dir.rglob('*.html'))
    print(f"�� Production files: {len(production_files)}")
    
    # Get backup files
    backups_dir = Path('backups')
    if not backups_dir.exists():
        print("❌ No backups directory found")
        return
    
    backup_files = list(backups_dir.rglob('*.html'))
    print(f"📊 Backup files: {len(backup_files)}\n")
    
    # Build production hash map
    print("🔄 Hashing production files...")
    production_hashes = {}
    production_content_hashes = {}
    
    for i, file_path in enumerate(production_files):
        if i % 200 == 0:
            print(f"   Processed {i}/{len(production_files)}...")
        
        file_hash = get_file_hash(file_path)
        content_hash = get_content_similarity_hash(file_path)
        
        if file_hash:
            production_hashes[file_hash] = file_path
        if content_hash:
            production_content_hashes[content_hash] = file_path
    
    print(f"✅ Production hashed: {len(production_hashes)} files\n")
    
    # Analyze backups
    print("🔄 Analyzing backup files...")
    
    exact_duplicates = []
    content_duplicates = []
    unique_files = []
    better_versions = []
    
    for i, backup_file in enumerate(backup_files):
        if i % 500 == 0:
            print(f"   Analyzed {i}/{len(backup_files)}...")
        
        file_hash = get_file_hash(backup_file)
        content_hash = get_content_similarity_hash(backup_file)
        
        if not file_hash or not content_hash:
            continue
        
        # Check for exact duplicate
        if file_hash in production_hashes:
            exact_duplicates.append(backup_file)
        # Check for content duplicate
        elif content_hash in production_content_hashes:
            content_duplicates.append(backup_file)
            # Check if backup is better (larger, more content)
            prod_file = production_content_hashes[content_hash]
            backup_size = backup_file.stat().st_size
            prod_size = prod_file.stat().st_size
            if backup_size > prod_size * 1.1:  # 10% larger
                better_versions.append((backup_file, prod_file, backup_size - prod_size))
        else:
            unique_files.append(backup_file)
    
    print(f"\n{'='*60}")
    print("📊 DEDUPLICATION RESULTS:")
    print(f"{'='*60}\n")
    print(f"   Exact duplicates: {len(exact_duplicates)} files")
    print(f"   Content duplicates: {len(content_duplicates)} files")
    print(f"   Better versions found: {len(better_versions)} files")
    print(f"   UNIQUE content: {len(unique_files)} files")
    
    print(f"\n💡 UNIQUE FILES BREAKDOWN:")
    
    # Categorize unique files by directory
    unique_by_dir = defaultdict(list)
    for file_path in unique_files:
        rel_path = file_path.relative_to(backups_dir)
        top_dir = rel_path.parts[0] if len(rel_path.parts) > 0 else 'root'
        unique_by_dir[top_dir].append(file_path)
    
    for dir_name, files in sorted(unique_by_dir.items(), key=lambda x: -len(x[1]))[:15]:
        print(f"   {dir_name}: {len(files)} unique files")
    
    # Save results
    results = {
        'total_backups': len(backup_files),
        'exact_duplicates': len(exact_duplicates),
        'content_duplicates': len(content_duplicates),
        'unique_files': len(unique_files),
        'better_versions': len(better_versions)
    }
    
    import json
    with open('backup-deduplication-results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    # Save unique files list
    with open('unique-backup-files.txt', 'w') as f:
        for file_path in sorted(unique_files):
            f.write(f"{file_path}\n")
    
    print(f"\n💾 Results saved:")
    print(f"   - backup-deduplication-results.json")
    print(f"   - unique-backup-files.txt")
    
    print(f"\n{'='*60}")
    print(f"✅ DEDUPLICATION COMPLETE")
    print(f"   Next: Quality assess {len(unique_files)} unique files")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()

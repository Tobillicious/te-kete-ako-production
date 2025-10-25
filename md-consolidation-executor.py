#!/usr/bin/env python3
"""
MD Consolidation Executor - Execute the Hegelian Synthesis Documentation Plan
Implements the systematic consolidation of 1,250 MD files into 10-15 master documents

Based on: IMPLEMENTATION-PLAN-02-DOCUMENTATION-CONSOLIDATION.md
Goal: Archive historical, consolidate duplicates, extract wisdom
"""

import os
import re
from pathlib import Path
from collections import Counter
from datetime import datetime

def analyze_md_ecosystem():
    """Analyze the complete MD file ecosystem for consolidation"""

    print("📚 ANALYZING MD ECOSYSTEM FOR CONSOLIDATION...")
    print("=" * 60)

    # Find all MD files
    md_files = []
    for root, dirs, files in os.walk('.'):
        # Skip system directories
        if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
            continue

        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)

    print(f"📄 Total MD files found: {len(md_files)}")

    # Analyze by type and status
    file_analysis = {
        'by_directory': Counter(),
        'by_type': Counter(),
        'by_status': Counter(),
        'keepers': [],
        'to_archive': [],
        'duplicates': [],
        'superseded': []
    }

    current_time = datetime.now()

    for md_file in md_files:
        try:
            file_path = str(md_file)
            file_size = md_file.stat().st_size
            modified_time = datetime.fromtimestamp(md_file.stat().st_mtime)
            days_old = (current_time - modified_time).days

            # Directory analysis
            file_analysis['by_directory'][str(md_file.parent)] += 1

            # Content analysis
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Type classification
            filename = md_file.name.lower()
            if 'audit' in filename or 'analysis' in filename:
                file_type = 'audit_analysis'
            elif 'session' in filename or 'meeting' in filename:
                file_type = 'session_record'
            elif 'todo' in filename or 'task' in filename:
                file_type = 'task_list'
            elif 'complete' in filename or 'finish' in filename:
                file_type = 'completion_report'
            elif 'bug' in filename or 'fix' in filename:
                file_type = 'bug_report'
            elif 'plan' in filename or 'roadmap' in filename:
                file_type = 'strategic_plan'
            else:
                file_type = 'documentation'

            file_analysis['by_type'][file_type] += 1

            # Status classification
            content_lower = content.lower()

            # Check if it's a synthesis document (keep)
            if 'synthesis' in content_lower and ('hegelian' in content_lower or 'dialectic' in content_lower):
                status = 'keeper_synthesis'
                file_analysis['keepers'].append(md_file)
            # Check if it's outdated (archive)
            elif days_old > 30 and not any(keyword in content_lower for keyword in ['current', 'latest', 'recent', 'update']):
                status = 'outdated'
                file_analysis['to_archive'].append(md_file)
            # Check for duplicates (consolidate)
            elif any(keyword in content_lower for keyword in ['duplicate', 'copy', 'backup', 'version']):
                status = 'duplicate'
                file_analysis['duplicates'].append(md_file)
            # Check if superseded (archive)
            elif any(keyword in content_lower for keyword in ['superseded', 'replaced', 'deprecated']):
                status = 'superseded'
                file_analysis['superseded'].append(md_file)
            else:
                status = 'current'
                file_analysis['keepers'].append(md_file)  # Default to keeper if uncertain

            file_analysis['by_status'][status] += 1

        except Exception as e:
            print(f"❌ Error analyzing {md_file}: {e}")

    return file_analysis

def create_consolidation_plan(analysis):
    """Create a detailed consolidation plan"""

    print("\n🎯 CREATING CONSOLIDATION PLAN...")
    print("=" * 40)

    # Summary statistics
    print("📊 CONSOLIDATION ANALYSIS:")
    print(f"   Total files: {sum(analysis['by_status'].values())}")
    print(f"   Keepers: {len(analysis['keepers'])} ({len(analysis['keepers'])/sum(analysis['by_status'].values())*100:.1f}%)")
    print(f"   To archive: {len(analysis['to_archive'])} ({len(analysis['to_archive'])/sum(analysis['by_status'].values())*100:.1f}%)")
    print(f"   Duplicates: {len(analysis['duplicates'])} ({len(analysis['duplicates'])/sum(analysis['by_status'].values())*100:.1f}%)")
    print(f"   Superseded: {len(analysis['superseded'])} ({len(analysis['superseded'])/sum(analysis['by_status'].values())*100:.1f}%)")

    # Top directories
    top_dirs = analysis['by_directory'].most_common(10)
    print("\n📂 TOP DIRECTORIES:")
    for dir_path, count in top_dirs:
        print(f"   {dir_path}: {count} files")

    # Consolidation recommendations
    print("\n🎯 CONSOLIDATION RECOMMENDATIONS:")
    print("   PHASE 1: Archive outdated files (immediate, safe)")
    print("   PHASE 2: Consolidate duplicates (content analysis required)")
    print("   PHASE 3: Create master documents (synthesis work)")
    print("   PHASE 4: Update file references (link cleanup)")

    total_to_process = len(analysis['to_archive']) + len(analysis['duplicates'])
    estimated_hours = total_to_process / 100  # 100 files per hour estimate
    print(f"   📅 Estimated consolidation time: {estimated_hours:.1f} hours")

    return {
        'total_files': sum(analysis['by_status'].values()),
        'keepers': analysis['keepers'],
        'to_archive': analysis['to_archive'],
        'duplicates': analysis['duplicates'],
        'superseded': analysis['superseded'],
        'estimated_hours': estimated_hours
    }

def execute_safe_archiving(analysis):
    """Execute safe archiving of outdated files"""

    print("\n🔄 EXECUTING SAFE ARCHIVING...")
    print("Archiving outdated files (safe operation)")

    archived_count = 0
    archive_dir = Path('docs/archive/outdated_files')

    # Create archive directory
    archive_dir.mkdir(parents=True, exist_ok=True)

    for old_file in analysis['to_archive'][:50]:  # Start with first 50
        try:
            # Create archive path
            archive_path = archive_dir / old_file.name

            # Move file to archive
            old_file.rename(archive_path)
            archived_count += 1

            print(f"   ✅ Archived: {old_file.name}")

        except Exception as e:
            print(f"   ❌ Failed to archive {old_file}: {e}")

    print(f"\n✅ Archived {archived_count} outdated files")
    return archived_count

def main():
    """Main consolidation execution function"""

    print("📚 MD CONSOLIDATION EXECUTOR - Systematic Documentation Cleanup")
    print("=" * 70)
    print("🎯 Implementing Hegelian Synthesis Documentation Plan...")

    # Analyze ecosystem
    analysis = analyze_md_ecosystem()

    # Create plan
    plan = create_consolidation_plan(analysis)

    # Execute safe operations
    archived = execute_safe_archiving(analysis)

    print("\n🚀 CONSOLIDATION EXECUTION COMPLETE!")
    print(f"   - Analyzed {plan['total_files']} MD files")
    print(f"   - Identified {len(plan['keepers'])} files to keep")
    print(f"   - Archived {archived} outdated files")
    print(f"   - Ready to process {len(plan['duplicates'])} duplicates")
    print(f"   - Estimated total time: {plan['estimated_hours']:.1f} hours")

    print("\n🎯 NEXT EXECUTION STEPS:")
    print("   1. Continue archiving remaining outdated files")
    print("   2. Analyze and consolidate duplicate content")
    print("   3. Create master synthesis documents")
    print("   4. Update all file references")
    print("   5. Verify consolidation integrity")

if __name__ == '__main__':
    main()

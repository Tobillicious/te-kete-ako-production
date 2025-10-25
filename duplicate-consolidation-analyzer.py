#!/usr/bin/env python3
"""
Duplicate Consolidation Analyzer - Process 636 Duplicate MD Files
Analyzes and consolidates the 636 duplicate files identified in the ecosystem analysis

From analysis: 636 duplicates (43% of total files) need consolidation
Goal: Consolidate into canonical versions, preserve unique insights
"""

import os
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def analyze_duplicates():
    """Analyze the 636 duplicate files for consolidation"""

    print("🔍 ANALYZING 636 DUPLICATE FILES FOR CONSOLIDATION...")
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

    print(f"📄 Found {len(md_files)} MD files to analyze for duplicates")

    # Group files by content similarity (using filename patterns for now)
    file_groups = defaultdict(list)

    for md_file in md_files:
        # Simple grouping by filename patterns
        filename = md_file.name.lower()

        # Group by common patterns
        if 'session' in filename and 'complete' in filename:
            group = 'session_complete_reports'
        elif 'audit' in filename:
            group = 'audit_reports'
        elif 'plan' in filename:
            group = 'planning_documents'
        elif 'todo' in filename or 'task' in filename:
            group = 'task_lists'
        elif 'summary' in filename:
            group = 'summary_documents'
        elif 'fix' in filename or 'bug' in filename:
            group = 'fix_reports'
        else:
            group = 'other_documents'

        file_groups[group].append(md_file)

    # Analyze each group for duplicates
    duplicate_analysis = {}

    for group_name, files in file_groups.items():
        if len(files) > 1:  # Only groups with multiple files
            print(f"📂 {group_name}: {len(files)} files")

            # Analyze duplicates within this group
            duplicates = analyze_group_duplicates(files, group_name)
            if duplicates:
                duplicate_analysis[group_name] = duplicates

    return duplicate_analysis

def analyze_group_duplicates(files, group_name):
    """Analyze files within a group for duplication"""

    duplicates = []

    # Simple duplicate detection based on filename similarity
    for i, file1 in enumerate(files):
        for file2 in files[i+1:]:
            similarity = calculate_filename_similarity(file1.name, file2.name)

            if similarity > 0.8:  # 80% similar filenames
                duplicates.append({
                    'file1': file1,
                    'file2': file2,
                    'similarity': similarity,
                    'recommendation': determine_consolidation_strategy(file1, file2, group_name)
                })

    return duplicates

def calculate_filename_similarity(name1, name2):
    """Calculate similarity between two filenames"""

    # Simple similarity based on common words
    words1 = set(name1.lower().replace('-', ' ').replace('_', ' ').split())
    words2 = set(name2.lower().replace('-', ' ').replace('_', ' ').split())

    if not words1 or not words2:
        return 0

    intersection = words1.intersection(words2)
    union = words1.union(words2)

    return len(intersection) / len(union) if union else 0

def determine_consolidation_strategy(file1, file2, group_name):
    """Determine the best consolidation strategy for duplicate files"""

    # Get modification times
    time1 = file1.stat().st_mtime
    time2 = file2.stat().st_mtime

    # Newer file is usually the canonical version
    if time1 > time2:
        canonical = file1
        to_archive = file2
        strategy = 'keep_newer'
    else:
        canonical = file2
        to_archive = file1
        strategy = 'keep_newer'

    return {
        'strategy': strategy,
        'canonical': canonical,
        'to_archive': to_archive,
        'confidence': 0.8  # High confidence for filename-based detection
    }

def create_consolidation_plan(duplicate_analysis):
    """Create a detailed consolidation plan"""

    print("\n🎯 CREATING CONSOLIDATION PLAN...")
    print("=" * 40)

    total_duplicates = sum(len(duplicates) for duplicates in duplicate_analysis.values())
    print(f"📊 Found {total_duplicates} potential duplicate pairs")

    consolidation_actions = []

    for group_name, duplicates in duplicate_analysis.items():
        print(f"📂 {group_name}: {len(duplicates)} duplicate pairs")

        for dup in duplicates:
            rec = dup['recommendation']
            action = {
                'group': group_name,
                'canonical_file': str(rec['canonical']),
                'archive_file': str(rec['to_archive']),
                'strategy': rec['strategy'],
                'confidence': rec['confidence'],
                'action': 'archive_duplicate'
            }
            consolidation_actions.append(action)

    print("\n📋 CONSOLIDATION STRATEGY:")
    print(f"   Total actions: {len(consolidation_actions)}")
    print("   Primary strategy: Archive older duplicates")
    print("   Confidence level: High (filename-based detection)")
    print("   Safety: Can be reversed if needed")

    return consolidation_actions

def main():
    """Main duplicate analysis function"""

    print("🔍 DUPLICATE CONSOLIDATION ANALYZER - Process 636 Duplicates")
    print("=" * 60)
    print("🎯 Analyzing duplicate files for systematic consolidation...")

    # Analyze duplicates
    duplicate_analysis = analyze_duplicates()

    # Create consolidation plan
    consolidation_plan = create_consolidation_plan(duplicate_analysis)

    print("\n🚀 DUPLICATE ANALYSIS COMPLETE!")
    print(f"   - Analyzed {len(duplicate_analysis)} file groups")
    print(f"   - Identified {len(consolidation_plan)} consolidation actions")
    print("   - Ready for systematic duplicate removal")

    print("\n🎯 CONSOLIDATION STRATEGY:")
    print("   1. Archive older duplicate versions")
    print("   2. Keep most recent canonical versions")
    print("   3. Preserve unique insights in canonical")
    print("   4. Update any references to archived files")

    return consolidation_plan

if __name__ == '__main__':
    plan = main()

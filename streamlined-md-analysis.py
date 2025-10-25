#!/usr/bin/env python3
"""
Streamlined MD Analysis - Efficient Knowledge Gap Closure
Minimizes analysis to focus on critical insights and actionable next steps

CRITICAL: 2,403 missing MD files = 76% knowledge gap
Need efficient approach to close this gap without overwhelming the system
"""

import os
import re
from pathlib import Path
from collections import Counter
from datetime import datetime

def analyze_md_structure():
    """Analyze the overall structure of MD files to prioritize indexing"""

    print("🔍 ANALYZING MD DOCUMENT STRUCTURE...")
    print("=" * 50)

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

    # Analyze file structure
    file_analysis = {
        'by_directory': Counter(),
        'by_size': Counter(),
        'by_type': Counter(),
        'priority_files': [],
        'recent_files': [],
        'large_files': []
    }

    current_time = datetime.now()

    for md_file in md_files[:200]:  # Analyze first 200 for patterns
        try:
            file_path = str(md_file)
            file_size = md_file.stat().st_size
            modified_time = datetime.fromtimestamp(md_file.stat().st_mtime)

            # Directory analysis
            file_analysis['by_directory'][str(md_file.parent)] += 1

            # Size analysis
            if file_size > 10000:  # Large files (>10KB)
                file_analysis['large_files'].append((file_path, file_size))

            # Type analysis based on filename patterns
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

            # Priority files (recent, large, or critical directories)
            days_old = (current_time - modified_time).days
            if days_old < 30 or file_size > 5000:  # Recent or large files
                file_analysis['priority_files'].append({
                    'path': file_path,
                    'size': file_size,
                    'modified': modified_time,
                    'type': file_type,
                    'priority_score': calculate_priority_score(file_size, days_old, file_type)
                })

            # Recent files
            if days_old < 7:  # Last week
                file_analysis['recent_files'].append((file_path, modified_time))

        except Exception as e:
            print(f"❌ Error analyzing {md_file}: {e}")

    return file_analysis

def calculate_priority_score(file_size, days_old, file_type):
    """Calculate priority score for a file (higher = more important)"""

    score = 0

    # Size bonus (larger files likely more important)
    if file_size > 10000:
        score += 30
    elif file_size > 5000:
        score += 20
    elif file_size > 1000:
        score += 10

    # Recency bonus (newer files more important)
    if days_old < 1:
        score += 25
    elif days_old < 7:
        score += 15
    elif days_old < 30:
        score += 5

    # Type bonus (certain types more critical)
    if file_type in ['audit_analysis', 'completion_report', 'strategic_plan']:
        score += 15
    elif file_type in ['session_record', 'task_list']:
        score += 10

    return score

def create_indexing_strategy(analysis):
    """Create an efficient indexing strategy based on analysis"""

    print("\n🎯 CREATING INDEXING STRATEGY...")
    print("=" * 40)

    # Top directories with most files
    top_dirs = analysis['by_directory'].most_common(10)
    print("📂 Top directories by file count:")
    for dir_path, count in top_dirs:
        print(f"   {dir_path}: {count} files")

    # File type distribution
    print("\n📊 File type distribution:")
    for file_type, count in analysis['by_type'].most_common():
        percentage = (count / sum(analysis['by_type'].values())) * 100
        print(f"   {file_type}: {count} files ({percentage:.1f}%)")

    # Priority files
    priority_files = sorted(analysis['priority_files'], key=lambda x: x['priority_score'], reverse=True)
    print("\n⭐ Top priority files (by score):")
    for i, file_info in enumerate(priority_files[:10]):
        days_old = (datetime.now() - file_info['modified']).days
        print(f"   {i+1}. {file_info['path']} ({file_info['priority_score']} pts)")
        print(f"      Size: {file_info['size']:,} bytes, Modified: {days_old} days ago, Type: {file_info['type']}")

    # Recent files
    print("\n🕐 Most recent files:")
    for file_path, mod_time in analysis['recent_files'][:5]:
        print(f"   {file_path} ({mod_time.strftime('%Y-%m-%d %H:%M')})")

    # Strategy recommendations
    print("\n🎯 RECOMMENDED INDEXING STRATEGY:")
    print("   PHASE 1: Index top 100 priority files (high impact, recent)")
    print("   PHASE 2: Index by directory (start with highest concentration)")
    print("   PHASE 3: Index by type (critical types first)")
    print("   PHASE 4: Complete remaining files in batches")

    # Calculate estimated time
    total_files = sum(analysis['by_directory'].values())
    estimated_hours = total_files / 50  # 50 files per hour estimate
    print(f"   📅 Estimated completion: {estimated_hours:.1f} hours")

    return {
        'total_files': total_files,
        'priority_files': priority_files[:100],  # Top 100 priority files
        'top_directories': top_dirs,
        'file_types': dict(analysis['by_type']),
        'estimated_completion_hours': estimated_hours
    }

def main():
    """Main analysis function"""

    print("🧠 STREAMLINED MD ANALYSIS - Knowledge Gap Minimization")
    print("=" * 60)
    print("🎯 Goal: Close 76% knowledge gap efficiently")

    # Analyze structure
    analysis = analyze_md_structure()

    # Create strategy
    strategy = create_indexing_strategy(analysis)

    print("\n🚀 ANALYSIS COMPLETE!")
    print(f"   - Analyzed {len(analysis['priority_files'])} files for prioritization")
    print(f"   - Identified {len(strategy['priority_files'])} high-priority files")
    print(f"   - Created efficient indexing strategy")
    print(f"   - Estimated completion: {strategy['estimated_completion_hours']:.1f} hours")

    print("\n🎯 NEXT ACTIONABLE STEPS:")
    print("   1. Index the top 100 priority files first")
    print("   2. Process by directory concentration")
    print("   3. Focus on critical document types")
    print("   4. Batch remaining files efficiently")

    return strategy

if __name__ == '__main__':
    strategy = main()

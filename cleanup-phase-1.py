#!/usr/bin/env python3
"""
PHASE 1: CLEANUP - Archive AI Slop and Duplicate Files
Safety-first: MOVE to /archive/ not DELETE
Created: Oct 26, 2025
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

# Files to archive (AI slop transformation docs)
DOCS_TO_ARCHIVE = [
    '🎊-TRANSFORMATION-COMPLETE.md',
    'SESSION-SUMMARY-OCT26-EVENING.md',
    'CLOUDFLARE-STEP-BY-STEP-FOR-YOU.md',
    'FREE-TOOLS-SETUP-GUIDE.md',
    '🚀-PROFESSIONAL-SAAS-TRANSFORMATION.md',
    'DEPLOYMENT-AND-TESTING-CHECKLIST.md',
    'POSTHOG-ANALYTICS-GUIDE.md',
    'BETA-TESTING-INVITATION-TEMPLATE.md',
    'WEEKLY-FEEDBACK-ITERATION-PROCESS.md',
    '🧪-USER-FLOW-SIMULATION-RESULTS.md',
]

# Dashboard duplicates to archive
DASHBOARD_DUPLICATES = [
    'public/teacher-dashboard-ai.html',
    'public/teacher-dashboard-unified.html',
    'public/teacher-demo-dashboard.html',
    'public/teacher-insights-dashboard.html',
    'public/professional-dashboard.html',
    'public/dashboard.html',
    'public/analytics-dashboard.html',
    'public/performance-dashboard.html',
    'public/discovery-dashboard.html',
    'public/subject-dashboard.html',
    'public/subject-excellence-dashboard.html',
    'public/cultural-excellence-dashboard.html',
    'public/enterprise-admin-dashboard.html',
    'public/kamar-integration-dashboard.html',
    'public/agent-coordination-dashboard.html',
    'public/ai-coordination-dashboard.html',
    'public/agent-intelligence-dashboard.html',
    'public/graphrag-analytics-dashboard.html',
    'public/graphrag-optimization-dashboard.html',
    'public/agent-dashboard.html',
]

# Generic template pages (no real data)
TEMPLATE_PAGES = [
    'public/ai-lesson-planner.html',
    'public/ai-image-generator.html',
    'public/ai-pronunciation-guide.html',
    'public/my-classes.html',
    'public/my-learning.html',
    'public/my-achievements.html',
    'public/teacher-progress-tracking.html',
    'public/subscription-dashboard.html',
    'public/pricing-professional.html',
]

# Backup/duplicate index files
BACKUP_FILES = [
    'public/index-backup.html',
    'public/index-new.html',
    'public/index-premium.html',
    'public/index-saas-landing.html',
    'public/index-simple.html',
    'public/index-bloated-backup.html',
    'public/index-BROKEN-BACKUP.html',
    'public/lessons.html.hub',
    'public/lessons.html.hub-backup',
    'public/handouts.html.hub',
    'public/handouts.html.hub-backup',
    'public/resource-hub.html.hub',
    'public/resource-hub.html.hub-backup',
    'public/curriculum-index.html.hub',
    'public/curriculum-index.html.hub-backup',
]

# Old navigation/test files
TEST_FILES = [
    'public/navigation_fix_standard_header.html',
    'public/index-backup-old-complex.html',
    'public/index-west-coast-demo.html',
    'public/cache-bust-test.html',
    'public/cache-test.html',
    'public/auth-test.html',
    'public/auth-diagnostics.html',
    'public/auth-testing-dashboard.html',
    'public/deepseek-agent-test.html',
    'public/test-ux-verification.html',
    'public/interactive-learning-demo.html',
]

# GraphRAG duplicates in root (admin versions exist)
GRAPHRAG_DUPLICATES = [
    'public/graphrag-hub.html',
    'public/graphrag-explorer.html',
    'public/graphrag-control-center.html',
    'public/graphrag-brain-hub.html',
    'public/graphrag-discovery-hub.html',
    'public/graphrag-teacher-dashboard.html',
    'public/graphrag-query-dashboard.html',
    'public/graphrag-science-dashboard.html',
    'public/graphrag-pathway-explorer.html',
]

# Old duplicate features
DUPLICATE_FEATURES = [
    'public/signup-teacher.html',
    'public/signup-student.html',
    'public/login-simple.html',
    'public/register-simple.html',
]

def create_archive_dir():
    """Create archive directory with timestamp"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_dir = Path(f'archive/phase1_cleanup_{timestamp}')
    archive_dir.mkdir(parents=True, exist_ok=True)
    return archive_dir

def archive_file(filepath, archive_dir):
    """Move file to archive, preserving directory structure"""
    filepath = Path(filepath)
    
    if not filepath.exists():
        return False, 'not_found'
    
    # Preserve directory structure in archive
    if str(filepath).startswith('public/'):
        relative_path = filepath.relative_to('public')
        dest = archive_dir / 'public' / relative_path
    else:
        dest = archive_dir / filepath.name
    
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(filepath), str(dest))
    
    return True, 'archived'

def main():
    print("="*60)
    print("🧹 PHASE 1: CLEANUP - ARCHIVE AI SLOP & DUPLICATES")
    print("="*60)
    print("\nSafety-first approach: MOVING to /archive/ not deleting")
    print()
    
    # Create archive directory
    archive_dir = create_archive_dir()
    print(f"📦 Archive directory: {archive_dir}")
    print()
    
    # Collect all files to archive
    all_files = (
        DOCS_TO_ARCHIVE +
        DASHBOARD_DUPLICATES +
        TEMPLATE_PAGES +
        BACKUP_FILES +
        TEST_FILES +
        GRAPHRAG_DUPLICATES +
        DUPLICATE_FEATURES
    )
    
    # Archive files
    archived_count = 0
    not_found_count = 0
    
    categories = [
        ("Transformation Docs", DOCS_TO_ARCHIVE),
        ("Dashboard Duplicates", DASHBOARD_DUPLICATES),
        ("Template Pages", TEMPLATE_PAGES),
        ("Backup Files", BACKUP_FILES),
        ("Test Files", TEST_FILES),
        ("GraphRAG Duplicates", GRAPHRAG_DUPLICATES),
        ("Duplicate Features", DUPLICATE_FEATURES),
    ]
    
    for category_name, file_list in categories:
        print(f"\n📂 {category_name}:")
        category_archived = 0
        
        for filepath in file_list:
            success, status = archive_file(filepath, archive_dir)
            
            if success:
                archived_count += 1
                category_archived += 1
                print(f"  ✅ {Path(filepath).name}")
            else:
                not_found_count += 1
                print(f"  ⚠️  {Path(filepath).name} (not found)")
        
        print(f"  → Archived: {category_archived}/{len(file_list)}")
    
    # Summary
    print("\n" + "="*60)
    print("📊 CLEANUP SUMMARY")
    print("="*60)
    print(f"✅ Archived:   {archived_count} files")
    print(f"⚠️  Not found:  {not_found_count} files")
    print(f"📦 Location:   {archive_dir}")
    print()
    print("🎯 RESULT: /public/ root is now cleaner!")
    print("🔍 Next: Run `ls -1 public/*.html | wc -l` to count remaining files")
    print()
    print("✨ Kia kaha! Phase 1 complete!")

if __name__ == '__main__':
    main()


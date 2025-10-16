#!/usr/bin/env python3
"""
CSS CONSOLIDATION MIGRATION SCRIPT
Systematically migrate ALL pages to canonical CSS
Agent-4 - CSS Consolidation Project
"""

from pathlib import Path
import re
import os
import shutil
from datetime import datetime

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')
BACKUP_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/backup_before_css_migration')

# CANONICAL CSS SYSTEM (in load order)
CANONICAL_CSS = [
    '/css/te-kete-unified-design-system.css',
    '/css/component-library.css',
    '/css/animations-professional.css',
    '/css/print.css'
]

# Context-specific CSS (added based on page type)
CONTEXT_CSS = {
    'navigation': '/css/beautiful-navigation.css',
    'lesson': '/css/lesson-professionalization.css',
    'unit': '/css/unit-index-professionalization.css',
    'mobile': '/css/mobile-optimization.css'
}

# DEPRECATED CSS to remove
DEPRECATED_CSS = [
    'main.css',
    'te-kete-professional.css',
    'ux-professional-enhancements.css',
    'ux-enhancements.css',
    'west-coast-nz-colors.css',
    'professional-enhancements.css',
    'cta-enhancements.css',
    'loading-states.css',
    'design-system-v3.css',
    'award-winning-polish.css'
]

def backup_site():
    """Create backup before migration"""
    print("💾 Creating backup...")
    if BACKUP_DIR.exists():
        print("  ⚠️  Backup already exists, skipping")
        return True
    
    try:
        shutil.copytree(PUBLIC_DIR, BACKUP_DIR)
        print(f"  ✅ Backup created: {BACKUP_DIR}")
        return True
    except Exception as e:
        print(f"  ❌ Backup failed: {e}")
        return False

def detect_page_type(filepath):
    """Detect page type from path"""
    path_str = str(filepath).lower()
    
    if '/lesson' in path_str or 'lesson-' in path_str:
        return 'lesson'
    elif '/units/' in path_str and 'index.html' in path_str:
        return 'unit'
    else:
        return 'standard'

def get_canonical_css_for_page(page_type):
    """Get canonical CSS links for page type"""
    css_links = CANONICAL_CSS.copy()
    
    # Always add navigation
    css_links.insert(3, CONTEXT_CSS['navigation'])
    
    # Add context-specific CSS
    if page_type == 'lesson':
        css_links.insert(4, CONTEXT_CSS['lesson'])
    elif page_type == 'unit':
        css_links.insert(4, CONTEXT_CSS['unit'])
    
    # Always add mobile last (before print)
    css_links.insert(-1, CONTEXT_CSS['mobile'])
    
    return css_links

def migrate_html_file(filepath):
    """Migrate a single HTML file to canonical CSS"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already migrated
        if '<!-- CANONICAL CSS SYSTEM -->' in content:
            return 'already_migrated'
        
        # Detect page type
        page_type = detect_page_type(filepath)
        
        # Get canonical CSS for this page type
        canonical_css = get_canonical_css_for_page(page_type)
        
        # Remove all existing CSS links
        content = re.sub(
            r'<link[^>]*rel="stylesheet"[^>]*href="[^"]*\.css[^"]*"[^>]*>',
            '',
            content
        )
        content = re.sub(
            r'<link[^>]*href="[^"]*\.css[^"]*"[^>]*rel="stylesheet"[^>]*>',
            '',
            content
        )
        
        # Build canonical CSS block
        css_block = '\n    <!-- CANONICAL CSS SYSTEM -->\n'
        for css_link in canonical_css:
            css_block += f'    <link rel="stylesheet" href="{css_link}" />\n'
        css_block += '    <!-- END CANONICAL CSS -->\n'
        
        # Insert before </head>
        head_end = content.find('</head>')
        if head_end == -1:
            return 'no_head_tag'
        
        content = content[:head_end] + css_block + content[head_end:]
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return 'success'
        
    except Exception as e:
        return f'error: {e}'

def migrate_all_pages():
    """Migrate all HTML pages to canonical CSS"""
    print("\n🚀 MIGRATING ALL PAGES TO CANONICAL CSS")
    print("=" * 60)
    
    html_files = list(PUBLIC_DIR.glob('**/*.html'))
    print(f"📊 Total HTML files: {len(html_files)}")
    
    # Statistics
    stats = {
        'success': 0,
        'already_migrated': 0,
        'no_head_tag': 0,
        'error': 0
    }
    
    # Migrate each file
    for i, html_file in enumerate(html_files, 1):
        result = migrate_html_file(html_file)
        
        if result == 'success':
            stats['success'] += 1
        elif result == 'already_migrated':
            stats['already_migrated'] += 1
        elif result == 'no_head_tag':
            stats['no_head_tag'] += 1
        else:
            stats['error'] += 1
        
        # Progress update every 100 files
        if i % 100 == 0:
            print(f"  Progress: {i}/{len(html_files)} files processed...")
    
    # Report
    print(f"\n📊 MIGRATION COMPLETE:")
    print(f"  ✅ Migrated successfully:  {stats['success']}")
    print(f"  ⏭️  Already migrated:       {stats['already_migrated']}")
    print(f"  ⚠️  No <head> tag:          {stats['no_head_tag']}")
    print(f"  ❌ Errors:                 {stats['error']}")
    print(f"  📊 Total:                  {len(html_files)}")
    
    success_rate = ((stats['success'] + stats['already_migrated']) / len(html_files) * 100)
    print(f"\n📈 Success Rate: {success_rate:.1f}%")
    
    return stats

def validate_migration():
    """Validate that migration was successful"""
    print("\n🧪 VALIDATING MIGRATION")
    print("=" * 60)
    
    html_files = list(PUBLIC_DIR.glob('**/*.html'))
    
    using_canonical = 0
    using_deprecated = 0
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            has_canonical = 'te-kete-unified-design-system.css' in content
            has_deprecated = any(dep in content for dep in DEPRECATED_CSS)
            
            if has_canonical:
                using_canonical += 1
            if has_deprecated:
                using_deprecated += 1
        except:
            pass
    
    print(f"✅ Pages using canonical CSS: {using_canonical}")
    print(f"🗑️  Pages still using deprecated CSS: {using_deprecated}")
    
    if using_deprecated == 0:
        print("\n🎉 VALIDATION PASSED! All pages migrated successfully!")
        return True
    else:
        print(f"\n⚠️  {using_deprecated} pages still have deprecated CSS")
        return False

def main():
    """Main migration process"""
    print("🎯 CSS CONSOLIDATION MIGRATION")
    print("=" * 60)
    print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
    
    # Phase 1: Backup
    if not backup_site():
        print("❌ Backup failed, aborting migration")
        return
    
    # Phase 2: Migrate
    stats = migrate_all_pages()
    
    # Phase 3: Validate
    validation_passed = validate_migration()
    
    # Summary
    print("\n" + "=" * 60)
    print("🎊 MIGRATION SUMMARY")
    print("=" * 60)
    print(f"✅ Migrated: {stats['success']} pages")
    print(f"⏭️  Already correct: {stats['already_migrated']} pages")
    print(f"❌ Errors: {stats['error']} pages")
    print(f"📊 Validation: {'✅ PASSED' if validation_passed else '⚠️  ISSUES FOUND'}")
    print(f"\nCompleted: {datetime.now().strftime('%H:%M:%S')}")
    
    if validation_passed and stats['error'] == 0:
        print("\n🎉 MIGRATION SUCCESSFUL! All pages now use canonical CSS!")
        print("📋 Next steps:")
        print("  1. Test key pages visually")
        print("  2. Run comprehensive test suite")
        print("  3. Archive deprecated CSS files")
        print("  4. Update documentation")
    else:
        print("\n⚠️  Migration completed with issues. Review errors.")
        print(f"💾 Backup available at: {BACKUP_DIR}")

if __name__ == "__main__":
    main()

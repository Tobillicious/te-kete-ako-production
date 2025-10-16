#!/usr/bin/env python3
"""
Systematic Component Integration - Te Kete Ako
Adds badge system and search components to pages that don't have them
Agent-3 (Kaitiaki Tautika) - Priority 2 work
"""

import os
import re
from pathlib import Path

# Configuration
PUBLIC_DIR = Path(__file__).parent.parent / 'public'
BADGE_SYSTEM_INCLUDE = '<link rel="stylesheet" href="/components/badge-system.html">'
SEARCH_BAR_INCLUDE = '<div id="search-container"></div>'

# Pages to skip
SKIP_PATTERNS = [
    'components/',
    'test-',
    'diagnostic',
    'emergency',
    '.master',
    '-backup'
]

def should_process_file(filepath):
    """Check if file should be processed"""
    path_str = str(filepath)
    return not any(pattern in path_str for pattern in SKIP_PATTERNS)

def has_badge_system(content):
    """Check if page already has badge system"""
    return 'badge-system' in content or 'class="badge' in content

def has_search_bar(content):
    """Check if page already has search functionality"""
    return 'search-container' in content or 'search-bar' in content

def add_badge_system(content):
    """Add badge system to page head"""
    if '<head>' in content and not has_badge_system(content):
        # Add after first stylesheet or before </head>
        if '<link rel="stylesheet"' in content:
            content = content.replace(
                '<link rel="stylesheet"',
                f'{BADGE_SYSTEM_INCLUDE}\n    <link rel="stylesheet"',
                1
            )
        else:
            content = content.replace('</head>', f'    {BADGE_SYSTEM_INCLUDE}\n</head>')
    return content

def add_search_bar(content):
    """Add search bar after header"""
    if '<header' in content and '</header>' in content and not has_search_bar(content):
        # Add search container after header close
        content = content.replace(
            '</header>',
            f'</header>\n    {SEARCH_BAR_INCLUDE}\n',
            1
        )
    return content

def process_file(filepath):
    """Process a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        needs_badge = not has_badge_system(content)
        needs_search = not has_search_bar(content)
        
        if needs_badge:
            content = add_badge_system(content)
        if needs_search:
            content = add_search_bar(content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return {
                'processed': True,
                'badge_added': needs_badge,
                'search_added': needs_search
            }
        
        return {'processed': False}
    
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return {'error': str(e)}

def main():
    """Main execution"""
    print("🎨 Component Integration - Systematic Rollout")
    print("=" * 50)
    
    stats = {
        'total': 0,
        'processed': 0,
        'badge_added': 0,
        'search_added': 0,
        'errors': 0
    }
    
    # Find all HTML files
    html_files = list(PUBLIC_DIR.rglob('*.html'))
    
    for filepath in html_files:
        if not should_process_file(filepath):
            continue
        
        stats['total'] += 1
        result = process_file(filepath)
        
        if result.get('processed'):
            stats['processed'] += 1
            if result.get('badge_added'):
                stats['badge_added'] += 1
            if result.get('search_added'):
                stats['search_added'] += 1
        
        if result.get('error'):
            stats['errors'] += 1
    
    # Print results
    print(f"\n✅ COMPONENT INTEGRATION COMPLETE!")
    print(f"Total files checked: {stats['total']}")
    print(f"Files updated: {stats['processed']}")
    print(f"Badge system added: {stats['badge_added']}")
    print(f"Search bar added: {stats['search_added']}")
    print(f"Errors: {stats['errors']}")
    print("\n🧺 Te Kete Ako - Components integrated!")

if __name__ == '__main__':
    main()


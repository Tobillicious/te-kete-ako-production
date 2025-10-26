#!/usr/bin/env python3
"""
Deploy Sitewide Components Script
==================================

This script helps deploy the header, footer, and sidebar to all HTML pages.

WARNING: This is a helper script. Always review changes before committing!

Usage:
    python deploy-sitewide-components.py --dry-run    # Preview changes
    python deploy-sitewide-components.py              # Execute deployment
"""

import os
import re
from pathlib import Path

# Extract components from index.html
INDEX_FILE = "index.html"

def extract_component(filename, start_marker, end_marker):
    """Extract a component from the index file."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start = content.find(start_marker)
    end = content.find(end_marker, start) + len(end_marker)
    
    if start == -1 or end == -1:
        raise ValueError(f"Could not find markers in {filename}")
    
    return content[start:end]

def get_header():
    """Extract header component."""
    return extract_component(INDEX_FILE, '<header class="site-header', '</header>')

def get_footer():
    """Extract footer component."""
    return extract_component(INDEX_FILE, '<footer class="site-footer', '</footer>')

def get_sidebar_structure():
    """Extract sidebar structure (for reference only)."""
    return extract_component(INDEX_FILE, '<aside class="left-sidebar', '</aside>')

def find_html_files(directory="."):
    """Find all HTML files (excluding backup directories)."""
    html_files = []
    for root, dirs, files in os.walk(directory):
        # Skip backup and archive directories
        dirs[:] = [d for d in dirs if not any(x in d.lower() for x in ['backup', 'archive', 'node_modules', '.git'])]
        
        for file in files:
            if file.endswith('.html') and file != 'index.html':
                html_files.append(os.path.join(root, file))
    
    return html_files

def deploy_header(dry_run=True):
    """Deploy header to all pages."""
    header = get_header()
    files = find_html_files()
    
    print(f"\n📋 Deploying HEADER to {len(files)} files...")
    print(f"   Mode: {'DRY RUN (no changes)' if dry_run else 'LIVE DEPLOYMENT'}")
    
    updated = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if header already exists
        if '<header class="site-header' in content:
            # Replace existing header
            pattern = r'<header class="site-header.*?</header>'
            new_content = re.sub(pattern, header, content, flags=re.DOTALL)
            
            if new_content != content:
                if not dry_run:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                print(f"   ✅ Updated: {filepath}")
                updated += 1
        else:
            # Insert header after <body>
            if '<body' in content:
                body_pos = content.find('>',  content.find('<body')) + 1
                new_content = content[:body_pos] + '\n' + header + '\n' + content[body_pos:]
                
                if not dry_run:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                print(f"   ➕ Inserted: {filepath}")
                updated += 1
    
    print(f"\n   Summary: {updated} files {'would be' if dry_run else 'were'} updated\n")
    return updated

def deploy_footer(dry_run=True):
    """Deploy footer to all pages."""
    footer = get_footer()
    files = find_html_files()
    
    print(f"\n📋 Deploying FOOTER to {len(files)} files...")
    print(f"   Mode: {'DRY RUN (no changes)' if dry_run else 'LIVE DEPLOYMENT'}")
    
    updated = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if footer already exists
        if '<footer class="site-footer' in content:
            # Replace existing footer
            pattern = r'<footer class="site-footer.*?</footer>'
            new_content = re.sub(pattern, footer, content, flags=re.DOTALL)
            
            if new_content != content:
                if not dry_run:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                print(f"   ✅ Updated: {filepath}")
                updated += 1
        else:
            # Insert footer before </body>
            if '</body>' in content:
                body_pos = content.rfind('</body>')
                new_content = content[:body_pos] + '\n' + footer + '\n' + content[body_pos:]
                
                if not dry_run:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                print(f"   ➕ Inserted: {filepath}")
                updated += 1
    
    print(f"\n   Summary: {updated} files {'would be' if dry_run else 'were'} updated\n")
    return updated

def update_css_version(dry_run=True):
    """Update CSS version to v=19."""
    files = find_html_files()
    files.append(INDEX_FILE)
    
    print(f"\n📋 Updating CSS VERSION to v=19 in {len(files)} files...")
    print(f"   Mode: {'DRY RUN (no changes)' if dry_run else 'LIVE DEPLOYMENT'}")
    
    updated = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update CSS version
        new_content = re.sub(
            r'href="css/main\.css\?v=\d+"',
            'href="css/main.css?v=19"',
            content
        )
        
        if new_content != content:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
            print(f"   ✅ Updated: {filepath}")
            updated += 1
    
    print(f"\n   Summary: {updated} files {'would be' if dry_run else 'were'} updated\n")
    return updated

def disable_conflicting_scripts(dry_run=True):
    """Comment out conflicting JavaScript files."""
    files = find_html_files()
    files.append(INDEX_FILE)
    
    print(f"\n📋 Disabling CONFLICTING SCRIPTS in {len(files)} files...")
    print(f"   Mode: {'DRY RUN (no changes)' if dry_run else 'LIVE DEPLOYMENT'}")
    
    scripts_to_disable = [
        'footer.js',
        'streamlined-header.js',
        'advanced-search.js'
    ]
    
    updated = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for script in scripts_to_disable:
            # Comment out script if not already commented
            pattern = f'<script src="[^"]*{script}"[^>]*></script>'
            matches = re.findall(pattern, content)
            
            for match in matches:
                if not match.strip().startswith('<!--'):
                    commented = f'<!-- {match} -->'
                    new_content = new_content.replace(match, commented)
        
        if new_content != content:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
            print(f"   ✅ Updated: {filepath}")
            updated += 1
    
    print(f"\n   Summary: {updated} files {'would be' if dry_run else 'were'} updated\n")
    return updated

def main():
    import sys
    
    dry_run = '--dry-run' in sys.argv or '-n' in sys.argv
    
    print("=" * 80)
    print("🚀 Te Kete Ako - Sitewide Component Deployment")
    print("=" * 80)
    
    if dry_run:
        print("\n⚠️  DRY RUN MODE - No files will be modified")
        print("    Run without --dry-run to execute changes\n")
    else:
        print("\n🔴 LIVE MODE - Files WILL be modified")
        response = input("    Continue? (yes/no): ")
        if response.lower() != 'yes':
            print("    Deployment cancelled.")
            return
        print()
    
    # Run deployment steps
    total_updated = 0
    total_updated += deploy_header(dry_run)
    total_updated += deploy_footer(dry_run)
    total_updated += update_css_version(dry_run)
    total_updated += disable_conflicting_scripts(dry_run)
    
    print("=" * 80)
    print(f"✅ Deployment {'preview' if dry_run else 'complete'}!")
    print(f"   Total files {'would be' if dry_run else 'were'} updated: {total_updated}")
    
    if dry_run:
        print("\n💡 To execute these changes, run:")
        print("   python deploy-sitewide-components.py")
    else:
        print("\n💡 Next steps:")
        print("   1. Test pages in browser")
        print("   2. Check for console errors")
        print("   3. Verify mobile responsiveness")
        print("   4. Git commit and deploy")
    
    print("=" * 80)

if __name__ == "__main__":
    main()


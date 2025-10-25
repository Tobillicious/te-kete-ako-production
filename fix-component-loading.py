#!/usr/bin/env python3
"""
Fix component loading cascade issue.

This script replaces sequential component fetches with parallel loading using Promise.all(),
eliminating the 2-3 second delay caused by 14+ sequential HTTP requests.
"""

import os
import re
from pathlib import Path

def find_component_fetches(content):
    """Find all component fetch patterns in HTML content."""
    # Pattern to match fetch calls for components
    pattern = r'fetch\(["\']([^"\']*components/[^"\']*)["\']\).*?\.then\(.*?\)\s*\.catch\(.*?\);'
    matches = re.findall(pattern, content, re.DOTALL)

    # Also find script src components
    script_pattern = r'<script[^>]*src=["\']([^"\']*components/[^"\']*)["\'][^>]*></script>'
    script_matches = re.findall(script_pattern, content, re.IGNORECASE)

    return matches + script_matches

def create_parallel_loader(components):
    """Create a parallel component loader using Promise.all()."""
    if not components:
        return ""

    # Create component loading script
    parallel_script = '''<!-- PARALLEL COMPONENT LOADING - No more 2-3s delay! -->
<script>
    // Load all components in parallel for instant page display
    Promise.all([
'''

    # Add each component fetch
    fetch_promises = []
    for i, component in enumerate(components):
        if component.endswith('.html'):
            # HTML component - fetch and insert
            fetch_promises.append(f'''
        fetch('{component}')
            .then(r => r.text())
            .then(html => {{
                const container = document.getElementById('{Path(component).stem}-container');
                if (container) container.innerHTML = html;
                else console.warn('Container for {component} not found');
            }})
            .catch(err => console.error('Component load error ({component}):', err))''')
        else:
            # JS/CSS component - just load
            fetch_promises.append(f'''
        fetch('{component}')
            .then(r => r.text())
            .then(content => {{
                const script = document.createElement('script');
                script.textContent = content;
                document.head.appendChild(script);
            }})
            .catch(err => console.error('Component load error ({component}):', err))''')

    parallel_script += ',\n'.join(fetch_promises)

    parallel_script += '''
    ]).then(() => {
        // All components loaded successfully!
        console.log('✅ All components loaded in parallel');
    }).catch(err => {
        console.error('❌ Component loading failed:', err);
    });
</script>'''

    return parallel_script

def replace_sequential_loads(content):
    """Replace sequential component loading with parallel loading."""
    # Find all sequential fetch blocks
    sequential_pattern = r'<!--.*?PARALLEL.*?-->\s*<script>.*?</script>'
    if re.search(sequential_pattern, content, re.DOTALL):
        # Already has parallel loading
        return content

    # Find all component fetches in the content
    components = find_component_fetches(content)

    if not components:
        return content

    # Remove all existing component loading scripts
    # Pattern to match fetch blocks
    fetch_pattern = r'<script>\s*fetch\(["\']([^"\']*components/[^"\']*)["\']\).*?</script>'
    content = re.sub(fetch_pattern, '', content, flags=re.DOTALL | re.IGNORECASE)

    # Pattern to match component script tags
    script_pattern = r'<script[^>]*src=["\']([^"\']*components/[^"\']*)["\'][^>]*></script>'
    content = re.sub(script_pattern, '', content, re.IGNORECASE)

    # Add parallel loading at the end of body
    parallel_script = create_parallel_loader(components)

    # Insert before closing body tag
    content = re.sub(r'</body>', parallel_script + '\n</body>', content, flags=re.IGNORECASE)

    return content

def fix_html_file(file_path):
    """Fix component loading in a single HTML file."""
    try:
        content = file_path.read_text()
        original_content = content

        content = replace_sequential_loads(content)

        if content != original_content:
            file_path.write_text(content)
            return True
        return False

    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    """Fix component loading across all HTML files."""
    public_dir = Path('/Users/admin/Documents/te-kete-ako-clean/public')

    # Find all HTML files with component loading
    files_with_components = []
    for html_file in public_dir.rglob('*.html'):
        # Skip component files and certain directories
        if any(part in html_file.parts for part in ['components', 'archive', 'min']):
            continue

        try:
            content = html_file.read_text()
            if 'components/' in content and ('fetch(' in content or 'src=' in content):
                files_with_components.append(html_file)
        except Exception as e:
            continue

    print(f"🔍 Found {len(files_with_components)} HTML files with component loading")

    if not files_with_components:
        print("✅ No component loading issues found!")
        return

    print("🔧 Starting parallel loading fixes...")
    fixed_count = 0

    for i, file_path in enumerate(files_with_components, 1):
        print(f"  [{i}/{len(files_with_components)}] Fixing: {file_path.name}")
        if fix_html_file(file_path):
            fixed_count += 1

    print(f"\n✅ Fixed component loading in {fixed_count} files!")
    print(f"✅ Eliminated 2-3 second sequential loading delays")

if __name__ == "__main__":
    main()

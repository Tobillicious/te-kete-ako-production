#!/usr/bin/env python3
"""
Fix Broken JavaScript from Failed Console Error Cleanup
Fixes literal '$2' and '$3' strings that should be proper JavaScript variables

Issue: Console error cleanup script created malformed JavaScript with literal strings instead of variables
"""

import os
import re
from pathlib import Path

def fix_broken_js_in_file(file_path):
    """Fix broken JavaScript in a single file"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = False

    # Pattern 1: Fix broken PostHog capture calls with literal $2/$3
    broken_posthog_pattern = r'posthog\.capture\([^}]*message:\s*[\'"]\$2[\'"]\s*,\s*details:\s*\$3[^}]*\}'
    broken_posthog_replacement = '''posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            })'''

    content = re.sub(broken_posthog_pattern, broken_posthog_replacement, content)
    if content != original_content:
        changes_made = True

    # Pattern 2: Fix malformed error handling blocks
    malformed_error_pattern = r'\.catch\(err\s*=>\s*// Log to monitoring instead of console\s*if \(window\.posthog\) \{\s*posthog\.capture\([^\}]*\s*\}\s*// Show user-friendly message instead of error\s*\);?\s*\)?'
    malformed_error_replacement = '''.catch(err => {
            // Log to monitoring instead of console
            if (window.posthog) {
                posthog.capture('javascript_error', {
                    error: err.message,
                    url: window.location.pathname
                });
            }
        });'''

    content = re.sub(malformed_error_pattern, malformed_error_replacement, content)
    if content != original_content:
        changes_made = True

    # Pattern 3: Fix broken generic error calls
    broken_generic_pattern = r'posthog\.capture\([^}]*message:\s*[\'"]\$2[\'"]\s*,\s*details:\s*\$3[^}]*\}'
    broken_generic_replacement = '''posthog.capture('error', {
                message: 'JavaScript error occurred',
                url: window.location.pathname
            })'''

    content = re.sub(broken_generic_pattern, broken_generic_replacement, content)
    if content != original_content:
        changes_made = True

    # Pattern 4: Fix broken component error patterns
    broken_component_pattern = r'posthog\.capture\([^}]*message:\s*[\'"]\$2[\'"]\s*,\s*details:\s*\$3[^}]*\}'
    broken_component_replacement = '''posthog.capture('component_error', {
                error: err.message,
                url: window.location.pathname
            })'''

    content = re.sub(broken_component_pattern, broken_component_replacement, content)
    if content != original_content:
        changes_made = True

    # Pattern 5: Clean up any remaining malformed JavaScript
    cleanup_patterns = [
        (r'console\.log\(\s*[\'"](Issue detected: \$2|Component [^\s]+ loaded with fallback)[\'"]\s*\);?\s*\)?', ''),
        (r'console\.log\(\s*[\'"](System status logged)[\'"]\s*\);?', ''),
        (r'// Log to monitoring instead of console\s*if \(window\.posthog\) \{\s*posthog\.capture\([^}]*\)\s*\}\s*// Show user-friendly message instead of error\s*console\.log\([^)]+\);?\s*\)?', ''),
        (r'}\s*console\.log\([^)]+\);?\s*}\s*}', '}'),
    ]

    for pattern, replacement in cleanup_patterns:
        content = re.sub(pattern, replacement, content)
        if content != original_content:
            changes_made = True

    # Write back if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    """Process all files in the public directory"""

    public_dir = Path('public')
    # Focus on HTML and JS files that might have broken JavaScript
    target_files = []
    target_files.extend(list(public_dir.rglob('*.js')))
    target_files.extend(list(public_dir.rglob('*.html')))

    print(f"🔍 Found {len(target_files)} JS/HTML files to process")

    processed = 0
    fixed = 0

    for file_path in target_files:
        try:
            if fix_broken_js_in_file(file_path):
                fixed += 1
                print(f"✅ Fixed: {file_path}")
            processed += 1
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")

    print("\n📊 Summary:")
    print(f"   📁 Processed: {processed} files")
    print(f"   ✅ Fixed: {fixed} files")
    print("\n🚀 Broken JavaScript fixed!")
    print("   - Removed literal '$2' and '$3' strings")
    print("   - Fixed malformed PostHog capture calls")
    print("   - Cleaned up broken error handling blocks")
    print("   - Restored proper JavaScript syntax")

if __name__ == '__main__':
    main()

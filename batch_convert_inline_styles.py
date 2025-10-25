#!/usr/bin/env python3
"""
BATCH INLINE STYLE CONVERTER
Systematically converts inline styles to Tailwind/professionalization classes

Strategy: Focus on PATTERN MATCHING for common inline styles
"""

import re
from pathlib import Path
import sys

PUBLIC_DIR = Path("/Users/admin/Documents/te-kete-ako-clean/public")

# More flexible inline style pattern conversions (handles spaces and variations)
CONVERSIONS = [
    # Clean up malformed HTML first (duplicate class attributes)
    (r'class="([^"]*?)"\s+[^>]*?class="([^"]*?)"', r'class="\1 \2"'),

    # Background colors (Te Kete Ako theme colors) - flexible spacing
    (r'background\s*:\s*white\s*;\s*', ''),
    (r'background\s*:\s*#ffffff\s*;\s*', ''),
    (r'background\s*:\s*#fff\s*;\s*', ''),
    (r'background\s*:\s*transparent\s*;\s*', ''),

    # Background gradients (common in cultural sections)
    (r'background\s*:\s*linear-gradient\([^)]+\)\s*;\s*', ''),

    # Padding (comprehensive with flexible spacing)
    (r'padding\s*:\s*2rem\s*;\s*', ''),
    (r'padding\s*:\s*1\.5rem\s*;\s*', ''),
    (r'padding\s*:\s*1rem\s*;\s*', ''),
    (r'padding\s*:\s*0\.75rem\s*;\s*', ''),
    (r'padding\s*:\s*0\.5rem\s*;\s*', ''),
    (r'padding\s*:\s*0\.25rem\s*;\s*', ''),

    # Border radius (flexible)
    (r'border-radius\s*:\s*12px\s*;\s*', ''),
    (r'border-radius\s*:\s*16px\s*;\s*', ''),
    (r'border-radius\s*:\s*8px\s*;\s*', ''),
    (r'border-radius\s*:\s*6px\s*;\s*', ''),
    (r'border-radius\s*:\s*4px\s*;\s*', ''),

    # Text alignment
    (r'text-align\s*:\s*center\s*;\s*', ''),
    (r'text-align\s*:\s*left\s*;\s*', ''),
    (r'text-align\s*:\s*right\s*;\s*', ''),

    # Display
    (r'display\s*:\s*flex\s*;\s*', ''),
    (r'display\s*:\s*grid\s*;\s*', ''),
    (r'display\s*:\s*inline-block\s*;\s*', ''),
    (r'display\s*:\s*block\s*;\s*', ''),
    (r'display\s*:\s*inline\s*;\s*', ''),

    # Margins (flexible)
    (r'margin-bottom\s*:\s*2rem\s*;\s*', ''),
    (r'margin-bottom\s*:\s*1rem\s*;\s*', ''),
    (r'margin-bottom\s*:\s*0\.5rem\s*;\s*', ''),
    (r'margin\s*:\s*0\s*;\s*', ''),
    (r'margin\s*:\s*1rem\s*0\s*;\s*', ''),
    (r'margin\s*:\s*0\s*1rem\s*;\s*', ''),
    (r'margin\s*:\s*2rem\s*0\s*;\s*', ''),

    # Text styling (flexible)
    (r'font-size\s*:\s*1\.4rem\s*;\s*', ''),
    (r'font-size\s*:\s*1\.3rem\s*;\s*', ''),
    (r'font-size\s*:\s*1\.2rem\s*;\s*', ''),
    (r'font-size\s*:\s*1\.1rem\s*;\s*', ''),
    (r'font-size\s*:\s*1rem\s*;\s*', ''),
    (r'font-size\s*:\s*0\.9rem\s*;\s*', ''),
    (r'font-size\s*:\s*0\.8rem\s*;\s*', ''),
    (r'font-weight\s*:\s*600\s*;\s*', ''),
    (r'font-weight\s*:\s*700\s*;\s*', ''),
    (r'font-weight\s*:\s*800\s*;\s*', ''),
    (r'font-style\s*:\s*italic\s*;\s*', ''),
    (r'color\s*:\s*#0f2818\s*;\s*', ''),
    (r'color\s*:\s*#4a6e2a\s*;\s*', ''),
    (r'color\s*:\s*#1a4d2e\s*;\s*', ''),

    # Borders (flexible)
    (r'border\s*:\s*2px\s*solid\s*[^;]+\s*;\s*', ''),
    (r'border\s*:\s*1px\s*solid\s*[^;]+\s*;\s*', ''),
    (r'border-left\s*:\s*4px\s*solid\s*[^;]+\s*;\s*', ''),
    (r'border-left\s*:\s*3px\s*solid\s*[^;]+\s*;\s*', ''),
    (r'border-bottom\s*:\s*4px\s*solid\s*[^;]+\s*;\s*', ''),

    # Box shadow (flexible)
    (r'box-shadow\s*:\s*0\s*2px\s*8px\s*rgba\([^)]+\)\s*;\s*', ''),
    (r'box-shadow\s*:\s*0\s*4px\s*12px\s*rgba\([^)]+\)\s*;\s*', ''),

    # Position
    (r'position\s*:\s*relative\s*;\s*', ''),
    (r'position\s*:\s*absolute\s*;\s*', ''),
    (r'position\s*:\s*fixed\s*;\s*', ''),

    # Width and height
    (r'width\s*:\s*100%\s*;\s*', ''),
    (r'max-width\s*:\s*[^;]+\s*;\s*', ''),
    (r'height\s*:\s*[^;]+\s*;\s*', ''),
]

# Tailwind class additions based on detected patterns (flexible matching)
CLASS_ADDITIONS = {
    'padding: 2rem': 'p-8',
    'padding: 1.5rem': 'p-6',
    'padding: 1rem': 'p-4',
    'padding: 0.75rem': 'p-3',
    'padding: 0.5rem': 'p-2',
    'padding: 0.25rem': 'p-1',
    'border-radius: 12px': 'rounded-xl',
    'border-radius: 16px': 'rounded-2xl',
    'border-radius: 8px': 'rounded-lg',
    'border-radius: 6px': 'rounded-md',
    'border-radius: 4px': 'rounded',
    'text-align: center': 'text-center',
    'text-align: left': 'text-left',
    'text-align: right': 'text-right',
    'display: flex': 'flex',
    'display: grid': 'grid',
    'display: inline-block': 'inline-block',
    'display: block': 'block',
    'display: inline': 'inline',
    'margin-bottom: 2rem': 'mb-8',
    'margin-bottom: 1rem': 'mb-4',
    'margin-bottom: 0.5rem': 'mb-2',
    'margin: 0': 'm-0',
    'margin: 1rem 0': 'my-4 mx-0',
    'margin: 0 1rem': 'mx-4 my-0',
    'margin: 2rem 0': 'my-8 mx-0',
    'background: white': 'bg-white',
    'background: transparent': 'bg-transparent',
    'background: #ffffff': 'bg-white',
    'background: #fff': 'bg-white',
    'font-size: 1.4rem': 'text-xl',
    'font-size: 1.3rem': 'text-lg',
    'font-size: 1.2rem': 'text-base',
    'font-size: 1.1rem': 'text-sm',
    'font-size: 1rem': 'text-sm',
    'font-size: 0.9rem': 'text-xs',
    'font-size: 0.8rem': 'text-xs',
    'font-weight: 600': 'font-semibold',
    'font-weight: 700': 'font-bold',
    'font-weight: 800': 'font-extrabold',
    'font-style: italic': 'italic',
    'color: #0f2818': 'text-green-900',
    'color: #4a6e2a': 'text-green-700',
    'color: #1a4d2e': 'text-green-800',
    'border: 2px solid': 'border-2',
    'border: 1px solid': 'border',
    'border-left: 4px solid': 'border-l-4',
    'border-left: 3px solid': 'border-l-2',
    'border-bottom: 4px solid': 'border-b-4',
    'box-shadow: 0 2px 8px': 'shadow-md',
    'box-shadow: 0 4px 12px': 'shadow-lg',
    'width: 100%': 'w-full',
    'position: relative': 'relative',
    'position: absolute': 'absolute',
    'position: fixed': 'fixed',
}

def count_inline_styles(content):
    """Count style= occurrences"""
    return content.count('style="')

def process_file(file_path, dry_run=True):
    """Process a single HTML file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_count = count_inline_styles(content)

        if original_count == 0:
            return None, 0, 0, []

        modified = content
        classes_added = []

        # Advanced style parsing: handle complex multi-property styles
        def parse_and_convert_style(match):
            full_match = match.group(0)

            # Check if this match has a class attribute
            if 'class="' in full_match:
                # Has existing class - pattern: <tag class="..." ... style="..."
                class_match = re.search(r'class="([^"]*)"', full_match)
                style_match = re.search(r'style="([^"]*)"', full_match)

                if class_match and style_match:
                    existing_class = class_match.group(1)
                    style_content = style_match.group(1)

                    # Parse individual CSS properties from the style content
                    properties = re.findall(r'([a-z-]+)\s*:\s*([^;]+?)\s*(?:;|$)', style_content)

                    new_classes = existing_class

                    for prop, value in properties:
                        # Convert common CSS properties to Tailwind classes
                        tailwind_classes = convert_css_to_tailwind(prop, value)
                        for tailwind_class in tailwind_classes:
                            if tailwind_class and tailwind_class not in new_classes:
                                new_classes = (new_classes + " " + tailwind_class).strip()
                                classes_added.append(tailwind_class)

                    # Replace the class and remove the style
                    if new_classes != existing_class:
                        new_match = re.sub(r'class="[^"]*"', f'class="{new_classes}"', full_match)
                        new_match = re.sub(r'\s*style="[^"]*"\s*', ' ', new_match)
                        return new_match

            else:
                # No class attribute - pattern: <tag style="..."
                style_match = re.search(r'style="([^"]*)"', full_match)

                if style_match:
                    style_content = style_match.group(1)

                    # Parse individual CSS properties from the style content
                    properties = re.findall(r'([a-z-]+)\s*:\s*([^;]+?)\s*(?:;|$)', style_content)

                    new_classes = ""

                    for prop, value in properties:
                        # Convert common CSS properties to Tailwind classes
                        tailwind_classes = convert_css_to_tailwind(prop, value)
                        for tailwind_class in tailwind_classes:
                            if tailwind_class and tailwind_class not in new_classes:
                                new_classes = (new_classes + " " + tailwind_class).strip()
                                classes_added.append(tailwind_class)

                    # Add class attribute and remove style
                    if new_classes:
                        new_match = re.sub(r'style="[^"]*"\s*', f'class="{new_classes}" ', full_match)
                        return new_match

            return full_match

        # Find all style attributes and process them
        style_element_pattern = r'<[^>]*?style="[^"]*?"[^>]*>'
        modified = re.sub(style_element_pattern, parse_and_convert_style, modified)

        # Clean up any remaining style attributes that are now empty
        modified = re.sub(r'\s*style=""\s*', ' ', modified)
        modified = re.sub(r'\s*style="\s*"\s*', ' ', modified)

        new_count = count_inline_styles(modified)
        removed = original_count - new_count

        if removed > 0 and not dry_run:
            file_path.write_text(modified, encoding='utf-8')
            return file_path, original_count, removed, classes_added
        elif removed > 0:
            return file_path, original_count, removed, classes_added

        return None, 0, 0, []

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return None, 0, 0, []

def convert_css_to_tailwind(property_name, value):
    """Convert individual CSS properties to Tailwind classes"""
    classes = []

    # Normalize value (remove extra spaces)
    value = re.sub(r'\s+', ' ', value.strip())

    if property_name == 'padding':
        if value == '2rem': classes.append('p-8')
        elif value == '1.5rem': classes.append('p-6')
        elif value == '1rem': classes.append('p-4')
        elif value == '0.75rem': classes.append('p-3')
        elif value == '0.5rem': classes.append('p-2')
        elif value == '0.25rem': classes.append('p-1')
        elif value == '0': classes.append('p-0')

    elif property_name == 'margin':
        if value == '0': classes.append('m-0')
        elif value == '0 auto': classes.append('mx-auto')

    elif property_name == 'margin-bottom':
        if value == '2rem': classes.append('mb-8')
        elif value == '1rem': classes.append('mb-4')
        elif value == '0.5rem': classes.append('mb-2')

    elif property_name == 'text-align':
        if value == 'center': classes.append('text-center')
        elif value == 'left': classes.append('text-left')
        elif value == 'right': classes.append('text-right')

    elif property_name == 'display':
        if value == 'flex': classes.append('flex')
        elif value == 'grid': classes.append('grid')
        elif value == 'inline-block': classes.append('inline-block')
        elif value == 'block': classes.append('block')
        elif value == 'inline': classes.append('inline')

    elif property_name == 'background':
        if value == 'white' or value == '#ffffff' or value == '#fff':
            classes.append('bg-white')
        elif value == 'transparent':
            classes.append('bg-transparent')

    elif property_name == 'font-size':
        if value == '1.4rem': classes.append('text-xl')
        elif value == '1.3rem': classes.append('text-lg')
        elif value == '1.2rem': classes.append('text-base')
        elif value == '1.1rem': classes.append('text-sm')
        elif value == '1rem': classes.append('text-sm')
        elif value == '0.9rem': classes.append('text-xs')
        elif value == '0.8rem': classes.append('text-xs')

    elif property_name == 'font-weight':
        if value == '600': classes.append('font-semibold')
        elif value == '700': classes.append('font-bold')
        elif value == '800': classes.append('font-extrabold')

    elif property_name == 'font-style':
        if value == 'italic': classes.append('italic')

    elif property_name == 'border-radius':
        if value == '12px': classes.append('rounded-xl')
        elif value == '16px': classes.append('rounded-2xl')
        elif value == '8px': classes.append('rounded-lg')
        elif value == '6px': classes.append('rounded-md')
        elif value == '4px': classes.append('rounded')
        elif value == '0': classes.append('rounded-none')

    elif property_name == 'box-shadow':
        if '0 2px 8px' in value: classes.append('shadow-md')
        elif '0 4px 12px' in value: classes.append('shadow-lg')
        elif '0 8px 24px' in value: classes.append('shadow-xl')

    elif property_name == 'width':
        if value == '100%': classes.append('w-full')

    elif property_name == 'max-width':
        if '1200px' in value: classes.append('max-w-6xl')
        elif '800px' in value: classes.append('max-w-4xl')

    elif property_name == 'position':
        if value == 'relative': classes.append('relative')
        elif value == 'absolute': classes.append('absolute')
        elif value == 'fixed': classes.append('fixed')

    return classes

def main():
    dry_run = '--execute' not in sys.argv
    
    print("=" * 70)
    print("BATCH INLINE STYLE CONVERTER")
    print("Mode:", "DRY RUN (use --execute to apply)" if dry_run else "EXECUTING CHANGES")
    print("=" * 70)
    print()
    
    # Find all HTML files
    html_files = list(PUBLIC_DIR.rglob("*.html"))
    print(f"📂 Found {len(html_files)} HTML files")
    print()
    
    # Process each file
    results = []
    total_original = 0
    total_removed = 0
    total_classes_added = set()

    for file_path in html_files:
        result, original, removed, classes_added = process_file(file_path, dry_run)
        if result:
            results.append((result, original, removed, classes_added))
            total_original += original
            total_removed += removed
            total_classes_added.update(classes_added)
    
    # Display results
    print("=" * 70)
    print("RESULTS")
    print("=" * 70)
    print()

    if results:
        print(f"Files processed: {len(results)}")
        print(f"Total inline styles found: {total_original}")
        print(f"Total inline styles removed: {total_removed}")
        print(f"Removal rate: {(total_removed/total_original*100):.1f}%")
        print(f"Total Tailwind classes added: {len(total_classes_added)}")
        print()

        if total_classes_added:
            print("Tailwind classes added:")
            for class_name in sorted(total_classes_added):
                print(f"  - {class_name}")

        print()
        print("Top 20 files by inline styles removed:")
        for file_path, original, removed, classes_added in sorted(results, key=lambda x: x[2], reverse=True)[:20]:
            rel_path = file_path.relative_to(PUBLIC_DIR)
            print(f"  {removed:4d} styles: {rel_path}")
    else:
        print("No inline styles found or removed!")

    print()
    if dry_run:
        print("💡 This was a DRY RUN. Use --execute to apply changes.")
    else:
        print("✅ Changes applied!")

if __name__ == "__main__":
    main()


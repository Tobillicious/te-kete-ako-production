#!/usr/bin/env python3

import os
import re
import glob

def standardize_navigation(file_path):
    """Standardize navigation for a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove old navigation containers and scripts
        patterns_to_remove = [
            r'<div id="professional-nav-container"></div>',
            r'<div id="beautiful-nav-container"></div>',
            r'<div id="header-next-level"[^>]*></div>',
            r'<script>\s*fetch\([\'"]/components/professional-navigation\.html[\'"]\)[^<]*</script>',
            r'<script>\s*fetch\([\'"]/components/navigation-mega-menu\.html[\'"]\)[^<]*</script>',
            r'<script>\s*fetch\([\'"]/navigation-header\.html[\'"]\)[^<]*</script>',
        ]
        
        for pattern in patterns_to_remove:
            content = re.sub(pattern, '', content, flags=re.MULTILINE | re.DOTALL)
        
        # Standard navigation component
        standard_nav = '''    <!-- Professional Mega Menu Navigation -->
    <div id="beautiful-nav-container"></div>
    <script>
        fetch('/components/navigation-mega-menu.html')
            .then(r => r.text())
            .then(html => {
                const div = document.createElement('div');
                div.innerHTML = html;
                document.body.insertBefore(div.firstElementChild, document.body.firstChild);
            });
    </script>'''
        
        # Find the <body> tag and add navigation after it
        body_match = re.search(r'<body[^>]*>', content)
        if body_match:
            body_end = body_match.end()
            # Insert navigation after <body> tag
            content = content[:body_end] + '\n' + standard_nav + '\n' + content[body_end:]
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        else:
            print(f"  ⚠️  No <body> tag found in {file_path}")
            return False
            
    except Exception as e:
        print(f"  ❌ Error processing {file_path}: {e}")
        return False

def main():
    print("🎯 STANDARDIZING NAVIGATION ACROSS ALL PAGES")
    print("=============================================")
    
    # Define file patterns to process
    patterns = [
        "public/*.html",
        "public/units/*/index.html",
        "public/units/*/lessons/*.html",
        "public/generated-resources-alpha/*.html",
        "public/generated-resources-alpha/handouts/*.html",
        "public/generated-resources-alpha/lessons/*.html",
    ]
    
    files_processed = 0
    files_successful = 0
    
    for pattern in patterns:
        files = glob.glob(pattern)
        for file_path in files:
            if os.path.isfile(file_path):
                print(f"  🔧 Processing: {file_path}")
                files_processed += 1
                if standardize_navigation(file_path):
                    files_successful += 1
                    print(f"    ✅ Success")
                else:
                    print(f"    ❌ Failed")
    
    print("")
    print("=============================================")
    print(f"✅ NAVIGATION STANDARDIZATION COMPLETE!")
    print(f"📊 Files processed: {files_processed}")
    print(f"📊 Files successful: {files_successful}")
    print("🎯 All pages now use: navigation-mega-menu.html")
    print("=============================================")

if __name__ == "__main__":
    main()

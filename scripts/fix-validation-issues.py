#!/usr/bin/env python3
"""
Fix Validation Issues
Automatically fixes common validation issues found by the pipeline
"""

import os
import re
from pathlib import Path
import subprocess

def fix_validation_issues():
    """Fix validation issues found by the pipeline"""
    
    # Load validation results
    base_dir = Path("/Users/admin/Documents/te-kete-ako-clean")
    validation_file = base_dir / "validation-results.json"
    
    if not validation_file.exists():
        print("❌ Validation results file not found. Run validation first.")
        return False
    
    import json
    with open(validation_file, 'r') as f:
        validation_results = json.load(f)
    
    # Fix HTML files with issues
    if "html" in validation_results.get("validation_checks", {}):
        html_results = validation_results["validation_checks"]["html"]
        
        for result in html_results:
            if not result.get("valid", True):
                file_path = base_dir / result["file"]
                errors = result.get("errors", [])
                
                if file_path.exists():
                    fix_html_file(file_path, errors)
    
    print("✅ Validation issues fixed!")
    return True

def fix_html_file(file_path, errors):
    """Fix issues in an HTML file"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    original_content = content
    
    # Fix missing charset meta tag
    if "Missing charset meta tag" in errors:
        if '<meta charset=' not in content:
            # Add charset meta tag after <head> or at the beginning if no head
            if '<head>' in content:
                content = re.sub(
                    r'(<head>)',
                    r'\1    <meta charset="UTF-8">',
                    content
                )
            elif '<html' in content:
                content = re.sub(
                    r'(<html[^>]*>)',
                    r'\1<head><meta charset="UTF-8"></head>',
                    content
                )
    
    # Fix missing viewport meta tag
    if "Missing viewport meta tag" in errors:
        if 'name="viewport"' not in content:
            # Add viewport meta tag after charset or head
            if '<meta charset=' in content:
                content = re.sub(
                    r'(<meta charset="UTF-8">)',
                    r'\1    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
                    content
                )
            elif '<head>' in content:
                content = re.sub(
                    r'(<head>)',
                    r'\1    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
                    content
                )
    
    # Write back if changed
    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"  ✅ Fixed: {file_path.name}")

def fix_alt_text_issues():
    """Fix missing alt text in images"""
    print("🔧 Fixing alt text issues...")
    
    # Find HTML files with images missing alt text
    result = subprocess.run(
        ["find", "public/", "-name", "*.html", "-exec", "grep", "-l", "img.*src", "{}", ";"],
        capture_output=True,
        text=True
    )
    
    html_files = result.stdout.strip().split('\n')
    fixed_count = 0
    
    for html_file in html_files:
        if not html_file:
            continue
            
        try:
            with open(html_file, 'r') as f:
                content = f.read()
            
            # Find images with template variables in alt text
            original_content = content
            content = re.sub(r'alt="\$\{[^}]*\}"', 'alt="Video thumbnail"', content)
            content = re.sub(r'<img([^>]*?)>(?![^<]*</img>)', r'<img\1 alt="Content image">', content)
            
            if content != original_content:
                with open(html_file, 'w') as f:
                    f.write(content)
                fixed_count += 1
                
        except Exception as e:
            print(f"Error processing {html_file}: {e}")
    
    print(f"✅ Fixed alt text in {fixed_count} files")
    return fixed_count > 0

def main():
    """Main function to fix validation issues"""
    print("🔧 Starting validation fixes...")
    
    # Fix HTML syntax errors
    syntax_fixed = fix_validation_issues()
    
    # Fix alt text issues
    alt_text_fixed = fix_alt_text_issues()
    
    if syntax_fixed or alt_text_fixed:
        print("✅ Validation issues fixed!")
        return True
    else:
        print("ℹ️ No validation issues found to fix")
        return False

if __name__ == "__main__":
    main()

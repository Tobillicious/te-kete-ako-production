#!/usr/bin/env python3
"""Count remaining issues from .cursorrules priorities"""

import os
import subprocess

print("🎯 PRIORITY ISSUES STATUS")
print("=" * 70)

# 1. Missing CSS/JS includes
total_html = len(subprocess.check_output(
    "find public -name '*.html' -type f", 
    shell=True
).decode().strip().split('\n'))

with_main_css = int(subprocess.check_output(
    "grep -r 'main.css' public --include='*.html' | wc -l",
    shell=True
).decode().strip())

print(f"\n1️⃣ MISSING CSS/JS INCLUDES:")
print(f"   Total HTML files: {total_html}")
print(f"   With main.css: {with_main_css}")
print(f"   Still need fix: {total_html - with_main_css}")

# 2. Orphaned pages in generated-resources-alpha
orphaned = len(subprocess.check_output(
    "find public/generated-resources-alpha -name '*.html' -type f",
    shell=True
).decode().strip().split('\n'))

print(f"\n2️⃣ ORPHANED PAGES (need linking):")
print(f"   Pages in generated-resources-alpha: {orphaned}")

# 3. Check for placeholder content
placeholders = int(subprocess.check_output(
    "grep -r 'TODO\\|placeholder\\|FIXME' public --include='*.html' | wc -l",
    shell=True
).decode().strip())

print(f"\n3️⃣ PLACEHOLDER CONTENT:")
print(f"   Files with TODO/placeholder/FIXME: {placeholders}")

print("\n" + "=" * 70)

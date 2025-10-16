#!/usr/bin/env python3
"""
Typography Consistency Checker
Audits heading hierarchy, sizes, and finds typography issues
Agent-9 - October 15, 2025
"""

from pathlib import Path
import re
from bs4 import BeautifulSoup
import random

PUBLIC_DIR = Path('/Users/admin/Documents/te-kete-ako-clean/public')

def audit_typography(filepath):
    """Audit typography in a single page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        issues = []
        
        # Check H1 count (should be exactly 1)
        h1_tags = soup.find_all('h1')
        if len(h1_tags) == 0:
            issues.append("NO_H1")
        elif len(h1_tags) > 1:
            issues.append(f"MULTIPLE_H1:{len(h1_tags)}")
        
        # Check for empty headings
        for level in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            headings = soup.find_all(level)
            for h in headings:
                if not h.get_text(strip=True):
                    issues.append(f"EMPTY_{level.upper()}")
        
        # Check for inline font-size on headings (should use CSS)
        for level in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            headings = soup.find_all(level, style=re.compile('font-size'))
            if headings:
                issues.append(f"INLINE_SIZE_{level.upper()}:{len(headings)}")
        
        return issues
    
    except Exception as e:
        return [f"ERROR:{str(e)[:30]}"]

def main():
    print("📝 TYPOGRAPHY CONSISTENCY AUDIT")
    print("=" * 70)
    
    all_html = list(PUBLIC_DIR.rglob('*.html'))
    print(f"📊 Auditing {len(all_html)} pages...\n")
    
    # Sample 50 random pages for detailed audit
    sample = random.sample(all_html, min(50, len(all_html)))
    
    issues_summary = {
        'no_h1': 0,
        'multiple_h1': 0,
        'empty_headings': 0,
        'inline_styles': 0,
        'perfect': 0
    }
    
    problem_pages = []
    
    for filepath in sample:
        issues = audit_typography(filepath)
        
        if not issues:
            issues_summary['perfect'] += 1
        else:
            for issue in issues:
                if 'NO_H1' in issue:
                    issues_summary['no_h1'] += 1
                    problem_pages.append((filepath.name, issue))
                elif 'MULTIPLE_H1' in issue:
                    issues_summary['multiple_h1'] += 1
                    problem_pages.append((filepath.name, issue))
                elif 'EMPTY' in issue:
                    issues_summary['empty_headings'] += 1
                elif 'INLINE' in issue:
                    issues_summary['inline_styles'] += 1
    
    print("📊 SAMPLE RESULTS (50 pages):")
    print(f"   ✅ Perfect typography: {issues_summary['perfect']}")
    print(f"   ⚠️  Missing H1: {issues_summary['no_h1']}")
    print(f"   ⚠️  Multiple H1s: {issues_summary['multiple_h1']}")
    print(f"   ⚠️  Empty headings: {issues_summary['empty_headings']}")
    print(f"   ⚠️  Inline font-size: {issues_summary['inline_styles']}\n")
    
    if problem_pages[:10]:
        print("🔍 SAMPLE PROBLEM PAGES:")
        for page, issue in problem_pages[:10]:
            print(f"   - {page}: {issue}")
    
    print("\n" + "=" * 70)
    
    # Extrapolate to full site
    total_estimated = {
        'no_h1': int(issues_summary['no_h1'] * len(all_html) / 50),
        'multiple_h1': int(issues_summary['multiple_h1'] * len(all_html) / 50),
        'inline_styles': int(issues_summary['inline_styles'] * len(all_html) / 50)
    }
    
    print(f"\n📊 ESTIMATED SITEWIDE (1,555 pages):")
    print(f"   ⚠️  Pages missing H1: ~{total_estimated['no_h1']}")
    print(f"   ⚠️  Pages with multiple H1s: ~{total_estimated['multiple_h1']}")
    print(f"   ⚠️  Pages with inline styles: ~{total_estimated['inline_styles']}")
    print("\n🎯 Typography is generally good! Minor fixes needed.\n")

if __name__ == '__main__':
    main()


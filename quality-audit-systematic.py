#!/usr/bin/env python3
"""
SYSTEMATIC QUALITY AUDIT
Check each resource for quality issues ONE BY ONE
Quality is EVERYTHING in teaching resources
"""

import sqlite3
from pathlib import Path
import re

class QualityAuditor:
    def __init__(self):
        self.db = sqlite3.connect("te-kete-local-index.db")
        self.issues = []
        
    def audit_all_resources(self):
        """Audit each resource systematically"""
        print("🔍 SYSTEMATIC QUALITY AUDIT")
        print("=" * 70)
        print("Checking each resource for quality issues...\n")
        
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT path, title, type FROM resources 
            WHERE type IN ('lesson', 'handout', 'unit')
            ORDER BY type, path
        """)
        
        resources = cursor.fetchall()
        print(f"📋 Auditing {len(resources)} educational resources...")
        print()
        
        for i, (path, title, res_type) in enumerate(resources, 1):
            issues = self.check_resource_quality(path, title, res_type)
            
            if issues:
                self.issues.append({
                    'path': path,
                    'title': title,
                    'type': res_type,
                    'issues': issues
                })
                
            # Progress update
            if i % 100 == 0:
                print(f"   ✅ Audited {i}/{len(resources)} resources...")
        
        return self.issues
    
    def check_resource_quality(self, path, title, res_type):
        """Check single resource for quality issues"""
        issues = []
        
        try:
            content = Path(path).read_text(encoding='utf-8', errors='ignore')
            
            # Check 1: Template placeholders
            if re.search(r'\[INSERT|\[TODO|\[ADD|\[FILL|placeholder|PLACEHOLDER', content, re.I):
                if 'template' not in path.lower():  # Templates are allowed to have placeholders
                    issues.append("Has template placeholders that should be filled in")
            
            # Check 2: Missing title
            if not re.search(r'<title>[^<]{5,}</title>', content, re.I):
                issues.append("Missing or empty title tag")
            
            # Check 3: Missing description
            if not re.search(r'<meta name="description"', content, re.I):
                issues.append("Missing meta description")
            
            # Check 4: Cultural context (for lessons/units)
            if res_type in ['lesson', 'unit']:
                if not re.search(r'whakataukī|whakatauaki|cultural context|te ao māori', content, re.I):
                    issues.append("Missing cultural context section")
            
            # Check 5: Navigation
            if not re.search(r'<nav|navigation-standard|breadcrumb', content, re.I):
                issues.append("Missing navigation")
            
            # Check 6: Print optimization
            if res_type in ['handout', 'lesson']:
                if not re.search(r'no-print|print\.css|@media print', content, re.I):
                    issues.append("Missing print optimization")
            
            # Check 7: Professional CSS
            if not re.search(r'te-kete-professional\.css|te-kete-unified-design-system\.css', content, re.I):
                issues.append("Not using professional CSS system")
            
            # Check 8: Broken internal links
            links = re.findall(r'href="(/[^"]+\.html)"', content)
            for link in links[:10]:  # Check first 10 links
                link_path = Path('public' + link)
                if not link_path.exists():
                    issues.append(f"Broken link: {link}")
                    break  # Just report one broken link per file
            
            # Check 9: Lorem ipsum
            if 'lorem ipsum' in content.lower():
                issues.append("Contains lorem ipsum placeholder text")
            
            # Check 10: Duplicate content (very short files might be incomplete)
            if len(content) < 500:
                issues.append("Very short file - might be incomplete")
                
        except Exception as e:
            issues.append(f"Error reading file: {e}")
        
        return issues
    
    def categorize_issues(self):
        """Categorize issues by severity"""
        print("\n" + "=" * 70)
        print("📊 QUALITY AUDIT RESULTS")
        print("=" * 70)
        
        critical = [i for i in self.issues if any(x in str(i['issues']) for x in ['placeholder', 'lorem ipsum', 'broken link'])]
        high = [i for i in self.issues if any(x in str(i['issues']) for x in ['cultural context', 'title', 'description'])]
        medium = [i for i in self.issues if any(x in str(i['issues']) for x in ['navigation', 'print', 'CSS'])]
        low = [i for i in self.issues if any(x in str(i['issues']) for x in ['short file'])]
        
        print(f"\n🚨 CRITICAL Issues: {len(critical)}")
        print(f"⚠️  HIGH Priority: {len(high)}")
        print(f"📋 MEDIUM Priority: {len(medium)}")
        print(f"💡 LOW Priority: {len(low)}")
        
        print(f"\n✅ Clean Resources: {1593 - len(self.issues)}")
        print(f"⚠️  Resources Needing Work: {len(self.issues)}")
        print(f"📊 Quality Score: {((1593 - len(self.issues)) / 1593 * 100):.1f}%")
        
        # Show top 10 critical issues
        if critical:
            print(f"\n🚨 TOP 10 CRITICAL ISSUES TO FIX:")
            for i, issue in enumerate(critical[:10], 1):
                print(f"\n{i}. {issue['title']}")
                print(f"   Path: {issue['path']}")
                print(f"   Issues:")
                for problem in issue['issues']:
                    print(f"      - {problem}")
        
        return {
            'critical': critical,
            'high': high,
            'medium': medium,
            'low': low
        }

if __name__ == "__main__":
    auditor = QualityAuditor()
    issues = auditor.audit_all_resources()
    categorized = auditor.categorize_issues()
    
    print("\n" + "=" * 70)
    print("✅ Quality audit complete!")
    print(f"   Found {len(issues)} resources needing improvement")
    print("=" * 70)


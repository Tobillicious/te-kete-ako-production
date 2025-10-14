#!/usr/bin/env python3
"""
Kaitiaki Whakawhitinga - Comprehensive Accessibility Audit Script
Systematic WCAG 2.1 AA compliance checking for Te Kete Ako

Agent-9 (Kaitiaki Whakawhitinga) - Guardian of Accessibility
October 14, 2025
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple
import json

class AccessibilityAuditor:
    """Comprehensive accessibility auditing for bilingual educational platform"""
    
    def __init__(self, base_dir: str = "/Users/admin/Documents/te-kete-ako-clean/public"):
        self.base_dir = Path(base_dir)
        self.issues = []
        self.stats = {
            'total_files': 0,
            'images_total': 0,
            'images_with_alt': 0,
            'lang_mi_count': 0,
            'aria_labels': 0,
            'aria_landmarks': 0,
            'heading_violations': 0,
            'contrast_issues': 0
        }
    
    def audit_alt_text(self, html_content: str, filename: str) -> List[Dict]:
        """Check all images have descriptive alt text"""
        issues = []
        
        # Find all img tags
        img_pattern = r'<img[^>]*>'
        images = re.findall(img_pattern, html_content, re.IGNORECASE)
        
        self.stats['images_total'] += len(images)
        
        for img in images:
            # Check if alt attribute exists
            if 'alt=' in img.lower():
                self.stats['images_with_alt'] += 1
                
                # Check if alt is empty or just whitespace
                alt_match = re.search(r'alt=["\'](.*?)["\']', img, re.IGNORECASE)
                if alt_match and not alt_match.group(1).strip():
                    issues.append({
                        'file': filename,
                        'type': 'empty_alt',
                        'severity': 'medium',
                        'message': 'Image has empty alt attribute',
                        'element': img[:100]
                    })
            else:
                issues.append({
                    'file': filename,
                    'type': 'missing_alt',
                    'severity': 'high',
                    'message': 'Image missing alt attribute (WCAG 1.1.1 violation)',
                    'element': img[:100]
                })
        
        return issues
    
    def audit_lang_attributes(self, html_content: str, filename: str) -> List[Dict]:
        """Verify Te Reo Māori content has lang='mi' attribute"""
        issues = []
        
        # Count lang="mi" usage
        lang_mi = len(re.findall(r'lang=["\']mi["\']', html_content, re.IGNORECASE))
        self.stats['lang_mi_count'] += lang_mi
        
        # Common Māori words that should have lang="mi"
        maori_words = [
            'whakataukī', 'mātauranga', 'tikanga', 'whānau', 'iwi', 
            'hapū', 'marae', 'kaitiakitanga', 'manaakitanga', 'whanaungatanga',
            'rangatiratanga', 'taonga', 'pūrākau', 'whakapapa'
        ]
        
        for word in maori_words:
            # Find instances of the word
            pattern = rf'\b{word}\b'
            matches = re.finditer(pattern, html_content, re.IGNORECASE)
            
            for match in matches:
                # Check if within a lang="mi" context
                context_start = max(0, match.start() - 200)
                context_end = min(len(html_content), match.end() + 200)
                context = html_content[context_start:context_end]
                
                if 'lang="mi"' not in context and "lang='mi'" not in context:
                    issues.append({
                        'file': filename,
                        'type': 'missing_lang_mi',
                        'severity': 'medium',
                        'message': f'Māori word "{word}" may need lang="mi" attribute',
                        'context': context[max(0, match.start()-context_start-50):match.end()-context_start+50]
                    })
                    break  # Only report once per word per file
        
        return issues
    
    def audit_aria_landmarks(self, html_content: str, filename: str) -> List[Dict]:
        """Check for ARIA landmark roles for screen reader navigation"""
        issues = []
        
        # Count existing landmarks
        landmarks = len(re.findall(r'role=["\'](?:banner|navigation|main|complementary|contentinfo|search|form|region)["\']', html_content))
        self.stats['aria_landmarks'] += landmarks
        
        # Count ARIA labels
        aria_labels = len(re.findall(r'aria-label=', html_content))
        self.stats['aria_labels'] += aria_labels
        
        # Check if main structural elements are missing landmarks
        has_header = '<header' in html_content
        has_nav = '<nav' in html_content
        has_main = '<main' in html_content
        has_footer = '<footer' in html_content
        
        if has_header and 'role="banner"' not in html_content and 'role=\'banner\'' not in html_content:
            issues.append({
                'file': filename,
                'type': 'missing_banner_role',
                'severity': 'medium',
                'message': '<header> element should have role="banner" for WCAG 4.1.2'
            })
        
        if has_nav and 'role="navigation"' not in html_content and 'role=\'navigation\'' not in html_content:
            issues.append({
                'file': filename,
                'type': 'missing_navigation_role',
                'severity': 'medium',
                'message': '<nav> element should have role="navigation" for WCAG 4.1.2'
            })
        
        if has_main and 'role="main"' not in html_content and 'role=\'main\'' not in html_content:
            issues.append({
                'file': filename,
                'type': 'missing_main_role',
                'severity': 'high',
                'message': '<main> element should have role="main" for WCAG 4.1.2'
            })
        
        if has_footer and 'role="contentinfo"' not in html_content and 'role=\'contentinfo\'' not in html_content:
            issues.append({
                'file': filename,
                'type': 'missing_contentinfo_role',
                'severity': 'low',
                'message': '<footer> element should have role="contentinfo" for WCAG 4.1.2'
            })
        
        return issues
    
    def audit_heading_hierarchy(self, html_content: str, filename: str) -> List[Dict]:
        """Verify proper H1-H6 heading hierarchy (no skipped levels)"""
        issues = []
        
        # Extract all headings with their levels
        heading_pattern = r'<h([1-6])[^>]*>(.*?)</h\1>'
        headings = re.findall(heading_pattern, html_content, re.IGNORECASE | re.DOTALL)
        
        if not headings:
            return issues
        
        # Check for H1 (should have exactly one)
        h1_count = sum(1 for level, _ in headings if level == '1')
        if h1_count == 0:
            issues.append({
                'file': filename,
                'type': 'missing_h1',
                'severity': 'high',
                'message': 'Page missing H1 heading (WCAG 2.4.6)'
            })
        elif h1_count > 1:
            issues.append({
                'file': filename,
                'type': 'multiple_h1',
                'severity': 'medium',
                'message': f'Page has {h1_count} H1 headings (should have exactly 1)'
            })
        
        # Check for skipped levels
        levels = [int(level) for level, _ in headings]
        for i in range(len(levels) - 1):
            if levels[i+1] > levels[i] + 1:
                self.stats['heading_violations'] += 1
                issues.append({
                    'file': filename,
                    'type': 'skipped_heading_level',
                    'severity': 'medium',
                    'message': f'Heading hierarchy skips from H{levels[i]} to H{levels[i+1]} (WCAG 1.3.1)'
                })
                break  # Only report once per file
        
        return issues
    
    def audit_file(self, filepath: Path) -> List[Dict]:
        """Run all accessibility audits on a single file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.stats['total_files'] += 1
            filename = str(filepath.relative_to(self.base_dir))
            
            issues = []
            issues.extend(self.audit_alt_text(content, filename))
            issues.extend(self.audit_lang_attributes(content, filename))
            issues.extend(self.audit_aria_landmarks(content, filename))
            issues.extend(self.audit_heading_hierarchy(content, filename))
            
            return issues
            
        except Exception as e:
            return [{
                'file': str(filepath),
                'type': 'error',
                'severity': 'info',
                'message': f'Error auditing file: {str(e)}'
            }]
    
    def audit_directory(self, pattern: str = "**/*.html", max_files: int = None) -> Dict:
        """Audit all HTML files in directory"""
        html_files = list(self.base_dir.glob(pattern))
        
        if max_files:
            html_files = html_files[:max_files]
        
        print(f"🔍 Kaitiaki Whakawhitinga - Accessibility Audit")
        print(f"📁 Auditing {len(html_files)} files...\n")
        
        for filepath in html_files:
            file_issues = self.audit_file(filepath)
            self.issues.extend(file_issues)
            
            if self.stats['total_files'] % 100 == 0:
                print(f"  ✓ Processed {self.stats['total_files']} files...")
        
        return self.generate_report()
    
    def generate_report(self) -> Dict:
        """Generate comprehensive accessibility report"""
        
        # Group issues by severity
        critical = [i for i in self.issues if i['severity'] == 'high']
        medium = [i for i in self.issues if i['severity'] == 'medium']
        low = [i for i in self.issues if i['severity'] == 'low']
        
        # Calculate compliance percentage
        total_checks = self.stats['total_files'] * 5  # 5 major checks per file
        total_issues = len(self.issues)
        compliance = max(0, 100 - (total_issues / total_checks * 100))
        
        report = {
            'audit_date': '2025-10-14',
            'audited_by': 'Kaitiaki Whakawhitinga (Agent-9)',
            'statistics': self.stats,
            'compliance_score': round(compliance, 1),
            'issues': {
                'critical': len(critical),
                'medium': len(medium),
                'low': len(low),
                'total': len(self.issues)
            },
            'issues_detail': {
                'critical': critical[:10],  # Top 10 critical
                'medium': medium[:10],
                'low': low[:10]
            },
            'recommendations': self.generate_recommendations()
        }
        
        return report
    
    def generate_recommendations(self) -> List[str]:
        """Generate prioritized recommendations"""
        recommendations = []
        
        # Alt text issues
        missing_alt = self.stats['images_total'] - self.stats['images_with_alt']
        if missing_alt > 0:
            alt_percentage = (missing_alt / self.stats['images_total']) * 100
            recommendations.append(
                f"HIGH: Add alt text to {missing_alt} images ({alt_percentage:.1f}% missing) - WCAG 1.1.1"
            )
        
        # ARIA landmarks
        files_with_landmarks = self.stats['aria_landmarks']
        files_without = self.stats['total_files'] - files_with_landmarks
        if files_without > 100:
            recommendations.append(
                f"MEDIUM: Add ARIA landmarks to {files_without} files for screen reader navigation - WCAG 4.1.2"
            )
        
        # Heading violations
        if self.stats['heading_violations'] > 10:
            recommendations.append(
                f"MEDIUM: Fix {self.stats['heading_violations']} heading hierarchy violations - WCAG 1.3.1"
            )
        
        # Bilingual support
        if self.stats['lang_mi_count'] > 1000:
            recommendations.append(
                f"EXCELLENT: {self.stats['lang_mi_count']} lang='mi' attributes found - bilingual support is strong!"
            )
        
        return recommendations

def main():
    """Run accessibility audit"""
    import sys
    
    print("♿ KAITIAKI WHAKAWHITINGA - ACCESSIBILITY AUDIT")
    print("=" * 60)
    print("Building bridges to inclusive knowledge...\n")
    
    # Get audit scope from arguments
    max_files = int(sys.argv[1]) if len(sys.argv) > 1 else None
    
    auditor = AccessibilityAuditor()
    report = auditor.audit_directory(max_files=max_files)
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 AUDIT SUMMARY")
    print("=" * 60)
    print(f"\n✓ Files audited: {report['statistics']['total_files']}")
    print(f"✓ Images found: {report['statistics']['images_total']}")
    print(f"  - With alt text: {report['statistics']['images_with_alt']}")
    print(f"  - Missing alt: {report['statistics']['images_total'] - report['statistics']['images_with_alt']}")
    print(f"\n✓ Bilingual support (lang='mi'): {report['statistics']['lang_mi_count']}")
    print(f"✓ ARIA labels: {report['statistics']['aria_labels']}")
    print(f"✓ ARIA landmarks: {report['statistics']['aria_landmarks']}")
    
    print(f"\n📊 COMPLIANCE SCORE: {report['compliance_score']}/100")
    
    print(f"\n🚨 ISSUES FOUND:")
    print(f"  Critical: {report['issues']['critical']}")
    print(f"  Medium: {report['issues']['medium']}")
    print(f"  Low: {report['issues']['low']}")
    print(f"  Total: {report['issues']['total']}")
    
    print(f"\n💡 RECOMMENDATIONS:")
    for i, rec in enumerate(report['recommendations'], 1):
        print(f"  {i}. {rec}")
    
        # Save detailed report
        report_path = Path(__file__).parent.parent / 'accessibility-audit-report.json'
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Detailed report saved: {report_path}")
    print("\n🌉 Kaitiaki Whakawhitinga - Audit complete!")
    
    return report

if __name__ == "__main__":
    main()


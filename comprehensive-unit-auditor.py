#!/usr/bin/env python3
"""
COMPREHENSIVE UNIT AUDITOR
Audits ALL units for world-class quality standards
No terminal needed - pure file operations
"""

from pathlib import Path
import re
import json
from collections import defaultdict

PUBLIC_DIR = Path("public")

class WorldClassAuditor:
    def __init__(self):
        self.units = []
        self.quality_scores = {}
        self.gaps_found = []
        
    def scan_all_units(self):
        """Find ALL unit directories and index pages"""
        print("🔍 COMPREHENSIVE UNIT SCAN")
        print("=" * 60)
        
        # Find all potential unit directories
        unit_patterns = [
            PUBLIC_DIR / "units",
            PUBLIC_DIR / "y8-systems",
            PUBLIC_DIR / "guided-inquiry-unit",
            PUBLIC_DIR / "critical-thinking",
            PUBLIC_DIR / "writers-toolkit",
            PUBLIC_DIR / "generated-resources-alpha",
            PUBLIC_DIR / "interactive-literacy",
            PUBLIC_DIR / "lessons" / "mathematics-science-interactive-toolkit",
            PUBLIC_DIR / "lessons" / "walker",
            PUBLIC_DIR / "lessons" / "herangi",
        ]
        
        for pattern in unit_patterns:
            if pattern.exists():
                if pattern.name == "units":
                    # Scan subdirectories
                    for subdir in pattern.iterdir():
                        if subdir.is_dir():
                            self.audit_unit_directory(subdir)
                else:
                    self.audit_unit_directory(pattern)
        
        print(f"\n✅ Found {len(self.units)} total units")
        
    def audit_unit_directory(self, unit_dir):
        """Audit a single unit directory"""
        index_file = unit_dir / "index.html"
        
        if not index_file.exists():
            self.gaps_found.append({
                'path': str(unit_dir),
                'issue': 'NO INDEX PAGE',
                'severity': 'HIGH'
            })
            return
        
        # Read and audit the index page
        try:
            content = index_file.read_text(encoding='utf-8')
            
            unit_info = {
                'path': str(unit_dir),
                'name': unit_dir.name,
                'index_file': str(index_file),
                'scores': self.evaluate_unit(content, unit_dir)
            }
            
            self.units.append(unit_info)
            
        except Exception as e:
            self.gaps_found.append({
                'path': str(unit_dir),
                'issue': f'READ ERROR: {e}',
                'severity': 'CRITICAL'
            })
    
    def evaluate_unit(self, content, unit_dir):
        """Evaluate unit against world-class standards"""
        scores = {
            'completeness': 0,
            'quality': 0,
            'cultural_integration': 0,
            'technical_excellence': 0,
            'total': 0,
            'tier': 'FRAGMENT'
        }
        
        # COMPLETENESS (30 points)
        completeness_checks = {
            'has_title': bool(re.search(r'<title>(.+?)</title>', content)),
            'has_meta_description': 'meta name="description"' in content,
            'has_lessons_section': 'lesson' in content.lower(),
            'has_objectives': 'objective' in content.lower() or 'whāinga' in content.lower(),
            'has_assessment': 'assessment' in content.lower() or 'rubric' in content.lower(),
            'has_resources': 'resource' in content.lower() or 'handout' in content.lower()
        }
        
        completeness = sum(completeness_checks.values()) * 5
        scores['completeness'] = completeness
        
        # QUALITY (30 points)
        quality_checks = {
            'professional_css': 'te-kete-unified-design-system.css' in content,
            'navigation_component': 'navigation-standard.html' in content or 'beautiful-nav' in content,
            'responsive_design': 'mobile-optimization.css' in content or 'viewport' in content,
            'accessibility': 'role="main"' in content or 'aria-' in content,
            'print_friendly': 'print.css' in content,
            'no_inline_styles': content.count('style=') < 20  # Some inline is ok
        }
        
        quality = sum(quality_checks.values()) * 5
        scores['quality'] = quality
        
        # CULTURAL INTEGRATION (25 points)
        cultural_checks = {
            'whakatauaki': 'whakataukī' in content.lower() or 'whakatauaki' in content.lower(),
            'cultural_context': 'cultural context' in content.lower() or 'horopaki ahurea' in content.lower(),
            'house_values': 'whaimana' in content.lower() or 'whaiora' in content.lower() or 'whaiara' in content.lower(),
            'maori_concepts': 'mātauranga' in content.lower() or 'kaitiakitanga' in content.lower(),
            'cultural_safety': 'cultural safety' in content.lower() or 'culturally safe' in content.lower()
        }
        
        cultural = sum(cultural_checks.values()) * 5
        scores['cultural_integration'] = cultural
        
        # TECHNICAL EXCELLENCE (15 points)
        technical_checks = {
            'valid_doctype': '<!DOCTYPE html>' in content[:200],
            'utf8_encoding': 'charset="UTF-8"' in content or 'charset="utf-8"' in content,
            'semantic_html': '<main' in content and '<header' in content
        }
        
        technical = sum(technical_checks.values()) * 5
        scores['technical_excellence'] = technical
        
        # TOTAL SCORE
        total = completeness + quality + cultural + technical
        scores['total'] = total
        
        # TIER CLASSIFICATION
        if total >= 90:
            scores['tier'] = 'GOLD STANDARD'
        elif total >= 75:
            scores['tier'] = 'PROFESSIONAL'
        elif total >= 60:
            scores['tier'] = 'GOOD'
        elif total >= 40:
            scores['tier'] = 'PARTIAL'
        else:
            scores['tier'] = 'FRAGMENT'
        
        # Count lessons and resources
        lesson_files = list(unit_dir.glob('**/lesson-*.html'))
        lesson_files += list(unit_dir.glob('**/lessons/*.html'))
        handout_files = list(unit_dir.glob('**/handout*.html'))
        handout_files += list(unit_dir.glob('**/handouts/*.html'))
        
        scores['lesson_count'] = len([f for f in lesson_files if 'backup' not in str(f)])
        scores['handout_count'] = len([f for f in handout_files if 'backup' not in str(f)])
        
        return scores
    
    def generate_comprehensive_report(self):
        """Generate world-class audit report"""
        print("\n" + "=" * 60)
        print("📊 WORLD-CLASS QUALITY AUDIT RESULTS")
        print("=" * 60)
        
        # Sort by total score
        sorted_units = sorted(self.units, key=lambda x: x['scores']['total'], reverse=True)
        
        # Group by tier
        by_tier = defaultdict(list)
        for unit in sorted_units:
            tier = unit['scores']['tier']
            by_tier[tier].append(unit)
        
        # Print summary
        print(f"\n🏆 TIER SUMMARY:")
        print(f"   GOLD STANDARD: {len(by_tier['GOLD STANDARD'])} units")
        print(f"   PROFESSIONAL:  {len(by_tier['PROFESSIONAL'])} units")
        print(f"   GOOD:          {len(by_tier['GOOD'])} units")
        print(f"   PARTIAL:       {len(by_tier['PARTIAL'])} units")
        print(f"   FRAGMENT:      {len(by_tier['FRAGMENT'])} units")
        
        # Show top performers
        print(f"\n⭐ TOP 10 UNITS (Feature These!):")
        for i, unit in enumerate(sorted_units[:10], 1):
            name = unit['name']
            score = unit['scores']['total']
            tier = unit['scores']['tier']
            lessons = unit['scores']['lesson_count']
            print(f"   {i}. {name}")
            print(f"      Score: {score}/100 | {tier} | {lessons} lessons")
        
        # Show units needing improvement
        print(f"\n⚠️  UNITS NEEDING IMPROVEMENT:")
        needs_work = [u for u in sorted_units if u['scores']['total'] < 60]
        for unit in needs_work[:5]:
            name = unit['name']
            score = unit['scores']['total']
            print(f"   - {name}: {score}/100")
            print(f"     Missing:")
            if unit['scores']['completeness'] < 15:
                print(f"       • Content completeness")
            if unit['scores']['quality'] < 15:
                print(f"       • Technical quality")
            if unit['scores']['cultural_integration'] < 12:
                print(f"       • Cultural integration")
        
        # Generate JSON report
        report = {
            'audit_date': str(Path.cwd()),
            'total_units': len(self.units),
            'tier_counts': {tier: len(units) for tier, units in by_tier.items()},
            'units': sorted_units,
            'gaps': self.gaps_found,
            'recommendations': self.generate_recommendations(by_tier)
        }
        
        with open('world-class-unit-audit.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n✅ Detailed audit saved to: world-class-unit-audit.json")
    
    def generate_recommendations(self, by_tier):
        """Generate actionable recommendations"""
        recommendations = []
        
        # Feature gold standard
        if by_tier['GOLD STANDARD']:
            recommendations.append({
                'priority': 'HIGH',
                'action': 'FEATURE',
                'target': f"{len(by_tier['GOLD STANDARD'])} Gold Standard units",
                'detail': 'Add these to homepage featured section'
            })
        
        # Improve partial/fragments
        if by_tier['PARTIAL'] or by_tier['FRAGMENT']:
            count = len(by_tier['PARTIAL']) + len(by_tier['FRAGMENT'])
            recommendations.append({
                'priority': 'MEDIUM',
                'action': 'IMPROVE',
                'target': f"{count} Partial/Fragment units",
                'detail': 'Add missing content, cultural context, and styling'
            })
        
        # Fill gaps
        if self.gaps_found:
            recommendations.append({
                'priority': 'HIGH',
                'action': 'FIX_GAPS',
                'target': f"{len(self.gaps_found)} directories missing index pages",
                'detail': 'Create unit overview pages for directories with lessons'
            })
        
        return recommendations

def main():
    print("\n🌟 WORLD-CLASS UNIT QUALITY AUDIT")
    print("Evaluating ALL units against excellence standards\n")
    
    auditor = WorldClassAuditor()
    auditor.scan_all_units()
    auditor.generate_comprehensive_report()
    
    print("\n" + "=" * 60)
    print("✨ AUDIT COMPLETE!")
    print("=" * 60)
    print("\n📖 Next Steps:")
    print("   1. Review world-class-unit-audit.json")
    print("   2. Feature Gold Standard units on homepage")
    print("   3. Improve Partial/Fragment units to Professional tier")
    print("   4. Create missing index pages")
    print("   5. Ensure 100% cultural integration")
    print("\n🎯 Goal: ALL units at Professional tier or above!")

if __name__ == "__main__":
    main()


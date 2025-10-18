#!/usr/bin/env python3
"""
DEEP .master FILE COMPARISON
Compare all 127 .master files with current versions
Find what features were lost/gained
"""

from pathlib import Path
import re
from collections import defaultdict

class MasterFileAnalyzer:
    def __init__(self):
        self.comparisons = []
        self.features_lost = defaultdict(list)
        self.features_gained = defaultdict(list)
        self.summary = {
            'total_files': 0,
            'identical': 0,
            'current_better': 0,
            'master_better': 0,
            'mixed': 0
        }
    
    def analyze_features(self, content):
        """Extract features from HTML content"""
        features = {
            'dropdown_menu': 'dropdown-menu' in content or 'dropdown-card' in content,
            'mega_menu': 'mega-menu' in content or 'dropdown-grid' in content,
            'badge_system': 'badge-system' in content or 'class="badge' in content,
            'search_bar': 'search-container' in content or 'search-bar' in content,
            'breadcrumbs': 'breadcrumb' in content,
            'cultural_context': 'whakataukī' in content.lower() or 'cultural context' in content.lower(),
            'lesson_nav': 'lesson-sequence-nav' in content or 'prev-next' in content,
            'sidebar': 'sidebar' in content or 'aside' in content,
            'animations': 'animations-professional.css' in content,
            'unified_css': 'te-kete-unified-design-system.css' in content,
            'old_css': 'te-kete-professional.css' in content and 'unified' not in content,
            'component_library': 'component-library.css' in content,
            'mobile_css': 'mobile-optimization.css' in content,
        }
        
        # Count CSS files
        features['css_count'] = len(re.findall(r'<link[^>]*stylesheet[^>]*>', content))
        
        # Check for placeholders
        features['has_placeholders'] = '[TO BE FILLED]' in content or 'TODO' in content
        
        # Check file size
        features['size'] = len(content)
        
        return features
    
    def compare_files(self, master_path, current_path):
        """Compare master vs current file"""
        try:
            master_content = master_path.read_text(encoding='utf-8', errors='ignore')
            current_content = current_path.read_text(encoding='utf-8', errors='ignore')
            
            master_features = self.analyze_features(master_content)
            current_features = self.analyze_features(current_content)
            
            # Determine which is better
            lost = []
            gained = []
            
            # Check dropdown/mega menu
            if master_features['dropdown_menu'] and not current_features['dropdown_menu']:
                lost.append('dropdown_menu')
            elif current_features['dropdown_menu'] and not master_features['dropdown_menu']:
                gained.append('dropdown_menu')
            
            # Check other features
            for feature in ['badge_system', 'search_bar', 'breadcrumbs', 'lesson_nav', 
                           'sidebar', 'animations', 'unified_css', 'component_library', 'mobile_css']:
                if master_features[feature] and not current_features[feature]:
                    lost.append(feature)
                elif current_features[feature] and not master_features[feature]:
                    gained.append(feature)
            
            # Assess overall
            assessment = 'mixed'
            if not lost and gained:
                assessment = 'current_better'
            elif lost and not gained:
                assessment = 'master_better'
            elif not lost and not gained:
                if current_features['size'] > master_features['size']:
                    assessment = 'current_better'
                else:
                    assessment = 'identical'
            
            return {
                'file': str(current_path.relative_to(Path('public'))),
                'master_features': master_features,
                'current_features': current_features,
                'lost': lost,
                'gained': gained,
                'assessment': assessment,
                'size_diff': current_features['size'] - master_features['size']
            }
            
        except Exception as e:
            return None
    
    def run_analysis(self):
        """Analyze all .master files"""
        print("\n🔬 DEEP .master FILE ANALYSIS")
        print("=" * 70)
        print("Comparing all 127 .master files with current versions...")
        print()
        
        # Find all .master files
        master_files = list(Path('public').rglob('*.master'))
        
        print(f"📊 Found {len(master_files)} .master files\n")
        
        for master_path in master_files:
            current_path = Path(str(master_path).replace('.master', ''))
            
            if current_path.exists():
                result = self.compare_files(master_path, current_path)
                if result:
                    self.comparisons.append(result)
                    self.summary['total_files'] += 1
                    self.summary[result['assessment']] += 1
                    
                    # Track features
                    for feature in result['lost']:
                        self.features_lost[feature].append(result['file'])
                    for feature in result['gained']:
                        self.features_gained[feature].append(result['file'])
        
        self.generate_report()
    
    def generate_report(self):
        """Generate comprehensive report"""
        print("\n" + "=" * 70)
        print("📊 ANALYSIS RESULTS")
        print("=" * 70)
        
        print(f"\n📁 Files Analyzed: {self.summary['total_files']}")
        print(f"   ✅ Current version better: {self.summary['current_better']}")
        print(f"   ⚠️  Master version better: {self.summary['master_better']}")
        print(f"   🔄 Mixed (trade-offs): {self.summary['mixed']}")
        print(f"   ⚪ Identical: {self.summary['identical']}")
        
        # Features lost
        if self.features_lost:
            print(f"\n⚠️  FEATURES LOST IN CURRENT VERSIONS:")
            for feature, files in sorted(self.features_lost.items(), key=lambda x: len(x[1]), reverse=True):
                print(f"   {feature}: {len(files)} files")
                if len(files) <= 3:
                    for f in files:
                        print(f"      - {f}")
        
        # Features gained
        if self.features_gained:
            print(f"\n✅ FEATURES GAINED IN CURRENT VERSIONS:")
            for feature, files in sorted(self.features_gained.items(), key=lambda x: len(x[1]), reverse=True):
                print(f"   {feature}: {len(files)} files")
        
        # Show specific cases where master might be better
        master_better = [c for c in self.comparisons if c['assessment'] == 'master_better']
        if master_better:
            print(f"\n🚨 FILES WHERE .master MIGHT BE BETTER:")
            for comp in master_better[:10]:
                print(f"   📄 {comp['file']}")
                print(f"      Lost: {', '.join(comp['lost'])}")
                print(f"      Size: {comp['size_diff']:+d} bytes")
        
        # Show mixed trade-offs
        mixed = [c for c in self.comparisons if c['assessment'] == 'mixed']
        if mixed:
            print(f"\n🔄 TRADE-OFF CASES ({len(mixed)} files):")
            print("   (Lost some features but gained others)")
            for comp in mixed[:5]:
                print(f"   📄 {comp['file']}")
                print(f"      Lost: {', '.join(comp['lost'])}")
                print(f"      Gained: {', '.join(comp['gained'])}")
        
        # Overall verdict
        print("\n" + "=" * 70)
        print("🎯 OVERALL VERDICT")
        print("=" * 70)
        
        current_better_pct = (self.summary['current_better'] / self.summary['total_files'] * 100) if self.summary['total_files'] > 0 else 0
        
        print(f"\n{current_better_pct:.1f}% of files: Current version is better")
        
        if current_better_pct > 80:
            print("\n✅ RECOMMENDATION: Archive .master files")
            print("   Current versions are clearly superior")
        elif current_better_pct > 50:
            print("\n⚠️  RECOMMENDATION: Selectively archive")
            print("   Some .master files might have useful features")
        else:
            print("\n🚨 RECOMMENDATION: Keep .master files")
            print("   They may have important features we lost")
        
        # Save detailed report
        import json
        report_path = Path('master-files-comparison-report.json')
        report_path.write_text(json.dumps({
            'summary': self.summary,
            'features_lost': {k: len(v) for k, v in self.features_lost.items()},
            'features_gained': {k: len(v) for k, v in self.features_gained.items()},
            'comparisons': self.comparisons
        }, indent=2))
        
        print(f"\n📄 Detailed report saved: {report_path}")

if __name__ == '__main__':
    analyzer = MasterFileAnalyzer()
    analyzer.run_analysis()


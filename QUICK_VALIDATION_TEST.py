#!/usr/bin/env python3
"""
Quick validation test - verify BMAD is on all pages
"""

import os
from pathlib import Path
import re

def test_bmad_integration():
    """Test that all HTML files have BMAD system"""
    
    public_dir = Path('public')
    html_files = list(public_dir.rglob('*.html'))
    
    print(f"🧪 TESTING {len(html_files)} HTML FILES\n")
    
    results = {
        'has_bmad_css': 0,
        'has_framer': 0,
        'has_tailwind': 0,
        'has_cultural_patterns': 0,
        'has_old_css': 0,
        'total': len(html_files)
    }
    
    old_css_files = []
    missing_bmad_files = []
    
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for BMAD components
            if 'te-kete-ultimate-beauty-system.css' in content:
                results['has_bmad_css'] += 1
            else:
                missing_bmad_files.append(str(filepath))
                
            if 'framer-cultural-gestures-ultimate.js' in content:
                results['has_framer'] += 1
                
            if 'tailwind.config.ultimate.js' in content:
                results['has_tailwind'] += 1
                
            if 'cultural-pattern-library-ultimate.css' in content:
                results['has_cultural_patterns'] += 1
            
            # Check for old CSS (should be zero!)
            if 'te-kete-professional.css' in content:
                results['has_old_css'] += 1
                old_css_files.append(str(filepath))
                
        except Exception as e:
            print(f"❌ Error reading {filepath}: {e}")
    
    # Print results
    print("="*70)
    print("📊 BMAD INTEGRATION TEST RESULTS")
    print("="*70)
    print(f"\n✅ BMAD CSS: {results['has_bmad_css']}/{results['total']} ({results['has_bmad_css']*100//results['total']}%)")
    print(f"✅ Framer Motion: {results['has_framer']}/{results['total']} ({results['has_framer']*100//results['total']}%)")
    print(f"✅ Tailwind Config: {results['has_tailwind']}/{results['total']} ({results['has_tailwind']*100//results['total']}%)")
    print(f"✅ Cultural Patterns: {results['has_cultural_patterns']}/{results['total']} ({results['has_cultural_patterns']*100//results['total']}%)")
    
    print(f"\n⚠️  OLD CSS (te-kete-professional.css): {results['has_old_css']} files")
    
    if results['has_old_css'] > 0:
        print(f"\n🚨 FAILED: Found {results['has_old_css']} files with old CSS:")
        for f in old_css_files[:10]:
            print(f"   - {f}")
    else:
        print("   ✅ PERFECT! Zero old CSS conflicts!")
    
    if len(missing_bmad_files) > 0:
        print(f"\n⚠️  {len(missing_bmad_files)} files missing BMAD CSS:")
        for f in missing_bmad_files[:10]:
            print(f"   - {f}")
    else:
        print("\n   ✅ PERFECT! All files have BMAD CSS!")
    
    # Overall result
    print("\n" + "="*70)
    if results['has_old_css'] == 0 and results['has_bmad_css'] == results['total']:
        print("🎉 TEST PASSED: BMAD DEPLOYMENT 100% SUCCESSFUL!")
        return True
    else:
        print("⚠️  TEST WARNING: Some files need attention")
        return False

if __name__ == '__main__':
    success = test_bmad_integration()
    exit(0 if success else 1)


#!/usr/bin/env python3
"""
Validate that all 7 passes were successfully applied
Sample files and check for expected enhancements
"""

from pathlib import Path
import random

def validate_file(file_path):
    """Check if file has all expected enhancements"""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except:
        return {'error': 'Could not read'}
    
    checks = {
        'has_css': 'te-kete-professional.css' in content,
        'has_js': 'te-kete-professional.js' in content,
        'has_navigation': '<nav' in content.lower() or 'breadcrumb' in content.lower(),
        'has_walt': 'WALT' in content or 'Learning Objective' in content,
        'has_teacher_resources': 'Teacher Resources' in content or 'teacher-resources' in content,
        'has_cultural': 'whakataukī' in content.lower() or 'whaimana' in content.lower(),
        'has_assessment': 'Assessment' in content or 'assessment' in content.lower(),
        'has_accessibility': 'aria-label' in content or 'lang=' in content,
    }
    
    score = sum(checks.values())
    return {'checks': checks, 'score': score, 'max': len(checks)}

def main():
    public_dir = Path('public')
    
    # Sample 50 random files
    all_files = [f for f in public_dir.rglob('*.html') if 'backup' not in str(f).lower()]
    sample = random.sample(all_files, min(50, len(all_files)))
    
    print("🔍 VALIDATION: SAMPLING 50 ENHANCED FILES")
    print("="*60)
    
    results = []
    for file_path in sample:
        validation = validate_file(file_path)
        if 'error' not in validation:
            results.append(validation)
    
    # Calculate statistics
    avg_score = sum(r['score'] for r in results) / len(results)
    max_possible = results[0]['max'] if results else 8
    
    print(f"\n📊 VALIDATION RESULTS:")
    print(f"   Files sampled: {len(results)}")
    print(f"   Average score: {avg_score:.1f}/{max_possible} ({avg_score/max_possible*100:.1f}%)")
    
    # Check distribution
    check_totals = {}
    for result in results:
        for check, passed in result['checks'].items():
            check_totals[check] = check_totals.get(check, 0) + (1 if passed else 0)
    
    print(f"\n✅ ENHANCEMENT COVERAGE:")
    for check, count in sorted(check_totals.items(), key=lambda x: -x[1]):
        percentage = count / len(results) * 100
        status = "✅" if percentage >= 90 else "⚠️" if percentage >= 70 else "❌"
        print(f"   {status} {check}: {count}/{len(results)} ({percentage:.0f}%)")
    
    # Identify any gaps
    gaps = [check for check, count in check_totals.items() if count / len(results) < 0.9]
    if gaps:
        print(f"\n⚠️  Areas needing attention:")
        for gap in gaps:
            print(f"      - {gap}")
    else:
        print(f"\n✅ ALL ENHANCEMENTS SUCCESSFULLY APPLIED!")
    
    print(f"\n{'='*60}")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Batch process discovered content with quality gates
- Score files using rubric
- Apply technical fixes
- Categorize by tier
- Generate integration plan
"""

import json
from pathlib import Path
import re

def score_file(file_path):
    """Score a file using the quality rubric (0-10)"""
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except:
        return {'score': 0, 'cultural': 0, 'educational': 0, 'technical': 0, 'usability': 0, 'error': 'Could not read file'}
    
    scores = {'cultural': 0, 'educational': 0, 'technical': 0, 'usability': 0}
    
    # Cultural (0-3)
    cultural_markers = ['māori', 'maori', 'te reo', 'whakapapa', 'kaitiakitanga', 'mana', 'tikanga']
    cultural_count = sum(1 for marker in cultural_markers if marker.lower() in content.lower())
    if cultural_count >= 5:
        scores['cultural'] = 2
    elif cultural_count >= 2:
        scores['cultural'] = 1
    
    # Educational (0-3)
    educational_markers = ['learning objective', 'walt', 'wilf', 'success criteria', 'activity', 'assessment']
    educational_count = sum(1 for marker in educational_markers if marker.lower() in content.lower())
    if educational_count >= 4:
        scores['educational'] = 2
    elif educational_count >= 2:
        scores['educational'] = 1
    
    # Technical (0-2)
    has_css = 'te-kete-professional.css' in content
    has_proper_structure = '<!DOCTYPE html>' in content and content.count('<!DOCTYPE html>') == 1
    if has_css and has_proper_structure:
        scores['technical'] = 2
    elif has_proper_structure:
        scores['technical'] = 1
    
    # Usability (0-2)
    file_size = len(content)
    has_content = file_size > 5000  # Substantial content
    if has_content and educational_count >= 2:
        scores['usability'] = 1
    
    total = sum(scores.values())
    scores['score'] = total
    
    return scores

def categorize_by_score(score):
    """Categorize file by score"""
    if score >= 9:
        return 'exemplar'
    elif score >= 7:
        return 'professional'
    elif score >= 6:
        return 'usable'
    elif score >= 4:
        return 'needs_work'
    else:
        return 'discard'

def process_batch(file_paths, batch_num):
    """Process a batch of files"""
    results = []
    
    for file_path in file_paths:
        scores = score_file(file_path)
        tier = categorize_by_score(scores['score'])
        
        results.append({
            'file': str(file_path),
            'score': scores['score'],
            'cultural': scores['cultural'],
            'educational': scores['educational'],
            'technical': scores['technical'],
            'usability': scores['usability'],
            'tier': tier
        })
    
    return results

def main():
    # Load discovery results
    discovery_file = Path('content-discovery-results.json')
    if not discovery_file.exists():
        print("❌ content-discovery-results.json not found")
        return
    
    data = json.load(discovery_file.open())
    print(f"📊 Loaded {len(data)} discovered files\n")
    
    # Skip already processed (generated-resources-alpha)
    processed_dirs = ['public/generated-resources-alpha/']
    remaining = [
        item for item in data 
        if not any(pd in item.get('path', '') for pd in processed_dirs)
    ]
    
    print(f"✅ Already processed: {len(data) - len(remaining)}")
    print(f"📋 Remaining to process: {len(remaining)}\n")
    
    # Process first batch of 100
    batch_size = 100
    batch_1 = remaining[:batch_size]
    
    print(f"🔄 Processing Batch 1 ({len(batch_1)} files)...\n")
    
    file_paths = [Path(item['path']) for item in batch_1 if Path(item['path']).exists()]
    results = process_batch(file_paths, 1)
    
    # Summarize
    tiers = {}
    for result in results:
        tier = result['tier']
        tiers[tier] = tiers.get(tier, 0) + 1
    
    print("📊 BATCH 1 RESULTS:")
    print(f"   Exemplar (9-10): {tiers.get('exemplar', 0)}")
    print(f"   Professional (7-8): {tiers.get('professional', 0)}")
    print(f"   Usable (6): {tiers.get('usable', 0)}")
    print(f"   Needs Work (4-5): {tiers.get('needs_work', 0)}")
    print(f"   Discard (0-3): {tiers.get('discard', 0)}")
    
    # Save results
    output_file = Path('batch-1-scores.json')
    with output_file.open('w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Results saved to {output_file}")

if __name__ == '__main__':
    main()

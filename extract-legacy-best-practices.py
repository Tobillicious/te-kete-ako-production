#!/usr/bin/env python3
"""
Extract Best Practices from Legacy Backups
Mine the 8,318 backup items for design patterns, performance optimizations, and UX excellence
"""

from supabase import create_client
import re

supabase = create_client(
    'https://nlgldaqtubrlcqddppbq.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
)

def extract_legacy_patterns():
    print('🎨 EXTRACTING LEGACY BEST PRACTICES')
    print('=' * 80)
    print()
    
    # Get high-quality legacy resources
    result = supabase.table('graphrag_resources').select('*').like('file_path', '%backup%').gte('quality_score', 90).limit(50).execute()
    
    legacy_gems = result.data
    print(f'Found {len(legacy_gems)} high-quality legacy resources (Q:90+)')
    print()
    
    patterns_found = {
        'critical_css_inline': [],
        'preconnect_optimization': [],
        'auth_protection_overlay': [],
        'svg_filter_effects': [],
        'progressive_enhancement': [],
        'smooth_loading_states': [],
        'bilingual_navigation': [],
        'cultural_integration': []
    }
    
    # Analyze each legacy gem
    for gem in legacy_gems:
        file_path = gem.get('file_path', '')
        title = gem.get('title', 'Untitled')
        quality = gem.get('quality_score', 0)
        
        # Try to read the file to analyze patterns
        try:
            # Convert GraphRAG path to actual file path
            actual_path = file_path.replace('./', '')
            
            with open(actual_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Check for performance patterns
                if '<style>' in content and 'Critical' in content:
                    patterns_found['critical_css_inline'].append({
                        'file': file_path,
                        'title': title,
                        'quality': quality
                    })
                
                if 'preconnect' in content:
                    patterns_found['preconnect_optimization'].append({
                        'file': file_path,
                        'title': title
                    })
                
                if 'auth-protection' in content or 'Authenticating' in content:
                    patterns_found['auth_protection_overlay'].append({
                        'file': file_path,
                        'title': title
                    })
                
                if '<filter id=' in content or 'feGaussianBlur' in content:
                    patterns_found['svg_filter_effects'].append({
                        'file': file_path,
                        'title': title
                    })
                
                if 'loading-spinner' in content or 'loading-state' in content:
                    patterns_found['smooth_loading_states'].append({
                        'file': file_path,
                        'title': title
                    })
                    
        except Exception as e:
            # File might not exist or be accessible
            pass
    
    # Report findings
    print('📋 PATTERNS DISCOVERED:')
    print('-' * 80)
    
    for pattern_name, examples in patterns_found.items():
        if examples:
            print(f'\n{pattern_name.replace("_", " ").title()}:')
            print(f'  Found in {len(examples)} legacy files')
            for example in examples[:3]:
                print(f'    - {example["title"][:50]} (Q:{example.get("quality", "N/A")})')
    
    print()
    print('=' * 80)
    print('🎯 RECOMMENDATION: Synthesize these patterns into current site!')
    print('=' * 80)
    
    return patterns_found

if __name__ == "__main__":
    patterns = extract_legacy_patterns()
    
    # Save findings
    import json
    with open('legacy-patterns-extracted.json', 'w') as f:
        json.dump(patterns, f, indent=2)
    
    print('\n✅ Patterns saved to legacy-patterns-extracted.json')


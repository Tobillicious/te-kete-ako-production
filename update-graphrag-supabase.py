#!/usr/bin/env python3
"""
Update GraphRAG (Supabase resources table) with ALL site content
Scans 1,071+ HTML pages and adds them to database for agent coordination
"""

import os
import re
from pathlib import Path
from datetime import datetime

def extract_title(content):
    """Extract title from HTML"""
    match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    if match:
        return match.group(1).strip()[:200]
    match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE)
    if match:
        return re.sub(r'<[^>]+>', '', match.group(1)).strip()[:200]
    return "Untitled"

def extract_description(content):
    """Extract meta description"""
    match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)', content, re.IGNORECASE)
    if match:
        return match.group(1).strip()[:500]
    # Fallback: first paragraph
    match = re.search(r'<p[^>]*>(.*?)</p>', content, re.IGNORECASE)
    if match:
        return re.sub(r'<[^>]+>', '', match.group(1)).strip()[:500]
    return ""

def determine_type(path_str):
    """Determine resource type from path"""
    path_lower = path_str.lower()
    if 'handout' in path_lower:
        return 'handout'
    elif 'lesson' in path_lower:
        return 'lesson'
    elif 'game' in path_lower:
        return 'game'
    elif 'unit' in path_lower:
        return 'unit-plan'
    elif 'assessment' in path_lower or 'rubric' in path_lower:
        return 'assessment'
    elif 'activity' in path_lower or 'activities' in path_lower:
        return 'activity'
    else:
        return 'interactive'

def determine_subject(content, path_str):
    """Determine subject from content and path"""
    text = (content + " " + path_str).lower()
    
    if any(term in text for term in ['māori', 'te reo', 'cultural', 'whakapapa', 'tikanga']):
        return 'Te Ao Māori'
    elif any(term in text for term in ['math', 'algebra', 'geometry', 'statistics']):
        return 'Mathematics'
    elif any(term in text for term in ['science', 'climate', 'ecology', 'physics']):
        return 'Science'
    elif any(term in text for term in ['english', 'writing', 'literacy', 'writers']):
        return 'English'
    elif any(term in text for term in ['social', 'society', 'systems', 'government']):
        return 'Social Studies'
    elif any(term in text for term in ['digital', 'technology', 'ai', 'coding']):
        return 'Digital Technology'
    else:
        return 'General'

def scan_all_resources():
    """Scan all HTML files and prepare for GraphRAG"""
    public_dir = Path("public")
    resources = []
    
    for html_file in public_dir.rglob("*.html"):
        # Skip backup/temp files
        if any(skip in str(html_file) for skip in ['.backup', '.tmp', '.batch', 'node_modules']):
            continue
            
        try:
            content = html_file.read_text(encoding='utf-8', errors='ignore')
            path_str = str(html_file.relative_to(Path(".")))
            
            resource = {
                'title': extract_title(content),
                'description': extract_description(content),
                'path': path_str,
                'type': determine_type(path_str),
                'subject': determine_subject(content, path_str),
                'level': 'Year 7-13',  # Could be more sophisticated
                'cultural_elements': {
                    'has_maori_content': 'māori' in content.lower(),
                    'has_whakatauaki': 'whakataukī' in content.lower(),
                    'te_reo_present': bool(re.search(r'[āēīōū]', content))
                },
                'tags': [],
                'difficulty_level': 'intermediate',
                'estimated_duration_minutes': 45
            }
            
            resources.append(resource)
            
        except Exception as e:
            print(f"⚠️ Error: {html_file}: {e}")
            continue
    
    return resources

def main():
    """Main execution"""
    print("🧠 KAITIAKI ARONUI - GraphRAG Full Update")
    print("=" * 60)
    
    print("\n📊 Scanning all HTML files...")
    resources = scan_all_resources()
    
    print(f"✅ Found {len(resources)} resources to index")
    
    # Save for import
    import json
    with open('graphrag-full-index-oct14.json', 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'total': len(resources),
            'resources': resources
        }, f, indent=2)
    
    print(f"\n💾 Saved to: graphrag-full-index-oct14.json")
    
    # Print SQL for bulk insert
    print(f"\n📋 To update Supabase GraphRAG:")
    print(f"   Use MCP Supabase tool to bulk insert from JSON")
    print(f"   OR import via Supabase dashboard")
    
    # Stats
    by_type = {}
    for r in resources:
        rtype = r['type']
        by_type[rtype] = by_type.get(rtype, 0) + 1
    
    print(f"\n📈 Resource Breakdown:")
    for rtype, count in sorted(by_type.items(), key=lambda x: x[1], reverse=True):
        print(f"   {rtype}: {count}")
    
    print(f"\n✅ GraphRAG index ready for import!")
    print(f"   Agents will be able to coordinate with FULL site knowledge!")

if __name__ == "__main__":
    main()


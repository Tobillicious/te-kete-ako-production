#!/usr/bin/env python3
"""
INDEX EVERYTHING TO GRAPHRAG!
Complete automated indexing of entire codebase
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import json

def extract_metadata(html_path):
    """Extract metadata from any HTML file"""
    try:
        with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # Extract title
        title_tag = soup.find('title')
        title = title_tag.text.strip() if title_tag else Path(html_path).stem.replace('-', ' ').title()
        title = title[:200]  # Limit length
        
        # Detect cultural elements
        has_te_reo = bool(re.search(r'\b(māori|whānau|kaitiakitanga|whakapapa|tikanga|mātauranga|aroha|taonga|whenua|pūrākau|whakataukī)\b', content, re.I))
        has_whakataukī = bool(re.search(r'whakataukī', content, re.I))
        cultural_context = has_te_reo or has_whakataukī
        
        # Detect subject from path and content
        subject = detect_subject(html_path, content)
        year_level = detect_year_level(html_path, content)
        resource_type = detect_resource_type(html_path)
        
        # Calculate quality
        quality_score = calculate_quality(soup, content, cultural_context)
        
        return {
            'file_path': f'/public/{html_path.relative_to(Path("/Users/admin/Documents/te-kete-ako-clean/public"))}',
            'title': title,
            'resource_type': resource_type,
            'subject': subject,
            'year_level': year_level,
            'quality_score': quality_score,
            'cultural_context': cultural_context,
            'has_whakataukī': has_whakataukī,
            'has_te_reo': has_te_reo
        }
    except Exception as e:
        print(f"Error: {html_path.name}: {str(e)[:50]}")
        return None

def detect_subject(path, content):
    """Detect subject from path and content"""
    p = str(path).lower()
    c = content.lower()
    
    # Path-based
    if any(x in p for x in ['math', 'algebra', 'geometry', 'calculus', 'statistics']): return 'Mathematics'
    if any(x in p for x in ['science', 'ecology', 'physics', 'chemistry', 'biology']): return 'Science'
    if any(x in p for x in ['english', 'writing', 'writers', 'literacy']): return 'English'
    if any(x in p for x in ['digital', 'technology', 'coding']): return 'Technology'
    if any(x in p for x in ['social', 'history', 'geography', 'walker']): return 'Social Studies'
    if any(x in p for x in ['arts', 'visual', 'music', 'drama', 'haka']): return 'Arts'
    if any(x in p for x in ['health', 'pe', 'wellbeing', 'hauora']): return 'Health & PE'
    if any(x in p for x in ['te-reo', 'māori', 'te reo']): return 'Te Reo Māori'
    if any(x in p for x in ['teacher', 'professional']): return 'Professional Development'
    
    # Content-based fallback
    if any(x in c for x in ['algebra', 'equation', 'geometry']): return 'Mathematics'
    if any(x in c for x in ['ecosystem', 'climate', 'biology']): return 'Science'
    
    return 'Cross-Curricular'

def detect_year_level(path, content):
    """Detect year level"""
    p = str(path).lower()
    
    # Year in path
    for y in range(1, 14):
        if f'y{y}' in p or f'year {y}' in p or f'year-{y}' in p:
            return f'Year {y}'
    
    # Level in path
    level_match = re.search(r'level[- ](\d+)', p)
    if level_match:
        level = int(level_match.group(1))
        year_map = {1: '5-6', 2: '7-8', 3: '7-8', 4: '9-10', 5: '9-10', 6: '11-12', 7: '11-13'}
        return f'Years {year_map.get(level, "7-13")}'
    
    # Senior/Junior
    if 'senior' in p: return 'Years 11-13'
    if 'junior' in p: return 'Years 7-9'
    if 'teacher' in p or 'professional' in p: return 'Teachers'
    if 'student' in p: return 'Students'
    
    return 'Years 7-13'

def detect_resource_type(path):
    """Detect resource type from path"""
    p = str(path).lower()
    
    if '/lessons/' in p or 'lesson-plan' in p or 'lesson-' in p: return 'lesson'
    if '/handouts/' in p or 'handout' in p: return 'handout'
    if '/games/' in p or 'game' in p or 'wordle' in p or 'wordsearch' in p: return 'interactive_game'
    if '/assessments/' in p or 'rubric' in p or 'assessment' in p: return 'assessment'
    if '/units/' in p and 'index.html' in p: return 'unit'
    if 'hub' in p: return 'hub_page'
    if '/components/' in p: return 'component'
    if 'activity' in p or 'practice' in p: return 'activity'
    if 'dashboard' in p: return 'dashboard'
    if 'toolkit' in p: return 'toolkit'
    if 'interactive' in p: return 'interactive'
    if '/tools/' in p: return 'tool'
    if p.endswith('index.html'): return 'index_page'
    
    return 'resource'

def calculate_quality(soup, content, cultural):
    """Calculate quality score"""
    score = 75
    
    if soup.find(['h1', 'h2']): score += 5
    if soup.find('nav'): score += 3
    if cultural: score += 10
    if soup.find('script'): score += 4
    if len(content) > 5000: score += 3
    if soup.find('link', href=re.compile(r'te-kete')): score += 5
    
    return min(score, 100)

def scan_and_index():
    """Scan entire public directory"""
    base = Path('/Users/admin/Documents/te-kete-ako-clean/public')
    all_html = list(base.rglob('*.html'))
    
    print(f"🔍 Found {len(all_html)} HTML files")
    
    indexed = []
    sql_batches = []
    
    for i, html_file in enumerate(all_html):
        if i % 100 == 0:
            print(f"  Processing {i}/{len(all_html)}...")
        
        metadata = extract_metadata(html_file)
        if metadata:
            indexed.append(metadata)
            
            # Generate SQL
            sql = f"""INSERT INTO graphrag_resources (file_path, resource_type, title, subject, year_level, quality_score, cultural_context, has_whakataukī, has_te_reo, metadata) VALUES ('{metadata['file_path']}', '{metadata['resource_type']}', $${metadata['title']}$$, '{metadata['subject']}', '{metadata['year_level']}', {metadata['quality_score']}, {str(metadata['cultural_context']).lower()}, {str(metadata['has_whakataukī']).lower()}, {str(metadata['has_te_reo']).lower()}, '{{"auto_indexed": true}}'::jsonb) ON CONFLICT (file_path) DO UPDATE SET quality_score = EXCLUDED.quality_score, cultural_context = EXCLUDED.cultural_context;"""
            
            sql_batches.append(sql)
    
    # Save to SQL file
    with open('index-everything.sql', 'w', encoding='utf-8') as f:
        f.write("-- INDEX EVERYTHING TO GRAPHRAG\n")
        f.write(f"-- Total files: {len(indexed)}\n")
        f.write(f"-- Auto-generated: {len(sql_batches)} SQL statements\n\n")
        f.write('\n'.join(sql_batches))
    
    print(f"\n✅ Indexed {len(indexed)} resources")
    print(f"📄 SQL saved to: index-everything.sql")
    
    # Stats
    by_type = {}
    by_subject = {}
    cultural_count = sum(1 for r in indexed if r['cultural_context'])
    
    for r in indexed:
        by_type[r['resource_type']] = by_type.get(r['resource_type'], 0) + 1
        by_subject[r['subject']] = by_subject.get(r['subject'], 0) + 1
    
    print(f"\n📊 BREAKDOWN:")
    print(f"  Cultural: {cultural_count} ({cultural_count*100//len(indexed)}%)")
    print(f"  Top types: {dict(sorted(by_type.items(), key=lambda x: -x[1])[:10])}")
    print(f"  Top subjects: {dict(sorted(by_subject.items(), key=lambda x: -x[1])[:10])}")

if __name__ == '__main__':
    print("🧠 INDEX EVERYTHING TO GRAPHRAG")
    print("=" * 70)
    scan_and_index()
    print("\n🎯 Ready to import to GraphRAG!")

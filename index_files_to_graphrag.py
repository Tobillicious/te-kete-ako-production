#!/usr/bin/env python3
import os
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime

def extract_metadata_from_html(file_path):
    """Extract metadata from HTML file"""
    try:
        with open(f"/Users/admin/Documents/te-kete-ako-clean/public/{file_path}", 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract title
        title_tag = soup.find('title')
        title = title_tag.get_text().strip() if title_tag else "Untitled"
        
        # Extract description
        desc_tag = soup.find('meta', {'name': 'description'})
        description = desc_tag.get('content', '').strip() if desc_tag else ""
        
        # Determine resource type
        resource_type = determine_resource_type(file_path, content)
        
        # Extract year level
        year_level = extract_year_level(content, file_path)
        
        # Extract subject
        subject = extract_subject(content, file_path)
        
        # Check for cultural elements
        has_whakatauki = 'whakataukī' in content.lower() or 'whakatauki' in content.lower()
        has_te_reo = bool(re.search(r'[āēīōūĀĒĪŌŪ]', content))
        
        # Generate content preview
        content_preview = description or title
        
        # Calculate quality score (simplified heuristic)
        quality_score = calculate_quality_score(content, has_whakatauki, has_te_reo)
        
        return {
            'file_path': f'/{file_path}',
            'title': title,
            'resource_type': resource_type,
            'quality_score': quality_score,
            'cultural_context': has_te_reo or has_whakatauki,
            'year_level': year_level,
            'subject': subject,
            'has_whakataukī': has_whakatauki,
            'has_te_reo': has_te_reo,
            'content_preview': content_preview[:500],  # First 500 chars
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def determine_resource_type(file_path, content):
    """Determine resource type from path and content"""
    if '/lessons/' in file_path:
        return 'lesson'
    elif '/handouts/' in file_path:
        return 'handout'
    elif '/units/' in file_path:
        return 'unit'
    elif '/games/' in file_path:
        return 'game'
    elif 'hub' in file_path.lower():
        return 'hub'
    elif 'dashboard' in file_path.lower():
        return 'dashboard'
    elif 'index' in file_path.lower():
        return 'index'
    else:
        return 'other'

def extract_year_level(content, file_path):
    """Extract year level from content or path"""
    # Look for year patterns in content
    year_patterns = [
        r'year[ -](\d+)', r'y(\d+)', r'level[ -](\d+)',
        r'class[ -](\d+)', r'grade[ -](\d+)'
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return match.group(1)
    
    # Look for year in path
    path_match = re.search(r'/(?:year-|y)(\d+)/', file_path, re.IGNORECASE)
    if path_match:
        return path_match.group(1)
    
    return None

def extract_subject(content, file_path):
    """Extract subject from content or path"""
    subjects = [
        'mathematics', 'math', 'science', 'english', 'social studies', 
        'digital technologies', 'arts', 'health', 'physical education',
        'te ao māori', 'languages', 'music', 'drama', 'dance'
    ]
    
    # Check path first
    for subject in subjects:
        if subject.replace(' ', '-') in file_path.lower():
            return subject.title()
    
    # Check content
    content_lower = content.lower()
    for subject in subjects:
        if subject in content_lower:
            return subject.title()
    
    return 'General'

def calculate_quality_score(content, has_whakatauki, has_te_reo):
    """Calculate a quality score based on content analysis"""
    score = 50  # Base score
    
    # Length bonus
    if len(content) > 10000:
        score += 20
    elif len(content) > 5000:
        score += 10
    
    # Cultural integration
    if has_te_reo:
        score += 15
    if has_whakatauki:
        score += 10
    
    # Structure indicators
    if '<h1' in content:
        score += 5
    if '<h2' in content:
        score += 5
    if 'learning objective' in content.lower():
        score += 5
    
    return min(score, 100)

def main():
    # Load files to index
    with open('files_to_index.json', 'r') as f:
        files_to_index = json.load(f)
    
    print(f"Starting to process {len(files_to_index)} files...")
    
    resources_to_insert = []
    for i, file_path in enumerate(files_to_index[:100]):  # Start with first 100
        print(f"Processing {i+1}/{len(files_to_index)}: {file_path}")
        
        metadata = extract_metadata_from_html(file_path)
        if metadata:
            resources_to_insert.append(metadata)
    
    print(f"Extracted metadata for {len(resources_to_insert)} files")
    
    # Write to a file for manual review before insertion
    with open('resources_to_insert.json', 'w') as f:
        json.dump(resources_to_insert, f, indent=2, default=str)
    
    print(f"Written {len(resources_to_insert)} resources to resources_to_insert.json")
    print("Ready for manual review and GraphRAG insertion")

if __name__ == "__main__":
    main()

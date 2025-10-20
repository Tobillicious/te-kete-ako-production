#!/usr/bin/env python3
"""
Sync Priority Files to GraphRAG
Focus on hub pages, index pages, and main lessons first
"""

import os
import json
import re
from supabase import create_client

# Supabase connection
supabase = create_client(
    'https://nlgldaqtubrlcqddppbq.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
)

def extract_content_info(file_path):
    """Extract content information from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else os.path.basename(file_path)
        
        # Extract content preview (first 200 chars of visible text)
        text_content = re.sub(r'<[^>]+>', '', content)
        text_content = re.sub(r'\s+', ' ', text_content).strip()
        content_preview = text_content[:200] + '...' if len(text_content) > 200 else text_content
        
        # Determine resource type
        if 'hub' in file_path.lower():
            resource_type = 'Hub Page'
        elif 'lesson' in file_path.lower():
            resource_type = 'Lesson'
        elif 'assessment' in file_path.lower():
            resource_type = 'Assessment'
        elif 'resource' in file_path.lower():
            resource_type = 'Resource'
        elif 'index' in file_path.lower():
            resource_type = 'Hub Page'
        else:
            resource_type = 'Page'
        
        # Determine subject
        if 'math' in file_path.lower() or 'algebra' in file_path.lower() or 'geometry' in file_path.lower():
            subject = 'Mathematics'
        elif 'science' in file_path.lower() or 'ecology' in file_path.lower():
            subject = 'Science'
        elif 'english' in file_path.lower() or 'writing' in file_path.lower():
            subject = 'English'
        elif 'social' in file_path.lower() or 'systems' in file_path.lower():
            subject = 'Social Studies'
        elif 'digital' in file_path.lower() or 'ai' in file_path.lower():
            subject = 'Digital Technologies'
        elif 'te-ao' in file_path.lower() or 'maori' in file_path.lower():
            subject = 'Te Ao Māori'
        else:
            subject = 'Cross-Curricular'
        
        # Determine year level
        year_match = re.search(r'y(\d+)', file_path.lower())
        if year_match:
            year_level = f"Year {year_match.group(1)}"
        elif 'teachers' in file_path.lower():
            year_level = 'Teachers'
        else:
            year_level = 'Years 7-13'
        
        # Check for cultural context
        cultural_context = any(word in content.lower() for word in ['māori', 'te reo', 'tikanga', 'whakataukī', 'kaitiakitanga'])
        
        # Check for te reo
        has_te_reo = any(word in content.lower() for word in ['māori', 'te reo', 'whakataukī'])
        
        # Check for whakataukī
        has_whakataukī = 'whakataukī' in content.lower() or 'whakatauki' in content.lower()
        
        # Calculate quality score based on content
        quality_score = 60  # Base score
        if cultural_context:
            quality_score += 20
        if has_te_reo:
            quality_score += 10
        if has_whakataukī:
            quality_score += 10
        if 'hub' in file_path.lower():
            quality_score += 10
        if 'lesson' in file_path.lower():
            quality_score += 5
        
        quality_score = min(quality_score, 95)  # Cap at 95
        
        return {
            'file_path': file_path,
            'title': title,
            'content_preview': content_preview,
            'resource_type': resource_type,
            'subject': subject,
            'year_level': year_level,
            'cultural_context': cultural_context,
            'has_te_reo': has_te_reo,
            'has_whakataukī': has_whakataukī,
            'quality_score': quality_score
        }
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def sync_priority_files():
    """Sync priority files to GraphRAG"""
    
    # Get existing files in GraphRAG
    result = supabase.table('graphrag_resources').select('file_path').execute()
    existing_files = set(r['file_path'] for r in result.data)
    
    # Find priority files to sync
    priority_patterns = ['index.html', 'hub.html', 'lesson-', 'assessment', 'resources']
    priority_files = []
    
    for root, dirs, files in os.walk('public'):
        for file in files:
            if file.endswith('.html'):
                rel_path = os.path.relpath(os.path.join(root, file), 'public')
                full_path = f'./public/{rel_path}'
                
                if full_path not in existing_files:
                    # Check if it's a priority file
                    if any(pattern in file.lower() or pattern in rel_path.lower() for pattern in priority_patterns):
                        priority_files.append(full_path)
    
    print(f"Found {len(priority_files)} priority files to sync")
    
    # Sync files in batches
    batch_size = 50
    synced_count = 0
    
    for i in range(0, len(priority_files), batch_size):
        batch = priority_files[i:i+batch_size]
        batch_data = []
        
        for file_path in batch:
            content_info = extract_content_info(file_path)
            if content_info:
                batch_data.append(content_info)
        
        if batch_data:
            try:
                result = supabase.table('graphrag_resources').insert(batch_data).execute()
                synced_count += len(batch_data)
                print(f"Synced batch {i//batch_size + 1}: {len(batch_data)} files")
            except Exception as e:
                print(f"Error syncing batch {i//batch_size + 1}: {e}")
    
    print(f"Total synced: {synced_count} files")
    return synced_count

if __name__ == "__main__":
    sync_priority_files()

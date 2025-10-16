#!/usr/bin/env python3
"""
KNOWLEDGE SYNTHESIS PIPELINE
Extracts critical information from archived MD files and stores it in GraphRAG
"""

import os
import re
from datetime import datetime
from supabase import create_client, Client

# Initialize Supabase
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjQ5NjkwOTQsImV4cCI6MjA0MDU0NTA5NH0.wq5FqLT9qx9WoLqsjLZKM7xhqSWRpXCJhNVL0BdVlRU"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def extract_key_decisions(content):
    """Extract key decisions and achievements from MD content"""
    decisions = []
    
    # Look for common patterns
    patterns = [
        r'##\s*(?:Key Decisions?|Achievements?|Completed?|Changes?)(.*?)(?=##|\Z)',
        r'✅\s*([^\n]+)',
        r'COMPLETED?:\s*([^\n]+)',
        r'ACHIEVEMENT:\s*([^\n]+)',
        r'DECISION:\s*([^\n]+)',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
        for match in matches:
            text = match.strip()
            if text and len(text) > 10 and len(text) < 500:
                decisions.append(text[:300])  # Truncate long ones
    
    return list(set(decisions))[:20]  # Top 20 unique decisions

def extract_technical_specs(content):
    """Extract technical specifications and implementation details"""
    specs = {}
    
    # Look for file paths
    files = re.findall(r'`([a-zA-Z0-9_\-./]+\.[a-zA-Z]{2,4})`', content)
    if files:
        specs['files_mentioned'] = list(set(files))[:30]
    
    # Look for URLs  
    urls = re.findall(r'https?://[^\s\)]+', content)
    if urls:
        specs['urls'] = list(set(urls))[:10]
    
    # Look for code blocks
    code_blocks = re.findall(r'```(?:python|javascript|sql|bash)\n(.*?)```', content, re.DOTALL)
    if code_blocks:
        specs['code_snippets_count'] = len(code_blocks)
    
    return specs

def extract_agent_names(content):
    """Extract agent names mentioned in the document"""
    agent_patterns = [
        r'Agent[- ]?\d+',
        r'agent[- ]?\d+',
        r'Kaitiaki',
        r'Kaiārahi',
    ]
    
    agents = []
    for pattern in agent_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        agents.extend(matches)
    
    return list(set(agents))[:10]

def process_archived_file(filepath, filename):
    """Process a single archived MD file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract knowledge
        key_decisions = extract_key_decisions(content)
        tech_specs = extract_technical_specs(content)
        agents = extract_agent_names(content)
        
        # Determine document type
        doc_type = 'coordination'
        if 'AUTH' in filename or 'auth' in filename.lower():
            doc_type = 'authentication'
        elif 'CSS' in filename or 'style' in filename.lower():
            doc_type = 'styling'
        elif 'GRAPHRAG' in filename or 'knowledge' in filename.lower():
            doc_type = 'knowledge_management'
        elif 'AGENT' in filename or 'coordination' in filename.lower():
            doc_type = 'agent_coordination'
        elif 'DEPLOYMENT' in filename or 'production' in filename.lower():
            doc_type = 'deployment'
        
        return {
            'filename': filename,
            'doc_type': doc_type,
            'key_decisions': key_decisions,
            'tech_specs': tech_specs,
            'agents_involved': agents,
            'word_count': len(content.split()),
            'archived_at': datetime.now().isoformat()
        }
    
    except Exception as e:
        print(f"   ⚠️  Error processing {filename}: {e}")
        return None

def store_in_graphrag(knowledge_items):
    """Store extracted knowledge in GraphRAG system"""
    
    stored = 0
    for item in knowledge_items:
        # Create a knowledge entry
        try:
            result = supabase.table('agent_knowledge').insert({
                'source_type': 'archived_md',
                'source_name': item['filename'],
                'doc_type': item['doc_type'],
                'key_insights': item['key_decisions'],
                'technical_details': item['tech_specs'],
                'agents_involved': item['agents_involved'],
                'created_at': item['archived_at']
            }).execute()
            
            print(f"   ✅ Stored: {item['filename']} ({item['doc_type']})")
            stored += 1
            
        except Exception as e:
            print(f"   ⚠️  Failed to store {item['filename']}: {e}")
    
    return stored

def main():
    print("\n" + "="*70)
    print("📚 KNOWLEDGE SYNTHESIS PIPELINE")
    print("   Extracting Critical Information from Archived MDs")
    print("="*70 + "\n")
    
    archive_dir = '/Users/admin/Documents/te-kete-ako-clean/docs/archive/synthesis-oct16-evening'
    
    if not os.path.exists(archive_dir):
        print(f"❌ Archive directory not found: {archive_dir}")
        return
    
    # Process all archived files
    knowledge_items = []
    
    print("📖 SCANNING ARCHIVED FILES...")
    print()
    
    for filename in os.listdir(archive_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(archive_dir, filename)
            print(f"   Processing: {filename}")
            
            item = process_archived_file(filepath, filename)
            if item and item['key_decisions']:
                knowledge_items.append(item)
    
    print(f"\n✅ Processed {len(knowledge_items)} files with extractable knowledge\n")
    
    # Summary by type
    print("📊 KNOWLEDGE SUMMARY BY TYPE:")
    print()
    
    types = {}
    for item in knowledge_items:
        doc_type = item['doc_type']
        types[doc_type] = types.get(doc_type, 0) + 1
    
    for doc_type, count in sorted(types.items()):
        print(f"   {doc_type}: {count} documents")
    
    print("\n" + "="*70)
    
    # Store in GraphRAG
    print("\n💾 STORING IN GRAPHRAG...")
    print()
    
    stored = store_in_graphrag(knowledge_items)
    
    print("\n" + "="*70)
    print("✅ KNOWLEDGE SYNTHESIS COMPLETE!")
    print(f"   Extracted insights from {len(knowledge_items)} documents")
    print(f"   Stored {stored} entries in GraphRAG")
    print(f"   Available for collective intelligence")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()

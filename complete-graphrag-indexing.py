#!/usr/bin/env python3
"""
COMPLETE GRAPHRAG INDEXING - Final Mission
Systematically index ALL unmapped content in the codebase
"""

import os
import json
from pathlib import Path
from supabase import create_client
from datetime import datetime

# Supabase setup
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_KEY:
    print("❌ ERROR: SUPABASE_KEY environment variable not set")
    exit(1)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Track stats
stats = {
    "total_scanned": 0,
    "already_indexed": 0,
    "newly_indexed": 0,
    "errors": 0,
    "categories": {}
}

def is_indexed(file_path):
    """Check if file already in GraphRAG"""
    try:
        result = supabase.table('graphrag_resources').select('file_path').eq('file_path', file_path).execute()
        return len(result.data) > 0
    except:
        return False

def categorize_file(file_path):
    """Determine resource type and metadata"""
    path_str = str(file_path)
    
    # Agent/Dev infrastructure
    if path_str.startswith('_'):
        return "Infrastructure", {"category": "agent_system"}
    
    # Units
    if '/units/' in path_str and '/lessons/' in path_str:
        return "Lesson", {"unit": path_str.split('/units/')[1].split('/')[0]}
    elif '/units/' in path_str and 'index.html' in path_str:
        return "Unit Plan", {"unit": path_str.split('/units/')[1].split('/')[0]}
    
    # Games
    if '/games/' in path_str:
        return "Interactive Game", {"category": "game"}
    
    # Hub pages
    if '-hub.html' in path_str:
        return "Hub Page", {"category": "navigation"}
    
    # Components
    if '/components/' in path_str:
        return "Component", {"category": "ui_component"}
    
    # JavaScript/CSS
    if path_str.endswith('.js'):
        return "JavaScript", {"category": "code"}
    elif path_str.endswith('.css'):
        return "Stylesheet", {"category": "design"}
    
    # Python scripts
    if path_str.endswith('.py'):
        return "Python Script", {"category": "automation"}
    
    # Handouts/Resources
    if '/handouts/' in path_str or 'handout' in path_str.lower():
        return "Handout", {"category": "student_resource"}
    
    # Legacy backup
    if path_str.startswith('backup_before_css_migration'):
        return "Legacy Resource", {"era": "pre_oct18", "dialectical_analysis": True}
    
    # Default
    return "Page", {"category": "general"}

def extract_cultural_signals(file_path, content=None):
    """Detect Te Ao Māori content"""
    path_lower = str(file_path).lower()
    
    cultural_context = any([
        'maori' in path_lower,
        'te-reo' in path_lower,
        'whakatau' in path_lower,
        'kaitiaki' in path_lower,
        'te-ao' in path_lower,
        'virtual-marae' in path_lower
    ])
    
    has_te_reo = 'te-reo' in path_lower or 'maori' in path_lower
    has_whakatauaki = 'whakatau' in path_lower
    
    return cultural_context, has_te_reo, has_whakatauaki

def index_file(file_path):
    """Index a single file to GraphRAG"""
    global stats
    
    stats["total_scanned"] += 1
    
    # Skip if already indexed
    if is_indexed(file_path):
        stats["already_indexed"] += 1
        if stats["total_scanned"] % 100 == 0:
            print(f"⏩ Progress: {stats['total_scanned']} scanned, {stats['already_indexed']} already indexed, {stats['newly_indexed']} new")
        return
    
    try:
        # Categorize
        resource_type, metadata = categorize_file(file_path)
        cultural_context, has_te_reo, has_whakatauaki = extract_cultural_signals(file_path)
        
        # Determine quality score (conservative estimates)
        quality_score = 75  # Default
        if resource_type == "Lesson":
            quality_score = 80
        elif resource_type == "Unit Plan":
            quality_score = 85
        elif resource_type == "Legacy Resource":
            quality_score = 70  # Lower initially, can upgrade after dialectical analysis
        elif resource_type == "Interactive Game":
            quality_score = 65  # Known quality issues
        
        # Subject extraction
        subject = "General"
        if 'mathematics' in str(file_path).lower() or 'y8-perimeter' in str(file_path).lower():
            subject = "Mathematics"
        elif 'science' in str(file_path).lower() or 'ecology' in str(file_path).lower():
            subject = "Science"
        elif 'english' in str(file_path).lower() or 'writers-toolkit' in str(file_path).lower():
            subject = "English"
        elif 'te-ao-maori' in str(file_path).lower() or cultural_context:
            subject = "Te Ao Māori"
        elif 'digital' in str(file_path).lower() or 'kaitiakitanga' in str(file_path).lower():
            subject = "Digital Technologies"
        
        # Build title from filename
        title = Path(file_path).stem.replace('-', ' ').replace('_', ' ').title()
        if len(title) > 100:
            title = title[:97] + "..."
        
        # Enhanced metadata
        metadata.update({
            "indexed_date": datetime.now().isoformat(),
            "indexer": "complete-graphrag-indexing.py",
            "needs_relationship_building": True
        })
        
        # Insert
        data = {
            "file_path": file_path,
            "resource_type": resource_type,
            "title": title,
            "quality_score": quality_score,
            "cultural_context": cultural_context,
            "subject": subject,
            "has_whakataukī": has_whakatauaki,
            "has_te_reo": has_te_reo,
            "metadata": json.dumps(metadata)
        }
        
        supabase.table('graphrag_resources').insert(data).execute()
        
        stats["newly_indexed"] += 1
        stats["categories"][resource_type] = stats["categories"].get(resource_type, 0) + 1
        
        if stats["newly_indexed"] % 50 == 0:
            print(f"✅ Indexed {stats['newly_indexed']} new resources...")
        
    except Exception as e:
        stats["errors"] += 1
        if stats["errors"] < 10:  # Only print first 10 errors
            print(f"❌ Error indexing {file_path}: {e}")

def scan_directory(directory, extensions=['.html', '.js', '.css', '.py']):
    """Recursively scan directory for indexable files"""
    print(f"\n🔍 Scanning {directory}...")
    
    for root, dirs, files in os.walk(directory):
        # Skip unwanted directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', '.git']]
        
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                # Make path relative to repo root
                file_path = file_path.replace('/Users/admin/Documents/te-kete-ako-clean/', '')
                index_file(file_path)

def main():
    print("🚀 COMPLETE GRAPHRAG INDEXING - STARTING")
    print("=" * 60)
    
    # Scan all major directories
    directories_to_scan = [
        'public',
        'backup_before_css_migration',
        '.',  # Root level files
    ]
    
    for directory in directories_to_scan:
        if os.path.exists(directory):
            scan_directory(directory)
    
    print("\n" + "=" * 60)
    print("📊 FINAL STATISTICS:")
    print(f"Total files scanned: {stats['total_scanned']}")
    print(f"Already indexed: {stats['already_indexed']}")
    print(f"Newly indexed: {stats['newly_indexed']}")
    print(f"Errors: {stats['errors']}")
    print("\n📁 NEW RESOURCES BY TYPE:")
    for resource_type, count in sorted(stats['categories'].items(), key=lambda x: -x[1]):
        print(f"  {resource_type}: {count}")
    
    print("\n✅ GRAPHRAG INDEXING COMPLETE!")
    print(f"🎯 Total GraphRAG resources: ~{stats['already_indexed'] + stats['newly_indexed']}")

if __name__ == "__main__":
    main()


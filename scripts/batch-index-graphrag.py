#!/usr/bin/env python3
"""
BATCH GRAPHRAG INDEXER - Te Kete Ako
=====================================
Scans /public/ directory recursively and indexes all HTML files into graphrag_resources table.

CRITICAL: Deployment blocker - 1,294 files missing from GraphRAG (only 843/2,137 indexed = 39%)

Author: Cursor AI Agent
Date: October 23, 2025
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional
import json
from datetime import datetime

# Supabase connection details
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM"

# Directory configuration
PUBLIC_DIR = Path(__file__).parent.parent / "public"
PRIORITY_DIRS = [
    "lessons",
    "units", 
    "handouts",
    "integrated-lessons",
    "generated-resources-alpha"
]

# Subject detection patterns
SUBJECT_PATTERNS = {
    "Mathematics": [r"math", r"algebra", r"geometry", r"statistics", r"calculus"],
    "Science": [r"science", r"biology", r"chemistry", r"physics", r"ecology"],
    "English": [r"english", r"writing", r"reading", r"literature", r"literacy"],
    "Social Studies": [r"social", r"history", r"geography", r"civics"],
    "Digital Technologies": [r"digital", r"tech", r"coding", r"programming", r"computer"],
    "Te Ao Māori": [r"maori", r"te-reo", r"te-ao", r"whakataukī", r"tikanga"],
    "Health & PE": [r"health", r"pe", r"physical", r"wellbeing"],
    "The Arts": [r"arts", r"music", r"drama", r"visual"],
    "Te Reo Māori": [r"te-reo-maori"],
}

# Year level detection
YEAR_PATTERNS = [
    (r"y(\d{1,2})", r"Year \1"),
    (r"year[_-](\d{1,2})", r"Year \1"),
    (r"year(\d{1,2})", r"Year \1"),
]

# Resource type detection
RESOURCE_TYPE_PATTERNS = {
    "lesson": [r"/lessons/", r"-lesson-", r"lesson-\d+"],
    "handout": [r"/handouts/", r"-handout"],
    "unit": [r"/units/", r"unit-plan"],
    "assessment": [r"assessment", r"rubric", r"quiz"],
    "interactive_game": [r"game", r"interactive", r"simulation"],
    "activity": [r"activity", r"worksheet"],
    "video": [r"video", r"multimedia"],
}


def parse_html_file(file_path: Path) -> Optional[Dict]:
    """Parse HTML file and extract metadata."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else file_path.stem.replace('-', ' ').title()
        
        # Clean title
        title = re.sub(r'\s*\|\s*Te Kete Ako\s*$', '', title)
        title = re.sub(r'\s+', ' ', title).strip()
        
        # Get relative path from /public/ (MUST BE FIRST!)
        rel_path = '/' + str(file_path.relative_to(PUBLIC_DIR.parent))
        
        # Detect unit (from path or content)
        unit_match = re.search(r'/units/([^/]+)/', rel_path)
        unit = unit_match.group(1) if unit_match else None
        
        # Detect subject
        subject = detect_subject(rel_path, content)
        
        # Detect year level
        year_level = detect_year_level(rel_path, content)
        
        # Detect resource type
        resource_type = detect_resource_type(rel_path, content)
        
        # Detect cultural markers
        has_te_reo = bool(re.search(r'\b(kia ora|tēnā koe|whānau|ako|māori|kaitiakitanga)\b', content, re.IGNORECASE))
        has_whakataukī = bool(re.search(r'whakataukī|proverb|saying', content, re.IGNORECASE))
        cultural_context = has_te_reo or has_whakataukī or 'māori' in content.lower()
        
        # Estimate quality score based on content analysis
        quality_score = estimate_quality(content, title, title)
        
        # Content preview (first 500 chars of visible text)
        visible_text = re.sub(r'<[^>]+>', ' ', content)
        visible_text = re.sub(r'\s+', ' ', visible_text).strip()
        content_preview = visible_text[:500] if len(visible_text) > 500 else visible_text
        
        # Build metadata JSON
        metadata = {
            'file_size': len(content),
            'has_navigation': '<nav' in content.lower(),
            'has_footer': '<footer' in content.lower(),
        }
        
        return {
            'file_path': rel_path,
            'title': title,
            'resource_type': resource_type,
            'subject': subject,
            'canonical_subject': subject,
            'year_level': year_level,
            'unit': unit,
            'quality_score': quality_score,
            'cultural_context': cultural_context,
            'has_te_reo': has_te_reo,
            'has_whakataukī': has_whakataukī,
            'content_preview': content_preview,
            'metadata': metadata,
        }
        
    except Exception as e:
        print(f"❌ Error parsing {file_path}: {e}")
        return None


def detect_subject(path: str, content: str) -> str:
    """Detect subject from path and content."""
    path_lower = path.lower()
    content_lower = content.lower()
    
    # Check path patterns first (more reliable)
    for subject, patterns in SUBJECT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, path_lower):
                return subject
    
    # Check content if path didn't match
    for subject, patterns in SUBJECT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, content_lower[:2000]):  # First 2000 chars
                return subject
    
    return "Cross-Curricular"


def detect_year_level(path: str, content: str) -> str:
    """Detect year level from path and content."""
    text = (path + " " + content[:1000]).lower()
    
    for pattern, replacement in YEAR_PATTERNS:
        match = re.search(pattern, text)
        if match:
            year_num = int(match.group(1))
            if 7 <= year_num <= 13:
                return f"Year {year_num}"
    
    return "All Years"


def detect_resource_type(path: str, content: str) -> str:
    """Detect resource type from path and content."""
    path_lower = path.lower()
    
    for res_type, patterns in RESOURCE_TYPE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, path_lower):
                return res_type
    
    # Check for common HTML page indicators
    if 'index.html' in path_lower or 'hub.html' in path_lower:
        return 'Page'
    
    return 'lesson'  # Default


def estimate_quality(content: str, title: str, description: str) -> int:
    """Estimate quality score based on content analysis."""
    score = 70  # Base score
    
    # Length indicators
    if len(content) > 5000:
        score += 5
    if len(content) > 10000:
        score += 5
    
    # Structure indicators
    if '<nav' in content or 'navigation' in content.lower():
        score += 3
    if '<footer' in content:
        score += 2
    if re.search(r'<h[123]>', content):
        score += 3
    
    # Quality content markers
    if 'whakataukī' in content.lower():
        score += 5
    if 'kaitiakitanga' in content.lower() or 'manaakitanga' in content.lower():
        score += 3
    if re.search(r'learning objective|achievement objective', content.lower()):
        score += 3
    if 'assessment' in content.lower() or 'rubric' in content.lower():
        score += 3
    
    # Title quality
    if len(title) > 30 and len(title) < 100:
        score += 2
    
    # Description quality
    if description and len(description) > 50:
        score += 2
    
    # CSS/JS includes (indicates professional styling)
    if 'te-kete-professional.css' in content:
        score += 5
    
    # Cap at 95 (only manual review can give 95+)
    return min(score, 95)


def scan_directory(directory: Path, priority_only: bool = False) -> List[Path]:
    """Scan directory for HTML files."""
    html_files = []
    
    if priority_only:
        # Only scan priority directories
        for priority_dir in PRIORITY_DIRS:
            dir_path = directory / priority_dir
            if dir_path.exists():
                html_files.extend(dir_path.rglob("*.html"))
    else:
        # Scan all HTML files
        html_files = list(directory.rglob("*.html"))
    
    # Filter out unwanted files
    excluded_patterns = [
        r'backup',
        r'\.bak',
        r'archive',
        r'node_modules',
        r'\.git',
        r'dist(?!-handouts)',  # Exclude dist but not dist-handouts
        r'backups/',
    ]
    
    filtered = []
    for file in html_files:
        file_str = str(file)
        if not any(re.search(pattern, file_str, re.IGNORECASE) for pattern in excluded_patterns):
            filtered.append(file)
    
    return filtered


def generate_sql_inserts(resources: List[Dict]) -> str:
    """Generate SQL INSERT statements."""
    if not resources:
        return ""
    
    sql_parts = []
    sql_parts.append("-- BATCH GRAPHRAG INDEX - Generated by batch-index-graphrag.py")
    sql_parts.append(f"-- Total resources: {len(resources)}")
    sql_parts.append(f"-- Generated: {datetime.now()}")
    sql_parts.append("")
    sql_parts.append("INSERT INTO graphrag_resources (")
    sql_parts.append("  file_path, title, resource_type, subject, canonical_subject,")
    sql_parts.append("  year_level, unit, quality_score, cultural_context,")
    sql_parts.append("  has_te_reo, has_whakataukī, content_preview, metadata")
    sql_parts.append(") VALUES")
    
    values = []
    for i, res in enumerate(resources):
        # Escape single quotes in strings
        def escape_sql(s):
            if s is None:
                return 'NULL'
            return "'" + str(s).replace("'", "''").replace("\\", "\\\\") + "'"
        
        # Convert metadata to JSON string
        import json
        metadata_json = json.dumps(res['metadata'])
        
        value = f"""(
  {escape_sql(res['file_path'])},
  {escape_sql(res['title'])},
  {escape_sql(res['resource_type'])},
  {escape_sql(res['subject'])},
  {escape_sql(res['canonical_subject'])},
  {escape_sql(res['year_level'])},
  {escape_sql(res['unit'])},
  {res['quality_score']},
  {str(res['cultural_context']).lower()},
  {str(res['has_te_reo']).lower()},
  {str(res['has_whakataukī']).lower()},
  {escape_sql(res['content_preview'])},
  '{metadata_json}'::jsonb
)"""
        values.append(value)
    
    sql_parts.append(',\n'.join(values))
    sql_parts.append("ON CONFLICT (file_path) DO UPDATE SET")
    sql_parts.append("  title = EXCLUDED.title,")
    sql_parts.append("  resource_type = EXCLUDED.resource_type,")
    sql_parts.append("  quality_score = EXCLUDED.quality_score,")
    sql_parts.append("  cultural_context = EXCLUDED.cultural_context,")
    sql_parts.append("  updated_at = NOW();")
    
    return '\n'.join(sql_parts)


def main():
    """Main execution."""
    print("=" * 80)
    print("🚀 BATCH GRAPHRAG INDEXER - Te Kete Ako")
    print("=" * 80)
    print()
    
    # Scan files
    print(f"📂 Scanning {PUBLIC_DIR}...")
    html_files = scan_directory(PUBLIC_DIR, priority_only=False)
    print(f"✅ Found {len(html_files)} HTML files")
    print()
    
    # Parse files
    print("📝 Parsing files...")
    resources = []
    errors = []
    
    for i, file_path in enumerate(html_files, 1):
        if i % 100 == 0:
            print(f"  Progress: {i}/{len(html_files)} ({i*100//len(html_files)}%)")
        
        resource = parse_html_file(file_path)
        if resource:
            resources.append(resource)
        else:
            errors.append(file_path)
    
    print(f"✅ Successfully parsed {len(resources)} files")
    if errors:
        print(f"⚠️  {len(errors)} files had errors")
    print()
    
    # Generate SQL
    print("💾 Generating SQL...")
    output_file = PUBLIC_DIR.parent / "scripts" / "graphrag-batch-index.sql"
    sql = generate_sql_inserts(resources)
    
    output_file.parent.mkdir(exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(sql)
    
    print(f"✅ SQL written to: {output_file}")
    print()
    
    # Statistics
    print("📊 STATISTICS:")
    print(f"  Total resources: {len(resources)}")
    
    subjects = {}
    for r in resources:
        subjects[r['subject']] = subjects.get(r['subject'], 0) + 1
    print(f"  Subjects: {len(subjects)}")
    for subject, count in sorted(subjects.items(), key=lambda x: x[1], reverse=True):
        print(f"    - {subject}: {count}")
    
    cultural = sum(1 for r in resources if r['cultural_context'])
    print(f"  Culturally integrated: {cultural} ({cultural*100//len(resources)}%)")
    
    quality_90 = sum(1 for r in resources if r['quality_score'] >= 90)
    print(f"  Gold standard (Q90+): {quality_90} ({quality_90*100//len(resources)}%)")
    
    avg_quality = sum(r['quality_score'] for r in resources) / len(resources)
    print(f"  Average quality: {avg_quality:.2f}")
    print()
    
    print("=" * 80)
    print("✅ BATCH INDEXING COMPLETE!")
    print()
    print("📋 NEXT STEPS:")
    print("  1. Review generated SQL: scripts/graphrag-batch-index.sql")
    print("  2. Run SQL in Supabase or via MCP: mcp_supabase_execute_sql")
    print("  3. Verify indexing: SELECT COUNT(*) FROM graphrag_resources")
    print("=" * 80)


if __name__ == "__main__":
    main()


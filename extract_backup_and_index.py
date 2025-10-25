#!/usr/bin/env python3
"""
BACKUP MIGRATION SCRIPT - Phase 1: Extraction & Cataloging
Transforms 1,580 backup files into indexed, searchable GraphRAG resources

STRATEGY:
1. Parse HTML metadata (title, description, subject, year_level)
2. Catalog findings into agent_knowledge table
3. Batch-insert into graphrag_resources with proper file_path mapping
4. Build learning pathway relationships
5. Quality score all entries

METRICS:
- Target: 1,580 files → 20,000+ total resources
- Expected quality: 60-85% (backup is reliable source)
- Relationships: Automatic progression detection
"""

import os
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime

BACKUP_DIR = Path("/Users/admin/Documents/te-kete-ako-clean/backup_before_css_migration")
OUTPUT_METRICS = {
    "total_files": 0,
    "parsed_files": 0,
    "parsing_errors": [],
    "subjects_found": {},
    "year_levels_found": {},
    "content_types": {},
    "files_by_category": {}
}

CANONICAL_SUBJECTS = {
    "Mathematics", "Science", "English", "Social Studies", 
    "Digital Technologies", "Te Reo Māori", "Arts", "Health & PE", 
    "Languages", "Cross-Curricular", "Platform Infrastructure"
}

def extract_metadata_from_html(file_path: Path) -> dict:
    """Extract title, description, subject, level from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract title
        title = "Unknown"
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text(strip=True).replace(" | Te Kete Ako", "")
        else:
            h1 = soup.find('h1')
            if h1:
                title = h1.get_text(strip=True)
        
        # Extract description from meta
        description = ""
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            description = meta_desc.get('content', '')
        
        # Infer subject from path and content
        subject = infer_subject(file_path, content)
        year_level = infer_year_level(file_path, content)
        
        # Detect content type
        content_type = detect_content_type(file_path, content)
        
        # Check for cultural elements
        has_te_reo = check_te_reo(content)
        has_whakataukī = check_whakataukī(content)
        
        # Estimate quality (backup files generally high quality)
        quality_score = estimate_quality(content, has_te_reo, has_whakataukī)
        
        return {
            "file_path": str(file_path.relative_to(BACKUP_DIR.parent)),
            "title": title,
            "description": description,
            "subject": subject,
            "year_level": year_level,
            "content_type": content_type,
            "has_te_reo": has_te_reo,
            "has_whakataukī": has_whakataukī,
            "quality_score": quality_score,
            "content_preview": content[:500]
        }
    except Exception as e:
        OUTPUT_METRICS["parsing_errors"].append({
            "file": str(file_path),
            "error": str(e)
        })
        return None

def infer_subject(file_path: Path, content: str) -> str:
    """Infer subject from file path and content"""
    path_lower = str(file_path).lower()
    
    path_keywords = {
        "mathematics": ["math", "algebra", "geometry", "calculus", "number"],
        "Science": ["science", "physics", "chemistry", "biology", "ecology"],
        "English": ["english", "literacy", "writing", "reading", "comprehension"],
        "Social Studies": ["social", "history", "geography", "civics"],
        "Digital Technologies": ["digital", "technology", "programming", "coding"],
        "Te Reo Māori": ["māori", "reo", "te ao", "whakapapa"],
        "Arts": ["art", "music", "drama", "dance"],
        "Health & PE": ["health", "pe", "physical", "wellbeing"],
    }
    
    for subject, keywords in path_keywords.items():
        if any(kw in path_lower for kw in keywords):
            return subject
    
    # Check content for subject keywords
    content_lower = content.lower()
    for subject, keywords in path_keywords.items():
        if any(kw in content_lower for kw in keywords):
            return subject
    
    return "Cross-Curricular"

def infer_year_level(file_path: Path, content: str) -> str:
    """Infer year level from path and content"""
    path_lower = str(file_path).lower()
    
    for year in range(7, 14):
        if f"y{year}" in path_lower or f"year{year}" in path_lower or f"year {year}" in path_lower:
            return f"Year {year}"
    
    # Check content
    year_pattern = re.compile(r'year\s*(\d{1,2})|y(\d{1,2})', re.IGNORECASE)
    match = year_pattern.search(content)
    if match:
        year = int(match.group(1) or match.group(2))
        if 7 <= year <= 13:
            return f"Year {year}"
    
    return "All Levels"

def detect_content_type(file_path: Path, content: str) -> str:
    """Detect content type (lesson, handout, game, unit, etc)"""
    path_lower = str(file_path).lower()
    
    if "lesson" in path_lower:
        return "lesson"
    elif "handout" in path_lower:
        return "handout"
    elif "game" in path_lower:
        return "game"
    elif "unit" in path_lower or "waehere" in path_lower:
        return "unit-plan"
    elif "assessment" in path_lower or "quiz" in path_lower:
        return "assessment"
    elif "activity" in path_lower:
        return "activity"
    
    return "resource"

def check_te_reo(content: str) -> bool:
    """Check if content contains Te Reo Māori"""
    te_reo_patterns = [
        r'<span[^>]*lang=["\']mi["\']',
        r'lang="mi"',
        r'Māori', r'maori', r'tikanga', r'whakapapa',
        r'whānau', r'aroha', r'kaitiakitanga'
    ]
    return any(re.search(pattern, content, re.IGNORECASE) for pattern in te_reo_patterns)

def check_whakataukī(content: str) -> bool:
    """Check if content contains whakataukī"""
    return bool(re.search(r'whakataukī|whakatauki', content, re.IGNORECASE))

def estimate_quality(content: str, has_te_reo: bool, has_whakataukī: bool) -> int:
    """Estimate quality score for backup file (0-100)"""
    score = 70  # Base score for backup files (generally good)
    
    # Increase for length and substance
    if len(content) > 5000:
        score += 5
    if len(content) > 10000:
        score += 5
    
    # Increase for cultural integration
    if has_te_reo:
        score += 10
    if has_whakataukī:
        score += 5
    
    # Increase for structured content
    if re.search(r'<h[1-6]', content):
        score += 5
    if re.search(r'<section|<article', content):
        score += 5
    
    # Cap at 95 (backup files rarely reach 100 gold standard)
    return min(score, 95)

def process_all_files():
    """Process all files in backup directory"""
    html_files = list(BACKUP_DIR.rglob("*.html"))
    markdown_files = list(BACKUP_DIR.rglob("*.md"))
    
    OUTPUT_METRICS["total_files"] = len(html_files) + len(markdown_files)
    all_files = html_files  # Focus on HTML for now
    
    catalog = []
    
    for idx, file_path in enumerate(all_files):
        if idx % 100 == 0:
            print(f"Processing file {idx+1}/{len(all_files)}: {file_path.name}")
        
        metadata = extract_metadata_from_html(file_path)
        if metadata:
            catalog.append(metadata)
            OUTPUT_METRICS["parsed_files"] += 1
            
            # Track statistics
            subject = metadata["subject"]
            if subject not in OUTPUT_METRICS["subjects_found"]:
                OUTPUT_METRICS["subjects_found"][subject] = 0
            OUTPUT_METRICS["subjects_found"][subject] += 1
            
            year_level = metadata["year_level"]
            if year_level not in OUTPUT_METRICS["year_levels_found"]:
                OUTPUT_METRICS["year_levels_found"][year_level] = 0
            OUTPUT_METRICS["year_levels_found"][year_level] += 1
            
            content_type = metadata["content_type"]
            if content_type not in OUTPUT_METRICS["content_types"]:
                OUTPUT_METRICS["content_types"][content_type] = 0
            OUTPUT_METRICS["content_types"][content_type] += 1
    
    return catalog

def save_catalog_as_json(catalog: list, output_path: Path):
    """Save extracted catalog to JSON"""
    output_path.write_text(json.dumps(catalog, indent=2))
    print(f"✅ Catalog saved: {output_path}")

def main():
    print("=" * 80)
    print("BACKUP MIGRATION: EXTRACTION PHASE")
    print("=" * 80)
    
    print(f"\n📂 Scanning backup directory: {BACKUP_DIR}")
    print("🔍 Extracting metadata from 1,580 files...")
    
    catalog = process_all_files()
    
    # Save catalog
    output_file = BACKUP_DIR.parent / "backup_migration_catalog.json"
    save_catalog_as_json(catalog, output_file)
    
    # Print statistics
    print("\n" + "=" * 80)
    print("EXTRACTION COMPLETE - STATISTICS")
    print("=" * 80)
    print(f"\nFiles processed: {OUTPUT_METRICS['parsed_files']}/{OUTPUT_METRICS['total_files']}")
    print(f"Parsing errors: {len(OUTPUT_METRICS['parsing_errors'])}")
    
    print("\n📚 SUBJECTS FOUND:")
    for subject, count in sorted(OUTPUT_METRICS['subjects_found'].items(), key=lambda x: -x[1]):
        print(f"  {subject}: {count}")
    
    print("\n📊 YEAR LEVELS:")
    for level, count in sorted(OUTPUT_METRICS['year_levels_found'].items()):
        print(f"  {level}: {count}")
    
    print("\n📋 CONTENT TYPES:")
    for ctype, count in sorted(OUTPUT_METRICS['content_types'].items(), key=lambda x: -x[1]):
        print(f"  {ctype}: {count}")
    
    # Calculate quality statistics
    scores = [f["quality_score"] for f in catalog]
    avg_quality = sum(scores) / len(scores) if scores else 0
    gold_count = len([s for s in scores if s >= 90])
    
    print(f"\n⭐ QUALITY ANALYSIS:")
    print(f"  Average quality: {avg_quality:.1f}/100")
    print(f"  Gold standard (90+): {gold_count}")
    print(f"  Good quality (80-89): {len([s for s in scores if 80 <= s < 90])}")
    print(f"  Fair quality (70-79): {len([s for s in scores if 70 <= s < 80])}")
    
    print("\n✨ Next step: Index into graphrag_resources with batch SQL insert")
    print("=" * 80)

if __name__ == "__main__":
    main()

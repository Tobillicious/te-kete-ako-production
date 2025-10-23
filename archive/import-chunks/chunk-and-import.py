#!/usr/bin/env python3
"""
SQL Chunker & Importer for GraphRAG
Splits large SQL file into chunks and generates import commands
"""

import re
from pathlib import Path

SQL_FILE = Path(__file__).parent / "graphrag-batch-index.sql"
CHUNK_SIZE = 200  # Records per chunk
OUTPUT_DIR = Path(__file__).parent / "chunks"

def split_sql_file():
    """Split SQL file into manageable chunks."""
    print("📂 Reading SQL file...")
    with open(SQL_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract header (everything before VALUES)
    header_match = re.search(r'(.*?)\) VALUES\s*\n', content, re.DOTALL)
    if not header_match:
        print("❌ Could not find VALUES clause!")
        return
    
    header = header_match.group(1) + ") VALUES\n"
    
    # Extract footer (everything after last value)
    footer_match = re.search(r'\nON CONFLICT.*$', content, re.DOTALL)
    footer = footer_match.group(0) if footer_match else ";"
    
    # Extract all value tuples
    values_section = content[header_match.end():footer_match.start() if footer_match else len(content)]
    
    # Split by ),\n( to get individual records
    # But we need to be careful with nested parentheses in content
    records = []
    current_record = []
    paren_depth = 0
    in_quote = False
    quote_char = None
    
    for line in values_section.split('\n'):
        current_record.append(line)
        
        # Check if this line ends a record (has ),)
        if line.strip().endswith('),') or line.strip().endswith(')'):
            # Found end of record
            records.append('\n'.join(current_record))
            current_record = []
    
    print(f"✅ Found {len(records)} records")
    
    # Create chunks
    OUTPUT_DIR.mkdir(exist_ok=True)
    chunks = []
    
    for i in range(0, len(records), CHUNK_SIZE):
        chunk_records = records[i:i+CHUNK_SIZE]
        chunk_num = i // CHUNK_SIZE + 1
        
        # Build chunk SQL
        chunk_sql = header
        chunk_sql += ',\n'.join(chunk_records)
        chunk_sql += footer
        
        # Write chunk file
        chunk_file = OUTPUT_DIR / f"chunk_{chunk_num:03d}.sql"
        with open(chunk_file, 'w', encoding='utf-8') as f:
            f.write(chunk_sql)
        
        chunks.append({
            'file': chunk_file,
            'num': chunk_num,
            'records': len(chunk_records)
        })
        
        print(f"  📝 Chunk {chunk_num}: {len(chunk_records)} records → {chunk_file.name}")
    
    print(f"\n✅ Created {len(chunks)} chunks")
    print(f"📂 Location: {OUTPUT_DIR}")
    print()
    print("📋 IMPORT INSTRUCTIONS:")
    print("Run each chunk via MCP in sequence:")
    for chunk in chunks:
        print(f"  {chunk['num']}. mcp_supabase_execute_sql with chunk_{chunk['num']:03d}.sql")
    
    return chunks

if __name__ == "__main__":
    split_sql_file()


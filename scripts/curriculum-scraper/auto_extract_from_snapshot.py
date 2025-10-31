#!/usr/bin/env python3
"""
Automated extraction from browser snapshot YAML files.
Parses the accessibility tree structure to extract curriculum statements.
"""

import re
import sys

def extract_statements_from_snapshot(snapshot_file):
    """
    Extract curriculum statements from browser snapshot YAML.
    Returns structured data organized by strand, sub-strand, year, element.
    """
    
    with open(snapshot_file, 'r') as f:
        content = f.read()
    
    statements = []
    current_strand = None
    current_sub_strand = None
    current_year = None
    current_element = None
    
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        # Detect strand headings (e.g., "Materials", "History", "Geography")
        if '- heading' in line and 'level=4' in line:
            # Extract heading text from next line or current line
            heading_match = re.search(r'heading "([^"]+)"', line)
            if heading_match:
                heading = heading_match.group(1)
                
                # Check if this is a strand name
                if heading in ['History', 'Geography', 'Civics and Society', 'Economic Activity', 
                              'Materials', 'Matter Interactions and Energy', 'Motion and Forces',
                              'Earth Systems', 'Earth and Space', 'Organism Diversity', 
                              'Body Systems', 'Ecosystems', 'New Zealand History', 'Global History']:
                    current_strand = heading
        
        # Detect year levels
        if '- heading "During Year' in line:
            year_match = re.search(r'During Year (\d+)', line)
            if year_match:
                current_year = int(year_match.group(1))
        
        # Detect Knowledge/Practices
        if '- heading "Knowledge"' in line:
            current_element = 'Knowledge'
        elif '- heading "Practices"' in line:
            current_element = 'Practices'
        
        # Detect sub-strand (strong tags)
        if '- strong [ref=' in line and i + 1 < len(lines):
            next_line = lines[i + 1]
            sub_strand_match = re.search(r': (.+)', next_line)
            if sub_strand_match:
                current_sub_strand = sub_strand_match.group(1).strip()
        
        # Extract list items (statements)
        if '- listitem [ref=' in line and i + 1 < len(lines):
            next_line = lines[i + 1]
            # Try to extract the statement text
            statement_match = re.search(r': (.+)', next_line)
            if statement_match:
                statement = statement_match.group(1).strip()
                
                # Skip empty or very short statements
                if len(statement) < 10:
                    continue
                
                # Skip "For example, consider:" prompts
                if 'For example, consider' in statement:
                    continue
                
                # Skip "Note:" items (metadata, not statements)
                if statement.startswith('Note:'):
                    continue
                
                # Skip emphasis/italic items that are historical figures
                if '(' in statement and '–' in statement and ')' in statement:
                    # This might be a historical figure attribution
                    continue
                
                statements.append({
                    'strand': current_strand,
                    'sub_strand': current_sub_strand,
                    'year': current_year,
                    'element': current_element,
                    'statement': statement
                })
    
    return statements

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 auto_extract_from_snapshot.py <snapshot_file>")
        sys.exit(1)
    
    snapshot_file = sys.argv[1]
    statements = extract_statements_from_snapshot(snapshot_file)
    
    print(f"Extracted {len(statements)} potential statements")
    
    # Group by strand
    by_strand = {}
    for stmt in statements:
        strand = stmt['strand'] or 'Unknown'
        if strand not in by_strand:
            by_strand[strand] = []
        by_strand[strand].append(stmt)
    
    print("\nBreakdown by strand:")
    for strand, stmts in sorted(by_strand.items()):
        print(f"  {strand}: {len(stmts)} statements")
    
    # Save to JSON for review
    import json
    output_file = snapshot_file.replace('.log', '_extracted.json')
    with open(output_file, 'w') as f:
        json.dump(statements, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Saved to: {output_file}")


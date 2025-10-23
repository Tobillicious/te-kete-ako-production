# 🚀 Batch GraphRAG Indexer - Quick Start

## What It Does
Scans all HTML files in `/public/` and generates SQL to index them in the `graphrag_resources` table.

**Critical**: Fixes deployment blocker - 1,294 files missing from GraphRAG!

## Quick Run

```bash
# From project root
cd /Users/admin/Documents/te-kete-ako-clean

# Run the script
python3 scripts/batch-index-graphrag.py

# This generates: scripts/graphrag-batch-index.sql
```

## What It Detects

- ✅ **Title** from `<title>` tag
- ✅ **Subject** from path patterns (Math, Science, English, etc.)
- ✅ **Year Level** (Year 7-13 or "All Years")
- ✅ **Resource Type** (lesson, handout, unit, etc.)
- ✅ **Quality Score** (estimated 70-95 based on content)
- ✅ **Cultural Markers** (Te Reo, whakataukī, cultural context)
- ✅ **Description** from meta tags

## Output

Generates `graphrag-batch-index.sql` with INSERT statements like:

```sql
INSERT INTO graphrag_resources (
  file_path, title, description, subject, ...
) VALUES
  ('/public/lessons/y7-math-patterns.html', 'Patterns & Algebra', ...),
  ('/public/handouts/treaty-handout.html', 'Treaty of Waitangi', ...),
  ...
ON CONFLICT (file_path) DO UPDATE SET ...
```

## Next Steps

1. ✅ Review the generated SQL
2. ✅ Run via MCP: `mcp_supabase_execute_sql` with the SQL content
3. ✅ Verify: `SELECT COUNT(*) FROM graphrag_resources`
4. ✅ Expected: ~2,000+ resources (up from 879!)

## Features

- **Smart filtering**: Excludes backups, archives, node_modules
- **Conflict handling**: Updates existing records, inserts new ones
- **Quality estimation**: Analyzes content for quality indicators
- **Cultural detection**: Finds Te Reo, whakataukī, cultural context
- **Progress tracking**: Shows progress every 100 files

## Statistics Provided

- Total resources indexed
- Breakdown by subject
- Cultural integration rate
- Gold standard (Q90+) count
- Average quality score

---

**Built by**: Cursor AI Agent  
**Date**: October 23, 2025  
**Purpose**: Unlock 1,294 hidden resources for deployment!


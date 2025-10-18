#!/bin/bash
cd /Users/admin/Documents/te-kete-ako-clean
python3 index-all-code-files.py > code-indexing-output.txt 2>&1
echo "Exit code: $?" >> code-indexing-output.txt


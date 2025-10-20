#!/usr/bin/env python3
"""
EXECUTE SPRINT INTELLIGENCE
Run GraphRAG queries and batch CSS operations for collaborative sprint
"""

import subprocess
import sys
import os
from datetime import datetime

def run_python_script(script_path):
    """Run a Python script and return success status"""
    try:
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, timeout=300)
        if result.returncode == 0:
            print(f"✅ {script_path} completed successfully")
            return True
        else:
            print(f"❌ {script_path} failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"⏰ {script_path} timed out")
        return False
    except Exception as e:
        print(f"❌ {script_path} error: {e}")
        return False

def main():
    """Execute sprint intelligence operations"""
    print("🚀 COLLABORATIVE SPRINT INTELLIGENCE EXECUTION")
    print("=" * 70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Change to project directory
    os.chdir('/Users/admin/Documents/te-kete-ako-clean')
    
    # 1. Run GraphRAG Sprint Queries
    print("📊 STEP 1: GRAPHRAG SPRINT QUERIES")
    print("-" * 50)
    success1 = run_python_script('graphrag-sprint-queries.py')
    
    # 2. Batch Add Professional CSS
    print("\n🎨 STEP 2: BATCH ADD PROFESSIONAL CSS")
    print("-" * 50)
    success2 = run_python_script('batch-add-professional-css.py')
    
    # 3. Summary
    print("\n📋 SPRINT EXECUTION SUMMARY")
    print("=" * 70)
    
    if success1:
        print("✅ GraphRAG queries: COMPLETED")
    else:
        print("❌ GraphRAG queries: FAILED")
    
    if success2:
        print("✅ Professional CSS: COMPLETED")
    else:
        print("❌ Professional CSS: FAILED")
    
    if success1 and success2:
        print("\n🎉 SPRINT INTELLIGENCE EXECUTION COMPLETE!")
        print("Ready for next phase: Orphan rescue and relationship mining")
    else:
        print("\n⚠️  Some operations failed - check logs above")
    
    print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()

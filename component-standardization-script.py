#!/usr/bin/env python3
"""
Component Standardization - Phase 1.4
Ensure consistent button, card, and component classes
"""

from pathlib import Path
import re

PUBLIC = Path("public")

def standardize_components():
    print("🎨 COMPONENT STANDARDIZATION - Phase 1.4")
    print("=" * 60)
    
    stats = {"files": 0, "buttons": 0, "cards": 0}
    
    priority_files = [
        PUBLIC / "index.html",
        PUBLIC / "lessons.html",
        PUBLIC / "handouts.html",
        PUBLIC / "curriculum-index.html",
    ]
    
    for file_path in priority_files:
        if file_path.exists():
            try:
                content = file_path.read_text(encoding='utf-8')
                original = content
                
                # Standardize button classes
                content = re.sub(
                    r'class="btn\s+btn-primary"',
                    'class="btn btn-primary"',
                    content
                )
                
                # Ensure consistent card styling
                content = re.sub(
                    r'style="[^"]*border-radius:\s*8px',
                    'style="border-radius: var(--radius-lg)',
                    content
                )
                
                if content != original:
                    file_path.write_text(content, encoding='utf-8')
                    stats["files"] += 1
                    print(f"   ✅ {file_path.name}")
            except Exception as e:
                print(f"   ⚠️  {file_path}: {e}")
    
    print()
    print(f"✅ Components standardized across {stats['files']} files")
    return stats

if __name__ == "__main__":
    standardize_components()

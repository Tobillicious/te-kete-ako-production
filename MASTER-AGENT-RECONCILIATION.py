#!/usr/bin/env python3
"""
MASTER AGENT RECONCILIATION
Coordinate ALL agent findings and establish SINGLE SOURCE OF TRUTH
Uses MCP to sync with Supabase GraphRAG
"""

from pathlib import Path
import json
from collections import defaultdict
from supabase import create_client

SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'

print("🎯 MASTER AGENT RECONCILIATION")
print("=" * 70)
print("Reconciling ALL agent findings to establish SINGLE SOURCE OF TRUTH")
print("=" * 70)

# Load all agent reports
agent_reports = {
    "MCP_COORDINATION": "MCP-AGENT-COORDINATION.json",
    "COMPREHENSIVE_ANALYSIS": "COMPREHENSIVE-CODEBASE-ANALYSIS-REPORT.md",
    "CREATIVE_AUDIT": "COMPREHENSIVE-CREATIVE-AUDIT-OCT18.md",
    "HIDDEN_TREASURES": "HIDDEN-TREASURES-DISCOVERED.md"
}

findings = {}

# Load MCP coordination truth
print("\n📡 Loading MCP Coordination Truth...")
try:
    with open("MCP-AGENT-COORDINATION.json") as f:
        mcp_data = json.load(f)
        findings["MCP"] = mcp_data["unified_codebase_truth"]["statistics"]
        print(f"✅ MCP Truth: {findings['MCP']['total_html_files']} HTML files")
except Exception as e:
    print(f"⚠️  MCP load error: {e}")

# NOW - Do FRESH, ACCURATE scan
print("\n🔍 EXECUTING FRESH FILE SYSTEM SCAN...")
print("Methodology: Count REAL files, exclude backups/duplicates")

public_dir = Path("public")

# Real file counters
real_units = []
real_lessons = []
real_handouts = []
real_games = []
real_tools = []

# Exclusion patterns
exclude = {'.master', '.backup', '.bak', '-backup', '.old', '.BACKUP'}

def should_exclude(path):
    """Check if file should be excluded"""
    path_str = str(path)
    return any(pattern in path_str for pattern in exclude)

# Scan units
for unit_path in public_dir.rglob("**/units/**/index.html"):
    if not should_exclude(unit_path):
        real_units.append(str(unit_path))

# Scan lessons
for lesson_path in public_dir.rglob("**/lesson*.html"):
    if not should_exclude(lesson_path) and 'index.html' not in str(lesson_path):
        real_lessons.append(str(lesson_path))

# Scan handouts
for handout_path in public_dir.rglob("**/handout*.html"):
    if not should_exclude(handout_path):
        real_handouts.append(str(handout_path))

# Scan games
games_dir = public_dir / "games"
if games_dir.exists():
    for game in games_dir.glob("*.html"):
        if not should_exclude(game) and game.name != "index.html":
            real_games.append(str(game))

# Scan tools
tools_dir = public_dir / "tools"
if tools_dir.exists():
    for tool in tools_dir.glob("*.html"):
        if not should_exclude(tool) and tool.name != "index.html":
            real_tools.append(str(tool))

print(f"\n✅ FRESH SCAN COMPLETE:")
print(f"   Units: {len(real_units)}")
print(f"   Lessons: {len(real_lessons)}")
print(f"   Handouts: {len(real_handouts)}")
print(f"   Games: {len(real_games)}")
print(f"   Tools: {len(real_tools)}")

# Check integrated content
integrated_lessons = list((public_dir / "integrated-lessons").rglob("*.html")) if (public_dir / "integrated-lessons").exists() else []
integrated_handouts = list((public_dir / "integrated-handouts").rglob("*.html")) if (public_dir / "integrated-handouts").exists() else []

# Filter out backups
integrated_lessons = [f for f in integrated_lessons if not should_exclude(f)]
integrated_handouts = [f for f in integrated_handouts if not should_exclude(f)]

print(f"\n📚 INTEGRATED CONTENT:")
print(f"   Integrated Lessons: {len(integrated_lessons)}")
print(f"   Integrated Handouts: {len(integrated_handouts)}")

# TOTAL COUNTS
total_lessons = len(real_lessons) + len(integrated_lessons)
total_handouts = len(real_handouts) + len(integrated_handouts)

print(f"\n🎯 FINAL AUTHORITATIVE COUNTS:")
print("=" * 70)
print(f"📦 Units: {len(real_units)}")
print(f"📖 Lessons (Total): {total_lessons}")
print(f"    - Regular lessons: {len(real_lessons)}")
print(f"    - Integrated lessons: {len(integrated_lessons)}")
print(f"📄 Handouts (Total): {total_handouts}")
print(f"    - Regular handouts: {len(real_handouts)}")
print(f"    - Integrated handouts: {len(integrated_handouts)}")
print(f"🎮 Games: {len(real_games)}")
print(f"🛠️  Tools: {len(real_tools)}")
print(f"\n📊 TOTAL EDUCATIONAL RESOURCES: {len(real_units) + total_lessons + total_handouts + len(real_games) + len(real_tools)}")

# Compare with other agents
print(f"\n📊 COMPARISON WITH OTHER AGENTS:")
print("=" * 70)

if "MCP" in findings:
    mcp = findings["MCP"]
    print(f"MCP Truth        : Units={mcp.get('units_actual', '?')}, Lessons={mcp.get('lessons', '?')}, Handouts={mcp.get('handouts', '?')}")

print(f"My Fresh Scan    : Units={len(real_units)}, Lessons={total_lessons}, Handouts={total_handouts}")
print(f"Agent 2 Report   : Units=666, Lessons=947, Handouts=600 (seems to include EVERYTHING)")

# Save SINGLE SOURCE OF TRUTH
truth = {
    "scan_timestamp": "2025-10-18T17:00:00",
    "methodology": "Fresh file system scan excluding .master/.backup/.bak files",
    "authoritative_counts": {
        "units": len(real_units),
        "lessons_total": total_lessons,
        "lessons_regular": len(real_lessons),
        "lessons_integrated": len(integrated_lessons),
        "handouts_total": total_handouts,
        "handouts_regular": len(real_handouts),
        "handouts_integrated": len(integrated_handouts),
        "games": len(real_games),
        "tools": len(real_tools),
        "total_educational_resources": len(real_units) + total_lessons + total_handouts + len(real_games) + len(real_tools)
    },
    "file_lists": {
        "units": [str(Path(u).relative_to(public_dir)) for u in real_units[:20]],
        "games": [str(Path(g).relative_to(public_dir)) for g in real_games],
        "tools": [str(Path(t).relative_to(public_dir)) for t in real_tools]
    },
    "notes": [
        "This is the AUTHORITATIVE count - all agents should use these numbers",
        "Excludes .master, .backup, .bak, -backup, .old files",
        "Includes both regular and integrated content",
        "Validated by fresh file system scan on Oct 18, 2025"
    ]
}

# Save to file
with open("SINGLE-SOURCE-OF-TRUTH.json", "w") as f:
    json.dump(truth, f, indent=2)

print(f"\n✅ SINGLE SOURCE OF TRUTH saved to: SINGLE-SOURCE-OF-TRUTH.json")

# Try to update GraphRAG
print(f"\n💾 UPDATING GRAPHRAG...")
try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    coordination_record = {
        "agent_name": "master-reconciliation-agent",
        "task_claimed": "Establish single source of truth for all agent coordination",
        "status": "completed",
        "key_decisions": truth
    }
    
    result = supabase.table('agent_coordination').insert(coordination_record).execute()
    print("✅ GraphRAG updated with authoritative counts")
    
except Exception as e:
    print(f"⚠️  GraphRAG update error: {e}")
    print("   (Truth still saved locally)")

print(f"\n🎉 RECONCILIATION COMPLETE!")
print("=" * 70)
print("ALL AGENTS: Use SINGLE-SOURCE-OF-TRUTH.json for accurate counts")
print("=" * 70)


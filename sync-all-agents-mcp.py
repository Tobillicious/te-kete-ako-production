#!/usr/bin/env python3
"""
MCP Agent Coordination - Sync all agent findings
"""

import json
from pathlib import Path

print("🤝 SYNCING ALL AGENT DISCOVERIES")
print("=" * 60)

# Load all analysis files
analyses = []
for json_file in Path(".").glob("*-analysis.json"):
    try:
        with open(json_file) as f:
            data = json.load(f)
            analyses.append({
                "source": json_file.name,
                "data": data
            })
            print(f"✅ Loaded: {json_file.name}")
    except:
        pass

# Load audit files
for json_file in Path(".").glob("*-audit.json"):
    try:
        with open(json_file) as f:
            data = json.load(f)
            analyses.append({
                "source": json_file.name,
                "data": data
            })
            print(f"✅ Loaded: {json_file.name}")
    except:
        pass

print(f"\n📊 Loaded {len(analyses)} agent analysis files")

# Merge findings
merged = {
    "units": set(),
    "lessons": set(),
    "handouts": set(),
    "files": set()
}

for analysis in analyses:
    data = analysis["data"]
    
    # Extract units
    if "units" in data:
        if isinstance(data["units"], list):
            for unit in data["units"]:
                if isinstance(unit, dict):
                    merged["units"].add(unit.get("name") or unit.get("path") or str(unit))
                else:
                    merged["units"].add(str(unit))
    
    # Extract lessons/handouts
    if "educational_content" in data:
        edu = data["educational_content"]
        if "lessons" in edu:
            for lesson in edu["lessons"]:
                merged["lessons"].add(str(lesson))
        if "handouts" in edu:
            for handout in edu["handouts"]:
                merged["handouts"].add(str(handout))

print("\n🎯 MERGED AGENT FINDINGS:")
print(f"   Total Units: {len(merged['units'])}")
print(f"   Total Lessons: {len(merged['lessons'])}")
print(f"   Total Handouts: {len(merged['handouts'])}")

# Save merged findings
with open("merged-agent-findings.json", "w") as f:
    json.dump({
        "units": sorted(list(merged["units"])),
        "lessons": sorted(list(merged["lessons"])),
        "handouts": sorted(list(merged["handouts"])),
        "stats": {
            "total_units": len(merged["units"]),
            "total_lessons": len(merged["lessons"]),
            "total_handouts": len(merged["handouts"])
        }
    }, f, indent=2)

print("\n✅ Merged findings saved to: merged-agent-findings.json")

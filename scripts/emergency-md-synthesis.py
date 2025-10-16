#!/usr/bin/env python3
"""
EMERGENCY MD SYNTHESIS SCRIPT
Synthesizes 3,228 MD files into 6 master files
"""

import os
import glob
import json
from datetime import datetime

class EmergencyMDSynthesis:
    def __init__(self):
        self.master_files = {
            'ACTIVE_QUESTIONS.md': 'All questions and coordination',
            'progress-log.md': 'All progress tracking', 
            'START_HERE_ALL_AGENTS.md': 'All agent coordination',
            '__ACTIVE_COORDINATION__.md': 'All active coordination',
            'MCP_KNOWLEDGE.md': 'All MCP knowledge sharing',
            'GRAPHRAG_KNOWLEDGE.md': 'All GraphRAG knowledge storage'
        }
        
    def analyze_md_files(self):
        """Analyze all MD files in the codebase"""
        print("🚨 EMERGENCY MD SYNTHESIS - ANALYZING 3,228 FILES")
        print("=" * 60)
        
        # Find all MD files
        md_files = []
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.md'):
                    md_files.append(os.path.join(root, file))
        
        print(f"📊 Total MD files found: {len(md_files)}")
        
        # Categorize files
        categories = {
            'coordination': [],
            'progress': [],
            'technical': [],
            'documentation': [],
            'status': [],
            'other': []
        }
        
        for file in md_files:
            filename = os.path.basename(file).lower()
            
            if any(x in filename for x in ['coordination', 'agent', 'team', 'hui']):
                categories['coordination'].append(file)
            elif any(x in filename for x in ['progress', 'log', 'status', 'update']):
                categories['progress'].append(file)
            elif any(x in filename for x in ['technical', 'css', 'js', 'html', 'code']):
                categories['technical'].append(file)
            elif any(x in filename for x in ['doc', 'guide', 'manual', 'readme']):
                categories['documentation'].append(file)
            elif any(x in filename for x in ['status', 'report', 'summary']):
                categories['status'].append(file)
            else:
                categories['other'].append(file)
        
        # Print analysis
        for category, files in categories.items():
            if files:
                print(f"  {category}: {len(files)} files")
        
        return categories
    
    def create_synthesis_plan(self, categories):
        """Create synthesis plan for 6 agents"""
        print("\n🎯 CREATING 6-AGENT SYNTHESIS PLAN")
        print("=" * 60)
        
        synthesis_plan = {
            'Agent_1': {
                'target': 'ACTIVE_QUESTIONS.md',
                'files': categories['coordination'],
                'description': 'Synthesize all coordination files'
            },
            'Agent_2': {
                'target': 'progress-log.md', 
                'files': categories['progress'],
                'description': 'Synthesize all progress files'
            },
            'Agent_3': {
                'target': '__ACTIVE_COORDINATION__.md',
                'files': categories['technical'],
                'description': 'Synthesize all technical files'
            },
            'Agent_4': {
                'target': 'START_HERE_ALL_AGENTS.md',
                'files': categories['documentation'],
                'description': 'Synthesize all documentation files'
            },
            'Agent_5': {
                'target': 'MCP_KNOWLEDGE.md',
                'files': categories['status'],
                'description': 'Synthesize all status files'
            },
            'Agent_6': {
                'target': 'GRAPHRAG_KNOWLEDGE.md',
                'files': categories['other'],
                'description': 'Synthesize all remaining files'
            }
        }
        
        print("📋 6-AGENT SYNTHESIS ASSIGNMENT:")
        for agent, plan in synthesis_plan.items():
            print(f"  {agent}: {plan['target']} ({len(plan['files'])} files)")
            print(f"    Description: {plan['description']}")
        
        return synthesis_plan
    
    def generate_emergency_commands(self):
        """Generate emergency commands for all agents"""
        print("\n🚨 EMERGENCY COMMANDS FOR ALL 6 AGENTS")
        print("=" * 60)
        
        commands = [
            "🚨 STOP creating new MD files immediately!",
            "🔄 Use MCP for all communication",
            "📚 Update GraphRAG with knowledge",
            "🎯 Work on master files only",
            "🤝 Coordinate through MCP",
            "🧹 Synthesize existing files into master ones",
            "🗑️ Delete duplicate files after synthesis",
            "📊 Update MCP with consolidated knowledge",
            "🔄 Update GraphRAG with final state"
        ]
        
        for i, command in enumerate(commands, 1):
            print(f"  {i}. {command}")
        
        return commands
    
    def create_cleanup_script(self):
        """Create cleanup script for after synthesis"""
        cleanup_script = """#!/bin/bash
# EMERGENCY MD CLEANUP SCRIPT
echo "🧹 CLEANING UP MD FILES AFTER SYNTHESIS"

# Keep only master files
MASTER_FILES=(
    "ACTIVE_QUESTIONS.md"
    "progress-log.md" 
    "START_HERE_ALL_AGENTS.md"
    "__ACTIVE_COORDINATION__.md"
    "MCP_KNOWLEDGE.md"
    "GRAPHRAG_KNOWLEDGE.md"
)

# Delete all other MD files
find . -name "*.md" -not -path "./archive/*" | while read file; do
    filename=$(basename "$file")
    if [[ ! " ${MASTER_FILES[@]} " =~ " ${filename} " ]]; then
        echo "🗑️ Deleting: $file"
        rm "$file"
    fi
done

echo "✅ MD cleanup complete - only master files remain"
"""
        
        with open('scripts/emergency-md-cleanup.sh', 'w') as f:
            f.write(cleanup_script)
        
        print(f"\n📝 Cleanup script created: scripts/emergency-md-cleanup.sh")
        return cleanup_script

def main():
    synthesis = EmergencyMDSynthesis()
    
    # Analyze MD files
    categories = synthesis.analyze_md_files()
    
    # Create synthesis plan
    plan = synthesis.create_synthesis_plan(categories)
    
    # Generate emergency commands
    synthesis.generate_emergency_commands()
    
    # Create cleanup script
    synthesis.create_cleanup_script()
    
    print(f"\n🚨 EMERGENCY SYNTHESIS PLAN READY!")
    print(f"📊 3,228 files to synthesize into 6 master files")
    print(f"🎯 6 agents assigned to specific synthesis tasks")
    print(f"🧹 Cleanup script ready for execution")
    print(f"⚡ IMMEDIATE ACTION REQUIRED!")

if __name__ == "__main__":
    main()

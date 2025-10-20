#!/usr/bin/env python3
"""
🚀 EXECUTE GRAPHRAG TODOS - Master Script
Run all GraphRAG intelligence expansion tools in optimal sequence

Impact: 10x-100x multipliers across the platform

Tools:
1. Agent Intelligence Amplifier (50x) - Get briefing
2. Orphan Rescue (Quick wins) - Connect 20 gems
3. Relationship Miner (100x) - Scale 30 types
4. Year Bridge Builder (Critical) - Y11→Y13 NCEA

Usage: python3 scripts/execute-graphrag-todos.py [--dry-run] [--tools tool1,tool2]
"""

import sys
import os
import subprocess
import json
from datetime import datetime

TOOLS = {
    'amplifier': {
        'script': 'scripts/agent-intelligence-amplifier.py',
        'name': 'Agent Intelligence Amplifier',
        'impact': '50x',
        'description': 'Generate comprehensive intelligence briefing',
        'time': '2 min',
        'priority': 1
    },
    'orphan-rescue': {
        'script': 'scripts/orphan-rescue.py',
        'name': 'Orphan Rescue',
        'impact': 'Quick wins',
        'description': 'Connect 20 orphaned Q90+ resources',
        'time': '5 min',
        'priority': 2
    },
    'relationship-miner': {
        'script': 'scripts/graphrag-relationship-miner.py',
        'name': 'Relationship Miner',
        'impact': '100x',
        'description': 'Scale 30 underutilized relationship types',
        'time': '10-15 min',
        'priority': 3
    },
    'year-bridges': {
        'script': 'scripts/year-bridge-builder.py',
        'name': 'Year Bridge Builder',
        'impact': 'Critical',
        'description': 'Build Y11→Y12→Y13 NCEA bridges',
        'time': '5-10 min',
        'priority': 4
    }
}

def print_banner():
    """Print execution banner"""
    print("\n" + "="*70)
    print("🚀 GRAPHRAG TODO MASTER EXECUTOR")
    print("   Run all intelligence expansion tools in optimal sequence")
    print("="*70 + "\n")

def print_tool_menu():
    """Print available tools"""
    print("📋 Available Tools:\n")
    
    for tool_id, tool_info in sorted(TOOLS.items(), key=lambda x: x[1]['priority']):
        print(f"{tool_info['priority']}. {tool_info['name']} ({tool_info['impact']} impact)")
        print(f"   {tool_info['description']}")
        print(f"   Estimated time: {tool_info['time']}")
        print()

def execute_tool(tool_id: str, dry_run: bool = False) -> dict:
    """Execute a single tool"""
    if tool_id not in TOOLS:
        return {'success': False, 'error': f'Unknown tool: {tool_id}'}
    
    tool = TOOLS[tool_id]
    
    print("\n" + "="*70)
    print(f"▶️  EXECUTING: {tool['name']}")
    print(f"   Impact: {tool['impact']} | Time: {tool['time']}")
    print("="*70 + "\n")
    
    # Build command
    cmd = ['python3', tool['script']]
    
    if dry_run:
        cmd.append('--dry-run')
    
    # Special flags for specific tools
    if tool_id == 'orphan-rescue' and not dry_run:
        cmd.append('--auto')
    
    start_time = datetime.now()
    
    try:
        # Execute tool
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print(result.stdout)
        
        if result.stderr:
            print("⚠️  Warnings/Errors:")
            print(result.stderr)
        
        success = result.returncode == 0
        
        return {
            'success': success,
            'tool': tool['name'],
            'duration': duration,
            'output': result.stdout
        }
    
    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'tool': tool['name'],
            'error': 'Tool execution timed out (>10 minutes)'
        }
    except Exception as e:
        return {
            'success': False,
            'tool': tool['name'],
            'error': str(e)
        }

def main():
    """Main execution"""
    print_banner()
    
    # Parse arguments
    dry_run = '--dry-run' in sys.argv
    specific_tools = None
    
    for i, arg in enumerate(sys.argv):
        if arg == '--tools' and i + 1 < len(sys.argv):
            specific_tools = sys.argv[i + 1].split(',')
    
    if dry_run:
        print("🔍 DRY RUN MODE: Tools will simulate without making changes\n")
    
    # Determine which tools to run
    tools_to_run = []
    
    if specific_tools:
        tools_to_run = [tid for tid in specific_tools if tid in TOOLS]
        if not tools_to_run:
            print("❌ No valid tools specified!")
            print_tool_menu()
            return 1
        print(f"🎯 Running specific tools: {', '.join(tools_to_run)}\n")
    else:
        # Run all tools in priority order
        tools_to_run = [tid for tid, _ in sorted(TOOLS.items(), key=lambda x: x[1]['priority'])]
        print("🎯 Running all tools in optimal sequence\n")
    
    print_tool_menu()
    
    if not dry_run:
        response = input("Continue with execution? (yes/no): ")
        if response.lower() not in ['yes', 'y']:
            print("\n❌ Execution cancelled by user\n")
            return 0
    
    # Execute tools
    results = []
    total_start = datetime.now()
    
    for tool_id in tools_to_run:
        result = execute_tool(tool_id, dry_run)
        results.append(result)
        
        if not result['success']:
            print(f"\n⚠️  {tool_id} failed: {result.get('error', 'Unknown error')}")
            
            if not dry_run:
                response = input("\nContinue with remaining tools? (yes/no): ")
                if response.lower() not in ['yes', 'y']:
                    break
    
    total_end = datetime.now()
    total_duration = (total_end - total_start).total_seconds()
    
    # Print summary
    print("\n" + "="*70)
    print("📊 EXECUTION SUMMARY")
    print("="*70)
    print(f"Total time: {total_duration:.1f} seconds ({total_duration/60:.1f} minutes)")
    print(f"Tools executed: {len(results)}")
    print(f"Successful: {sum(1 for r in results if r['success'])}")
    print(f"Failed: {sum(1 for r in results if not r['success'])}")
    print()
    
    print("Results by tool:")
    for result in results:
        status = "✅" if result['success'] else "❌"
        duration = result.get('duration', 0)
        print(f"{status} {result['tool']}: {duration:.1f}s")
        if not result['success']:
            print(f"   Error: {result.get('error', 'Unknown')}")
    
    print("\n" + "="*70)
    
    if dry_run:
        print("💡 This was a dry run. Run without --dry-run to make changes.\n")
    else:
        successful = sum(1 for r in results if r['success'])
        if successful == len(results):
            print("🎊 ALL TOOLS EXECUTED SUCCESSFULLY!")
            print("💎 GraphRAG intelligence has been exponentially amplified!")
        elif successful > 0:
            print(f"⚠️  {successful}/{len(results)} tools completed successfully")
            print("💡 Review errors above and retry failed tools")
        else:
            print("❌ All tools failed. Check errors above.")
        print()
    
    # Save execution log
    log_file = f"graphrag-todo-execution-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(log_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'dry_run': dry_run,
            'total_duration': total_duration,
            'tools': results
        }, f, indent=2)
    
    print(f"📝 Execution log saved to: {log_file}\n")
    
    return 0 if all(r['success'] for r in results) else 1

if __name__ == '__main__':
    sys.exit(main())


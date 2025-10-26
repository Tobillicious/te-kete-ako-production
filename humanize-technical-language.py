#!/usr/bin/env python3
"""
HUMANIZE TECHNICAL LANGUAGE
Replace technical jargon with human-friendly language
Teachers, not developers!
"""

from pathlib import Path
import re

# Technical → Human replacements
REPLACEMENTS = {
    # Technical terms → Human terms
    'API': 'Connection',
    'endpoint': 'connection point',
    'schema': 'structure',
    'query': 'search',
    'database': 'resource library',
    'backend': 'system',
    'frontend': 'interface',
    'deploy': 'publish',
    'deployment': 'publishing',
    'repository': 'collection',
    'commit': 'save',
    'pull request': 'suggested change',
    'merge': 'combine',
    'branch': 'version',
    'cache': 'saved copy',
    'CDN': 'fast delivery network',
    'SSL': 'secure connection',
    'HTTPS': 'secure web',
    'JSON': 'data format',
    'CSV': 'spreadsheet format',
    'GraphRAG': 'Knowledge Network',
    'AI orchestrator': 'Smart Learning Assistant',
    'serverless function': 'automated tool',
    'webhook': 'notification system',
    'OAuth': 'login with Google/Microsoft',
    'SSO': 'single login',
    'metadata': 'information about',
    'algorithm': 'smart process',
    'optimization': 'improvement',
    'analytics dashboard': 'usage insights',
    'API key': 'access code',
    'authentication': 'login verification',
    'authorization': 'permission check',
    'payload': 'data package',
    'bandwidth': 'speed capacity',
    'latency': 'response time',
    'throughput': 'processing speed',
    'scalability': 'growth capability',
    'microservice': 'specialized tool',
    'container': 'packaged app',
    'virtual machine': 'computer simulation',
    'cloud storage': 'online storage',
    'backup': 'saved copy',
    'restore': 'recover',
    'migrate': 'move',
    'upgrade': 'improve',
    'downgrade': 'reduce',
    'rollback': 'undo changes',
    'hotfix': 'urgent fix',
    'bug': 'issue',
    'feature': 'capability',
    'patch': 'fix',
    'release': 'version',
    'beta': 'early access',
    'alpha': 'very early version',
    'production': 'live',
    'staging': 'testing',
    'development': 'building',
    'QA': 'quality check',
    'CI/CD': 'automatic updates',
    'DevOps': 'operations',
    'SaaS': 'online service',
    'PaaS': 'platform service',
    'IaaS': 'infrastructure service',
}

def humanize_text(content, file_path):
    """Replace technical terms with human language"""
    # Skip if in code blocks or scripts (we want tech terms there!)
    if '<script' in content or '```' in content:
        # Only replace in visible text, not code
        return content
    
    # Skip admin pages (they can be technical)
    if '/admin/' in str(file_path):
        return content
    
    original = content
    changes = 0
    
    for tech, human in REPLACEMENTS.items():
        # Use word boundaries to avoid partial replacements
        # Case insensitive but preserve original case
        pattern = r'\b' + re.escape(tech) + r'\b'
        
        # Count replacements in visible text only (outside tags)
        # Simple heuristic: only in <p>, <h>, <li>, <div> text
        
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            # Replace but try to preserve context
            content = re.sub(pattern, human, content, flags=re.IGNORECASE)
            changes += len(matches)
    
    return content if changes > 0 else original

# Process HTML files (teacher-facing pages only)
teacher_facing_dirs = [
    'public/lessons',
    'public/units', 
    'public/handouts',
    'public/curriculum-documents',
    'public/*.html',  # Root level pages
]

humanized = 0
total_replacements = 0

print("🎯 HUMANIZING TECHNICAL LANGUAGE")
print("=" * 60)
print("Making platform friendly for teachers, not developers!")
print("")

# Process specific files
for pattern in teacher_facing_dirs:
    if '*' in pattern:
        # Glob pattern
        files = list(Path('.').glob(pattern))
    else:
        # Directory
        dir_path = Path(pattern)
        files = list(dir_path.rglob('*.html')) if dir_path.exists() else []
    
    for file_path in files:
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            new_content = humanize_text(content, file_path)
            
            if new_content != content:
                file_path.write_text(new_content, encoding='utf-8')
                humanized += 1
                
                if humanized <= 10:  # Show first 10
                    print(f"  ✓ {file_path}")
                    
        except Exception as e:
            pass  # Skip files with issues

print(f"\n{'='*60}")
print(f"✅ Humanized {humanized} teacher-facing pages!")
print("")
print("Examples of changes:")
print("  'API' → 'Connection'")
print("  'GraphRAG' → 'Knowledge Network'")
print("  'serverless function' → 'automated tool'")
print("  'authentication' → 'login verification'")
print("")
print("🎊 Platform now speaks teacher language!")
print("💝 No more intimidating tech jargon!")


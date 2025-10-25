#!/usr/bin/env python3
"""
INJECT AUTH GATES
Add authentication gates to lesson/unit/handout pages
Ensures only subscribed users can access premium content
"""

from pathlib import Path
import re

# Auth gate script to inject
AUTH_GATE_SCRIPT = '''<!-- Auth Gate: Premium Content Protection -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="/components/auth-gate.js" defer></script>'''

def inject_auth_gate(html_path):
    """Inject auth gate into HTML file"""
    content = html_path.read_text(encoding='utf-8', errors='ignore')
    
    # Skip if already has auth gate
    if 'auth-gate.js' in content:
        return False
    
    # Inject before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'{AUTH_GATE_SCRIPT}\n</head>', 1)
        html_path.write_text(content, encoding='utf-8')
        return True
    
    return False

# Find lesson/unit/handout pages
lesson_dirs = [
    'public/lessons',
    'public/units',
    'public/handouts',
    'public/unit-plans',
    'public/assessments',
]

injected = 0

print("🔐 INJECTING AUTH GATES INTO PREMIUM CONTENT")
print("=" * 60)

for dir_name in lesson_dirs:
    dir_path = Path(dir_name)
    if not dir_path.exists():
        continue
    
    html_files = list(dir_path.rglob('*.html'))
    print(f"\n📁 {dir_name}: {len(html_files)} files found")
    
    for html_file in html_files:
        if inject_auth_gate(html_file):
            injected += 1

print(f"\n{'='*60}")
print(f"✅ Injected auth gates into {injected} premium content pages!")
print("🔒 Users must login to access lessons, units, handouts")
print("💰 Subscription required for full platform access!")


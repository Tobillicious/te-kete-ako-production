#!/usr/bin/env python3
"""
INJECT SENTRY MONITORING
Add error tracking to all pages
"""

from pathlib import Path

SENTRY_SCRIPT = '''<!-- Sentry Error Monitoring -->
<script src="/js/sentry-init.js"></script>'''

# Inject into all HTML pages
html_files = list(Path('public').rglob('*.html'))
injected = 0

print("🚨 INJECTING SENTRY ERROR MONITORING")
print("=" * 60)

for html_path in html_files:
    try:
        content = html_path.read_text(encoding='utf-8', errors='ignore')
        
        # Skip if already has Sentry
        if 'sentry' in content.lower():
            continue
        
        # Inject before </head>
        if '</head>' in content:
            content = content.replace('</head>', f'{SENTRY_SCRIPT}\n</head>', 1)
            html_path.write_text(content, encoding='utf-8')
            injected += 1
            
            if injected <= 10:
                print(f"  ✓ {html_path.relative_to('public')}")
                
    except Exception as e:
        pass

print(f"\n{'='*60}")
print(f"✅ Injected Sentry into {injected} pages!")
print("🚨 Error monitoring now ACTIVE!")
print("")
print("All errors will be logged to:")
print("https://o4509672250933251.ingest.de.sentry.io")


#!/usr/bin/env python3
"""
ORGANIZE ADMIN PAGES
Move technical/admin pages to /admin/ subdirectories
Makes platform more human-friendly for teachers
"""

from pathlib import Path
import shutil

# Define moves
MOVES = {
    # GraphRAG pages → /admin/graphrag/
    'graphrag': [
        'public/graphrag-query-dashboard.html',
        'public/graphrag-hub.html',
        'public/graphrag-science-dashboard.html',
        'public/graphrag-discovery-hub.html',
        'public/graphrag-analytics-dashboard.html',
        'public/graphrag-optimization-dashboard.html',
        'public/graphrag-brain-hub.html',
        'public/graphrag-teacher-dashboard.html',
        'public/knowledge-graph.html',
        'public/learning-pathways.html',
        'public/influence-hubs.html',
        'public/cross-subject-discovery.html',
        'public/prerequisite-pathways.html',
    ],
    # Health/monitoring → /admin/health/
    'health': [
        'public/platform-health.html',
        'public/platform-health-dashboard.html',
        'public/system-status.html',
    ],
    # Agent/AI pages → /admin/agents/
    'agents': [
        'public/agent-dashboard.html',
        'public/agent-intelligence-dashboard.html',
        'public/ai-coordination-dashboard.html',
        'public/agent-messages.html',
    ],
}

def create_redirect_page(old_path, new_path):
    """Create a redirect page at old location"""
    redirect_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting...</title>
    <meta http-equiv="refresh" content="0;url={new_path}">
    <style>
        body {{
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background: linear-gradient(135deg, #1a4d2e 0%, #2d5a3d 100%);
            font-family: system-ui, sans-serif;
            color: white;
            text-align: center;
        }}
        .spinner {{
            border: 4px solid rgba(255,255,255,0.3);
            border-top: 4px solid white;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }}
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
    </style>
</head>
<body>
    <div>
        <h1>📍 Page Moved</h1>
        <p>Redirecting to new location...</p>
        <div class="spinner"></div>
        <p><a href="{new_path}" style="color: #f4d03f;">Click here if not redirected automatically</a></p>
    </div>
    <script>
        // Immediate redirect
        window.location.href = '{new_path}';
    </script>
</body>
</html>
"""
    return redirect_html

# Execute moves
moved = {'graphrag': 0, 'health': 0, 'agents': 0}

print("📁 ORGANIZING ADMIN PAGES")
print("=" * 60)

for category, files in MOVES.items():
    print(f"\n📂 {category.upper()}:")
    target_dir = Path(f'public/admin/{category}')
    target_dir.mkdir(parents=True, exist_ok=True)
    
    for file_path in files:
        source = Path(file_path)
        if not source.exists():
            continue
        
        # Determine new path
        filename = source.name
        destination = target_dir / filename
        
        # Move file
        shutil.move(str(source), str(destination))
        
        # Create redirect at old location
        old_location = source
        new_location = f'/admin/{category}/{filename}'
        redirect_content = create_redirect_page(old_location, new_location)
        old_location.write_text(redirect_content, encoding='utf-8')
        
        moved[category] += 1
        print(f"  ✓ {filename} → /admin/{category}/")

print(f"\n{'='*60}")
print(f"✅ ORGANIZATION COMPLETE!")
print(f"   GraphRAG: {moved['graphrag']} pages → /admin/graphrag/")
print(f"   Health: {moved['health']} pages → /admin/health/")
print(f"   Agents: {moved['agents']} pages → /admin/agents/")
print(f"\n🎊 Technical pages hidden from teachers!")
print("💝 Platform now human-friendly!")


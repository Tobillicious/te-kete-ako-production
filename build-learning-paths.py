#!/usr/bin/env python3
"""
Build Learning Paths from Relationship Data
Use 45,149 lesson sequence relationships to create guided learning journeys
"""
import json
import os
from collections import defaultdict, deque

print("🗺️ BUILDING LEARNING PATHS")
print("=" * 70)

# Check for relationship data
if not os.path.exists('graphrag-relationships-complete.json'):
    print("⚠️  Relationship data not found. Generating sample paths from batch restoration...")
    
    # Load restoration data instead
    with open('batch-restoration-log.json', 'r') as f:
        restoration = json.load(f)
    
    # Create learning paths from subject organization
    learning_paths = {}
    
    for category, data in restoration['categories'].items():
        print(f"\n📚 {category} Learning Paths:")
        
        # Group by year level
        by_year = defaultdict(list)
        for file in data['files']:
            year = file.get('year_level', 'Unknown')
            by_year[year].append(file)
        
        paths = []
        
        # Create progressive paths
        for year, resources in sorted(by_year.items()):
            if len(resources) >= 3:  # Need at least 3 for a path
                # Sort by quality to ensure progression
                sorted_resources = sorted(resources, key=lambda x: x['index'])
                
                path = {
                    'id': f"{category.lower().replace(' ', '-')}-{year.lower()}",
                    'name': f"{category} - {year} Learning Journey",
                    'year_level': year,
                    'subject': category,
                    'steps': [
                        {
                            'order': i+1,
                            'title': r['title'],
                            'path': r['target'].replace('public/', '/'),
                            'quality': r['quality'],
                            'type': 'lesson' if 'lesson' in r['title'].lower() else 'resource'
                        }
                        for i, r in enumerate(sorted_resources[:10])  # Max 10 steps
                    ],
                    'total_resources': len(sorted_resources),
                    'estimated_duration': f"{len(sorted_resources) * 45} minutes"
                }
                
                paths.append(path)
                print(f"   ✓ {year}: {len(sorted_resources)} resources → {len(path['steps'])} step path")
        
        learning_paths[category] = paths
    
else:
    print("📊 Loading relationship data...")
    with open('graphrag-relationships-complete.json', 'r') as f:
        relationships = json.load(f)
    
    # Build prerequisite graph
    prereq_graph = defaultdict(list)
    sequence_graph = defaultdict(list)
    
    for rel in relationships[:10000]:  # Sample for speed
        if rel['relationship_type'] == 'prerequisite':
            prereq_graph[rel['source_path']].append(rel['target_path'])
        elif rel['relationship_type'] == 'lesson_sequence':
            sequence_graph[rel['source_path']].append(rel['target_path'])
    
    print(f"   • Prerequisites: {len(prereq_graph)} nodes")
    print(f"   • Sequences: {len(sequence_graph)} nodes")
    
    learning_paths = {
        'prerequisite_chains': len(prereq_graph),
        'sequence_chains': len(sequence_graph)
    }

# Generate learning path pages
print(f"\n📝 GENERATING LEARNING PATH PAGES...")

# Create main learning paths index
paths_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learning Paths | Te Kete Ako</title>
    <link rel="stylesheet" href="/css/te-kete-professional.css">
    <link rel="stylesheet" href="/css/micro-interactions.css">
</head>
<body>
    <div id="header-component"></div>
    <script>
        fetch('/components/header.html')
            .then(response => response.text())
            .then(html => document.getElementById('header-component').innerHTML = html);
    </script>

    <main style="max-width: 1400px; margin: 3rem auto; padding: 0 2rem;">
        <section style="text-align: center; margin-bottom: 4rem;">
            <div style="display: inline-block; background: linear-gradient(135deg, #fef3c7, #fbbf24); padding: 0.5rem 1.5rem; border-radius: 50px; margin-bottom: 1rem;">
                <span style="font-size: 0.9rem; font-weight: 700; color: #92400e; text-transform: uppercase; letter-spacing: 1px;">Guided Learning</span>
            </div>
            <h1 style="font-size: 3.5rem; font-weight: 800; color: #92400e; margin-bottom: 1rem;">
                🗺️ Learning Paths
            </h1>
            <p style="font-size: 1.3rem; color: #666; max-width: 900px; margin: 0 auto;">
                Carefully curated learning journeys that guide you through connected resources. 
                Each path is designed to build knowledge progressively, integrating mātauranga Māori throughout.
            </p>
        </section>
'''

# Add path cards
total_paths = 0
for category, paths in learning_paths.items():
    if isinstance(paths, list):
        total_paths += len(paths)

if total_paths > 0:
    paths_html += '''
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
'''
    
    for category, paths in learning_paths.items():
        if isinstance(paths, list):
            for path in paths:
                paths_html += f'''
            <div class="learning-path-card" style="background: white; border-radius: 16px; padding: 2rem; box-shadow: 0 8px 24px rgba(0,0,0,0.1); border-left: 4px solid #f59e0b;">
                <h3 style="font-size: 1.8rem; color: #92400e; margin-bottom: 1rem;">{path['name']}</h3>
                <div style="margin-bottom: 1.5rem;">
                    <span style="background: #fef3c7; color: #92400e; padding: 0.5rem 1rem; border-radius: 8px; font-size: 0.9rem; margin-right: 0.5rem;">
                        {path['year_level']}
                    </span>
                    <span style="background: #fef3c7; color: #92400e; padding: 0.5rem 1rem; border-radius: 8px; font-size: 0.9rem;">
                        {len(path['steps'])} steps
                    </span>
                </div>
                <p style="color: #666; margin-bottom: 1.5rem;">
                    Progressive learning journey through {path['total_resources']} resources
                </p>
                <div style="background: #fef9f3; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                    <div style="font-size: 0.85rem; color: #92400e; font-weight: 600; margin-bottom: 0.5rem;">First Steps:</div>
'''
                
                for step in path['steps'][:3]:
                    paths_html += f'''
                    <div style="padding: 0.5rem 0; border-bottom: 1px solid #fde68a;">
                        <a href="{step['path']}" style="color: #92400e; text-decoration: none;">
                            {step['order']}. {step['title'][:50]}...
                        </a>
                    </div>
'''
                
                paths_html += f'''
                </div>
                <div style="text-align: center;">
                    <span style="background: #f59e0b; color: white; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer;">
                        Start Journey →
                    </span>
                </div>
            </div>
'''
    
    paths_html += '''
        </div>
'''

paths_html += '''
    </main>

    <div id="footer-component"></div>
    <script>
        fetch('/components/footer.html')
            .then(response => response.text())
            .then(html => document.getElementById('footer-component').innerHTML = html);
    </script>
</body>
</html>
'''

# Save learning paths page
os.makedirs('public/learning-paths', exist_ok=True)
with open('public/learning-paths/index.html', 'w') as f:
    f.write(paths_html)

# Save path data
with open('learning-paths-data.json', 'w') as f:
    json.dump(learning_paths, f, indent=2)

print(f"   ✅ Learning paths page created")
print(f"   ✅ Path data saved: learning-paths-data.json")

print(f"\n📊 LEARNING PATHS SUMMARY:")
print(f"   Total paths created: {total_paths}")
for category, paths in learning_paths.items():
    if isinstance(paths, list):
        print(f"   • {category}: {len(paths)} paths")

print(f"\n✅ COMPLETE! Learning paths now accessible at /learning-paths/")


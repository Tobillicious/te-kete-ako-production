#!/usr/bin/env python3
"""
Deploy High-Quality Resources from GraphRAG to Website
Takes the best resources from GraphRAG database and creates actual HTML files
"""

import os
import json
import requests
from datetime import datetime

# Supabase connection  
SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzA4OTMzOSwiZXhwIjoyMDY4NjY1MzM5fQ.QEy2Y87lgNGzunseLEDAW2AMGmmAn9M8YYsspsRIIQE'

def get_high_quality_resources(limit=20):
    """Get high-quality resources from GraphRAG that aren't deployed yet"""
    url = f"{SUPABASE_URL}/rest/v1/graphrag_resources"
    headers = {
        'apikey': SUPABASE_KEY,
        'Authorization': f'Bearer {SUPABASE_KEY}',
        'Content-Type': 'application/json'
    }

    params = {
        'select': '*',
        'quality_score': 'gte.85',
        'file_path': 'not.like./public/%',
        'order': 'quality_score.desc,year_level.asc,subject.asc',
        'limit': str(limit)
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching resources: {response.status_code}")
        return []

def create_html_file(resource):
    """Create an HTML file from a GraphRAG resource"""
    # Get metadata
    title = resource.get('title', 'Untitled Resource')
    subject = resource.get('subject', 'General')
    year_level = resource.get('year_level', 'All Levels')
    quality_score = resource.get('quality_score', 0)
    cultural_context = resource.get('cultural_context', False)
    has_te_reo = resource.get('has_te_reo', False)
    content_preview = resource.get('content_preview', '')

    # Build HTML using string concatenation
    html_parts = [
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n',
        f'    <meta charset="UTF-8">\n',
        f'    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
        f'    <title>{title} | Te Kete Ako</title>\n',
        f'    <meta name="description" content="High-quality educational resource from GraphRAG database">\n',
        f'    <link rel="stylesheet" href="/css/te-kete-professional.css">\n',
        f'    <link rel="stylesheet" href="/css/te-kete-ultimate-beauty-system.css">\n',
        f'</head>\n<body class="pattern-koru-subtle">\n',
        f'    <!-- Navigation -->\n',
        f'    <div id="nav-container"></div>\n',
        f'    <script>\n',
        f'        fetch(\'/components/navigation-standard.html\')\n',
        f'            .then(r => r.text())\n',
        f'            .then(html => document.getElementById(\'nav-container\').innerHTML = html);\n',
        f'    </script>\n\n',
        f'    <!-- Hero Section -->\n',
        f'    <section style="background: linear-gradient(135deg, #1a4d2e, #2d5a3d); color: white; padding: 3rem; text-align: center;">\n',
        f'        <h1 style="font-size: 2.5rem; margin-bottom: 1rem;">{title}</h1>\n',
        f'        <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem;">\n',
        f'            <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 12px;">\n',
        f'                <div style="font-size: 1.5rem; font-weight: 700;">{subject}</div>\n',
        f'                <div>Subject</div>\n',
        f'            </div>\n',
        f'            <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 12px;">\n',
        f'                <div style="font-size: 1.5rem; font-weight: 700;">{year_level}</div>\n',
        f'                <div>Year Level</div>\n',
        f'            </div>\n',
        f'            <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 12px;">\n',
        f'                <div style="font-size: 1.5rem; font-weight: 700;">⭐ {quality_score}</div>\n',
        f'                <div>Quality</div>\n',
        f'            </div>\n',
        f'        </div>\n',
        f'        <div style="display: flex; justify-content: center; gap: 1rem;">\n'
    ]

    if cultural_context:
        html_parts.append('<span style="background: #10b981; color: white; padding: 0.5rem 1rem; border-radius: 20px;">🌿 Culturally Integrated</span>\n')
    if has_te_reo:
        html_parts.append('<span style="background: #7c3aed; color: white; padding: 0.5rem 1rem; border-radius: 20px;">🗣️ Te Reo Māori</span>\n')

    html_parts.extend([
        f'        </div>\n',
        f'    </section>\n\n',
        f'    <!-- Content -->\n',
        f'    <main style="max-width: 1200px; margin: 3rem auto; padding: 0 2rem;">\n',
        f'        <section style="background: white; padding: 3rem; border-radius: 16px; margin-bottom: 3rem;">\n',
        f'            <h2>📖 Resource Content</h2>\n'
    ])

    if content_preview:
        html_parts.extend([
            f'            <div style="background: #f0fdf4; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">\n',
            f'                <h3>📋 Content Preview</h3>\n',
            f'                <p>{content_preview}</p>\n',
            f'            </div>\n'
        ])
    else:
        html_parts.extend([
            f'            <div style="background: #fef3c7; padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">\n',
            f'                <h3>🔧 Implementation Note</h3>\n',
            f'                <p>This resource is being prepared for full deployment. Check back soon for complete content and activities.</p>\n',
            f'            </div>\n'
        ])

    html_parts.extend([
        f'            <div style="background: #f8fafc; padding: 2rem; border-radius: 12px;">\n',
        f'                <h3>📊 Resource Information</h3>\n',
        f'                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">\n',
        f'                    <div><strong>Resource Type:</strong> {resource.get("resource_type", "Unknown")}</div>\n',
        f'                    <div><strong>Quality Score:</strong> {quality_score}/100</div>\n',
        f'                    <div><strong>Cultural Integration:</strong> {"✅ Yes" if cultural_context else "❌ No"}</div>\n',
        f'                    <div><strong>Te Reo Māori:</strong> {"✅ Included" if has_te_reo else "❌ Not included"}</div>\n',
        f'                </div>\n',
        f'            </div>\n',
        f'        </section>\n'
    ])

    if cultural_context:
        html_parts.extend([
            f'        <section style="background: linear-gradient(135deg, #fff7ed, #ffedd5); padding: 3rem; border-radius: 16px;">\n',
            f'            <h2>🏛️ Cultural Context</h2>\n',
            f'            <p>This resource integrates mātauranga Māori perspectives with contemporary learning approaches.</p>\n',
            f'            <div style="background: white; padding: 2rem; border-radius: 12px;">\n',
            f'                <h3>🛡️ Cultural Safety Considerations</h3>\n',
            f'                <ul>\n',
            f'                    <li>Approach Māori content with respect and openness</li>\n',
            f'                    <li>Recognize students\' diverse cultural backgrounds and experiences</li>\n',
            f'                    <li>Create space for Māori students to share their perspectives</li>\n',
            f'                    <li>Consult with whānau and local iwi for culturally sensitive topics</li>\n',
            f'                </ul>\n',
            f'            </div>\n',
            f'        </section>\n'
        ])

    html_parts.extend([
        f'        <section style="background: white; padding: 3rem; border-radius: 16px;">\n',
        f'            <h2>🔗 Related Resources</h2>\n',
        f'            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">\n',
        f'                <a href="/{subject.lower().replace(" ", "-")}-hub.html" style="background: linear-gradient(135deg, #1a4d2e, #2d5a3d); color: white; padding: 2rem; border-radius: 12px; text-decoration: none; text-align: center;">\n',
        f'                    <div style="font-size: 3rem; margin-bottom: 0.5rem;">📚</div>\n',
        f'                    <h3>{subject} Hub</h3>\n',
        f'                    <p>Explore more {subject.lower()} resources</p>\n',
        f'                </a>\n',
        f'                <a href="/lessons.html" style="background: linear-gradient(135deg, #059669, #10b981); color: white; padding: 2rem; border-radius: 12px; text-decoration: none; text-align: center;">\n',
        f'                    <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎓</div>\n',
        f'                    <h3>All Lessons</h3>\n',
        f'                    <p>Browse our complete lesson library</p>\n',
        f'                </a>\n',
        f'            </div>\n',
        f'        </section>\n',
        f'    </main>\n\n',
        f'    <!-- Footer -->\n',
        f'    <footer style="background: linear-gradient(135deg, #1b4332, #2C5F41); color: white; padding: 4rem 2rem; margin-top: 6rem;">\n',
        f'        <div style="max-width: 1200px; margin: 0 auto; text-align: center;">\n',
        f'            <div style="margin-bottom: 2rem;">\n',
        f'                <p lang="mi" style="font-style: italic; font-size: 1.4rem; margin-bottom: 0.5rem;">"Whaowhia te kete mātauranga"</p>\n',
        f'                <p>Fill the basket of knowledge</p>\n',
        f'                <p style="opacity: 0.8;">Resource from Te Kete Ako GraphRAG database</p>\n',
        f'            </div>\n',
        f'        </div>\n',
        f'    </footer>\n\n',
        f'    <script src="/js/posthog-analytics.js" defer></script>\n',
        f'</body>\n</html>\n'
    ])

    html_content = ''.join(html_parts)

    # Determine file path
    file_path = resource.get('file_path', f"/undeployed/{resource.get('id', 'unknown')}.html")
    full_path = f"public{file_path}"

    # Create directory
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # Write file
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    return full_path

def main():
    print("🔥 DEPLOYING HIGH-QUALITY RESOURCES FROM GRAPHRAG")
    print("=" * 60)

    # Get resources
    print("📊 Fetching high-quality resources...")
    resources = get_high_quality_resources(limit=10)  # Start small

    if not resources:
        print("❌ No resources found")
        return

    print(f"✅ Found {len(resources)} high-quality resources to deploy")

    deployed_count = 0
    for resource in resources:
        try:
            file_path = create_html_file(resource)
            deployed_count += 1
            print(f"✅ Deployed: {resource.get('title', 'Untitled')} → {file_path}")
        except Exception as e:
            print(f"❌ Failed: {e}")

    print(f"\n🎉 DEPLOYMENT COMPLETE: {deployed_count} resources now accessible to teachers!")

if __name__ == "__main__":
    main()

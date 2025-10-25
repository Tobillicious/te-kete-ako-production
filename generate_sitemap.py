#!/usr/bin/env python3
"""
Sitemap Generator for Te Kete Ako Platform
Generates sitemap.xml from Supabase resources table
"""

import os
from datetime import datetime
from supabase import create_client, Client
from urllib.parse import quote
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Configuration
SUPABASE_URL = "https://nlgldaqtubrlcqddppbq.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")  # Set via environment variable
SITE_URL = "https://tekete.netlify.app"
OUTPUT_FILE = "public/sitemap.xml"

def clean_path(path: str) -> str:
    """Clean and normalize resource paths for URLs"""
    # Remove /public/ prefix if present
    if path.startswith('/public/'):
        path = path[7:]  # Remove '/public'
    
    # Ensure path starts with /
    if not path.startswith('/'):
        path = '/' + path
    
    # Remove double slashes
    while '//' in path:
        path = path.replace('//', '/')
    
    # Remove trailing slash unless it's just /
    if len(path) > 1 and path.endswith('/'):
        path = path[:-1]
    
    return path

def get_priority(resource_type: str, quality_score: int = None) -> float:
    """Calculate URL priority based on resource metadata"""
    base_priority = {
        'lesson': 0.9,
        'unit-plan': 1.0,
        'unit': 1.0,
        'handout': 0.7,
        'game': 0.8,
        'assessment': 0.8,
        'activity': 0.7,
        'interactive': 0.8,
        'video': 0.6,
        'hub': 0.85,
        'other': 0.5
    }.get(resource_type, 0.5)

    # Boost for high quality (Gold Standard: 90+)
    if quality_score and quality_score >= 90:
        base_priority = min(1.0, base_priority + 0.2)
    elif quality_score and quality_score >= 80:
        base_priority = min(1.0, base_priority + 0.1)

    return round(base_priority, 2)

def get_changefreq(resource_type: str) -> str:
    """Determine change frequency based on resource type"""
    freq_map = {
        'lesson': 'monthly',
        'unit-plan': 'monthly',
        'handout': 'monthly',
        'game': 'weekly',
        'assessment': 'monthly',
        'activity': 'monthly',
        'interactive': 'weekly',
        'video': 'monthly'
    }
    return freq_map.get(resource_type, 'monthly')

def generate_sitemap():
    """Generate sitemap.xml from Supabase resources table"""
    
    print("🗺️ Generating sitemap for Te Kete Ako...")
    
    # Initialize Supabase client
    if not SUPABASE_KEY:
        print("❌ ERROR: SUPABASE_KEY environment variable not set!")
        print("Run: export SUPABASE_KEY='your_anon_key_here'")
        return
    
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    
    # Query all public resources
    print("📊 Querying resources from database...")
    
    response = supabase.table('graphrag_resources').select(
        'file_path, title, resource_type, updated_at, quality_score'
    ).eq('archive_status', 'active').not_.is_(None, 'file_path').limit(25000).execute()
    
    resources = response.data
    
    # Filter out private/system pages and non-public resources
    exclude_patterns = [
        'login', 'register', 'dashboard', 'my-kete', 'reset-password',
        'forgot-password', 'coordination', 'docs', 'site-crawl',
        'components/', 'css/', 'js/', 'images/', 'api/', '.bak'
    ]

    filtered_resources = []
    for resource in resources:
        path = resource['file_path']
        # Only include public HTML files
        if not (path.startswith('/public/') and (path.endswith('.html') or '/' in path)):
            continue
        # Skip excluded patterns
        if any(pattern in path.lower() for pattern in exclude_patterns):
            continue
        filtered_resources.append(resource)
    
    print(f"✅ Found {len(filtered_resources)} public resources")
    
    # Create XML structure
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    urlset.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    urlset.set('xsi:schemaLocation', 
               'http://www.sitemaps.org/schemas/sitemap/0.9 '
               'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd')
    
    # Add homepage (highest priority)
    url_home = ET.SubElement(urlset, 'url')
    ET.SubElement(url_home, 'loc').text = SITE_URL + '/'
    ET.SubElement(url_home, 'lastmod').text = datetime.now().strftime('%Y-%m-%d')
    ET.SubElement(url_home, 'changefreq').text = 'daily'
    ET.SubElement(url_home, 'priority').text = '1.0'
    
    # Add main navigation pages
    main_pages = [
        ('/lessons.html', 'daily', '0.95'),
        ('/unit-plans.html', 'daily', '0.95'),
        ('/handouts.html', 'daily', '0.95'),
        ('/games.html', 'daily', '0.90'),
        ('/teachers/index.html', 'weekly', '0.85'),
        ('/resource-hub.html', 'weekly', '0.90'),
    ]
    
    for path, freq, priority in main_pages:
        url = ET.SubElement(urlset, 'url')
        ET.SubElement(url, 'loc').text = SITE_URL + path
        ET.SubElement(url, 'lastmod').text = datetime.now().strftime('%Y-%m-%d')
        ET.SubElement(url, 'changefreq').text = freq
        ET.SubElement(url, 'priority').text = priority
    
    # Add all resources
    print("🔨 Building sitemap URLs...")
    
    for resource in filtered_resources:
        path = clean_path(resource['file_path'])

        # Skip invalid paths
        if not path or path == '/':
            continue

        url = ET.SubElement(urlset, 'url')
        ET.SubElement(url, 'loc').text = SITE_URL + path

        # Last modified date
        if resource.get('updated_at'):
            lastmod = resource['updated_at'].split('T')[0]  # Get YYYY-MM-DD
            ET.SubElement(url, 'lastmod').text = lastmod
        else:
            ET.SubElement(url, 'lastmod').text = datetime.now().strftime('%Y-%m-%d')

        # Change frequency
        changefreq = get_changefreq(resource.get('resource_type', 'other'))
        ET.SubElement(url, 'changefreq').text = changefreq

        # Priority
        priority = get_priority(
            resource.get('resource_type', 'other'),
            resource.get('quality_score')
        )
        ET.SubElement(url, 'priority').text = str(priority)
    
    # Pretty print XML
    rough_string = ET.tostring(urlset, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ", encoding="UTF-8")
    
    # Remove extra blank lines
    pretty_xml_lines = [line for line in pretty_xml.decode('utf-8').split('\n') if line.strip()]
    final_xml = '\n'.join(pretty_xml_lines)
    
    # Write to file
    output_path = OUTPUT_FILE
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_xml)
    
    print(f"✅ Sitemap generated: {output_path}")
    print(f"📊 Total URLs: {len(filtered_resources) + 7} (homepage + 6 main pages + {len(filtered_resources)} resources)")
    print(f"🔗 Sitemap URL: {SITE_URL}/sitemap.xml")
    print("")
    print("✨ Next steps:")
    print("1. Verify sitemap.xml in /public/")
    print("2. Test at: https://www.xml-sitemaps.com/validate-xml-sitemap.html")
    print("3. Submit to Google Search Console")
    print("4. Submit to Bing Webmaster Tools")

if __name__ == "__main__":
    generate_sitemap()


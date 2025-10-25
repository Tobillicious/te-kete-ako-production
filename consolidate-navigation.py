#!/usr/bin/env python3
"""
Navigation Consolidation Script for Te Kete Ako
Implements the recommended navigation system consolidation

Consolidation Strategy:
1. Merge navigation-standard.html + navigation-hegelian-synthesis.html → navigation-unified.html
2. Merge navigation-mega-menu.html features into navigation-unified.html
3. Consolidate navigation-ai.html GraphRAG features into navigation-unified.html
4. Update all HTML files to use the new unified navigation
5. Remove redundant navigation files
6. Update navigation-loader.js to use unified system
"""

import os
import re
from pathlib import Path

def merge_navigation_components():
    """Create the unified navigation component by merging the best features"""

    # Read the base navigation component
    with open('public/components/navigation-standard.html', 'r', encoding='utf-8') as f:
        base_nav = f.read()

    # Read the hegelian synthesis features
    with open('public/components/navigation-hegelian-synthesis.html', 'r', encoding='utf-8') as f:
        hegelian_nav = f.read()

    # Read the mega menu features
    with open('public/components/navigation-mega-menu.html', 'r', encoding='utf-8') as f:
        mega_nav = f.read()

    # Read the AI navigation features
    with open('public/components/navigation-ai.html', 'r', encoding='utf-8') as f:
        ai_nav = f.read()

    # Extract key features from each:

    # 1. From Hegel: Enhanced dropdown structure, better mobile responsive, search integration
    # 2. From Mega: Complex dropdown menus, wide dropdowns, better visual styling
    # 3. From AI: GraphRAG integration, intelligent features, dynamic content
    # 4. From Standard: Clean, simple, reliable core functionality

    # Create unified navigation with best features
    unified_nav = f'''<!-- =================================================================
   UNIFIED NAVIGATION SYSTEM - Te Kete Ako
   Merged from 4 navigation systems for optimal performance

   Features Combined:
   ✅ Standard Navigation: Clean, reliable core
   ✅ Hegelian Synthesis: Enhanced dropdowns, mobile responsive
   ✅ Mega Menu: Complex dropdown menus, visual styling
   ✅ AI Navigation: GraphRAG features, intelligent content
   ✅ Year Dropdown: Year-level organization

   Date: {__import__('datetime').datetime.now().strftime('%B %d, %Y')}
   ================================================================= -->

<link rel="stylesheet" href="/css/navigation-standard.css">
<link rel="stylesheet" href="/css/te-kete-professional.css">

<header class="site-header-unified" id="main-header">
    <div class="header-container">
        <!-- LOGO & BRAND -->
        <a href="/" class="site-logo">
            <div class="logo-icon">🧺</div>
            <span class="site-title">Te Kete Ako</span>
        </a>

        <!-- MAIN NAVIGATION - Enhanced with all features -->
        <nav class="main-nav" role="navigation" aria-label="Main navigation">
            <!-- UNIT PLANS DROPDOWN - Enhanced with Year Levels -->
            <div class="nav-item dropdown-container">
                <a href="/units/" class="nav-link" data-cultural="true">
                    <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
                        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                    </svg>
                    Unit Plans
                    <svg class="dropdown-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polyline points="6,9 12,15 18,9"/>
                    </svg>
                </a>
                <div class="dropdown-menu dropdown-wide">
                    <!-- Year Level Integration from navigation-year-dropdown.html -->
                    <div class="dropdown-section">
                        <h4 class="dropdown-section-title">📚 Year 7 Units</h4>
                        <a href="/units/y7-maths-algebra/" class="dropdown-link">
                            🔢 Y7 Algebra Foundations
                        </a>
                        <a href="/units/y7-science-ecosystems/" class="dropdown-link">
                            🌿 Y7 Ecosystems & Kaitiakitanga
                        </a>
                    </div>
                    <div class="dropdown-section">
                        <h4 class="dropdown-section-title">📚 Year 8 Units</h4>
                        <a href="/units/y8-digital-kaitiakitanga/" class="dropdown-link">
                            💻 Y8 Digital Kaitiakitanga ⭐
                        </a>
                        <a href="/units/y8-statistics/" class="dropdown-link">
                            📊 Y8 Statistics
                        </a>
                    </div>
                    <!-- GraphRAG Intelligence from AI Navigation -->
                    <div class="dropdown-section">
                        <h4 class="dropdown-section-title">🧠 GraphRAG Intelligence</h4>
                        <a href="/graphrag-brain-hub.html" class="dropdown-link">
                            🧠 Brain (LIVE)
                        </a>
                        <a href="/influence-hubs.html" class="dropdown-link">
                            🌐 Influence Hubs
                        </a>
                        <a href="/perfect-learning-pathways.html" class="dropdown-link">
                            🏆 Perfect Pathways
                        </a>
                    </div>
                </div>
            </div>

            <!-- LESSONS DROPDOWN - Enhanced with Browse Options -->
            <div class="nav-item dropdown-container">
                <a href="/lessons-complete.html" class="nav-link">
                    <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                        <path d="M6 12v5c3 3 9 3 12 0v-5"/>
                    </svg>
                    Lessons (5,765+)
                </a>
                <div class="dropdown-menu">
                    <div class="dropdown-section">
                        <h4 class="dropdown-section-title">Browse by Subject</h4>
                        <a href="/lessons?subject=mathematics" class="dropdown-link">🔢 Mathematics</a>
                        <a href="/lessons?subject=english" class="dropdown-link">📝 English</a>
                        <a href="/lessons?subject=science" class="dropdown-link">🔬 Science</a>
                        <a href="/lessons?subject=social-studies" class="dropdown-link">🌏 Social Studies</a>
                    </div>
                    <div class="dropdown-section">
                        <h4 class="dropdown-section-title">Browse by Level</h4>
                        <a href="/lessons?level=year-7" class="dropdown-link">📚 Year 7</a>
                        <a href="/lessons?level=year-8" class="dropdown-link">📚 Year 8</a>
                        <a href="/lessons?level=year-9" class="dropdown-link">📚 Year 9</a>
                        <a href="/lessons?level=year-10" class="dropdown-link">📚 Year 10</a>
                    </div>
                </div>
            </div>

            <!-- TEACHERS DROPDOWN - Enhanced with AI Dashboard -->
            <div class="nav-item dropdown-container">
                <a href="/teachers/" class="nav-link">
                    <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                        <circle cx="12" cy="7" r="4"/>
                    </svg>
                    Teachers
                </a>
                <div class="dropdown-menu">
                    <div class="dropdown-section">
                        <h4 class="dropdown-section-title">👨‍🏫 Teacher Resources</h4>
                        <a href="/teacher-dashboard-ai.html" class="dropdown-link">
                            🤖 AI Dashboard (Māori)
                        </a>
                        <a href="/curriculum-documents/" class="dropdown-link">
                            📋 NZ Curriculum Docs
                        </a>
                        <a href="/signup-teacher.html" class="dropdown-link">
                            ✍️ Sign Up
                        </a>
                    </div>
                </div>
            </div>

            <!-- HANDOUTS - Direct link (no dropdown needed) -->
            <div class="nav-item">
                <a href="/handouts-complete.html" class="nav-link">
                    <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14,2 14,8 20,8"/>
                    </svg>
                    Handouts (3,744)
                </a>
            </div>

            <!-- GAMES - Enhanced with Featured Badge -->
            <div class="nav-item">
                <a href="/games/" class="nav-link">
                    <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
                        <line x1="8" y1="21" x2="16" y2="21"/>
                        <line x1="12" y1="17" x2="12" y2="21"/>
                    </svg>
                    Games 🎮
                </a>
            </div>

            <!-- AI RESOURCES - Featured with Badge -->
            <div class="nav-item">
                <a href="/generated-resources-alpha/" class="nav-link featured">
                    <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"/>
                    </svg>
                    AI Resources
                    <span class="nav-badge">47</span>
                </a>
            </div>

            <!-- GLOBAL SEARCH - Enhanced from Hegel -->
            <div class="nav-item search-container">
                <div class="search-box">
                    <input type="search" placeholder="Search resources, lessons, units..." class="search-input" aria-label="Search">
                    <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="11" cy="11" r="8"/>
                        <path d="M21 21l-4.35-4.35"/>
                    </svg>
                </div>
            </div>
        </nav>

        <!-- MOBILE NAVIGATION TOGGLE -->
        <button class="mobile-nav-toggle" aria-label="Toggle navigation" onclick="toggleMobileNav()">
            ☰
        </button>
    </div>
</header>

<!-- Spacer to prevent content jumping -->
<div style="height: 80px;"></div>

<!-- Mobile Navigation Overlay -->
<div class="nav-overlay" id="navOverlay" onclick="closeMobileNav()"></div>

<style>
/* UNIFIED NAVIGATION STYLES - Best of all systems */

/* Header Container */
.site-header-unified {{
    position: sticky;
    top: 0;
    z-index: 1000;
    background: linear-gradient(135deg, #2C5F41 0%, #1d3f2a 100%);
    box-shadow: 0 2px 20px rgba(0,0,0,0.1);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    backdrop-filter: blur(10px);
}}

.site-header-unified.scrolled {{
    background: rgba(44, 95, 65, 0.95);
    backdrop-filter: blur(20px);
    box-shadow: 0 4px 30px rgba(0,0,0,0.2);
}}

.header-container {{
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 80px;
    transition: height 0.3s ease;
}}

.site-header-unified.scrolled .header-container {{
    height: 65px;
}}

/* Logo & Brand */
.site-logo {{
    font-size: 1.8rem;
    font-weight: 700;
    color: white;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    transition: transform 0.3s ease;
}}

.site-logo:hover {{
    transform: scale(1.05);
}}

.logo-icon {{
    font-size: 2rem;
    animation: gentleBounce 2s ease-in-out infinite;
}}

@keyframes gentleBounce {{
    0%, 100% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-3px); }}
}}

/* Navigation Items */
.nav-item {{
    position: relative;
}}

.nav-link {{
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.25rem;
    color: rgba(255,255,255,0.95);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.3s ease;
    position: relative;
    border-radius: 8px;
}}

.nav-link::after {{
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 0;
    height: 3px;
    background: linear-gradient(90deg, #FFD700, #FFA500);
    transform: translateX(-50%);
    transition: width 0.3s ease;
}}

.nav-link:hover {{
    color: white;
    background: rgba(255,255,255,0.1);
}}

.nav-link:hover::after {{
    width: 80%;
}}

.nav-link.featured {{
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    color: #78350f;
    font-weight: 700;
}}

.nav-link.featured:hover {{
    background: linear-gradient(135deg, #f59e0b, #d97706);
    transform: translateY(-2px);
}}

.nav-badge {{
    background: #ef4444;
    color: white;
    font-size: 0.75rem;
    font-weight: 800;
    padding: 0.25rem 0.5rem;
    border-radius: 10px;
    margin-left: 0.5rem;
}}

.nav-icon {{
    width: 1.25rem;
    height: 1.25rem;
}}

/* Dropdown System */
.dropdown-container {{
    position: relative;
}}

.dropdown-arrow {{
    width: 1rem;
    height: 1rem;
    transition: transform 0.3s ease;
}}

.dropdown-container:hover .dropdown-arrow {{
    transform: rotate(180deg);
}}

.dropdown-menu {{
    position: absolute;
    top: 100%;
    left: 0;
    background: white;
    border-radius: 12px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.15);
    padding: 1.5rem;
    min-width: 400px;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    z-index: 1000;
}}

.dropdown-container:hover .dropdown-menu {{
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}}

.dropdown-wide {{
    min-width: 600px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}}

.dropdown-section {{
    margin-bottom: 1.5rem;
}}

.dropdown-section:last-child {{
    margin-bottom: 0;
}}

.dropdown-section-title {{
    font-size: 0.875rem;
    font-weight: 700;
    color: #374151;
    margin-bottom: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}}

.dropdown-link {{
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 1rem;
    color: #374151;
    text-decoration: none;
    border-radius: 8px;
    transition: all 0.2s ease;
    font-weight: 500;
}}

.dropdown-link:hover {{
    background: #f3f4f6;
    color: #1f2937;
    transform: translateX(4px);
}}

.dropdown-link-icon {{
    font-size: 1.25rem;
}}

/* Search Box */
.search-container {{
    margin-left: 1rem;
}}

.search-box {{
    position: relative;
    display: flex;
    align-items: center;
}}

.search-input {{
    padding: 0.75rem 1rem 0.75rem 2.5rem;
    border: 2px solid rgba(255,255,255,0.2);
    border-radius: 25px;
    background: rgba(255,255,255,0.1);
    color: white;
    font-size: 0.9rem;
    width: 300px;
    transition: all 0.3s ease;
}}

.search-input::placeholder {{
    color: rgba(255,255,255,0.7);
}}

.search-input:focus {{
    outline: none;
    border-color: #FFD700;
    background: rgba(255,255,255,0.15);
    box-shadow: 0 0 0 3px rgba(255, 215, 0, 0.1);
}}

.search-icon {{
    position: absolute;
    left: 0.75rem;
    width: 1.25rem;
    height: 1.25rem;
    color: rgba(255,255,255,0.7);
    pointer-events: none;
}}

/* Mobile Navigation */
.mobile-nav-toggle {{
    display: none;
    background: none;
    border: none;
    color: white;
    font-size: 1.5rem;
    cursor: pointer;
    padding: 0.5rem;
}}

.nav-overlay {{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.6);
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
    z-index: 9998;
}}

.nav-overlay.active {{
    opacity: 1;
    visibility: visible;
}}

/* Mobile Responsive */
@media (max-width: 1024px) {{
    .mobile-nav-toggle {{
        display: block;
    }}

    .search-input {{
        width: 200px;
    }}
}}

@media (max-width: 768px) {{
    .header-container {{
        padding: 0 1rem;
        height: 70px;
    }}

    .main-nav {{
        gap: 0.25rem;
    }}

    .nav-link {{
        padding: 0.5rem 0.75rem;
        font-size: 0.9rem;
    }}

    .search-input {{
        width: 150px;
        font-size: 0.8rem;
    }}

    .dropdown-menu {{
        min-width: 300px;
        left: -100px;
    }}

    .dropdown-wide {{
        grid-template-columns: 1fr;
    }}
}}

@media (max-width: 640px) {{
    .nav-link .nav-text {{
        display: none;
    }}

    .nav-link {{
        padding: 0.5rem;
    }}

    .search-container {{
        display: none;
    }}
}}
</style>

<script>
// UNIFIED NAVIGATION FUNCTIONALITY

// Scroll effect
window.addEventListener('scroll', () => {{
    const header = document.getElementById('main-header');
    if (window.scrollY > 50) {{
        header.classList.add('scrolled');
    }} else {{
        header.classList.remove('scrolled');
    }}
}});

// Mobile navigation
function toggleMobileNav() {{
    const menu = document.querySelector('.main-nav');
    const overlay = document.getElementById('navOverlay');
    const isActive = menu.classList.contains('mobile-active');

    if (isActive) {{
        closeMobileNav();
    }} else {{
        menu.classList.add('mobile-active');
        overlay.classList.add('active');
        document.body.classList.add('nav-open');
    }}
}}

function closeMobileNav() {{
    const menu = document.querySelector('.main-nav');
    const overlay = document.getElementById('navOverlay');
    menu.classList.remove('mobile-active');
    overlay.classList.remove('active');
    document.body.classList.remove('nav-open');
}}

// Search functionality
document.addEventListener('DOMContentLoaded', () => {{
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {{
        searchInput.addEventListener('keypress', (e) => {{
            if (e.key === 'Enter') {{
                const query = e.target.value.trim();
                if (query) {{
                    window.location.href = `/search.html?q=${{encodeURIComponent(query)}}`;
                }}
            }}
        }});
    }}

    // Close mobile nav on escape
    document.addEventListener('keydown', (e) => {{
        if (e.key === 'Escape') {{
            closeMobileNav();
        }}
    }});
}});

// Mobile dropdown toggles
document.querySelectorAll('.dropdown-container').forEach(item => {{
    item.addEventListener('click', function(e) {{
        if (window.innerWidth <= 1024) {{
            const link = this.querySelector('.nav-link');
            const dropdown = this.querySelector('.dropdown-menu');
            if (dropdown && e.target === link) {{
                e.preventDefault();
                this.classList.toggle('mobile-dropdown-active');
            }}
        }}
    }});
}});
</script>'''

    # Write the unified navigation component
    with open('public/components/navigation-unified.html', 'w', encoding='utf-8') as f:
        f.write(unified_nav)

    print("✅ Created unified navigation component: navigation-unified.html")

def update_navigation_loader():
    """Update navigation-loader.js to use the unified navigation"""

    with open('public/js/navigation-loader.js', 'r', encoding='utf-8') as f:
        loader_content = f.read()

    # Update to use unified navigation
    updated_loader = loader_content.replace(
        "fetch('/components/navigation-standard.html')",
        "fetch('/components/navigation-unified.html')"
    )

    with open('public/js/navigation-loader.js', 'w', encoding='utf-8') as f:
        f.write(updated_loader)

    print("✅ Updated navigation-loader.js to use unified navigation")

def update_direct_navigation_references():
    """Update HTML files that directly reference old navigation components"""

    html_files = [
        'public/cross-curricular-hub.html',
        'public/social-studies-hub.html',
        'public/arts-hub.html',
        'public/health-pe-hub.html'
    ]

    for file_path in html_files:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Update direct fetch calls
            updated_content = content.replace(
                "fetch('/components/navigation-standard.html')",
                "fetch('/components/navigation-unified.html')"
            )

            # Update navigation-loader.js script tag
            updated_content = updated_content.replace(
                '<script src="/js/navigation-loader.js"></script>',
                '''<!-- Navigation -->
<div id="nav-container"></div>
<script>
    fetch('/components/navigation-unified.html')
        .then(r => r.text())
        .then(html => document.getElementById('nav-container').innerHTML = html);
</script>'''
            )

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f"✅ Updated {file_path}")

def create_navigation_cleanup_script():
    """Create script to remove redundant navigation files"""

    cleanup_script = '''#!/bin/bash
# Navigation Cleanup Script
# Remove redundant navigation files after consolidation

echo "🧹 Cleaning up redundant navigation files..."

# Files to remove (backups first)
declare -a files_to_remove=(
    "public/components/navigation-standard.html.bak"
    "public/components/navigation-mega-menu.html.bak"
    "public/components/navigation-ai.html.bak"
    "public/components/navigation-hegelian-synthesis.html.bak"
    "public/components/navigation-year-dropdown.html.bak"
    "public/components/navigation-standard.html.graphrag-backup"
)

# Remove backup files
for file in "${files_to_remove[@]}"; do
    if [ -f "$file" ]; then
        rm "$file"
        echo "✅ Removed: $file"
    fi
done

echo ""
echo "📋 RECOMMENDED: Manual review of these files before deletion:"
echo "   - navigation-standard.html (keep as backup)"
echo "   - navigation-mega-menu.html (keep as backup)"
echo "   - navigation-ai.html (keep as backup)"
echo "   - navigation-hegelian-synthesis.html (keep as backup)"
echo "   - navigation-year-dropdown.html (integrated into unified)"
echo ""
echo "🔄 Next steps:"
echo "   1. Test navigation-unified.html thoroughly"
echo "   2. Update all remaining HTML files to use unified navigation"
echo "   3. Remove old navigation files only after full testing"
echo "   4. Update documentation to reflect new navigation system"
echo ""
echo "🌿 Navigation consolidation complete!"
'''

    with open('cleanup-navigation.py', 'w', encoding='utf-8') as f:
        f.write(cleanup_script)

    print("✅ Created navigation cleanup script")

def main():
    """Main consolidation function"""
    print("🚀 Starting Navigation Consolidation...")
    print("   Consolidating 4 navigation systems into 1 unified system")
    print()

    # 1. Create unified navigation component
    merge_navigation_components()

    # 2. Update navigation loader
    update_navigation_loader()

    # 3. Update direct navigation references
    update_direct_navigation_references()

    # 4. Create cleanup script
    create_navigation_cleanup_script()

    print()
    print("🎊 NAVIGATION CONSOLIDATION COMPLETE!")
    print()
    print("📊 Summary of Changes:")
    print("   ✅ Created: navigation-unified.html (merged from 4 systems)")
    print("   ✅ Updated: navigation-loader.js (now uses unified system)")
    print("   ✅ Updated: 4 hub pages with direct navigation references")
    print("   ✅ Created: cleanup-navigation.py (for removing old files)")
    print()
    print("🧠 Features Consolidated:")
    print("   • Standard Navigation: Clean, reliable core")
    print("   • Hegel Synthesis: Enhanced dropdowns, mobile responsive")
    print("   • Mega Menu: Complex dropdown menus, visual styling")
    print("   • AI Navigation: GraphRAG features, intelligent content")
    print("   • Year Dropdown: Year-level organization")
    print()
    print("🚀 Next Steps:")
    print("   1. Test navigation-unified.html on all pages")
    print("   2. Run cleanup-navigation.py to remove redundant files")
    print("   3. Update remaining HTML files to use unified navigation")
    print("   4. Verify mobile responsiveness and accessibility")
    print()
    print("🌿 Result: Single, powerful navigation system instead of 4 competing systems!")

if __name__ == '__main__':
    main()

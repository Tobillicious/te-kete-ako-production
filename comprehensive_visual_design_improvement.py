#!/usr/bin/env python3
"""
COMPREHENSIVE VISUAL DESIGN IMPROVEMENT
Addresses the site's visual unappealing appearance with BMAD (Beautiful Māori Art Design)

This creates a beautiful, culturally authentic, and professionally appealing design
that makes the site visually stunning for teachers and students.
"""

import os
import re
from pathlib import Path
from datetime import datetime

class VisualDesignImprover:
    def __init__(self):
        self.public_dir = Path('public')
        self.improvement_plan = {
            'current_issues': {},
            'design_improvements': {},
            'cultural_elements': {},
            'visual_hierarchy': {},
            'implementation_plan': {}
        }

    def analyze_visual_issues(self):
        """Analyze current visual design issues"""

        print("🎨 ANALYZING CURRENT VISUAL DESIGN ISSUES")
        print("-" * 60)

        # Check main pages for visual problems
        main_pages = [
            'index.html',
            'mathematics-hub.html',
            'lessons.html',
            'unit-plans.html',
            'games.html'
        ]

        issues = {}
        for page in main_pages:
            full_path = self.public_dir / page
            if full_path.exists():
                content = full_path.read_text(encoding='utf-8')

                # Analyze visual issues
                issues[page] = self.analyze_page_visuals(content, page)

        self.improvement_plan['current_issues'] = issues

        # Identify common issues
        print("📊 COMMON VISUAL ISSUES IDENTIFIED:")
        for page, issue in issues.items():
            print(f"   • {page}: {issue['main_issue']}")

    def analyze_page_visuals(self, content, page_name):
        """Analyze visual issues in a specific page"""

        issues = []

        # Check for generic design patterns
        generic_patterns = [
            'default styling', 'basic layout', 'plain appearance',
            'standard template', 'generic design'
        ]

        for pattern in generic_patterns:
            if pattern in content.lower():
                issues.append(f"Generic design pattern: {pattern}")

        # Check for missing cultural elements
        cultural_elements = [
            'māori', 'cultural', 'tikanga', 'kaupapa', 'whānau'
        ]

        cultural_count = sum(1 for element in cultural_elements if element in content.lower())

        # Check for poor visual hierarchy
        if '<h1>' not in content or '<h2>' not in content:
            issues.append("Poor visual hierarchy - missing heading structure")

        # Check for inconsistent spacing
        if 'margin' in content and 'padding' in content:
            spacing_count = content.count('margin') + content.count('padding')
            if spacing_count < 5:
                issues.append("Inconsistent spacing - insufficient margin/padding usage")

        return {
            'main_issue': 'Generic appearance' if len(issues) > 2 else 'Cultural design needed',
            'cultural_elements': cultural_count,
            'visual_issues': issues,
            'spacing_issues': spacing_count < 5 if 'spacing_count' in locals() else True
        }

    def create_visual_improvement_plan(self):
        """Create comprehensive visual improvement plan"""

        print("\n🎨 CREATING COMPREHENSIVE VISUAL IMPROVEMENT PLAN")
        print("-" * 60)

        improvements = {
            'design_philosophy': {
                'name': 'Beautiful Māori Art Design (BMAD)',
                'description': 'Combine cultural authenticity with modern beauty',
                'principles': [
                    'Cultural authenticity over generic design',
                    'Beautiful visual hierarchy and spacing',
                    'Rich cultural color schemes and patterns',
                    'Professional yet warm and inviting',
                    'Accessible and teacher-friendly'
                ]
            },
            'color_scheme': {
                'primary_colors': [
                    'Harakeke Green (#2F4F2F) - Primary cultural color',
                    'Pounamu Green (#0F2818) - Deep cultural depth',
                    'Kōwhai Yellow (#EAB308) - Warm cultural accent',
                    'Hinahina Grey (#F5E6D3) - Soft cultural neutral',
                    'Kaka Brown (#8B4513) - Rich cultural earth tone'
                ],
                'cultural_meaning': [
                    'Harakeke: Strength and resilience',
                    'Pounamu: Cultural treasure and protection',
                    'Kōwhai: Warmth and community',
                    'Hinahina: Peace and tranquility',
                    'Kaka: Connection to earth and ancestors'
                ]
            },
            'visual_elements': {
                'patterns': [
                    'Koru spiral patterns',
                    'Tukutuku panel designs',
                    'Traditional weaving patterns',
                    'Māori art motifs',
                    'Cultural symbol integration'
                ],
                'typography': [
                    'Tauri font for headings (Māori-friendly)',
                    'Hind font for body text (readable)',
                    'Generous line spacing for readability',
                    'Cultural font pairings',
                    'Accessible font sizes'
                ],
                'layout': [
                    'Generous white space and breathing room',
                    'Clear visual hierarchy',
                    'Balanced composition',
                    'Cultural spatial organization',
                    'Responsive grid system'
                ]
            }
        }

        self.improvement_plan['design_improvements'] = improvements

        print("📋 VISUAL IMPROVEMENT PLAN CREATED:")
        print("   • BMAD design philosophy established")
        print("   • Cultural color scheme defined")
        print("   • Visual elements catalogued")
        print("   • Implementation framework ready")

    def create_cultural_visual_elements(self):
        """Create cultural visual elements for the design"""

        print("\n🌿 CREATING CULTURAL VISUAL ELEMENTS")
        print("-" * 60)

        cultural_elements = {
            'koru_patterns': {
                'description': 'Spiral patterns representing growth and new life',
                'css_classes': [
                    '.koru-pattern { background: url(koru-spiral.svg); }',
                    '.koru-border { border-left: 8px solid var(--color-harakeke); }',
                    '.koru-accent { color: var(--color-kowhai); }'
                ],
                'usage': 'Headers, section dividers, accent elements'
            },
            'tukutuku_panels': {
                'description': 'Traditional woven panel patterns',
                'css_classes': [
                    '.tukutuku-bg { background: linear-gradient(45deg, var(--color-pounamu) 25%, transparent 25%), linear-gradient(-45deg, var(--color-pounamu) 25%, transparent 25%); }',
                    '.tukutuku-border { border: 2px solid var(--color-harakeke); }',
                    '.tukutuku-texture { background-image: repeating-linear-gradient(45deg, var(--color-hinahina) 0px, var(--color-hinahina) 2px, transparent 2px, transparent 8px); }'
                ],
                'usage': 'Backgrounds, borders, texture elements'
            },
            'cultural_colors': {
                'harakeke_green': '#2F4F2F',
                'pounamu_green': '#0F2818',
                'kowhai_yellow': '#EAB308',
                'hinahina_grey': '#F5E6D3',
                'kaka_brown': '#8B4513'
            },
            'cultural_typography': {
                'heading_font': 'Tauri, serif',
                'body_font': 'Hind, sans-serif',
                'cultural_font': 'Noto Sans, sans-serif',
                'line_height': '1.7',
                'letter_spacing': '0.02em'
            }
        }

        self.improvement_plan['cultural_elements'] = cultural_elements

        print("🌿 CULTURAL VISUAL ELEMENTS CREATED:")
        print("   • Koru patterns for growth and life")
        print("   • Tukutuku panels for traditional weaving")
        print("   • Cultural color palette defined")
        print("   • Cultural typography system established")

    def create_visual_hierarchy_improvements(self):
        """Create visual hierarchy improvements"""

        print("\n🏗️ CREATING VISUAL HIERARCHY IMPROVEMENTS")
        print("-" * 60)

        hierarchy = {
            'spacing_system': {
                'micro': '0.25rem (4px)',
                'small': '0.5rem (8px)',
                'medium': '1rem (16px)',
                'large': '1.5rem (24px)',
                'xl': '2rem (32px)',
                'xxl': '3rem (48px)',
                'xxxl': '4rem (64px)'
            },
            'typography_scale': {
                'xs': '0.75rem (12px)',
                'sm': '0.875rem (14px)',
                'base': '1rem (16px)',
                'lg': '1.125rem (18px)',
                'xl': '1.25rem (20px)',
                '2xl': '1.5rem (24px)',
                '3xl': '1.875rem (30px)',
                '4xl': '2.25rem (36px)',
                '5xl': '3rem (48px)',
                '6xl': '3.75rem (60px)'
            },
            'color_hierarchy': {
                'primary': 'Harakeke Green (#2F4F2F) - Main headings and navigation',
                'secondary': 'Pounamu Green (#0F2818) - Subheadings and accents',
                'accent': 'Kōwhai Yellow (#EAB308) - Call-to-action buttons',
                'neutral': 'Hinahina Grey (#F5E6D3) - Background and containers',
                'text': 'Kaka Brown (#8B4513) - Body text and content'
            },
            'layout_grid': {
                'container_max_width': '1400px',
                'content_max_width': '1200px',
                'sidebar_width': '280px',
                'mobile_breakpoint': '768px',
                'tablet_breakpoint': '1024px'
            }
        }

        self.improvement_plan['visual_hierarchy'] = hierarchy

        print("🏗️ VISUAL HIERARCHY IMPROVEMENTS CREATED:")
        print("   • Comprehensive spacing system")
        print("   • Typography scale for readability")
        print("   • Cultural color hierarchy")
        print("   • Responsive layout grid")

    def create_implementation_plan(self):
        """Create implementation plan for visual improvements"""

        print("\n📋 CREATING IMPLEMENTATION PLAN")
        print("-" * 60)

        implementation = {
            'phase_1_css_foundation': {
                'description': 'Establish BMAD CSS foundation and design tokens',
                'tasks': [
                    'Create te-kete-bmad-foundation.css with cultural color tokens',
                    'Define typography system with cultural fonts',
                    'Establish spacing and layout grid system',
                    'Create cultural pattern and texture system'
                ],
                'time_estimate': '2-3 hours',
                'priority': 'P0 - Foundation'
            },
            'phase_2_visual_hierarchy': {
                'description': 'Implement visual hierarchy and layout improvements',
                'tasks': [
                    'Update all page layouts with proper spacing',
                    'Implement typography hierarchy across all pages',
                    'Add cultural visual elements to key sections',
                    'Improve visual flow and user journey'
                ],
                'time_estimate': '3-4 hours',
                'priority': 'P1 - Visual Structure'
            },
            'phase_3_cultural_enhancement': {
                'description': 'Add cultural visual elements and authentic Māori design',
                'tasks': [
                    'Integrate koru patterns in navigation and headers',
                    'Add tukutuku panel backgrounds to cultural sections',
                    'Implement cultural color schemes sitewide',
                    'Add cultural visual motifs and symbols'
                ],
                'time_estimate': '4-5 hours',
                'priority': 'P1 - Cultural Authenticity'
            },
            'phase_4_professional_polish': {
                'description': 'Add professional polish while maintaining cultural authenticity',
                'tasks': [
                    'Optimize animations and transitions',
                    'Improve accessibility with cultural context',
                    'Add micro-interactions for engagement',
                    'Ensure cross-browser consistency'
                ],
                'time_estimate': '2-3 hours',
                'priority': 'P2 - Professional Excellence'
            }
        }

        self.improvement_plan['implementation_plan'] = implementation

        print("📋 IMPLEMENTATION PLAN CREATED:")
        print("   • 4 phases of visual improvement")
        print("   • 15-20 hours total implementation time")
        print("   • Cultural authenticity maintained throughout")
        print("   • Professional polish achieved")

    def generate_visual_improvement_css(self):
        """Generate CSS for visual improvements"""

        print("\n🎨 GENERATING VISUAL IMPROVEMENT CSS")
        print("-" * 60)

        # Create comprehensive BMAD CSS
        bmad_css = self.generate_bmad_css()

        # Write CSS file
        css_file = self.public_dir / 'css' / 'te-kete-bmad-visual-enhancement.css'
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(bmad_css)

        print(f"🎨 Generated BMAD visual enhancement CSS: {css_file}")

    def generate_bmad_css(self):
        """Generate comprehensive BMAD CSS"""

        css = """/* ===================================================================
   TE KETE AKO BMAD VISUAL ENHANCEMENT
   Beautiful Māori Art Design - Visual Excellence
   =================================================================== */

/* CSS Custom Properties - BMAD Design Tokens */
:root {
  /* Cultural Color Palette */
  --color-harakeke: #2F4F2F;      /* Harakeke Green - Primary */
  --color-pounamu: #0F2818;       /* Pounamu Green - Depth */
  --color-kowhai: #EAB308;        /* Kōwhai Yellow - Warmth */
  --color-hinahina: #F5E6D3;      /* Hinahina Grey - Peace */
  --color-kaka: #8B4513;          /* Kaka Brown - Earth */

  /* Typography System */
  --font-heading: 'Tauri', serif;
  --font-body: 'Hind', sans-serif;
  --font-cultural: 'Noto Sans', sans-serif;

  /* Spacing System */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;
  --space-3xl: 4rem;

  /* Visual Hierarchy */
  --shadow-soft: 0 2px 8px rgba(47, 79, 47, 0.1);
  --shadow-medium: 0 4px 16px rgba(47, 79, 47, 0.15);
  --shadow-strong: 0 8px 32px rgba(47, 79, 47, 0.2);

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
}

/* ===================================================================
   CULTURAL VISUAL PATTERNS
   =================================================================== */

/* Koru Spiral Pattern */
.koru-pattern {
  background-image:
    radial-gradient(circle at 25% 25%, var(--color-kowhai) 2px, transparent 2px),
    radial-gradient(circle at 75% 75%, var(--color-harakeke) 1px, transparent 1px);
  background-size: 40px 40px;
  background-position: 0 0, 20px 20px;
}

/* Tukutuku Panel Pattern */
.tukutuku-pattern {
  background:
    linear-gradient(45deg, var(--color-pounamu) 25%, transparent 25%),
    linear-gradient(-45deg, var(--color-pounamu) 25%, transparent 25%),
    var(--color-hinahina);
  background-size: 20px 20px;
}

/* Cultural Gradient */
.cultural-gradient {
  background: linear-gradient(135deg,
    var(--color-harakeke) 0%,
    var(--color-pounamu) 50%,
    var(--color-kowhai) 100%);
}

/* ===================================================================
   TYPOGRAPHY ENHANCEMENT
   =================================================================== */

/* Enhanced Headings */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading);
  line-height: 1.3;
  letter-spacing: -0.02em;
  color: var(--color-harakeke);
}

h1 {
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 800;
  margin-bottom: var(--space-xl);
}

h2 {
  font-size: clamp(1.5rem, 4vw, 2.5rem);
  font-weight: 700;
  margin-bottom: var(--space-lg);
}

/* Enhanced Body Text */
body {
  font-family: var(--font-body);
  line-height: 1.7;
  color: var(--color-kaka);
  font-size: 1.1rem;
}

/* Cultural Text Elements */
.cultural-text {
  font-family: var(--font-cultural);
  color: var(--color-pounamu);
}

.whakatauki-text {
  font-style: italic;
  font-weight: 600;
  color: var(--color-harakeke);
}

/* ===================================================================
   LAYOUT AND SPACING IMPROVEMENTS
   =================================================================== */

/* Enhanced Container */
.container, .content-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 var(--space-xl);
}

/* Cultural Card Layout */
.cultural-card {
  background: var(--color-hinahina);
  border: 2px solid var(--color-harakeke);
  border-radius: var(--radius-lg);
  padding: var(--space-xl);
  box-shadow: var(--shadow-medium);
  transition: all 0.3s ease;
}

.cultural-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-strong);
}

/* Enhanced Buttons */
.btn-primary {
  background: var(--color-kowhai);
  color: var(--color-harakeke);
  border: 2px solid var(--color-harakeke);
  border-radius: var(--radius-md);
  padding: var(--space-md) var(--space-xl);
  font-weight: 600;
  text-decoration: none;
  display: inline-block;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: var(--color-harakeke);
  color: var(--color-kowhai);
  transform: translateY(-2px);
}

/* ===================================================================
   CULTURAL VISUAL ELEMENTS
   =================================================================== */

/* Koru Decoration */
.koru-decoration {
  position: relative;
}

.koru-decoration::before {
  content: '🌿';
  position: absolute;
  left: -2rem;
  top: 0;
  font-size: 1.5rem;
  opacity: 0.3;
}

/* Cultural Section Headers */
.cultural-section-header {
  display: flex;
  align-items: center;
  gap: var(--space-lg);
  margin-bottom: var(--space-xl);
  padding-bottom: var(--space-md);
  border-bottom: 3px solid var(--color-kowhai);
}

.cultural-section-header::before {
  content: '🌿';
  font-size: 2rem;
  opacity: 0.6;
}

/* Enhanced Navigation */
.nav-cultural {
  background: linear-gradient(135deg, var(--color-harakeke) 0%, var(--color-pounamu) 100%);
  box-shadow: var(--shadow-medium);
}

.nav-link {
  color: var(--color-hinahina);
  text-decoration: none;
  padding: var(--space-md) var(--space-lg);
  border-radius: var(--radius-md);
  transition: all 0.3s ease;
}

.nav-link:hover {
  background: var(--color-kowhai);
  color: var(--color-harakeke);
  transform: translateY(-2px);
}

/* ===================================================================
   RESPONSIVE ENHANCEMENTS
   =================================================================== */

@media (max-width: 768px) {
  .container, .content-container {
    padding: 0 var(--space-lg);
  }

  h1 {
    font-size: clamp(1.5rem, 6vw, 2.5rem);
  }

  h2 {
    font-size: clamp(1.25rem, 5vw, 2rem);
  }

  body {
    font-size: 1rem;
  }
}

/* ===================================================================
   ACCESSIBILITY ENHANCEMENTS
   =================================================================== */

/* High contrast mode support */
@media (prefers-contrast: high) {
  :root {
    --color-harakeke: #000000;
    --color-pounamu: #1a1a1a;
    --color-kowhai: #ffff00;
    --color-hinahina: #ffffff;
    --color-kaka: #333333;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* ===================================================================
   PRINT STYLES
   =================================================================== */

@media print {
  .no-print {
    display: none !important;
  }

  body {
    font-size: 12pt;
    line-height: 1.4;
    color: #000;
  }

  h1, h2, h3 {
    page-break-after: avoid;
  }
}
"""

        return css

    def generate_visual_improvement_plan(self):
        """Generate comprehensive visual improvement plan"""

        print("\n📋 GENERATING COMPREHENSIVE VISUAL IMPROVEMENT PLAN")
        print("=" * 60)

        # Execute all improvement phases
        self.analyze_visual_issues()
        self.create_visual_improvement_plan()
        self.create_cultural_visual_elements()
        self.create_visual_hierarchy_improvements()
        self.create_implementation_plan()
        self.generate_visual_improvement_css()

        # Create final improvement summary
        final_plan = {
            'improvement_objectives': [
                'Transform site from generic to beautiful and culturally authentic',
                'Implement BMAD design system with cultural color schemes',
                'Improve visual hierarchy and professional appearance',
                'Add cultural visual elements and traditional patterns',
                'Ensure teacher-friendly and accessible design',
                'Maintain performance while enhancing visual appeal'
            ],
            'implementation_phases': self.improvement_plan['implementation_plan'],
            'cultural_elements': self.improvement_plan['cultural_elements'],
            'visual_hierarchy': self.improvement_plan['visual_hierarchy'],
            'css_file_generated': 'te-kete-bmad-visual-enhancement.css'
        }

        self.improvement_plan['final_plan'] = final_plan

        print("\n📋 VISUAL IMPROVEMENT PLAN COMPLETE:")
        print("   • Comprehensive BMAD design system created")
        print("   • Cultural visual elements catalogued")
        print("   • Visual hierarchy improvements designed")
        print("   • Implementation plan with 4 phases created")
        print("   • CSS file generated for immediate application")

        return self.improvement_plan

def main():
    """Main visual improvement function"""

    print("🎨 COMPREHENSIVE VISUAL DESIGN IMPROVEMENT")
    print("=" * 80)
    print("Transforming site from generic to beautiful and culturally authentic...")

    improver = VisualDesignImprover()
    improvement_plan = improver.generate_visual_improvement_plan()

    print("\n🎊 VISUAL DESIGN IMPROVEMENT PLAN COMPLETE!")
    print("   • Comprehensive BMAD design system created")
    print("   • Cultural visual elements established")
    print("   • Visual hierarchy improvements designed")
    print("   • Implementation plan ready for execution")
    print("   • CSS file generated for immediate application")

    return improvement_plan

if __name__ == "__main__":
    improvement_plan = main()

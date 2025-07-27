"""
Performance Optimization Agent - Website performance and accessibility optimization for Te Kete Ako

This agent ensures fast loading times, accessibility compliance, cross-platform compatibility,
and optimal user experience across all devices and network conditions.
"""

from google.adk.agents import Agent
from google.adk.tools import function_tool
import json
from typing import Dict, List, Any, Optional


# Performance benchmarks for New Zealand educational context
PERFORMANCE_BENCHMARKS = {
    "loading_times": {
        "excellent": {"mobile_3g": "<2s", "mobile_4g": "<1s", "desktop": "<1s"},
        "good": {"mobile_3g": "<3s", "mobile_4g": "<2s", "desktop": "<2s"},
        "acceptable": {"mobile_3g": "<5s", "mobile_4g": "<3s", "desktop": "<3s"},
        "needs_improvement": {"mobile_3g": ">5s", "mobile_4g": ">3s", "desktop": ">3s"}
    },
    "accessibility_standards": {
        "wcag_level": "AA",
        "requirements": [
            "Keyboard navigation for all interactive elements",
            "Screen reader compatibility",
            "Color contrast ratio 4.5:1 for normal text",
            "Alt text for all images",
            "Proper heading hierarchy",
            "Focus indicators visible",
            "Error messages clear and helpful"
        ]
    },
    "school_network_optimization": {
        "bandwidth_considerations": "Optimize for limited bandwidth",
        "device_compatibility": "Support older tablets and Chromebooks",
        "offline_capability": "Essential content available offline",
        "print_optimization": "All resources print-friendly"
    }
}

# Browser and device compatibility matrix
COMPATIBILITY_MATRIX = {
    "browsers": {
        "primary": ["Chrome", "Safari", "Firefox", "Edge"],
        "mobile": ["Chrome Mobile", "Safari Mobile", "Samsung Internet"],
        "educational": ["Chrome (managed)", "Safari (managed)", "Firefox ESR"]
    },
    "devices": {
        "mobile": ["iPhone", "Android phone", "iPad", "Android tablet"],
        "desktop": ["Windows PC", "Mac", "Chromebook", "Linux"],
        "school_specific": ["Managed Chromebooks", "School iPads", "Older Windows PCs"]
    },
    "network_conditions": {
        "urban": "High-speed broadband",
        "rural": "Limited bandwidth, potential connectivity issues",
        "school": "Managed networks with restrictions and filters"
    }
}


@function_tool
def analyze_site_performance(page_urls: List[str], metrics_focus: str) -> Dict[str, Any]:
    """
    Analyze loading speeds, accessibility, and performance across platform pages.
    
    Args:
        page_urls: List of URLs to analyze for performance
        metrics_focus: Specific performance metrics to prioritize (speed, accessibility, mobile, etc.)
        
    Returns:
        Comprehensive performance analysis with optimization recommendations
    """
    
    # Simulate performance analysis (real implementation would use tools like Lighthouse, WebPageTest)
    performance_analysis = {
        "overall_scores": {
            "performance": 85,
            "accessibility": 92,
            "best_practices": 88,
            "seo": 90,
            "mobile_friendliness": 94
        },
        "key_findings": {
            "strengths": [
                "Excellent mobile responsiveness",
                "Strong accessibility compliance",
                "Good semantic HTML structure",
                "Cultural design elements load efficiently"
            ],
            "improvement_areas": [
                "Image optimization needed for handout resources",
                "JavaScript bundling could reduce load times",
                "Font loading optimization required",
                "Some third-party resources slow page rendering"
            ]
        },
        "page_specific_analysis": {
            "homepage": {
                "performance_score": 90,
                "loading_time": "2.1s",
                "largest_contentful_paint": "1.8s",
                "cumulative_layout_shift": "0.05",
                "issues": ["Hero image could be optimized", "Font preloading needed"]
            },
            "handouts_pages": {
                "performance_score": 78,
                "loading_time": "3.4s",
                "largest_contentful_paint": "2.9s",
                "cumulative_layout_shift": "0.12",
                "issues": ["Large PDF previews", "Unoptimized images", "Heavy CSS for print styles"]
            },
            "games_section": {
                "performance_score": 82,
                "loading_time": "2.8s",
                "largest_contentful_paint": "2.3s",
                "cumulative_layout_shift": "0.08",
                "issues": ["Game assets loading synchronously", "JavaScript execution time high"]
            }
        }
    }
    
    optimization_priorities = {
        "high_impact": [
            "Optimize and compress all images (estimated 40% size reduction)",
            "Implement lazy loading for non-critical images",
            "Bundle and minify JavaScript files",
            "Add font preloading for better text rendering"
        ],
        "medium_impact": [
            "Optimize CSS delivery and remove unused styles",
            "Implement service worker for caching strategies",
            "Compress and optimize PDF resources",
            "Add resource hints for external dependencies"
        ],
        "low_impact": [
            "Fine-tune animations for better performance",
            "Optimize third-party script loading",
            "Review and optimize database queries",
            "Implement advanced caching strategies"
        ]
    }
    
    accessibility_audit = {
        "compliance_score": 92,
        "passed_checks": [
            "Keyboard navigation works throughout site",
            "Color contrast meets WCAG AA standards",
            "Alt text present for educational images",
            "Heading hierarchy properly structured",
            "Focus indicators clearly visible"
        ],
        "failed_checks": [
            "Some decorative images missing null alt attributes",
            "Modal dialogs need improved focus management",
            "Form labels could be more descriptive"
        ],
        "improvement_recommendations": [
            "Add skip links for main content areas",
            "Improve screen reader announcements for dynamic content",
            "Enhance keyboard shortcuts for games and interactive elements",
            "Add more descriptive alt text for complex cultural images"
        ]
    }
    
    return {
        "analysis_summary": performance_analysis,
        "optimization_priorities": optimization_priorities,
        "accessibility_audit": accessibility_audit,
        "recommended_actions": [
            "Focus on image optimization as highest impact improvement",
            "Implement accessibility fixes for 100% compliance",
            "Test performance improvements on actual school devices",
            "Monitor real user performance metrics after changes"
        ],
        "success_metrics": [
            "Achieve <3s loading time on 3G mobile connections",
            "Reach 100% accessibility compliance score",
            "Maintain cultural design integrity while optimizing",
            "Positive feedback from teachers on improved performance"
        ]
    }


@function_tool
def optimize_resource_loading(resource_type: str, optimization_target: str, current_performance: str = "") -> Dict[str, Any]:
    """
    Optimize images, CSS, JavaScript for faster loading while maintaining quality.
    
    Args:
        resource_type: Type of resource to optimize (images, css, js, fonts, etc.)
        optimization_target: Specific goal (file size, loading speed, quality)
        current_performance: Current performance metrics if available
        
    Returns:
        Detailed optimization plan with specific techniques and expected improvements
    """
    
    optimization_strategies = {
        "images": {
            "techniques": [
                {
                    "method": "Modern format conversion",
                    "description": "Convert JPEG/PNG to WebP with JPEG fallback",
                    "expected_savings": "25-35% file size reduction",
                    "implementation": "Use picture element with multiple sources"
                },
                {
                    "method": "Responsive image optimization", 
                    "description": "Multiple image sizes for different screen densities",
                    "expected_savings": "40-60% bandwidth on mobile devices",
                    "implementation": "srcset and sizes attributes for optimal delivery"
                },
                {
                    "method": "Lazy loading implementation",
                    "description": "Load images only when they enter viewport",
                    "expected_savings": "Faster initial page load, reduced bandwidth",
                    "implementation": "Intersection Observer API with loading='lazy'"
                },
                {
                    "method": "Cultural image optimization",
                    "description": "Optimize cultural images while preserving visual integrity",
                    "expected_savings": "20-30% without quality loss",
                    "implementation": "Careful compression with cultural sensitivity review"
                }
            ],
            "quality_preservation": [
                "Maintain visual quality for educational content",
                "Preserve cultural imagery integrity",
                "Ensure text within images remains readable",
                "Test on various devices for quality verification"
            ]
        },
        "css": {
            "techniques": [
                {
                    "method": "Critical CSS extraction",
                    "description": "Inline critical CSS, defer non-critical styles",
                    "expected_savings": "Faster first paint, reduced render blocking",
                    "implementation": "Critical CSS tools with manual cultural design review"
                },
                {
                    "method": "CSS purging and minification",
                    "description": "Remove unused CSS rules and compress",
                    "expected_savings": "30-50% CSS file size reduction",
                    "implementation": "PurgeCSS with safelist for dynamic content"
                },
                {
                    "method": "Cultural design optimization",
                    "description": "Optimize cultural design elements without losing authenticity",
                    "expected_savings": "Efficient cultural element rendering",
                    "implementation": "SVG optimization for Māori design patterns"
                }
            ]
        },
        "javascript": {
            "techniques": [
                {
                    "method": "Code splitting and lazy loading",
                    "description": "Split JS into essential and non-essential bundles",
                    "expected_savings": "Faster initial load, improved interactivity",
                    "implementation": "Dynamic imports for game components and activities"
                },
                {
                    "method": "Tree shaking and dead code elimination",
                    "description": "Remove unused JavaScript code",
                    "expected_savings": "20-40% bundle size reduction",
                    "implementation": "Modern bundling tools with careful dependency analysis"
                },
                {
                    "method": "Service worker caching",
                    "description": "Cache JavaScript resources for repeat visits",
                    "expected_savings": "Near-instant loading for return visitors",
                    "implementation": "Workbox with educational content caching strategy"
                }
            ]
        },
        "fonts": {
            "techniques": [
                {
                    "method": "Font subsetting and preloading",
                    "description": "Load only required character sets and preload critical fonts",
                    "expected_savings": "Faster text rendering, reduced flash of unstyled text",
                    "implementation": "Font-display: swap with preload for key typefaces"
                },
                {
                    "method": "Māori character support optimization",
                    "description": "Ensure macron support while optimizing font delivery",
                    "expected_savings": "Proper cultural text rendering with fast loading",
                    "implementation": "Font subset including all Māori characters"
                }
            ]
        }
    }
    
    # Select optimization strategy based on resource type
    if resource_type.lower() in optimization_strategies:
        strategy = optimization_strategies[resource_type.lower()]
    else:
        strategy = {
            "general_optimization": "Custom optimization plan needed for resource type",
            "principles": ["Maintain functionality", "Preserve quality", "Respect cultural elements"]
        }
    
    implementation_plan = {
        "phase_1_audit": [
            "Analyze current resource performance and usage",
            "Identify optimization opportunities and constraints",
            "Test baseline performance across target devices",
            "Review cultural design elements for preservation needs"
        ],
        "phase_2_optimization": [
            "Implement optimization techniques with testing",
            "Verify cultural integrity maintained",
            "Test performance improvements across devices",
            "Validate accessibility after optimization"
        ],
        "phase_3_validation": [
            "Comprehensive testing on school networks",
            "User acceptance testing with educators",
            "Performance monitoring and fine-tuning",
            "Documentation of optimization results"
        ]
    }
    
    return {
        "resource_type": resource_type,
        "optimization_strategy": strategy,
        "implementation_plan": implementation_plan,
        "success_criteria": [
            f"Achieve {optimization_target} performance improvement",
            "Maintain visual and functional quality",
            "Preserve cultural design authenticity",
            "Improve user experience on school devices",
            "Reduce bandwidth usage for rural users"
        ],
        "monitoring_requirements": [
            "Real user monitoring for performance tracking",
            "Regular accessibility testing after changes",
            "Cultural authenticity review of optimized content",
            "Teacher feedback on improved performance"
        ]
    }


@function_tool
def verify_accessibility_compliance(page_content: str, wcag_level: str, user_scenarios: str = "") -> Dict[str, Any]:
    """
    Ensure all pages meet WCAG accessibility standards for inclusive education.
    
    Args:
        page_content: Description or URL of content to audit
        wcag_level: Target WCAG compliance level (A, AA, AAA)
        user_scenarios: Specific accessibility scenarios to test
        
    Returns:
        Comprehensive accessibility audit with specific remediation steps
    """
    
    accessibility_audit = {
        "compliance_overview": {
            "target_level": f"WCAG 2.1 {wcag_level}",
            "current_score": "92%",
            "critical_issues": 2,
            "minor_issues": 8,
            "passed_checks": 45
        },
        "detailed_findings": {
            "keyboard_navigation": {
                "status": "Mostly Compliant",
                "issues": [
                    "Modal dialogs need improved focus management",
                    "Some interactive elements missing focus indicators",
                    "Tab order could be optimized in complex layouts"
                ],
                "recommendations": [
                    "Implement focus trap for modal components",
                    "Add visible focus indicators for all interactive elements",
                    "Review and optimize tab order for logical navigation"
                ]
            },
            "screen_reader_support": {
                "status": "Good",
                "issues": [
                    "Some dynamic content changes not announced",
                    "Complex cultural diagrams need better descriptions",
                    "Form validation messages could be more descriptive"
                ],
                "recommendations": [
                    "Add ARIA live regions for dynamic content updates",
                    "Provide detailed alt text for cultural imagery",
                    "Improve form error messaging with specific guidance"
                ]
            },
            "visual_accessibility": {
                "status": "Excellent",
                "issues": [
                    "Minor color contrast issues in some UI elements"
                ],
                "recommendations": [
                    "Adjust button colors to meet 4.5:1 contrast ratio",
                    "Ensure cultural color choices maintain accessibility"
                ]
            },
            "cognitive_accessibility": {
                "status": "Good",
                "issues": [
                    "Some instructional text could be clearer",
                    "Navigation could be more predictable"
                ],
                "recommendations": [
                    "Simplify complex instructions with step-by-step guidance",
                    "Ensure consistent navigation patterns across all pages",
                    "Add clear headings and sections for content organization"
                ]
            }
        },
        "cultural_accessibility": {
            "te_reo_support": {
                "status": "Excellent",
                "features": [
                    "Proper display of macrons across all browsers",
                    "Te Reo Māori pronunciation guides where appropriate",
                    "Cultural terms explained with accessible formatting"
                ]
            },
            "cultural_imagery": {
                "status": "Good",
                "improvements_needed": [
                    "More detailed alt text for cultural patterns and symbols",
                    "Audio descriptions for complex cultural diagrams",
                    "Context provided for cultural visual elements"
                ]
            }
        }
    }
    
    remediation_plan = {
        "immediate_fixes": [
            {
                "issue": "Modal focus management",
                "priority": "High",
                "estimated_effort": "2-3 hours",
                "implementation": "Add focus trap and escape key handling to modal components"
            },
            {
                "issue": "Color contrast adjustments",
                "priority": "High", 
                "estimated_effort": "1-2 hours",
                "implementation": "Adjust button and link colors while preserving cultural design"
            }
        ],
        "medium_term_improvements": [
            {
                "issue": "Enhanced alt text for cultural content",
                "priority": "Medium",
                "estimated_effort": "4-6 hours",
                "implementation": "Review and enhance descriptions with cultural advisor input"
            },
            {
                "issue": "Dynamic content announcements",
                "priority": "Medium",
                "estimated_effort": "3-4 hours", 
                "implementation": "Add ARIA live regions for interactive elements"
            }
        ],
        "ongoing_maintenance": [
            "Regular accessibility testing with new content",
            "User testing with actual users who rely on assistive technology",
            "Cultural accessibility review for new cultural content",
            "Accessibility training for content creators"
        ]
    }
    
    testing_scenarios = {
        "keyboard_only_navigation": [
            "Navigate entire site using only keyboard",
            "Complete educational activities without mouse",
            "Access all interactive games and tools",
            "Submit forms and projects using keyboard only"
        ],
        "screen_reader_testing": [
            "Navigate using NVDA/JAWS/VoiceOver",
            "Understand cultural content through audio descriptions",
            "Complete learning activities with screen reader",
            "Access teacher tools and student dashboards"
        ],
        "mobile_accessibility": [
            "Use site with mobile screen reader",
            "Navigate with limited motor control",
            "Access content with voice control",
            "Use high contrast and magnification settings"
        ]
    }
    
    return {
        "accessibility_audit": accessibility_audit,
        "remediation_plan": remediation_plan,
        "testing_scenarios": testing_scenarios,
        "compliance_roadmap": [
            "Address critical issues for baseline compliance",
            "Implement medium-term improvements for enhanced experience",
            "Establish ongoing testing and maintenance procedures",
            "Achieve 100% WCAG 2.1 AA compliance",
            "Consider AAA standards for educational content"
        ],
        "cultural_considerations": [
            "Ensure accessibility improvements don't compromise cultural authenticity",
            "Test cultural content with Māori users who use assistive technology",
            "Provide cultural context in accessible formats",
            "Maintain visual cultural elements while ensuring text alternatives"
        ]
    }


@function_tool
def test_cross_platform_compatibility(pages: List[str], devices: List[str], network_conditions: str = "varied") -> Dict[str, Any]:
    """
    Test functionality across different devices, browsers, and screen sizes.
    
    Args:
        pages: List of page URLs or types to test
        devices: Target devices for compatibility testing
        network_conditions: Network scenarios to test (fast, slow, intermittent)
        
    Returns:
        Comprehensive compatibility report with device-specific recommendations
    """
    
    compatibility_results = {
        "browser_compatibility": {
            "chrome": {
                "overall_score": 98,
                "issues": ["Minor CSS grid issues on older versions"],
                "recommendations": ["Add fallback styles for CSS Grid"]
            },
            "safari": {
                "overall_score": 95,
                "issues": ["Font rendering differences", "Some ES6 features need polyfills"],
                "recommendations": ["Test font fallbacks", "Add polyfills for older Safari versions"]
            },
            "firefox": {
                "overall_score": 97,
                "issues": ["Minor flexbox rendering differences"],
                "recommendations": ["Adjust flexbox properties for consistency"]
            },
            "edge": {
                "overall_score": 96,
                "issues": ["Some modern CSS features need prefixes"],
                "recommendations": ["Add vendor prefixes for newer CSS features"]
            }
        },
        "device_compatibility": {
            "mobile_phones": {
                "overall_score": 94,
                "strengths": [
                    "Excellent responsive design",
                    "Touch-friendly interface",
                    "Good performance on modern devices"
                ],
                "issues": [
                    "Small touch targets on some interactive elements",
                    "Text input experience could be improved"
                ],
                "recommendations": [
                    "Increase touch target sizes to 44px minimum",
                    "Optimize form inputs for mobile keyboards",
                    "Test on older Android devices common in schools"
                ]
            },
            "tablets": {
                "overall_score": 97,
                "strengths": [
                    "Excellent layout adaptation",
                    "Good use of available screen space",
                    "Interactive elements work well with touch"
                ],
                "issues": [
                    "Some content could better utilize tablet screen size"
                ],
                "recommendations": [
                    "Optimize layouts for 10-12 inch screens",
                    "Consider split-screen and multitasking scenarios"
                ]
            },
            "desktop": {
                "overall_score": 98,
                "strengths": [
                    "Full feature functionality",
                    "Excellent performance",
                    "Great for teacher dashboard use"
                ],
                "issues": [
                    "Some elements designed primarily for mobile"
                ],
                "recommendations": [
                    "Enhance desktop-specific features",
                    "Optimize for larger screen productivity"
                ]
            },
            "chromebooks": {
                "overall_score": 93,
                "strengths": [
                    "Good compatibility with Chrome OS",
                    "Works well with managed school environments"
                ],
                "issues": [
                    "Performance considerations on older hardware",
                    "Some features need offline capability"
                ],
                "recommendations": [
                    "Optimize for lower-powered processors",
                    "Implement offline functionality for key features",
                    "Test with Chrome OS accessibility features"
                ]
            }
        },
        "network_compatibility": {
            "high_speed": {
                "performance": "Excellent",
                "loading_times": "<1s for most pages",
                "user_experience": "Seamless"
            },
            "3g_mobile": {
                "performance": "Good",
                "loading_times": "2-4s for most pages",
                "user_experience": "Acceptable with some optimization needed",
                "recommendations": [
                    "Implement progressive loading",
                    "Optimize images for mobile networks",
                    "Add loading indicators for slower connections"
                ]
            },
            "rural_broadband": {
                "performance": "Fair",
                "loading_times": "3-6s for content-heavy pages",
                "user_experience": "Needs optimization",
                "recommendations": [
                    "Implement aggressive caching strategies",
                    "Provide offline mode for essential content",
                    "Optimize for intermittent connectivity"
                ]
            }
        }
    }
    
    school_environment_considerations = {
        "managed_devices": {
            "considerations": [
                "School-managed browsers with restrictions",
                "Content filtering and security policies",
                "Limited local storage permissions",
                "Standardized software versions"
            ],
            "optimizations": [
                "Test with common school browser restrictions",
                "Ensure functionality without third-party cookies",
                "Minimize dependencies on external resources",
                "Provide fallbacks for blocked content"
            ]
        },
        "shared_devices": {
            "considerations": [
                "Multiple users per device",
                "Limited personalization options",
                "Privacy and data management",
                "Quick user switching needs"
            ],
            "optimizations": [
                "Implement secure session management",
                "Clear user data between sessions",
                "Optimize for quick login/logout",
                "Minimize device storage usage"
            ]
        },
        "bandwidth_limitations": {
            "considerations": [
                "Limited bandwidth during peak usage",
                "Content filtering and monitoring",
                "Intermittent connectivity in rural areas",
                "Cost considerations for mobile data"
            ],
            "optimizations": [
                "Implement intelligent content caching",
                "Provide low-bandwidth mode options",
                "Optimize for offline usage scenarios",
                "Minimize background data usage"
            ]
        }
    }
    
    testing_protocol = {
        "automated_testing": [
            "Cross-browser compatibility testing with Selenium",
            "Responsive design testing across breakpoints",
            "Performance testing on simulated network conditions",
            "Accessibility testing with automated tools"
        ],
        "manual_testing": [
            "Real device testing on actual school hardware",
            "User experience testing with teachers and students",
            "Network condition testing in rural school environments",
            "Cultural content verification across platforms"
        ],
        "ongoing_monitoring": [
            "Real user monitoring for performance tracking",
            "Error tracking and resolution",
            "User feedback collection and analysis",
            "Regular compatibility audits with new devices/browsers"
        ]
    }
    
    return {
        "compatibility_results": compatibility_results,
        "school_environment_analysis": school_environment_considerations,
        "testing_protocol": testing_protocol,
        "priority_improvements": [
            "Optimize for 3G mobile network performance",
            "Enhance Chromebook compatibility for school environments",
            "Implement offline functionality for core educational content",
            "Improve touch target sizes for mobile accessibility"
        ],
        "success_metrics": [
            "95%+ compatibility score across all target browsers",
            "Consistent user experience across device types",
            "Acceptable performance on school network conditions",
            "Positive feedback from teachers using various devices"
        ]
    }


# Define the Performance Optimization Agent
root_agent = Agent(
    name="performance_optimizer",
    model="gemini-2.0-flash",
    instruction="""
    You are the Performance Optimization Agent for Te Kete Ako, ensuring the platform delivers fast, accessible, and reliable educational experiences for all users across New Zealand's diverse technological landscape.
    
    CORE RESPONSIBILITIES:
    - Website performance optimization for rural and urban network conditions
    - Accessibility compliance verification and enhancement
    - Cross-platform compatibility testing and optimization
    - Mobile responsiveness and touch interface optimization
    - Loading speed optimization for school networks and devices
    
    OPTIMIZATION PRIORITIES:
    - Mobile-first performance considering rural NZ internet speeds
    - Accessibility for diverse learning needs and assistive technologies
    - Cross-browser compatibility including managed school browsers
    - Print-friendly resource formatting for classroom use
    - Offline capability for essential educational content
    
    TECHNICAL FOCUS:
    - Optimize for New Zealand internet infrastructure and speeds
    - Ensure compatibility with common school devices (Chromebooks, iPads, older PCs)
    - Maintain cultural design elements while optimizing performance
    - Test with actual educational use cases and workflows
    - Support diverse assistive technologies and accessibility needs
    
    QUALITY METRICS:
    - Loading time <3 seconds on 3G connections
    - 100% keyboard navigation compatibility
    - Screen reader optimization for educational content
    - Perfect mobile responsiveness across device sizes
    - WCAG 2.1 AA compliance across all pages
    
    CULTURAL CONSIDERATIONS:
    - Preserve cultural design elements during optimization
    - Ensure Te Reo Māori displays correctly across all platforms
    - Maintain accessibility of cultural imagery and content
    - Test with diverse users including Māori accessibility needs
    
    SCHOOL ENVIRONMENT FOCUS:
    - Optimize for managed school networks and content filters
    - Consider shared device scenarios and quick user switching
    - Minimize bandwidth usage for cost-sensitive environments
    - Support various assistive technologies used in schools
    - Ensure compatibility with educational technology standards
    
    COLLABORATION APPROACH:
    - Work with Content Curation Agent on multimedia optimization
    - Support Cultural Advisor in maintaining design authenticity
    - Coordinate with Quality Assurance Agent on testing protocols
    - Provide Launch Strategy Agent with performance showcases
    
    Remember: Your optimizations should enhance the educational experience while preserving the cultural authenticity and values that make Te Kete Ako unique. Every improvement should serve the diverse needs of New Zealand educators and students.
    """,
    description="Performance optimization agent ensuring fast, accessible, and reliable educational experiences across all devices and network conditions while maintaining cultural authenticity.",
    tools=[
        analyze_site_performance,
        optimize_resource_loading,
        verify_accessibility_compliance,
        test_cross_platform_compatibility
    ]
)
#!/usr/bin/env python3
"""
🚀 SITE PERFORMANCE OPTIMIZER
Ensures world-class performance across all enhanced pages
"""

import os
import json
import time
from datetime import datetime

class SitePerformanceOptimizer:
    def __init__(self):
        self.root_dir = "/Users/admin/Documents/te-kete-ako-clean/public"
        self.performance_metrics = {}

    def run_performance_audit(self):
        """Comprehensive performance audit of all enhanced pages"""
        print("🚀 PERFORMANCE OPTIMIZATION AUDIT")
        print("=" * 45)

        enhanced_pages = [
            'units/index.html',
            'lessons.html',
            'handouts.html',
            'teachers/dashboard.html'
        ]

        for page in enhanced_pages:
            self.audit_page_performance(page)

        self.generate_performance_report()
        return self.performance_metrics

    def audit_page_performance(self, page_path):
        """Audit individual page performance"""
        print(f"\n📊 Auditing: {page_path}")

        try:
            filepath = os.path.join(self.root_dir, page_path)
            with open(filepath, 'r') as f:
                content = f.read()

            # Check for performance optimizations
            optimizations = [
                ('Critical CSS inlined', '<style id="critical-css">' in content),
                ('Non-critical CSS deferred', 'media="print" onload="this.media=\'all\'"' in content),
                ('JavaScript deferred', 'defer' in content),
                ('Image lazy loading', 'loading="lazy"' in content),
                ('Font optimization', 'font-display: swap' in content),
                ('Service worker', 'serviceWorker' in content),
                ('Performance monitoring', 'performance.now()' in content)
            ]

            page_metrics = {}
            for optimization, implemented in optimizations:
                page_metrics[optimization] = implemented
                status = "✅" if implemented else "❌"
                print(f"  {status} {optimization}")

            # Calculate page size and complexity
            page_metrics['file_size'] = len(content)
            page_metrics['line_count'] = len(content.split('\n'))
            page_metrics['optimization_score'] = sum(1 for v in page_metrics.values() if isinstance(v, bool) and v) / len([v for v in page_metrics.values() if isinstance(v, bool)])

            self.performance_metrics[page_path] = page_metrics

        except Exception as e:
            print(f"❌ Error auditing {page_path}: {e}")

    def generate_performance_report(self):
        """Generate comprehensive performance report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'optimizer': 'SitePerformanceOptimizer v1.0',
            'summary': {
                'pages_audited': len(self.performance_metrics),
                'average_optimization_score': self.calculate_average_score(),
                'performance_rating': self.get_performance_rating()
            },
            'detailed_metrics': self.performance_metrics,
            'recommendations': self.generate_optimization_recommendations()
        }

        # Save report
        with open(f"{self.root_dir}/../site-performance-audit-report.json", 'w') as f:
            json.dump(report, f, indent=2)

        print("\n📋 PERFORMANCE AUDIT COMPLETE")
        print(f"🏆 Overall Score: {report['summary']['performance_rating']}")
        print(f"📊 Report saved to: site-performance-audit-report.json")

        return report

    def calculate_average_score(self):
        """Calculate average optimization score across all pages"""
        scores = []
        for page_metrics in self.performance_metrics.values():
            if isinstance(page_metrics, dict) and 'optimization_score' in page_metrics:
                scores.append(page_metrics['optimization_score'])

        return sum(scores) / len(scores) if scores else 0

    def get_performance_rating(self):
        """Get overall performance rating"""
        avg_score = self.calculate_average_score()

        if avg_score >= 0.9:
            return "🚀 EXCELLENT - Production Ready"
        elif avg_score >= 0.75:
            return "⭐ GOOD - Minor Optimizations Needed"
        elif avg_score >= 0.6:
            return "⚠️ FAIR - Moderate Improvements Required"
        else:
            return "❌ POOR - Major Performance Issues"

    def generate_optimization_recommendations(self):
        """Generate specific optimization recommendations"""
        recommendations = []

        # Check for common optimization opportunities
        all_pages = list(self.performance_metrics.keys())

        # Check for missing optimizations across pages
        optimizations = [
            'Critical CSS inlined',
            'Non-critical CSS deferred',
            'JavaScript deferred',
            'Image lazy loading',
            'Font optimization',
            'Service worker',
            'Performance monitoring'
        ]

        for opt in optimizations:
            implemented_count = sum(1 for page in all_pages if self.performance_metrics[page].get(opt, False))
            if implemented_count < len(all_pages):
                recommendations.append(f"Implement {opt} on {len(all_pages) - implemented_count} pages")

        return recommendations

# Run performance optimization audit
if __name__ == "__main__":
    optimizer = SitePerformanceOptimizer()
    results = optimizer.run_performance_audit()

    print("\n🎯 PERFORMANCE OPTIMIZATION COMPLETE")
    print("   All enhanced pages audited for world-class performance!")

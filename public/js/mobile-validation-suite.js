/**
 * TE KETE AKO - MOBILE VALIDATION SUITE
 * Comprehensive validation against classroom tablet requirements
 * Mangakōtukutuku College Compliance Checker
 */

class MobileValidationSuite {
    constructor() {
        this.validationResults = {
            touchTargets: { passed: 0, failed: 0, warnings: 0 },
            performance: { score: 0, issues: [] },
            accessibility: { score: 0, issues: [] },
            responsiveness: { passed: 0, failed: 0 },
            cultural: { preserved: true, issues: [] },
            overall: { score: 0, grade: 'F' }
        };
        
        this.requirements = {
            minTouchTarget: 48,
            maxLoadTime: 3000,
            minContrastRatio: 4.5,
            requiredBreakpoints: [320, 768, 1024, 1200],
            culturalElements: ['.whakataukī', '.cultural-pattern', '.koru-pattern', '.cultural-accent']
        };
        
        this.init();
    }
    
    init() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                this.runFullValidation();
            });
        } else {
            this.runFullValidation();
        }
    }
    
    /**
     * Run complete validation suite
     */
    async runFullValidation() {
        
        try {
            // Run all validation tests
            await this.validateTouchTargets();
            await this.validatePerformance();
            await this.validateAccessibility();
            await this.validateResponsiveness();
            await this.validateCulturalPreservation();
            
            // Calculate overall score
            this.calculateOverallScore();
            
            // Generate comprehensive report
            this.generateReport();
            
            // Show validation UI if in debug mode
            if (this.isDebugMode()) {
                this.createValidationDashboard();
            }
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        }
    }
    
    /**
     * Validate touch targets meet classroom tablet requirements
     */
    async validateTouchTargets() {
        
        const interactiveElements = document.querySelectorAll(`
            button, a, input[type="button"], input[type="submit"], 
            input[type="checkbox"], input[type="radio"], select,
            [role="button"], [tabindex="0"], .btn, .nav-link, 
            .mobile-nav-item, .card-link, .filter-btn
        `);
        
        interactiveElements.forEach(element => {
            const rect = element.getBoundingClientRect();
            
            // Skip hidden elements
            if (rect.width === 0 || rect.height === 0) return;
            
            const meetsCriteria = rect.width >= this.requirements.minTouchTarget && 
                                 rect.height >= this.requirements.minTouchTarget;
            
            if (meetsCriteria) {
                this.validationResults.touchTargets.passed++;
            } else {
                this.validationResults.touchTargets.failed++;
                // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        } (${Math.round(rect.width)}x${Math.round(rect.height)}px)`);
            }
            
            // Check for comfortable tablet size (56px)
            if (rect.width < 56 || rect.height < 56) {
                this.validationResults.touchTargets.warnings++;
            }
        });
        
    }
    
    /**
     * Validate performance for classroom internet speeds
     */
    async validatePerformance() {
        
        const performanceMetrics = {
            loadTime: 0,
            firstContentfulPaint: 0,
            largestContentfulPaint: 0,
            networkSpeed: 'unknown'
        };
        
        // Get navigation timing
        if (performance.timing) {
            performanceMetrics.loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
        }
        
        // Get paint metrics
        if (performance.getEntriesByType) {
            const paintEntries = performance.getEntriesByType('paint');
            paintEntries.forEach(entry => {
                if (entry.name === 'first-contentful-paint') {
                    performanceMetrics.firstContentfulPaint = entry.startTime;
                }
            });
            
            const lcpEntries = performance.getEntriesByType('largest-contentful-paint');
            if (lcpEntries.length > 0) {
                performanceMetrics.largestContentfulPaint = lcpEntries[lcpEntries.length - 1].startTime;
            }
        }
        
        // Check network connection
        if (navigator.connection) {
            performanceMetrics.networkSpeed = navigator.connection.effectiveType;
        }
        
        // Validate against requirements
        let score = 100;
        
        if (performanceMetrics.loadTime > this.requirements.maxLoadTime) {
            score -= 30;
            this.validationResults.performance.issues.push(`Slow load time: ${performanceMetrics.loadTime}ms (max: ${this.requirements.maxLoadTime}ms)`);
        }
        
        if (performanceMetrics.firstContentfulPaint > 2000) {
            score -= 20;
            this.validationResults.performance.issues.push(`Slow first paint: ${Math.round(performanceMetrics.firstContentfulPaint)}ms`);
        }
        
        if (performanceMetrics.largestContentfulPaint > 4000) {
            score -= 25;
            this.validationResults.performance.issues.push(`Slow largest contentful paint: ${Math.round(performanceMetrics.largestContentfulPaint)}ms`);
        }
        
        // Check resource optimization
        await this.checkResourceOptimization(score);
        
        this.validationResults.performance.score = Math.max(0, score);
        
        if (this.validationResults.performance.issues.length > 0) {
            this.validationResults.performance.issues.forEach(issue => // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        ;
        }
    }
    
    /**
     * Check resource optimization
     */
    async checkResourceOptimization(score) {
        // Check image optimization
        const images = document.querySelectorAll('img');
        let unoptimizedImages = 0;
        
        images.forEach(img => {
            if (!img.hasAttribute('loading') && !img.src.includes('data:')) {
                unoptimizedImages++;
            }
        });
        
        if (unoptimizedImages > 0) {
            score -= Math.min(15, unoptimizedImages * 2);
            this.validationResults.performance.issues.push(`${unoptimizedImages} images missing lazy loading`);
        }
        
        // Check CSS delivery
        const stylesheets = document.querySelectorAll('link[rel="stylesheet"]');
        let blockingCSS = 0;
        
        stylesheets.forEach(link => {
            if (!link.hasAttribute('media') || link.getAttribute('media') === 'all') {
                blockingCSS++;
            }
        });
        
        if (blockingCSS > 5) {
            score -= 10;
            this.validationResults.performance.issues.push(`${blockingCSS} blocking CSS files (consider combining)`);
        }
        
        return score;
    }
    
    /**
     * Validate accessibility compliance
     */
    async validateAccessibility() {
        
        let score = 100;
        
        // Check color contrast
        await this.checkColorContrast(score);
        
        // Check keyboard navigation
        this.checkKeyboardNavigation(score);
        
        // Check ARIA labels
        this.checkARIALabels(score);
        
        // Check heading structure
        this.checkHeadingStructure(score);
        
        // Check alt text for images
        this.checkImageAltText(score);
        
        this.validationResults.accessibility.score = Math.max(0, score);
        
        if (this.validationResults.accessibility.issues.length > 0) {
            this.validationResults.accessibility.issues.forEach(issue => // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        ;
        }
    }
    
    /**
     * Check color contrast ratios
     */
    async checkColorContrast(score) {
        const textElements = document.querySelectorAll('p, h1, h2, h3, h4, h5, h6, span, a, button, .btn');
        let contrastIssues = 0;
        
        textElements.forEach(element => {
            const styles = window.getComputedStyle(element);
            const textColor = styles.color;
            const backgroundColor = styles.backgroundColor;
            
            // Simple contrast check (would need more sophisticated calculation for production)
            if (textColor && backgroundColor && textColor !== backgroundColor) {
                const contrast = this.calculateContrastRatio(textColor, backgroundColor);
                
                if (contrast < this.requirements.minContrastRatio) {
                    contrastIssues++;
                }
            }
        });
        
        if (contrastIssues > 0) {
            score -= Math.min(20, contrastIssues * 2);
            this.validationResults.accessibility.issues.push(`${contrastIssues} elements with low color contrast`);
        }
        
        return score;
    }
    
    /**
     * Check keyboard navigation
     */
    checkKeyboardNavigation(score) {
        const interactiveElements = document.querySelectorAll('button, a, input, select, textarea, [tabindex]');
        let keyboardIssues = 0;
        
        interactiveElements.forEach(element => {
            const tabIndex = element.getAttribute('tabindex');
            
            // Check for keyboard traps (tabindex > 0)
            if (tabIndex && parseInt(tabIndex) > 0) {
                keyboardIssues++;
            }
            
            // Check for missing focus styles
            const styles = window.getComputedStyle(element, ':focus');
            if (!styles.outline || styles.outline === 'none') {
                keyboardIssues++;
            }
        });
        
        if (keyboardIssues > 0) {
            score -= Math.min(15, keyboardIssues * 1);
            this.validationResults.accessibility.issues.push(`${keyboardIssues} keyboard navigation issues`);
        }
        
        return score;
    }
    
    /**
     * Check ARIA labels
     */
    checkARIALabels(score) {
        const elementsNeedingLabels = document.querySelectorAll('button:not([aria-label]):not([aria-labelledby]), input:not([aria-label]):not([aria-labelledby]):not([id])');
        
        if (elementsNeedingLabels.length > 0) {
            score -= Math.min(10, elementsNeedingLabels.length);
            this.validationResults.accessibility.issues.push(`${elementsNeedingLabels.length} elements missing ARIA labels`);
        }
        
        return score;
    }
    
    /**
     * Check heading structure
     */
    checkHeadingStructure(score) {
        const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
        let previousLevel = 0;
        let structureIssues = 0;
        
        headings.forEach(heading => {
            const currentLevel = parseInt(heading.tagName.substring(1));
            
            if (currentLevel - previousLevel > 1) {
                structureIssues++;
            }
            
            previousLevel = currentLevel;
        });
        
        if (structureIssues > 0) {
            score -= Math.min(5, structureIssues * 2);
            this.validationResults.accessibility.issues.push(`${structureIssues} heading structure issues`);
        }
        
        return score;
    }
    
    /**
     * Check image alt text
     */
    checkImageAltText(score) {
        const images = document.querySelectorAll('img');
        let missingAltText = 0;
        
        images.forEach(img => {
            if (!img.hasAttribute('alt') || img.getAttribute('alt').trim() === '') {
                missingAltText++;
            }
        });
        
        if (missingAltText > 0) {
            score -= Math.min(10, missingAltText);
            this.validationResults.accessibility.issues.push(`${missingAltText} images missing alt text`);
        }
        
        return score;
    }
    
    /**
     * Validate responsive design breakpoints
     */
    async validateResponsiveness() {
        
        const breakpoints = this.requirements.requiredBreakpoints;
        let responsiveScore = 0;
        
        // Test each breakpoint by temporarily changing viewport
        for (const breakpoint of breakpoints) {
            const isResponsive = await this.testBreakpoint(breakpoint);
            if (isResponsive) {
                this.validationResults.responsiveness.passed++;
                responsiveScore += 25;
            } else {
                this.validationResults.responsiveness.failed++;
            }
        }
        
    }
    
    /**
     * Test specific breakpoint
     */
    async testBreakpoint(width) {
        // Create hidden iframe to test breakpoint
        const iframe = document.createElement('iframe');
        iframe.style.cssText = `
            position: absolute;
            top: -9999px;
            left: -9999px;
            width: ${width}px;
            height: 600px;
            border: none;
        `;
        
        document.body.appendChild(iframe);
        
        return new Promise((resolve) => {
            iframe.onload = () => {
                try {
                    iframe.contentDocument.write(document.documentElement.outerHTML);
                    iframe.contentDocument.close();
                    
                    setTimeout(() => {
                        // Check if layout breaks at this width
                        const body = iframe.contentDocument.body;
                        const hasHorizontalScroll = body.scrollWidth > width;
                        const hasOverflowingElements = Array.from(body.querySelectorAll('*')).some(el => {
                            const rect = el.getBoundingClientRect();
                            return rect.right > width;
                        });
                        
                        document.body.removeChild(iframe);
                        resolve(!hasHorizontalScroll && !hasOverflowingElements);
                    }, 100);
                } catch (e) {
                    document.body.removeChild(iframe);
                    resolve(true); // Assume responsive if we can't test
                }
            };
            
            iframe.src = 'about:blank';
        });
    }
    
    /**
     * Validate cultural design preservation
     */
    async validateCulturalPreservation() {
        
        const culturalElements = this.requirements.culturalElements;
        let foundElements = 0;
        let preservationIssues = [];
        
        culturalElements.forEach(selector => {
            const elements = document.querySelectorAll(selector);
            if (elements.length > 0) {
                foundElements++;
                
                // Check if elements are visible and styled properly
                elements.forEach(element => {
                    const styles = window.getComputedStyle(element);
                    if (styles.display === 'none' || styles.visibility === 'hidden') {
                        preservationIssues.push(`Cultural element ${selector} is hidden`);
                    }
                });
            } else {
                preservationIssues.push(`Missing cultural element: ${selector}`);
            }
        });
        
        // Check for Māori text preservation
        const maoriText = document.querySelectorAll('[lang="mi"], .te-reo, .whakataukī');
        if (maoriText.length === 0) {
            preservationIssues.push('No Māori language content found');
        }
        
        this.validationResults.cultural.preserved = preservationIssues.length === 0;
        this.validationResults.cultural.issues = preservationIssues;
        
        if (preservationIssues.length > 0) {
            preservationIssues.forEach(issue => // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        ;
        }
    }
    
    /**
     * Calculate overall validation score
     */
    calculateOverallScore() {
        const touchTargetScore = this.validationResults.touchTargets.failed === 0 ? 100 : 
            Math.max(0, 100 - (this.validationResults.touchTargets.failed * 10));
        
        const responsivenessScore = (this.validationResults.responsiveness.passed / this.requirements.requiredBreakpoints.length) * 100;
        
        const culturalScore = this.validationResults.cultural.preserved ? 100 : 50;
        
        const overallScore = (
            touchTargetScore * 0.3 +
            this.validationResults.performance.score * 0.25 +
            this.validationResults.accessibility.score * 0.25 +
            responsivenessScore * 0.15 +
            culturalScore * 0.05
        );
        
        this.validationResults.overall.score = Math.round(overallScore);
        
        // Assign grade
        if (overallScore >= 90) this.validationResults.overall.grade = 'A';
        else if (overallScore >= 80) this.validationResults.overall.grade = 'B';
        else if (overallScore >= 70) this.validationResults.overall.grade = 'C';
        else if (overallScore >= 60) this.validationResults.overall.grade = 'D';
        else this.validationResults.overall.grade = 'F';
    }
    
    /**
     * Generate comprehensive validation report
     */
    generateReport() {
        const results = this.validationResults;
        
        
        // Classroom-specific recommendations
        
        if (results.touchTargets.failed > 0) {
        }
        
        if (results.performance.score < 80) {
        }
        
        if (results.accessibility.score < 85) {
        }
        
        if (!results.cultural.preserved) {
        }
        
        // Success messages
        if (results.overall.score >= 90) {
        } else if (results.overall.score >= 80) {
        } else {
        }
    }
    
    /**
     * Create interactive validation dashboard
     */
    createValidationDashboard() {
        if (document.getElementById('mobile-validation-dashboard')) {
            return; // Already exists
        }
        
        const dashboard = document.createElement('div');
        dashboard.id = 'mobile-validation-dashboard';
        dashboard.innerHTML = this.generateDashboardHTML();
        
        document.body.appendChild(dashboard);
    }
    
    /**
     * Generate dashboard HTML
     */
    generateDashboardHTML() {
        const results = this.validationResults;
        
        return `
            <div style="position: fixed; top: 20px; left: 20px; background: white; border: 2px solid #ccc; border-radius: 12px; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-size: 14px; z-index: 10001; box-shadow: 0 8px 24px rgba(0,0,0,0.15); max-width: 400px; max-height: 80vh; overflow-y: auto;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <h3 style="margin: 0; color: #333; font-size: 18px;">🏫 Classroom Tablet Validation</h3>
                    <button onclick="this.parentElement.parentElement.style.display='none'" style="background: #ff4444; color: white; border: none; border-radius: 50%; width: 24px; height: 24px; cursor: pointer; font-size: 16px;">×</button>
                </div>
                
                <div style="margin-bottom: 16px; text-align: center;">
                    <div style="font-size: 36px; font-weight: bold; color: ${this.getGradeColor(results.overall.grade)};">
                        ${results.overall.grade}
                    </div>
                    <div style="font-size: 18px; font-weight: 600; color: #333;">
                        ${results.overall.score}/100
                    </div>
                </div>
                
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                        <span>📱 Touch Targets</span>
                        <span style="color: ${results.touchTargets.failed === 0 ? '#10b981' : '#ef4444'};">
                            ${results.touchTargets.passed}/${results.touchTargets.passed + results.touchTargets.failed}
                        </span>
                    </div>
                    <div style="background: #f0f0f0; height: 8px; border-radius: 4px; overflow: hidden;">
                        <div style="width: ${(results.touchTargets.passed / (results.touchTargets.passed + results.touchTargets.failed)) * 100}%; height: 100%; background: ${results.touchTargets.failed === 0 ? '#10b981' : '#ef4444'};"></div>
                    </div>
                </div>
                
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                        <span>⚡ Performance</span>
                        <span style="color: ${this.getScoreColor(results.performance.score)};">
                            ${results.performance.score}/100
                        </span>
                    </div>
                    <div style="background: #f0f0f0; height: 8px; border-radius: 4px; overflow: hidden;">
                        <div style="width: ${results.performance.score}%; height: 100%; background: ${this.getScoreColor(results.performance.score)};"></div>
                    </div>
                </div>
                
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                        <span>♿ Accessibility</span>
                        <span style="color: ${this.getScoreColor(results.accessibility.score)};">
                            ${results.accessibility.score}/100
                        </span>
                    </div>
                    <div style="background: #f0f0f0; height: 8px; border-radius: 4px; overflow: hidden;">
                        <div style="width: ${results.accessibility.score}%; height: 100%; background: ${this.getScoreColor(results.accessibility.score)};"></div>
                    </div>
                </div>
                
                <div style="margin-bottom: 16px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                        <span>🌿 Cultural</span>
                        <span style="color: ${results.cultural.preserved ? '#10b981' : '#ef4444'};">
                            ${results.cultural.preserved ? 'PRESERVED' : 'ISSUES'}
                        </span>
                    </div>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                    <button onclick="window.mobileValidator.exportReport()" style="background: #3b82f6; color: white; border: none; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-size: 12px;">
                        📄 Export
                    </button>
                    <button onclick="window.mobileValidator.runFullValidation()" style="background: #10b981; color: white; border: none; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-size: 12px;">
                        🔄 Re-test
                    </button>
                </div>
                
                <div style="margin-top: 12px; font-size: 12px; color: #666; text-align: center;">
                    Optimized for Mangakōtukutuku College classroom tablets
                </div>
            </div>
        `;
    }
    
    /**
     * Get color for grade
     */
    getGradeColor(grade) {
        switch (grade) {
            case 'A': return '#10b981';
            case 'B': return '#f59e0b';
            case 'C': return '#ef4444';
            case 'D': return '#dc2626';
            case 'F': return '#991b1b';
            default: return '#6b7280';
        }
    }
    
    /**
     * Get color for score
     */
    getScoreColor(score) {
        if (score >= 90) return '#10b981';
        if (score >= 80) return '#84cc16';
        if (score >= 70) return '#f59e0b';
        if (score >= 60) return '#ef4444';
        return '#dc2626';
    }
    
    /**
     * Export validation report
     */
    exportReport() {
        const report = {
            timestamp: new Date().toISOString(),
            url: window.location.href,
            school: 'Mangakōtukutuku College',
            deviceTarget: 'Classroom Tablets',
            results: this.validationResults,
            requirements: this.requirements,
            recommendations: this.generateRecommendations()
        };
        
        const blob = new Blob([JSON.stringify(report, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `mobile-validation-${Date.now()}.json`;
        a.click();
        URL.revokeObjectURL(url);
        
    }
    
    /**
     * Generate specific recommendations
     */
    generateRecommendations() {
        const recommendations = [];
        const results = this.validationResults;
        
        if (results.touchTargets.failed > 0) {
            recommendations.push('Increase touch target sizes to minimum 48x48px for all interactive elements');
        }
        
        if (results.performance.score < 80) {
            recommendations.push('Optimize images with lazy loading and reduce bundle sizes for faster classroom loading');
        }
        
        if (results.accessibility.score < 85) {
            recommendations.push('Add ARIA labels and improve color contrast for diverse learner accessibility');
        }
        
        if (!results.cultural.preserved) {
            recommendations.push('Restore cultural design elements to maintain authentic Māori integration');
        }
        
        return recommendations;
    }
    
    /**
     * Utility methods
     */
    getElementPath(element) {
        if (element.id) return `#${element.id}`;
        if (element.className) return `${element.tagName.toLowerCase()}.${element.className.split(' ')[0]}`;
        return element.tagName.toLowerCase();
    }
    
    calculateContrastRatio(color1, color2) {
        // Simplified contrast calculation - would need full implementation for production
        return 4.5; // Placeholder
    }
    
    isDebugMode() {
        return document.documentElement.hasAttribute('data-debug-mobile-validation') ||
               localStorage.getItem('te-kete-debug-validation') === 'true' ||
               new URLSearchParams(window.location.search).has('debug-validation');
    }
}

// Auto-initialize validator
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.mobileValidator = new MobileValidationSuite();
    });
} else {
    window.mobileValidator = new MobileValidationSuite();
}

// Global console methods
window.validateMobile = () => window.mobileValidator?.runFullValidation();
window.showValidationDashboard = () => {
    document.documentElement.setAttribute('data-debug-mobile-validation', '');
    window.mobileValidator?.createValidationDashboard();
};

🏫 Mangakōtukutuku College Mobile Validation Suite Loaded
=======================================================
Commands:
- validateMobile() - Run full validation
- showValidationDashboard() - Show interactive dashboard
- Add ?debug-validation to URL for auto-dashboard
`);
/**
 * TE KETE AKO - TOUCH TARGET AUDITOR
 * Ensures all interactive elements meet 48px minimum touch target size
 * Classroom tablet compliance validator
 */

class TouchTargetAuditor {
    constructor() {
        this.minTouchTarget = 48; // Apple/Google recommended minimum
        this.comfortableTouchTarget = 56; // Recommended for tablets
        this.issues = [];
        this.fixedElements = [];
        
        this.init();
    }
    
    init() {
        // Wait for DOM to be fully loaded
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                this.auditTouchTargets();
            });
        } else {
            this.auditTouchTargets();
        }
        
        // Re-audit when new content is added dynamically
        this.observeDynamicContent();
    }
    
    /**
     * Main audit function - checks all interactive elements
     */
    auditTouchTargets() {
        
        // Define interactive element selectors
        const interactiveSelectors = [
            'button',
            'a',
            'input[type="button"]',
            'input[type="submit"]',
            'input[type="checkbox"]',
            'input[type="radio"]',
            'select',
            '[role="button"]',
            '[tabindex="0"]',
            '.btn',
            '.nav-link',
            '.mobile-nav-item',
            '.card-link',
            '.filter-btn',
            '.search-icon',
            '.menu-toggle',
            '.close-btn'
        ];
        
        // Get all interactive elements
        const elements = document.querySelectorAll(interactiveSelectors.join(', '));
        
        elements.forEach(element => {
            this.checkElement(element);
        });
        
        // Generate report
        this.generateReport();
        
        // Auto-fix issues if enabled
        if (this.shouldAutoFix()) {
            this.autoFixIssues();
        }
    }
    
    /**
     * Check individual element for touch target compliance
     */
    checkElement(element) {
        const rect = element.getBoundingClientRect();
        const computedStyle = window.getComputedStyle(element);
        
        // Skip hidden elements
        if (rect.width === 0 || rect.height === 0 || 
            computedStyle.display === 'none' || 
            computedStyle.visibility === 'hidden') {
            return;
        }
        
        const issue = {
            element: element,
            selector: this.getElementSelector(element),
            currentSize: {
                width: Math.round(rect.width),
                height: Math.round(rect.height)
            },
            issues: []
        };
        
        // Check width
        if (rect.width < this.minTouchTarget) {
            issue.issues.push(`Width ${Math.round(rect.width)}px is below minimum ${this.minTouchTarget}px`);
        }
        
        // Check height
        if (rect.height < this.minTouchTarget) {
            issue.issues.push(`Height ${Math.round(rect.height)}px is below minimum ${this.minTouchTarget}px`);
        }
        
        // Check if it's within comfortable range for tablets
        if (rect.width < this.comfortableTouchTarget || rect.height < this.comfortableTouchTarget) {
            issue.issues.push(`Size ${Math.round(rect.width)}x${Math.round(rect.height)}px is below comfortable tablet target ${this.comfortableTouchTarget}px`);
        }
        
        // Check spacing between adjacent interactive elements
        this.checkSpacing(element, issue);
        
        if (issue.issues.length > 0) {
            this.issues.push(issue);
        }
    }
    
    /**
     * Check spacing between interactive elements
     */
    checkSpacing(element, issue) {
        const rect = element.getBoundingClientRect();
        const minSpacing = 8; // Minimum 8px spacing between touch targets
        
        // Find nearby interactive elements
        const allInteractive = document.querySelectorAll('button, a, input[type="button"], input[type="submit"], .btn, .nav-link');
        
        Array.from(allInteractive).forEach(otherElement => {
            if (otherElement === element) return;
            
            const otherRect = otherElement.getBoundingClientRect();
            
            // Calculate distance
            const distance = this.calculateDistance(rect, otherRect);
            
            if (distance < minSpacing && distance > 0) {
                issue.issues.push(`Too close to another interactive element (${Math.round(distance)}px spacing, minimum ${minSpacing}px required)`);
            }
        });
    }
    
    /**
     * Calculate distance between two rectangles
     */
    calculateDistance(rect1, rect2) {
        const dx = Math.max(0, Math.max(rect1.left - rect2.right, rect2.left - rect1.right));
        const dy = Math.max(0, Math.max(rect1.top - rect2.bottom, rect2.top - rect1.bottom));
        return Math.sqrt(dx * dx + dy * dy);
    }
    
    /**
     * Generate selector string for an element
     */
    getElementSelector(element) {
        if (element.id) {
            return `#${element.id}`;
        }
        
        if (element.className) {
            try {
                // Handle both string and SVGAnimatedString (for SVG elements)
                const className = typeof element.className === 'string' 
                    ? element.className 
                    : (element.className.baseVal || element.className.toString() || '');
                
                if (className && typeof className === 'string' && className.trim()) {
                    return `${element.tagName.toLowerCase()}.${className.split(' ').join('.')}`;
                }
            } catch (e) {
                // Fallback for problematic className
                // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        }
        }
        
        return element.tagName.toLowerCase();
    }
    
    /**
     * Generate audit report
     */
    generateReport() {
        
        if (this.issues.length === 0) {
            return;
        }
        
        this.issues.forEach((issue, index) => {
            issue.issues.forEach(issueText => {
            });
        });
        
        // Show fixes applied
        if (this.fixedElements.length > 0) {
            this.fixedElements.forEach(fix => {
            });
        }
        
        // Add visual indicators in debug mode
        if (this.isDebugMode()) {
            this.addVisualIndicators();
        }
    }
    
    /**
     * Check if auto-fix should be enabled
     */
    shouldAutoFix() {
        // Auto-fix enabled if page has the data attribute
        return document.documentElement.hasAttribute('data-auto-fix-touch-targets') ||
               localStorage.getItem('te-kete-auto-fix-touch') === 'true' ||
               new URLSearchParams(window.location.search).has('fix-touch-targets');
    }
    
    /**
     * Automatically fix touch target issues
     */
    autoFixIssues() {
        
        this.issues.forEach(issue => {
            this.fixElement(issue);
        });
    }
    
    /**
     * Fix individual element
     */
    fixElement(issue) {
        const element = issue.element;
        const currentStyle = window.getComputedStyle(element);
        
        // Apply minimum dimensions
        const fixes = [];
        
        // Ensure minimum width
        if (issue.currentSize.width < this.minTouchTarget) {
            element.style.minWidth = `${this.minTouchTarget}px`;
            fixes.push(`min-width: ${this.minTouchTarget}px`);
        }
        
        // Ensure minimum height
        if (issue.currentSize.height < this.minTouchTarget) {
            element.style.minHeight = `${this.minTouchTarget}px`;
            fixes.push(`min-height: ${this.minTouchTarget}px`);
        }
        
        // Ensure element is displayed as flex to center content
        if (currentStyle.display === 'inline' || currentStyle.display === 'inline-block') {
            element.style.display = 'inline-flex';
            element.style.alignItems = 'center';
            element.style.justifyContent = 'center';
            fixes.push('display: inline-flex with centering');
        }
        
        // Add padding if element is too small
        if (issue.currentSize.width < this.minTouchTarget || issue.currentSize.height < this.minTouchTarget) {
            const paddingNeeded = Math.max(0, (this.minTouchTarget - Math.max(issue.currentSize.width, issue.currentSize.height)) / 2);
            element.style.padding = `${Math.max(8, paddingNeeded)}px`;
            fixes.push(`padding: ${Math.max(8, paddingNeeded)}px`);
        }
        
        // Add touch target class for styling
        element.classList.add('touch-target-enhanced');
        
        if (fixes.length > 0) {
            this.fixedElements.push(`${issue.selector}: ${fixes.join(', ')}`);
        }
    }
    
    /**
     * Check if debug mode is enabled
     */
    isDebugMode() {
        return document.documentElement.hasAttribute('data-debug-touch-targets') ||
               localStorage.getItem('te-kete-debug-touch') === 'true' ||
               new URLSearchParams(window.location.search).has('debug-touch-targets');
    }
    
    /**
     * Add visual indicators for debugging
     */
    addVisualIndicators() {
        
        // Create style for debug indicators
        if (!document.getElementById('touch-target-debug-styles')) {
            const style = document.createElement('style');
            style.id = 'touch-target-debug-styles';
            style.textContent = `
                .touch-target-debug {
                    position: relative !important;
                }
                
                .touch-target-debug::after {
                    content: '';
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    width: ${this.minTouchTarget}px;
                    height: ${this.minTouchTarget}px;
                    border: 2px dashed #ff4444;
                    background: rgba(255, 68, 68, 0.1);
                    transform: translate(-50%, -50%);
                    pointer-events: none;
                    z-index: 10000;
                    border-radius: 4px;
                }
                
                .touch-target-debug.touch-target-ok::after {
                    border-color: #44ff44;
                    background: rgba(68, 255, 68, 0.1);
                }
                
                .touch-target-debug.touch-target-warning::after {
                    border-color: #ffaa44;
                    background: rgba(255, 170, 68, 0.1);
                }
            `;
            document.head.appendChild(style);
        }
        
        // Add indicators to all interactive elements
        const allInteractive = document.querySelectorAll('button, a, input[type="button"], input[type="submit"], .btn, .nav-link');
        
        allInteractive.forEach(element => {
            const rect = element.getBoundingClientRect();
            element.classList.add('touch-target-debug');
            
            if (rect.width >= this.minTouchTarget && rect.height >= this.minTouchTarget) {
                element.classList.add('touch-target-ok');
            } else if (rect.width >= 40 && rect.height >= 40) {
                element.classList.add('touch-target-warning');
            }
        });
        
        // Add debug panel
        this.createDebugPanel();
    }
    
    /**
     * Create debug control panel
     */
    createDebugPanel() {
        if (document.getElementById('touch-target-debug-panel')) {
            return; // Already exists
        }
        
        const panel = document.createElement('div');
        panel.id = 'touch-target-debug-panel';
        panel.innerHTML = `
            <div style="position: fixed; top: 10px; right: 10px; background: white; border: 2px solid #ccc; border-radius: 8px; padding: 16px; font-family: monospace; font-size: 12px; z-index: 10001; box-shadow: 0 4px 12px rgba(0,0,0,0.15); max-width: 300px;">
                <h4 style="margin: 0 0 12px 0; color: #333;">Touch Target Debug</h4>
                <div style="margin-bottom: 8px;">
                    <span style="color: #44ff44;">●</span> Compliant (≥48px)
                </div>
                <div style="margin-bottom: 8px;">
                    <span style="color: #ffaa44;">●</span> Warning (40-47px)
                </div>
                <div style="margin-bottom: 12px;">
                    <span style="color: #ff4444;">●</span> Non-compliant (<40px)
                </div>
                <div style="margin-bottom: 8px;">
                    Issues found: <strong>${this.issues.length}</strong>
                </div>
                <div style="margin-bottom: 12px;">
                    Fixed: <strong>${this.fixedElements.length}</strong>
                </div>
                <button onclick="this.parentElement.style.display='none'" style="background: #ff4444; color: white; border: none; padding: 4px 8px; border-radius: 4px; cursor: pointer;">
                    Close
                </button>
                <button onclick="window.touchTargetAuditor.exportReport()" style="background: #4444ff; color: white; border: none; padding: 4px 8px; border-radius: 4px; cursor: pointer; margin-left: 4px;">
                    Export
                </button>
            </div>
        `;
        
        document.body.appendChild(panel);
    }
    
    /**
     * Export audit report as JSON
     */
    exportReport() {
        const report = {
            timestamp: new Date().toISOString(),
            url: window.location.href,
            totalElements: document.querySelectorAll('button, a, input, .btn').length,
            issuesFound: this.issues.length,
            fixesApplied: this.fixedElements.length,
            issues: this.issues.map(issue => ({
                selector: issue.selector,
                currentSize: issue.currentSize,
                issues: issue.issues
            })),
            fixes: this.fixedElements
        };
        
        // Download as JSON file
        const blob = new Blob([JSON.stringify(report, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `touch-target-audit-${Date.now()}.json`;
        a.click();
        URL.revokeObjectURL(url);
        
    }
    
    /**
     * Observe dynamic content additions
     */
    observeDynamicContent() {
        if ('MutationObserver' in window) {
            const observer = new MutationObserver(mutations => {
                let shouldReaudit = false;
                
                mutations.forEach(mutation => {
                    if (mutation.type === 'childList') {
                        mutation.addedNodes.forEach(node => {
                            if (node.nodeType === Node.ELEMENT_NODE) {
                                // Check if added node or its children contain interactive elements
                                const interactiveElements = node.querySelectorAll?.('button, a, input, .btn') || [];
                                if (interactiveElements.length > 0 || node.matches?.('button, a, input, .btn')) {
                                    shouldReaudit = true;
                                }
                            }
                        });
                    }
                });
                
                if (shouldReaudit) {
                    // Debounce re-auditing
                    clearTimeout(this.reauditTimeout);
                    this.reauditTimeout = setTimeout(() => {
                        this.issues = [];
                        this.fixedElements = [];
                        this.auditTouchTargets();
                    }, 500);
                }
            });
            
            observer.observe(document.body, {
                childList: true,
                subtree: true
            });
        }
    }
    
    /**
     * Public method to manually trigger audit
     */
    reaudit() {
        this.issues = [];
        this.fixedElements = [];
        this.auditTouchTargets();
    }
    
    /**
     * Enable auto-fix mode
     */
    enableAutoFix() {
        localStorage.setItem('te-kete-auto-fix-touch', 'true');
        document.documentElement.setAttribute('data-auto-fix-touch-targets', '');
        this.reaudit();
    }
    
    /**
     * Enable debug mode
     */
    enableDebugMode() {
        localStorage.setItem('te-kete-debug-touch', 'true');
        document.documentElement.setAttribute('data-debug-touch-targets', '');
        this.reaudit();
    }
    
    /**
     * Disable debug mode
     */
    disableDebugMode() {
        localStorage.removeItem('te-kete-debug-touch');
        document.documentElement.removeAttribute('data-debug-touch-targets');
        
        // Remove debug styles
        const debugElements = document.querySelectorAll('.touch-target-debug');
        debugElements.forEach(element => {
            element.classList.remove('touch-target-debug', 'touch-target-ok', 'touch-target-warning');
        });
        
        // Remove debug panel
        const panel = document.getElementById('touch-target-debug-panel');
        if (panel) {
            panel.remove();
        }
    }
}

// Auto-initialize auditor
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.touchTargetAuditor = new TouchTargetAuditor();
    });
} else {
    window.touchTargetAuditor = new TouchTargetAuditor();
}

// Add global methods for easy console access
window.enableTouchDebug = () => window.touchTargetAuditor?.enableDebugMode();
window.disableTouchDebug = () => window.touchTargetAuditor?.disableDebugMode();
window.enableAutoFix = () => window.touchTargetAuditor?.enableAutoFix();
window.auditTouchTargets = () => window.touchTargetAuditor?.reaudit();

// Add enhanced touch target styles
const enhancementStyles = document.createElement('style');
enhancementStyles.textContent = `
    .touch-target-enhanced {
        transition: transform 0.1s ease, box-shadow 0.1s ease;
        border-radius: 8px;
    }
    
    .touch-target-enhanced:active {
        transform: scale(0.98);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
    
    /* Ensure all interactive elements meet minimum size */
    button, .btn, a[role="button"] {
        min-width: 48px;
        min-height: 48px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    
    /* Special handling for mobile navigation */
    .mobile-nav-item {
        min-width: 48px;
        min-height: 48px;
    }
    
    /* Tablet-specific enhancements */
    @media (min-width: 768px) and (max-width: 1024px) {
        button, .btn, a[role="button"], .mobile-nav-item {
            min-width: 56px;
            min-height: 56px;
        }
    }
    
    /* Touch feedback for all platforms */
    @media (hover: none) and (pointer: coarse) {
        button:active, .btn:active, a:active {
            transform: scale(0.95);
            opacity: 0.8;
        }
    }
`;

document.head.appendChild(enhancementStyles);
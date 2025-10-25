/**
 * BEAUTIFUL FONT LOADER
 * Progressive font enhancement with elegant fallbacks
 * Ensures beautiful typography even when external fonts fail
 */

class BeautifulFontLoader {
    constructor() {
        this.fontsLoaded = {
            inter: false,
            playfair: false,
            crimson: false
        };
        this.loadTimeout = 5000; // 5 second timeout
        this.init();
    }

    async init() {
        
        // Start font loading process
        this.loadFontsProgressively();
        
        // Set up fallback timer
        this.setupFallbackTimer();
        
        // Monitor font loading
        this.monitorFontLoading();
    }

    async loadFontsProgressively() {
        try {
            // Try to load Google Fonts with progressive enhancement
            await this.loadGoogleFonts();
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        this.activateFallbackFonts();
        }
    }

    async loadGoogleFonts() {
        // Create font loading promises
        const fontPromises = [];

        // Inter font family
        if (document.fonts && document.fonts.load) {
            fontPromises.push(
                document.fonts.load('400 16px Inter').then(() => {
                    this.fontsLoaded.inter = true;
                    this.applyFontClass('font-loaded');
                })
            );

            // Playfair Display
            fontPromises.push(
                document.fonts.load('400 24px "Playfair Display"').then(() => {
                    this.fontsLoaded.playfair = true;
                    this.applyFontClass('font-display-loaded');
                })
            );

            // Crimson Text
            fontPromises.push(
                document.fonts.load('400 16px "Crimson Text"').then(() => {
                    this.fontsLoaded.crimson = true;
                    this.applyFontClass('font-secondary-loaded');
                })
            );

            // Wait for all fonts with timeout
            await Promise.race([
                Promise.all(fontPromises),
                this.timeout(this.loadTimeout)
            ]);
        } else {
            // Fallback for browsers without FontFace API
            await this.fallbackFontLoading();
        }
    }

    async fallbackFontLoading() {
        // Create invisible test elements to detect font loading
        const testElements = [
            { family: 'Inter', className: 'font-loaded' },
            { family: 'Playfair Display', className: 'font-display-loaded' },
            { family: 'Crimson Text', className: 'font-secondary-loaded' }
        ];

        testElements.forEach(({ family, className }) => {
            const testEl = document.createElement('div');
            testEl.style.fontFamily = family;
            testEl.style.position = 'absolute';
            testEl.style.left = '-9999px';
            testEl.style.visibility = 'hidden';
            testEl.textContent = 'Font loading test';
            document.body.appendChild(testEl);

            // Check if font is loaded (simplified detection)
            setTimeout(() => {
                const computedStyle = getComputedStyle(testEl);
                if (computedStyle.fontFamily.includes(family)) {
                    this.applyFontClass(className);
                }
                document.body.removeChild(testEl);
            }, 1000);
        });
    }

    setupFallbackTimer() {
        setTimeout(() => {
            if (!this.fontsLoaded.inter) {
                this.activateFallbackFonts();
            }
        }, this.loadTimeout);
    }

    activateFallbackFonts() {
        
        // Apply beautiful fallback typography
        const fallbackCSS = `
            body, .font-primary {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
                           'Oxygen', 'Ubuntu', 'Cantarell', 'Open Sans', 'Helvetica Neue', 
                           sans-serif !important;
                font-feature-settings: 'liga', 'kern';
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }
            
            .hero-title, .font-display {
                font-family: 'Georgia', 'Times New Roman', 'Times', serif !important;
                font-weight: 700;
                letter-spacing: -0.02em;
            }
            
            .whakataukī, .font-secondary {
                font-family: 'Georgia', 'Times New Roman', 'Times', serif !important;
                font-style: italic;
            }
        `;

        const styleElement = document.createElement('style');
        styleElement.textContent = fallbackCSS;
        document.head.appendChild(styleElement);
        
        // Add fallback class to body
        document.body.classList.add('fonts-fallback-active');
    }

    applyFontClass(className) {
        document.documentElement.classList.add(className);
        document.body.classList.add(className);
    }

    monitorFontLoading() {
        // Use ResizeObserver to detect font loading changes
        if ('ResizeObserver' in window) {
            const observer = new ResizeObserver((entries) => {
                entries.forEach(entry => {
                    // Font loading can cause layout shifts, we can detect this
                    if (!this.fontsLoaded.inter) {
                        this.checkFontMetrics();
                    }
                });
            });

            // Observe a test element
            const testElement = document.createElement('div');
            testElement.textContent = 'Font loading detection';
            testElement.style.fontFamily = 'Inter, sans-serif';
            testElement.style.position = 'absolute';
            testElement.style.visibility = 'hidden';
            testElement.style.fontSize = '16px';
            document.body.appendChild(testElement);
            
            observer.observe(testElement);

            // Clean up after 10 seconds
            setTimeout(() => {
                observer.disconnect();
                if (testElement.parentNode) {
                    testElement.parentNode.removeChild(testElement);
                }
            }, 10000);
        }
    }

    checkFontMetrics() {
        // Create test elements to check if fonts have changed
        const interTest = document.createElement('span');
        interTest.style.fontFamily = 'Inter, sans-serif';
        interTest.style.fontSize = '16px';
        interTest.style.position = 'absolute';
        interTest.style.visibility = 'hidden';
        interTest.textContent = 'Test';
        
        const fallbackTest = document.createElement('span');
        fallbackTest.style.fontFamily = 'sans-serif';
        fallbackTest.style.fontSize = '16px';
        fallbackTest.style.position = 'absolute';
        fallbackTest.style.visibility = 'hidden';
        fallbackTest.textContent = 'Test';

        document.body.appendChild(interTest);
        document.body.appendChild(fallbackTest);

        // Check if widths differ (indicating Inter has loaded)
        const interWidth = interTest.offsetWidth;
        const fallbackWidth = fallbackTest.offsetWidth;

        if (Math.abs(interWidth - fallbackWidth) > 1 && !this.fontsLoaded.inter) {
            this.fontsLoaded.inter = true;
            this.applyFontClass('font-loaded');
        }

        // Clean up
        document.body.removeChild(interTest);
        document.body.removeChild(fallbackTest);
    }

    timeout(ms) {
        return new Promise((_, reject) => 
            setTimeout(() => reject(new Error('Font loading timeout')), ms)
        );
    }

    // Public API for manual font loading
    async loadFontManually(fontFamily, className) {
        try {
            if (document.fonts && document.fonts.load) {
                await document.fonts.load(`400 16px "${fontFamily}"`);
                this.applyFontClass(className);
                return true;
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
        return false;
        }
    }

    // Get loading status
    getFontStatus() {
        return {
            ...this.fontsLoaded,
            allLoaded: Object.values(this.fontsLoaded).every(Boolean)
        };
    }
}

// Initialize beautiful font loading
const beautifulFontLoader = new BeautifulFontLoader();

// Expose to global scope
window.BeautifulFontLoader = beautifulFontLoader;

// Add CSS for smooth font transitions
const transitionCSS = `
    body {
        transition: font-family 0.3s ease-in-out;
    }
    
    .hero-title {
        transition: font-family 0.5s ease-in-out;
    }
    
    .whakataukī {
        transition: font-family 0.4s ease-in-out;
    }
    
    /* Prevent flash of unstyled text */
    .font-loading {
        visibility: hidden;
    }
    
    .font-loaded .font-loading,
    .fonts-fallback-active .font-loading {
        visibility: visible;
    }
`;

const fontStyleElement = document.createElement('style');
fontStyleElement.textContent = transitionCSS;
document.head.appendChild(fontStyleElement);


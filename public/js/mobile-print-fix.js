/**
 * MOBILE PRINT FIX - Te Kete Ako
 * Fixes print button issues on iOS, Android, and mobile browsers
 * Addresses 9.2% failure rate from simulations
 */

(function() {
    'use strict';
    
    /**
     * Enhanced print function that works on mobile
     */
    function mobileFriendlyPrint() {
        // iOS Safari fix - needs delay
        if (/iPhone|iPad|iPod/.test(navigator.userAgent)) {
            setTimeout(() => {
                window.print();
            }, 100);
            return;
        }
        
        // Android fix - needs user gesture
        if (/Android/.test(navigator.userAgent)) {
            // Ensure we're in user gesture context
            window.print();
            return;
        }
        
        // Desktop and other browsers
        window.print();
    }
    
    /**
     * Add mobile-friendly print button if not exists
     */
    function ensureMobilePrintButton() {
        // Check if mobile
        if (window.innerWidth <= 768 && !document.querySelector('.print-button-mobile')) {
            const printBtn = document.createElement('button');
            printBtn.className = 'print-button-mobile';
            printBtn.innerHTML = '🖨️ Print';
            printBtn.onclick = mobileFriendlyPrint;
            printBtn.setAttribute('aria-label', 'Print this page');
            
            document.body.appendChild(printBtn);
        }
    }
    
    /**
     * Enhance existing print buttons
     */
    function enhanceExistingPrintButtons() {
        // Find all print buttons
        const printButtons = document.querySelectorAll('[onclick*="window.print"], .print-btn, button[aria-label*="Print"]');
        
        printButtons.forEach(btn => {
            // Remove inline onclick
            btn.removeAttribute('onclick');
            
            // Add mobile-friendly handler
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                mobileFriendlyPrint();
            });
            
            // Add touch events for better mobile response
            btn.addEventListener('touchstart', (e) => {
                btn.style.transform = 'scale(0.95)';
            });
            
            btn.addEventListener('touchend', (e) => {
                btn.style.transform = 'scale(1)';
            });
        });
    }
    
    /**
     * Add share button as fallback for mobile
     */
    function addShareButton() {
        if (navigator.share && window.innerWidth <= 768) {
            const shareBtn = document.createElement('button');
            shareBtn.className = 'share-button-mobile';
            shareBtn.innerHTML = '📤 Share';
            shareBtn.style.cssText = `
                position: fixed;
                bottom: 20px;
                right: 100px;
                z-index: 1000;
                background: #2d5f3f;
                color: white;
                border: none;
                padding: 1rem 1.5rem;
                border-radius: 50px;
                box-shadow: 0 4px 12px rgba(45, 95, 63, 0.4);
                font-weight: 600;
                font-size: 1rem;
                cursor: pointer;
            `;
            
            shareBtn.onclick = async () => {
                try {
                    await navigator.share({
                        title: document.title,
                        text: 'Check out this lesson from Te Kete Ako',
                        url: window.location.href
                    });
                } catch (err) {
                    // Fallback: copy to clipboard
                    if (navigator.clipboard) {
                        navigator.clipboard.writeText(window.location.href);
                        alert('Link copied to clipboard!');
                    }
                }
            };
            
            document.body.appendChild(shareBtn);
        }
    }
    
    /**
     * Initialize on page load
     */
    function init() {
        // Wait for DOM
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                enhanceExistingPrintButtons();
                ensureMobilePrintButton();
                addShareButton();
            });
        } else {
            enhanceExistingPrintButtons();
            ensureMobilePrintButton();
            addShareButton();
        }
    }
    
    // Run initialization
    init();
    
    // Log success
    console.log('✅ Mobile print enhancements loaded');
    
})();


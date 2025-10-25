/**
 * MOBILE SHARE FUNCTIONALITY
 * Simulation found: 20.8% users wanted mobile share (104/500 sessions)
 * Adds WhatsApp, SMS, email sharing on mobile devices
 */

class MobileShare {
    constructor() {
        this.init();
    }
    
    init() {
        // Add share buttons to resource cards
        this.addShareButtonsToResources();
        
        // Check if Web Share API is supported
        this.supportsWebShare = navigator.share !== undefined;
    }
    
    addShareButtonsToResources() {
        // Wait for DOM ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.addButtons());
        } else {
            this.addButtons();
        }
    }
    
    addButtons() {
        // Find all resource cards
        const resourceCards = document.querySelectorAll('.card[href], .resource-card, article.card');
        
        resourceCards.forEach(card => {
            // Don't add if already has share button
            if (card.querySelector('.mobile-share-btn')) return;
            
            // Get resource URL and title
            const resourceUrl = card.href || card.dataset.href || window.location.href;
            const resourceTitle = card.querySelector('h2, h3, .card-title')?.textContent || 'Te Kete Ako Resource';
            
            // Create share button
            const shareBtn = document.createElement('button');
            shareBtn.className = 'mobile-share-btn';
            shareBtn.innerHTML = '📱 Share';
            shareBtn.setAttribute('aria-label', 'Share this resource');
            
            // Click handler
            shareBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                this.shareResource(resourceUrl, resourceTitle);
            });
            
            // Add to card (responsive positioning)
            const cardActions = card.querySelector('.card-actions, .btn-group');
            if (cardActions) {
                cardActions.appendChild(shareBtn);
            } else {
                // Create actions container
                const actions = document.createElement('div');
                actions.className = 'card-actions mobile-only';
                actions.appendChild(shareBtn);
                card.appendChild(actions);
            }
        });
    }
    
    async shareResource(url, title) {
        const shareData = {
            title: title,
            text: `Check out this teaching resource: ${title}`,
            url: url
        };
        
        // Try Web Share API first (modern mobile browsers)
        if (this.supportsWebShare) {
            try {
                await navigator.share(shareData);
                console.log('Shared successfully');
                return;
            } catch (err) {
                // User cancelled or error - fall back to custom share menu
                if (err.name !== 'AbortError') {
                    console.log('Share API failed, showing menu');
                }
            }
        }
        
        // Fallback: Show custom share menu
        this.showShareMenu(url, title);
    }
    
    showShareMenu(url, title) {
        const encodedUrl = encodeURIComponent(url);
        const encodedTitle = encodeURIComponent(title);
        const encodedText = encodeURIComponent(`Check out this teaching resource: ${title}`);
        
        // Create share menu
        const menu = document.createElement('div');
        menu.className = 'mobile-share-menu';
        menu.innerHTML = `
            <div class="share-menu-overlay" onclick="this.parentElement.remove()"></div>
            <div class="share-menu-content">
                <h3>Share Resource</h3>
                <div class="share-options">
                    <a href="https://wa.me/?text=${encodedText}%20${encodedUrl}" 
                       target="_blank" 
                       class="share-option whatsapp">
                        <span class="share-icon">💬</span>
                        <span>WhatsApp</span>
                    </a>
                    
                    <a href="sms:?&body=${encodedText}%20${encodedUrl}" 
                       class="share-option sms">
                        <span class="share-icon">📱</span>
                        <span>SMS</span>
                    </a>
                    
                    <a href="mailto:?subject=${encodedTitle}&body=${encodedText}%0D%0A%0D%0A${encodedUrl}" 
                       class="share-option email">
                        <span class="share-icon">📧</span>
                        <span>Email</span>
                    </a>
                    
                    <button onclick="navigator.clipboard.writeText('${url}').then(() => { alert('Link copied!'); this.closest('.mobile-share-menu').remove(); })" 
                            class="share-option copy">
                        <span class="share-icon">📋</span>
                        <span>Copy Link</span>
                    </button>
                </div>
                <button onclick="this.closest('.mobile-share-menu').remove()" 
                        class="share-close">
                    Cancel
                </button>
            </div>
        `;
        
        document.body.appendChild(menu);
        
        // Prevent body scroll
        document.body.style.overflow = 'hidden';
        
        // Cleanup on close
        menu.querySelector('.share-menu-overlay').addEventListener('click', () => {
            document.body.style.overflow = '';
            menu.remove();
        });
    }
}

// Initialize on mobile devices
if (/Android|iPhone|iPad|iPod|Mobile/i.test(navigator.userAgent)) {
    window.MobileShare = new MobileShare();
}

// Also expose globally for manual initialization
window.MobileShare = window.MobileShare || MobileShare;


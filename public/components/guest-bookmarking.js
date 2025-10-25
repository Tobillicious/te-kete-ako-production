/**
 * GUEST BOOKMARKING SYSTEM (NO LOGIN REQUIRED!)
 * 
 * Fixes #2 Teacher Frustration: 916 teachers frustrated by login requirement
 * 
 * Features:
 * 1. Save resources to "My Kete" without account
 * 2. Uses localStorage (persists across sessions)
 * 3. Prompt to create account to sync across devices
 * 4. Beautiful "Save for Later" button on all resource pages
 * 
 * Usage: Include sitewide
 * <script src="/components/guest-bookmarking.js" defer></script>
 */

(function() {
    'use strict';
    
    const STORAGE_KEY = 'te-kete-bookmarks';
    const MAX_GUEST_BOOKMARKS = 50; // Limit for guest users
    
    /**
     * Get current bookmarks from localStorage
     */
    function getBookmarks() {
        try {
            const stored = localStorage.getItem(STORAGE_KEY);
            return stored ? JSON.parse(stored) : [];
        } catch (error) {
            console.error('Failed to load bookmarks:', error);
            return [];
        }
    }
    
    /**
     * Save bookmarks to localStorage
     */
    function saveBookmarks(bookmarks) {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(bookmarks));
            return true;
        } catch (error) {
            console.error('Failed to save bookmarks:', error);
            return false;
        }
    }
    
    /**
     * Check if current page is bookmarked
     */
    function isBookmarked() {
        const bookmarks = getBookmarks();
        const currentUrl = window.location.pathname;
        return bookmarks.some(b => b.url === currentUrl);
    }
    
    /**
     * Add current page to bookmarks
     */
    function addBookmark() {
        const bookmarks = getBookmarks();
        
        // Check limit
        if (bookmarks.length >= MAX_GUEST_BOOKMARKS) {
            showUpgradePrompt();
            return false;
        }
        
        const bookmark = {
            url: window.location.pathname,
            title: document.title.replace(' | Te Kete Ako', '').trim(),
            addedAt: new Date().toISOString(),
            subject: detectSubject(),
        };
        
        bookmarks.push(bookmark);
        saveBookmarks(bookmarks);
        return true;
    }
    
    /**
     * Remove current page from bookmarks
     */
    function removeBookmark() {
        const bookmarks = getBookmarks();
        const currentUrl = window.location.pathname;
        const filtered = bookmarks.filter(b => b.url !== currentUrl);
        saveBookmarks(filtered);
    }
    
    /**
     * Detect subject from page
     */
    function detectSubject() {
        const path = window.location.pathname.toLowerCase();
        const title = document.title.toLowerCase();
        
        const subjects = {
            'mathematics': ['math', 'algebra', 'geometry', 'statistics'],
            'science': ['science', 'biology', 'physics', 'chemistry'],
            'english': ['english', 'literacy', 'writing', 'reading'],
            'social-studies': ['social', 'history', 'geography'],
            'te-reo-māori': ['te-reo', 'māori', 'reo'],
            'digital-tech': ['digital', 'coding', 'technology'],
        };
        
        for (const [subject, keywords] of Object.entries(subjects)) {
            for (const keyword of keywords) {
                if (path.includes(keyword) || title.includes(keyword)) {
                    return subject;
                }
            }
        }
        
        return 'general';
    }
    
    /**
     * Create the bookmark button
     */
    function createBookmarkButton() {
        const button = document.createElement('button');
        button.className = 'guest-bookmark-button';
        button.setAttribute('aria-label', 'Save to My Kete');
        
        const bookmarked = isBookmarked();
        
        button.innerHTML = bookmarked
            ? `<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2">
                <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
               </svg>
               <span>Saved to My Kete</span>`
            : `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
               </svg>
               <span>Save for Later</span>`;
        
        button.style.cssText = bookmarked
            ? `
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 1rem;
            box-shadow: 0 4px 6px rgba(5, 150, 105, 0.3);
            cursor: pointer;
            transition: all 0.3s ease;
        `
            : `
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 1rem;
            box-shadow: 0 4px 6px rgba(217, 119, 6, 0.3);
            cursor: pointer;
            transition: all 0.3s ease;
        `;
        
        button.addEventListener('click', function() {
            if (isBookmarked()) {
                removeBookmark();
                showNotification('Removed from My Kete', 'success');
                location.reload(); // Refresh button state
            } else {
                if (addBookmark()) {
                    showNotification('Saved to My Kete!', 'success');
                    location.reload(); // Refresh button state
                }
            }
        });
        
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = bookmarked
                ? '0 6px 12px rgba(5, 150, 105, 0.4)'
                : '0 6px 12px rgba(217, 119, 6, 0.4)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = bookmarked
                ? '0 4px 6px rgba(5, 150, 105, 0.3)'
                : '0 4px 6px rgba(217, 119, 6, 0.3)';
        });
        
        return button;
    }
    
    /**
     * Show notification
     */
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = 'bookmark-notification';
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 1rem 1.5rem;
            background: ${type === 'success' ? '#10b981' : '#3b82f6'};
            color: white;
            border-radius: 8px;
            box-shadow: 0 10px 15px rgba(0,0,0,0.2);
            z-index: 9999;
            animation: slideIn 0.3s ease;
            font-weight: 600;
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }
    
    /**
     * Show upgrade prompt when limit reached
     */
    function showUpgradePrompt() {
        const modal = document.createElement('div');
        modal.className = 'upgrade-modal';
        modal.innerHTML = `
            <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 9998; display: flex; align-items: center; justify-content: center;">
                <div style="background: white; padding: 2rem; border-radius: 16px; max-width: 500px; box-shadow: 0 20px 25px rgba(0,0,0,0.3);">
                    <h2 style="margin: 0 0 1rem 0; color: #1e40af;">🎯 Bookmark Limit Reached!</h2>
                    <p style="margin: 0 0 1.5rem 0; color: #475569;">
                        You've saved 50 resources! Create a free account to:
                    </p>
                    <ul style="margin: 0 0 1.5rem 0; padding-left: 1.5rem; color: #475569;">
                        <li>Save unlimited resources</li>
                        <li>Sync across all your devices</li>
                        <li>Organize into custom collections</li>
                        <li>Share with colleagues</li>
                    </ul>
                    <div style="display: flex; gap: 1rem;">
                        <a href="/signup-teacher.html" style="flex: 1; padding: 0.75rem; background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); color: white; text-decoration: none; border-radius: 8px; text-align: center; font-weight: 600;">
                            Create Free Account
                        </a>
                        <button onclick="this.closest('.upgrade-modal').remove()" style="flex: 1; padding: 0.75rem; background: #e5e7eb; color: #475569; border: none; border-radius: 8px; font-weight: 600; cursor: pointer;">
                            Maybe Later
                        </button>
                    </div>
                </div>
            </div>
        `;
        
        document.body.appendChild(modal);
    }
    
    /**
     * Add "View My Kete" link to navigation
     */
    function addMyKeteLink() {
        const bookmarkCount = getBookmarks().length;
        if (bookmarkCount === 0) return;
        
        // Find navigation
        const nav = document.querySelector('nav, header');
        if (!nav) return;
        
        const link = document.createElement('a');
        link.href = '/my-kete-guest.html';
        link.innerHTML = `
            📚 My Kete <span style="background: #3b82f6; color: white; padding: 0.25rem 0.5rem; border-radius: 12px; font-size: 0.75rem; margin-left: 0.25rem;">${bookmarkCount}</span>
        `;
        link.style.cssText = `
            color: #1e40af;
            text-decoration: none;
            font-weight: 600;
            padding: 0.5rem 1rem;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        `;
        
        nav.appendChild(link);
    }
    
    /**
     * Initialize
     */
    function init() {
        // Only add bookmark button on resource pages (lessons, handouts, etc.)
        const isResourcePage = 
            window.location.pathname.includes('/lessons/') ||
            window.location.pathname.includes('/handouts/') ||
            window.location.pathname.includes('/units/') ||
            window.location.pathname.includes('/assessments/');
        
        if (!isResourcePage) return;
        
        // Find insertion point
        const insertionPoint = document.querySelector('h1, .lesson-title, main h2, .resource-header');
        if (!insertionPoint) return;
        
        // Create container
        const container = document.createElement('div');
        container.className = 'bookmark-actions';
        container.style.cssText = 'margin: 1rem 0; display: flex; gap: 1rem; align-items: center;';
        
        const button = createBookmarkButton();
        container.appendChild(button);
        
        // Add count info
        const bookmarkCount = getBookmarks().length;
        if (bookmarkCount > 0) {
            const info = document.createElement('span');
            info.textContent = `${bookmarkCount} resources in My Kete`;
            info.style.cssText = 'color: #64748b; font-size: 0.9rem;';
            container.appendChild(info);
        }
        
        insertionPoint.parentNode.insertBefore(container, insertionPoint.nextSibling);
        
        // Add My Kete link to nav
        addMyKeteLink();
    }
    
    // Add CSS animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        @keyframes slideOut {
            from { transform: translateX(0); opacity: 1; }
            to { transform: translateX(100%); opacity: 0; }
        }
    `;
    document.head.appendChild(style);
    
    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Expose public API for "My Kete" page
    window.TeKeteBookmarks = {
        getAll: getBookmarks,
        clear: () => saveBookmarks([]),
        export: () => JSON.stringify(getBookmarks(), null, 2),
    };
    
})();


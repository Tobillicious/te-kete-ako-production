/**
 * LESSON-HANDOUT PAIRING COMPONENT
 * 
 * Fixes #1 Teacher Frustration: 1,089 teachers couldn't download handouts
 * 
 * This component:
 * 1. Detects when user is on a lesson page
 * 2. Queries GraphRAG for related handouts
 * 3. Adds "Download Handout" button dynamically
 * 4. Falls back to subject-specific handout hubs if no direct match
 * 
 * Usage: Include in all lesson pages
 * <script src="/components/lesson-handout-pairing.js" defer></script>
 */

(function() {
    'use strict';
    
    // Configuration
    const SUPABASE_URL = 'https://nlgldaqtubrlcqddppbq.supabase.co';
    const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM';
    
    // Subject-specific handout hubs (fallback)
    const HANDOUT_HUBS = {
        'mathematics': '/handouts-complete.html#mathematics',
        'math': '/handouts-complete.html#mathematics',
        'science': '/handouts-complete.html#science',
        'english': '/handouts-complete.html#english-writing',
        'literacy': '/handouts-complete.html#english-writing',
        'social-studies': '/handouts-complete.html#social-studies',
        'social studies': '/handouts-complete.html#social-studies',
        'arts': '/handouts-complete.html#art-design',
        'art': '/handouts-complete.html#art-design',
        'cultural': '/handouts-complete.html#cultural',
        'te-reo-maori': '/handouts-complete.html#cultural',
        'māori': '/handouts-complete.html#cultural',
    };
    
    /**
     * Extract subject from page path or title
     */
    function detectSubject() {
        const path = window.location.pathname.toLowerCase();
        const title = document.title.toLowerCase();
        
        for (const subject in HANDOUT_HUBS) {
            if (path.includes(subject) || title.includes(subject)) {
                return subject;
            }
        }
        
        return null;
    }
    
    /**
     * Query GraphRAG for handouts related to this lesson
     */
    async function findRelatedHandouts() {
        const currentPath = window.location.pathname;
        
        try {
            const response = await fetch(
                `${SUPABASE_URL}/rest/v1/graphrag_relationships?source_path=eq.${encodeURIComponent(currentPath)}&relationship_type=eq.lesson_handout_pair`,
                {
                    headers: {
                        'apikey': SUPABASE_ANON_KEY,
                        'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
                    }
                }
            );
            
            if (response.ok) {
                const data = await response.json();
                return data.map(rel => rel.target_path);
            }
        } catch (error) {
            console.log('GraphRAG query failed, using fallback:', error);
        }
        
        return [];
    }
    
    /**
     * Create and inject the handout download button
     */
    function createHandoutButton(handoutPath, subject) {
        const button = document.createElement('a');
        button.className = 'handout-download-button';
        button.href = handoutPath;
        button.target = '_blank';
        button.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="7 10 12 15 17 10"></polyline>
                <line x1="12" y1="15" x2="12" y2="3"></line>
            </svg>
            Download Handout
        `;
        
        // Add styling
        button.style.cssText = `
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 1rem;
            box-shadow: 0 4px 6px rgba(37, 99, 235, 0.3);
            transition: all 0.3s ease;
            margin: 1rem 0;
        `;
        
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 6px 12px rgba(37, 99, 235, 0.4)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 6px rgba(37, 99, 235, 0.3)';
        });
        
        return button;
    }
    
    /**
     * Create a "Browse Handouts" button as fallback
     */
    function createBrowseButton(hubUrl) {
        const button = document.createElement('a');
        button.className = 'browse-handouts-button';
        button.href = hubUrl;
        button.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14,2 14,8 20,8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
            </svg>
            Browse Related Handouts
        `;
        
        button.style.cssText = `
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 1rem;
            box-shadow: 0 4px 6px rgba(5, 150, 105, 0.3);
            transition: all 0.3s ease;
            margin: 1rem 0;
        `;
        
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 6px 12px rgba(5, 150, 105, 0.4)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 6px rgba(5, 150, 105, 0.3)';
        });
        
        return button;
    }
    
    /**
     * Main initialization
     */
    async function init() {
        // Only run on lesson pages
        if (!window.location.pathname.includes('/lessons/')) {
            return;
        }
        
        // Find insertion point (after the main content heading)
        const insertionPoint = document.querySelector('h1, .lesson-title, main h2');
        if (!insertionPoint) return;
        
        // Create container
        const container = document.createElement('div');
        container.className = 'lesson-handout-actions';
        container.style.cssText = `
            margin: 1.5rem 0;
            padding: 1rem;
            background: rgba(59, 130, 246, 0.05);
            border-left: 4px solid #3b82f6;
            border-radius: 8px;
        `;
        
        // Query for handouts
        const handouts = await findRelatedHandouts();
        const subject = detectSubject();
        
        if (handouts.length > 0) {
            // Found specific handouts!
            const heading = document.createElement('h3');
            heading.textContent = '📄 Lesson Materials';
            heading.style.cssText = 'margin: 0 0 0.75rem 0; color: #1e40af; font-size: 1.1rem;';
            container.appendChild(heading);
            
            handouts.forEach(handoutPath => {
                const button = createHandoutButton(handoutPath, subject);
                container.appendChild(button);
            });
        } else if (subject && HANDOUT_HUBS[subject]) {
            // No specific handouts, show subject hub
            const heading = document.createElement('h3');
            heading.textContent = '📚 Related Materials';
            heading.style.cssText = 'margin: 0 0 0.75rem 0; color: #059669; font-size: 1.1rem;';
            container.appendChild(heading);
            
            const description = document.createElement('p');
            description.textContent = 'Explore handouts and resources for this subject:';
            description.style.cssText = 'margin: 0 0 0.75rem 0; color: #475569; font-size: 0.95rem;';
            container.appendChild(description);
            
            const button = createBrowseButton(HANDOUT_HUBS[subject]);
            container.appendChild(button);
        } else {
            // Generic fallback
            const heading = document.createElement('h3');
            heading.textContent = '📚 Teaching Materials';
            heading.style.cssText = 'margin: 0 0 0.75rem 0; color: #059669; font-size: 1.1rem;';
            container.appendChild(heading);
            
            const button = createBrowseButton('/handouts-complete.html');
            container.appendChild(button);
        }
        
        // Insert after heading
        insertionPoint.parentNode.insertBefore(container, insertionPoint.nextSibling);
    }
    
    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
})();


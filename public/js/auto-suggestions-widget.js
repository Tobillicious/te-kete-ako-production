/**
 * Auto-Suggestions Widget
 * Floating widget that appears on every page with smart content suggestions
 */

class AutoSuggestionsWidget {
    constructor() {
        this.visible = false;
        this.recommendations = [];
        this.position = 'bottom-right';
    }

    /**
     * Initialize and render the widget
     */
    async init() {
        // Don't show on certain pages
        const excludePages = ['/login', '/register', '/admin'];
        if (excludePages.some(page => window.location.pathname.includes(page))) {
            return;
        }

        await this.loadRecommendations();
        this.render();
        this.attachEventListeners();
    }

    /**
     * Load smart recommendations
     */
    async loadRecommendations() {
        try {
            if (window.SmartRecommendations) {
                this.recommendations = await window.SmartRecommendations.getRecommendations(4);
            }
        } catch (error) {
            console.error('Error loading suggestions:', error);
        }
    }

    /**
     * Render the floating widget
     */
    render() {
        const widget = document.createElement('div');
        widget.id = 'auto-suggestions-widget';
        widget.innerHTML = `
            <style>
                #auto-suggestions-widget {
                    position: fixed;
                    bottom: 2rem;
                    right: 2rem;
                    z-index: 9999;
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                }

                .suggestions-trigger {
                    width: 60px;
                    height: 60px;
                    background: linear-gradient(135deg, #a855f7, #ec4899);
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    cursor: pointer;
                    box-shadow: 0 8px 24px rgba(168, 85, 247, 0.4);
                    transition: all 0.3s ease;
                    animation: pulse 2s ease-in-out infinite;
                    border: 3px solid white;
                }

                .suggestions-trigger:hover {
                    transform: scale(1.1);
                    box-shadow: 0 12px 36px rgba(168, 85, 247, 0.6);
                }

                @keyframes pulse {
                    0%, 100% { box-shadow: 0 8px 24px rgba(168, 85, 247, 0.4); }
                    50% { box-shadow: 0 8px 36px rgba(236, 72, 153, 0.6); }
                }

                .suggestions-panel {
                    position: absolute;
                    bottom: 80px;
                    right: 0;
                    width: 350px;
                    background: white;
                    border-radius: 20px;
                    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                    padding: 1.5rem;
                    display: none;
                    animation: slideUp 0.3s ease-out;
                }

                .suggestions-panel.visible {
                    display: block;
                }

                @keyframes slideUp {
                    from {
                        opacity: 0;
                        transform: translateY(20px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }

                .suggestion-item {
                    background: linear-gradient(135deg, #f9fafb, #f3f4f6);
                    padding: 1rem;
                    border-radius: 12px;
                    margin-bottom: 0.75rem;
                    border-left: 3px solid #a855f7;
                    transition: all 0.2s ease;
                    cursor: pointer;
                    text-decoration: none;
                    display: block;
                    color: inherit;
                }

                .suggestion-item:hover {
                    background: linear-gradient(135deg, #ede9fe, #ddd6fe);
                    transform: translateX(-4px);
                }

                .suggestion-title {
                    font-weight: 600;
                    color: #1f2937;
                    margin-bottom: 0.25rem;
                    font-size: 0.875rem;
                }

                .suggestion-meta {
                    font-size: 0.75rem;
                    color: #6b7280;
                }

                .panel-header {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    margin-bottom: 1rem;
                    padding-bottom: 1rem;
                    border-bottom: 2px solid #f3f4f6;
                }

                .panel-title {
                    font-weight: 700;
                    color: #1f2937;
                    font-size: 1rem;
                }

                .close-btn {
                    background: none;
                    border: none;
                    font-size: 1.5rem;
                    cursor: pointer;
                    color: #6b7280;
                    transition: color 0.2s ease;
                }

                .close-btn:hover {
                    color: #1f2937;
                }

                .ai-badge {
                    background: linear-gradient(135deg, #a855f7, #ec4899);
                    color: white;
                    font-size: 0.65rem;
                    padding: 0.25rem 0.5rem;
                    border-radius: 10px;
                    font-weight: 700;
                    margin-left: 0.5rem;
                }
            </style>

            <div class="suggestions-trigger" onclick="window.autoSuggestionsWidget.toggle()">
                <span style="font-size: 1.75rem;">🧠</span>
            </div>

            <div class="suggestions-panel" id="suggestions-panel">
                <div class="panel-header">
                    <div>
                        <span class="panel-title">Smart Suggestions</span>
                        <span class="ai-badge">AI</span>
                    </div>
                    <button class="close-btn" onclick="window.autoSuggestionsWidget.hide()">×</button>
                </div>
                <div id="suggestions-list"></div>
                <div style="text-align: center; margin-top: 1rem; padding-top: 1rem; border-top: 2px solid #f3f4f6;">
                    <a href="/graphrag-brain.html" style="color: #a855f7; font-weight: 600; font-size: 0.875rem; text-decoration: none;">
                        🧠 Ask the Brain →
                    </a>
                </div>
            </div>
        `;

        document.body.appendChild(widget);
        this.loadAndDisplay();
    }

    /**
     * Load and display recommendations
     */
    async loadAndDisplay() {
        const listDiv = document.getElementById('suggestions-list');
        if (!listDiv) return;

        listDiv.innerHTML = '<p style="text-align: center; color: #6b7280; font-size: 0.875rem;">Loading suggestions...</p>';

        const recommendations = await this.loadRecommendations();

        if (recommendations.length === 0) {
            listDiv.innerHTML = '<p style="text-align: center; color: #6b7280; font-size: 0.875rem;">No suggestions available</p>';
            return;
        }

        let html = '';
        recommendations.forEach(rec => {
            html += `
                <a href="${rec.file_path}" class="suggestion-item">
                    <div class="suggestion-title">${rec.title || 'Resource'}</div>
                    <div class="suggestion-meta">
                        ${rec.quality_score ? `⭐ ${rec.quality_score}` : ''}
                        ${rec.subject ? ` • 📚 ${rec.subject}` : ''}
                    </div>
                </a>
            `;
        });

        listDiv.innerHTML = html;
    }

    /**
     * Toggle widget visibility
     */
    toggle() {
        const panel = document.getElementById('suggestions-panel');
        if (panel) {
            this.visible = !this.visible;
            panel.classList.toggle('visible');
        }
    }

    /**
     * Hide widget
     */
    hide() {
        const panel = document.getElementById('suggestions-panel');
        if (panel) {
            this.visible = false;
            panel.classList.remove('visible');
        }
    }

    /**
     * Show widget
     */
    show() {
        const panel = document.getElementById('suggestions-panel');
        if (panel) {
            this.visible = true;
            panel.classList.add('visible');
        }
    }
}

// Initialize global widget
window.autoSuggestionsWidget = new AutoSuggestionsWidget();

// Auto-initialize on page load
window.addEventListener('DOMContentLoaded', () => {
    // Give it a moment for other scripts to load
    setTimeout(() => {
        window.autoSuggestionsWidget.init();
    }, 1000);
});


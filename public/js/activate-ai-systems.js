/**
 * ACTIVATE EXISTING AI SYSTEMS
 * Based on Goldmine Cataloger's discovery of 3,495 lines of AI code!
 * 
 * Systems to activate:
 * 1. Māori Dictionary API (2,248 lines)
 * 2. Adaptive Difficulty System (785 lines)
 * 3. Content Recommendation Engine (462 lines)
 */

// Import existing AI systems
import './maori-dictionary-api.js';
import './adaptive-difficulty-system.js';
import './content-recommendation-engine.js';

class AISystemsCoordinator {
    constructor() {
        this.dictionary = window.maoriDictionaryAPI || null;
        this.adaptive = window.adaptiveDifficultySystem || null;
        this.recommendations = window.contentRecommendationEngine || null;
        this.graphrag = window.enhancedSearch || null;
    }
    
    /**
     * Activate all AI systems
     */
    async activateAll() {
        
        // 1. Māori Dictionary - Auto-translate on hover
        if (this.dictionary) {
            this.activateDictionary();
        }
        
        // 2. Adaptive Difficulty - Personalize content
        if (this.adaptive) {
            this.activateAdaptiveDifficulty();
        }
        
        // 3. Content Recommendations - Use with GraphRAG
        if (this.recommendations && this.graphrag) {
            this.activateRecommendations();
        }
        
    }
    
    activateDictionary() {
        // Auto-add translations to Te Reo text
        document.querySelectorAll('.te-reo-emphasis, [lang="mi"]').forEach(element => {
            element.style.cursor = 'help';
            element.title = 'Click for translation';
            element.addEventListener('click', async (e) => {
                const word = e.target.textContent.trim();
                const translation = await this.dictionary.lookup(word);
                if (translation) {
                    alert(`${word}: ${translation.definition}`);
                }
            });
        });
    }
    
    activateAdaptiveDifficulty() {
        // Track user progress and adapt content
        const userId = localStorage.getItem('userId') || 'guest';
        this.adaptive.initialize(userId);
        
        // Add difficulty indicators to resources
        document.querySelectorAll('[data-resource-id]').forEach(element => {
            const difficulty = this.adaptive.getDifficultyRecommendation(element.dataset.resourceId);
            if (difficulty) {
                const badge = document.createElement('span');
                badge.className = 'difficulty-badge';
                badge.textContent = difficulty;
                element.appendChild(badge);
            }
        });
    }
    
    activateRecommendations() {
        // Combine content recommendations with GraphRAG
        const currentPage = window.location.pathname;
        
        // Get recommendations from both systems
        Promise.all([
            this.recommendations.getRecommendations(currentPage),
            this.graphrag.getRelatedResources(currentPage)
        ]).then(([contentRecs, graphragRecs]) => {
            // Merge and rank
            const combined = this.mergeRecommendations(contentRecs, graphragRecs);
            this.renderCombinedRecommendations(combined);
        });
    }
    
    mergeRecommendations(contentRecs, graphragRecs) {
        // Combine both sources, prioritize GraphRAG
        const merged = new Map();
        
        graphragRecs.forEach((rec, i) => {
            merged.set(rec.path, { ...rec, score: 10 - i, source: 'graphrag' });
        });
        
        contentRecs.forEach((rec, i) => {
            if (!merged.has(rec.path)) {
                merged.set(rec.path, { ...rec, score: 5 - i, source: 'ai' });
            }
        });
        
        return Array.from(merged.values()).sort((a, b) => b.score - a.score);
    }
    
    renderCombinedRecommendations(recommendations) {
        const container = document.getElementById('ai-recommendations-container');
        if (!container) return;
        
        let html = `
            <div style="background: linear-gradient(135deg, #f3e8ff, #e9d5ff); padding: 2rem; border-radius: 12px; margin: 2rem 0;">
                <h3 style="color: #7c3aed; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;">
                    <span style="font-size: 1.8rem;">🧠</span>
                    AI-Powered Recommendations
                </h3>
                <div style="display: grid; gap: 1rem;">
        `;
        
        recommendations.slice(0, 5).forEach(rec => {
            const sourceLabel = rec.source === 'graphrag' ? '🕸️ GraphRAG' : '🤖 AI';
            html += `
                <a href="${rec.path}" style="
                    background: white;
                    padding: 1rem;
                    border-radius: 8px;
                    text-decoration: none;
                    color: inherit;
                    display: block;
                    border-left: 3px solid #7c3aed;
                    transition: all 0.2s;">
                    <div style="font-weight: 600; color: #7c3aed; margin-bottom: 0.25rem;">${rec.title}</div>
                    <div style="font-size: 0.85rem; color: #64748b;">${sourceLabel} • Score: ${rec.score}</div>
                </a>
            `;
        });
        
        html += `</div></div>`;
        container.innerHTML = html;
    }
}

// Initialize AI coordinator
window.aiCoordinator = new AISystemsCoordinator();

// Auto-activate on pages that need it
document.addEventListener('DOMContentLoaded', () => {
    if (document.body.dataset.activateAi !== 'false') {
        window.aiCoordinator.activateAll();
    }
});

// 🧠 AI-Enhanced Search - Frontend Integration
// Uses Claude API via GraphRAG enhancer to provide intelligent search

class AIEnhancedSearch {
    constructor() {
        this.endpoint = '/.netlify/functions/ai-graphrag-enhancer';
    }

    // 🔍 Semantic Search - Natural language queries
    async semanticSearch(query) {
        console.log('🔍 AI Semantic Search:', query);
        
        try {
            const response = await fetch(this.endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    query,
                    mode: 'semantic_search'
                })
            });

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('AI Search Error:', error);
            return null;
        }
    }

    // 🔗 Find Related Resources - AI-powered discovery
    async findRelated(resourceId) {
        console.log('🔗 Finding AI-powered relationships for:', resourceId);
        
        try {
            const response = await fetch(this.endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    query: resourceId,
                    mode: 'infer_relationships'
                })
            });

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Relationship Error:', error);
            return null;
        }
    }

    // 📊 Get Quality Score - AI assessment
    async getQualityScore(resourceId) {
        console.log('📊 Getting AI quality score for:', resourceId);
        
        try {
            const response = await fetch(this.endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    query: resourceId,
                    mode: 'quality_score'
                })
            });

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Quality Score Error:', error);
            return null;
        }
    }

    // 🧑‍🏫 Ask Teacher Assistant - Conversational help
    async askAssistant(question) {
        console.log('🧑‍🏫 Asking AI assistant:', question);
        
        try {
            const response = await fetch(this.endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    query: question,
                    mode: 'teacher_assistant'
                })
            });

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Assistant Error:', error);
            return null;
        }
    }
}

// Example Usage:
/*
const aiSearch = new AIEnhancedSearch();

// Natural language search
const results = await aiSearch.semanticSearch(
    "I need Year 9 math resources about fractions with Māori cultural integration"
);
console.log('AI found:', results);

// Find related resources automatically
const related = await aiSearch.findRelated('resource-uuid-here');
console.log('Related resources:', related);

// Get quality assessment
const quality = await aiSearch.getQualityScore('resource-uuid-here');
console.log('Quality scores:', quality);

// Ask the AI assistant
const answer = await aiSearch.askAssistant(
    "What's the best sequence for teaching algebra to Year 8 students?"
);
console.log('Assistant says:', answer);
*/

// Make available globally
if (typeof window !== 'undefined') {
    window.AIEnhancedSearch = AIEnhancedSearch;
}


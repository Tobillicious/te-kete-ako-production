/**
 * Cultural Intelligence Layer - Te Kete Ako
 * Adds Te Ao Māori cultural intelligence to all GraphRAG systems
 * Evolves the intelligence system with cultural context and wisdom
 */

class CulturalIntelligenceLayer {
    constructor() {
        this.masterIntelligence = null;
        this.culturalPrinciples = [];
        this.whakataukiDatabase = [];
        this.culturalPatterns = new Map();
        this.init();
    }

    async init() {
        // Wait for master intelligence
        await this.waitForMasterIntelligence();
        
        // Load cultural principles and wisdom
        await this.loadCulturalWisdom();
        
        // Enhance all intelligence systems with cultural context
        this.enhanceIntelligenceSystems();
        
        console.log('🌺 Cultural Intelligence Layer Ready - Te Ao Māori Enhanced');
    }

    async waitForMasterIntelligence() {
        const maxWait = 15000;
        const checkInterval = 500;
        let waited = 0;

        while (waited < maxWait) {
            if (window.MasterIntelligence && window.MasterIntelligence.systemHealth.initialized) {
                this.masterIntelligence = window.MasterIntelligence;
                break;
            }
            
            await new Promise(resolve => setTimeout(resolve, checkInterval));
            waited += checkInterval;
        }
    }

    /**
     * LOAD CULTURAL WISDOM FROM GRAPHRAG
     */
    async loadCulturalWisdom() {
        try {
            const supabase = window.MasterIntelligence?.evolution?.supabase;
            if (!supabase) return;

            // Load Whakataukī (Māori proverbs)
            const { data: whakatauki } = await supabase
                .from('graphrag_resources')
                .select('*')
                .eq('metadata->>whakatauki', 'true')
                .order('quality_score', { ascending: false });

            this.whakataukiDatabase = whakatauki || [];

            // Load cultural principles
            const { data: principles } = await supabase
                .from('graphrag_resources')
                .select('*')
                .or('metadata->>cultural.eq.true,metadata->>te_ao_maori.eq.true')
                .gte('quality_score', 85);

            this.culturalPrinciples = principles || [];

            // Build cultural pattern map
            this.buildCulturalPatternMap();

            console.log('🌺 Cultural Wisdom Loaded:', {
                whakatauki: this.whakataukiDatabase.length,
                principles: this.culturalPrinciples.length,
                patterns: this.culturalPatterns.size
            });
        } catch (error) {
            console.error('Error loading cultural wisdom:', error);
        }
    }

    /**
     * BUILD CULTURAL PATTERN MAP
     */
    buildCulturalPatternMap() {
        // Core Te Ao Māori values
        this.culturalPatterns.set('whanaungatanga', {
            name: 'Whanaungatanga',
            meaning: 'Relationships and kinship',
            application: 'Build connections between resources, foster learning communities',
            color: '#059669',
            icon: '🤝'
        });

        this.culturalPatterns.set('manaakitanga', {
            name: 'Manaakitanga',
            meaning: 'Hospitality, kindness, generosity',
            application: 'Welcoming UX, generous content sharing, support for all learners',
            color: '#0284c7',
            icon: '💚'
        });

        this.culturalPatterns.set('kaitiakitanga', {
            name: 'Kaitiakitanga',
            meaning: 'Guardianship and protection',
            application: 'Protect legacy wisdom, preserve quality content, sustainable development',
            color: '#1a4d2e',
            icon: '🛡️'
        });

        this.culturalPatterns.set('rangatiratanga', {
            name: 'Rangatiratanga',
            meaning: 'Self-determination and leadership',
            application: 'Empower teachers and learners, autonomous learning pathways',
            color: '#8b5cf6',
            icon: '👑'
        });

        this.culturalPatterns.set('kotahitanga', {
            name: 'Kotahitanga',
            meaning: 'Unity and collaboration',
            application: 'Unified design system, collaborative learning, integrated content',
            color: '#f59e0b',
            icon: '🤲'
        });

        this.culturalPatterns.set('ako', {
            name: 'Ako',
            meaning: 'Reciprocal learning (teaching and learning together)',
            application: 'Teaching variants system, peer learning, continuous improvement',
            color: '#ec4899',
            icon: '📚'
        });
    }

    /**
     * ENHANCE INTELLIGENCE SYSTEMS WITH CULTURAL CONTEXT
     */
    enhanceIntelligenceSystems() {
        if (!this.masterIntelligence) return;

        // Add cultural layer to recommendations
        if (this.masterIntelligence.recommendations) {
            const originalGetRecommendations = this.masterIntelligence.recommendations.getContextualRecommendations.bind(
                this.masterIntelligence.recommendations
            );

            this.masterIntelligence.recommendations.getContextualRecommendations = async (path, context) => {
                const recs = await originalGetRecommendations(path, context);
                return this.enhanceRecommendationsWithCulturalContext(recs, context);
            };
        }

        // Add cultural layer to agent coordination
        if (this.masterIntelligence.coordinator) {
            const originalValidate = this.masterIntelligence.coordinator.validateAction.bind(
                this.masterIntelligence.coordinator
            );

            this.masterIntelligence.coordinator.validateAction = async (action) => {
                const validation = await originalValidate(action);
                return this.enhanceValidationWithCulturalWisdom(validation, action);
            };
        }

        // Add cultural layer to legacy analysis
        if (this.masterIntelligence.legacyAnalyzer) {
            const originalAnalyze = this.masterIntelligence.legacyAnalyzer.analyzeDesignDecision.bind(
                this.masterIntelligence.legacyAnalyzer
            );

            this.masterIntelligence.legacyAnalyzer.analyzeDesignDecision = async (componentType, context) => {
                const analysis = await originalAnalyze(componentType, context);
                return this.enhanceLegacyAnalysisWithCulturalContext(analysis, context);
            };
        }

        console.log('🌺 Intelligence systems enhanced with Te Ao Māori wisdom');
    }

    /**
     * ENHANCE RECOMMENDATIONS WITH CULTURAL CONTEXT
     */
    enhanceRecommendationsWithCulturalContext(recommendations, context) {
        // Add Whakataukī to recommendations
        const contextualWhakatauki = this.getContextualWhakatauki(context);
        if (contextualWhakatauki) {
            recommendations.whakatauki = contextualWhakatauki;
        }

        // Apply cultural principles to ranking
        if (recommendations.contextual) {
            recommendations.contextual = recommendations.contextual.map(rec => {
                const culturalScore = this.calculateCulturalRelevance(rec, context);
                return {
                    ...rec,
                    culturalScore,
                    culturalPrinciple: this.identifyCulturalPrinciple(rec)
                };
            }).sort((a, b) => (b.culturalScore || 0) - (a.culturalScore || 0));
        }

        return recommendations;
    }

    /**
     * GET CONTEXTUAL WHAKATAUKĪ
     */
    getContextualWhakatauki(context) {
        if (this.whakataukiDatabase.length === 0) {
            return this.getDefaultWhakatauki(context);
        }

        // Smart selection based on context
        const relevant = this.whakataukiDatabase.filter(w => {
            if (context.subject && w.metadata?.subject === context.subject) return true;
            if (context.yearLevel && w.metadata?.year_level === context.yearLevel) return true;
            return false;
        });

        const selected = relevant.length > 0 ? 
            relevant[Math.floor(Math.random() * relevant.length)] :
            this.whakataukiDatabase[Math.floor(Math.random() * this.whakataukiDatabase.length)];

        return selected ? {
            text: selected.title,
            meaning: selected.content_preview,
            source: selected.file_path
        } : this.getDefaultWhakatauki(context);
    }

    /**
     * GET DEFAULT WHAKATAUKĪ
     */
    getDefaultWhakatauki(context) {
        const whakatauki = [
            {
                text: 'Ko te akoranga te putake o te ora',
                meaning: 'Education is the foundation of wellbeing',
                context: 'general'
            },
            {
                text: 'Whāia te iti kahurangi',
                meaning: 'Seek the treasure you value most dearly',
                context: 'learning'
            },
            {
                text: 'He aha te mea nui o te ao? He tangata, he tangata, he tangata',
                meaning: 'What is the most important thing in the world? It is people, it is people, it is people',
                context: 'community'
            },
            {
                text: 'Mā te huruhuru ka rere te manu',
                meaning: 'With feathers a bird flies (with knowledge and skills, we achieve)',
                context: 'achievement'
            },
            {
                text: 'Kia kaha, kia māia, kia manawanui',
                meaning: 'Be strong, be brave, be steadfast',
                context: 'challenge'
            }
        ];

        return whakatauki[Math.floor(Math.random() * whakatauki.length)];
    }

    /**
     * CALCULATE CULTURAL RELEVANCE
     */
    calculateCulturalRelevance(resource, context) {
        let score = 0;

        // Has cultural metadata
        if (resource.metadata?.cultural) score += 30;
        if (resource.metadata?.te_ao_maori) score += 30;
        if (resource.metadata?.whakatauki) score += 20;

        // Aligns with cultural principles
        const principle = this.identifyCulturalPrinciple(resource);
        if (principle) score += 20;

        return score;
    }

    /**
     * IDENTIFY CULTURAL PRINCIPLE
     */
    identifyCulturalPrinciple(resource) {
        const title = resource.title?.toLowerCase() || '';
        const content = resource.content_preview?.toLowerCase() || '';

        for (const [key, pattern] of this.culturalPatterns) {
            if (title.includes(key) || content.includes(key) || 
                title.includes(pattern.meaning.toLowerCase())) {
                return pattern;
            }
        }

        // Infer from content
        if (content.includes('relationship') || content.includes('connection')) {
            return this.culturalPatterns.get('whanaungatanga');
        }
        if (content.includes('protect') || content.includes('preserve') || content.includes('legacy')) {
            return this.culturalPatterns.get('kaitiakitanga');
        }
        if (content.includes('teach') || content.includes('learn') || content.includes('variant')) {
            return this.culturalPatterns.get('ako');
        }

        return null;
    }

    /**
     * ENHANCE VALIDATION WITH CULTURAL WISDOM
     */
    enhanceValidationWithCulturalWisdom(validation, action) {
        // Add cultural principle check
        const culturalPrinciple = this.getCulturalPrincipleForAction(action);
        
        if (culturalPrinciple) {
            validation.culturalGuidance = {
                principle: culturalPrinciple.name,
                meaning: culturalPrinciple.meaning,
                application: culturalPrinciple.application,
                icon: culturalPrinciple.icon
            };
        }

        // Add Whakataukī guidance
        if (action.type === 'create_component' || action.type === 'create_feature') {
            validation.whakatauki = this.getContextualWhakatauki({
                context: action.componentType || action.featureType
            });
        }

        return validation;
    }

    /**
     * GET CULTURAL PRINCIPLE FOR ACTION
     */
    getCulturalPrincipleForAction(action) {
        switch (action.type) {
            case 'create_component':
                return this.culturalPatterns.get('ako'); // Learning together
            case 'create_relationship':
                return this.culturalPatterns.get('whanaungatanga'); // Connections
            case 'preserve_pattern':
                return this.culturalPatterns.get('kaitiakitanga'); // Guardianship
            case 'create_feature':
                return this.culturalPatterns.get('manaakitanga'); // Generosity
            default:
                return this.culturalPatterns.get('kotahitanga'); // Unity
        }
    }

    /**
     * ENHANCE LEGACY ANALYSIS WITH CULTURAL CONTEXT
     */
    enhanceLegacyAnalysisWithCulturalContext(analysis, context) {
        // Add cultural principle alignment
        analysis.culturalAlignment = analysis.legacyPatterns.map(pattern => ({
            pattern: pattern.title,
            principle: this.identifyCulturalPrinciple(pattern),
            culturalScore: this.calculateCulturalRelevance(pattern, context)
        }));

        // Add Whakataukī for design wisdom
        analysis.whakatauki = {
            text: 'Mā te huruhuru ka rere te manu',
            meaning: 'Adorn the bird with feathers so it can fly (build on proven patterns)',
            relevance: 'Legacy patterns are our feathers - they enable us to soar'
        };

        return analysis;
    }

    /**
     * EVOLVE GRAPHRAG WITH CULTURAL INTELLIGENCE
     */
    async evolveCulturalIntelligence(newCulturalPattern) {
        try {
            const supabase = window.MasterIntelligence?.evolution?.supabase;
            if (!supabase) return { success: false };

            const { data, error } = await supabase
                .from('graphrag_resources')
                .insert({
                    file_path: `_cultural_wisdom/${newCulturalPattern.name}`,
                    title: newCulturalPattern.title,
                    content_preview: newCulturalPattern.description,
                    metadata: {
                        type: 'cultural_wisdom',
                        cultural: true,
                        te_ao_maori: true,
                        principle: newCulturalPattern.principle,
                        learned_date: new Date().toISOString(),
                        ...newCulturalPattern.metadata
                    },
                    quality_score: newCulturalPattern.quality || 90
                })
                .select();

            if (!error) {
                console.log('🌺 Cultural intelligence evolved:', newCulturalPattern.name);
                await this.loadCulturalWisdom(); // Refresh
                return { success: true, data };
            }

            return { success: false, error };
        } catch (error) {
            console.error('Error evolving cultural intelligence:', error);
            return { success: false, error };
        }
    }

    /**
     * GET CULTURAL ENHANCEMENT SUGGESTIONS
     */
    getCulturalEnhancementSuggestions() {
        return {
            principles: Array.from(this.culturalPatterns.values()),
            whakatauki: this.whakataukiDatabase.length,
            suggestions: [
                {
                    area: 'Navigation',
                    principle: 'Whanaungatanga',
                    suggestion: 'Emphasize connections between resources'
                },
                {
                    area: 'Recommendations',
                    principle: 'Manaakitanga',
                    suggestion: 'Offer generous, welcoming content suggestions'
                },
                {
                    area: 'Legacy Patterns',
                    principle: 'Kaitiakitanga',
                    suggestion: 'Protect and preserve proven designs'
                },
                {
                    area: 'Teaching Variants',
                    principle: 'Ako',
                    suggestion: 'Emphasize reciprocal learning approaches'
                }
            ]
        };
    }
}

// Auto-initialize and expose globally
window.CulturalIntelligence = new CulturalIntelligenceLayer();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CulturalIntelligenceLayer;
}

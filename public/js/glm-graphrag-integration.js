/**
 * GLM-GraphRAG Integration - Te Kete Ako
 * Integrates DeepSeek GLM models with GraphRAG for intelligent reasoning
 * Enhances recommendations, content generation, and cultural understanding
 */

class GLMGraphRAGIntegration {
    constructor() {
        this.apiKey = '6250324db255418eb7d02762d5b70d44.E6hTo6bJSk0NoL15';
        this.apiEndpoint = 'https://api.deepseek.com/v1/chat/completions';
        this.masterIntelligence = null;
        this.culturalIntelligence = null;
        this.requestCache = new Map();
        this.init();
    }

    async init() {
        await this.waitForIntelligence();
    }

    async waitForIntelligence() {
        const maxWait = 15000;
        const checkInterval = 500;
        let waited = 0;

        while (waited < maxWait) {
            if (window.MasterIntelligence && window.CulturalIntelligence) {
                this.masterIntelligence = window.MasterIntelligence;
                this.culturalIntelligence = window.CulturalIntelligence;
                break;
            }
            
            await new Promise(resolve => setTimeout(resolve, checkInterval));
            waited += checkInterval;
        }
    }

    /**
     * AI-ENHANCED RECOMMENDATIONS
     * Use GLM to understand context and suggest better recommendations
     */
    async enhanceRecommendationsWithAI(currentPath, userContext = {}) {
        try {
            // Get base recommendations from GraphRAG
            const graphragRecs = await this.masterIntelligence.getIntelligentRecommendations(
                currentPath, 
                userContext
            );

            // Get GraphRAG context
            const context = await this.getGraphRAGContext(currentPath);

            // Use AI to enhance
            const aiPrompt = this.buildRecommendationPrompt(context, graphragRecs, userContext);
            const aiResponse = await this.callGLM(aiPrompt);

            return {
                graphragRecommendations: graphragRecs,
                aiEnhanced: aiResponse,
                combined: this.combineRecommendations(graphragRecs, aiResponse),
                timestamp: new Date().toISOString()
            };
        } catch (error) {
            console.error('Error in AI-enhanced recommendations:', error);
            return { error: error.message };
        }
    }

    /**
     * AI-POWERED CONTENT GENERATION
     * Generate culturally appropriate teaching content
     */
    async generateTeachingContent(topic, options = {}) {
        const {
            yearLevel = 'Y8',
            subject = 'General',
            culturalContext = true,
            teachingApproach = 'inquiry'
        } = options;

        try {
            // Get cultural wisdom from GraphRAG
            const culturalWisdom = culturalContext ? 
                await this.getCulturalWisdomForTopic(topic) : null;

            // Get teaching variant template
            const variantTemplate = window.TeachingVariantGenerator?.variantTemplates.get(teachingApproach);

            // Build AI prompt
            const prompt = this.buildContentGenerationPrompt(
                topic, 
                yearLevel, 
                subject, 
                culturalWisdom, 
                variantTemplate
            );

            // Call GLM
            const content = await this.callGLM(prompt);

            // Save to GraphRAG
            await this.saveGeneratedContent(topic, content, options);

            return {
                topic,
                yearLevel,
                subject,
                content,
                culturalElements: culturalWisdom,
                teachingApproach,
                timestamp: new Date().toISOString()
            };
        } catch (error) {
            console.error('Error generating teaching content:', error);
            return { error: error.message };
        }
    }

    /**
     * AI-POWERED CULTURAL INTELLIGENCE
     * Enhance cultural context understanding
     */
    async enhanceCulturalContext(resource) {
        try {
            const prompt = `
Analyze this educational resource through a Te Ao Māori lens and suggest cultural enhancements:

Resource: ${resource.title}
Content: ${resource.content_preview}

Please provide:
1. Relevant Māori cultural principles (from: Whanaungatanga, Manaakitanga, Kaitiakitanga, Rangatiratanga, Kotahitanga, Ako)
2. Suggested Whakataukī (Māori proverb) that connects to this content
3. Ways to integrate Te Ao Māori perspective
4. Cultural context that would enrich learning

Respond in JSON format with keys: principles, whakatauki, integration_suggestions, cultural_context
`;

            const response = await this.callGLM(prompt, { temperature: 0.7 });
            
            // Parse and integrate
            const culturalEnhancement = this.parseCulturalEnhancement(response);
            
            // Save back to GraphRAG
            await this.saveCulturalEnhancement(resource.file_path, culturalEnhancement);

            return culturalEnhancement;
        } catch (error) {
            console.error('Error enhancing cultural context:', error);
            return { error: error.message };
        }
    }

    /**
     * AI-POWERED GAP ANALYSIS
     * Identify content gaps and opportunities
     */
    async analyzeContentGaps() {
        try {
            // Query GraphRAG for resource distribution
            const supabase = this.masterIntelligence?.evolution?.supabase;
            if (!supabase) throw new Error('GraphRAG not available');

            const { data: stats } = await supabase
                .rpc('get_content_statistics');

            const prompt = `
As an educational content strategist for a New Zealand platform integrating Te Ao Māori values, analyze these content statistics and identify gaps:

${JSON.stringify(stats, null, 2)}

Platform values:
- Whanaungatanga (relationships)
- Manaakitanga (generosity)
- Kaitiakitanga (guardianship)
- Cultural integration
- Teaching variants (2-3 approaches per lesson)

Identify:
1. Year level gaps
2. Subject area needs
3. Cultural integration opportunities
4. Teaching variant expansion areas
5. High-priority content to create

Respond in JSON format with actionable recommendations.
`;

            const analysis = await this.callGLM(prompt, { temperature: 0.8 });

            return {
                stats,
                aiAnalysis: analysis,
                recommendations: this.parseGapAnalysis(analysis),
                timestamp: new Date().toISOString()
            };
        } catch (error) {
            console.error('Error in gap analysis:', error);
            return { error: error.message };
        }
    }

    /**
     * CALL GLM API
     */
    async callGLM(prompt, options = {}) {
        const {
            model = 'deepseek-chat',
            temperature = 0.7,
            maxTokens = 2000
        } = options;

        // Check cache
        const cacheKey = `${prompt.substring(0, 100)}_${model}_${temperature}`;
        if (this.requestCache.has(cacheKey)) {
            return this.requestCache.get(cacheKey);
        }

        try {
            const response = await fetch(this.apiEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${this.apiKey}`
                },
                body: JSON.stringify({
                    model: model,
                    messages: [
                        {
                            role: 'system',
                            content: 'You are an educational AI assistant specializing in New Zealand curriculum and Te Ao Māori (Māori worldview). You help create culturally responsive, engaging educational content.'
                        },
                        {
                            role: 'user',
                            content: prompt
                        }
                    ],
                    temperature: temperature,
                    max_tokens: maxTokens
                })
            });

            if (!response.ok) {
                throw new Error(`GLM API error: ${response.status}`);
            }

            const data = await response.json();
            const result = data.choices[0].message.content;

            // Cache result
            this.requestCache.set(cacheKey, result);

            return result;
        } catch (error) {
            console.error('GLM API call failed:', error);
            throw error;
        }
    }

    /**
     * BUILD RECOMMENDATION PROMPT
     */
    buildRecommendationPrompt(context, graphragRecs, userContext) {
        return `
As an educational recommendation AI for Te Kete Ako (New Zealand platform), analyze these GraphRAG recommendations and enhance them:

Current Resource: ${context.title}
GraphRAG Recommendations: ${JSON.stringify(graphragRecs.contextual.slice(0, 5), null, 2)}
User Context: ${JSON.stringify(userContext)}

Cultural Principles Available:
- Whanaungatanga (relationships/connections)
- Manaakitanga (generosity/hospitality)
- Kaitiakitanga (guardianship)
- Ako (reciprocal learning)

Please:
1. Explain WHY each recommendation is valuable
2. Suggest the BEST learning sequence
3. Add cultural connections
4. Identify which teaching approach (inquiry, collaborative, guided, project, experiential) suits each

Respond in JSON format with enhanced recommendations.
`;
    }

    /**
     * BUILD CONTENT GENERATION PROMPT
     */
    buildContentGenerationPrompt(topic, yearLevel, subject, culturalWisdom, variantTemplate) {
        return `
Create a complete lesson plan for New Zealand students:

Topic: ${topic}
Year Level: ${yearLevel}
Subject: ${subject}
Teaching Approach: ${variantTemplate?.name || 'Guided Learning'}

${culturalWisdom ? `Cultural Context:\n${JSON.stringify(culturalWisdom, null, 2)}\n` : ''}

${variantTemplate ? `Lesson Structure to follow:\n${JSON.stringify(variantTemplate.structure, null, 2)}\n` : ''}

Create a full lesson including:
1. Learning objectives (aligned with NZ Curriculum)
2. Hook/Engagement (use cultural context if provided)
3. Main teaching sequence
4. Activities (hands-on, engaging)
5. Assessment ideas
6. Differentiation strategies
7. Resources needed
8. Cultural integration (Te Ao Māori perspective)

Make it engaging, culturally responsive, and practical for teachers.

Respond in JSON format with all sections clearly structured.
`;
    }

    /**
     * GET GRAPHRAG CONTEXT
     */
    async getGraphRAGContext(path) {
        try {
            const supabase = this.masterIntelligence?.evolution?.supabase;
            if (!supabase) return { title: 'Unknown', content_preview: '' };

            const { data } = await supabase
                .from('graphrag_resources')
                .select('*')
                .eq('file_path', path)
                .single();

            return data || { title: 'Unknown', content_preview: '' };
        } catch (error) {
            return { title: 'Unknown', content_preview: '' };
        }
    }

    /**
     * GET CULTURAL WISDOM FOR TOPIC
     */
    async getCulturalWisdomForTopic(topic) {
        try {
            const supabase = this.masterIntelligence?.evolution?.supabase;
            if (!supabase) return null;

            const { data } = await supabase
                .from('graphrag_resources')
                .select('*')
                .or('metadata->>cultural.eq.true,metadata->>te_ao_maori.eq.true')
                .ilike('title', `%${topic}%`)
                .limit(3);

            return data || [];
        } catch (error) {
            return null;
        }
    }

    /**
     * COMBINE RECOMMENDATIONS
     */
    combineRecommendations(graphragRecs, aiResponse) {
        try {
            const aiEnhanced = JSON.parse(aiResponse);
            
            return graphragRecs.contextual.map((rec, index) => ({
                ...rec,
                aiReasoning: aiEnhanced[index]?.reasoning || 'AI enhancement pending',
                learningSequence: aiEnhanced[index]?.sequence || index + 1,
                culturalConnection: aiEnhanced[index]?.cultural || null,
                suggestedApproach: aiEnhanced[index]?.approach || 'guided'
            }));
        } catch (error) {
            return graphragRecs.contextual;
        }
    }

    /**
     * PARSE CULTURAL ENHANCEMENT
     */
    parseCulturalEnhancement(response) {
        try {
            return JSON.parse(response);
        } catch (error) {
            return {
                principles: [],
                whakatauki: null,
                integration_suggestions: [],
                cultural_context: response
            };
        }
    }

    /**
     * PARSE GAP ANALYSIS
     */
    parseGapAnalysis(response) {
        try {
            return JSON.parse(response);
        } catch (error) {
            return { raw: response };
        }
    }

    /**
     * SAVE GENERATED CONTENT TO GRAPHRAG
     */
    async saveGeneratedContent(topic, content, options) {
        try {
            const supabase = this.masterIntelligence?.evolution?.supabase;
            if (!supabase) return { success: false };

            const { data, error } = await supabase
                .from('graphrag_resources')
                .insert({
                    file_path: `_ai_generated/${topic.toLowerCase().replace(/\s+/g, '-')}`,
                    title: `AI Generated: ${topic}`,
                    content_preview: typeof content === 'string' ? content.substring(0, 500) : JSON.stringify(content).substring(0, 500),
                    metadata: {
                        type: 'ai_generated_lesson',
                        generated_by: 'GLM',
                        year_level: options.yearLevel,
                        subject: options.subject,
                        teaching_approach: options.teachingApproach,
                        cultural: options.culturalContext,
                        generated_date: new Date().toISOString()
                    },
                    quality_score: 80 // Start at 80, can be reviewed
                })
                .select();

            return { success: !error, data, error };
        } catch (error) {
            console.error('Error saving generated content:', error);
            return { success: false, error };
        }
    }

    /**
     * SAVE CULTURAL ENHANCEMENT
     */
    async saveCulturalEnhancement(filePath, enhancement) {
        try {
            const supabase = this.masterIntelligence?.evolution?.supabase;
            if (!supabase) return { success: false };

            const { data, error } = await supabase
                .from('graphrag_resources')
                .update({
                    metadata: {
                        cultural: true,
                        te_ao_maori: true,
                        ai_enhanced_cultural: true,
                        cultural_principles: enhancement.principles,
                        whakatauki: enhancement.whakatauki,
                        cultural_integration: enhancement.integration_suggestions
                    }
                })
                .eq('file_path', filePath)
                .select();

            return { success: !error, data, error };
        } catch (error) {
            console.error('Error saving cultural enhancement:', error);
            return { success: false, error };
        }
    }

    /**
     * CLEAR CACHE
     */
    clearCache() {
        this.requestCache.clear();
    }

    /**
     * GET STATS
     */
    getStats() {
        return {
            cacheSize: this.requestCache.size,
            apiKey: this.apiKey ? '✅ Configured' : '❌ Missing',
            masterIntelligence: this.masterIntelligence ? '✅ Connected' : '❌ Disconnected',
            culturalIntelligence: this.culturalIntelligence ? '✅ Connected' : '❌ Disconnected'
        };
    }
}

// Auto-initialize and expose globally
window.GLMGraphRAG = new GLMGraphRAGIntegration();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = GLMGraphRAGIntegration;
}


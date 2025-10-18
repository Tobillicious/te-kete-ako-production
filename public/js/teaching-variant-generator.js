/**
 * Teaching Variant Generator - Te Kete Ako
 * Intelligently generates teaching variants using GraphRAG + Cultural Intelligence
 * Creates 2-3 pedagogical approaches for each lesson
 */

class TeachingVariantGenerator {
    constructor() {
        this.masterIntelligence = null;
        this.culturalIntelligence = null;
        this.variantTemplates = new Map();
        this.init();
    }

    async init() {
        await this.waitForIntelligence();
        this.defineVariantTemplates();
        console.log('🎓 Teaching Variant Generator Ready');
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
     * DEFINE VARIANT TEMPLATES
     * Based on pedagogical approaches and cultural principles
     */
    defineVariantTemplates() {
        // Inquiry-Based Learning (Rangatiratanga - Self-determination)
        this.variantTemplates.set('inquiry', {
            name: 'Inquiry-Based Learning',
            principle: 'Rangatiratanga',
            icon: '🔍',
            description: 'Students lead their own learning through questions and discovery',
            structure: {
                hook: 'Provoke curiosity with open-ended question',
                explore: 'Student-led investigation and research',
                develop: 'Collaborative meaning-making',
                apply: 'Create solutions to authentic problems',
                reflect: 'Share discoveries and insights'
            },
            strengths: ['Student autonomy', 'Deep understanding', 'Critical thinking'],
            culturalAlignment: 'Honors student leadership and self-determination'
        });

        // Collaborative Learning (Whanaungatanga - Relationships)
        this.variantTemplates.set('collaborative', {
            name: 'Collaborative Learning',
            principle: 'Whanaungatanga',
            icon: '🤝',
            description: 'Learning through relationships and group work',
            structure: {
                hook: 'Community-building activity',
                explore: 'Small group investigation',
                develop: 'Peer teaching and shared knowledge building',
                apply: 'Collective project or presentation',
                reflect: 'Group reflection and celebration'
            },
            strengths: ['Social learning', 'Peer support', 'Communication skills'],
            culturalAlignment: 'Builds whanaungatanga and collective success'
        });

        // Direct Instruction with Cultural Context (Ako - Reciprocal learning)
        this.variantTemplates.set('guided', {
            name: 'Guided Learning with Cultural Context',
            principle: 'Ako',
            icon: '📚',
            description: 'Teacher-guided instruction with reciprocal learning moments',
            structure: {
                hook: 'Cultural story or Whakataukī',
                explore: 'Teacher modeling and explanation',
                develop: 'Guided practice with teacher support',
                apply: 'Independent practice with choice',
                reflect: 'Student teaching back (reciprocal Ako)'
            },
            strengths: ['Clear structure', 'Scaffolded support', 'Cultural grounding'],
            culturalAlignment: 'Honors reciprocal teaching and learning relationship'
        });

        // Project-Based Learning (Kotahitanga - Unity)
        this.variantTemplates.set('project', {
            name: 'Project-Based Learning',
            principle: 'Kotahitanga',
            icon: '🎯',
            description: 'Extended projects that integrate multiple skills and knowledge',
            structure: {
                hook: 'Real-world challenge or community need',
                explore: 'Research and planning phase',
                develop: 'Iterative creation and refinement',
                apply: 'Final product or presentation to authentic audience',
                reflect: 'Impact assessment and celebration'
            },
            strengths: ['Authentic learning', 'Integration', 'Long-term engagement'],
            culturalAlignment: 'Builds unity through shared purpose and community impact'
        });

        // Experiential Learning (Manaakitanga - Generosity of experience)
        this.variantTemplates.set('experiential', {
            name: 'Experiential Learning',
            principle: 'Manaakitanga',
            icon: '🌟',
            description: 'Learning through direct experience and reflection',
            structure: {
                hook: 'Immersive experience or simulation',
                explore: 'Active participation and observation',
                develop: 'Debrief and connect to concepts',
                apply: 'Transfer learning to new contexts',
                reflect: 'Personal meaning-making'
            },
            strengths: ['Memorable', 'Embodied learning', 'Personal connection'],
            culturalAlignment: 'Generously provides rich experiences for all learners'
        });
    }

    /**
     * GENERATE VARIANTS FOR LESSON
     * Uses GraphRAG to analyze lesson and suggest best variants
     */
    async generateVariantsForLesson(lessonPath) {
        try {
            // Get lesson data from GraphRAG
            const supabase = this.masterIntelligence?.evolution?.supabase;
            if (!supabase) return { error: 'GraphRAG not available' };

            const { data: lesson } = await supabase
                .from('graphrag_resources')
                .select('*')
                .eq('file_path', lessonPath)
                .single();

            if (!lesson) return { error: 'Lesson not found' };

            // Analyze lesson characteristics
            const analysis = this.analyzeLessonCharacteristics(lesson);

            // Select best 2-3 variant templates
            const selectedVariants = this.selectOptimalVariants(analysis);

            // Generate full variants
            const variants = selectedVariants.map(template => 
                this.generateFullVariant(lesson, template, analysis)
            );

            return {
                lesson: lesson.title,
                analysis,
                variants,
                culturalContext: this.getCulturalContext(lesson),
                whakatauki: this.culturalIntelligence?.getContextualWhakatauki({
                    subject: lesson.metadata?.subject,
                    yearLevel: lesson.metadata?.year_level
                })
            };
        } catch (error) {
            console.error('Error generating variants:', error);
            return { error: error.message };
        }
    }

    /**
     * ANALYZE LESSON CHARACTERISTICS
     */
    analyzeLessonCharacteristics(lesson) {
        const analysis = {
            yearLevel: lesson.metadata?.year_level || 'Unknown',
            subject: lesson.metadata?.subject || 'Unknown',
            complexity: this.assessComplexity(lesson),
            socialLearningPotential: this.assessSocialPotential(lesson),
            culturalElements: this.identifyCulturalElements(lesson),
            suggestedVariants: []
        };

        // Recommend variants based on characteristics
        if (analysis.socialLearningPotential === 'high') {
            analysis.suggestedVariants.push('collaborative');
        }
        if (analysis.complexity === 'high') {
            analysis.suggestedVariants.push('inquiry');
        }
        if (analysis.culturalElements.length > 0) {
            analysis.suggestedVariants.push('guided');
        }
        
        // Always offer project-based as an option
        if (analysis.suggestedVariants.length < 3) {
            analysis.suggestedVariants.push('project');
        }

        // Ensure we have exactly 2-3 variants
        return {
            ...analysis,
            suggestedVariants: analysis.suggestedVariants.slice(0, 3)
        };
    }

    /**
     * ASSESS COMPLEXITY
     */
    assessComplexity(lesson) {
        const content = lesson.content_preview?.toLowerCase() || '';
        const title = lesson.title?.toLowerCase() || '';
        
        const complexityIndicators = [
            'critical thinking', 'analyze', 'evaluate', 'synthesize',
            'advanced', 'complex', 'multiple perspectives'
        ];

        const matches = complexityIndicators.filter(indicator => 
            content.includes(indicator) || title.includes(indicator)
        );

        if (matches.length >= 3) return 'high';
        if (matches.length >= 1) return 'medium';
        return 'low';
    }

    /**
     * ASSESS SOCIAL LEARNING POTENTIAL
     */
    assessSocialPotential(lesson) {
        const content = lesson.content_preview?.toLowerCase() || '';
        
        const socialIndicators = [
            'discuss', 'collaborate', 'group', 'team', 'share',
            'peer', 'together', 'community'
        ];

        const matches = socialIndicators.filter(indicator => content.includes(indicator));

        if (matches.length >= 3) return 'high';
        if (matches.length >= 1) return 'medium';
        return 'low';
    }

    /**
     * IDENTIFY CULTURAL ELEMENTS
     */
    identifyCulturalElements(lesson) {
        const elements = [];
        
        if (lesson.metadata?.cultural) elements.push('Cultural context');
        if (lesson.metadata?.te_ao_maori) elements.push('Te Ao Māori');
        if (lesson.metadata?.whakatauki) elements.push('Whakataukī');
        if (lesson.metadata?.maori_language) elements.push('Te Reo Māori');

        return elements;
    }

    /**
     * SELECT OPTIMAL VARIANTS
     */
    selectOptimalVariants(analysis) {
        const variants = [];

        for (const variantKey of analysis.suggestedVariants) {
            const template = this.variantTemplates.get(variantKey);
            if (template) {
                variants.push(template);
            }
        }

        // Ensure we have at least 2 variants
        if (variants.length < 2) {
            const allTemplates = Array.from(this.variantTemplates.values());
            while (variants.length < 2 && allTemplates.length > 0) {
                const random = allTemplates[Math.floor(Math.random() * allTemplates.length)];
                if (!variants.includes(random)) {
                    variants.push(random);
                }
            }
        }

        return variants;
    }

    /**
     * GENERATE FULL VARIANT
     */
    generateFullVariant(lesson, template, analysis) {
        return {
            id: `${lesson.file_path}-${template.name.toLowerCase().replace(/\s+/g, '-')}`,
            name: template.name,
            principle: template.principle,
            icon: template.icon,
            description: template.description,
            lessonStructure: template.structure,
            adaptedForLesson: {
                hook: this.adaptPhase('hook', lesson, template),
                explore: this.adaptPhase('explore', lesson, template),
                develop: this.adaptPhase('develop', lesson, template),
                apply: this.adaptPhase('apply', lesson, template),
                reflect: this.adaptPhase('reflect', lesson, template)
            },
            strengths: template.strengths,
            culturalAlignment: template.culturalAlignment,
            bestFor: this.identifyBestFor(template, analysis),
            materials: this.suggestMaterials(template, lesson),
            timing: this.suggestTiming(template, analysis.yearLevel)
        };
    }

    /**
     * ADAPT PHASE FOR SPECIFIC LESSON
     */
    adaptPhase(phase, lesson, template) {
        const lessonTitle = lesson.title || 'this lesson';
        const subject = lesson.metadata?.subject || 'the topic';
        
        return template.structure[phase]
            .replace(/students?/gi, 'students')
            .replace(/topic/gi, subject)
            .replace(/lesson/gi, lessonTitle);
    }

    /**
     * IDENTIFY BEST FOR
     */
    identifyBestFor(template, analysis) {
        const bestFor = [];
        
        if (template.name.includes('Inquiry') && analysis.complexity === 'high') {
            bestFor.push('Students who love asking questions');
        }
        if (template.name.includes('Collaborative')) {
            bestFor.push('Students who thrive in groups');
        }
        if (template.name.includes('Guided')) {
            bestFor.push('Students who prefer clear structure');
        }
        if (template.name.includes('Project')) {
            bestFor.push('Students who like creating tangible outcomes');
        }
        if (template.name.includes('Experiential')) {
            bestFor.push('Kinesthetic learners');
        }

        return bestFor;
    }

    /**
     * SUGGEST MATERIALS
     */
    suggestMaterials(template, lesson) {
        const materials = ['Lesson content', 'Student devices or worksheets'];
        
        if (template.name.includes('Collaborative')) {
            materials.push('Group work spaces', 'Collaboration tools');
        }
        if (template.name.includes('Project')) {
            materials.push('Project materials', 'Presentation tools');
        }
        if (template.name.includes('Experiential')) {
            materials.push('Hands-on materials', 'Simulation resources');
        }

        return materials;
    }

    /**
     * SUGGEST TIMING
     */
    suggestTiming(template, yearLevel) {
        const baseTime = 45; // minutes
        
        if (template.name.includes('Project')) {
            return '2-4 lessons (extended)';
        }
        if (template.name.includes('Inquiry')) {
            return '60-90 minutes';
        }
        
        return `${baseTime}-${baseTime + 15} minutes`;
    }

    /**
     * GET CULTURAL CONTEXT
     */
    getCulturalContext(lesson) {
        if (!this.culturalIntelligence) return null;

        const principle = this.culturalIntelligence.identifyCulturalPrinciple(lesson);
        return principle;
    }

    /**
     * SAVE VARIANTS TO GRAPHRAG
     */
    async saveVariantsToGraphRAG(lessonPath, variants) {
        try {
            const supabase = this.masterIntelligence?.evolution?.supabase;
            if (!supabase) return { success: false };

            const { data, error } = await supabase
                .from('graphrag_resources')
                .update({
                    metadata: {
                        teaching_variants: true,
                        variant_count: variants.length,
                        variants: variants.map(v => ({
                            name: v.name,
                            principle: v.principle,
                            id: v.id
                        }))
                    }
                })
                .eq('file_path', lessonPath)
                .select();

            if (!error) {
                console.log('🎓 Teaching variants saved for:', lessonPath);
                return { success: true, data };
            }

            return { success: false, error };
        } catch (error) {
            console.error('Error saving variants:', error);
            return { success: false, error };
        }
    }
}

// Auto-initialize and expose globally
window.TeachingVariantGenerator = new TeachingVariantGenerator();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = TeachingVariantGenerator;
}

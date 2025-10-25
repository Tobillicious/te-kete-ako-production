/**
 * TEACHING VARIANTS SYNTHESIZER - Te Kete Ako
 * Intelligently synthesizes duplicate lessons into 2-3 pedagogical options
 * Gives real kaiako choice while maintaining clean organization
 */

class TeachingVariantsSynthesizer {
    constructor() {
        this.variants = new Map();
        this.synthesisRules = {
            maxVariants: 3,
            minQualityScore: 75,
            preferredTypes: ['recommended', 'alternative', 'advanced']
        };
    }

    /**
     * Analyze duplicate lessons and synthesize into teaching variants
     * @param {Array} duplicateLessons - Array of similar lessons from GraphRAG
     * @returns {Object} Synthesized teaching variants
     */
    synthesizeVariants(duplicateLessons) {
        if (!duplicateLessons || duplicateLessons.length === 0) {
            return { variants: [], message: 'No duplicate lessons found' };
        }

        // Filter by quality and sort
        const qualityLessons = duplicateLessons
            .filter(lesson => lesson.quality_score >= this.synthesisRules.minQualityScore)
            .sort((a, b) => b.quality_score - a.quality_score);

        if (qualityLessons.length === 0) {
            return { variants: [], message: 'No high-quality lessons found' };
        }

        // Synthesize into 2-3 distinct pedagogical approaches
        const synthesized = this.createPedagogicalVariants(qualityLessons);
        
        return {
            variants: synthesized,
            originalCount: duplicateLessons.length,
            synthesizedCount: synthesized.length,
            reductionPercent: Math.round((1 - synthesized.length / duplicateLessons.length) * 100)
        };
    }

    /**
     * Create pedagogical variants from duplicate lessons
     * @param {Array} lessons - Quality-filtered lessons
     * @returns {Array} Synthesized variants
     */
    createPedagogicalVariants(lessons) {
        const variants = [];
        
        // Strategy 1: Find the highest quality lesson as "Recommended"
        const topLesson = lessons[0];
        variants.push(this.createVariant(topLesson, 'recommended', 'Enhanced Gold Standard'));

        // Strategy 2: Find a different pedagogical approach as "Alternative"
        const alternativeLesson = this.findAlternativeApproach(lessons, topLesson);
        if (alternativeLesson) {
            variants.push(this.createVariant(alternativeLesson, 'alternative', 'Legacy CSS Variant'));
        }

        // Strategy 3: Find an advanced/optimized version as "Advanced"
        const advancedLesson = this.findAdvancedVersion(lessons);
        if (advancedLesson && variants.length < this.synthesisRules.maxVariants) {
            variants.push(this.createVariant(advancedLesson, 'advanced', 'Production Optimized'));
        }

        return variants;
    }

    /**
     * Create a teaching variant from a lesson
     * @param {Object} lesson - Lesson object
     * @param {String} type - Variant type (recommended, alternative, advanced)
     * @param {String} title - Display title
     * @returns {Object} Teaching variant
     */
    createVariant(lesson, type, title) {
        return {
            id: `variant-${lesson.id || Date.now()}`,
            title: title,
            description: this.generateDescription(lesson, type),
            type: type,
            features: this.extractFeatures(lesson, type),
            duration: this.calculateDuration(lesson),
            difficulty: this.assessDifficulty(lesson),
            primaryAction: {
                text: 'Use This Version',
                url: lesson.file_path || '#'
            },
            secondaryAction: {
                text: 'Preview',
                url: this.generatePreviewUrl(lesson)
            },
            originalLesson: lesson
        };
    }

    /**
     * Find alternative pedagogical approach
     * @param {Array} lessons - All lessons
     * @param {Object} topLesson - Top quality lesson
     * @returns {Object|null} Alternative lesson
     */
    findAlternativeApproach(lessons, topLesson) {
        // Look for lessons with different CSS systems, teaching methods, or cultural approaches
        return lessons.find(lesson => 
            lesson.id !== topLesson.id && (
                lesson.file_path.includes('legacy') ||
                lesson.file_path.includes('traditional') ||
                lesson.metadata?.teaching_method !== topLesson.metadata?.teaching_method ||
                lesson.cultural_context !== topLesson.cultural_context
            )
        ) || lessons[1]; // Fallback to second best
    }

    /**
     * Find advanced/optimized version
     * @param {Array} lessons - All lessons
     * @returns {Object|null} Advanced lesson
     */
    findAdvancedVersion(lessons) {
        return lessons.find(lesson => 
            lesson.file_path.includes('optimized') ||
            lesson.file_path.includes('production') ||
            lesson.file_path.includes('enhanced') ||
            lesson.metadata?.optimization_level === 'high'
        ) || lessons[2]; // Fallback to third best
    }

    /**
     * Generate description based on lesson and type
     * @param {Object} lesson - Lesson object
     * @param {String} type - Variant type
     * @returns {String} Description
     */
    generateDescription(lesson, type) {
        const descriptions = {
            'recommended': `Comprehensive lesson with full cultural integration, multimedia resources, and assessment rubrics. Quality score: ${lesson.quality_score}`,
            'alternative': `Traditional teaching approach with proven methods and simplified cultural elements. Quality score: ${lesson.quality_score}`,
            'advanced': `Streamlined version optimized for digital delivery with minimal setup requirements. Quality score: ${lesson.quality_score}`
        };
        
        return descriptions[type] || `High-quality lesson variant. Quality score: ${lesson.quality_score}`;
    }

    /**
     * Extract features from lesson
     * @param {Object} lesson - Lesson object
     * @param {String} type - Variant type
     * @returns {Array} Feature list
     */
    extractFeatures(lesson, type) {
        const baseFeatures = [];
        
        // Cultural integration
        if (lesson.has_whakataukī || lesson.cultural_context) {
            baseFeatures.push('Māori cultural integration');
        }
        
        // Quality indicators
        if (lesson.quality_score >= 90) {
            baseFeatures.push('Premium quality content');
        }
        
        // Type-specific features
        switch (type) {
            case 'recommended':
                baseFeatures.push('Full multimedia resources', 'Assessment rubrics included', 'Differentiated learning paths');
                break;
            case 'alternative':
                baseFeatures.push('Traditional teaching methods', 'Proven assessment strategies', 'Quick implementation');
                break;
            case 'advanced':
                baseFeatures.push('Digital-first design', 'Minimal setup required', 'Auto-grading capabilities');
                break;
        }
        
        return baseFeatures;
    }

    /**
     * Calculate lesson duration
     * @param {Object} lesson - Lesson object
     * @returns {String} Duration
     */
    calculateDuration(lesson) {
        // Extract duration from metadata or estimate based on content
        if (lesson.metadata?.duration) {
            return lesson.metadata.duration;
        }
        
        // Estimate based on quality score (higher quality = more comprehensive)
        if (lesson.quality_score >= 90) return '60 min';
        if (lesson.quality_score >= 80) return '45 min';
        return '30 min';
    }

    /**
     * Assess lesson difficulty
     * @param {Object} lesson - Lesson object
     * @returns {String} Difficulty level
     */
    assessDifficulty(lesson) {
        if (lesson.year_level?.includes('13') || lesson.year_level?.includes('12')) return 'Hard';
        if (lesson.year_level?.includes('9') || lesson.year_level?.includes('10')) return 'Medium';
        return 'Easy';
    }

    /**
     * Generate preview URL
     * @param {Object} lesson - Lesson object
     * @returns {String} Preview URL
     */
    generatePreviewUrl(lesson) {
        const basePath = lesson.file_path?.replace('.html', '') || '#';
        return `/preview${basePath}`;
    }

    /**
     * Load variants from GraphRAG for a specific lesson
     * @param {String} lessonId - Lesson identifier
     * @returns {Promise<Array>} Teaching variants
     */
    async loadVariantsFromGraphRAG(lessonId) {
        try {
            // Query GraphRAG for similar lessons
            const response = await fetch('/api/graphrag/similar-lessons', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ lessonId, similarityThreshold: 0.8 })
            });
            
            const similarLessons = await response.json();
            return this.synthesizeVariants(similarLessons);
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        console.log('Issue detected: $2');
            return { variants: [], error: error.message };
        }
    }

    /**
     * Track teacher preferences for future synthesis
     * @param {String} variantId - Selected variant ID
     * @param {String} lessonId - Original lesson ID
     * @param {String} teacherId - Teacher identifier
     */
    async trackTeacherPreference(variantId, lessonId, teacherId) {
        try {
            await fetch('/api/graphrag/teacher-preferences', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    variantId,
                    lessonId,
                    teacherId,
                    timestamp: new Date().toISOString()
                })
            });
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        console.log('Issue detected: $2');
        }
    }
}

// Export for use in other components
window.TeachingVariantsSynthesizer = TeachingVariantsSynthesizer;

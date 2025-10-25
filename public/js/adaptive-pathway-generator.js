/**
 * Adaptive Pathway Generator - Te Kete Ako
 * Uses GraphRAG relationships to build personalized learning journeys
 * Creates Netflix-style adaptive pathways through 19,696 resources
 */

class AdaptivePathwayGenerator {
    constructor() {
        this.supabase = null;
        this.culturalIntelligence = null;
        this.pathwayCache = new Map();
        this.init();
    }

    async init() {
        await this.waitForDependencies();
    }

    async waitForDependencies() {
        const maxWait = 15000;
        const checkInterval = 500;
        let waited = 0;

        while (waited < maxWait) {
            if (window.supabaseSingleton && window.CulturalIntelligence) {
                this.supabase = await window.supabaseSingleton.getClient();
                this.culturalIntelligence = window.CulturalIntelligence;
                break;
            }
            
            await new Promise(resolve => setTimeout(resolve, checkInterval));
            waited += checkInterval;
        }
    }

    /**
     * GENERATE LEARNING PATHWAY
     * Build personalized path from concept A to concept B
     */
    async generatePathway(startResource, endResource, userPreferences = {}) {
        const cacheKey = `${startResource}_${endResource}_${JSON.stringify(userPreferences)}`;
        
        if (this.pathwayCache.has(cacheKey)) {
            return this.pathwayCache.get(cacheKey);
        }

        try {
            const pathway = {
                start: startResource,
                end: endResource,
                userPreferences,
                steps: [],
                totalSteps: 0,
                estimatedTime: 0,
                culturalIntegration: null,
                teachingVariants: []
            };

            // Find path using BFS-like approach through relationships
            const path = await this.findOptimalPath(startResource, endResource, userPreferences);
            
            if (!path || path.length === 0) {
                return { error: 'No path found between these resources' };
            }

            // Enhance each step with intelligence
            pathway.steps = await Promise.all(
                path.map(step => this.enhancePathStep(step, userPreferences))
            );

            pathway.totalSteps = pathway.steps.length;
            pathway.estimatedTime = this.calculateEstimatedTime(pathway.steps);
            pathway.culturalIntegration = await this.addCulturalContext(pathway.steps);
            pathway.teachingVariants = this.suggestTeachingVariants(pathway.steps);

            this.pathwayCache.set(cacheKey, pathway);
            return pathway;

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
            return { error: error.message };
        }
    }

    /**
     * FIND OPTIMAL PATH
     * BFS-like search through relationship graph
     */
    async findOptimalPath(start, end, preferences) {
        try {
            // Simple path finding using relationships
            const visited = new Set();
            const queue = [[start]];
            const maxDepth = 5;

            while (queue.length > 0) {
                const path = queue.shift();
                const current = path[path.length - 1];

                if (path.length > maxDepth) continue;
                if (current === end) return path;
                if (visited.has(current)) continue;

                visited.add(current);

                // Get next steps from relationships
                const { data: nextSteps } = await this.supabase
                    .from('graphrag_relationships')
                    .select('target_path, confidence, relationship_type')
                    .eq('source_path', current)
                    .gte('confidence', 0.75)
                    .order('confidence', { ascending: false })
                    .limit(5);

                if (nextSteps) {
                    for (const step of nextSteps) {
                        if (!visited.has(step.target_path)) {
                            queue.push([...path, step.target_path]);
                        }
                    }
                }
            }

            // No direct path found - create scaffolded path
            return await this.createScaffoldedPath(start, end, preferences);

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
            return [];
        }
    }

    /**
     * CREATE SCAFFOLDED PATH
     * When no direct path exists, build intelligent progression
     */
    async createScaffoldedPath(start, end, preferences) {
        try {
            const { data: startRes } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('file_path', start)
                .single();

            const { data: endRes } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('file_path', end)
                .single();

            if (!startRes || !endRes) return [start, end];

            // Find intermediate resources
            const intermediate = await this.findIntermediateResources(
                startRes, 
                endRes, 
                preferences
            );

            return [start, ...intermediate.map(r => r.file_path), end];

        } catch (error) {
            return [start, end];
        }
    }

    /**
     * FIND INTERMEDIATE RESOURCES
     * Fill gaps in learning progression
     */
    async findIntermediateResources(start, end, preferences) {
        try {
            // Find resources in same subject with progressive difficulty
            const { data: candidates } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('metadata->>subject', start.metadata?.subject || end.metadata?.subject)
                .gte('quality_score', 80)
                .order('quality_score', { ascending: false })
                .limit(10);

            if (!candidates) return [];

            // Select 2-3 intermediate steps
            return candidates.slice(0, 3);

        } catch (error) {
            return [];
        }
    }

    /**
     * ENHANCE PATH STEP
     * Add intelligence to each step
     */
    async enhancePathStep(resourcePath, preferences) {
        try {
            const { data: resource } = await this.supabase
                .from('graphrag_resources')
                .select('*')
                .eq('file_path', resourcePath)
                .single();

            if (!resource) return { path: resourcePath, error: 'Not found' };

            return {
                path: resourcePath,
                title: resource.title,
                type: resource.metadata?.type,
                subject: resource.metadata?.subject,
                quality: resource.quality_score,
                estimatedMinutes: this.estimateTimeForResource(resource),
                culturalElements: this.identifyCulturalElements(resource),
                teachingApproach: this.suggestTeachingApproach(resource, preferences),
                prerequisites: await this.getPrerequisites(resourcePath),
                nextSteps: await this.getNextSteps(resourcePath)
            };

        } catch (error) {
            return { path: resourcePath, error: error.message };
        }
    }

    /**
     * ESTIMATE TIME FOR RESOURCE
     */
    estimateTimeForResource(resource) {
        const type = resource.metadata?.type;
        const baseMinutes = {
            'lesson': 45,
            'unit': 180,
            'handout': 15,
            'activity': 30,
            'assessment': 60
        };
        return baseMinutes[type] || 30;
    }

    /**
     * IDENTIFY CULTURAL ELEMENTS
     */
    identifyCulturalElements(resource) {
        const elements = [];
        if (resource.metadata?.cultural) elements.push('Cultural context');
        if (resource.metadata?.te_ao_maori) elements.push('Te Ao Māori');
        if (resource.metadata?.whakatauki) elements.push('Whakataukī');
        return elements;
    }

    /**
     * SUGGEST TEACHING APPROACH
     */
    suggestTeachingApproach(resource, preferences) {
        if (preferences.teachingStyle) return preferences.teachingStyle;
        
        const type = resource.metadata?.type;
        if (type === 'lesson') return 'guided';
        if (type === 'activity') return 'collaborative';
        if (type === 'assessment') return 'independent';
        return 'flexible';
    }

    /**
     * GET PREREQUISITES
     */
    async getPrerequisites(resourcePath) {
        try {
            const { data } = await this.supabase
                .from('graphrag_relationships')
                .select('source_path, confidence')
                .eq('target_path', resourcePath)
                .eq('relationship_type', 'prerequisite')
                .order('confidence', { ascending: false })
                .limit(3);

            return data?.map(r => r.source_path) || [];
        } catch (error) {
            return [];
        }
    }

    /**
     * GET NEXT STEPS
     */
    async getNextSteps(resourcePath) {
        try {
            const { data } = await this.supabase
                .from('graphrag_relationships')
                .select('target_path, confidence')
                .eq('source_path', resourcePath)
                .gte('confidence', 0.80)
                .order('confidence', { ascending: false })
                .limit(3);

            return data?.map(r => r.target_path) || [];
        } catch (error) {
            return [];
        }
    }

    /**
     * CALCULATE ESTIMATED TIME
     */
    calculateEstimatedTime(steps) {
        const totalMinutes = steps.reduce((sum, step) => sum + (step.estimatedMinutes || 30), 0);
        const hours = Math.floor(totalMinutes / 60);
        const minutes = totalMinutes % 60;
        
        if (hours > 0) {
            return `${hours}h ${minutes}m`;
        }
        return `${minutes}m`;
    }

    /**
     * ADD CULTURAL CONTEXT
     */
    async addCulturalContext(steps) {
        const culturalSteps = steps.filter(s => s.culturalElements && s.culturalElements.length > 0);
        
        if (culturalSteps.length === 0) return null;

        return {
            culturalStepsCount: culturalSteps.length,
            percentage: ((culturalSteps.length / steps.length) * 100).toFixed(1),
            whakatauki: this.culturalIntelligence?.getContextualWhakatauki({ 
                context: 'learning_pathway' 
            })
        };
    }

    /**
     * SUGGEST TEACHING VARIANTS
     */
    suggestTeachingVariants(steps) {
        const lessonSteps = steps.filter(s => s.type === 'lesson');
        
        return lessonSteps.map(step => ({
            resource: step.path,
            suggestedApproach: step.teachingApproach,
            alternatives: ['inquiry', 'collaborative', 'guided'].filter(a => a !== step.teachingApproach)
        }));
    }

    /**
     * SAVE PATHWAY TO USER
     * Store custom pathway for teacher
     */
    async savePathway(pathway, teacherId) {
        try {
            const { data, error } = await this.supabase
                .from('teacher_learning_pathways')
                .insert({
                    teacher_id: teacherId,
                    pathway_data: pathway,
                    created_at: new Date().toISOString()
                })
                .select();

            return { success: !error, data, error };
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
            return { success: false, error };
        }
    }
}

// Auto-initialize and expose globally
window.AdaptivePathway = new AdaptivePathwayGenerator();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AdaptivePathwayGenerator;
}


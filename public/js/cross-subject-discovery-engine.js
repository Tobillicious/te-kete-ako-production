/**
 * Cross-Subject Discovery Engine - Te Kete Ako
 * Finds unexpected connections between subjects
 * Breaks down silos and enables interdisciplinary learning
 */

class CrossSubjectDiscoveryEngine {
    constructor() {
        this.supabase = null;
        this.culturalIntelligence = null;
        this.discoveryCache = new Map();
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
            if (window.supabase && window.ENV && window.CulturalIntelligence) {
                if (window.supabaseSingleton) {
                    this.supabase = await window.supabaseSingleton.getClient();
                }
                this.culturalIntelligence = window.CulturalIntelligence;
                break;
            }
            
            await new Promise(resolve => setTimeout(resolve, checkInterval));
            waited += checkInterval;
        }
    }

    /**
     * DISCOVER INTERDISCIPLINARY CONNECTIONS
     * Find where subjects naturally intersect
     */
    async discoverInterdisciplinaryConnections(primarySubject) {
        const cacheKey = `interdisciplinary_${primarySubject}`;
        
        if (this.discoveryCache.has(cacheKey)) {
            return this.discoveryCache.get(cacheKey);
        }

        try {
            const connections = {
                primarySubject,
                discoveries: [],
                culturalThreads: [],
                realWorldApplications: []
            };

            // Strategy 1: Concept overlap
            const conceptConnections = await this.findConceptOverlap(primarySubject);
            connections.discoveries.push(...conceptConnections);

            // Strategy 2: Cultural threading
            const culturalConnections = await this.findCulturalThreads(primarySubject);
            connections.culturalThreads = culturalConnections;

            // Strategy 3: Real-world applications
            const realWorld = await this.findRealWorldBridges(primarySubject);
            connections.realWorldApplications = realWorld;

            this.discoveryCache.set(cacheKey, connections);
            return connections;

        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        return { error: error.message };
        }
    }

    /**
     * FIND CONCEPT OVERLAP
     * Where do different subjects teach the same concepts?
     */
    async findConceptOverlap(primarySubject) {
        try {
            // Get resources from primary subject
            const { data: primary } = await this.supabase
                .from('graphrag_resources')
                .select('file_path, title, content_preview, metadata')
                .eq('metadata->>subject', primarySubject)
                .gte('quality_score', 80)
                .limit(20);

            if (!primary) return [];

            const overlaps = [];

            // For each primary resource, find concepts in other subjects
            for (const resource of primary) {
                const concepts = this.extractConcepts(resource.content_preview || resource.title);
                
                // Search for these concepts in other subjects
                for (const concept of concepts) {
                    const { data: matches } = await this.supabase
                        .from('graphrag_resources')
                        .select('file_path, title, metadata')
                        .neq('metadata->>subject', primarySubject)
                        .or(`title.ilike.%${concept}%,content_preview.ilike.%${concept}%`)
                        .gte('quality_score', 80)
                        .limit(3);

                    if (matches && matches.length > 0) {
                        overlaps.push({
                            concept,
                            primaryResource: resource.file_path,
                            connectsTo: matches.map(m => ({
                                path: m.file_path,
                                title: m.title,
                                subject: m.metadata?.subject,
                                reason: `Both teach: ${concept}`
                            })),
                            bridgeStrength: 0.85,
                            type: 'concept_overlap'
                        });
                    }
                }
            }

            return overlaps.slice(0, 10); // Top 10 discoveries

        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        return [];
        }
    }

    /**
     * FIND CULTURAL THREADS
     * Trace Te Ao Māori principles across subjects
     */
    async findCulturalThreads(primarySubject) {
        try {
            const culturalPrinciples = [
                'Whanaungatanga', 'Manaakitanga', 'Kaitiakitanga',
                'Rangatiratanga', 'Kotahitanga', 'Ako'
            ];

            const threads = [];

            for (const principle of culturalPrinciples) {
                // Find where this principle appears in primary subject
                const { data: inPrimary } = await this.supabase
                    .from('graphrag_resources')
                    .select('file_path, title')
                    .eq('metadata->>subject', primarySubject)
                    .or(`title.ilike.%${principle}%,content_preview.ilike.%${principle}%`)
                    .limit(5);

                // Find where it appears in other subjects
                const { data: inOthers } = await this.supabase
                    .from('graphrag_resources')
                    .select('file_path, title, metadata')
                    .neq('metadata->>subject', primarySubject)
                    .or(`title.ilike.%${principle}%,content_preview.ilike.%${principle}%,metadata->>cultural.eq.true`)
                    .limit(5);

                if (inPrimary && inPrimary.length > 0 && inOthers && inOthers.length > 0) {
                    threads.push({
                        principle,
                        icon: this.getPrincipleIcon(principle),
                        inPrimarySubject: inPrimary,
                        inOtherSubjects: inOthers,
                        threadStrength: 0.90,
                        type: 'cultural_thread'
                    });
                }
            }

            return threads;

        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        return [];
        }
    }

    /**
     * FIND REAL-WORLD BRIDGES
     * Where subjects meet in real-world contexts
     */
    async findRealWorldBridges(primarySubject) {
        // Real-world context keywords
        const realWorldContexts = {
            mathematics: ['climate change', 'economics', 'architecture', 'health', 'sports statistics'],
            science: ['environmental policy', 'health education', 'technology design', 'art conservation'],
            english: ['scientific writing', 'historical analysis', 'cultural storytelling', 'media literacy'],
            te_ao_maori: ['sustainable practice', 'community wellbeing', 'environmental guardianship']
        };

        const contexts = realWorldContexts[primarySubject] || [];
        const bridges = [];

        try {
            for (const context of contexts) {
                const { data: matches } = await this.supabase
                    .from('graphrag_resources')
                    .select('file_path, title, metadata')
                    .or(`title.ilike.%${context}%,content_preview.ilike.%${context}%`)
                    .gte('quality_score', 80)
                    .limit(5);

                if (matches && matches.length > 0) {
                    bridges.push({
                        realWorldContext: context,
                        resources: matches,
                        bridgeType: 'real_world_application',
                        subjects: [...new Set(matches.map(m => m.metadata?.subject))].filter(Boolean)
                    });
                }
            }

            return bridges;

        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        return [];
        }
    }

    /**
     * EXTRACT CONCEPTS FROM TEXT
     */
    extractConcepts(text) {
        if (!text) return [];
        
        const concepts = [];
        const keywords = text.toLowerCase().split(/\s+/);
        
        // Look for multi-word concepts
        const conceptPatterns = [
            /climate change/i,
            /critical thinking/i,
            /data analysis/i,
            /problem solving/i,
            /sustainability/i,
            /indigenous knowledge/i,
            /collaborative learning/i,
            /digital literacy/i
        ];

        for (const pattern of conceptPatterns) {
            if (pattern.test(text)) {
                concepts.push(pattern.source.replace(/[\/\\^$*+?.()|[\]{}]/g, '').replace(/i$/, ''));
            }
        }

        return [...new Set(concepts)];
    }

    /**
     * GET PRINCIPLE ICON
     */
    getPrincipleIcon(principle) {
        const icons = {
            'Whanaungatanga': '🤝',
            'Manaakitanga': '💚',
            'Kaitiakitanga': '🛡️',
            'Rangatiratanga': '👑',
            'Kotahitanga': '🤲',
            'Ako': '📚'
        };
        return icons[principle] || '🌺';
    }

    /**
     * BUILD INTERDISCIPLINARY UNIT
     * Auto-generate cross-subject unit from discoveries
     */
    async buildInterdisciplinaryUnit(discoveries) {
        const unit = {
            title: `Interdisciplinary Unit: ${discoveries.primarySubject}`,
            subjects: [discoveries.primarySubject],
            resources: [],
            culturalIntegration: discoveries.culturalThreads,
            realWorldContext: discoveries.realWorldApplications
        };

        // Collect resources from all discoveries
        discoveries.discoveries.forEach(disc => {
            disc.connectsTo.forEach(conn => {
                if (!unit.subjects.includes(conn.subject)) {
                    unit.subjects.push(conn.subject);
                }
                unit.resources.push({
                    path: conn.path,
                    title: conn.title,
                    subject: conn.subject,
                    concept: disc.concept
                });
            });
        });

        return unit;
    }

    /**
     * EXPORT DISCOVERIES FOR GRAPHRAG
     */
    async exportDiscoveriesToGraphRAG(subject, discoveries) {
        try {
            const { data, error } = await this.supabase
                .from('graphrag_resources')
                .insert({
                    file_path: `_cross_subject_discoveries/${subject}_${Date.now()}`,
                    title: `Cross-Subject Discoveries: ${subject}`,
                    content_preview: JSON.stringify(discoveries).substring(0, 500),
                    metadata: {
                        type: 'cross_subject_discovery',
                        primary_subject: subject,
                        connections_found: discoveries.discoveries.length,
                        cultural_threads: discoveries.culturalThreads.length,
                        discovered_at: new Date().toISOString()
                    },
                    quality_score: 90
                })
                .select();

            return { success: !error, data, error };
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        return { success: false, error };
        }
    }

    /**
     * CLEAR CACHE
     */
    clearCache() {
        this.discoveryCache.clear();
    }
}

// Auto-initialize and expose globally
window.CrossSubjectDiscovery = new CrossSubjectDiscoveryEngine();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CrossSubjectDiscoveryEngine;
}


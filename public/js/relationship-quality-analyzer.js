/**
 * Relationship Quality Analyzer - Te Kete Ako
 * Analyzes and improves relationship confidence scores
 * Detects confidence inflation and recalibrates the graph
 */

class RelationshipQualityAnalyzer {
    constructor() {
        this.supabase = null;
        this.qualityMetrics = {
            confidence: {
                veryStrong: 0.95,
                strong: 0.90,
                medium: 0.80,
                moderate: 0.70,
                weak: 0.60
            },
            healthyDistribution: {
                veryStrong: 0.05,    // 5% should be very strong
                strong: 0.10,         // 10% strong
                medium: 0.60,         // 60% medium
                moderate: 0.20,       // 20% moderate
                weak: 0.05            // 5% weak
            }
        };
        this.init();
    }

    async init() {
        if (window.supabase && window.ENV) {
            if (window.supabaseSingleton) {
                this.supabase = await window.supabaseSingleton.getClient();
            }
        }
    }

    /**
     * ANALYZE CONFIDENCE DISTRIBUTION
     * Check if confidence scores are healthy or inflated
     */
    async analyzeConfidenceDistribution() {
        try {
            const { data: distribution } = await this.supabase
                .from('graphrag_relationships')
                .select('confidence')
                .limit(10000); // Sample for performance

            if (!distribution) return { error: 'No data' };

            const analysis = {
                sampleSize: distribution.length,
                distribution: this.calculateDistribution(distribution),
                healthAssessment: null,
                recommendations: []
            };

            // Compare to healthy distribution
            analysis.healthAssessment = this.assessDistributionHealth(analysis.distribution);
            analysis.recommendations = this.generateRecommendations(analysis.distribution);

            return analysis;

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
        return { error: error.message };
        }
    }

    /**
     * CALCULATE DISTRIBUTION
     */
    calculateDistribution(relationships) {
        const buckets = {
            veryStrong: 0,
            strong: 0,
            medium: 0,
            moderate: 0,
            weak: 0
        };

        relationships.forEach(rel => {
            const conf = rel.confidence;
            if (conf >= this.qualityMetrics.confidence.veryStrong) buckets.veryStrong++;
            else if (conf >= this.qualityMetrics.confidence.strong) buckets.strong++;
            else if (conf >= this.qualityMetrics.confidence.medium) buckets.medium++;
            else if (conf >= this.qualityMetrics.confidence.moderate) buckets.moderate++;
            else buckets.weak++;
        });

        const total = relationships.length;
        return {
            veryStrong: { count: buckets.veryStrong, percent: (buckets.veryStrong / total * 100).toFixed(2) },
            strong: { count: buckets.strong, percent: (buckets.strong / total * 100).toFixed(2) },
            medium: { count: buckets.medium, percent: (buckets.medium / total * 100).toFixed(2) },
            moderate: { count: buckets.moderate, percent: (buckets.moderate / total * 100).toFixed(2) },
            weak: { count: buckets.weak, percent: (buckets.weak / total * 100).toFixed(2) }
        };
    }

    /**
     * ASSESS DISTRIBUTION HEALTH
     */
    assessDistributionHealth(distribution) {
        const issues = [];
        const strengths = [];

        // Check for inflation (too many high confidence)
        const highConf = parseFloat(distribution.veryStrong.percent) + parseFloat(distribution.strong.percent);
        if (highConf > 20) {
            issues.push({
                type: 'confidence_inflation',
                severity: 'medium',
                message: `${highConf}% of relationships are high confidence (expected ~15%)`,
                impact: 'May be too generous with confidence scores'
            });
        }

        // Check for too many weak connections
        const weakConf = parseFloat(distribution.weak.percent);
        if (weakConf > 10) {
            issues.push({
                type: 'too_many_weak',
                severity: 'high',
                message: `${weakConf}% of relationships are weak (expected ~5%)`,
                impact: 'Weak connections creating noise'
            });
        }

        // Check for good medium distribution
        const mediumConf = parseFloat(distribution.medium.percent);
        if (mediumConf >= 50 && mediumConf <= 70) {
            strengths.push({
                type: 'healthy_medium',
                message: `${mediumConf}% medium confidence - healthy distribution`,
                impact: 'Most relationships are reasonably confident'
            });
        }

        return {
            overall: issues.length === 0 ? 'healthy' : 
                     issues.some(i => i.severity === 'high') ? 'needs_attention' : 'monitor',
            issues,
            strengths,
            score: this.calculateHealthScore(distribution)
        };
    }

    /**
     * CALCULATE HEALTH SCORE
     */
    calculateHealthScore(distribution) {
        let score = 100;

        // Penalty for deviation from ideal
        const ideal = this.qualityMetrics.healthyDistribution;
        
        score -= Math.abs(parseFloat(distribution.veryStrong.percent) - ideal.veryStrong * 100) * 0.5;
        score -= Math.abs(parseFloat(distribution.strong.percent) - ideal.strong * 100) * 0.5;
        score -= Math.abs(parseFloat(distribution.medium.percent) - ideal.medium * 100) * 0.3;
        score -= Math.abs(parseFloat(distribution.moderate.percent) - ideal.moderate * 100) * 0.3;
        score -= Math.abs(parseFloat(distribution.weak.percent) - ideal.weak * 100) * 0.5;

        return Math.max(0, Math.min(100, score)).toFixed(1);
    }

    /**
     * GENERATE RECOMMENDATIONS
     */
    generateRecommendations(distribution) {
        const recommendations = [];

        const weakPercent = parseFloat(distribution.weak.percent);
        if (weakPercent > 5) {
            recommendations.push({
                priority: 'high',
                action: 'Prune weak connections',
                reason: `${weakPercent}% of relationships are weak (<0.70)`,
                strategy: 'Run pruning with threshold 0.65'
            });
        }

        const veryStrongPercent = parseFloat(distribution.veryStrong.percent);
        if (veryStrongPercent < 3) {
            recommendations.push({
                priority: 'medium',
                action: 'Create more high-confidence connections',
                reason: `Only ${veryStrongPercent}% are very strong (0.95+)`,
                strategy: 'Build excellence clusters for Q95+ resources'
            });
        }

        const mediumPercent = parseFloat(distribution.medium.percent);
        if (mediumPercent < 50) {
            recommendations.push({
                priority: 'low',
                action: 'Boost medium-confidence relationships',
                reason: `Only ${mediumPercent}% are medium confidence`,
                strategy: 'Review and upgrade moderate relationships'
            });
        }

        return recommendations;
    }

    /**
     * RECALIBRATE CONFIDENCE SCORES
     * Adjust scores based on actual relationship value
     */
    async recalibrateConfidenceScores(relationshipType) {
        try {
            // Get all relationships of this type
            const { data: rels } = await this.supabase
                .from('graphrag_relationships')
                .select('id, source_path, target_path, confidence, metadata')
                .eq('relationship_type', relationshipType)
                .limit(100);

            if (!rels) return { error: 'No relationships found' };

            const recalibrations = [];

            for (const rel of rels) {
                // Get source and target quality
                const [source, target] = await Promise.all([
                    this.supabase.from('graphrag_resources').select('quality_score').eq('file_path', rel.source_path).single(),
                    this.supabase.from('graphrag_resources').select('quality_score').eq('file_path', rel.target_path).single()
                ]);

                if (!source.data || !target.data) continue;

                // Recalculate confidence based on quality alignment
                const qualityDiff = Math.abs(source.data.quality_score - target.data.quality_score);
                const qualityBonus = qualityDiff < 10 ? 0.10 : qualityDiff < 20 ? 0.05 : 0;
                const baseConfidence = rel.confidence;
                const newConfidence = Math.min(0.95, baseConfidence + qualityBonus);

                if (Math.abs(newConfidence - baseConfidence) > 0.05) {
                    recalibrations.push({
                        id: rel.id,
                        oldConfidence: baseConfidence,
                        newConfidence,
                        reason: `Quality alignment: ${source.data.quality_score} ↔ ${target.data.quality_score}`
                    });
                }
            }

            return {
                relationshipType,
                analyzed: rels.length,
                recalibrations: recalibrations.length,
                samples: recalibrations.slice(0, 10)
            };

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
        return { error: error.message };
        }
    }

    /**
     * GET QUALITY REPORT
     */
    async getQualityReport() {
        const analysis = await this.analyzeConfidenceDistribution();
        
        return {
            timestamp: new Date().toISOString(),
            distribution: analysis.distribution,
            health: analysis.healthAssessment,
            recommendations: analysis.recommendations,
            actionItems: this.prioritizeActionItems(analysis.recommendations)
        };
    }

    /**
     * PRIORITIZE ACTION ITEMS
     */
    prioritizeActionItems(recommendations) {
        return recommendations
            .sort((a, b) => {
                const priority = { high: 3, medium: 2, low: 1 };
                return priority[b.priority] - priority[a.priority];
            })
            .map((rec, index) => ({
                order: index + 1,
                ...rec
            }));
    }
}

// Auto-initialize and expose globally
window.RelationshipQualityAnalyzer = new RelationshipQualityAnalyzer();

// Export for Node/agent tools
if (typeof module !== 'undefined' && module.exports) {
    module.exports = RelationshipQualityAnalyzer;
}


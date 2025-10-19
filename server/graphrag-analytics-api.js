/**
 * GraphRAG Analytics API - Te Kete Ako
 * RESTful API for querying and analyzing the graph
 * Provides insights, metrics, and recommendations
 * 
 * SETUP: npm install express @supabase/supabase-js cors
 * RUN: node server/graphrag-analytics-api.js
 */

const express = require('express');
const { createClient } = require('@supabase/supabase-js');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const supabase = createClient(
    process.env.SUPABASE_URL || 'https://nlgldaqtubrlcqddppbq.supabase.co',
    process.env.SUPABASE_SERVICE_KEY || process.env.SUPABASE_ANON_KEY
);

/**
 * GET GRAPH OVERVIEW
 * High-level statistics about the entire graph
 */
app.get('/api/graphrag/overview', async (req, res) => {
    try {
        const [resources, relationships] = await Promise.all([
            supabase.from('graphrag_resources').select('id', { count: 'exact', head: true }),
            supabase.from('graphrag_relationships').select('id', { count: 'exact', head: true })
        ]);

        const overview = {
            totalResources: resources.count,
            totalRelationships: relationships.count,
            avgRelationshipsPerResource: (relationships.count / resources.count).toFixed(2),
            lastUpdated: new Date().toISOString()
        };

        res.json(overview);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

/**
 * GET SUPER HUBS
 * Most connected resources
 */
app.get('/api/graphrag/super-hubs', async (req, res) => {
    try {
        const limit = parseInt(req.query.limit) || 20;

        // This would ideally be a materialized view for performance
        const { data, error } = await supabase
            .rpc('get_super_hubs', { result_limit: limit })
            .catch(() => ({ data: null, error: 'RPC not available' }));

        if (error || !data) {
            return res.json({ 
                message: 'Super hubs query requires database function',
                sample: [
                    { title: 'Assessments Library', connections: 4342 },
                    { title: 'Writers Toolkit', connections: 3002 },
                    { title: 'Homepage', connections: 949 }
                ]
            });
        }

        res.json(data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

/**
 * GET RECOMMENDATIONS
 * Intelligent recommendations for a resource
 */
app.get('/api/graphrag/recommendations/:resourcePath', async (req, res) => {
    try {
        const resourcePath = decodeURIComponent(req.params.resourcePath);
        const minConfidence = parseFloat(req.query.minConfidence) || 0.75;

        const { data: relationships } = await supabase
            .from('graphrag_relationships')
            .select('target_path, confidence, relationship_type, metadata')
            .eq('source_path', resourcePath)
            .gte('confidence', minConfidence)
            .order('confidence', { ascending: false })
            .limit(20);

        if (!relationships || relationships.length === 0) {
            return res.json({ recommendations: [] });
        }

        // Get resource details
        const targetPaths = relationships.map(r => r.target_path);
        const { data: resources } = await supabase
            .from('graphrag_resources')
            .select('*')
            .in('file_path', targetPaths);

        const enriched = relationships.map(rel => {
            const resource = resources?.find(r => r.file_path === rel.target_path);
            return {
                ...resource,
                confidence: rel.confidence,
                relationshipType: rel.relationship_type
            };
        });

        res.json({ 
            resourcePath,
            recommendations: enriched,
            count: enriched.length
        });

    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

/**
 * FIND LEARNING PATHWAY
 * Shortest path between two resources
 */
app.post('/api/graphrag/find-pathway', async (req, res) => {
    try {
        const { start, end, maxSteps = 5 } = req.body;

        // This is complex - would need graph traversal
        // For now, return conceptual structure
        res.json({
            pathway: [start, end],
            steps: 2,
            note: 'Advanced pathfinding requires graph database for optimal performance',
            recommendation: 'Use AdaptivePathwayGenerator client-side for now'
        });

    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

/**
 * GET SUBJECT STATISTICS
 * Analytics per subject
 */
app.get('/api/graphrag/subjects/:subject', async (req, res) => {
    try {
        const subject = req.params.subject;

        const { data: resources } = await supabase
            .from('graphrag_resources')
            .select('file_path, quality_score')
            .eq('metadata->>subject', subject);

        if (!resources) {
            return res.json({ subject, resources: 0 });
        }

        const stats = {
            subject,
            resourceCount: resources.length,
            avgQuality: (resources.reduce((sum, r) => sum + r.quality_score, 0) / resources.length).toFixed(1),
            qualityDistribution: {
                excellent: resources.filter(r => r.quality_score >= 95).length,
                high: resources.filter(r => r.quality_score >= 90 && r.quality_score < 95).length,
                good: resources.filter(r => r.quality_score >= 80 && r.quality_score < 90).length
            }
        };

        res.json(stats);

    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

/**
 * GRAPH HEALTH CHECK
 * Overall graph health metrics
 */
app.get('/api/graphrag/health', async (req, res) => {
    try {
        // Sample relationships for health check
        const { data: sample } = await supabase
            .from('graphrag_relationships')
            .select('confidence')
            .limit(1000);

        const avgConfidence = sample?.reduce((sum, r) => sum + r.confidence, 0) / sample?.length;

        const health = {
            status: avgConfidence > 0.80 ? 'healthy' : 
                    avgConfidence > 0.70 ? 'moderate' : 'needs_attention',
            avgConfidence: avgConfidence?.toFixed(3),
            sampleSize: sample?.length,
            recommendations: avgConfidence < 0.75 ? 
                ['Consider pruning weak relationships', 'Focus on quality over quantity'] :
                ['Maintain current quality standards']
        };

        res.json(health);

    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

/**
 * SEARCH GRAPH
 * Semantic search with relationship context
 */
app.get('/api/graphrag/search', async (req, res) => {
    try {
        const query = req.query.q;
        if (!query) {
            return res.status(400).json({ error: 'Query parameter required' });
        }

        const { data: results } = await supabase
            .from('graphrag_resources')
            .select('*')
            .or(`title.ilike.%${query}%,content_preview.ilike.%${query}%`)
            .order('quality_score', { ascending: false })
            .limit(20);

        res.json({ query, results: results || [], count: results?.length || 0 });

    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

/**
 * GET CULTURAL THREADS
 * Trace cultural principles through the graph
 */
app.get('/api/graphrag/cultural-threads/:principle', async (req, res) => {
    try {
        const principle = req.params.principle;

        const { data: resources } = await supabase
            .from('graphrag_resources')
            .select('*')
            .or(`title.ilike.%${principle}%,content_preview.ilike.%${principle}%,metadata->>cultural.eq.true`)
            .order('quality_score', { ascending: false })
            .limit(30);

        res.json({
            principle,
            resources: resources || [],
            count: resources?.length || 0,
            culturalPrinciples: [
                'Whanaungatanga', 'Manaakitanga', 'Kaitiakitanga',
                'Rangatiratanga', 'Kotahitanga', 'Ako'
            ]
        });

    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start server
const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
    console.log(`🚀 GraphRAG Analytics API running on port ${PORT}`);
    console.log(`📊 Endpoints available:`);
    console.log(`   GET  /api/graphrag/overview`);
    console.log(`   GET  /api/graphrag/super-hubs`);
    console.log(`   GET  /api/graphrag/recommendations/:path`);
    console.log(`   POST /api/graphrag/find-pathway`);
    console.log(`   GET  /api/graphrag/subjects/:subject`);
    console.log(`   GET  /api/graphrag/health`);
    console.log(`   GET  /api/graphrag/search?q=query`);
    console.log(`   GET  /api/graphrag/cultural-threads/:principle`);
});

module.exports = app;


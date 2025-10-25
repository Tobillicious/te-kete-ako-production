/**
 * GraphRAG Performance Monitor
 * Tracks GraphRAG query performance, caching, and optimization opportunities
 * Created: October 21, 2025
 */

(function() {
    'use strict';

    window.GraphRAGPerformance = {
        queries: [],
        cache: new Map(),
        config: {
            cacheEnabled: true,
            cacheExpiry: 5 * 60 * 1000, // 5 minutes
            maxCacheSize: 100,
            slowQueryThreshold: 2000, // 2 seconds
            reportingEnabled: true
        },

        async executeQuery(queryFn, cacheKey = null) {
            const startTime = performance.now();
            const queryId = `query_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;

            try {
                // Check cache first
                if (cacheKey && this.config.cacheEnabled) {
                    const cached = this.cache.get(cacheKey);
                    if (cached && Date.now() - cached.timestamp < this.config.cacheExpiry) {
                        const duration = performance.now() - startTime;
                        this.recordQuery({
                            queryId,
                            duration,
                            cached: true,
                            success: true,
                            cacheKey
                        });
                        return cached.data;
                    }
                }

                // Execute query
                const result = await queryFn();
                const duration = performance.now() - startTime;

                // Cache result
                if (cacheKey && this.config.cacheEnabled) {
                    this.addToCache(cacheKey, result);
                }

                // Record metrics
                this.recordQuery({
                    queryId,
                    duration,
                    cached: false,
                    success: true,
                    cacheKey,
                    resultCount: Array.isArray(result) ? result.length : null
                });

                // Alert on slow queries
                if (duration > this.config.slowQueryThreshold) {
                    // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        }ms`, {
                        cacheKey,
                        resultCount: Array.isArray(result) ? result.length : 'N/A'
                    });
                }

                return result;

            } catch (error) {
                const duration = performance.now() - startTime;
                this.recordQuery({
                    queryId,
                    duration,
                    cached: false,
                    success: false,
                    error: error.message,
                    cacheKey
                });
                throw error;
            }
        },

        recordQuery(queryData) {
            this.queries.push({
                ...queryData,
                timestamp: Date.now()
            });

            // Keep only last 100 queries
            if (this.queries.length > 100) {
                this.queries.shift();
            }

            // Report to analytics if enabled
            if (this.config.reportingEnabled && window.TeKeteAnalytics) {
                window.TeKeteAnalytics.track('graphrag_query', 'executed', {
                    duration: queryData.duration,
                    cached: queryData.cached,
                    success: queryData.success,
                    slow: queryData.duration > this.config.slowQueryThreshold
                });
            }
        },

        addToCache(key, data) {
            // Implement LRU cache
            if (this.cache.size >= this.config.maxCacheSize) {
                const firstKey = this.cache.keys().next().value;
                this.cache.delete(firstKey);
            }

            this.cache.set(key, {
                data,
                timestamp: Date.now()
            });
        },

        getMetrics() {
            const queries = this.queries;
            if (queries.length === 0) {
                return null;
            }

            const successful = queries.filter(q => q.success);
            const failed = queries.filter(q => !q.success);
            const cached = successful.filter(q => q.cached);
            const slow = successful.filter(q => q.duration > this.config.slowQueryThreshold);

            const durations = successful.map(q => q.duration);
            const avgDuration = durations.reduce((a, b) => a + b, 0) / durations.length;
            const maxDuration = Math.max(...durations);
            const minDuration = Math.min(...durations);

            return {
                total: queries.length,
                successful: successful.length,
                failed: failed.length,
                cached: cached.length,
                slow: slow.length,
                cacheHitRate: (cached.length / queries.length * 100).toFixed(1) + '%',
                avgDuration: avgDuration.toFixed(0) + 'ms',
                maxDuration: maxDuration.toFixed(0) + 'ms',
                minDuration: minDuration.toFixed(0) + 'ms',
                cacheSize: this.cache.size
            };
        },

        logMetrics() {
            const metrics = this.getMetrics();
            if (!metrics) {
                return;
            }

            console.table(metrics);
        },

        clearCache() {
            this.cache.clear();
        },

        // Wrapper for Supabase queries
        async wrapSupabaseQuery(query, cacheKey) {
            return this.executeQuery(async () => {
                const { data, error } = await query;
                if (error) throw error;
                return data;
            }, cacheKey);
        }
    };

    // Log metrics every minute
    setInterval(() => {
        if (window.GraphRAGPerformance.queries.length > 0) {
            window.GraphRAGPerformance.logMetrics();
        }
    }, 60000);

    // Expose to console for debugging
    window.gp = window.GraphRAGPerformance;


})();


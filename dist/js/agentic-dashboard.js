// AGENTIC DASHBOARD CREATION - KAITIAKI ARONUI
// Autonomous analytics and progress tracking agent

class AgenticDashboard {
    constructor() {
        this.resources = 775;
        this.metrics = {
            totalVisits: 0,
            resourcesAccessed: 0,
            searchQueries: 0,
            culturalEngagement: 0,
            aiInteractions: 0
        };
        this.culturalProgress = {};
        this.init();
    }

    init() {
        this.trackUserMetrics();
        this.createDashboardWidget();
        this.implementProgressTracking();
        this.deployAnalytics();
        this.setupRealTimeUpdates();
    }

    trackUserMetrics() {
        // Autonomous metric collection
        this.incrementMetric('totalVisits');
        
        // Track scroll depth (cultural engagement indicator)
        let maxScroll = 0;
        window.addEventListener('scroll', () => {
            const scrollPercent = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
            if (scrollPercent > maxScroll) {
                maxScroll = scrollPercent;
                this.updateCulturalEngagement(maxScroll);
            }
        });

        // Track search interactions
        document.addEventListener('input', (e) => {
            if (e.target.id === 'agentic-search' || e.target.type === 'search') {
                this.incrementMetric('searchQueries');
            }
        });

        // Track AI interactions
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('ai-interaction-btn') || 
                e.target.classList.contains('agentic-enhanced')) {
                this.incrementMetric('aiInteractions');
            }
        });
    }

    createDashboardWidget() {
        // Create floating dashboard widget
        const dashboardWidget = document.createElement('div');
        dashboardWidget.id = 'agentic-dashboard';
        dashboardWidget.className = 'dashboard-widget collapsed';
        dashboardWidget.innerHTML = `
            <div class="dashboard-toggle" onclick="window.agenticDashboard.toggleDashboard()">
                📊 <span class="dashboard-count">${this.resources}</span>
            </div>
            <div class="dashboard-content">
                <div class="dashboard-header">
                    <h3>🌟 Te Kete Ako Analytics</h3>
                    <button class="dashboard-close" onclick="window.agenticDashboard.toggleDashboard()">✕</button>
                </div>
                <div class="metrics-grid">
                    <div class="metric-card">
                        <div class="metric-value" id="metric-visits">${this.metrics.totalVisits}</div>
                        <div class="metric-label">Session Visits</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value" id="metric-resources">${this.metrics.resourcesAccessed}</div>
                        <div class="metric-label">Resources Explored</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value" id="metric-searches">${this.metrics.searchQueries}</div>
                        <div class="metric-label">AI Searches</div>
                    </div>
                    <div class="metric-card cultural">
                        <div class="metric-value" id="metric-cultural">${this.metrics.culturalEngagement}%</div>
                        <div class="metric-label">Cultural Engagement</div>
                    </div>
                </div>
                <div class="progress-section">
                    <div class="progress-header">🎯 Learning Progress</div>
                    <div class="progress-bar">
                        <div class="progress-fill" id="overall-progress" style="width: 0%"></div>
                    </div>
                    <div class="progress-stats">
                        <span>Te Reo: <strong id="te-reo-progress">0%</strong></span>
                        <span>Tikanga: <strong id="tikanga-progress">0%</strong></span>
                        <span>Academic: <strong id="academic-progress">0%</strong></span>
                    </div>
                </div>
                <div class="ai-insights">
                    <div class="insight-header">🧠 AI Insights</div>
                    <div class="insight-content" id="ai-insights">
                        <div class="insight-item">✨ Welcome to your learning journey!</div>
                        <div class="insight-item">🔍 Start searching to discover resources</div>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(dashboardWidget);
        window.agenticDashboard = this; // Global access
    }

    toggleDashboard() {
        const dashboard = document.getElementById('agentic-dashboard');
        dashboard.classList.toggle('collapsed');
        
        if (!dashboard.classList.contains('collapsed')) {
            this.updateDashboardData();
            this.generateAIInsights();
        }
    }

    incrementMetric(metricName) {
        if (this.metrics.hasOwnProperty(metricName)) {
            this.metrics[metricName]++;
            this.updateMetricDisplay(metricName);
            this.saveMetricsLocally();
        }
    }

    updateCulturalEngagement(scrollPercent) {
        this.metrics.culturalEngagement = Math.max(this.metrics.culturalEngagement, scrollPercent);
        this.updateMetricDisplay('culturalEngagement');
    }

    updateMetricDisplay(metricName) {
        const mappings = {
            'totalVisits': 'metric-visits',
            'resourcesAccessed': 'metric-resources', 
            'searchQueries': 'metric-searches',
            'culturalEngagement': 'metric-cultural',
            'aiInteractions': 'metric-ai'
        };

        const elementId = mappings[metricName];
        const element = document.getElementById(elementId);
        
        if (element) {
            const value = metricName === 'culturalEngagement' 
                ? `${this.metrics[metricName]}%` 
                : this.metrics[metricName];
            element.textContent = value;
            
            // Add pulse animation
            element.classList.add('metric-pulse');
            setTimeout(() => element.classList.remove('metric-pulse'), 600);
        }
    }

    implementProgressTracking() {
        // Track learning progress across cultural domains
        const domains = ['te-reo', 'tikanga', 'academic'];
        
        domains.forEach(domain => {
            this.culturalProgress[domain] = this.calculateDomainProgress(domain);
            this.updateProgressDisplay(domain, this.culturalProgress[domain]);
        });

        // Update overall progress
        const overallProgress = Object.values(this.culturalProgress).reduce((a, b) => a + b, 0) / domains.length;
        this.updateOverallProgress(overallProgress);
    }

    calculateDomainProgress(domain) {
        // AI-enhanced progress calculation based on interactions
        const baseProgress = Math.min(this.metrics.searchQueries * 5, 40);
        const engagementBonus = Math.min(this.metrics.culturalEngagement * 0.3, 30);
        const interactionBonus = Math.min(this.metrics.aiInteractions * 3, 30);
        
        return Math.min(baseProgress + engagementBonus + interactionBonus, 100);
    }

    updateProgressDisplay(domain, progress) {
        const element = document.getElementById(`${domain}-progress`);
        if (element) {
            element.textContent = `${Math.round(progress)}%`;
        }
    }

    updateOverallProgress(progress) {
        const progressFill = document.getElementById('overall-progress');
        if (progressFill) {
            progressFill.style.width = `${Math.round(progress)}%`;
            progressFill.style.background = `linear-gradient(90deg, #2C5F41 0%, #00b0b9 ${progress}%)`;
        }
    }

    deployAnalytics() {
        // Professional analytics tracking
        console.log('📊 Agentic Dashboard Analytics Active');
        
        // Track page visibility changes
        document.addEventListener('visibilitychange', () => {
            if (document.visibilityState === 'visible') {
                this.incrementMetric('totalVisits');
            }
        });

        // Track time on page
        this.startTime = Date.now();
        window.addEventListener('beforeunload', () => {
            const sessionTime = Math.round((Date.now() - this.startTime) / 1000);
            this.saveSessionTime(sessionTime);
        });
    }

    setupRealTimeUpdates() {
        // Real-time dashboard updates
        setInterval(() => {
            this.updateDashboardData();
        }, 30000); // Update every 30 seconds

        // Update counter in collapsed state
        setInterval(() => {
            const counter = document.querySelector('.dashboard-count');
            if (counter) {
                const totalActivity = Object.values(this.metrics).reduce((a, b) => a + b, 0);
                counter.textContent = `${this.resources}+${totalActivity > 0 ? '+' + totalActivity : ''}`;
            }
        }, 5000);
    }

    updateDashboardData() {
        // Refresh all metrics displays
        Object.keys(this.metrics).forEach(metric => {
            this.updateMetricDisplay(metric);
        });
        
        // Update progress tracking
        this.implementProgressTracking();
    }

    generateAIInsights() {
        const insights = document.getElementById('ai-insights');
        if (!insights) return;

        const aiInsights = this.getSmartInsights();
        insights.innerHTML = aiInsights.map(insight => 
            `<div class="insight-item">${insight}</div>`
        ).join('');
    }

    getSmartInsights() {
        const insights = [];
        
        if (this.metrics.searchQueries > 5) {
            insights.push('🔍 Great search activity! You\'re exploring our knowledge base effectively.');
        }
        
        if (this.metrics.culturalEngagement > 70) {
            insights.push('🌺 Excellent cultural engagement! You\'re deeply exploring Te Ao Māori content.');
        }
        
        if (this.metrics.aiInteractions > 10) {
            insights.push('🧠 High AI interaction! You\'re making the most of our smart features.');
        }

        if (insights.length === 0) {
            insights.push('✨ Start exploring to unlock personalized insights!');
            insights.push('🎯 Use the AI search to find relevant cultural resources.');
        }

        return insights.slice(0, 3); // Limit to 3 insights
    }

    saveMetricsLocally() {
        try {
            localStorage.setItem('te-kete-metrics', JSON.stringify(this.metrics));
        } catch (e) {
            console.log('📊 Analytics storage not available');
        }
    }

    loadMetricsLocally() {
        try {
            const saved = localStorage.getItem('te-kete-metrics');
            if (saved) {
                this.metrics = { ...this.metrics, ...JSON.parse(saved) };
            }
        } catch (e) {
            console.log('📊 Loading saved metrics failed');
        }
    }

    saveSessionTime(sessionTime) {
        console.log(`📊 Session time: ${sessionTime} seconds`);
    }
}

// AGENTIC ACTIVATION
document.addEventListener('DOMContentLoaded', () => {
    new AgenticDashboard();
    console.log('📊 AGENTIC DASHBOARD AGENT DEPLOYED - Analytics tracking active');
});

// Export for agent coordination
window.AgenticDashboard = AgenticDashboard;
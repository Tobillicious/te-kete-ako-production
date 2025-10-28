// Advanced Analytics and Learning Dashboard
class TeKeteAkoAnalytics {
    constructor() {
        this.sessionData = {
            startTime: Date.now(),
            pageViews: [],
            interactions: [],
            learningPath: [],
            assessmentResults: [],
            gameScores: []
        };
        
        this.learningMetrics = {
            engagementScore: 0,
            comprehensionLevel: 0,
            culturalEngagement: 0,
            collaborationRating: 0,
            progressVelocity: 0
        };
        
        this.teacherInsights = {
            mostUsedResources: [],
            studentEngagementPatterns: {},
            curriculumCoverage: {},
            assessmentTrends: []
        };
        
        this.initializeAnalytics();
        this.startDataCollection();
    }

    initializeAnalytics() {
        // Create analytics overlay (hidden by default)
        this.createAnalyticsOverlay();
        
        // Initialize tracking systems
        this.trackPageInteractions();
        this.trackLearningEvents();
        this.trackAssessmentData();
        this.trackGamePerformance();
        
        // Set up periodic data analysis
        setInterval(() => this.analyzeEngagementPatterns(), 30000); // Every 30 seconds
    }

    createAnalyticsOverlay() {
        const overlay = document.createElement('div');
        overlay.id = 'analytics-overlay';
        overlay.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #E67E22, #D35400);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 1000;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            color: white;
            font-size: 2rem;
        `;
        overlay.innerHTML = '🐛';
        overlay.title = 'Report a Bug (Beta)';
        
        overlay.addEventListener('click', () => this.openBugReportForm());
        overlay.addEventListener('mouseenter', () => {
            overlay.style.transform = 'scale(1.1)';
            overlay.style.boxShadow = '0 6px 25px rgba(230, 126, 34, 0.5)';
        });
        overlay.addEventListener('mouseleave', () => {
            overlay.style.transform = 'scale(1)';
            overlay.style.boxShadow = '0 4px 20px rgba(0,0,0,0.3)';
        });
        
        document.body.appendChild(overlay);
    }

    openBugReportForm() {
        // Create bug report modal
        const modal = document.createElement('div');
        modal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
            padding: 2rem;
        `;

        modal.innerHTML = `
            <div style="background: white; border-radius: 12px; padding: 2rem; max-width: 600px; width: 100%; max-height: 90vh; overflow-y: auto; box-shadow: 0 20px 60px rgba(0,0,0,0.3);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                    <h2 style="color: #E67E22; margin: 0; display: flex; align-items: center; gap: 0.5rem;">
                        🐛 <span>Report a Bug</span>
                    </h2>
                    <button onclick="this.closest('div[style*=\"position: fixed\"]').remove()" 
                            style="background: none; border: none; font-size: 2rem; cursor: pointer; color: #999; line-height: 1;">
                        ×
                    </button>
                </div>
                
                <p style="color: #666; margin-bottom: 1.5rem;">
                    Help us improve Te Kete Ako! Report any bugs, issues, or unexpected behavior you encounter.
                </p>

                <form id="bug-report-form" style="display: flex; flex-direction: column; gap: 1rem;">
                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #333;">
                            What type of issue is this?
                        </label>
                        <select required style="width: 100%; padding: 0.75rem; border: 2px solid #ddd; border-radius: 6px; font-size: 1rem;">
                            <option value="">Select issue type...</option>
                            <option value="display">Display/Layout Issue</option>
                            <option value="functionality">Feature Not Working</option>
                            <option value="data">Data/Content Error</option>
                            <option value="performance">Performance/Speed Issue</option>
                            <option value="accessibility">Accessibility Issue</option>
                            <option value="other">Other</option>
                        </select>
                    </div>

                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #333;">
                            Where did this happen?
                        </label>
                        <input type="text" required placeholder="Page URL or location" 
                               value="${window.location.href}"
                               style="width: 100%; padding: 0.75rem; border: 2px solid #ddd; border-radius: 6px; font-size: 1rem;">
                    </div>

                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #333;">
                            Describe the bug
                        </label>
                        <textarea required placeholder="What happened? What did you expect to happen?" 
                                  rows="5"
                                  style="width: 100%; padding: 0.75rem; border: 2px solid #ddd; border-radius: 6px; font-size: 1rem; resize: vertical; font-family: inherit;"></textarea>
                    </div>

                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #333;">
                            Steps to reproduce (optional)
                        </label>
                        <textarea placeholder="1. Go to...&#10;2. Click on...&#10;3. See error" 
                                  rows="3"
                                  style="width: 100%; padding: 0.75rem; border: 2px solid #ddd; border-radius: 6px; font-size: 1rem; resize: vertical; font-family: inherit;"></textarea>
                    </div>

                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #333;">
                            Your email (optional - for follow-up)
                        </label>
                        <input type="email" placeholder="your.email@example.com"
                               style="width: 100%; padding: 0.75rem; border: 2px solid #ddd; border-radius: 6px; font-size: 1rem;">
                    </div>

                    <div style="display: flex; gap: 1rem; margin-top: 1rem;">
                        <button type="submit" 
                                style="flex: 1; padding: 1rem; background: linear-gradient(135deg, #E67E22, #D35400); color: white; border: none; border-radius: 6px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                            🐛 Submit Bug Report
                        </button>
                        <button type="button" onclick="this.closest('div[style*=\"position: fixed\"]').remove()"
                                style="padding: 1rem 1.5rem; background: #f0f0f0; color: #666; border: none; border-radius: 6px; font-size: 1rem; font-weight: 600; cursor: pointer;">
                            Cancel
                        </button>
                    </div>
                </form>

                <div style="margin-top: 1.5rem; padding: 1rem; background: #f8f9fa; border-radius: 6px; border-left: 4px solid #E67E22;">
                    <p style="margin: 0; font-size: 0.9rem; color: #666;">
                        <strong>🔒 Privacy:</strong> Bug reports help us improve Te Kete Ako. Technical details (browser, page) are automatically included.
                    </p>
                </div>
            </div>
        `;

        // Close modal when clicking outside
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.remove();
            }
        });

        modal.querySelector('#bug-report-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const form = e.target;
            const submitBtn = form.querySelector('button[type="submit"]');
            
            // Show loading state
            submitBtn.disabled = true;
            submitBtn.textContent = '⏳ Submitting...';
            
            try {
                // Get form data
                const issueType = form.querySelector('select').value;
                const pageUrl = form.querySelectorAll('input')[0].value;
                const description = form.querySelectorAll('textarea')[0].value;
                const stepsToReproduce = form.querySelectorAll('textarea')[1]?.value || null;
                const email = form.querySelectorAll('input')[1]?.value || null;
                
                // Get browser info
                const browserInfo = {
                    userAgent: navigator.userAgent,
                    platform: navigator.platform,
                    language: navigator.language,
                    screenResolution: `${window.screen.width}x${window.screen.height}`,
                    viewport: `${window.innerWidth}x${window.innerHeight}`,
                    timestamp: new Date().toISOString()
                };
                
                // Get current user ID if logged in
                const { data: { user } } = await window.supabaseClient?.auth?.getUser() || { data: { user: null } };
                
                // Insert bug report into Supabase
                const { data, error } = await window.supabaseClient
                    .from('bug_reports')
                    .insert({
                        user_id: user?.id || null,
                        issue_type: issueType,
                        page_url: pageUrl,
                        description: description,
                        steps_to_reproduce: stepsToReproduce,
                        email: email,
                        user_agent: navigator.userAgent,
                        browser_info: browserInfo,
                        status: 'new',
                        priority: 'medium'
                    })
                    .select()
                    .single();
                
                if (error) throw error;
                
                // Show success message
                modal.innerHTML = `
                    <div style="background: white; border-radius: 12px; padding: 3rem; max-width: 500px; text-align: center;">
                        <div style="font-size: 4rem; margin-bottom: 1rem;">✅</div>
                        <h2 style="color: #27ae60; margin-bottom: 1rem;">Bug Report Submitted!</h2>
                        <p style="color: #666; margin-bottom: 0.5rem;">
                            <strong>Ngā mihi!</strong> Thank you for helping us improve Te Kete Ako.
                        </p>
                        <p style="color: #999; font-size: 0.9rem; margin-bottom: 2rem;">
                            Report ID: ${data.id.substring(0, 8)}...
                        </p>
                        ${email ? `<p style="color: #666; font-size: 0.9rem; margin-bottom: 2rem;">We'll email you at <strong>${email}</strong> with updates.</p>` : ''}
                        <button id="close-success-btn"
                                style="padding: 1rem 2rem; background: #27ae60; color: white; border: none; border-radius: 6px; font-size: 1rem; font-weight: 600; cursor: pointer;">
                            Close
                        </button>
                    </div>
                `;
                
                // Add close button functionality
                modal.querySelector('#close-success-btn').addEventListener('click', () => {
                    modal.remove();
                });
                
                console.log('✅ Bug report saved to database:', data.id);
                
            } catch (error) {
                console.error('Error submitting bug report:', error);
                
                // Show error message
                modal.innerHTML = `
                    <div style="background: white; border-radius: 12px; padding: 3rem; max-width: 500px; text-align: center;">
                        <div style="font-size: 4rem; margin-bottom: 1rem;">⚠️</div>
                        <h2 style="color: #e74c3c; margin-bottom: 1rem;">Submission Error</h2>
                        <p style="color: #666; margin-bottom: 2rem;">
                            Oops! There was a problem submitting your bug report. Please try again or contact us directly.
                        </p>
                        <div style="display: flex; gap: 1rem; justify-content: center;">
                            <button id="retry-btn"
                                    style="padding: 1rem 2rem; background: #3498db; color: white; border: none; border-radius: 6px; font-size: 1rem; font-weight: 600; cursor: pointer;">
                                Try Again
                            </button>
                            <button id="close-error-btn"
                                    style="padding: 1rem 2rem; background: #95a5a6; color: white; border: none; border-radius: 6px; font-size: 1rem; font-weight: 600; cursor: pointer;">
                                Close
                            </button>
                        </div>
                    </div>
                `;
                
                modal.querySelector('#retry-btn').addEventListener('click', () => {
                    modal.remove();
                    // Reopen the form
                    setTimeout(() => this.openBugReportForm(), 100);
                });
                
                modal.querySelector('#close-error-btn').addEventListener('click', () => {
                    modal.remove();
                });
            }
        });

        document.body.appendChild(modal);
    }

    trackPageInteractions() {
        // Track clicks on educational resources
        document.addEventListener('click', (e) => {
            const target = e.target.closest('a, button, .resource-card, .game-btn, .assessment-card');
            if (target) {
                this.logInteraction({
                    type: 'click',
                    element: target.className || target.tagName,
                    content: target.textContent?.substring(0, 50) || '',
                    timestamp: Date.now(),
                    page: window.location.pathname
                });
            }
        });

        // Track time spent on sections
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.logInteraction({
                        type: 'section_view',
                        section: entry.target.id || entry.target.className,
                        timestamp: Date.now(),
                        page: window.location.pathname
                    });
                }
            });
        });

        // Observe key sections
        document.querySelectorAll('section, .resource-card, .lesson-section').forEach(el => {
            observer.observe(el);
        });
    }

    trackLearningEvents() {
        // Track assessment submissions
        document.addEventListener('submit', (e) => {
            if (e.target.closest('.assessment-tools, .interactive-assessment')) {
                this.logLearningEvent({
                    type: 'assessment_submitted',
                    context: 'interactive_assessment',
                    timestamp: Date.now()
                });
            }
        });

        // Track video interactions
        document.addEventListener('click', (e) => {
            if (e.target.closest('a[href*="youtube"]')) {
                this.logLearningEvent({
                    type: 'video_accessed',
                    resource: e.target.textContent,
                    timestamp: Date.now()
                });
            }
        });

        // Track game starts
        document.addEventListener('click', (e) => {
            if (e.target.closest('.game-btn, a[href*="games/"]')) {
                this.logLearningEvent({
                    type: 'game_started',
                    game: e.target.textContent || e.target.href,
                    timestamp: Date.now()
                });
            }
        });
    }

    trackAssessmentData() {
        // Listen for assessment tool interactions
        document.addEventListener('click', (e) => {
            if (e.target.closest('[onclick*="showRubric"], [onclick*="generateExitTicket"], [onclick*="openProgressTracker"]')) {
                this.logAssessmentEvent({
                    type: 'assessment_tool_used',
                    tool: e.target.textContent,
                    timestamp: Date.now()
                });
            }
        });

        // Track progress dot clicks
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('dot')) {
                this.logAssessmentEvent({
                    type: 'progress_updated',
                    level: e.target.parentElement.children.length,
                    timestamp: Date.now()
                });
            }
        });
    }

    trackGamePerformance() {
        // Listen for game events (would be called by game scripts)
        window.addEventListener('gameScore', (e) => {
            this.sessionData.gameScores.push({
                game: e.detail.game,
                score: e.detail.score,
                wordsFound: e.detail.wordsFound || 0,
                culturalBonus: e.detail.culturalBonus || 0,
                timestamp: Date.now()
            });
        });

        window.addEventListener('gameComplete', (e) => {
            this.analyzeGamePerformance(e.detail);
        });
    }

    logInteraction(data) {
        this.sessionData.interactions.push(data);
        this.updateEngagementMetrics();
    }

    logLearningEvent(data) {
        this.sessionData.learningPath.push(data);
        this.updateLearningMetrics();
    }

    logAssessmentEvent(data) {
        this.sessionData.assessmentResults.push(data);
        this.updateAssessmentMetrics();
    }

    updateEngagementMetrics() {
        const interactions = this.sessionData.interactions;
        const timeActive = Date.now() - this.sessionData.startTime;
        
        // Calculate engagement score
        this.learningMetrics.engagementScore = Math.min(100, 
            (interactions.length / (timeActive / 60000)) * 10
        );

        // Analyze interaction patterns
        const culturalInteractions = interactions.filter(i => 
            i.content?.toLowerCase().includes('māori') || 
            i.content?.toLowerCase().includes('cultural') ||
            i.element?.includes('cultural')
        );
        
        this.learningMetrics.culturalEngagement = 
            (culturalInteractions.length / interactions.length) * 100;
    }

    updateLearningMetrics() {
        const events = this.sessionData.learningPath;
        
        // Analyze learning progression
        const assessmentEvents = events.filter(e => e.type.includes('assessment'));
        const videoEvents = events.filter(e => e.type.includes('video'));
        const gameEvents = events.filter(e => e.type.includes('game'));
        
        // Calculate comprehension level based on activity diversity
        this.learningMetrics.comprehensionLevel = Math.min(100,
            (assessmentEvents.length * 25) + 
            (videoEvents.length * 15) + 
            (gameEvents.length * 10)
        );
    }

    updateAssessmentMetrics() {
        const assessments = this.sessionData.assessmentResults;
        
        // Track assessment tool usage
        const toolUsage = assessments.reduce((acc, curr) => {
            acc[curr.tool] = (acc[curr.tool] || 0) + 1;
            return acc;
        }, {});

        // Update collaboration rating based on assessment interactions
        this.learningMetrics.collaborationRating = Math.min(100,
            assessments.filter(a => a.type === 'progress_updated').length * 20
        );
    }

    analyzeEngagementPatterns() {
        const currentTime = Date.now();
        const sessionDuration = currentTime - this.sessionData.startTime;
        
        // Calculate progress velocity
        this.learningMetrics.progressVelocity = 
            this.sessionData.learningPath.length / (sessionDuration / 60000);

        // Generate insights
        this.generateTeacherInsights();
    }

    generateTeacherInsights() {
        const interactions = this.sessionData.interactions;
        
        // Most used resources
        const resourceCounts = interactions.reduce((acc, curr) => {
            if (curr.type === 'click' && curr.content) {
                acc[curr.content] = (acc[curr.content] || 0) + 1;
            }
            return acc;
        }, {});

        this.teacherInsights.mostUsedResources = Object.entries(resourceCounts)
            .sort(([,a], [,b]) => b - a)
            .slice(0, 5)
            .map(([resource, count]) => ({ resource, count }));

        // Engagement patterns
        this.teacherInsights.studentEngagementPatterns = {
            peakEngagementTime: this.findPeakEngagementTime(),
            averageSessionDuration: Date.now() - this.sessionData.startTime,
            interactionFrequency: this.learningMetrics.engagementScore,
            culturalContentEngagement: this.learningMetrics.culturalEngagement
        };
    }

    findPeakEngagementTime() {
        const interactions = this.sessionData.interactions;
        const timeSlots = {};
        
        interactions.forEach(interaction => {
            const timeSlot = Math.floor(interaction.timestamp / 300000) * 300000; // 5-minute slots
            timeSlots[timeSlot] = (timeSlots[timeSlot] || 0) + 1;
        });

        const peakSlot = Object.entries(timeSlots)
            .sort(([,a], [,b]) => b - a)[0];
        
        return peakSlot ? new Date(parseInt(peakSlot[0])).toLocaleTimeString() : 'N/A';
    }

    openAnalyticsDashboard() {
        const modal = document.createElement('div');
        modal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(250,251,252,0.95);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 2000;
            overflow-y: auto;
            padding: 2rem;
        `;
        
        const dashboard = document.createElement('div');
        dashboard.style.cssText = `
            background: linear-gradient(135deg, var(--color-primary), var(--color-accent));
            border-radius: 20px;
            padding: 2rem;
            max-width: 1000px;
            width: 100%;
            color: white;
            position: relative;
            max-height: 90vh;
            overflow-y: auto;
        `;
        
        dashboard.innerHTML = this.generateDashboardHTML();
        modal.appendChild(dashboard);
        document.body.appendChild(modal);
        
        // Add close functionality
        modal.addEventListener('click', (e) => {
            if (e.target === modal) modal.remove();
        });
    }

    generateDashboardHTML() {
        return `
            <button onclick="this.closest('div[style*=\"position: fixed\"]').remove()" 
                    style="position: absolute; top: 1rem; right: 1rem; background: none; border: none; color: white; font-size: 1.5rem; cursor: pointer;">×</button>
            
            <h2 style="color: white; margin-bottom: 2rem; text-align: center;">📊 Te Kete Ako Learning Analytics</h2>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;">
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 12px; text-align: center;">
                    <h3 style="color: var(--color-secondary); margin-bottom: 0.5rem;">Engagement Score</h3>
                    <div style="font-size: 2rem; font-weight: bold;">${Math.round(this.learningMetrics.engagementScore)}</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Interactions per minute</div>
                </div>
                
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 12px; text-align: center;">
                    <h3 style="color: var(--color-secondary); margin-bottom: 0.5rem;">Cultural Engagement</h3>
                    <div style="font-size: 2rem; font-weight: bold;">${Math.round(this.learningMetrics.culturalEngagement)}%</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Te Ao Māori content interaction</div>
                </div>
                
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 12px; text-align: center;">
                    <h3 style="color: var(--color-secondary); margin-bottom: 0.5rem;">Learning Progress</h3>
                    <div style="font-size: 2rem; font-weight: bold;">${Math.round(this.learningMetrics.comprehensionLevel)}%</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Activity completion rate</div>
                </div>
                
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 12px; text-align: center;">
                    <h3 style="color: var(--color-secondary); margin-bottom: 0.5rem;">Collaboration</h3>
                    <div style="font-size: 2rem; font-weight: bold;">${Math.round(this.learningMetrics.collaborationRating)}%</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Interactive assessment use</div>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 2rem;">
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 12px;">
                    <h3 style="color: white; margin-bottom: 1rem;">📈 Learning Path Analysis</h3>
                    <div style="max-height: 200px; overflow-y: auto;">
                        ${this.sessionData.learningPath.slice(-5).map(event => `
                            <div style="padding: 0.5rem; margin: 0.5rem 0; background: rgba(255,255,255,0.1); border-radius: 6px; font-size: 0.9rem;">
                                <strong>${event.type.replace('_', ' ')}</strong>
                                <div style="opacity: 0.8;">${new Date(event.timestamp).toLocaleTimeString()}</div>
                            </div>
                        `).join('')}
                    </div>
                </div>
                
                <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 12px;">
                    <h3 style="color: white; margin-bottom: 1rem;">🎯 Most Used Resources</h3>
                    <div style="max-height: 200px; overflow-y: auto;">
                        ${this.teacherInsights.mostUsedResources.map(item => `
                            <div style="padding: 0.5rem; margin: 0.5rem 0; background: rgba(255,255,255,0.1); border-radius: 6px; font-size: 0.9rem; display: flex; justify-content: space-between;">
                                <span>${item.resource.substring(0, 30)}...</span>
                                <strong>${item.count}</strong>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
            
            <div style="margin-top: 2rem; background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 12px;">
                <h3 style="color: white; margin-bottom: 1rem;">🧠 AI Learning Insights</h3>
                <div style="display: grid; gap: 1rem;">
                    <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px;">
                        <strong>Learning Style Analysis:</strong>
                        <p style="margin: 0.5rem 0; opacity: 0.9;">${this.generateLearningStyleInsight()}</p>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px;">
                        <strong>Recommended Next Steps:</strong>
                        <p style="margin: 0.5rem 0; opacity: 0.9;">${this.generateRecommendations()}</p>
                    </div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 2rem;">
                <button onclick="this.exportAnalyticsData()" style="background: var(--color-secondary); color: white; border: none; padding: 1rem 2rem; border-radius: 25px; margin: 0.5rem; cursor: pointer;">📊 Export Data</button>
                <button onclick="this.generateTeacherReport()" style="background: white; color: var(--color-primary); border: none; padding: 1rem 2rem; border-radius: 25px; margin: 0.5rem; cursor: pointer;">📋 Teacher Report</button>
            </div>
        `;
    }

    generateLearningStyleInsight() {
        const assessmentUse = this.sessionData.assessmentResults.length;
        const gameUse = this.sessionData.gameScores.length;
        const videoUse = this.sessionData.learningPath.filter(e => e.type === 'video_accessed').length;
        
        if (assessmentUse > gameUse && assessmentUse > videoUse) {
            return "Strong analytical learner - prefers structured assessment and feedback tools.";
        } else if (gameUse > assessmentUse && gameUse > videoUse) {
            return "Kinesthetic/interactive learner - thrives with game-based learning and hands-on activities.";
        } else if (videoUse > assessmentUse && videoUse > gameUse) {
            return "Visual/auditory learner - benefits from multimedia content and video explanations.";
        } else {
            return "Balanced multimodal learner - engages well with diverse learning approaches.";
        }
    }

    generateRecommendations() {
        const culturalEngagement = this.learningMetrics.culturalEngagement;
        const comprehensionLevel = this.learningMetrics.comprehensionLevel;
        
        if (culturalEngagement < 30) {
            return "Increase engagement with Te Ao Māori content - try the enhanced cultural handouts or Māori astronomy resources.";
        } else if (comprehensionLevel < 50) {
            return "Focus on foundational concepts - use the interactive assessment tools and watch related YouTube videos.";
        } else if (comprehensionLevel > 80) {
            return "Ready for advanced challenges - try the comprehensive lesson plans and create your own learning pathways.";
        } else {
            return "Steady progress - continue with current learning pattern and explore new subject areas.";
        }
    }

    exportAnalyticsData() {
        const data = {
            sessionData: this.sessionData,
            learningMetrics: this.learningMetrics,
            teacherInsights: this.teacherInsights,
            timestamp: new Date().toISOString()
        };
        
        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `te-kete-ako-analytics-${new Date().toISOString().split('T')[0]}.json`;
        a.click();
        URL.revokeObjectURL(url);
    }

    generateTeacherReport() {
        const reportWindow = window.open('', '_blank');
        reportWindow.document.write(`
            <html>
                <head>
                    <title>Te Kete Ako Learning Report</title>
                    <style>
                        body { font-family: Arial, sans-serif; margin: 40px; }
                        .header { text-align: center; border-bottom: 2px solid #2C5F41; padding-bottom: 20px; }
                        .metric { background: #f0f8f0; padding: 15px; margin: 10px 0; border-radius: 8px; }
                        .insights { background: #e6f3ff; padding: 15px; margin: 10px 0; border-radius: 8px; }
                    </style>
                </head>
                <body>
                    <div class="header">
                        <h1>Te Kete Ako Learning Analytics Report</h1>
                        <p>Generated: ${new Date().toLocaleString()}</p>
                    </div>
                    
                    <h2>Learning Metrics</h2>
                    <div class="metric">
                        <strong>Engagement Score:</strong> ${Math.round(this.learningMetrics.engagementScore)}/100
                    </div>
                    <div class="metric">
                        <strong>Cultural Engagement:</strong> ${Math.round(this.learningMetrics.culturalEngagement)}%
                    </div>
                    <div class="metric">
                        <strong>Learning Progress:</strong> ${Math.round(this.learningMetrics.comprehensionLevel)}%
                    </div>
                    
                    <h2>AI-Generated Insights</h2>
                    <div class="insights">
                        <strong>Learning Style:</strong> ${this.generateLearningStyleInsight()}
                    </div>
                    <div class="insights">
                        <strong>Recommendations:</strong> ${this.generateRecommendations()}
                    </div>
                    
                    <h2>Session Summary</h2>
                    <p><strong>Total Interactions:</strong> ${this.sessionData.interactions.length}</p>
                    <p><strong>Learning Activities:</strong> ${this.sessionData.learningPath.length}</p>
                    <p><strong>Assessment Events:</strong> ${this.sessionData.assessmentResults.length}</p>
                </body>
            </html>
        `);
    }

    startDataCollection() {
        // Begin collecting analytics data
        console.log('Te Kete Ako Analytics Dashboard initialized');
        
        // Track page load
        this.logLearningEvent({
            type: 'page_loaded',
            page: window.location.pathname,
            timestamp: Date.now()
        });
    }
}

// Initialize analytics when DOM loads
document.addEventListener('DOMContentLoaded', () => {
    window.teKeteAkoAnalytics = new TeKeteAkoAnalytics();
});
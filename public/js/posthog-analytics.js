/**
 * PostHog Analytics Integration - Te Kete Ako
 * Teacher insights dashboard and student engagement metrics
 * Phase 2 of Tech Stack Evolution
 */

class TeKeteAnalytics {
    constructor() {
        this.posthog = null;
        this.teacherId = null;
        this.schoolId = null;
        this.init();
    }

    async init() {
        await this.loadPostHog();
        this.setupEventTracking();
        this.setupTeacherInsights();
        this.setupStudentEngagement();
    }

    async loadPostHog() {
        if (window.posthog) {
            this.posthog = window.posthog;
            return;
        }

        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = 'https://app.posthog.com/static/array.js';
            script.onload = () => {
                window.posthog.init('phc_te-kete-ako-key', {
                    api_host: 'https://app.posthog.com',
                    person_profiles: 'identified_only',
                    capture_pageview: false,
                    capture_pageleave: true,
                    loaded: (posthog) => {
                        this.posthog = posthog;
                        resolve();
                    }
                });
            };
            script.onerror = reject;
            document.head.appendChild(script);
        });
    }

    setupEventTracking() {
        // Track page views
        this.trackPageView();
        
        // Track lesson interactions
        this.trackLessonInteractions();
        
        // Track resource downloads
        this.trackResourceDownloads();
        
        // Track search queries
        this.trackSearchQueries();
        
        // Track teaching variant selections
        this.trackTeachingVariants();
    }

    trackPageView() {
        const page = window.location.pathname;
        const title = document.title;
        
        this.posthog?.capture('page_viewed', {
            page: page,
            title: title,
            timestamp: new Date().toISOString(),
            user_agent: navigator.userAgent,
            referrer: document.referrer
        });
    }

    trackLessonInteractions() {
        // Track lesson views
        document.addEventListener('click', (e) => {
            const lessonLink = e.target.closest('a[href*="/lessons/"]');
            if (lessonLink) {
                const lessonId = this.extractLessonId(lessonLink.href);
                this.posthog?.capture('lesson_viewed', {
                    lesson_id: lessonId,
                    lesson_url: lessonLink.href,
                    timestamp: new Date().toISOString()
                });
            }
        });

        // Track lesson completions
        document.addEventListener('click', (e) => {
            if (e.target.matches('.lesson-complete-btn')) {
                const lessonId = e.target.getAttribute('data-lesson-id');
                this.posthog?.capture('lesson_completed', {
                    lesson_id: lessonId,
                    completion_time: new Date().toISOString(),
                    time_spent: this.calculateTimeSpent(lessonId)
                });
            }
        });
    }

    trackResourceDownloads() {
        document.addEventListener('click', (e) => {
            const downloadLink = e.target.closest('a[href*="/handouts/"], a[href*="/download/"]');
            if (downloadLink) {
                const resourceType = this.getResourceType(downloadLink.href);
                const resourceId = this.extractResourceId(downloadLink.href);
                
                this.posthog?.capture('resource_downloaded', {
                    resource_type: resourceType,
                    resource_id: resourceId,
                    resource_url: downloadLink.href,
                    timestamp: new Date().toISOString()
                });
            }
        });
    }

    trackSearchQueries() {
        const searchInput = document.getElementById('unit-search');
        if (searchInput) {
            let searchTimeout;
            searchInput.addEventListener('input', (e) => {
                clearTimeout(searchTimeout);
                searchTimeout = setTimeout(() => {
                    if (e.target.value.length > 2) {
                        this.posthog?.capture('search_query', {
                            query: e.target.value,
                            results_count: this.getSearchResultsCount(),
                            timestamp: new Date().toISOString()
                        });
                    }
                }, 1000);
            });
        }
    }

    trackTeachingVariants() {
        document.addEventListener('click', (e) => {
            const variantCard = e.target.closest('.variant-card');
            if (variantCard) {
                const variantType = variantCard.getAttribute('data-variant-type');
                const lessonId = variantCard.getAttribute('data-lesson-id');
                
                this.posthog?.capture('teaching_variant_selected', {
                    variant_type: variantType,
                    lesson_id: lessonId,
                    timestamp: new Date().toISOString()
                });
            }
        });
    }

    setupTeacherInsights() {
        // Teacher dashboard analytics
        this.trackTeacherDashboardUsage();
        this.trackClassroomManagement();
        this.trackCurriculumPlanning();
    }

    trackTeacherDashboardUsage() {
        // Track dashboard sections accessed
        document.addEventListener('click', (e) => {
            const dashboardSection = e.target.closest('[data-dashboard-section]');
            if (dashboardSection) {
                const section = dashboardSection.getAttribute('data-dashboard-section');
                this.posthog?.capture('dashboard_section_accessed', {
                    section: section,
                    teacher_id: this.teacherId,
                    timestamp: new Date().toISOString()
                });
            }
        });
    }

    trackClassroomManagement() {
        // Track class creation and management
        document.addEventListener('submit', (e) => {
            const classForm = e.target.closest('#class-creation-form');
            if (classForm) {
                const formData = new FormData(classForm);
                this.posthog?.capture('class_created', {
                    class_name: formData.get('className'),
                    year_level: formData.get('yearLevel'),
                    student_count: formData.get('studentCount'),
                    teacher_id: this.teacherId,
                    timestamp: new Date().toISOString()
                });
            }
        });
    }

    trackCurriculumPlanning() {
        // Track unit plan usage
        document.addEventListener('click', (e) => {
            const unitPlanLink = e.target.closest('a[href*="/units/"]');
            if (unitPlanLink) {
                const unitId = this.extractUnitId(unitPlanLink.href);
                this.posthog?.capture('unit_plan_accessed', {
                    unit_id: unitId,
                    unit_url: unitPlanLink.href,
                    teacher_id: this.teacherId,
                    timestamp: new Date().toISOString()
                });
            }
        });
    }

    setupStudentEngagement() {
        // Track student progress
        this.trackStudentProgress();
        this.trackStudentInteractions();
        this.trackLearningOutcomes();
    }

    trackStudentProgress() {
        // Track student lesson progress
        document.addEventListener('click', (e) => {
            if (e.target.matches('.student-progress-btn')) {
                const studentId = e.target.getAttribute('data-student-id');
                const lessonId = e.target.getAttribute('data-lesson-id');
                const progress = e.target.getAttribute('data-progress');
                
                this.posthog?.capture('student_progress_updated', {
                    student_id: studentId,
                    lesson_id: lessonId,
                    progress: progress,
                    timestamp: new Date().toISOString()
                });
            }
        });
    }

    trackStudentInteractions() {
        // Track student engagement with content
        document.addEventListener('click', (e) => {
            if (e.target.matches('.student-interaction')) {
                const interactionType = e.target.getAttribute('data-interaction-type');
                const contentId = e.target.getAttribute('data-content-id');
                
                this.posthog?.capture('student_interaction', {
                    interaction_type: interactionType,
                    content_id: contentId,
                    timestamp: new Date().toISOString()
                });
            }
        });
    }

    trackLearningOutcomes() {
        // Track learning outcomes and assessments
        document.addEventListener('submit', (e) => {
            const assessmentForm = e.target.closest('#assessment-form');
            if (assessmentForm) {
                const formData = new FormData(assessmentForm);
                this.posthog?.capture('learning_outcome_assessed', {
                    student_id: formData.get('studentId'),
                    lesson_id: formData.get('lessonId'),
                    outcome: formData.get('outcome'),
                    score: formData.get('score'),
                    timestamp: new Date().toISOString()
                });
            }
        });
    }

    // Helper methods
    extractLessonId(url) {
        const match = url.match(/\/lessons\/([^\/]+)/);
        return match ? match[1] : null;
    }

    extractUnitId(url) {
        const match = url.match(/\/units\/([^\/]+)/);
        return match ? match[1] : null;
    }

    extractResourceId(url) {
        const match = url.match(/\/handouts\/([^\/]+)/);
        return match ? match[1] : null;
    }

    getResourceType(url) {
        if (url.includes('/handouts/')) return 'handout';
        if (url.includes('/download/')) return 'download';
        return 'unknown';
    }

    getSearchResultsCount() {
        const resultsElement = document.getElementById('results-count');
        if (resultsElement) {
            const text = resultsElement.textContent;
            const match = text.match(/(\d+)/);
            return match ? parseInt(match[1]) : 0;
        }
        return 0;
    }

    calculateTimeSpent(lessonId) {
        // Calculate time spent on lesson (simplified)
        const startTime = localStorage.getItem(`lesson_start_${lessonId}`);
        if (startTime) {
            return Date.now() - parseInt(startTime);
        }
        return 0;
    }

    // Teacher identification
    identifyTeacher(teacherId, teacherData) {
        this.teacherId = teacherId;
        this.posthog?.identify(teacherId, {
            email: teacherData.email,
            name: teacherData.name,
            school: teacherData.school,
            role: 'teacher'
        });
    }

    // School identification
    identifySchool(schoolId, schoolData) {
        this.schoolId = schoolId;
        this.posthog?.group('school', schoolId, {
            name: schoolData.name,
            type: schoolData.type,
            location: schoolData.location,
            student_count: schoolData.studentCount
        });
    }

    // Custom events for Te Kete Ako
    trackCulturalIntegration(lessonId, culturalElement) {
        this.posthog?.capture('cultural_integration_used', {
            lesson_id: lessonId,
            cultural_element: culturalElement,
            timestamp: new Date().toISOString()
        });
    }

    trackGraphRAGUsage(query, resultsCount) {
        this.posthog?.capture('graphrag_query', {
            query: query,
            results_count: resultsCount,
            timestamp: new Date().toISOString()
        });
    }

    trackPrintUsage(resourceId, printFormat) {
        this.posthog?.capture('resource_printed', {
            resource_id: resourceId,
            print_format: printFormat,
            timestamp: new Date().toISOString()
        });
    }
}

// Initialize analytics when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => new TeKeteAnalytics());
} else {
    new TeKeteAnalytics();
}

// Export for global access
window.TeKeteAnalytics = TeKeteAnalytics;

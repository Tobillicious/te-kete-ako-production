/**
 * ================================================================
 * STUDENT DASHBOARD - TE KETE AKO
 * ================================================================
 * Personalized learning dashboard for NZ students
 * Features: Progress tracking, recommendations, cultural engagement
 * Agent-4 + Agent-9 Collaborative Build - Task 3
 * ================================================================
 */

let supabase;
let currentStudent = null;

/**
 * Initialize student dashboard
 */
async function initStudentDashboard() {
    // Initialize Supabase
    if (typeof window.supabase === 'undefined') {
        console.error('Supabase not loaded');
        showError('Unable to connect. Please refresh the page.');
        return;
    }
    
    supabase = window.supabase.createClient(
        'https://nlgldaqtubrlcqddppbq.supabase.co',
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
    );
    
    // Check authentication
    const { data: { session } } = await supabase.auth.getSession();
    
    if (!session) {
        // Not logged in - redirect to login
        window.location.href = '/login.html';
        return;
    }
    
    // Fetch student profile
    await loadStudentProfile(session.user.id);
    
    // Load dashboard data
    await Promise.all([
        loadProgressData(),
        loadRecommendedResources(),
        loadMyClasses(),
        loadSavedResources(),
        loadAchievements()
    ]);
    
    // Show dashboard (hide loading)
    document.getElementById('loading').style.display = 'none';
    document.getElementById('dashboard').style.display = 'block';
}

/**
 * Load student profile from database
 */
async function loadStudentProfile(userId) {
    try {
        const { data, error } = await supabase
            .from('profiles')
            .select('*')
            .eq('user_id', userId)
            .eq('role', 'student')
            .single();
        
        if (error) throw error;
        
        currentStudent = data;
        
        // Update UI with student info
        document.getElementById('studentName').textContent = data.first_name || data.display_name || 'Student';
        document.getElementById('studentSchool').textContent = data.school_name || 'Your School';
        document.getElementById('studentYear').textContent = data.year_level || '8';
        document.getElementById('year-display').textContent = data.year_level || '8';
        
        // Load cultural-specific content if Māori
        if (data.cultural_identity && data.cultural_identity.includes('Māori')) {
            loadCulturalContent(data.iwi_affiliation);
        }
        
        // Apply language preference
        if (data.preferred_language === 'Te Reo Māori' || data.preferred_language === 'Both') {
            enableTeReoInterface();
        }
        
    } catch (error) {
        console.error('Profile load error:', error);
        showError('Unable to load your profile. Please try again.');
    }
}

/**
 * Load progress data
 */
async function loadProgressData() {
    if (!currentStudent) return;
    
    try {
        // Get student progress records
        const { data, error } = await supabase
            .from('student_progress')
            .select('*')
            .eq('student_id', currentStudent.user_id);
        
        if (error) throw error;
        
        // Calculate stats
        const lessonsCompleted = data ? data.filter(p => p.completed_at).length : 0;
        const totalProgress = data && data.length > 0 
            ? Math.round(data.reduce((sum, p) => sum + (p.progress_percentage || 0), 0) / data.length)
            : 0;
        const avgCultural = data && data.length > 0
            ? Math.round(data.reduce((sum, p) => sum + (p.cultural_engagement_score || 0), 0) / data.length)
            : 0;
        
        // Calculate streak (simplified)
        const streak = calculateStreak(data);
        
        // Update UI
        document.getElementById('stat-lessons').textContent = lessonsCompleted;
        document.getElementById('stat-progress').textContent = totalProgress + '%';
        document.getElementById('stat-streak').textContent = '🔥 ' + streak;
        document.getElementById('stat-cultural').textContent = avgCultural + '%';
        
        // Load continue learning section
        if (data && data.length > 0) {
            const inProgress = data.find(p => !p.completed_at && p.progress_percentage > 0);
            if (inProgress) {
                displayContinueLearning(inProgress);
            }
        }
        
    } catch (error) {
        console.error('Progress load error:', error);
        // Continue with default values
    }
}

/**
 * Calculate learning streak
 */
function calculateStreak(progressData) {
    // Simplified streak calculation
    // In production, would check consecutive days with activity
    if (!progressData || progressData.length === 0) return 0;
    
    // For now, return days with any progress this week
    const weekAgo = new Date();
    weekAgo.setDate(weekAgo.getDate() - 7);
    
    const recentActivity = progressData.filter(p => {
        if (!p.updated_at) return false;
        const updateDate = new Date(p.updated_at);
        return updateDate > weekAgo;
    });
    
    return Math.min(recentActivity.length, 7);
}

/**
 * Display continue learning section
 */
function displayContinueLearning(progressRecord) {
    const container = document.getElementById('continue-learning');
    
    // Fetch resource details
    supabase
        .from('graphrag_resources')
        .select('*')
        .eq('id', progressRecord.resource_id)
        .single()
        .then(({ data, error }) => {
            if (error || !data) return;
            
            container.innerHTML = `
                <div class="resource-card-student" style="background: linear-gradient(135deg, var(--color-accent-50), white);">
                    <div style="display: flex; justify-content: space-between; align-items: start; gap: 1rem;">
                        <div style="flex: 1;">
                            <h3 style="color: var(--color-primary-500); margin-bottom: 0.5rem;">${data.title}</h3>
                            <p style="color: var(--color-neutral-600); font-size: 0.95rem; margin-bottom: 1rem;">${data.description || ''}</p>
                            <div style="background: var(--color-neutral-100); border-radius: 8px; overflow: hidden; height: 8px; margin-bottom: 0.5rem;">
                                <div style="background: var(--color-success-500); height: 100%; width: ${progressRecord.progress_percentage}%; transition: width 0.5s ease;"></div>
                            </div>
                            <p style="font-size: 0.85rem; color: var(--color-neutral-600);">${progressRecord.progress_percentage}% Complete</p>
                        </div>
                        <button class="btn btn-primary" onclick="window.location.href='${data.path}'">
                            Continue →
                        </button>
                    </div>
                </div>
            `;
        });
}

/**
 * Load recommended resources based on student profile
 */
async function loadRecommendedResources() {
    if (!currentStudent) return;
    
    try {
        // Query resources matching student's year level
        const { data, error } = await supabase
            .from('graphrag_resources')
            .select('*')
            .eq('level', `y${currentStudent.year_level}`)
            .eq('is_active', true)
            .limit(6);
        
        if (error) throw error;
        
        const container = document.getElementById('recommended-resources');
        
        if (!data || data.length === 0) {
            container.innerHTML = '<p style="color: var(--color-neutral-600);">No recommendations yet. Check back soon!</p>';
            return;
        }
        
        container.innerHTML = data.map(resource => `
            <div class="card card-hover" onclick="window.location.href='${resource.path}'">
                <div class="card-content">
                    <div class="badge badge-primary" style="margin-bottom: 0.75rem;">${resource.subject || 'General'}</div>
                    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">${resource.title}</h3>
                    <p style="font-size: 0.9rem; color: var(--color-neutral-600); margin-bottom: 1rem;">${(resource.description || '').substring(0, 100)}...</p>
                    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                        ${(resource.tags || []).slice(0, 3).map(tag => 
                            `<span class="badge badge-sm badge-neutral">${tag}</span>`
                        ).join('')}
                    </div>
                </div>
            </div>
        `).join('');
        
    } catch (error) {
        console.error('Recommendations error:', error);
    }
}

/**
 * Load student's classes
 */
async function loadMyClasses() {
    if (!currentStudent) return;
    
    try {
        // Query teacher_classes where student is enrolled
        const { data, error } = await supabase
            .from('teacher_classes')
            .select('*, profiles!teacher_classes_teacher_id_fkey(display_name)')
            .contains('student_ids', [currentStudent.user_id]);
        
        if (error) throw error;
        
        const container = document.getElementById('my-classes');
        
        if (!data || data.length === 0) {
            // Keep default message
            return;
        }
        
        container.innerHTML = data.map(cls => `
            <div class="resource-card-student">
                <h3 style="color: var(--color-primary-500); margin-bottom: 0.5rem;">
                    ${cls.class_name}
                </h3>
                <p style="color: var(--color-neutral-600); font-size: 0.9rem;">
                    ${cls.subject} | Year ${cls.year_level} | Teacher: ${cls.profiles?.display_name || 'Staff'}
                </p>
                <p style="font-size: 0.85rem; color: var(--color-neutral-500); margin-top: 0.5rem;">
                    Class Code: <strong>${cls.class_code}</strong>
                </p>
            </div>
        `).join('');
        
    } catch (error) {
        console.error('Classes load error:', error);
    }
}

/**
 * Load saved resources (My Kete)
 */
async function loadSavedResources() {
    if (!currentStudent) return;
    
    try {
        const { data, error } = await supabase
            .from('user_saved_resources')
            .select('*, resources(*)')
            .eq('user_id', currentStudent.user_id)
            .order('saved_at', { ascending: false })
            .limit(5);
        
        if (error) throw error;
        
        const container = document.getElementById('my-kete');
        
        if (!data || data.length === 0) {
            // Keep default message
            return;
        }
        
        container.innerHTML = data.map(saved => `
            <div class="resource-card-student" onclick="window.location.href='${saved.resources.path}'">
                <h4 style="color: var(--color-primary-500); margin-bottom: 0.25rem;">${saved.resources.title}</h4>
                <p style="font-size: 0.85rem; color: var(--color-neutral-600);">${saved.resources.subject || 'General'} | Saved ${formatDate(saved.saved_at)}</p>
            </div>
        `).join('');
        
    } catch (error) {
        console.error('Saved resources error:', error);
    }
}

/**
 * Load achievements
 */
async function loadAchievements() {
    // Placeholder for achievement system
    // In production, would query achievements/badges earned
    const badgeContainer = document.getElementById('badge-container');
    
    // Check if student has completed any lessons
    if (currentStudent) {
        const { data } = await supabase
            .from('student_progress')
            .select('*')
            .eq('student_id', currentStudent.user_id)
            .not('completed_at', 'is', null);
        
        if (data && data.length > 0) {
            badgeContainer.innerHTML = '<span class="achievement-badge">🌟 First Lesson Complete!</span>';
            
            if (data.length >= 5) {
                badgeContainer.innerHTML += '<span class="achievement-badge">🔥 5 Lessons Mastered!</span>';
            }
            
            if (data.length >= 10) {
                badgeContainer.innerHTML += '<span class="achievement-badge">🏆 Learning Champion!</span>';
            }
            
            // Cultural engagement badge
            const avgCultural = data.reduce((sum, p) => sum + (p.cultural_engagement_score || 0), 0) / data.length;
            if (avgCultural > 80) {
                badgeContainer.innerHTML += '<span class="achievement-badge">🌿 Cultural Kaitiaki!</span>';
            }
        }
    }
}

/**
 * Load cultural-specific content
 */
function loadCulturalContent(iwiAffiliation) {
    // Could load iwi-specific whakataukī
    // Could highlight iwi-related resources
    // For now, acknowledge cultural identity
    console.log('Loading cultural content for:', iwiAffiliation);
}

/**
 * Enable Te Reo interface
 */
function enableTeReoInterface() {
    // Would translate UI labels to Te Reo Māori
    // For now, add bilingual labels
    console.log('Te Reo interface enabled');
}

/**
 * Helper: Format date
 */
function formatDate(dateString) {
    const date = new Date(dateString);
    const now = new Date();
    const diffMs = now - date;
    const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return 'today';
    if (diffDays === 1) return 'yesterday';
    if (diffDays < 7) return `${diffDays} days ago`;
    return date.toLocaleDateString('en-NZ');
}

/**
 * Browse resources
 */
function browseResources() {
    window.location.href = '/resource-hub.html';
}

/**
 * Show error message
 */
function showError(message) {
    const loading = document.getElementById('loading');
    if (loading) {
        loading.innerHTML = `
            <div style="font-size: 3rem;">⚠️</div>
            <p style="font-size: 1.2rem; color: var(--color-error-500);">${message}</p>
            <button class="btn btn-primary" onclick="window.location.reload()">Try Again</button>
        `;
    }
}

/**
 * Logout function
 */
async function logoutStudent() {
    if (confirm('Are you sure you want to log out?')) {
        await supabase.auth.signOut();
        window.location.href = '/index.html';
    }
}

/**
 * ================================================================
 * TEACHER DASHBOARD - TE KETE AKO
 * Comprehensive teacher portal functionality
 * ================================================================
 */

let supabaseClient = null;
let currentTeacher = null;

// Wait for Supabase to be ready
window.addEventListener('supabaseReady', (event) => {
    supabaseClient = event.detail.client;
    initializeDashboard();
});

/**
 * Initialize dashboard
 */
async function initializeDashboard() {
    try {
        // Check authentication
        const { data: { user }, error: authError } = await supabaseClient.auth.getUser();
        
        if (authError || !user) {
            // Not logged in - redirect to login
            window.location.href = '/login.html?redirect=/teachers/dashboard.html';
            return;
        }
        
        // Get teacher profile
        const { data: profile, error: profileError } = await supabaseClient
            .from('profiles')
            .select('*')
            .eq('user_id', user.id)
            .single();
        
        if (profileError) throw profileError;
        
        // Verify role is teacher
        if (profile.role !== 'teacher') {
            window.location.href = '/student-dashboard.html';
            return;
        }
        
        currentTeacher = profile;
        
        // Load dashboard data
        await Promise.all([
            loadTeacherInfo(profile),
            loadClasses(profile.user_id),
            loadRecentActivity(profile.user_id),
            loadResourceLibrary(profile)
        ]);
        
        // Hide loading, show dashboard
        document.getElementById('loading').style.display = 'none';
        document.getElementById('dashboard').style.display = 'block';
        
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
        showError('Error loading dashboard. Please refresh the page.');
    }
}

/**
 * Load teacher information
 */
async function loadTeacherInfo(profile) {
    // Update welcome message
    const teacherNameEl = document.getElementById('teacherName');
    if (teacherNameEl) {
        const name = profile.first_name || profile.display_name || 'Teacher';
        teacherNameEl.textContent = name;
    }
    
    // Update school
    const schoolEl = document.getElementById('teacherSchool');
    if (schoolEl && profile.school_name) {
        schoolEl.textContent = profile.school_name;
    }
}

/**
 * Load teacher's classes
 */
async function loadClasses(teacherId) {
    try {
        const { data: classes, error } = await supabaseClient
            .from('teacher_classes')
            .select(`
                *,
                student_count:class_students(count)
            `)
            .eq('teacher_id', teacherId)
            .order('class_name');
        
        if (error) throw error;
        
        // Update stats
        const totalClassesEl = document.getElementById('totalClasses');
        if (totalClassesEl) {
            totalClassesEl.textContent = classes?.length || 0;
        }
        
        // Calculate total students
        const totalStudents = classes?.reduce((sum, cls) => sum + (cls.student_count?.[0]?.count || 0), 0) || 0;
        const totalStudentsEl = document.getElementById('totalStudents');
        if (totalStudentsEl) {
            totalStudentsEl.textContent = totalStudents;
        }
        
        // Render classes list
        renderClassesList(classes || []);
        
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

/**
 * Render classes list
 */
function renderClassesList(classes) {
    const container = document.getElementById('classesContainer');
    if (!container) return;
    
    if (classes.length === 0) {
        container.innerHTML = `
            <div style="text-align: center; padding: 3rem; color: var(--color-neutral-600);">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📚</div>
                <p style="font-size: 1.2rem; margin-bottom: 1rem;">No classes yet</p>
                <button class="btn btn-primary" onclick="showCreateClassModal()">
                    ➕ Create Your First Class
                </button>
            </div>
        `;
        return;
    }
    
    container.innerHTML = classes.map(cls => `
        <div class="class-card" style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); cursor: pointer;" onclick="openClass('${cls.id}')">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                <div>
                    <h3 style="font-size: 1.5rem; color: var(--color-primary-500); margin-bottom: 0.5rem;">${cls.class_name}</h3>
                    <div style="color: var(--color-neutral-600);">
                        ${cls.subject || ''} • Year ${cls.year_level || 'All'}
                    </div>
                </div>
                <div class="badge" style="background: var(--color-accent-100); color: var(--color-accent-700); padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600;">
                    ${cls.student_count?.[0]?.count || 0} students
                </div>
            </div>
            <div style="font-size: 0.9rem; color: var(--color-neutral-500);">
                Period: ${cls.period || 'Not set'} • Room: ${cls.room || 'Not set'}
            </div>
        </div>
    `).join('');
}

/**
 * Load recent activity
 */
async function loadRecentActivity(teacherId) {
    // For now, show placeholder
    // In production, query actual activity logs
    const container = document.getElementById('recentActivity');
    if (!container) return;
    
    container.innerHTML = `
        <div style="color: var(--color-neutral-600); padding: 1rem;">
            <p>📝 No recent activity</p>
        </div>
    `;
}

/**
 * Load resource library filtered by teacher's subjects
 */
async function loadResourceLibrary(profile) {
    try {
        let query = supabaseClient
            .from('graphrag_resources')
            .select('*')
            .eq('is_active', true)
            .order('created_at', { ascending: false })
            .limit(10);
        
        // Filter by teacher's subjects if available
        if (profile.subjects_taught) {
            // TODO: Filter by subjects
        }
        
        const { data: resources, error } = await query;
        
        if (error) throw error;
        
        // Update count
        const countEl = document.getElementById('resourcesAssigned');
        if (countEl) {
            countEl.textContent = resources?.length || 0;
        }
        
        renderResourceLibrary(resources || []);
        
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

/**
 * Render resource library
 */
function renderResourceLibrary(resources) {
    const container = document.getElementById('resourceLibrary');
    if (!container) return;
    
    if (resources.length === 0) {
        container.innerHTML = `
            <div style="text-align: center; padding: 2rem; color: var(--color-neutral-600);">
                <p>No resources found. Browse the <a href="/resource-hub.html">Resource Hub</a>!</p>
            </div>
        `;
        return;
    }
    
    container.innerHTML = resources.slice(0, 6).map(resource => `
        <div class="resource-card" style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
            <h4 style="color: var(--color-primary-500); margin-bottom: 0.5rem;">${resource.title}</h4>
            <p style="font-size: 0.9rem; color: var(--color-neutral-600); margin-bottom: 1rem;">${resource.description?.substring(0, 100)}...</p>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem;">
                ${resource.subject ? `<span class="badge" style="background: var(--color-secondary-100); color: var(--color-secondary-700); padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem;">${resource.subject}</span>` : ''}
                ${resource.level ? `<span class="badge" style="background: var(--color-neutral-100); color: var(--color-neutral-700); padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem;">${resource.level}</span>` : ''}
            </div>
            <button class="btn btn-sm btn-primary" onclick="assignResource('${resource.id}')">
                📋 Assign to Class
            </button>
        </div>
    `).join('');
}

/**
 * Show create class modal
 */
function showCreateClassModal() {
    alert('Create Class feature coming soon! For now, classes are managed through your school\'s admin portal.');
}

/**
 * Sync with KAMAR
 */
function syncKAMAR() {
    if (!currentTeacher?.kamar_sync_enabled) {
        alert('KAMAR sync not enabled. Please update your profile settings.');
        return;
    }
    
    alert('KAMAR sync feature coming soon! This will import your classes and students automatically.');
}

/**
 * Open class details
 */
function openClass(classId) {
    window.location.href = `/teachers/class.html?id=${classId}`;
}

/**
 * Assign resource to class
 */
function assignResource(resourceId) {
    alert('Resource assignment coming soon! You\'ll be able to assign resources to specific classes.');
}

/**
 * Show error message
 */
function showError(message) {
    const loading = document.getElementById('loading');
    if (loading) {
        loading.innerHTML = `
            <div style="text-align: center; padding: 4rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">⚠️</div>
                <p style="font-size: 1.2rem; color: var(--color-neutral-600); margin-bottom: 2rem;">${message}</p>
                <button class="btn btn-primary" onclick="window.location.reload()">
                    🔄 Refresh Page
                </button>
            </div>
        `;
    }
}

/**
 * Logout function
 */
async function logout() {
    const confirmed = confirm('Are you sure you want to log out?');
    if (!confirmed) return;
    
    try {
        await supabaseClient.auth.signOut();
        window.location.href = '/';
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
        alert('Error logging out. Please try again.');
    }
}

// Console log


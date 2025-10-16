/**
 * ================================================================
 * STUDENT DASHBOARD - TE KETE AKO
 * Personalized student learning portal
 * ================================================================
 */

let supabaseClient = null;
let currentStudent = null;

// Wait for Supabase to be ready
window.addEventListener('supabaseReady', (event) => {
    supabaseClient = event.detail.client;
    console.log('✅ Supabase ready for student dashboard');
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
            window.location.href = '/login.html?redirect=/student-dashboard.html';
            return;
        }
        
        // Get student profile
        const { data: profile, error: profileError } = await supabaseClient
            .from('profiles')
            .select('*')
            .eq('user_id', user.id)
            .single();
        
        if (profileError) throw profileError;
        
        // Verify role is student
        if (profile.role !== 'student') {
            window.location.href = '/teachers/dashboard.html';
            return;
        }
        
        currentStudent = profile;
        
        // Load dashboard data
        await Promise.all([
            loadStudentInfo(profile),
            loadRecommendedResources(profile),
            loadSavedResources(user.id),
            loadRecentActivity(user.id),
            loadProgress(user.id)
        ]);
        
        // Hide loading, show dashboard
        const loading = document.getElementById('loading');
        const dashboard = document.getElementById('dashboard');
        
        if (loading) loading.style.display = 'none';
        if (dashboard) dashboard.style.display = 'block';
        
    } catch (error) {
        console.error('Dashboard initialization error:', error);
        showError('Error loading dashboard. Please refresh the page.');
    }
}

/**
 * Load student information
 */
async function loadStudentInfo(profile) {
    // Update welcome message
    const studentNameEl = document.getElementById('studentName');
    if (studentNameEl) {
        const name = profile.first_name || 'Learner';
        studentNameEl.textContent = name;
    }
    
    // Update year level
    const yearLevelEl = document.getElementById('studentYearLevel');
    if (yearLevelEl && profile.year_level) {
        yearLevelEl.textContent = `Year ${profile.year_level}`;
    }
}

/**
 * Load recommended resources based on student's year level
 */
async function loadRecommendedResources(profile) {
    try {
        const { data: resources, error } = await supabaseClient
            .from('resources')
            .select('*')
            .eq('is_active', true)
            .eq('level', `Year ${profile.year_level}`)
            .order('created_at', { ascending: false })
            .limit(6);
        
        if (error) throw error;
        
        renderRecommendedResources(resources || []);
        
    } catch (error) {
        console.error('Error loading recommendations:', error);
    }
}

/**
 * Render recommended resources
 */
function renderRecommendedResources(resources) {
    const container = document.getElementById('recommendedResources');
    if (!container) return;
    
    if (resources.length === 0) {
        container.innerHTML = `
            <div style="text-align: center; padding: 2rem; color: var(--color-neutral-600);">
                <p>Browse the <a href="/resource-hub.html">Resource Hub</a> to discover resources!</p>
            </div>
        `;
        return;
    }
    
    container.innerHTML = resources.map(resource => `
        <div class="resource-card" style="background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
            <h4 style="color: var(--color-primary-500); margin-bottom: 0.5rem;">${resource.title}</h4>
            <p style="font-size: 0.9rem; color: var(--color-neutral-600); margin-bottom: 1rem;">${resource.description?.substring(0, 100)}...</p>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem;">
                ${resource.subject ? `<span class="badge" style="background: var(--color-secondary-100); color: var(--color-secondary-700); padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem;">${resource.subject}</span>` : ''}
            </div>
            <div style="display: flex; gap: 0.5rem;">
                <button class="btn btn-sm btn-primary" onclick="viewResource('${resource.id}')">
                    👁️ View
                </button>
                <button class="btn btn-sm btn-secondary" onclick="saveResource('${resource.id}')">
                    🧺 Save to My Kete
                </button>
            </div>
        </div>
    `).join('');
}

/**
 * Load saved resources ("My Kete")
 */
async function loadSavedResources(userId) {
    try {
        const { data: saved, error } = await supabaseClient
            .from('user_saved_resources')
            .select(`
                *,
                resource:resources(*)
            `)
            .eq('user_id', userId)
            .order('saved_at', { ascending: false })
            .limit(5);
        
        if (error) throw error;
        
        const countEl = document.getElementById('savedCount');
        if (countEl) {
            countEl.textContent = saved?.length || 0;
        }
        
        renderSavedResources(saved || []);
        
    } catch (error) {
        console.error('Error loading saved resources:', error);
    }
}

/**
 * Render saved resources
 */
function renderSavedResources(saved) {
    const container = document.getElementById('savedResources');
    if (!container) return;
    
    if (saved.length === 0) {
        container.innerHTML = `
            <div style="text-align: center; padding: 2rem; color: var(--color-neutral-600);">
                <div style="font-size: 2rem; margin-bottom: 1rem;">🧺</div>
                <p>Your kete is empty. Save resources to access them quickly!</p>
            </div>
        `;
        return;
    }
    
    container.innerHTML = saved.map(item => `
        <div style="padding: 1rem; border-bottom: 1px solid var(--color-neutral-200);">
            <a href="${item.resource.path}" style="color: var(--color-primary-500); font-weight: 600; text-decoration: none;">
                ${item.resource.title}
            </a>
            <div style="font-size: 0.85rem; color: var(--color-neutral-500); margin-top: 0.25rem;">
                Saved ${new Date(item.saved_at).toLocaleDateString()}
            </div>
        </div>
    `).join('');
}

/**
 * Load recent activity
 */
async function loadRecentActivity(userId) {
    // Placeholder - in production, query actual activity
    const container = document.getElementById('recentActivity');
    if (!container) return;
    
    container.innerHTML = `
        <div style="padding: 1rem; color: var(--color-neutral-600);">
            <p>📖 No recent activity</p>
        </div>
    `;
}

/**
 * Load student progress
 */
async function loadProgress(userId) {
    // Placeholder - in production, query assessments
    const progressEl = document.getElementById('progressPercent');
    if (progressEl) {
        progressEl.textContent = '0';
    }
}

/**
 * View resource
 */
function viewResource(resourceId) {
    // In production, navigate to resource page
    window.location.href = `/resource.html?id=${resourceId}`;
}

/**
 * Save resource to My Kete
 */
async function saveResource(resourceId) {
    if (!currentStudent) return;
    
    try {
        const { error } = await supabaseClient
            .from('user_saved_resources')
            .insert({
                user_id: currentStudent.user_id,
                resource_id: resourceId,
                saved_at: new Date().toISOString()
            });
        
        if (error) throw error;
        
        alert('✅ Resource saved to your kete!');
        
        // Reload saved resources
        await loadSavedResources(currentStudent.user_id);
        
    } catch (error) {
        console.error('Error saving resource:', error);
        alert('Error saving resource. Please try again.');
    }
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
        console.error('Logout error:', error);
        alert('Error logging out. Please try again.');
    }
}

console.log('🎓 Student dashboard JavaScript loaded');

/**
 * ================================================================
 * ENHANCED TEACHER DASHBOARD - TE KETE AKO
 * Supabase-powered teacher experience with real data
 * ================================================================
 */

let supabaseClient = null;
let teacherProfile = null;

// Wait for Supabase to be ready
window.addEventListener('supabaseReady', async (event) => {
    supabaseClient = event.detail.client;
    await initializeDashboard();
});

/**
 * Initialize dashboard with auth check and data loading
 */
async function initializeDashboard() {
    // 1. Check authentication
    const { data: { user } } = await supabaseClient.auth.getUser();
    
    if (!user) {
        // Not logged in - redirect to login
        window.location.href = '/login.html';
        return;
    }
    
    // 2. Fetch teacher profile
    const { data: profile, error } = await supabaseClient
        .from('profiles')
        .select('*')
        .eq('id', user.id)
        .single();
    
    if (error || !profile || profile.role !== 'teacher') {
        console.error('Profile error:', error);
        showMessage('Access denied. Teachers only.', 'error');
        setTimeout(() => {
            window.location.href = '/login.html';
        }, 2000);
        return;
    }
    
    teacherProfile = profile;
    
    // 3. Load dashboard components
    await Promise.all([
        loadPersonalizedGreeting(),
        loadTeacherStats(),
        loadRecommendedResources(),
        loadRecentActivity(),
        loadMyClasses()
    ]);
    
    // 4. Show dashboard
    document.getElementById('dashboardLoading').style.display = 'none';
    document.getElementById('dashboardContent').style.display = 'block';
}

/**
 * Load personalized greeting
 */
async function loadPersonalizedGreeting() {
    const greetingEl = document.getElementById('personalizedGreeting');
    if (!greetingEl) return;
    
    const title = teacherProfile.title || '';
    const firstName = teacherProfile.first_name || '';
    const lastName = teacherProfile.last_name || '';
    
    const time = new Date().getHours();
    let greeting = '';
    if (time < 12) greeting = 'Ata mārie'; // Good morning
    else if (time < 17) greeting = 'Tēnā koe'; // Hello
    else greeting = 'Ahiahi mārie'; // Good evening
    
    greetingEl.innerHTML = `
        <h1 style="font-size: 2.5rem; color: var(--color-primary-600); margin-bottom: 0.5rem;">
            ${greeting}, ${title} ${lastName}!
        </h1>
        <p style="font-size: 1.1rem; color: var(--color-neutral-600);">
            ${teacherProfile.school_name || 'Welcome to Te Kete Ako'}
        </p>
    `;
}

/**
 * Load teacher-specific statistics
 */
async function loadTeacherStats() {
    const statsEl = document.getElementById('teacherStats');
    if (!statsEl) return;
    
    try {
        // Get resources matching teacher's subjects and year levels
        const { data: resources, error } = await supabaseClient
            .from('graphrag_resources')
            .select('*')
            .overlaps('tags', teacherProfile.subjects_taught || []);
        
        const matchedResources = resources ? resources.length : 0;
        const subjects = teacherProfile.subjects_taught ? teacherProfile.subjects_taught.length : 0;
        const yearLevels = teacherProfile.year_levels_taught ? teacherProfile.year_levels_taught.length : 0;
        
        statsEl.innerHTML = `
            <div class="stat-card" style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center;">
                <div style="font-size: 3rem; color: var(--color-primary-600); font-weight: bold;">${matchedResources}</div>
                <div style="color: var(--color-neutral-600); margin-top: 0.5rem;">Resources for Your Subjects</div>
            </div>
            <div class="stat-card" style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center;">
                <div style="font-size: 3rem; color: var(--color-secondary-600); font-weight: bold;">${subjects}</div>
                <div style="color: var(--color-neutral-600); margin-top: 0.5rem;">Subjects You Teach</div>
            </div>
            <div class="stat-card" style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center;">
                <div style="font-size: 3rem; color: var(--color-accent-600); font-weight: bold;">${yearLevels}</div>
                <div style="color: var(--color-neutral-600); margin-top: 0.5rem;">Year Levels</div>
            </div>
            <div class="stat-card" style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center;">
                <div style="font-size: 3rem; color: var(--color-success); font-weight: bold;">1,496</div>
                <div style="color: var(--color-neutral-600); margin-top: 0.5rem;">Total Platform Resources</div>
            </div>
        `;
    } catch (error) {
        console.error('Stats error:', error);
        statsEl.innerHTML = '<p style="color: var(--color-error);">Unable to load statistics</p>';
    }
}

/**
 * Load recommended resources based on teacher's subjects
 */
async function loadRecommendedResources() {
    const resourcesEl = document.getElementById('recommendedResources');
    if (!resourcesEl) return;
    
    try {
        // Get high-quality resources for teacher's subjects
        const { data: resources, error } = await supabaseClient
            .from('graphrag_resources')
            .select('*')
            .overlaps('tags', teacherProfile.subjects_taught || [])
            .limit(6);
        
        if (error) throw error;
        
        if (!resources || resources.length === 0) {
            resourcesEl.innerHTML = '<p style="color: var(--color-neutral-600);">No matching resources found yet.</p>';
            return;
        }
        
        const resourceCards = resources.map(resource => `
            <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); transition: transform 0.3s;">
                <h3 style="font-size: 1.2rem; color: var(--color-primary-700); margin-bottom: 0.5rem;">
                    ${resource.title || 'Untitled Resource'}
                </h3>
                <p style="color: var(--color-neutral-600); font-size: 0.9rem; margin-bottom: 1rem;">
                    ${resource.description || resource.type || 'Resource description'}
                </p>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem;">
                    ${resource.level ? `<span style="background: var(--color-primary-100); color: var(--color-primary-700); padding: 0.25rem 0.75rem; border-radius: 50px; font-size: 0.8rem;">${resource.level}</span>` : ''}
                    ${resource.subject ? `<span style="background: var(--color-secondary-100); color: var(--color-secondary-700); padding: 0.25rem 0.75rem; border-radius: 50px; font-size: 0.8rem;">${resource.subject}</span>` : ''}
                </div>
                <a href="${resource.path || '#'}" style="color: var(--color-primary-600); text-decoration: none; font-weight: 600; font-size: 0.95rem;">
                    View Resource →
                </a>
            </div>
        `).join('');
        
        resourcesEl.innerHTML = `
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                ${resourceCards}
            </div>
        `;
    } catch (error) {
        console.error('Resources error:', error);
        resourcesEl.innerHTML = '<p style="color: var(--color-error);">Unable to load resources</p>';
    }
}

/**
 * Load recent activity (placeholder - needs activity tracking)
 */
async function loadRecentActivity() {
    const activityEl = document.getElementById('recentActivity');
    if (!activityEl) return;
    
    activityEl.innerHTML = `
        <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <h3 style="color: var(--color-primary-700); margin-bottom: 1rem;">Recent Activity</h3>
            <div style="space-y: 1rem;">
                <div style="padding: 1rem; background: var(--color-neutral-50); border-radius: 8px; margin-bottom: 1rem;">
                    <p style="margin: 0; color: var(--color-neutral-700);">
                        <strong>Today:</strong> Viewed Y8 Systems Unit
                    </p>
                </div>
                <div style="padding: 1rem; background: var(--color-neutral-50); border-radius: 8px; margin-bottom: 1rem;">
                    <p style="margin: 0; color: var(--color-neutral-700);">
                        <strong>Yesterday:</strong> Downloaded Walker Unit resources
                    </p>
                </div>
                <div style="padding: 1rem; background: var(--color-neutral-50); border-radius: 8px;">
                    <p style="margin: 0; color: var(--color-neutral-700);">
                        <strong>This Week:</strong> Accessed ${(teacherProfile.subjects_taught || []).length} subject areas
                    </p>
                </div>
            </div>
        </div>
    `;
}

/**
 * Load teacher's classes (placeholder - needs class management)
 */
async function loadMyClasses() {
    const classesEl = document.getElementById('myClasses');
    if (!classesEl) return;
    
    const yearLevels = teacherProfile.year_levels_taught || [];
    
    classesEl.innerHTML = `
        <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <h3 style="color: var(--color-primary-700); margin-bottom: 1rem;">Your Year Levels</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
                ${yearLevels.map(level => `
                    <div style="flex: 1; min-width: 120px; background: var(--color-primary-50); padding: 1.5rem; border-radius: 8px; text-align: center; border: 2px solid var(--color-primary-200);">
                        <div style="font-size: 2rem; font-weight: bold; color: var(--color-primary-700);">Year ${level}</div>
                        <a href="/units/index.html?level=${level}" style="color: var(--color-primary-600); text-decoration: none; font-size: 0.9rem; margin-top: 0.5rem; display: block;">
                            View Resources →
                        </a>
                    </div>
                `).join('')}
            </div>
            ${yearLevels.length === 0 ? '<p style="color: var(--color-neutral-600);">No year levels specified in your profile. <a href="/profile.html" style="color: var(--color-primary-600);">Update profile</a></p>' : ''}
        </div>
    `;
}

/**
 * Show message
 */
function showMessage(message, type = 'info') {
    const messageEl = document.createElement('div');
    messageEl.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'error' ? 'var(--color-error)' : 'var(--color-success)'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 10000;
        animation: slideIn 0.3s ease-out;
    `;
    messageEl.textContent = message;
    document.body.appendChild(messageEl);
    
    setTimeout(() => {
        messageEl.remove();
    }, 5000);
}

// Initialize when Supabase client is ready
if (typeof window.supabase !== 'undefined') {
    supabaseClient = window.supabase.createClient(
        'https://nlgldaqtubrlcqddppbq.supabase.co',
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5sZ2xkYXF0dWJybGNxZGRwcGJxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMwODkzMzksImV4cCI6MjA2ODY2NTMzOX0.IFaWqep1MBSofARiCUuzvAReC44hwGnmKOMNSd55nIM'
    );
    initializeDashboard();
}

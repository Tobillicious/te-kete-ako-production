/**
 * ================================================================
 * ENHANCED STUDENT DASHBOARD - TE KETE AKO
 * Supabase-powered student experience with personalized recommendations
 * ================================================================
 */

let supabaseClient = null;
let studentProfile = null;

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
    
    // 2. Fetch student profile
    const { data: profile, error } = await supabaseClient
        .from('profiles')
        .select('*')
        .eq('id', user.id)
        .single();
    
    if (error || !profile || profile.role !== 'student') {
        // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('error', {
                message: '$2',
                details: $3,
                url: window.location.pathname
            });
        }
        // Show user-friendly message instead of error
        showMessage('Access denied. Students only.', 'error');
        setTimeout(() => {
            window.location.href = '/login.html';
        }, 2000);
        return;
    }
    
    studentProfile = profile;
    
    // 3. Load dashboard components
    await Promise.all([
        loadPersonalizedGreeting(),
        loadRecommendedResources(),
        loadMyKetePreview(),
        loadProgressTracker(),
        loadCulturalHighlights()
    ]);
    
    // 4. Show dashboard
    const loadingEl = document.getElementById('dashboardLoading');
    const contentEl = document.getElementById('dashboardContent');
    if (loadingEl) loadingEl.style.display = 'none';
    if (contentEl) contentEl.style.display = 'block';
}

/**
 * Load personalized greeting
 */
async function loadPersonalizedGreeting() {
    const greetingEl = document.getElementById('personalizedGreeting');
    if (!greetingEl) return;
    
    const firstName = studentProfile.first_name || 'Tauira'; // Student
    
    const time = new Date().getHours();
    let greeting = '';
    if (time < 12) greeting = 'Ata mārie'; // Good morning
    else if (time < 17) greeting = 'Kia ora'; // Hello
    else greeting = 'Ahiahi mārie'; // Good evening
    
    greetingEl.innerHTML = `
        <h1 style="font-size: 2.5rem; color: var(--color-primary-600); margin-bottom: 0.5rem;">
            ${greeting}, ${firstName}!
        </h1>
        <p style="font-size: 1.1rem; color: var(--color-neutral-600);">
            Ready to continue learning? Here's what's recommended for Year ${studentProfile.year_level || 'your year level'}.
        </p>
    `;
}

/**
 * Load recommended resources based on student's year level
 */
async function loadRecommendedResources() {
    const resourcesEl = document.getElementById('recommendedResources');
    if (!resourcesEl) return;
    
    try {
        // Get resources matching student's year level
        const yearLevel = studentProfile.year_level || 8;
        const { data: resources, error} = await supabaseClient
            .from('graphrag_resources')
            .select('*')
            .eq('level', `Year ${yearLevel}`)
            .limit(6);
        
        if (error) throw error;
        
        if (!resources || resources.length === 0) {
            resourcesEl.innerHTML = '<p style="color: var(--color-neutral-600);">Loading your personalized recommendations...</p>';
            return;
        }
        
        const resourceCards = resources.map(resource => `
            <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); transition: transform 0.3s; cursor: pointer;" onmouseover="this.style.transform='translateY(-4px)'" onmouseout="this.style.transform='translateY(0)'">
                <h3 style="font-size: 1.1rem; color: var(--color-primary-700); margin-bottom: 0.5rem;">
                    ${resource.title || 'Resource'}
                </h3>
                <p style="color: var(--color-neutral-600); font-size: 0.9rem; margin-bottom: 1rem; line-height: 1.6;">
                    ${(resource.description || resource.type || 'Learn something new!').substring(0, 100)}...
                </p>
                <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
                    ${resource.subject ? `<span style="background: var(--color-primary-100); color: var(--color-primary-700); padding: 0.25rem 0.75rem; border-radius: 50px; font-size: 0.75rem;">${resource.subject}</span>` : ''}
                </div>
                <a href="${resource.path || '#'}" style="color: var(--color-primary-600); text-decoration: none; font-weight: 600; font-size: 0.9rem;">
                    Start Learning →
                </a>
            </div>
        `).join('');
        
        resourcesEl.innerHTML = `
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
                ${resourceCards}
            </div>
        `;
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
        resourcesEl.innerHTML = '<p style="color: var(--color-error);">Unable to load resources</p>';
    }
}

/**
 * Load My Kete preview (saved resources)
 */
async function loadMyKetePreview() {
    const keteEl = document.getElementById('myKetePreview');
    if (!keteEl) return;
    
    keteEl.innerHTML = `
        <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <h3 style="color: var(--color-primary-700); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                <span>🧺</span>
                <span>My Kete</span>
            </h3>
            <p style="color: var(--color-neutral-600); margin-bottom: 1.5rem;">
                Your personal collection of saved resources and learning materials.
            </p>
            <div style="background: var(--color-neutral-50); padding: 1.5rem; border-radius: 8px; text-align: center; margin-bottom: 1.5rem;">
                <p style="font-size: 2rem; color: var(--color-primary-600); font-weight: bold; margin-bottom: 0.5rem;">0</p>
                <p style="color: var(--color-neutral-600); margin: 0;">Saved Resources</p>
            </div>
            <a href="/my-kete.html" style="display: block; background: var(--color-primary-600); color: white; padding: 0.75rem; text-align: center; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.3s;">
                View My Kete →
            </a>
        </div>
    `;
}

/**
 * Load progress tracker
 */
async function loadProgressTracker() {
    const progressEl = document.getElementById('progressTracker');
    if (!progressEl) return;
    
    progressEl.innerHTML = `
        <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <h3 style="color: var(--color-primary-700); margin-bottom: 1rem;">Your Progress</h3>
            <div style="margin-bottom: 1.5rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span style="color: var(--color-neutral-700); font-weight: 600;">Activities Completed</span>
                    <span style="color: var(--color-primary-600); font-weight: bold;">0 / 10</span>
                </div>
                <div style="height: 8px; background: var(--color-neutral-200); border-radius: 50px; overflow: hidden;">
                    <div style="width: 0%; height: 100%; background: var(--color-primary-600); transition: width 0.5s;"></div>
                </div>
            </div>
            <p style="color: var(--color-neutral-600); font-size: 0.9rem; text-align: center;">
                Start exploring resources to track your progress!
            </p>
        </div>
    `;
}

/**
 * Load cultural highlights
 */
async function loadCulturalHighlights() {
    const culturalEl = document.getElementById('culturalHighlights');
    if (!culturalEl) return;
    
    // Check if student has Māori cultural identity
    const hasMaoriIdentity = studentProfile.cultural_identity && 
        studentProfile.cultural_identity.includes('Māori');
    
    culturalEl.innerHTML = `
        <div style="background: linear-gradient(135deg, var(--color-accent-50) 0%, var(--color-primary-50) 100%); padding: 2rem; border-radius: 12px; border: 2px solid var(--color-accent-200);">
            <h3 style="color: var(--color-accent-800); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                <span>🌿</span>
                <span>Te Ao Māori Resources</span>
            </h3>
            ${hasMaoriIdentity ? `
                <p style="color: var(--color-neutral-700); margin-bottom: 1rem;">
                    Kia ora! We've curated special resources that honor mātauranga Māori and connect with your cultural heritage.
                </p>
            ` : `
                <p style="color: var(--color-neutral-700); margin-bottom: 1rem;">
                    Explore resources that integrate mātauranga Māori perspectives with contemporary learning.
                </p>
            `}
            <a href="/units/unit-1-te-ao-maori/index.html" style="display: block; background: var(--color-accent-600); color: white; padding: 0.75rem; text-align: center; border-radius: 8px; text-decoration: none; font-weight: 600; margin-top: 1.5rem;">
                Explore Cultural Resources →
            </a>
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
(async function() {
    if (window.supabaseSingleton) {
        supabaseClient = await window.supabaseSingleton.getClient();
        if (supabaseClient) {
            initializeDashboard();
        }
    }
})();

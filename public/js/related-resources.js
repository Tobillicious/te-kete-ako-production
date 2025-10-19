/**
 * ================================================================
 * RELATED RESOURCES - GraphRAG-Powered Navigation
 * Automatically finds and displays related lessons, handouts, units
 * ================================================================
 */

// Supabase client
let supabaseClient = null;

// Current page metadata (will be set by lesson pages)
let currentResource = {
    title: null,
    subject: null,
    level: null,
    tags: [],
    type: null,
    path: window.location.pathname
};

// Wait for Supabase to be ready
window.addEventListener('supabaseReady', async (event) => {
    supabaseClient = event.detail.client;
    await loadRelatedResources();
});

/**
 * Set current resource metadata
 * Call this from lesson pages: setCurrentResource({ title, subject, level, tags, type })
 */
window.setCurrentResource = function(metadata) {
    currentResource = { ...currentResource, ...metadata };
    // If Supabase is already ready, load immediately
    if (supabaseClient) {
        loadRelatedResources();
    }
};

/**
 * Load all related resources
 */
async function loadRelatedResources() {
    if (!supabaseClient) {
        console.log('Supabase not ready, skipping related resources');
        return;
    }
    
    try {
        await Promise.all([
            loadRelatedLessons(),
            loadRelatedHandouts(),
            loadRelatedUnits()
        ]);
    } catch (error) {
        console.error('Error loading related resources:', error);
    }
}

/**
 * Load related lessons
 */
async function loadRelatedLessons() {
    const container = document.getElementById('related-lessons');
    if (!container) return;
    
    try {
        // Build query based on current resource
        let query = supabaseClient
            .from('graphrag_resources')
            .select('title, path, subject, level, tags')
            .eq('type', 'lesson')
            .eq('is_active', true);
        
        // Filter by subject if available
        if (currentResource.subject) {
            query = query.or(`subject.eq.${currentResource.subject},subject.ilike.%${currentResource.subject}%`);
        }
        
        // Filter by level if available
        if (currentResource.level) {
            query = query.or(`level.eq.${currentResource.level},level.ilike.%${currentResource.level}%`);
        }
        
        const { data, error } = await query.limit(4);
        
        if (error) throw error;
        
        if (!data || data.length === 0) {
            container.innerHTML = '<div style="color: var(--color-neutral-500); font-size: 0.9rem;">No related lessons found</div>';
            return;
        }
        
        // Filter out current page
        const filtered = data.filter(item => item.path !== currentResource.path).slice(0, 3);
        
        container.innerHTML = filtered.map(lesson => `
            <a href="${lesson.path}" class="related-item">
                <div class="related-item-title">${lesson.title}</div>
                <div class="related-item-meta">
                    ${lesson.subject ? `<span class="related-badge">${lesson.subject}</span>` : ''}
                    ${lesson.level ? `<span class="related-badge">${lesson.level}</span>` : ''}
                </div>
            </a>
        `).join('');
        
    } catch (error) {
        console.error('Error loading related lessons:', error);
        container.innerHTML = '<div style="color: var(--color-neutral-500); font-size: 0.9rem;">Unable to load related lessons</div>';
    }
}

/**
 * Load related handouts
 */
async function loadRelatedHandouts() {
    const container = document.getElementById('related-handouts');
    if (!container) return;
    
    try {
        let query = supabaseClient
            .from('graphrag_resources')
            .select('title, path, subject, level')
            .eq('type', 'handout')
            .eq('is_active', true);
        
        // Filter by subject
        if (currentResource.subject) {
            query = query.or(`subject.eq.${currentResource.subject},subject.ilike.%${currentResource.subject}%`);
        }
        
        const { data, error } = await query.limit(5);
        
        if (error) throw error;
        
        if (!data || data.length === 0) {
            container.innerHTML = '<div style="color: var(--color-neutral-500); font-size: 0.9rem;">No related handouts found</div>';
            return;
        }
        
        container.innerHTML = data.slice(0, 4).map(handout => `
            <a href="${handout.path}" class="related-item" target="_blank">
                <div class="related-item-title">
                    📄 ${handout.title}
                </div>
                <div class="related-item-meta">
                    ${handout.subject ? `<span class="related-badge">${handout.subject}</span>` : ''}
                    ${handout.level ? `<span class="related-badge">${handout.level}</span>` : ''}
                </div>
            </a>
        `).join('');
        
    } catch (error) {
        console.error('Error loading related handouts:', error);
        container.innerHTML = '<div style="color: var(--color-neutral-500); font-size: 0.9rem;">Unable to load related handouts</div>';
    }
}

/**
 * Load related units
 */
async function loadRelatedUnits() {
    const container = document.getElementById('related-units');
    if (!container) return;
    
    try {
        let query = supabaseClient
            .from('graphrag_resources')
            .select('title, path, description, subject, level')
            .eq('type', 'unit-plan')
            .eq('is_active', true);
        
        // Filter by subject
        if (currentResource.subject) {
            query = query.or(`subject.eq.${currentResource.subject},subject.ilike.%${currentResource.subject}%`);
        }
        
        const { data, error } = await query.limit(3);
        
        if (error) throw error;
        
        if (!data || data.length === 0) {
            container.innerHTML = '<div style="color: var(--color-neutral-500); font-size: 0.9rem;">No related units found</div>';
            return;
        }
        
        container.innerHTML = data.slice(0, 2).map(unit => `
            <a href="${unit.path}" class="related-item">
                <div class="related-item-title">
                    📚 ${unit.title}
                </div>
                <div class="related-item-meta">
                    ${unit.subject ? `<span class="related-badge">${unit.subject}</span>` : ''}
                    ${unit.level ? `<span class="related-badge">${unit.level}</span>` : ''}
                </div>
            </a>
        `).join('');
        
    } catch (error) {
        console.error('Error loading related units:', error);
        container.innerHTML = '<div style="color: var(--color-neutral-500); font-size: 0.9rem;">Unable to load related units</div>';
    }
}

/**
 * Advanced: Find resources by tag similarity
 */
async function findBySimilarTags(tags, type, limit = 3) {
    if (!tags || tags.length === 0) return [];
    
    try {
        const { data, error } = await supabaseClient
            .from('graphrag_resources')
            .select('title, path, subject, level, tags')
            .eq('type', type)
            .eq('is_active', true)
            .limit(limit * 2);
        
        if (error) throw error;
        
        // Score by tag overlap
        const scored = data.map(item => {
            const overlap = (item.tags || []).filter(tag => tags.includes(tag)).length;
            return { ...item, score: overlap };
        });
        
        // Sort by score and return top results
        return scored
            .sort((a, b) => b.score - a.score)
            .filter(item => item.score > 0)
            .slice(0, limit);
            
    } catch (error) {
        console.error('Error finding by tags:', error);
        return [];
    }
}

console.log('✅ Related resources component loaded');


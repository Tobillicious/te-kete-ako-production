/**
 * Save Resource Functionality
 * Allows users to save resources to "My Kete" via Supabase
 */

// Save a resource to user's kete
async function saveResource(resourceUrl, resourceTitle, resourceType = 'handout') {
    try {
        // Check if user is logged in
        const { data: { user } } = await supabase.auth.getUser();
        
        if (!user) {
            // Redirect to login with return URL
            window.location.href = `/login.html?return=${encodeURIComponent(window.location.pathname)}`;
            return;
        }

        // Check if already saved
        const { data: existing } = await supabase
            .from('user_saved_resources')
            .select('id')
            .eq('user_id', user.id)
            .eq('resource_url', resourceUrl)
            .single();

        if (existing) {
            showNotification('✅ Already in your kete!', 'info');
            return;
        }

        // Save to database
        const { error } = await supabase
            .from('user_saved_resources')
            .insert({
                user_id: user.id,
                resource_url: resourceUrl,
                resource_title: resourceTitle,
                resource_type: resourceType,
                saved_at: new Date().toISOString()
            });

        if (error) throw error;

        showNotification('⭐ Saved to My Kete!', 'success');
        
        // Update button state if on page
        updateSaveButtonState(resourceUrl, true);
        
    } catch (error) {
        console.error('Error saving resource:', error);
        showNotification('❌ Failed to save. Please try again.', 'error');
    }
}

// Remove a resource from user's kete
async function unsaveResource(resourceUrl) {
    try {
        const { data: { user } } = await supabase.auth.getUser();
        
        if (!user) return;

        const { error } = await supabase
            .from('user_saved_resources')
            .delete()
            .eq('user_id', user.id)
            .eq('resource_url', resourceUrl);

        if (error) throw error;

        showNotification('🗑️ Removed from My Kete', 'info');
        updateSaveButtonState(resourceUrl, false);
        
    } catch (error) {
        console.error('Error removing resource:', error);
        showNotification('❌ Failed to remove. Please try again.', 'error');
    }
}

// Check if a resource is already saved
async function isResourceSaved(resourceUrl) {
    try {
        const { data: { user } } = await supabase.auth.getUser();
        
        if (!user) return false;

        const { data, error } = await supabase
            .from('user_saved_resources')
            .select('id')
            .eq('user_id', user.id)
            .eq('resource_url', resourceUrl)
            .single();

        return !!data && !error;
        
    } catch (error) {
        return false;
    }
}

// Update save button visual state
function updateSaveButtonState(resourceUrl, isSaved) {
    const saveBtn = document.querySelector(`[data-resource-url="${resourceUrl}"]`);
    if (!saveBtn) return;

    if (isSaved) {
        saveBtn.innerHTML = '✅ Saved';
        saveBtn.classList.add('saved');
        saveBtn.onclick = () => unsaveResource(resourceUrl);
    } else {
        saveBtn.innerHTML = '⭐ Save to My Kete';
        saveBtn.classList.remove('saved');
        saveBtn.onclick = () => {
            const title = saveBtn.dataset.resourceTitle || document.title;
            const type = saveBtn.dataset.resourceType || 'handout';
            saveResource(resourceUrl, title, type);
        };
    }
}

// Show notification to user
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `save-notification save-notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#2C5F41' : type === 'error' ? '#dc3545' : '#6c757d'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 9999;
        font-weight: 500;
        animation: slideIn 0.3s ease-out;
    `;

    document.body.appendChild(notification);

    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add animation CSS if not already present
if (!document.getElementById('save-resource-styles')) {
    const style = document.createElement('style');
    style.id = 'save-resource-styles';
    style.textContent = `
        @keyframes slideIn {
            from {
                transform: translateX(400px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        @keyframes slideOut {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(400px);
                opacity: 0;
            }
        }
        .save-button {
            background: var(--color-primary);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 1rem;
        }
        .save-button:hover {
            background: var(--color-secondary);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        .save-button.saved {
            background: #28a745;
        }
        .save-button.saved:hover {
            background: #218838;
        }
    `;
    document.head.appendChild(style);
}

// Initialize save buttons on page load
document.addEventListener('DOMContentLoaded', async () => {
    // Check if we're on a resource page
    const saveButtons = document.querySelectorAll('[data-save-resource]');
    
    if (saveButtons.length > 0) {
        const currentUrl = window.location.pathname;
        const isSaved = await isResourceSaved(currentUrl);
        
        saveButtons.forEach(btn => {
            updateSaveButtonState(currentUrl, isSaved);
        });
    }
});

// Export for use in other scripts
window.saveResourceHelpers = {
    saveResource,
    unsaveResource,
    isResourceSaved,
    updateSaveButtonState,
    showNotification
};


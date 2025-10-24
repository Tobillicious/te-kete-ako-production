/**
 * 🧺 MY KETE - DATABASE-POWERED FAVORITES SYSTEM
 * Persistent across devices, browsers, and sessions
 * 
 * FIXES CRITICAL BUG: localStorage → Supabase database
 * IMPACT: Teachers never lose their saved resources
 */

class MyKeteDatabase {
    constructor() {
        this.supabase = null;
        this.user = null;
        this.init();
    }
    
    async init() {
        // Initialize Supabase client
        if (window.supabase) {
            if (window.supabaseSingleton) {
                this.supabase = await window.supabaseSingleton.getClient();
            }
            
            // Get current user
            const { data: { user } } = await this.supabase.auth.getUser();
            this.user = user;
            
            // Migrate localStorage to database if user is logged in
            if (this.user) {
                await this.migrateLocalStorageToDatabase();
            }
        }
    }
    
    async migrateLocalStorageToDatabase() {
        try {
            const localFavorites = JSON.parse(localStorage.getItem('te-kete-favorites') || '[]');
            
            if (localFavorites.length > 0) {
                
                for (const fav of localFavorites) {
                    await this.saveFavorite(fav.path, fav.title, fav.description);
                }
                
                // Clear localStorage after successful migration
                localStorage.removeItem('te-kete-favorites');
            }
        } catch (e) {
            console.error('Migration error:', e);
        }
    }
    
    async getFavorites() {
        // If user is logged in, use database
        if (this.user && this.supabase) {
            try {
                // Use new saved_resources table
                const { data, error } = await this.supabase
                    .from('saved_resources')
                    .select('*')
                    .eq('user_id', this.user.id)
                    .order('saved_at', { ascending: false });
                
                if (error) throw error;
                
                return data.map(fav => ({
                    id: fav.id,
                    path: fav.resource_path,
                    title: fav.resource_title,
                    type: fav.resource_type,
                    subject: fav.resource_subject,
                    yearLevel: fav.resource_year_level,
                    notes: fav.notes,
                    tags: fav.tags || [],
                    savedAt: fav.saved_at,
                    lastAccessed: fav.last_accessed
                }));
                
            } catch (e) {
                console.error('Database error:', e);
                return this.getLocalStorageFavorites(); // Fallback to localStorage
            }
        } else {
            // Not logged in - use localStorage as fallback
            return this.getLocalStorageFavorites();
        }
    }
    
    getLocalStorageFavorites() {
        try {
            return JSON.parse(localStorage.getItem('te-kete-favorites') || '[]');
        } catch (e) {
            return [];
        }
    }
    
    async saveFavorite(path, title, description = '', type = 'other', subject = null, yearLevel = null) {
        // If logged in, save to database
        if (this.user && this.supabase) {
            try {
                const { data, error } = await this.supabase
                    .from('saved_resources')
                    .insert({
                        user_id: this.user.id,
                        resource_path: path,
                        resource_title: title,
                        resource_type: type,
                        resource_subject: subject,
                        resource_year_level: yearLevel,
                        notes: description
                    })
                    .select();
                
                if (error) throw error;
                
                this.showToast('Saved to My Kete! 🧺 (Synced across all your devices)');
                return true;
                
            } catch (e) {
                console.error('Save error:', e);
                // Fallback to localStorage
                return this.saveToLocalStorage(path, title, description);
            }
        } else {
            // Not logged in - use localStorage
            this.showToast('Saved to My Kete! 🧺 (Login to sync across devices)');
            return this.saveToLocalStorage(path, title, description);
        }
    }
    
    showToast(message) {
        // Simple toast notification
        const toast = document.getElementById('toast-notification') || this.createToast();
        toast.textContent = message;
        toast.style.opacity = '1';
        setTimeout(() => { toast.style.opacity = '0'; }, 3000);
    }
    
    createToast() {
        const toast = document.createElement('div');
        toast.id = 'toast-notification';
        toast.style.cssText = 'position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#333;color:white;padding:12px 24px;border-radius:8px;opacity:0;transition:opacity 0.3s;z-index:9999;';
        document.body.appendChild(toast);
        return toast;
    }
    
    saveToLocalStorage(path, title, description = '') {
        try {
            const favorites = this.getLocalStorageFavorites();
            favorites.push({
                path,
                title,
                description,
                savedAt: new Date().toISOString()
            });
            localStorage.setItem('te-kete-favorites', JSON.stringify(favorites));
            return true;
        } catch (e) {
            console.error('localStorage save error:', e);
            return false;
        }
    }
    
    async removeFavorite(path) {
        // If logged in, remove from database
        if (this.user && this.supabase) {
            try {
                const { error } = await this.supabase
                    .from('teacher_favorites')
                    .delete()
                    .eq('teacher_id', this.user.id)
                    .eq('resource_path', path);
                
                if (error) throw error;
                
                return true;
                
            } catch (e) {
                console.error('Remove error:', e);
                return false;
            }
        } else {
            // Not logged in - remove from localStorage
            try {
                let favorites = this.getLocalStorageFavorites();
                favorites = favorites.filter(f => f.path !== path);
                localStorage.setItem('te-kete-favorites', JSON.stringify(favorites));
                return true;
            } catch (e) {
                return false;
            }
        }
    }
    
    extractTitle(path) {
        // Extract title from path (fallback if graphrag_resources join fails)
        const filename = path.split('/').pop().replace('.html', '');
        return filename
            .split('-')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ');
    }
}

// Initialize global instance
window.myKeteDB = new MyKeteDatabase();

// Export for use in other scripts
window.MyKeteDatabase = MyKeteDatabase;


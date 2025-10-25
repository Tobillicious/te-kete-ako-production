/**
 * Enterprise Bulk Operations - Te Kete Ako
 * Bulk operations for schools, users, and content
 * Phase 3 of Tech Stack Evolution
 */

class TeKeteBulkOperations {
    constructor() {
        this.supabase = null;
        this.selectedItems = [];
        this.operationQueue = [];
        this.init();
    }

    async init() {
        await this.initializeSupabase();
        this.setupBulkOperationHandlers();
        this.setupProgressTracking();
    }

    async initializeSupabase() {
        if (window.supabase && window.ENV) {
            if (window.supabaseSingleton) {
                this.supabase = await window.supabaseSingleton.getClient();
            }
        }
    }

    setupBulkOperationHandlers() {
        // Bulk user import
        document.addEventListener('change', (e) => {
            if (e.target.matches('#bulk-user-csv')) {
                this.handleBulkUserImport(e.target.files[0]);
            }
        });

        // Bulk resource assignment
        document.addEventListener('click', (e) => {
            if (e.target.matches('.bulk-assign-btn')) {
                this.executeBulkResourceAssignment();
            }
        });

        // Bulk user role update
        document.addEventListener('click', (e) => {
            if (e.target.matches('.bulk-role-update-btn')) {
                this.executeBulkRoleUpdate();
            }
        });

        // Bulk content operations
        document.addEventListener('click', (e) => {
            if (e.target.matches('.bulk-content-btn')) {
                this.executeBulkContentOperation();
            }
        });

        // Select all checkboxes
        document.addEventListener('change', (e) => {
            if (e.target.matches('.select-all-checkbox')) {
                this.handleSelectAll(e.target);
            }
        });

        // Individual checkbox selection
        document.addEventListener('change', (e) => {
            if (e.target.matches('.item-checkbox')) {
                this.handleItemSelection(e.target);
            }
        });
    }

    setupProgressTracking() {
        // Create progress modal
        this.progressModal = this.createProgressModal();
        document.body.appendChild(this.progressModal);
    }

    createProgressModal() {
        const modal = document.createElement('div');
        modal.id = 'bulk-operation-progress';
        modal.style.display = 'none';
        modal.innerHTML = `
            <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 9999; display: flex; align-items: center; justify-content: center;">
                <div style="background: white; border-radius: 16px; padding: 2rem; max-width: 500px; width: 90%;">
                    <h3 style="color: #1a4d2e; margin-bottom: 1rem;">Bulk Operation in Progress</h3>
                    <div id="operation-status" style="margin-bottom: 1rem; color: #6b7280;"></div>
                    <div style="width: 100%; height: 20px; background: #e5e7eb; border-radius: 10px; overflow: hidden;">
                        <div id="operation-progress" style="height: 100%; background: linear-gradient(90deg, #059669 0%, #10b981 100%); width: 0%; transition: width 0.3s ease;"></div>
                    </div>
                    <div id="operation-details" style="margin-top: 1rem; font-size: 0.9rem; color: #6b7280;"></div>
                </div>
            </div>
        `;
        return modal;
    }

    showProgress(status, progress, details) {
        this.progressModal.style.display = 'block';
        document.getElementById('operation-status').textContent = status;
        document.getElementById('operation-progress').style.width = `${progress}%`;
        document.getElementById('operation-details').textContent = details;
    }

    hideProgress() {
        this.progressModal.style.display = 'none';
    }

    // Bulk User Import
    async handleBulkUserImport(file) {
        try {
            this.showProgress('Reading CSV file...', 10, 'Parsing user data');
            
            const csvContent = await this.readFileAsText(file);
            const users = this.parseCSV(csvContent);
            
            this.showProgress('Validating users...', 30, `${users.length} users found`);
            
            // Validate users
            const validUsers = await this.validateUsers(users);
            
            this.showProgress('Importing users...', 50, `Importing ${validUsers.length} valid users`);
            
            // Import users in batches
            const batchSize = 50;
            let imported = 0;
            
            for (let i = 0; i < validUsers.length; i += batchSize) {
                const batch = validUsers.slice(i, i + batchSize);
                await this.importUserBatch(batch);
                
                imported += batch.length;
                const progress = 50 + (imported / validUsers.length * 40);
                this.showProgress('Importing users...', progress, `${imported}/${validUsers.length} users imported`);
            }
            
            this.showProgress('Complete!', 100, `${validUsers.length} users imported successfully`);
            
            setTimeout(() => {
                this.hideProgress();
                this.showSuccess(`${validUsers.length} users imported successfully!`);
            }, 2000);
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        this.hideProgress();
            this.showError('Failed to import users. Please check the CSV format.');
        }
    }

    async validateUsers(users) {
        const validUsers = [];
        
        for (const user of users) {
            if (user.email && user.name && this.isValidEmail(user.email)) {
                validUsers.push(user);
            }
        }
        
        return validUsers;
    }

    async importUserBatch(users) {
        try {
            const { error } = await this.supabase
                .from('profiles')
                .insert(users);

            if (error) throw error;
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        throw error;
        }
    }

    // Bulk Resource Assignment
    async executeBulkResourceAssignment() {
        try {
            const selectedUsers = this.getSelectedUsers();
            const selectedResources = this.getSelectedResources();
            
            if (selectedUsers.length === 0 || selectedResources.length === 0) {
                this.showError('Please select both users and resources');
                return;
            }
            
            this.showProgress('Preparing assignment...', 10, `${selectedUsers.length} users, ${selectedResources.length} resources`);
            
            const totalAssignments = selectedUsers.length * selectedResources.length;
            let completed = 0;
            
            for (const userId of selectedUsers) {
                for (const resourceId of selectedResources) {
                    await this.assignResourceToUser(userId, resourceId);
                    
                    completed++;
                    const progress = (completed / totalAssignments) * 90;
                    this.showProgress('Assigning resources...', progress, `${completed}/${totalAssignments} assignments complete`);
                }
            }
            
            this.showProgress('Complete!', 100, `${totalAssignments} assignments complete`);
            
            setTimeout(() => {
                this.hideProgress();
                this.showSuccess(`Resources assigned to ${selectedUsers.length} users!`);
            }, 2000);
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        this.hideProgress();
            this.showError('Failed to assign resources. Please try again.');
        }
    }

    async assignResourceToUser(userId, resourceId) {
        try {
            const { error } = await this.supabase
                .from('user_resources')
                .insert({
                    user_id: userId,
                    resource_id: resourceId,
                    assigned_at: new Date().toISOString()
                });

            if (error) throw error;
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        throw error;
        }
    }

    // Bulk Role Update
    async executeBulkRoleUpdate() {
        try {
            const selectedUsers = this.getSelectedUsers();
            const newRole = document.getElementById('bulk-role-select')?.value;
            
            if (selectedUsers.length === 0 || !newRole) {
                this.showError('Please select users and a role');
                return;
            }
            
            this.showProgress('Updating roles...', 10, `Updating ${selectedUsers.length} users`);
            
            for (let i = 0; i < selectedUsers.length; i++) {
                await this.updateUserRole(selectedUsers[i], newRole);
                
                const progress = ((i + 1) / selectedUsers.length) * 90;
                this.showProgress('Updating roles...', progress, `${i + 1}/${selectedUsers.length} roles updated`);
            }
            
            this.showProgress('Complete!', 100, `${selectedUsers.length} roles updated`);
            
            setTimeout(() => {
                this.hideProgress();
                this.showSuccess(`Updated ${selectedUsers.length} user roles!`);
            }, 2000);
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        this.hideProgress();
            this.showError('Failed to update roles. Please try again.');
        }
    }

    async updateUserRole(userId, newRole) {
        try {
            const { error } = await this.supabase
                .from('profiles')
                .update({ role: newRole })
                .eq('id', userId);

            if (error) throw error;
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        throw error;
        }
    }

    // Bulk Content Operations
    async executeBulkContentOperation() {
        try {
            const operation = document.getElementById('bulk-content-operation')?.value;
            const selectedContent = this.getSelectedContent();
            
            if (selectedContent.length === 0 || !operation) {
                this.showError('Please select content and an operation');
                return;
            }
            
            this.showProgress(`Executing ${operation}...`, 10, `Processing ${selectedContent.length} items`);
            
            switch (operation) {
                case 'publish':
                    await this.bulkPublishContent(selectedContent);
                    break;
                case 'unpublish':
                    await this.bulkUnpublishContent(selectedContent);
                    break;
                case 'archive':
                    await this.bulkArchiveContent(selectedContent);
                    break;
                case 'delete':
                    await this.bulkDeleteContent(selectedContent);
                    break;
            }
            
            this.showProgress('Complete!', 100, `${selectedContent.length} items processed`);
            
            setTimeout(() => {
                this.hideProgress();
                this.showSuccess(`${operation} completed for ${selectedContent.length} items!`);
            }, 2000);
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        this.hideProgress();
            this.showError('Failed to execute operation. Please try again.');
        }
    }

    async bulkPublishContent(contentIds) {
        for (let i = 0; i < contentIds.length; i++) {
            await this.updateContentStatus(contentIds[i], 'published');
            const progress = 10 + ((i + 1) / contentIds.length) * 80;
            this.showProgress('Publishing content...', progress, `${i + 1}/${contentIds.length} items published`);
        }
    }

    async bulkUnpublishContent(contentIds) {
        for (let i = 0; i < contentIds.length; i++) {
            await this.updateContentStatus(contentIds[i], 'draft');
            const progress = 10 + ((i + 1) / contentIds.length) * 80;
            this.showProgress('Unpublishing content...', progress, `${i + 1}/${contentIds.length} items unpublished`);
        }
    }

    async bulkArchiveContent(contentIds) {
        for (let i = 0; i < contentIds.length; i++) {
            await this.updateContentStatus(contentIds[i], 'archived');
            const progress = 10 + ((i + 1) / contentIds.length) * 80;
            this.showProgress('Archiving content...', progress, `${i + 1}/${contentIds.length} items archived`);
        }
    }

    async bulkDeleteContent(contentIds) {
        if (!confirm(`⚠️ WARNING: This will permanently delete ${contentIds.length} items!\n\nThis action cannot be undone.\n\nAre you sure?`)) {
            this.hideProgress();
            return;
        }
        
        for (let i = 0; i < contentIds.length; i++) {
            await this.deleteContent(contentIds[i]);
            const progress = 10 + ((i + 1) / contentIds.length) * 80;
            this.showProgress('Deleting content...', progress, `${i + 1}/${contentIds.length} items deleted`);
        }
    }

    async updateContentStatus(contentId, status) {
        try {
            const { error } = await this.supabase
                .from('graphrag_resources')
                .update({ status: status })
                .eq('id', contentId);

            if (error) throw error;
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        throw error;
        }
    }

    async deleteContent(contentId) {
        try {
            const { error } = await this.supabase
                .from('graphrag_resources')
                .delete()
                .eq('id', contentId);

            if (error) throw error;
            
        } catch (error) {
            // Log to monitoring instead of console
        if (window.posthog) {
            posthog.capture('javascript_error', {
                error: err.message,
                url: window.location.pathname
            }));
        }
        // Show user-friendly message instead of error
        throw error;
        }
    }

    // Helper methods
    handleSelectAll(checkbox) {
        const container = checkbox.closest('.checkbox-list');
        const checkboxes = container.querySelectorAll('.item-checkbox');
        
        checkboxes.forEach(cb => {
            cb.checked = checkbox.checked;
        });
    }

    handleItemSelection(checkbox) {
        if (checkbox.checked) {
            this.selectedItems.push(checkbox.value);
        } else {
            this.selectedItems = this.selectedItems.filter(id => id !== checkbox.value);
        }
    }

    getSelectedUsers() {
        return Array.from(document.querySelectorAll('.user-checkbox:checked'))
            .map(cb => cb.value);
    }

    getSelectedResources() {
        return Array.from(document.querySelectorAll('.resource-checkbox:checked'))
            .map(cb => cb.value);
    }

    getSelectedContent() {
        return Array.from(document.querySelectorAll('.content-checkbox:checked'))
            .map(cb => cb.value);
    }

    readFileAsText(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = (e) => resolve(e.target.result);
            reader.onerror = reject;
            reader.readAsText(file);
        });
    }

    parseCSV(csvContent) {
        const lines = csvContent.split('\n');
        const headers = lines[0].split(',').map(h => h.trim());
        const users = [];
        
        for (let i = 1; i < lines.length; i++) {
            if (!lines[i].trim()) continue;
            
            const values = lines[i].split(',').map(v => v.trim());
            if (values.length === headers.length) {
                const user = {};
                headers.forEach((header, index) => {
                    user[header] = values[index];
                });
                users.push(user);
            }
        }
        
        return users;
    }

    isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    showSuccess(message) {
        this.showNotification(message, 'success');
    }

    showError(message) {
        this.showNotification(message, 'error');
    }

    showNotification(message, type) {
        const notification = document.createElement('div');
        notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
            type === 'success' ? 'bg-green-500 text-white' : 'bg-red-500 text-white'
        }`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 5000);
    }
}

// Initialize bulk operations when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => new TeKeteBulkOperations());
} else {
    new TeKeteBulkOperations();
}

// Export for global access
window.TeKeteBulkOperations = TeKeteBulkOperations;
